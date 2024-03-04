---
layout: post
title: "Odbijanie smartfona z rąk Google'a – aplikacje"
subtitle: "Zamienniki lepsze niż oryginały!"
description: "Zamienniki lepsze niż oryginały!"
date:   2024-02-19 10:00:00 +0100
tags: [Android, Centralizacja, Inwigilacja, Open Source, Porady]
firmy: [Google, Motorola]
image:
  path: /assets/posts/google/smartfon-degoogle-apki/degoogle-aplikacje-baner.jpg
  width: 1200
  height: 700
  alt: "Dwa masywne, humanoidalne duchy z anime Jojo's Bizarre Adventure okładają się pięściami. Na twarz i pięści jednego z nich nałożono ikony aplikacji firmy Google, a na pięści drugiego ikony niezależnych aplikacji"
---

Witam w&nbsp;drugim wpisie na temat uwalniania od Google'a smartfonów z&nbsp;systemem Android!

Przypomnę kontekst: po dłuższym korzystaniu z&nbsp;Huaweia miałem okazję poznać Motorolę G22. Nieco się przeraziłem tym, jak mocno ten smartfon był zżyty ze śledzącymi aplikacjami korporacji Google. Ale stopniowo go uwalniałem od badziewia, a&nbsp;swoje doświadczenia przekułem w&nbsp;poradnik.

[Poprzedni wpis](/2024/02/03/smartfon-degoogle){:.internal} dotyczył ustawień ogólnych, systemowych. Pokazałem, w&nbsp;jaki sposób przez odrobinę grzebania w&nbsp;opcjach osłabić aplikacje Google'a albo je wyłączyć. Bo usunąć nie zawsze się dało.

Problem w&nbsp;tym, że Wujek G&nbsp;trzyma łapy na wielu rzeczach. Nawet na zegarze czy apce od dzwonienia. Gdyby tak po prostu zneutralizować w&nbsp;ciemno rzeczy od niego, to by się zostało bez sprawnych aplikacji.

Żeby po odgooglowaniu zachować możliwości smartfona, trzeba zainstalować zamienniki.  
Temu właśnie poświęcam ten wpis. Pokażę **alternatywy dla aplikacji Google'a**. Proste w&nbsp;obsłudze, a&nbsp;czasem zostawiające te domyślne daleko w&nbsp;tyle.

{:.bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle-apki/degoogle-aplikacje-baner.jpg" alt="Dwie masywne, humanoidalne postacie z&nbsp;anime Jojo's Bizarre Adventure okładające się pięściami. Na twarz i&nbsp;pięści jednego z&nbsp;nich nałożono ikony aplikacji Google, a&nbsp;na pięści drugiego ikony kilku aplikacji niezależnych. Nad nimi widać czerwony napis Fight (po angielsku: walka)."/>

{:.figcaption}
Źródło: anime *Jojo's Bizarre Adventure: Stardust Crusaders*. Napis z&nbsp;dawnego [*Mortal Kombat*](https://www.gog.com/blog/finish-him-experience-the-classic-mortal-kombat-games-once-more/).

## Spis treści

* [Blaski i&nbsp;cienie Play Store'a](#blaski-icienie-play-storea)
  * [Na czym polega instalowanie aplikacji](#na-czym-polega-instalowanie-aplikacji)
  * [Alternatywne źródła](#alternatywne-źródła)
  * [Plan działania](#plan-działania)
  * [Wyłączenie Play Protect](#wyłączenie-play-protect)
* [Przeglądarka internetowa – Firefox](#przeglądarka-internetowa--firefox)
  * [Zmiana wyszukiwarki na DuckDuckGo](#zmiana-wyszukiwarki-na-duckduckgo)
  * [Dodatek uBlock Origin](#dodatek-ublock-origin)
* [Podstawowe aplikacje](#podstawowe-aplikacje)
  * [Ciemna strona drobnych aplikacji](#ciemna-strona-drobnych-aplikacji)
  * [Alternatywa – Fossify](#alternatywa--fossify)
  * [Inne aplikacje](#inne-aplikacje)
* [Ustawianie domyślnych aplikacji](#ustawianie-domyślnych-aplikacji)
* [Multimedia – VLC](#multimedia--vlc)
* [Klawiatura ekranowa – OpenBoard](#klawiatura-ekranowa--openboard)
* [Mapy i&nbsp;nawigacja](#mapy-inawigacja)
* [Dla chętnych: firewall](#dla-chętnych-firewall)
* [Dla chętnych: Termux](#dla-chętnych-termux)
* [Open source kontra YouTube](#open-source-kontra-youtube)

{% include info.html
type="Porada"
text="Wpis jest względnie niezależny od pierwszego, a&nbsp;opisy aplikacji -- od siebie nawzajem. Gdyby okazał się za długi na jedno czytanie, to można to robić na raty.  
Zachęcam też do przeczytania [poprzedniego wpisu](/2024/02/03/smartfon-degoogle){:.internal}, żeby mieć szerszy obraz."
%}

## Blaski i&nbsp;cienie Play Store'a

Bardzo wiele organizacji oferuje własne aplikacje. Odwiedzając ich strony internetowe, można się natknąć na takie coś:

{:.figure .bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle-apki/playstore-appstore-duopol.jpg" alt="Dwa przyciski ustawione obok siebie. Jeden zawiera napis 'Pobierz przez AppStore', a&nbsp;drugi: 'Pobierz przez PlayStore'."/>

{:.figcaption}
Tu akurat zrzut ekranu ze strony mObywatela, oficjalnej apki dla obywateli Polski. Ona również jest podporządkowana gigantom cyfrowym.

Czasem, bardzo rzadko, jest tu również AppGallery od Huaweia (co wiele nie zmienia; ot, kolejne korpo). Ale zazwyczaj są tylko dwie opcje. App Store dla tych, którzy korzystają z&nbsp;iPhone'a. Google Play, jeśli ktoś ma Androida.

Po kliknięciu cegiełki Google Play otwiera się **Play Store**. Jeśli ktoś nie jest zalogowany na konto Google, to prosi, żeby to zrobić. Potem trzeba kliknąć odpowiedni przycisk i&nbsp;czekać, aż aplikacja się zainstaluje.

Ktoś mógłby pomyśleć, że nie ma wyboru, trzeba w&nbsp;taki sposób.  
A nie trzeba. Play Store nie jest *jedyną* opcją. Czasem nie jest nawet *najlepszą*. Dlatego, nim przejdę do konkretnych aplikacji, omówię ich możliwe źródła.

### Na czym polega instalowanie aplikacji

W instalowaniu aplikacji -- szok i&nbsp;niedowierzanie -- nie ma żadnej magii. Przeciętna aplikacja na system Android to zwykły plik. Dokładniej: **plik z&nbsp;rozszerzeniem APK**.

{% include info.html
type="Ciekawostka"
text="APK to tak naprawdę umowne rozszerzenie, a&nbsp;pod względem budowy jest to spakowane archiwum.  
Można pobrać taki plik na komputer (tu [przykład](https://signal.org/android/apk/), apka Signala), zmienić rozszerzenie z&nbsp;`.apk` na `.zip` i&nbsp;rozpakować. Na systemie Linux nie trzeba nawet zmieniać rozszerzenia, bo on widzi „prawdziwą naturę” plików."
%}

Instalacja apki przez Play Store'a polega po prostu na tym, że:

1. Google sobie analizuje parę rzeczy na temat nas i&nbsp;wybranej aplikacji;
2. Play Store pobiera plik APK;
3. Play Store każe systemowi Android zainstalować plik, a&nbsp;system to robi.

Punkt pierwszy jest wybitnie niekorzystny z&nbsp;punktu widzenia prywatności. Korzystanie z&nbsp;Play Store'a **wymaga zalogowania się na konto Google**. Będą zatem jednoznacznie widzieli, kto co instaluje.

Jeśli ktoś używa apki od śledzenia cyklu miesiączkowego, to poznają płeć. Jeśli ma apkę od modlitw, to wyznanie. Aplikacje randkowe, zdrowotne, od diet... Sam fakt ich posiadania ukaże rzeczy, których raczej by się nie wpisało w&nbsp;pierwszy lepszy formularz.

### Alternatywne źródła

W związku z&nbsp;tym pojawia się zasadnicze pytanie -- czy można obejść punkt 1&nbsp;i wykonać całą instalację na własną rękę? Tak! I&nbsp;wcale nie wymaga to większego nakładu pracy niż przez Play Store'a.

Można to zrobić na kilka równie łatwych sposobów:

* przez alternatywną bazę aplikacji;
* przez zwykłą przeglądarkę;
* z&nbsp;pliku APK (używając apki do przeglądania plików).

W idealnym świecie każdy twórca umieszczałby u&nbsp;siebie, obok linku do Play Store'a, link do czystego pliku APK. Chętni mogliby zdobyć aplikację jednym kliknięciem, bez pośrednictwa Google'a.

{:.post-meta .bigspace-after}
Właściwie Google i&nbsp;tak może się dowiedzieć, póki nie wyłączy się skanowania aplikacji. O&nbsp;tym za moment.

Ale świat nie jest idealny, a&nbsp;apki na stronach to mniejszość. Wiele osób rozprowadza je tylko przez bazę Google'a.

Teoretycznie wiele apek można zdobyć przez strony zwane *mirrorami*, jak APK Mirror, które oficjalnie pobierają pliki APK przez Play Store'a, a&nbsp;potem umieszczają je u&nbsp;siebie.

Pojawia się tu jednak **problem zaufania**. Skąd mamy pewność, że mObywatel lub aplikacja banku z&nbsp;mirrora jest prawdziwą wersją, a&nbsp;nie podpuchą od kradzieży tożsamości? W&nbsp;nazwie i&nbsp;wyglądzie nie ma nic magicznego, każdy mógł stworzyć kopię.

Z tego względu *jakaś* weryfikacja jednak się przydaje. I&nbsp;tutaj wyróżniają się **aplikacje _open source_ -- ich kod źródłowy jest publicznie dostępny i&nbsp;chętni mogą go prześwietlić**. Automatyczne narzędzia i&nbsp;czujne oczy upewniają się, że aplikacje nie zawierają syfu.

Ludzie ze świata *open source* stworzyli całą bazę takich aplikacji -- **F-Droid**. Alternatywę dla Play Store'a. Apki są sprawdzane przez autorów i&nbsp;budowane przez nich z&nbsp;kodu źródłowego.

### Plan działania

W związku z&nbsp;powyższymi faktami proponuję:

1. Zminimalizować kontakt z&nbsp;Play Store'em.

   Pobrać z&nbsp;niego tylko rzeczy od większych organizacji, które strach by było brać z&nbsp;nieznanych źródeł. Na przykład przeglądarkę, aplikacje własne firm.

2. Pobrać F-Droida w&nbsp;roli sprawdzonego źródła alternatywnego.
3. Resztę aplikacji zainstalować właśnie przez F-Droida.
4. Odebrać Play Store'owi jak najwięcej możliwości.

{:.bigspace}
<img src="/assets/posts/google/smartfon-degoogle-apki/playstore-fdroid-zmiana.jpg" alt="Schemat. Od ikony aplikacji PlayStore idzie zielona strzałka w&nbsp;stronę ikony F-Droida. Obok niej jest ikona PlayStore'a nakryta koszem na śmieci." width="60%"/>

Osobiście pobrałem przez Play Store'a jedynie Firefoksa, Mapy.cz i&nbsp;nieliczne apki użytkowe, jak te od linii lotniczych. Potem zainstalowałem [F-Droida ze strony twórców](https://f-droid.org/) (przez Firefoksa). Resztę pozyskałem albo przez F-Droida, albo prosto ze stron.

Gdy Play Store już spełni swoje zadanie, to można go wyłączyć (spokojnie, to nic nieodwracalnego). A&nbsp;jeśli ktoś wyłączyć nie chce, to może chociaż ubić funkcję skanowania aplikacji.

### Wyłączenie Play Protect

Aplikacja Play Store pozwala sobie na wiele. Między innymi na używanie funkcji **Play Protect** do okresowego skanowania zainstalowanych aplikacji. Rzekomo w&nbsp;celu wykrywania wirusów.

{:.bigspace}
<img src="/assets/posts/google/smartfon-degoogle-apki/play-protect-duperele.jpg" alt="Powiadomienie smartfonowe mówiące, że Ochrona Google Play Protect jest włączona i&nbsp;chroni przed szkodliwymi aplikacjami" width="500px"/>

Jak to w&nbsp;przypadku Google'a, skan zapewne opiera się na algorytmach uczenia maszynowego, nazywanych marketingowo AI. Które bywają zawodne. Niedawno ten antywirus Play Store'a **automatycznie usunął ludziom niegroźne aplikacje**.

Jedną z&nbsp;nich były [oficjalne apki Samsunga](https://futurebeat.pl/newsroom/dziwny-ruch-google-aplikacje-samsunga-wydaja-mu-sie-szkodliwe-wie/zc27199): Portfel i&nbsp;Wiadomości.  
Kolejną -- przydatna i&nbsp;ceniona [aplikacja KDE Connect](https://old.reddit.com/r/kde/comments/175upzi/has_play_protect_removed_kde_connect_from_your/), służąca do synchronizacji plików między urządzeniami.

Pikanterii sprawie dodaje fakt, że **usunięta apka była pobrana z&nbsp;F-Droida. Spoza rewiru Play Store'a i&nbsp;Google'a**. Może nawet specjalnie po to, żeby ominąć kontrolę Wujka G. Ale wszystko na nic, bo ten zrobił ze smartfona swój osobisty folwark.

{:.figure .bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle-apki/kde-connect-uninstall.jpg" alt="Komunikat od aplikacji Google Play Protect mowiący, że usunął aplikację KDE Connect, którą uznał za szkodliwą." width="500px"/>

{:.figcaption}
„Dla naszego bezpieczeństwa”. Jak wiele innych odpałów Google'a.

Żeby wyłączyć agresywne skanowanie i&nbsp;zmienić ustawienia Play Protect, trzeba:

* uruchomić apkę Play Store (czyli siłą rzeczy zalogować się na konto),
* kliknąć ikonę swojego konta w górnym rogu,
* wybrać opcję `Play Protect`.

Będą tam dwa pstryczki. Dolny to funkcja rozszerzona -- sprawia, że **Play Store wysyła Google'owi do analizy nieznane aplikacje znalezione na telefonie**.  
Tę opcję można od razu wyłączyć. Zwłaszcza jeśli ktoś testuje prototyp czegoś rewolucyjnego i&nbsp;nie chce, żeby kolorowy gigant podkradł pomysł :wink:

Górna opcja to z&nbsp;kolei skanowanie i&nbsp;usuwanie aplikacji pobranych z&nbsp;Play Store'a. Żeby nie irytować ludzi od cyberbezpieczeństwa, proponuję kompromis -- nim się to wyłączy, trzeba sobie obiecać, że:

* będzie się instalowało jak najmniej aplikacji, jedynie te naprawdę potrzebne;
* w&nbsp;miarę możliwości tylko z&nbsp;F-Droida albo stron autorów;
* będzie się kontrolowało pozwolenia na telefonie i&nbsp;nadawało ich jak najmniej.

Ktoś, kto ma taką cyfrową higienę, nie potrzebuje ochrony Wujka G. I&nbsp;może sobie pozwolić na wyłączenie Play Protect, albo i&nbsp;całego Play Store'a.

To tyle co do instalowania apek. Przejdę teraz do polecania zamienników. Oczywiście ta część będzie mocno subiektywna, bo smartfon to indywidualna sprawa, a&nbsp;nie przetestowałem nawet ułamka możliwości.

## Przeglądarka internetowa – Firefox

Gdyby jakaś osoba mi powiedziała, że ma lenia i&nbsp;może wymienić najwyżej jedną aplikację od Google'a, to powiedziałbym: „wymień Chrome'a”. Bez wahania.

**Przeglądarka to jeden z&nbsp;najważniejszych elementów smartfona**. Jeśli chce się minimalizować liczbę apek na telefonie, używając zamiast nich stron internetowych, to wszystko będzie się kręciło wokół niej.

Chrome nie wydaje się godzien takiego zaufania i&nbsp;działa czasem wbrew użytkownikom.  
Krótki przegląd jego [ciemnych stron](/google/2021/10/30/google-skandale-wprowadzenie#chrome-przegl%C4%85darka){:.internal} umieściłem w&nbsp;pierwszym wpisie o&nbsp;Google'u. Jeszcze gorsze są [pomysły z&nbsp;zeszłego roku](/google/2023/07/29/web-environment-integrity){:.internal}, wprost wymierzone w&nbsp;wolność internetu.  
Wersja mobilna Chrome'a oczywiście też niesie za sobą te kontrowersje.

Lepszych alternatyw jest kilka, dwie znane to Firefox i&nbsp;Brave. Lis i&nbsp;lew. Osobiście postawiłem na Firefoksa z&nbsp;dodatkiem blokującym (o&nbsp;nim za moment).

{:.post-meta .bigspace-after}
Są też nowsze alternatywy od znanych graczy w&nbsp;świecie prywatności -- jak przeglądarka DuckDuckGo czy [Mullvad Browser](https://mullvad.net/en/browser) -- ale nie miałem okazji ich lepiej poznać.

<img src="/assets/posts/google/smartfon-degoogle-apki/chrome-firefox-zmiana.jpg" alt="Ikona przeglądarki Chrome z&nbsp;dorobionym niebieskim okiem pośrodku. Prowadzi od niej zielona strzałka ku ikonie Firefoksa" width="50%"/>

{% include info.html
type="Porada"
text="Na czym polegają różnice między Firefoksem a&nbsp;Brave'em?  
Intuicyjnie: Brave ma wyższą „podłogę” (ochronę bazową, bez instalacji dodatków). Firefox ma wyższy „sufit” (potencjał po zainstalowaniu dodatków przeciw profilowaniu).  
Poza tym **Firefox ma własny, niezależny silnik**. W&nbsp;przeciwieństwie do większości nie bazuje na tzw. Chromium. Dla codziennych użytkowników rzecz niezauważalna. Ale ważna dla utrzymania różnorodności."
%}

Kolejna sprawa to źródło. Zainstalowałem Firefoksa przez Play Store'a, mimo wszelkich jego wad. W&nbsp;F-Droidzie nie ma oficjalnego Firefoksa, choć są przeróbki (Fennec i&nbsp;Mull). Poza tym potraktowałem to jak rzucenie rękawicy Google'owi i&nbsp;lekkie podbicie Lisowi statystyk pobrań.

{% include info.html
type="Porada"
text="A gdyby ktoś koniecznie chciał Firefoksa spoza Play Store'a, to można go znaleźć w&nbsp;[zakładce](https://github.com/mozilla-mobile/firefox-android/releases) na oficjalnej stronie z&nbsp;kodem źródłowym. Trzeba spojrzeć pod nagłówkiem `Firefox Beta`, kliknąć `Assets`, żeby wyświetlić dostępne pliki APK, i&nbsp;wybrać ten pasujący do swojego procesora mobilnego. 
Większość telefonów ma 64-bitowe, więc powinna pasować pozycja kończąca się na `arm64-v8a.apk`."
%}

### Zmiana wyszukiwarki na DuckDuckGo

Mamy naszego Firefoksa... ale to dopiero początek. Po pierwszym uruchomieniu obok paska wyszukiwania ukaże się znajoma czterokolorowa narośl w&nbsp;kształcie literki G.  
Tak. **Domyślną wyszukiwarką na Firefoksie jest Google, bo kupił sobie ten przywilej**.

Co gorsza, jest to [główne źródło zarobków Firefoksa](https://www.pcmag.com/news/mozilla-signs-lucrative-3-year-google-search-deal-for-firefox). Pojawiają się nawet głosy, że Google trzyma Lisa przy życiu, żeby móc twierdzić, że ma konkurencję i&nbsp;nie trzeba go karać za monopolizację. Ponura perspektywa, nieprawdaż?

Na szczęście użytkowników nie obowiązują żadne *byznesowe deale* i&nbsp;mogą łatwo zmienić wyszukiwarkę. Osobiście wybrałem DuckDuckGo i&nbsp;od tamtego czasu rzadko muszę wchodzić na Google'a.  
Żeby to zrobić, trzeba kliknąć ikonkę wyszukiwarki w&nbsp;rogu, potem wejść w&nbsp;opcję `Domyślna wyszukiwarka` i&nbsp;tam sobie wybrać z&nbsp;listy zamiennik.

{:.bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle-apki/google-duckduckgo-zmiana.jpg" alt="Zrzuty ekranu pokazujące po kolei, jak zmienić domyślną wyszukiwarkę z Google na DuckDuckGo" width="50%"/>

{% include info.html
type="Porada"
text="Jeśli wyniki wyświetlone przez DDG nie będą do końca zadowalające, to można dopisać do swojego wyszukania `!g` (po spacji). W&nbsp;ten sposób wyszukamy to samo przez stronę Google'a, oczywiście ze wszelkimi konsekwencjami dla prywatności.  
Już nieraz odkrywałem po takim sprawdzeniu, że wyniki Kaczora wcale nie były gorsze."
%}

### Dodatek uBlock Origin

{% include info.html
type="Uwaga"
text="Te porady dotyczą Firefoksa, bo niestety nie da się instalować dodatków na większości mobilnych przeglądarek.  
Dałoby się też na Kiwi Browser, ale ona z&nbsp;kolei nie powala pod względem prywatności."
%}

Ten dodatek cenię na tyle, że poświęciłem mu dwa wpisy. Poczynając od [krótszego, wprowadzającego](/2021/10/21/ublock-origin){:.internal}.

Choć jest niepozorny, skutecznie zwalcza jedną z&nbsp;najgorszych metod śledzenia -- **elementy od firm reklamowych (w&nbsp;tym Google'a) zagnieżdżone na cudzych stronach**. To one pozwalają analizować czyjeś wędrówki po sieci i&nbsp;łączyć niezwiązane ze sobą strony w&nbsp;jeden spójny profil cech i&nbsp;zainteresowań. Który może być potem użyty do celów manipulacji.

Nieliczne, lecz głośne osoby demonizują takie dodatki, mówiąc że to odbieranie zarobków twórcom stron. Tyle że uBO to dużo więcej niż *bloker reklam* -- on blokuje *śledzenie*.

Gdyby internetowe reklamy były zwykłymi obrazkami wśród treści, to filtr domen by ich nie odsiewał. Słusznie by je uznał za część strony.  
A że są pobierane z&nbsp;zewnątrz, od firm reklamowych, i&nbsp;używają piramid kodu JavaScript do analizowania ludzi? To są blokowane. Takie życie.

Co do instalowania uBO na Firefoksie:

* klikamy ikonę trzech kropek w&nbsp;górnym rogu,
* następnie `Dodatki`,
* potem `Zarządzaj dodatkami`,
* wybieramy z&nbsp;listy uBlock Origin. Instalujemy. I&nbsp;już! 

## Podstawowe aplikacje

Każdy smartfon posiada kilka aplikacji użytkowych. Minimalistycznych, ułatwiających życie. Jak budzik wydający głośne dźwięki o&nbsp;określonej godzinie. Apka od przeglądania i&nbsp;prostej edycji zdjęć. Lista kontaktów od szybkiego wybierania numerów.

Gdy robiłem pierwszą czystkę na smartfonie, widziałem że Google w&nbsp;wiele miejsc wpycha swoje czterokolorowe rzeczy. Blokowałem je. Odciąłem też niebieskie Duo czy Android Auto (bo wiedziałem skądś, że też googlowe). Myślałem, że mam spokój.

Ale zostałem przechytrzony. Jak się okazuje, **wiele tych minimalistycznych apek o&nbsp;prostych ikonach należy do Google'a**. Czy to źle? Tak.

### Ciemna strona drobnych aplikacji

System Android jest rozwijany przez Google publicznie, każda osoba na świecie ma dostęp do [kodu źródłowego](https://source.android.com/).

W dawnych, dobrych czasach ten kod zawierał podstawowe aplikacje od dzwonienia i&nbsp;SMS-ów. Teoretycznie wszyscy chętni mieli dobry fundament pod własny system smartfonowy.

Potem Google stworzył własne aplikacje na bazie tego publicznego kodu. Rzekomo po to, żeby wnieść jakąś *wartość dodaną* dzięki swoim usługom. Producenci zaczęli instalować je na telefonach. Niedawno [ugięło się Xiaomi](https://cellularnews.com/mobile-apps/google-phone-messages-apps-to-be-pre-installed-on-xiaomi-smartphones/).

W 2022&nbsp;roku wyszło na jaw, że ta *wartość dodana* może być ujemna dla użytkowników. Badacz z&nbsp;Trinity College w&nbsp;Dublinie stworzył artykuł opisujący [zakres danych](https://www.scss.tcd.ie/doug.leith/privacyofdialerandsmsapps.pdf), jakie zbierają bajery Google'a. Po konsultacjach z&nbsp;nim Google rzekomo wszystko załatał (tutaj przystępniejsza [dyskusja](https://news.ycombinator.com/item?id=30751751) o&nbsp;sprawie).

A wersje otwarte z&nbsp;kodu Androida, na których Google zbudował te swoje? Niedawno je [usunęli](https://www.androidauthority.com/google-kill-android-aosp-dialer-messages-app-3334980/). Od teraz „czysty” system Android, zbudowany z&nbsp;otwartego kodu, nie byłby w&nbsp;stanie obsługiwać smartfona.

Tyle z&nbsp;historii. Obecna sytuacja wygląda tak, że na nowym telefonie to Google odpowiada za SMS-y, dzwonienie i&nbsp;wiele innych rzeczy. Zaś jego apki witają takim czymś:

{:.figure .bigspace}
<img src="/assets/posts/google/smartfon-degoogle-apki/wifi-chat-antywzorzec.jpg" alt="Komunikat od Google pokazujący uśmiechnięte rysunkowe postacie w&nbsp;stylu alegria art oraz tekst mówiący, że włączenie czatu wi-fi przyniesie korzyści, ale wymaga udostępnienia informacji. Pod spodem widać dwie klikalne opcje." width="60%"/>

Pomijając sterylną korpografikę, która mnie drażni, zwrócę uwagę na manipulacyjny interfejs. Są tu dwie opcje. U&nbsp;dołu `Zgadzam się`, wyżej -- `Używaj Wiadomości bez funkcji czatu`.

**Opcja niewyrażenia zgody zlewa się z&nbsp;tłem**. Ta od zgody jest jaskrawa, wręcz nawołuje do kliknięcia. A&nbsp;to kliknięcie, jak sugeruje tekst, oznacza większe zbieranie danych. Nie znamy przy tym konkretów, jesteśmy odsyłani do regulaminów.

Czyli Google daje od siebie manipulację, korpografiki i&nbsp;pewnie do tego zbieranie danych. Mocne argumenty za tym, żeby wymienić podstawowe apki!

### Alternatywa – Fossify

Dobra nowina -- nie trzeba się rozdrabniać i&nbsp;szukać po jednym zamienniku naraz. Istnieje **Fossify, cała seria prostych apek użytkowych**.

Pochodzą od jednej grupy twórców, więc mają spójny wygląd, jednolitą stylistykę. Są przewidywalne w&nbsp;działaniu. Robią tylko to co powinny i&nbsp;robią to dobrze. Do tego są darmowe, a&nbsp;ich kod źródłowy -- otwarty.

{:.figure .bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle-apki/android-zestaw-alternatyw.jpg" alt="Ekran główny systemu Android, na którym widać ikony ośmiu aplikacji o&nbsp;zielonych kolorach" width="50%"/>

{:.figcaption}
Seria Fossify plus *Mapy.cz* plus F-Droid. Nowy zielony ład aplikacjowy.

Wiele tych aplikacji można zainstalować przez F-Droida. W&nbsp;dniu tworzenia wpisu nie mieli jeszcze Aparatu ani Zegara, ale ich dodanie powinno być tylko kwestią czasu.

{% include info.html
type="Uwaga"
text="Wśród aplikacji z&nbsp;F-Droida można też trafić na takie z&nbsp;bardzo podobnymi, choć pomarańczowymi ikonami, o&nbsp;nazwach w&nbsp;stylu *Prosty Aparat*.  
To seria Simple Mobile Tools. Twórca sprzedał prawa do niej firmie reklamowej, a&nbsp;niektórzy uczestnicy projektu wzięli publiczny kod i&nbsp;założyli Fossify jako alternatywę.  
Choć F-Droid czuwa i&nbsp;może nie pozwolić na niekorzystne, śledzące aktualizacje, lepiej zachować ostrożność. I&nbsp;wybrać serię zieloną, a&nbsp;nie pomarańczową."
%}

### Inne aplikacje

Nim poznałem Fossify, zainstalowałem sobie jako aplikację od SMS-ów [QKSMS](https://github.com/moezbhatti/qksms), również z&nbsp;F-Droida i&nbsp;z otwartym kodem źródłowym. Ponad 3&nbsp;tysiące gwiazdek na stronie z&nbsp;kodem źródłowym, więc popularna i&nbsp;lubiana. Cenię ją sobie.

Kolejna sprawa to **przeglądarka plików**. Na smartfonie nie tak kluczowa jak na pececie (bo wiele aplikacji ma własną wbudowaną). Ale przydatna, żeby coś pobrać, zapisać i&nbsp;wysłać dalej. Domyślnie chciałoby nią być Files by Google.

Osobiście korzystam z&nbsp;przeglądarki plików od Fossify. Niedawno mignęła mi też ciekawa alternatywa, [Little File Explorer](https://github.com/martinmimigames/little-file-explorer). *Open source*, waży tylko kilkadziesiąt kB, wspiera wszystkie wersje systemu Android.

Jeśli chodzi o&nbsp;przeglądarkę plików PDF, domyślnie chciały tę rolę Arkusze Google. A&nbsp;ja postawiłem na [MuPDF Mini](https://f-droid.org/packages/com.artifex.mupdf.mini.app/) z&nbsp;F-Droida.

W tym miejscu pokażę również przykładowy łańcuszek działań z&nbsp;życia. Co zrobić, gdy jestem w&nbsp;podróży i&nbsp;chcę kupić przez internet bilet na pociąg?

1. Wchodzę przez Firefoksa na stronę przewoźnika.  
   Nie używam ich aplikacji, bo jest zamknięta, dostępna tylko przez Play Store. Chcę jak najmniej takich.
2. Po zakupie odwiedzam swojego maila -- załóżmy że Gmail. Również nie przez aplikację od Google'a, tylko przez Firefoksa.
3. Stamtąd pobieram plik PDF z&nbsp;biletem, a&nbsp;podczas kontroli wyświetlam go na ekranie w&nbsp;muPDF Mini.

Współczesność? Jest. Ale bez zależności od Google'a i&nbsp;innych zamkniętych aplikacji.

### Ustawianie domyślnych aplikacji

Mając te czy inne zamienniki aplikacji, warto wejść w&nbsp;`Ustawienia`, potem w&nbsp;`Aplikacje` i&nbsp;w `Domyślne aplikacje`.  
Tam można paroma kliknięciami ustawić:

* aplikację od dzwonienia (dałem Telefon od Fossify);
* aplikację od SMS-ów (dałem QKSMS);
* przeglądarkę (dałem Firefoksa).

A po co? Bo w&nbsp;ten sposób kontrolujemy te funkcje telefonu, które nie wychodzą od nas, lecz od systemu.

Jeśli na przykład wewnątrz jakiejś aplikacji *niebędącej przeglądarką* klikniemy link, to może się ona zwrócić do systemu. „Systemie, otwórz to swoją domyślną przeglądarką, jaka by nie była”.

Gdyby domyślną był Chrome, a&nbsp;strona zawierałaby jakieś cenne informacje, to mógłby je poznać również Google. A&nbsp;to niedobrze!

## Multimedia – VLC

Domyślnie od plików multimedialnych miałbym zestaw rozstrzelonych aplikacji. YouTube, YouTube Music... 

Ale ja wolę muzykę offline, w&nbsp;formie plików, więc wybór odtwarzacza był prosty. **VLC**, jedna z&nbsp;najsolidniejszych aplikacji *open source*, dostępna również przez F-Droida.

Nie będę się o&nbsp;niej rozpisywał, bo jest bardzo intuicyjna. Wybiera się piosenkę lub film z&nbsp;listy, naciska jego nazwę i&nbsp;zaczyna się odtwarzać.  
VLC w&nbsp;kombinacji z&nbsp;paroma innymi programami pozwala uwolnić się od internetu i&nbsp;YouTube'a. O&nbsp;tym więcej pod koniec wpisu.

## Klawiatura ekranowa – OpenBoard

{:.bigspace-after}
<img src="/assets/posts/google/smartfon-degoogle-apki/gboard-openboard-zmiana.jpg" alt="Zielona strzałka prowadząca od ikony aplikacji Gboard do ikony OpenBoard" width="50%"/>

Dla niektórych może to być szokiem, ale **standardowa klawiatura, która wysuwa się czasem z&nbsp;dołu ekranu, również należy do Google'a**.  
To widżet zwany `GBoard`. Jak pokazałem w&nbsp;poprzednim wpisie, w&nbsp;ciągu paru tygodni testowego korzystania [wysłał do sieci](/2024/02/03/smartfon-degoogle#usuwanie-iwyłączanie){:.internal} całe megabajty bliżej nieokreślonych danych.

Klawiatura jest czymś szczególnie newralgicznym, bo ma dostęp na żywo do całego wpisywanego tekstu. Jak mocnego szyfrowania by nie używał czyjś komunikator -- klawiatura „zobaczy” wpisywane informacje wcześniej. Niezaszyfrowane.

Nawet gdyby nie wysyłała nikomu tekstu, wciąż może analizować czyjeś unikalne zachowania. Szybkość pisania, często stosowane emoty i&nbsp;zwroty, korzystanie z&nbsp;autokorekty... Dane niemalże biometryczne, unikalnie identyfikujące.  
Wiele można odczytać nawet [z historii wiadomości](/facebook_dane/2022/01/16/messenger-dalsza-analiza){:.internal}, a&nbsp;co dopiero na żywo z&nbsp;klawiatury. 

Nie miałem wątpliwości, że trzeba zmienić GBoarda. Otworzyłem F-Droida i&nbsp;wpisałem `keyboard`. Wyskoczyło kilka propozycji, więc zacząłem o&nbsp;nich czytać.

Na zamiennik GBoarda ostatecznie wybrałem [OpenBoard](https://github.com/openboard-team/openboard). Projekt o&nbsp;otwartym kodzie źródłowym, który zebrał pozytywne noty od ponad 2000&nbsp;osób ze światka programistycznego.  
A jeśli ktoś chce lepiej poznać opcje, to przegląd prywatniejszych klawiatur opracowała [Naomi Brockwell](https://www.youtube.com/watch?v=y4brX6x3mrM&pp=ygUXbmFvbWkgYnJvY3dlbGwga2V5Ym9hcmQ%3D) (uwaga: YouTube). 

OpenBoard ma też pewien fajny bajer -- przesuwając palcem po spacji, przesuwa się jednocześnie kursor w&nbsp;polu tekstowym. Można łatwo przejechać wstecz i&nbsp;naprawić po sobie literówki, bez męczenia się z&nbsp;klikaniem w&nbsp;tekst.

{% include info.html
type="Uwaga"
text="Po zainstalowaniu nowej klawiatury warto wejść w&nbsp;`Ustawienia`, potem w&nbsp;`System`, `Języki i metody wprowadzania`. Upewnić się, że nówka jest ustawiona w&nbsp;zakładce `Klawiatura ekranowa`. Jeśli nie, to ją wybrać z&nbsp;listy."
%}

## Mapy i&nbsp;nawigacja

Tutaj nie musiałem długo się wahać, bo mam sprawdzone rozwiązanie. **_Mapy.cz_**. Miażdżą te od Google'a, zwłaszcza gdy wyjedzie się poza miasto.  
Może małe porównanie? Oto widok z&nbsp;obu map na to samo, dość popularne miejsce. Śnieżne Kotły w&nbsp;Karkonoszach:

{:.bigspace}
<img src="/assets/posts/google/mapy/google-mapycz-porownanie.jpg" alt="Zestawienie obok siebie fragmentów dwóch map. Ta po lewej jest podpisana Google, ma jednolite szare tło z&nbsp;odrobiną niebieskiego i&nbsp;zieleni, podpisane dwa schroniska, ścieżki w&nbsp;identycznych kolorach. Mapa po prawej jest podpisana Mapy.cz i&nbsp;jest znacznie bardziej szczegółowa. Widać na niej poziomice oraz więcej ścieżek, z&nbsp;czego niektóre oznaczone kolorami szlaków."/>

Kolejną zaletą jest to, że *Mapy.cz* nie potrzebują do działania Usług Google Play -- śmigają zarówno na Huaweiu, który nigdy ich nie miał, jak i&nbsp;na Motoroli, na której je zablokowałem.

Mapy wybranych okolic można pobrać na telefon i&nbsp;korzystać z&nbsp;nich offline, bez łączności z&nbsp;internetem. W&nbsp;tym celu trzeba kliknąć ikonę w&nbsp;dolnym lewym rogu, wybrać `Mapy offline` i&nbsp;obszar, jaki chcemy pobrać. W&nbsp;Polsce można pobierać województwami.

Ta funkcja przydaje się zwłaszcza tam, gdzie zasięg jest niepewny albo dane mobilne byłyby kosztowne (jak Bieszczady przy granicy z&nbsp;Ukrainą, gdzie niektórym zjadło setki złotych). Poza tym odciąża to trochę serwery autorów.

{% include info.html
type="Uwaga"
text="W przeciwieństwie do innych aplikacji z&nbsp;tego wpisu, *Mapy.cz* nie są *open source* (udostępniają jedynie [parę modułów](https://github.com/mapycz)).  
Osobiście nie mam z&nbsp;tym problemu, zresztą i&nbsp;tak nie daję im łączności z&nbsp;siecią (używam w&nbsp;trybie offline, a&nbsp;do tego odcinam im internet *firewallem*, o&nbsp;którym będzie później).  
Purystów otwartego kodu może natomiast zainteresować aplikacja [Organic Maps](https://organicmaps.app/pl/), też oparta na danych OpenStreetMap.  
Z kolei osoby, które chciałyby wnieść coś od siebie w&nbsp;rozwój publicznych map, mogą dodawać do nich informacje przez apki takie jak [StreetComplete](https://github.com/streetcomplete/StreetComplete) (dostępna w&nbsp;F-Droidzie oraz luzem, jako plik APK)."
%}

### Nawigacja

*Mapy.cz* mają również tryb nawigacji, przydatny podczas podróży autem. Działa i&nbsp;robi swoje.  
Żeby go użyć, trzeba przytrzymać palec na jakimś punkcie mapy, potem kliknąć `Trasa`. Warto się upewnić, że u&nbsp;góry podświetlona jest ikonka samochodu, a&nbsp;nie piechura. Potem wystarczy nacisnąć opcję `Nawiguj`. 

Nie zmienia to jednak faktu, że ciężko przeskoczyć aktualne informacje o&nbsp;korkach na drodze, jakie podaje Google.  
Zresztą prawie żadna mapa nie będzie w&nbsp;stanie tego zrobić. Wuj G&nbsp;ma te informacje dzięki swojej powszechności. A&nbsp;powszechność zdobył dzięki różnym sztuczkom, niemożliwym dla mniejszych graczy.

Jest w&nbsp;tym pewne błędne koło. **Pełno osób używa Map Google, bo mają dane o&nbsp;korkach. Mają te dane, bo pełno osób ich używa**. Równie dobrze na ich miejscu mogłaby stać inna firma, bardziej wyspecjalizowana w&nbsp;mapach niż śledzeniu... No ale jest jak jest.

Jeśli ktoś za bardzo lubi dane o&nbsp;ruchu, to może je odczytać bez używania apki.  
W tym celu trzeba otworzyć Firefoksa lub inną przeglądarkę, wejść na stronę [*google.com/maps*](https://www.google.com/maps). Wpisać nazwę jednego punktu, kliknąć `Wyznacz trasę`, wybrać drugi. Pokaże się trasa, a&nbsp;czas przejazu będzie uwzględniał korki.

Żeby było nieco prywatniej, warto:

* nie być zalogowanym na Konto Google;
* mieć wyłączony dostęp przeglądarki do GPS-a; 
* nie wskazywać swojego prawdziwego celu, tylko coś pobliskiego (np. centrum miejscowości).

Po poznaniu warunków na drodze można zapamiętać trasę, ustawić ją w&nbsp;*Mapach.cz* i&nbsp;wyłączyć przeglądarkę. W&nbsp;razie potrzeby co pewien czas do niej wracając.

## Dla chętnych: firewall

Wspominałem wcześniej, że przydałyby się pstryczki wyłączające aplikacjom dostęp do internetu. Domyślnie ich nie ma. Ale da się je zdobyć, instalując **firewalla -- aplikację od przechwytywania i&nbsp;modyfikowania ruchu internetowego**. Osobiście wybrałem RethinkDNS.

Zapewne jeszcze nieraz wrócę do tematu, więc dokładniej opisałem instalację i&nbsp;korzystanie z&nbsp;apki w&nbsp;[osobnym samouczku](/tutorials/rethink-dns){:.internal}. A&nbsp;streszczając:

1. najlepiej zainstalować apkę przez F-Droida;
2. można kliknąć w&nbsp;ikonę `DNS` na głównym ekranie i&nbsp;wybrać opcję `System DNS` (żeby ewentualna awaria RDNS-a nie wpływała na całą łączność);
3. żeby blokować internet konkretnym aplikacjom, wystarczy wejść w&nbsp;menu `Aplikacje` i&nbsp;klikać ikonki po prawej stronie, aż się przekreślą.

Oczywiście odebrałem dostęp wszystkim rzeczom od Google'a -- pamiętając, że domyślny Telefon, Zegar itp. też się do nich zaliczają. Ale także aplikacjom zaufanym, które nie potrzebują łączności. Jak *Mapy.cz* (bo korzystam w&nbsp;wersji offline).

<img src="/assets/posts/google/smartfon-degoogle-apki/rethink-dns-blokowanie.jpg" alt="Schemat pokazujący ustawienia RethinkDNS. Pośrodku widać okno z&nbsp;ustawieniami dla dwóch aplikacji. Apka Files By Google ma wyłączoną łączność, a&nbsp;strzałka wychodząca od jej ikony odbija się od okna z&nbsp;ustawieniami. Strzałka wychodząca od aplikacji Firefox, która ma włączone przełączniki, normalnie dociera do ikony kuli ziemskiej po drugiej stronie okna." />

{:.figcaption}
Źródła: oficjalne ikony, [kula ziemska](https://www.flaticon.com/free-icon/navigation_2763373) autorstwa *vectorsmarket15* (serwis Flaticon).

## Dla chętnych: Termux

Termux nie każdemu się spodoba, bo bardzo się różni od tradycyjnych aplikacji. Ma postać *konsoli*, w&nbsp;którą można wpisywać różne polecenia.  
To fajna sprawa dla osób, które chcą:

* wprawić się w używaniu konsoli, nie mając komputera pod ręką;
* użyć sprawdzonych konsolowych programów na telefonie;
* zmienić smartfona z&nbsp;narzędzia konsumpcji w&nbsp;pełnoprawne narzędzie pracy.

Radzę brać wersję z&nbsp;F-Droida. [Ta z&nbsp;Play Store'a jest przestarzała](https://wiki.termux.com/wiki/Termux_Google_Play), bo Google rzucał twórcom kłody pod nogi.

Choć możliwości Termuksa są ogromne, nie trzeba wiedzy technicznej, żeby używać gotowych, przydatnych programików. To tylko kwestia wpisywania odpowiednich rzeczy. Już spieszę z&nbsp;przykładem.

## Open source kontra YouTube

Uwolnienie smartfona nie oznacza jeszcze uwolnienia się od Google'a.  
Niektóre ich usługi nie mają swoich odpowiedników. Przykładem YouTube. Wielu materiałów -- również tych pomocnych przeciw samemu gigantowi -- zwyczajnie nie znajdziemy poza tą platformą.

Motorola G22 miała zainstalowane aplikacje YouTube oraz YouTube Music. Oczekiwania duetu Google-Motorola były zapewne takie, że odwiedzam stronę przez aplikację i tylko streamuję sobie multimedia.

Nie mam niczego na własność i&nbsp;jest mi z&nbsp;tym źle. Wszystko może wyparować, gdy twórca dostanie [losowego bana](/google/2022/04/18/youtube-ai-reklamy#banowanie-idemonetyzacja){:.internal}.

Z tego względu wolę mieć multimedia u&nbsp;siebie, na „dysku” smartfona. **Gdy są u&nbsp;mnie, to jestem niezależny od internetu i&nbsp;cudzych kaprysów**. Mógłbym stracić zasięg, ktoś mógłby stracić konto, YouTube mógłby upaść... a&nbsp;moje filmy i&nbsp;piosenki pozostaną u&nbsp;mnie. Zawsze dostępne.

Do uzyskania niezależności można użyć `yt-dlp`, uniwersalnego pobieracza multimediów ([z wielu stron](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md); w&nbsp;żadnym razie nie zmuszam do odwiedzania YouTube'a).

To programik konsolowy, więc do działania wymaga Termuksa. No i&nbsp;przyda się odtwarzacz, jak wspomniany już VLC, żeby posłuchać pobranych rzeczy. Z&nbsp;kolei na temat instalacji i&nbsp;używania `yt-dlp` na Androidzie już się kiedyś [rozpisałem](/tutorials/yt-dlp-android){:.internal}.

Mając ten programik, mógłbym odwiedzić dowolną wspieraną stronkę przez Firefoksa. Skopiować sobie link do strony z&nbsp;piosenką. A&nbsp;wewnątrz Termuksa przejść do publicznego folderu na muzykę i&nbsp;użyć komendy:

```
yt-dlp -f bestaudio SKOPIOWANY_LINK
```

...I po chwili piosenka byłaby u&nbsp;mnie, gotowa do odtworzenia przez VLC. I&nbsp;posłuchania przez słuchawki za 20&nbsp;zł, a&nbsp;nie jakieś bezprzewodowe bajery. Zaleta Motoroli i&nbsp;wejścia typu *jack*.

Firefox. F-Droid. Termux. YT-DLP. VLC.  
Używając łańcuszka programów *open source*, można wyjąć piosenkę z&nbsp;korporacyjnych rąk i&nbsp;posłuchać jej na własnych zasadach :metal: Aż zacytuję elektroniczno-punkowy bangerek sprzed 15&nbsp;lat:

> Let's march right out of this godforsaken place  
Take back control and stand up straight  
We played by the book, now we do it our way  
We're the soldiers of tomorrow and we're here to stay! 

{:.figcaption}
Źródło: Alice in Videoland, [*We Are Rebels*](https://www.youtube.com/watch?v=WqJ9_VFkGe0).

Do zobaczenia w&nbsp;kolejnych wpisach!

