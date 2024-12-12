---
layout: post
title: "Echo w rurach i WC. Program konsolowy od podstaw"
subtitle: "Trochę hobbystycznej cyfrowej hydrauliki."
description: "Trochę hobbystycznej cyfrowej hydrauliki."
tags: [Konsola, Podstawy, Python]
date:   2024-12-09 08:05:00 +0100
image:
  path: assets/posts/konsola/rury/wpis-numer-100-baner.jpg
  width: 1200
  height: 700
  alt: "Okno konsoli widoczne na pierwszym planie, w które wpisane są słowa 'Wpis numer 100', pionowa kreska i słowo 'wc'. W tle widać plątaninę generowanych losowo rur."
---

Po kilku latach jest i&nbsp;on -- okrągły wpis numer 100&nbsp;na stronie głównej bloga :smile:

Zastanawiałem się, którą z&nbsp;rzeczy z&nbsp;wirtualnej szuflady powinienem z&nbsp;tej okazji dokończyć.  
„Niespiskową teorię świata” z&nbsp;ogólnymi przemyśleniami na temat korupcji i&nbsp;współczesnego kolonializmu? Wpis o&nbsp;największej branżowej akcji dezinformacyjnej, z&nbsp;jaką się spotkałem? O&nbsp;potencjale śledzącym akcelerometru? Może coś o&nbsp;ciemnych stronach Play Store'a?

Ale ostatecznie uznałem, że nie ma co się spinać. Okrągła liczba ma znaczenie chyba tylko dla mnie, bo raczej mało kto czyta bloga liniowo. A&nbsp;zatem: zamiast wielkich, smoczych spraw będzie wpis luźniejszy, który bawi i&nbsp;uczy. A&nbsp;zamiast smoczego ognia będzie woda, bo niedawno było o&nbsp;niej głośno. Jak nie powódź w&nbsp;Polsce, to w&nbsp;Hiszpanii.

A jak woda, to rury. Przybliżę, intuicyjnie i&nbsp;na schematach, **rury w&nbsp;konsoli systemu Linux**, pozwalające „przelewać” dane z&nbsp;jednego programu do drugiego. Krok po kroku stworzę też drobny skrypt w&nbsp;języku Python, po każdej poprawce coraz lepiej zintegrowany z&nbsp;systemem.

Zapraszam! Również osoby mniej konsolowe, żeby się oswajały :smile:

{:.figure .bigspace-before}
<img src="/assets/posts/konsola/rury/wpis-numer-100-baner.jpg" alt="Okno konsoli widoczne na pierwszym planie, w&nbsp;które wpisane są słowa 'Wpis numer 100', pionowa kreska i&nbsp;słowo 'wc'. W&nbsp;tle widać plątaninę generowanych losowo rur."/>

{:.figcaption}
Źródła: kultowy [wygaszacz ekranu](https://www.youtube.com/watch?v=tCpnDTzRAjE), konsola systemu Linux Mint. Przeróbki moje.

{% include info.html
type="Uwaga o&nbsp;systemach"
text="Wpis stworzyłem z&nbsp;myślą o systemie Linux Mint. Te same programiki działają na zwykłym, niemodyfikowanym smartfonie z&nbsp;Androidem (wewnątrz apki [Termux](/tutorials/termux){:.internal}).  
Nie testowałem ich natomiast na systemie Windows. Ale, z&nbsp;tego co zerknąłem, w&nbsp;windowsowej konsoli PowerShell można znaleźć program [`echo`](https://stackoverflow.com/a/1639960), a&nbsp;także [rury](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines?view=powershell-7.4), zaś odpowiednikiem `wc` wydaje się [`Measure-Object`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/measure-object?view=powershell-7.4).  
A zatem: jeśli ktoś ma Windowsa, ale też się chce pobawić, to zapraszam! Ale nie gwarantuję, że będzie śmigało."
%}

## Spis treści

* [Wprowadzenie](#wprowadzenie)
* [WC i&nbsp;inne mikroprogramy](#wc-iinne-mikroprogramy)
* [Konstrukcja własnego programu](#konstrukcja-własnego-programu)
  * [Przyjmowanie i&nbsp;wyrzucanie tekstu](#przyjmowanie-iwyrzucanie-tekstu)
  * [Problem pierwszy: niewykonywalność](#problem-pierwszy-niewykonywalność)
  * [Problem drugi: niewskazanie Pythona](#problem-drugi-niewskazanie-pythona)
  * [Ulepszenie: magiczna linijka](#ulepszenie:-magiczna-linijka)
  * [Ulepszenie: wzywanie z&nbsp;dowolnego miejsca](#ulepszenie-wzywanie-zdowolnego-miejsca)
* [Podsumowanie](#podsumowanie)
* [Bonus: możliwe modyfikacje](#bonus-możliwe-modyfikacje)

## Wprowadzenie

Choć postronnym konsola może kojarzyć się z hakerstwem i&nbsp;jakimśtam stopniem wtajemniczenia, tak naprawdę można się z&nbsp;nią spotkać w&nbsp;całkiem codziennych i&nbsp;prozaicznych sytuacjach.

Ot na przykład: nie pamiętam, jaką mam w&nbsp;laptopie kartę graficzną i&nbsp;chcę to sobie sprawdzić. A&nbsp;zatem wpisuję w&nbsp;zwykłą internetową wyszukiwarkę: `linux how to check graphics card`. Wyskakuje mi jakaś stronka, [być może ta](https://itsfoss.com/check-graphics-card-linux/). A&nbsp;tam krótkie polecenie, które powinno rozwiązać moje problemy:

<div class="black-bg mono">
lspci |&nbsp;grep VGA
</div>

{:.figcaption}
Jego objaśnienie za parę akapitów.

Dla jasności: bardzo możliwe, że te same informacje byłyby do wyklikania w&nbsp;jakimś najzwyklejszym, graficznym menu. **To mit, że używanie Linuksa wymaga znajomości konsoli**. Zresztą nawet w&nbsp;podlinkowanym artykule jest opisany sposób oparty na klikaniu myszką.

Sposób konsolowy ma natomiast wielką, ogromną zaletę -- jest uniwersalny. Powinien zadziałać wszędzie, na każdej z&nbsp;wielu odmian (*dystrybucji*) Linuksa. Nawiązując do konsoli, autor artykułu trafia do szerszego grona, niż gdyby pisał o&nbsp;jednej nakładce graficznej.

Inną zaletą jest szybkość i&nbsp;prostota. Wystarczy po prostu skopiować podany tekst, uruchomić konsolę (przez ikonkę z dolnego paska albo kombinację klawiszy `Ctrl+Alt+T`), wkleić komendę i&nbsp;nacisnąć `Enter`. I&nbsp;zrobione, wyświetli się szukana nazwa karty graficznej.

Uniwersalność metody konsolowej wynika z&nbsp;tego, że system często zawiera zestaw domyślnie zainstalowanych programów, prostych i&nbsp;niezawodnych. Jak tutaj: `lspci` od wypisywania informacji o&nbsp;częściach komputera, `grep` od wyszukiwania konkretnego tekstu (tu akurat: `VGA`, bo taki jest przy karcie graficznej).  
Takie małe programiki są zgodne z&nbsp;tak zwaną *filozofią uniksową* (od systemu Unix, praprzodka wielu współczesnych systemów) -- „rób jedną prostą rzecz, ale rób ją dobrze”. Aprobuję.

Jeszcze ważniejszą rzeczą od programów jest natomiast pomost między nimi -- `|`, czyli po angielsku *pipe operator*, inaczej **_pipe_. W&nbsp;dosłownym tłumaczeniu: „rura”**.

To element często stosowany w&nbsp;konsoli. Pozwala przekazywać to, co wypluje program po jego lewej stronie, do programu po prawej. Łączyć mikroprogramy w&nbsp;rozwiązywacze codziennych problemów.  
A że Linux ceni wolność, to nie jesteśmy ograniczeni do programików z&nbsp;zamkniętej, narzuconej odgórnie listy; trzymając się paru zasad, można tworzyć również własne skrypty, w&nbsp;pełni pasujące do wszelkich rurociągów. Co za chwilę uczynię.

Ale do *tanga*{:.corr-del} rury trzeba dwojga, więc przyda się jakiś program, z&nbsp;którym fajnie by się zintegrował ten mój skrypt, który dopiero powstanie. Który z&nbsp;wielu domyślnych by tutaj wybrać?  
Jestem prostym człowiekiem. Jak rury, to woda. Jak woda, to WC.

## WC i&nbsp;inne mikroprogramy

Choć nazwa programiku konsolowego `wc` może budzić uśmiech, to tak naprawdę [skrót od *word count*](https://linuxize.com/post/linux-wc-command/). „Liczarka słów”. A&nbsp;także linijek i&nbsp;znaków (z&nbsp;pewnym zastrzeżeniem, o&nbsp;którym za sekundę). Fajne narzędzie pozwalające na przykład się rozeznać, jak duże są różne nasze pliki.

Wrzucę do tej liczarki jakiś tekst na próbę, podając go rurą. Musi być otoczony cudzysłowami, żeby spacje nie miały dla konsoli specjalnego znaczenia. Pierwsza myśl:

<pre class="black-bg mono">
<span class="red">'Jakiś tekst' |&nbsp;wc</span>
</pre>

...Ale **to nie zadziała, bo tekst „luzem”, nieprzywiązany do niczego, nie jest tolerowany przez konsolę**. Trzeba go „przemycić” wewnątrz jakiegoś programu czy zmiennej. Sposobów jest wiele, ale chwycę się najprostszego. Można wprowadzić tekst do konsoli programem `echo`:

<pre class="black-bg mono">
echo 'Jakiś tekst' |&nbsp;wc
</pre>

Takie polecenie już zadziała, tekst trafi do liczarki i&nbsp;wyświetlą się trzy liczby: `1  2 13`. Liczba linijek, liczba słów i&nbsp;liczba... znaków? Tyle że z&nbsp;ostatnią coś się nie zgadza, o&nbsp;czym za sekundę. Ale najpierw drobny schemat:

{:.bigspace-before}
<img src="/assets/posts/konsola/rury/echo-wc-konsola.jpg" alt="Schemat działania rur w&nbsp;konsoli pokazujący, jak słowa 'Jakiś tekst' wpadają do maszynki do mięsa podpisanej 'echo', z&nbsp;niej do zakrzywionej rury, a&nbsp;stamtąd do toalety podpisanej 'wc'. Pod nią wyświetlają się trzy liczby"/>

{:.figcaption}
Wybaczcie mi kloaczny humor.  
Źródła: Flaticon -- [czerwona](https://www.flaticon.com/free-icon/down-arrow_2268142) i&nbsp;[zielona strzałka](https://www.flaticon.com/free-icon/arrow-right_2267911) od *Creative Stall Premium*, [maszynka do mięsa](https://www.flaticon.com/free-icon/meat-grinder_836411), [toaleta](https://www.flaticon.com/free-icon/toilet_2203717) i&nbsp;[rura](https://www.flaticon.com/free-icon/pipe_2443858) od *Freepik*. Przeróbki moje.

Odnośnie liczby, która się nie zgadza: wyraźnie mamy 5&nbsp;liter w&nbsp;pierwszym słowie, 5&nbsp;w&nbsp;drugim, jedną spację. Łącznie 11&nbsp;znaków, a&nbsp;pokazuje 13.

Jedna nadwyżkowa rzecz bierze się stąd, że **`echo` domyślnie dodaje na końcu wprowadzonego tekstu znak kończący linijkę**. W&nbsp;wielu kontekstach jest on umownie zapisywany jako `\n`, ale jego długość wynosi 1.  
Można go sobie wyobrazić jak oznaczenie niewidoczne gołym okiem, ale bez wątpienia obecne w&nbsp;danych. Jak znaczek <img src="/assets/posts/konsola/rury/koniec-linijki.jpg" alt="" height="18"/>{:.inline}, który Word czy LibreOffice dodają w&nbsp;trybie wyświetlania znaków specjalnych.

To wyjaśnia rozbieżność o&nbsp;1, ale skąd przesunięcie numer 2? Mówiąc prosto -- **`wc` liczby bajty, a&nbsp;nie widoczne znaki**. 
Żeby nie siać zamętu, zignoruję ten fakt i&nbsp;odtąd będę wrzucał do konsoli tylko podstawowe znaki i&nbsp;litery. A&nbsp;szczegóły pozostawię osobom chętnym.

<details class="bigspace">
<summary><strong>Szczegóły (dla chętnych)</strong></summary>

<p>Druga nadwyżka wynika z&nbsp;obecności polskiego <code class="language-plaintext highlighter-rouge">ś</code>, które za kulisami jest złożone z&nbsp;dwóch bajtów danych. W&nbsp;przeciwieństwie do podstawowych znaków angielskiego alfabetu, które są jednobajtowe. Polskie znaki to i&nbsp;tak pikuś – emoty (zwłaszcza flagi krajów) są jeszcze cięższe.</p>

<p>Ogólniej, chcąc dokładniej zbadać, co tam <em>echo</em> przyniosło, możemy użyć <a href="https://stackoverflow.com/questions/1765311/how-to-view-files-in-binary-from-bash">prostego sposobu</a> z&nbsp;forum StackOverflow. Korzystając z niezawodnej <em>rury</em>, wrzucić tekst do programiku <code class="language-plaintext highlighter-rouge">od</code>:</p>

<div class="black-bg mono">
echo 'Jakiś tekst' | od -c
</div>

<p>Pokaże nam wtedy, z&nbsp;czego się on składał:</p>

<pre class="black-bg mono">
J   a   k   i 305 233       t   e   k   s   t  \n
</pre>

<p>Gdyby zamiast <code class="language-plaintext highlighter-rouge">ś</code> użyć litery <code class="language-plaintext highlighter-rouge">s</code>, a&nbsp;do <em>Echa</em> dopisać po spacji argument <code class="language-plaintext highlighter-rouge">-n</code> (nakaz, żeby nie dodawało znaku końca linii), to liczba na końcu wyniesie oczekiwane 11.</p>

<p><img src="/assets/posts/konsola/rury/wc-liczenie-slow-przyklady.jpg" alt="Kilka linijek konsolowych pokazujących, jak usunięcie polskiej litery i&nbsp;dopisanie n&nbsp;po kreseczce wpływają na wynik programu wc" /></p>

<p class="post-meta bigspace-after">Koniec bonusowego objaśnienia.</p>

</details>

I na koniec, żeby `wc` nie jawił się jako zabaweczka, pokażę jedno jego praktyczne zastosowanie w&nbsp;kombinacji z&nbsp;innym mikroprogramem. Będzie to **liczenie elementów w&nbsp;dowolnym folderze**, wykonane w&nbsp;duecie z&nbsp;programem `ls`:

<div class="black-bg mono">
ls | wc
</div>

Działa to w&nbsp;ten sposób, że programik `ls`, wypisujący nazwy rzeczy (plików/folderów...) zawartych w&nbsp;aktywnym folderze, wypluwa *po jednej rzeczy na linijkę*. Gdy do `wc` przerzuci się te wszystkie linijki, to ich liczba siłą rzeczy będzie równa liczbie rzeczy w&nbsp;folderze.

{:.post-meta .bigspace-after}
Można też napisać `wc -l`, żeby pokazało *jedynie* liczbę linijek.

## Konstrukcja własnego programu

Przedstawiłem cegiełki, więc teraz czas z&nbsp;nich coś zbudować.

Skoro już mamy rury i&nbsp;WC, to przyda się coś również nawiązującego do motywu wody. Dlatego **swój mikroprogram nazwę `zbiornik`**. I&nbsp;niech działa podobnie jak zbiorniki retencyjne -- zatrzymuje część lecących danych. Jeśli ich ilość będzie większa niż jego pojemność, to reszta danych się „przeleje” i&nbsp;poleci dalej.  
Programik ten docelowo ustawię między `echo` a&nbsp;`wc`.

To do dzieła! Stworzyłem sobie plik o&nbsp;nazwie `zbiornik` (na Linuksie nie ma problemów, jeśli nie dopiszę końcówki `.py`, typowej dla skryptów Pythona). A&nbsp;teraz co do niego wpisać?

### Przyjmowanie i&nbsp;wyrzucanie tekstu

{:.post-meta .bigspace-after}
Ta część jest napisana w&nbsp;Pythonie, ale nie zrażajcie się, jeśli go nie znacie; można wziąć na wiarę, że działa, i&nbsp;przejść do dalszych spraw wokół rur.

Skoro chcę stawiać swój zbiornik na drodze lecących danych, to siłą rzeczy musi mieć jakiś wlot i&nbsp;wylot. W&nbsp;jaki sposób mogę sprawić, żeby:

1. przyjął to, co wypluł program przed nim,
2. podał dalej coś innego?

Przydaje się tu szczypta terminologii. To, co wpada -- do programów i&nbsp;nie tylko -- to w&nbsp;światku komputerowym *input*. Rzeczy wypadające to *output*. Wiedząc to, mogłem powierzyć wyszukiwarce DuckDuckGo swój problem: `python accepting console input output`. I&nbsp;niezawodny Stack pokazał rozwiązanie:

```python
import sys

for stream in sys.stdin:

    # W tym miejscu mogę coś zrobić

    sys.stdout.write( stream )
```

<details class="figcaption">
<summary>Objaśnienie (kliknij, żeby rozwinąć).</summary>
<p>
Moduł <code class="language-plaintext highlighter-rouge">sys</code> jest domyślnie zawarty w&nbsp;Pythonie i&nbsp;pozwala na integrację z&nbsp;różnymi systemowymi rzeczami, ale trzeba go <em>importować</em>, żeby skorzystać z&nbsp;jego możliwości;<br />
<code class="language-plaintext highlighter-rouge">sys.stdin</code> pozwala sięgać po dane wpadające wejściem standardowym (czyli zwykle rurą);<br />
wpadają one linijka po linijce, więc też obrabiam je po kolei, w&nbsp;pętli <code class="language-plaintext highlighter-rouge">for</code>;<br />
<code class="language-plaintext highlighter-rouge">stream</code> to nazwa umowna (mogłaby być inna), tymczasowa, dla każdej z&nbsp;wpadających rzeczy;<br />
na końcu jest obiekt <code class="language-plaintext highlighter-rouge">sys.stdout</code>, który ma swoją funkcję <code class="language-plaintext highlighter-rouge">write</code>, wyrzucającą dane z&nbsp;powrotem do „świata konsolowego”.
</p>
</details>

Linijkę „(...) coś zrobić” z&nbsp;komentarza wyżej zastąpiłem kodem, który ucina część wpadających danych (w&nbsp;praktyce: bajtów). Uznałem, że będzie to zawsze **5 pierwszych rzeczy**. Taki mikrozbiornik. Może politykom nie chciało się zanadto przeznaczać nań budżetu.

```python
import sys

empty_space = 5
for stream in sys.stdin:
    stream = stream[empty_space:]
    empty_space = max(0, empty_space - len(stream))
    if stream:
        sys.stdout.write( stream )
```

<details class="figcaption">
<summary>Omówienie (kliknij, żeby rozwinąć)</summary>
<p>Pojemność zbiornika <code class="language-plaintext highlighter-rouge">empty_space</code> powinna być resetowana przy każdym uruchomieniu skryptu, ale nie między napływem linijek. Dlatego umieszczam ją <em>powyżej</em> pętli.<br />
Przy pierwszej napływającej linijce ignoruję pięć elementów na początku, od 0&nbsp;do 4&nbsp;(listy Pythona są numerowane od zera). Biorę tylko dalsze.<br />
Potem odpowiednio zmniejszam dostępną pojemność, ale z&nbsp;głową, nie poniżej zera.<br />
Jeśli zostały jakieś dane, to puszczam je dalej.<br />
Cały cykl się powtarza. Przy którymś strumieniu dostępna pojemność wreszcie sięgnie 0; od tego momentu <em>wszystko</em> będzie przelatywało w&nbsp;niezmienionej postaci.</p>
</details>

{% include info.html
type="Uwaga"
text="Od teraz wszystkie konsolowe polecenia -- póki nie powiem inaczej -- wykonuję **w tym samym folderze, w&nbsp;którym jest mój skrypt**.  
Żeby otworzyć tam konsolę, mogę po prostu odwiedzić ten folder w&nbsp;domyślnym eksploratorze Minta, kliknąć prawym przyciskiem myszy pustą przestrzeń i&nbsp;wybrać opcję `Otwórz w terminalu`."
%}

### Problem pierwszy: niewykonywalność

Miałem swój skrypt, zaś w&nbsp;nim wlot, część przetwarzającą i&nbsp;wylot. Pozostało sprawdzić, co się stanie po połączeniu go rurami z&nbsp;konsolową klasyką:

<pre class="black-bg mono">
echo 'Testowy tekst' | zbiornik | wc
</pre>

A tu *błąd*. Informacja o&nbsp;braku potrzebnych pozwoleń :roll_eyes:

To dlatego, że na Linuksie jest coś takiego jak **wykonywalność plików**. Nie da się tak po prostu wpinać własnych rzeczy w&nbsp;konsolowy „rurociąg”, odpowiednio ich wcześniej nie oznaczając.  
Analogia? Mój niewykonywalny plik był jak coś oklejonego czarno-żółtymi taśmami i&nbsp;opatrzonego tabliczką z&nbsp;zakazem korzystania. Żaden szanujący się system-inspektor mi tego nie podłączy, choćbym chciał.

W przypadku Linuksa można bardzo łatwo ściągać te ograniczenia. Trzeba w&nbsp;tym celu uruchomić konsolę w&nbsp;tym samym folderze co skrypt, po czym użyć polecenia:

<div class="black-bg mono">
chmod +x zbiornik
</div>

{:.figcaption}
Ta komenda włącza wykonywalność na wszystkich poziomach. Na komputerze osobistym, którego jestem panem i&nbsp;władcą, nie widzę w&nbsp;tym problemu. Ale niektórzy mogliby działać ostrożniej.

Od tej pory mój `zbiornik` stał się *plikiem wykonywalnym*. W&nbsp;oczach systemu przestał być tylko wsadem do maszyn i&nbsp;stał się czymś, co można podłączać do rurociągów wszelakich.

### Problem drugi: niewskazanie Pythona

Mimo powyższej zmiany komenda nadal by nie działała. Dlaczego? **Bo skrypt Pythona to jedynie odrobina tekstu**.

Instrukcje. Jak kartka mówiąca, że należy zrobić na maszynie to i&nbsp;owo. Ale do wykonania tej instrukcji potrzeba jeszcze maszyny z&nbsp;prawdziwego zdarzenia. A&nbsp;skrypt -- kartka papieru -- nią nie jest. **Maszyną jest sam Python** (a&nbsp;żeby powiedzieć formalniej: *interpreter Pythona*).

Inne porównanie? Skrypt jest jak nabierak, ale bez koparki. Jak przyczepa bez samochodu, opryskiwacz bez traktora. I&nbsp;inne rzeczy w&nbsp;tym stylu -- to moduł, który trzeba podłączyć do czegoś z&nbsp;silnikiem.

Żeby działało, muszę jakoś nakazać konsoli: „ten plik odczytaj Pythonem”.  
Jedną z&nbsp;opcji jest zrobienie tego wprost. W&nbsp;moim przypadku nowsza wersja Pythona (3) figuruje w&nbsp;konsoli jako `python3` i&nbsp;właśnie takim słowem mogę ją przywołać:

```
echo 'Testowy tekst' | python3 zbiornik | wc
```

I bingo, program zadziała!  
...Tylko że każdorazowe wołanie Pythona nieco się kłóci z&nbsp;prostotą, do tego polecenie by nie zadziałało, gdyby go użyć w&nbsp;innym folderze niż ten ze skryptem. Czas się pozbyć tych słabości.

{% include info.html
type="Uwaga"
text="Nie jest to jakąś uniwersalną zasadą, że wersji 3&nbsp;Pythona odpowiada skrót `python3`. Tak było u&nbsp;mnie (Linux Mint), a&nbsp;Python był zainstalowany domyślnie.  
Z kolei na Termuksie trzeba wpisać polecenie instalujące (co [opisuję](/tutorials/termux#python){:.internal}), a&nbsp;potem przyzywać Pythona samym słowem `python`.  
Na Windowsie też trzeba go pobrać i&nbsp;zainstalować; do tego zaznaczyć podczas instalacji opcję w&nbsp;stylu „Dodaj do zmiennych środowiskowych”, żeby zyskać przyzywalność (słowem bodaj `python` albo `python.exe`)."
%}

### Ulepszenie: magiczna linijka

Zadbam teraz o&nbsp;to, żeby skrypt był *domyślnie* otwierany przez Pythona i&nbsp;żebym nie musiał go stale wołać przez `python3 zbiornik`. Będzie mi potrzebna pełna ścieżka do mojego Pythona. A&nbsp;ujawni mi ją chociażby komenda konsolowa `type python3`:

<pre class="black-bg mono">
/usr/bin/python3
</pre>

Zdobytą ścieżkę należy wstawić w&nbsp;**„magicznej linijce” na samym początku skryptu Pythona**, dopisując przed nią `#!`:

<pre class="black-bg mono">
#!/usr/bin/python3
</pre>

W ten sposób skrypt został podpięty do konkretnego Pythona. Będzie automatycznie się z nim „łączył” po uruchomieniu w&nbsp;konsoli.

{% include info.html
type="Ciekawostki"
text="Krzyżyk na początku linijki oznacza w&nbsp;Pythonie komentarze. Dzięki jego obecności skrypt zostanie bezproblemowo odczytany nawet przez programy nierozumiejące magicznych linijek (ale rozumiejące Pythona).  
Poza tym dość ciekawa ścieżka wychodzi na Termuksie -- jako „szeregowa” aplikacja nie zajmuje on żadnego uprzywilejowanego miejsca w&nbsp;systemie. Dlatego przed zwyczajowym `usr/bin/python` (przypominam: na Termuksie bez trójki) jego ścieżka zawiera całą drogę prowadzącą od rdzenia Androida do apki Termux: `/data/data/com.termux/files/`."
%}

I dla jasności schemat świeżo dodanego powiązania skryptowo-programowego:

<img src="/assets/posts/konsola/rury/zbiornik-python-polaczenie.jpg" alt="Schemat pokazujący nakładkę z&nbsp;napisem 'Zbiornik' przymocowaną do maszyny podpisanej 'Python'. Po prawej równolegle przebiega rząd podpisanych, połączonych strzałkami folderów prowadzących do tej samej maszyny Pythona"/>

{:.figcaption}
Dla uproszczenia dałem tu `python` zamiast `python3`.

### Ulepszenie: wzywanie z&nbsp;dowolnego miejsca

To co, mogę wreszcie użyć upragnionego polecenia?

<pre class="black-bg mono">
<span class="red">echo 'Testowy tekst' | zbiornik | wc</span>
</pre>

...Nie, nadal nie działa. Nie znajduje Zbiornika, choć jest w&nbsp;tym samym folderze. Dlaczego?

Otóż mój skrypt jest dla systemu taką płotką, nikim. System go nie zna i&nbsp;trzeba wprost mu mówić, gdzie ma go szukać, podając do niego *ścieżkę*:

* jeśli jestem w&nbsp;tym samym folderze -- mogę napisać `./zbiornik` (gdzie `./` oznacza „patrz w&nbsp;aktywnym folderze”);
* jeśli jestem w&nbsp;innym folderze, to muszę podać dłuższą ścieżkę do pliku ze skryptem -- pełną albo względną.

A ja tych ścieżek nie chcę, chcę przywoływać jednym słowem: `zbiornik`. W&nbsp;jaki sposób mogę dać mojemu skryptowi przywileje, które na to pozwolą?

Rozpoznawalność opiera się na szczęście na prostej zasadzie -- żeby dało się wołać programy po samej nazwie, muszą się znajdować w&nbsp;którymś ze **specjalnych folderów**. Ich kwestię już kiedyś poruszyłem w&nbsp;[innym wpisie Pythonowo-konsolowym](/2024/03/05/python-skrypty-startowe){:.internal}.

Żeby poznać te specjalne lokalizacje, mogę wpisać w&nbsp;konsolę `echo $PATH`. Wyświetli się lista pełnych ścieżek do folderów, rozdzielana średnikami. Skrypt można umieścić w&nbsp;dowolnym z&nbsp;nich. Na Linuksie dobrą opcją jest na przykład `$HOME/.local/bin` (gdzie zamiast `$HOME` będzie nazwa użytkownika, inna dla każdego).  
Polecenie kopiujące Zbiornik w&nbsp;to miejsce:

<pre class="black-bg mono">
cp zbiornik $HOME/.local/bin
</pre>

{% include info.html
type="Porady"
text="Na Termuksie ścieżka będzie inna niż ta wyżej i&nbsp;będzie zakończona na `/usr/bin`. To tam należy przenosić pliki.  
Gdybyśmy natomiast spróbowali przenieść plik do `/usr/bin` czy innej lokalizacji systemowej na Linuksie, to wyskoczyłaby informacja o&nbsp;braku pozwolenia. Chcąc tam kopiować pliki, trzeba dopisać na początku komendy `sudo` i&nbsp;spację, a&nbsp;po jej wykonaniu wpisać hasło."
%}

Od teraz wszystko działa jak powinno -- krótkie polecenie `echo 'Testowy tekst' | zbiornik | wc` da ten sam wynik w&nbsp;każdym folderze. W&nbsp;roli wisienki na torcie dam tu pełen schemat działania:

<img src="/assets/posts/konsola/rury/echo-rury-zbiornik-wc.jpg" alt="Spory schemat pokazujący, jak słowa 'Testowy tekst' wpadają do programu Echo. Z&nbsp;niego, już z&nbsp;oznaczeniem końca linii, lecą do nakładki podpisanej Zbiornik, połączonej z&nbsp;programem podpsanym Python. Stamtąd wylatuje sam tekst 'wy tekst' ze znakiem końca. Wpada do toalety podpisanej WC, a&nbsp;pod nią wyświetlają się trzy liczby"/>

## Podsumowanie

Czasem wystarczy kilka kroków, żeby stworzyć własny skrypt dobrze współpracujący z&nbsp;kultowymi klasykami Linuksa, jak `wc`. U&nbsp;mnie były to takie kroki:

* dodanie możliwości czytania z&nbsp;systemu danych wejściowych i&nbsp;wyjściowych (`sys.stdin` oraz `sys.stdout`),
* włączenie wykonywalności skryptu,
* dodanie magicznej linijki wskazującej ścieżkę do Pythona,
* umieszczenie skryptu w&nbsp;specjalnym, ogólnodostępnym folderze.

Efekt tego połączenia jest taki, że zaciera się granica między tym co systemowe, a&nbsp;tym co moje. Mogę przywoływać `zbiornik` jednym słowem i&nbsp;go łączyć z&nbsp;legendami Linuksa:

<pre class="black-bg mono">
echo 'Kap' | zbiornik | wc
</pre>

Do `wc` nie trafi nic, bo pojemność Zbiornika (5) była większa niż 4-bajtowe kapnięcie (trzy litery i&nbsp;znak końca linijki). Zatrzymał wszystko. Ale jeśli wpadnie coś większego, to liczarka nie będzie miała wolnego:

<pre class="black-bg mono">
echo 'Testowy tekst' | zbiornik | wc
</pre>

Gdybym chciał zapobiec przelaniu, nic nie stoi na przeszkodzie, żebym po prostu postawił na drodze więcej zbiorników:

<pre class="black-bg mono">
echo 'KapKap' | zbiornik | zbiornik | wc
</pre>

Mogę też skierować przelewające się dane do jakiegoś niefortunnego pliku :smiling_imp:

<pre class="black-bg mono nospace">
echo 'Duża ilość wody' | zbiornik >> moja_piwnica.txt
</pre>

{:.figcaption}
Znak `>` to również taka rura, tylko że kierująca dane do pliku, a&nbsp;nie programu. Z&nbsp;kolei użycie podwójnego znaku (`>>`) dopisuje dane do końca pliku, zamiast całkiem go nadpisywać.

Potencjał Linuksa jest ogromny. Jak wspomniałem na początku, konsola nie jest żadną koniecznością. Ale znając parę zasad, można szybko i&nbsp;sprawnie tworzyć własne rzeczy, integrować je ze sobą i&nbsp;dopasować urządzenie do własnych potrzeb i&nbsp;zachcianek. Zyskać poczucie wolności, o&nbsp;jakie czasem coraz trudniej na tym świecie :smile:

I na tym skończę główną część wpisu. Dalej będzie już parę możliwych usprawnień, które pozwoliłyby jeszcze lepiej wykorzystać potencjał konsolki (a&nbsp;dokładniej strumienie błędów oraz argumenty).

Swoją drogą... Mój Zbiornik to takie trochę ponowne wynalezienie *koła*{:.corr-del} [`cut`](https://stackoverflow.com/questions/971879/what-is-a-unix-command-for-deleting-the-first-n-characters-of-a-line)a -- programiku ucinającego kilka pierwszych wskazanych rzeczy.

## Bonus: możliwe modyfikacje

Załóżmy, że podczas działania Zbiornika chciałbym również wyświetlać w&nbsp;konsoli jakieś informacje. Na przykład ostrzec użytkowników, że danych było sporo i&nbsp;się przelały.

Ale, ze względu na specyfikę programu, mam tu utrudnione zadanie. Gdybym użył typowego `print('komunikat')` z&nbsp;Pythona, to tekst zostałby *dołączony* do wylatujących danych i&nbsp;wskazania `wc` byłyby zawyżone.

Rozwiązaniem może tu być (nad-)użycie **wyjścia na błędy**. To taka osobna przegródka, poza głównym strumieniem danych. Wrzucone tu komunikaty wyświetlą się użytkownikom (może nawet w&nbsp;szczególnym kolorze, jeśli tak sobie ustawili), ale nie wpłyną na główny przepływ.

Żeby kierować dane do tej przegrody, mogę dopisać do swojego kodu, tuż nad linijką z&nbsp;`sys.stdout`:

```python
sys.stderr.write( 'Przelało się!\n' )
```

{:.post-meta}
Znak końca linii dodaję tu wprost, bo domyślnie by go nie było.

Innym przydatnym usprawnieniem byłaby **możliwość przyjmowania argumentów**. Żeby dało się, przez dopisanie jednej krótkiej rzeczy, zmieniać działanie programu. I&nbsp;na przykład wskazywać, że dany zbiornik ma mieć pojemność inną niż domyślna.

W tym celu warto sięgnąć do zmiennej `sys.argv`, która jest listą *argumentów* związanych z&nbsp;danym programem.  
Jeśli użyjemy Zbiornika luzem, to ta lista będzie zawierała tylko jeden element, nazwę programu. Ale jeśli po tej nazwie coś w&nbsp;konsoli dopiszemy, oddzielając to spacjami, to lista się odpowiednio rozrośnie.

Wniosek? Możemy sobie przyjąć konwencję, że drugi argument (jeśli jest) zawsze traktujemy jak liczbę narzucającą pojemność zbiornika. I&nbsp;dopisujemy w&nbsp;kodzie, pod pierwszym określeniem `empty_space`, ale nad pętlą:

```python
if len(sys.argv) == 2:
    empty_space = int(sys.argv[1])
```

{:.figcaption}
Lojalnie uprzedzam: kod czysto ilustracyjny, z&nbsp;zerową odpornością na rzeczy nietypowe. Jeśli użytkownik wpisze w&nbsp;konsoli coś innego niż dodatnią liczbę, to się wszystko posypie.

Efekt? Jeśli chcemy, możemy od teraz dopisywać po zbiorniku jego pojemność. I, jeśli zajdzie taka potrzeba, postawić na drodze przepływu większy zbiornik:

```
echo 'KapKap' | zbiornik 10 | wc
```

...A gdybyśmy chcieli tworzyć bardziej złożone programy konsolowe, z&nbsp;własnymi podprogramami lub wbudowaną instrukcją, to Python ma w&nbsp;zanadrzu moduł `argparse`.

To tyle na dziś! Na koniec zachęcam do osobistej zabawy z&nbsp;przykładem i&nbsp;dodawania nowych bajerów. Przez zabawę najfajniej przełamać niechęć do konsoli, wiem coś o&nbsp;tym :wink:

Do zobaczenia w&nbsp;kolejnych, już bardziej aferowo-prywatnościowych wpisach! Setka już jest, to czas na marsz po&nbsp;128.
