---
layout: post
title: "Bloby i szyfry. Przyjemna konsolowa przygoda"
subtitle: "Szukamy dowodów na certyfikowaną wrogość producenta."
description: "Szukamy dowodów na certyfikowaną wrogość producenta."
date:   2023-04-26 08:00:00 +0100
tags: [Centralizacja, DRM, Hardware, Podstawy]
image:
  path: /assets/posts/apki/imx_firmware/blob-baner.jpg
  width: 1200
  height: 700
  alt: "Obrazek pokazujący krzyczącą twarz uwięzioną w galarecie z plakatu filmu The Blob. Całość widać zza półprzezroczystej ściany zer i jedynek"
---

Swego czasu ukazał się ciekawy post na stronie *devever.net*, zatytułowany [*The i.MX8 cannot be deblobbed*](https://www.devever.net/~hl/imx8).

Odwołuje się on do smutnego faktu, że **podstawowe części naszych telefonów opierają się na zamkniętych, nieprzeniknionych programach**.  
Nawet telefony stawiające na prywatność i&nbsp;otwarty kod muszą, chcąc nie chcąc, polegać na takich podzespołach. Bo nie ma alternatyw.

Autor potwierdził w&nbsp;swoim wpisie, że kontrola sięga głębiej. Nawet gdyby ktoś stworzył wierny zamiennik dla zamkniętego programu, to nie wszystko by działało. Bo **programy mogą być ściśle przypisane do części poprzez szyfrowanie** (a&nbsp;dokładniej: przez bazujący na nim cyfrowy podpis).

Nasza zależność od takich modułów jest kolejnym objawem centralizacji władzy. Zmory współczesnych czasów.

Mój wpis nie będzie jednak omówieniem tej patologii, lecz czymś bardziej popularyzatorskim. Zweryfikuję odkrycie autora, komentując przystępnym językiem jego działania.

Dzięki temu osoby, które nie znają świata programików konsolowych, będą mogły nieco się z&nbsp;nim oswoić. Zobaczyć, że za tajemniczymi zaklęciami kryją się czasem zadziwiająco proste rzeczy :wink:

## Kontekst

Współczesne telefony zawierają wiele różnych elementów. Modem. Układ obsługujący karty SIM. Moduł Bluetooth. Żyroskop. I&nbsp;wiele innych.

Tymi fizycznymi częściami steruje pewien szczególny rodzaj programów, nazywanych *firmware'em*. Są zwykle stworzone przez producentów i&nbsp;ściśle zintegrowane z&nbsp;funkcjami fizycznych części.

Są również nieprzeniknione -- to często bloki złożone z&nbsp;zer i&nbsp;jedynek, w których kryje się wiele nieopisanych funkcji. Żargonowo nazywa się je *binary large objects*, duże obiekty binarne. Nieformalny skrót to *bloby*.

Ich nieprzejrzystość jest problemem -- nie wiadomo, czy nie działają na szkodę użytkowników, na przykład wysyłając ukradkiem informacje (dotyczy to zwłaszcza blobów w&nbsp;modemie).  
A nawet jeśli nie, to mogą mieć jakieś luki w&nbsp;zabezpieczeniach, które kiedyś pozwoliłyby hakerom dobrać się do naszych urządzeń.

To między innymi z&nbsp;tych powodów osoby związane z&nbsp;ruchem *open source* wzięły sobie za cel zastąpienie blobów otwartym kodem, który każdy mógłby zweryfikować. Ich inicjatywy nazywa się nieformalnie *deblobbingiem*, „walką z&nbsp;blobami”.

{:.bigspace-before}
<img src="/assets/posts/apki/imx_firmware/blob-baner.jpg" alt="Plakat filmu The Blob, pokazujący czerwoną galaretę i&nbsp;uwięzioną w&nbsp;niej, krzyczącą twarz. U&nbsp;góry czerwonymi literami napisany jest tytuł filmu. Całość jest zakryta półprzezroczystą ścianą niebieskich zer i&nbsp;jedynek."/>

{:.figcaption}
Źródła: plakat horroru The Blob z&nbsp;1988 roku, zera i&nbsp;jedynki z&nbsp;[Pixabay](https://pixabay.com/illustrations/binary-code-privacy-policy-woman-1327493/). Aranżacja moja.

Ale niektórzy producenci nie lubią otwartej konkurencji, która mogłaby ich wygryźć. **Próbują wymusić, żeby fizyczny sprzęt akceptował jedynie ich własny _firmware_**. Mogą wykorzystywać do tego celu *certyfikaty* -- cyfrowe podpisy niemożliwe do podrobienia.

Zbadaniem takiej kwestii zajął się Hugo Landau, autor strony Devever.  
Wyczytał w&nbsp;dokumentach fragment, który dało się rozumieć dwojako. I&nbsp;spróbował wykazać, że bloby związane z&nbsp;[procesorami i.MX 8&nbsp;oraz i.MX 8M](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors:IMX8-SERIES) są właśnie w&nbsp;ten sposób zaplombowane.

Motywowało go między innymi to, że takich procesorów używają rzekomo prywatnościowe smartfony firmy Librem (choć niektórzy tego [nie potwierdzają](https://forums.puri.sm/t/the-i-mx8-cannot-be-deblobbed-nxp-signed-hdmi-firmware/6081/39)).

Konieczność bazowania na niezaufanym kodzie byłaby dla nich szczególnie mocnym ciosem. Ale na rynku niestety nie jest na tyle łatwo o&nbsp;procesory dla urządzeń mobilnych, żeby mogli wybrzydzać.

{% include info.html
type="Ciekawostka"
text="Dokładniej rzecz biorąc, autor skupił się na kodzie odpowiedzialnym za obsługę popularnego złącza od multimediów, [HDMI](https://pl.wikipedia.org/wiki/HDMI).  
Na forum HackerNews znajdziemy [spekulacje](https://news.ycombinator.com/item?id=35684859) o&nbsp;tym, że uszczelnianie tego konkretnego kodu może wynikać z&nbsp;chęci przypodobania się producentom filmów. To grupa często naciskająca na to, żeby chronić ich treści przed użytkownikami.
"%}

Misja autora opierała się na następujących krokach:

* zdobyć firmware od producenta, firmy NXP;
* znaleźć w&nbsp;jego bebechach certyfikat;
* sprawdzić, czy jest przypisany do tego konkretnego producenta.

## Powtarzamy kroki

Autor opisuje krok po kroku, co zrobił, wkleja treść użytych komend. Dzięki temu można łatwo zweryfikować jego wyniki, za co ma u&nbsp;mnie wielkiego plusa.

Pisze jednak z&nbsp;(uzasadnionym) założeniem, że odbiorcy rozumieją konsolę. A&nbsp;we mnie, na widok ścian tekstu, odżywają wspomnienia dawnych czasów.

Próbując się wgryźć w&nbsp;tematy komputerowe, zerkałem na popularne fora.  
Ktoś tam wklejał komendy, które miały rzekomo rozwiązać cudzy problem. Bez dodatkowego komentarza, tak jakby rozwiązanie było oczywiste.

A ja nawet nie wiedziałem, gdzie to wpisać. Nie wiedziałem, że istnieje coś takiego jak konsola, pozwalająca „rozmawiać” bezpośrednio z&nbsp;komputerem. I&nbsp;innymi programami, które znałem tylko jako ikony do klikania.

Gdy już odkryłem konsolę, to często coś mi nie działało. Bo potrzeba jakiegoś programu. A&nbsp;ja nie wiem, skąd go zdobyć, nie znajduję żadnego instalatora.  
Czasem po chwili szukania odkrywałem, że cała podana komenda działa tylko na systemie Linux. A&nbsp;na swoim ówczesnym Windowsie musiałbym użyć jakiegoś zamiennika.

I tak dalej. Odbijałem się od tematu jak od ściany. **Rzeczy proste wydawały się magią, kiedy tyle osób „cytowało konsolę” bez dodatkowego kontekstu**.

Odkrycie autora Devever broni się samo. Ale uważam, że zasługuje na jeszcze przystępniejsze omówienie, żeby więcej osób je doceniło. A&nbsp;zatem je tutaj zapewnię.

### Wypatrujemy komend

Sam [wpis z&nbsp;Devever](https://www.devever.net/~hl/imx8) jest mieszanką poleceń konsolowych, komentarzy autora oraz wyświetlonych wyników. To wszystko może się nieco zlewać, więc najpierw ustalmy sobie, jak rozumieć tekst.

* **Komendy z&nbsp;konsoli to linijki mające na początku znak dolara** (`$`);
* Linijki rozpoczynające się od krzyżyka (`#`) to komentarze autora;
* Reszta tekstu to treść, jaka mu się wyświetliła.

Dolar nie jest jakimś wymysłem autora, tylko szeroko przyjętą konwencją. Wiele terminali go wyświetla na początku linijki, żeby dać nam znać, że czekają na wpisanie polecenia.

{% include info.html
type="Porada"
text="
Mam drobną prośbę do twórców stron. Jeśli chcecie na nich cytować komendy z&nbsp;dolarkiem, to bardzo proszę, niech będzie *nie do zaznaczenia*.  
Dzięki temu wystarczy dwukrotnie kliknąć myszką linijkę tekstu, żeby zaznaczyć całość, gotową do skopiowania, bez dolara. Nie trzeba go usuwać z&nbsp;zaznaczenia, jest szybciej. Mała rzecz, a&nbsp;cieszy :wink:  
Jeśli nasz szablon strony nie daje dostępu do arkuszy styli, to w&nbsp;najprostszym przypadku można po prosto robić w&nbsp;takich sytuacjach tabelki. Dolara w&nbsp;pierwszej kolumnie, a&nbsp;resztę komendy w&nbsp;drugiej.
"%}

Swoją drogą **komendy konsolowe z&nbsp;artykułu odnoszą się do systemu Linux**. To na nim mamy (często z&nbsp;domysłu) zainstalowane programiki, których używa autor. Sam również używałem systemu Linux Mint, tworząc ten wpis.  
Ale niech użytkownicy Windowsa się nie zrażają. Na nim też da się powtórzyć większość kroków, tylko parę ostatnich wymaga więcej pracy.

Skoro już wiemy, które fragmenty tekstu to komendy, to po kolei je sobie omówmy.

### Pobranie pliku

Zaczynajmy! Pierwsza komenda wpisana przez autora była taka:

```
wget http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/firmware-imx-8.0.bin
```

{:.figcaption}
Na urządzeniach mobilnych komendy nie wyświetlają się w&nbsp;całości. Można odsłonić resztę, kładąc palec na czarnym polu i&nbsp;ruszając nim w&nbsp;lewo.

Ogólna zasada -- **w konsoli spacje rozdzielają różne elementy**. Nazwa programu to element pierwszy, najbardziej po lewej. Reszta to wrzucane do niego opcje, takie jak nazwy plików do odczytania.

{:.post-meta .bigspace-after}
Nieco się to zmienia, jeśli mamy w&nbsp;linijce specjalne operatory. Jeszcze o&nbsp;nich będzie w&nbsp;tym wpisie.

Użytym programem jest tu zatem `wget`. Odpowiada za pobieranie różnych plików z&nbsp;internetu.  
Zaś drugi człon, po spacji, to link do konkretnej rzeczy na stronie *freescale.com*, gdzie są przykłady interesującego nas firmware'u.

W tym prostym przypadku użycie `wget`a jest właściwie tym samym, co odwiedzenie strony przez przeglądarkę.  
Zresztą sami możemy to sprawdzić! Gdybyśmy spróbowali wkleić ten adres w&nbsp;przeglądarkę, to by nas zapytało, czy chcemy pobrać plik:

{:.figure .bigspace}
<img src="/assets/posts/apki/imx_firmware/wget-alternatywa.jpg" alt="Komunikat wyświetlany przez przeglądarkę, pytający czy chcemy zapisać plik bin, czy też otworzyć go domyślnym programem"/>

{% include info.html
type="Ciekawostka"
text="Czasem `wget` nie otrzymuje tego, co próbuje pobrać, ponieważ jest „zbyt szczery”. Wprost załącza do swoich zapytań informację o&nbsp;tym, że jest skryptem. A&nbsp;niektóre strony nie dopuszczają do siebie automatów.  
Kiedy natomiast prośba o&nbsp;daną rzecz wygląda na coś pochodzącego od popularnej przeglądarki, to zostanie spełniona. Za odróżnianie automatów od ludzi odpowiada często informacja zwana [*user agentem*](/internetowa_inwigilacja/2021/06/11/user-agent){:.internal}.
"%}

### Rozpakowywanie pliku

Kiedy już mamy plik na dysku, to znaczy że można z&nbsp;nim pracować.

Ale czym on w&nbsp;ogóle jest? `.bin` to rozszerzenie pliku oznaczające *binary*, czyli jakiśtam blok zer i&nbsp;jedynek. Mało nam to mówi, a&nbsp;plik może być czymkolwiek.

Autor pisze w&nbsp;komentarzu, że to w&nbsp;rzeczywistości skompresowany plik plus trochę tekstu, którym jest licencja użytkownika (EULA).

{:post-meta .bigspace-after}
Nie mówi, w&nbsp;jaki sposób poznał ten fakt, ale bardzo możliwe, że użył na pobranym pliku programu Binwalk. Nieco później to właśnie po niego sięgnął.

Skoro plik jest skompresowany, to można spróbować go rozpakować. Autor zrobił to tak:

```
7z x firmware-imx-8.0.bin
```

`7z` to tutaj [programik 7-Zip](https://7-zip.org/download.html) do pracy ze skompresowanymi plikami, takimi jak ZIP czy RAR. Ale póki zna metodę kompresji, działa też na innych.

Ostatni, trzeci człon polecenia to nasz plik. A&nbsp;co oznacza `x`?  
To zapewne jakaś opcja programu. A&nbsp;to oznacza, że wyjaśnienie powinno być zawarte w&nbsp;jego instrukcji. Wpisałem w&nbsp;konsolę `7z --help` (bardzo wiele programów ma taką opcję) i&nbsp;zobaczyłem tam:

{:.bigspace .no-right-border}
> x&nbsp;: eXtract files with full paths

Czyli cała komenda to po prostu rozpakowanie pliku!  
Właściwie nie potrzeba do tego nawet 7-Zipa, bo wiele domyślnych przeglądarek plików, jak Eksplorator na Windowsie, ma wbudowaną opcję rozpakowywania archiwów.

Jednak nasz program do eksplorowania plików musi wiedzieć, że ma traktować plik *bin* jak archiwum. Zatem wybieramy opcję zmiany nazwy pliku i&nbsp;zmieniamy końcówkę na `.zip`.

{:.bigspace-before}
<img src="/assets/posts/apki/imx_firmware/bin-zip-zmiana-nazwy.jpg" alt="Schemat pokazujący ikonę pliku tekstowego, od której odchodzi strzałka do ikony pliku o&nbsp;takiej samej nazwie, lecz kończącej się na ZIP. Również ikona drugiego pliku pokazuje folder zapięty na zamek. Strzałka jest podpisana nazwą opcji 'Zmień nazwę'." />

{:.figcaption}
Źródło ikonek i&nbsp;opcji: system Linux Mint. Strzałka ze strony Flaticon. Przeróbki moje.

Potem mój Linux Mint się nie buntował, kiedy kliknąłem plik prawym przyciskiem myszy i&nbsp;wybrałem opcję `Rozpakuj tutaj`. Wydobył z&nbsp;pliku jego zawartość, również o&nbsp;nazwie *firmware-imx-8.0*.

{:.bigspace}
<img src="/assets/posts/apki/imx_firmware/zip-rozpakowanie.jpg" alt="Schemat pokazujący ikonę pliku ZIP, od której odchodzi strzałka do srebrnej ikony ogólnego skompresowanego pliku. Strzałka jest podpisana nazwą opcji 'Wypakuj tutaj'."/>

### Ponowne rozpakowanie

Po rozpakowaniu otrzymaliśmy... kolejny skompresowany plik. Trochę jak rosyjska matrioszka.  
Nic dziwnego, że kolejna komenda autora też odpowiadała za rozpakowanie. Ale tym razem programikiem `tar`:

```
tar xvf firmware-imx-8.0
```

`xvf` to zwięzła forma na podanie `tar`owi kilku instrukcji naraz:

* `x` oznacza, że ma rozpakować plik;
* `f PLIK` mówi, [jaki plik ma załadować](https://unix.stackexchange.com/questions/1280/what-does-the-f-parameter-do-in-the-tar-command);
* `v` (*verbose*) oznacza, że ma wyświetlić szczegółową listę wypakowanych plików.

Tutaj ponownie dało się użyć zwykłego eksploratora. Kliknąć plik *firmware-imx-8.0* prawym przyciskiem myszy i&nbsp;wybrać opcję rozpakowania. Na systemie Linux Mint nie musiałem nawet zmieniać rozszerzenia na *zip*.

W ten sposób otrzymaliśmy najzwyklejszy folder, po którym można chodzić przez Eksploratora Plików.

{:.bigspace}
<img src="/assets/posts/apki/imx_firmware/zip-rozpakowanie-2.jpg" alt="Schemat pokazujący ikonę skompresowanego pliku, od której odchodzi strzałka do ikony zwykłego folderu. Strzałka jest podpisana nazwą opcji 'Wypakuj tutaj'."/>

### Szukanie plików

Po zwykłym folderze można nie tylko chodzić; można też szukać w&nbsp;nim plików! I&nbsp;to właśnie zrobił autor swoim kolejnym poleceniem.

Po tym, co wyczytał w&nbsp;dokumencie firmowym, interesowały go rzeczy związane ze słowem *hdmi* (nazwa złącza). Poszukał go:

```
find firmware-imx-8.0 -type f | grep hdmi
```

To nieco inna komenda, bo złożona właściwie z&nbsp;dwóch niezależnych programów. Zdradza nam to obecność pionowej krechy, „rury” (ang. *pipe operator*) -- `|`.  
Oznacza ona po prostu tyle, że **wynik działania programiku po lewej stronie wrzucamy do tego po prawej**.

Program `find` znajduje w&nbsp;podanym folderze wszystkie pliki (co sugeruje nam dopisek `-type f`, gdzie f&nbsp;to skrót od *file*).  
Poprzez rurę ich lista trafia do `grep`a.  
A on z&nbsp;kolei wyłapuje te z&nbsp;nich, które gdzieś w nazwie (tu: gdziekolwiek w&nbsp;ścieżce) mają tekst *hdmi*.

{:.figure .bigspace}
<img src="/assets/posts/apki/imx_firmware/grep-wyniki.jpg" alt="Zrzut ekranu z&nbsp;konsoli pokazujący 5&nbsp;różnych ścieżek, jakie znalazł grep. Słowo 'hdmi' jest w&nbsp;nich wyróżnione na czerwono"/>

To samo osiągnęlibyśmy w&nbsp;zwykłym Eksploratorze Plików, naciskając `Ctrl+F` i&nbsp;wpisując słowo *hdmi*.

{:.figure .bigspace}
<img src="/assets/posts/apki/imx_firmware/find-alternatywa.jpg" alt="Okno Eksploratora Plików na systemie Linux Mint, pokazujące ikony czterech plików w&nbsp;wynikach wyszukiwania, a&nbsp;nad nimi pasek wyszukiwanie ze wpisanym słowem 'hdmi'."/>

Byłoby to nawet nieco precyzyjniejsze. Nie pokazuje nam bowiem tych plików, które jedynie znajdują się w&nbsp;podfolderze *hdmi*, ale same nie mają tego tekstu w&nbsp;nazwie.

### Przejście do znalezionych plików

Autor używa następnie programiku `cd`:

```
cd firmware-imx-8.0/firmware/hdmi/cadence
```

Jego nazwa to skrót od *change directory*. „Przejdź do innego folderu”. I&nbsp;dokładnie to robi ten program, kiedy poda mu się ścieżkę tegoż folderu.

A dlaczego autor nie musi podawać pełnej ścieżki? Tego, co na Windowsie zaczynałoby się na przykład od `C:\`?

Bo swoją konsolę uruchomił w&nbsp;tym samym folderze co plik *.bin*. To on jest dla niego aktywnym folderem, punktem odniesienia. Wystarczy używać ścieżek *względnych* wobec niego.

A samą ścieżkę sobie po prostu skopiował z&nbsp;wyników wyszukiwania poprzednią komendą.  
Na podobnej zasadzie moglibyśmy w&nbsp;graficznym Eksploratorze kliknąć dwukrotnie nazwę folderu *hdmi*, żeby do niego przejść.

### Eksploracja pliku

Autora interesował jeden konkretny plik spośród wyników -- *signed_hdmi_imx8.bin*. Kolejny blok zer i&nbsp;jedynek.

A skąd wiedział, że akurat o&nbsp;ten plik chodzi? Jego wzrok mogło zwrócić słowo *signed* w&nbsp;nazwie, sugerujące że jest tam coś podpisanego (podpisem cyfrowym).  
Skoro szukał certyfikatów, to mógł być wyczulony na takie szczególne słowa.

Do eksploracji użył programu [Binwalk](https://github.com/ReFirmLabs/binwalk). Który przemierza takie bloki zero-jedynkowe, porównuje ich ciągi do swojej listy wzorców i&nbsp;na tej podstawie znajduje fragmenty tekstu oraz różne zagnieżdżone pliki.

<pre class="black-bg mono">
binwalk signed_hdmi_imx8<span class="corr-ins">m</span>.bin
</pre>

Wydaje mi się, że w&nbsp;tym miejscu autor zrobił literówkę (albo coś zmienili pod pierwotnym linkiem). W&nbsp;moim folderze był tylko plik z&nbsp;literką *m* na końcu; zakładam, że to o&nbsp;niego chodziło, bo reszta informacji się zgadza.

Binwalk odnalazł w&nbsp;naszym pliku tajemniczy „certyfikat w&nbsp;formacie DER”:

{:.figure .bigspace}
<img src="/assets/posts/apki/imx_firmware/imx-cert-found.jpg" alt="Zrzut ekranu z&nbsp;konsoli pokazujący komunikat mówiący, że od bajtu 103636 zaczyna się certyfikat w formacie DER."/>

Tutaj niestety mam złą wiadomość dla użytkowników Windowsa chcących sprawdzić wyniki. **Binwalk jest dość mocno przystosowany do Linuksa**; do tego stopnia, że oficjalna strona ma instrukcje instalacji działające tylko na nim.

Chętni daliby radę go zainstalować również na Windzie, ale wymagałoby to trochę zachodu. Podobnie będzie z&nbsp;pozostałymi dwoma krokami.  
Jeśli znajdę jakiś sposób na łatwe odtworzenie tego i&nbsp;kolejnych kroków na Windowsie, to zaktualizuję wpis. Ale póki co pozostaje chyba uwierzyć na słowo w&nbsp;pokazywane tu rzeczy :wink:

### Wyciągnięcie certyfikatu

Skoro autor wiedział, że plik składa się z&nbsp;dwóch głównych członów, a&nbsp;interesował go ten drugi, to mógł wydać polecenie: „weź wszystko od miejsca, w&nbsp;którym zaczyna się certyfikat, aż do końca”. W&nbsp;ten sposób mógłby wywlec certyfikat z&nbsp;pliku.

Skopiował sobie zatem numer bajtu początkowego (103636&nbsp;z kolumny *DECIMAL* z&nbsp;poprzednich wyników). Dodał do niego 1.

Dlaczego? Przyznam, że jeszcze muszę doczytać; może pierwszy bajt był jakimś początkiem pliku, niezwiązanym z&nbsp;samym certyfikatem? W&nbsp;każdym razie bez tego by potem wyskoczył błąd.  
Potem użył komendy:

<pre class="black-bg mono">
tail -c +103637 signed_hdmi_imx8<span class="corr-ins">m</span>.bin > x.bin
</pre>

Programem z&nbsp;lewej strony jest tutaj `tail`. Odpowiada za czytanie plików *od końca*.  
Mamy również kolejny specjalny operator. Strzałkę (`>`), czyli zapisanie wyników polecenia po jej lewej do pliku po prawej (o&nbsp;dowolnej podanej przez nas nazwie; jeśli takiego nie ma, to zostanie stworzony).

Cała komenda oznacza: „weź z&nbsp;pliku dane od bajtu numer 103637&nbsp;do końca”. Zaś strzałka dodaje od siebie: „...i zapisz to do pliku *x.bin*”.

### Odczytanie certyfikatu

Mając certyfkat w&nbsp;osobnym pliku, można do niego zajrzeć. Powinna być tam informacja o&nbsp;tym, przez kogo został wydany. Autor użył komendy:

```
openssl x509 -inform der -in x.bin -text
```

OpenSSL to bardzo popularny, spory pakiet do pracy ze wszelkimi szyframi. Dostępny [również na Windowsa](https://wiki.openssl.org/index.php/Binaries).

Spójrzmy bliżej na parametry użyte w&nbsp;poleceniu:

* `x509` oznacza, że z&nbsp;całego pakietu OpenSSL-a wybieramy konkretny program, odpowiedzialny za certyfikaty.
* `-inform der` to wbrew pozorom nie informacje, lecz skrót od *input format*. 

  Ta komenda wymaga wskazania formatu z&nbsp;zamkniętej listy: DER, NET albo PEM. Wiemy że u&nbsp;nas jest DER, bo tak powiedział wcześniej Binwalk.

* `-in PLIK` wskazuje nam, jaki plik chcemy wczytać. Autor wybrał ten wcześniej wyciągnięty certyfikat.
* `-text` nakazuje wyświetlić informacje w&nbsp;formie tekstowej.

Pod tą komendą mamy na stronie całą ścianę tekstu. Zawierającą różne informacje, w&nbsp;tym te mocno techniczne, dotyczące szyfrów.

Ale nas interesuje jedno konkretne pole. `Issuer`, czyli podmiot wystawiający certyfikat.

{:.figure .bigspace}
<img src="/assets/posts/apki/imx_firmware/imx-certificate-issuer.jpg" alt="Zrzut ekranu z&nbsp;konsoli pokazujący fragment informacji dotyczących certyfikatu, takich jak data jego wydania oraz ważności. Zielonym tłem oznaczone jest pole issuer, wskazujące stronę nxp.com."/>

### Werdykt

Wystawcą certyfikatu jest strona *nxp.com*, należąca do firmy NXP. Tej samej, która stworzyła sam procesorek i.MX 8.

Czyli obawy zapewne się potwierdziły.  
Nawet gdyby ktoś przeanalizował cały ten *firmware*, wielki blok zer i&nbsp;jedynek, po czym przepisał go na coś czytelnego i&nbsp;przyjaźniejszego użytkownikom... To cała robota byłaby na nic.

**Fizyczny sprzęt mógłby nie akceptować zmienionego firmware'u**. Bo patrzyłby na cyfrowy podpis niczym doskonały grafolog. I&nbsp;widziałby, że nie pasuje do wzoru producenta, który ma u&nbsp;siebie zakodowany.

Stąd ponury wniosek -- kompletne usunięcie nieprzeniknionych elementów i&nbsp;„oczyszczenie” firmware'u od NXP byłoby bardzo trudne lub wręcz niemożliwe. Nie nawrócimy go na jasną stronę, możemy co najwyżej nie korzystać z&nbsp;funkcji HDMI.

{:.no-right-border}
> these chips can never be fully deblobbed

A jeśli producent kiedyś padnie, a&nbsp;jego certyfikat straci ważność, to wszystkie szyfrowane funkcje wygasną na zawsze.

## Podsumowanie

Konsola nie jest taka zła! Choć enigmatyczne komendy mogą odstraszać, często stoją za nimi całkiem prozaiczne rzeczy. Takie, które każdy użytkownik komputera może wykonać na własną rękę. Ona po prostu przyspiesza pracę.

Powtarzając kroki autora strony Devever, mogliśmy użyć następujących programów oraz specjalnych operatorów:

<div class="bigspace black-bg mono">
wget, 7z, tar, find, grep, cd, binwalk, tail, openssl, |, >
</div>

Całkiem nieźle jak na krótką eksplorację!

Mieliśmy również wgląd w&nbsp;fascynujący świat inżynierii wstecznej.  
To tam różne mądre głowy wyciągają z&nbsp;zer i&nbsp;jedynek szczegóły działania programów. Nieraz po to, żeby stworzyć alternatywy dla zamkniętych korposystemów -- bardziej szanujące ludzi oraz ich prywatność i&nbsp;niezależność.

Widzimy jednak, jak bardzo utrudnia im życie szyfrowanie (rzecz, paradoksalnie, często [chroniąca prywatność]({% post_url 2022-08-13-https %}){:.internal}).  
Wykorzystują je chętnie producenci, którzy chcą sobie zapewnić, że to oni i&nbsp;tylko oni będą mieli kontrolę nad fundamentami współczesnej elektroniki.

Kto wygra ten wyścig zbrojeń? Czy będzie trzeba odejść od prób otwarcia cudzego kodu i&nbsp;zejść niżej, na poziom *open hardware*?  
Nie wiem. Ale zawsze trzymam stronę dzielnych ruchów oporu :smile:
