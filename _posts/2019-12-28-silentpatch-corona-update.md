---
layout: post
title: "New SilentPatch release -- \"The Corona Update\""
feature-img: "assets/img/silentpatch_banner.png"
thumbnail: "assets/img/posts/corona-update/coronaupdate_bg.png"
image: "assets/img/posts/corona-update/coronaupdate_bg.png"
excerpt: "Numerous nice fixes right for the 6th anniversary 🎂"
game-series: "gta-sa"
date: 2019-12-28 18:05:00 +0100
twitter: {card: "summary_large_image"}
tags: [Releases]
juxtapose: true
---

🎂 Happy Birthday SilentPatch! On December 29th 2013, the very first SilentPatch builds were released! 🎂

For this occasion, new builds have been released for GTA III, Vice City and San Andreas!
For the first time the releases have received a name! Due to the amount of fixes related to coronas and lights,
this release has been dubbed **"The Corona Update"**:

{% include screenshot.html thumbnail="/assets/img/posts/corona-update/coronaupdate_bg.png" style="natural"
        caption="Note from Silent, updating this page in 2023: I am aware how badly this name aged." %}

Also for the first time, I am experimenting with a new way of presenting changes introduced in these builds, so bear with me.

Coronas
=======

* An interesting PS2 vs PC difference
[has been identified on GTAForums recently](https://gtaforums.com/topic/669045-silentpatch/?do=findComment&comment=1070991808).
GTA III, Vice City and San Andreas on PS2 rotate light coronas as camera gets closer for them for a nice, subtle effect.
For what I theoretize to have been a mistake in deleting wrong code, this feature was broken in San Andreas on PC --but not anymore!
Starting with Build 32, this has been fixed.
{% include video.html link="https://streamable.com/s/lhe9m/pyrzkq" %}

* For the longest time "shadows under pickups" have been fixed and showing up correctly in PC versions of GTA III and GTA Vice City.
However, turns out San Andreas needed this fix to correctly light up the ground under fires! With this fixed,
fires should have visual parity with a PS2 version.
{% include screenshot.html link="https://i.imgur.com/UZgtS22.png" thumbnail="https://i.imgur.com/UZgtS22h.png" %}

* Moon phases have been fixed in San Andreas for a while. However, that fix would not play nice with a widescreen fix,
causing moon to appear stretched. This has now been fixed.
{% include screenshot.html link="https://i.imgur.com/2TV3MK4.png" thumbnail="https://i.imgur.com/2TV3MK4h.png" %}

* Highlight of this release (pun intended) -- sirens of emergency vehicles received correct placements, so they now actually match models!
In GTA III and Vice City, most sirens had misplaced coronas -- with this update, they have all been fixed. \\
  \\
  Affected vehicles:
  - Fire Truck (GTA III & Vice City)
  - Ambulance (GTA III & Vice City)
  - Police (Vice City only)
  - Enforcer (GTA III & Vice City)
  - Taxi (GTA III & Vice City)
  - FBI Rancher (Vice City only)
  - FBI Washington (Vice City only) -- siren has been **added**, as it was completely absent before
  - Vice Cheetah (Vice City only)
  - Police Chopper (GTA III & Vice City) -- search light has been misplaced in both games, red tail light was misplaced only in Vice City

  <div class="media-container small">
  {% include juxtapose.html left="/assets/img/posts/corona-update/iii-firetruck-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/iii-firetruck-after.jpg" right-label="After" %}
  {% include juxtapose.html left="/assets/img/posts/corona-update/iii-taxi-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/iii-taxi-after.jpg" right-label="After" %}
  {% include juxtapose.html left="/assets/img/posts/corona-update/iii-ambulan-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/iii-ambulan-after.jpg" right-label="After" %}
  {% include juxtapose.html left="/assets/img/posts/corona-update/iii-enforcer-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/iii-enforcer-after.jpg" right-label="After" %}
  {% include juxtapose.html left="/assets/img/posts/corona-update/vc-police-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/vc-police-after.jpg" right-label="After" %}
  {% include juxtapose.html left="/assets/img/posts/corona-update/vc-rancher-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/vc-rancher-after.jpg" right-label="After" %}
  {% include juxtapose.html left="/assets/img/posts/corona-update/vc-washington-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/vc-washington-after.jpg" right-label="After" %}
  {% include juxtapose.html left="/assets/img/posts/corona-update/vc-maverick-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/vc-maverick-after.jpg" right-label="After" %}
  </div>

  Do note -- this fix can be **disabled** from the INI file if you happen to use modified vehicles which account for those misplacements.
  For GTA Vice City, [Fixed Xbox Vehicles](https://gtaforums.com/topic/942192-vc-fixed-xbox-vehicles/) have been adapted to fit fixed placements
  perfectly, so new additions such as FBI Washington sirens will match the model perfectly!

Other highlights
================

Not only coronas were given attention in this release. Other changes include, but are not limited to:

* Sirens of FBI vehicles in both GTA III and Vice City have been improved. In GTA III, secondary siren would sound together with car's horn,
and for Vice City, FBI Washington used a Vice Cheetah siren sound. It's now been changed to the FBI siren sound, same as FBI Rancher:
{% include video.html link="https://www.youtube.com/embed/xcLHBxALc2A" %}

* A glitch present in all trilogy games which allowed vehicles to spawn without any extras has been fixed.
In layman's terms this means that a bug allowing "lightless taxis" (in III/Vice City) and "engineless bikes" (in San Andreas) to spawn
is now gone! If you want to stock up on those truly unique vehicles, do it before updating SilentPatch --
your existing trophy vehicles will **not** be affected by this fix, so you can keep them even with this bug fixed!
{% include screenshot.html link="https://i.imgur.com/gB8lbx5.png" thumbnail="https://i.imgur.com/gB8lbx5h.png" %}

* GTA III has a few models which were supposed to have very high draw distance. However, this caused them to be treated as LOD models and
would cause them to disappear when camera is near. This was undesirable and caused models like cranes and window lights to disappear when the player got closer!
This has now been fixed and should make Liberty City look a bit nicer, especially with window lights working properly:
<div class="media-container small">
{% include juxtapose.html left="/assets/img/posts/corona-update/iii-crane-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/iii-crane-after.jpg" right-label="After" %}
{% include juxtapose.html left="/assets/img/posts/corona-update/iii-window-before.jpg" left-label="Before"
              right="/assets/img/posts/corona-update/iii-window-after.jpg" right-label="After" %}
</div>

* An oversight during GTA Vice City development resulted in an issue which made all submachine guns sound the same when
the player was performing a Drive-By. This naturally was not an issue to GTA III, as it had only a single weapon the player could use to fire from cars.
A fix has been introduced which makes Drive-By sound exactly the same as shooting on foot, introducing some much needed variety and consistency.

* When controlling an in-car camera with mouse in San Andreas, you may have noticed an issue not present when controlling the camera with the gamepad.
When looking left/right/behind, camera movement is supposed to be fully restricted -- however, when using the mouse it was not fully restricted,
and so the player could attempt to move it up/down. While moving left/right did nothing, it did give the radar some sort of an existential crisis.
Now it's been fixed, bringing parity in camera controls across mouse and gamepad.
{% include figures/video.html link="https://i.imgur.com/bDWEwC5.mp4" attributes="controls muted" %}

Miscellaneous fixes
===================

* GTA III: Enlarged the bounding box of Catalina's chopper and the police chopper to prevent it from being cut off on screen edges.
* GTA III/Vice City: Fixed corona lines rendering on non-NVIDIA graphics cards.
* GTA San Andreas: Fixed parachute animations.
* GTA San Andreas: "Keep weapons after wasted" and "keep weapons after busted" now reset on New Game.
* GTA Vice City/San Andreas: extra6 can now be picked by the game when random extra is to be picked.


Internal changes
--------------

Changes to existing SilentPatch code:
* GTA III/Vice City: Fix for light glows not showing under pickups/fire has been redone from scratch.
* GTA San Andreas: Fix for dancing minigame timings has been slightly altered to potentially reduce precision loss.
* GTA San Andreas: Moon phases fix is now not applied when SA-MP is used, as SA-MP erroneously keeps altering in-game date and breaks that feature.

***

The newest builds can be downloaded from *Mods & Patches* section here: \\
<a href="{% link _games/gta/gta-iii.md %}#silentpatch" class="button" role="button">{{ site.theme_settings.download_icon }} Download for GTA III</a>
<a href="{% link _games/gta/gta-vc.md %}#silentpatch" class="button" role="button">{{ site.theme_settings.download_icon }} Download for GTA Vice City</a>
<a href="{% link _games/gta/gta-sa.md %}#silentpatch" class="button" role="button">{{ site.theme_settings.download_icon }} Download for GTA San Andreas</a>

