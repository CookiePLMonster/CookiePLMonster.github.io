---
layout: post
title: "Yakuza Arcade Machines Player - Native Virtua Fighter 5: Final Showdown on PC"
excerpt: "Turning an in-Yakuza Virtua Fighter 5: Final Showdown into a native PC game using game files from Yakuza."
thumbnail: "assets/img/games/bg/vf5fs.jpg"
feature-img: "assets/img/games/bg/vf5fs.jpg"
image: "assets/img/games/bg/vf5fs.jpg"
game-series: "vf5fs"
date: 2021-06-01 21:00:00 +0200
tags: [Articles, Releases]
---

*TL;DR - if you are not interested in a rundown of how YAMP works,
scroll down to the [**Download**](#download) section for a download link.*

***

Today is a good day for the Virtua Fighter communities. SEGA has released [Virtua Fighter 5: Ultimate Showdown for PS4](https://virtuafighter5us.sega.com/),
a remastered version from the game by RGG Studio themselves, and now I am happy to unveil **Yakuza Arcade Machines Player -- a launcher
that allows you to run Virtua Fighter 5: Final Showdown, standalone and native, on PC, provided you own a Steam copy of Yakuza 6[^1]!**

[^1]: While Yakuza: Like a Dragon also has VF5FS, it's not supported by YAMP at the time of writing this post.

# Technical overview

This sounds familiar -- [wasn't this already done before]({{ site.baseurl }}{% post_url 2021-04-19-virtua-fighter-5-final-showdown-unlocker %})?
While this idea may seem similar to a previously released **VF5FS Unlocker**, it's anything but the same -- VF5FS Unlocker transforms the in-game arcades,
while YAMP allows running VF5FS outside of Yakuza, effectively making it work as a "proper" PC version of the game.
At the moment, YAMP supports only VF5FS from Yakuza 6 (despite the name hinting otherwise) and no other arcades, but support might be expanded in the future.

So, how does it work? Even though arcade games in modern Yakuza games are separate DLLs, they are very tightly coupled to their respective games,
with internal data types being used all over. Therefore, ABI isn't preserved even across patches, let alone separate games.

The way YAMP works can be split into a few parts -- to get the arcades running standalone, it has to perform proper **initialization**, **importing**,
and **patching**. That last point is technically optional, but numerous features of the original Virtua Fighter 5 have either been stubbed out
or flat out broken when "porting" the game to Yakuza arcades, so YAMP has to inject patched code to the arcade DLL to fix these issues and/or
reinstate features.

## Initialization

*Yakuza Arcade Machines Player* closely reimplements those isolated code parts of Yakuza that are required by arcade games to function.
The backbone of the entire process is encapsulated in an input structure passed to the `module_start` function in the respective DLL files:

```cpp
struct module_params_t
{
	size_t size;
	const sl_module_t* sl_module;
	const gs_module_t* gs_module;
	const ct_module_t* ct_module;
	const icri* cri_ptr;
	const char* root_path;
	module_func_t* module_main;
	vf5fs_game_config_t config;
};
```

The engine features are passed through:
* `sl_module` (**S**hared **L**ibraries?) -- miscellaneous parts of the game's engine, such as data containers, file IO interfaces, and input.
* `gs_module` (**G**raphic**S**?) -- parts related to rendering.
* `ct_module` (**C**on**T**roller?) -- its exact role is unknown, as VF5FS ignores that module.
* `cri` -- **CRI**WARE interfaces, responsible for audio and FMVs.

YAMP implements a subset of features from `sl` and `gs`, ignores `ct` and stubs `cri`, so at the moment there is no audio in the game, sorry!

`sl_module` and `gs_module` are both huge structures (8KB for `gs`, 62KB for `sl`!), but there is a trick that saved me an indeterminate amount
of time -- both these classes have instances constructed in the game DLL, and when running the games via Yakuza, they go unused:

```cpp
pxd::sl::context_t::context_t()
{
	// `pxd::sl::sm_context_instance` should've been passed as a `this` parameter, but compiler optimizations hardcoded that specific object in Yakuza 6.
	pxd::sl::sm_context_instance.tag_id = 0x6C73424C;
	pxd::sl::sm_context_instance.version = 0x40601;
	pxd::sl::sm_context_instance.size_of_struct = 61248;
	pxd::sl::sm_context_instance.export_context.size_of_struct = 0;
	pxd::sl::sm_context_instance.export_context.p_context = 0;
	pxd::sl::sm_context_instance.processor_num = 1;
	pxd::sl::sm_context_instance.main_thread_id = 0;
	pxd::sl::sm_context_instance.processor_affinity_mask = 0;
	pxd::sl::sm_context_instance.p_temp_work = 0;
	pxd::sl::sm_context_instance.temp_work_size = 0;
	pxd::sl::sm_context_instance.count_frequency = 0;

	// ...and so on...
}
```

Instead of constructing these huge structures (would also require defining them in their entirety!),
YAMP "imports" the in-DLL instance and passes it to the DLL in the aforementioned input structure.
Then, all I had to do was mirror parts of the game's post-construction `initialize` methods to "fill in the blanks" in these modules, for example:
```cpp
device_context->initialize(reinterpret_cast<sbgl::ccontext*>(context->sbgl_device.m_pD3DDeviceContext));
context->p_device_context = device_context;

constexpr unsigned int FX_MAX = 256;
constexpr unsigned int VS_MAX = 512;
constexpr unsigned int PS_MAX = 512;
constexpr unsigned int GS_MAX = 256;
constexpr unsigned int DS_MAX = 256;
constexpr unsigned int HS_MAX = 256;
constexpr unsigned int GTS_MAX = 256;
constexpr unsigned int TEX_MAX = 1024;
context->handle_tex.initialize(nullptr, TEX_MAX);
context->handle_vs.initialize(nullptr, VS_MAX);
context->handle_ps.initialize(nullptr, PS_MAX);
context->handle_gs.initialize(nullptr, GS_MAX);
context->handle_ds.initialize(nullptr, DS_MAX);
context->handle_hs.initialize(nullptr, HS_MAX);
context->handle_gts.initialize(nullptr, GTS_MAX);
context->handle_fx.initialize(nullptr, FX_MAX);

// Fill the export context
auto& export_context = context->export_context;
export_context.size_of_struct = sizeof(export_context);
export_context.sbgl_context.p_value[0] = window.GetD3D11Device();
export_context.sbgl_context.p_value[1] = static_cast<sbgl::cdevice_native*>(&context->sbgl_device);
export_context.sbgl_context.p_value[2] = &context->sbgl_device.m_swap_chain;

gs::primitive_initialize();
```

Since with YAMP there is no need to share the modules between Virtua Fighter 5 and another entity, this approach is completely valid and saves
a lot of effort. The most time consuming part of that is ensuring that the relevant class fields are properly named and reside on correct offsets,
but once found in the game, they are automatically validated:
```cpp
static_assert(offsetof(context_t, frame_counter) == 0x60);
static_assert(offsetof(context_t, p_device_context) == 0xB0);
static_assert(offsetof(context_t, sbgl_device) == 0xC0);
static_assert(offsetof(context_t, sbgl_device.m_pD3DDeviceContext) == 0x150);
```

## Importing

Naturally, most of the initialization has to be performed in a game-specific way, e.g. initializing file handles, containers, contexts.
I could reimplement those functions from scratch based on their Yakuza 6 definitions, but for the most part, there is an easier way -- the arcade DLL
contains a good part of those functions inside itself, and they are identical to the Yakuza ones as they come from the same source!

These functions are not exported from the DLL in the traditional sense, but it's never been a problem in modding 😬
All the functions are easily callable from function pointers, especially since it's a 64-bit codebase (a single calling convention!)
and it seems like Link Time Code Generation was not used (no custom calling conventions!):

```cpp
Import(sl::sm_context, ImportSymbol::SL_CONTEXT_INSTANCE);
Import(gs::sm_context, ImportSymbol::GS_CONTEXT_INSTANCE);
Import(sl::file_create_internal, ImportSymbol::SL_FILE_CREATE);
Import(sl::file_open_internal, ImportSymbol::SL_FILE_OPEN);
Import(sl::file_read, ImportSymbol::SL_FILE_READ);
Import(sl::file_close, ImportSymbol::SL_FILE_CLOSE);
Import(sl::handle_create_internal, ImportSymbol::SL_HANDLE_CREATE);
Import(sl::file_handle_destroy, ImportSymbol::SL_FILE_HANDLE_DESTROY);
Import(sl::archive_lock_wlock, ImportSymbol::ARCHIVE_LOCK_WLOCK);
Import(sl::archive_lock_wunlock, ImportSymbol::ARCHIVE_LOCK_WUNLOCK);
Import(cgs_device_context::reset_state_all_internal, ImportSymbol::DEVICE_CONTEXT_RESET_STATE_ALL);
Import(gs::vb_create, ImportSymbol::VB_CREATE);
Import(gs::ib_create, ImportSymbol::IB_CREATE);
Import(shift_next_mode, ImportSymbol::SHIFT_NEXT_MODE);
Import(shift_next_mode_sub, ImportSymbol::SHIFT_NEXT_MODE_SUB);
```

Initially, all the functions were referenced by hardcoded addresses, but after [the latest Yakuza 6 patch](https://store.steampowered.com/news/app/1388590/view/3081002794567807678)
they all changed, so I modified them to use pattern matching instead, much like in SilentPatches:
```cpp
Imports symbols{
	// Functions/globals
	{ S::SL_CONTEXT_INSTANCE, immediate(get_module_pattern(dll, "48 89 5C 24 ? 48 8D 3D", 5 + 3)) },
	{ S::GS_CONTEXT_INSTANCE, immediate(get_module_pattern(dll, "48 8D 2D ? ? ? ? 48 89 68 08", 3)) },
	{ S::GS_CONTEXT_PTR, immediate(get_module_pattern(dll, "48 8B 05 ? ? ? ? 8B F1 BA", 3)) },
	{ S::D3DDEVICE, immediate(get_module_pattern(dll, "48 89 05 ? ? ? ? 48 8B 41 28", 3)) },
	{ S::SL_FILE_CREATE, get_module_pattern(dll, "48 8B 05 ? ? ? ? 48 8B F9", -0x13) },
	{ S::SL_FILE_OPEN, get_module_pattern(dll, "48 8B 05 ? ? ? ? 48 8B D9 45 33 F6", -0x12) },
	{ S::SL_FILE_READ, get_module_pattern(dll, "4C 8B 0D ? ? ? ? 8B C1", -0x6) },
	{ S::SL_FILE_CLOSE, immediate(get_module_pattern(dll, "E8 ? ? ? ? 48 C7 44 3B ? ? ? ? ?", 1)) },
	{ S::SL_HANDLE_CREATE, get_module_pattern(dll, "48 8B 3D ? ? ? ? 48 8B F1 45 33 FF", -0x18) },
	// ...and so on...
```

Once the functions are imported, they can be freely used as if they were a part of the YAMP executable itself:
```cpp
csl_archive* csl_archive::create_instance(sl::handle_t handle)
{
	sl::archive_lock_wlock(sl::sm_context->sync_archive_condvar);
	csl_archive* archive = sl::handle_instance<csl_archive>(handle, 6);
	if (archive != nullptr)
	{
		archive->add_ref();
	}
	sl::archive_lock_wunlock(sl::sm_context->sync_archive_condvar);
	return archive;
}
```

This approach has also one more benefit that will only become clear later -- importing these functions instead of reimplementing them
by hand means I don't need to worry about any implementation differences between Yakuza 6 and other games! This will save me some time in the future.

## Patching

As mentioned before, things have been cut and/or broken from the Yakuza 6 version of Virtua Fighter 5 Final Showdown. I even outlined a few such issues in the VF5FS Unlocker release post:
> * Saving doesn’t work
> * To start the game, coins must be inserted twice (Y/Triangle on the gamepad)
> * English texts are cut off, as this build of VF5FS seems to be a Japanese SKU with English texts
> * Pause menu is tricky to access and resuming the game does not unfreeze gameplay

As I wanted YAMP to deliver the best experience possible, I had to resort to patching up the game DLL at runtime, once again not unlike SilentPatches do:
```cpp
// Fix pause countdown not counting down
// In Y6 this code uses frame time, in YLAD it just uses count-- - a possible failed attempt at making the code support high framerates?
{
	void* get_frame_speed_stub = hop->Jump(&get_frame_speed_pause_stub);
	for (const auto& [key, addr] : symbols.GetSymbolRange(ImportSymbol::TASK_PAUSE_CTRL_COUNTDOWN_PATCH))
	{
		Memory::InjectHook(addr, get_frame_speed_stub);
	}
}
```

As a result, I was able to correct most shortcomings from my previous release, VF5FS Unlocker. Those are:
* Saving has been restored.
* When in Console mode, the game goes to the main menu after the intro splash.
* "Press START button" has been restored.
* Cross/Circle can now be swapped in the menu navigation.
* The pause softlock has been fixed.
* In-game button mappings are usable again.

Of course, not all such issues are fixed yet, for example, texts still don't have proper line breaks. The foundations are there, however,
so adding more patches in the future should be easy.

# Download

Yakuza Arcade Machines Player is shipped as a single executable file to be dropped in your Yakuza 6 directory.
For a feature list and a to-do list, check the mod's downloads page.

<div style="overflow:auto;padding:10px">
<div style="width:50%;float:left;"><img src="{% link assets/img/posts/yamp/YAMP_GUGrgBQqJg.jpg %}"></div>
<div style="width:50%;float:right;"><img src="{% link assets/img/posts/yamp/YAMP_Vq9hoxdKCi.jpg %}"></div>
<div style="width:50%;float:left;"><img src="{% link assets/img/posts/yamp/YAMP_dftKEuMb56.jpg %}"></div>
<div style="width:50%;float:right;"><img src="{% link assets/img/posts/yamp/YAMP_ml0nXhWrBF.jpg %}"></div>
</div>

<a href="{% link _games/vf5fs.md %}#yamp" class="button" role="button" target="_blank">{{ site.theme_settings.download_icon }} Download Yakuza Arcade Machines Player</a> \\
After downloading, all you need to do is to extract the archive to your Yakuza 6 directory (or the `vf5fs` subdirectory), and that's it!
The in-game configuration menu is accessed by pressing `F1`.
Not sure how to proceed? Check the [Setup Instructions]({% link pages/setup-instructions.md %}).
**YAMP only works with the Steam version of Yakuza 6! It hasn't been tested with the Gamepass version, but it is unlikely to work with it.**

## Known issues and shortcomings

* Audio is not implemented.
* No online features are implemented and are unlikely to be implemented for a long time.
* Only Yakuza 6 is supported so far, Yakuza: Like a Dragon is planned to be added later.
* Just like when playing through in-game arcades, the game renders at fixed 720p and stretches to fullscreen. Proper high resolution rendering support may be added later.
* Offline Versus cannot be played with a keyboard and a gamepad. For now, two gamepads are required.
* Keyboard bindings are hardcoded for now. Please refer to `F1` -> `Controls` for a list of controls.


# Disclaimer

**Yakuza Arcade Machines Player does not redistribute ANY copyrighted files.**
**You must own an original Steam copy of Yakuza 6: The Song of Life to play games via YAMP.**
**Pirated game copies WILL NOT receive any support.**

All rights to Virtua Fighter 5: Final Showdown belong to SEGA.

***

For those interested,
the full source code of Yakuza Arcade Machine Player has been published on GitHub, so it can be freely used as a point of reference: \\
<a href="https://github.com/CookiePLMonster/YAMP" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
