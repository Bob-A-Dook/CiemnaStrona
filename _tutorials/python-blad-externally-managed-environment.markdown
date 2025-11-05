---
layout: page
title: Python na Linuksie i błąd „externally managed environment”
description: "Większa stabilność dla systemu, ale większe utrapienie dla niektórych."
---

Czas na krzyżówkę dwóch światów -- języka programowania Python (któremu kiedyś poświęciłem kilka poradników) oraz systemu Linux (któremu w&nbsp;tym roku poświęciłem ich całkiem sporo; przykładem [ten o&nbsp;instalacji](/tutorials/ventoy){:.internal}).

{:.post-meta .bigspace-after}
Dla purystów: wiem, że nie ma jednego Linuksa, tylko różne systemy oparte na jądrze o&nbsp;nazwie Linux. Ale mowa potoczna ma swoje prawa.

Dawniej życie było jakieś prostsze. Na Linuksie Python był zainstalowany domyślnie -- nie trzeba było go celowo pobierać, jak w&nbsp;przypadku Windowsa. Cała podstawowa biblioteka była pod ręką od pierwszego załadowania systemu.
 
Z czasem przychodziła zwykle potrzeba sięgnięcia po jakieś dodatkowe moduły. Wystarczyło wówczas włączyć konsolę i&nbsp;wpisać:

<div class="black-bg mono bigspace-before">
pip3 install MODUŁ
</div>

{:.figcaption}
Skąd trójka? Bo w&nbsp;czasach, kiedy zaczynałem pisać, na systemie były dwie wersje Pythona. Pisząc samo `pip`, używałoby się starszej.

To polecenie wołało program od instalacji modułów Pythona. Zamiast *MODUŁ* należało wpisać nazwę jednego z&nbsp;niezliczonych projektów dostępnych w&nbsp;oficjalnej bazie PyPI. Po chwili pobrany pakiet gościł na komputerze, gotów do połączenia z&nbsp;naszymi własnymi programami.

{:.bigspace-before}
<img src="/assets/tutorials/python-externally-managed-environment/xkcd-python-antigravity-edit.jpg" alt="Kolaż pokazujący rysunkową postać, która pyta drugą, unoszącą się w&nbsp;powietrzu, jakim cudem lata. Postać odpowiada, że to dzięki Pythonowi, o&nbsp;użyła polecenia 'import antigravity'. I&nbsp;raczej nie dlatego, że spróbowała dla porównania leków z&nbsp;szafki."/>

{:.figcaption}
Źródło: [XKCD](https://xkcd.com/353/). Przeróbki moje.

Teraz jednak czasy się zmieniły. Po pierwsze: PIP nie jest już domyślnie zainstalowany (przynajmniej na systemie Linux Mint, którego używam).  
Bolączka niewielka, bo instalacja jest dość prosta. Ale na niej nie kończą się problemy. Gorzej, że cytowane wyżej, **klasyczne polecenie -- zalecane przez wiele internetowych samouczków -- prowadzi od teraz do błędu**.

Pojawia się długi komunikat, w&nbsp;którym wyróżnia się czerwonym kolorem tekst u&nbsp;góry. **_Externally managed environment_**. Dosłownie: „środowisko zarządzane zewnętrznie”.

{% include details.html summary="Pełna treść komunikatu o&nbsp;błędzie" %}

```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

{% include details-end.html %}

Treść błędu zawiera kilka rozwiązań, owszem. Ale jest pełna żargonu i&nbsp;może przytłoczyć osoby, które nie siedzą w&nbsp;Pythonie, a&nbsp;jedynie kopiują cudze polecenia, żeby np. użyć jednego skryptu (jak mojego od [mapowania trolli korporacyjnych](/2022/12/24/biotechnologia-trolle-youtube){:.internal}). Takich osób może być coraz więcej wraz z&nbsp;upowszechnianiem się Linuksa.
 
W tym samouczku pokażę, z&nbsp;czego wynika błąd. Będą też różne sposoby na jego rozwiązanie i&nbsp;odzyskanie możliwości swobodnego instalowania cudów z&nbsp;Pythona.

Zapraszam!

## Spis treści

* [Uzasadnienie zmiany](#uzasadnienie-zmiany)
* [Sposoby na rozwiązanie problemu](#sposoby-na-rozwiązanie-problemu)
  * [Instalacja przez APT](#instalacja-przez-apt)
  * [PIP z&nbsp;opcją *break-system-packages*](#pip-zopcją-break-system-packages)
  * [Instalacja w&nbsp;środowisku wirtualnym](#instalacja-wśrodowisku-wirtualnym)
* [Bonus: rozwiązanie ręczne](#bonus-rozwiązanie-ręczne)

{% include info.html
type="Zanim zaczniemy"
text="Każdy z&nbsp;wymienionych tu sposobów (poza ręcznym, który często nie rozwiązuje problemu) wykorzystuje w&nbsp;mniejszym lub większym stopniu program APT, instalatora pakietów.  
Nie jest on domyślnie obecny na każdym Linuksie, a&nbsp;jedynie na tych należących do „rodziny” Debiana (jak Mint, Ubuntu, Zorin). Jeśli korzystasz z&nbsp;innego Linuksa, to skorzystaj z&nbsp;alternatywy odpowiedniej dla swojego systemu.  
Reszta porad, poza samym programem instalującym, powinna być raczej uniwersalna."
%}

## Uzasadnienie zmiany

Zmiana, nie ukrywajmy, może nieco irytować. Kiedyś była prosta komenda i&nbsp;wszystko działało, Python na systemie rósł w&nbsp;siłę*, a&nbsp;ludziom żyło się dostatniej*{:.corr-del}. Teraz to zabrano.  
Są jednak powody, dla których tak się stało.

Python nie gości na Linuksach tylko po, żeby łatwiej było tworzyć swoje skrypty. Jest tam głównie jako **filar wielu programów systemowych**.  
Niejeden program z&nbsp;interfejsem graficznym w&nbsp;rzeczywistości opiera się na jakimś skrypcie Pythona. Przykładem na Mincie jest Captain, pozwalający instalować pobrane pliki DEB po ich dwukrotnym kliknięciu.

{% include info.html
type="Ciekawostka"
text="Gdy przeszukałem na świeżym Mincie folder systemowy `\usr\bin` (z&nbsp;programami), znalazło mi jedynie dwa pliki kończące się na `.py` -- skrypty Pythona o&nbsp;tradycyjnej nazwie.  
Tyle że programy i&nbsp;skrypty na Linuksie nie muszą mieć końcówki jasno sugerującej język, w&nbsp;jakim je napisano. Pewniejszym sposobem byłoby wyszukanie w&nbsp;ich treści [magicznej linijki](/2024/12/09/rury-wprowadzenie#ulepszenie-magiczna-linijka){:.internal} `#!/usr/bin/python`.  
Znalazło mi takich plików 74. Podkreślę: w&nbsp;folderze z&nbsp;programami raczej bezpośrednio wołanymi przez system. W&nbsp;folderach wewnętrznych Pythona, jak `/lib/python3`, znajdziemy ich nieporównywalnie więcej. Widać, że ma spory wpływ na system."
%}

Python pozwala modułom instalowanym przez PIP-a na dość śmiałe ingerencje w&nbsp;swoje otoczenie. A&nbsp;że otoczeniem tym były pliki kluczowe dla systemu -- to trafiały się czasem piękne katastrofy.

Zdarzało się, że po instalacji zewnętrznych modułów Pythona [system przestał prawidłowo działać](https://peps.python.org/pep-0668/#references). Raporty o&nbsp;błędach spływały do ludzi, którzy nie ponosili winy za awarię (twórców Linuksów, ewentualnie Pythona). Robił się szum.

{:.post-meta .bigspace-after}
Od tamtego czasu spam raczej się pogorszył, bo ludzie wysyłają nieraz raporty automatycznie generowane przez Ej-Aj. Nie zmienia to faktu, że dawne zgłoszenia też irytowały.

Nic dziwnego, że niektórzy poprosili o&nbsp;możliwość **oznaczenia systemowego Pythona jako czegoś, co nie powinno być zmieniane**.  
Twórcy języka Python wyszli temu naprzeciw i&nbsp;dodali tryb „zarządzania zewnętrznego”, po którego włączeniu znikają niektóre możliwości ingerencji -- to [zmiana *PEP 668*](https://peps.python.org/pep-0668/) (o&nbsp;niemal diabelskim numerze!) wspomniana pod koniec komunikatu.

Ogólnie: rozumiem motywację i&nbsp;chęć ucięcia dawnego stanu rzeczy. Ale nie zmienia to faktu, że niejedna osoba trafiająca w&nbsp;internecie na porady i&nbsp;samouczki będzie się odbijała od nowego problemu. Jest ryzyko, że się zniechęci -- albo do Pythona, albo do Linuksa.

W tym momencie pojawia się Ciemna Strona, cała na biało :smile: Spróbuję poratować poradami tych, którzy zderzyli się z&nbsp;błędem. Nie odpuszczajcie, rozwiązania już nadchodzą!

## Sposoby na rozwiązanie problemu

Opiszę tu kilka rozwiązań:

* szybkie, proste i&nbsp;bezpieczne -- ale obejmujące tylko część modułów ([APT](#instalacja-przez-apt){:.internal}),
* szybkie i&nbsp;proste -- które czasem może jednak coś popsuć ([*break-system-packages*](#pip-zopcją-break-system-packages){:.internal}),
* bardziej wymagające, ale bezpieczne i&nbsp;uczące dobrych nawyków ([środowiska wirtualne](#instalacja-wśrodowisku-wirtualnym){:.internal}).

Na końcu będzie też o&nbsp;rozwiązaniu ręcznym, przez pełne obejście instalatorów -- ale to bardziej w&nbsp;ramach ciekawostki.

{:.post-meta .bigspace-after}
Na razie nie mam opisu instalacji przez PIPX, również proponowanej przez komunikat. Może go dodam, kiedy lepiej się oswoję z&nbsp;tym sposobem.

{% include info.html
type="Podstawy konsoli"
text="Żeby uruchomić konsolę na Mincie (i&nbsp;wielu Linuksach), można użyć kombinacji `Ctrl+Alt+T` albo kliknąć odpowiednią ikonkę.  
Żeby coś wkleić do konsoli, należy użyć kombinacji `Ctrl+Shift+V` (ew. kliknąć konsolę prawym przyciskiem myszy i&nbsp;wybrać opcję `Wklej`).  
Kiedy piszę o&nbsp;„uruchomieniu konsoli w&nbsp;folderze”, to można to zrobić przez graficzną przeglądarkę plików. Po przejściu do odpowiedniego folderu należy np. kliknąć opcję `Plik` z&nbsp;górnego paska, a&nbsp;potem `Otwórz w terminalu`."
%}

### Instalacja przez APT

Niektóre popularne pakiety Pythona zostały „przepakowane” do postaci pakietów DEB. Dzięki temu **można je instalować przez APT-a (systemowego menedżera pakietów)**. Tak jak wiele innych linuksowych programów.

{:.post-meta .bigspace-after}
Przypomnę uwagę z&nbsp;początku wpisu: APT jest obecny tylko na niektórych Linuksach, nie na wszystkich.

W tej nowej formie udostępniane są tak popularne pakiety jak: `matplotlib` (wykresy), `numpy` (obliczenia na macierzach), `pynput` (automatyzacja), `opencv` (przetwarzanie obrazów)...

Żeby sprawdzić, czy dany pakiet jest w&nbsp;bazie, najlepiej najpierw odświeżyć dostępne źródła:

<div class="black-bg mono">
sudo apt update
</div>

{:.figcaption}
Jak to przy komendzie `sudo` -- może poprosić o&nbsp;hasło.

Następnie można wyszukać w&nbsp;zasobach APT-a nazwy pakietów, przykładowo:

```
apt search matplotlib
```

Wyskoczy kilka wyników. Jak ustalić, którego z&nbsp;nich nam potrzeba?

Zazwyczaj **nazwy pakietów mają konkretny format: `python3-PAKIET`**, gdzie *PAKIET* to nazwa, pod jaką by się go instalowało w&nbsp;świecie Pythona.

W tym przypadku do szablonu pasuje pakiet o&nbsp;nazwie `python3-matplotlib`. Można go zainstalować:

```
sudo apt install python3-matplotlib
```

{:.post-meta .bigspace-after}
Podczas takiej instalacji -- jeśli poprzednio coś instalowaliśmy i&nbsp;nie pykło -- może się pojawić [dość rzadki błąd *Unmet dependencies*](/tutorials/linux-blad-package-system-is-broken){:.internal}. Pod linkiem mój krótki przewodnik po rozwiązaniu tego problemu.

Efektem działań będzie zainstalowanie pakietu na naszym systemie. Można go od teraz importować wewnątrz różnych skryptów Pythona, a&nbsp;także (jeśli wspiera takie coś) wołać go przez konsolę.

Sposób dotyczy jednak tylko niektórych pakietów, które ekipa od APT-a uznała za godne publikacji. Większość modułów (jak znany `torch`, czyli *Pytorch*, od uczenia maszynowego) nie jest w&nbsp;taki sposób udostępnianych.

{% include info.html
type="Krótko"
text="Tej metody instalacji warto użyć, gdy chcemy po prostu któregoś z&nbsp;najpopularniejszych pakietów Pythona.  
O ile są w&nbsp;bazie (i&nbsp;odpowiadają nam ich wersje), to zainstalujemy je szybko i&nbsp;równie prosto jak dawniej, przez samo `pip install`."
%}

{% include details.html summary="Bonus: instalacja offline" %}

{:.bigspace-before}
Jeśli ktoś nie chce za każdym razem łączyć się z&nbsp;internetem, żeby pobierać moduły Pythona, to można je pobrać tylko raz, na początku, a&nbsp;potem nosić ze sobą jako pakiety DEB i&nbsp;instalować w&nbsp;razie potrzeby. Bez żadnego internetu.

Najpierw należy zmienić polecenie instalujące na pobierające:

```
apt download python3-MODUŁ
```

Pobierze się zestaw plików DEB (gdyby zapisało jako archiwum, to można je rozpakować i&nbsp;wyjąć z&nbsp;niego DEB-y).

Następnie, w&nbsp;**fazie instalacji**, należy skopiować te pliki do jakiegoś folderu na Linuksie, na którym chcemy je instalować, po czym użyć w&nbsp;tym folderze polecenia:

```
sudo dpkg -i python3*.deb
```

Efekt końcowy powinien być taki sam, jak bezpośrednia instalacja przez APT-a.

{% include details-end.html %}

### PIP z&nbsp;opcją *break-system-packages*

Długi komunikat o&nbsp;błędzie zawiera w&nbsp;dolnej części pewną propozycję, obwarowaną ostrzeżeniami:

> You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages

*Passing* oznacza tutaj przekazanie (argumentu). Po ludzku: **jeśli dopisze się do komendy instalującej `--break-system-packages`, to zadziała jak dawniej**.

Angielska nazwa wydaje się sugerować, że wykonanie takiego polecenia *zawsze* popsuje systemowe pakiety. Oczywiście to tylko straszak.  
Co w&nbsp;końcu mógłby popsuć jednoplikowy skrypt, którego „instalacja” polega tylko na włożeniu go do folderu Pythona, żeby był dostępny dla innych?

Gdyby ktoś chciał instalować w&nbsp;tym trybie, to należy najpierw zainstalować PIP-a (którego domyślnie nie ma na Mincie):

```
apt install python3-pip
```

Mając PIP-a, można używać polecenia:

```
pip3 install PAKIET --break-system-packages
```

Gdybym chciał się bawić w&nbsp;moralizatora, to bym mówił: „nie róbcie tego! To ryzyko! Środowiska wirtualne jedyną właściwą drogą”.

...Ale wiem jak jest. Środowiska wirtualne dokładają kroków i&nbsp;mogą irytować, gdy chce się użyć na próbę dosłownie jednego, prostego, cudzego skryptu.  
Proponuję kompromis. Używajmy tej metody wtedy, kiedy:

* modułu, który chcemy zainstalować, nie ma w&nbsp;bazie APT,
* do zainstalowania jest jedynie prosty moduł Pythona,
* obiecujemy sobie nie zawracać głowy twórcom naszego Linuksa, jeśli pojawią się dziwne problemy  
  (albo przynajmniej: przed zawaracaniem sprawdzić na czystym Linuksie z&nbsp;pendrive'a, czy tam również występują).

{% include info.html
type="Krótko"
text="Tej metody mogą użyć osoby, które chcą pobrać lekki skrypt (np. `pyperclip` od obsługi schowka) z&nbsp;taką samą łatwością jak w&nbsp;dawnych czasach.  
Jednocześnie upewniły się, że skrypt podczas instalacji nie grzebie w&nbsp;systemowym Pythonie i&nbsp;nie ma opcji niczego popsuć (doceniam wnikliwość).  
Albo po prostu lubią ryzyko (też doceniam) :smiling_imp:"
%}

### Instalacja w&nbsp;środowisku wirtualnym

Środowisko wirtualne Pythona (nie mylić z&nbsp;maszyną wirtualną, choćby taką o&nbsp;[zastosowaniach prywatnościowych](/2025/02/10/prywatnosc-maszyny-wirtualne){:.internal}) ma dwojakie oblicze:

* od strony systemu: **to odrębny folder z&nbsp;kopiami podstawowych programów Pythona**;
* od strony działania: to osobna przestrzeń na pliki Pythona, niewchodząca w&nbsp;drogę wersji systemowej.

  Osobny, zamykany pokój dla dzieciaków :wink: W&nbsp;to miejsce najchętniej „wypchnęliby” nas opiekunowie Linuksa, żebyśmy nie rozbili podczas zabaw wazonów z&nbsp;przedpokoju.

Żeby *stworzyć* środowisko, trzeba uruchomić konsolę w&nbsp;jakimś folderze (najlepiej łatwo dostępnym, bo może być często odwiedzany) i&nbsp;wpisać:

```
python3 -m venv ŚRODOWISKO
```

{% include details.html summary="Co zrobić, jeśli po tej komendzie wyskoczy błąd" %}

{:.bigspace-before}
Może się zdarzyć -- przynajmniej na czystym Mincie -- że po użyciu cytowanego wyżej polecenia ukaże się taki komunikat:

<div class="black-bg mono post-meta bigspace">
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.
</div>

Wynika z&nbsp;tego, że moduł `venv` (choć działa) nie ma na początku wszystkich rzeczy potrzebnych do stworzenia środowiska. Należy je sobie zainstalować:

<div class="black-bg mono nospace">
sudo apt install python3-venv
</div>

{:.figcaption .nospace}
**Uwaga:** przypominam, że APT to instalator dla Minta i&nbsp;innych systemów „debianowatych”; na innych Linuksach mógłby być inny komunikat.

{% include details-end.html %}

`ŚRODOWISKO` to tutaj nazwa środowiska. Całkiem subiektywna, choć warto ustawić coś względnie krótkiego i&nbsp;niewywołującego ciarek żenady (nazwa domyślnie będzie widoczna w&nbsp;każdej linijce konsoli).

Po wykonaniu polecenia powstanie wspomniany folder ze środowiskiem wirtualnym -- układ folderów i&nbsp;programów skopiowanych od systemowego Pythona.  
Wśród tych programów jest jeden specjalny, o&nbsp;nazwie `activate`, który aktywuje całe środowisko. Można go sobie uruchomić:

```
source ŚRODOWISKO/bin/activate
```

{:.bigspace}
<img src="/assets/tutorials/python-externally-managed-environment/venv-tworzenie-aktywacja.png" alt="Kolaż ze zrzutów ekranu, pokazujący wpisane w&nbsp;konsoli polecenie tworzące środowisko, następnie wygląd stworzonego folderu, potem polecenie aktywujące środowisko, a&nbsp;na koniec wygląd pola konsoli po jego aktywacji."/>

Zobaczymy, że wygląd konsoli się zmieni -- na początku linijki, w&nbsp;nawiasie, pojawi się nazwa naszego środowiska.  
W tym trybie **wszystkie pliki instalowane przez PIP-a będą trafiały do folderów środowiska, a&nbsp;nie do systemowych**. No i, co istotne -- PIP zacznie działać bez przeszkód!

Pewną wadą środowiska jest to, że trzeba sobie zapamiętać, gdzie się je stworzyło, i&nbsp;każdorazowo je aktywować, żeby sięgać do zebranych tam skryptów.  
Wymaga to pewnej zmiany przyzwyczajeń... Ale myślę, że da się przywyknąć.

Co do sposobu stosowania -- teoretycznie tym „właściwym” byłoby robienie osobnego środowiska na każdy projekt. Ale jeśli ktoś się uprze, to może po prostu stworzyć je raz, a&nbsp;potem wrzucić do systemowych programów wygodne skróty od jego obsługi.

{:.post-meta .bigspace-after}
Pomysł: alias `vpip PAKIET` -- aktywacja środowiska + instalacja wskazanego pakietu przez PIP-a.

W ten sposób miałoby się na systemie dwa Pythony: systemowy, którego zostawia się w&nbsp;spokoju, oraz własny -- nasz osobisty plac zabaw.

{% include info.html
type="Krótko"
text="Środowiska wirtualne to „ta właściwa” metoda, zalecana przez mędrców Pythona.  
Dla osób nieprzyzwyczajonych może być z&nbsp;początku dziwna, bo wymaga więcej konsoli i&nbsp;dodatkowych krokow. Ale na dłuższą metę daje gwarancję, że świat systemowego Pythona nigdy nie zderzy się z&nbsp;tym bardziej chaotycznym, w&nbsp;którym sobie eksperymentujemy ze skryptami."
%}

## Bonus: rozwiązanie ręczne

W przypadku Pythona „instalacja” może oznaczać wiele rzeczy. Przy prostych modułach bywa po prostu **umieszczeniem plików w&nbsp;ogólnodostępnej przestrzeni Pythona**.

Weźmy taki przydatny [moduł `mss`](https://github.com/BoboTiG/python-mss) (skrót od *Multiple ScreenShots*) od robienia zrzutów ekranu. Nie ma go w&nbsp;bazie APT-a, dla niektórych byłby zbyt lekki na osobne środowisko wirtualne, a&nbsp;instalacja siłowa jednak nieco odstrasza.

Istnieje czwarty sposób -- zdobycie jego kodu z&nbsp;pominięciem instalatorów.

Najpierw należy znaleźć moduł [na stronie PyPI](https://pypi.org/project/mss/#files) i&nbsp;przejść tam do zakładki `Download files` z&nbsp;plikami do pobrania. Pod nagłówkiem *Built Distribution*, na dole, znajdują się pliki WHL (w&nbsp;tym wypadku tylko jeden). Po kliknięciu nazwy plik pobierze się na komputer.

Gdybyśmy go spróbowali zainstalować przez PIP, to nadal wyskakiwałby błąd. Można jednak kliknąć go prawym przyciskiem myszy i&nbsp;rozpakować jak zwykłe archiwum ZIP (gdyby nie było widać takiej opcji, to można najpierw zmienić końcówkę pliku na `.zip`).

Po rozpakowaniu ukażą się dwa foldery. Jeden ma w&nbsp;nazwie `dist-info`, a&nbsp;drugi nazywa się po prostu `mss`. To on nas interesuje -- jest **samowystarczalnym modułem** i&nbsp;znajdują się w&nbsp;nim już wszystkie pliki potrzebne do działania.

Oficjalna instalacja obejmowałaby,  poza rozpakowaniem, umieszczenie tego folderu w&nbsp;odpowiednim miejscu. Można je znaleźć na własną rękę. W&nbsp;ustaleniu, gdzie Python trzyma swoje pliki, pomoże takie polecenie:

```
python3 -m site
```

Wyświetli się kilka ścieżek, jedna pod drugą. Każda z&nbsp;nich to dla Pythona **folder szybkiego dostępu**. Jeśli wrzuci się nasz folder/moduł `mss` do dowolnego z&nbsp;nich, to Python zawsze go znajdzie.

{% include info.html
type="Powiązane wpisy"
text="Opisałem kiedyś, w&nbsp;jaki sposób można [stworzyć własny folder na skrypty Pythona](/tutorials/using-python){:.internal}, a&nbsp;następnie dodać go do listy szybkiego dostępu.  
Może to być dobre rozwiązanie dla osób, które nie chcą, żeby skrypty pobierane z&nbsp;zewnątrz wymieszały się z&nbsp;ich własnymi wynalazkami."
%}

Kiedy skopiujemy nasz folder `mss` do któregoś z&nbsp;wymienionych folderów (polecam ten kończący się na `site-packages`, o&nbsp;ile istnieje), to zyskamy możliwość importowania zawartych tam rzeczy przez systemowego Pythona:

{:.bigspace-before}
<img src="/assets/tutorials/python-externally-managed-environment/python-mss-konsola.png" alt="Zrzut ekranu z&nbsp;konsoli, pokazujący najpierw aktywowanie Pythona, potem importowanie wewnątrz niego modułu MSS. Na koniec widać ścieżkę do folderu site-packages, w&nbsp;którym moduł się znajduje."/>

{:.figcaption}
Kolorem żółtym oznaczyłem rzeczy, które osobiście wpisałem w&nbsp;konsolę. Reszta tekstu -- w&nbsp;tym ścieżka, do której wrzuciłem moduł -- to rzeczy, które się wyświetliły.

**Rozwiązanie ma oczywiście wiele ograniczeń**. Istnieją moduły, których instalacja polega na rzeczach znacznie bardziej złożonych niż skopiowanie folderu w&nbsp;inne miejsce.

Nawet moduł MSS z&nbsp;naszego przykładu, „zainstalowany” taką metodą, nie miałby pełni funkcji. Brakowałoby [skryptu-uruchamiacza](/2024/03/05/python-skrypty-startowe){:.internal}, który powinien się znaleźć w&nbsp;systemowym folderze szybkiego dostępu (jak `/usr/bin`) i&nbsp;pozwalałby przywoływać moduł z&nbsp;dowolnego miejsca, krótką komendą `mss`.

Tym niemniej: jeśli komuś po prostu zależy na dostępie do prostego kodu, a&nbsp;grzęźnie na instalatorach, to warto wiedzieć, że czasem istnieje droga na skróty. Wiele sprowadza się do położenia odpowiednich plików w&nbsp;odpowiednich miejscach.

Na tym kończę dzisiejszy wpis. Mam nadzieję, że opisany tu błąd PIP-a uda się łatwo pokonać albo obejść którąś z&nbsp;kilku pokazanych tu metod :smile:

