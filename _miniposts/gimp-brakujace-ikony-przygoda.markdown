---
layout: page
title: "Program GIMP i polowanie na brakujące ikonki"
description: ""
---

W tym wpisie pobocznym (spoza strony głównej) opiszę historię **rozwiązania problemu kilku brakujących ikonek w&nbsp;programie GIMP**, służącym do obróbki grafiki. Pokażę krok po kroku, jak dzięki odrobinie dedukcji i&nbsp;prostych poleceń konsolowych udało się dojść do źródła błędu.

Opis może się przydać osobom chcącym zobaczyć trochę majsterkowania w&nbsp;praktyce i&nbsp;może kiedyś samodzielnie rozwiązywać problemy z&nbsp;Linuksami.  
Zapraszam, znajomość programowania zbędna :wink:

{:.post-meta .bigspace-after}
Choć formalnie nazwę programu powinno się zapisywać jako „GIMP”, dla ułatwienia i&nbsp;czytelności będę odtąd pisał „Gimp”.

## Spis treści

* [Trochę kontekstu](#trochę kontekstu)
* [Nieudane próby](#nieudane-próby)
* [Rozwiązanie problemu](#rozwiązanie-problemu)
  * [Punkt zaczepienia: tekst elementu](#punkt-zaczepienia-tekst-elementu)
  * [Plik z&nbsp;kodem edytora tekstu](#plik-zkodem-edytora-tekstu)
  * [Plik z&nbsp;definicjami ikonek](#plik-zdefinicjami-ikonek)
  * [Ustalenie folderu na ikonki](#ustalenie-folderu-na-ikonki)
  * [Przeszukanie całego systemu](#przeszukanie-całego-systemu)
  * [Kopiowanie ikon do folderu Gimpa](#kopiowanie-ikon-do-folderu-gimpa)
* [Bonus: stworzenie pakietu instalacyjnego](#bonus-stworzenie-pakietu-instalacyjnego)


## Trochę kontekstu

Od kilku miesięcy dość często korzystam z&nbsp;systemu **PorteuX**, opartego na Linuksie. Cenię go przede wszystkim za *ulotność*, czyli fakt, że po każdym włączeniu ładuje się od zera (ale błyskawicznie), z&nbsp;pendrive'a.

Dzięki temu nie mam obaw, że coś sobie trwale popsuję w systemie podczas eksperymentów. Poza tym zyskuję sporo prywatności, bo na komputerze nie gromadzą się pliki osobiste ani charakterystyczne. A&nbsp;przynajmniej nie przez czas dłuższy niż jedna posiadówka.

PorteuX ma jednak pewne bariery wejścia. Jedną z&nbsp;nich jest nietypowa forma instalowania programów zewnętrznych -- ładuje się je z plików XZM, zaś ich domyślnym źródłem są bazy **Slackware'a**.  
Działa to sprawnie od strony technicznej, nie mówię że nie. Ale w&nbsp;porównaniu z&nbsp;popularniejszymi sposobami instalowania, ten niestety jest dość słabo opisany i&nbsp;obgadany na forach. Jeśli któryś program od Slackware'a nie do końca działa, to jestem zwykle zdany na siebie.

Tak było również w&nbsp;przypadku **Gimpa**, czyli popularnego programu do edycji grafiki. Moduł dostępny w&nbsp;domyślnej bazie (`getpkg -m gimp`) nie działał i&nbsp;musiałem zdobyć jeszcze trochę *zależności*, czyli programów i&nbsp;bibliotek niezbędnych do jego uruchomienia. W&nbsp;końcu się to udało, ale to temat na osobną opowieść.

W każdym razie, kiedy już doszedłem do etapu, gdy Gimp się włączał i&nbsp;śmigał, pozostały kwestie kosmetyczne. **Nie wyświetlały mi się niektóre ikonki, jak te w&nbsp;narzędziu do edycji tekstu**. Różne przekształcenia (pogrubienie, kursywa...) nie miały własnych oznaczeń graficznych, tylko ikony zastępcze:

{:.figure .bigspace-before}
<img src="/assets/tutorials/gimp/brakujace-ikony/gimp-narzedzie-tekstu-brak-ikon.png" alt="Narzędzie tekstu Gimpa, z&nbsp;zaznaczonym szeregiem ikon zastępczych" />

{:.figcaption}
Przy tym powiększeniu niezbyt to widać, ale na ikonkach zastępczych widnieje Wilber (maskotka Gimpa) ze styraną miną.

Metoda rozwiązywania błędów, która dotąd się przy Gimpie sprawdzała -- czytanie komunikatów konsolowych, w&nbsp;których wprost ostrzegał o&nbsp;brakach -- w&nbsp;tym wypadku nie pomagała. Nie było żadnych komunikatów.

Przyznam, że nie rozwiązałem problemu od strzała, brakło mi cierpliwości. Zamiast tego co parę tygodni do niego wracałem i&nbsp;poświęcałem do pół godziny na wypróbowanie czegoś, co przyszło do głowy. W&nbsp;końcu się udało.

## Nieudane próby

Wcześniej korzystałem ze świetnego programu **`strace`**, pozwalającego monitorować wszystkie interakcje wskazanego programu z&nbsp;systemem plików.

Dokładniej rzecz biorąc, po zainstalowaniu świeżego Gimpa używałem takiej komendy konsolowej.

```
strace -o gimp-zapiski.txt -f -yy -s 1 gimp
```


{% include info.html
type="Drobna uwaga"
text="Przyjmę tu taką konwencję: komendy konsolowe będą tekstem takim jak wyżej, jaśniejszym. Tekst *wyświetlany* w&nbsp;konsoli albo innych programach będzie ciemniejszy. Fragmenty interesujące będę w&nbsp;paru miejscach wyróżniał dodatkowymi kolorami."
%}

{% include details.html summary="Omówienie komendy" %}

{:.bigspace-before}
Na początku jest nazwa samego programu, `strace`. Cała reszta to wrzucane do niego *parametry* o&nbsp;następujących efektach:

* `-o PLIK` zapisuje wyniki monitorowania do konkretnego pliku, w&nbsp;tym wypadku `gimp-zapiski.txt`,
* `-f` każe monitorować również podprocesy aktywowane przez ten śledzony,
* `-yy` każe zapisywać pełne nazwy i&nbsp;ścieżki plików (kluczowe!),
* `-s 1` ogranicza do minimum podgląd rzeczy zapisywanych lub odczytywanych (znaczna oszczędność miejsca w&nbsp;tworzonym pliku),
* `gimp` to komenda, pod którą podpinam śledzenie, po prostu uruchamiająca Gimpa w&nbsp;domyślnym trybie działania.

{% include details-end.html %}

Niestety, jak zobaczymy, Gimp nie ładował ikon w&nbsp;sposób najprostszy i&nbsp;bezpośredni. Droga przez *strace'a* -- choć [nieraz sprawdzona](/miniposts/linux-mint-mate-klawiatura){:.internal}, również przy innych dziwactwach Gimpa -- tym razem nie doprowadziła mnie do celu.

{% include details.html summary="Oczekiwania kontra rzeczywistość" %}

{:.bigspace-before}
Liczyłem na to, że w&nbsp;zapiskach *strace'a* trafię z&nbsp;grubsza na taki komunikat o&nbsp;nieudanym wczytaniu pliku z&nbsp;ikoną:

{:.post-meta}
```
openat({ścieżka}/icons/{nazwa_pliku}) = (File not found)
```

W ten sposób jasno bym widział: Gimp próbował odczytać ikonę, ale jej nie znalazł i&nbsp;zrezygnował. Miałbym nazwę brakującego pliku, której mógłbym poszukać w&nbsp;internecie.

Niestety ta eksploracja mnie donikąd nie doprowadziła; przy ikonach zdarzało się nieraz, że Gimp nie znalazł pliku w&nbsp;jednym miejscu, ale chwilę potem sprawdził w&nbsp;kolejnym i&nbsp;już go wczytał. Musiałbym odsiać takie przypadki, żeby zostać wyłącznie z&nbsp;zapiskami dotyczącymi wczytania całkiem nieudanego.

Poza tym nie wiedziałem nawet, pod jakimi nazwami wypatrywać brakujących plików, ani czy w&nbsp;ogóle są w&nbsp;wynikach *strace'a* (Gimp mógł pytać o&nbsp;pliki jakiegoś procesu systemowego, który nie był monitorowany).

{% include details-end.html %}

## Rozwiązanie problemu

Podczas jednej ze wspomnianych szybkich prób ugryzienia problemu zrobiłem wreszcie dwie rzeczy, które okazały się kluczem do rozwiązania zagadki.

1. Pobrałem [kod źródłowy Gimpa](https://github.com/GNOME/gimp).

   {:.post-meta}
   Można to zrobić, klikając zielony przycisk `Code` i&nbsp;wybierając opcję `Download ZIP`. Nie będzie tam historii zmian, a&nbsp;jedynie zrzut aktualnego kodu, ale nie potrzebowałem niczego więcej.

2. Najechałem kursorem na brakującą ikonę.

Rzecz pierwsza jest dość oczywista, druga nieco mniej.  
Chodzi o&nbsp;to, że po najechaniu kursorem wyświetla się pomocniczy opis wskazywanego elementu. W&nbsp;ten sposób **poznałem tekst przypisany do jednego z&nbsp;przycisków bez ikony**.

{:.figure .bigspace}
<img src="/assets/tutorials/gimp/brakujace-ikony/gimp-narzedzie-tekstu-podpis-ikony.png" alt="Narzędzie tekstu Gimpa. Kursor znajduje się na brakującej ikonie, a&nbsp;pod nią widać jej podpis" />

### Punkt zaczepienia: tekst elementu

*Strikethrough*, czyli przekreślenie. Nie wyglądało to na szukaną nazwę ikony... Ale mogłem mieć podejrzenie, że w&nbsp;kodzie Gimpa tekst i&nbsp;ikona pojawią się gdzieś blisko siebie.

{:.post-meta .bigspace-after}
Zaleta poboczna: to słowo dość charakterystyczne, niekoniecznie popularne w&nbsp;programie graficznym. Miałem nadzieję, że liczba wystąpień w&nbsp;kodzie będzie znośna.

Mając folder z&nbsp;kodem źródłowym, wszedłem do jego wnętrza i&nbsp;użyłem linuksowego „przeszukiwacza wnętrza plików”, Grepa:

<pre class="black-bg mono nospace">grep -r "Strikethrough"</pre>

{:.figcaption}
Argument `-r` sprawia, że Grep przeszukuje wszystkie pliki i&nbsp;podfoldery (oraz *ich* podfoldery itd.) w&nbsp;miejscu, w&nbsp;którym odpaliłem komendę.

W konsoli wyskoczyło całkiem sporo linijek! Miały ogólny format:

{:.post-meta}
```
{nazwa_pliku}: {linijka_z_szukanym_tekstem}
```

Wiele tych plików miało końcówkę `.po`. To popularny format, zawierający tłumaczenia tekstu. Nic dziwnego, że się pojawiły; w&nbsp;końcu szukałem słowa widocznego dla użytkowników, a&nbsp;Gimpa przełożono na wiele języków.

Wspólną cechą plików z&nbsp;tłumaczeniami była ścieżka zaczynająca się od `po/`. A&nbsp;to pozwoliło łatwo je odsiać, gdy dodałem do pierwszego Grepa filtrowanie:

<pre class="black-bg mono nospace">grep -r "Strikethrough" |&nbsp;grep -v "po/"</pre>

{:.post-meta .bigspace-after}
Łączenie komend w&nbsp;*combosy* pionowymi kreskami („rurami”) to jedna z&nbsp;najcenniejszych możliwości konsoli. Miałem przyjemność opisać ją [w setnym wpisie na blogu](/2024/12/09/rury-wprowadzenie){:.internal}. 

Po filtrowaniu pozostał tylko jeden pasujący wynik. Pomijając dla czytelności wielokrotne spacje:

<pre class="black-bg mono post-meta"><span class="red">app/widgets/gimptextstyleeditor.c</span>:  _("Strikethrough"));</pre>

Kolorem wyróżniłem ścieżkę do pliku. Miał w&nbsp;nazwie `text style editor`, czyli brzmiał dokładnie jak to, czego szukałem!  
Co jeszcze mówiła mi nazwa? Końcówka pliku `.c` sugerowała, że to kod źródłowy napisany w&nbsp;[języku C](https://pl.wikibooks.org/wiki/C/Dlaczego_uczy%C4%87_si%C4%99_j%C4%99zyka_C%3F). Którego nie znam... Ale mogłem mieć nadzieję, że będzie na tyle intuicyjny, że się połapię.

### Plik z&nbsp;kodem edytora tekstu

Znaleziony plik mogłem sobie otworzyć w&nbsp;czymkolwiek, wybrałem domyślny notatnik.

{:.post-meta .bigspace-after}
Niektórzy mogliby się pokusić o&nbsp;otwarcie na tym etapie mocniejszego edytora kodu, żeby trafnie pokazał zależności. Byłaby to lepsza opcja, ale w&nbsp;ramach wprawek w&nbsp;szukaniu postanowiłem traktować pliki jak zwykły tekst.

Wyszukałem w&nbsp;pliku słowo *Strikethrough* i&nbsp;zobaczyłem, że cały blok kodu, zapewne odpowiedzialny za stworzenie przycisku, wyglądał tak:

<pre class="black-bg mono post-meta nospace">
  gimp_text_style_editor_create_toggle (editor, editor->buffer->strikethrough_tag,
                                        GIMP_ICON_FORMAT_TEXT_STRIKETHROUGH,
                                        _("Strikethrough"));
</pre>

{:.figcaption}
Jeśli czytasz na urządzeniu mobilnym, to dolne linijki mogą nie zmieścić się na szerokość. Można wtedy przewinąć pole w&nbsp;poziomie.

Wokół było więcej podobnych bloków kodu, odpowiadających innym przyciskom edytora. Co najcenniejsze: miałem tu zmienną `GIMP_ICON_FORMAT_TEXT_STRIKETHROUGH`. Miała w&nbsp;tekście *ICON* -- mocna przesłanka za tym, że to tego szukałem!

Było to również jedyne wystąpienie tej zmiennej w&nbsp;pliku. A&nbsp;zmienne nie biorą się znikąd, muszą być gdzieś zdefiniowane.

Logiczny wniosek? **Ta zmienna musiała powstawać w&nbsp;innym pliku**, zaś w&nbsp;to miejsce była ładowana podczas działania programu.  
Za jej załadowanie odpowiadała zapewne któraś z&nbsp;linijek zaczynających się od `#include` i&nbsp;umieszczonych na początku pliku (podział kodu na moduły, podstawa programowania).

Było tych plików sporo, więc nie odwiedzałem ich po kolei, tylko zrobiłem kolejne przeszukiwanie masowe, wśród wszystkich plików źródłowych:

```
grep -r GIMP_ICON_FORMAT_TEXT_STRIKETHROUGH
```

Poza wiadomym wystąpieniem w&nbsp;pliku, w&nbsp;którym właśnie byłem, znalazło tylko jedno (kolorem wyróżniłem nazwę pliku):

<pre class="black-bg mono post-meta"><span class="red">libgimpwidgets/gimpicons.h</span>:#define GIMP_ICON_FORMAT_TEXT_STRIKETHROUGH  "format-text-strikethrough"</pre>

### Plik z&nbsp;definicjami ikonek

Nazwa znalezionego pliku zawierała tekst `gimp icons`, więc ponownie brzmiała obiecująco. Swoją drogą -- pliki `.h` również sugerują język programowania C.

Odwiedziłem go i&nbsp;istotnie była tam linijka, w&nbsp;której miało miejsce stworzenie interesującej mnie zmiennej:

{:.post-meta}
```
#define GIMP_ICON_FORMAT_TEXT_STRIKETHROUGH  "format-text-strikethrough"
```

Miałem tutaj przypisanie do zmiennej (po lewej) ciągu znaków (po prawej, otoczonego cudzysłowami) `format-text-strikethrough`.  
Skopiowałem ten tekst i&nbsp;zrobiłem kolejne pełne przeszukanie kodu. Ale nie występował nigdzie poza plikiem `gimpicons.h`.

Połączyłem to z&nbsp;faktem, że zmienna, do której został przypisany ten tekst, też nie była rozsiana po plikach; trafiała prosto do kodu tworzącego przycisk.  
Było zatem bardzo możliwe, że **tekst był początkiem całej drogi -- oczekiwaną nazwą ikony**. *Gdzieś* musiała być określona, a&nbsp;to miejsce pasowało.

Swoją drogą w&nbsp;kodzie miałem więcej linijek przypisujących tekst do zmiennych. Niektóre pasowały do innych przycisków, które mi się nie pokazywały.

{:.post-meta}
```
#define GIMP_ICON_FORMAT_TEXT_BOLD           "format-text-bold"
#define GIMP_ICON_FORMAT_TEXT_ITALIC         "format-text-italic"
#define GIMP_ICON_FORMAT_TEXT_UNDERLINE      "format-text-underline"
```

{% include details.html summary="Strace ślepym zaułkiem – potwierdzenie" %}

{:.bigspace-before}
Wspomniałem na początku, że programik *strace* mi tym razem nie pomógł, bo nie zaobserwowałem nietypowych błędów w&nbsp;ładowaniu ikon.

Teraz, mając konkretne nazwy plików, mogłem się upewnić, że nie było to przeoczenie. Użyłem tego polecenia co wcześniej, a&nbsp;potem przeszukałem zapiski pod kątem znalezionych nazw (jak np. `format-text-bold`).

Niczego nie znalazło, nawet nieudanych prób otwarcia. Utwierdziło mnie to w&nbsp;przekonaniu, że za ładowanie czcionek odpowiadał jakiś inny proces, niepodpięty pod Gimpa. A&nbsp;*strace* w&nbsp;tym trybie, w&nbsp;jakim go używałem, nic by nie pomógł.

{% include details-end.html %}

### Ustalenie folderu na ikonki

Na tym etapie miałem wystarczająco wiele informacji i&nbsp;charakterystycznych nazw, żeby spróbować poszukać w&nbsp;internecie brakujących ikon. Uruchomiłem wyszukiwarkę.

Po szukaniu pod hasłami pokroju `"format-text-bold" gimp icons` wyskoczyło mi parę stron z&nbsp;fragmentami kodu, które właśnie przed chwilą odkryłem... a&nbsp;także [konkretna ikona](https://github.com/Uzugijin/GIMP-IconThemes/blob/main/BlenderIconPack_v2/scalable/apps/format-text-direction-ltr-symbolic.svg) w&nbsp;formacie wektorowym SVG.

Sam [projekt](https://github.com/Uzugijin/GIMP-IconThemes), którego ta ikona była częścią, wydaje się nieoficjalnym motywem graficznym; personalizującym Gimpa, żeby przypominał program Blender.  
Mógłbym po prostu użyć tych ikon, gdyby zależało mi jedynie na uzupełnieniu braków. Ale to nie było *dokładnie to*, czego używał oficjalny Gimp.

Oprócz ikon projekt zawierał również opis ich instalowania, który naprowadził mnie na dobry trop. Była tam bowiem informacja o&nbsp;tym, co należy wyklikać w&nbsp;Gimpie, żeby poznać **ścieżki do folderów na ikony**.

U mnie (Gimp 3.0.6) rzeczy do przeklikania były inne, ale zbliżone:

> Edit > Preferences > Icon Theme

Był tam aktywny motyw (domyślny, *Default*) oraz jego ścieżka:

{:.bigspace}
<img src="/assets/tutorials/gimp/brakujace-ikony/gimp-motyw-ikon.png" alt="Lista dostępnych motywów ikon w&nbsp;Gimpie. Pod każdą nazwą motywu jest jego ścieżka"/>

Odwiedziłem ten folder. Wewnątrz było kilka innych podfolderów; pełna ścieżka do tego, z&nbsp;którego Gimp brał ikony, okazała się taka:

<pre class="black-bg mono post-meta nospace">/usr/share/gimp/3.0/icons/Default/scalable/apps</pre>

{:.figcaption}
W tym konkretnym miejscu już mógłby się przydać *strace* -- pozwoliłby potwierdzić, że Gimp bierze działające ikony z&nbsp;tego folderu.

Brakujących ikon z&nbsp;narzędzia tekstowego tu nie było, zero zaskoczenia. Mogłem natomiast przyjrzeć się ikonom *działającym*. Nie wiedziałem, czy wyłapię cokolwiek ciekawego, to była eksploracja.

Porównując nazwy ikonek z&nbsp;pliku `gimpicons.h` z&nbsp;plikami obecnymi w&nbsp;tym miejscu, zauważyłem parę różnic:

* ikonki kończyły się na `.svg`,
* wiele z&nbsp;nich miało w&nbsp;nazwie `-symbolic`.

Założyłem na tej podstawie, że w&nbsp;pliku z&nbsp;definicjami są same trzony, zaś **nazwa pliku jest tworzona według szablonu: `{trzon}-symbolic.svg`**.

{:.post-meta .bigspace-after}
A przynajmniej wtedy, kiedy włączona jest opcja korzystania z&nbsp;ikon symbolicznych, pokazana na obrazku.

### Przeszukanie całego systemu

Znałem już pełne, oczekiwane nazwy ikon. Wiedziałem, w&nbsp;jakim folderze je umieścić. Pozostaje tylko pytanie -- skąd je zdobyć?

Na tym etapie miałem kilka pomysłów, ale najpierw postanowiłem sprawdzić, czy takie ikony nie trafiły mi omyłkowo do jakiegoś innego podfolderu Gimpa. Zarzuciłem sieć szeroko, robiąc **przeszukanie nazw plików z&nbsp;całego systemu**:

```
sudo updatedb
locate "format-text-bold-symbolic"
```

Mocno się zdziwiłem, kiedy znalazło mi taki plik nie wewnątrz Gimpa, tylko **w plikach systemowego motywu graficznego**:

<pre class="black-bg mono post-meta">/usr/share/icons/elementary-xfce/actions/symbolic/<span class="red">format-text-bold-symbolic.svg</span></pre>

A czemu Gimp tutaj nie sięgał? Czy z&nbsp;założenia nigdy tego nie robił, czy też z&nbsp;moim motywem było coś nie tak?  
Tego niestety nie ustaliłem. Miałem natomiast mocne przeczucie, jak rozwiązać problem z&nbsp;ikonami.

{% include details.html summary="Ślepy zaułek – nagłówek pliku" %}

{:.bigspace-before}
Na tym etapie przyszło mi do głowy, że pliki SVG z&nbsp;motywu systemowego mogły być ignorowane, bo nie zawierały w&nbsp;pierwszej linijce nagłówka wskazującego typ pliku:

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
```

Wszystkie ikony z&nbsp;wnętrza Gimpa go miały, te z&nbsp;motywu systemowego już nie.

Ostatecznie nie okazało się to źródłem problemu, a&nbsp;ikony skopiowane do folderu Gimpa działały również bez nagłówka.  
Warto jednak pamiętać, że nagłówki też bywają kłopotliwe -- przykładowo **program Graphviz nie ładuje podlinkowanych plików, jeśli są ich pozbawione**.

{% include details-end.html %}

### Kopiowanie ikon do folderu Gimpa

Mogłem teraz odczytać nazwy ikon z&nbsp;pliku `gimpicons.h`, znaleźć ich odpowiedniki w&nbsp;plikach systemowych i&nbsp;skopiować je do folderu Gimpa. A&nbsp;potem zobaczyć, czy teraz Gimp je znajdzie.

Nie chciałem jednak robić tego na oko, bo istniało ryzyko, że naprawię tylko ikony dotąd znalezione, a&nbsp;pominę inne braki. Żeby rozwiązać to w&nbsp;sposób automatyczny i&nbsp;pełniejszy, stworzyłem <a download class="internal" href="/assets/skrypty/gimp-icon-debugger.py">skrypt pomocniczy w&nbsp;języku Python</a>, który:

1. zagląda do pliku `gimpicons.h` z&nbsp;kodu źródłowego  
   (musi być pobrany i&nbsp;wypakowany, domyślnie w&nbsp;tym folderze co skrypt),
2. kopiuje stamtąd trzony nazw ikon i&nbsp;tworzy z&nbsp;nich pełne nazwy według szablonu,
3. sprawdza, czy ma takie pliki w folderze z&nbsp;domyślnymi ikonami zainstalowanego Gimpa,
4. jeśli nie, to szuka plików o&nbsp;takich nazwach w&nbsp;folderach systemowych,
5. jeśli znajdzie pasujące ikony, to je kopiuje do folderu Gimpa.

Efekt działań? Do folderu Gimpa trafiało kilkanaście systemowych ikon. Zaś narzędzie od tekstu, podobnie jak parę innych elementów, stawało się czytelne:

{:.figure .bigspace}
<img src="/assets/tutorials/gimp/brakujace-ikony/gimp-narzedzie-tekstu-ikony-zdobyte.png" alt="Narzędzie tekstu Gimpa, już z&nbsp;kompletem ikonek" />

...Czy to rozwiązało wszystkie problemy? Niestety nie -- nadal **nie pokazuje mi się kilka ikon wewnątrz okna zapisu/eksportu plików**.

Mam podejrzenie, że to już jakiś problem ogólny, związany ze szkieletem GTK, na którym opiera się Gimp i&nbsp;niejedna inna aplikacja. To jednak sprawa na osobną przygodę.

Mam nadzieję, że wpis pokazał coś nowego albo przynajmniej użytecznego. Po kolejne zapraszam na stronę główną :smile:

### Bonus: stworzenie pakietu instalacyjnego

W obecnej sytuacji byłem zdany na skrypt Pythona, kopiujący brakujące ikony w&nbsp;oczekiwane miejsce (przypomnę: mój system celowo resetuje swój stan po każdym wyłączeniu, więc nie wystarczy, że skopiuję je tylko raz).

Co zrobić, żeby to uprościć i&nbsp;zyskać Gimpa, który po najprostszej instalacji już ma wszystkie ikony? Mogłem **stworzyć sobie przenośny instalator**. Coś, co po kliknięciu albo aktywacji programem umieszcza ikonki tam, gdzie powinny być.

{% include details.html summary="Tworzenie instalatora na systemie PorteuX" %}

{:.post-meta .bigspace-after}
Ta część jest już ściśle związana z&nbsp;systemem PorteuX, ale pewne zasady (pełna ścieżka odtworzona wewnątrz innego folderu itd.) są raczej uniwersalne dla linuksowych instalatorów.

W skrypcie ustawiłem (wpisując ścieżkę w zmienną `CUSTOM_ICON_COPIES_FOLDER`), żeby skopiowało mi brakujące ikony nie do folderu Gimpa, tylko do innego, który nazwałem `gicons`. Wybór nazwy czysto subiektywny.

Następnie uruchomiłem konsolę i&nbsp;stworzyłem sobie ścieżkę -- na razie tylko jako zmienną -- której pierwszy człon nazwałem `gimp-missing-icons` (też wedle kaprysu). Jej dalsza część (wyróżniona) była identyczna jak pełna ścieżka do folderu na ikony Gimpa:

<pre class="black-bg mono">iconpath=gimp-missing-icons<span class="red">/usr/share/gimp/3.0/icons/Default/scalable/apps</span></pre>

Następnie stworzyłem wszystkie foldery składające się na tę ścieżkę:

```
mkdir -p $iconpath
```

A potem skopiowałem tam ikony z&nbsp;folderu tymczasowego `gicons`:

{:.big-wordspace}
```
cp gicons/*.svg $iconpath
```

W ten sposób miałem małe drzewko folderów, które po nałożeniu na moje główne, systemowe, „włożyłoby liście” (pliki SVG) prosto do folderu Gimpa. Tam, gdzie ten ich domyślnie wypatruje.

Pozostało spakować to równoległe drzewko w&nbsp;moduł XZM. Tym razem musiałem odwołać się do folderu *na początku* całej ścieżki:

```
dir2xzm gimp-missing-icons
```

{:.post-meta .bigspace-after}
Zapewne poprosi na tym etapie o&nbsp;hasło admina; to normalne.

Efektem komendy był plik `gimp-missing-icons.xzm`, zawierający pełne „drzewko uzupełniające” plików i&nbsp;folderów, do nałożenia na główny system plików.

Mogłem go sobie teraz umieścić na pendrivie i&nbsp;aktywować razem z&nbsp;pozostałymi modułami związanymi z&nbsp;Gimpem. Gdybym chciał, mógłbym również go scalić z modułem głównym Gimpa:

{:.big-wordspace}
```
mergexzm {moduł_główny}.xzm gimp-missing-icons.xzm
```

W ten sposób miałbym wszystko upakowane w&nbsp;jednym samowystarczalnym pliku.

{% include details-end.html %}

