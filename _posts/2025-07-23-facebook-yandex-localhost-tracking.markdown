---
layout: post
title: "Afera localhost – aplikacje widziały, jakie strony przeglądasz"
subtitle: "List do twojej szuflady. Ale dla kogoś innego. A ciebie obgaduje."
description: "List do twojej szuflady. Ale dla kogoś innego. A ciebie obgaduje."
date:   2025-07-23 10:00:34 +0100
tags: [Apki, Internet, Inwigilacja]
firmy: [Facebook, Meta, Yandex]
image:
  path: /assets/posts/inwigilacja/localhost/localhost-tracking-baner.jpg
  width: 1200
  height: 700
  alt: "Przeróbka mema ze schematem podziemnej kryjówki Saddama Husajna. Jego leżący kontur jest oznaczony jako dane użytkowników. W górnej części obrazka dwie postacie z logami apek Facebook i Yanex zamiast głów zaczynają kopać."
---

W zeszłym miesiącu badacze cyberbezpieczeństwa zdemaskowali bardzo ciekawe sztuczki, dzięki którym paru cyfrowych gigantów gromadziło dane swoich użytkowników. 

Tożsamość winowajców nie jest zaskoczeniem. Koncern Meta wraz ze swoimi portalami, Facebookiem i&nbsp;Instagramem, to już niemal synonim naruszeń prywatności. Drugi sprawca, rosyjski Yandex, nie od dziś stara się zostać wschodnim Google'em -- tak pod względem wachlarza usług, jak i&nbsp;śledzenia ludzi.

Zaskakiwać może natomiast trik, jakiego użyły obie firmy, niezależnie od siebie. Sprawnie obeszły bariery stawiane przez system smartfonowy Android, wykorzystując *localhosta* -- wspólną przestrzeń dostępną dla różnych aplikacji. Trochę tak, jakby szpiedzy ukrywali listy do siebie w&nbsp;nieużywanych szafkach na pływalni. Niemal na widoku.

Stosując to obejście, firmy mogły **łączyć naszą tożsamość, znaną ich aplikacjom, z&nbsp;naszymi wędrówkami po sieci**. Mimo że odbywały się one wewnątrz zwykłych przeglądarek; niezależnych, a&nbsp;czasem wręcz trzymających stronę użytkowników.

W tym wpisie opiszę, przystępnie i&nbsp;krok po kroku, o&nbsp;co chodziło w&nbsp;całej tej *aferze localhostowej*. Pokażę również, że wystarczyłaby zmiana paru podstawowych ustawień i&nbsp;trzymanie się uniwersalnych zasad, żeby ochronić swoją prywatność.

{:.post-meta .bigspace-after}
Skupię się na Mecie, bo jej śledzenie dotyka znacznie więcej osób, zwłaszcza w&nbsp;naszym rejonie. Będę wprowadzał rozróżnienie między firmami tam, gdzie ich metody różniły się od siebie.

Zapraszam!

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/localhost/localhost-tracking-baner.jpg" alt="Przeróbka mema ze schematem podziemnej kryjówki Saddama Husajna. Jego leżący kontur jest oznaczony jako dane użytkowników. W&nbsp;górnej części obrazka dwie postacie z&nbsp;logami apek Facebook i&nbsp;Yanex zamiast głów zaczynają kopać."/>

{:.figcaption}
Źródła: mem o&nbsp;[kryjówce Saddama Husajna](https://knowyourmeme.com/editorials/guides/whats-up-with-memes-about-saddam-husseins-hiding-spot-red-silhouette-diagrams-explained) , mem o&nbsp;[dwóch kopaczach](https://knowyourmeme.com/memes/never-give-up-digging-for-diamonds). Przeróbki moje.

## Spis treści

* [Pliki cookies i&nbsp;klasyczne śledzenie](#pliki-cookies-iklasyczne-śledzenie)
  * [Kulturalne logowanie](#kulturalne-logowanie)
  * [Niekulturalne elementy śledzące](#niekulturalne-elementy-śledzące)
* [Aplikacje jako utrudnienie](#aplikacje-jako-utrudnienie)
* [Obejście barier](#obejście-barier)
  * [WebRTC – sposób wysłania](#webrtc--sposób-wysłania)
  * [Localhost – sposób odbioru](#localhost--sposób-odbioru)
  * [Łączenie danych](#łączenie-danych)
* [Konsekwencje](#konsekwencje)
* [Co pomoże, a&nbsp;co nie](#co-pomoże-aco-nie)

{% include info.html
type="Źródła"
text="Punktem wyjścia do wpisu była praca badaczy opisana na stronie [*localmess.github.io*](https://localmess.github.io/) (polecam! Ciut bardziej techniczne, ale nie jest tak źle. Szczególnym atutem jest interaktywna lista stron zawierających elementy śledzące od Facebooka).  
Drugim głównym źródłem było [omówienie ich badań ze strony *zeropartydata.es*](https://www.zeropartydata.es/p/localhost-tracking-explained-it-could), wraz z&nbsp;analizą potencjalnych kar, jakimi mógłby oberwać Facebook.  
Reszta to [dyskusje na forach](https://news.ycombinator.com/item?id=44235467) oraz wiedza własna, którą od dawna się dzielę na blogu. Będzie sporo linków do innych wpisów!"
%}

## Pliki cookies i&nbsp;klasyczne śledzenie

Cała sprawa dotyczyła **smartfonów z&nbsp;systemem Android**, nie dotknęła iPhone'ów ani komputerów osobistych.

W przypadku komputerów nie wynika to jednak z&nbsp;jakiejś ich odporności, lecz raczej z&nbsp;tego, że już są rozpracowane przez Metę i&nbsp;innych łapserdaków. Pozwolę sobie na początek opisać panującą na nich anarchię i&nbsp;przejść stopniowo do sytuacji na smartfonach, która wymaga od technogigantów pewnych forteli.

{:.post-meta .bigspace-after}
Jeśli ktoś już pewnie się czuje z&nbsp;wiedzą na temat *trackerów* i&nbsp;nie chce powtórki, to może [przeskoczyć do sedna](#aplikacje-jako-utrudnienie){:.internal}.

Kluczowa sprawa: na komputerach osobistych wiele rzeczy odbywa się zazwyczaj przez ogólną przeglądarkę, jak Firefox czy Opera. To wewnątrz niej ładuje się zarówno terytorium Mety (rozciągające się na domeny takie jak `instagram.com` czy `facebook.com`), jak i&nbsp;całe galaktyki niezależnych stron: portale informacyjne, katalogi przepisów czy kolekcje kocich zdjęć.

### Kulturalne logowanie

Załóżmy, że ktoś odwiedza po raz pierwszy stronę Facebooka. W&nbsp;takim przypadku Facebook poprosi o&nbsp;podanie maila i&nbsp;hasła. Gdy je podamy, to wyświetli się zawartość naszego konta na platformie.

Taki jest obraz widoczny na zewnątrz. Ale pod spodem wygląda to inaczej -- w&nbsp;chwili zalogowania przeglądarka otrzymała tzw. „ciasteczko”, czyli *plik cookie*. Krótki tekst, który w&nbsp;bazie danych Facebooka jest jednoznacznie przypisany do konkretnej osoby. Można powiedzieć poetycko, że to tożsamość zapisana w&nbsp;bajtach.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/localhost/fb-cookie-otrzymywanie-schemat.jpg" alt="Schemat pokazujący za pomocą strzałek interakcję między laptopem a&nbsp;Facebookiem. Laptop wysyła login i&nbsp;hasło, a&nbsp;Facebook odsyła ikonę symbolizującą plik cookie."/>

{:.figcaption}
Źródła: laptop i&nbsp;strzałki z&nbsp;serwisu Flaticon; oficjalne ikony Facebooka i&nbsp;przeglądarki Firefox. Przeróbki moje.

Po zapisaniu ciasteczka przeglądarka zmienia swoje zachowanie. Od teraz okazuje ten plik przy każdym kolejnym kontakcie ze stroną `facebook.com`, ujawniając kim jesteśmy.  
Dzięki temu nie musimy się każdorazowo logować. Od razu po załadowaniu strony widzimy znajomych, wydarzenia, nowinki ze świata -- ale częściej wygenerowane komputerowo bzdety -- dopasowane specjalnie do siebie.

{:.bigspace}
<img src="/assets/posts/inwigilacja/localhost/fb-cookie-korzystanie-schemat.jpg" alt="Kolejny schemat interakcji między laptopem a&nbsp;serwerem Facebooka. Obok laptopa widać ikonę ciasteczka. Wysyła on pytanie „co tam?” i&nbsp;otrzymuje od Facebooka odpowiedź „to tam”."/>

Na tym etapie ciasteczko wydaje się jeszcze praktyczne i&nbsp;sensowne, ułatwia życie.

{:.post-meta .bigspace-after}
Warto jednak zapamiętać, że w&nbsp;takich realiach nie istnieje coś takiego jak anonimowe logowanie; co jakiś czas ktoś się nacina na braku tej wiedzy.

Problem w&nbsp;tym, że przeglądarka okazuje ciasteczko przy *każdym* kontakcie ze stroną `facebook.com`. Również wówczas, gdy wcale nie odwiedzamy Facebooka, a&nbsp;jedynie trafiamy na mały, pochodzący od niego element gościnny na całkiem obcej stronie.

### Niekulturalne elementy śledzące

**Takie małe „posterunki” Facebooka również mogą odczytywać i&nbsp;zapisywać związane z&nbsp;nim ciasteczka**. Elementy nazywa się *trackerami*, zaś związane z&nbsp;nimi ciasteczka to [*third-party cookies*](/internetowa_inwigilacja/2021/12/08/cookies-piksele-sledzace){:.internal} (ciasteczka od stron zewnętrznych). A&nbsp;co robią w&nbsp;internecie? Właściciele stron nieraz sami je dodają, skuszeni możliwościami współpracy reklamowej albo ściślejszej integracji z&nbsp;*social mediami*.

Działanie *trackerów* w&nbsp;praktyce, krok po kroku:

* nasza przeglądarka (mająca w&nbsp;sobie zapisany plik cookie od Fejsa) prosi o&nbsp;jakąś stronę, całkiem od Facebooka niezależną;
* otrzymuje ją, zwykle jako plik HTML, i&nbsp;odczytuje jej treść;
* widzi, że strona jest jeszcze niekompletna, bo brakuje elementu od Facebooka, zwanego Facebook Pixel;
* prosi o&nbsp;ten element stronę `facebook.com`, załączając do prośby plik cookie, który nas identyfikuje.

  My otrzymujemy mały, niezbyt wartościowy dla nas element. W&nbsp;zamian Facebook dostaje informację, że konkretna osoba o&nbsp;danej porze odwiedziła stronę X. Być może portal ze zdjęciami kotów, a&nbsp;może (zmyśloną) `leczymy-weneryczne.pl`. Nie nazwałbym tej wymiany interesem życia :roll_eyes:

Wisienka na torcie? Sam element, wbrew nazwie Pixel, nie jest żadnym pikselem, lecz kolekcją różnych rzeczy, w&nbsp;tym skryptów w&nbsp;języku JavaScript. Mogą kazać naszemu urządzeniu robić różne rzeczy, pozyskiwać informacje i&nbsp;wysyłać je Facebookowi. Warto zapamiętać ten fakt, bo jeszcze odegra ważną rolę.

{:.post-meta .bigspace-after}
Elementy od Yandeksa działają na tej samej zasadzie, ale raczej rzadziej występują w&nbsp;światowej sieci i&nbsp;mają nieco mniej mylącą nazwę Yandex Metrica.

A tutaj, dla osób lubiących obrazki, schemat całego opisanego procesu:

{:.bigspace-before}
<img id="cookies-schemat" src="/assets/posts/inwigilacja/localhost/facebook-third-party-cookies.jpg" alt="Schemat pokazujący, za pomocą numerowanych strzałek, jak laptop najpierw pyta stronę o&nbsp;rysunek kota i&nbsp;otrzymuje w&nbsp;odpowiedzi miniaturkę strony internetowej. Czerwoną ramką zaznaczono na niej brakujący element Facebooka. Kolejne strzałki pokazują, jak laptop prosi o&nbsp;ten element samego Facebooka, wysyłając własne informacje."/>

{:.figcaption}
Źródła: serwer ze strony Flaticon, ikona kota z&nbsp;Emojipedii, reszta jak wcześniej. Przeróbki moje.

Ciasteczka od stron zewnętrznych to problem znany od dawna i&nbsp;poczyniono spore postępy w&nbsp;odchodzeniu od nich. Przeszkodą pozostaje Google, który nadal staje w&nbsp;ich obronie.  
...Ale nawet gdyby nikt od nich nie planował odchodzić, obecnie wiele firm mogłoby nie czerpać z&nbsp;nich takiej wartości jak kiedyś. Częściowo dlatego, że internet przejmują urządzenia mobilne, na których przeglądarka nie stanowi centrum świata.

## Aplikacje jako utrudnienie

Cała powyższa sytuacja to norma na komputerach osobistych, bo tam wszystko dzieje się w&nbsp;obrębie jednej przeglądarki. Jest jedna i&nbsp;ta sama przegródka na ciastka Mety, które są okazywane zarówno ich serwisom, jak i&nbsp;pomniejszym elementom-wartownikom na stronkach nienależących do firmy. 

...Ale **na smartfonach Meta ma utrudnione zadanie**. Z&nbsp;dwóch przyczyn:

1. Użytkownicy często korzystają z&nbsp;jej własnych aplikacji, jak Facebook czy Instagram, zamiast otwierać w&nbsp;przeglądarce `facebook.com` lub `instagram.com`.

   Wprawdzie wersje mobilne też są dostępne, np. pod adresem `m.facebook.com`, ale apka Facebooka bywa nieraz domyślnie zainstalowana na telefonie, do tego sama strona nakłania na apkę. Dlatego to ona zgarnia ludzi.  
   Ma to sens, bo aplikacja ma większy wgląd w&nbsp;system i&nbsp;dane użytkowników (w&nbsp;szczególności do listy kontaktów). Ale stawiając na to rozwiązanie, Facebook zamyka sobie inną opcję, o&nbsp;czym za sekundę.

2. Dane z&nbsp;przeglądarki są osłonięte podwójną barierą.

   Po pierwsze: zabezpieczenia samego systemu Android. Jego twórcy chyba się czegoś nauczyli z&nbsp;historii komputerów osobistych i&nbsp;tego, do czego prowadziły nieograniczone możliwości ingerowania jednych programów w&nbsp;drugie.

   Na Androidze każda apka ma własną, prywatną przestrzeń i&nbsp;nie może zaglądać do innych aplikacji. Możliwy powinien być tylko wgląd we wspólne przestrzenie. Ten podział to tak zwany *sandboxing*.

   Po drugie: przeglądarkom zależy na reputacji szczelnych, więc są ostrożne i&nbsp;m.in. unikają zapisywania plików do wspólnej przestrzeni. Nawet Chrome, szorujący po prywatnościowym dnie, przynajmniej dba o&nbsp;to, żeby tylko Google mógł żłopać informacje, a&nbsp;cudze apki były od nich odcięte.

Efekt? Nadal zachodzi pięć etapów ze wcześniejszego schematu. Tyle że **Meta nie dostaje ciasteczka-tożsamości w pakiecie z danymi stron internetowych**. Ciastka identyfikujące leżą jedynie wewnątrz ich apki (Facebooka lub Instagrama). Historie wędrówek po internecie gromadzą się zaś w&nbsp;przeglądarce, która nie zamierza ich wręczyć gigantowi.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/localhost/apki-piramida-facebook-cookies.jpg" alt="Schemat pokazujący dane z&nbsp;kilku stron zamknięte wewnątrz aplikacji-przeglądarki oraz ikonkę oznaczającą tożsamość zamkniętą w&nbsp;osobnej aplikacji Facebooka. Wspólną podstawą, na której stoją obie aplikacje, jest tu system Android." width="80%"/>

{:.figcaption}
Źródła: [pierścień](https://emojipedia.org/google/16.0-june-2025-update/ring) w&nbsp;wersji Google'a oraz [samochodzik](https://emojipedia.org/joypixels/9.0/automobile) w&nbsp;wersji JoyPixels z&nbsp;Emojipedii, reszta jak wcześniej.

Z punktu widzenia naszego korpo był to niekorzystny impas. Choć mieli inne metody (o&nbsp;nich niżej, w&nbsp;rozwijanej ciekawostce), nic nie pobiłoby unikalnego identyfikatora. Dlatego mocno szukali sposobu na powiązanie ze sobą obu źródeł danych.

{% include details.html summary="Jakie metody śledzenia pozostają Facebookowi (dla zainteresowanych)" %}

{:.bigspace-before}
Warto wiedzieć, że sytuacja, wbrew pozorom, wcale nie jest dla Mety/Facebooka taka beznadziejna. Opisana tu metoda przez *localhosta* mogła być dla nich najwygodniejsza, ale mają też inne sposoby na śledzenie ludzi.

Zacznę od rzeczy pewnych. Cała opisana wyżej rozdzielność między apką a&nbsp;przeglądarką ma zastosowanie tylko wtedy, gdy faktycznie korzystamy z&nbsp;przeglądarki. Brzmi banalnie? Ale Facebook **nabrał wiele osób, imitując przeglądarkę**.

Jeśli klikniemy link do jakiejś zewnętrznej strony wewnątrz jednej z&nbsp;aplikacji Mety (Facebook albo Messenger; Instagrama i&nbsp;WhatsAppa nie sprawdzałem), to tak naprawdę nie opuszczamy ich terenu. To, co się otwiera, ma wprawdzie górny pasek z&nbsp;adresem i&nbsp;wygląd zwykłej przeglądarki, ale jest jedynie [imitacją wbudowaną w&nbsp;Facebooka/Messengera](/apki/2023/08/08/wbudowane-przegladarki){:.internal}. Pozostając w&nbsp;niej, pozostajemy na oku Mety.

{% include info.html type="Ciekawostka"
text="Swoją drogą linki z Facebooka nie są bezpieczne również w&nbsp;standardowej przeglądarce. W&nbsp;chwili kliknięcia są dyskretnie [podmieniane na przekierowania](/facebook_dane/2025/01/12/facebook-link-shimming){:.internal}.  
Kiedy je klikamy, to nie trafiamy prosto na stronę docelowej, tylko przechodzimy najpierw przez „śluzę” -- małą stronkę między terytorium Facebooka a&nbsp;zewnętrznym internetem. Platforma widzi, dokąd idziemy i&nbsp;może to sobie zapisywać. Zaś z&nbsp;parametrów, czyli tekstu dodawanego do linków, może odczytać jeszcze więcej informacji, niż ujawniałby sam link."
%}

A co z&nbsp;rzeczami, które niekoniecznie są dla Facebooka kluczowe, ale *mogłyby* im ułatwić identyfikację?

Przede wszystkim mają do dyspozycji [adres IP](/internetowa_inwigilacja/2021/06/11/adres-ip){:.internal}, siłą rzeczy otrzymywany przez strony Facebooka podczas każdej interakcji. Pozwala on (zwłaszcza w&nbsp;krótszym okresie) trafnie łączyć aktywność internetową z&nbsp;aplikacjową.  
„Z tego adresu odwiedziła nas Barbara P. Kilka minut później ten sam adres aktywował naszego *trackera* na stronie `koty-nieloty.pl` (zmyśliłem). Hipoteza: to Barbara P. odwiedziła stronę”.

Adres ma jednak różne swoje słabości. Jeśli jest nadawany przez sieć mobilną, to co pewien czas się zmienia. Może go również współdzielić wiele osób -- przykładem router w&nbsp;rodzinnym mieszkaniu albo publiczny hotspot. No i&nbsp;ktoś może celowo użyć pośrednika, takiego jak VPN, żeby ten adres zamaskować. Nie dziwota, że Facebook wolał pewniejszy sposób&nbsp;identyfikacji.

Inną metodą jest profilowanie, czyli [*fingerprinting*](/internetowa_inwigilacja/2022/06/10/fingerprinting){:.internal}. Jak pokazuje wcześniejszy [schemat](#cookies-schemat){:.internal}, elementy od Facebooka mogą w&nbsp;kroku 5&nbsp;uruchamiać kod JavaScript. A&nbsp;za jego pomocą można odczytać bardzo szczegółowe informacje na temat systemu, a&nbsp;nawet sprzętu fizycznego (zainstalowane czcionki, możliwości karty graficznej, charakterystyczny wygląd pikseli po rysowaniu wskazanych elementów...).

Takie informacje mogą umożliwić jednoznaczną identyfikację urządzenia. Apka Facebooka wykonuje jedno profilowanie, zaś elementy na stronach zewnętrznych -- kolejne. Jeśli wyniki się pokryją, to mogą przyjąć, że rozpoznali konkretną osobę. Wadą metody może być jej inwazyjność, spowalniająca nieco urządzenia i&nbsp;czyniąca metodę względnie łatwą do wykrycia, zwłaszcza dla badaczy. Ale pokusa może być silniejsza.

W każdym razie dwie metody wyżej to gdybanie. Czas wrócić do pewniaka, czyli naszego *localhosta*.

{% include details-end.html %}

## Obejście barier

Podsumujmy sobie to, co dotychczas wiemy. Facebook ma:

* jedną lub więcej aplikacji, w&nbsp;całości pod swoją kontrolą, zawierających czyjąś tożsamość;
* swój mały element załadowany w&nbsp;przeglądarce, który może z&nbsp;nią rozmawiać i&nbsp;ma dane na temat aktywności na stronie;
* barierę między tymi dwoma światami, którą chciałby przekroczyć.

Żeby nie było nudno i&nbsp;technicznie, spróbujmy się wczuć w&nbsp;Facebooka. A&nbsp;konkretniej -- w&nbsp;jakiegoś (zmyślonego, fikcyjnego) klepacza kodu zatrudnionego w&nbsp;tej firmie.  
Być może menedżer kazał mu znaleźć sposób na powiązanie aktywności internetowej z&nbsp;apką. Oczywiście wątpię, żeby w&nbsp;rozmowie użył słowa „śledzenie”. Prędzej frazesu w&nbsp;stylu „*bridge app and website experiences*”. Bo w&nbsp;końcu w&nbsp;korporealiach zawsze są „przeżycia”, rzadziej konkrety.

I teraz ten biedny pracownik stuka w&nbsp;klawiaturę, jak w&nbsp;[perkusję z&nbsp;filmu *Whiplash*](https://www.youtube.com/watch?v=LCSN7WwV534) (uwaga: YouTube), wyobrażając sobie w&nbsp;głowie, że właśnie dąży do perfekcji i&nbsp;Czyni Dobro™. Buduje rzeczy wielkie. Rozwój, postęp. Postęp, rozwój.  
„Uczestnicy chcą być widziani. Chcą czuć nas przy sobie. A&nbsp;te złe bariery nas od nich dzielą!”. Czy takie coś słyszy w&nbsp;swojej głowie?

{:.post-meta .bigspace-after}
Dodatkowo może go motywować fakt, że w&nbsp;razie niepowodzenia straci wizę pracowniczą i&nbsp;Ameryczka odeśle go do kraju urodzenia, wróci stara bida. Ale nie będę psuł przyziemnością górnolotnej motywacji.

Pracownik myśli, główkuje. Jakie są punkty wspólne między aplikacjami na systemie Android? Jak mogą ze sobą rozmawiać?

Pomysł 1: można zapisać jakiś tekstowy identyfikator przez przeglądarkę we wspólnej przestrzeni smartfona. Potem aplikacje od Mety mogłyby go odczytać.
  
Owszem, można. Tylko że przy próbie zapisu w&nbsp;przeglądarce wyświetli się wtedy okno wprost pytające użytkownika, czy chce coś pobrać z&nbsp;sieci. Takie jak np. przy pobieraniu PDF-a. I&nbsp;takie coś działoby się często. Zero szans na dyskrecję, odpada.

Pomysł 2: schowek (znany jako „kopiuj-wklej”). Strona internetowa skopiuje do niego dane, a&nbsp;apka Facebooka je odczyta.

Tylko że to by, po pierwsze, nadpisywało dane użytkowników już obecne w&nbsp;schowku, wywołując chaos. Po drugie: nie byłoby dyskrecji, bo Android wyświetla systemowy komunikat, gdy apka sięga po dane ze schowka. Ten pomysł też odpadał.

Zdesperowany pracownik oblewa się zimnym potem. Już widzi w&nbsp;wyobraźni, jak menedżer nazywa go *non-performant* i&nbsp;wyznacza mu za karę *obóz reedukacyjny*{:.corr-del} *Performance Improvement Plan*. Zdalnie, bezdusznie, podczas wideokonferencji.

...I w&nbsp;tym momencie doznaje olśnienia. Wideokonferencja. I&nbsp;obsługujący ją protokół, **WebRTC**.

### WebRTC – sposób wysłania

WebRTC ma parę ogromnych zalet z&nbsp;punktu widzenia śledzenia.  
Działa w&nbsp;tle, w&nbsp;sposób niewidoczny dla użytkowników. Pozwala nawiązać bezpośredni kontakt z&nbsp;dowolnym adresem. Może go uruchomić każdy element stron internetowych, który wykorzystuje kod JavaScript.

A ten kod jest wszechobecny i&nbsp;nawet wspomniane już Pixele, małe elementy gościnne od Mety, mogą go używać. Jak coś odsyłam do [schematu](#cookies-schemat){:.internal} z&nbsp;plikami cookies. *Chanel*{:.corr-del} Strzałka numer 5.

Protokół WebRTC to bestia złożona i&nbsp;pełna niuansów, właściwie cały parasol pomniejszych protokołów. Zainteresowane osoby znajdą więcej na stronce [*webrtcHacks*](https://webrtchacks.com/). Moja znajomość WebRTC jest gorzej niż pobieżna... Ale hej! I&nbsp;tak się wypowiem, bo w&nbsp;naszej historii protokół został użyty w&nbsp;równie pobieżny sposób.

Nikomu ze śledzących nie zależy na pełnoprawnej komunikacji. WebRTC w&nbsp;tym wypadku ma być tylko pretekstem, żeby wysłać dane. Wykorzystany zostaje jedynie jeden z&nbsp;prostszych protokołów z&nbsp;parasola, **SDP (_Session Description Protocol_)**, służący do wynegocjowania między dwoma urządzeniami sposobu komunikacji.

{:.post-meta .bigspace-after}
Samo zapoznawanie ze sobą dwóch urządzeń miałem już okazję opisać, nazywając je swataniem. Pokazałem też ciemną stronę takiego swatania -- złe strony mogą udawać, że chcą rozpocząć połączenie przez WebRTC, żeby [dorwać nasz prawdziwy adres IP](/internetowa_inwigilacja/2023/11/05/webrtc){:.internal}.

W ramach SDP wysyłanych jest [sporo różnych informacji](https://dyte.io/blog/webrtc-sdp-internals/). Jedna z&nbsp;nich nazywa się `ice-ufrag` i&nbsp;powinna zawierać nazwę użytkownika. Zamiast niej Facebook Pixel upychał tu identyfikator tymczasowy użytkownika, nazwany `_fbp` (nazwa całkowicie dowolna, wybrana przez twórców).  
Upychanie to nazywa się oficjalnie *SDP munging* i&nbsp;polega na bezpośrednim edytowaniu informacji związanych z&nbsp;SDP, tuż przed ich wysłaniem (ogólnie za WebRTC odpowiada przeglądarka, a&nbsp;skrypty mają ograniczoną kontrolę, ale na początku mogą trochę gmerać).

{% include info.html
type="Analogia"
text="SDP z&nbsp;założenia jest trochę jak napisanie komuś na komunikatorze: „może przejdziemy z&nbsp;tym na maila? Mój adres to `romek@zmyslona-strona.pl`, możesz tam załączyć obrazki”. Taka próba utworzenia nowego kanału komunikacji, opis jego możliwości.  
*SDP munging* w&nbsp;wydaniu Mety byłby natomiast jak nadużycie tego formatu rozmowy i&nbsp;podanie, zamiast swojej nazwy użytkownika, pseudonimu jakiegoś nieszczęśnika odwiedzającego sklep internetowy: „mój adres to `uzytkownik-strony-xyz-19821370@zmyslona-strona.pl`”."
%}

Pierwsza trudność (*jak* wysłać niepostrzeżenie dane użytkownika) została rozwiązana. Pozostała kolejna: *dokąd* to wysłać? Trzeba było wskazać jakieś miejsce docelowe, żeby WebRTC zadziałało.

### Localhost – sposób odbioru

Wcześniej zmyśliłem sobie biednego pracownika, który wpadł na pomysł wysłania danych przez WebRTC, kojarząc z&nbsp;tym słowo „wideokonferencja”. W&nbsp;podobny sposób mógłby wpaść na pomysł ich odebrania przez **interfejs _localhost_**, przypominając sobie, jak to swego czasu aplikacja konferencyjna *Zoom* [dość kreatywnie go (nad-)użyła](https://www.theverge.com/2019/7/10/20689644/apple-zoom-web-server-automatic-removal-silent-update-webcam-vulnerability).

...A czym właściwie jest *localhost*?

Najpierw wyobraźmy sobie interfejs sieciowy, czyli miejsce, z&nbsp;którego wysyła się i&nbsp;odbiera rzeczy wymieniane z&nbsp;szerszym światem. To taki **wielki paczkomat -- rząd szafek, z&nbsp;których każda ma własny numer i&nbsp;jest nazywana _portem_**.

{:.post-meta}
„Paczkomat” z&nbsp;małej, bo traktuję to jak rzeczownik powszechny -- inaczej, niż by chcieli [prawnicy InPostu](https://obserwatorlogistyczny.pl/2024/03/11/odmiana-paczkomat-inpost-zakazana-jak-teraz-musimy-mowic/) :smiling_imp:

{% include info.html
type="Ciekawostka"
text="Szafek możliwych do wykorzystania jest bardzo wiele. Dokładniej rzecz biorąc: zazwyczaj [65 536](https://stackoverflow.com/questions/24174795/how-many-ports-does-a-mobile-os-have). Ta liczba, choć wydaje się z&nbsp;czapy, nie jest przypadkowa. Dokładnie tyle możliwości da się wyrazić w&nbsp;16 bitach (gdzie każdy bit to jedno zero albo jedynka), a&nbsp;kiedyś umownie przyjęto za numer portu liczbę 16-bitową. I&nbsp;tak w&nbsp;wielu systemach zostało do dziś."
%}

Niektóre szafki/porty są używane bardzo często, inne rzadko. Przykładowo port numer 443&nbsp;obsługuje ruch przez HTTPS, czyli większość aktywności związanej z&nbsp;surfowaniem po sieci. Wiele innych portów jest z&nbsp;kolei nieużywanych.

Dokładna kopia tego paczkomatu, przeznaczonego do kontaktu ze światem, stoi również wewnątrz systemu. Jest przeznaczona **wyłącznie do użytku wewnętrznego**. Na przykład symulowania na własnym urządzeniu działania serwera. I&nbsp;takim właśnie wewnętrznym paczkomatem jest bohater afery, *localhost*. 

{:.post-meta .bigspace-after}
Nie jest to żadna egzotyka. Sam na przykład każdorazowo czytam wpis z&nbsp;bloga przez *localhosta*, żeby móc wiernie ocenić jego wygląd przed publikacją. Tym niemniej zaskoczyło mnie, że na Androidzie tak wiele aplikacji mogło tutaj sięgnąć.

Żeby coś wysłać do *localhosta*, wystarczy wskazać jako cel specjalny adres IP, `127.0.0.1`. Zawsze odnosi się on do aktywnego urządzenia, a&nbsp;nie czegoś zewnętrznego. Oprócz adresu należy wskazać port docelowy (numer szafki).

Oba wścibinosy, Meta i&nbsp;Yandex, kazały swoim aplikacjom *nasłuchiwać* portów dużo rzadziej odwiedzanych. Meta upodobała sobie porty o&nbsp;numerach 12387, 12388&nbsp;oraz zakres od 12580&nbsp;do 12585. Yandex wybrał numery 29009, 29010, 30102&nbsp;i 30103.  
Można powiedzieć, że firmowe aplikacje co pewien czas otwierały szafki o&nbsp;odpowiednich numerach i&nbsp;patrzyły, czy w&nbsp;środku znajdują się jakieś nowe informacje.

### Łączenie danych

Dzięki localhostowi Facebook i&nbsp;Yandex zyskały możliwość komunikacji między swoim elementem śledzącym a&nbsp;kontrolowanymi przez siebie aplikacjami. Do tego  zarówno elementy ze stron, jak i&nbsp;aplikacje, mogły swobodnie kontaktować się z&nbsp;serwerami firmy.

W takich warunkach łączenie danych w&nbsp;jeden profil stało się formalnością. Metody przyjęte przez obie firmy minimalnie się od siebie różniły, ale trzon działania był ten sam.

W przypadku Mety:

* Po krótkiej sesji siedzenia w&nbsp;apce użytkownik z&nbsp;niej wychodzi; apka przechodzi w&nbsp;tryb działania w&nbsp;tle i&nbsp;obserwuje interesujące ją porty *localhosta*.
* Użytkownik odwiedza w&nbsp;przeglądarce stronę zawierającą element od Facebooka. Ten go nie poznaje, więc przypisuje mu „pseudonim” -- identyfikator tymczasowy.
* Pseudonim, wzbogacony o&nbsp;informacje na temat odwiedzonej strony, etapu zakupów itd., wysyła Mecie (`pseudonim = aktywność-na-stronie`).
* Ten sam pseudonim, ale bez dodatkowych danych, śle w&nbsp;opisany już sposób do *localhosta*.
* Czuwająca tam aplikacja odbiera pseudonim i&nbsp;przypisuje go do tożsamości zapisanej w&nbsp;swoim wnętrzu (`pseudonim = tożsamość`). Wysyła to powiązanie Mecie.
* Na serwerach Mety następuje łączenie danych w&nbsp;ostateczną postać, znacznie bardziej użyteczną dla cybergiganta:   `tożsamość = aktywność-na-stronie`.

Yandex podszedł do sprawy nieco inaczej. Być może dlatego, że nie miał takiej popularności w&nbsp;sieci jak Meta, więc tożsamość odczytana z&nbsp;jego własnych aplikacji nie byłaby tak uniwersalnym, globalnym identyfikatorem jak inne opcje.

Zamiast czerpać `tożsamość` z&nbsp;wnętrza własnych aplikacji, sięgali do **identyfikatora reklamowego wbudowanego w&nbsp;smartfony**. Google domyślnie umieszcza to dziadostwo na typowych smartfonach z&nbsp;Androidem. Każda aplikacja może o&nbsp;nie zapytać i&nbsp;dostaje w&nbsp;odpowiedzi ciąg znaków, który powinien odpowiadać konkretnemu urządzeniu.

Następnie wysyłali ID reklamowe swojemu elementowi śledzącemu, który wciąż miał aktywną komunikację przez WebRTC. Element odczytywał je, tworzył komplet `unikalne-ID = aktywność-na-stronie` i&nbsp;wysyłał do Yandeksa.

Streszczając: w&nbsp;przypadku Yandeksa komunikacja przez WebRTC była dwustronna, w&nbsp;roli tożsamości używano identyfikatora reklamowego, a&nbsp;wysyłanie danych na serwery Yandeksa należało wyłącznie do elementów śledzących ze stronek internetowych. Ale ogólna koncepcja obchodzenia ograniczeń przez *localhosta* była taka sama.

## Konsekwencje

Facebook i&nbsp;Yandex nie mają wymówek. To nie jakaś drobna zmiana czy wyciek informacji, który dałoby się usprawiedliwiać gafą. Działali celowo, obchodząc zabezpieczenia, zostali złapani na gorącym uczynku.

Obie firmy tuż po wykryciu szybko przestały korzystać ze swojego triku. Teraz będą czekały na kary. Sprawa wywołała również techniczne dyskusje nad uszczelnieniem dostępu do *localhosta*. Możliwe, że dostęp do niego będzie np. wymagał udzielenia zgody przez użytkowników. W&nbsp;każdym razie metoda raczej przestanie być dyskretna.

W związku z&nbsp;całą sytuacją przeciwko Mecie w&nbsp;USA złożono [pozew zbiorowy](https://ia800708.us.archive.org/29/items/gov.uscourts.cand.450524/gov.uscourts.cand.450524.1.0.pdf), którego twarzą jest Devin Rose z&nbsp;Kalifornii (w&nbsp;której obowiązują ściślejsze przepisy chroniące prywatność, bliższe poziomowi unijnemu).

Szczególne możliwości ma jednak Unia Europejska. Jak analizuje autor strony *zeropartydata.es*, Meta mogłaby [oberwać skumulowanym efektem kilku różnych kar](https://www.zeropartydata.es/p/localhost-tracking-explained-it-could) -- związanych z&nbsp;przepisami GDPR (w&nbsp;Polsce znanymi jako RODO), *Digital Markets Act* oraz *Digital Services Act*.

Przepisy te nie opierają się na stałych kwotach, lecz na procencie od przychodów. Autor wylicza, że **Facebook mógłby oberwać teoretyczną karą do 32&nbsp;mld dolarów**.

{:.post-meta .bigspace-after}
Od razu zaznaczę, że nie znam przepisów na tyle, żeby wiedzieć czy to realne; ale autor podaje źródła, a&nbsp;jego stwierdzenia na temat przepisów są zbieżne z&nbsp;tym, co sam o&nbsp;nich wyczytałem. Dlatego daję jego słowom kredyt zaufania, choć wątpię w&nbsp;pełen wymiar kary.

Mam nadzieję, że wreszcie się doigrają, bo z&nbsp;ich strony naruszanie prywatności to już regularna recydywa. Zaś w&nbsp;międzyczasie, zamiast czekać na prawodawców, można wziąć sprawy we własne ręce.

## Co pomoże, a&nbsp;co nie

Metoda z&nbsp;tego wpisu nie tylko pozwala łączyć światy apek i&nbsp;przeglądarek, które od początku powinny być rozłączne, ale również **obchodzi kilka najprostszych (i&nbsp;przez to najpopularniejszych) sposobów na ochronę prywatności**.

Korzystasz z&nbsp;pośrednika, takiego jak VPN? Może cię to nie chronić.  
Prośba o&nbsp;zainicjowanie WebRTC po prostu sobie przejdzie przez cały łańcuszek pośredników, a&nbsp;twoje dane trafią do odpowiedniej przegródki *localhosta*. Stamtąd odbierze je nasłuchująca apka, połączy z&nbsp;tożsamością i&nbsp;wyśle swoim twórcom.

Często usuwasz pliki *cookies*? Dobry zwyczaj, często pomaga. Ale nie w&nbsp;tym wypadku.  
Ciasteczko identyfikujące tkwi wewnątrz apki Facebooka (albo uprzywilejowanych Usług Google'a, jeśli to ID reklamowe używane przez Yandeksa). Żadne czyszczenie przeglądarki nie ma na nie wpływu.

Na czas wrażliwszego wyszukiwania korzystasz z&nbsp;innej przeglądarki? Na przykład używasz Firefoksa zamiast swojej codziennej Opery?  
Dobry zwyczaj. Ale tutaj, o&nbsp;ile któraś z&nbsp;przeglądarek A&nbsp;i B&nbsp;nie jest dodatkowo zabezpieczona, dane z&nbsp;nich tak czy siak trafią do wspólnej szafki w&nbsp;*localhoście*. Stamtąd odbierze je apka i&nbsp;przypisze do konkretnego profilu.

### Promyk nadziei

Sprawa z&nbsp;nadużywaniem *localhosta* może być kubłem zimnej wody i&nbsp;sugerować, że giganci zawsze przechytrzą starania o&nbsp;szczyptę prywatności. To woda na młyn defetystów piszących lekceważąco, że „prywatność już nie istnieje, czas się poddać”.

Proponuję jednak spojrzeć na to inaczej. Ten wyciek istotnie był unikalny i&nbsp;nieco zniuansowany, ale możliwy jedynie dzięki splotowi kilku czynników. Gdyby choć jeden z&nbsp;nich nie zachodził, to Facebook i&nbsp;Yandex nie miałyby możliwości zebrania danych.

Oto lista rzeczy (nieraz bardzo szybkich i&nbsp;łatwych), dzięki którym cała metoda śledzenia straciłaby rację bytu. Ułożyłem je od najistotniejszych do pobocznych.

* Korzystanie z&nbsp;**dodatku blokującego śledzenie**, takiego jak uBlock Origin (albo z&nbsp;przeglądarki z&nbsp;wbudowanym blokerem).

  Rozwiązanie kwestii elementów śledzących na logikę wydaje się proste. „Kiedy jestem na stronie, która nie jest Facebookiem, to nie chcę mu niczego wysyłać”. I&nbsp;taką regułę wdrażają dodatki blokujące, z&nbsp;których w&nbsp;szczególności polecam [uBlock Origin](/2021/10/21/ublock-origin){:.internal}. Skuteczny, darmowy, o&nbsp;otwartym kodzie źródłowym. Już nieraz o&nbsp;nim pisałem na blogu.

  Bloker w&nbsp;ogóle nie pobierałby elementów śledzących od Facebooka, dzięki czemu platforma nie dostałaby żadnych, nawet najprostszych informacji o&nbsp;użytkownikach (w&nbsp;ogóle nie zaszłyby etapy 3-5 z&nbsp;początkowego [schematu](#cookies-schemat){:.internal}).
  
  Niestety nie każda przeglądarka mobilna daje możliwość instalowania dodatków. Żeby cieszyć się mocami uBO, należy zainstalować mobilnego Firefoksa.  
  Inną opcją jest mobilna przeglądarka Brave. Nie ma uBO, ale zawiera własnego, wbudowanego blokera reklam -- o&nbsp;mniejszych możliwościach, ale działającego z&nbsp;miejsca.

  {:.post-meta .bigspace-after}
  Przeglądarek stawiających na prywatność jest więcej -- choćby DuckDuckGo Browser czy Mullvad Browser -- ale nie miałem okazji ich dokładniej przetestować. Polecam to, co sam sprawdziłem.

* [Wyłączenie ID reklamowego](/2025/03/23/gravy-analytics-wyciek#usuwanie-id-reklamowego){:.internal}

  Ten krok **pomógłby w&nbsp;przypadku Yandeksa, ale nie Facebooka**. Ale ogólnie to rzecz tak prosta i&nbsp;pozbawiona efektów ubocznych, że polecam ją absolutnie wszystkim. Dałaby ochronę przed wieloma innymi nadużyciami, jak choćby afera Gravy Analytics opisana w&nbsp;podlinkowanym wpisie.

* [Wyłączenie kodu JavaScript](/internetowa_inwigilacja/2022/05/03/javascript2#ca%C5%82kowite-wy%C5%82%C4%85czenie-javascriptu){:.internal} na stronach internetowych.
 
  Bez niego w&nbsp;ogóle by nie zadziałał etap 5&nbsp;z pierwotnego [schematu](#cookies-schemat){:.internal}. Czyli w&nbsp;przypadku elementów od Mety i&nbsp;Yandeksa: włączenie WebRTC i&nbsp;wysłanie danych.

  To metoda nie dla każdego, bo od JS-a zależy działanie wielu stron internetowych, zwłaszcza większych. Niektóre osoby stykają się z takimi stronami często, inne rzadziej.  
  Moja sugestia? Zainstalować na mobilnym Firefoksie uBO, który i&nbsp;tak by się przydał. Na próbę wyłączyć JS-a w&nbsp;jego opcjach i&nbsp;w razie czego reaktywować go paroma kliknięciami na kłopotliwych stronach. Ocenić, czy rozwiązanie nam pasuje.
  
* [Wyłączenie WebRTC](/tutorials/webrtc-wylaczenie){:.internal} w&nbsp;przeglądarce.

  Na każdej działa to nieco inaczej, więc zachęcam do zerknięcia w&nbsp;link. Uprzedzam, że po zablokowaniu nie będą działały niektóre programydo wideokonferencji, więc warto sobie zapisać sposób na odblokowanie.  
  W&nbsp;przeglądarce anonimizującej Tor Browser ta funkcja jest domyślnie wyłączona, dzięki czemu domyślnie chroni użytkowników przed powiązaniem tożsamości -- nie trzeba uruchamiać dodatkowych funkcji, jak blokada JavaScriptu, mimo że też by pomogły. Tylko pozazdrościć twórcom intuicji do wykrywania zagrożeń :wink:

* Wyłączanie aplikacji, kiedy z&nbsp;nich nie korzystamy 

  Nieraz widziałem, jak ktoś pyta w&nbsp;sieci o&nbsp;sposób na *pełne* wyłączenie aplikacji, żeby nie zjadały baterii. Inni odpisywali często, że to bzdet, że Android sam dobrze zarządza pamięcią.  
  ...A teraz się okazuje, że osoby ubijające aplikacje byłyby lepiej chronione. Nie działając w&nbsp;tle, apki nie są w&nbsp;stanie warować przy portach. Jakie to życie przewrotne :wink:  
  Aby wyłączyć konkretną aplikację, można wejść w&nbsp;`Ustawienia`, potem `Aplikacje`, wybrać ją z&nbsp;listy i&nbsp;kliknąć opcję `Wymuś zatrzymanie`. Pojawi się ostrzeżenie, proponuję zignorować.

Proponuję, żebyśmy z&nbsp;całej sytuacji wynieśli taką lekcję: ochrona prywatności jest wprawdzie pełna niuansów i&nbsp;stale wypływają nowe zagrożenia, ale **zadbanie o&nbsp;parę prywatnościowych podstaw konsekwentnie chroni tyłek**.

Tu i&nbsp;teraz zmień swój świat. Wyłącz ID reklamowe (zajmnie to mniej niż minutę). Zainstaluj Firefoksa, na nim zainstaluj uBlock Origin (kilka minut plus czas na pobranie). Nie musisz od razu przeskakiwać na ten zestaw, możesz się z&nbsp;nim stopniowo oswajać. Wszystkie instrukcje w&nbsp;linkach wyżej.

Te proste zmiany wystarczą, żeby zrobić symboliczny krok ku niezależności i&nbsp;odejść od świata, w&nbsp;którym jest się strzyżonym na łyso przez różnych chytrusów. I&nbsp;takiego lepszego świata nam życzę! :smile:
