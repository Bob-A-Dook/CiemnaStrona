---
layout: page
title: Linux Mint Cinnamon, kulisy włączania polskiej klawiatury
description: "Od czytelnego interfejsu po konsolowe ściany tekstu."
---

System Linux Mint to jedna z&nbsp;najsolidniejszych otwartych alternatyw dla dominującego Windowsa. Kibicuję mu z&nbsp;całego serca, a&nbsp;od pewnego czasu tworzę różne poradniki, które ułatwią polskim użytkownikom przejście na ten system.

Jedną z&nbsp;rzeczy, które opisałem, było [ustawianie języka polskiego](/tutorials/linux-mint-jezyk-polski-system.html){:.internal}. Pokazałem zarówno klikanie w&nbsp;interfejs, jak i&nbsp;polecenia konsolowe dające ten sam efekt.

...Ale od tamtego czasu odkryłem, że konsola nie do końca daje to samo. W&nbsp;szczególności na **Cinnamonie**, czyli jednym z&nbsp;wariantów Minta.

Jeśli wyklikam w&nbsp;menu systemu, że chcę polski układ klawiatury, to nie tylko będę mógł wstawiać literę `ą` przez naciśnięcie `Alt+A`, ale również zyskam nową ikonę na dolnym pasku. Dzięki niej można przełączać się między układami.  
Szybkie polecenie konsolowe `setxkbmap pl` mi tego nie daje; literki działają, ale pasek się nie zmienia. Do tego układ wraca do poprzedniego stanu po ponownym zalogowaniu.

W jaki sposób sprawić za pomocą konsoli, że na dolnym pasku Cinnamona pojawi się kontrolka od układu klawiatury, ustawiona na język polski? Postanowiłem zanurkować w&nbsp;bebechy systemu, szukając odpowiedzi na to pytanie.

{% include info.html
type="Uwaga"
text="Lojalnie uprzedzam, że wpis nie zawiera odpowiedzi.  
Jeśli ktoś chce po prostu zyskać polskie znaki na Mincie, obojętnie w&nbsp;jaki sposób -- to polecam menu graficzne oraz mój przewodnik, podlinkowany wyżej.  
Obecny wpis może się natomiast przydać osobom chcącym lepiej poznać Minta i&nbsp;stopniowo przechodzić od interfejsu graficznego do debugowania w&nbsp;konsoli. Opisuję całą eksplorację krok po kroku. Z&nbsp;pozycji ucznia, nie mistrza (do którego mi daleko)."
%}

## Z&nbsp;punktu widzenia użytkowników

Najpierw zobrazuję dokładniej, na ilustracjach, na jakim efekcie mi zależało.

Każda osoba mająca pod ręką myszkę lub touchpada może kliknąć znak Minta w&nbsp;lewym dolnym rogu, następnie ikonkę z lewej kolumny otwierającą Centrum Sterowania *Światem*{:.corr-del}. Tam można znaleźć ikonkę odsyłającą do menu odpowiedzialnego za klawiaturę.

{:.bigspace}
<img src="/assets/tutorials/mint-cinnamon-klawiatura-strace/mint-cinnamon-menu-klawiatury.png" alt="Trzy ikonki: logo Minta, ikona Centrum Ustawień, ikona ustawień od klawiatury"/>

W tym menu można z&nbsp;kolei wejść w&nbsp;zakładkę `Layouts`. Pokaże się lista, na której jest tylko układ angielski. Należy kliknąć plusa pod nią, żeby dodać nowy układ. W&nbsp;kolejnym okienku znaleźć i&nbsp;wybrać polski.

{:.bigspace}
<img src="/assets/tutorials/mint-cinnamon-klawiatura-strace/cinnamon-polska-klawiatura.png" alt="Kolaż pokazujący przyciski, jakie należy kliknąć, żeby dodać polski układ klawiatury do listy wspieranych"/>

Efektem tych działań będzie dodanie flagi USA do dolnego paska. Po jej kliknięciu rozwinie się menu, z&nbsp;którego można wybrać flagę polską. A&nbsp;po jej kliknięciu -- zaczną nam działać polskie znaki.

{:.bigspace}
<img src="/assets/tutorials/mint-cinnamon-klawiatura-strace/cinnamon-polska-klawiatura-wybor.png" alt="Zrzut ekranu pokazujący wybranie polskiej flagi z&nbsp;dolnego paska Cinnamona"/>

Chciałem osiągnąć ten sam efekt. Mieć jakieś jedno konsolowe polecenie, które daje ikonkę polskiej flagi i&nbsp;działające polskie litery.

## Motywacja i&nbsp;oczekiwania

Nie był to pierwszy przypadek, gdy wychodziłem od klikania w&nbsp;interfejs, a&nbsp;potem patrzyłem, co się dzieje pod spodem.

Przykładowo: porównałem kiedyś, jakie pliki otwiera program działający, a&nbsp;jakie niedziałający. Ustaliłem, że w&nbsp;obu przypadkach to te same pliki. A&nbsp;zatem to nie brak czcionek był przyczyną [niewłaściwego wyświetlania azjatyckich znaków](/tutorials/linux-odzyskiwanie-azjatyckich-znakow.html){:.internal}.

Inny przykład: chciałem ustalić, jak działa program rozpakowujący pliki ZIP. Zwłaszcza że użycie programiku `unzip` na pliku, z&nbsp;którym ten graficzny dawał radę, kończyło się błędem.  
W tamtym przypadku odkryłem, że klikanie w&nbsp;interfejs woła program `7z`, czyli *7Zip*. Mogłem go użyć zamiast *unzipa* i&nbsp;zyskać pożądany efekt.

W tym przypadku również liczyłem, że znajdę którąś z&nbsp;dwóch rzeczy:

1. jakiś plik konfiguracyjny, do którego zapisywane jest konkretne ustawienie;
2. nazwę i&nbsp;ustawienia programiku konsolowego wołanego przez Centrum Sterowania.

W każdym z&nbsp;tych przypadków mógłbym łatwo stworzyć konsolowy zamiennik, a&nbsp;potem dodać go do jakiegoś większego skryptu, żeby wszystko sobie zautomatyzować.

Nie do końca poszło po mojej myśli, ale wyprzedzam fakty. Póki co -- plecak na plecy, czołówka na głowę. Czas na eksplorację ciemnej konsoli.

## Zaglądanie za kulisy

Na początek uruchomiłem konsolę kombinacją `Ctrl+Alt+T`. Obok niej ustawiłem najzwyklejsze okno Centrum Sterowania, z&nbsp;otwartą zakładką od układu klawiatury (jak na obrazku z&nbsp;poprzedniej sekcji, zawierającym słowo *Layouts*). 

### Ustalanie odpowiedzialnego programu

Wiedziałem, że za widocznym oknem z&nbsp;ustawieniami musi stać jakiś program-opiekun. Zależało mi na poznaniu jego nazwy, bo była potrzebna do dalszego konsolowego monitoringu.

W konsolę wpisałem polecenie:

```
xprop | grep WM_CLASS
```

{% include details.html summary="Objaśnienie" %}
`xprop` to programik od uzyskiwania informacji na temat okien. Po jego użyciu kursor przyjmuje kształt plusa. Jeśli teraz kliknę dowolne okno, to w&nbsp;konsoli wyświetli się sporo informacji na jego temat.

Te informacje, zamiast do konsoli, lecą do [rury](/2024/12/09/rury-wprowadzenie){:.internal} (`|`), a&nbsp;przez nią do innego programu.

Jest nim `grep`, program od wyszukiwania tekstu. Dostaje informacje o&nbsp;oknie i&nbsp;wyszukuje w&nbsp;nich tekst *WM_CLASS*; stojący zwyczajowo przy linijce z&nbsp;nazwą programu, do którego przypisane jest okno.

{% include details-end.html %}

Po kliknięciu okna z&nbsp;ustawieniami znalazło mi linijkę:

<div class="black-bg mono post-meta">
WM_CLASS(STRING) = "cinnamon-settings.py", "Cinnamon-settings.py"
</div>

{:.figcaption}
Żeby odróżnić treść komend konsolowych od wypluwanego przez nią tekstu, będę oznaczał ten drugi kolorem szarym.

Znaleziony tekst oznacza, że za okno ustawień odpowiada programik `cinnamon-settings.py`. Skrypt Pythona, bardzo dobrze! W&nbsp;tym języku akurat cośtam „mówię”. Gdybym nie miał innego pomysłu, to zawsze mogę spróbować się w&nbsp;nim rozczytać.
 
Na razie nie chciałem natomiast zaglądać do kodu, tylko potraktować program jak czarną skrzynkę, którą będę analizował.

Pierwsza rzecz do sprawdzenia: czy dałoby się go wykonać przez konsolę? Tak po prostu wpisując nazwę?

<pre class="black-bg mono">
cinnamon-settings.py<br/><span class="post-meta">cinnamon-settings.py: command not found</span>
</pre>

Nie. Skrypt widocznie nie znajduje się wewnątrz żadnego z&nbsp;folderów specjalnych Minta i&nbsp;nie wystarczy wołanie go po nazwie.

Żeby skutecznie go wołać, muszę wprost wskazać *ścieżkę*, jaka do niego prowadzi.  
Jak ją ustalić? A&nbsp;chociażby programikiem `locate`, który przeszukuje systemową bazę nazw plików:

```
locate cinnamon-settings.py
```

Znajduje mi dokładnie jeden plik na cały system i&nbsp;wyświetla jego pełną ścieżkę:

{:.post-meta}
```
/usr/share/cinnamon/cinnamon-settings/cinnamon-settings.py
```

### Strace

Mając pełną ścieżkę programu, mogłem go uruchamiać przez konsolę. A&nbsp;to pozwala na przykład podpinać pod niego różne analizatory i&nbsp;ustalić, co dokładnie robi.  
Takim analizatorem jest choćby *strace*, domyślnie zainstalowany na Mincie.

{% include info.html
type="Jak działa strace"
text="Za każdym razem, kiedy programy chcą na przykład zajrzeć do wnętrza plików, muszą prosić o&nbsp;to jądro systemu (czyli *de facto* Linuksa). Te prośby to po angielsku *syscalle* i&nbsp;dzielą się na różne rodzaje.  
Jeśli uznamy, że jądro systemu jest jak król udzielający programom audiencji -- to *strace* jest jak kronikarz, którego wysyłamy do sali tronowej. Zapisuje sobie wszystkie prośby, a&nbsp;następnie zdaje nam dokładną relację."
%}

Polecenie, którego użyłem:

```
strace -f -o PLIK PROGRAM
```
* Argument `-f` mówi, żeby śledzić nie tylko główny proces, ale również jego „dzieciaki”.
* Fragment `-o PLIK` wskazuje, do jakiego pliku *strace* powinien zapisać wynik swojego działania. Całkiem subiektywnie wybrałem nazwę *klawiatura.txt*, ale to naprawdę obojętne. Byle w&nbsp;kolejnych komendach była ta sama.
* Zamiast `PROGRAM` jest odkryta wyżej długa ścieżka do skryptu.

Po użyciu polecenia uruchamia się typowe okno z&nbsp;ustawieniami -- w&nbsp;końcu aktywowałem program, który nim steruje.

Zależało mi na śledzeniu zmian dotyczących układu klawiatury, więc wykonałem wszystkie kroki opisane [na początku wpisu](#zpunktu-widzenia-użytkowników){:.internal}, zyskując flagę na dolnym pasku. W&nbsp;tym momencie zamknąłem okno z&nbsp;ustawieniami, a&nbsp;*strace* przestał notować.

Rezultatem tej dość krótkiej interakcji był spory plik, liczący w&nbsp;moim przypadku 3,9 MB.

### Przegląd interakcji z&nbsp;plikami

Czego szukać w&nbsp;kronice *strace'a*? Dotąd miałem dobre doświadczenia ze sprawdzaniem interakcji z&nbsp;plikami. Dlatego również tutaj poszukałem na początek przypadków użycia funkcji `openat` (proszącej jądro systemu o&nbsp;otwarcie wskazanego pliku):

```
grep 'openat' PLIK
```

Wyskoczy bardzo dużo linijek, z&nbsp;których większość odpowiada ładowaniu elementów podczas samego uruchamiania programu. Może się to wydawać przytłaczające, ale parę intuicyjnych regułek pomaga okiełznać złożoność.

{% include details.html summary="Sposób na odsiewanie wyników ze strace'a" %}

{:.bigspace-before}
Gdybym miał wskazać regułkę dość uniwersalną -- **rzeczy interesujące będą raczej pod koniec, a&nbsp;nie na początku**.

Programy często po uruchomieniu ładują różne biblioteki, zależności, ikonki... *Strace* to wszystko łapie. Ale nie będzie tu rzeczy związanych *stricte* ze zmianą ustawień, dokonaną grubo po załadowaniu programu.

Poza tym przypomnę, że zawęziłem wyniki do funkcji *openat*, od otwierania plików. W&nbsp;tym kontekście można się wspomagać paroma innymi zasadami.

* Rzeczy zawierające w&nbsp;swojej ścieżce *icons* oraz końcówkę pliku *.svg* albo *.png* to różne ikonki, raczej mniej ciekawe.
* Pliki zawierające w&nbsp;ścieżce `python3/dist-packages` to zapewne różne moduły Pythona, potrzebne do działania obecnemu programikowi (który, przypomnę, sam jest skryptem Pythona).

  Niekoniecznie ciekawe w&nbsp;tym przypadku, bo zapewne są ładowane za każdym razem, gdy włączamy Centrum Sterowania.

* Pliki zawierające w&nbsp;ścieżce `.config/cinnamon/spices` to zapewne elementy interfejsu.

  Z&nbsp;pozoru wydają się czymś ciekawym; ale w&nbsp;nazwach widać rzeczy takie jak *printers* („drukarki”), więc może to być po prostu lista rzeczy ładowanych każdorazowo. Niezwiązana z&nbsp;układem klawiatury.

* Pliki nieznalezione (z&nbsp;wiadomością *No such file or directory* na końcu) były dla mnie mało interesujące, bo liczyłem na coś, do czego zapisano ustawienia.

Jeśli ktoś nie chce filtrować na oko i&nbsp;widzi, że szumu w&nbsp;danych jest za dużo, to można rozbudowywać regułkę Grepa, odsiewając stopniowo mniej ciekawe informacje. W&nbsp;tym celu można podać wynik z&nbsp;pierwszego Grepa do kolejnego, ale *wykluczającego* pewne wzorce (co daje argument `-v`).

Gdybym na przykład chciał odsiać pliki z&nbsp;ikonami, mające tekst `/icons/` w&nbsp;swojej ścieżce, zrobiłbym to tak:

```
grep 'openat' PLIK | grep -v '/icons/'
```

W moim przypadku nie rejestrowałem czasu wewnątrz *strace'a*. Ale gdybym to robił, to dawałoby to kolejną możliwość filtrowania -- „wydarzenia ze znacznikiem czasu większym od&nbsp;X”. Mógłbym celowo zawęzić wyniki do ostatnich sekund, kiedy to zmieniłem ustawienia.

{% include details-end.html %}

Oceniając wyniki na oko, znalazłem parę potencjalnych tropów, takich jak otwieranie plików zawierających w&nbsp;nazwie tekst *iso* albo zakopanych w&nbsp;głębi folderu o&nbsp;nazwie *X11*.

{% include details.html summary="Objaśnienie tropów pobocznych" %}

Słowo *iso* odnosi się zapewne do *International Standards Organisation* i&nbsp;ogólnie występuje tam, gdzie mamy jakieś oficjalne regulacje. Miary, wagi i&nbsp;te sprawy.

...Czy możliwe, że dwa znalezione pliki z&nbsp;tym słowem w&nbsp;nazwie odnoszą się do dwóch flag wyświetlanych w&nbsp;nowym menu? Żeby to sprawdzić, otworzyłem jeden ze znalezionych plików, kopiując jego ścieżkę przed „uniwersalnego otwieracza”, `xdg-open`:

```
xdg-open /usr/share/xml/iso-codes/iso_3166.xml
```

Po otwarciu pliku mogłem znaleźć w&nbsp;nagłówku komentarz wyjaśniający, czym on jest.

> This file gives a&nbsp;list of all countries in the ISO 3166&nbsp;standard, and is used to provide translations via gettext

Zatem faktycznie rzecz związana ze standardem i&nbsp;językami... Tyle że to wygląda na wewnętrzne informacje ładowane przez system, a&nbsp;nie plik od przechowywania ustawień.

W odmętach *strace'a* znalazłem również takie coś:

{:.post-meta}
```
/usr/share/X11/xkb/rules/evdev.xml
```

To też mocny trop, bo X11 odpowiada za różne rzeczy na Linuksie. Zarządzanie oknami, dostarczanie do programów zdarzeń z&nbsp;myszy i&nbsp;klawiatury...

Odczytując ten plik, mogłem zobaczyć, że istotnie dotyczy różnych układów klawiatury.

Ale nie ma co się cieszyć na wyrost, bo oprócz plików liczy się to, co robił z&nbsp;nimi program. Za chwilę zobaczymy, że jedynie *odczytywał* stąd informacje. Nie mogły to być zatem poszukiwane pliki konfiguracyjne.

{% include details-end.html %}


Spośród plików wyłapanych przez *strace'a* szczególnie zaciekawił mnie ten:

{:.post-meta}
```
/usr/share/cinnamon-control-center/ui/cinnamon-region-panel-layout-chooser.ui
```

Występowało tu parę ciekawych, charakterystycznych słów:

* *ui* (*User Interface*, czyli ogólna nazwa na to, co widzi użytkownik),
* *panel* (określenie na dolny pasek),
* *chooser* (element odpowiedzialny za wybieranie).

Miałem mocne podejrzenie, że to ten plik odpowiada za wszystko. Pojawił się zatem nowy pomysł: wyświetlić teraz *wszystkie* zapiski ze *strace'a*, już bez zawężania do funkcji *openat*. Ale trzymać się tylko tej linijki i&nbsp;późniejszych.

### Przegląd pełnych wyników strace'a

Plik stworzony przez *strace'a* był duży, a&nbsp;przeglądanie go w&nbsp;notatniku byłoby żmudne. Dlatego otwarłem go programikiem `less`, który ładuje zawartość na raty i&nbsp;radzi sobie z&nbsp;dowolnie wielkimi plikami:

```
less PLIK
```

Problemem była duża liczba linijek z&nbsp;komendami `recvmsg` oraz `poll`, z&nbsp;których praktycznie wszystkie wyglądały tak samo. Postanowiłem je odsiać, dlatego wyłączyłem *lessa* (przyciskiem `Q`) i&nbsp;uruchomiłem ponownie, dostawiając przed nim lekkie filtrowanie:

```
grep -F -v -e recvmsg -e poll PLIK | less
```

{% include details.html summary="Omówienie komendy" %}
* `-F` wyłącza znaki specjalne i&nbsp;sprawia, że Grep nas nie zaskoczy. Kropka faktycznie jest kropką, a&nbsp;nie oznaczeniem „jakakolwiek rzecz”.

  W&nbsp;tym wypadku ten argument nie robi różnicy, bo szukamy jedynie rzeczy złożonych z&nbsp;prostych liter. Ale warto go znać.

* `-v` sprawia, że Grep *odrzuca* rzeczy pasujące do wzorca.
* `-e TEKST` wskazuje tekst do wyszukania, można tego użyć wiele razy w&nbsp;jednej komendzie.

  Poprzednio tego nie używałem, ale teraz to robię, bo chcę znaleźć kilka rzeczy jedną komendą.

  {:.post-meta}
  Szukanie kilku wzorców naraz można też zapisać jako `'rzecz1|rzecz2'`, ale wyraźne wskazywanie każdej z&nbsp;nich z&nbsp;osobna wydaje mi się bardziej przejrzyste.

{% include details-end.html %}

Po użyciu komendy w&nbsp;konsoli zrobiło się znacznie czyściej. Ale wciąż nie chciało mi się przewijać wielu linijek dotyczących zwykłego ładowania menu.

Żeby przejść w&nbsp;dobre miejsce, użyłem funkcji szukania wbudowanej w&nbsp;*lessa*: nacisnąłem ukośnik (`/`), wpisałem `layout-chooser` (charakterystyczny fragment nazwy pliku, który mnie interesował), po czym nacisnąłem `Enter`. Przewinęło do odpowiedniej linijki.

Przy interesującym mnie pliku widać było ciekawy wzorzec:

<pre class="black-bg mono post-meta">
<span style="color:#59bc6d">openat</span>(AT_FDCWD, "ŚCIEŻKA", O_RDONLY|O_CLOEXEC) = <span class="red">13</span><br/>fstat(<span class="red">13</span>, {st_mode=S_IFREG|0644, <span style="color:#6959bc">st_size=8337</span>, ...}) = 0<br/>read(<span class="red">13</span>, "<?xml version=\"1.0\" encoding=\"UT"..., 8337) = <span style="color:#6959bc">8337</span><br/><span style="color:#59bc6d">close</span>(<span class="red">13</span>)
</pre>

Rozmiar pliku, odczytany z&nbsp;jego metadanych w&nbsp;linijce drugiej, wynosi 8337. Dane o&nbsp;takim samym rozmiarze zostały później wczytane z&nbsp;pliku w&nbsp;linijce trzeciej.  
Wniosek: wczytano całą zawartość pliku.

Ponadto plik został otwarty w&nbsp;linijce pierwszej (otrzymując numer 13), a&nbsp;zamknięty w&nbsp;czwartej. Wniosek? **Nie nastąpiło nic poza wczytaniem zawartości pliku**. Nie był zmieniany.

A to sugeruje, że nie był to plik konfiguracyjny, do którego zapisano jakieś nowe ustawienie. Zamiast tego program sterujący menu Cinnamona wczytał sobie informacje i&nbsp;coś z&nbsp;nimi zrobił.

{:.post-meta .bigspace-after}
Podobny wzorzec -- wczytanie danych i&nbsp;natychmiastowe zamknięcie -- widać też przy innych plikach, jak te zawierające w&nbsp;nazwie *iso*, które omawiałem wyżej jako poboczne tropy.

A co takiego zrobił nasz program? Tego niestety nie ustaliłem. Kolejne linijki *strace'a* pokazują między innymi użycie komendy `sendmsg`, na oko z&nbsp;danymi niebędącymi tekstem -- może program ulepił coś z&nbsp;informacji i&nbsp;wysłał to do jakiegoś innego procesu systemowego?

W każdym razie nie znalazłem ani zmiany pliku konfiguracyjnego, ani przywołania znanego podprogramu. Inne mechanizmy działania Linuksa są mi na razie mniej znane, więc odłożyłem sprawę na później.

## Podsumowanie

Na ten moment nie wyłapałem, co dokładnie zachodzi od momentu wybrania polskiej klawiatury z&nbsp;graficznego menu do pojawienia się ikonki na dolnym pasku Cinnamona.

Znam natomiast nazwę apletu (`keyboard@cinnamon.org`, odczytana po prawokliknięciu ikony flagi). Wiem również, gdzie szukać programu sterującego całym działaniem. To skrypt Pythona, więc będę w stanie się w&nbsp;nim rozczytać i&nbsp;może wyciągnąć jakieś wnioski. Ogólnie: wyzwanie na później :sunglasses:

Póki co była natomiast eksploracja: `xprop`, `locate`, `strace` do pliku, `grep`, `less`, filtrowanie i&nbsp;szukanie na oko... Mam nadzieję, że kronika z&nbsp;tej wyprawy pomoże komuś, kto chce osobiście, krok po kroku, zajrzeć za kurtynę i&nbsp;lepiej odkryć, jak działa Linux.

Ta wiedza się przyda, żeby go doskonalić i&nbsp;pomagać innym osobom w&nbsp;skutecznej migracji (która, mam nadzieję, będzie coraz intensywniejsza).
