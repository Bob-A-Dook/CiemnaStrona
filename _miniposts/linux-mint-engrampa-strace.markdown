---
layout: page
title: Co rozpakowuje pliki na systemie Linux Mint MATE? Małe śledztwo
description: "Otwieranie ZIP-a może być ciekawsze niż jego zawartość."
---

W tym miniwpisie opiszę historię z&nbsp;życia -- przypadek, kiedy skorzystałem z&nbsp;paru konsolowych programów załączonych do Linuksa.  
Dzięki nim zajrzałem „pod maskę” przyjaznego interfejsu pewnego programu i&nbsp;znalazłem sposób na odtworzenie jego działania we własnym, minimalistycznym skrypcie.

{:.post-meta .bigspace-after}
A jako wątek poboczny -- obecność jawnego tekstu haseł w&nbsp;niektórych wynikach programu *strace*.

## Spis treści

* [Opis problemu](#opis-problemu)
* [Śledztwo](#śledztwo)
  * [Ustalenie nazwy programu (*xprop*)](#ustalenie-nazwy-programu-xprop)
  * [Krótka lektura dokumentacji](#krótka-lektura-dokumentacji)
  * [Program pod obserwacją (*strace*)](#program-pod-obserwacją-strace)
  * [Przeszukanie zapisków (*grep*)](#przeszukanie-zapisków-grep)
* [Kwestia prywatności](#kwestia-prywatności)
* [Podsumowanie](#podsumowanie)

## Opis problemu

Miałem pewne spakowane, zabezpieczone hasłem archiwum w&nbsp;formacie ZIP. Dajmy na to: `archiwum.zip`. Wewnątrz niego różne pliki, z&nbsp;którymi chciałem coś porobić.

System Linux Mint (wariant MATE), z&nbsp;którego korzystam, jest bardzo przyjazny codziennym użytkownikom. Mógłbym łatwo rozpakować plik najzwyklejszym klikaniem.

W tym celu wystarczyłoby odnaleźć archiwum w&nbsp;przeglądarce plików, kliknąć je prawym przyciskiem myszy i&nbsp;wybrać opcję `Rozpakuj tutaj`.

{:.bigspace}
<img src="/assets/tutorials/mint-mate-engrampa-strace/linux-mint-mate-rozpakowywanie.png" alt="Zrzut ekranu pokazujący fragment rozwijanego menu po kliknięciu na plik ZIP. Widać tam opcję rozpakowania plików"/>

W związku z&nbsp;tym, że to ZIP chroniony hasłem, pojawia się okno z&nbsp;prośbą o&nbsp;jego wpisanie. Jeśli podam poprawne, to zaczyna się rozpakowywanie archiwum. Obok jego ikony pojawią się wszystkie zawarte w&nbsp;nim pliki i&nbsp;foldery.

{:.bigspace}
<img src="/assets/tutorials/mint-mate-engrampa-strace/linux-mint-mate-rozpakowywanie-haslo.png" alt="Zrzut ekranu pokazujący okno proszące o&nbsp;podanie hasła do pliku ZIP"/>

Parę razy rozpakowałem archiwa ręcznie, właśnie w&nbsp;taki sposób. Ale kiedy się okazało, że będę musiał to robić częściej -- wraz z&nbsp;powtarzalnymi działaniami na wypakowanych plikach -- to wewnętrzny leniuch rzekł stanowczo: „automatyzujmy”.

A do tego przydałyby mi się nazwy programów do wpisywania w&nbsp;konsolę. Zaczęło się szperanie.

### Unzip i&nbsp;mylny trop

Wyszukałem w&nbsp;sieci odpowiedzi na pytanie w&nbsp;stylu: „jak rozpakować plik ZIP na systemie Linux”? Któraś z&nbsp;odpowiedzi zasugerowała programik `unzip`.

Użyłem go przez konsolę na swoim zahasłowanym pliku. O&nbsp;dziwo zadziałało nawet bez pytania o&nbsp;hasło, rozpakowało zawartość... Tyle że były tam same foldery. Nie było natomiast żadnych *plików*, na których mi zależało.

{% include info.html
type="Wątek prywatnościowy"
text="Nawet plik ZIP zabezpieczony hasłem zawiera na widoku nazwy i&nbsp;hierarchię zawartych w&nbsp;sobie plików i&nbsp;folderów.  
To dlatego `unzip` mógł odtworzyć strukturę folderów -- do tego wystarczą same ścieżki. Ale pliki już były zaszyfrowane, więc ich nie tknął.  
Wniosek: **lepiej nie umieszczać żadnych wrażliwych informacji w&nbsp;nazwach plików wrzucanych do archiwów** :wink:  
Pomijam już to, że samo hasło do pliku też nieraz łatwo złamać metodami siłowymi, zwłaszcza jeśli zawęzi się przestrzeń możliwości. Fajnie to pokazał [ten wpis](https://informatykzakladowy.pl/lamiemy-haslo-do-szyfrowanego-pdf-a/) Informatyka Zakładowego."
%}

Skoro ogólnie *unzip* działał, a&nbsp;jedynym problemem było hasło, to kolejna rzecz do wyszukania: „jak rozpakować przez *unzipa* plik chroniony hasłem”. Wpisałem takie coś i... [okazało się, że raczej się nie da](https://stackoverflow.com/a/60550751). Nie przy tym programie i&nbsp;tym szyfrowaniu.

## Śledztwo

Tam, gdzie *unzip* poległ, domyślny program Minta dawał radę. Przyjmował hasło i&nbsp;rozpakowywał archiwum. Jak? Czy dałoby się w&nbsp;prosty sposób włączyć go w&nbsp;moją automatyzację?  
Szukając odpowiedzi na te pytania, rozpocząłem krótkie śledztwo.

### Ustalenie nazwy programu (*xprop*)

Zależało mi na nazwie programu, jakiemu odpowiadało okienko interfejsu pytające o&nbsp;hasło.

Mógłbym teoretycznie kliknąć pierwszą opcję z&nbsp;menu z&nbsp;pierwszego screena. Jest tam o&nbsp;otwarciu archiwum, więc mógłbym założyć, że pojawi się ten sam program, który rozpakowuje. Po jego uruchomieniu zajrzałbym w&nbsp;zakładkę `O programie` i&nbsp;poznał nazwę.

Ale nie zawsze jest możliwość prostego przejścia od okna/opcji do programu. Sposobem bardziej uniwersalnym jest uruchomienie konsoli/terminala (np. kombinacją `Ctrl+Alt+T`) i&nbsp;użycie polecenia:

```
xprop | grep WM_CLASS
```

Są tu dwa programiki: `xprop` od sprawdzania informacji o&nbsp;wskazanym oknie, `grep` od wyszukiwania tekstu (tu: *WM_CLASS*). Rura między nimi sprawia, że informacje ustalone przez pierwszy lecą do drugiego.

Kursor zmienił się w&nbsp;plusa. Kiedy kliknąłem okno pytające o&nbsp;hasło, wyświetliła się nazwa stojącego za nim programu:

{:.post-meta}
```
WM_CLASS(STRING) = "engrampa", "Engrampa"
```

**_Engrampa_**. Nazwa trochę kojarzy mi się z&nbsp;[n-gramami](https://pl.wikipedia.org/wiki/N-gram), trochę z&nbsp;dziadkiem -- i&nbsp;faktycznie program jest już nieco leciwy. Ale wciąż sprawny.

### Krótka lektura dokumentacji

Wiedziałem z&nbsp;doświadczenia, że programy mają czasem dwa oblicza:

* Graficzne

  Uruchamiane przez kliknięcie jakiejś ikony wewnątrz systemu; czasem również przez wpisanie w&nbsp;konsolę samej nazwy programu.

* Konsolowe

  Dopisując po nazwie programiku dodatkowe opcje, da się z&nbsp;niego korzystać w&nbsp;sposób niestandardowy, na przykład robiąć coś całkowicie w&nbsp;tle, bez interfejsu graficznego.

Gdybym po prostu wpisał w&nbsp;konsolę `engrampa archiwum.zip`, to otwarłoby interfejs graficzny od przeglądania -- nawet nie znajome okno pytające o&nbsp;hasło.  
Ja natomiast liczyłem na możliwość zrobienia czegoś takiego:

{:.red .post-meta}
```
engrampa --password=HASŁO archiwum.zip
```

Czy moje oczekiwania miały szansę się spełnić? Nie wiedziałem tego, bo każdy program może działać po swojemu. Musiałem poznać możliwości Engrampy. Na przykład takim poleceniem.

<div class="black-bg mono nospace">
engrampa --help
</div>

{% include details.html summary="Parę uwag" %}
Nie każdy program da się wołać samą nazwą. Żeby się dało, musi się znajdować w&nbsp;którymś z&nbsp;[folderów szybkiego dostępu](/2024/12/09/rury-wprowadzenie#ulepszenie-wzywanie-zdowolnego-miejsca){:.internal}. W&nbsp;innym razie trzeba podać jego pełną ścieżkę.

Poza tym nie każdy wyświetla dostępne opcje po dopisaniu `--help`. To popularna konwencja, ale nie wszyscy twórcy się jej trzymają.

Przy Engrampie miałem to szczęście, że obie rzeczy się sprawdziły.

{% include details-end.html %}

Wyświetliło mi garść informacji po angielsku. W&nbsp;tym jedną z&nbsp;dostępnych opcji, która brzmiała interesująco:

{:.post-meta}
```
-h, --extract-here
              Extract archives using the archive name as destination folder and quit the program
```

Opcja `--extract-here` pasowała idealnie do tego, co chciałem zrobić. Ale używając jej na swoim archiwum, po prostu przywołałem znajome okno pytające o&nbsp;hasło.  
Nie było to samo w&nbsp;sobie takie złe. Tyle że mnie, przypomnę, najbardziej pasowałoby rozwiązanie w&nbsp;całości konsolowe.

Spróbowałem jeszcze zajrzeć do dokładniejszej instrukcji, wpisując:

<div class="black-bg mono nospace">
man engrampa
</div>

{:.figcaption}
Programik [`man`](https://en.wikipedia.org/wiki/Man_page) (skrót od *manual*) to uniwersalny sposób na otwarcie instrukcji programów konsolowych.

W tym wypadku instrukcja była dość lakoniczna i&nbsp;zawierała właściwie te same informacje co skrócona pomoc konsolowa.

Na tym etapie mógłbym odpuścić i&nbsp;pogodzić się z&nbsp;tym, że moją automatyzację będzie przerywało jedno graficzne okno. Albo znaleźć inny program rozpakowujący.  
Ale postanowiłem trochę drążyć. Sięgnąłem po program konsolowy **`strace`**.

### Program pod obserwacją (*strace*)


*Strace* to linuksowy odpowiednik agenta wysyłanego na przeszpiegi. Notującego z&nbsp;ukrycia wszystko, o&nbsp;co Engrampa prosi jądro systemu. Może to pozwoli rozpracować naszego odpakowywacza.

Żeby użyć *strace'a*, wystarczy dopisać po nim komendę, którą chciałoby się śledzić. Odpowiednie polecenie dla Engrampy ustaliłem parę akapitów wyżej. Dodałem jeszcze parę parametrów dla *strace'a* i&nbsp;uzyskałem takie polecenie:

<pre class="black-bg mono">
strace -f -o zapis.txt <span style="color:#59bc6d">engrampa --extract-here archiwum.zip</span>
</pre>

{:.post-meta .bigspace-after}
Kolorem zielonym wyróżniłem polecenie dla Engrampy. Reszta dotyczy samego *strace'a*.  
Argument `-f` rozszerza zakres monitoringu o&nbsp;procesy tworzone przez ten śledzony. Z&nbsp;kolei `-o` wskazuje plik, do którego mają trafić zapiski. Nazwa *zapis.txt* całkowicie subiektywna.

Po wykonaniu polecenia uruchomiło się to samo okienko pytające o&nbsp;hasło co poprzednio. Wpisałem je, poczekałem aż rozpakuje mi ZIP-a. Programik z&nbsp;powodzeniem zakończył działanie, a&nbsp;*strace* skończył notować.

W folderze, w&nbsp;którym użyłem konsoli, powstał plik liczący aż 4,5 MB. Szczegółowy zapis wszystkich interakcji Engrampy z&nbsp;systemem podczas tej krótkiej sesji.

### Przeszukanie zapisków (*grep*)

Miałem pełną historię, mogłem teraz wyciągnąć z&nbsp;niej różne informacje.

Tak duży plik byłby jednak uciążliwy do przeglądania w&nbsp;domyślnym *Notatniku*{:.corr-del} Xedzie. Nawet przez programik `less`, który ładuje pliki na raty, ręczne szukanie byłoby żmudne.

Może dałoby się wyjść od czegoś jak najbliżej momentu rozpakowania?  
Wiedziałem, jakie podałem hasło do ZIP-a, więc spróbowałem je sobie wyszukać w&nbsp;obszernych zapiskach:

```
grep HASŁO zapis.txt
```

...I faktycznie, wyskoczyło kilka linijek, w&nbsp;których się pojawiło! Aż się zdziwiłem.

Kilka pierwszych, zawierających różne ścieżki, kończyło się tekstem `Nie ma takiego pliku ani katalogu`. Sugeruje to, że *strace* bezskutecznie szukał. Aż dotarło do linijki, która chyba zakończyła się sukcesem:

<div class="black-bg mono nospace">
execve("/usr/lib/7zip/7z", ["/usr/lib/7zip/7z", "x", "-bd", "-bb1", "-y", "-p<span class="red">HASŁO"</span>, "-o<span class="post-meta">/home/mint/demo/archiwum</span>", "--", "<span class="post-meta">/home/mint/demo/archiwum</span>.zip"], 0x576555d87ee8 /* 52&nbsp;vars */) = 0
</div>

{:.figcaption}
Włączyłem zawijanie tekstu, żeby wszystko się zmieściło, za cenę lekkiego chaosu; ciemniejszym szarym wyróżniłem ścieżki, czerwonym hasło.

Początek linijki, `execve`, wskazuje na wołanie przez śledzony proces Engrampy innego programu.

Pierwszą rzeczą w nawiasie jest ścieżka wołanego programu (gdzie `/usr/lib/7zip` to ścieżka do folderu, zaś `7z` to konsolowa nazwa [popularnego programu *7-Zip*](https://pl.wikipedia.org/wiki/7-Zip)).

Potem miałem serię nawiasów kwadratowych. A&nbsp;to, co między nimi, było tak naprawdę pełną listą opcji (*argumentów*) przekazanych „podwykonawcy”, czyli 7-Zipowi.

Mogłem to sobie skopiować, oczyścić z&nbsp;cudzysłowów podwójnych oraz przecinków, zastąpić ścieżki zmiennymi... i&nbsp;tak oto zdobyłem **polecenie rozpakowujące plik**.

<pre class="black-bg mono">
/usr/lib/7zip/7z x&nbsp;-bd -bb1 -y -p<span class="red">HASŁO</span> -o<span class="post-meta">PLIK</span> -- <span class="post-meta">PLIK</span>.zip
</pre>

{% include details.html summary="Omówienie" %}

Znaczenie większości opcji z&nbsp;komendy (zwanych zwyczajowo *argumentami*) mogłem łatwo poznać, wpisując `7z --help`. I&nbsp;tak oto, po kolei:

* `/usr/lib/7zip/7z` to po prostu pełna ścieżka do programu *7-Zip* na moim Mincie.
* `x` każe programowi działać w&nbsp;trybie rozpakowywania plików.
* `-bd` ukrywa konsolowy wskaźnik postępów w&nbsp;rozpakowywaniu.
* `-bb1` wskazuje, jak szczegółowe (w&nbsp;skali od 0&nbsp;do 3, tu `1`) mają być informacje wyświetlane przez program.
* `-y` sprawia, że program nie pyta, czy na pewno chcę coś zrobić, tylko zawsze to robi.
* `-p` to hasło; tutaj zapisane od razu po nazwie argumentu, więc ciut się z&nbsp;nim zlewa.
* `-o` to ścieżka i&nbsp;nazwa folderu wyjściowego; tutaj taka sama jak nazwa archiwum (tyle że bez `.zip` na końcu).
* podwójna kreska (`--`) wskazuje, że to [koniec ustawiania opcji](https://unix.stackexchange.com/a/11382). Po niej jest już tylko główny „wsad” do programu -- ścieżka do archiwum.

{% include details-end.html %}

Użyłem na próbę tego polecenia (zamiast `HASŁO` dając oczywiście prawdziwe hasło do pliku, a&nbsp;zamiast `PLIK` jego pełną ścieżkę, ale bez rozszerzenia `.zip`).  
Zadziałało, moje archiwum zostało rozpakowane w&nbsp;aktywnym folderze. Bez udziału interfejsu graficznego. Programem domyślnie zainstalowanym na systemie.

## Kwestia prywatności

Choć możliwość wołania *7-Zipa* przez konsolę jest bardzo wygodna i&nbsp;fajnie się integruje ze skryptami, warto zwrócić uwagę na możliwą ciemną stronę tego ułatwienia.

Jak widać w&nbsp;powyższym przypadku -- **wynik _strace'a_ zawierał na widoku hasło, którego używałem do rozpakowania pliku**.

*Strace* dla wielu osób nie będzie czymś, z&nbsp;czego korzysta się na co dzień... Ale zdarza się, że po wrzuceniu swojego problemu z&nbsp;komputerem na forum publiczne dostaje się prośbę właśnie o&nbsp;wynik działania *strace'a* (bo jego szczegółowość ułatwia rozwiązywanie problemów). Szkoda by było, gdyby zaplątało się tam coś, czego się nie chce ujawniać.

{:.post-meta .bigspace-after}
Już nawet pomijam ten konkretny przykład z&nbsp;plikiem ZIP, bo ciężko mi sobie wyobrazić scenariusz, gdy ktoś daje innym i&nbsp;wynik _strace'a_, i&nbsp;ważny szyfrowany plik. Mówię tak ogólnie.

Widzę tu pewien potencjał na **tryb prywatny _strace'a_** albo chociaż nakładkę, która pozwoliłaby wyłapywać właśnie takie przypadki i&nbsp;nieco cenzurować zapiski.  
Przy okazji mogłaby ukrywać nazwę użytkownika, również widoczną wewnątrz ścieżek do plików i&nbsp;mogącą ujawniać tożsamość; u&nbsp;mnie był to tylko domyślny `mint`, u kogoś będzie `arek-przykładnik`.

{% include info.html
type="Ciekawostka"
text="Na Cinnamonie, czyli innym wariancie Minta, nie byłem w&nbsp;stanie powtórzyć działań z&nbsp;tego wpisu.  
Zamiast Engrampy jest tam inny program, o&nbsp;nazwie `file-roller` (wedle pliku pomocy: to na jego kodzie opiera się Engrampa). Wygląda ciut inaczej, dając między innymi możliwość wyświetlania hasła podczas wpisywania.  
...No i&nbsp;chyba więcej ukrywa, bo w&nbsp;zapiskach *strace'a* nie znalazłem ani wołania *7-Zipa*, ani użytego hasła. Ale dokładnego mechanizmu działania jeszcze nie rozgryzłem, więc różnica niekoniecznie gwarantuje prywatnościową przewagę Cinnamona."
%}

## Podsumowanie

Na systemie Linux Mint MATE interfejs graficzny od pracy z&nbsp;plikami ZIP nazywa się Engrampa. Wykonawcą jego woli, wysyłanym do praktycznej roboty, jest natomiast 7-Zip.

Jak się okazuje, *strace* był strzałem w&nbsp;dziesiątkę, pozwalającym nie tylko odkryć tę zależność, ale nawet bezpośrednio zdobyć polecenie konsolowe, pomijające interfejs graficzny.  
Mogłem je skopiować i&nbsp;wykorzystać wewnątrz własnego skryptu, żeby usprawnić pracę z&nbsp;zawartością archiwów.

Przy okazji wyszło na jaw, że w&nbsp;wynikach *strace'a* może się chować hasełko. Nie jest to może powód do bicia na alarm, ale warto to uwzględnić, udostępniając innym wyniki do celów debugowania.

{% include info.html
type="Podobne wpisy"
text="Niedawno próbowałem też zbadać, co się dzieje za kulisami [podczas zmiany języka na polski](/miniposts/cinnamon-klawiatura){:.internal} na systemie Mint Cinnamon.  
W tamtym przypadku sprawa okazała się nieco bardziej złożona i&nbsp;nie znalazłem szybkiego rozwiązania, więc jeszcze do niej wrócę.  
Tym niemniej: jest tam jeszcze więcej konsolowej analizy. Jak ktoś lubi, to zapraszam."
%}
