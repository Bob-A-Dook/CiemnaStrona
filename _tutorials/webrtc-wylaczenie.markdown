---
layout: page
title: Wyłączanie WebRTC w różnych programach
description: "Gdy nie chcemy być swatani."
---

Ten samouczek uzupełnia mój [wpis na temat WebRTC]({% post_url 2023-11-05-webrtc %}){:.internal} -- standardu odpowiedzialnego głównie za wideorozmowy. Jednym z&nbsp;jego filarów jest odsunięcie pośrednika i&nbsp;komunikacja *peer-to-peer*, między użytkownikami.

Problem w&nbsp;tym, że w&nbsp;ten sposób może łatwo dojść do ujawnienia prawdziwego adresu IP, chowanego na przykład za VPN-em. A&nbsp;to niedobre dla prywatności.

Niektórzy mogą łatać luki i&nbsp;testować VPN-y, aż dopasują rozwiązanie do siebie. Ale najprościej chyba po prostu wyłączyć WebRTC.  
Pokażę tutaj, w&nbsp;jaki sposób można to zrobić w&nbsp;różnych przeglądarkach i&nbsp;paru innych aplikacjach.

{% include info.html
type="Uwaga"
text="Po wyłączeniu WebRTC **siłą rzeczy przestanie działać większość wideorozmów**. Albo innych, [mniej oczywistych rzeczy](https://news.ycombinator.com/item?id=33330740). Nawet jeśli działać nie przestaną, bo mają awaryjny wariant z&nbsp;pośrednikiem, to mogą być dużo wolniejsze.  
Chcąc z&nbsp;kimś porozmawiać w&nbsp;dobrej jakości, musielibyśmy wrócić do opcji i&nbsp;przywrócić poprzednie ustawienie.  
Dla codziennych użytkowników (jak rodzinka, której pomaga się ustawić elektronikę) może to być zaskakujące i&nbsp;wkurzające. Dlatego lepiej nie robić tego bez ich wiedzy."
%}

## Spis treści

* [Sprawdzanie w&nbsp;przeglądarkach](#sprawdzanie-wprzeglądarkach)
* [Wyłączanie w&nbsp;przeglądarkach](#wyłączanie-wprzeglądarkach)
  * [Chrome](#chrome)
  * [Edge](#edge)
  * [Opera](#opera)
  * [Vivaldi](#vivaldi)
  * [Firefox](#firefox)
  * [Tor Browser](#tor-browser)
* [Wyłączanie w komunikatorach](#na-różnych-komunikatorach)
  * [Signal](#signal)
  * [Telegram, Viber, Threema](#telegram-viber-threema)
  * [WhatsApp, Messenger, FaceTime](#whatsapp-messenger-facetime)


## Sprawdzanie w&nbsp;przeglądarkach

W przypadku przeglądarek praktycznie każda stronka, która doda do siebie odpowiedni kod, może otworzyć połączenie WebRTC, by po cichu zdemaskować adres IP.

Ta łatwość to zagrożenie, ale z&nbsp;drugiej strony -- zaleta. Połączenie może otworzyć też stronka sprzyjająca prywatności. Po czym w&nbsp;przystępny sposób ostrzec użytkownika, że mu prawdziwe IP wystaje.

Jedną z takich stronek jest [BrowserLeaks](https://browserleaks.com/webrtc), zawierająca wiele innych cennych informacji związanych z&nbsp;profilowaniem użytkowników. To jej użyję w&nbsp;tym przykładzie.  
A żeby nie było, że nie polecam alternatyw -- jest też [*ipleak.net*](https://ipleak.net).

Gdy odwiedziłem powyższy link do BrowserLeaks przez Operę *bez* włączonego VPN-a czy innego pośrednika, to wyświetliło, że nie ma wycieku. 

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/webrtc/bez-vpna.jpg" alt="Zrzut ekranu pokazujący fragment interfejsu BrowserLeaks. Wyświetlają się dwa adresy IP w&nbsp;różnych formatach, przy każdym widnieje polska flaga. Informacje poniżej mówią, że nie wykryto wycieku." />

Ale to żadne pocieszenie. **Jeśli ktoś w&nbsp;ogóle nie maskuje adresu IP, to po prostu ma wszystko na widoku. Nic wtedy nie da uszczelnianie WebRTC**.

Załóżmy, że ktoś jednak idzie o&nbsp;krok dalej i&nbsp;wykorzystuje jakiegoś pośrednika. Chociażby tego nisko ocenianego, ale darmowego VPN-a wbudowanego w&nbsp;Operę. Włączyłem go, a&nbsp;BrowserLeaks pokazał, że spod oficjalnego (szwedzkiego) IP widać ten prawdziwy:

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/webrtc/vpn-wyciek.jpg"  alt="Zrzut ekranu z&nbsp;Opery. U&nbsp;góry widać ikonkę VPN świecącą się na niebiesko. Poniżej widać stronę Browserleaks. Są tam dwa adresy IP ze szwedzkimi flagami, ale na dole znajduje się wzmianka, wyróżniona czerwonym kolorem, że wykryto inny adres IP, niezgodny z&nbsp;tym oficjalnym. To jeden z&nbsp;adresów z&nbsp;poprzedniego przykładu. Obok niego znajduje się polska flaga." />

W takiej sytuacji wszedłem w&nbsp;opcje Opery i&nbsp;paroma kliknięciami wyłączyłem całkowicie WebRTC. Kiedy to zrobiłem, to BrowserLeaks zaczął pokazywać, że wykrywa tylko szwedzkie IP i&nbsp;żadnego innego. Wyciek zatkany!

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/webrtc/vpn-bez-wycieku.jpg"  alt="Zrzut ekranu z&nbsp;Browserleaks. Pokazuje dwa adresy IP, przy nich szwedzkie flagi, a&nbsp;na dole informację o&nbsp;tym, że nie wykryto żadnego wycieku." />

Proste? Proste. A&nbsp;teraz pokażę, jak wyłączać WebRTC w&nbsp;różnych przeglądarkach. Gdy już to zrobicie, koniecznie sprawdźcie przez BrowserLeaks, czy wszystko jest jak na trzecim ekranie.

## Wyłączanie w&nbsp;przeglądarkach

### Chrome

Zacznę od najpopularniejszego Chrome'a, żeby mieć go z&nbsp;głowy.  
W jego przypadku stronka BrowserLeaks [radzi](https://browserleaks.com/webrtc#howto-disable-webrtc), żeby użyć oficjalnego dodatku od Google'a, [*WebRTC Network Limiter*](https://chrome.google.com/webstore/detail/webrtc-network-limiter/npeicpdbkakmehahjeeohfdhnlpdklia). To samo proponuje IPLeak.

Oznacza to jednak zależność od Wujka G, dla którego prywatność nie jest sprawą priorytetową. Sam dodatek miał w&nbsp;ostatnich latach czas, gdy [przez półtora roku nie działała ważna funkcja](https://bugs.chromium.org/p/chromium/issues/detail?id=1247217).

W związku z&nbsp;tym Ciemna Strona radzi, żeby Chrome'a w&nbsp;ogóle nie używać, chyba że do jednorazowych zadań :wink:

### Edge

Kolejna korpoprzeglądarka, tym razem od Microsoftu. Ale ponoć daje możliwość całkowitego wyłączenia WebRTC.

Trzeba wpisać w&nbsp;górny pasek przeglądarki `about:flags` i&nbsp;aktywować opcję `Ukrywaj mój lokalny adres IP podczas połączeń WebRTC`.

{:.post-meta}
Źródło: [TechRadar](https://www.techradar.com/vpn/webrtc-leaks), osobiście nie sprawdzałem.

### Opera

Trzeba:

* wpisać w&nbsp;górnym pasku przeglądarki `about:config`,
* kliknąć zakładkę `Zaawansowane` po lewej,
* następnie zakładkę `Prywatność i bezpieczeństwo`.
* przewinąć długą listę aż do rzeczy pod nagłówkiem `WebRTC`.

Są tam cztery opcje kontrolujące WebRTC. Najlepsza dla prywatności będzie ostatnia, `Disable non-proxied UDP` (przypomnę: *non-proxied*, czyli bez pośrednika; *UDP*, czyli protokół u&nbsp;podstaw WebRTC).

Całkowicie wyłączy ona funkcję WebRTC. A&nbsp;na stronce BrowserLeaks nie pokaże już prawdziwego IP.

### Vivaldi

A jak *w „Porach roku”*{:.corr-del} u&nbsp;Vivaldiego? Według ich forum -- [dość łatwo](https://forum.vivaldi.net/topic/85493/can-i-block-real-ip-leak-by-webrtc-in-the-browser-s-setting). Trzeba:

* wejść w&nbsp;ustawienia,
* kliknąć zakładkę `Prywatność i bezpieczeństwo`,
* znaleźć pstryczki pod nagłówkiem `Ochrona przed śledzeniem`,
* odznaczyć ten mówiący o&nbsp;transmitowaniu adresu IP dla lepszego działania WebRTC.

  {:.post-meta}
  Osobiście nie sprawdzałem, więc faktyczne polskie tłumaczenie może nieco się różnić; sens ten sam.

Warto zaznaczyć, że jeden z&nbsp;użytkowników pisze na forum, że mu to nie działa. Inni piszą, że działa.  
Możliwe, że ma jakąś nietypową konfigurację albo coś zamotał. W&nbsp;każdym razie, jak zawsze, warto sprawdzić efekt przez BrowserLeaks.

### Firefox

Tu poszło łatwo.

Musiałem wpisać w&nbsp;górny pasek adresów `about:config`. Wyskoczył komunikat mówiący, żebym zachował ostrożność. Niezbyt ze mną współgrał, ale napis `Akceptuję ryzyko` na przycisku pod nim -- już bardziej. Dlatego go kliknąłem.

Aktywował się pasek wyszukiwania. Zacząłem wpisywać w&nbsp;niego `media.peerconnection.enabled`. Kiedy pojawiła się opcja o&nbsp;tej nazwie, to dwukrotnie ją kliknąłem, żeby zmienić `true` na `false`. Gotowe!

### Tor Browser

Ta anonimizująca przeglądarka jest oparta na Firefoksie. Zaglądając w&nbsp;opcje, znalazłoby się to samo ustawienie co w&nbsp;punkcie wyżej, tyle że domyślnie *wyłączone*.  
Ale nawet jego włączenie nic by nie dało. Bo, według odpowiedzi twórców z&nbsp;2022 roku, [Tor Browser po prostu nie wspiera WebRTC](https://forum.torproject.org/t/enable-webrtc-in-tor-browser/2815). Z&nbsp;własnego wyboru. Jest zatem bezpieczny.

{% include info.html
type="Uwaga"
text="Warto pamiętać, że Tor jest pojęciem szerszym niż Tor Browser. Gdyby ktoś połączył się z&nbsp;siecią Tor, używając innej, zwyczajnej przeglądarki (da się tak), to nadal byłby narażony na wyciek przez WebRTC. Dlatego warto się trzymać Tor Browsera.  
Fajnie pokazuje to [film użytkownika AKM](https://www.youtube.com/watch?v=u4jF3TtkEao)."
%}

## Na różnych komunikatorach

Wideorozmowy przez WebRTC obsługują nie tylko przeglądarki, ale również wiele komunikatorów. W&nbsp;tym szyfrowanych, które nie mają wglądu do treści wiadomości.  
Przejście na *peer-to-peer* to dla nich oszczędność danych, więc chętnie parują w&nbsp;ten sposób użytkowników.

W przypadku komunikatorów **zagrożenie wydaje mi się mniejsze niż w&nbsp;przypadku stron internetowych**.

Podczas surfowania po sieci adres IP mogą demaskować podmioty zawodowo profilujące użytkowników.  
Obecne na wielu stronach. Gromadzące poza adresami również pliki *cookies* i&nbsp;inne dane, dokładniej mapujące wędrówki ludzi po sieci.

W porównaniu z&nbsp;tym zagrożeniem komunikatory mało mogą. Wspierając *peer-to-peer*, raczej nie mają złych intencji. Opcja nadużyć jest niewielka. A&nbsp;gdyby wszyscy korzystali z&nbsp;ich pośrednictwa, to by je dobili rachunkiem za serwery.

Tym niemniej fakt jest faktem. Podczas wideorozmowy *peer-to-peer* **telekom wyraźnie zobaczy, że dwa adresy IP wymieniają między sobą informacje**.

Co, jeśli oba adresy ma w&nbsp;swojej bazie? Bo to na przykład sieć Play, a&nbsp;rozmówcy to jej klienci?  
Może wówczas spojrzeć na osoby, do jakich są przypisane w&nbsp;danej chwili. I&nbsp;dostać na tacy: „Arek J. odbył siódmą wideorozmowę w&nbsp;tym tygodniu z&nbsp;Maćkiem H.”.

Dlatego, jeśli ktoś nie chce ujawnienia swoich powiązań, może z&nbsp;własnej woli wybrać pośrednictwo apki. Niektóre dają taką możliwość.

Aktualny stan rzeczy oraz porady dotyczące apek (tylko na iOS, nie wiem czy na Androidzie jest podobnie) można znaleźć w&nbsp;[artykule serwisu TechCrunch](https://techcrunch.com/2023/11/03/psa-chat-call-apps-reveal-ip-address/) sprzed paru dni. 

### Signal

To akurat sprawdziłem osobiście, na systemie Android 12.

Domyślnie „swatanie” jest włączone między osobami, które mają siebie nawzajem w&nbsp;kontaktach. W&nbsp;innych przypadkach wyłączone.

Jeśli ktoś chce, to może nakazać, żeby dane zawsze szły przez serwery Signala, nawet między kontaktami.  
W tym celu trzeba nacisnąć:

* ikonę trzech kropek w&nbsp;górnym prawym rogu,
* opcję `Ustawienia`,
* opcję `Prywatność`,
* opcję `Zaawansowane` (na samym dole),
* opcję `Zawsze przekazuj połączenia`.

### Telegram, Viber, Threema

Podobnie jak Signal, te komunikatory stosują *peer-to-peer* tylko między ludźmi, którzy mają siebie nawzajem w&nbsp;kontaktach. Czyli teoretycznie powinni sobie ufać.

Ale jeśli nie ufają infrastrukturze po drodze, to zawsze mogą wrócić do pośrednictwa serwerów.

Zdam się na porady z&nbsp;podlinkowanego wyżej artykułu TechCrunch oraz drugiego, o&nbsp;[Telegramie](https://techcrunch.com/2023/10/19/telegram-is-still-leaking-user-ip-addresses-to-contacts).  
Tłumaczenie moje, więc może nie zgadzać się co do litery. Ale sens powinien być zachowany.

* **Telegram**

  Ustawienia, potem `Prywatność i bezpieczeństwo`, `Połączenia` (ang. *Calls*), opcja `Nigdy` pod nagłówkiem „Peer to Peer”.

* **Viber**

  Trzy kropki, potem `Ustawienia`, `Prywatność`, odznaczamy `Peer-to-peer`.

* **Threema**

  `Ustawienia`, `Połączenia Threema` (ang. *Threema calls*), `Zawsze przekazuj połączenia` (ang. *Always Relay Calls*).

### WhatsApp, Messenger, FaceTime

Zarówno apki od Facebooka, jak i&nbsp;ta od Apple, nie dają użytkownikowi kontroli nad pośrednictwem. **Ujawniają adres IP i&nbsp;nie da się wyłączyć tej opcji**.

WhatsApp ponoć planuje to zmienić w&nbsp;bliższym czasie i&nbsp;dać możliwość wyłączenia połączeń *peer-to-peer*.  
W przypadku Messengera brak możliwości oficjalnie potwierdził rzecznik, zmian nie ma w&nbsp;planie.

Jeśli chodzi o&nbsp;Apple, nikt nie odpowiedział dziennikarzowi. Wyczytał za to ładne słówka o&nbsp;szyfrowaniu treści (które jest tu bez znaczenia, bo nie obejmuje IP).
