---
title: Uptime Faker
order: 0
game-series: "tools"
excerpt: "Generic Windows library designed to help detecting issues related to high PC uptime."
date: 8-04-2021
---
The most accurate timers in Windows all count time from the time Windows has started. Historically, these values often were relatively small, as people usually shut down their PC at night, and therefore uptime stayed low. However, with the introduction of Fast Startup in Windows 8, uptime stopped resetting after shutting down the PC (since it's now effectively a partial hibernation). This led to uptimes inflating noticeably for most people, as with Fast Startup enabled it resets only on a full PC reboot.

Turns out, older software often cannot handle high uptimes. Much to my surprise, Application Verifier did not have any options to help detecting such issues by faking high uptime, I decided to create this plugin.

To allow using Uptime Faker as a general purpose fix for games and/or applications not handling high uptime gracefully, v1.1 added a ProcessTime INI option, making timers count time from the process creation instead of the last reboot.

{% include setup-instructions.html %}

***

<a href="https://github.com/CookiePLMonster/UptimeFaker/releases/latest/download/UptimeFaker32.zip" class="button">{{ site.theme_settings.download_icon }} Download (32-bit version)</a>
<a href="https://github.com/CookiePLMonster/UptimeFaker/releases/latest/download/UptimeFaker64.zip" class="button">{{ site.theme_settings.download_icon }} Download (64-bit version)</a>

<a href="https://github.com/CookiePLMonster/UptimeFaker" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
