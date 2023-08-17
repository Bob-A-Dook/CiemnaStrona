---
layout: post
title: "Apki to pułapki 6 – śledzenie lokalizacji"
subtitle: "Aplikacje wiedzą, gdzie nas znaleźć."
description: "Aplikacje wiedzą, gdzie nas znaleźć."
date:   2023-07-15 14:24:00 +0100
tags: [Apki, Hardware, Inwigilacja, Podstawy]
firmy: [Google]
category: apki
category_readable: "Apki to pułapki"
image:
  path: /assets/posts/inwigilacja/sledzenie-lokalizacji/location-tracking-banner.jpg
  width: 1200
  height: 700
  alt: "Zdjęcie pokazujące planetę Ziemię, na którą nałożono lupę. W powiększeniu widać mangową postać w kapeluszu. Wokół lupy widać proste czerwone ikonki odpowiadające funkcjom telefonu"
---

Witam w&nbsp;kolejnym -- po dłuższej przerwie -- wpisie z&nbsp;serii „Apki to pułapki”!

Tradycyjnie omówię różne informacje, jakie wścibskie firmy mogą odczytać z&nbsp;naszego telefonu, głównie przez zainstalowane na nim aplikacje.

Tym razem skupimy się na różnorodnych czujnikach, które mogą -- z&nbsp;osobna albo we współpracy ze sobą -- **pokazać z&nbsp;dużą dokładnością, w&nbsp;jakim miejscu się znajdujemy**. I&nbsp;śledzić na tej podstawie nasze wędrówki.

Spojrzymy na rzeczy oczywiste, takie jak wbudowany GPS. A&nbsp;także nieco bardziej zaskakujące, jak mikrofon czy nawet akcelerometr.

Zapraszam!

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/sledzenie-lokalizacji/location-tracking-banner.jpg" alt="Planeta Ziemia, na którą nałożono zdjęcie lupy. W&nbsp;jej powiększeniu widać postać z&nbsp;mangi w&nbsp;płaszczu i&nbsp;kapeluszu. Wokół lupy widać proste czerwone ikonki odpowiadające funkcjom telefonu: mikrofonowi, Wi-Fi, Bluetoothowi, internetowi oraz GPS-owi."/>

{:.figcaption}
Źródła: Ziemia i&nbsp;lupa od Wikimedia Commons, [ikona mikrofonu](https://www.flaticon.com/free-icon/microphone_9790386) autorstwa *kliwir art* ze strony Flaticon, ikonki systemu Huawei, manga *Battle Angel Alita: Last Order*. Przeróbki moje.

### Spis treści

* [GPS](#gps)
* [Śledzenie przez inne moduły](#śledzenie-przez-inne-moduły)
  * [Wi-Fi](#wi-fi)
  * [Bluetooth](#bluetooth)
  * [Mikrofon](#mikrofon)
  * [Akcelerometr](#akcelerometr)
* [Śledzenie przez sieć komórkową](#śledzenie-przez-sieć-komórkową)
* [Jak się chronić](#jak-się-chronić)


## GPS

To najprostsza sprawa. Aplikacja mająca uprawnienia do danych z&nbsp;GPS-a (*Global Positioning System*) może tak po prostu zapytać systemu: „Gdzie jest ten użytkownik?”. W&nbsp;odpowiedzi dostanie komplet współrzędnych.

Jeśli w&nbsp;ciągu dnia nie wyłączamy GPS-a, to apka może cały czas żłopać te dane i&nbsp;dokładnie poznać różne informacje:

* nasze miejsce zamieszkania  
  (tam, gdzie w&nbsp;godzinach nocnych zwykle przestają się zmieniać wspołrzędne);
* miejsce pracy  
  (o&nbsp;ile nie mamy zdalnej, to będzie to miejsce, które regularnie odwiedzamy w&nbsp;tygodniu);
* preferencje komunikacyjne  
  (samochód czy komunikacja miejska -- odczyt na podstawie szybkości ruchu oraz miejsca startu);
* udział w&nbsp;zgromadzeniach  
  (kiedy z&nbsp;jednego miejsca przybywa więcej danych o&nbsp;lokalizacji);
* osoby, u&nbsp;których nocowaliśmy  
  (najpierw wyłapanie nocy, kiedy nie jesteśmy tam gdzie zwykle; następnie wyszukanie tego miejsca w&nbsp;bazie wszystkich użytkowników. Zadziała nawet wtedy, gdy osoba, która nas gości, zwykle wyłącza GPS&#8209;a).

I tak dalej, opcji jest multum. Niektóre informacje może pozyskać każda apka. Te dotyczące zgromadzeń i&nbsp;korelacji międzyludzkich to raczej domena apek popularniejszych. Taki na przykład Google zdobyłby je bez problemu.

GPS działa niezależnie od sieci komórkowej. Jak najbardziej może się zdarzyć, że nie mamy zasięgu, ale geolokalizacja śmiga całkiem nieźle. Nie zadzwonimy, nie zajrzymy do internetu... Ale wiemy, gdzie jesteśmy. Wiedzą to również apki mające dostęp do odczytów GPS-a.

{:.figure}
<img src="/assets/posts/inwigilacja/sledzenie-lokalizacji/gps-bez-sieci.jpg" width="450px" alt="Zrzut ekranu z&nbsp;telefonu, pokazujący fragment mapy turystycznej oraz niebieską kropkę odpowiadającą aktualnemu położeniu właściciela. W&nbsp;górnym pasku z&nbsp;informacjami wyróżniono tekst mówiący o&nbsp;braku zasięgu sieci. Jest tam również ikona pinezki, oznaczająca że GPS jest włączony i&nbsp;działa."/>

{:.figcaption}
Losowe miejsce w&nbsp;Beskidzie Żywieckim, gdzie nie ma łączności telefonicznej. Ale GPS śmiga.  
Mapka wyświetla się tylko dlatego, że to *Mapy.cz* w&nbsp;wersji offline, pobrane na zapas.

Dokładność GPS-a miewa swoje wahania. Przykład z&nbsp;życia? W&nbsp;niektórych górskich i&nbsp;zalesionych okolicach potrafiło pokazać, że jestem kilkanaście kilometrów dalej niż w&nbsp;rzeczywistości.  
Ale nie ma co polegać na niedokładnościach. Dla aplikacji byłoby całkiem łatwe wykrycie takich anomalii i&nbsp;usunięcie ich ze zbioru danych.

Warto pamiętać, że GPS może być dla nas groźny również w&nbsp;sposób pośredni -- przez **geotagowanie zdjęć**.

To funkcja dostępna zwykle w&nbsp;systemowej apce Aparat. Jeśli ją włączymy, to do każdego zrobionego zdjęcia [zostaną dodane nasze współrzędne]({% post_url 2021-02-10-gdzie-jestem-zapytaj-moich-zdjec %}){:.internal} w&nbsp;momencie jego robienia.

I tak -- trafią one bezpośrednio do pliku ze zdjęciem, nie do jakiejś wewnętrznej bazy telefonu. Co oznacza, że każda apka mająca dostęp do plików (nawet jeśli nie ma dostępu do GPS-a) może sobie te koordynaty łatwo odczytać.

{% include info.html
type="Ciekawostka"
text="Choć śledzenie konkretnych osób najbardziej narusza prywatność, czasem nawet informacje zanonimizowane i&nbsp;uśrednione mogą ujawniać sekrety.  
Przykład? Aplikacja Strava (od statystyk dotyczących aktywności fizycznej) tworzyła na podstawie anonimowych statystyk mapy cieplne pokazujące, jak często różni ludzie trenują na danej trasie.  
Użytkownicy wypatrzyli dziwne ślady treningów pośrodku pustyni. Jak się okazało -- były to trasy [patroli w&nbsp;bazie wojskowej](https://businessinsider.com.pl/technologie/nowe-technologie/aplikacja-strava-dane-z-map-ujawnily-tajne-bazy-wojskowe/9rvwvt9)."
%}

## Śledzenie przez inne moduły

Skoro już mamy z&nbsp;głowy najprostszego GPS-a, to czas na mniej oczywiste metody, polegające na innych modułach naszego telefonu. Jak modem, mikrofon, Bluetooth. **Każda z&nbsp;tych metod śledzenia zadziała nawet wtedy, gdy mamy wyłączony GPS**.

### Wi-Fi

Czasem nie chcemy płacić za zużycie danych mobilnych. Wyświetlamy sobie zatem listę hotspotów, punktów dostępu do internetu. Znajdujemy jakiś publicznie dostępny, łączymy się z&nbsp;nim.

Ta czytelna, widoczna dla nas nazwa (jak *Hostel Guest*, *Uczelnia Free*, *McD Hotspot*) to według oficjalnego nazewnictwa `SSID`. Oprócz niej routery wysyłają również `BSSID` -- mniej czytelny, za to (teoretycznie) unikalny numer. Zwykle nie pokazuje się nam, ale nasz telefon go widzi.

Jeśli hotspot nie jest czymś tymczasowym, tylko fizycznym routerem, to jest spora szansa, że nie ruszy się z&nbsp;miejsca. Zarówno jego fizyczne położenie, jak i&nbsp;cyfrowy identyfikator, długo pozostaną niezmienne.

A ta stałość otwiera furtkę do śledzenia -- **można tworzyć wielkie bazy danych łączące numery hotspotów z&nbsp;ich konkretnymi położeniami w&nbsp;świecie fizycznym**. Zbieranie tych danych określa się jako *wardriving*.

I takie bazy hulają w&nbsp;najlepsze:

* Wozy Google'a jeździły po świecie, robiąc zdjęcia ulic na potrzeby projektu StreetView. Ale nie każdy wie, że jednocześnie [budowały wielkie bazy](https://www.darkreading.com/risk/google-wardriving-how-engineering-trumped-privacy) łączące identyfikatory hotspotów z&nbsp;ich fizycznymi lokalizacjami.
* Telefony innych firm (np. Huawei) same oferują funkcję dokładniejszego lokalizowania na podstawie danych o&nbsp;Wi-Fi. Opiera się ona właśnie o&nbsp;takie bazy.
* Nawet hobbyści zebrali całkiem pokaźne ilości danych, chociażby w&nbsp;bazie [Wigle](https://wigle.net/).

  {:.figure}
  <img src="/assets/posts/inwigilacja/sledzenie-lokalizacji/wigle-polskie-morze.jpg" alt="Zrzut ekranu pokazujący mapkę, na której widać Gdańsk oraz fragment Półwyspu Helskiego. Niektóre miejsca nad brzegiem oznaczone są jaskrawymi kolorami, tam gdzie liczba wykrytych hotspotów jest największa."/>

  {:.figcaption}
  Hotspoty nad polskim morzem. Może nieco ich mniej niż parawanów, ale nieznacznie.  
  Mapkę można zbliżać, uzyskując dokładność do pojedynczych punktów. 

Jeśli autorzy apki-szpiega z&nbsp;naszego telefonu mają dostęp do takiej bazy, a&nbsp;my mamy włączone Wi-Fi i&nbsp;nie jesteśmy w&nbsp;kompletnej dziczy (czytaj: mamy w&nbsp;zasięgu hotspoty), to nas zlokalizują. Nawet jeśli mamy wyłączonego GPS-a.

Nasz telefon wykona skan, szukając hotspotów w&nbsp;okolicy. Zbierze ich identyfikatory. Apka sięgnie do tej listy i&nbsp;wyśle ją autorom. A&nbsp;ich serwery sprawdzą, jakiej lokalizacji odpowiadają te identyfikatory. Dowiedzą się, gdzie jesteśmy. *Nawet jeśli ostatecznie nie połączymy się z&nbsp;żadnym z&nbsp;tych hotspotów*.

Czasem apka mogłaby nawet odgadywać miejsce na podstawie samych nazw, nie mając dostępu do bazy geograficznej. Jeśli wśród nazw hotspotów wokół nas powtarza się nazwa znanego parku rozrywki... No to gdzie my możemy być? :wink:

### Bluetooth

Bluetooth, czyli wszechstronny protokół od przesyłania danych. Dzięki niemu możemy na przykład wysłać komuś plik bez użycia internetu albo puszczać muzykę przez głośnik bezprzewodowy.

Kiedy urządzenia chcą się skomunikować przez Bluetooth, to każde z&nbsp;nich wysyła w&nbsp;eter swój unikalny identyfikator. Inne mogą je znaleźć i&nbsp;poprosić o&nbsp;połączenie. Trochę jak w&nbsp;przypadku hotspotów.

Różnica polega na tym, że Bluetooth nie jest tak publiczny i&nbsp;stały jak Wi-Fi. Śledzenie nie opiera się zatem na odpytywaniu jakiejś wielkiej bazy.  
Zamiast tego firma chcąca śledzić użytkowników kupuje zestaw małych nadajników, tak zwanych *beaconów*. Każdy ustawia w&nbsp;innym miejscu. Każdy emituje swój unikalny identyfikator.

Aplikacja na naszym smartfonie, należąca do właściciela *beaconów* (albo innej, współpracującej z&nbsp;nią firmy), prowadzi z&nbsp;kolei nasłuch. Jeśli wyłapie któryś z&nbsp;charakterystycznych identyfikatorów, to może zapytać swojej wewnętrznej bazy, gdzie jesteśmy.

{:.bigspace}
> **Pytanie:** Telefon użytkownika X&nbsp;wykrył sygnał Beacona 7778. Gdzie to jest?  
**Odpowiedź:** Galeria Invigilada, drugie piętro, toaleta męska. Kabina po lewej.

Żeby skuteczenie używać *beaconów*, firmy musiałyby w&nbsp;jakiś sposób kontrolować przestrzeń, w&nbsp;której je rozmieszczą. Dlatego szczególnie narażone na śledzenie będą osoby w&nbsp;miejscach takich jak galerie handlowe, parki rozrywki, kampusy i&nbsp;tym podobne.

Raczej żadna firma nie jest na tyle potężna, żeby poustawiać swoje *beacony* po całym świecie. Co nie znaczy, że kiedyś nie spróbują.

Aplikacje wykorzystujące tę metodę śledzenia znajdziemy w&nbsp;świecie rzeczywistym. Aplikacja AccuWeather (od aktualnej prognozy pogody) [wysyłała współrzędne GPS oraz numery hotspotów firmie analitycznej](https://medium.com/hackernoon/advisory-accuweather-ios-app-sends-location-information-to-data-monetization-firm-83327c6a4870). Wprost chwalili się również, że wspierają *beacony Bluetooth* i&nbsp;również wykorzystują dane z&nbsp;nich do dokładniejszego śledzenia.

{% include info.html
type="Wątek Google'a"
text="Aplikacja Google Maps podobno kiedyś [wymagała dostępu do danych dotyczących hotspotów](https://news.ycombinator.com/item?id=30167865), żeby w ogóle działać.  
Mimo że zupełnie dobrze by sobie radziła z&nbsp;samym GPS-em. Wszystko wskazuje na próbę sięgnięcia po więcej danych (i&nbsp;na temat użytkowników, i&nbsp;hotspotów na świecie).  
Zaznaczę, że Google'a staram się nie wpuszczać w&nbsp;swoje życie. Apki nie mam, więc nie potwierdzę doniesień. Ale podlinkowane forum jest dośc wiarygodne."
%}

### Mikrofon

Tutaj sprawa jest bardzo podobna jak z&nbsp;Bluetoothem. Autor wścibskiej apki (albo jego partner biznesowy) nabywa *beacony* -- małe nadajniki, tylko że wysyłające [dźwięk na skraju słyszalności]({% post_url 2023-03-26-apki-mikrofon-zagrozenia %}#dźwięk-wsłużbie-śledzenia){:.internal}.

Każdy z&nbsp;tych dźwięków jest nieco inny. Mikrofon, czulszy niż ludzkie ucho, powinien być w&nbsp;stanie to wyłapać. A&nbsp;wtedy apka dostanie jednoznaczną informację -- jesteśmy w&nbsp;pobliżu konkretnego nadajnika, a&nbsp;zatem w&nbsp;konkretnym miejscu.

{:.bigspace}
> \[ LOGI APLIKACJI „NASŁUCH” OD BIG BRO SP. Z&nbsp;O.O. \]  
Konto podpięte -- Dawid M. (27&nbsp;lat, *dużo innych danych*).  
Sprawdzanie mikrofonu...  
Wykryto sygnał znanego czujnika (nr 37293).  
Sprawdzanie czujnika w&nbsp;bazie...  
Ustalona lokalizacja -- Galeria Invigilada, drugie piętro, placówka okulistyczna.  
Wstępna analiza -- „Dawid M. może mieć problemy ze wzrokiem.”  
Wyniki analizy wysłano do Big Bro Sp. z&nbsp;o.o.

Z punktu widzenia śledzących firm ta opcja może być mniej wygodna niż Bluetooth. Nowsze wersje systemów wyświetlają ostrzegawczą kropkę, gdy działa nam mikrofon.

Poza tym wszystko mocno zależy od czułości naszego mikrofonu. Zapcha się okruchami po ciastkach albo zatonie między warstwami ciuchów w&nbsp;plecaku? Peszek, śledzenie nie zadziała. Tym niemniej warto wiedzieć o&nbsp;istnieniu tej metody.

### Akcelerometr

To może być dla niektórych największym szokiem, ale tak -- najzwyklejszy akcelerometr (*przyspieszeniomierz*) może działać przeciwko nam. **To moduł bardzo wyczulony na ruch, informujący o&nbsp;zmianie położenia w&nbsp;przestrzeni**.

Jest wykorzystywany chociażby do liczenia naszych kroków albo wykrywania, czy się przewróciliśmy. Jest na tyle dokładny, że może nawet wyłapywać drgania powietrza i&nbsp;działać w&nbsp;roli ubogiego mikrofonu (nie na tyle dokładny, żeby nagrywać; ale może np. [odgadnąć płeć rozmówcy](https://dl.acm.org/doi/pdf/10.1145/3309074.3309076) na podstawie barwy głosu).

Poświęcę mu jeszcze osobny wpis, ale póki co skupmy się na śledzeniu lokalizacji. Akcelerometr gromadzi i&nbsp;analizuje dane o&nbsp;przyspieszeniach, jakie oddziaływały na telefon. Na tej podstawie może wyłapać, *skąd i&nbsp;dokąd* się przemieściliśmy oraz jakiego użyliśmy środka transportu.

Akcelerometr nie ujawni naszego dokładnego położenia sam z&nbsp;siebie. Ale jeśli apka-szpieg znajdzie jakiś punkt zaczepienia, to może użyć danych z&nbsp;niego do uzupełnienia obrazu naszej lokalizacji.

Wyobraźmy sobie przykład z&nbsp;życia. Wyjeżdżamy w&nbsp;Bieszczady, skuszeni opowieściami o&nbsp;tamtejszej dziczy, wolności od spraw biznesowych i&nbsp;tym podobnego syfu. Planujemy nocować w&nbsp;bazie namiotowej. Na naszym telefonie jest apka, która nie szanuje prywatności.

* Wysiadamy w&nbsp;Wetlinie. Nigdy tu nie byliśmy, więc dla pewności odpalamy GPS-a. Albo może siadamy w&nbsp;którejś z&nbsp;pobliskich knajp i&nbsp;łapiemy tam ostatni haust Wi-Fi przed planowanym cyfrowym detoksem?

  W&nbsp;każdym razie -- aplikacja zapisuje sobie naszą lokalizację. Ma punkt odniesienia.

* Wiemy już, dokąd iść. Wyłączamy wszystkie czujniki (w&nbsp;tym Wi-Fi i&nbsp;GPS-a). Drepczemy do bazy.

  Na tym etapie pałeczkę przejmuje akcelerometr. Zapisuje sobie naszą prawdopodobną trasę od ostatniej znanej lokalizacji. Najpierw żwawy ruch pieszy, potem tylko minimalne drgania.  
  Do tego, pytając system o&nbsp;godzinę, apka ustala, że brak ruchu koreluje z&nbsp;nocną porą. Wniosek? Dotarliśmy do noclegu. A&nbsp;po połączeniu danych odczyta, że była nim baza PTTK.

* Mamy wyłączony internet, więc na razie zapisuje to wszystko *offline*, do plików. Ale kiedy odzyskamy łączność, to komplet danych poleci do autorów aplikacji.

  Algorytmy zdiagnozują nas jako turystów. Zaczną nam się wyświetlać reklamy promujące drogie, komercyjne wyjazdy namiotowe i&nbsp;*glampingowe*. Tyle z&nbsp;naszego detoksu.

<img src="/assets/posts/inwigilacja/sledzenie-lokalizacji/gps-akcelerometr-osobne-dane.jpg" alt="Dwa zrzuty ekranu obok siebie, pokazujące działanie różnych czujników. Pierwszy, podpisany 'Sam GPS', pokazuje mały fragment mapy z&nbsp;oznaczoną pinezką-położeniem. Drugi, podpisany 'sam akcelerometr', pokazuje niebieski ślad idący z&nbsp;północy na południe. W&nbsp;tle widać jednak tylko czerń, nie ma żadnej mapy."/>

<img src="/assets/posts/inwigilacja/sledzenie-lokalizacji/gps-akcelerometr-fuzja-danych.jpg" alt="Zrzut ekranu pokazujący nałożenie na siebie dwóch rodzajów danych. Widać zarówno pinezkę startową w&nbsp;Wetlinie oraz niebieski ślad z&nbsp;akcelerometru, tym razem nałożony na rzeczywistą mapę i&nbsp;kończący się w&nbsp;bazie namiotowej."/>

{:.figcaption}
Źródło map: OpenStreetMap.

Ta metoda ma oczywiście niedoskonałości, ale na krótszą metę może być zadziwiająco trafna. Zwłaszcza jeśli będą powstawały coraz dokładniejsze akcelerometry.  
Jest też o&nbsp;tyle wredna, że **aplikacje nie muszą pytać o&nbsp;pozwolenie na dostęp do akcelerometru**. To dane, do których mogą sobie tak po prostu sięgnąć.

## Śledzenie przez sieć komórkową

Przy tylu sposobach na ustalanie lokalizacji można zwątpić w&nbsp;smartfony.  
I załóżmy, że zwątpiliśmy. Wyłączamy wszystkie dodatkowe moduły, cofamy pozwolenia wszystkim aplikacjom.

Albo w&nbsp;ogóle nie używamy smartfona, tylko *oldschoolowego* telefonu komórkowego. Jak te z&nbsp;wielkimi klawiszami, przeznaczone dla osób starszych (miałem, polecam; dało się nawet robić zdjęcia w&nbsp;jakości tostera i&nbsp;wysyłać znajomym przez wiadomości MMS).

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/sledzenie-lokalizacji/stara-nokia-3310.jpg" alt="Zdjęcie pokazujące stary telefon komórkowy, Nokię 3310, z&nbsp;fizycznymi klawiszami oraz emotką wyświetloną na ekranie" width="300px"/>

{:.figcaption}
Klasyczna Nokia 3310. Niezniszczalna, ale nawet ona nas nie ocali przed śledzeniem.  
Źródło: [Wikimedia Commons](https://en.m.wikipedia.org/wiki/File:Nokia_3310_blue_R7309170_wp.jpg). Zdjęcie autorstwa Rainera Knäppera.

Czy nasza prywatność jest chroniona? Przed większością firm -- tak. Ale nie do końca.

Istnieje bowiem **metoda ustalania lokalizacji przez sieć komórkową. Nie wymaga żadnej apki i&nbsp;żaden telefon nie będzie na nią odporny. Przez sam fakt, że jest telefonem**.

Cała metoda działania jest z&nbsp;grubsza podobna do tego, co widzieliśmy wcześniej przy hotspotach. Cały świat jest obstawiony jakimiś punktami wejścia do sieci -- tyle że tym razem komórkowej. Stacje bazowe, nadajniki GSM, jak zwał.

{:.post-meta .bigspace-after}
Gdybyśmy chcieli lepiej sobie wyobrazić zagęszczenie nadajników, to proponuję zerknąć do otwartej bazy [OpenCelliD](https://opencellid.org).

Nasz telefon, łącząc się z&nbsp;taką stacją, wysyła swój unikalny numer. Zaś operatorzy telekomunikacyjni (jak Orange, Play...) posiadają listę lokalizacji odpowiadających poszczególnym stacjom. Mogą skorelować dane z&nbsp;kilku nadajników naraz i&nbsp;całkiem dokładnie ustalić nasze położenie. 

A czy do danych o&nbsp;nadajnikach w&nbsp;naszym sąsiedztwie mogą sięgnąć cudze aplikacje? Przetestowałem to z&nbsp;użyciem apki Termux (komenda `termux-telephony-cellinfo`) i&nbsp;mam mieszane wieści.

1. Aplikacja [musi mieć dostęp do GPS&#8209;a](https://github.com/termux/termux-api/issues/307), żeby sięgnąć po te dane.

   To mocne ograniczenie dla wścibskich apek. A&nbsp;gdyby miały dostęp do GPS-a, to i&nbsp;tak lepiej by znały nasze położenie niż przez jakieś nadajniki.

2. Ale jest tak od wersji 8&nbsp;Androida, co może sugerować, że poprzednie wersje systemu tak po prostu udzielały tej informacji na życzenie.

   Nie zagłębiałem się w&nbsp;temat. Ale gdyby tak było, to wścibska aplikacja (dowolnej firmy, niekoniecznie telekomunikacyjnej) mogłaby pewnie wyciągnąć dane o&nbsp;stacjach wokół nas, sprawdzić je w&nbsp;bazie i&nbsp;ustalić, gdzie jesteśmy. Analogicznie jak przy hotspotach.

Załóżmy natomiast, że aplikacje nie dostaną tych danych, że będzie je miał tylko operator telekomunikacyjny. Czy w&nbsp;takim wypadku powinniśmy się obawiać? Niestety tak.

Po pierwsze, nie wszędzie mamy Europę i&nbsp;przepisy chroniące prywatność danych. **Znani amerykańscy operatorzy telekomunikacyjni wprost sprzedawali dane o&nbsp;lokalizacji swoich użytkowników**. Uzyskane właśnie przez sieć komórkową, bez udziału żadnych aplikacji.

Informacje [trafiały najpierw](https://www.zdnet.com/article/us-cell-carriers-selling-access-to-real-time-location-data/) do mniej znanej firmy, a&nbsp;następnie były kupowane przez oficjalne rządowe agencje (aby obejść zakaz bezpośredniego kupowania przez rząd od telekomów).  
Telekomy oberwały za cały proceder [wielomilionowymi karami](https://www.wired.com/story/fcc-fines-wireless-companies-selling-users-location-data/).

A nawet jeśli same telekomy będą niegroźne, to mogą istnieć prywatne firmy wykorzystujące słabości ich infrastruktury do [lokalizowania konkretnych telefonów](https://zaufanatrzeciastrona.pl/post/jak-namierzyc-lokalizacje-dowolnej-komorki-na-calym-swiecie/).

## Jak się chronić

Żeby aplikacje nie mogły tak łatwo się dowiedzieć, gdzie jesteśmy, przyda się wyrobienie paru dobrych nawyków. Przede wszystkim minimalizacja.

Po pierwsze -- **ograniczamy się tylko do kilku zaufanych aplikacji**. I&nbsp;nie mam tutaj na myśli „bierzemy tylko z&nbsp;oficjalnego źródła, PlayStore'a”. Całkiem przydatne i&nbsp;minimalistyczne aplikacje *open source* możemy na przykład znaleźć w&nbsp;alternatywnym F-Droidzie.

Warto patrzeć na informacje o&nbsp;twórcach i&nbsp;zachować szczególną podejrzliwość wobec aplikacji stworzonych przez amerykańskie startupy z&nbsp;Doliny Krzemowej. Tam jest inna mentalność i&nbsp;mniej szanuje się dane użytkowników niż w&nbsp;Europie.

Po drugie -- ograniczamy liczbę pozwoleń, jakie mają przyznane aplikacje. Jeśli już jakiegoś udzielamy, to najlepiej w&nbsp;trybie `Tylko podczas korzystania`, żeby nie hulało cały czas w&nbsp;tle.

Z tych modułów, które omówiłem w&nbsp;tym wpisie, poprzez system pozwoleń możemy regulować dwa -- mikrofon oraz GPS-a.  
Osobiście daję dostęp do tego pierwszego tylko oficjalnej, systemowej apce do nagrywania wideo. Z&nbsp;kolei do GPS-a może zerkać tylko aplikacja *Mapy.cz*.

Aby chronić się przed lokalizowaniem przez Bluetooth i&nbsp;Wi-Fi, warto mieć je wyłączone, kiedy z&nbsp;nich nie korzystamy (czyli raczej przez większość czasu). Włączajmy tylko na krótki czas -- gdy trzeba coś przesłać albo zerknąć do sieci.  
Dodatkowa zaleta: pomijając kwestie prywatnościowe, w&nbsp;ten sposób oszczędzimy nieco baterii.

<img src="/assets/posts/inwigilacja/sledzenie-lokalizacji/telefon-ustawienia-dobre-niedobre.jpg" alt="Dwa zrzuty ekranu, jeden pod drugim, pokazujące ikony odpowiadające za włączanie różnych funkcji na smartfonie. U&nbsp;góry, przy obrazku oznaczonym czerwonym krzyżykiem, większośc czujników jest włączona. U&nbsp;dołu, przy obrazku oznaczonym zielonym znaczkiem OK, włączony jest tylko internet mobilny." width="500px"/>

{:.figcaption}
Na systemie Android można łatwo włączać i&nbsp;wyłączać niektóre funkcje przez główne menu. W&nbsp;tym celu przykładamy palec do górnej części ekranu i&nbsp;kilka razy ciągniemy w&nbsp;dół.

Wszystkie powyższe rzeczy nie ocalą nas przed akcelerometrem. Nie wymaga on żadnych pozwoleń i&nbsp;nie ma pstryczka, który by go wyłączył. Ale pamiętajmy, że w&nbsp;odosobnieniu nie jest aż taki groźny. Dbajmy o&nbsp;inne sprawy wskazane powyżej, a&nbsp;powinno być w&nbsp;porządku. 

Jeśli mamy czas, kiedy akurat nie potrzebujemy smartfona (bo na przykład śpimy albo mamy długi przejazd pociągiem)... To możemy po prostu wyłączać całe urządzenie.  
Nawet jeśli siedzi u&nbsp;nas wścibska apka gapiąca się w&nbsp;akcelerometr, to z&nbsp;wyłączonego smartfona nic nie odczyta.

A jeśli chcemy prywatności przed operatorem telekomunikacyjnym, to pomóc nam może **tryb samolotowy** -- jeśli działa prawidłowo, to na czas jego aktywacji wyłączają nam się wszelkie formy łączności bezprzewodowej.

To moim zdaniem wszystko, co potrzebne zwykłemu człowiekowi przeciw śledzeniu korporacyjnemu. Jakieś ruchy oporu we wrogich reżimach mogłyby zamiast tego postawić na telefony jednorazowe (*burner phone'y*) oraz torebki Faradaya, blokujące wszelkie wychodzące sygnały. Ale ta seria nie skupia się na takich tematach.

I z&nbsp;tym zestawem porad Was zostawiam. Życzę, żebyście przez te wakacje poznali jakieś fajne miejsca. I&nbsp;oby nie poznały ich szpiegujące aplikacje :smile:
