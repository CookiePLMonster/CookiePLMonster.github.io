---
layout: page
title: Importing custom decals into Tokyo Xtreme Racer (2025)
excerpt: Personalize your car more.
feature-img: "assets/img/games/bg/tokyo-xtreme-racer-2025.jpg"
image: "assets/img/tutorials/txr2025-custom-decals/branding.jpg"
permalink: /tutorials/tokyo-xtreme-racer-2025/custom-decals/
hide: true
---

With this tutorial, you can **replace** the default decals with your custom ones.
It's currently unknown if **adding** decals is possible.

1. TOC
{:toc}

# Required tools

1. [FModel](https://fmodel.app/){:target="_blank"}
2. [UE4-DDS-Tools](https://github.com/matyalatte/UE4-DDS-tools/releases){:target="_blank"} (`UE4-DDS-Tools-*-GUI.zip`)
3. [UnrealReZen](https://github.com/rm-NoobInCoding/UnrealReZen/releases){:target="_blank"}

# Instructions

## Extracting the original decals

1. Open FModel.
2. Add Tokyo Xtreme Racer to the list of games in FModel. You will only have to do these steps once.
   1. Click on <i class="fas fa-arrows-up-down"></i> under `ADD UNDETECTED GAME`.
   2. Click on <i class="fas fa-ellipsis"></i> and navigate to the game directory, then select it.
   3. Click on <i class="fas fa-plus"></i> to add the game to the list.
   4. Click on the `UE Versions` dropdown and select `GAME_UE5_4`.
3. Select Tokyo Xtreme Racer from the list and click <kbd>OK</kbd>.
   If FModel mentions available updates, you may safely dismiss this dialog.
4. Set a proper AES key for the game. Again, you will only have to do these steps once.
   1. Navigate to <kbd>Directory</kbd> &rarr; <kbd>AES</kbd>.
   2. In the `Main Static Key` field, paste:
      ```
      0xD499D0D1C8E2B87D576EA9756B5137306D1A96D378124C16A6F033BE2A9CBB4A
      ```
      {:.pre-wrap}
      and press <kbd>OK</kbd>.
   3. If done correctly, `pakchunk0-Windows.utoc` in the `GAME ARCHIVES` list will no longer be greyed out.
5. Double-click on `pakchunk0-Windows.utoc` and navigate to the directory with decals: `TokyoXtremeRacer/Content/ITSB/ArtAssets/Models/Livery/Vinyl`.
6. Find the decal(s) you want to replace. Right-click on each and select <kbd><i class="fas fa-file-arrow-up"></i> Export Raw Data (.uasset)</kbd>.
7. If done correctly, the decal(s) will be extracted to a new directory created where FModel is. The decal(s) will be located in `Output/Exports/TokyoXtremeRacer/Content/...`.

## Replacing the decals

For each decal, do the following:

1. Open UE4-DDS-Tools.
2. Navigate to the directory with the extracted decals (`Output/Exports/TokyoXtremeRacer/Content/...`),
   drag and drop the `.uasset` file into the field that says <kbd>Drop .uasset here!</kbd>.
3. Drag and drop the image you want to replace the decal with into the field that says <kbd>Drop an image here!</kbd>.
4. Change the `UE version` field to `5.4` if necessary.
5. Press <kbd>Inject</kbd>.
6. A new `.uasset` file will be created in an `injected` directory. Take this asset, and replace the original asset from FModel's `Output` directory with that one.

## Importing the decals back into the game

1. Open the Command Prompt in a directory with UnrealReZen.
2. Run:
   ```
   UnrealReZen.exe --content-path "<path-to-fmodel>\Output\Exports" --game-dir "<path-to-game>\TokyoXtremeRacer\Content\Paks" --output-path "<path-to-game>\TokyoXtremeRacer\Content\Paks\CustomDecals_P.utoc" --compression-format Oodle --engine-version GAME_UE5_4 --aes-key 0xD499D0D1C8E2B87D576EA9756B5137306D1A96D378124C16A6F033BE2A9CBB4A
   ```
   {:.pre-wrap}
   where:
   * `<path-to-fmodel>` is the path where FModel is located. Next to that should be an `Output` directory where you extracted the original decals.
   * `<path-to-game>` is the path where Tokyo Xtreme Racer is installed. Notice this path is present twice in the command.
     A correctly constructed path **must** include `TokyoXtremeRacer` twice.
3. If done correctly, `CustomDecals_P.pak`, `CustomDecals_P.ucas` and `CustomDecals_P.utoc` files will be created in `<path-to-game>\TokyoXtremeRacer\Content\Paks`.
   If the decals are packed correctly, `CustomDecals_P.ucas` will **not** be 1KB in size. If it is, you've done something wrong.
4. If later you want to come back and repack the archive after adding more custom decals, do note that due to a bug in UnrealReZen, the tool currently cannot overwrite existing archives
   and it will crash when trying to do so. To fix this, go to `<path-to-game>\TokyoXtremeRacer\Content\Paks` and delete `CustomDecals_P.pak`, `CustomDecals_P.ucas` and `CustomDecals_P.utoc`,
   and re-run UnrealReZen.

***

You may now use your decals in the Livery Editor. Please note that the preview images will **NOT** be replaced! Custom decals only show once you place them on your car.

{% include figures/image.html link="/assets/img/tutorials/txr2025-custom-decals/screens/TokyoXtremeRacer-Win64-Shipping_U9flHqgR5R.jpg" thumbnail="auto" %}
