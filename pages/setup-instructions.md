---
layout: page
title: Setup Instructions
excerpt: Step-by-step setup instructions for mods and patches.
permalink: /setup-instructions/
hide: true
---

These instructions are general and apply to every download from this website.
Games used for the presentation do not have any relevance for the steps.

1. [Locating your game directory](#locating-directory)
    * [Steam](#steam)
    * [GOG Galaxy](#gog-galaxy)
    * [Rockstar Games Launcher](#rgl)
    * [Uplay](#uplay)
    * [Retail (disc)](#retail)
2. [Extracting the mod files](#extracting-files)
3. [Configuration](#configuration)

# 1. Locating your game directory {#locating-directory}

## Steam {#steam}

1. Locate the game entry in your Steam Library.
2. Right-click on the game entry, select *Manage -> Browse local files*. \\
    <p align="center">
    <img src="{% link assets/img/setup/steam.jpg %}">
    </p>
3. An Explorer window will open, revealing your game directory. You'll want to put your mod files here.

## GOG Galaxy {#gog-galaxy}

1. Locate the game entry in the GOG Galaxy client in the *Installed* tab.
2. Click on the <i class='fas icomoon icon-gog-settings'></i> icon, select *Manage installation -> Show folder*. \\
    <p align="center">
    <img src="{% link assets/img/setup/gog-galaxy.jpg %}">
    </p>
3. An Explorer window will open, revealing your game directory. You'll want to put your mod files here.

## Rockstar Games Launcher {#rgl}

1. In the RGL client, click *SETTINGS*.
2. Click on the game entry in the *My installed games* list.
3. Click *OPEN* next to the *View installation folder* entry. \\
    <p align="center">
    <img src="{% link assets/img/setup/rgl.jpg %}">
    </p>
4. An Explorer window will open, revealing your game directory. You'll want to put your mod files here.

## Uplay {#uplay}

1. Locate the game entry in the Uplay client in the *Games* -> *Installed* tab.
2. Right-click on the game entry, select *View game details*.
2. Click on *Properties*, then on *Open folder* in the *Local files* section. \\
    <p align="center">
    <img src="{% link assets/img/setup/uplay.jpg %}">
    </p>
4. An Explorer window will open, revealing your game directory. You'll want to put your mod files here.

## Retail (disc) {#retail}

If you've installed the game with a traditional installer from the disc, you probably know where the game is installed.
If not, it's easiest to locate it by following either its Desktop shortcut or the Start Menu shortcut:

1. Locate the game shortcut on Desktop or the Start Menu. Usually, it's easiest to locate the shortcut in the Start Menu by typing the game name.
2. Right-click the located shortcut and select *Open file location*.
    * On Windows 10, selecting this option on the Start Menu shortcut might take you to the location of the shortcut, not the game's executable
      (easily identifiable by `Start Menu` in the path). If that happens, right-click the shortcut and select *Open file location* from the context menu.
3. An Explorer window will open, revealing your game directory. You'll want to put your mod files here.   

# 2. Extracting the mod files {#extracting-files}
_This section assumes that you don't use WinZIP, WinRAR or 7-Zip and instead refers to the tools included in Windows._
_If you use any of these third-party file archivers, I assume you know how to extract the archives._

1. Right-click on the mod's archive (`.zip` file), select *Extract All...*.
2. Set the Destination folder to the game's directory you have previously located and click *Extract*. \\
    <p align="center">
    <img src="{% link assets/img/setup/extract-all.jpg %}">
    </p> \\
    If a prompt saying "*The destination has X files with the same names*" shows up, select "*Replace the files in the destination*".
3. Files will be extracted and the extracted files will appear in the game directory. \\
    <p align="center">
    <img src="{% link assets/img/setup/mod-files.jpg %}">
    </p>

# 3. Configuration {#configuration}
_This section is applicable only to select downloads._

1. Locate the game directory and the mod's configuration file -- if the mod has a configuration file,
   it has the same name as the mod's `.asi` file and has a `.ini` extension. If you have file extensions hidden,
   it might appear without one.
2. Double-click the file to open it in a text editor of choice -- typically Notepad.
3. Make the necessary changes as instructed by individual mod's configuration files, and save the file.