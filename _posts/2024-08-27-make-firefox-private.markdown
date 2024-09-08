---
layout: post
title: "Make Firefox Private Again – omówienie strony"
subtitle: "Lis zwęszył reklamy, ale mam go na smyczy."
description: "Lis zwęszył reklamy, ale mam go na smyczy."
date:   2024-08-27 08:00:00 +0100
tags: [Reklamy, Inwigilacja, Konsola]
firmy: [Facebook, Mozilla]
image:
  path: /assets/posts/open_source/firefox/make-firefox-private/make-firefox-private-baner.jpg
  width: 1200
  height: 700
  alt: "Mężczyzna z mema, mający zamiast głowy logo przeglądarki Firefox, kieruje się ku lewej stronie kadru, gdzie widać las jaskrawych billboardów. Zatrzymuje go ręką drugi mężczyzna, oznaczony jako wyłączona opcja dopasowywania reklam"
---

Od jakiegoś czasu krążyła mi po głowie myśl, żeby zrobić wpis pokazujący trochę ciemnych stron przeglądarki Firefox.

Mówię to jako jej wieloletni użytkownik, a&nbsp;zarazem [krytyk Google'a](/serie/google){:.internal}, wobec którego Firefox jest prywatniejszą, przyjazną alternatywą. Zresztą pozostaję stały w&nbsp;poglądach. Nadal planuję używać Lisa i&nbsp;punktować Wujka G... Ale na niektóre rzeczy wolę nie przymykać oka.

W każdym razie to jeszcze nie będzie ta przekrojowa krytyka. Pokażę tylko jedną dziwną akcję Firefoksa, która ostatnio zirytowała grono użytkowników. Prowadząc nawet do powstania tytułowej stronki, *Make Firefox Private Again*.

Najpierw będzie część bardzo lekka, czyli przybliżenie afery i&nbsp;proste rzeczy, które warto sobie wyklikać w&nbsp;opcjach, żeby wyłączyć reklamowe nowinki.

Potem będzie szczypta techniki. Omówię, na czym polegają skrypty ze stronki, która mnie do wpisu zainspirowała. Ale na tyle przystępnie, żeby było to strawne dla osób spoza cyfrowej bańki, za to obdarzonych ciekawością świata.

Zapraszam!

<img src="/assets/posts/open_source/firefox/make-firefox-private/make-firefox-private-baner.jpg" alt="Mężczyzna z&nbsp;mema, mający zamiast głowy logo przeglądarki Firefox, kieruje się ku lewej stronie kadru, gdzie widać las jaskrawych billboardów. Zatrzymuje go ręką drugi mężczyzna, oznaczony jako wyłączona opcja dopasowywania reklam."/>

{:.figcaption}
Źródło: popularny [mem](https://knowyourmeme.com/photos/1454482-bro-not-cool) na podstawie reklamy Gillette, logo Firefoksa, billboardy wygenerowane przez Binga. Aranżacja moja.

## Spis treści

* [Część całkiem nietechniczna](#część całkiem-nietechniczna)
  * [Zwrot Firefoksa ku reklamom](#zwrot-firefoksa-ku-reklamom)
  * [Gdy nie pytasz, to nie odmówią](#gdy-nie-pytasz-to-nie-odmówią)
  * [Wyłączanie nowych ustawień](#wyłączanie-nowych-ustawień)
  * [Sposób alternatywny](#sposób-alternatywny)
* [Przystępna część techniczna](#przystępna-część-techniczna)
  * [Ogólnie o stronce](#ogólnie-ostronce)
  * [Echo](#echo)
  * [Uproszczenie pierwszej linijki](#uproszczenie-pierwszej-linijki)
  * [Tee](#tee)
  * [Dopasowanie do działania Firefoksa](#dopasowanie-do-działania-firefoksa)
  * [Zmienna $HOME](#zmienna-home)
  * [Grep](#grep)
  * [Cut](#cut)
  * [Podsumowanie w&nbsp;formie schematu](#podsumowanie-wformie-schematu)
* [Wątki poboczne](#wątki-poboczne)
  * [Wątek cyber(nie)bezpieczeństwa](#wątek-cyberniebezpieczeństwa)
  * [Świat majsterkowania z&nbsp;*user.js*](#świat-majsterkowania-zuserjs)

## Część całkiem nietechniczna

### Zwrot Firefoksa ku reklamom

Zacznę od ogólnych informacji z&nbsp;nowopowstałej stronki, *Make Firefox Private Again* (będę czasem skracał do *MFPA*).  
Autor, uzasadniając jej powstanie, linkuje między innymi do [wpisu](https://blog.mozilla.org/en/mozilla/privacy-preserving-attribution-for-advertising/) z&nbsp;oficjalnego bloga Mozilli, firmy tworzącej Firefoksa.

Wpis wspomina o&nbsp;tym, że **Firefox zaczął współpracę z&nbsp;firmą Meta nad nowym modelem reklam**, rzekomo „szanujących prywatność”.

{:.bigspace}
> Advertising provides critical support for the Web. We’ve been looking to apply privacy preserving advertising technology (...)  
For the last few months we have been working with a&nbsp;team from Meta (formerly Facebook) on a&nbsp;new proposal that aims to enable conversion measurement – or attribution – for advertising called **Interoperable Private Attribution, or IPA**.

Gdyby chodziło o&nbsp;zwykłe, „martwe” obrazki, dodawane do stron internetowych na wzór plakatów i&nbsp;billboardów, to jeszcze pół biedy. Ale mowa o&nbsp;tzw. reklamach śledzących, które analizują działania użytkowników i&nbsp;dopasowują się do nich.

Firefox ramię w&nbsp;ramię z Facebookiem, w&nbsp;interesie reklamodawców? Gorzka coś ta IPA i&nbsp;trudna do przełknięcia.  
Ale czemu nie zaciekawiło to innych, czujniejszych ode mnie osób? Nie wznieciło ognia buntu, choć post ma już swoje lata, pochodzi z&nbsp;2022 roku?

Może dlatego, że firma Mozilla z&nbsp;wieloma rzeczami eksperymentowała. Pocket, Mozilla Location Services, [Deepspeech](https://github.com/mozilla/DeepSpeech) od komputerowego rozpoznawania mowy, [wirtualna rzeczywistość](https://blog.mozilla.org/en/products/firefox/firefox-reality-now-available/), że tak wymienię parę przykładów. Nie wszystkie doprowadzili do końca, z&nbsp;niektórych się wycofali. Eksperymenty z&nbsp;reklamami mogły zostać uznane za jedną z takich inicjatyw i&nbsp;przemknąć bez protestów.

Ogólnikowo o&nbsp;nowej propozycji: ma polegać na tym, że przeglądarka będzie stała między użytkownikami a&nbsp;reklamodawcami okupującymi wiele stron internetowych. Ma im ujawniać na życzenie pewne informacje o&nbsp;skuteczności reklam. Ponoć jedynie zagregowane, uśrednione dla większych grup osób.

W ten sposób reklamodawcy nie powinni być w&nbsp;stanie ustalić: „ta osoba była wcześniej na stronach X&nbsp;i&nbsp;V, a&nbsp;na stronie Z&nbsp;podała swoje imię i&nbsp;nazwisko, czyli...”, jak to obecnie mogą zrobić, opierając się głównie na *plikach cookies* (tutaj [dokładniejszy opis]({% post_url 2021-12-08-cookies-piksele-sledzace %}){:.internal} tej metody śledzenia).

Zmiana na lepsze? Nie jestem przekonany. Podejście Mozilli wydaje się opierać na *appeasemencie*, ugłaskaniu reklamodawców. Zakłada, że wybiorą wygodną opcję *zamiast* tradycyjnego, inwazyjnego śledzenia.  
Tymczasem dotychczasowa zachłanność *ad techu* sugerowałaby raczej, że będą zbierali, co tylko się da (jak nie przez pliki cookies, to przez [bardziej inwazyjne metody]({% post_url 2022-05-03-javascript2 %}){:.internal}). A&nbsp;łagodniejszych reklam od Firefoksa użyją *oprócz* tego.

### Gdy nie pytasz, to nie odmówią

Nawet gdybym widział potencjał w&nbsp;samej strategii... Za nic nie mogę zaakceptować innej rzeczy, o&nbsp;której autor *Make Firefox...* akurat nie napisał. W&nbsp;ramach ostatniej aktualizacji **Firefox domyślnie włączył eksperymentalny model reklam, nie informując użytkowników**.

Nie było żadnego pytania o&nbsp;zgodę. Ba, nie było nawet informacji o&nbsp;fakcie dokonanym. Mimo że po każdej aktualizacji pojawia się zwięzły ekran z&nbsp;informacjami, który byłby idealnym miejscem na wzmiankę.  
Po prostu wśród opcji programu po aktualizacji do wersji 128&nbsp;pojawiła się nowa. [Domyślnie włączona](https://support.mozilla.org/en-US/kb/privacy-preserving-attribution).

Jeśli dodać do tego parę innych faktów -- jak to, że firma Mozilla zwolniła parę lat temu część ekipy od przeglądarki, podczas gdy pani prezes podwyższyła sobie wynagrodzenie [do poziomów kilkumilionowych](https://www.reddit.com/r/browsers/comments/yy986k/can_someone_explain_why_mozillas_ceo_salary/) -- to zrozumiałe stają się obawy przed możliwą korporatyzacją Firefoksa.

{% include info.html
type="Ciekawostka"
text="Stronka MFPA linkuje też do [artykułu](https://www.theregister.com/2024/06/18/mozilla_buys_anonym_betting_privacy/) z&nbsp;portalu *The Register* z&nbsp;czerwca tego roku. Wspomina on o&nbsp;zakupie przez Mozillę firmy Anonym, zajmującej się właśnie „prywatnymi reklamami”.  
Z drugiej strony dyrektor ds. technicznych z&nbsp;Mozilli [wypowiedział się na forum Reddit](https://www.reddit.com/r/firefox/comments/1e43w7v/a_word_about_private_attribution_in_firefox/) i&nbsp;pisze wprost, że dodany chyłkiem „prywatny pomiar reklam” nie ma związku z&nbsp;zakupem Anonyma.  
W związku z&nbsp;tym proponuję potraktować tę sprawę jako wątek poboczny. Który jednak potwierdzałby tezę, że Firefox wyszedł w&nbsp;sprawie reklam poza luźne eksperymenty."
%}

W internecie pojawiło się sporo poradników mówiących, w&nbsp;jaki sposób wyłączyć nową opcję. Jedno z&nbsp;rozwiązań zaproponował autor *Make Firefox...*.  
Jest ono jednak nieco bardziej *hakierskie* i&nbsp;działa tylko na systemie Linux. Dlatego zostawię je na potem. Póki co opiszę, jak osiągnąć niemal ten sam efekt w&nbsp;parę kliknięć, przez ustawienia samego Firefoksa.

### Wyłączanie nowych ustawień

Na szczęście Firefox nie robi żadnych problemów z&nbsp;wyłączeniem nowej opcji. Wystarczy kliknąć w&nbsp;ikonę trzech kresek w&nbsp;górnym prawym rogu, a&nbsp;potem wejść w&nbsp;`Ustawienia`.

{:.bigspace}
<img src="/assets/posts/open_source/firefox/make-firefox-private/firefox-zakladka-ustawienia.jpg" alt="Zrzut ekranu pokazujący górny prawy róg programu Firefox oraz opcje, jakie należy kliknąć"/>

Następnie po lewej stronie należy kliknąć zakładkę `Prywatność i bezpieczeństwo`.

{:.figure .bigspace}
<img src="/assets/posts/open_source/firefox/make-firefox-private/firefox-zakladka-prywatnosc.jpg" alt="Zrzut ekranu pokazujący zaznaczony na niebiesko tekst 'Prywatność i&nbsp;bezpieczeństwo'"/>

Na koniec trzeba znaleźć i&nbsp;odhaczyć odpowiednią funkcję.

{:.bigspace}
<img src="/assets/posts/open_source/firefox/make-firefox-private/firefox-wylaczanie-reklam.jpg" alt="Zrzut ekranu z&nbsp;opcji, pokazujący wyłączoną funkcję dopasowywania reklam"/>

I tyle! Co pewien czas, zwłaszcza po aktualizacji, można dla pewności sprawdzać, czy Mozilla przypadkiem nie przywróciła opcji. Gdyby to zrobili, to już oficjalnie poszliby w&nbsp;ślady Microsoftu czy Google'a.

### Sposób alternatywny

Firefox pozwala zmieniać swoje ustawienia na kilka sposobów. Żeby osiągnąć ten sam efekt co wyżej, ale potencjalnie trwalszy (opisana wyżej opcja stała się u&nbsp;mnie szara, nieklikalna), można również:

* wpisać w&nbsp;górny pasek, tam gdzie są zwykle adresy stron, `about:config`,
* zamknąć jednym kliknięciem rutynowe ostrzeżenie,
* zacząć wpisywać obok ikony lupy  
 `dom.private-attribution.submission.enabled`  
  (już po kilku pierwszych literkach na ekranie powinna pozostać jedyna pasująca opcja),
* kliknąć opcję, aby zmieniła wartość na `false`.

Na tym koniec części najważniejszej dla codziennych użytkowników. Ale zachęcam do pozostania ze mną, mimo że pojawi się teraz odrobina konsoli. Zawsze to jakiś wgląd do Firefoksa oraz świata automatyzacji i&nbsp;zlecania brudnej roboty skryptom :smile:

## Przystępna część techniczna

### Ogólnie o&nbsp;stronce

Adres stronki to, przypomnę, *[https://make-firefox-private-again.com/](https://make-firefox-private-again.com/)*.  
Po jej załadowaniu ukazuje się prosty, czarny tekst na białym tle. Nietypowa, prosta szata graficzna? Nie; **to tak naprawdę plik tekstowy. Skrypt w&nbsp;języku Bash**.

{% include info.html
type="Uwaga"
text="Choć sam autor o&nbsp;tym nie wspomina, takie skrypty są przeznaczone z&nbsp;założenia dla systemu Linux. Dlatego żadna z&nbsp;instrukcji nie zadziałałaby na zwyczajnym Windowsie.  
Poza tym skrypt nie zadziałałby też na smartfonach z&nbsp;Androidem, wewnątrz apki [Termux](/tutorials/termux){:.internal}. Choć jest tam konsola i&nbsp;potrzebne programiki, przeszkodą są zabezpieczenia Androida. Aplikacje nie mogą ingerować w&nbsp;wewnętrzne pliki innych aplikacji. A&nbsp;skrypt ze strony musi zajrzeć do folderów Firefoksa, żeby zadziałać."
%}

Raczej nikogo nie zdziwi fakt, że przeglądarka umie otwierać inne rzeczy niż strony internetowe. W&nbsp;końcu może otwierać nawet pliki PDF, jak [ten losowy przykład](https://research.mozilla.org/files/2018/04/The-Effect-of-Ad-Blocking-on-User-Engagement-with-the-Web.pdf). O&nbsp;ile ktoś ręcznie nie zmieniał opcji, to takie pliki wyświetlą się w&nbsp;trybie specjalnie pod PDF-y. W&nbsp;prostym czytniku.

Zaskoczenie może natomiast budzić fakt, że w&nbsp;górnym pasku nie ma tu żadnej nazwy, która by sugerowała plik tekstowy. Jest tam tylko adres: `https://make-firefox-private-again.com/`.

To dlatego, że ścieżka z&nbsp;górnego paska jest tak naprawdę czymś innym, niż w&nbsp;świadomości codziennych użytkowników.  
Intuicyjnie można powiedzieć, że przeglądarka mówi górnym paskiem: „oto, o&nbsp;co poprosiłam czyjś serwer”. Reszta ekranu, pod paskiem, wskazuje z&nbsp;kolei: „oto rzecz, którą dostałam w&nbsp;odpowiedzi, plus wszystkie elementy powiązane”.  
Zwykle między tymi dwiema rzeczami jest zgodność. Ale nie zawsze.

{% include info.html
type="Ciekawostka"
text="W naturze trafiają się też odwrotne sytuacje -- gdy link sugeruje nietypowy plik, a&nbsp;dostajemy zwykłą stronę internetową.  
W przypadku Facebooka niektóre linki kończą się na przykład na `profile.php` (plus zwykle dodatkowe parametry po znaku zapytania). A&nbsp;jednak po kliknięciu nasza przeglądarka wyświetla nie skrypt w&nbsp;języku PHP, tylko jakąś stronę internetową."
%}

Wyświetlony skrypt jest dość krótki, więc dla wygody załączam jego screena:

{:.figure .bigspace-before}
<img src="/assets/posts/open_source/firefox/make-firefox-private/make-firefox-private-skrypt.jpg" alt="Oznaczona kolorami, pełna treść skryptu ze strony Make Firefox Private Again. Poza pierwszymi dwoma linijkami wszystko jest zaznaczone na niebiesko, jako komentarze"/>

{:.figcaption}
Źródło: cała zawartość *Make Firefox Private Again*. Kolorowanie składni w&nbsp;programie Gedit. Górne linijki rozpoczynające się słowem `echo` są zawinięte dla czytelności, ale tak naprawdę są tylko dwie.

Najważniejsza informacja na początek -- za podstawową jednostkę w&nbsp;skryptach Basha można uznać linijki tekstu. W&nbsp;każdej z&nbsp;tych linijek **tekst po krzyżyku (`#`) to komentarz**, który zostanie przez konsolę zignorowany. Jest przeznaczony dla czytelników.

{:.post-meta .bigspace-after}
Jak często bywa: istnieją wyjątki, a&nbsp;„specjalność” krzyżyków może być czasem wyłączona. Ale w&nbsp;tym przykładzie zawsze, bez wyjątku, oznaczają komentarze.

Wniosek? Skrypt składa się tak naprawdę tylko z&nbsp;dwóch linijek. Tych u&nbsp;góry. Reszta to czytelne instrukcje dla użytkownika. Dobrze to widać, jeśli otworzy się plik w&nbsp;jakimkolwiek programie rozpoznającym i&nbsp;kolorującym składnię, jak Gedit z&nbsp;przykładu wyżej.

### Echo

To teraz czas omówić te dwie linijki. Zacznę od drugiej, krótszej:

```
echo 'Restart Firefox for the change to have effect'
```

Pierwsza po lewej jest nazwa programu -- `echo`.  
Potem jest spacja, która oddziela nazwę programu od *argumentów*, czyli wrzucanych do niego rzeczy.  
Na końcu jest tekst, który można poznać po obecności cudzysłowów na początku i&nbsp;końcu. Jest traktowany jak pojedynczy element, niepodzielny i&nbsp;nierozbijany na spacjach.

Konsola jest miejscem, w&nbsp;którym można wpisywać nazwy programów albo wrzucanych do nich rzeczy, ewentualnie specjalne zmienne. Nic więcej. Jeśli wpisze się luzem nazwę, której nie ma w&nbsp;bazie rzeczy dopuszczalnych, to wyskoczy błąd.

Jak zatem wprowadzić do konsoli zwykły tekst, niemający dla niej specjalnego znaczenia? **Trzeba go przemycić jako „wsad” do któregoś z&nbsp;dozwolonych programów**. Wiele osób, tak jak autor stronki w&nbsp;tym skrypcie, wykorzystuje do tego celu Echo. Minimalistyczny program, który po prostu podaje tekst dalej.

Przy prostej postaci `echo TEKST` nie będą się z&nbsp;tym tekstem działy żadne szczególne rzeczy. Przeleci sobie przez „układ pokarmowy” konsoli i trafi do wyjścia. Najczęściej: wyświetli się na ekranie.

Wniosek? Linijka druga oznacza po prostu, że po wykonaniu linijki pierwszej wyświetli się tekst „*Restart Firefox for the change to have effect*”.

### Uproszczenie pierwszej linijki

Linijka numer jeden jest dużo dłuższa! Pojawiają się w niej aż cztery programy: `echo`, `tee`, `grep`, `cut`, do tego rura (`|`), do tego parę zmiennych, zagnieżdżone w&nbsp;sobie cudzysłowy, ukośniki...

```bash
echo 'user_pref("dom.private-attribution.submission.enabled", false);' | tee -a  $HOME/.mozilla/firefox/$(grep "Default=.*\.default*" "$HOME/.mozilla/firefox/profiles.ini" | cut -d"=" -f2)/user.js
```

Ale spokojnie. W&nbsp;takich sytuacjach lubię sobie rozbijać większego dziada na mniejsze, z&nbsp;których każdy już mieści się w mózgu.

Proponuję zacząć od lewej strony, bo jest tam wspomniane przed chwilą `echo`, którego znaczenie jest względnie jasne. Jego ogólny sens jest ten sam co poprzednio -- wprowadza tekst do konsoli.

Tekst zaczyna się i kończy pojedynczymi cudzysłowami (`'`). Na razie go sobie odłożę na bok, bo dla konsoli nie ma żadnego specjalnego znaczenia. Mogłoby tam być wpisane „*lorem ipsum*”, a&nbsp;skrypt zadziałałby tak samo (choć Firefox zapewne by później dostał czkawki).

Kolejną rzecz do uproszczenia można zobaczyć bliżej końca linijki. Jest tam dolar, a&nbsp;po nim tekst w&nbsp;nawiasach -- `$(COŚ)`.  
W skryptach Basha oznacza się w&nbsp;ten sposób zmienne. Wewnątrz nawiasów mogą znajdować się nie tylko proste wartości, ale również, jak tutaj, całe instrukcje dla programów.

Ten tekst również można chwilowo odłożyć na bok. Po obu uproszczeniach zostaje coś znacznie przyjemniejszego do czytania:

```
echo JAKIŚ_TEKST | tee -a  $HOME/.mozilla/firefox/$(ZMIENNA)/user.js
```

Czytając od lewej: `echo` tradycyjnie wprowadza do konsoli tekst.  
Po nim znajduje się pionowa kreska, czyli „rura” (ang. *pipe*). Jej zasada działania jest prosta -- pozwala wziąć efekt działania programu przed sobą i&nbsp;podać go programowi po swojej prawej stronie. A&nbsp;jest nim...

### Tee

O tym programiku można poczytać choćby [na stronce Linuxize](https://linuxize.com/post/linux-tee-command/). Pozwala on **zapisać otrzymany tekst do jednego lub więcej plików**, jednocześnie wyświetlając go w&nbsp;konsoli. Poświęćmy mu parę sekund.

{% include info.html
type="Ciekawostka"
text="Tajemnicza nazwa programu wynika z&nbsp;tego, że *tee* w&nbsp;języku angielskim to potoczne określenie na literę T (zresztą w&nbsp;ten sposób mówi się czasem na T-shirty). Z&nbsp;kolei litera T&nbsp;może symbolizować rozgałęzienie. Które pasuje do przypadku, gdy program wyrzuca tę samą rzecz w&nbsp;kilka miejsc, do pliku i&nbsp;konsoli.  
Można go zatem nazwać intuicyjnie „rozgałęźnikiem”."
%}

Do programu `tee`, oprócz tekstu wpadającego przez rurę, trafiają dwa argumenty:

* Opcja `-a`.

  Od słowa *append*. Mówi programowi, żeby dopisywał nową treść na końcu pliku. To ważne, bo w&nbsp;innym wypadku by ten plik nadpisał, usuwając całą jego poprzednią zawartość.

* Ścieżka do pliku.

  Skąd wiem, że ścieżka? Rozpoznaję po ukośnikach, które rozdzielają pliki i&nbsp;foldery -- to skrypt na Linuksa, więc są skierowane w&nbsp;prawą stronę (`/`), odwrotnie niż na Windowsie.  
  Skąd wiem, że jedna? Nie wiem tego na pewno, ale tak obstawiam, bo nie ma w&nbsp;niej żadnych spacji i&nbsp;nie jest otoczona cudzysłowami. Dla konsoli byłaby traktowana jak jeden ciąg. Ale z&nbsp;drugiej strony spację mogłaby zawierać `$(ZMIENNA)`, więc jeszcze nie wiem na 100%.
 
Nazwa pliku, jak to w&nbsp;ścieżkach, znajduje się na końcu, po ostatnim ukośniku. To *user.js*. Z&nbsp;kolei fragment `.mozilla/firefox` sugeruje, że mowa tu o&nbsp;folderach związanych z&nbsp;przeglądarką Firefox.

Zatem esencja pierwszej linijki skryptu jest taka -- **zapisuje tekst wskazany na początku do pliku _user.js_ w&nbsp;folderze wewnętrznym Firefoksa**.

### Dopasowanie do działania Firefoksa

Na chwilę zrobię odskocznię od konsoli, żeby wyjaśnić parę spraw. Dlaczego poprzez `echo` wprowadzono akurat taki tekst? Dlaczego do jakiegoś *user.js*?

Tu akurat wyjaśnienie jest proste. W&nbsp;tych nazwach nie ma nic specjalnego z&nbsp;punktu widzenia konsoli. To wszystko konwencja przyjęta przez twórców Firefoksa.

* Firefox na systemach Linux zapisuje różne swoje ustawienia do podfolderu `.mozilla/firefox` (na innych systemach do innych lokalizacji).
* Plik *user.js* zawiera ustawienia odbiegające od domyślnych, dodane przez użytkowników. Jest wczytywany podczas uruchamiania Firefoksa.
* Za nowe reklamy odpowiada ustawienie  
  `dom.private-attribution.submission.enabled`.
* Rozszerzenie *.js* oznacza, że to plik w&nbsp;języku JavaScript, innym skryptowym. Ludzie z&nbsp;Firefoksa zapewne udostępnili publicznie funkcję `user_pref(ZMIENNA, WARTOŚĆ)`, która pozwala zmieniać wartości różnych ustawień.

Autor *Make Firefox...* zapewne wyszukał na początku, skąd Firefox bierze ustawienia. Po czym stworzył skrypt wprowadzający te zmiany tam, gdzie będą dla Lisa czytelne.  
Na tym się często opiera automatyzacja -- trzeba poczytać o&nbsp;wewnętrznym działaniu jakiegoś innego programu i&nbsp;dopasować się do niego. Czasem przeklinając, jeśli ten nie ułatwia współpracy :wink:

### Zmienna $HOME 

W dwóch miejscach pojawia się tekst `$HOME`. Dolar na początku sugeruje, że to jakaś zmienna o&nbsp;specjalnym znaczeniu.

Nie trzeba jej nigdzie wcześniej określać, bo to jedna ze [zmiennych *wbudowanych* w&nbsp;konsolę](https://www.gnu.org/software/bash/manual/html_node/Shell-Variables.html). Takie zmienne to zwykle różne informacje na temat komputera, plików, czy samej konsoli.

Autor *Make Firefox...*, tworząc swój skrypt, musiał podać pełną ścieżkę do paru plików. Ta ścieżka zawsze zawiera *folder domowy*, którego nazwa jest zależna od użytkownika. Dla jednej osoby będzie to `/home/dorota`, dla kogoś innego `/home/marek`...  
Używając zmiennej, autor może sprawić, że jego skrypt zadziała u&nbsp;wszystkich, dopasowując się do ich urządzenia.

### Grep

Przejdę teraz do ostatniej nieomówionej rzeczy. Oto wnętrze tej złożonej zmiennej, która pojawiła się *wewnątrz* ścieżki:

```bash
grep "Default=.*\.default*" "$HOME/.mozilla/firefox/profiles.ini" | cut -d"=" -f2
```

Ponownie -- można czytać od lewej, aż trafi się na pionową kreskę. Nieotoczona cudzysłowami, więc to nie tekst, tylko rura o&nbsp;specjalnym działaniu. Po jej lewej stronie jest program `grep` i&nbsp;jego argumenty, a&nbsp;wynik jego działania trafia do programu `cut`.

Zacznę od Grepa. Służy do wyszukiwania tekstu wewnątrz plików i&nbsp;ma składnię:

<div class="black-bg mono">
grep <span class="red">TEKST_DO_ZNALEZIENIA</span> <strong>PLIK</strong>
</div>

W roli pliku jest tutaj (ścieżka do) jakiegoś *profiles.ini*, również w&nbsp;wewnętrznym folderze Firefoksa.

Żeby zrozumieć sens tego fragmentu, warto wiedzieć, że **Firefox dopuszcza wiele profili użytkowników**, z&nbsp;których każdy ma jakieś własne ustawienia. I&nbsp;własny folder wewnętrzny, którego nazwa to ciąg losowych znaków, inny dla każdego użytkownika.  
Plik *profiles.ini* jakoś to porządkuje, przypisując rodzaje profili do nazw folderów. A&nbsp;że autor *MFPA* potrzebuje pełnej ścieżki, to do niego zagląda.

Tekstem do znalezienia w&nbsp;tym pliku jest natomiast `"Default=.*\.default*"`. Dla jasności można zerknąć do pliku i&nbsp;zobaczyć, co w&nbsp;ten sposób znajduje:

{:.figure .bigspace}
<img src="/assets/posts/open_source/firefox/make-firefox-private/firefox-profile.jpg" alt="Zrzut ekranu z&nbsp;notatnika, pokazujący format pliku z&nbsp;profilami. Trzy z&nbsp;nich, których nazwy zakryto różnymi kolorami, pasują do wzorca."/>

Warto też wiedzieć, że kropki, gwiazdki i&nbsp;ukośniki zaserwowane Grepowi mają dla niego [specjalne znaczenie](https://linuxize.com/post/how-to-use-grep-command-to-search-files-in-linux/):

* `.` oznacza jeden *dowolny* znak (niekoniecznie kropkę!);
* ...ale `\.` oznacza już konkretnie kropkę, bo ukośnik wyłącza specjalność;
* `*` oznacza „zero lub więcej tej rzeczy, która stoi bezpośrednio przed gwiazdką”  
  (przykład: `ba*` wyłapywałoby *b*, *ba*, *baaa* itd.);
* `.*` oznacza dowolną ilość znaków, aż do napotkania tego po prawej stronie.

{% include info.html
type="Nieoczekiwany błąd"
text="Swoją drogą na tym etapie coś poszło nie tak, bo Grep wykrył u&nbsp;mnie trzy pasujące nazwy folderów. Potem podał je dalej jako trzy rzeczy rozdzielane spacjami. W&nbsp;oczach programu *tee*: trzy ścieżki, z&nbsp;czego tylko jedna sensowna.  
Ogólnie: nie zadziałało :roll_eyes:  
Być może to przez to, że mam u&nbsp;siebie kilka różnych Firefoksów, z&nbsp;czego jeden jest dość wiekowy. Może mam przez to więcej folderów z&nbsp;profilami niż oczekiwałby skrypt. A&nbsp;może to niedopatrzenie w&nbsp;skrypcie.  
W każdym razie, gdybym chciał profilu kończącego się słowem *default*, pomogłaby zamiana (w&nbsp;tekście dla Grepa) ostatniej gwiazdki na dolara, wskazującego koniec tekstu. Wówczas skrypt znalazłby tylko jeden profil."
%}

### Cut

Znaleziony fragment tekstu trafia do programu `cut`. Jego zadaniem, jak angielska nazwa wskazuje, jest wycięcie z&nbsp;otrzymanej linijki tylko tej części, która go interesuje. Dostaje dwie opcje:

* `-d`, od *delimiter* (znak rozdzielający)  
  mówi, na jakich znakach program powinien podzielić otrzymany tekst. W&nbsp;tym wypadku na znakach `=`. Kiedy to zrobi, zostaje z&nbsp;kilkoma częściami składowymi. W&nbsp;tym wypadku z&nbsp;dwiema, które sobie numeruje jako 1&nbsp;i 2.
* `-f`  
  mówi, którą z&nbsp;tych rzeczy powinien wybrać. Jest `2`, czyli drugą. To, co będzie *po* znaku równości.

{:.post-meta .bigspace-after}
Choć argumenty są tutaj zapisane bez spacji między nazwą i&nbsp;wartością, to równie dobrze mogłyby ją zawierać. Byłoby czytelniej.

Podsumowując współpracę programów `grep` i&nbsp;`cut` -- pierwszy wyciąga ze spisu profili odpowiednią wartość. Drugi wyciąga z&nbsp;niej tekst odpowiadający nazwie folderu dla danego profilu.  
Ta nazwa zostaje wstawiona zamiast zmiennej, w&nbsp;której siedzą oba programy. Dzięki temu cały skrypt dostaje pełną ścieżkę do pliku z&nbsp;ustawieniami (a&nbsp;przynajmniej powinien, gdyby mi działał).

### Podsumowanie w&nbsp;formie schematu

Na koniec coś dla wzrokowców. Działanie najważniejszej, pierwszej linijki, pokazane w&nbsp;formie autorskiego schematu.

{:.bigspace-before}
<img src="/assets/posts/open_source/firefox/make-firefox-private/firefox-userjs-schemat.jpg" alt="Schemat pokazujący przepływ informacji między czterema konsolowymi programami, oznaczonymi jako podpisane, rysunkowe maszynki do mięsa: grep, cut, echo oraz tee. Po drodze strzałka wskazuje również wczytanie danych z&nbsp;pliku z&nbsp;profilami, a&nbsp;na końcu odchodzą dwie strzałki. Jedna z&nbsp;nich trafia do konsoli, a&nbsp;druga do pliku users.js"/>

{:.figcaption}
Źródło: ikony plików systemu Linux Mint; [maszynki do mięsa](https://www.flaticon.com/free-icon/meat-grinder_836411) i&nbsp;niektóre [strzałki](https://www.flaticon.com/free-icon/arrow-right_2267911) z&nbsp;serwisu Flaticon (autorstwa odpowiednio: *Freepik* i *Creative Stall Premium*). Przeróbki moje.

## Wątki poboczne

Skoro działanie skryptu już wyjaśnione, to przejdę do paru spraw luźniej powiązanych, które warto przy okazji poznać. 

### Wątek cyber(nie)bezpieczeństwa

Skrypt zawiera jeszcze parę programów, choć jedynie w&nbsp;części opisowej, instruktażowej. Pod hasłem „jak uruchomić” znajduje się linijka do wykonania w&nbsp;konsoli:

<div class="black-bg mono">
curl https://make-firefox-private-again.com |&nbsp;sh
</div>

Wzbudziła ona pewien sprzeciw u&nbsp;paru komentujących na forum HN. Dlaczego? Ano dlatego, że sugerowany sposób instalowania jest dość niefrasobliwy. Oznacza po prostu „pobierz w&nbsp;ciemno i&nbsp;uruchom” (gdzie `curl` to pobieracz, a&nbsp;`sh` to uruchamiacz).

Ale przecież kod źródłowy jest na widoku? I, jak pokazałem wyżej, nieszkodliwy?  
Problem w&nbsp;tym, że **nawet przeczytanie kodu źródłowego może nie dać wystarczającej ochrony**, jeśli po przeczytaniu, już uspokojeni, pobierzemy skrypt innym programem.

Wynika to z&nbsp;podstaw działania internetu. Podczas wysyłania cudzemu serwerowi próśb o&nbsp;różne rzeczy -- strony, obrazki, skrypty -- wiele programów ujawnia pewne podstawowe informacje. W&nbsp;tym swoją zwięzłą wizytówkę, zawartą w&nbsp;polu nazywającym się [*user agent*]({% post_url 2021-06-11-user-agent %}){:.internal}.  
Tak robi również *curl* -- [przedstawia się inaczej](https://everything.curl.dev/http/modify/user-agent.html) niż popularne przeglądarki. Każdy serwer, z&nbsp;którym się kontaktuje, może go rozpoznać i&nbsp;wręczyć mu niespodziankę, której nie dałby użytkownikom przeglądarek.

Bezpieczniejszym rozwiązaniem jest ręczne pobranie skryptu, zapoznanie się z kodem źródłowym (przynajmniej pobieżne) i&nbsp;dopiero wtedy uruchomienie *tego samego zapisanego pliku* programem `sh` lub innym.

### Świat majsterkowania z&nbsp;*user.js*

Rozwiązanie ze stronki *MFPA* jest krótkie i&nbsp;eleganckie (o&nbsp;ile działa), ale samo nie aspiruje do miana nowatorskiego. To dlatego, że wokół Firefoksa już od dawna działa aktywna społeczność, personalizująca swoje ustawienia właśnie przez gmeranie w&nbsp;pliku *user.js*.

Jednym z&nbsp;przykładów jest [BetterFox](https://github.com/yokoffing/BetterFox), czyli skrypt *user.js* z&nbsp;ustawieniami poprawiającymi szybkość Firefoksa. Linkują też do paru innych wariantów, skupiających się na innych aspektach.

Innym przykładem jest [plik *user.js* od użytkownika Arkenfox](https://github.com/arkenfox/user.js/), pozwalający uszczelnić prywatność Firefoksa (kosztem wyłączenia pewnych bajerów, więc warto dokładnie się wczytać przed jego użyciem).

Te rozwiązania są idealne dla osób, które chcą wyższego poziomu prywatności, ale obawiałyby się niezależnych projektów opartych na kodzie źródłowym Firefoksa (jak Waterfox czy LibreWolf). Mamy tu bowiem oficjalnego Firefoksa, od Mozilli. Ale dopasowanego pod siebie.

Istnienie tych możliwości daje nadzieję, nawet w&nbsp;obliczu wieści takich jak te o&nbsp;zabawach Mozilli z&nbsp;reklamami. Niezależnie od tego, co wymyśli sobie bardziej „byznesowa” część twórców Firefoksa, zawsze pozostaną ręczne modyfikacje i&nbsp;alternatywy od społeczności.  
Przynajmniej dopóty, dopóki kod źródłowy Lisa jest otwarty, a&nbsp;opcje personalizacji rozbudowane. Oby się to nie zmieniło! :smile:
