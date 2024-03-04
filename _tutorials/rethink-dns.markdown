---
layout: page
title: RethinkDNS – jak zabrać internet niedobrym aplikacjom
description: "Przełącznik, którego nie da czysty Android."
---

Android to obecnie [najpopularniejszy](https://www.statista.com/statistics/272698/global-market-share-held-by-mobile-operating-systems-since-2009/) system operacyjny na smartfonach. Ale pod względem ochrony prywatności daleko mu do *naj*.  
Choć na przestrzeni lat załatano parę luk, aplikacje nadal mogą dość łatwo dobrać się do danych i&nbsp;wysłać je komuś przez internet.

Za jedną z największych luk uważam **brak precyzyjnej kontroli nad dostępem aplikacji do internetu**.

System pozwala co najwyżej wyłączać wybranym aplikacjom funkcję przesyłania danych „po cichu”, kiedy z&nbsp;nich nie korzystamy. Jest też przełącznik ogólny, odcinający internet *wszystkim* aplikacjom.

Nie istnieje natomiast coś, co łączyłoby w&nbsp;sobie *precyzję* (możliwość wskazania konkretnych aplikacji) i&nbsp;*skuteczność* (kompletne, bezwarunkowe odcięcie im internetu). To moim zdaniem wielka wada Androida.

...A przynajmniej nie istnieje w&nbsp;domyślnych opcjach. Powstały jednak *firewalle* -- aplikacje, które ustawiają się jako „kontrolerzy” całego ruchu internetowego. I&nbsp;dzielą się tą kontrolą z&nbsp;użytkownikami. Dając dokładnie takie przełączniki, o&nbsp;jakich marzyłem.

W tym samouczku pokażę jedną taką aplikację, **RethinkDNS**. Darmową, o&nbsp;otwartym kodzie źródłowym, łatwą w obsłudze. I&nbsp;skuteczną.

{:.post-meta}
Na chwilę obecną omawiam tylko dwie funkcje aplikacji, DNS-a oraz *firewalla*. W&nbsp;miarę poznawania pozostałych będę rozbudowywał wpis.

## Spis treści

* [Weryfikacja i&nbsp;instalacja](#weryfikacja-iinstalacja)
  * [Instalacja](#instalacja)
  * [RethinkDNS – VPN tylko z&nbsp;nazwy](#rethinkdns--vpn-tylko-znazwy)
* [Obsługa aplikacji](#obsługa-aplikacji)
  * [DNS](#dns)
  * [Firewall](#firewall)
  * [Logi](#logi)
  * [Eksport logów i&nbsp;ustawień](#eksport-logów-iustawień)

## Weryfikacja i&nbsp;instalacja

Świat *open source* bywa dynamiczny. Zdarza się czasem, że jakiś projekt zmieni właściciela albo zostanie sprzedany. W&nbsp;dniu tworzenia wpisu ufam RDNS-owi, ale czy to się kiedyś nie zmieni?

Dlatego przed instalacją warto sobie zweryfikować, czy z&nbsp;aplikacją wszystko w&nbsp;porządku. Na początek można odwiedzić [jej stronę główną](https://rethinkdns.com/app).

Jest tam informacja o&nbsp;tym, że apka jest/była częścią inicjatywy Mozilla Builders (od firmy Mozilla, twórców Firefoksa). Na stronie samej incjatywy [znajdziemy potwierdzenie](https://builders.mozilla.community/old/alumni.html#rethinkdns).  
To pierwszy plus, bo Mozilla akurat weryfikują aplikacje.

{% include info.html
type="Ciekawostka"
text="Dawniej projekt działał pod nazwą BraveDNS, a&nbsp;strona główna była pod adresem *bravedns.com*.  
Nie mają jednak nic wspólnego z&nbsp;przeglądarką Brave i&nbsp;zmienili nazwę na RethinkDNS zapewne ze względu na [częste mylenie tych dwóch projektów](https://github.com/celzero/rethink-app/issues/69)."
%}

Jest też link do [kodu źródłowego](https://github.com/celzero/rethink-app). Ponad 2100&nbsp;gwiazdek od użytkowników, czyli całkiem sporo. Sam opis również wyjaśnia, co leży twórcom apki na sercu i&nbsp;na jakich stronach są aktywni. Ogólnie budzą zaufanie.

Podsumowując: na dzień dzisiejszy polecam Rethink DNS. Ale czas płynie, świat się zmienia. Dlatego dla pewności warto poszukać informacji na zewnętrznych stronach:

* wpisać w&nbsp;ogólną wyszukiwarkę `rethink dns site:reddit.com` i&nbsp;zobaczyć, co tam na forum Reddit;
* poszukać [najnowszych wątków](https://hn.algolia.com/?dateRange=all&page=0&prefix=false&query=rethinkdns&sort=byDate&type=story) na forum Hacker News.

Potem można sobie poczytać, czy są jakieś aktualne, większe skandale. Pojedynczymi komentarzami krytycznymi nie warto się przejmować -- światek prywatnościowy jest dość wymagający :wink:

### Instalacja

Zachęcam do RethinkDNS-a zainstalować w&nbsp;następujący sposób:

1. Pobrać aplikację F-Droid.

   To alternatywne źródło aplikacji. Dopuszczają tylko te o&nbsp;otwartym kodzie źródłowym.  
   Poza tym są wymagający, więc gdyby RDNS zmienił się na niekorzyść, to jest szansa że nie przyjmą niekorzystnej aktualizacji i&nbsp;zostaną przy starej, dobrej wersji.

2. Wpisać `rethink` w&nbsp;wyszukiwarkę F-Droida i&nbsp;zainstalować RDNS przez niego.

### RethinkDNS – VPN tylko z&nbsp;nazwy

Od strony formalnej RethinkDNS jest ustawiony na systemie jako **aplikacja typu VPN**.  
To dlatego, że takie apki dostają od Androida kontrolę nad przepływem danych do internetu. Są jak szeroki lejek zbierający wszystko, co próbują wysłać w&nbsp;świat inne aplikacje.

Wiele osób może kojarzyć VPN-y z&nbsp;ukrywaniem tożsamości, choćby w&nbsp;celu ominięcia blokad geograficznych.

Po włączeniu typowych VPN-ów cała komunikacja idzie przez pośrednika (cudzy serwer). Ten pośrednik nie ujawnia naszego adresu IP. A&nbsp;to m.in. po adresie ustala się kraj pochodzenia.

Ale warto pamiętać, że RethinkDNS to VPN jedynie na papierze. **Samo jego włączenie nie ukryje prawdziwego adresu IP przed adresatami**.

{:.post-meta .bigspace-after}
Chcąc mieć taki bajer, musielibyśmy sami o&nbsp;niego zadbać, zmieniając ustawienia pod kategorią `Proxy` (której jeszcze nie zbadałem).

{% include info.html
type="Uwaga"
text="Spotkałem się z uwagami, że *król*{:.corr-del} VPN może być tylko jeden.  
W związku z&nbsp;tym włączony RDNS nie pozwalałby korzystać równocześnie z&nbsp;innych VPN-ów (tych typowych, od maskowania adresu IP)."
%}

W każdym razie, jeśli ktoś nie potrzebuje VPN-ów ani ich funkcji, to prawdziwa natura RDNS-a nie ma żadnego znaczenia. Po zainstalowaniu tej apki w&nbsp;górnej części ekranu pokaże się ikonka kluczyka. To znaczy że działa. I&nbsp;ten fakt wystarczy.

## Obsługa aplikacji

**Uwaga**: zachęcam do przeczytania części „DNS” nawet osoby, które nie planują ustawiać nic własnego. Warto bowiem pomyśleć o&nbsp;zmianie jednego ustawienia.

### DNS

Czym jest DNS? W&nbsp;uproszczeniu: to książka telefoniczna internetu. W&nbsp;praktyce jakiś serwer.

Po pierwsze: system musi znać adres jakiegoś DNS-a, żeby się z&nbsp;nim połączyć. Zwykle jest on proponowany przez hotspota albo operatora (w&nbsp;przypadku sieci mobilnej). Można też ustawić coś własnego.

Kiedy aplikacja (np. przeglądarka) chce zdobyć coś ze strony internetowej, a&nbsp;zna jedynie jej czytelną nazwę (jak *ciemnastrona.com.pl*), to zwraca się do DNS-a. Ten odsyła aktualny adres IP odpowiadający tej nazwie. A&nbsp;reszta interakcji zachodzi już bezpośrednio ze stroną spod tego adresu.

<img src="/assets/posts/dns/internet-plus-dns-schemat.jpg" alt="Schemat pokazujący wymianę informacji między laptopem a&nbsp;serwerami: DNS-em oraz adresatem docelowym"/>

{:.figcaption}
DNS udziela odpowiedzi tylko na pierwszym etapie. System zapisuje sobie adres i&nbsp;przez pewien czas już go nie pyta.

Apka RethinkDNS domyślnie kieruje wszystkie pytania o&nbsp;strony do serwera DNS kontrolowanego przez jej autorów. Ponoć szyfrującego informacje. To na plus.  
Niektórzy mogą jednak mimo wszystko **zmienić to ustawienie i&nbsp;pozostać przy tym, co zapewnia system**.

Po pierwsze: ze względu na (ograniczone) zaufanie.

Do DNS-a podsuniętego przez apkę będą trafiały ogólne nazwy domen, jakie odwiedzamy (bez konkretnych podstron). Jak: *youtube.com*, *ciemnastrona.com.pl*, *niegrzeczne-obrazki.gov.pl*.

Zazwyczaj takie informacje trafiają do właściciela hotspota, którego używamy, albo do firmy telekomunikacyjnej. Używając rozwiązania od twórców RDNS-a, przenosimy to zaufanie na nich. Może nie ma w&nbsp;tym nic złego, ale lepiej mieć świadomośc. 

Po drugie: ze względu na stabilność.

Serwerowi DNS zapewnianemu przez twórców RDNS-a może się coś przytrafić. I&nbsp;[czasem się przytrafia](https://www.reddit.com/r/rethinkdns/comments/xjfnyi/is_rethink_dns_down/). A&nbsp;że apka pośredniczy we wszystkim, to do czasu naprawienia usterki telefon *de facto* straci łączność z&nbsp;internetem.

Z powyższego względu -- zwłaszcza jeśli ustawiamy firewalla osobie mniej lubiącej się z elektroniką -- warto wrócić do domyślnego, systemowego DNS-a, podsuwanego przez hotspota/operatora. Minimalizuje to szansę niemiłych zaskoczeń.

Zmiana DNS-a jest bardzo łatwa. Wystarczy kliknąć na ekranie głównym RDNS-a kafelek `DNS` u&nbsp;góry i&nbsp;wybrać z&nbsp;krótkiej listy opcję `System DNS`.

{:.post-meta .bigspace-after}
Jeśli ktoś chce, może też wybrać `Inne DNS` i&nbsp;wpisać adres dowolnego DNS-a, żeby to z&nbsp;niego korzystać. Byle nie 8.8.8.8 ani 8.8.4.4, [bo to Google](https://en.wikipedia.org/wiki/Google_Public_DNS) :wink:

### Firewall

To ta funkcja pozwala odciąć od sieci aplikacje, którym nie ufamy.

Po otwarciu RDNS-a pokaże się ekran zawierający kilka głównych kategorii. Trzeba kliknąć tę na dole, `Aplikacje`.

Pokaże się lista wszystkich aplikacji na smartfonie. Żeby odciąć wybranym dostęp do sieci, trzeba klikać odpowiadające im ikonki po prawej, aż się przekreślą. Jedna odpowiada za hotspoty, druga za sieć komórkową.

Na liście są również aplikacje systemowe, które łatwo poznać po ikonie wyglądającej jak głowa robota (Androida). Proponuję zachować ostrożność i&nbsp;nie wyłączać im sieci na chybił-trafił.

A kogo odciąć? Przede wszystkim aplikacje, które raczej nie mają interesu w&nbsp;łączności z&nbsp;siecią. Takie jak Zegar.

Osobiście zablokowałem przez RDNS-a również aplikacje Google'a, których nie dało się odinstalować, a&nbsp;jedynie wyłączyć.  
Bloka dałem nawet [Usługom Google Play](/2024/02/03/smartfon-degoogle#finałowy-boss--usługi-google-play){:.internal}, wcześniej wyłączonym. Wiem że będę tu w&nbsp;mniejszości, bo wiele aplikacji jednak na nich polega.

{:.bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle-apki/rethink-dns-blokowanie.jpg" alt="Schemat pokazujący ustawienia RethinkDNS. Pośrodku widać okno z&nbsp;ustawieniami dla dwóch aplikacji. Apka Files By Google ma wyłączoną łączność, a&nbsp;strzałka wychodząca od jej ikony odbija się od okna z&nbsp;ustawieniami. Strzałka wychodząca od aplikacji Firefox, która ma włączone przełączniki, normalnie dociera do ikony kuli ziemskiej po drugiej stronie okna." />

{:.figcaption}
Źródła: oficjalne ikony, [kula ziemska](https://www.flaticon.com/free-icon/navigation_2763373) autorstwa *vectorsmarket15* (serwis Flaticon).

Firewall pozwala również ustawiać bardziej złożone regułki niż zwykłe tak/nie. Ale o&nbsp;tym może napiszę innym razem, kiedy już poeksperymentuję.

### Logi

Kolejną cenną rzeczą, jaką oferuje Rethink DNS, jest możliwość zerknięcia do logów (historii połączeń z&nbsp;siecią) i&nbsp;ujrzenia na własne oczy, z&nbsp;czym łączyły się aplikacje.

Żeby w&nbsp;tę historię zajrzeć, trzeba kliknąć zakładkę `Logi` na ekranie głównym. U&nbsp;góry będą dwie zakładki:

* `Logi sieciowe`
* `DNS`

Zakładka `Logi sieciowe` to ułożona chronologicznie lista, pokazująca wymianę informacji między aplikacjami a&nbsp;zewnętrznymi serwisami. Przykładowa pozycja z&nbsp;listy wygląda tak:

{:.figure .bigspace}
<img src="/assets/tutorials/rethink-dns/rdns-logi-sieciowe-przyklad.jpg" alt="Pojedyncza pozycja z&nbsp;listy pokazująca ikonkę przeglądarki Firefox, stronę news.ycmbinator.com, jej adres IP oraz godzinę połączenia i&nbsp;parę pomniejszych informacji"/>

Widać tu:

* nazwę oraz ikonę aplikacji,
* adres IP i&nbsp;nazwę serwisu (domenę), z&nbsp;jakim się połączyła,
* ilość przesłanych danych (strzałka w&nbsp;górę -- wysłane, w&nbsp;dół -- pobrane),
* protokół, jakim się połączyła (tu: szyfrowany HTTPS),
* czas wykonania połączenia,
* kraj, w&nbsp;jakim znajduje się serwis (na podstawie adresu IP).

Druga górna zakładka, `DNS`, to z&nbsp;kolei podobnie wyglądająca lista zapytań do [DNS-a](#dns){:.internal}. Są to przeważnie nazwy domen, wysyłane z&nbsp;nadzieją na otrzymanie odpowiadających im adresów IP.  
Zapytania z&nbsp;tej listy nie są już przypisane do konkretnych aplikacji, co może nieco utrudniać ustalanie winnych.

{% include info.html
type="Ciekawostka"
text="Przy niektórych pozycjach widnieje czas połączenia 0&nbsp;ms -- oznacza to zapewne, że żądanie w&nbsp;ogóle nie poleciało w&nbsp;sieć, bo adres został wzięty z&nbsp;**pamięci podręcznej**.  
Powiązania domena-adres są na pewien czas zapisywane na urządzeniu, żeby system *był dużym chłopcem i*{:.corr-del} przestał ciągle słać pytania do DNS-a."
%}

W jaki sposób można korzystać z&nbsp;logów? Proponuję co pewien czas sprawdzać obie listy. Jeśli któryś element wyda się podejrzany, to można poszukać w&nbsp;internecie nazwy domeny, ewentualnie dopisując słowa `is malicious`, `privacy` i&nbsp;tak dalej, żeby nadać kontekstu.

Jeśli obawy się potwierdzą -- albo nie zostaną rozwiane -- to można kliknąć na dany element z&nbsp;listy, po czym paroma kliknięciami zablokować łączność z&nbsp;wybraną domeną. Mając na uwadze, że czasem może to prowadzić do błędów aplikacji.

Przykład: dzięki logom odkryłem, że moja aplikacja Termux zapytała o&nbsp;coś DNS-a pod adresem 8.8.8.8, czyli należącego do Google'a, zamiast mojego domyślnego. Niedobrze.

Miałem podejrzenie, że nastąpiło to po uźyciu [programiku *dig*]({% post_url 2023-12-26-dns-rekordy %}#dig-izaglądanie-do-rekordów-dns-a){:.internal}, więc poszukałem pod hasłem `dig termux google dns`.  
Jak się okazało, to problem Androida. Niektóre apki biorą adres DNS-a z&nbsp;pewnego pliku systemowego. A&nbsp;w nim domyślnie znajdują się [adresy DNS-a od Google'a](https://www.reddit.com/r/termux/comments/gk838u/android_ignoring_dns_via_dhcp_termux_and_others/). Podejrzana sprawa.

Logi pozwoliłyby również wykryć, że jakaś strona otwarła się w&nbsp;[przeglądarce wbudowanej]({% post_url 2023-08-08-wbudowane-przegladarki %}){:.internal} w&nbsp;Facebooka, zamiast w&nbsp;(oczekiwanej) systemowej. Moją uwagę zwróciłby fakt, że aplikacja Facebooka połączyła się ze stroną, która nijak nie jest z&nbsp;Metą/Facebookiem związana.

### Eksport logów i&nbsp;ustawień

Przeglądarka logów od RDNS-a ma swoje ograniczenia. Pozwala szukać po nazwie aplikacji albo odfiltrowywać aplikacje (nie-)blokowane... Ale to w&nbsp;sumie tyle.

Nie da się na przykład wyświetlić tylko połączeń wykonanych w&nbsp;określonym przedziale czasowym. Nie mówiąc o&nbsp;jakiejś wizualizacji liczby połączeń w&nbsp;skali, dajmy na to, kilku tygodni.

Żeby przeprowadzić dokładniejszą analizę, trzeba wyciągnąć plik z&nbsp;wnętrza RDNS-a i&nbsp;trochę przy nim popracować innymi programami. Mam w&nbsp;planie zrobić coś takiego na blogu, ale póki co pokażę jedynie, jak wyeksportować dane.

{:.post-meta .bigspace-after}
Ta część może się przydać również osobom, które pozmieniały dużo ustawień i&nbsp;chciałyby je przenieść do innej apki. Zostaną wyeksportowane razem z&nbsp;logami.

Wystarczy kliknąć ikonkę `Skonfiguruj` na samym dole, potem wybrać opcję `Kopia zapasowa i przywracanie`, przeklikać się przez okienka i&nbsp;wybrać folder, do jakiego zostaną zapisane dane z&nbsp;aplikacji.

{:.bigspace-before}
<img src="/assets/tutorials/rethink-dns/rdns-kopia-zapasowa.jpg" alt="Trzy fragmenty zrzutów ekranu pokazujące po kolei, jak wyeksportować dane z&nbsp;apki Rethink DNS" width="60%"/>

{% include info.html
type="Uwaga"
text="Jeden z&nbsp;komunikatów mówi, że eksport danych wymaga ponownego uruchomienia VPN-a (czyli zapewne również firewalla).  
Jeśli ktoś się obawia, że to okno czasowe wykorzystają któreś z&nbsp;blokowanych aplikacji i&nbsp;dorwą się do sieci, to dla pewności można **wyłączyć internet na poziomie całego smartfona**. I&nbsp;przywrócić po wyeksportowaniu.  
Osoby szczególnie wyczulone mogą również upewnić się, że żadne nielubiane aplikacje nie mają pozwolenia na dostęp do plików. Cenne logi trafią bowiem do publicznej części smartfona, gdzie każdy może zajrzeć."
%}

Dane zostaną zapisane w&nbsp;wybranym folderze, do pliku z&nbsp;rozszerzeniem `.rbk`. Od strony technicznej to zwykłe archiwum, które można rozpakować (w&nbsp;Eksploratorze Windowsa: po ręcznej zmianie rozszerzenia na `.zip`).  
W środku jest kilka plików, w&nbsp;tym dwie bazy danych typu *SQLite*. Logi znajdują się wewnątrz tej o&nbsp;nazwie `rethink_logs.db`.

Jeśli już umiecie dłubać w&nbsp;takim formacie, to super! Jeśli nie, to możecie poczytać [praktyczny opis takiej eksploracji](https://chrisnicoll.net/2020/02/exploring-an-sqlite-database-from-jupyter-notebook/). Albo poczekać na mój wpis :wink: 

