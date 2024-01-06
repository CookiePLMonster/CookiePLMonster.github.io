---
title: Adjusted triggers sensitivity
game-series: "gran-turismo-concept"
order: 1
date: 04-03-2023
---

{:.credit}
Patch further improved by Aero_.

Since Gran Turismo games have always offered full control remapping, it's possible to utilize triggers on modern controllers for throttle/brake,
much like most modern games do. However, unlike in newer Gran Turismos, doing this in the PS2 games results in a mediocre experience -- analog sensitivity
is tailored for analog buttons of the DualShock 2 controller, and therefore inputs are heavily scaled. In practice, this means that anything over ~half the trigger
press is already registered as a 100% input, so precise throttle control is hard. With this code, I've removed this scaling as much as reasonably possible,
so now 100% input registers from a near full press of the trigger, therefore making the experience closer to how the later Gran Turismo games handle it.

{% include setup-instructions.html platform="ps2" %}

<a href="https://github.com/CookiePLMonster/Console-Cheat-Codes/blob/master/PS2/Gran%20Turismo%20Concept/Adjusted%20triggers%20sensitivity/SCES-50858_60013EBD_triggers.pnach" class="button" role="button" target="_blank">{{ site.theme_settings.eu_flag }} PAL (Tokyo-Geneva)</a> \\
<a href="https://github.com/CookiePLMonster/Console-Cheat-Codes/blob/master/PS2/Gran%20Turismo%20Concept/Adjusted%20triggers%20sensitivity/SCPS-55903_6810C3BC_triggers.pnach" class="button" role="button" target="_blank">ASIA (Tokyo-Geneva)</a>