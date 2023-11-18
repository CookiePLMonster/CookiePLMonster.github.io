---
layout: page
title: Setup Instructions (PS2)
excerpt: Step-by-step setup instructions for PlayStation 2 patches.
permalink: /setup-instructions/ps2/
hide: true
---

These instructions are general and apply to every PS2 download from this website.
These steps apply to any game.

These instructions target PCSX2 on Desktop and AetherSX2 on Android.

1. [Downloading patches](#downloading-patches)
2. [Applying patches](#applying-patches)
    * [PCSX2 (Desktop)](#pcsx2)
    * [AetherSX2 (Android)](#aethersx2)

# 1. Downloading patches {#downloading-patches}

1. The download button opens a GitHub page with the patch. View the raw patch file by pressing <kbd><samp>Raw</samp></kbd>.
2. Right click and select <kbd><samp>Save As...</samp></kbd> (PC) or press the Download button (Android) on the page with the patch.
3. Save the file, changing its extension from `.pnach.txt` to `.pnach`. For that, you need to change the file type to <kbd><samp>All Files</samp></kbd>.
   The rest of the filename **must be preserved!**

# 2. Applying patches {#applying-patches}

## PCSX2 {#pcsx2}

1. Locate your `patches` directory. If your PCSX2 installation is portable, the directory resides next to PCSX2's executable file.
   Otherwise, it's located in `Documents\PCSX2`.
2. Put the downloaded `.pnach` file in that directory, ensure the file extension is **not** `.pnach.txt`.
3. Launch PCSX2, right click the game you've installed patches for on the Game List and select <kbd><samp>Properties...</samp></kbd>.
4. Navigate to <kbd><samp>Patches</samp></kbd> and enable the patch(es) you want to use by ticking the <kbd><samp>Enabled</samp></kbd> box.
   {% include figures/image.html thumbnail="/assets/img/setup/pcsx2-patch-screen.jpg" %}
5. Verify that patches have been activated correctly by launching the game.
   If everything was done correctly, a '<samp>X game patches are active.</samp>' message will show on startup in the top left corner.
   {% include figures/image.html thumbnail="/assets/img/setup/pcsx2-patches-enabled-qt.jpg" %}

## AetherSX2 {#aethersx2}

1. Open AetherSX2 and launch the game you downloaded patches for.
2. Open the pause menu and select <kbd><samp>Patch Codes</samp></kbd>. If a warning gets shown, click <kbd><samp>Yes</samp></kbd> to open the Cheat Manager.
3. Select <kbd><samp>Add Patch</samp></kbd> &rarr; <kbd><samp>IMPORT FROM FILE</samp></kbd>. Navigate to the patch file you've downloaded and select it.
4. Open <kbd><samp>Patch Codes</samp></kbd> again. If <kbd><samp>Enable Patches</samp></kbd> button is listed, click it.
5. If everything was done correctly, a '<samp>X cheat patches are active.</samp>' message will show on startup in the top left corner.
