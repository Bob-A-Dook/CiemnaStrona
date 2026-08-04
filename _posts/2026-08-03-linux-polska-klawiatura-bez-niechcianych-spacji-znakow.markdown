---
layout: post
title: "Dziwne znaki, spacje i stylometria – polska klawiatura na Linuksie"
subtitle: "Niemiłe niespodzianki od klawisza Alt."
description: "Niemiłe niespodzianki od klawisza Alt."
date:   2026-08-03 18:00:00 +0100
tags: [Inwigilacja, Linux, Open source, Stylometria, UX]
image:
  path: /assets/posts/open_source/linux-polska-klawiatura/uklad-klawiatury-polski-baner.jpg
  width: 1200
  height: 700
  alt: "Mem pokazujący dwie rysunkowe postacie, posępną i szczęśliwą. Przy posępnej widać niepolskie znaki i rozjechany tekst, a przy szczęśliwej nazwę układu klawiatury, który to naprawia"
---

Na łamach tego bloga od lat pisuję o&nbsp;cyfrowej prywatności i&nbsp;wolności. Od zeszłego roku istotną rolę zajęły tu również -- raczej poza stroną główną -- treści dotyczące Linuksa. Albo oficjalniej: systemów *na bazie* Linuksa.

Tak się bowiem składa, że widzę w&nbsp;tych otwartych systemach ratunek przed wszechobecną monopolizacją i&nbsp;dojeniem ludzi subskrypcjami. Im popularniejsze staną się Linuksy, tym większy opór napotkają korporacje przy próbie ich wykluczania.

W tym wpisie mam okazję pogodzić oba wspomniane nurty, linuksowy i&nbsp;prywatnościowy.  
Pokażę, że kiedy na Linuksach korzysta się z&nbsp;domyślnego polskiego układu klawiatury, to **do tworzonych tekstów mogą trafiać niewidoczne, nietypowe spacje. Albo znaki nieznane w&nbsp;języku polskim**.

Może to być źródłem frustracji dla nowych użytkowników. Rzeczą prozaiczną, ale irytującą, utrudniającą oswojenie się z&nbsp;nowym systemem.

Zagrożenie dla anonimowości jest subtelniejsze, ale też istnieje. Drobne anomalie mogą ujawniać, że ktoś napisał tekst na innym urządzeniu niż zwykle. W&nbsp;skrajnych przypadkach mogą wspomagać analizę identyfikującą konkretnego autora tekstu.

Przybliżę problem i&nbsp;pokażę, w&nbsp;jaki sposób można zmienić ustawienia na Mincie i&nbsp;paru innych Linuksach, zyskując ergonomiczny (i&nbsp;niewyróżniający z&nbsp;tłumu) układ klawiatury: ze znakami polskimi, bez obcojęzycznych, bez dziwnych spacji.

Zapraszam!

<img src="/assets/posts/open_source/linux-polska-klawiatura/uklad-klawiatury-polski-baner.jpg" alt="Mem pokazujący dwie rysunkowe postacie, posępną i&nbsp;szczęśliwą. Przy posępnej widać niepolskie znaki i&nbsp;rozjechany tekst, a&nbsp;przy szczęśliwej nazwę układu klawiatury, który to naprawia"/>

## Spis treści

* [Zarys problemów](#zarys-problemów)
  * [Problem pierwszy: obce litery](#problem-pierwszy-obce-litery)
  * [Problem drugi: spacje](#problem-drugi-spacje)
* [Ciemne strony niespodziewanych znaków](#ciemne-strony-niespodziewanych-znaków)
* [Co można zrobić](#co-można-zrobić)
  * [Ogólny plan działania](#ogólny-plan-działania)
  * [Zmiana układu na konkretnych Linuksach](#zmiana-układu-na-konkretnych-linuksach)

    {:.post-meta}
    Obecnie to: Mint (MATE, Cinnamon i LMDE), PorteuX (MATE i Cinnamon), Zorin.

## Zarys problemów

Po przesiadce na Linuksa pierwszym odruchem wielu osób jest [ustawienie języka polskiego](/tutorials/linux-mint-jezyk-polski-system.html){:.internal}. W&nbsp;tym wybranie polskiego układu klawiatury.

Rzecz szybka i&nbsp;prosta. Rozwinięcie listy, na przykład podczas instalowania nowego systemu na dysku. Wypatrzenie na niej najprostszego układu polskiego.  
Pozostałe -- `Polish (cośtam)` -- są raczej ignorowane jako zbędna egzotyka.

{:.post-meta .bigspace-after}
Z perspektywy codziennego użytkownika. Wiem, że dla niektórych ludzi wsiąkniętych w&nbsp;świat cyfrowy spersonalizowana klawiatura to świętość.

Działanie klawiatury można sprawdzić, otwierając notatnik i&nbsp;naciskając np. `Alt+O` (jak *Ola*). Powinno wstawić w&nbsp;polu literkę `ó`. Sukces, działa!

### Problem pierwszy: obce litery

Jeśli jednak wciśnie się `Alt` w&nbsp;połączeniu z&nbsp;innymi literami, na których nie opierają się polskie znaki, to efekt może zaskakiwać. Przykładowo:

* `Alt+D` daje `ð`,
* `Alt+T` daje `ß`,
* `Alt+G` daje `ŋ`,
* `Alt+W` daje `œ`.

{:.post-meta .bigspace-after}
Nie mam pod ręką Windowsa, żeby to jednoznacznie potwierdzić, ale wydaje mi się, że tam znaków obcych nie ma. Albo przynajmniej kiedyś nie było. Pamiętam, że były dla mnie zaskoczeniem po przesiadce na Linuksa.

Te obce litery są pewnym utrapieniem, ale przynajmniej je widać i&nbsp;da się przywyknąć. Zwłaszcza jeśli z&nbsp;czasem nabierze się wprawy w&nbsp;pisaniu, liczba literówek spadnie, a&nbsp;szybkość ich poprawiania wzrośnie.

Oprócz nich pojawia się jednak coś gorszego. Rzecz niewidoczna zwykle gołym okiem i&nbsp;trudna do wyłapania. To **spacje nierozdzielające**.

### Problem drugi: spacje

{% include info.html
type="O spacji słów parę"
text="Spacja nierozdzielająca, inaczej niełamliwa (ang. *non-breaking space*), ma dwa oblicza.  
Na zewnątrz, w&nbsp;oczach człowieka, wygląda jak najzwyklejsza spacja. Dla komputera jest natomiast oznaczeniem specjalnym, mówiącym: „nie rozdzielaj tego, co jest złączone tym znakiem”.  
A po co się je stosuje? Choćby dla celów estetycznych -- można na przykład zapobiegać sytuacjom, gdy linijki kończą się pojedynczymi literkami (jak `i`), tak jakby myśl zawarta w&nbsp;zdaniu nagle się urywała. Uniknie się kąśliwych uwag od recenzenta :wink:"
trailer="<p><img class='bigspace-before' src='/assets/posts/open_source/linux-polska-klawiatura/recenzja-fragment-sieroty.jpg' alt='Fragment recenzji naukowej mówiący, że niektóre linijki pracy doktorskiej kończą się pojedynczymi literami, co jest błędem'/></p>
<p class='figcaption nospace'>Ciekawostka: takie litery nazywa się <a href='https://pl.wikipedia.org/wiki/Sierotka_(typografia)'><i>sierotami</i></a>.</p>"
%}

{:.post-meta .bigspace-after}
Według [artykułu z&nbsp;Wikipedii](https://pl.wikipedia.org/wiki/Spacja_nie%C5%82ami%C4%85ca) istnieje pewien niuans -- jeśli spacja ma stałą szerokość i&nbsp;nie reaguje na justowanie tekstu, to jest *spacją twardą*. Tu jednak dla uproszczenia pominę tę właściwość i&nbsp;nazwę wszystkie *nierozdzielającymi*.

Z nietypowymi spacjami zetknąłem się już jakiś czas temu, kiedy edytowałem dokumenty w&nbsp;programie LibreOffice.  
Zauważyłem, że tekst czasem dziwnie się układał. Słowa przeskakiwały do kolejnej linijki, mimo że zmieściłyby się w&nbsp;poprzedniej. Że tak to zilustruję:

{:.bigspace}
<img src="/assets/posts/open_source/linux-polska-klawiatura/tekst-przeskakujacy.png" alt="Tekst w&nbsp;programie LibreOffice. Jedno słowo znajduje się w&nbsp;drugiej linijce, choć zmieściłoby się w&nbsp;pierwszej"/>

Po włączeniu podglądu znaków specjalnych okazało się, że źródłem problemu istotnie są spacje nierozdzielające. **Pojawiały się zwykle po polskich znakach** -- istotny fakt, którego znaczenie mi umknęło.

{:.bigspace-before}
<img src="/assets/posts/open_source/linux-polska-klawiatura/tekst-przeskakujacy-wyjasnienie.png" alt="Tekst w programie LibreOffice z widocznymi znakami formatowania."/>

{:.figcaption}
Okrąg na szarym tle to wewnątrz LibreOffice'a oznaczenie spacji nierozdzielającej. Spacje standardowe oznaczane są zaś jako niebieskie kropki.

Ogólnie nie miałbym problemu ze spacjami nierozdzielającymi; ba, celowo je czasem wstawiałem, naciskając kombinację `Ctrl+Shift+Spacja` (typowa dla LibreOffice'a, ale nie jakaś uniwersalna).

Ale tych *innych* spacji nie chciałem i&nbsp;nie zamawiałem. A&nbsp;skoro nie... To skąd się wzięły?

Musiało minąć dobre kilka lat od napotkania problemu, nim ustaliłem jego przyczynę. Jeśli kogoś interesuje ta historia, to można poczytać rozwijaną zakładkę. W&nbsp;innym wypadku można przewijać dalej.

{% include details.html summary="O szukaniu źródła problemu" %}

{:.bigspace-before}
Póki spacje widywałem tylko wewnątrz LibreOffice'a -- i&nbsp;póki nie różniły się na oko od tych celowych -- nie miałem punktu zaczepienia. Szukanie pod hasłem `libreoffice unwanted non-breaking space` mi nie pomagało.

Uznałem, że może to jakiś błąd LibreOffice'a, że po polskich znakach wstawia niechciane rzeczy. Typografia trudna rzecz *itede*. Przywykłem i&nbsp;po prostu czyściłem dokumenty z&nbsp;dziwnych spacji, ręcznie albo skryptem.

Z problemem zetknąłem się ponownie kilka lat później, tworząc tego bloga.

Minimum technikaliów: wpisy na blogu mają postać plików `.markdown`, czytelnych dla człowieka i&nbsp;łatwych do edycji. Potem program budujący bloga przetwarza je na format HTML, przyjaźniejszy z&nbsp;kolei dla przeglądarki ładującej strony.  
W tych wpisach często celowo wstawiam (głównie własnym skryptem, nie ręcznie) spacje nierozdzielające w&nbsp;[postaci HTML-owej, czyli `&nbsp;`](https://www.freecodecamp.org/news/html-space-how-to-add-a-non-breaking-space-with-the-nbsp-character-entity/).

Pewnego dnia zauważyłem, że tekst dziwnie się zachowuje. Słowo, które powinno być ostatnim w&nbsp;linijce, bo miało miejsce, przeskoczyło linijkę niżej.  
Pliki tekstowe mają tę zaletę, że wiele rzeczy w&nbsp;nich widać od razu. Jak to, że w&nbsp;miejscu przeskoku nie było oznaczenia `&nbsp;`.

Na oko była tam zwykła spacja... ale oczy są zawodne. Wrzuciłem tekst do Pythona i&nbsp;spojrzałem na jego postać niesformatowaną. Szybko się okazało, że **oprócz spacji wstawianych celowo, jako HTML, miałem tam również „pierwotne”, zapisywane jako [`\xa0`](https://stackoverflow.com/questions/10993612/how-to-remove-xa0-from-string-in-python)**. Przeglądarka traktowała oba rodzaje tak samo.

Zrobiłem na tym etapie [jedną z&nbsp;największych zmian w&nbsp;historii bloga](https://github.com/Bob-A-Dook/CiemnaStrona/commit/36684c0da1b79f5a9220303e87f4ff123712cc5d), masowo zamieniając niechciane spacje nierozdzielające na zwykłe. Zadbałem też o&nbsp;to, żeby sprawniej je wyłapywać na etapie edycji.

...A potem poszukałem również przyczyn problemu.

Na tym etapie wiedziałem, że problem jest ogólniejszy niż LibreOffice czy polskie znaki. Miałem również konkretny ciąg znaków odpowiadających niechcianym spacjom. Poszukałem w&nbsp;internecie, pod hasłami w&nbsp;stylu `linux unwanted non-breaking spaces inserted` albo `linux \xa0 in text`. W&nbsp;końcu doprowadziło mnie to do rozwiązania.

{% include details-end.html %}

Przyczyną problemu był fakt, że **domyślny polski układ klawiatury przypisuje spacji nierozdzielającej kombinację `Alt+Spacja`**.

Wyjaśniało to, dlaczego spacje tak często pojawiały się po polskich znakach. Wstawiając je, siłą rzeczy trzymałem `Alt`. Dając po nich spację, widocznie nie do końca puszczałem klawisz. Komputer odczytywał to jako kombinację `Alt+Spacja` i&nbsp;wstawiał spację nierozdzielającą.

## Ciemne strony niespodziewanych znaków

Obecność nietypowych i&nbsp;prawie niedostrzegalnych spacji była dla mnie pewnym utrapieniem. Na szczęście raczej tylko pod względem estetycznym.

Niektórzy mają z&nbsp;nimi większe problemy. Ktoś opisał na swoim blogu [różne metody wyłączania tych spacji](https://hauweele.net/~gawen/blog/?p=32) (po angielsku), pisząc że zawadzają mu podczas pisania kodu, bo programy przetwarzające kod źródłowy sobie z&nbsp;nimi nie radzą.

Nie zdziwiłbym się, gdyby nietypowe spacje były też realnym problemem podczas interakcji z&nbsp;niektórymi serwisami dla konsumentów.

Takie serwisy mogą domyślnie rozbijać słowa na *zwykłych* spacjach, bo ich twórcy nie przewidzieli istnienia innych. Jeśli ktoś wpisze w&nbsp;formularz przykładowo `Jan Nowak`, to serwis może rozbijać tekst na różne części w&nbsp;zależności od tego, jaka była w&nbsp;nim spacja.

* zwykła -- `["Jan", "Nowak"]` (2&nbsp;elementy);
* niełamliwa -- <code>["Jan<span class="red">\xc2\xa0</span>Nowak"]</code> (1&nbsp;element).

{:.post-meta .bigspace-after}
Wygląd listy elementów i&nbsp;tekstu inspirowany językiem Python. Fragment wyróżniony kolorem odpowiada tutaj spacji nierozdzielającej w&nbsp;zapisie „bajtowym”.

W ten sposób mogą powstawać błędy trudne do wyłapania, zwłaszcza dla osób oddalonych od świata komputerów. A&nbsp;wszystko przez parę małych, niewidocznych spacji.

### Aspekty prywatnościowe

Dziwne wytwory klawiatury na Linuksie mogą uprzykrzyć życie osób chcących zachować anonimowość w&nbsp;sieci i&nbsp;nie wyróżniać się z&nbsp;tłumu.

Trudno bowiem mówić o&nbsp;niewyróżnianiu się, kiedy komuś zamiast `sąd` pisze się czasem `sąð`, bo `Alt` się zacina. Można nawet przeoczyć taką literówkę, litery dość podobne.

Takie widoczne litery oraz spacje nierozdzielające to **anomalie**. Rzeczy niestandardowe, których u&nbsp;typowego użytkownika by się raczej nie zauważyło. Na ich podstawie można, w&nbsp;zależności od sytuacji, ustalić parę rzeczy:

* „Ta osoba stworzyła wiadomość z&nbsp;innymi znakami niż zwykle”.  
   Można złapać człowieka dotąd windowsowego na używaniu Linuksa.

* „Ta osoba używa innych znaków niż większość użytkowników naszego forum”.  
  Punkt wyjścia do wyłapania czyichś *alt-kont* na forum zdominowanym przez „normików klawiaturowych”?

Istnieje cała dziedzina oparta na analizowaniu tekstu i&nbsp;wyłapywaniu takich nietypowych wzorców wyróżniających ludzi. Jest nią [stylometria](https://pl.wikipedia.org/wiki/Stylometria). Polega na przepuszczeniu tekstu przez program, który analizuje jego właściwości. Długość zdań, użyte słowa, interpunkcję...

W ten sposób tworzy coś w&nbsp;rodzaju **stylistycznego „odcisku palca”** danej osoby. Można potem porównywać z&nbsp;nim „odcisk” innych tekstów i&nbsp;ustalić, jaka jest szansa, że napisała je ta sama osoba. Skuteczność tym większa, im więcej materiału źródłowego.

Na ile jest skuteczna ta metoda „w naturze”? To zależy.

Jeśli na jakimś forum *darknetowym* ktoś pisze (ogólnikowe) zdania szykiem mistrza Yody, żeby nie powiązano stylu z&nbsp;jego wiadomościami w&nbsp;szyfrowanym komunikatorze -- to już idzie za daleko jak na mój gust :wink:

Nie zmienia to jednak faktu, że potencjał stylometrii jest realny. Pozwoliła choćby [złapać Teda „Unabombera” Kaczynskiego](https://theconversation.com/how-the-unabombers-unique-linguistic-fingerprints-led-to-his-capture-207681).  
Niektóre używane przez niego zwroty były typowe dla uczelni z&nbsp;rejonu Chicago, inne dla osób w&nbsp;konkretnym przedziale wiekowym. To zawęziło krąg podejrzanych.  
Decydujący okazał się natomiast rzadki zwrot *cool-headed logicians* -- użyty zarówno w&nbsp;opublikowanym tekście, jak i&nbsp;w rozmowach z&nbsp;rodziną.

Inny przykład stylometrii praktycznej, która wyłapała parę *alt-kont* i&nbsp;była dla ludzi małym szokiem, można znaleźć w&nbsp;pamiętnej [dyskusji na forum HN](https://news.ycombinator.com/item?id=33755016). Nie będę streszczał, proponuję po prostu poczytać.

**Nietypowe znaki w&nbsp;tekście pisanym to wymarzony wsad do takich analiz**. Same w&nbsp;sobie nie określają jednoznacznie autora, ale wydają się solidnym punktem danych w&nbsp;połączeniu z&nbsp;innymi czynnikami.  
Z tego względu można rozważyć -- czy to na serio, czy dla zabawy i&nbsp;larpowania -- „ustandaryzowanie” swojej linuksowej klawiatury i&nbsp;pozbycie się anomalii. Zaraz do tego przejdę.

{% include info.html
type="Powiązane wpisy"
text="Miałem kiedyś okazję napisać o&nbsp;[anomaliach dotyczących wiadomości z&nbsp;Messengera](/facebook_dane/2021/05/14/messenger-analiza.html){:.internal}. W&nbsp;szczególności: choć na zewnątrz widać tę samą emotę, z&nbsp;danych można odczytać, czy została sklecona z&nbsp;prostych znaków -- `:)` itp. -- czy wstawiona z&nbsp;przybornika.  
Niektóre osoby mają swoje wyraźne preferencje. Od czasu stworzenia wpisu poznałem nawet osobę wstawiającą nietypowe, podwójne uśmiechy tekstowe, jak `;))` (pozdrawiam, I.).  
We wpisie na temat [Monitora Sądowego i&nbsp;Gospodarczego](/krs-msig/2022/06/17/msig-problemy#kapry%C5%9Bne-kolumny){:.internal} pokazuję z&nbsp;kolei, że zarówno metadane plików PDF, jak i&nbsp;sposób rozmieszczania elementów na stronie -- jako wielu drobnych pól tekstowych zamiast całych linijek -- mogą ujawniać, w&nbsp;jakim programie powstał plik."
%}

## Co można zrobić

Pierwszy podstawowy fakt: **nie ma czegoś takiego jak jeden Linux, są _Linuksy_**. To cała galaktyka różnych odmian, zwanych *dystrybucjami*.

Z układem klawiatury jest na Linuksach jak ze wszystkim -- każdy może go wdrażać po swojemu. Nie ma jednego, świętego standardu. Zawsze jest zatem ryzyko, że metoda znana z&nbsp;jednego systemu nie zadziała na innym.

Na szczęście nie ma również całkowitej wolnej amerykanki. Osoby odpowiedzialne za różne dystrybucje nie chcą raczej ingerować w&nbsp;takie fundamenty jak kod wgrywający układ klawiatury i&nbsp;sięgają po gotowce. Dzięki temu jest trochę cech wspólnych.

{:.post-meta .bigspace-after}
Wedle moich obserwacji rzeczy są raczej podobne w&nbsp;obrębie tego samego *środowiska graficznego* (jak Cinnamon), między środowiskami różnią się nieznacznie (np. nazwami wewnętrznymi ustawień), zaś dystrybucja ma na tym tle znikome znaczenie.

Widzę co najmniej dwa sposoby na dokonanie zmiany:

1. zmiana układu klawiatury na inny, też polski, ale mniej problematyczny;
2. edycja plików związanych z&nbsp;domyślnym polskim układem klawiatury.

Drugie rozwiązanie jest ciut bardziej techniczne, więc zostawię je na osobny wpis dla chętnych. Skupię się na tym, co można zrobić łatwo i&nbsp;szybko, nieraz również bez konsoli. Na tym, **jak ustawić inny układ klawiatury na wybranych systemach**. A&nbsp;będą nimi: Linux Mint (w&nbsp;wariantach MATE, Cinnamon i&nbsp;LMDE), Porteux (MATE i&nbsp;Cinnamon) oraz Zorin.

{% include info.html
type="Uwaga"
text="Wszystko sprawdzałem na systemach w&nbsp;trybie *live*, świeżo załadowanych z&nbsp;pendrive'a do pamięci. Nie gwarantuję, że na Linuksach zainstalowanych na stałe, na dysku, jest tak samo. Ale powinno być."
%}

### Ogólny plan działania

Na wszystkich wymienionych systemach najprostszy polski układ, wybierany przez większość osób, jest oznaczony po prostu skrótem `pl`. To on jest obarczony wspomnianymi problemami niechcianych znaków i&nbsp;spacji.

Istnieją też warianty tego układu. Często zapisywane jako `pl`, potem jakiś znak łączący, a&nbsp;potem słowo uzupełniające. Będę je zapisywał jako `pl+coś`.  
Niektóre z&nbsp;nich są wyspecjalizowane. Wolę ich nikomu nie proponować, bo zamieniają klawisze miejscami.

Ostatecznie zawężę dostępne rozwiązania do dwóch:

* `pl+legacy`{:.red} -- „układ dawny”.

  Bardzo podobny do domyślnego; przynajmniej pod względem tych cech, które mnie interesują. Nadal zawiera obce znaki, ale przynajmniej `Alt+Spacja` daje wyłącznie zwykłe spacje.

* `pl+intl`{:.red} -- „układ międzynarodowy” (*international*).

  Brzmi idealnie, bo **nie zawiera ani dziwnych znaków, ani spacji nierozdzielających**.  
  `Alt+D` daje zwykłe `D`, `Alt+Spacja` zwykłą spację... Jest jednak pewien haczyk. Ten układ jest wewnętrznie oznaczony jako egzotyczny. To sprawia, że na niektórych Linuksach nie ma go na liście, a&nbsp;na innych jest ukryty.

Na wszystkich systemach przyjmę tę samą taktykę -- **skupię się na próbie włączenia tego lepszego układu „międzynarodowego”**. Jeśli jest niedostępny, to zwykle na otarcie łez można wybrać z&nbsp;listy układ dawny.

Po zmianie układu warto sobie sprawdzić, czy spacje faktycznie „znormalniały”. Można to zrobić wygodną funkcją konsolową. Więcej szczegółów w&nbsp;rozwijanej zakładce.

{% include details.html summary="Sprawdzanie, czy układ się zmienił (i&nbsp;ogólnie o&nbsp;konsoli)" %}

{:.bigspace-before}
Zachowanie spacji można sprawdzić szybko i&nbsp;łatwo, bez otwierania ciężkiego programu w&nbsp;stylu LibreOffice'a. Wystarczy Python&nbsp;3, zainstalowany domyślnie na każdym znanym mi Linuksie.
 
Żeby to zrobić, można otworzyć przez menu konsolę, zwaną też Terminalem. I&nbsp;wkleić do niej (<code>Ctrl+<span class="red">Shift</span>+V</code>) takiego jednolinijkowca:

```
python3 -c "print(input('Twój tekst: ').encode('utf-8'))"
```

Po wykonaniu tej komendy wyświetli się prośba o&nbsp;wpisanie tekstu. W&nbsp;tym momencie należy nacisnąć kombinację `Alt+Spacja`, a&nbsp;potem `Enter`.

Jeśli pod spodem pokaże się zwykła „bajtowa” spacja (`b' '`), to znaczy że nowy układ nas uwolnił od nierozdzielających. Jest dobrze.  
Jeśli natomiast pojawią się znaki `b'\xc2\xa0'`, to znaczy że nadal wstawia nierozdzielające. Niedobrze.

{% include details-end.html %}

### Zmiana układu na konkretnych Linuksach

Koniec ogólników, od tego miejsca będą sposoby dotyczące konkretnych systemów.  
W każdej zakładce będę opisywał kolejno:

* sposób oparty na zwykłym klikaniu w&nbsp;menu,
* sposób konsolowy.

  Polecam go zwłaszcza osobom korzystającym z&nbsp;trybu *live* albo ustawiającym swojej firmie/rodzince komputery z&nbsp;Linuksem.  
  Używając skryptów, można ustawiać lubiane rzeczy od razu po włączeniu komputera, bez konieczności żmudnego i&nbsp;powtarzalnego klikania.

{% include info.html
type="Powiązane wpisy"
text="Wszystkie opisane tu sposoby konsolowe opierają się na zmianie ustawień programem Dconf, który jest zwykle domyślnie zainstalowany.  
Zapraszam do [przewodnika po jego obsłudze](/tutorials/linux-dconf-skryptowanie.html){:.internal}, w&nbsp;którym pokazuję, jak odkryć komendy konsolowe stojące za pstryczkami z&nbsp;menu.  
To uniwersalna wiedza na przyszłość; powinna zachować aktualność znacznie dłużej niż bezpośrednie cytaty z&nbsp;ustawień."
%}

A teraz do rzeczy. O&nbsp;zmianie układu klawiatury na konkretnych systemach.  
Niżej opisy dla tych opartych na środowisku Cinnamon.

{:.post-meta .bigspace-after}
Jest niemała szansa, że tak samo zadziała na innych systemach z&nbsp;Cinnamonem, nie tylko tych wymienionych.

<a id="cinnamon-menu-klawiatury"/>
{% include details.html summary="Mint Cinnamon i&nbsp;PorteuX Cinnamon (przez menu)" %}

{:.bigspace-before}
Wspólnym mianownikiem jest tu środowisko graficzne Cinnamon, które muszę mocno pochwalić. Przez jego menu można łatwo -- po zaznaczeniu jednej opcji -- sięgnąć po układy rzadsze i&nbsp;bez problemu ustawić ten najlepszy polski.

Najpierw należy rozwinąć menu główne, klikając ikonę systemu w&nbsp;dolnym lewym rogu. Potem trzeba wejść do ustawień klawiatury, w&nbsp;dowolny sposób: 

* klikając zakładkę `Preferences`, potem zakładkę `Keyboard`;
* wybierając `Control Center` z&nbsp;kolumny po lewej i&nbsp;tam znajdując kafelek `Keyboard`.

W oknie z&nbsp;ustawieniami klawiatury należy kliknąć zakładkę `Layouts` (*Układy*) na górnym pasku. Pokaże się lista dostępnych układów, a&nbsp;pod nią przycisk `Add` (*Dodaj*). Klikamy go.

{:.post-meta .bigspace-after}
Może być wyszarzony, jeśli są już ustawione cztery układy; w&nbsp;takim wypadku należy któryś usunąć z&nbsp;listy.

Żeby na liście pokazał się ten najlepszy układ, `Polish (intl.), with dead keys`, należy **zaznaczyć opcję `Include less-common layouts` poniżej listy**. Potem należy wybrać pożądany układ. A&nbsp;na koniec -- kliknąć przycisk `Add` w&nbsp;dolnym prawym rogu.

{:.figure .bigspace}
<img src="/assets/posts/open_source/linux-polska-klawiatura/cinnamon-wybor-ukladu-pl-intl.png" alt="Okno z&nbsp;listą różnych polskich układów klawiatury. Kolorem wyróżniono elementy, które należy po kolei kliknąć."/>

Po dodaniu układu do listy można z&nbsp;niej usunąć inne układy, jak podstawowy polski. A&nbsp;jeśli ktoś woli go zostawić -- to należy kliknąć widżeta na dolnym systemowym pasku (pokazującego flagę albo skrót nazwy kraju, w&nbsp;zależności od ustawień). Klikając go, można zmienić aktywny układ na ten lepszy.
 
Można sobie teraz sprawdzić -- choćby sposobem opisanym wyżej -- czy dziwne znaki i&nbsp;spacje przestały się pojawiać.

{% include details-end.html %}

{% include details.html summary="Mint Cinnamon i&nbsp;PorteuX Cinnamon (jedną linijką w&nbsp;konsoli)" %}

{:.bigspace-before}
Na różnych systemach z&nbsp;Cinnamonem można użyć w&nbsp;konsoli takiej komendy, żeby zostawić sobie tylko układ polski międzynarodowy:

<pre class="black-bg mono nospace">
dconf write /org/cinnamon/desktop/input-sources/sources "[('xkb', 'pl+intl')]"</pre>

{:.post-meta .bigspace-after}
A gdyby ktoś wolał układ dawny -- można zmienić słowo *intl* na *legacy*.

Zmiana powinna nastąpić natychmiast po użyciu komendy. Można sobie sprawdzić.

A jeśli ktoś woli zostawić sobie do wyboru dwa układy -- angielski i&nbsp;polski międzynarodowy:

```
dconf write /org/cinnamon/desktop/input-sources/sources "[('xkb', 'us'), ('xkb', 'pl+intl')]"
```

{% include details-end.html %}

Dla systemów opartych na MATE:

{:.post-meta .bigspace-after}
Jest niemała szansa, że tak samo zadziała na innych systemach z&nbsp;MATE, nie tylko tych wymienionych.

{% include details.html summary="Mint MATE i&nbsp;PorteuX MATE (przez menu)" %}

{:.bigspace-before}
MATE wyróżnia się dwiema rzeczami:

1. Zmiana na układ „międzynarodowy” jest trudniejsza niż na Cinnamonie, bo **jest domyślnie ukryty, a&nbsp;jego „odkrycie” wymaga użycia polecenia konsolowego**:

   <pre class="black-bg mono nospace">
dconf write /org/mate/desktop/peripherals/keyboard/general/load-extra-items true</pre>

   {:.post-meta .bigspace-after}
   Bez użycia tej komendy można sięgnąć przez menu co najwyżej do układu *dawnego* -- bez dziwnych spacji, ale z&nbsp;dziwnymi znakami.

2. Na systemie Mint MATE nawet domyślny polski wstawia spacje zwykłe zamiast nierozdzielających.

   Jego użytkownicy to szczęściarze :wink: Tym niemniej nadal warto zmienić układ, jeśli chce się pozbyć również obcych znaków.

   {:.post-meta .bigspace-after}
   Poza tym nie mam pewności, czy ta właściwość jest zamierzona i&nbsp;się utrzyma. Na wersji 22.2 działa, ale może tylko dlatego, że ktoś tworzący system zostawił w&nbsp;nim swoje ustawienia, jak chustkę w&nbsp;ciele pacjenta?

Potem w&nbsp;każdym przypadku trzeba wejść w&nbsp;ustawienia -- kliknąć ikonę systemu na pasku i&nbsp;wybrać `Control Center`. Tam wypatrzyć kafelek `Keyboard`.  
Po otwarciu okna z&nbsp;ustawieniami klawiatury należy wejść w&nbsp;zakładkę `Layouts`. Pod listą dostępnych układów powinien być przycisk `Add`. Klikamy go.

{:.post-meta .bigspace-after}
Skoro już jesteśmy w&nbsp;tym menu, to można też odhaczyć opcję `Separate layout for each window`, żeby cały system miał jeden i&nbsp;ten sam układ.

Przeniesie nas do okna z&nbsp;dwiema rozwijanymi zakładkami. Z&nbsp;zakładki podpisanej *Country* można wybrać `Poland`.  
Jeśli wcześniej włączyło się pokazywanie rzadszych układów, to w&nbsp;zakładce drugiej, podpisanej *Variants*, będzie można teraz wybrać `Polish (intl., with dead keys)`. Jeśli nie, to na otarcie łez pozostaje `Polish (Legacy)`.

Po dokonaniu wyboru należy kliknąć przycisk `Add` w&nbsp;dolnym rogu okna. Nowy układ pojawi się na liście.

{:.bigspace-before}
<img src="/assets/posts/open_source/linux-polska-klawiatura/mate-wybor-ukladu-pl-legacy.png" alt="Okno wyboru układu klawiatury na systemie Mint MATE"/>

{:.figcaption}
Tutaj przykład dla sytuacji, gdy nie pokazuje egzotycznych układów. Pozostaje wybranie układu dawnego.

{% include info.html
type="Ciekawostka"
text="Na systemie PorteuX MATE zakładki od wyboru układu były wcześniej wyszarzone i&nbsp;nieaktywne, bo brakowało modułu zwanego `iso-codes`.  
[Zgłosiłem sprawę](https://github.com/porteux/porteux/issues/111), twórca poprawił i&nbsp;od wersji 2.7 już powinno działać. Jeśli ktoś używa starszej, albo innego systmu z&nbsp;podobnym problemem, to należy osobiście zdobyć wspomniany moduł."
%}

Jeśli zostawiliśmy sobie więcej niż jeden układ, to należy jeszcze wybrać nowy polski „bezspacjowy” jako aktywny. Można to zrobić przez widżeta, który pojawi się na pasku systemowym.  
Po najechaniu na niego kursorem pokaże się pełna nazwa aktywnego układu. Można się upewnić, czy to ten, który chcemy. A potem sprawdzić, czy działa.

{% include details-end.html %}

{% include details.html summary="Mint MATE i&nbsp;PorteuX MATE (jedną linijką w&nbsp;konsoli)" %}

{:.bigspace-before}
Ustawienia klawiatury na MATE wyróżniają się tym, że nazwy układów są zapisywane **z&nbsp;tabulatorem, a&nbsp;nie plusem** -- dla układu najlepszego, międzynarodowego, mamy na przykład `pl\tintl`.  
A żeby zmienić na ten układ, należy użyć komendy:

<pre class="black-bg mono nospace">
dconf write /org/mate/desktop/peripherals/keyboard/kbd/layouts "['pl\tintl']"</pre>

{:.post-meta .bigspace-after}
Osoby wolące układ dawny -- albo mające system bez układów egzotycznych -- mogłyby z&nbsp;kolei wpisać `pl\tlegacy`.

Zmiany powinny zajść od razu. Można się teraz cieszyć nowym układem.

A gdyby ktoś chciał dwa układy -- angielski oraz międzynarodowy polski:

<pre class="black-bg mono nospace">
dconf write /org/mate/desktop/peripherals/keyboard/kbd/layouts "['us', 'pl\tintl']"</pre>

{% include details-end.html %}

Dla innych systemów:

{% include details.html summary="Mint LMDE" %}

{:.bigspace-before}
Na świeżym LMDE 7, który sprawdzałem, **spacje nierozdzielające były wyłączone nawet w zwykłym polskim układzie**. Jeśli tylko one komuś przeszkadzają, to nie trzeba nic robić. Nadal jednak warto zmienić układ, żeby pozbyć się obcych liter.

Na tym systemie klawiaturę ustawia się przez menu właściwie tak samo jak na Mincie Cinnamonie. Jedyne różnice są kosmetyczne: znak plusa zamiast przycisku `Add`, opcja pokazywania rzadszych układów umieszczona obok listy, a&nbsp;nie pod nią...

Żeby się nie powtarzać, proponuję po prostu przewinąć w&nbsp;górę, do odpowiedniej [zakładki](#cinnamon-menu-klawiatury){:.internal} i&nbsp;działać zgodnie z&nbsp;instrukcją.

Różnica pojawia się jednak na poziomie konsoli. **Na LMDE należy użyć innej komendy, żeby ustawić układ polski międzynarodowy**:

```
dconf write /org/gnome/libgnomekbd/keyboard/layouts "['pl\tintl']"
```

Pod względem używania tabulatorów ten system przypomina bardziej MATE niż Cinnamona. A&nbsp;ścieżka do ustawień jeszcze inna. Ciekawa sprawa -- taka trochę sklejka, jak dziobak w&nbsp;przyrodzie :wink:

{% include details-end.html %}

{% include details.html summary="Zorin OS" %}

{:.post-meta .bigspace-after}
Testowałem na Zorinie 18.

Zorin to system oparty na środowisku GNOME, czyli czymś jeszcze innym niż wspomniane wyżej MATE i&nbsp;Cinnamon. Jest jednak mocno zmodyfikowany, więc nie traktowałbym go jak typowego GNOME'a.

Co ważniejsze: **na Zorinie nie ma układu klawiatury `pl+intl`**. Albo jest tak ukryty, że go nie znalazłem.  
Oznacza to, że trzeba raczej się zadowolić układem `pl+legacy` -- bez spacji niełamliwych, ale z&nbsp;obcymi znakami.

{:.post-meta .bigspace-after}
Można też ingerować w&nbsp;pliki odpowiedzialne za podstawowy polski układ. Ale to temat na osobny wpis.

Wybór przez menu jest łatwy -- wchodzi się w&nbsp;ustawienia systemu, centrum sterowania, potem ustawienia klawiatury. Tam, w&nbsp;obliczu niedostępności najlepszego układu, wybiera się na pocieszenie `Polish (legacy)`.

{:.bigspace}
<img src="/assets/posts/open_source/linux-polska-klawiatura/zorin-klawiatura-polska-legacy.png" alt="Zrzut ekranu z ustawieniami klawiatury na Zorinie i wybranym układem Polish legacy"/>

Można też ustawić sobie listę układów komendą konsolową, zostawiając ten wspomniany wyżej jako jedyny dostępny:

<pre class="black-bg mono nospace">
dconf write /org/gnome/desktop/input-sources/sources "[('xkb','pl+legacy')]"</pre>

{:.figcaption}
Gdyby wpisać niedostępny `intl` zamiast `legacy`,  to ustawiłoby jedynie domyślny angielski.

{:.nospace}
{% include info.html
type="Uwaga"
text="Warto wiedzieć, że **na Zorinie wybór układu jest chyba _zbugowany_**.  
Odkryłem to, dodając sobie do listy kilka układów: zwykły polski, polski dawny (*legacy*) i&nbsp;układ własny (*custom*). Kiedy klikałem potem nazwę układu na pasku, to nie zmieniało mi na ten, na który powinno. Dla *legacy* nadal wstawiało nierozdzielające. Pomogła pokazana wyżej komenda konsolowa.  
Warto o&nbsp;tym pamiętać, gdyby wydawało się, że nowy układ nie działa. Raczej działa jak należy... ale nie ręczę za widżeta z&nbsp;paska."
%}

{% include details-end.html %}

Na tym kończę wpis. Mam nadzieję, że choć parę osób uwolnię od klawiaturowych przeszkadzajek. Oby nasze teksty tworzone na Linuksie wyróżniały się jakością, a&nbsp;nie dziwnymi znakami :smile:

