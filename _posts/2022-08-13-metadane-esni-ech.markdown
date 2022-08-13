---
layout: post
title:  "Internetowa inwigilacja plus 2 – ukrywanie metadanych"
subtitle: "Dokąd idę? Nie powiem."
description: "Dokąd idę? Nie powiem"
date:   2022-08-13 20:45:00 +0100
firmy: [Apple, Cloudflare, Mozilla]
tags: [Centralizacja, Internet, Inwigilacja]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: "https/esni-baner.jpg"
image-width: 1200
image-height: 700
---

Witam w&nbsp;drugim wpisie rozszerzającym serię „Internetowa inwigilacja”! Nadal skupiamy się na chowaniu wysyłanych informacji przed podglądaczami, takimi jak firmy telekomunikacyjne.

{:.post-meta .bigspace}
Dupochronik: to luźny wpis od hobbysty dla hobbystów. Nie zajmuję się cyberbezpieczeństwem. Zachęcam do weryfikowania informacji z&nbsp;tego wpisu w&nbsp;innych źródłach.

Poprzedni wpis mógł być nieco uspokajający, bo zobaczyliśmy, że osoby trzecie nie są w&nbsp;stanie dostrzec szczegółowych informacji, takich jak treść oglądanych przez nas stron, ich dokładne adresy, pliki cookies albo podstawowe informacje o&nbsp;naszej przeglądarce.  
Wszystko to dzięki powszechnie przyjętej szyfrowanej komunikacji przez HTTPS.

{% include info.html
type="Uwaga"
text="Mocno zachęcam, żeby czytać ten wpis na świeżo po <a href='/internetowa_inwigilacja/2022/08/13/https.html' class='internal'>poprzednim, dotyczącym HTTPS-a</a>. Przedstawiam tam nieco nietypową analogię, w&nbsp;której szyfrowana komunikacja polega na tym, że wymieniamy się otwartymi kłódkami, a&nbsp;potem przesyłamy sobie rzeczy w&nbsp;zamkniętych pancernych skrzynkach."
%}

Ale oprócz samej treści wiadomości, zaszyfrowanej przez HTTPS, pozostają jeszcze **_metadane_ -- ogólne informacje, które ujawniają, _jakie strony_ odwiedzaliśmy**. Na szczęście na nie również są sposoby.

# Spis treści

* [O metadanych](#o-metadanych)
* [Wykorzystanie VPN-a](#wykorzystanie-vpn-a)
* [Światowy marsz ku prywatności](#światowy-marsz-ku-prywatności)
  * [Koniec z&nbsp;prośbami o&nbsp;weryfikację](#koniec-zprośbami-oweryfikację)
  * [Upychanie wielu osób pod jednym IP](#upychanie-wielu-osób-pod-jednym-ip)
  * [ESNI – szyfrujemy dokładny adres](#esni--szyfrujemy-dokładny-adres)
  * [ECH – szyfrujemy prawie wszystko](#ech--szyfrujemy-prawie-wszystko)
* [Podsumowanie](#podsumowanie)

## O metadanych

Metadane to informacje wysyłane jawnie przy każdej internetowej interakcji. Nie zdradzą wprost, jaki konkretny wpis z&nbsp;bloga czytaliśmy, ale mówią bez owijania w&nbsp;bawełnę, że weszliśmy na przykład na *ciemnastrona.com.pl*.

{:.bigspace-before}
<div class="black-bg mono">
https://www.ciemnastrona.com.pl<span class="red">/internetowa_inwigilacja/2022/08/13/https</span>
</div>

{:.figcaption}
Dokładny adres poprzedniego wpisu. Operator telekomunikacyjny nie widzi tego, co na czerwono, ale widzi domenę.

Takie dane mógłby odczytać każdy, kto ma kontrolę nad routerem, przez który łączymy się z&nbsp;internetem.

Jedna grupa to podglądacze amatorscy; na przykład znudzony studenciak na śmieciówce sprawdzający, co odwiedza jakiś klient przez kawiarnianego hotspota.  
Ich możliwości nie są zbyt wielkie -- widzą jedynie nazwy tych stron, które odwiedzimy, sącząc u&nbsp;nich kawę. W&nbsp;najgorszym razie zapamiętają sobie kogoś. *"O, to typ(-iara), co ogląda u&nbsp;nas niegrzeczne stronki*".

Gorsi są podglądacze wytrawni -- jak dostawcy usług internetowych (ang. ISP, *Internet Service Provider*), od których mamy naszego routera domowego. Praktycznie codziennie korzystamy z&nbsp;ich infrastruktury, więc mogą zebrać pokaźną kolekcję odwiedzanych przez nas stron, a&nbsp;tym samym naszych zwyczajów i&nbsp;zachowań.

Potem, jeśli chcą, [przekazują te dane policji](https://www.privateinternetaccess.com/blog/starting-november-1st-chinese-police-can-go-to-any-chinese-isp-to-copy-your-data/). „Delikwent często wchodzi na strony antyrządowe? Obniżymy mu ranking społeczny”.  
Albo [sprzedają  je reklamodawcom](https://blog.simpleanalytics.com/vodafone-deutsche-telekom-to-introduce-persistent-user-tracking). Co kto woli.

Z różnych powodów moglibyśmy chcieć ukryć przed nimi, jakie strony odwiedzamy. Jak to zrobić?

## Wykorzystanie VPN-a

Firmy telekomunikacyjne to nie Sauron, nie są wszechwidzące. Zwykle **ich wzrok sięga jedynie do pierwszego podmiotu, z&nbsp;którym się skontaktujemy**.

A co, jeśli tym podmiotem będzie zaufany pośrednik? Jak na przykład operator VPN-a?

W takim wypadku telekom zobaczy jedynie, że wymieniliśmy się z pośrednikiem swoimi kłódkami, a&nbsp;potem przesyłamy sobie wiele rzeczy w&nbsp;zamkniętych pancernych skrzynkach.  
Nie będzie natomiast widział, co pośrednik z&nbsp;tych pudełek wyjmuje i&nbsp;do kogo przesyła później nasze wiadomości. Straci nas z&nbsp;oczu.

<img src="/assets/posts/https/https-plus-vpn.jpg" alt="Schemat pokazujący komunikację przy użyciu VPN-a. Widać że "/>

{:.figcaption}
Szyfrowana komunikacja z&nbsp;udziałem VPN-a. Dla czytelności przeskoczyłem etap przesyłania sobie kłódek, ale oczywiście również ma tu miejsce.  
Pudło w&nbsp;górnej części jest półprzezroczyste tylko na schemacie; nikt nie podejrzy jego zawartości.  
Źródło ikon: Flaticon.

Rozwiązanie idealne? Niekoniecznie.  
O VPN-ach wspomniałem już w&nbsp;swoim [wpisie o&nbsp;adresach IP]({% post_url 2021-06-12-adres-ip %}){:.internal}. Byłem wtedy nieco sceptyczny i&nbsp;nadal to podtrzymuję. VPN-y są bowiem znane z&nbsp;reklam, w&nbsp;których opowiadają o&nbsp;sobie [niestworzone historie](https://www.youtube.com/watch?v=WVDQEoe6ZWY) (link do YT). Podkreślając w&nbsp;szczególności, że są niezbędną częścią cyfrowego życia i&nbsp;że chronią nas przed hakerami.

**Ochronę przed podglądaczami i&nbsp;podszywaczami zapewnia nam już HTTPS**. VPN-y nie dają pod tym względem zbyt wiele wartości dodanej, zaś wrogi hotspot przechwytujący nasze hasła do banku jest trochę jak czarna wołga -- taki straszak na niegrzeczne dzieci.

Fakt faktem, nieco chronią metadane przed wzrokiem telekomów. Ale nie przed swoim własnym. Korzystanie z&nbsp;VPN-ów oznacza po prostu **przeniesienie zaufania z&nbsp;jednego wielkiego podmiotu na inny**.  
Telekom nie zobaczy, że odwiedzaliśmy domenę *ciemnastrona.com.pl*, tylko że odwiedzaliśmy naszego VPN-a. Ale już VPN tę domenę zobaczy. A&nbsp;czy możemy mu ufać? Kwestia do przemyślenia.

Tym niemniej sposób działa. Jeśli dostawca internetu jest w&nbsp;naszych oczach zagrożeniem pewnym i&nbsp;najgorszym, zaś VPN odległym i&nbsp;teoretycznym, to jak najbardziej można owego VPN-a odpalić.  
O ile możemy -- świat zna bowiem kraje, które [wlepiają kary](https://www.comparitech.com/vpn/where-are-vpns-legal-banned/) za korzystanie z&nbsp;VPN-a. Często te same, które mają wścibskich operatorów sieci.

Nie polecę tutaj żadnego konkretnego operatora, zachęcam do samodzielnej lektury.

Oczywiście zamiast VPN-a można użyć też innych sieciowych pośredników, jak przeglądarka [Tor Browser](https://www.torproject.org/download/). Mając na uwadze, że bywa dość powolna i&nbsp;czasem blokowana przez nadgorliwe strony.

Ogólnie jedynym warunkiem jest to, żeby wszystkie rzeczy wysyłane i&nbsp;odbierane przez nas były szyfrowane i&nbsp;przechodziły przez co najmniej jeden obcy serwer. W&nbsp;ten sposób telekomy nie podejrzą, z&nbsp;kim piszemy.

A czy jest jakiś sposób na to, żeby podczas codziennego przeglądania internetu ochronić się przed wzrokiem telekomów, ale bez korzystania z&nbsp;pośredników? Tak! Ale to sam front walki o&nbsp;internetową prywatność.

Zainteresowanych zapraszam do dalszej lektury :smile:

## Światowy marsz ku prywatności

Zacznijmy od tego, że sami niewiele tu zdziałamy, bo wysyłanie pewnych informacji jest integralną częścią internetu. Gdybyśmy ustawili w&nbsp;swoim komputerze, żeby ich nie wysyłało, to po prostu by nam się przestały ładować strony. Taki odpowiednik wysyłania listów bez adresu.

Do tanga trzeba dwojga. Nas i&nbsp;naszych adresatów.

Poprawienie prywatności **wymaga zmian w&nbsp;protokołach -- zasadach działania internetu**. Niektóre organizacje, jak Mozilla i&nbsp;Cloudflare, podjęły obiecujące działania w&nbsp;kierunku ukrywania metadanych. Uszczelnili w&nbsp;tym celu interakcje, podczas których ujawniamy, jaką domenę odwiedzamy:

1. Nazwa domeny wysyłana do DNS-a  
   (na razie nie musimy wiedzieć, co to takiego, omawiam go w&nbsp;następnym wpisie; zapamiętajmy tylko, że jest na początku).
2. Nazwa bezpośrednio na rzeczach wysyłanych odwiedzanej stronie  
   (albo adres IP, jeśli jednoznacznie ją ujawnia).
3. Nazwa umieszczona na liście do certyfikatora, z&nbsp;prośbą o&nbsp;weryfikację kłódki.

**Trzeba ukryć wszystkie te informacje, żeby całkiem zataić, jakie strony odwiedzamy**. Gdyby choć jedna pozostała widoczna, to nasz operator telekomunikacyjny zapewne ją podejrzy.

Kwestie DNS-owe opisałem w&nbsp;odrębnym wpisie, więc nie poświęcimy im tu uwagi. Skupmy się na pozostałych dwóch. Zaczynając od kwestii weryfikacji kłódek, bo właściwie rozwiązała się sama.

# Koniec z&nbsp;prośbami o&nbsp;weryfikację

Wróćmy do naszej przeciętnej szyfrowanej interakcji. W&nbsp;normalnym przypadku przebiega następująco:

1. Wysyłamy swojemu adresatowi -- dajmy na to pani Y&nbsp;-- zaproszenie do bezpiecznej korespondencji.
2. W&nbsp;odpowiedzi otrzymujemy otwartą kłódkę.
3. Wysyłamy dokładne informacje o&nbsp;tej kłódce do producenta, z&nbsp;pytaniem czy to na pewno kłódka pani Y.
4. Otrzymujemy (oby!) odpowiedź twierdzącą.
5. Od tej pory korespondujemy z&nbsp;panią Y, wysyłając sobie pudełka zamknięte na kłódki.

Dawno nie było akronimów, więc rzucę paroma -- punkty 3&nbsp;i 4, czyli ogólnie komunikację z&nbsp;„producentem” w&nbsp;celu potwierdzenia wiarygodności kłódki, określamy skrótem *OCSP* (*Online Certificate Status Protocol*).

Z punktu widzenia prywatności ta wymiana jest problematyczna. Pytając, czy kłódka na pewno należy do jakiejś osoby, musimy tę osobę wskazać. „Czy to na pewno kłódka od *ciemnastrona.com.pl*?”. Wszystko to [na widoku albo łatwe do ustalenia](https://blog.seanmcelroy.com/2019/01/05/ocsp-web-activity-is-not-private/).

Na szczęście ten problem już został w&nbsp;znacznej mierze rozwiązany; niejako przy okazji poprawiania wydajności.

Wyobraźcie to sobie -- za każdym razem, kiedy ktoś otrzymał od jakiejś strony kłódkę, słał do certyfikatora pytanie o&nbsp;jej autentyczność. A&nbsp;przecież wymiany odbywały się non stop.  
Serwery trzeszczały od obciążenia, aż „producenci kłódek” nie wytrzymali. Udostępnili metodę, dzięki której nie musimy się z&nbsp;nimi kontaktować. Przerzucili odpowiedzialność na właścicieli stronek.

Metoda nosi nazwę *[OCSP stapling](https://en.wikipedia.org/wiki/OCSP_stapling)*. Chcąc wyrobić dla siebie kłódkę, stronki muszą regularnie zamawiać od producenta cyfrowy odpowiednik naklejek lub hologramów. Same je potem umieszczają na kłódkach.

Taki hologram wskazuje producenta, od którego dana kłódka pochodzi (a nawet cały łańcuszek firm, które ją stworzyły). Ma też określoną datę ważności -- wyobraźmy sobie, że wygląda to dokładnie jak te hologramy naklejane co semestr na odwrocie legitymacji studenckiej. I&nbsp;jest prawie niemożliwy do podrobienia.

{:.bigspace-before}
<img src="/assets/posts/https/ocsp-stapling-padlock.jpg" alt="Emoji otwartej kłódki. W&nbsp;jej dolnym prawym rogu znajduje się naklejony hologram jak z&nbsp;legitymacji studenckiej, z&nbsp;widoczną datą ważności do 2016&nbsp;roku." width="350px"/>

{:.figcaption}
Przykładowa kłódka z&nbsp;firmowym hologramem i&nbsp;datą ważności.

Tylko że odejście od kontaktu z&nbsp;certyfikatorem niesie za sobą zagwozdkę. Skąd nasza „poczta” (przeglądarka) ma teraz wiedzieć, że ta rzecz naklejona na kłódkę to jego niepodrabialny hologram? A&nbsp;nie świstek, który jakiś podszywacz sobie nakleił dla uwiarygodnienia?  
Wie, bo trzyma gdzieś u&nbsp;siebie **zamkniętą listę zaufanych podmiotów**. Porównuje z&nbsp;nią otrzymany hologram. Jeśli się zgadza, to znaczy że kłódka pochodzi od tego, od kogo powinna.

{% include info.html
type="Wątki poboczne"
text="Słowa „zamknięta lista podmiotów” może budzić pewien niepokój, zwłaszcza jeśli znacie moje podejście do centralizacji i&nbsp;skupiania władzy w&nbsp;rękach nielicznych. Istotnie, zależność całego internetu od wąskiego grona „producentów kłódek” to sprawa ciekawa i&nbsp;do zbadania. Ale nie na ten wpis.  
Jeśli chodzi o&nbsp;sprawę „presji” OCSP na serwery, to wyszła na tym tle ciekawa aferka z&nbsp;firmą Apple. Kiedyś przez ich przeciążenie wyszło na jaw, że każde uruchomienie dowolnego programu na Macu prowadziło do [wysłania informacji do Apple](https://www.howtogeek.com/701176/does-apple-track-every-mac-app-you-run-ocsp-explained/)."
%}

Dzięki tej zmianie -- przerzuceniu obowiązków na stronę nabywającą kłódki -- pozbywamy się konieczności pisania z&nbsp;ich producentem. Uszczelniamy pierwszą z&nbsp;interakcji ujawniających, jaką stronę odwiedzamy.  
Nowsze metody ochrony prywatności wymagają korzystania z&nbsp;metody **TLS w&nbsp;wersji co najmniej 1.3**. Brak kłopotliwych (dla prywatności) pytań o&nbsp;certyfikat mamy wtedy niejako w&nbsp;pakiecie.

# Upychanie wielu osób pod jednym IP

Jedna rzecz z&nbsp;głowy, pozostała kwestia adresu IP naszego adresata. Który jest obowiązkowy i&nbsp;potrafi całkiem sporo [ujawniać](https://blog.apnic.net/2019/08/23/what-can-you-learn-from-an-ip-address/).

W najbardziej skrajnym przypadku mamy **stronkę pod stałym i&nbsp;niezmiennym adresem IP. To przypadek beznadziejny**. Gdzieś w&nbsp;końcu musimy umieścić adres, żeby nasze przesyłki dotarły na miejsce. Telekom ten adres odczyta, a&nbsp;adres wprost identyfikuje stronę.

Żeby nie ujawniać jej nazwy, musielibyśmy skorzystać z&nbsp;pośrednika. Innej rady nie ma.

Nieco lepszą sytuację mamy wtedy, kiedy pod jednym adresem IP znajduje się jak najwięcej różnych odbiorców. Wtedy sam adres IP nikogo jednoznacznie nie ujawnia.  
Analogia: adresując list do jakiegoś domu jednorodzinnego, wystarczy napisać ulicę i&nbsp;numer domu. Jednoznacznie wskazuje to adresata. Ale w&nbsp;przypadku mieszkania w&nbsp;bloku trzeba dodać jeszcze numer lokalu, bo w&nbsp;bloku jest wiele mieszkań.

Wyobraźmy sobie, że mamy jakieś wielkie strzeżone osiedle. Ulica Zielona 4. Firma, dajmy na to, Cloudflare Development. Cała korespondencja do mieszkańców trafia do zaufanego osiedlowego stróża, który następnie roznosi listy i&nbsp;paczki pod konkretne mieszkania.

Ale my chcemy napisać do Nowaka z&nbsp;mieszkania *20*, a&nbsp;nie do jakiegoś Kowalskiego czy innego z&nbsp;tysięcy lokatorów! Gdzieś to *20* dla stróża trzeba umieścić. 

Jest to źródłem pewnych problemów i&nbsp;zaraz do tego przejdziemy. Na chwilę obecną zapamiętajmy tylko, że **lepszą sytuacją jest dla nas wiele różnych stron pod jednym adresem IP**. „Lepiej pisać z&nbsp;ludźmi z&nbsp;blokowisk, niż z&nbsp;domów jednorodzinnych”.

Tylko że blokowiska, choć lepsze z&nbsp;punktu widzenia naszej prywatności, siłą rzeczy oznaczają wepchnięcie ludzi w&nbsp;szpony branży deweloperskiej.  
Podobnie jest z&nbsp;internetem -- żeby być częścią wielkiej zbiorowości, strony musiałyby być hostowane przez dużych graczy, jak Cloudflare. Zganiając wszystkich w&nbsp;jedno miejsce, umacniamy kontrolę giganta. Widać zatem pewien dylemat między prywatnością a&nbsp;centralizacją.

Jest to jednak wątek poboczny. Warto o&nbsp;tym wiedzieć, ale tutaj skupiamy się *stricte* na prywatności. Dlatego przejdźmy dalej.

# ESNI – szyfrujemy dokładny adres

Jak pisałem, gdzieś trzeba umieścić nasz „numer lokalu”. Informację dla stróża mówiącą, do którego z&nbsp;wielu lokatorów piszemy.

W przypadku komputerów **taka informacja, wskazująca konkretną domenę spośród wielu, nosi nazwę _SNI_** (*Server Name Indication*). I&nbsp;jest -- tak, zgadliście -- publicznie widoczna!

Może się zatem wydawać, że upychanie wielu stron pod jednym IP jest bezcelowe. Ale spokojnie -- to po prostu warunek konieczny, lecz nie wystarczający. W&nbsp;jaki sposób można załatać tę lukę i&nbsp;ukryć SNI?

Odpowiedź: zastosować [ESNI](https://blog.cloudflare.com/encrypted-sni/) (*E* od *Encrypted*, *szyfrowane*), metodę fajnie opisaną na blogu Cloudflare.

Wyobraźmy sobie, że osiedlowy stróż postanawia zadbać o&nbsp;prywatność nadawców. Zostawia w&nbsp;naszym tajemniczym DNS-ie -- którego i&nbsp;tak każdy musi odwiedzić po drodze -- małą otwartą kłódkę (inną niż ta nasza czy naszego adresata). Kluczyk do niej oczywiście trzyma u&nbsp;siebie.

Korzystając z&nbsp;tej małej kłódki, zamykamy pudełeczko zawierające informację o&nbsp;SNI („dokładnym numerze mieszkania”). I&nbsp;przyczepiamy to do korespondencji, którą chcemy wysłać Nowakowi.

Kiedy stróż otrzyma nasz pakunek, widzi że pudełko z&nbsp;ESNI jest zamknięte na jedną z&nbsp;jego kłódek. Więc bierze swój kluczyk ze stróżówki, otwiera pudełko i&nbsp;odczytuje, że to dla Nowaka z&nbsp;mieszkania numer 20. Zanosi mu przesyłkę.

Reszta interakcji to już typowa szyfrowana korespondencja z&nbsp;Nowakiem. HTTPS-owe pancerne pudełka, tylko że przekazywane przez stróża. Który nie ma możliwości zajrzeć do ich wnętrza, bo w&nbsp;końcu ma jedynie kluczyk do ESNI.

{:.bigspace-before}
<img src="/assets/posts/https/esni-ech-schemat.jpg" alt="Schemat pokazujący komunikację z&nbsp;udziałem ESNI. W&nbsp;lewym górnym rogu widać ikonę laptopa i&nbsp;odchodzącą od niego strzałkę w&nbsp;dół, po skosie. Strzałka ta znajduje się wewnątrz niebieskiej elipsy symbolizującej obszar w&nbsp;zasięgu wszystkowidzącego oka. Widać nad nią dwa pudła zamknięte na kłódki, czerwoną i&nbsp;zieloną, oraz napis 'do IP 1.1.1.1'. Strzałka prowadzi do pomarańczowej ikony serwera podpisanej 1.1.1.1, mającej obok siebie czerwony kluczyk. To najwyższy punkt obszaru otoczonego pomarańczową obwódką i&nbsp;podpisanego na dole Cloudflare. Oprócz niego znajduje się tam kilka identycznych szarych serwerów. Od pomarańczowego serwera odchodzi kolejna strzałka w&nbsp;dół, do szarego serwera leżącego w&nbsp;dolnym prawym rogu, w&nbsp;połowie wewnątrz obwódki Cloudflare, a&nbsp;w połowie poza jakimkolwiek obszarem. Zamiast pudła zamkniętego na czerwoną kłódkę nad strzałką widać teraz napis 'Nowak'."/>

{:.figcaption}
Przyznam się, że nie ustaliłem dotąd, czy ESNI jest wysyłane w&nbsp;każdej interakcji, czy tylko na samym początku, a&nbsp;potem zostaje zastąpione przez jakiś wewnętrzny identyfikator odbiorcy. W&nbsp;każdym razie efekt ten sam: nazwa naszego odbiorcy zawsze będzie nieczytelna dla postronnych.

Z ESNI wiąże się pewien problem -- wymaga stróża skorego do współpracy. Gotowego zostawić gdzieś swoją kłódkę i&nbsp;wiedzącego, że może otwierać zamknięte nią rzeczy. Mówiąc językiem komputerowym: **serwer, któremu coś wysyłamy, musi wspierać ESNI**. Inaczej to wszystko nie zadziała.

Jeśli jednak trafimy na takiego stróża, to super. W&nbsp;ten sposób połączyliśmy ze sobą kilka rzeczy:

* HTTPS zamiast HTTP (korespondencja szyfrowana zamiast zwykłej).
* TLS wersję 1.3 (koniec ujawniania domeny podczas pisania z&nbsp;certyfikatorem).
* Upychanie wielu stron pod jednym adresem IP.
* ...i na koniec szyfrowanie dokładnego adresu strony.

Można mocno zamieszać, otrzymując prywatność w&nbsp;sieci.  
...Tylko że nie. Brakuje nam jeszcze jednego kluczowego składnika, jakim jest DNS. Poza tym ESNI da się zastąpić jeszcze lepszym składnikiem. 

Warto dodać, że rozwiązania oparte na TLS 1.3 oraz ESNI są albo mają być blokowane przez naszych ulubionych autokratów, [Chiny](https://www.zdnet.com/article/china-is-now-blocking-all-encrypted-https-traffic-using-tls-1-3-and-esni) i&nbsp;[Rosję](https://www.privateinternetaccess.com/blog/russia-wants-to-outlaw-tls-1-3-esni-dns-over-https-and-dns-over-tls).  
Uważam to za całkiem dobrą reklamę tych rozwiązań :wink:

# ECH – szyfrujemy prawie wszystko

ESNI, choć świetne jako koncepcja, miało parę słabości technicznych, których tu nie będę opisywał.

Ponadto SNI nie jest jedyną wrażliwą informacją (*rozszerzeniem*) wysyłaną na widoku; są też inne rozszerzenia, jak choćby ALPN. Polegający z&nbsp;grubsza na tym, że wypisujemy swoje możliwości, żeby osoba z&nbsp;drugiej strony lepiej dobrała do nas sposób komunikacji. Coś jak tagi z&nbsp;kategorii „zainteresowania”. Co nieco o&nbsp;nas ujawniają.

Poza tym metadane nie są sprawą zamkniętą. Pojawiają się pomysły na nowe rozszerzenia, żeby nieco lepiej dopasować internet do współczesności. Niektóre z&nbsp;nich siłą rzeczy musiałyby zdradzać wrażliwe informacje.

Ograniczając się do chowania samego SNI i&nbsp;wysyłania reszty na widoku, projektanci internetu nieco by się ograniczali. Mogłoby się to skończyć pogonią za standardami, przypominającą bieg Achillesa za żółwiem. Dlatego postanowili zrobić coś radykalniejszego.

W jaki sposób można zapewnić prywatność wszystkim informacjom z&nbsp;pierwszego kontaktu, również tym nieznanym, które mogą zostać dodane dopiero w&nbsp;przyszłości? Ktoś wpadł na pomysł: „pójdźmy na całość! Zaszyfrujmy wszystko poza adresem IP!”.

Siłą rzeczy oznacza to rezygnację z&nbsp;ESNI -- skoro do zamkniętego pudełka upychamy wszystko, łącznie z&nbsp;SNI, to nie ma potrzeby szyfrować go dwa razy.  
Ale dzięki temu dostaniemy coś jeszcze mocniejszego. *[Encrypted Client Hello](https://blog.cloudflare.com/encrypted-client-hello/)*  
(przypominam poprzedni wpis: *client hello* to pierwsza rzecz, jaką wysyłamy. Nasza prośba o&nbsp;szyfrowany kontakt).

Metoda działania jest taka sama jak przy ESNI. Najpierw pozyskujemy z&nbsp;ustalonej skrytki (DNS-a) kłódkę stróża odpowiedzialnego za roznoszenie przesyłek po swoim osiedlu. Używając jej, zamykamy w&nbsp;małym pudełku *wszystkie* informacje dodatkowe. SNI, ALPN oraz inne potworki.  
A następnie wysyłamy to pudełko pod ogólny adres osiedla (*adres IP*), współdzielony przez wiele osób. Stróż odbiera przesyłkę, otwiera swoim kluczykiem, odczytuje nasze *client hello* (w tym dokładny adres mieszkania) i&nbsp;dostarcza resztę gdzie trzeba.

W ten sposób zredukowaliśmy do minimum informacje ujawniane osobom postronnym podczas korespondencji. Wszystkie, w&nbsp;tym te, o&nbsp;jakich jeszcze się nam nie śniło. Zaś ta jedna, którą ujawnić trzeba -- adres IP -- jest współdzielona przez wiele osób i&nbsp;mało co zdradza.

Bieżące sprawy związane z&nbsp;ECH można znaleźć na [blogu Cloudflare](https://blog.cloudflare.com/handshake-encryption-endgame-an-ech-update/).

## Podsumowanie

Poczyniliśmy znaczne kroki w&nbsp;stronę zrozumienia zagrożeń „po drodze”, między nami a&nbsp;adresatami. Wliczając w&nbsp;to wszelkich podglądaczy, małych i&nbsp;dużych. Środki w&nbsp;naszym arsenale to przejście na szyfrowaną komunikację (HTTPS), rezygnacja z&nbsp;publicznego pisania w&nbsp;sprawie certyfikatów, upychanie wielu stron pod jednym IP, szyfrowanie nawet metadanych.

Gdy rozwiązania z tego wpisu się upowszechnią i&nbsp;zacznie je wspierać więcej firm od infrastruktury internetowej, to będą tak po prostu działały w tle, chroniąc przed wścibskimi oczami.  
Natomiast gdyby adresat naszej korespondencji nie wspierał tych nowinek, możemy po prostu korzystać z&nbsp;VPN-ów i&nbsp;innych pośredników. Z&nbsp;zastrzeżeniem, że wtedy to oni dostają nasze informacje zamiast telekomów.

Warto też przypomnieć, że na naszej drodze nieraz pojawiał się **dylemat między prywatnością a&nbsp;centralizacją**.

Zyskaliśmy HTTPS -- szyfrowaną i&nbsp;wygodną komunikację dla szerszej społeczności... Ale w&nbsp;tym celu przeglądarka musi polegać na nielicznych, zaufanych organizacjach uwierzytelniających.  
Zyskujemy prywatność, kiedy odwiedzany przez nas adres IP zlewa się z tłumem... Ale najlepiej się to sprawdzi, kiedy mamy jedną organizację zrzeszającą wiele różnych stronek.

Takich dylematów będzie coraz więcej. Bowiem kształt internetu wcale nie zależy tak bardzo od szarych użytkowników. To bardziej oligarchia niż demokracja.

Poza tym ten wpis to zaledwie kolejny element układanki. „Łańcuch jest tak wytrzymały, jak jego najsłabsze ogniwo”.  
A kiedy już wzmocniliśmy kwestie wokół HTTPS-a i&nbsp;metadanych, to słabym ogniwem pozostaje DNS, o&nbsp;którym dotąd wspominałem tylko ogólnikowo. „Książka telefoniczna internetu”, z&nbsp;którą często się kontaktujemy, odwiedzając nieznane nam strony.

No i&nbsp;muszę uprzedzić, że nawet DNS nie domknie tematu -- szczególnie wścibskie telekomy mogą analizować rozmiar przesyłanych rzeczy oraz czas ich przesłania.  
Ale to sprawa dość niszowa, muszę jeszcze trochę doczytać w&nbsp;temacie. Zostawię ją na przyszłość, a&nbsp;zainteresowani mogą szukać pod hasłem *traffic analysis*.

Tymczasem czas załatać luki DNS-owe. Zapraszam do kolejnego wpisu! :smile:

