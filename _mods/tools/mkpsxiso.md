---
title: MKPSXISO
order: 4
game-series: "tools"
excerpt: "A tool to unpack and/or build PlayStation CD images."
date: 18-09-2023
version: "2.04"
---

{:.credit}
MKPSXISO v1.x was developed by Lameguy64.
MKPSXISO v2.x is co-developed by G4Vi, spicyjpeg, Chromaryu, and myself.

`mkpsxiso` builds PlayStation CD images from an XML document.

`dumpsxiso` dumps PlayStation CD images to files and documents the precise structure to a `mkpsxiso` compatible XML document.

`mkpsxiso` is meant to provide a faster, cross-platform, modern replacement of the BUILDCD from the official development tools. BUILDCD unfortunately only runs on 16 bit DOS compatible systems and it's output format is unusable by modern CD burning tools. Other ISO creation tools such as MKISOFS do not allow controlling the precise order of files (necessary for optimizing access times) and do not support mixed-mode type files for CD streaming such as XA audio and MDEC video streams used by many PlayStation games. `mkpsxiso` outputs either a standard `.bin` and `.cue` or `.iso` ready to burn to CD or use in an emulator! The hope is that `mkpsxiso` tools ease PlayStation homebrew development and ROM hacking and reverse engineer efforts. `mkpsxiso` can also be used as a regular ISO creation tool that complies with the older ISO9660 standard with no Joliet extensions.

`mkpsxiso` can properly license the image with the Sony license data during ISO building eliminating the use of the extra program. However, you must supply your own copy. It can be found in the PsyQ SDK, see [Starting PSX Development](https://psx.arthus.net/starting.html). `dumpsxiso` can also dump the license data of an existing disk.

## Features

* Uses XML for scripting ISO projects.
* Outputs ISO images directly to iso or bin+cue image format.
* Injects license data into ISO image correctly.
* File LBA controlled by order of files allowing for file seek optimization (just like BUILDCD).
* Supports mixed-mode CD-XA stream files such as XA audio and STR video.
* Supports CDDA audio tracks from wav, flac, pcm, and mp3 files, both as DA files and just as audio tracks
* Can output log of all files packed with details such as LBA, size and timecode offset.
* Extract CDDA tracks from ISO as wav, flac, and pcm.
* Many images can be rebuilt 1:1 now.
    * XML generation: by default in strict LBA order, but can instead sort by dir for pretty output.
    * Timestamps and XA attributes are preserved.

<a href="https://github.com/Lameguy64/mkpsxiso/releases/download/v{{ page.version }}/mkpsxiso-{{ page.version }}-win64.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download (Windows 64-bit)</a> \\
<a href="https://github.com/Lameguy64/mkpsxiso/releases/download/v{{ page.version }}/mkpsxiso-{{ page.version }}-Linux.deb" class="button" role="button">{{ site.theme_settings.download_icon }} Download (Linux 64-bit, DEB)</a>
<a href="https://github.com/Lameguy64/mkpsxiso/releases/download/v{{ page.version }}/mkpsxiso-{{ page.version }}-Linux.rpm" class="button" role="button">{{ site.theme_settings.download_icon }} Download (Linux 64-bit, RPM)</a>
<a href="https://github.com/Lameguy64/mkpsxiso/releases/download/v{{ page.version }}/mkpsxiso-{{ page.version }}-Linux.zip" class="button" role="button">{{ site.theme_settings.download_icon }} Download (Linux 64-bit, ZIP)</a> \\
<a href="https://github.com/Lameguy64/mkpsxiso" class="button github" role="button" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>