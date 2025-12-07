---
layout: page
title: O mnie
excerpt: Moje krótkie bio.
last_modified_at: 2023-08-20
permalink: /about/pl/
hide: true
lang: pl
locale: pl_PL
---

{:.sidenote}
Ta strona dostępna jest w:
[{% include elements/flag.html flag="gb" %} English]({% link pages/about.md %}){:style="white-space:nowrap" lang="en" hreflang="en"}
[{% include elements/flag.html flag="pl" %} polski]({% link pages/about-pl.md %}){:style="white-space:nowrap" lang="pl" hreflang="pl"}

***

<div style="display: flow-root" markdown="1">
{% include figures/image.html thumbnail="/assets/img/about.jpg" caption="To może dziwić, ale nie jestem niebieski ani futrzasty." style="natural aside" %}
Hej, jestem **Adrian** -- za dnia pracuję przy programowaniu gier, wieczorami moduję i&nbsp;zajmuję się inżynierią zwrotną.
Próbuję naprawiać różne gry. W&nbsp;sieci udzielam się jako **Silent** lub **CookiePLMonster**.

***
{:style="display: flow-root"}

Odkąd pamiętam, zawsze w&nbsp;jakiś sposób grzebałem w&nbsp;plikach gier. Pierwsze <q>próby</q>, do których sięgam pamięcią,
to m.in. podmienianie plików dźwiękowych w&nbsp;Driverze, modyfikowanie tekstur w&nbsp;różnych grach freeware,
próby rozbudowywania Javowych skryptów Street Legal Racing Redline (jednak z&nbsp;marnym skutkiem).
Pierwsze poważniejsze modyfikacje zacząłem tworzyć w&nbsp;2008 roku, kiedy po raz pierwszy zagłębiłem się
w&nbsp;Grand Theft Auto: San Andreas i&nbsp;używany w&nbsp;nim [język skryptowy](https://gtamods.com/wiki/SCM_language){:target="_blank"}.
Po jakimś czasie zacząłem chcieć robić więcej niż pozwalały same skrypty, więc po około
dwóch latach zacząłem zagłębiać się w&nbsp;kod gry za pomocą inżynierii zwrotnej i&nbsp;eksperymentować z&nbsp;coraz to
bardziej złożonymi hackami w&nbsp;asemblerze (tak, zanim nauczyłem się jakiegokolwiek języka wysokiego poziomu,
programowałem w&nbsp;asemblerze). To w&nbsp;końcu spowodowało, że w&nbsp;połowie 2011 roku zacząłem uczyć się C++.

Wszystko toczyło się w&nbsp;swoim dość wolnym tempie aż do końca 2013 roku, kiedy wydałem SilentPatch do Grand Theft Auto III
i&nbsp;Vice City -- modyfikację naprawiającą błędy w&nbsp;grach. Okazała się ona dużo bardziej popularna niż pierwotnie zakładałem,
co spowodowało, że wydałem więcej SilentPatchy -- po kilku miesiącach do San Andreas, później do innych gier,
kompletnie niezwiązanych z&nbsp;GTA.

Przełomem dla mnie okazało się wydanie [Hotline Miami 2 XP Support Patch]({% link _games/hm2.md %}#hm2-xp)
w&nbsp;marcu 2015 roku, kilka dni po premierze gry. Patch został zauważony przez twórców i&nbsp;oficjalnie <q>zatwierdzony</q>,
a&nbsp;także okazał się moim punktem wejścia do zdobycia kontaktów w&nbsp;branży gier -- co ostatecznie pozwoliło mi zdobyć
pierwszą pracę (w&nbsp;której jestem do dziś).

***
{:style="display: flow-root"}

Czym zajmuję się obecnie?
* Oferuję profesjonalne usługi wsparcia i&nbsp;doradztwa w&nbsp;zakresie wydawania starych gier PC na współczesne komputery
  (sprawdź wpisy oznaczone jako <q>Independent</q> w&nbsp;moim [Portfolio]({% link pages/portfolio.md %})). Moją specjalnością jest modernizacja starszych projektów,
  zapewniająca kompatybilność ze współczesnymi kompilatorami, systemami operacyjnymi oraz sprzętem. Problemy tego typu rozwiązuję również bez konieczności dostępu do kodu źródłowego gry. \\
  **Jeśli jesteś wydawcą planującym wydanie swojej klasycznej gry na platformach cyfrowej dystrybucji i&nbsp;potrzebujesz pomocy w&nbsp;zapewnieniu, by gra działała jak należy,**
  **daj mi znać -- nawet jeśli nie masz dostępu do kodu źródłowego tej gry!**
* Za dnia zajmuję się portowaniem i&nbsp;współtworzeniem gier (sprawdź moje [Portfolio]({% link pages/portfolio.md %})).
* Wciąż wydaję nowe modyfikacje i&nbsp;patche (sprawdź moje [Mody & Patche]({% link pages/mods.md %})). Moje hobby obejmuje ponad 40 gier na różnych platformach.
* Okazjonalnie udzielam się w&nbsp;różnych projektach z&nbsp;otwartym kodem źródłowym, takich jak np. [OpenRCT2](https://openrct2.io/){:target="_blank"} czy [PCSX2](https://pcsx2.net/){:target="_blank"}
  (sprawdź moją [aktywność na GitHubie](https://github.com/CookiePLMonster){:target="_blank"}).
* Regularnie udzielam się w&nbsp;[projekcie Redump Disc Preservation](http://redump.org/){:target="_blank"}. Swoją działalność skupiam na utrwalaniu płyt PC.

{% assign lastdate = page.last_modified_at %}
{% assign m = lastdate | date: "%-m" %}
{%- capture date_string -%}
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
{% endcase %} {{ lastdate | date: "%Y" }}
{%- endcapture -%}
{:.sidenote}
Ostatnia aktualizacja: {% include elements/time.html date=page.last_modified_at text=date_string %}
</div>
