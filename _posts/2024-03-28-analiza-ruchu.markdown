---
layout: post
title: "Internetowa inwigilacja plus 7 – analiza ruchu sieciowego"
subtitle: "Nawet szyfry nie pomogą, gdy pakietów mnogo."
description: "Nawet szyfry nie pomogą, gdy pakietów mnogo."
date:   2024-03-28 10:00:00 +0100
tags: [Internet, Inwigilacja, Tor]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image:
  path: /assets/posts/inwigilacja/ruch-sieciowy/analiza-ruchu-baner.jpg
  width: 1200
  height: 700
  alt: "Mechaniczne oko spogląda na taśmociąg, którym jadą metalowe pudła różnych rozmiarów, z różowymi sercami na ściankach"
---

Zacznę od anegdotki związanej z&nbsp;zabawą weselną, w&nbsp;jakiej brałem kiedyś udział.

Staliśmy w&nbsp;męskim kółku i&nbsp;podawaliśmy sobie z&nbsp;rąk do rąk pudełka -- do momentu, aż muzyka przestanie grać. W&nbsp;jednym z&nbsp;nich była muszka pana młodego. Reszta była pusta. Kto zostanie z&nbsp;muszką, ten ponoć się hajtnie jako następny.

Teoretycznie każdy miał równe szanse. Ale paru spryciarzy szybko odkryło, w&nbsp;którym pudełku jest muszka. Wystarczyło mocniej potrząsnąć i&nbsp;dało się usłyszeć, jak obija się o&nbsp;wnętrze pudła. Losowość prysła.

Podobnie jest z&nbsp;danymi wysyłanymi przez internet. Jak pobierane przez kogoś filmy, odwiedzane strony... Nawet jeśli z&nbsp;zewnątrz są zaszyfrowane -- jak zamknięte pudełka -- można na parę sposobów odgadnąć, czym są. Analizując ilość pakietów, pochodzenie, rozmiar, czas wysłania.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/ruch-sieciowy/analiza-ruchu-baner.jpg" alt="Mechaniczne oko spogląda na taśmociąg, którym jadą metalowe pudła w&nbsp;różnych rozmiarach z&nbsp;różowymi sercami na ściankach"/>

{:.figcaption}
Źródło: Bing Create. Zdołałem stworzyć kilkanaście obrazków, nim dostałem losowego bana.

To obszerne zagadnienie, które można nazwać ogólnie **analizą ruchu sieciowego** (ang. *traffic analysis*). Pokażę tu pobieżnie jej potęgę, a&nbsp;także sposoby, w&nbsp;jakie można się przed nią chronić.

Zapraszam, będzie przystępnie!

{% include info.html
type="Uwaga"
text="Ten wpis skupia się na przypadku, gdy przeciwnik jest bierny i&nbsp;jedynie analizuje przelatujące dane.  
Ale jeśli oprócz tego wykaże własną inicjatywę i&nbsp;odwiedzi te same miejsca co my, to może wykonać profilowanie stron (ang. *website fingerprinting*). Tej kwestii poświęcę kolejny wpis."
%}

## Spis treści

* [Profil przeciwnika](#profil-przeciwnika)
* [Co można podejrzeć](#co-można-podejrzeć)
  * [Programy do samopodglądania](#programy-do-samopodglądania)
  * [System, przeglądarka, aplikacje](#system-przeglądarka-aplikacje)
  * [Rozpoznawanie interakcji](#rozpoznawanie-interakcji)
  * [Styl pisania](#styl-pisania)
  * [Ustalenie zwyczajów](#ustalenie-zwyczajów)
  * [Powiązania między osobami](#powiązania-między-osobami)
* [Jak się chronić](#jak-się-chronić)
  * [Niewierność wobec podglądacza](#niewierność-wobec-podglądacza)
  * [Szyfrowany DNS i&nbsp;ECH](#szyfrowany-dns-iech)
  * [VPN](#vpn)
  * [Sieć Tor](#sieć-tor)
* [Pułapka korelacji czasowej](#pułapka-korelacji-czasowej)

## Profil przeciwnika

Od pewnego czasu wyróżniam w&nbsp;serii „Internetowa inwigilacja” różne rodzaje przeciwników, żeby lepiej porządkować informacje.

Pierwszy z&nbsp;nich to firmy reklamowe, których produkty goszczą na współpracujących z&nbsp;nimi stronach internetowych. Widzą niemal to samo co one, ale ich wzrok nie sięga zwykle na strony obce (nie każda firma reklamowa to Google).

W przypadku analizy ruchu **przeciwnik należy do drugiej kategorii -- właścicieli infrastruktury**.

To odpowiednicy listonoszy i&nbsp;firm kurierskich w&nbsp;fizycznym świecie. Zwykle nie mogą „czytać zaplombowanych listów” (dzięki powszechnemu szyfrowaniu). Widzą natomiast ogólniejsze *metadane*, nazwy odbiorców.  
Ich inwigilacja jest płytsza, ale szersza. Bo widzą nazwy *wszystkich* serwisów, z&nbsp;jakimi użytkownik wchodzi w&nbsp;interakcje.

To dość zróżnicowana kategoria przeciwników, do której może należeć:

* firma telekomunikacyjna (Play, Orange...),
* właściciel publicznego hotspota (jak sieć uczelniana),
* złośliwy współlokator (albo współlokatorka!) z&nbsp;dostępem do wspólnego routera,
* właściciel VPN-a, jeśli z&nbsp;jakiegoś korzystamy.

Możliwości jest wiele. Odpuszczam rzeczy bardziej abstrakcyjne, jak szpiega przyssanego [prosto do światłowodu](https://www.reuters.com/article/2014/02/24/us-eu-brazil-idUSBREA1N0PL20140224/), którym lecą dane. Tradycyjnie trzymam się spraw goblińskich, a&nbsp;nie smoczych :wink: 

Motywacje przeciwników mogą być najróżniejsze. Więksi operatorzy mogą przykładowo współpracować z&nbsp;firmami zewnętrznymi i&nbsp;[sprzedawać im dane użytkowników](https://www.vice.com/en/article/jg84yy/data-brokers-netflow-data-team-cymru) na większą skalę, jak to ma miejsce w&nbsp;USA.

Inny, bardziej stalkerski wariant? Być może jakiemuś właścicielowi knajpy wpadła w&nbsp;oko klientka, która siadła z&nbsp;laptopem w&nbsp;rogu.  
Jest niemała szansa, że podłączyła się do hotspota. Więc właściciel jakiś czas po jej wyjściu bierze router i&nbsp;zerka w&nbsp;historię, licząc na poznanie jakichś informacji. 

## Co można podejrzeć

W najgorszym przypadku, gdy odwiedza się strony rozpoczynające się od `http://` (bez `s` na końcu), podglądacz widzi *wszystkie* informacje wymieniane z&nbsp;inną stroną. Zarówno swoistą „wizytówkę użytkownika” ([nagłówki HTTP]({% post_url 2021-01-11-internetowa-inwigilacja-1-podstawy %}){:.internal}), jak i&nbsp;pełną treść wiadomości, wysyłane hasła i&nbsp;tak dalej.

{% include info.html
type="Ciekawostka"
text="Co więcej, podglądacz może również *modyfikować* takie nieszyfrowane informacje. W&nbsp;2014 roku jeden z&nbsp;największych operatorów telekomunikacyjnych w&nbsp;USA, Verizon, dodawał do nich [identyfikator](https://www.eff.org/deeplinks/2014/11/verizon-x-uidh) pozwalający reklamodawcom rozpoznawać ludzi."
%}
 
Ale to przykład dość skrajny. Obecnie większość stron z&nbsp;automatu szyfruje komunikację, zwłaszcza te większe. Jeśli adres strony zaczyna się od `https://`, to dane są zaszyfrowane, niemożliwe do odczytania i&nbsp;zmodyfikowania przez zewnętrzne podmioty. Również w&nbsp;tym wpisie **zakładam, że cała treść jest szyfrowana**.

Co pozostaje na widoku? *Metadane*. Adres IP i&nbsp;czytelna nazwa domeny, jak `www.ciemnastrona.com.pl`.

Podrzucę tutaj adres dawnego wpisu, w&nbsp;którym trochę pisałem o&nbsp;metadanych (ale głównie o&nbsp;samych nazwach domen). Na czerwono oznaczyłem to, czego *nie widzą* podglądacze. Widzą natomiast to, co na biało.

<div class="black-bg mono bigspace-before">
https://www.ciemnastrona.com.pl<span class="red">/internetowa_inwigilacja/2022/08/13/https</span>
</div>

Oprócz tego podglądacze widzą:

* „kierunek” danych (pobrane czy wysłane),
* ich rozmiar,
* czas ich wysłania.

### Programy do samopodglądania

Istnieje kilka sposobów na to, żeby podejrzeć własny ruch sieciowy i&nbsp;lepiej sobie uzmysłowić, co mogą widzieć podglądacze.

Pierwszy z&nbsp;nich to **narzędzia przeglądarki**. Ograniczone tylko do niej, ale bardzo intuicyjne.  
Są wbudowane w&nbsp;chyba wszystkie popularne przeglądarki. Wystarczy nacisnąć kombinację `Ctrl+Shift+I`, żeby je wyświetlić. Potem trzeba kliknąć zakładkę `Sieć` w&nbsp;ich górnej części i&nbsp;w razie potrzeby odświeżyć stronę. Wyświetli się lista pobranych elementów oraz garść informacji o&nbsp;nich.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/ruch-sieciowy/ruch-internetowy-pobrane.jpg" alt="Widok na listę pobranych plików w&nbsp;Narzędziach Przeglądarki. Ich nazwy i&nbsp;rodzaje są zakryte czarnymi prostokątami"/>

To przybliżenie tego, co widzą podglądacze -- rozmiar plików, rodzaj interakcji (pobranie/wysłanie; tu tylko pobrania) oraz domeny, z&nbsp;jakimi się kontaktujemy. Czerwoną ramką wyróżniłem domenę `github.githubassets.com`, z&nbsp;której pobrana została emota. Ma inne źródło niż reszta treści.

Podglądacze nie widzieliby natomiast, że przeglądarka coś wzięła z&nbsp;pamięci podręcznej, czyli sięgnęła do wcześniej zapisanego pliku, żeby nie pobierać po raz kolejny.

{% include info.html
type="Ciekawostka"
text="Uwagę mogą zwracać dwie ostatnie kolumny. Widać różnicę między rozmiarem pobranych danych a&nbsp;wielkością pliku końcowego.  
Czasem wynika ona z&nbsp;kompresowania, a&nbsp;czasem z&nbsp;faktu, że dane są wysyłane w&nbsp;częściach (**pakietach**), dopchnięte cyfrowym odpowiednikiem folii bąbelkowej."
%}

A jak podejrzeć ruch na smartfonie? Jeśli ktoś nie chce *rootować*, to ma ograniczone możliwości. Ani smartfon, ani przeglądarki (wyjątek: Kiwi Browser) zwykle nie dają dostępu do narzędzi.

Można jednak zyskać pewien wgląd, instalując na Androidzie *firewalla*, takiego jak aplikacja Rethink DNS. Wyłapuje ona, na poziomie całego telefonu, z&nbsp;jakimi domenami łączyły się różne aplikacje.

{:.figure .bigspace-before}
<img src="/assets/tutorials/rethink-dns/rdns-logi-sieciowe-przyklad.jpg" alt="Pojedyncza pozycja z&nbsp;listy pokazująca ikonkę przeglądarki Firefox, stronę news.ycmbinator.com, jej adres IP oraz godzinę połączenia i&nbsp;parę pomniejszych informacji"/>

{:.figcaption}
Podglądacz nie widziałby, w&nbsp;przeciwieństwie do użytkowników apki, że jakaś prośba wyszła od Firefoksa. Resztę by widział.

{% include info.html
type="Inne programy"
text="Odpowiednikiem Rethinka na systemie Mac OS wydaje się popularny, choć płatny Little Snitch (nie testowałem, zresztą nie mam MacBooka).  
System Linux ma z&nbsp;kolei otwartoźródłowego [OpenSnitcha](https://github.com/evilsocket/opensnitch). Może on działać również [na linuksowych smartfonach](https://puri.sm/posts/snitching-on-phones-that-snitch-on-you/).
"%} 

Najmocniejszym narzędziem -- za cenę wyższej bariery wejścia dla nowicjuszy, jak ja -- jest natomiast program [Wireshark](https://www.wireshark.org/). Przechwytuje cały ruch sieciowy, wszystkie pakiety danych. Daje wgląd w&nbsp;najdrobniejsze szczegóły.

{:.figure}
<img src="/assets/posts/inwigilacja/ruch-sieciowy/wireshark-ruch-internetowy.jpg" alt="Przycięty ekran z&nbsp;programu Wireshark, w&nbsp;którym wyróżniono nazwę domeny Github Assets w&nbsp;głębi jednego z&nbsp;pakietów"/>

{:.figcaption}
Znowu emota, jak ta wypatrzona w&nbsp;narzędziach przeglądarki. Ale tym razem jest więcej szczegółów.

Wireshark najlepiej oddaje, jakie dane widziałby prawdziwy podglądacz. A&nbsp;co mógłby z&nbsp;nich wyciągnąć? Czas na przykłady.

### System, przeglądarka, aplikacje

Nawet gdyby podglądacz całkiem olał inne detale i&nbsp;patrzył na same nazwy domen, wciąż mógłby sporo z&nbsp;nich odczytać. Chociażby to, **z jakich aplikacji korzystam, a&nbsp;nawet (czasem) co w&nbsp;nich robię**.

Ta sprawa bardziej pasuje do mojej innej serii, [„Apki to pułapki”](/serie/apki){:.internal}. Ale jest na tyle istotna, że przynajmniej ją streszczę. 

Wiele popularnych systemów i&nbsp;programów regularnie łączy się ze swoimi twórcami. Czy to w&nbsp;celu automatycznej aktualizacji, czy też wysłania danych *telemetrycznych* (ogólnych informacji dotyczących korzystania z&nbsp;aplikacji).

Zaobserwowałem takie połączenia na smartfonie, w&nbsp;logach apki Rethink DNS. Niekoniecznie wykonane w&nbsp;złych celach... Co nie zmienia faktu, że podglądacz też widzi te domeny (zapewne; zakładam brak szyfrowania metadanych). Kilka przykładów:

* `moto-cds.appspot.com` (domena, z&nbsp;której pobierane są [aktualizacje do Motoroli](https://xdaforums.com/t/tool-win-ota-updates-motorola.3810863/post-77433067));
* `incoming.telemetry.mozilla.org` (domena Mozilli, twórców Firefoksa); 
* `graph.facebook.com`;
* `chat.signal.org`;
* `staticcdn.duckduckgo.com` (domena wyszukiwarki [DuckDuckGo](https://duckduckgo.com));
* `sync.ryanair.com` (domena linii lotniczej Ryanair).

Od jakiego producenta mam telefon? Jakiej zapewne używam przeglądarki i&nbsp;wyszukiwarki? Z&nbsp;jaką linią latałem (a&nbsp;przynajmniej: gmerałem w&nbsp;jej apce)?

Wszystkie te informacje są widoczne. Podglądacze mogliby przypisywać domeny do aplikacji i&nbsp;na tej podstawie mnie szufladkować.  
Signal, Firefox i&nbsp;DuckDuckGo? Dla reklamodawcy: „Stereotypowy prywatnościowiec. Spróbuję mu sprzedać VPN-a albo klucze sprzętowe”.

### Rozpoznawanie interakcji

Odgadnięcie nazwy aplikacji może być zaledwie początkiem śledzenia.

Jedna apka może w&nbsp;końcu obsługiwać różne tryby działania. Dla każdego z&nbsp;nich powiązane domeny i&nbsp;rozmiar danych mogą nieco się różnić. Jeśli podglądacz zna się na działaniu apki, to może **odczytać z&nbsp;ruchu sieciowego, w&nbsp;jakim trybie jej używałem**.

Z ciekawości zrobiłem sobie na przykład reset hasła w&nbsp;apce linii Ryanair. Potem w&nbsp;historii Rethink DNS-a mogłem zobaczyć dość nietypową kombinację domen, z&nbsp;jakimi mnie połączyło. W&nbsp;tym jakąś zewnętrzną usługę weryfikacyjną -- `risk-api.inauth.com`. Podczas normalnego korzystania się nie pojawiała.

{% include info.html
type="Ciekawostka"
text="To już sprawa mniej związana z&nbsp;prywatnością *osobistą*, ale w&nbsp;ten sposób użytkownicy aplikacji mogliby poznawać powiązania biznesowe jej twórców. W&nbsp;końcu jeśli regularnie łączą się z czyimś serwisem, to zapewne korzystają z&nbsp;jego usług."
%}
  
Nieszkodliwa anegdotka? To mam groźniejszy przykład.

Stalker od kawiarnianego hotspota mógłby zobaczyć po domenie, że używająca go osoba właśnie weszła w&nbsp;interakcję z&nbsp;wrażliwą stroną typu OnlyFans.  
I nie w&nbsp;celach konsumpcji. Po rozmiarze danych wysłanych poznałby, że *wrzuciła* tam jakiś plik. Wiedziałby, co to oznacza :wink:

A potem -- znając dokładny czas wrzucenia, twarz tej osoby (z&nbsp;monitoringu) i&nbsp;fakt, że to ktoś z&nbsp;Polski -- mógłby ją wystalkować na portalu.

### Styl pisania

Inny przykład: komunikatory. Zapewne część z&nbsp;nich nie dba o&nbsp;ochronę przed analizą ruchu. Chlubnym wyjątkiem jest Signal, który nawet dopycha pliki pustymi danymi, żeby [ukryć, jakie pobrano *gify*](https://signal.org/blog/signal-and-giphy-update/).

Podglądacz widzi pojedynczy wyrzut danych ku domenie komunikatora? Czyli pewnie wysłaliśmy wiadomość.  
Jeśli nijak nie dopychają danych, to jej rozmiar odpowiadałby jej długości. A&nbsp;to aż się prosi o&nbsp;analizę :smiling_imp:. Podobną do tej, jaką kiedyś przeprowadziłem na swoich [wiadomościach z&nbsp;Messengera]({% post_url 2021-05-14-messenger-analiza %}){:.internal}.

Ktoś obserwujący ruch mógłby odgadnąć, czy strzelamy krótkimi wiadomościami, czy komponujemy dłuższe. Jak często wysyłamy obrazki (duże wyrzuty danych) i&nbsp;filmy (największe wyrzuty).  
A nawet... Jaka jest nasza szybkość pisania. Byłby to rozmiar wyrzutów danych -- ale tylko tych drobniejszych -- podzielony przez czas między wyrzutami.

### Ustalenie zwyczajów

Było o&nbsp;stalkerze widzącym twarz, to teraz o&nbsp;firmie telekomunikacyjnej. Która niekoniecznie widzi twarz, ale ma na tacy cyfrową część życia. Analizując mój ruch sieciowy dzień w&nbsp;dzień, przez lata, dobrze pozna moje zwyczaje. Takie jak:

* godziny aktywności,

  W&nbsp;jakich godzinach zwykle zaczyna się wzmożone przesyłanie danych? Kiedy się kończy? Jest spora szansa, że ukazuje moment porannego sprawdzania telefonu oraz [*doomscrollingu*](https://pl.wikipedia.org/wiki/Doomscrolling) przed snem.

* skłonność do konsumpcji multimediów,

  Jeśli odwiedzam domenę znaną z tego, że hostuje materiały wideo, a&nbsp;w dodatku pobieram sporo danych... To jest spora szansa, że te filmy oglądam. Podglądacz nie dowie się, *które dokładnie*. Ale dowie się, *jak często*.

* podzielność uwagi w&nbsp;pracy (:wink:).

  Czy często korzystam z&nbsp;aplikacji w&nbsp;godzinach i&nbsp;dniach, kiedy powinienem siedzieć w&nbsp;pracy? Zapewne wtedy *się obijam*{:.corr-del} działam wielozadaniowo.

### Powiązania między osobami 

Ktoś planuje zgadać się z inną osobą przez wideokonferencję. Loguje się na odpowiednią platformę, zaprasza osobę z&nbsp;listy kontaktów. Czeka na połączenie, zaczynają rozmawiać.

A podczas wideokonferencji często dochodzi do [ujawnienia prawdziwych adresów IP]({% post_url 2023-11-05-webrtc %}){:.internal}. Takie zeswatanie ze sobą dwóch urządzeń, żeby nie obciążały platformy pośrednictwem między sobą. Adresy trafiają na widok publiczny.

W oczach podglądacza: najpierw było pobranie danych z&nbsp;domeny należącej do platformy wideokonferencyjnej. Potem duża ilość danych wymieniona z&nbsp;konkretnym adresem IP (nienależącym do znanego portalu). Diagnoza: obserwowana osoba **rozpoczęła wideorozmowę z&nbsp;tym drugim adresem IP**.

Czasem adres może być statyczny (niezmienny) i&nbsp;przypisany do konkretnej organizacji. Gdyby podglądacz mógł to sprawdzić w&nbsp;jakiejś bazie, to by wiedział, z&nbsp;kim dana osoba weszła w&nbsp;interakcje. Być może adres IP pasuje do kogoś ciekawego, jak kancelaria od spraw rozwodowych? Albo klinika leczenia nowotworów?

Takie dane mógłby zdobyć nawet prosty kawiarniany stalker. Ale jego możliwości bledną przy tym, co może operator sieci komórkowej, jeśli to przez nią odbyła się rozmowa. Ten drugi mógłby nawet **ustalić tożsamość rozmawiających osób**.

Przez jedną bazę wykonuje przejście `adres IP → numer telefonu` (w&nbsp;końcu wie, komu przydzielił adres). Przez drugą bazę `numer telefonu → dane osobowe` (wymóg rejestracji karty SIM).  
Na pewno pozna co najmniej jedną osobę. A&nbsp;jeśli obie są jego klientami, to pozna konkretne powiązania osobowe. O&nbsp;ochronie przed takim czymś stworzyłem [osobny samouczek](/tutorials/webrtc-wylaczenie){:.internal}.

## Jak się chronić

Wnikliwe osoby zauważą, że wszystkie powyższe zagrożenia opierały się na tym, że przeciwnik znał nazwę odwiedzanej domeny. **Gdyby ją jakoś ukrywać, to jego plany ległyby w&nbsp;gruzach**.

{:.post-meta .bigspace-after}
A przynajmniej powinny. Pod koniec tego wpisu i&nbsp;wewnątrz kolejnego będą kontrprzykłady.

Żeby móc tę informację ukryć, trzeba wiedzieć, gdzie się znajduje. Są co najmniej dwa główne etapy interakcji, kiedy to nazwa domeny znajduje się na widoku:

1. Kontakt z&nbsp;DNS-em, swoistą „książką telefoniczną internetu”, w&nbsp;celu poznania adresu strony. Nie ma szyfrowania, dane są widoczne.  
2. Kontakt ze stroną docelową. Szyfrowany, ale na pancernych pudłach są etykiety z&nbsp;nazwą odbiorcy.

Oto schemat interakcji podczas odwiedzania zmyślonej stronki *przyklad.pl*:

<img src="/assets/posts/inwigilacja/ruch-sieciowy/https-komunikacja.jpg" alt="Schemat komunikacji ze stroną internetową przyklad.pl. Widać na nim laptopa połączonego strzałkami z&nbsp;dwoma serwerami, z&nbsp;których jeden jest podpisany DNS, a&nbsp;drugi przyklad.pl. W&nbsp;kilku miejscach widać nazwy tego drugiego."/>

{:.figcaption}
Źródło obrazków na tym i kolejnych schematach: Flaticon, skrzynka z gry *Portal*.  
Szczegóły pod koniec wpisu. Aranżacja moja.

A teraz przejdę do środków zaradczych.

### Niewierność wobec podglądacza

Tak na logikę -- jeśli nie połączymy się z&nbsp;internetem, to podglądacz nie zobaczy, co do niego wysyłamy ([obowiązkowy mem](https://imgflip.com/i/20osaf)).

...No dobra, może to niekoniecznie realne w&nbsp;obecnych czasach. Ale wciąż można przestrzegać paru intuicyjnych zasad:

* nie zaglądać na stronki o&nbsp;wiele mówiących nazwach przez cudzego hotspota,
* albo w&nbsp;drugą stronę -- nie szukać kontrowersyjnych, acz legalnych informacji (o&nbsp;długach, nałogach itp.) przez swoją sieć. Tylko przez publicznie dostępny komputer w&nbsp;bibliotece, gdzie nikt nas nie zna.

W ten sposób, choć nie ukrywamy aktywnie nazw domen, przynajmniej rozdzielamy informacje między podglądaczy. Nie ma jednego stalkera/reklamodawcy, który znałby i&nbsp;twarz, i&nbsp;personalia, i&nbsp;wrażliwe wędrówki po sieci.

Można też odebrać dostęp do internetu programom, które go nie potrzebują.  
Na smartfonie [blokuję apki przez Rethink DNS](/tutorials/rethink-dns#firewall){:.internal}. Między innymi aplikację od map, bo korzystam z&nbsp;nich w&nbsp;wersji *offline*, po pobraniu na telefon. Operator nie zobaczy, jak często z&nbsp;nich korzystam, a&nbsp;śmigają normalnie.

Mając rozwiązanie intuicyjne z&nbsp;głowy, przejdę do aktywnych sposobów ukrywania domen.

### Szyfrowany DNS i&nbsp;ECH

Jednym ze sposobów na prywatność jest zaszyfrowanie nazwy domeny we wszystkich miejscach, w&nbsp;których się pojawia.  
Podczas interakcji z&nbsp;DNS-em można ją ukryć, korzystając z&nbsp;metody [DoH (albo DoT)]({% post_url 2022-08-14-dns-dot-doh %}){:.internal}. Podczas interakcji ze stroną docelową wykorzystuje się z kolei [ECH]({% post_url 2022-08-13-metadane-esni-ech %}){:.internal}. Obie metody opisałem dokładniej w&nbsp;podlinkowanych wpisach, więc pominę szczegóły.

Sedno sprawy -- zaszyfrowane jest wszystko poza adresem IP:

<img src="/assets/posts/inwigilacja/ruch-sieciowy/https-doh-ech-komunikacja.jpg" alt="Schemat komunikacji ze stroną internetową przyklad.pl. Widać na nim laptopa połączonego strzałkami z&nbsp;dwoma serwerami, z&nbsp;których jeden jest podpisany DNS, a&nbsp;drugi przyklad.pl. Ale nazwy serwera docelowego są w&nbsp;każdym miejscu zakryte."/>

Wielką zaletą tych metod jest fakt, że są wspierane za kulisami. Bez widocznych zmian po stronie użytkowników. W&nbsp;przyszłości być może z&nbsp;automatu.

Wady? Nawet jeśli podglądacz nie widzi domeny, nadal widzi docelowe adresy IP.

W skrajnym przypadku adres IP odpowiada jeden do jednego jakiejś konkretnej stronie. Wtedy ukrycie domeny byłoby na nic.

W obecnych czasach pod jednym adresem IP nieraz występuje wiele różnych domen. Utrudnia to rozpoznawanie, dokąd ktoś idzie... Ale niekoniecznie je uniemożliwia.  
Niektórzy badacze byli w&nbsp;stanie odgadywać odwiedzane strony [na podstawie kombinacji adresów IP](https://www3.cs.stonybrook.edu/~mikepo/papers/fingerprinting.pets21.pdf), z&nbsp;jakimi były związane. Opiszę to dokładniej w&nbsp;kolejnym wpisie.

Druga słabość kombinacji DoH+ECH to fakt, że na razie metoda dopiero się przebija do mainstreamu, [wiele stron jej nie obsługuje](https://link.springer.com/chapter/10.1007/978-3-031-25460-4_10). Nawet jeśli się spopularyzuje, nigdy nie ochroni *wszystkich* stron.

### VPN

Inną metodą może być **skorzystanie z&nbsp;pośrednika** między sobą a&nbsp;innymi serwisami. Istnieją różne rodzaje takich pośredników, najbardziej znane są VPN-y.

Wzrok podglądaczy nie sięga zwykle dalej niż do pierwszego adresata. A&nbsp;jeśli będzie nim pośrednik -- który potem popyta inne serwisy w&nbsp;naszym imieniu, poza rewirem podglądaczy -- to niewiele zobaczą.

Wszystkie dane w&nbsp;ich oczach będą zaszyfrowane i&nbsp;będą miały tego samego adresata. Pośrednika. Nie zobaczą końcowej domeny ani jej adresu. Jedynie rozmiar i&nbsp;ilość danych, które trudno by było do czegoś przypisać.

<img src="/assets/posts/inwigilacja/ruch-sieciowy/https-vpn-komunikacja.jpg" alt="Schemat komunikacji ze stroną internetową przyklad.pl przez VPN-a. Widać na nim laptopa połączonego strzałkami z&nbsp;VPN-em. Ten z&nbsp;kolei jest połączony z&nbsp;dwoma serwerami, z&nbsp;których jeden jest podpisany DNS, a&nbsp;drugi przyklad.pl."/>

Wielką zaletą pośredników jest fakt, że przy odpowiednich ustawieniach można pod nich podpiąć cały swój ruch. Nie tylko z&nbsp;przeglądarki, o&nbsp;której piszę tu najwięcej, ale również ten wychodzący z&nbsp;innych programów.

Są też niezależni od tego, czy strona docelowa wspiera szyfrowanie danych. Zapewniają je po swojej stronie, podczas interakcji z&nbsp;nimi. Można nawet odwiedzać z&nbsp;nimi stronki nieobsługujące szyfrowania, zaczynające się od `http://`, a&nbsp;podglądacz i&nbsp;tak nic nie odczyta.

{:.post-meta .bigspace-after}
Ale nadal odradzam *logowanie się* na tego rodzaju stronki, bo VPN mógłby sobie gromadzić hasła dostępu. Stronki nieszyfrowane są do przełknięcia tylko wtedy, gdy to statyczna treść.

Wada rozwiązania, jeśli po drodze stoi tylko jeden VPN? Wymaga **przeniesienia zaufania na tego pośrednika**. Ten nadal będzie widział, z&nbsp;kim się kontaktujemy. Nie mamy gwarancji, poza jego obietnicami, że nie dzieli się tymi informacjami.  
Z tego względu nie będę tutaj polecał żadnego konkretnego VPN-a. Nie chcę mieć nikogo na sumieniu :wink:

### Sieć Tor

Rozwiązaniem jeszcze potężniejszym, do tego darmowym, byłoby skorzystanie z&nbsp;przeglądarki [Tor Browser](https://www.torproject.org/download/).

Wykorzystuje ona sieć Tor.  
To cała pajęczyna pośredników, rozrzuconych po świecie i&nbsp;przydzielanych losowo na potrzeby naszych interakcji. Każdy z&nbsp;nich zna tylko część informacji, więc mieliby poważny problem, żeby przypisać odwiedziny na stronach do konkretnych osób. 

A to zaledwie początek. Sieć Tor celowo [miesza, żeby utrudnić analizę ruchu](https://youtu.be/trMLnwZAqEM?feature=shared&t=151) (YouTube). Dodaje od siebie trochę sztucznych pakietów, wprowadza nieregularne opóźnienia... Aktywnie utrudnia podglądaczom życie.

Sieć jest rozwiązaniem ogólnym, z&nbsp;którego mogą korzystać inne przeglądarki. Funkcję wspiera choćby Brave. Ale to Tor Browser, autorska przeglądarka od ekipy tworzącej sieć, zawiera najwięcej bajerów chroniących prywatność.

{% include info.html
type="Uwaga"
text="Przeglądarka Tor Browser, choć w&nbsp;mediach bywa demonizowana i&nbsp;nazywana „przeglądarką od darknetu”, nie zmusza nikogo do wchodzenia w&nbsp;ciemniejsze zakamarki sieci. Wystarczy nie odwiedzać stron zakończonych na `.onion`, a&nbsp;jedynie te co zwykle. Wtedy Tor to po prostu VPN na sterydach.  
[Problemem nie jest żaden darknet](/2023/06/02/clearnet-deepnet-darknet){:.internal}. Tylko co najwyżej fakt, że niektóre strony rozpoznają ruch idący przez Tora i&nbsp;złośliwie go nie wpuszczają albo każą rozwiązywać Captche.
"%}

## Pułapka korelacji czasowej

Tor jest super. Ale nawet on nie ocali tych, którzy całkiem się nie pilnują.

Znany jest przypadek pewnego studenta z&nbsp;USA, który [wpadł mimo korzystania z&nbsp;Tora](https://www.forbes.com/sites/runasandvik/2013/12/18/harvard-student-receives-f-for-tor-failure-while-sending-anonymous-bomb-threat/). I&nbsp;nie musiało go demaskować żadne FBI czy NSA. Mógłby to zrobić nawet zwykły administrator sieci uczelnianej.

Bez wchodzenia w&nbsp;szczegóły: gość wysłał swojej uczelni wiadomość z&nbsp;treścią karalną. Zrobił to przez jakiegoś hotspota na kampusie, ale używał Tora, myśląc że jest anonimowy.
 
Problem w&nbsp;tym, że **korzystał z&nbsp;tej samej sieci (uczelnianej) co odbiorca docelowy**. Dzięki temu dało się **skorelować** dane z&nbsp;początku i&nbsp;końca drogi.  
Tutaj cały łańcuszek dla wzrokowców, czerwonym kolorem oznaczyłem miejsca podglądane:

<pre class="black-bg mono">
Student → <span class="red">sieć uczelni</span> → sieć Tor → <span class="red">sieć uczelni</span> → odbiorca 
</pre>

Uczelnia znała godzinę otrzymania maila. Widziała, że przyszedł z&nbsp;sieci Tor, bo istnieją publiczne bazy związanych z nią adresów IP.  
Skoro wyszło z&nbsp;Tora, to musiało też wejść do Tora. Wystarczyło zatem poszukać, jakie urządzenia o&nbsp;podobnej godzinie kontaktowały się z&nbsp;innym IP ze znanej listy.  
Jak się okazało, student był jedyną osobą pasującą do wzorca. Tor nie był jakimś hitem kampusu. 

Ta historia nie pokazuje słabości sieci Tor, bo ta dobrze robiła swoją robotę. Ale, wciśnięta między dwa wrogie punkty, traciła swoje właściwości.  
Z kolei fakt, że istnieją listy związanych z&nbsp;nią adresów IP, jest raczej nieunikniony. Serwery są trochę jak nieruchomości, nie są w&nbsp;stanie ciągle się przemieszczać.

Gdyby kogoś zainteresował temat, to proponuję poszukać w&nbsp;sieci frazy `tor correlation attack`. To cały obszar badań i&nbsp;można znaleźć różne ciekawe prace.

Na dziś to tyle! Niebawem wrzucę jeszcze jeden wpis, w&nbsp;którym rozwijam wątek analizy ruchu o&nbsp;aktywne tworzenie mapek stron. Tak zwany *website fingerprinting*.

{% include info.html
type="Źródło obrazków"
text="Główne źródło: serwis Flaticon."
trailer="
<ul class='with-next' id='obrazki'>
 <li>Ikona <a href='https://www.flaticon.com/free-icon/laptop-screen_288870'>laptopa</a> autorstwa <em>vectorsmarket15</em>.</li>
  <li>Ikona <a href='https://www.flaticon.com/free-icon/server_742282'>serwera</a> autorstwa <em>Smashicons</em>.</li>
 <li><a href='https://www.flaticon.com/free-icons/down-arrow'>Strzałki</a> autorstwa <em>Freepik</em>.</li>
</ul>"
%}


