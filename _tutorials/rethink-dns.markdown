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

## Weryfikacja i&nbsp;instalacja

Świat *open source* bywa dynamiczny. Zdarza się czasem, że jakiś projekt zmieni właściciela albo zostanie sprzedany. W&nbsp;dniu tworzenia wpisu ufam RDNS-owi, ale czy to się kiedyś nie zmieni?

Dlatego przed instalacją warto sobie zweryfikować, czy z&nbsp;aplikacją wszystko w&nbsp;porządku. Na początek można odwiedzić [jej stronę główną](https://rethinkdns.com/app).

Jest tam informacja o&nbsp;tym, że apka jest/była częścią inicjatywy Mozilla Builders (od firmy Mozilla, twórców Firefoksa). Na stronie samej incjatywy [znajdziemy potwierdzenie](https://builders.mozilla.community/old/alumni.html#rethinkdns).  
To pierwszy plus, bo Mozilla akurat weryfikują aplikacje.

{% include info.html
type="Ciekawostka"
text="Dawniej projekt działał pod nazwą BraveDNS, a&nbsp;strona główna była pod adresem *beavedns.com*.  
Nie mają jednak nic wspólnego z&nbsp;przeglądarką Brave i&nbsp;zmienili nazwę na RethinkDNS ze względu na [częste ich mylenie](https://github.com/celzero/rethink-app/issues/69)."
%}

Jest też link do [kodu źródłowego](https://github.com/celzero/rethink-app). Ponad 2100&nbsp;gwiazdek od użytkowników, czyli całkiem sporo. Sam opis również wyjaśnia, co leży twórcom apki na sercu i&nbsp;na jakich stronach są aktywni. Ogólnie budzą zaufanie.

Podsumowując: na dzień dzisiejszy mam powody, żeby polecić RDNS. Ale czas płynie, świat się zmienia. Dlatego dla pewności warto poszukać informacji na zewnętrznych stronach:

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

**Uwaga**: zachęcam do przeczytania części „DNS” nawet wtedy, jeśli nie planujemy nic ręcznie ustawiać. Warto bowiem pomyśleć o&nbsp;zmianie jednego ustawienia.

### DNS

Czym jest DNS? W&nbsp;uproszczeniu: to książka telefoniczna internetu. W&nbsp;praktyce jakiś serwer.

Kiedy aplikacja (np. przeglądarka) chce zdobyć coś ze strony internetowej, a&nbsp;zna jedynie jej czytelną nazwę (jak *ciemnastrona.com.pl*), to zwraca się do jakiegoś DNS-a. Ten odsyła aktualny adres IP odpowiadający tej nazwie. A&nbsp;reszta interakcji zachodzi już bezpośrednio ze stroną spod tego adresu.

<img src="/assets/posts/dns/internet-plus-dns-schemat.jpg" alt="Schemat pokazujący wymianę informacji między laptopem a&nbsp;serwerami: DNS-em oraz adresatem docelowym"/>

{:.figcaption}
DNS udziela odpowiedzi tylko na pierwszym etapie, a&nbsp;po podaniu adresu nie jest już pytany.

Apka RethinkDNS domyślnie kieruje wszystkie pytania o&nbsp;strony do serwera DNS kontrolowanego przez jej autorów. Ponoć szyfrującego informacje, co jest atutem.  
Niektórzy mogą jednak chcieć **zmienić to ustawienie i&nbsp;pozostać przy tym, co zapewnia system**.

Po pierwsze: ze względu na kwestie zaufania.

Przy takim układzie do twórców będą trafiały ogólne nazwy domen, jakie odwiedzamy (bez konkretnych podstron). Jak: *youtube.com*, *ciemnastrona.com.pl*, *niegrzeczne-obrazki.gov.pl*.

Zazwyczaj takie informacje trafiają do właściciela hotspota, którego używamy, albo do firmy telekomunikacyjnej. Używając rozwiązania od twórców RDNS-a, przenosimy to zaufanie na nich. Może nie ma w&nbsp;tym nic złego, ale lepiej mieć świadomośc. 

Po drugie: ze względu na kwestie awarii.

Serwerowi DNS zapewnianemu przez twórców RDNS-a może się coś przytrafić. I&nbsp;czasem się przytrafia. A&nbsp;że apka pośredniczy we wszystkim, to do czasu naprawienia usterki telefon straci łączność z&nbsp;wieloma stronami.

Z powyższego względu -- zwłaszcza jeśli ustawiamy telefon osobie mniej lubiącej się z elektroniką -- warto wrócić do domyślnego, systemowego DNS-a, podsuwanego przez hotspota/operatora. Minimalizuje to szansę niemiłych zaskoczeń.

Zmiana DNS-a jest bardzo łatwa. Wystarczy kliknąć na ekranie głównym RDNS-a kafelek `DNS` u&nbsp;góry i&nbsp;wybrać z&nbsp;krótkiej listy opcję `System DNS`.

{:.post-meta .bigspace-after}
Jeśli ktoś chce, może też wybrać `Inne DNS` i&nbsp;wpisać adres dowolnego DNS-a, żeby to z&nbsp;niego korzystać. Byle nie 8.8.8.8 ani 8.8.4.4, [bo to Google](https://en.wikipedia.org/wiki/Google_Public_DNS) :wink:

### Firewall

To ta funkcja pozwala odciąć od sieci aplikacje, którym nie ufamy.

Po otwarciu RDNS-a pokaże się ekran zawierający kilka głównych kategorii. Trzeba kliknąć tę na dole, `Aplikacje`.

Pokaże się lista wszystkich aplikacji na smartfonie. Żeby odciąć wybranym dostęp do sieci, trzeba klikać odpowiadające im ikonki po prawej, aż się przekreślą. Jedna odpowiada za łączność przez hotspoty, inna przez sieć komórkową.

Na liście są również aplikacje systemowe, które łatwo poznać po ikonie wyglądającej jak głowa robota (Androida). Proponuję zachować ostrożność i&nbsp;nie wyłączać im sieci na chybił-trafił.

A kogo odciąć? Przede wszystkim aplikacje, które raczej nie mają interesu w&nbsp;łączności z&nbsp;siecią. Takie jak Zegar.

Osobiście zablokowałem przez RDNS-a również aplikacje Google'a, których nie dało się odinstalować, a&nbsp;jedynie wyłączyć.  
Bloka dałem nawet [Usługom Google Play](/2024/02/03/smartfon-degoogle#finałowy-boss--usługi-google-play){:.internal}, wcześniej wyłączonym. Wiem że będę tu w&nbsp;mniejszości, bo wiele aplikacji jednak na nich polega.

{:.bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle-apki/rethink-dns-blokowanie.jpg" alt="Schemat pokazujący ustawienia RethinkDNS. Pośrodku widać okno z&nbsp;ustawieniami dla dwóch aplikacji. Apka Files By Google ma wyłączoną łączność, a&nbsp;strzałka wychodząca od jej ikony odbija się od okna z&nbsp;ustawieniami. Strzałka wychodząca od aplikacji Firefox, która ma włączone przełączniki, normalnie dociera do ikony kuli ziemskiej po drugiej stronie okna." />

{:.figcaption}
Źródła: oficjalne ikony, [kula ziemska](https://www.flaticon.com/free-icon/navigation_2763373) autorstwa *vectorsmarket15* (serwis Flaticon).

Firewall pozwala również ustawiać bardziej złożone regułki niż zwykłe tak/nie. Ale o&nbsp;tym może napiszę innym razem, kiedy już poeksperymentuję.

