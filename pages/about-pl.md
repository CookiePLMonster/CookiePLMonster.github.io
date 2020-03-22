---
layout: page
title: O mnie
excerpt: Moje krótkie bio.
permalink: /about/pl/
hide: true
---

*Ta strona dostępna jest w:*
<a href="{% link pages/about.md %}"><img style="height:1em;padding: 0 0.5em 0 1em"
    src="{% link assets/img/flags/gb.svg %}" alt="GB">*English*</a>
<a href="{% link pages/about-pl.md %}"><img style="height:1em;padding: 0 0.5em 0 1em"
    src="{% link assets/img/flags/pl.svg %}" alt="PL">*polski*</a>

***

<div style="max-width:35%;float:right;text-align:center" >
<img style="padding:0 5%;float:right" src="https://i.imgur.com/nnXmF1k.jpg" alt="Photo">
<em>To może dziwić, ale<br>nie jestem niebieski ani futrzasty.</em>
</div>
Hej, jestem **Adrian** -- za dnia pracuję przy programowaniu gier, wieczorami moduję i zajmuję się inżynierią zwrotną.
Próbuję naprawiać różne gry. W sieci udzielam się jako **Silent** lub **CookiePLMonster**.

***

Odkąd pamiętam, zawsze w jakiś sposób grzebałem w plikach gier. Pierwsze "próby", do których sięgam pamięcią,
to m.in. podmienianie plików dźwiękowych w Driverze, modyfikowanie tekstur w różnych grach freeware,
próby rozbudowywania Javowych skryptów Street Legal Racing Redline (jednak z marnym skutkiem).
Pierwsze poważniejsze modyfikacje zacząłem tworzyć w 2008 roku, kiedy po raz pierwszy zagłębiłem się
w Grand Theft Auto: San Andreas i używany w nim [język skryptowy](https://gtamods.com/wiki/SCM_language).
Po jakimś czasie zacząłem chcieć robić więcej niż pozwalały same skrypty, więc po około
dwóch latach zacząłem zagłębiać się w kod gry za pomocą inżynierii zwrotnej i eksperymentować z coraz to
bardziej złożonymi hackami w assemblerze (tak, zanim nauczyłem się jakiegokolwiek języka wysokiego poziomu,
programowałem w assemblerze). To w końcu spowodowało, że w połowie 2011 roku zacząłem uczyć się C++.

Wszystko toczyło się w swoim dość wolnym tempie aż do końca 2013 roku, kiedy wydałem SilentPatch do Grand Theft Auto III
i Vice City -- modyfikację naprawiającą błędy w grach. Okazała się ona dużo bardziej popularna niż pierwotnie zakładałem,
co spowodowało, że wydałem więcej SilentPatchy -- po kilku miesiącach do San Andreas, później do innych gier,
kompletnie niezwiązanych z GTA.

Przełomem dla mnie okazało się wydanie [Hotline Miami 2 XP Support Patch]({% link _games/hm2.md %}#hm2-xp)
w marcu 2015 roku, kilka dni po premierze gry. Patch został zauważony przez twórców i oficjalnie "zatwierdzony",
a także okazał się moim punktem wejścia do zdobycia kontaktów w branży gier -- co ostatecznie pozwoliło mi zdobyć
pierwszą pracę (w której jestem do dziś).

Czym zajmuję się obecnie? Utrzymuję się z portowania gier (sprawdź moje [Portfolio]({% link pages/portfolio.md %})),
dalej wydaję nowe modyfikacje i patche dosyć regularnie (sprawdź moje [Mody & Patche]({% link pages/mods.md %})),
a ostatnio też od czasu do czasu udzielam się w developmencie kilku emulatorów konsol
(sprawdź moją [aktywność na GitHubie](https://github.com/CookiePLMonster)).

{% assign lastdate = "2020-03-22" %}
{% assign m = lastdate | date: "%-m" %}
*Ostatnia aktualizacja:
{{ lastdate | date: "%-d" }} {% case m %}
  {% when '1' %}stycznia
  {% when '2' %}lutego
  {% when '3' %}marca
  {% when '4' %}kwietnia
  {% when '5' %}maja
  {% when '6' %}czerwca
  {% when '7' %}lipca
  {% when '8' %}sierpnia
  {% when '9' %}września
  {% when '10' %}października
  {% when '11' %}listopada
  {% when '12' %}grudnia
{% endcase %} {{ lastdate | date: "%Y" }}*