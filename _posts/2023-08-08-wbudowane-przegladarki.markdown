---
layout: post
title: "Apki to pułapki 7 – fałszywe przeglądarki"
subtitle: "Przejażdżka, za którą zapłacisz danymi."
description: "Przejażdżka, za którą zapłacisz danymi."
date:   2023-08-08 21:17:23 +0100
tags: [Apki, Inwigilacja, Podstawy]
firmy: [Facebook, TikTok]
category: apki
category_readable: "Apki to pułapki"
image:
  path: /assets/posts/apki/in-app-browser/fake-browser-baner.jpg
  width: 1200
  height: 700
  alt: "Obrazek pokazujący czarną taksówkę z przerobionym złotym napisem Fake Browser na boku. Z okna wychyla się kierowca, którego twarz jest zakryta logiem Messengera"
---

We współczesnym świecie życie kręci się wokół internetu. Przeglądarka to stały element każdego smartfona.

Jak pokazywałem w&nbsp;innej swojej serii, [„Internetowej inwigilacji”](/serie/internetowa_inwigilacja/){:.internal}, przeglądarki zwykle chronią naszą prywatność podczas internetowych wojaży (niechlubnym wyjątkiem jest Chrome). Owszem, odwiedzane strony wciąż mogą się sporo o&nbsp;nas dowiedzieć. Ale muszą stosować sztuczki.

Ale linki do stron trafiają się nie tylko w&nbsp;przeglądarce. Co się dzieje, gdy klikniemy jakiś w innej aplikacji?

Zwykle po prostu otworzy nam się strona w&nbsp;tej głównej, szczelnej, chroniącej nasz tyłek przeglądarce. Nic strasznego.

Ale może się też zdarzyć, że **zamiast niej otworzy się przeglądarka fałszywa. Wbudowana w&nbsp;aplikację, żeby zbierać nasze informacje**.

To dość zaskakujący sposób śledzenia i&nbsp;warto go poznać. Zapraszam do lektury!

{:.figure .bigspace-before}
<img src="/assets/posts/apki/in-app-browser/fake-browser-baner.jpg" alt="Przeróbka pokazująca czarną taksówkę ze znanej serii filmików stojącą na placu. Na boku ma nieco przerobiony złoty napis Fake Browser. Z&nbsp;okna wychyla się kierowca, pokazując kciukiem znak OK. Zamiast głowy ma logo Messengera, komiksowy dymek w&nbsp;odcieniach fioletu i&nbsp;niebieskiego, z&nbsp;białą błyskawicą pośrodku."/>

## Spis treści

* [Zarys tematu](#zarys-tematu)
* [Podstawowe założenia](#podstawowe-założenia)
* [Zostawianie linków przeglądarce](#zostawianie-linków-przeglądarce)
* [WebView -- „okno na świat”](#webview--okno-na-świat)
  * [Okno nieszczelne](#okno-nieszczelne)
  * [Okno szczelne](#okno-szczelne)
* [Przeglądarka udająca apkę](#przeglądarka-udająca-apkę)
* [Czarne scenariusze](#czarne-scenariusze)
  * [Czytanie haseł i wrażliwych danych](czytanie-haseł-iwrażliwych-danych)
  * [Wyciąganie danych przez linki](#wyciąganie-danych-przez-linki)
  * [Doskonalsza replika przeglądarki](#doskonalsza-replika-przeglądarki)
  * [Ustalanie marki czyjegoś telefonu](#ustalanie-marki-czyjegoś telefonu)
* [Jak się chronić?](#jak-się-chronić)

## Zarys tematu

Mniej więcej rok temu pewien badacz zajmujący się sprawami cyfrowymi, Felix Krause, opublikował niepokojący raport. Pokazał, że niektóre znane aplikacje [mogą odczytywać wszystko, co robimy na stronach internetowych](https://krausefx.com/blog/ios-privacy-instagram-and-facebook-can-track-anything-you-do-on-any-website-in-their-in-app-browser). Modyfikując w&nbsp;tym celu ich treść i&nbsp;dodając kod śledzący.

Stworzył również [stronę internetową *inappbrowser.com*](https://krausefx.com/blog/announcing-inappbrowsercom-see-what-javascript-commands-get-executed-in-an-in-app-browser), która pokazuje w&nbsp;zrozumiały sposób, co taki kod jest w&nbsp;stanie zrobić.  
A może bardzo wiele. W&nbsp;skrajnych przypadkach -- odczytać każdy dotknięty element, każdą wpisaną literkę. Również na stronach cudzych, zupełnie niezwiązanych z&nbsp;daną apką.

W jakich sytuacjach może dojść do wstrzyknięcia w&nbsp;stronę śledzącego kodu? Wtedy, gdy nie odwiedzamy jej przez naszą domyślną przeglądarkę, tylko przez **przeglądarkę wbudowaną** bezpośrednio w&nbsp;aplikację śledzącą (ang. *in-app browser*).

I nie są to niszowe przypadki. Dotyczy to między innymi aplikacji od firmy Meta -- Facebooka, Instagrama, Messengera. Znanych recydywistów w&nbsp;sprawie naruszania prywatności.  
Swoje wbudowane przeglądarki mają również inne duże platformy, jak chociażby Reddit i&nbsp;Twitter.

Ale palma pierwszeństwa w&nbsp;kwestii inwazyjności należy do TikToka. Nie dość, że na stronie badacza [wypada najgorzej](https://krausefx.com/blog/announcing-inappbrowsercom-see-what-javascript-commands-get-executed-in-an-in-app-browser#ios-apps-that-have-their-own-in-app-browser)... To do tego nie daje opcji otwierania linków w&nbsp;naszej własnej przeglądarce. Wchodząc do przeglądarki TikToka, stajemy się jej więźniami.

Ich rzecznik [twierdzi](https://techcrunch.com/2022/08/19/tiktok-fb-in-app-browser-tracking-analysis), że przenoszenie użytkownika do innej przeglądarki... uderzałoby w&nbsp;płynność korzystania z&nbsp;apki (*would make for a&nbsp;clunky, less slick experience*).

Skoro widzimy skalę zagrożenia, to poznajmy je nieco bliżej! Omówmy sobie, czym są wbudowane przeglądarki. Ale najpierw parę podstaw.

## Podstawowe założenia

### Niezależność aplikacji mobilnych

Przypomnę tu podstawową, wałkowaną przez całą serię zasadę mobilnych systemów operacyjnych. Mianowicie: **każda apka ma własną prywatną przestrzeń. Aplikacje nie mogą zaglądać nawzajem do swoich plików**. 

Każda apka widzi większość rzeczy, jakie robimy wewnątrz niej samej. Nie widzi, co robimy wewnątrz innych apek. Całą sprawę nieco dokładniej opisałem we [wpisie na temat systemu plików]({% post_url 2022-11-16-apki-pliki %}){:.internal}.

Może to być nieintuicyjne dla osób wychowanych na komputerach osobistych. Tam zdarzało się, że programy zaglądały do siebie, a&nbsp;nawet modyfikowały cudzy kod (*cheaty* do gier). Ale w&nbsp;przypadku smartfonów twórcy systemów postawili na coś szczelniejszego.

Jeśli jakaś Apka 1&nbsp;chce mieć oko na nasze ruchy, to jedynym pewnym sposobem jest trzymanie nas jak najdłużej na swoim terytorium. Gdy tylko przejdziemy do Apki 2, to stracą nas z&nbsp;oczu.

<img src="/assets/posts/apki/in-app-browser/apki-rozdzielenie-prywatnosc.jpg" alt="Schemat złożony z&nbsp;dwóch linijek. W&nbsp;górnej widać czerwone pole w&nbsp;kształcie trapezu, podpisane Apka 1. Wewnątrz znajduje się groźnie wyglądająca ikona oka oraz smutna emotka. Druga linijka pokazuje to samo pole, al tym razem jest w&nbsp;nim tylko oko, ze łzą. Emotka przebywa w&nbsp;zielonym trapezie obok, podpisanym Apka 2, i&nbsp;jest uśmiechnięta." width="500px"/>

{% include info.html
type="Ciekawostka"
text="Pewną osobę zaniepokoił fakt, że TikTok na ogólnej liście zbieranych danych wymienia [dostęp do historii przeglądania](https://android.stackexchange.com/questions/250618/can-an-app-access-my-browser-history-from-other-apps).  
Ale na szczęście nadal obowiązuje tu uniwersalna zasada. Apki nie mogą do siebie zaglądać. TikTok nie zajrzy do historii naszej głównej przeglądarki. Co najwyżej do *historii nagromadzonej w&nbsp;jego przeglądarce wbudowanej*.  
Co nie zmienia faktu, że niektórzy mogą zostawić w&nbsp;takiej tiktokowej historii dość osobiste rzeczy."
%}

### Przeglądarka = silnik + interfejs

Praktycznie każdy system operacyjny zawiera wbudowaną aplikację do przeglądania internetu. Nazywamy ją **przeglądarką systemową**. Oprócz tego można instalować inne, niezależne przeglądarki. A&nbsp;nawet ustawiać je jako domyślne, jeśli wolimy je od systemowej.

Każdą przeglądarkę możemy sobie podzielić na dwie główne części.

* Silnik,  
  czyli zestaw programików za kulisami. Odpowiadają za działanie przeglądarki. Proszenie o&nbsp;strony, szyfrowanie połączeń, analizę treści, układanie elementów na stronie.

* Interfejs,  
  czyli to, co widzimy. Paski z&nbsp;opcjami, strzałki `Wstecz` i&nbsp;`Dalej`, przycisk od odświeżania strony...

Na systemie Android najczęstszą bazą jest **Chromium od Google'a** (*bazą*, nie silnikiem, bo to właściwie pełnoprawna przeglądarka).  
To na niej opiera się wiele domyślnych, systemowych przeglądarek. Miewają różne nazwy, bo wielu producentów często tworzy coś własnego. Czasem to po prostu aplikacja zwana `Internet`, obecna od początku na ekranie głównym telefonu.

W przypadku Apple wszystkie przeglądarki muszą korzystać z&nbsp;tego samego silnika -- stworzonego przez nich WebKita. Czy to Firefox, Chrome czy Brave... każda jest jedynie nakładką, a&nbsp;pod spodem tkwi WebKit.  
Z kolei ich oficjalną, systemową przeglądarką jest **Safari (też na bazie WebKita)**.

{:.bigspace-before}
<img src="/assets/posts/internet/ios-android-silniki.jpg" alt="Ikony przeglądarek z&nbsp;dwóch systemów. Po lewej stronie, pod napisem Android, mamy dużą ikonę przeglądarki Samsunga, a&nbsp;pod nią małą ikonę Chromium. Po prawej, pod napisem iOS, mamy dużą ikonę Safari opartą na małej ikonie silnika WebKit." width="400px"/>

{:.figcaption}
Główne przeglądarki oraz ich fundamenty. W&nbsp;przypadku Androida użyłem ikony przeglądarki Samsunga.  
Innych, alternatywnych systemów operacyjnych tutaj nie omówię. Ale uznaję ich istnienie, a&nbsp;mobilnym Linuksom wręcz kibicuję :wink:

## Zostawianie linków przeglądarce

Aplikacje mogą otwierać linki na różne sposoby. Zacznijmy od tego najmniej groźnego -- po prostu usuwają się z&nbsp;drogi i&nbsp;każą otworzyć nasz link domyślnej przeglądarce.

* Jesteśmy w&nbsp;jakiejś apce A, jest tam link. Naciskamy go.
* Aplikacja A&nbsp;to wyłapuje. Wysyła systemowi prośbę „otwórz ten link”.
* System słucha i&nbsp;otwiera link w&nbsp;domyślnej przeglądarce, czyli całkiem osobnej apce.

Ta metoda daje najwięcej prywatności. Po kliknięciu przechodzimy do przeglądarki i&nbsp;znikamy apce A&nbsp;z&nbsp;oczu. Możliwe, że nawet nie będzie wiedziała, co to za przeglądarka.  
Parafrazując infantylne memy: skoro nas kochają, to puszczają nas wolno :wink:

Ale uwaga! **Choć apka traci możliwość śledzenia, nadal może nadużyć tej metody do _wysłania_ tego, co już wyśledziła**. Zwłaszcza że otwarcie linku nie wymaga żadnego pozwolenia. Zagrożenie omówię bliżej końca wpisu.

## WebView -- „okno na świat”

Czasem aplikacja, zamiast oddawać użytkownika jego przeglądarce, woli zatrzymać go u&nbsp;siebie. Niekoniecznie w&nbsp;złych celach... Ale to zależy od tego, które z&nbsp;dostępnych rozwiązań technicznych wybierze.

W tym celu **sama otwiera stronę internetową, wewnątrz siebie** (we własnym interfejsie). Może ona zajmować całość ekranu, może zajmować jedynie część.

Jednocześnie apka nie musi sama wcielać się w&nbsp;przeglądarkę. Wystarczy, że zwróci się do systemu.  
„Systemie, otwórz mi w&nbsp;tym miejscu okno na świat, o&nbsp;wymiarach takich a&nbsp;takich. I&nbsp;otwórz w&nbsp;nim `https://jakas-zmyslona-stronka.com.pl`”.

A system otwiera okno, korzystając z&nbsp;dostępnego sobie silnika albo przeglądarki bazowej. Czyli, przypomnę: Chromium na Androidach, WebKit na iOS. Takie okno znamy ogólnie pod nazwą **WebView**.

Wspomniałem wyżej, że WV nie musi być otwierane w&nbsp;złych celach. Ale to w&nbsp;dużej mierze zależy od „szczelności” takiego okna. Od tego, czy aplikacja goszcząca je u&nbsp;siebie może wyciągać z&nbsp;niego informacje.

Omówmy sobie te dwa rodzaje „okien na świat”, szczelne i&nbsp;nieszczelne. Ich rodzaje na systemach iOS i&nbsp;Android są w&nbsp;miarę zbliżone. A&nbsp;bardziej subtelne różnice pozwolę sobie pominąć.

{% include info.html
type="Ciekawostka"
text="Wbudowane przeglądarki są zjawiskiem zadziwiająco popularnym -- [odpowiadają za kilkanaście procent ruchu internetowego na świecie](https://www.w3.org/blog/2022/making-webviews-work-for-the-web/).  
Nie wiem natomiast, jaki odsetek ich użytkowników ma świadomość zagrożeń."
%}

### Okno nieszczelne

To okno otwierające się wewnątrz cudzej aplikacji. Niekoniecznie na cały ekran, może zajmować tylko część przestrzeni. Wewnątrz niego -- widok na internet.

Takie okno **nie ma dostępu do danych głównej przeglądarki**. Nie zajrzy nam w&nbsp;historię czy też pliki cookies. Może je sobie co najwyżej niezależnie zbierać, w&nbsp;miarę odwiedzania przez nas kolejnych stron.

Z drugiej strony -- aplikacja, wewnątrz której otwiera się okno, może dodawać do odwiedzanych przez nas stron rzeczy od siebie. Takie jak [kod JavaScript]({% post_url 2022-05-02-javascript1 %}){:.internal}, którego łatwo użyć do zbierania i&nbsp;wysyłania innym dokładnych informacji o&nbsp;nas.

W ten sposób apka ma wgląd w&nbsp;nasze działania w&nbsp;szerszym internecie, poza swoim głównym obszarem działań. To właśnie na temat tego zagrożenia wypowiadał się Felix Krause.

W przypadku Androida taki nieszczelny element nazywa się po prostu [`WebView`](https://developer.android.com/develop/ui/views/layout/webapps/webview). Na systemach iOS bardzo podobna rzecz to [`WKWebView`](https://developer.apple.com/documentation/webkit/wkwebview).

{:.post-meta .bigspace-after}
Kiedyś na iOS było też coś takiego jak `UIWebView`, jeszcze mniej szczelne. Ale od kilku wersji systemu ten element nie jest wspierany.

<img src="/assets/posts/apki/in-app-browser/webview-nieszczelne-okno.jpg" alt="Schemat pokazujący dwa warianty aplikacji, na Androida i&nbsp;iOS. Są przedstawione jako czerwone trapezy z&nbsp;groźnie wyglądającym okiem w&nbsp;rogu. W&nbsp;każdej z&nbsp;nich znajduje się prostokąt wykonany z&nbsp;przerywanych kresek, z&nbsp;dwiema strzałkami na brzegu (od apki do jego wnętrza i&nbsp;vice versa). Wewnątrz prostokątów widać loga silników: Chromium oraz WebKita."/>

{:.figcaption}
WebView w&nbsp;wariancie nieszczelnym. Na smartfonach z&nbsp;Androidem jest obsługiwane przez Chromium, na iPhone'ach przez WebKita.

### Okno szczelne

Oba systemy oferują autorom aplikacji również **szczelną wersję WebView. Otwiera się wewnątrz apki, ale jest od niej odizolowana**.

Na systemach Android możemy użyć w&nbsp;swoich apkach elementu zwanego [`CustomTab`](https://developer.chrome.com/docs/android/custom-tabs/). Jego odpowiednikiem na systemie iOS jest [`SFSafariViewController`](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller).

W obu przypadkach wewnątrz cudzej aplikacji otwiera nam się okno naszej głównej przeglądarki. Tej, której zwykle używamy do łażenia po internecie. Wraz ze znajomym interfejsem (wyglądem), zapisanymi hasłami, historią...

Tyle że apka, w&nbsp;której się to okno otworzyło, nie ma możliwości zaglądania do niego, patrzenia co robimy. Nie może też dodawać od siebie żadnego JavaScriptu.

Android posiada również nówkę z&nbsp;2020 roku, [`Trusted Web Activity`](https://developer.chrome.com/docs/android/trusted-web-activity/). To coś w&nbsp;rodzaju wersji hybrydowej -- okno oparte na `CustomTab`, ale bez pełnego interfejsu przeglądarki. Jest parę innych różnic, ale dla nas mniej ciekawych. To po prostu inne szczelne okno.

{:.bigspace}
<img src="/assets/posts/apki/in-app-browser/webview-szczelne-okno.jpg" alt="Schemat pokazujący dwa warianty aplikacji, na Androida i&nbsp;iOS. Są przedstawione jako czerwone trapezy z&nbsp;groźnie wyglądającym okiem w&nbsp;rogu. W&nbsp;każdej z&nbsp;nich znajduje się nieprzezroczysty prostokąt symbolizujący pzeglądarkę otwartą wewnątrz apki. Na jednym z&nbsp;nich widać logo przeglądarki Samsunga, na drugim ikonę przeglądarki Safari."/>

{% include info.html
type="Ciekawostka"
text="Złe apki mogłyby teoretycznie obejść izolację, nakładając na ekran niewidzialne elementy. Każde dotknięcie palcem przechodziłoby najpierw przez nie. W&nbsp;ten sposób dałoby się np. ustalić, jakie elementy strony naciskał użytkownik.  
Google i&nbsp;Apple mogą wyłapywać takie apki i&nbsp;nie wpuszczać ich do swoich baz aplikacji (Apple [wprost zabrania](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller#overview) zakrywania okna innymi rzeczami).  
Ale czy mamy oprócz tego pewniejsze, techniczne zabezpieczenia przed obchodzeniem izolacji? Nie wiem, ale spróbuję się dowiedzieć. 
"%}

Szczelne okna są dobre dla prywatności. Podobnie jak przy zostawianiu linków przeglądarce -- twórcy odbierają sobie możliwość łypania na to, co robimy na stronach. Ale uwaga! Nadal mogą użyć takich okien do *wysłania* naszych danych. O&nbsp;tym bliżej końca wpisu.

W każdym razie, skoro oba systemy dają takie narzędzie... to dlaczego TikTok, apki Facebooka i&nbsp;inni domyślnie z&nbsp;niego nie korzystają? Czemu wolą wersję nieszczelną?  
Tak, pamiętam, „płynność korzystania”... Ale jestem sceptyczny.

## Przeglądarka udająca apkę

Tutaj przedstawię zagrożenie bardziej teoretyczne, ale realne.

Mianowicie: aplikacje na Androidzie nie muszą wchodzić w interakcje z&nbsp;internetem poprzez WebView. **Mogą również umieścić w&nbsp;sobie własny, niezależny silnik. Nie _otwierać w&nbsp;sobie_ przeglądarki, tylko _być_ przeglądarką**.

W przypadku iOS-a byłoby trudniej, tam wszystko musi korzystać z&nbsp;WebKita. Poza tym Apple [wprost pisze](https://developer.apple.com/design/human-interface-guidelines/web-views), że krzywo patrzą na próby tworzenia replik przeglądarki.

> Attempting to replicate the functionality of Safari in your app is unnecessary and discouraged.

W każdym razie -- załóżmy, że taka aplikacja z&nbsp;własnym silnikiem, *de facto* przeglądarka (ale oficjalnie udająca coś innego), prześlizguje się przez kontrolę wielkich firm i&nbsp;trafia w&nbsp;ręce użytkowników.

Ma wiele możliwości. Może nadać części swojego okna taki wygląd, jak te szczelniejsze wersje WebView na Androidzie i&nbsp;iOS.  
Oczywiście nie będzie idealną imitacją, bo nie ma chociażby dostępu do historii przeglądania czy zapisanych haseł -- te tkwią jedynie w&nbsp;domyślnej przeglądarce. A&nbsp;apki, pamiętajmy, nie mogą do siebie zerkać.

Ale powierzchowna imitacja mogłaby wystarczyć do uśpienia naszej czujności.  
Jednocześnie apka miałaby całkiem swobodny dostęp do tego, co przeglądamy, wszystkich naszych działań. Nawet lepszy niż przez oficjalne WebView, bo ściśle z&nbsp;nią zintegrowany.

Osobiście myślę, że coś tak oczywistego by nie przeszło przez sito procesu oceniania i&nbsp;nie trafiło do PlayStore'a czy AppStore'a. Ale zagrożenie warto znać.

## Czarne scenariusze

### Czytanie haseł i&nbsp;wrażliwych danych

To najbardziej jaskrawy przykład. Jeśli apka może dodawać od siebie dowolny kod do stron, to **może rejestrować wszystko co robimy**. Naciśnięte obszary strony, wpisany tekst, czas jaki na danej stronce spędzamy. Wszystkie dane może zbierać i&nbsp;przesyłać do siebie.

Na pocieszenie -- takie zachowanie jest już typowym atakiem na użytkownika, więc jest szansa, że aplikacje nie zostałyby zaakceptowane przez największe bazy aplikacji, takie jak PlayStore czy AppStore.  
...Chociaż z&nbsp;drugiej strony -- TikTok i&nbsp;apki Facebooka jakoś funkcjonują.

### Wyciąganie danych przez linki

Wyżej zasugerowałem, że nawet najbezpieczniejsze metody -- otwarcie linku w&nbsp;przeglądarce systemowej albo w&nbsp;jakimś szczelniejszym wariancie WebView -- mają swoją lukę.  
Apka nie będzie w&nbsp;stanie nas śledzić po oddaniu linku w&nbsp;ręce systemu... Ale **może w&nbsp;tym linku upchnąć nasze sekrety**.

Sam Google pisze na swojej stronie na temat funkcji Trusted Web Activities, czyli tego najszczelniejszego okna (w&nbsp;punkcie 4):

> możesz skomunikować aplikację z&nbsp;treściami sieciowymi, przekazując dane dla/od stron wewnątrz adresów URL

{:.figcaption}
Źródło: [Google](https://developer.chrome.com/docs/android/trusted-web-activity/). Luźne tłumaczenie moje.

Może to brzmieć niejasno, ale prawdopodobnie chodzi im o&nbsp;[parametry w&nbsp;linkach]({% post_url 2021-04-09-internetowa-inwigilacja-parametry %}){:.internal}.

Ich działanie opiera się na fakcie, że na końcu linku, po znaku zapytania, możemy dodać dowolne rzeczy. Byle format się zgadzał, ale to małe ograniczenie.  
Nie powinno to wpłynąć na działanie samego linku, na stronę do której prowadzi. Ale **nasz adresat odbierze całość, razem z&nbsp;parametrami. I&nbsp;może wyczytać z&nbsp;nich informacje**.

Przykład? Mamy u&nbsp;siebie złą apkę. Na podstawie różnych analiz (GPS, SMS-y, zawartość plików itp.) ustala nasze dane osobowe i&nbsp;miejsce zamieszkania. Teraz chce to wysłać swoim właścicielom, ale jak najdyskretniej.

Może podsunąć nam link do strony, którą kontrolują jej autorzy. Dajmy na to: link do podstrony z&nbsp;regulaminem. A&nbsp;na końcu tego linku, po parametrach, upycha nasze informacje.

<div class="black-bg mono">
https://www.strona-niedobrej-apki.pl/regulamin<span class="red">?name=kazimierz&lastname=nowak&location=warszawa-ulica-fikcyjna-13</span>
</div>

{:.figcaption}
Tutaj dane to imię (Kazimierz), nazwisko (Nowak), miejsce zamieszania (Warszawa, ul. Fikcyjna 13).

Kiedy otworzy nam się ten regulamin, to dane polecą do właścicieli strony. Czyli zarazem autorów złej apki.

Gdyby próbowali wysyłać dane ludzi do siebie, wprost przez apkę, to może ktoś by ich złapał. Ale kiedy chowają je w&nbsp;linkach, a&nbsp;linki otwierają się w teoretycznie bezpieczny sposób (poza ich oczami)? Mniej osób będzie podejrzewało śledzenie.

### Doskonalsza replika przeglądarki

Jeśli używamy niestandardowej przeglądarki (takiej jak Firefox Focus) to rośnie szansa, że rozpoznamy, gdy apka spróbuje otworzyć przeglądarkę wbudowaną. Po prostu coś będzie nie tak. Inny kolor pasków, inny wygląd przycisków.

Ale gdybyśmy mieli szczególnie wrednego przeciwnika, to **mógłby próbować poznać wygląd naszej przeglądarki i&nbsp;się pod nią podszyć jak kameleon**.

Na początku podsunąłby nam link do kontrolowanej przez siebie strony. I&nbsp;otworzył go w&nbsp;*domyślnej* przeglądarce. Uzasadniając to na przykład tym, że musimy przeczytać regulamin. I&nbsp;wszystko OK, prawda? Domyślna, czyli bezpieczna?

Tyle że odwiedzając tę stronę, nasza przeglądarka wysłałaby trochę informacji o&nbsp;sobie (np. to, że jest Firefoksem albo Brave'em). Inne informacje dałoby się ustalić na podstawie kodu obecnego na stronie. Albo nawet obrazków, jakie pobierze przeglądarka.

Mając te informacje, nasz przeciwnik może sprawdzić w&nbsp;wielkiej bazie, jak powinien wyglądać interfejs naszej przeglądarki.  
A przy kolejnych interakcjach już nie będzie otwierał linków w&nbsp;przeglądarce domyślnej, jak zrobił w&nbsp;kroku pierwszym. Od teraz może używać nieszczelnego WebView albo pełnej podróbki. Tyle że wystylizowanej na naszą przeglądarkę. 

Nie będzie to w&nbsp;100% dokładne, bo przeglądarki nie ujawniają stronom swojego pełnego wyglądu. Ale uwiarygodniłoby fałszywą przeglądarkę. Jest szansa, że się nie połapiemy i&nbsp;wpiszemy coś wrażliwego.

### Ustalanie marki czyjegoś telefonu

Tutaj przypadek raczej niegroźny na tle powyższych. Ale pokazuje, że **działanie wbudowanych przeglądarek mogą wykorzystać osoby z&nbsp;zewnątrz, niezwiązane z&nbsp;ich autorami**. Mogą odczytać pewne informacje, których normalnie by nie dostały.

Wyobraźmy sobie, że ktoś znajomy nam pisze, że ma nowy telefon. Nie przyznaje, jakiej marki. Ale układamy w&nbsp;głowie diabelski plan, który pozwoli się tego dowiedzieć. Kontrolujemy własną stronę internetową. Mamy wgląd do jej serwera.

Pierwsza myśl -- napiszemy przez Signala zaproszenie na naszą stronę („O, super! Działa ci na tym telefonie moja animacja?”).  
Gdy ta osoba tam wejdzie, jej przeglądarka wyśle nam coś zwanego [*user agent*]({% post_url 2021-06-11-user-agent %}){:.internal}. Krótką informację o&nbsp;systemie i&nbsp;przeglądarce. To normalna część działania internetu.

Tylko że znajoma osoba jako domyślną przeglądarkę ma ustawionego Firefoksa. A&nbsp;ten wysyła jedynie lakoniczne informacje:

<div class="black-bg mono">
... Android 10; Mobile; rv:(<span class="red">NR WERSJI FIREFOKSA</span>) ...
</div>

{:.figcaption}
Informacje sprawdzone na stronie [BrowserLeaks](https://browserleaks.com/ip); zachęcam do porównania sobie na niej różnych przeglądarek.

Nasz plan upadł? Niekoniecznie! Bo możemy jeszcze wykorzystać wbudowaną przeglądarkę.

* Wysyłamy link do naszej strony nie przez Signala, tylko przez Messengera.

  Jest spora szansa, że znajoma osoba niczego nie zmieniała w&nbsp;opcjach; zatem link po kliknięciu otworzy się w przeglądarce wbudowanej.

* **Przeglądarka wbudowana zmienia _user-agenta_. Na takiego, który zawiera w&nbsp;sobie nazwę marki telefonu**.  
  Przynajmniej w&nbsp;przypadku pewnego rozsądnego cenowo Huaweia. Innych nie sprawdzałem.

* ...a że odwiedza stronę należącą do nas, to wysyła jej komplet informacji.  
  W&nbsp;tym *user agenta*.

* ...a że mamy dostęp do serwera, to możemy sprawdzić logi (historię).

  Widzimy w&nbsp;nich, że krótko po odebraniu linku przez znajomą osobę zostaliśmy odwiedzeni przez kogoś z&nbsp;telefonem Huawei, konkretniej [model Y6P](https://www.gsmarena.com/huawei_y6p-10222.php). Przychodzącego z&nbsp;apki od Facebooka.

  <div class="black-bg mono">
  ... Android 10; MED-LX9N Build/<span class="red">HUAWEIMED-LX9N</span> ... <span class="red">FB_IAB</span>
  </div>

* Możemy teraz odpisać: „Ten twój telefon. Niech zgadnę, Huawei Y6P?” :smiling_imp:

A na większą skalę? Właściciele stron mogą analizować takie szczegółowe *user agenty*. Przypisywać konkretnym użytkownikom używane marki telefonów oraz aplikacje, z&nbsp;których korzystają. Tworzyć dokładniejsze profile.  
A potem chociażby decydować na tej podstawie, jak drogi chłam będą nam podsuwać.

## Jak się chronić?

Przede wszystkim korzystajmy z&nbsp;zaufanych aplikacji. Szkoda byłoby pobrać coś szemranego, co zawiera własną wbudowaną przeglądarkę i&nbsp;będzie próbowało czytać nasze hasła bankowe.

W przeciwieństwie do spraw z&nbsp;ostatnich wpisów o&nbsp;apkach -- tutaj nie pomoże nam system pozwoleń. Prawie każda aplikacja wymaga dostępu do internetu.

### Rozpoznawanie zagrożenia

Jak w&nbsp;ogóle się połapać, czy nie jesteśmy przypadkiem zamknięci w&nbsp;cudzym WebView, pod lupą?

Warto pomyśleć nad użyciem przeglądarki innej niż domyślna. Jak Firefox. I&nbsp;jej wystylizowaniem, jeśli jest taka opcja. Możemy na przykład wybrać nietypowy motyw kolorystyczny.

Pisałem wcześniej, w&nbsp;jaki sposób apki mogłyby, we współpracy ze stronami internetowymi, udoskonalać swoje imitacje. Ale do wewnętrznych motywów przeglądarki nie powinny mieć wglądu.  
Jeśli zatem w&nbsp;cudzej apce otworzy nam się coś wyglądającego jak przeglądarka, ale kolory nie pasują... To czas się niepokoić.

{% include info.html
type="Uwaga"
text="Motyw kolorystyczny lepiej ustawić w&nbsp;samej przeglądarce. Systemowy motyw ciemny może bowiem zostać wykryty przez stronki-podglądaczy, a&nbsp;potem użyty do pokazania nam lepszej repliki."
%}

Inna opcja, jeśli nie jesteśmy pewni? Wejdźmy na jakąś (mniej wrażliwą) stronę wymagającą logowania. Jeśli w&nbsp;normalnych warunkach pokazałoby nasze konto, a&nbsp;teraz jest tylko ekran logowania (czytaj: nie jesteśmy zalogowani), to od razu zapalmy czerwoną lampkę w głowie.

Można też sprawdzić wspomnianą [stronkę Felixa K](https://inappbrowser.com/). Powinna wykryć, jeśli ktoś dodał nam do strony kod, którego nie powinno tam być.  
Inna strona: BrowserLeaks (ale tam już musimy wiedzieć, na jakie informacje patrzeć).

### Trzymanie się domyślnej przeglądarki

Wiedząc, że jakaś aplikacja wpycha nas w&nbsp;WebView pod swoją kontrolą, możemy zacząć walczyć. I&nbsp;otwierać linki na swoich zasadach, we własnej przeglądarce.

Niektóre apki dają nam możliwość wyboru. Przykładowo, dla **Messengera**:

* klikamy swoje zdjęcie w&nbsp;górnym lewym rogu,
* wybieramy opcję `Zdjęcia i multimedia` (nieintuicyjnie!),
* zaznaczamy opcję `Otwieraj linki w domyślnej przeglądarce`.

Jeśli apka nie daje nam takiej możliwości w&nbsp;opcjach, to możliwe, że pozwala przynajmniej normalnie kopiować linki.

Żeby to zrobić, przytrzymujemy na linku palec i&nbsp;wybieramy opcję `Kopiuj link` (albo *Odnośnik*, albo coś podobnego; to od apki zależy, jak nazwie opcję i czy ją da).

Następnie zamykamy apkę, otwieramy swoją główną przeglądarkę. Wklejamy link w&nbsp;pasek (często od razu nam to podpowiada). I&nbsp;już! Będziemy poza oczami podglądaczy.

A jeśli mamy przypadki beznadziejne, jak TikTok, które za nic nie chcą nas wypuścić? Pozostaje unikać klikania w&nbsp;linki. Zapamiętywać, co chcemy sprawdzić, i&nbsp;sprawdzać to potem na komputerze, przez ich stronę internetową. 

### Dla autorów stron

A jeśli jesteśmy autorami stron? Możemy rozpoznać, po *user agencie* oraz innych informacjach, czy ktoś nas odwiedza przez wbudowaną przeglądarkę. Przykład wyżej.

Potem można wyświetlić odpowiednie ostrzeżenie. „Znam twój model telefonu, wiem że przybywasz z&nbsp;apki”.  
Można też dopisać, że TikTok, Facebook czy tam inna apka ujawnia te dane całemu internetowi. Taka mała akcja w&nbsp;ramach uświadamiania społeczeństwa :smiling_imp:

I na tym psotnym pomyślę kończę. Mam nadzieję, że żadna udawana przeglądarka nie weźmie Was na przejażdżkę wbrew woli.  
Do zobaczenia w&nbsp;kolejnych wpisach!

