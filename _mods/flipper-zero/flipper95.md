---
title: Flipper95
game-series: "flipper-zero"
excerpt: "Stress test your Flipper by crunching prime numbers."
order: 0
date: 18-09-2024
---

{::options auto_id_prefix="{{ page.id | split: '/' | last }}-" /}

Application to stress test the Flipper by finding Mersenne primes using the Lucas-Lehmer Test,
much like Prime95 does.

## Usage

By default, the app starts from the Mersenne prime `M2`. This can be overridden from the CLI,
and the application may be instructed to advance to testing a higher Mersenne number
for primality.

The following commands are added to `ufbt cli`:
* `flipper95 advance Mx` -- advance calculations to Mersenne number `Mx`, where `x` is a positive number.
* `flipper95 prime` -- print the last found Mersenne prime.
* `flipper95 perfect_number` -- print a perfect number corresponding to the last found Mersenne prime. This number is calculated on demand, so this command might take a very long time!

{% include figures/image.html link="https://raw.githubusercontent.com/CookiePLMonster/flipper-bakery/refs/heads/main/flipper95/.catalog/screens/screen0.png" %}

***

<a href="https://lab.flipper.net/apps/flipper95" class="button" target="_blank"><i class="fas fa-flask"></i> Download from Flipper Lab</a>

<a href="https://github.com/CookiePLMonster/flipper-bakery/tree/main/flipper95" class="button github" target="_blank">{{ site.theme_settings.github_icon }} See source on GitHub</a>
