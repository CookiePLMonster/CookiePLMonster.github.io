---
layout: post
title: "How a 20 year old bug in GTA San Andreas surfaced in Windows 11 24H2"
date: 2025-04-23 15:30:00 +0200
excerpt: After over two decades, players are now forbidden from flying a seaplane, all thanks to undefined code behavior.
game-series: "gta-sa"
image: "assets/img/posts/sa-win11-24h2-bug/gta_sa_Bg0aamH1rZ.jpg"
thumbnail: "assets/img/posts/sa-win11-24h2-bug/gta_sa_Bg0aamH1rZ.jpg"
feature-img: "assets/img/posts/sa-win11-24h2-bug/gta_sa_Bg0aamH1rZ.jpg"
twitter: {card: "summary_large_image"}
tags: [Articles]
---

* TOC
{:toc}

# Introduction

On the [SilentPatch GitHub issue tracker](https://github.com/CookiePLMonster/SilentPatch/issues/172){:target="_blank"},
I received a rather specific bug report:

> ### Skimmer airplane doesn't exist in Windows 11 24H2
> {:.no_toc .no_anchor}
>
> When I upgraded my windows to version 24H2, the Skimmer plane disappear completely from the game.
> It can't be spawn using trainer nor it can't be found anywhere on it's normal spawn points.
> I'm using both my modded copy (which is before the update, is completely fine) and vanilla copy with only silentpatch
> (I tried the 2018, 2020 and the most recent version of silentpatch) and the plane still won't exist.

If this was the first time I had heard about it, I'd likely consider it dubious and suspect there are more things at play,
and it's not specifically Windows 11 24H2. However, on GTAForums, I've been receiving comments about this exact issue since November last year.
Some of them said SilentPatch causes this issue, others however stated the same happens on a completely unmodded game:

> Apparently the skimmer cant spawn when playing on Windows 11 24h2 update, hope this bug gets fixed.
>
> EDIT: So I think I confirmed it, I set up a VM with Windows 11 23h2 and the damn plane spawns fine,
> and updating that same VM to 24h2 breaks the skimmer, why would a small feature update in 2024 break a random plane in a 2005 game is anyone's guess.

> After the latest Silent patch update there is no Skimmer in the game and when I try to spawn it with RZL-Trainer or Cheat Menu by Grinch,
> the game freezes and I have to close it via Task Manager.

> [...] I was forced to update to 24H2, and now after the update, I have the same problem with the Skimmer in GTA SA as others.
> This means that mods or anything else are not causing the issue, the problem appeared after the latest Windows update.

***

My home PC is still on Windows 10 22H2, while my work machine is on Windows 11 23H2, and, to no surprise, neither machine reproduced the issue -- Skimmer spawned
on the water just fine, creating one via script and putting CJ in a driver's seat worked too.

That said, I also asked a few people who upgraded to 24H2 to test this on their machines and they **all** hit this bug. Attempts to debug "remotely"
by giving instructions over the chat didn't go anywhere, so I set up a 24H2 virtual machine on my own. I copied the game over to the machine, set it up for remote
debugging from the host OS, headed to the usual place the Skimmer spawns, and sure enough, it wasn't there. All other planes and boats still spawned fine,
only this one vehicle did not:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/screens/gta_sa_SqUlKDKCRs.jpg" thumbnail="auto" caption="Skimmer is gone." %}
{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/screens/gta_sa_qnldPBAKRl.jpg" thumbnail="auto" caption="Other planes are still here, though." %}
</figure>

I then used the script to spawn a Skimmer and put CJ inside it, just to be launched
`1.0287648030984853e+0031` = **10.3 nonillion meters**, or **10.3 octillion kilometers**, or **1.087 quadrillion light-years** up in the sky 😆

{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/screens/gta_sa_5KOLUPPHLe.jpg" thumbnail="auto"
            caption="Scientists claim to have discovered a 'new color' no one has seen before." %}

With SilentPatch installed, the game freezes shortly after launching the player up, as the game code gets stuck in a loop.
Without SilentPatch, the game doesn't freeze, but instead, it succumbs to a famous "burn-in effect" known to occur when the camera gets launched into infinity or close to it.
Funny enough, you can still kind of make out the shape of the plane even though the animations give up completely to the inaccuracies of the floating point values:

<figure class="media-container small">
{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/screens/gta_sa_GXULFRni6Y.jpg" thumbnail="auto" %}
{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/screens/gta_sa_qQUqnmyhV6.jpg" thumbnail="auto" %}
</figure>

# Investigating the bug

## What is broken?

But, enough messing around; now I knew it was a real bug and I needed to figure out the root cause. At this point it wasn't possible to say
whether the game was at fault, or if I was really dealing with an API bug introduced in 24H2, as looking at how many games have issues with this OS version,
it could go either way.

I didn't have much to go with, but the fact the game froze with SilentPatch installed provided me with a good starting point. Upon entering the seaplane,
the game froze in a very small loop in `CPlane::PreRender`, attempting to normalize the rotor blade angle to the 0-360 degree range:

```cpp
this->m_fBladeAngle = CTimer::ms_fTimeStep * this->m_fBladeSpeed + this->m_fBladeAngle;
while (v12 > 6.2831855)
{
  this->m_fBladeAngle = this->m_fBladeAngle - 6.2831855;
}
```

In the debugged session, `this->m_fBladeSpeed` was `3.73340132e+29`. This value is obviously enormous, big enough to make decrementing the value by `6.2831855`
entirely ineffective due to the difference in floating point exponents of these two values.[^fp-explanation] But why is the blade speed so ridiculously high?
The blade speed is derived from the following formula:
```cpp
this->m_fBladeSpeed = (v34 - this->m_fBladeSpeed) * CTimer::ms_fTimeStep / 100.0 + this->m_fBladeSpeed;
```

[^fp-explanation]: In other words, due to the way floating point values are represented,
    subtracting a small floating point value from a huge floating point value might not change the result at all.

where `v34` is **proportional to the plane's altitude**. This matches the initial findings -- as mentioned earlier, the "burn-in effect" traditionally happens
when the camera is very far away from the map center, or at a great height.

What caused the plane to shoot so high up? There are two possibilities:
1. The plane spawns high up in the sky already.
2. The plane spawns at ground level and then shoots up in the next frame.

As for this test, I was spawning the Skimmer myself with a test script, so I could start from the function used in the game's SCM (script) interpreter,
named `CCarCtrl::CreateCarForScript`. This function spawns a vehicle with a specified ID at the provided coordinates, and those come from my test script,
so I know they are correct. However, this function transforms the supplied Z coordinate slightly:

```cpp
if (posZ <= 100.0)
{
  posZ = CWorld::FindGroundZForCoord(posX, posY);
}
posZ += newVehicle->GetDistanceFromCentreOfMassToBaseOfModel();
```

`CEntity::GetDistanceFromCentreOfMassToBaseOfModel` contains multiple code paths, but the one used in this case simply gets the negated maximum Z value
of the model's bounding box:
```cpp
return -CModelInfo::ms_modelInfoPtrs[this->m_wModelIndex]->pColModel->bbox.sup.z;
```

At this point, I expected this value to be incorrect, so I peeked into Skimmer's bounding box values just to find out that the maximum Z value is indeed corrupted:

```
- *(RwBBox**)0x00B2AC48	RwBBox *
  - sup	RwV3d
      x	-5.39924574	float
      y	-6.77431822	float
      z	-4.30747210e+33	float
  - inf	RwV3d
      x	5.42313004	float
      y	4.02343750	float
      z	1.87021971	float
```

If all the components of the bounding box were corrupted, I would have suspected some memory corruption, like another code writing past boundaries and overwriting
these values, but it's specifically `sup.z` that is corrupted that is neither the first nor the last field in the bounding box. Once again, two possibilities came to my mind:
1. The collision file is read incorrectly and some fields remain uninitialized, or read unrelated data instead of the bounding box? Highly unlikely, but not impossible given that
  this issue could potentially have been an OS bug.
2. The bounding box is read correctly, but then it's updated with an outrageously incorrect value.

A data breakpoint set up at `pColModel` reveals that at the time of the initial setup, the bounding box is correct, and the value of the Z coordinate is completely reasonable:
```
- *(RwBBox**)0x00B2AC48	RwBBox *
  - sup	RwV3d
    x	-5.39924574	float
    y	-6.77431822	float
    z	-2.21952772	float
  - inf	RwV3d
    x	5.42313004	float
    y	4.02343750	float
    z	1.87021971	float
```

Turns out, the first time a vehicle with a specific model is spawned, the game sets up the suspension in a function `SetupSuspensionLines`, and updates the Z coordinate
of the bounding box to reflect the car's natural suspension height:
```cpp
if (pSuspensionLines[0].p1.z < colModel->bbox.sup.z)
{
  colModel->bbox.sup.z = pSuspensionLines[0].p1.z;
}
```

This is where things went wrong first. The suspension lines are computed using a combination of values from `handling.cfg` and the wheel scale parameter
coming from `vehicles.ide`:
```cpp
for (int i = 0; i < 4; i++)
{
  CVector posn;
  modelInfo->GetWheelPosn(i, posn);

  posn.z += pHandling->fSuspensionUpperLimit;
  colModel->lines[i].p0 = posn;

  float wheelScale = i != 0 && i != 2 ? modelInfo->m_frontWheelScale : modelInfo->m_rearWheelScale;

  posn.z += pHandling->fSuspensionLowerLimit - pHandling->fSuspensionUpperLimit;
  posn.z -= wheelScale / 2.0;
  colModel->lines[i].p1 = posn;
}
```

Since I knew `colModel->lines[0].p1` is corrupted, this meant either `pHandling->fSuspensionLowerLimit`, `pHandling->fSuspensionUpperLimit`, or `wheelScale` were bogus.
Skimmer's `handling.cfg` values didn't seem any different to any other plane in the game, but then I spotted something interesting in `vehicles.ide`. Skimmer's line looks like this:
```
460, 	skimmer,	skimmer, 	plane,		SEAPLANE,	SKIMMER,	null,	ignore,		5,	0,	0
```
{:.pre-wrap}

Compare this line to any other plane in the game, in this example Rustler:
```
476, 	rustler, 	rustler, 	plane, 		RUSTLER, 	RUSTLER,	rustler, ignore,		10,	0,	0,		-1, 0.6, 0.3,		-1
```
{:.pre-wrap}

The line is shorter and it's missing the last four parameters, moreover, **two of the missing parameters are the front and rear wheel scale!**
This is normal for boats, but Skimmer is **the only** plane to omit these parameters.

Does re-adding those parameters fix the seaplane? Unsurprisingly, it does!

{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/screens/gta_sa_3hbE1KfRUe.jpg" thumbnail="auto" %}

## But why and how?

I have a likely explanation for why Rockstar made this specific mistake in the data to begin with -- in Vice City, Skimmer was defined as a **boat**,
and therefore did not have those values defined by design!
When in San Andreas they changed Skimmer's vehicle type to a **plane**, someone forgot to add those now-required extra parameters.
Since this game seldom verifies the completeness of its data, this mistake simply slipped under the radar.

Problem solved? Not quite yet, as for SilentPatch, I need to fix it from the code. A peek into the pseudocode of `CFileLoader::LoadVehicleObject`
reveals the true nature of this bug: the game assumes all parameters are always present in the definition line and it doesn't default any but two parameters,
nor it checks the return value of `sscanf`, and so in the case of all boats and Skimmer, those parameters remained uninitialized:
```cpp
void CFileLoader::LoadVehicleObject(const char* line)
{
  int objID = -1;
  char modelName[24];
  char texName[24];
  char type[8];
  char handlingID[16];
  char gameName[32];
  char anims[16];
  char vehClass[16];
  int frq;
  int flags;
  int comprules;
  int wheelModelID; // Uninitialized!
  float frontWheelScale, rearWheelScale; // Uninitialized!
  int wheelUpgradeClass = -1; // Funny enough, this one IS initialized

  int TxdSlot = CTxdStore::FindTxdSlot("vehicle");
  if (TxdSlot == -1)
  {
    TxdSlot = CTxdStore::AddTxdSlot("vehicle");
  }
  sscanf(line, "%d %s %s %s %s %s %s %s %d %d %x %d %f %f %d", &objID, modelName, texName, type, handlingID,
        gameName, anims, vehClass, &frq, &flags, &comprules, &wheelModelID, &frontWheelScale, &rearWheelScale,
        &wheelUpgradeClass);

  // More processing here...
}
```

Given the symptoms, those uninitialized values must have evaluated to small, valid floating point values all the way until now,
whereas with Windows 11 24H2 they got out of hand and tripped the bounding box calculations.

In SilentPatch, the fix is easy -- I wrap this call to `sscanf` and provide reasonable defaults for the final four parameters:
```cpp
static int (*orgSscanf)(const char* s, const char* format, ...);
static int sscanf_Defaults(const char* s, const char* format, int* objID, char* modelName, char* texName, char* type,
      char* handlingID, char* gameName, char* anims, char* vehClass, int* frequency, int* flags, int* comprules,
      int* wheelModelID, float* frontWheelSize, float* rearWheelSize, int* wheelUpgradeClass)
{
  *wheelModelID = -1;
  // Why 0.7 and not 1.0, I'll explain later
  *frontWheelSize = 0.7;
  *rearWheelSize = 0.7;
  *wheelUpgradeClass = -1;

  return orgSscanf(s, format, objID, modelName, texName, type, handlingID, gameName, anims, vehClass,
                  frequency, flags, comprules, wheelModelID, frontWheelSize, rearWheelSize, wheelUpgradeClass);
}
```

[Fixed!](https://github.com/CookiePLMonster/SilentPatch/commit/881aded7237067202025934796cc2313104cba8c){:target="_blank"}
Another compatibility win for the patch.

***

If this was a regular bug, I would've ended the post right here. However, in the case of this rabbit hole, the discovery of this fix only
raised more questions -- why did this break only now? What made the game work fine despite of this issue for over twenty years,
before a new update to Windows 11 suddenly challenged this status quo?

**Finally, is this somehow caused by a problem in Windows 11 24H2, or is this just an unfortunate coincidence, stars aligning just right?**

# Here be dragons -- the true root cause

## Diving deeper

At this point, the working theory was that the uninitialized local variables in `CFileLoader::LoadVehicleObject`
happened to have reasonable values until _something_ changed in Windows 11 24H2, and those values became "unreasonable".
What I knew could **not** be the cause was the CRT (and thus, the `sscanf` call) -- San Andreas uses a statically compiled CRT,
and therefore any OS-level hotfixes wouldn't apply to it.
However, considering the plethora of security enhancements in Windows 11, I couldn't rule out that one of those enhancements,
for example, **Kernel-mode Hardware-enforced Stack Protection**, ends up scrambling the stack in a way the game's bugged function doesn't like.

I set up an experiment where I broke into a debugger before a `sscanf` call when parsing Skimmer's line (vehicle ID 460) specifically,
and the observed variable values supported that claim. On my Windows 10 machine, they happened to be both `0.7`:
```
frontWheelSize  0x01779f14 {0.699999988}
rearWheelSize   0x01779f10 {0.699999988}
```
while on the Win11 24H2 VM, they are huge, similar in order of magnitude to the wrong values observed in the bounding box earlier.
The stack pointer has also shifted by 4 bytes for some reason, but that is unlikely to be related -- and it's likely caused by some changes
to the thread startup boilerplate inside `kernel32.dll`:
```
frontWheelSize  0x01779f18 {7.84421263e+33}
rearWheelSize   0x01779f14 {4.54809690e-38}
```

This got me curious - `0.7` is a bit "too good" of a value to be a result of interpreting random garbage from the stack as a floating point;
what's more likely is that it's an actual floating point value that was sitting on the stack in exactly the right spot.
I then inspected `vehicles.ide` for TopFun -- the vehicle defined directly before Skimmer. Sure enough, its wheel scale is `0.7`!
```
459,	topfun,		topfun,		car,		TOPFUN,		TOPFUN,		van,	ignore,		1,	0,	0,		-1, 0.7, 0.7,		-1
```
{:.pre-wrap}

`vehicles.ide` is parsed in order, in a function working similarly to this (pseudocode):
```cpp
void CFileLoader::LoadObjectTypes(const char* filename)
{
  // Open the file...

  while ((line = fgets(file)) != NULL)
  {
    // Parse the section indicators...
    switch (section)
    {
      // Different sections...
    case SECTION_CARS:
      LoadVehicleObject(line);
      break;
    }
  }
}
```

Seems like the code somehow persisted the stale wheel scale values, so Skimmer ends up getting the same wheel scales as Topfun.
I set up another experiment to verify this claim:
1. Set up a breakpoint before `sscanf` again, but this time before Topfun's line (vehicle ID 459) gets parsed.
2. Set up write breakpoints on `frontWheelScale` and `rearWheelScale`.
3. Resume execution until the game gets to parsing the next vehicle definition.

Windows 10 verified my claim -- **nothing wrote to these two stack values between the calls to `CFileLoader::LoadVehicleObject`,
so the function's effective behavior was to preserve (albeit, unintentionally) the wheel scale values between the consecutive calls!**

Repeating the same exercise on Windows 11 24H2 triggered the write breakpoint! However, it wasn't anywhere close to any security feature:
the stack values were overwritten by... `LeaveCriticalSection` inside `fgets`:
```
>	ntdll.dll!_RtlpAbFindLockEntry@4()	Unknown
 	ntdll.dll!_RtlAbPostRelease@8()	Unknown
 	ntdll.dll!_RtlLeaveCriticalSection@4()	Unknown
 	gta_sa.exe!fgets()	Unknown
```
{:.pre-wrap}

Seems like a change in Windows 11 24H2 modified the way [Critical Section Objects](https://learn.microsoft.com/en-us/windows/win32/sync/critical-section-objects){:target="_blank"}
work internally, and the new code unlocking the critical section uses more stack space than the old one.
I ran one more experiment, comparing the changes to the stack space that happened after `sscanf` inside `LoadVehicleObject`, until the next invocation of this function.
Changed values are highlighted in red:

<figure class="media-container">
{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/stack-win10.jpg"
      caption="On Windows 10, the stack values didn't change much between the calls.
        In fact, you can spot the two values of `0x3F449BA6` = `0.768` (highlighted on the screenshot).
        They correspond to Landstalker's wheel scales." %}
{% include figures/image.html link="/assets/img/posts/sa-win11-24h2-bug/stack-win11.jpg"
      caption="On Windows 11 24H2, more stack space was modified by a new implementation of Critical Sections.
                The wheel scales are nowhere to be found, as they were overwritten!" %}
</figure>

This is the exact proof I needed -- notice that in the Windows 10 run, some of the local variables are even still visible to the human eye (like the `normal` vehicle class),
while in Windows 11, they are completely gone. It's also worth pointing out that even in Windows 10, **the very next local variable** after the wheel scales has been overwritten
by `LeaveCriticalSection`, which means the game was **4 bytes away** from hitting this exact bug years earlier! The luck at display here is insane.

## Whose Stack Is It Anyway?

To illustrate why the game got away with this bug for so long, I need to show how the stack changes across calls.
Let's say the stack looks like this after the call to `LoadVehicleObject`. **Emphasis** on the local variables we're interested in:

<table>
  <tbody>
    <tr>
      <td markdown="span">return address from `LoadObjectTypes`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:5em">local variables of `LoadObjectTypes`...</td>
    </tr>
    <tr>
      <td markdown="span">return address from `LoadVehicleObject`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:8em">local variables of `LoadVehicleObject`...</td>
    </tr>
    <tr>
      <td markdown="span">**frontWheelScale**</td>
    </tr>
    <tr>
      <td markdown="span">**rearWheelScale**</td>
    </tr>
    <tr>
      <td markdown="span">more local variables...</td>
    </tr>
  </tbody>
</table>

The call to `fgets`, and consequently `LeaveCriticalSection`, that follows the call to `LoadVehicleObject`, reuses the stack space previously occupied by that function,
as the lifetime of the function stack is limited to the duration of the function itself and once the function is done, this space is up for grabs again.
On Windows 10, the stack looked like this once `fgets` and `LeaveCriticalSection` returned:

<table>
  <tbody>
    <tr>
      <td markdown="span">return address from `LoadObjectTypes`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:5em">local variables of `LoadObjectTypes`...</td>
    </tr>
    <tr>
      <td markdown="span">return address from `fgets`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:4em; box-shadow: inset 10px 0 DarkOrange">local variables of `fgets`...</td>
    </tr>
    <tr>
      <td markdown="span" style="box-shadow: inset 10px 0 DarkOrange">return address from `LeaveCriticalSection`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:3em; box-shadow: inset 10px 0 DarkOrange">local variables of `LeaveCriticalSection`...</td>
    </tr>
    <tr>
      <td markdown="span">**frontWheelScale**</td>
    </tr>
    <tr>
      <td markdown="span">**rearWheelScale**</td>
    </tr>
    <tr>
      <td markdown="span">more local variables...</td>
    </tr>
  </tbody>
</table>

<span style="color: DarkOrange">Highlighted parts</span> overwrite what used to be the stack space of `LoadVehicleObject`,
but notice how it doesn't reach the area of the stack where the wheel scales resided.
In Windows 11 24H2, `LeaveCriticalSection` uses more stack space, so the stack space instead looks more like this:

<table>
  <tbody>
    <tr>
      <td markdown="span">return address from `LoadObjectTypes`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:5em">local variables of `LoadObjectTypes`...</td>
    </tr>
    <tr>
      <td markdown="span">return address from `fgets`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:4em; box-shadow: inset 10px 0 DarkOrange">local variables of `fgets`...</td>
    </tr>
    <tr>
      <td markdown="span" style="box-shadow: inset 10px 0 DarkOrange">return address from `LeaveCriticalSection`</td>
    </tr>
    <tr>
      <td markdown="span" style="height:3em; box-shadow: inset 10px 0 DarkOrange">local variables of `LeaveCriticalSection`...</td>
    </tr>
    <tr>
      <td markdown="span" style="box-shadow: inset 10px 0 Crimson">**frontWheelScale is overwritten!**</td>
    </tr>
    <tr>
      <td markdown="span" style="box-shadow: inset 10px 0 Crimson">**rearWheelScale is overwritten!**</td>
    </tr>
    <tr>
      <td markdown="span">more local variables...</td>
    </tr>
  </tbody>
</table>

Parts of the stack <span style="color: Crimson">highlighted in red</span> are now also scrambled
when in the past they were left intact; those parts include the wheel scales read by the previous call to `LoadVehicleObject`!
This in turn exposes the bug caused by those variables being uninitialized, and since `sscanf` can't read those values from Skimmer's `vehicles.ide` definition,
they are kept as-is in garbage form, and propagate further to the vehicle's data.

## What are the odds this only broke now? Darn Windows 11!

I want to make it clear: **all these findings prove that the bug is NOT an issue with Windows 11 24H2,
as things like the way the stack is used by internal WinAPI functions are not contractual and they may change at any time, with no prior notice**.
The real issue here is the game relying on undefined behavior (uninitialized local variables), and to be honest,
I'm shocked that the game didn't hit this bug on so many OS versions, although as I pointed out earlier, it was extremely close.
San Andreas still supported Windows 98, which means it got away with this bug in **at least** a dozen different Windows versions **and** many more releases of Wine!

...or, did it? I found it hard to believe that the game would never hit this issue on any of the many, many platforms it released on,
so I looked into the binary files of some other releases. While this bug was **not** fixed in the official 1.01 PC patch, it **was** fixed in the original Xbox release,
where a "reasonable default" of `1.0` was added to the code, much like in my fix. This fix was then "inherited" by many future versions of San Andreas, including:
* Steam 3.0, newsteam, and RGL, as they were all based on the Xbox branch of the code.
* Any releases from War Drum Studios, including Android, X360, and PS3.
* The Definitive Edition.

However, unlike Rockstar, I decided to use the wheel scale of `0.7` instead of `1.0` as a default, for multiple reasons:
1. This is the effective wheel scale Skimmer had on PC (and possibly PS2) until now since that's the wheel scale of Topfun.
2. Two other non-boat vehicles that float on water, Sea Sparrow and Vortex, both have a wheel scale of `0.7`.
3. Many cars in the game have a wheel scale of `0.7`.

# I want this fixed in my game!

The code fix will be included in [the next SilentPatch hotfix](https://github.com/CookiePLMonster/SilentPatch/milestone/3){:target="_blank"},
but for now, you may easily fix it yourself by editing `vehicles.ide`:
1. In your San Andreas directory, open `data\vehicles.ide` with Notepad.
2. Scroll down to Skimmer's line beginning with `460, 	skimmer`.
3. Replace the original line with:
   ```
   460, 	skimmer,	skimmer, 	plane,		SEAPLANE,	SKIMMER,	null,	ignore,		5,	0,	0,		-1, 0.7, 0.7,		-1
   ```
   {:.pre-wrap}
4. Save the file.

# Final word

This was the most interesting bug I've encountered for a while. I initially had a hard time believing that a bug like this would directly tie to a specific OS release,
but I was proven completely wrong. At the end of the day, it was a simple bug in San Andreas and this function should have never worked right,
and yet, at least on PC it hid itself for two decades.

This is an interesting lesson in compatibility: even changes to the stack layout of the internal implementations can have compatibility implications if an application
is bugged and unintentionally relies on a specific behavior. This is also not the first time I encountered issues like this: regular visitors might remember
[Bully: Scholarship Edition]({%link _games/bully.md %}) which famously broke on Windows 10, for very similar reasons. Just like in this case,
Bully should have never worked properly to begin with, but instead, it got away with making incorrect assumptions for years, before changes in Windows 10 finally
made it run out of luck.

Yet again, we are reminded to:
* **Validate your input data** -- San Andreas was notoriously bad at this, and ultimately this was the main reason why an incomplete config line remained unnoticed.
* **Not ignore the compilation warnings** -- this code most likely threw a warning in the original code that was either ignored or disabled!

In the end, the GTA players are lucky: in many other games, issues like this would've remained unfixed and they'd become a folk legend.
Thankfully, GTAs are moddable and well understood, so we can act upon problems like this and ensure the game stays functional for many more years to come.

***
