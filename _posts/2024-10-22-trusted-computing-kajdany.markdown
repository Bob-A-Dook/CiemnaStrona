---
layout: post
title: "Trusted computing i cyfrowe kajdany"
subtitle: "Łańcuchami zaufania można spętać najmocniej."
description: "Łańcuchami zaufania można spętać najmocniej."
date:   2024-10-22 19:40:00 +0100
tags: [Centralizacja, DRM, Dystopia, Hardware]
firmy: [Google, Microsoft]
category: cyfrowy_feudalizm
category_readable: "Cyfrowy&nbsp;feudalizm"
image:
  path: /assets/posts/centralizacja/trusted-computing-wprowadzenie/trusted-computing-rzeczywistosc.jpg
  width: 1200
  height: 700
  alt: "Smutny człowiek z białą flagą oraz uśmiechnięty ludek z Monopoly po przeciwnych stronach znaku yin i yang."
---

Duże firmy technologiczne, zwane zbiorczo *big techem*, nieraz rzucają użytkownikom kłody pod nogi.  
Pogarszanie jakości aplikacji przez spam reklamowy i&nbsp;nachalne zbieranie danych. Udostępnianie filmów tylko na wybranych systemach operacyjnych. Skądinąd sprawne sprzęty, które przestają działać, gdy producent splajtuje i&nbsp;wyłączy swoją infrastrukturę.

W takich sytuacjach dało się zwykle zwrócić ku alternatywnym systemom czy aplikacjom. Albo zdać się na „dobrych hakerów”, którzy przełamią zabezpieczenia i&nbsp;upublicznią otwartą wersję.  
Niestety **swoboda wyboru bywa -- i&nbsp;może być coraz częściej -- ograniczana. Przez tytułowy _trusted computing_, czyli użycie szyfrów do zyskania różnych gwarancji**.

Zagrożenie jest o&nbsp;tyle subtelne, że jego części składowe są rzeczami raczej pozytywnymi, chroniącymi prywatność. Ale połączenie ich w&nbsp;całość może mieć opłakane skutki.

Żeby to zademonstrować, postanowiłem stworzyć ten popularyzatorski wpis, w&nbsp;którym konstruuję *trusted computing* od podstaw. Krok po kroku, jak najprościej, stawiając intuicję ponad ścisłością.  
Zapraszam! :smile:

{:.bigspace-before}
<img src="/assets/posts/centralizacja/trusted-computing-wprowadzenie/trusted-computing-rzeczywistosc.jpg" alt="Smutny człowiek z&nbsp;białą flagą oraz uśmiechnięty ludek z&nbsp;Monopoly po przeciwnych stronach znaku yin i&nbsp;yang. W&nbsp;człowieka wymierzone są dwa pistolety maszynowe, wystające z&nbsp;ciemnych obszarów znaku. Wewnątrz mniejszego czarnego koła, z&nbsp;którego wystaje jeden z&nbsp;nich, znajduje się chip komputerowy"/>

<details class="figcaption">
<summary>Źródła (kliknij, żeby rozwinąć)</summary>
<p>Ludek z&nbsp;Monopoly z&nbsp;<a href="https://www.aiophotoz.com/photos/original-monopoly-man-png-monopoly-man-png-cliparts-all-these-png.html"><em>aiophotoz.com</em></a>; ikony z&nbsp;serwisu Flaticon: <a href="https://www.flaticon.com/free-icon/machine-gun_4452905">pistolety maszynowe</a> (autor: <em>Georgy</em>), <a href="https://www.flaticon.com/free-icon/give-up_6554128">człowiek z&nbsp;białą flagą</a> od <em>Flat Icons</em>, <a href="https://www.flaticon.com/free-icons/server">serwer</a> od <em>Smashicons</em>, <a href="https://www.flaticon.com/free-icon/cpu_630413">chip</a> od <em>Freepik</em>.</p>
</details>

## Spis treści

* [Czym jest *trusted computing*](#czym-jest-trusted-computing)
* [Trusted computing krok po kroku](#trusted-computing-krok-po-kroku)
  * [Szyfrowanie](#szyfrowanie)
  * [Cyfrowe podpisy](#cyfrowe-podpisy)
  * [Warstwy systemu](#warstwy-systemu)
  * [Zwrot ku fizycznym chipom](#zwrot-ku-fizycznym-chipom)
  * [Secure boot](#secure-boot)
* [Ciemne strony](#ciemne-strony)
  * [Zdalna atestacja](#zdalna-atestacja)
  * [Wiązanie programów do sprzętu](#wiązanie-programów-do-sprzętu)
  * [DRM](#drm)
  * [Dystopijne scenariusze](#dystopijne-scenariusze)
* [Co robić?](#co-robić)


## Czym jest *trusted computing*

Zwykle nie lubię kalkować z&nbsp;angielskiego i&nbsp;staram się pisać po polsku. Ale niełatwo znaleźć polskie tłumaczenie dla *computing*, czyli z&nbsp;grubsza czynności od słowa *computer*. „Obliczenia” czy „komputery” wydają mi się zbyt wąskie.

Dlatego wyjątkowo zachowam angielską nazwę. Gdybym miał stworzyć coś polskiego, to chyba postawiłbym na „informatykę mocnych gwarancji” albo „informatykę wysokiego zaufania”. Jest jakiśtam poziom ogólności, plus mgliste podobieństwo do broni masowego rażenia :wink:

Pojęcie ma względnie przystępny [opis](https://en.wikipedia.org/wiki/Trusted_Computing) na angielskiej Wikipedii. Ale gdybym miał go uprościć do dwóch zdań, to napisałbym:

{:.bigspace}
> **rozwiązania technologiczne mające dawać gwarancję, że nikt nie zaingeruje w&nbsp;wybrane procesy. Opierają się na wykorzystaniu fizycznych chipów, szyfrowania i&nbsp;cyfrowych podpisów**.

Takie zagonienie kryptografii do pracy, żeby dostawać zawsze to, czego się chce... Problem w&nbsp;tym, że *osobą dostającą* niekoniecznie jest użytkownik. Mogą to być duże korporacje wpływające na standardy cyberbezpieczeństwa. Ale do tego przejdę później.

{:.figure .bigspace-before}
<img src="/assets/posts/centralizacja/trusted-computing-wprowadzenie/not-to-trust-you.jpg" alt="Angielskie słowa umieszczone na tle stylizowanym na kartkę papieru w kratkę. Mówią: 'to nie tobie postanowili zaufać'." width="250px"/>

{:.figcaption}
Źródło: [filmik](https://www.youtube.com/watch?v=m3iEU5enn14) sprzed, bagatela, kilkunastu lat. Od początku dostrzegano możliwe zagrożenie.

<details class="framed">
<summary><strong>Ciekawostka dotycząca słowa „zaufanie”</strong></summary>

<p>Również pierwsze słowo, <em>trusted</em>, niesie za sobą pewien niuans. Dotyczący nie tłumaczenia (bo to po prostu „zaufane”), tylko kontekstu.</p>
<p>Dla niektórych osób to słowo ma w&nbsp;języku potocznym znaczenie jednoznacznie pozytywne. Na równi z&nbsp;„dobry”, „rzetelny”, „kochany” i&nbsp;podobnymi. Rozumieją zwrot „jest zaufany” jak „na pewno nie wbije mi noża w&nbsp;plecy”.</p>

<p>Tymczasem w&nbsp;kontekście cyberbezpieczeństwa zaufanie ma inne znaczenie. <strong>Jest jak żeton w&nbsp;grze planszowej, który można położyć na wybranej przez siebie rzeczy</strong>. Oczywiście zwykle ma się ku temu jakieś powody, ale nie ma się żadnej gwarancji bezpieczeństwa.<br />
Niektórzy – i&nbsp;to badacze, nie nihiliści – idą z&nbsp;definicją jeszcze dalej. Pokazują zaufanie jako celowe ujawnienie przed kimś swojego słabego punktu.</p>

<p class="figure bigspace-before"><img src="/assets/posts/centralizacja/trusted-computing-wprowadzenie/zaufanie-definicja.jpg" alt="Zwięzła definicja ze slajdu mówiąca, że kiedy komuś/czemuś ufamy, to dajemy mu możliwość zaszkodzenia nam." width="60%" /></p>

<p class="figcaption">Źródło: <a href="https://www.youtube.com/watch?v=_tLi8TnIotM">wykład</a> z&nbsp;2009 roku (YouTube, ok. 2:00).</p>

<p>To chyba żadna tajemnica, że w&nbsp;tym wpisie <em>trusted computing</em> pokaże swoje ciemne strony. Ale nie jest to przypadek, gdy ktoś nadaje dobrą nazwę złej rzeczy. To nie jak z&nbsp;Ministerstwem Miłości u&nbsp;Orwella; tutaj od początku użyto pojęcia technicznego, które nie miało niczego obiecywać.</p>
</details>

## Trusted computing krok po kroku

Omawiane tu metody opierają się na pewnej szczególnie ważnej rzeczy, odróżniającej świat realny od cyfrowego -- **w świecie cyfrowym porównywanie i&nbsp;kopiowanie różnych rzeczy jest w&nbsp;stu procentach dokładne i&nbsp;bardzo szybkie**.

Można wykonywać najdokładniejsze kopie, ani trochę nie rozumiejąc kopiowanej rzeczy.  
To jakby wydać polecenie: „przeskanuj wszystkie atomy (i&nbsp;kwarki, itd.), z&nbsp;jakich składa się ten przedmiot, i&nbsp;stwórz mi taki sam”. W&nbsp;świecie rzeczywistym by to nie przeszło, w&nbsp;cyfrowym to codzienność.

Zapamiętajmy tę właściwość. A&nbsp;teraz czas ułożyć z&nbsp;kawałków, jak z&nbsp;puzzli, obraz *trusted computingu*.

### Szyfrowanie

Kawałek pierwszy: szyfrowanie. Pokażę je na przykładzie przeglądania internetu.  
Jest sobie nasze urządzenie (komputer, smartfon...), a&nbsp;na nim zainstalowana przeglądarka, jak Firefox czy Chrome. I&nbsp;jest cudzy komputer, ale mocniejszy -- *serwer*. Przechowuje całą zawartość jakiegoś portalu internetowego.

Podczas przeglądania internetu klikamy w&nbsp;link prowadzący do tego portalu. Za kulisami nasze urządzenie wysyła serwerowi prośbę (ang. *request*) o&nbsp;konkretną stronkę lub inny zasób, jak zdjęcie kota.

Między tymi dwoma punktami -- naszym komputerem a&nbsp;czyimś serwerem -- mogą tkwić **podglądacze**. Może jakiś zakapturzony haker, może więksi gracze podpięci do światłowodów. Ale najczęściej: operatorzy sieci telekomunikacyjnej.

Rodzaj podglądaczy jest drugorzędny, bo mają zbliżone możliwości. Mogą przechwytywać przelatujące dane i&nbsp;je oglądać. *Wszystkie* dane. Jeśli na widoku będą leciały informacje o&nbsp;naszym urządzeniu, hasła do kont bankowych czy wrażliwe wiadomości, to zostaną obejrzane i&nbsp;zapisane na później. Niedobrze.

<img src="/assets/posts/internet/podstawy/internet-http.jpg" alt="Schemat pokazujący prostą komunikację między laptopem a&nbsp;serwerem. Nad strzałką wychodzącą z laptopa widać napis INFO oraz ikonę kota z&nbsp;pytajnikiem. Od strony serwera wraca strzałka z&nbsp;taką samą ikoną kota. Nad strzałkami widać ikonę wszechwidzącego oka."/>

{:.figcaption}
Źródła: Flaticon (serwer jak wcześniej, [laptop](https://www.flaticon.com/free-icons/computer) od *vectorsmarket15*, [strzałki](https://www.flaticon.com/free-icons/down-arrow) od *Freepik*), obrazek kota z&nbsp;Emojipedii. Przeróbki moje.

Jak ochronić te dane, żeby nawet po (nieuniknionym) przechwyceniu nie miały wartości dla podglądacza? Najlepiej przez szyfrowanie. W&nbsp;kontekście internetu upowszechniło się [szyfrowanie przez HTTPS]({% post_url 2022-08-13-https %}){:.internal}.  
Zachodzi za każdym razem, gdy widzimy adres zaczynający się od `https://`. A&nbsp;jak to działa za kulisami? Czysto intuicyjnie:

1. Nasz komputer/smartfon wysyła serwerowi prośbę o&nbsp;szyfrowany kontakt.
2. Serwer odsyła odpowiednik otwartej kłódki (nie ujawniając klucza do niej).  
   A&nbsp;że kopiowanie jest łatwe -- zob. wstęp -- to odtąd mamy tyle kłódek, ile tylko chcemy.

3. Nasze urządzenie odsyła serwerowi *swoją* otwartą kłódkę (też nie ujawniając klucza).
4. Od teraz wszystkie rzeczy wysyłamy między sobą w&nbsp;pancernych pudełkach.

   My w&nbsp;pudełku zamkniętym na kłódkę serwera (do której tylko on ma klucz). Zaś serwer w&nbsp;pudełku zamkniętym na naszą kłódkę (do której tylko my mamy klucz).

Rzeczy wysyłane w&nbsp;punktach 1-3 -- prośba o&nbsp;kontakt i&nbsp;otwarte kłódki -- same w&nbsp;sobie nie mają wartości dla podglądacza. Nie jest w&nbsp;stanie ich użyć przeciwko nam. A&nbsp;jednak, po zakończeniu całej wymiany, zyskamy silną ochronę.

Podglądacz musi się bezsilnie przyglądać, jak gramy z&nbsp;cudzym serwerem w&nbsp;tego ping&#8209;ponga, wysyłając sobie kolejne składniki i&nbsp;stopniowo zacieśniając naszą szyfrowaną więź. A&nbsp;od punktu 4&nbsp;widzi tylko nieprzeniknione, zaszyfrowane pakiety danych.  
Podelektujmy się chwilę jego bezradnością, jeszcze do niej nawiążę.

<img src="/assets/posts/internet/podstawy/internet-https.jpg" alt="Schemat pokazujący szyfrowaną komunikację między laptopem a&nbsp;serwerem. Wzdłuż strzałek między nimi latają skrzynki z&nbsp;ikoną serca, a&nbsp;nad strzałkami widać ikonę płaczącego wszechwidzącego oka."/>

{:.figcaption}
Źródła: [kłódki i&nbsp;klucze](https://www.flaticon.com/free-icon/padlock_3113142) -- Freepik (serwis Flaticon), skrzynki z&nbsp;gry Portal. Reszta jak wcześniej.


Morał z&nbsp;całej tej historii? **Szyfrowanie pozwala rozpocząć i&nbsp;utrzymać bezpieczną komunikację między dwoma punktami. Nawet gdy wszystko między tymi punktami to terytorium wroga**.  
Na tym etapie widać głównie jasne strony. Szyfry znakomicie chronią prywatność.

<details class="framed">
<summary><strong>Możliwości podglądacza</strong></summary>

<p>Uparty przeciwnik na otarcie łez mógłby próbować coś <a href="/internetowa_inwigilacja/2024/03/28/analiza-ruchu" class="internal">wywróżyć z&nbsp;metadanych</a>, czyli ogólnych informacji o&nbsp;czasie wysłania danych, ich rozmiarze itd.</p>

<p>Od biedy mógłby też przechwytywać niektóre wysyłane rzeczy i&nbsp;je wyrzucać do kosza, nie pozwalając im trafić do odbiorcy. Ale wtedy przestałby być biernym podglądaczem i&nbsp;stałby się <a href="/2022/09/12/dns-ip-cenzura" class="internal">aktywnym cenzorem</a>.</p>

<p>Mógłby również masowo kopiować zaszyfrowane dane i&nbsp;je gromadzić. W&nbsp;nadziei na to, że metody deszyfrowania się kiedyś poprawią i&nbsp;zdoła poznać wszystkie tajemnice. To z&nbsp;kolei zagrożenie związane z&nbsp;nadchodzącymi komputerami kwantowymi.</p>
</details>

### Cyfrowe podpisy

W rozwiązaniu z&nbsp;powyższego przykładu istnieje pewna luka.  
Gdy w&nbsp;punkcie 2&nbsp;otrzymujemy kłódkę, to skąd wiemy, że należy do portalu, który chcemy przeglądać? Że nie jest podpuchą naszykowaną przez podglądacza?

{:.post-meta .bigspace-after}
Gdyby podglądacz podrzucił obu stronom komunikacji swoje fałszywe kłódki, do których ma klucz, to mógłby czytać wymieniane informacje w&nbsp;najlepsze. Nazywa się to oficjalnie atakiem *Man in the Middle*, w&nbsp;skrócie *MitM*.

W tym miejscu wkraczają **cyfrowe podpisy**, czyli metody poświadczenia własności i&nbsp;integralności. 

Można je sobie wyobrazić jak hologram (taki jak na legitymacji studenckiej). Pieczątkę przybijaną na dokumencie. Ogólniej: coś, co z&nbsp;założenia ma tylko osoba upoważniona. Nie dzieli się tym z&nbsp;innymi i&nbsp;używa tego do oznaczania swoich rzeczy. Ktoś inny, znając wygląd tego oznaczenia, może potem weryfikować jego autentyczność.

A przypomnę tu fundamentalną sprawę -- w&nbsp;świecie cyfrowym można dokonywać weryfikacji stuprocentowo dokładnej. O&nbsp;ile w&nbsp;świecie realnym dałoby się podrobić podpis rodzica na zwolnieniu, o&nbsp;tyle w&nbsp;wirtualu to nie przejdzie. Porównany zostanie każdy cyfrowy „atom”, zaś osoba porównująca zawsze dokładnie ustali, czy ma do czynienia z&nbsp;tym, czego oczekiwała.

{:.post-meta .bigspace-after}
W praktyce z&nbsp;podpisami cyfrowymi wiąże się nieco niuansów (wykorzystanie haszy, ścisły związek z&nbsp;szyframi...). Ale na potrzeby tego wpisu potraktuję je po prostu jak trwałe, unikalne oznaczenie.

Odnosząc cyfrowy podpis do opisanej wyżej szyfrowanej komunikacji:

* Wyrabiając dla siebie kłódkę, właściciel strony wypala na niej nazwę tejże strony.
* Na ten napis zostaje nałożone unikalne oznaczenie instytucji certyfikującej.

  Z&nbsp;założenia to organizacja, która nie daje oznaczeń byle komu; jeśli je umieściła, to znaczy że zweryfikowała właściciela kłódki. Jeśli nakładających się oznaczeń jest więcej, bo jedna organizacja poświadcza za tą pod sobą, to mamy do czynienia z&nbsp;*łańcuchem zaufania*.

  <img src="/assets/posts/centralizacja/trusted-computing-wprowadzenie/cyfrowe-podpisy-lancuch-zaufania.jpg" alt="Rysunkowa otwarta kłódka, na której widnieje napis ciemnastrona.com.pl. Na napis nałożona jest naklejka z&nbsp;napisem R10, a&nbsp;na nią jeszcze inna, z&nbsp;napisem ISRG X1."/>

  {:.figcaption}
  Źródła: Flaticon (kłódka jak wcześniej, [nalepka 1](https://www.flaticon.com/free-icon/approve_8622624) od *mynamepong*, [nalepka 2](https://www.flaticon.com/free-icon/approve_8622624) od *juicy_fish*).

* Kiedy przeglądarka dostaje kłódkę (pkt 2&nbsp;części o&nbsp;szyfrach), to porównuje oznaczenie na wierzchu z&nbsp;krótką, wbudowaną w&nbsp;siebie listą oznaczeń zaufanych.
* Jeśli znajdzie je na liście, to znaczy że właściciel kłódki dostał oznaczenie od zaufanego certyfikatora. Tylko w&nbsp;tym wypadku przeglądarka nawiąże szyfrowane połączenie; w&nbsp;innym razie wyświetli błąd.

  {:.post-meta .bigspace-after}
  Warto jednak pamiętać, że pomyślna weryfikacja oznacza jedynie, że szyfrujemy połączenie z&nbsp;tym, z&nbsp;kim chcieliśmy. Nie mówi natomiast niczego na temat (nie-)złośliwości samej odwiedzanej strony.

W ten sposób poznaliśmy kolejny element układanki -- **cyfrowy podpis pozwala ustalić, że jakaś konkretna osoba/organizacja oznaczyła jakąś konkretną rzecz**.

Oczywiście cyfrowe podpisy są znacznie ogólniejsze niż komunikacja internetowa. Mają zastosowanie w&nbsp;każdym przypadku, gdy jedna strona coś znakuje w&nbsp;swój unikalny sposób, zaś druga strona zna wzorzec, z&nbsp;którym porównuje to oznaczenie.  
Łapserdaki stojące między tymi dwiema stronami nie zdołają niczego podrobić w&nbsp;sposób niezauważalny. W&nbsp;końcu w&nbsp;świecie cyfrowym da się porównywać najmniejsze „atomy”.

### Warstwy systemu

Kolejnym składnikiem, po szyfrach i&nbsp;podpisach, są fizyczne chipy. Ale zanim do nich przejdę, pokażę ich szczególną rolę na tle całego systemu.

Każde konsumenckie urządzenie (laptopa, smartfona, peceta...) można sobie wyobrazić jak piramidkę, w&nbsp;której warstwy wyższe są zależne od niższych.  
Fundamentem piramidy są fizyczne elementy, jak procesor czy dysk twardy. Warstwa wyżej to małe programy przypisane do tych elementów i&nbsp;wgrane przez producentów -- *firmware*.  
Na nich opiera się system operacyjny, który można umownie podzielić na dwie warstwy:

* jądro -- bebechy systemu i&nbsp;różne pliki wewnętrzne,
* przestrzeń użytkownika -- interfejs i&nbsp;opcje, które można sobie zmieniać.

Na tym systemie opierają się z&nbsp;kolei różnorodne programy: Firefox, Word, apka TikToka... Na każdym z&nbsp;tych programów mogą się opierać jakieś dodatki, dopasowane specjalnie do niego (jak dodatki blokujące w&nbsp;przeglądarkach).

{:.bigspace-before}
<img src="/assets/posts/apki/apki-piramida.jpg" alt="Schemat pokazujący hierarchię we współczesnym urządzeniu. Ma kształt odwróconej piramidy. Na samym dole mamy ikonę procesora podpisaną CPU. Odchodzą od niej strzałki do ikonek symbolizujących aparat, mikrofon i&nbsp;sieć wi-fi. Cała warstwa jest podpisana 'hardware'. Nad nią w&nbsp;piramidzie mamy kolejno: 'firmware', 'jądro systemu' oraz 'system operacyjny'. Na tej warstwie stoją kolejne piramidy, już nie odwrócone. Jedna z&nbsp;nich jest podpisana 'programy', a&nbsp;na niej stoi warstwa podpisana 'dodatki do programów'."/>

{:.figcaption}
Źródło: ikony Firefoksa i&nbsp;Signala; Flaticon ([CPU](https://www.flaticon.com/free-icon/cpu_984391) od *Freepik*); Emojipedia; piramidka z&nbsp;Wikimedia Commons. Aranżacja i&nbsp;przeróbki moje.

{% include info.html
type="Ciekawostka"
text="Serwery, takie jak te wspomniane przy szyfrowaniu, nie są jakimś odstępstwem od zasad. Też można je przedstawić jako piramidki.  
Na samym dole fizyczny sprzęt (ale mocniejszy, inny niż na urządzeniach osobistych; np. procesory Intel Xeon). Wyżej system operacyjny, zwykle Linux. A&nbsp;jeszcze wyżej programy -- często Nginx, swoisty dyrygent od obsługiwania nadlatujących zapytań. Plus jego orkiestra, czyli inne zainstalowane programy, którym przekazuje zadania."
%}

Ta hierarchia dobrze obrazuje również **kontrolę**. Warstwy niższe narzucają wyższym sposób działania. Pomijając szczególne przypadki (np. wirusy), programy są na łasce ustawień systemowych i&nbsp;nie mogą ich zmieniać. Zaś elementy fizyczne kontrolują wszystko.  
Wniosek? **Jeśli czyjaś kontrola sięgnie najniższych warstw, to ma kontrolę nad całością**.

### Zwrot ku fizycznym chipom

Wszystkie powyższe rzeczy to takie podstawowe składowe współczesnego cyberświata. Wyprzedzają *trusted computing* i&nbsp;istniałyby niezależnie od niego. A&nbsp;teraz powoli wchodzimy w&nbsp;świat samego TC. 

Nie jest w&nbsp;żadnym razie niczym nowym, pierwsze realne koncepcje liczą ponad 20&nbsp;lat. [Historię TC](https://www.microsoft.com/en-us/security/blog/2022/01/21/celebrating-20-years-of-trustworthy-computing/) opisał na swojej stronie Microsoft. Przytaczają tam również mail właściciela firmy, Billa Gatesa, napisany w&nbsp;2002 roku i&nbsp;sugerujący potrzebę zwrotu ku czemuś, co nazwał *trustworthy computing*.

> Wydarzenia z&nbsp;zeszłego roku -- od wrześniowych ataków terrorystycznych po głośne przypadki złośliwych wirusów komputerowych -- przypomniały nam wszystkim, jak ważne jest zapewnienie integralności i&nbsp;bezpieczeństwa naszej infrastruktury krytycznej; zarówno linii lotniczych, jak i&nbsp;systemów komputerowych.

{:.figcaption}
Źródło: [mail Billa Gatesa](https://news.microsoft.com/2012/01/11/memo-from-bill-gates/). Tłumaczenie moje.

{% include info.html
type="Ciekawostka"
text="Jest pewna ironia losu w&nbsp;tym, że Microsoft tak bardzo chciał swoim uszczelnianiem świata zabezpieczyć infrastrukturę, w&nbsp;tym linie lotnicze... A&nbsp;tymczasem [najmocniejsze dotychczasowe uderzenie](/cyfrowy_feudalizm/2024/07/24/crowdstrike){:.internal}, paraliżujące wiele lotnisk, nie przyszło ze strony jakichś hakerów. Wynikało z&nbsp;błędnego działania antywirusa (w&nbsp;uproszczeniu) korporacji CrowdStrike, mającego uprzywilejowane możliwości w&nbsp;jądrze systemu Windows."
%}

A przechodząc do przykładów konkretniejszych niż abstrakcyjne „ataki hakerskie” -- faktycznie było i&nbsp;jest parę problemów, które trudno rozwiązać wyłącznie programowaniem na poziomie systemu:

* Przechowywanie szczególnie wrażliwych danych.

  Żeby działało odblokowanie telefonu odciskiem palca, smartfon musi gdzieś zapisać wzorzec, z&nbsp;którym będzie porównywał przykładane palce. Fajnie, gdyby nie był to zwykły plik na „dysku” smartfona, gdzie każdy może sięgnąć.

* Kradzież dysku twardego.

  Ktoś mógłby wyjąć dysk z&nbsp;komputera (np. oddanego do serwisu) i&nbsp;skopiować z&nbsp;niego wszystkie dane. Rozwiązaniem mogłoby być zaszyfrowanie dysku. Tylko gdzie wtedy zapisywać tajny klucz?

* [*Bootkity* i&nbsp;*rootkity*](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/secure-the-windows-10-boot-process), czyli wirusy infekujące niższe warstwy.

  Niektóre wredne wirusy potrafiły przeniknąć do najgłębszych rejonów piramidki. Nawet jeśli całkiem „ścięło się czubek” (przeinstalowało cały system) -- potrafiły to przeczekać, na przykład wewnątrz *firmware'u*, a&nbsp;potem zainfekować nowy, świeży system.

Wszystkie te problemy można rozwiązać, **tworząc na urządzeniach miejsca tak odizolowane, że nawet użytkownik nigdy nie zdoła tam sięgnąć**.  
Najniższe warstwy urządzenia, ze względu na swoją uprzywilejowaną rolę, wydają się idealną lokalizacją.

Można tam trzymać skompresowany odcisk palca. Klucz szyfrujący dysk. Listę kontrolną pozwalającą uruchamiać system w&nbsp;sposób ściśle kontrolowany, żeby znaleźć wszelkie *bootkity*. A&nbsp;to zaledwie początek [listy możliwości](https://github.com/tpm2dev/tpm.dev.tutorials/blob/master/Intro/README.md).

Na bazie tego ogólnego założenia powstały rozmaite wdrożenia. Czasem odizolowane miejsce to jakiś fragment pamięci, odgrodzony jedynie cyfrowymi barierami. Innym razem to część procesora. Albo osobny, wyspecjalizowany chip. TPM, TEE, HSM... Mnóstwo nazw i&nbsp;odmian, których w&nbsp;tym wpisie nie będę omawiał.

Wszystko sprowadza się do jednej rzeczy, izolacji. I&nbsp;dlatego lubię gromadzić wszystkie warianty pod zbiorczym pojęciem: **enklawy** (inspirowane *secure enclave*, nazwą używaną przez Apple). Ta nazwa, jako jedna z&nbsp;niewielu, podkreśla nie jakieś abstrakcyjne *zaufanie*, lecz właśnie izolację. Odrębność.

<details class="framed">
<summary><strong>Analogie</strong></summary>

<p>Takie małe niezależne obszary kojarzą mi się z&nbsp;kilkoma rzeczami. Streszczę je tutaj, bo może ułatwi to intuicyjne złapanie tematu.</p>

<p>Po pierwsze: są jak <em>ambasady</em>. Choć każdy kraj ma zwykle pełną kontrolę nad swoim terytorium, może mieć u&nbsp;siebie ambasady innych krajów. A&nbsp;te są niezależne i&nbsp;nawet w&nbsp;świetle <a href="https://pl.wikipedia.org/wiki/Eksterytorialno%C5%9B%C4%87">prawa międzynarodowego</a> są jak malutkie wycinki cudzego terytorium wewnątrz jakiegoś większego kraju.</p>

<div style="margin-top:3em;margin-bottom:3em">
  <div class="subcontent-heading">
<span style="padding-left: 10px; padding-right: 15px">
Ciekawostka
</span>
  </div>
  <div class="bold-border" style="padding:10px;border-radius:0px 10px 10px 0px">
    <p style="margin-bottom:0px">Swego czasu wewnątrz ambasady Ekwadoru, takiej enklawy w&nbsp;świecie rzeczywistym, <a href="https://zaufanatrzeciastrona.pl/post/dobry-czy-zly-wikileaks-julian-assange-i-jego-wiele-twarzy/">ukrył się Julian Assange</a>, twórca portalu WikiLeaks. Choć amerykańscy politycy bardzo chcieli go dorwać za ujawnianie ich brudów, nikt nie mógł tak po prostu wtargnąć na teren ambasady. Mogli jedynie czatować na zewnątrz.<br/>
W podobny sposób hakerzy nie mogą się dorwać do wzorca odcisku palca zamkniętego w&nbsp;enklawie (choć tutaj bariery są techniczne, nie prawne).</p>
    
  </div>
</div>

<p>Inne porównanie: enklawy są jak zdolności z&nbsp;niedawno zakończonej mangi <em>Jujutsu Kaisen</em>.</p>

<p>Nie wchodząc w&nbsp;szczegóły: to manga o&nbsp;walkach czarodziejów. Niektórzy mają specjalną zdolność zwaną <em>rozszerzeniem terytorium</em> (właściwie <em>domeny</em>, ale to mogłoby się zanadto kojarzyć komputerowcom :wink:). Po jej użyciu czarodzieje narzucają na pewnym obszarze swoją rzeczywistość. Ich ataki mogą zyskać gwarancję trafienia <em>itede</em>.</p>

<p>Niektórzy mogą to kontrować różnymi „terytoriami kieszonkowymi”, które tworzą wycinek bezpiecznej przestrzeni w&nbsp;tej wrogiej rzeczywistości. Zupełnie jak enklawy na kontrolowanych przez nas urządzeniach.</p>

<p class="post-meta">…Tylko czy to by nie sugerowało, że ktoś traktuje <em>wnętrze naszego urządzenia</em> jak wrogie terytorium?</p>
</details>

### Secure boot

...I *trusted boot*, bo są ze sobą [powiązane](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/secure-the-windows-10-boot-process). Tutaj będzie o&nbsp;tym bardzo pobieżnie, bo zostawię temat na inne wpisy.

Przy każdym uruchomieniu urządzenia **piramidka systemowa buduje się od dołu**. Najpierw malutki program na płycie głównej, potem większy *bootloader*, potem system, na koniec ten system włącza różne swoje programy.

{:.post-meta .bigspace-after}
Słowa *booting* oraz *boot* odnoszą się po prostu do uruchamiania urządzenia. Stąd również *bootloader*.

Enklawy mogą być integralną częścią procesu budowania systemu. Na każdym kroku analizują, czy wszystko jest jak powinno, a&nbsp;dolne partie systemu nie są zainfekowane wspomnianymi wcześniej *bootkitami*. Werdykt zostaje szczelnie zamknięty w&nbsp;enklawie i&nbsp;jest okazywany tylko na żądanie.

I owszem, przed czymśtam to chroni... Tylko że w&nbsp;ten sposób pojawia się **możliwość ustalenia, poza kontrolą użytkowników, czy ich system jest niemodyfikowany**. Zgodny z&nbsp;fabrycznymi ustawieniami, prosto ze stajni takiego np. Microsoftu. A&nbsp;stąd już krótki krok do ciemnych stron.

## Ciemne strony

Do tej pory wszystko było piękne i&nbsp;bajeczne. Nasz komputer, ściśle chroniony przed wirusami. Cudzy serwis -- jak inne, pewnie też bezpieczne terytorium. Internet między nimi -- czasem groźny, ale dzięki szyfrowaniu można go bezpiecznie przemierzać.

<img src="/assets/posts/centralizacja/trusted-computing-wprowadzenie/tc-oczekiwania.jpg" alt="Schemat pokazujący, jak na tle znaku yin i&nbsp;yang przelatuje zaszyfrowane pudełko z&nbsp;nadrukiem serca, wychodząc od serwera, trafiając do chipa, a&nbsp;stamtąd do laptopa."/>

Niestety ta sielanka była tylko pozorna. Firmy postanowiły wykorzystać kryptograficzne gwarancje do zacieśnienia swojej kontroli. Pokażę kilka sposobów, w&nbsp;jakie to zrobiły.

### Zdalna atestacja

To chyba najbardziej jaskrawy przykład nadchodzących patologii, więc to od niego zacznę. Zdalna atestacja polega w&nbsp;skrócie na tym, że **cudzy serwis rozmawia z&nbsp;naszą enklawą ponad naszymi głowami**.

* Zewnętrzny serwis wysyła otwartą kłódkę do naszego komputera, żeby rozpocząć szyfrowaną komunikację. Leci to sobie przez internet, odporne na podglądaczy.
* Dociera do programu/aplikacji na naszym urządzeniu... i&nbsp;nie zatrzymuje się tam, lecąc prosto do enklawy.
* Enklawa odsyła własną kłódkę.

  Cyfrowo podpisaną, więc żaden nasz program jej nie podrobi. Zaś narzędzie do cyfrowych podpisów tkwi wewnątrz enklawy, poza naszym zasięgiem.

* Kłódka od enklawy trafia do zewnętrznego serwisu.
* Od teraz korespondują ze sobą, wymieniając się informacjami.

  A&nbsp;wśród tych informacji mogą być na przykład fakty na temat naszego systemu, zgromadzone przez enklawę na etapie uruchamiania. Mówiące, czy nasz system jest na przykład niezmienianym Windowsem 11&nbsp;prosto od producenta. Jeśli odpowiedź nie spodoba się zewnętrznemu portalowi, bo np. nasz system jest niestandardowy, to może nas spławić.

Pamiętacie wcześniejszy punkt o&nbsp;szyfrowaniu, gdy mogliśmy się napawać bezradnością podglądacza? No to **teraz sami jesteśmy bezradni wobec szyfrowanej, podpisanej cyfrowo komunikacji**. Część naszego własnego urządzenia nas zdradza z&nbsp;cudzym serwisem i&nbsp;działa przeciwko nam. Przypomnę obrazek wprowadzający:

{:.bigspace}
<img src="/assets/posts/centralizacja/trusted-computing-wprowadzenie/trusted-computing-rzeczywistosc.jpg" alt="Smutny człowiek z&nbsp;białą flagą oraz uśmiechnięty ludek z&nbsp;Monopoly po przeciwnych stronach znaku yin i&nbsp;yang. W&nbsp;człowieka wymierzone są dwa pistolety maszynowe, wystające z&nbsp;ciemnych obszarów znaku. Wewnątrz mniejszego czarnego koła, z&nbsp;którego wystaje jeden z&nbsp;nich, znajduje się chip komputerowy"/>

W ten sposób miało działać [Web Environment Integrity]({% post_url 2023-07-29-web-environment-integrity %}){:.internal} -- rozwiązanie proponowane przez Google'a, które pozwoliłoby każdej stronie internetowej wysyłać do przeglądarki Chrome prośbę o&nbsp;weryfikację systemu.  
Nie dość, że umocniłoby to monopol Chrome'a, to do tego mogłoby służyć wykluczeniu rzadziej używanych systemów, jak Linux czy mobilne alternatywy. Zniknęłoby wyjście bezpieczeństwa na wypadek ogólnej monopolizacji.  
Na szczęście porzucili feralny pomysł pod naciskiem opinii publicznej... Ale czy na długo?

### Wiązanie programów do sprzętu

Wspomniałem, że fundamentami piramidki są: *hardware*, czyli fizyczny sprzęt, oraz *firmware*, czyli programy sterujące tym sprzętem. Zwykle nieprzeniknione i&nbsp;wgrane przez producentów. Czasem, ze względu na cięcie kosztów, *firmware* nie wykorzystuje w&nbsp;pełni potencjału sprzętu.

Tu jednak może pomóc pewien fakt -- **w&nbsp;świecie cyfrowym zera i&nbsp;jedynki są sobie równe**. Nie ma czegoś takiego jak zera/jedynki „graficzne” czy „dźwiękowe”. Istnieje oczywiście jakiś *właściwy* sposób ich czytania, ale to już poziom wyżej, kwestia interpretacji.

Zwykle da się dzięki temu podmienić cudzy, dziadowski *firmware* i&nbsp;wgrać tam coś własnego, lepszego, o&nbsp;otwartym kodzie źródłowym. Dopóki będzie to emitowało ciągi zer i&nbsp;jedynek o&nbsp;odpowiednim formacie, zrozumiałym dla sprzętu, to powinno działać sprawnie.

Problem w&nbsp;tym, że poprzez cyfrowe podpisy sprzęt może [weryfikować, czy *firmware* jest taki, jakiego oczekuje]({% post_url 2023-04-26-imx-deblobbing-konsola %}){:.internal}. Zabezpieczenie sztuczne, motywowane głównie chęcią kontroli... Ale skuteczne.  
Kiedy producent przestanie wspierać sprzęt, to rośnie szansa, że nikt nie stworzy otwartego *firmware'u*, żeby go wskrzesić, bo chętni nie będą w&nbsp;stanie podrobić wymaganego, unikalnego oznaczenia. Wszystko będzie musiało trafić do elektrośmieci.

### DRM

DRM to skrót od *Digital Rights Management*. Jak sugerują pierwsze dwa słowa, ma związek z&nbsp;prawami (autorskimi) w&nbsp;świecie cyfrowym. W&nbsp;praktyce to różne metody służące zabezpieczaniu cyfrowych produktów przed kopiowaniem.  

{% include info.html
type="Więcej informacji"
text="DRM to pojęcie szerokie, które nie musi się wiązać z&nbsp;TC. Można je uznać za dwa niezależne zbiory, które pokrywają się tylko w&nbsp;niektórych obszarach.  
Bardzo ciekawe filmy po polsku na temat DRM-ów, w&nbsp;tym również tych klasycznych, sprzed ery TC, stworzył [Kacper Szurek](https://www.youtube.com/watch?v=5JUTni4kgfA&pp=ygURa2FjcGVyIHN6dXJlayBkcm0%3D) (YouTube)."
%}

O ile atestacja uderza w&nbsp;ideę swobody w&nbsp;doborze programów, o&nbsp;tyle DRM **godzi w&nbsp;koncepcję własności**.

To przez niego mogą istnieć takie rzeczy jak filmy czy ebooki, z&nbsp;których nawet po kupnie można korzystać jedynie na zasadach ustalonych przez wydawcę. I&nbsp;działają tylko dopóty, dopóki istnieje ten wydawca.

Nie jest to zresztą mój wymysł. W&nbsp;przypadku ebooków Microsoft wyłączył kiedyś swoją platformę. Użytkownicy otrzymali komunikat: [„w dniu X&nbsp;twoje książki przestaną działać”](https://memex.craphound.com/2019/06/28/microsoft-is-about-to-shut-off-its-ebook-drm-servers-the-books-will-stop-working/).

W przypadku filmów istnieją zabezpieczenia takie jak Widevine od Google'a. Ma kilka poziomów restrykcji. Jeśli chce się oglądać filmy w&nbsp;lepszej jakości, to trzeba mieć urządzenie wspierające [poziom najwyższy, L1](https://www.xda-developers.com/check-widevine-drm-status-android/). Wymagający enklawy i&nbsp;niemodyfikowanego systemu.

W tym trybie zarówno przeglądarka, system, jak i&nbsp;procesor działają przeciw użytkownikowi, tworząc szyfrowany „tunel” między platformą streamingową a&nbsp;monitorem. Z&nbsp;założenia taki, żeby na żadnym etapie nie dało się niczego zescreenować ani przechwycić.

Użytkownik ma konsumować. A&nbsp;kiedy producent na dobre wycofa coś z&nbsp;repertuaru, nie uwalniając jednak licencji, to konsument ma grzecznie pochylić główkę. I&nbsp;pogodzić się z&nbsp;tym, że dorobek kulturowy zniknął na dobre.

### Dystopijne scenariusze

*Trusted computing* raczej nie pozostanie zjawiskiem marginalnym i&nbsp;może rosnąć w&nbsp;siłę. Za jego upowszechnieniem lobbuje organizacja Trusted Computing Group, która niedawno napisała chociażby:

> Hakerzy coraz częściej przejmują kontrolę nad urządzeniami podłączonymi do sieci, wyposażonymi między innymi w&nbsp;kamery, mikrofony i&nbsp;GPS. Ze względu na naturę zagrożenia, potrzeba zwiększania bezpieczeństwa jest większa niż kiedykolwiek wcześniej.

{:.figcaption}
Źródło: [tweet Trusted Computing Group](https://x.com/TrustedComputin/status/1844748236021739856). Tłumaczenie moje.

Google również działa aktywnie na rzecz uszczelniania systemu Android. Pomijając wspomniany wcześniej pomysł Web Environment Integrity, niedawno dali aplikacjom na Androida możliwość ustalania, czy zostały [zainstalowane przez oficjalną bazę Play Store](https://www.telepolis.pl/wiadomosci/aplikacje/android-koniec-instalowania-aplikacji-spoza-sklepu-google-play) (należącą do Google'a).

Niektóre z&nbsp;nich zapewne wykorzystają tę wiedzę do blokowania użytkowników alternatywnych, przyjaznych systemów mobilnych, jak LineageOS czy GrapheneOS. To ograniczenie sztuczne, nieuzasadnione. Do tego niekoniecznie związane z&nbsp;bezpieczeństwem, bo Graphene akurat góruje pod tym względem nad zwykłym Androidem. Jego twórcy [rozważają pozwanie Google'a](https://www.androidauthority.com/custom-roms-vs-google-3469378/) za działania antykonkurencyjne.

Najnowszy system Microsoftu, Windows 11, **wprost wymaga modułu TPM w&nbsp;wersji 2.0 lub nowszej**. Czyli: fizycznego chipa poza zasięgiem użytkowników, rodzaju enklawy.  
Oznacza to, że różne programy z&nbsp;upływem lat coraz częściej będą mogły zakładać jego obecność i&nbsp;nakładać na użytkowników dowolne restrykcje.

Wszystkie te trajektorie są niepokojące. Ale scenariusz prawdziwie cyberpunkowy nastąpiłby wówczas, gdyby do gry weszli gracze państwowi.  
Gdyby obywatele musieli na mocy przepisów mieć jakąś aplikację, zaś aplikacja dopuszczałaby poprzez *trusted computing* tylko nieliczne, najpopularniejsze systemy od dużych firm -- to mamy gotowy przepis na dystopijne, zmonopolizowane państwo.  
To zagrożenie na razie teoretyczne. Ale na tyle istotne, że warto cały czas mieć je w&nbsp;głowie.

## Co robić?

Przede wszystkim -- **szerzyć świadomość zagrożenia, bo jest bardzo niska**.

Można też przesiąść się na alternatywne produkty. W&nbsp;miarę możliwości [odgooglować swojego Androida]({% post_url 2024-02-03-smartfon-degoogle %}){:.internal}; spróbować Linuksa zamiast Windowsa (jest naprawdę przystępny; szczególnie w&nbsp;przypadku, gdy większość czasu spędza się w&nbsp;przeglądarce).

Protestować z&nbsp;całą mocą, gdyby państwo próbowało wprowadzić przymusem programy lub aplikacje, nie gwarantując zarazem pełnej otwartości ich kodu.

Warto wykazać zrozumienie i&nbsp;wsparcie dla pomniejszych projektów *open source*, nawet jeśli mają swoje niedogodności. Im więcej osób wejdzie w&nbsp;ten ekosystem, tym większy opór napotkają korporacje przy próbach jego stłamszenia.

Widzę również pewne możliwości na poziomie społecznym.  
Warto **publicznie odtrącać gadżety, ślepy konsumpcjonizm i&nbsp;tandetną „nowoczesność”**. Nie wpuszczać do swojego domu pierdół z&nbsp;Doliny Krzemowej czy jej chińskiego odpowiednika, opartych na zamkniętym oprogramowaniu: badziewnych gadżetów, asystentów głosowych, samojezdnych odkurzaczy i&nbsp;podobnego szmelcu.

Oczywiście marketingowa propaganda będzie się wtedy miotać, wyzywać od luddystów i&nbsp;jaskiniowców. Ale te słowa w&nbsp;moich oczach stopniowo stają się komplementami :wink:
