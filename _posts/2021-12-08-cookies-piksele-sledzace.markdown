---
layout: post
title:  "Internetowa inwigilacja 8 – pliki cookies i piksele śledzące"
subtitle: "„Już cię u kogoś widziałem...”"
description: "Opowieść o kawie i ciasteczkach"
date:   2021-12-08 08:30:00 +0100
tags: [Internet, Inwigilacja]
firmy: [Facebook, Google, Twitter]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: 
   path: /assets/posts/third-party-cookies/facebucks-large.jpg
   width: 1200
   height: 700

image-width: 1200
image-height: 700
---

W poprzednich wpisach pokazałem, że za każdym razem, gdy odwiedzamy jakąś stronę internetową, nasza przeglądarka wysyła jej „właścicielom” różne informacje w&nbsp;tzw. *nagłówkach HTTP*.

Ostatnio omówiłem dokładniej jedną z&nbsp;tych informacji, *pliki cookies*, zwane potocznie *ciasteczkami*. Krótkie fragmenty tekstu, które przeglądarka najpierw otrzymuje, potem przechowuje, a&nbsp;na koniec pokazuje tej samej stronce, od której je dostała.

Poprzedni wpis skupił się na ogólnym działaniu plików cookies oraz na ich mniej groźnym zastosowaniu -- logowaniu na swoje konto.  
Teraz natomiast przejdziemy do **plików cookies ze stron zewnętrznych (ang. _third party cookies_)**. Używanych głównie w&nbsp;celu śledzenia naszych wędrówek po internecie. 

Moim zdaniem to jeden z&nbsp;najważniejszych wpisów w&nbsp;całej serii.  
Zobaczymy tu, w&nbsp;jaki sposób dwa filary internetu -- nagłówki oraz pliki cookies -- zostały wykorzystane do masowego zbierania danych o&nbsp;użytkownikach.

Postaram się opisać wszystko w&nbsp;sposób przystępny, zaczynając od historyjki, żeby nawet nowi czytelnicy się w&nbsp;tym odnaleźli. Tym niemniej zachęcam do przeczytania wpisów [o&nbsp;nagłówkach HTTP]({% post_url 2021-01-11-internetowa-inwigilacja-1-podstawy %}){:.internal} oraz [o&nbsp;plikach cookies]({% post_url 2021-10-22-pliki-cookies %}){:.internal}, jeśli chcemy mieć więcej kontekstu.

# Spis treści

* [Historyjka o kawie i ciasteczkach](#historyjka-o-kawie-i-ciasteczkach)
  * [Pierwszy kontakt – korpo](#pierwszy-kontakt--korpo)
  * [Drugi kontakt – targi pracy](#drugi-kontakt--targi-pracy)
  * [Trzeci kontakt – kawiarnia](#trzeci-kontakt--kawiarnia)
  * [Epilog](#epilog)
  * [Powrót do rzeczywistości](#powrót-do-rzeczywistości)
* [Kulisy śledzenia](#kulisy-śledzenia)
  * [Jak wyglądają elementy śledzące](#jak-wyglądają-elementy-śledzące)
  * [Dlaczego piksele?](#dlaczego-piksele)
* [Jak się chronić?](#jak-się-chronić)
  * [Instalacja dodatku blokującego](#instalacja-dodatku-blokującego)
  * [Wyłącznik na Facebooku](#wyłącznik-na-facebooku)
* [Co przyniesie przyszłość](#co-przyniesie-przyszłość)

## Historyjka o kawie i ciasteczkach

W niektórych wpisach porównywałem internet do sieci placówek pocztowych. Ale tym razem użyję innej analogii, która lepiej mi pasuje. Będzie to fikcyjna historyjka z&nbsp;życia.

Wyobraźmy sobie, że wykonujemy pracę biurową w&nbsp;dużym mieście (czyt. jesteśmy korpoludkiem). Tym miastem jest internet.

# Pierwszy kontakt -- korpo

Zatrudniając się w&nbsp;naszym korpo (*zakładając konto*) dostaliśmy identyfikator na smyczce. To *plik cookie*. Dowolna rzecz, jaką dostaliśmy od określonej firmy i&nbsp;jaką pokazujemy tylko jej przedstawicielom.

Jak choćby recepcjoniście. Po wejściu do korpo za każdym razem dajemy mu firmowy identyfikator. On przykłada go do czytnika, sprawdza ważność. Jeśli jest OK, to nas wpuszcza.  
W tej prostej interakcji biorą udział dwie strony. My, odwiedzający, jesteśmy pierwszą. Recepcjonista drugą.

Jeśli recepcjonista chce, może sobie za naszymi plecami zanotować, że weszliśmy. O&nbsp;godzinie tej i&nbsp;tej, pokazując identyfikator taki i&nbsp;taki.  
Ogólnie każda osoba, z&nbsp;którą wejdziemy w&nbsp;interakcję (*serwer*) może to notować. A&nbsp;my się o&nbsp;tym nie dowiemy. No ale trudno, żyje się dalej.

Gdyby nie istniało coś takiego jak pliki cookies od stron trzecich, to historyjka mogłaby się skończyć w&nbsp;tym miejscu.

Ale tak nie jest. Pewnego dnia wita nas niespodzianka. Zaraz za wejściem rozstawił się punkt z&nbsp;darmową kawą!  
Nasze korpo uznało, że poprawi morale i&nbsp;tymczasowo zaprosiło do siebie popularną sieć kawiarni -- nazwijmy ją **Facebucks**. Nie bez znaczenia był fakt, że Facebucks oferuje takie gościnne występy za darmo.

{:.bigspace}
<img src="/assets/posts/third-party-cookies/facebucks-small.jpg" alt="Plastikowy kubek z&nbsp;kawą. jest zwieńczona bitą śmietaną i&nbsp;polana karmelem. Na kubku znajduje się okrągłe zielone logo z&nbsp;napisem Facebucks (oparte na połączeniu motywów Facebooka i&nbsp;Starbucksa). Pośrodku loga widnieje fragment wszechwidzącego oka, jak z&nbsp;amerykańskich dolarów. Za kubkiem widać ciasteczko z&nbsp;kawałkami czekolady."/> 

Pracownik obsługujący punkt z&nbsp;kawą jest w&nbsp;korpo gościem, więc to tak zwana trzecia strona (*third party*). Daje nam kawę, a&nbsp;oprócz niej kartę do zbierania pieczątek! Taki drobny upominek od osoby z&nbsp;zewnątrz to właśnie **ciasteczko od strony zewnętrznej**.

Nie pokazywaliśmy pracownikowi identyfikatora naszego korpo, więc nie zna naszych danych osobowych. Ale i&nbsp;tak notuje za naszymi plecami:

{:.bigspace}
*W siedzibie firmy Zdziw Corp, dnia A&nbsp;o godzinie B, dałem kartę numer 123420 osobie o&nbsp;blond włosach, zielonych oczach, mówiącej po polsku. Chyba tu pracuje.*

W świecie przeglądarek odpowiednikiem naszych widocznych cech są informacje z&nbsp;nagłówków HTTP.  
Nasz wygląd jest jak atrybut `User-Agent`. Język, jakim mówimy, jak atrybut `Accept-Language`. Ujawniamy te informacje podczas każdej interakcji z&nbsp;innymi.

# Drugi kontakt -- targi pracy

Nasze życie toczy się dalej. Przefarbowujemy włosy na białe -- bo wyszedł nowy sezon „Wiedźmina”, trzeba iść za trendami -- i&nbsp;zaczynamy nosić niebieskie szkła kontaktowe (zapamiętajcie, to ważne!).

Z tymi nowymi cechami odwiedzamy targi pracy, bo myślimy o&nbsp;zmianie korpo. Wchodzimy tam po okazaniu kupionego wcześniej biletu. On również jest jak plik cookie, tylko że od organizatora targów.  
A my jesteśmy dyskretni i&nbsp;każdej firmie pokazujemy tylko tę rzecz, jaką od nich dostaliśmy. Nasze korpo nie dowie się, że odwiedziliśmy targi. A&nbsp;targi nie dowiedzą się, gdzie pracujemy. Idealny układ.

Ale cóż to widzimy? Stoisko z&nbsp;kawą od Facebucksa! Targi ich tu wpuściły, żeby umilali czas odwiedzającym (no i&nbsp;-- nie ukrywajmy -- bo oferują takie gościnne występy za darmo. Oficjalnie po to, żeby nieść światu dobrą kawę). 

Stoisko obsługuje nieznana nam brunetka. Kiedy pokazujemy swoją kartę na pieczątki, to zerka na jej numer, wpisuje coś w&nbsp;terminal. W&nbsp;końcu podaje nam kawę, mówiąc: „Też&nbsp;myślałam o&nbsp;niebieskich soczewkach!”.

Odchodzimy z&nbsp;lekką konsternacją, macając palcem w&nbsp;okolicy oka. Aż tak widać, że nosimy soczewki? Przecież wyglądały naturalnie.  
A może... jakimś cudem wiedziała, że mieliśmy wcześniej inny kolor oczu? Ale odpędzamy od siebie tę głupią myśl.

Tylko że to nie była głupia myśl. Za kulisami wszystkie placówki Facebucksa korzystają ze wspólnej bazy i&nbsp;dzielą się informacjami. Każda karta na pieczątki (*plik cookie*, przypominam) ma unikalny numer przypisany konkretnej osobie. A&nbsp;nasze pozostałe cechy -- jak wyglądamy, gdzie i&nbsp;kiedy nas widziano -- trafiają do bazy jako informacje uzupełniające.

Teraz na przykład pracownica notuje za naszymi plecami:

{:.bigspace}
*Osoba numer 123420, dnia X&nbsp;o godzinie Y, odwiedziła targi pracy. Ma teraz białe włosy i&nbsp;niebieskie oczy. Reszta danych bez zmian.  
Analiza: prawdopodobnie chce zmienić obecną pracę, w&nbsp;Zdziw Corp. Ma soczewki kontaktowe i&nbsp;używa białej farby do włosów. Możliwe zainteresowanie serią „Wiedźmin”.*
  
Nie znają naszych danych osobowych, jesteśmy tylko numerem. Ale nadal mogą do tego numeru przypisywać różne obserwacje, powoli tworząc nasz **profil-cień (ang. _shadow profile_)**.

# Trzeci kontakt -- kawiarnia

A teraz wyobraźmy sobie, że kawiarnia Facebucks nas skusiła swoją ofertą specjalną. Wyrabiając imienną kartę członkowską, dostaniemy za darmo karmelowe latte bez mleka!

Tylko że takiego czegoś nie oferują małe mobilne punkty, a&nbsp;jedynie ich własne firmowe lokale. Odwiedzamy jeden z&nbsp;nich (*wchodzimy na stronę główną*).

Żeby wyrobić imienną kartę, musimy pokazać swój dowód osobisty i&nbsp;kartę z&nbsp;pieczątkami. I&nbsp;jeszcze tylko szybki podpis pod zgodą na przetwarzanie danych. Nie czytamy, bo przecież tak dobrze im z&nbsp;oczu patrzy.

W momencie, gdy podamy kartę na pieczątki razem z&nbsp;dowodem, za kulisami następuje **łączenie danych**. Cały profil-cień, budowany przez małe punkty z&nbsp;kawą dla anonimowego numeru, zyskał właśnie konkretną tożsamość. Imię, nazwisko, numer dowodu.

My tymczasem, w&nbsp;błogiej nieświadomości, konsumujemy naszą słodko-mdławą nagrodę.

# Epilog

Kiedy przychodzimy do naszego korpo, znowu widzimy punkt z&nbsp;kawą od Facebucksa. Tym razem obsługuje go inny, zupełnie nam obcy sprzedawca.  
Mimo to wystarczy mu rzut oka na numer naszej karty i&nbsp;na terminal, żeby zwrócił się do nas po imieniu, jak do kogoś znajomego:

„Cześć, Anon(-ka)! Słyszeliśmy, że myślisz o&nbsp;zmianie pracy. Mamy tu kilka ofert od naszych partnerów biznesowych, polecam gorąco.  
Aha, a&nbsp;może chcesz kupić płyn do soczewek?”.

I tak oto, z&nbsp;lekkim dreszczem, poznajemy odpowiedź na pytanie, jakim cudem Facebucksowi opłaca się odwiedzać za darmo każde możliwe miejsce. Ich biznes nigdy nie opierał się na kawie -- tylko na ciasteczkach. Posypanych danymi.

# Powrót do rzeczywistości

Mechanizm działania internetowych gigantów jest bardzo podobny jak kawiarni Facebucks z&nbsp;historyjki.

Tworzą coś, co by się przydało wielu mniejszym stronom. Udostępniają to za darmo. Nie jest to może kawa, ale też bywa pożądane:

* Facebook -- oferują przyciski, które po kliknięciu zostawiają stronie polubienia;
* Twitter -- opcję łatwego umieszczania treści tweetów na stronach zewnętrznych;
* Google -- cały arsenał darmowych narzędzi. Google Fonts, Google Analytics, reCaptcha...

Właściciele stron z&nbsp;tego korzystają i&nbsp;dodają te „elementy gościnne” do siebie. Efekt uboczny: gdy odwiedzamy takie strony, to dowiadują się o tym nie tylko one, ale również właściciele internetowych korporacji.

A ci goście goszczą w&nbsp;wielu miejscach.  
Przykładowo: skrypty od Google Analytics już w&nbsp;2009 roku znajdowały się na ponad połowie z&nbsp;10 000 najpopularniejszych stron. A&nbsp;w ostatnich latach? Według strony analizującej ruch w&nbsp;sieci, *w3techs.com*:

> Google Analytics jest wykorzystywane **przez 56,7% wszystkich stron internetowych**, co oznacza że jego udział w&nbsp;segmencie narzędzi do analizy ruchu wynosi 86,3%.

{:.figcaption}
Źródło: [raport w3techs.com](https://w3techs.com/technologies/overview/traffic_analysis) (tłumaczenie moje).

Na drugim miejscu plasuje się narzędzie Facebooka, *Facebook Pixel*, używane na 11,3%&nbsp;analizowanych stron.

Taka popularność sprawia, że podczas przeciętnego spaceru po internecie spotkamy zwykle przynajmniej kilka elementów analitycznych, zapewne od któregoś z&nbsp;cyfrowych gigantów.

Jeśli jesteśmy zalogowani na swoje konto na którejś z&nbsp;wielkich stron (czyt. po wejściu w&nbsp;odpowiedni adres -- *facebook.com*, *gmail.com* itp. -- widzimy swoje dane, a&nbsp;nie ogólny ekran logowania), to znaczy że nosimy ze sobą ich pliki cookies.

Kiedy je nosimy, elementy gościnne pochodzące z&nbsp;tej samej strony będą nas rozpoznawać.  
Będą wiedzieli, że byliśmy tu i&nbsp;tam, o&nbsp;porze takiej i&nbsp;takiej. Wszystkie te informacje mogą analizować i&nbsp;porównywać z&nbsp;istniejącymi schematami, szufladkując nas w&nbsp;odpowiedniej przegródce dla reklamodawców.

Istnieje wiele metod rozpoznawania użytkowników, sam je opisywałem w&nbsp;poprzednich wpisach. Ale strony nawet nie muszą po nie sięgać, jeśli użytkownicy sami im się przedstawiają. **Pliki cookies to takie internetowe odpowiedniki legitymacji albo dowodów osobistych**.

Były ogólne rozważania, więc po nich tradycyjnie czas na coś konkretniejszego. Pokażę, czym są piksele śledzące, bardzo ściśle związane z&nbsp;plikami cookies.

## Kulisy śledzenia

Tu już będzie szczypta techniki, całe kilka linijek HTML-a z&nbsp;objaśnieniami. Przeżyjemy? :wink:

# Jak wyglądają elementy śledzące

Przedstawiam Wam wyjątkowo prostą stronę. Zawiera dwa obrazki z&nbsp;podpisami. Jeden z&nbsp;Ciemnej Strony, jeden z&nbsp;Wikipedii. W&nbsp;przeglądarce wygląda tak:

{:.figure .bigspace}
<img src="/assets/posts/third-party-cookies/stronka-przyklad.jpg" alt="Zrzut ekranu pokazujący dwa obrazki. Jeden to logo Ciemnej Strony, drugi to tekst 'Just an example'. Nad pierwszym z&nbsp;nich widać tekst 'mój obrazek, a&nbsp;nad drugim 'cudzy obrazek'."/>

Natomiast jeśli zajrzymy w&nbsp;kod strony, zobaczymy coś takiego:

```html
<html>
 <body>

  <p>Mój obrazek:</p>
  <img src="moja-ikona.png"/>

  <p>Cudzy obrazek:</p>
  <img src="https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/Example.jpg"/>

 </body>
</html>
```

Zielony tekst po `<img src=` to źródła dwóch wyświetlanych obrazków.  
Zauważmy, że mamy dwa osobne rodzaje! W&nbsp;pierwszym przypadku to po prostu nazwa pliku, *moja-ikona.png*. Odnosi się do obrazka trzymanego w&nbsp;tym samym folderze co główna strona.

Natomiast **źródłem drugiego pliku jest link do obcej strony** -- *commons.wikimedia.org*. To z&nbsp;niej został pobrany obrazek z&nbsp;tekstem „Just an example”.

Wyobraźmy sobie, że cała ta strona z&nbsp;dwoma obrazkami wisi sobie gdzieś w&nbsp;internecie, na przykład pod adresem *example.com*.

Gdybyśmy weszli w&nbsp;link do niej, mielibyśmy wrażenie, że od razu „pojawiła” nam się kompletna strona. Ale to iluzja, po prostu internet jest szybki.  
W rzeczywistości dostajemy stronkę „na raty”, a&nbsp;za kulisami dzieją się następujące rzeczy:

1. Przeglądarka wysyła do *example.com* prośbę o&nbsp;stronę główną.

   Przy okazji wysyła parę informacji o&nbsp;sobie, jak przy każdej internetowej interakcji. Wśród tych informacji mogą być pliki cookies.

2. Dostaje stronę. Dokładniej: ten sam kod, który widzicie wyżej. Analizuje go i&nbsp;zauważa tam linki do dwóch obrazków.
3. Wysyła do *example.com* prośbę o&nbsp;pierwszy z&nbsp;obrazków, który również jest bezpośrednio od niej.

   Do tej prośby, jak do każdej innej, są załączone pewne podstawowe informacje. Wśród nich również mogą być pliki cookies. Ale nie są szczególnie groźne, bo w&nbsp;końcu w&nbsp;punkcie 1 przeglądarka już wysłała informacje tej samej stronce.

4. Wysyła do *wikimedia.org* prośbę o&nbsp;drugi z&nbsp;obrazków. Również załączając komplet informacji. Mogą być wśród nich pliki cookies.

   ...Zresztą „mogą” to zbyt zachowawcze stwierdzenie. Po otwarciu narzędzi przeglądarki i&nbsp;zakładki `Ciasteczka` widzimy, że one tam są. W&nbsp;liczbie sześciu:

   <img src="/assets/posts/third-party-cookies/wikimedia-pliki-cookies.jpg" alt="Zrzut ekranu pokazujący zakładkę 'Ciasteczka' i&nbsp;listę kilku plików cookies. Treść niektórych z&nbsp;nich zakryto."/>

Gdyby za portalem *wikimedia.org* stała jakaś organizacja chcąca śledzić nasz ruch, to wykorzystałaby te ciasteczka z&nbsp;czwartego punktu do rozpoznania nas. Zaś informacje dodatkowe oraz fakt, na jakiej stronie i&nbsp;o jakim czasie byliśmy, trafiłyby do naszej kartoteki.

Ale to luźne rozważania, bo akurat Wikimedia szanuję i&nbsp;ich nie posądzam. Najważniejszy wniosek z&nbsp;tej części jest prostszy: od strony technicznej **element śledzący może być dowolną rzeczą, która ma w&nbsp;atrybucie `src` link do obcej strony**. 

{%include info.html
type="Porada"
text="Jeśli chcemy zobaczyć, do jakich źródeł zwraca się nasza przeglądarka, możemy nacisnąć `Ctrl+Shift+I` (jak *Irena*), żeby otworzyć narzędzia przeglądarki. Następnie wchodzmy w&nbsp;zakładkę `Sieć` i&nbsp;w razie potrzeby odświeżamy stronę.  
Każda z&nbsp;pozycji na wyświetlonej liście to osobny element, o&nbsp;który poprosiła przeglądarka."
%}

# Dlaczego piksele?

Napisałem wyżej, że element śledzący może być dowolną rzeczą. Firmom śledzącym zależy jedynie na tym, żeby był pobierany z&nbsp;ich strony, a&nbsp;link do niego gościł na stronach cudzych.
  
Mogliby oferować link do filmiku. Albo do „Damy z&nbsp;łasiczką” w&nbsp;cyfrowej postaci. Albo do dowolnych innych multimediów. Nada się wszystko, byle pochodziło od nich.  
Oni jednak wolą przyoszczędzić. Jaka jest najmniejsza możliwa rzecz, jaką mogą zaproponować naszej przeglądarce, żeby ta wysłała im dane? Odpowiedź: to obrazek o&nbsp;wymiarach 1&nbsp;na&nbsp;1. Czyli piksel!

W ten sposób rozwiązaliśmy zagadkę. **W&nbsp;pikselach nie ma nic wyjątkowego, są po prostu najmniejszym możliwym elementem zewnętrznym**.

Tym, co umożliwia śledzenie, jest tak naprawdę sama „zewnętrzność” elementu, sprawienie żeby był pobierany od firmy śledzącej. Jego wygląd to detal bez większego znaczenia. Zresztą prawdopodobnie i&nbsp;tak go nie zobaczymy, bo będzie ukryty.

Piksele, filmiki czy obrazy Leonarda... Jakiejkolwiek formy nie przyjęłyby elementy śledzące, warto się chronić przed wścibskim wzrokiem ich właścicieli. Opiszę teraz, w&nbsp;jaki sposób możemy to zrobić.

## Jak się chronić?

Przypomnijmy: śledzenie opisane w&nbsp;tym wpisie polega na tym, że przeglądarka dostrzega link do obcego elementu i&nbsp;ochoczo go pobiera, razem z&nbsp;ciasteczkami.  
Zatem gdybyśmy sprawili, że będzie ignorowała niektóre elementy (albo przynajmniej nie przechowywała od nich ciasteczek), to pokonamy ten mechanizm.

W praktyce można to osiągnąć przez zainstalowanie dodatku do przeglądarki. Będzie porównywał elementy zewnętrzne ze znanymi czarnymi listami. Jeśli zobaczy coś, co mu się nie spodoba, to tego nie pobierze.

# Instalacja dodatku blokującego

Instalacja dodatku wydaje się najłatwiejszym rozwiązaniem, więc to na tym się skupię. Mam trzy, które osobiście sprawdziłem i&nbsp;polecam:

* **uBlock Origin**

  Koniecznie *Origin*, nie samo *uBlock*!  
  Jeśli czytaliście kilka moich ostatnich wpisów, to już możecie mieć lekkie *deja vu*, bo nieraz wspominałem o&nbsp;tym dodatku :wink:  
Ale po prostu nie sposób go nie wymienić w&nbsp;kontekście elementów śledzących. To jedno z&nbsp;najskuteczniejszych narzędzi w&nbsp;walce z&nbsp;nimi.  
Tutaj znajdziecie [mój wpis na jego temat]({% post_url 2021-10-21-ublock-origin %}){:.internal}. A&nbsp;tutaj [jego stronę główną](https://ublockorigin.com/).

* **AdNauseam**

  Zbudowany na bazie uBlock Origin, ale z&nbsp;dodatkowym bajerem. Chowa reklamy przed naszym wzrokiem, a&nbsp;ich stronom macierzystym wysyła informację zwrotną, że je kliknęliśmy :smiling_imp:  
  Jest z&nbsp;nim trochę zachodu, jeśli używamy Chrome'a i&nbsp;pokrewnych przeglądarek, bo został zbanowany. Trzeba go pobrać i&nbsp;zainstalować ręcznie, co nie jest trudne, ale to nadal dodatkowe kroki. Z&nbsp;kolei na takim Firefoksie instalacja jest bezproblemowa.  
Znajdziecie go [tutaj](https://adnauseam.io/).

* **Privacy Badger**

  Ma mniej opcji niż dwa wcześniej wspomniane dodatki, ale ta prostota może być jego atutem. Po prostu go instalujemy i&nbsp;o nim zapominamy, a&nbsp;reklam robi się mniej.  
Można go pobrać [ze strony Electronic Frontier Foundation](https://privacybadger.org/).

  {:.figure}
<img src="/assets/posts/third-party-cookies/privacy-badger-okno.jpg" alt="Zrzut ekranu pokazujący menu Privacy Badgera. Widać na nim kilka poziomych suwaków, mogących przyjmować jedną z&nbsp;trzech pozycji, ustawionych jeden pod drugim. Po ich lewej stronie widać nazwy stron internetowych, których elementy zostały zablokowane." width="400px"/>

  {:.figcaption}
  Menu Privacy Badgera. Suwaki w&nbsp;czerwonym kolorze oznaczają, że w&nbsp;całości zablokowano pobieranie zewnętrznego elementu. Te w&nbsp;żółtym oznaczają, że go pobrano, ale nie zapisano jego plików cookies.

Nie wykluczam, że są inne fajne dodatki blokujące. Ale na pewno lepiej unikać tych, które biorą udział w&nbsp;programie *Acceptable Ads* (AdBlock, AdBlock Plus, stary uBlock). Przepuszczają wybrane reklamy, a&nbsp;zatem również zawarte w&nbsp;nich elementy śledzące.

Dobry dodatek to nie wszystko. Powinien mieć też przeglądarkę, która pozwoli mu rozwinąć skrzydła. Na pewno **taką przeglądarką nie jest Chrome, który stoi po stronie śledzących reklam**. Warto go zmienić.  
Jeśli nie macie takiej opcji, to trudno, już lepszy Chrome z&nbsp;dodatkiem blokującym niż Chrome bez niczego.

Przeglądarką, która lubi się z&nbsp;dodatkami blokującymi, a&nbsp;przy tym sama daje pewną domyślną ochronę, jest Firefox (potrafi na przykład [automatycznie blokować Google Analytics](https://www.searchenginejournal.com/google-analytics-is-blocked-by-firefox-mozilla-explains-why/311471/#close)). Sam używam i&nbsp;polecam.

Można też użyć [przeglądarki Brave](https://brave.com/), która podobno daje jeszcze silniejszą ochronę domyślną. Acz jej akurat nie testowałem, czeka w&nbsp;kolejce.

# Wyłącznik na Facebooku

Zainstalowanie dodatku blokującego przynosi wielorakie korzyści i&nbsp;powinniśmy to zrobić w&nbsp;pierwszej kolejności. Nic nie stoi natomiast na przeszkodzie, żeby to uzupełnić o&nbsp;rozwiązania szczegółowe.

Niektóre duże strony -- zapewne pod naciskiem unijnych przepisów -- udostępniają własne menu, pozwalające wyłączyć łączenie danych z&nbsp;naszego głównego konta z&nbsp;tymi pozyskanymi przez elementy śledzące ze stron zewnętrznych.  
Przykładem takiej strony jest Facebook.

Żeby wyłączyć jego elementy śledzące, wchodzimy na [podstronę dotyczącą aktywności poza Facebookiem](https://www.facebook.com/off_facebook_activity).  
(Najlepiej przez komputer; spójrzcie też na pasek z&nbsp;adresem, żeby się upewnić, że to prawilna strona Facebooka, a&nbsp;nie jakaś podpucha :wink: ).

Tam, po prawej stronie, mamy menu. Klikamy w&nbsp;nim `Więcej opcji` u&nbsp;dołu, potem wybieramy `Zarządzaj przyszłą aktywnością` i&nbsp;odznaczamy co trzeba. Jeśli wolicie formę obrazkową, to służę:

{:.bigspace}
<img src="/assets/posts/third-party-cookies/facebook-odlaczanie-aktywnosci.jpg" alt="Zrzut ekranu pokazujący opcje, jakie należy kolejno klikać w&nbsp;menu Facebooka. Wykrzyknikiem oznaczono zdanie widoczne tuż nad ostatnim wyłącznikiem i&nbsp;mówiące, że w&nbsp;tym wypadku logowanie przez Facebooka do zewnętrznych stron będzie niemożliwe"/>

Zatrzymajmy się na moment przy zdaniu, które wyróżniłem wykrzyknikiem. Fejsik mówi nam, że jeśli wyłączymy łączenie danych z&nbsp;tymi zewnętrznymi (czyli przez pliki cookies), to stracimy opcję „Zaloguj przez Facebooka”.

Oczywiście nadal będziemy mieli dostęp do Fejsa. Tym niemniej **istnieją nieliczne strony, które dopuszczają tylko logowanie przez FB** zamiast tradycyjnego; spotkałem się kiedyś choćby z&nbsp;takim hotspotem. W&nbsp;takim wypadku pstryknięcie wyłącznikiem może nam nie być na rękę.

Ale wydaje mi się, że jeśli jakaś strona nie potrafi nam zapewnić normalnego logowania przez e-mail, tylko musi nas uzależniać od amerykańskich gigantów, to i&nbsp;tak nie zasługuje na naszą obecność. Zatem klikamy `Wyłącz`.

## Co przyniesie przyszłość

Jako zwykli użytkownicy możemy po prostu zainstalować dodatek, zmienić przeglądarkę i&nbsp;żyć dalej. Ale warto wiedzieć, że **za kulisami od wielu lat trwa konflikt w&nbsp;sprawie plików cookies** i&nbsp;ich losy mogą różnie się potoczyć.

Już kiedyś mieliśmy unijne przepisy nakazujące informować użytkowników, że strona zbiera ciasteczka. Niestety przyniosły one tylko wkurzające banery z&nbsp;informacjami, które zaczęliśmy odruchowo zamykać.

Nieco ostrzejsze przepisy weszły na poziomie Unii parę lat temu, wraz z&nbsp;dyrektywą **GDPR (w Polsce znaną jako RODO)**. Od teraz nie wystarczyło informowanie użytkowników o&nbsp;fakcie dokonanym -- muszą wprost wyrazić zgodę na śledzenie ich aktywności. W&nbsp;dodatku organizacje ds. ochrony danych zyskały możliwość nakładania kar finansowych.

Przechodząc z&nbsp;sektora publicznego w&nbsp;prywatny: sam Google ogłosił, że planuje [usunąć z&nbsp;Chrome'a](https://privacysandbox.com/) wsparcie dla ciasteczek ze stron zewnętrznych. W&nbsp;ten sposób cały mechanizm śledzenia z&nbsp;dnia na dzień przestałby istnieć.

Czyżby giganta tknęło sumienie?  
Optymista by chciał, ale realista powie raczej, że Google stał się już na tyle potężny, że ma lepsze źródła informacji. Usunięcie tej metody śledzenia podbiłoby mu PR i&nbsp;być może wykosiło mniejszych konkurentów, którzy są od niej bardziej zależni.  
Po co mu przybliżone dane z&nbsp;szerszego internetu, gdy może mieć dokładne -- z&nbsp;Androida, Chrome'a oraz własnych stron, dobrowolnie odwiedzanych przez użytkowników?

Innym argumentem przeciw dobrej woli Google'a jest to, że **planuje wprowadzić w&nbsp;Chromie zmiany, które zmniejszą skuteczność dodatków blokujących** (o&nbsp;czym [alarmuje twórca uBO](https://github.com/uBlockOrigin/uBlock-issues/issues/338#issuecomment-496009417)).

Poza tym w&nbsp;miejsce ciasteczek Google proponuje reklamodawcom własny system, *FLoC*. Zintegrowany z&nbsp;przeglądarką, niezależny od stron internetowych. Automatycznie, rzekomo w&nbsp;sposób anonimowy, rozdzielający ludzi na różne kategorie, do których będą kierowane odmienne reklamy.

{% include info.html
type="Ciekawostka"
text="Nazwa *FLoC* to rozwinięcie pewnego technicznego skrótu, ale kryje się pod nią dość ciekawa dwuznaczność -- identycznie brzmiące angielskie *flock* to między innymi określenie na stado owiec."
%}   

Propozycja spotkała się z&nbsp;oporem, ponieważ to kolejny krok do uczynienia internetu mniej otwartym, a&nbsp;bardziej zależnym od Google'a.  
[Wśród przeciwników są autorzy Wordpressa](https://www.theregister.com/2021/04/19/wordpress_core_contributor_proposes_treating/), najpopularniejszego silnika do tworzenia blogów. Zapowiedzieli, że domyślnie będą wyłączali opcję łączenia wordpressowych stron z&nbsp;Google'owym systemem.

Jak się to wszystko skończy? Zmianą ducha czasu i&nbsp;zniknięciem ciasteczek ze stron zewnętrznych? Przekształceniem ich w&nbsp;coś innego, trudniejszego do zwalczenia? Czy też kontratakiem korporacji i&nbsp;jeszcze większym obłożeniem internetu elementami śledzącymi?

Czas pokaże! Na pewno dołożymy do zmian swoją cegiełkę, chodząc po sieci z&nbsp;dodatkami blokującymi.

Tym wpisem kończę część „Internetowej inwigilacji” poświęconą informacjom, jakie nasza przeglądarka wysyła automatycznie, zanim w&nbsp;ogóle dostaniemy stronę internetową.

Teraz ta strona w&nbsp;końcu do nas dotarła, można ją odpakować jak prezent na Mikołajki.  
A w&nbsp;niej możemy znaleźć elementy interaktywne napisane w&nbsp;języku JavaScript. Dające mnóstwo możliwości... również jeśli chodzi o&nbsp;śledzenie.

To ten język będzie tematem kolejnego wpisu z&nbsp;serii. Do usłyszenia!
