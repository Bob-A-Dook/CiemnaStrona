---
layout: page
title: "Linux Mint i brakujące znaki z azjatyckich czcionek" 
description: "Tofu jest fu, a kanji jest mniam."
---

W tym miniwpisie opiszę problem z&nbsp;azjatyckimi znakami, jaki mi się przytrafił na systemie Linux Mint (dokładniej: edycja Mate, wersja 22.1). Obstawiam jednak, że ma proste przełożenie na inne Linuksy oraz inne przypadki, gdy nie wyświetlają się niektóre znaki.

Opisuję tu całą ścieżkę od zauważenia problemu do jego rozwiązania, po drodze dzieląc się paroma codziennymi konsolowymi sztuczkami.  
Jeśli ktoś nie ma cierpliwości, to może od razu przeskoczyć na koniec, do [rozwiązania](#podsumowanie){:.internal}.

{:.post-meta}
Spoiler: rozwiązaniem problemu było u&nbsp;mnie polecenie konsolowe `fc-cache -f -v`, odświeżające powiązania między czcionkami a&nbsp;językami.

## Zarys problemu

Pewnego dnia w&nbsp;przeglądarce Firefox przestały mi się wyświetlać znaki japońskiego alfabetu (*kanji* i&nbsp;nie tylko). Zamiast nich widać było prostokąty wypełnione cyframi -- tak zwane [*tofu*](https://english.stackexchange.com/questions/296505/where-is-tofu-for-font-fallback-box-glyph-coming-from), znaki zastępcze.  
Po pewnym czasie odkryłem, że problem dotykał również zwykłych plików tekstowych oraz nazw plików wyświetlanych w&nbsp;domyślnym „Eksploratorze”.

Nie chodzę po stronach azjatyckich, ale brak znaków utrudniałby mi życie. Nie widziałbym, czy ktoś pisze w&nbsp;komentarzach *arigato* czy *bakayaro*. No i&nbsp;tekstowe wzruszenia ramion nie były już jak dawniej:

{:.bigspace-before}
<img src="/assets/posts/open_source/linux_problemy/cjk-czcionki-tofu.png" alt="Zrzuty ekranu pokazujące przykłady brakujących azjatyckich znaków: raz w&nbsp;tekstowej reakcji na forum, dwa razy w&nbsp;nazwie pliku" width="100%"/>

{:.figcaption}
Brakujące znaki kolejno w: przeglądarce internetowej, przeglądarce plików, prostym edytorze tekstu.

Przyczyny problemu nie znałem. W&nbsp;tamtym czasie testowałem różne warianty Linuksa, więc było sporo instalowania i&nbsp;eksploracji. Może któryś z&nbsp;pakietów podczas instalacji przenosił czcionki w&nbsp;inne, tymczasowe miejsce? A&nbsp;mnie instalacja przerwała się w&nbsp;połowie, przez co nigdy nie wróciły ze swojego czyśćca? Nie wiem, mogę tylko gdybać.

W każdym razie: sam to na siebie sprowadziłem, a&nbsp;**większość użytkowników Linuksa nie zetknie się z&nbsp;tym problemem**. System będzie im śmigał, wyświetlając informacje we wszystkich językach świata.  
...Ale gdyby ktoś przypadkiem dołączył do grona nieszczęśliwców, to zapraszam na spacer w&nbsp;stronę rozwiązania problemu.

## Szukanie przyczyny

Chcąc odzyskać swoje kochane hieroglify, musiałem od czegoś zacząć.

Pierwsze założenie: **jeśli problem dotyczy wielu programów naraz, to zapewne wiąże się z&nbsp;czymś systemowym**.

Na systemie Linux czcionki działają na szczęście w&nbsp;bardzo prosty sposób -- umieszcza się je w&nbsp;paru specjalnych folderach, znanych systemowi. Na moim Mincie to `/usr/share/fonts` i&nbsp;jego podfoldery.

System sięga sobie do tych folderów, kiedy pojawia się taka potrzeba (np. napotka w&nbsp;danych nowy znak i&nbsp;musi go wyświetlić). Jeśli nie znajdzie jakiegoś znaku, to wyświetla zamiast niego znak zastępczy, czyli właśnie wspomniane *tofu*. Prostokąt z&nbsp;liczbami.

Wiedząc o&nbsp;tym i&nbsp;widząc, że reszta znaków działa, mogłem przyjąć założenie drugie -- brakuje mi jakiejś czcionki. Mówiąc dokładniej: **brakuje mi czcionek azjatyckich**. Sprawdziłem to, wchodząc sobie na koreańską Wikipedię i&nbsp;widząc więcej *tofu*.

Czcionki azjatyckie to w&nbsp;oficjalnym nazewnictwie *CJK fonts* (skrót od Chinese, Japanese, Korean). Zawsze miałbym jakiś punkt wyjścia do szukania w&nbsp;internecie: `linux mint cjk fonts not showing`. Na którymś forum znalazłbym zapewne polecenie instalujące, a&nbsp;po jego wykonaniu zdobyłbym brakujące czcionki -- choć niekoniecznie te co wcześniej.

Zamiast tego postanowiłem jednak działać metodycznie i&nbsp;sprawdzić, czego dokładnie mi brakowało. Część niżej jest nieobowiązkowa, jeśli panicznie boicie się konsoli. Mimo to zachęcam, bo pokazuje, w&nbsp;jaki sposób można rozwiązać krok po kroku swoje problemy.

### Porównanie stanu między systemami

Na początku czcionki mi działały, dopiero po drodze coś się zepsuło. Wiedząc o&nbsp;tym, mogłem założyć że **system czysty i&nbsp;nowy powinien zawierać prawidłowe wersje czcionek i&nbsp;ustawień**. Można podejrzeć, czym się różni od mojego wadliwego.

Miałem nadal na pendrivie plik ISO, którego użyłem podczas instalacji. Ten sam system, ta sama wersja -- idealnie! Jak grupa kontrolna w&nbsp;badaniach naukowych.
 
Włożyłem tego pendrive'a do portu USB, nacisnąłem odpowiednią kombinację klawiszy (u&nbsp;mnie `F12` tuż po wciśnięciu przycisku zasilania) i&nbsp;wybrałem opcję uruchomienia systemu z&nbsp;pendrive'a.  
Włączył się w&nbsp;tak zwanym trybie *live*. Mogłem sobie majsterkować bez zobowiązań, podczas gdy mój główny system „spał” sobie na dysku, nieruszany przez nikogo.

{% include info.html
type="Wątek poboczny"
text="Instalowanie Linuksów jeszcze kiedyś opiszę, ale zostawię tu streszczenie dla chętnych: pobieram plik ISO z&nbsp;wybranym Linuksem ze strony projektu oraz program Ventoy, szykuję też pustego pendrive'a.  
Uruchamiam Ventoya i&nbsp;wskazuję mu pendrive'a, zmieniając go w&nbsp;wielkiego instalatora LInuksów. Potem po prostu kopiuję na tego pendrive'a plik ISO. Lub więcej plików, jeśli chcę testować.  
Najtrudniejsza część to wejście w&nbsp;menu uruchamiania (*bootowania*), bo różni się ono między producentami i&nbsp;modelami komputerów."
%}

### Brakujące pliki?

Mając czysty system pod ręką, mogłem sprawdzić obecne na nim czcionki. Choćby przez wypisanie wszystkich plików zawartych w&nbsp;oficjalnym folderze czcionkowym `/usr/share/fonts` i&nbsp;jego podfolderach:

```
find /usr/share/fonts
```

To polecenie wypisuje listę plików i&nbsp;folderów. Domyślnie wyświetla się ona tylko w&nbsp;konsoli. Żeby zamiast tego zapisać ją do pliku, mogłem użyć operatora strzałki:

<pre class="black-bg mono nospace">
find /usr/share/fonts > czcionki-czysty-system.txt
</pre>

{:.figcaption}
Nazwa pliku całkiem dowolna, wybrana subiektywnie przeze mnie.

Po uzyskaniu listy z&nbsp;czystego systemu mogłem ją sobie zgrać na pendrive'a, wyłączyć komputer i&nbsp;uruchomić swój używany system. Powtórzyłem na nim polecenie, tym razem zapisując pliki do `czcionki-uzywany-system.txt`.

Do wyłapania różnicy między plikami użyłem własnego skryptu Pythona, ale równie dobrze mógłbym użyć wbudowanego programu:

```
diff PLIK1 PLIK2
```

Miałem nadzieję, że okaże się po prostu, że gdzieś mi wcięło pliki, i&nbsp;że skończy się na ich kopiowaniu z&nbsp;systemu czystego do „nieczystego”.

...Okazuje się jednak, że było inaczej. System używany miał wszystkie te pliki, co nowy, plus jeszcze trochę dodatkowych. W&nbsp;tym na przykład czcionkę o&nbsp;wdzięcznej nazwie *Lato*.

Problem tkwił w&nbsp;czymś więcej niż pliki. Musiałem przyjrzeć się sposobowi, w&nbsp;jaki system je ładuje.

{% include details.html summary="Sposób na ustalenie konkretnej ładowanej czcionki (strace)" %}

{:.bigspace-before}
Linux daje również możliwość użycia przydatnego programiku `strace`, monitorującego wszystkie interakcje z&nbsp;systemem. W&nbsp;tym otwieranie plików i&nbsp;ładowanie ich zawartości, co może się idealnie przydać w&nbsp;naszym przypadku.

Zarys planu? Mogę monitorować `strace`'em, jak otwieram plik zawierający obcojęzyczne znaki. Zobaczyć, co ładuje na sprawnym systemie, a&nbsp;co na niesprawnym.

Ze względu na prostotę wybrałem w&nbsp;roli tego programu edytor tekstu, odpowiednik Notatnika z&nbsp;Windowsa.  
Naszykowałem plik z&nbsp;kilkoma znakami japońskimi, które na czystym systemie są widoczne, a&nbsp;na używanym zmieniają się w&nbsp;*tofu* (to ten plik ze zrzutu ekranu na początku wpisu).

Programik `strace` wymaga pracy w&nbsp;konsoli, więc musiałem ustalić, jakie konsolowe polecenie odpowiada mojemu „Notatnikowi”. Najpierw uruchomiłem go klasycznie, kliknąłem w&nbsp;informacje, ustaliłem że jego nazwa to **Xed**.  
Na Linuksie nazwa konsolowa zwykle odpowiada oficjalnej, więc sprawdziłem, czy polecenie `xed` go uruchamia. Tak było.

Otwieranie pliku przez `xed`a jest bardzo proste: `xed PLIK`.  
Z kolei zapisywanie wyników `strace`'a do pliku wyjściowego, żeby móc je sobie potem porównać między systemami, wymaga podania argumentu `-o PLIK_WYJŚCIOWY`.

Łącząc to w&nbsp;całość, skleciłem ostateczne polecenie:

<pre class="black-bg mono nospace">
strace -o <span class="red">czysty-system-strace.txt</span> xed <span class="red">PLIK_Z_KANJI.txt</span>
</pre>

{:.figcaption}
Nazwy plików, wyróżnione na czerwono, jak zwykle dowolne i&nbsp;dobrane subiektywnie.

Poczekałem, aż plik się wczyta. Azjatyckie znaki działały na świeżym systemie jak marzenie. Zamknąłem edytor, pozostając z&nbsp;zapisaną pełną historią interakcji z&nbsp;systemem.  
Przeszukałem ją niezawodnym programem `grep`, wypatrując słowa *font*, bo wiedziałem, że powinno odpowiadać ścieżkom do czcionek:

<pre class="black-bg mono">
grep "font" <span class="red">czysty-system-strace.txt</span>
</pre>

Wyniki (nieco oczyszczone, żeby zostawić tylko przypadki otwarcia plików, bez duplikatów):

```
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libfontconfig.so.1", O_RDONLY|O_CLOEXEC)
openat(AT_FDCWD, "/usr/share/fonts/truetype/ubuntu/Ubuntu[wdth,wght].ttf", O_RDONLY)
openat(AT_FDCWD, "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", O_RDONLY)
openat(AT_FDCWD, "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", O_RDONLY)
```

Ostatnia linijka pokazuje mi, skąd załadował znaki bezproblemowy „czysty” system -- z&nbsp;pliku `/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc`, gdzie Noto to nazwa czcionki, zaś CJK ujawnia jej azjatycką naturę.

...Tyle że, jak wspomniałem, brak pliku nie był tu problemem i&nbsp;miałem go na obu systemach. Gdybym natomiast znalazł się w&nbsp;sytuacji, gdy szukam konkretnej rzeczy, to `strace` i&nbsp;patrzenie na otwierane pliki byłoby sensownym podejściem.

{% include details-end.html %}

### Brakujące przyporządkowania

Skoro problem nie tkwił w&nbsp;brakujących plikach, to w&nbsp;czym? Logika podpowiada, że system mógłby mieć jakąś swoją wewnętrzną regułę. Coś w&nbsp;stylu: „znak azjatycki? To muszę sięgnąć do pliku X”.

Pomogła mi tu odrobina wiedzy nagromadzona w&nbsp;innych przypadkach. Takie powiązanie między jedną rzeczą (językiem) a&nbsp;drugą (plikami zawierającymi czcionki) po angielsku nazywa się często *mapping*.

Odrobina szukania pod hasłami `linux showing system font mapping` itp. pokazała, że od zaglądania w&nbsp;czcionki system ma swój program `fc-list` (skrót od *fontconfig*).  
A zatem jak wcześniej -- uruchomiłem czysty system i&nbsp;użyłem polecenia zapisującego listę znanych rzeczy do pliku:

<div class="black-bg mono">
fc-list > czysty-system-fclist.txt
</div>

Potem to samo powtórzyłem na systemie z&nbsp;czcionkowym problemem.  
Miałem teraz dwie listy czcionek. Patrząc na różnice między nimi, mogłem ustalić, co się zmieniło. Zamiast robić pełną wizualizację różnic, użyłem na początku programiku `grep`, szukając słowa `CJK`, często obecnego w&nbsp;nazwach czcionek:

```
grep "CJK" czysty-system-fclist.txt
```

Zwróciło kilkadziesiąt wyników dla systemu czystego i&nbsp;sprawnego. Kilkadziesiąt powiązań między językiem a&nbsp;czcionką, tak jak być powinno.

A kiedy wykonałem to samo polecenie dla systemu problematycznego... Nie wyświetliło niczego. Wprawdzie system używany miał parę powiązań, których brakowało czystemu (np. do wspomnianej wyżej czcionki Lato), ale pod względem czcionek azjatyckich zostawał w&nbsp;tyle.

Miałem prawdopodobną przyczynę -- **na moim używanym systemie brakowało przyporządkowań językowo-plikowych, które miał system czysty**.

Patrząc pod hasłami `linux fixing font mapping` i&nbsp;zbliżonymi, znalazłem przypadkiem ciekawe polecenie. Analizuje ono pliki umieszczone w&nbsp;folderach czcionkowych, patrzy jakim logicznym znakom odpowiadają i&nbsp;zapisuje te informacje.  
To tak zwana *pamięć (podręczna) czcionek*. Po angielsku *font cache*. A&nbsp;polecenie to:

```
fc-cache -f -v
```

Użyłem tego polecenia, po czym ponownie sprawdziłem przez `fc-list`, jakie mam przyporządkowania. Pojawiły się te brakujące względem czystego systemu!

W przeglądarce plików nie od razu się poprawiło, musiałem uruchomić ponownie komputer. Natomiast Firefox po odświeżeniu zaczął wyświetlać brakujące znaki :smile:

Skąd się wziął cały problem? Nie wiem. Ale od teraz mogę przynajmniej zilustrować tę niewiedzę pełnoprawną reakcją bez *tofu*:

{:.bigspace-before}
<img src="/assets/posts/open_source/linux_problemy/wzruszenie-ramion-azjatycki-znak.png" alt="Ludek wzruszający ramionami ułożony z&nbsp;prostych znaków. Jego oczy i&nbsp;usta tworzy znak japońskiego alfabetu, który wcześniej się nie wyświetlał" width="200px"/>

## Podsumowanie

W tym miejscu kończę część eksploracyjną i&nbsp;podsumowuję rozwiązania problemu z&nbsp;azjatyckimi czcionkami.  
Zaczynając od rozwiązań najprostszych:

* Aktualizacja powiązań między znakami logicznymi a&nbsp;graficznymi.

  Trzeba otworzyć konsolę, wpisać w&nbsp;nią `fc-cache -f -v` i&nbsp;nacisnąć *Enter*. Jeśli przyczyną nie był brak plików, tylko brak powiązań, to w&nbsp;tym momencie powinno się naprawić. Jak u&nbsp;mnie.

* Zainstalowanie innego pakietu czcionek.

  Jeśli przyczyną problemu jest brak plików z&nbsp;czcionkami, to trzeba je pozyskać. Można to zrobić zarówno przez interfejs graficzny (na Mincie: menu w&nbsp;dolnym rogu, `Menedżer oprogramowania`), jak i&nbsp;konsolę -- np. wpisać

  ```
  sudo apt-get install ttf-mscorefonts-installer
  ```
  
  żeby zainstalować czcionki Microsoftu. Po instalacji tym sposobem powinny automatycznie powstać potrzebne powiązania.

  {:.post-meta .bigspace-after}
  Uwaga: po użyciu polecenia wyświetli się tekst licencji do zaakceptowania. Należy nacisnąć strzałkę w&nbsp;bok, żeby zaznaczyło opcję `OK`, a&nbsp;potem *Enter*, podobnie na kolejnym ekranie.

  Rozwiązanie szybkie i&nbsp;kompletne, jeśli chcemy po prostu widzieć brakujące znaki. Ale niewystarczające, jeśli zależy nam na konkretnej czcionce.

* Ręczna instalacja konkretnej czcionki.

  Jeśli wiemy, czego nam brakuje, to trzeba zdobyć plik z&nbsp;czcionką z&nbsp;jakiegoś źródła, zapewne internetu. Potem należy go umieścić w&nbsp;odpowiednim folderze (co będzie wymagało uprawnień administratora). A&nbsp;na koniec: odświeżyć pamięć czcionek, poleceniem `fc-cache -f -v`, jak parę punktów wyżej.

  {:.post-meta .bigspace-after}
  Ta część jest ogólnikowa, bo nie miałem okazji tego testować w&nbsp;praktyce.

* Ponowna instalacja systemu.

  Opcja nuklearna, ale pozwala przywrócić system do początkowego stanu. Może się przydać, gdyby się okazało, że za bardzo nabroiliśmy i&nbsp;problem jest większy niż jakiś brak czcionek. To zwykle prowadzi do usunięcia plików, więc należy najpierw je zgrać w&nbsp;bezpieczne miejsce.

### Na przyszłość

Rozwiązałem problem, ale nie ustaliłem jego źródła -- to mogłoby być zadanie na przyszłość.

Linux daje wiele możliwości kontrolowania swojego systemu. Załóżmy, że przyczyną mojego problemu był jakiś program zbyt śmiało ingerujący w&nbsp;pamięć czcionek.  
W takim wypadku pomógłby cyfrowy odpowiednik „fotokomórki” wyłapującej, kiedy jakiś program próbuje mi tam grzebać. Po wykryciu prób ingerencji mógłbym je blokować albo przynajmniej zapisywać, żeby ustalić winnych.

Ale póki co, nie widząc łatwego sposobu na odtworzenie błędu, umieszczę tu listę azjatyckich czcionek, jakie mi „wcięło” i&nbsp;jakich według `fc-list` nie miałem na używanym systemie. Może komuś to pomoże w&nbsp;przypadku napotkania podobnego błędu.

{% include details.html summary="Lista brakujących powiązań dla języków azjatyckich" %}
<pre class="black-bg mono">
/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc: Noto Serif CJK SC:style=Bold
/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc: Noto Serif CJK TC:style=Bold
/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc: Noto Serif CJK JP:style=Bold
/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc: Noto Serif CJK HK:style=Bold
/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc: Noto Serif CJK KR:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans CJK JP:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans CJK HK:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans CJK KR:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans CJK SC:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans CJK TC:style=Regular
/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc: Noto Serif CJK SC:style=Regular
/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc: Noto Serif CJK TC:style=Regular
/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc: Noto Serif CJK JP:style=Regular
/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc: Noto Serif CJK KR:style=Regular
/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc: Noto Serif CJK HK:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans Mono CJK TC:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans Mono CJK SC:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans Mono CJK KR:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans Mono CJK HK:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans Mono CJK JP:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans Mono CJK SC:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans Mono CJK TC:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans Mono CJK HK:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans Mono CJK KR:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc: Noto Sans Mono CJK JP:style=Regular
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans CJK JP:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans CJK KR:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans CJK HK:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans CJK TC:style=Bold
/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc: Noto Sans CJK SC:style=Bold
</pre>
{% include details-end.html %}

Tak działa świat otwartego źródła: ktoś zauważy problem, ktoś inny potwierdzi, ktoś nagłośni. Jakaś osoba wchodząca w&nbsp;świat programowania doda łatkę. O&nbsp;ile ktoś nie zrobi rewolucji i&nbsp;nie przepisze gruntownie swojego programu, to z&nbsp;każdą taką poprawką rzeczy działają coraz lepiej i&nbsp;stabilniej.

Dzięki tej współpracy świat *open source* może iść do przodu, być może [odbierając Windowsowi dotychczasowe bastiony](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}. Czemu bardzo kibicuję! :smile:

{% include info.html
type="Wątek prywatnościowy"
text="Strony internetowe mogą czasem zawierać elementy śledzące, [rozpoznające użytkowników po zestawie zainstalowanych czcionek](/internetowa_inwigilacja/2022/06/10/fingerprinting#czcionki){:.internal}.  
Patrząc na to w&nbsp;ten sposób, robienie co jakiś czas czystki i&nbsp;usuwanie czcionek poza domyślnymi, obecnymi na świeżym systemie, byłoby jak czyszczenie plików *cookies* albo historii przeglądania.  
Jeśli ktoś nie chce gmerać przy swoich czcionkach, ale myśli czasem o&nbsp;prywatności, to może w&nbsp;poważniejszych przypadkach korzystać z&nbsp;internetu przez [maszynę wirtualną](/2025/02/10/prywatnosc-maszyny-wirtualne){:.internal}."
%}
