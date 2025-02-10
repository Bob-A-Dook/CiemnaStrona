---
layout: post
title: "Python i zagadka szablonowych skryptów"
subtitle: "Odkrywam (od końca) niuanse instalowania modułów."
description: "Odkrywam (od końca) niuanse instalowania modułów."
date:   2024-03-05 14:00:00 +0100
tags: [Konsola, Podstawy, Python]
image:
  path: /assets/posts/open_source/python-skrypty-wejsciowe/skrypty-startowe-baner.jpg
  width: 1200
  height: 700
  alt: "Od ikony projektu YT DLP odchodzi strzałka w górę, do ikony Python Package Index. Stamtąd odchodzi kolejna strzałka, prowadząca do ikony laptopa."
---

Od jakiegoś czasu chciałem zrobić wpis **bardziej w&nbsp;stylu programistycznych blogów**, jakie chętnie czytam. Ale bez nurkowania w&nbsp;głębiny. Skupiający się zamiast tego na czymś podstawowym, co często bierze się za pewnik.  
Taki wpis, żeby była eksploracja. Radosne zaspokajanie ciekawości poznawczej. W&nbsp;stylu piosenkarki Björk [rozbierającej telewizor na części](https://www.youtube.com/watch?v=75WFTHpOw8Y).

Na początek pomyślałem, że zajrzę w&nbsp;bebechy programiku *yt-dlp*. Napisanego w&nbsp;języku Python, który najbardziej mi leży.

Ale ostatecznie wyszedłem poza ten konkretny program. Odciągnął mnie od niego ogólniejszy temat „skryptów wejściowych”. Tego, co pozwala wzywać programy konsolowe z&nbsp;dowolnej części systemu.

Odkryłem, jak wygląda ich droga od twórców do użytkowników. Przy okazji mogłem wprawić się w&nbsp;eksploracji z&nbsp;użyciem programów konsolowych.

Zapraszam! Znajomość Pythona nie jest konieczna, bo cała sprawa ma w&nbsp;sobie więcej z&nbsp;łamigłówki logicznej. Poza tym będę wszystko wyjaśniał. 

{% include info.html
type="Uwaga"
text="Pokazuję tu przykłady z&nbsp;aplikacji Termux na Androida oraz z&nbsp;domyślnej konsoli systemu Linux Mint. Na systemach z&nbsp;Windowsem (i&nbsp;być może MacOS, nie wiem) niektóre przykłady wpisywane w&nbsp;konsolę by nie zadziałały."
%}

## Spis treści

* [Początek: yt-dlp](#początek-yt-dlp)
  * [„Wołaj, a&nbsp;przybędę”](#wołaj-aprzybędę)
  * [Kulisy dostępności](#kulisy-dostępności)
  * [Znalezienie pliku](#znalezienie-pliku)
  * [Wnętrze pliku](#wnętrze-pliku)
* [Trendy wśród skryptów wejściowych](#trendy-wśród-skryptów-wejściowych)
  * [Różnice między skryptami](#różnice-między-skryptami)
  * [Zagadki linijki importującej](#zagadki-linijki-importującej)
  * [Zagadka znaku zapytania](#zagadka-znaku-zapytania)
* [Znalezienie części zmiennej](#znalezienie-części-zmiennej)
* [Znalezienie części szablonowej](#znalezienie-części-szablonowej)
  * [Stare szablony](#stare-szablony)
  * [Nowsze szablony](#nowsze-szablony)
  * [Podsumowanie wątku](#podsumowanie-wątku)
* [Od strony twórców](#od-strony-twórców)
* [Czego się nauczyłem](#czego-się-nauczyłem)

## Początek: yt-dlp

Wszystko zaczęło się od [*yt-dlp*](/tutorials/youtube-dl){:.internal}. To bardzo przydatny programik do pobierania multimediów z&nbsp;różnych stron (nie tylko z&nbsp;YouTube'a). Już nieraz się nad nim rozpływałem na tym blogu.

W pierwotnej postaci jest to **program konsolowy**. Używa się go przez wpisywanie konkretnych poleceń tekstowych w&nbsp;konsolę. Jakaś jest zwykle domyślnie zainstalowana na komputerach osobistych.

Analogia godna współczesności? Programy konsolowe są jak **ChatGPT bez lukru**.  
Zamiast pytań przyjmują polecenia. Zamiast kwieciście odpowiadać, robią dobrą robotę. Ewentualnie wprost piszą, że nas nie zrozumiały, zamiast zmyślać bzdurki.

Używając *yt-dlp*, można na przykład pobrać piosenkę z&nbsp;którejś ze wspieranych stron. Wystarczy skopiować link do niej i&nbsp;wpisać w&nbsp;konsolę:

```
yt-dlp -f bestaudio LINK
```

...A piosenka po chwili trafi na dysk. Albo na jego smartfonowy odpowiednik.

Smartfonowy, bo tego konkretnego programu można używać również [na smartfonach z&nbsp;systemem Android](/tutorials/yt-dlp-android){:.internal}. Najpierw pobiera się apkę Termux, przez nią język programowania Python, zaś przez narzędzia Pythona -- *yt-dlp*. Wszystko szybkie, zwięzłe i&nbsp;proste.

### „Wołaj, a&nbsp;przybędę”

W konsoli po lewej stronie zazwyczaj wyświetla się folder, w&nbsp;jakim obecnie jesteśmy (i&nbsp;tak, również tylda, `~`, to skrót odnoszący się do folderu. Domowego).

Po tych folderach można się poruszać. Wpisać na przykład polecenie `cd ŚCIEŻKA`, żeby przejść do folderu o&nbsp;podanej ścieżce (jeśli istnieje). Mikrociekawostka: *cd* to skrót od *change directory*.

W tym miejscu ukazuje się ciekawa właściwość *yt-dlp* wewnątrz Termuksa. Mianowicie: **w&nbsp;jakim folderze by się nie było, można przywołać ten program taką samą komendą**.

{:.bigspace-before}
<img src="/assets/posts/open_source/python-skrypty-wejsciowe/yt-dlp-termux-wywolywanie.jpg" alt="Dwa zrzuty ekranu pokazujące aplikację Termux i&nbsp;polecenie wywołujące yt-dlp przywołane z&nbsp;dwóch różnych folderów." width="50%"/>

{:.figcaption}
Konsola apki Termux. Na zielono ścieżki do folderów, w&nbsp;których akurat byłem.

W przypadku *yt-dlp* w&nbsp;Termuksie jest to o&nbsp;tyle istotne, że pobierane pliki będą zapisywane zawsze do tego folderu, w&nbsp;którym obecnie jesteśmy.  
Gdyby je pobierać do domyślnego folderu (który jest w&nbsp;*prywatnej części* Termuksa), to inne aplikacje, jak odtwarzacze multimediów, nie miałyby do nich dostępu.

Ale wracając do kwestii dostępności z&nbsp;każdego folderu -- ten ułatwiacz życia jest bardzo powszechny w&nbsp;świecie programów konsolowych. Jak to działa?

### Kulisy dostępności

Ogólnodostępność wynika z&nbsp;tego, że **wiele systemów ma swoje foldery specjalne, w&nbsp;których domyślnie wypatruje programów**.

Tak jak przeciętny obywatel wie, że najłatwiej znaleźć policjantów na komendzie, a&nbsp;lekarzy w&nbsp;szpitalu (choć oczywiście trafiają się też poza nim) -- tak samo konsola/Python wie, że swoich programów ma szukać w&nbsp;określonych folderach.

Żeby zobaczyć listę takich specjalnych lokalizacji, można wpisać w&nbsp;konsolę:

<div class="black-bg mono">
echo $PATH
</div>

Wyświetli się kilka ścieżek (na świeżym Termuksie -- jedna). Jeśli jest więcej, to będą **rozdzielane dwukropkami**.

Za każdym razem, kiedy wpisuje się proste konsolowe polecenie, dajmy na to zmyślone `abcd coś`, konsola rozbija je na spacjach. Następnie szuka we wspomnianych folderach specjalnych pliku o&nbsp;takiej samej nazwie jak pierwszy człon. Czyli w&nbsp;tym przypadku `abcd`.

Idąc tym tokiem rozumowania: wpisując *yt-dlp*, odnoszę się do jakiegoś pliku o&nbsp;takiej nazwie. I&nbsp;powinien być w&nbsp;tym jedynym folderze specjalnym, jaki mi pokazuje na Termuksie powyższe polecenie.

Ale to domysły. Jak sprawdzić to dokładniej: „*jaki* program odpowiada poleceniu *yt-dlp*?”. Albo, uogólniając: „jak poznać ścieżkę wołanego programu?”.

### Znalezienie pliku

Można zapytać internetów. Podczas wyszukiwania warto podać nazwę systemu, bo różnią się między sobą. Ja używałem Termuksa, ale wiem, że to konsola w&nbsp;stylu systemu Linux.  
Ostatecznie wpisałem w&nbsp;wyszukiwarkę DuckDuckGo: `linux checking program path`. I&nbsp;znalazłem [odpowiedź](https://superuser.com/questions/286147/find-out-path-of-program) z&nbsp;niezawodnego forum StackExchange.

Ludzie na forum napisali, że ścieżkę ujawni program konsolowy `which` albo `type`.  
Przy tym pierwszym Termux mówił, że nie jest zainstalowany (ale podpowiadał gotowe polecenie instalujące). Drugi od razu śmigał.

Po wpisaniu:

```
type yt-dlp
```

Wyświetliło mi pełną ścieżkę do pliku:

{:.figure .bigspace-before}
<img src="/assets/posts/open_source/python-skrypty-wejsciowe/termux-yt-dlp-path.jpg" alt="Pojedyncza ścieżka do pliku, która pojawia się po wpisaniy komendy type yt-dlp w&nbsp;Termuksa"/>

{:.figcaption}
Dla przypomnienia: tak to wygląda wewnątrz Termuksa, na komputerze byłaby inna ścieżka.  
Co ciekawe, `com.termux` to folder -- jeśli ktoś się przyzwyczaił, że kropki są tylko od rozszerzeń plików, to się może zaskoczyć.

### Wnętrze pliku

Znalazłem plik, pozostało do niego zajrzeć. Termux czy nie -- mogłem łatwo zaznaczyć ścieżkę i&nbsp;ją skopiować. Pozostało ją wrzucić do innego programu konsolowego, który odczyta plik. Wybrałem do tego `less`:

<pre class="black-bg mono with-next">
less ŚCIEŻKA_DO_PLIKU
</pre>

{:.figcaption}
Ogromna zaleta tego programu: wyświetla większe pliki „na raty”, kawałek po kawałku.  
W&nbsp;tym przypadku akurat mi to nie pomogło, bo plik był zwięzły.

{% include info.html
type="Porada"
text="Aby wyjść z&nbsp;programu `less`, wystarczy nacisnąć przycisk `Q` na klawiaturze. Dopóki tego nie odkryłem, pierwsze próby wyjścia były chaotyczne."
%}

Od tego miejsca będzie odrobina kodu. Ale właściwie nie trzeba nawet rozumieć, o&nbsp;co w&nbsp;nim chodzi, można potraktować całość jak logiczną łamigłówkę.

Okazuje się, że **plik o&nbsp;nazwie _yt-dlp_ (bez żadnego rozszerzenia) to skrypt Pythona**. To on się uruchamia, gdy wpisze się w&nbsp;konsolę *yt-dlp*. A&nbsp;oto cała jego zawartość:

```python
#!/data/data/com.termux/files/usr/bin/python3.11
# -*- coding: utf-8 -*-
import re
import sys
from yt_dlp import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```

Streszczając: ten skrypt to „uruchamiacz”. **Bierze (_importuje_) funkcję z&nbsp;jakiegoś innego skryptu, który nazywa się _yt\_dlp_. I&nbsp;ją aktywuje**.

A skąd Python wie, gdzie szukać tych pozostałych skryptów? No cóż, też ma swoje specjalne foldery. Analogiczne do tych systemowych, o&nbsp;których wcześniej wspomniałem.

{% include info.html
type="Nazewnictwo"
text="Gdy pojawiają się skrypty wołające inne skrypty, to łatwo się pogubić. Dlatego na czas reszty wpisu przyjmę pewną konwencję.  
Skrypty takie jak ten wyżej -- umieszczone w&nbsp;specjalnym folderze i&nbsp;uruchamiające coś innego -- będę nazywał *startowymi* albo *wejściowymi*. Te, które są przez nie wołane, będę z&nbsp;kolei nazywał *importowanymi*.  
Inne przydatne pojęcie to *moduł*. Tu: zestaw powiązanych ze sobą skryptów Pythona, często publikowanych jako całość."
%}

## Trendy wśród skryptów wejściowych

W tym momencie na pewien czas kończy się wątek konkretnego *yt-dlp*, a&nbsp;zaczyna ogólniejszy, związany ze skryptami Pythona.

Po poznaniu skryptu-uruchamiacza od *yt-dlp*, postanowiłem sprawdzić z&nbsp;ciekawości, jak wyglądają jego odpowiedniki dla innych modułów. W&nbsp;moim folderze szybkiego dostępu było bowiem więcej poinstalowanych skryptów.

Dla wygody użyłem oprócz Termuksa laptopa z&nbsp;lekko wiekowym systemem Linux Mint. Zerknąłem do folderu `.local/bin` w&nbsp;folderze domowym, który również jest folderem specjalnym na różne programy, przypisanym do konkretnego użytkownika.

{:.post-meta .bigspace-after}
Oprócz tego dałoby się również sprawdzić folder `/usr/bin`, na poziomie systemu, ale odpuściłem go sobie, bo był tam miks rzeczy pobranych i&nbsp;systemowych.

{% include info.html
type="Ciekawostka"
text="Słowo `bin` (które ciągle uparcie kojarzy mi się ze [śmietnikiem](https://www.diki.pl/slownik-angielskiego?q=bin)) to skrót od *binary*.  
Czasem określa się tak pliki nieczytelne dla człowieka, w&nbsp;odróżnieniu od tekstowych. A&nbsp;tymczasem większość plików, jakie znalazłem w&nbsp;tym folderze, zawierała wyłącznie czytelny tekst. Tak jakoś wyszło, że częściej pobieram skrypty.  
Ale w&nbsp;sumie za kulisami i&nbsp;tak każdy plik to zera i&nbsp;jedynki, więc nie będę się wykłócał :smile:"
%}

Wyświetliłem obok siebie treść kilku innych skryptów-uruchamiaczy. Skleconym na kolanie skryptem, ale równie dobrze mógłbym użyć (linuksowego odpowiednika) Notatnika.

Spodziewałem się pewnej różnorodności. Myślałem, że każda osoba publikująca swoje moduły Pythona tworzy również jakiś własny skrypt startowy. A&nbsp;tymczasem po sprawdzeniu innych skryptów odkryłem, że **wiele z&nbsp;nich było niemal identycznych**.

Rzuciło to nowe światło na całą sprawę. Przyszło mi na myśl, że skrypty są tworzone przez komputer, z&nbsp;jakiegoś szablonu.  
Żeby go poznać, postanowiłem porównać skrypty i&nbsp;spróbować w&nbsp;nich **wyróżnić części zmienne oraz niezmienne (szablonowe)**.

### Różnice między skryptami

Oto zawartość kilku wybranych skryptów startowych (można otworzyć w&nbsp;nowej karcie, żeby powiększyć):

{:.bigspace}
<img src="/assets/posts/open_source/python-skrypty-wejsciowe/moduly-skrypty-porownanie.jpg" alt="Zestawienie czterech skryptów Pythona, pochodzących z&nbsp;pakietów: yt-dlp, pip, mss oraz chardetect. Części powtarzalne w&nbsp;kolorze szarym, ważne różnice wyróżnione kolorem"/>

Najpierw odhaczę różnice, które uznałem za drobniejsze i&nbsp;zignorowałem, zostając przy istotniejszych:

* Różnice w&nbsp;liczbie pustych linijek.  
  Ta różnica jest ściśle skorelowana z&nbsp;inną, o&nbsp;której za moment.

* Różnice w&nbsp;linijce numer jeden.

  To ona mówi, jakiego Pythona użyć (a&nbsp;ściślej -- jakiego *interpretera*, programu odczytującego kod Pythona).  
  Inną miałem na Termuksie, inną na laptopie. Ale ogólnie: linijka zawsze wskazywała tego samego Pythona, którym zainstalowałem cały skrypt.

* Różnice w&nbsp;ostatniej linijce.

  Jej treść to `sys.exit(FUNKCJA())`, a&nbsp;ta `FUNKCJA` różniła się między skryptami.  
  Ale zawsze odnosiła się do funkcji importowanej parę linijek wyżej. Zatem nawet jeśli nie ma powtarzalności tekstu, jest pełna *powtarzalność zasady działania*.

Po odsianiu drobnicy zostały dwie ciekawe rzeczy do wyjaśnienia.

### Zagadki linijki importującej

Głównym źródłem różnic wydaje się być linijka, w&nbsp;której dochodzi do wzięcia jakiejś funkcji z&nbsp;innego skryptu stworzonego przez autorów. Każdy skrypt robi to inaczej:

<pre class="black-bg mono with-next">
from <span class="red">chardet.cli.chardetect</span> import main
from <span class="red">pip._internal.cli.main</span> import main
from <span class="red">yt_dlp</span> import main
from <span class="red">mss.__main__</span> import main
</pre>

{:.figcaption}
Kolorami wyróżniłem części zmienne, reszta to niezmienniki.

Gdybym miał tylko te moduły, to mógłbym pomyśleć, że również nazwa wyciąganej funkcji (*main*) zawsze jest taka sama. Ale nie! Parę nielicznych modułów, jak *tld*, wyłamuje się z&nbsp;tej konwencji:

<pre class="black-bg mono with-next">
from <span class="red">tld.utils</span> import <span class="red">update_tld_names_cli</span>
</pre>

### Zagadka znaku zapytania

Mniejsza, ale tym ciekawsza różnica pojawia się w&nbsp;linijce znajdującej (po czym usuwającej) końcówki nazw plików funkcją `re.sub`.  
W kilku modułach, jak *pip3*, *chardetect* i&nbsp;kilku innych, pojawiał się znak zapytania nieobecny w&nbsp;pozostałych:

<pre class="black-bg mono with-next">
r'(-script\.pyw<span class="red">?</span>|\.exe)?$'
r'(-script\.pyw|\.exe)?$'
</pre>

{:.figcaption}
Ograniczyłem się tutaj jedynie do fragmentu linijki, reszta była bez zmian.

Znak zapytania to część elastycznych regułek szukających. Sprawia, że rzecz stojąca przed nim [staje się opcjonalna](https://docs.python.org/3/library/re.html). Może być, może jej nie być. Ten wyróżniony odnosi się do literki&nbsp;*w*.  
W praktyce jedna wersja skryptu będzie usuwała z&nbsp;nazwy aktywnego programu (Pythona) jedynie końcówki `-script.pyw` i&nbsp;`.exe`, druga ponadto `-script.py`.

Ten znak, wedle moich obserwacji, zawsze występował razem z&nbsp;kilkoma pustymi linijkami (ilustracja wyżej). Dlatego w&nbsp;myślach wydzieliłem sobie dwie kategorie skryptów: „linijki i&nbsp;znak zapytania” oraz „zwięzłe, bez znaku”.

## Znalezienie części zmiennej

Co wspólnego miały ze sobą różne skrypty, które sprawdzałem? To, że **powstały po zainstalowaniu modułu programem `pip`**. Wziąłem swego czasu i&nbsp;wpisałem w&nbsp;konsolę:

<pre class="black-bg mono with-next">
pip install NAZWA_MODUŁU
</pre>

{:.figcaption}
Dokładniej rzecz biorąc, na komputerze musiałem wpisać `pip3`, bo miałem domyślnie dwie wersje Pythona. Ale to detal.

W ten sposób zdobyłem *yt-dlp*. Innym razem *mss* od robienia screenshotów, też pokazany powyżej. W&nbsp;każdym z&nbsp;tych przypadków do folderu specjalnego `bin` trafił szablonowy skrypt uruchamiający.

Pomyślałem, że rozwiązania zagadki trzeba poszukać u&nbsp;źródła. Wewnątrz PIP-a, czyli tego pythonowego instalatora.

Co się dzieje, kiedy używam powyższego polecenia?  
Ano to, że *pip* łączy się z&nbsp;PyPI -- centralną bazą, do której ludzie mogą wrzucać swoje własne moduły Pythona. PIP sprawdza, czy ma w&nbsp;tej bazie moduł o&nbsp;wpisanej przeze mnie nazwie. Jeśli tak, to go pobiera.

Do plików, które pobiera PIP, można również dobrać się ręcznie. Wejść na stronę konkretnego modułu (tu: [*yt-dlp*](https://pypi.org/project/yt-dlp/)), kliknąć zakładkę *Download Files*. Pod nagłówkiem *Built Distribution* (sugerującym, że to wersja dla użytkowników) znalazłem plik z&nbsp;rozszerzeniem `.whl`.

Pobrałem pliki dla modułów *yt-dlp* oraz *mss*. Jeśli to na ich podstawie instalator tworzył skrypty wejściowe, to gdzieś powinny w&nbsp;nich być odpowiednie informacje.

### Wnętrze plików WHL

Pobrany plik `.whl` ([skrót od *wheel*](https://peps.python.org/pep-0427/)) to tak naprawdę archiwum ZIP. Jak wiele innych plików, po których nie każdy by się tego spodziewał (dokumenty pakietu Office, aplikacje na Androida...).  
W każdym razie mogłem go rozpakować. Na Linuksie -- bez zmian rozszerzenia, po prostu prawe kliknięcie i&nbsp;wybranie odpowiedniej opcji.

Pierwsza myśl -- poszukam charakterystycznych słów ze skryptu startowego i&nbsp;zobaczę, czy gdzieś je znajdę w&nbsp;rozpakowanym folderze. Być może wszyscy twórcy osobiście załączają szablonowe skrypty startowe, a&nbsp;instalator jedynie je kopiuje w&nbsp;odpowiednie miejsce?

Do przeszukiwania zawartości folderów idealnie się nadaje programik *grep*, który w&nbsp;odpowiednim trybie odwiedza każdy plik po kolei:

<pre class="black-bg mono with-next">
grep -r -F "<span class="red">SZUKANY_TEKST</span>" ROZPAKOWANY_FOLDER
</pre>

{:.figcaption}
Argument `-r` po to, żeby przeszukać wszystkie pliki oraz podfoldery we wskazanym folderze;  
`-F` po to, żeby [nie traktowało żadnych znaków jak znaków specjalnych](https://stackoverflow.com/questions/10346816/using-grep-to-search-for-a-string-that-has-a-dot-in-it).

Najpierw poszukałem tekstu `sys.exit`. Części niby szablonowej, ale z&nbsp;drugiej strony na tym etapie dopuszczałem myśl, że każdy moduł trzyma gdzieś własny szablon.  
Ale *grep* niczego nie znalazł. Ani w&nbsp;*yt-dlp*, ani w&nbsp;paru innych.

W związku z&nbsp;tym, zamiast szukać części szablonowej, postanowiłem poszukać części zmiennych, różniących się między skryptami. Jak nazwy importowanych modułów i&nbsp;funkcji.

W przypadku MSS-a linijka ze skryptu startowego brzmiała:

```python
from mss.__main__ import main
```

Drugi zmienny człon, `main`, brzmiał dla mnie ciut zbyt ogólnie. Dlatego w&nbsp;rozpakowanym pliku WHL poszukałem pierwszego:

<pre class="black-bg mono with-next">
grep -r -F "<span class="red">mss.__main__</span>" mss-9.0.1-py3-none-any.whl_FILES
</pre>

{% include info.html
type="Porada"
text="Nie musiałem wpisywać ani kopiować pełnej nazwy rozpakowanego folderu. Wystarczyło wpisać pierwsze literki i&nbsp;nacisnąć klawisz `Tab`.  
Czasem to wystarczy, ale u&nbsp;mnie były dwie rzeczy o&nbsp;zbliżonych nazwach: WHL oraz wypakowany z&nbsp;niego folder. Dlatego dopisałem literkę *F*, żeby pasował już tylko folder (mający w&nbsp;nazwie *FILES*). I&nbsp;znów `Tab`, żeby dopełnić resztę nazwy."
%}

I eureka! Grep znalazł szukany tekst w&nbsp;podfolderze zakończonym na `dist-info`, w&nbsp;pliku o&nbsp;nazwie **_entry_points.txt_**. Zresztą cały plik zawierał tylko to:

```
[console_scripts]
mss = mss.__main__:main
```

Zgadzały się: nazwa skryptu startowego, nazwa importowanego, nazwa konkretnej funkcji (po dwukropku), cel tego wszystkiego („skrypty konsolowe” w&nbsp;nawiasach kwadratowych). Miałem mocne podejrzenie, że **to na podstawie tego pliku instalator uzupełnia szablon skryptów startowych**.

...Ale skąd brał sam szablon?

## Znalezienie części szablonowej

Na logikę: jeśli instalowane pliki zawierają tylko informacje do umieszczenia w&nbsp;szablonie, to sam szablon powinien tkwić **na moim komputerze, wewnątrz instalatora**. Może samego PIP-a. Może innego modułu, z&nbsp;którego korzysta.

Tyle że nie wiedziałem, gdzie szukać, zaś mój własny system zawierał więcej poinstalowanych modułów Pythona, które mogłyby wchodzić w&nbsp;drogę.  
Dlatego postanowiłem stworzyć jakieś czyste środowisko do eksperymentów, w&nbsp;którym wyizoluję sobie instalatora i&nbsp;to jego przeszukam.

W Pythonie taką możliwość zapewniają **środowiska wirtualne**.  
To coś w&nbsp;rodzaju odgrodzonej części systemu. Pozwalają eksperymentować z&nbsp;różnymi modułami Pythona, instalować je i&nbsp;usuwać, ale bez wpływu na główne pliki na komputerze.

W jakimś folderze X&nbsp;stworzyłem folder `skrypty-testy`, po czym uruchomiłem w&nbsp;tym samym folderze X&nbsp;konsolę i&nbsp;wpisałem:

<div class="black-bg mono with-next">
python3.7 -m venv skrypty-testy 
</div>

{:.figcaption}
Użyłem tu nieco starszej wersji Pythona (3.7), jaką u&nbsp;siebie miałem. Jak się potem okaże, ma to istotne znaczenie.

To polecenie wypełniło folder kilkoma podstawowymi modułami Pythona. Również tymi odpowiedzialnymi za instalację, jak PIP.

Środowisko wirtualne, choć ma nietypowe możliwości, jest dla systemu najzwyklejszym folderem `skrypty-testy`, całkiem publicznym. Wiedząc, że w&nbsp;środku mam instalatory, mogłem poszukać tekstu typowego dla szablonów. Postawiłem na fragment reguły ucinającej końcówki:

<pre class="black-bg mono with-next">
grep -rF "<span class="red">re.sub(r'(-script\.py</span>" skrypty-testy
</pre>

### Stare szablony

Wynik wyszukania? Wzmianka o&nbsp;dwóch plikach binarnych, których nie odczytało, oraz kilka tekstowych:

<pre class="black-bg mono with-next">
<span class="red">skrypty-testy/lib/python3.7/site-packages/pip/wheel.py</span>
<span class="red">skrypty-testy/lib/python3.7/site-packages/setuptools/command/easy_install.py</span>
skrypty-testy/bin/pip3.7
skrypty-testy/bin/pip
skrypty-testy/bin/pip3
skrypty-testy/bin/easy_install
skrypty-testy/bin/easy_install-3.7
</pre>

{:.figcaption}
Gdybym chciał celowo pominąć pliki binarne, nie dostając o&nbsp;nich nawet wzmianki, to mógłbym dopisać `-I` po słowie `grep`. Albo zwięźlej: zmienić `-rF` na `-rFI`. 

Pliki, które zawierały w&nbsp;swojej ścieżce *bin*, same były skryptami startowymi. Stworzonymi z&nbsp;szablonu, więc nie mogły *być* szablonem. Olałem je.

Skrypt `easy_install.py` zawierał klasę ScriptWriter, która miała swój szablon... Tyle że nieco zbyt długi. Zawierał szereg rzeczy nieobecnych w&nbsp;moich skryptach startowych.

Za to plik `wheel.py` był strzałem w&nbsp;dziesiątkę! Już sama nazwa sugeruje, że odpowiada za pliki WHL, do tego jego zawartość idealnie pasowała do niektórych skryptów startowych (nie zawierał jedynie pierwszej linijki, dodanej w&nbsp;innym miejscu):

{:.figure .bigspace}
<img src="/assets/posts/open_source/python-skrypty-wejsciowe/skrypt-startowy-stary-szablon.jpg" alt="Fragment skryptu wheel.py, zawierający tekst szablonu"/>

...Ale **ten szablon nie wyjaśniał wszystkiego**. Pasował do skryptów rozstrzelonych na więcej linijek, z&nbsp;dodatkowym znakiem zapytania w&nbsp;regułce.  
Nie powstał z&nbsp;niego natomiast ten drugi, zwięzły typ skryptów startowych. Co więcej: w&nbsp;żadnym ze znalezionych wyżej plików nie było pasującego szablonu.

### Nowsze szablony

Korzystałem w&nbsp;środowisku wirtualnym ze starszej wersji Pythona, która siłą rzeczy korzystała ze starszych wersji instalatorów. Uznałem, że je **zaktualizuję do najnowszych wersji** i&nbsp;zobaczę, czy to coś zmienia.

Żeby zaktualizować coś wewnątrz środowiska wirtualnego, musiałem w&nbsp;nie „wejść”. Będąc w&nbsp;tym samym folderze, w&nbsp;którym tkwił folder `skrypty-testy`, wpisałem:

<pre class="black-bg mono with-next">
source skrypty-testy/bin/activate
</pre>

{:.figcaption}
Programik konsolowy `source` służy do uruchamiania innych programów. Odnoszę się tu do programu *activate*, zakopanego w&nbsp;folderze `skrypty-testy`, podfolderze `bin`.

Mogłem łatwo poznać, że środowisko się włączyło, bo na początku linijki, między nawiasami, pojawiło się `skrypty-testy`. Nazwa aktualnego środowiska. Póki jestem w&nbsp;tym trybie, moduły Pythona są instalowane *wyłącznie* w&nbsp;jego obrębie.

Żeby zaktualizować rzeczy związane z&nbsp;instalacją, wpisałem:

```
pip3 install -U pip
pip3 install -U setuptools
```

Potem powtórzyłem polecenie do Grepa, jakim wcześniej znalazłem starszy szablon.  
Ponownie znalazło mi dwa potencjalnie ciekawe skrypty. Jeden był tym samym `easy-install.py` co poprzednio, który miał zbyt długi szablon.  
Drugi znaleziony skrypt różnił się natomiast od tego ze starszego instalatora:

```
skrypty-testy/lib/python3.7/site-packages/pip/_vendor/distlib/scripts.py
```

Zajrzałem do niego... I&nbsp;bingo! Był tam **szablon pasujący do drugiego rodzaju skryptów startowych**. Tych zwięzłych i&nbsp;bez znaku zapytania.

{:.figure .bigspace}
<img src="/assets/posts/open_source/python-skrypty-wejsciowe/python-skrypt-wejsciowy-szablon.jpg" alt="Fragment skryptu Pythona, pokazujący szablon skryptu z&nbsp;miejscami do uzupełnienia"/>

### Podsumowanie wątku

Na tym etapie byłem już przekonany, że rozgryzłem instalację skryptów startowych przez Pythona:

* instalator zdobywa plik WHL z&nbsp;centralnej bazy Pythona,
* znajduje w&nbsp;pakiecie plik *entry_points.txt*,
* odczytuje z&nbsp;niego, że powinien stworzyć skrypt startowy w&nbsp;folderze ogólnodostępnym,
* uzupełnia szablon ze swoich bebechów szczegółami z&nbsp;pliku,
* tworzy skrypt.

{:.post-meta .bigspace-after}
Gdybym chciał mieć pewność, mógłbym spróbować użyć PIP-a z&nbsp;jakimś profilerem albo programikiem typu `strace`. Zobaczyłbym dokładnie, jakie funkcje kolejno się włączały i&nbsp;jakie stworzyły mi pliki.  
Ale zadowoliłem się eksploracją samej treści skryptów.

A różnice między wyglądem finalnych skryptów? Wynikały z&nbsp;tego, że sama ekipa tworząca Pythona na przestrzeni wersji zmieniała swoje szablony.

A ja aktualizowałem instalatory, nie zmieniając przy tym niektórych rzeczy, które już wcześniej zainstalowałem. W&nbsp;folderze `bin` wymieszały mi się przez to skrypty startowe w&nbsp;wariantach starszych i&nbsp;nowszych.

{% include info.html
type="Ciekawostka"
text="Pojawia się tu również ciekawy wątek poboczny, może nawet związany z&nbsp;prywatnością (a&nbsp;na pewno ze swoistym *fingerprintingiem*) -- **na podstawie budowy skryptów startowych można ustalić, jaką wersją narzędzi Pythona były instalowane**.  
W ten sposób dałoby się np. oszacować, z&nbsp;jakiego okresu pochodzi folder skopiowany z&nbsp;czyjegoś komputera, jeśli nigdzie nie ma daty. Brzmi jak bzdet... Ale zdarzało się kiedyś, że [rozpoznano podróbki po użytych czcionkach](https://arstechnica.com/tech-policy/2017/07/not-for-the-first-time-microsofts-fonts-have-caught-out-forgers/). Oszuści twierdzili, że jakiś dokument jest stary, ale jego czcionka była współczesna."
%}

## Od strony twórców

Główna zagadka wyjaśniona, ale czułem niedosyt. Sama instalacja przez użytkowników to dopiero druga połowa drogi. A&nbsp;jak to wygląda między niezależnymi twórcami a&nbsp;bazą PyPI? Czy tworzą plik `entry_points.txt` oraz kilka innych ręcznie, przed dodaniem do pliku WHL?

Wyszukałem w&nbsp;sieci `entry_points.txt` oraz `console scripts`.  
Wyskoczyła mi stronka Pythona opisująca [konwencje związane ze skryptami startowymi](https://packaging.python.org/en/latest/specifications/entry-points/#file-format). Poznałem też ich oficjalną nazwę -- **_entry points_ (dosł. _punkty wejściowe_)**.

Strona wspomniała również, że twórcy nie dodają plików ręcznie. Zostawiają wytyczne dla programu łączącego ich skrypty w&nbsp;plik WHL, po czym to on tworzy pliki tekstowe.

Te wytyczne mogą umieszczać w kilku miejscach. Programik *yt-dlp* postawił na plik [*pyproject.toml*](https://github.com/yt-dlp/yt-dlp/blob/master/pyproject.toml). W&nbsp;przypadku ich projektu dość obszerny.  
Tam (na dzień dzisiejszy -- w&nbsp;linijkach 78&nbsp;i 79&nbsp;-- znajdują się instrukcje dotyczące skryptów startowych.

```
[project.scripts]
yt-dlp = "yt_dlp:main"
```

Podsumowując całą drogę skryptów startowych -- od twórców po użytkowników -- w&nbsp;formie schematu:

<img src="/assets/posts/open_source/python-skrypty-wejsciowe/python-pakowanie-instalacja-schemat.jpg" alt="Schemat pokazujący trzy kolejne etapy połączone strzałkami. Na początku jest kod źródłowy, potem baza PyPI, a&nbsp;na koniec komputer użytkownika." />

## Czego się nauczyłem

Podczas eksploracji trochę się dowiedziałem na temat tego, jak udostępniać moduły Pythona. Tak, żeby dało się ich używać jako programów konsolowych, reagujących na wezwanie z&nbsp;każdego folderu. To mi się przyda!

Okazuje się, że to nie takie trudne. **Wiele sprowadza się do wpisania paru linijek w&nbsp;plik tekstowy**.  
Resztę bierze na siebie najpierw program pakujący wszystko do jednego pliku WHL. A&nbsp;potem -- po stronie użytkowników -- wszystko załatwia instalator, czyli PIP. Oraz jego skrypty towarzyszące.

Zapewne twórcy każdego języka programowania stają przed podobnymi kwestiami -- „jak ułatwić tworzenie programów konsolowych w&nbsp;naszym języku?”, „czy mieć centralną bazę skryptów od różnych ludzi?”.

Nie zdziwiłbym się, gdyby wiele projektów dryfowało ku temu samemu rozwiązaniu, zwięzłym plikom konfiguracyjnym. Choć skupiłem się na Pythonie, zapewne wchłonąłem w&nbsp;głowę też parę ogólnych konwencji.

A czy nie mogłem po prostu zacząć od dokumentacji, zamiast odkrywać koło (WHL) na nowo? Pewnie mogłem. Ale nie miałbym z&nbsp;tego takiej frajdy :smile:


