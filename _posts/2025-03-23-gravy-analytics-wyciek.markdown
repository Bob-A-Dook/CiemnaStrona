---
layout: post
title: "Gravy Analytics i megawyciek danych o lokalizacji"
subtitle: "Niedostrzeżony następca Cambridge Analytica?"
description: "Niedostrzeżony następca Cambridge Analytica?"
date:   2025-03-23 21:00:00 +0100
tags: [Afera, Apki, Inwigilacja, Media, Reklamy]
firmy: [Apple, Google, Gravy Analytics]
image:
  path: /assets/posts/inwigilacja/gravy-analytics/gravy-analytics-wyciek-baner.jpg
  width: 1200
  height: 700
  alt: "Fragment mapy, na którym cała Europa jest pokryta czerwonymi punktami odpowiadającymi lokalizacji użytkowników."
---

W połowie stycznia ziścił się prawdziwy koszmar dla cyfrowej prywatności. Spółce Gravy Analytics wyciekły **tysiące gigabajtów danych o&nbsp;lokalizacji smartfonów**. Na pewnym forum hakerskim udostępniono ich malutką próbkę, ale nawet ona dawała wgląd w&nbsp;niejedno ludzkie życie.

Miliony punktów na mapie, łatwo przypisywalnych do poszczególnych użytkowników. Dałoby się zobaczyć jak na dłoni, że kropka odpowiadająca użytkownikowi X123 pojawia się w&nbsp;konkretnym domku na przedmieściach, w&nbsp;śródmiejskim biurowcu, w&nbsp;knajpkach wokół tego biurowca. A&nbsp;kiedyś może w&nbsp;klubie dla swingersów. 

Źródłem danych chomikowanych przez Gravy Analytics były giełdy reklamowe. Które z&nbsp;kolei otrzymywały informacje od elementów reklamowych z&nbsp;niektórych aplikacji. Czasem dość wrażliwych: cyfrowe modlitewniki, Tinder, Grindr... 

Z jakiegoś powodu sprawa, mimo swojej wagi, umknęła uwadze wielu osób. Była wprawdzie opisana na całkiem popularnych portalach, ale po ich relacjach w&nbsp;życiu bym nie pomyślał, że to coś większego.

Nawet media bardziej techniczne, choć wierniej nakreśliły zakres afery, pominęły jedno z&nbsp;głównych źródeł problemu -- **identyfikator reklamowy smartfonów**. Rzecz wredną, a&nbsp;banalnie łatwą do wyłączenia. Podobnie jak dostęp do GPS-a. Gdyby więcej osób poświęciło kilka minut na te dwie rzeczy, to afera by ich nie dotknęła.

Jak to zrobić? I&nbsp;na czym polegała cała ta afera? Już piszę.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/gravy-analytics/gravy-analytics-wyciek-baner.jpg" alt="Fragment mapy, na którym cała Europa jest pokryta czerwonymi punktami odpowiadającymi lokalizacji użytkowników"/>

{:.figcaption}
Źródło: Twitter/X, nitka opisująca aferę. Jeszcze do niej wrócę.

## Spis treści

* [Na początek – jak ochronić prywatność](#na-początek--jak-ochronić-prywatność)
  * [Usuwanie ID reklamowego](#usuwanie-id-reklamowego)
  * [Wyłączanie dostępu do lokalizacji](#wyłączanie-dostępu-do-lokalizacji)
* [Omówienie wrażliwych danych](#omówienie-wrażliwych-danych)
  * [Mapowanie ludzkiego życia](#mapowanie-ludzkiego-życia)
  * [Czarny scenariusz](#czarny-scenariusz)
* [Afera krok po kroku](#afera-krok-po-kroku)
  * [Gravy Analytics i&nbsp;giełdy reklamowe](#gravy-analytics-igiełdy-reklamowe)
  * [Ciepłe relacje z&nbsp;agencjami](#ciepłe-relacje-zagencjami)
  * [Ochłodzenie relacji i&nbsp;wyciek](#ochłodzenie-relacji-iwyciek)
* [Dotknięte aplikacje](#dotknięte-aplikacje)
* [Relacje w&nbsp;polskich mediach](#relacje-wpolskich-mediach)
  * [Media mniej techniczne](#media-mniej-techniczne)
  * [Stronki bardziej techniczne](#stronki-bardziej-techniczne)
  * [Podsumowanie wątku](#podsumowanie-wątku)
* [Jak się chronić – uzupełnienie](#jak-się-chronić--uzupełnienie)

## Na początek – jak ochronić prywatność

Zwykle w&nbsp;swoich wpisach najpierw prezentuję problem, potem rozwiązanie. Tutaj zrobię na odwrót, bo rozwiązanie jest tak szybkie i&nbsp;intuicyjne, że szkoda zwlekać. I&nbsp;daje sporo -- wbrew paru internetowym gugułom jojczącym, że „prywatność już nie istnieje”.

{:.post-meta .bigspace-after}
A gdyby ktoś wolał najpierw jednak poczytać o&nbsp;aferze, to można przeskoczyć do jej opisu. Wedle uznania.

### Usuwanie ID reklamowego

Krótko: we współczesnych smartfonach (i&nbsp;na systemie Android, i&nbsp;iOS) gnieździ się identyfikator reklamowy. Każda apka zawierająca reklamy może do niego sięgnąć.

Identyfikator umożliwia branży reklamowej **łączenie naszych danych z&nbsp;różnych aplikacji**. Odczytując go i&nbsp;oznaczając nim dane, widzą na przykład, że ktoś używał o&nbsp;8:03 aplikacji A, o&nbsp;8:10 aplikacji B, po tygodniu znów A... Czasem dostają też informacje o&nbsp;tym, co dana osoba robiła.

Identyfikator nie zawiera danych wrażliwych, jak imię i&nbsp;nazwisko. Ale to małe pocieszenie, bo z&nbsp;dużej ilości danych anonimowych można niepokojąco łatwo wyciągnąć osobowe.  
Z punktu widzenia prywatności -- coś strasznego. Na szczęście można łatwo wyłączyć dostęp do identyfikatora. Do czego gorąco zachęcam.

Instrukcje opieram na własnych doświadczeniach i&nbsp;paru przewodnikach; polecam w&nbsp;szczególności [ten od *Electronic Frontier Foundation*](https://www.eff.org/deeplinks/2022/05/how-disable-ad-id-tracking-ios-and-android-and-why-you-should-do-it-now) (po angielsku).

{% include details.html summary="Usuwanie ID reklamowego na smartfonach z&nbsp;Androidem"%}
Wchodzimy w&nbsp;`Ustawienia`. Te dotyczące ID reklamowego powinny być w&nbsp;którymś z&nbsp;podanych miejsc:

* `Google > Wszystkie usługi > Reklamy` (jeśli mamy działające Usługi Google),
* `Bezpieczeństwo i prywatność > Ustawienia prywatności > Reklamy`.

  {:.post-meta .bigspace-after}
  Lub ewentualnie `Bezpieczeństwo i prywatność > Więcej ustawień prywatności > Reklamy`; dokładna nazwa opcji może się różnić między smartfonami różnych producentów, ale zawsze powinna być gdzieś w&nbsp;zakładce prywatnościowej.

Następnie klikamy opcję `Usuń identyfikator wyświetlania reklam` (lub coś w&nbsp;tym stylu) i&nbsp;olewamy wiadomości próbujące nas zniechęcić.

{:.figure}
<img src="/assets/posts/google/smartfon-degoogle/ad-id-usuwanie.jpg" alt="Zrzut ekranu pokazujący opcję usuwania identyfikatora reklamowego" width="400px">

{:.post-meta .bigspace-after}
Gdyby w&nbsp;opcjach była jedynie możliwość przywrócenia identyfikatora, to znaczy, że już kiedyś go wyłączyliśmy. Super, w&nbsp;takim wypadku nic nie ruszamy!
{% include details-end.html %}

{% include details.html summary="Usuwanie ID reklamowego na iPhone'ach"%}

Na iPhone'ach identyfikator jest znany pod akronimem IDFA. Nie mając jabłkofona, muszę wierzyć cudzym poradnikom. Zetknąłem się z&nbsp;kilkoma różnymi instrukcjami, być może zależnymi od wersji systemu. Na wszelki wypadek przytoczę wszystkie.

1. Wchodzimy w&nbsp;`Ustawienia > Prywatność > Śledzenie` i&nbsp;odhaczamy `Pozwalaj aplikacjom żądać możliwości śledzenia`. Jeśli kiedyś udzieliliśmy zgód niektórym z&nbsp;nich, to w&nbsp;tym momencie wyświetli się opcja pozwalająca je wycofać. Proponuję skorzystać.

   {:.post-meta .bigspace-after}
   Opieram się na [tym przewodniku](https://spidersweb.pl/2021/04/ios-14-5-idfa-prywatnosc-jak-wylaczyc-sledzenie.html) z&nbsp;2021&nbsp;roku, ale nowsze angielskie wersje się z&nbsp;nim zgadzają.

2. Wchodzimy w&nbsp;`Ustawienia > Prywatność > Reklamy` i&nbsp;zaznaczamy opcję `Ogranicz reklamy śledzące` (ang. *Limit Ad Tracking*). Dla pewności można też kliknąć opcję `Resetuj identyfikator reklamowy`. Gdyby nie dało się go usunąć, to pozostaje resetowanie co pewien czas.

{:.post-meta .bigspace-after}
Być może sposób numer 2&nbsp;dotyczy jedynie starszych wersji systemu; nie ma co się obawiać, gdyby takiej opcji nie było (a&nbsp;gdybyśmy już wyłączyli śledzenie sposobem numer 1).

Według [przewodnika od EFF](https://www.eff.org/deeplinks/2022/05/how-disable-ad-id-tracking-ios-and-android-and-why-you-should-do-it-now), Apple ma również odrębny identyfikator reklamowy, odczytywany tylko przez nich. Nie było go w&nbsp;wycieku Gravy, ale dla pewności i&nbsp;tak bym to wyłączył. W&nbsp;tym celu trzeba wejść w&nbsp;`Ustawienia > Prywatność > Reklamy Apple` i&nbsp;odhaczyć opcję `Spersonalizowane reklamy`.
{% include details-end.html %}

Gdy identyfikator zniknie, to reklamodawcy stracą możliwość łatwego i&nbsp;szybkiego śledzenia użytkowników. Jeden z&nbsp;filarów naszej afery *Gravy Gate* upadnie :smile:

### Wyłączanie dostępu do lokalizacji

W opisywanej aferze istotną rolę odegrał też dostęp do danych lokalizacyjnych. Dlatego warto poświęcić kilka stuknięć w&nbsp;ekran na okiełznanie GPS-a.

{% include details.html summary="Odbieranie dostępu do GPS-a na smartfonach z&nbsp;Androidem"%}

Klikamy w&nbsp;`Ustawienia`, potem `Prywatność`, potem `Menedżer uprawnień`. Tam wchodzimy w&nbsp;zakładkę `Lokalizacja`.

W tej zakładce znajduje się lista aplikacji w&nbsp;podziale na cztery poziomy dostępu do GPS-a: ciągły dostęp, dostęp tylko podczas korzystania, „zawsze pytaj” i&nbsp;brak dostępu. Każdej z&nbsp;aplikacji, po kliknięciu w&nbsp;jej ikonę, można zmienić ustawiony poziom.

{:.post-meta .bigspace-after}
Jak to na Androidzie: dokładne nazwy opcji i&nbsp;poziomów uprawnień mogą się różnić między wersjami systemu i&nbsp;telefonami różnych producentów. Ale ogólne założenia powinny być podobne.

Proponuję trzymać się dwóch trybów: albo całkiem odebrać dostęp, albo wybrać opcję `Tylko podczas korzystania`. O&nbsp;dostępie ciągłym można pomyśleć dopiero w&nbsp;rzadkich przypadkach, gdyby apka odmawiała działania.
{% include details-end.html %}

{% include details.html summary="Odbieranie dostępu do GPS-a na iPhone'ach"%}

Wchodzimy w&nbsp;`Ustawienia > Prywatność i ochrona > Usługi lokalizacji`.

Tam można ustawić każdej z&nbsp;aplikacji poziom dostępu; proponuję`Nigdy` dla większości oraz `Gdy używam aplikacji` dla wybranych.

{:.post-meta .bigspace-after}
Źródło: [przewodnik od Apple](https://support.apple.com/pl-pl/102647).

{%include details-end.html%}

Odbieranie dostępu do ID reklamowego i&nbsp;GPS-a powinno zająć nie więcej niż kilka minut. Idealnie -- można zrobić sobie herbatę/kawusię i&nbsp;wywalczyć prywatność w&nbsp;trakcie czekania, aż nieco ostygnie :coffee: Tyle wystarczy, żeby trafić do grona osób, których afera wokół Gravy by zupełnie nie dotknęła.

...A właśnie, afera. Możecie wziąć w&nbsp;dłonie kawę/herbatę z poprzedniego akapitu i&nbsp;rozsiąść się wygodnie. Będzie straszno.

## Omówienie wrażliwych danych

Na chwilę jeszcze wstrzymam się z&nbsp;informacją o&nbsp;tym, czym było Gravy, skąd miało dane i&nbsp;jakim cudem wypłynęły na widok publiczny. Zacznę od tego, czy wyciek tych danych powinien budzić niepokój.  
O tak, powinien. Dane zawierały między innymi:

* nazwy aplikacji, z&nbsp;których je pozyskano;
* unikalne identyfikatory reklamowe;
* dokładną lokalizację użytkowników;
* znaczniki czasu.
  
  ...czyli dokładne daty i&nbsp;godziny; znaczniki podobno nie pojawiały się przy wszystkich danych, tylko przy mniej więcej połowie.

Identyfikator reklamowy umożliwia przypisywanie różnych danych do tego samego użytkownika. Łącząc go z&nbsp;nazwami, dałoby się na przykład ustalić, że ta sama osoba ma na telefonie jednocześnie modlitewnik i&nbsp;apkę Grindr („homoseksualnego Tindera”). Ups.

Ale samo to jeszcze mieści się w&nbsp;sferze ciekawostek. Gorzej, gdy dołoży się do tego dane lokalizacyjne, które jednoznacznie ukazują, że użytkownik tych dwóch apek często przebywa na terenie kościelnej plebanii. Albo Białego Domu: 

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/gravy-analytics/gravy-geofencing.jpg" alt="Zrzut ekranu, na którym Baptiste pokazuje trochę punktów na mapie połączonych liniami i&nbsp;pisze, że może mapować wędrówki postaci z&nbsp;wydzielonego obszaru."/>

Źródłem powyższego obrazka jest wątek, który opublikował na Twitterze niejaki [Baptiste Robert](https://xcancel.com/fs0c131y/status/1876975966334964076#m). Można tam znaleźć nieco więcej przykładów możliwych nadużyć.

{:.post-meta .bigspace-after}
Gdyby linki nie działały, to można zmienić *xcancel.com* na *x.com*.

{% include info.html
type="Ciekawostka"
text="Wydaje mi się, że w&nbsp;przypadku tego człowieka, może nieco wbrew intuicji, Baptiste jest imieniem, a&nbsp;Robert nazwiskiem.  
Dowody? Zarówno on sam, jak i&nbsp;francuskie tytuły artykułów z&nbsp;jego udziałem stosują właśnie ten szyk; w&nbsp;[zakładce](https://predictalab.fr/#about) na stronie jego firmy jest „Baptiste Robert i&nbsp;Thierry R.” (gdzie Thierry to ewidentnie imię); również według Wikipedii Baptiste [bywa imieniem](https://en.wikipedia.org/wiki/Baptiste_(name)).  
Nie mam stuprocentowej pewności, więc ze swojej strony będę po prostu pisał „Baptiste'a”."
%}

### Mapowanie ludzkiego życia

Z danych lokalizacyjnych, opatrzonych do tego znacznikami czasu, da się ułożyć całe ludzkie historie. **Od współrzędnych GPS-a łatwo przejść do adresów**. Baptiste pokazał na przykład, że jedna osoba przebywała na terenie kompleksu startowego rakiet kosmicznych, a&nbsp;punkty pozwalały prześledzić jej przejazdy między domem a&nbsp;pracą:

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/gravy-analytics/gravy-tracking-space.jpg" alt="Zrzut ekranu pokazujący kilka zdjęć satelitarnych i&nbsp;opisy wskazujące, jak wyglądał dzień osoby, której odpowiadają punkty. Okazuje się, że przebywała na obszarze platformy startowej rakiet kosmicznych."/>

Inny przykład? Gdy punkty na mapie pojawiały się w&nbsp;domach, to dało się łatwo odczytać ich adresy. Dzięki książkom telefonicznym lub innym źrodłom **przejść od adresów do osób**. Zaś przykładowo z&nbsp;*social mediów* odczytać dane osobowe, powiązania rodzinne i&nbsp;życiowe historie:

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/gravy-analytics/gravy-tracking.jpg" alt="Zrzut ekranu pokazujący kilka zdjęć satelitarnych i&nbsp;opisy wskazujące, jak wyglądał dzień osoby, której odpowiadają punkty"/>

Przykłady Baptiste'a są ze Stanów, ale dane pochodziły z&nbsp;całego świata -- wystarczy spojrzeć na początek wpisu i&nbsp;znaczniki pokrywające Europę.

Najstraszniejsze? Udostępniony komplet danych to tylko próbka (1,4 GB). Nieco ponad 30&nbsp;milionów punktów na mapie. **Cały zbiór wykradziony przez hakerów jest ponad 7100&nbsp;razy większy**.

### Czarny scenariusz

Wyżej mamy przykłady niepokojącego wglądu w&nbsp;ludzkie życie i&nbsp;relacje. Ale, żeby jeszcze wyraźniej pokazać zagrożenie: oto teoretyczny scenariusz ataku na osoby zamożne.

Polując na naprawdę grube ryby, cyberstalkerzy mogliby zacząć od mapy i&nbsp;wyłapać punkty bywające w&nbsp;miejscach luksusowych. Takich jak podmiejskie dzielnice willowe, ekskluzywne restauracje, pola golfowe...

Jeden taki punkt, wraz z&nbsp;drugim, regularnie przebywa w&nbsp;pewnej willi od godzin popołudniowych do porannych? Super, zapewne zamożna para, może małżeństwo. Można odczytać, jakie identyfikatory im odpowiadają. Dla każdego z&nbsp;nich wyświetlić wszystkie dane, jakie zebrało o&nbsp;tej osobie Gravy.

I oto widać, że źródłem niektórych z&nbsp;nich była apka randkowa Tinder. Ups.  
Stalker przełącza się teraz na dane lokalizacyjne odpowiadające tej osobie. Widzi, że czasem pojawia się w&nbsp;środku dnia, na krótko, w&nbsp;jakimś hotelu. Albo w&nbsp;godzinach nocnych w&nbsp;cudzym domu. Jeszcze większe ups, ktoś tu będzie szantażowany :smiling_imp:

Pomijam już nawet fakt, że z&nbsp;danych dałoby się odczytać czyjś rytm dnia, zwyczaje i&nbsp;inne informacje pomocne przy planowaniu przykładowego napadu.  
Możliwości jest multum i&nbsp;wszystkie są groźne.

## Afera krok po kroku

Na tym etapie przyda się nieco więcej informacji o&nbsp;kulisach całej afery. W&nbsp;szczególności: czym była firma Gravy Analytics i&nbsp;w jaki sposób pozyskiwała dane.

Spoiler: to nie jest historia pojedynczej firmy, która nie upilnowała danych. Mamy tutaj **zdemaskowanie całego ekosystemu reklam śledzących**.  
Dowód, że pod uspokajającymi sloganami „używamy tylko anonimowych, zagregowanych danych” kryje się zachłanne zbieractwo. Szkodliwe dla ludzi, za to cenione po cichu przez wielkie firmy i&nbsp;organizacje rządowe.

{% include info.html
type="Źródła"
text="Opis obecnych zdarzeń (po angielsku) można znaleźć na stronach portali [*404 Media*](https://www.404media.co/hackers-claim-massive-breach-of-location-data-giant-threaten-to-leak-data/) oraz [*Wired*](https://www.wired.com/story/gravy-location-data-app-leak-rtb/)."
%}

### Gravy Analytics i&nbsp;giełdy reklamowe

W języku angielskim istnieje taki idiom: *ride a&nbsp;gravy train*. W&nbsp;wolnym tłumaczeniu: „wskoczyć na wagon z&nbsp;żarciem”. Oznacza to dobre ustawienie się w&nbsp;życiu, zarabianie niewielkim wysiłkiem. Tak, jakby miało się własną maszynkę do zarabiania kasy.

I Gravy Analytics, zgodnie z&nbsp;nazwą, było taką maszynką. Formalnie -- **brokerem (lub agregatorem) danych**. Czyli w&nbsp;praktyce: podpięli się pod niekończący się strumień danych lokalizacyjnych. Zbierali je w&nbsp;spójne pakiety, które następnie sprzedawali chętnym.

No ale chwila, skąd mieli te dane? W&nbsp;tym miejscu przyda się przyspieszona wycieczka po współczesnym ekosystemie reklamowym:

* jakaś firma postanawia stworzyć aplikację na smartfony;
* myśląc o&nbsp;jej zmonetyzowaniu, trafia na ofertę firmy reklamowej;
* wymóg czerpania zysków z&nbsp;reklam: muszą dodać do swojej aplikacji kod zewnętrzny (tzw. SDK) autorstwa firmy reklamowej;
* dodany kod odczytuje różne informacje na temat użytkowników i&nbsp;wysyła je na **giełdę reklamową**;
* tam, na podstawie wysłanych informacji (oraz tych wcześniej zebranych, umieszczonych pod tym samym ID reklamowym), użytkownik trafia do określonej „szufladki” konsumenckiej;
* algorytm giełdy wybiera którąś z&nbsp;dostępnych reklam przeznaczonych dla tej szufladki;
* reklama zostaje wysłana na telefon i&nbsp;wyświetlona wewnątrz aplikacji.

Z założenia giełda reklamowa miała być jak taki mikser, w&nbsp;którym ciągle coś się dzieje. Jak wielkie, automatyczne centrum recyklingu, w&nbsp;którym automaty segregują wsad, ale nie poświęcają uwagi pojedynczym przedmiotom.  
Reklamodawcy mieli widzieć tylko, że ktoś wziął ich reklamę (i&nbsp;potrąciło im z&nbsp;konta). Autorzy aplikacji mieli widzieć, że zarobili jakiś procent.

...A jednak, w&nbsp;ten czy inny sposób (niestety nie poznałem jeszcze dokładnego mechanizmu), **dane nie zostają na giełdzie, tylko trafiają do brokerów**. Takich jak Gravy. Brokerzy opakowują dane i&nbsp;sprzedają je dalej.

To może wyjaśniać, dlaczego prawie wszystkie firmy zapytane o&nbsp;aferę zgodnie stwierdziły, że nie łączą ich relacje biznesowe z&nbsp;Gravy. Raczej nie kłamią... ale ich słowa są bez znaczenia.

Wina twórców aplikacji polega na tym, że przystali na warunki współpracy polegające na oddawaniu losu użytkowników w&nbsp;ręce cudzego kodu. Gromadzącego dane i&nbsp;wysyłającego je na giełdy.  
Dostali zapewne jakąś obiecankę, że dane będę zanonimizowane, dobrze traktowane i&nbsp;użyte tylko do przydzielenia reklam. I&nbsp;nie drążyli tematu, gdy leciały w&nbsp;świat.

A kto kupował dane opracowane przez Gravy? Jak podaje Baptiste, w&nbsp;danych z&nbsp;wycieku znajdowała się tabela z&nbsp;bazy danych nazwana `customers`. A&nbsp;w niej: nazwy takich firm jak Google, Uber, eBay, Grindr, Babel Street, LiveRamp, Spotify.

{:.post-meta .bigspace-after}
Wprawne oko zauważy, że Grindr pojawił się zarówno w&nbsp;przypadku „dawców”, jak i&nbsp;nabywców danych. Nie widzę sprzeczności -- mogli kupować dane od brokerów, żeby poznać fakty, których nie poznaliby przez apkę (bo np. ludzie nie korzystają z&nbsp;Grindra w&nbsp;pracy). A&nbsp;jednocześnie słać inne dane w&nbsp;ramach typowych partnerstw reklamowych.

A sektor prywatny nie był jedyną grupą docelową. Po dane z&nbsp;Gravy sięgały też ręce rządowe.

### Ciepłe relacje z&nbsp;agencjami

Gravy, choć niewielkie, nie było jakąś jednoosobową działalnością. Ba, mieli nawet własną spółkę zależną o&nbsp;nazwie Venntel i&nbsp;podobnym profilu działalności. Chcąc poznać kontrowersje wokół nich, warto szukać pod obiema nazwami.

Już kilka lat temu w&nbsp;mediach społecznościowych [pojawiały się pytania](https://www.reddit.com/r/AskNetsec/comments/w298mv/how_can_i_block_venntel_gravy_analytics/) o&nbsp;to, jak odbierać dostęp do lokalizacji Venntelowi i&nbsp;Gravy.  
Autor powołuje się na groźny cytat. Nie podał źródła, ale skopiowałem fragment `"came from its contract with Venntel"` (koniecznie w&nbsp;cudzysłowach, żeby szukało całej frazy) i&nbsp;wyszukałem go w&nbsp;DuckDuckGo. Wyskoczyło parę pasujących artykułów, jak [ten z&nbsp;Politico](https://www.politico.com/news/2022/07/18/dhs-location-data-aclu-00046208).

Artykuł wspomina o&nbsp;tym, że dane lokalizacyjne od obu brokerów były kupowane przez agencje rządowe. W&nbsp;ten sposób **agencje obchodziły zakaz śledzenia własnych obywateli**. Po prostu zostawiały to sektorowi prywatnemu i&nbsp;kupowały opracowane przez nich dane.

{% include info.html
type="Ciekawostka"
text="Jedną z&nbsp;firm wymienionych w&nbsp;tym kilkuletnim artykule, na równi z&nbsp;Venntelem, jest niejaka Babel Street. Jej nazwa znajdowała się w&nbsp;tabeli dotyczącej nabywców danych z&nbsp;obecnego wycieku. Może to potwierdzać, że brokerzy handlują też między sobą."
%}

W swoim artykule Politico podlinkowało też treść [ujawnionej prezentacji wewnętrznej](https://www.politico.com/f/?id=00000182-10fd-d06c-afbb-95fdce930000), w&nbsp;której agencja rządowa analizuje przed zakupem produkt Venntela/Gravy.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/gravy-analytics/ad-id-rachunek.jpg" alt="Rachunek, na którym widnieje pozycja, w&nbsp;tłumaczeniu na polski: dane od ad-techu związane z&nbsp;ID reklamowym"/>

Warto zwrócić uwagę na wyróżnioną część tekstu. Słowo `ad-tech` odnosi się do branży reklamowej. Skoro zbiorczo nazywają wszystkie dane <code>Ad-tech <span class="red">ID</span> data</code>, to może to sugerować, że identyfikator reklamowy pełni w&nbsp;nich centralną rolę. 

### Ochłodzenie relacji i&nbsp;wyciek

W 2023&nbsp;roku Gravy połączyło się z norweską spółką Unacast. [Na stronie firmy](https://www.unacast.com/post/unacast-and-gravy-analytics-merge) opublikowali oświadczenie -- zadziwiająco prozaiczny korpobełkot jak na działalność niemalże szpiegowską.

{:.bigspace-after}
> The time has come for a&nbsp;renaissance in the location data and intelligence industry - we are excited to welcome you on this journey

Coś się również popsuło w&nbsp;relacjach z&nbsp;amerykańskimi agencjami, a&nbsp;przynajmniej częścią z&nbsp;nich. 

Pod koniec zeszłego (2024) roku Gravy Analytics oraz inna firma, Mobilewalla, [zostały wzięte na cel](https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-takes-action-against-gravy-analytics-venntel-unlawfully-selling-location-data-tracking-consumers) przez amerykańską FTC (*Federal Trade Commission*; taki odpowiednik polskiego UOKiK-u). Na początku tego roku przedstawili ostateczne żądania, [nakazując firmie](https://natlawreview.com/article/ftc-finalizes-orders-against-data-brokers-over-sensitive-location-data) zaprzestać gromadzenia danych z&nbsp;wrażliwych lokalizacji, usunąć te dotychczas zebrane i&nbsp;działać tylko za zgodą użytkowników.

{% include info.html
type="Wątek poboczny"
text="Zastanawiam się: skoro o&nbsp;działalności Venntela/Gravy było wiadomo wcześniej, ale dopiero po fuzji z&nbsp;Unacastem sprawy ruszyły, to czy działał tu jakiś polityczny parasol ochronny? Niestety mogę tylko spekulować.  
Historia zna przypadki, gdy sądy w&nbsp;USA aktywowały się dopiero po zmianie właściciela. Przykładem pozwy, które [nie tykały firmy Monsanto](/2022/12/24/monsanto-posilac-roundup){:.internal}, a&nbsp;zaczęły się zlatywać po jej przejęciu przez niemieckiego Bayera."
%}

A to dopiero początek ich pecha.  
Gravy, jak to wiele firm, uległo obietnicom składanym przez [*rozwiązania chmurowe*](/cyfrowy_feudalizm/2021/04/07/cyfrowy-feudalizm-fakty#przenoszenie-wszystkiego-do-chmury){:.internal}. Przechowywali swoje dane na cudzych serwerach, w&nbsp;tym wypadku korzystając z&nbsp;Amazon Web Services. I, jak to często bywa, nie zabezpieczyli tych danych w&nbsp;wystarczającym stopniu. I&nbsp;nastąpił wyciek.

Hakerzy opublikowali próbkę danych na rosyjskojęzycznym forum XSS, żądając okupu w&nbsp;zamian za nieudostępnienie pozostałych. I&nbsp;być może ktoś uległ, bo post został usunięty, groźba megawycieku chwilowo odsunięta w&nbsp;czasie.  
Ale skutki afery zostaną z&nbsp;Gravy już do (może rychłego) końca.

## Dotknięte aplikacje

Na stronie  Wired można znaleźć link do [obszernej listy](https://docs.google.com/spreadsheets/d/1Ukgd0gIWd9gpV6bOx2pcSHsVO6yIUqbjnlM4ewjO6Cs/edit?usp=sharing) aplikacji z&nbsp;Androida i&nbsp;iOS, których nazwy znalazły się rzekomo w&nbsp;udostępnionej próbce danych.

Wśród aplikacji były: Tinder, Grindr, MyFitnessPal, Candy Crush, wiele gier mobilnych. Z&nbsp;polskich aplikacji (wyszukałem ciąg `.pl`) mamy na liście Onet Pocztę oraz WP Pocztę. 

{:.post-meta .bigspace-after}
**Dupochron:** nie mogę na sto procent wykluczyć przykładowego dopisania losowych nazw aplikacji przez hakerów. Mogliby w&nbsp;ten sposób sztucznie podbić wartość danych. Tak było niedawno z&nbsp;rzekomymi danymi z&nbsp;pewnej polskiej sieciówki.  
Faktem jest natomiast, że znany portal technologiczny *Wired* udostępnił listę aplikacji znalezionych w&nbsp;wycieku, a&nbsp;na liście były konkretne nazwy.

{% include info.html
type="Ciekawostka"
text="Na liście, oprócz zwykłych czytelnych nazw, można tez zobaczyć formy zapisane z&nbsp;kropkami. Zwykle, choć nie zawsze, podobne do tej głównej nazwy.  
W oficjalnej terminologii Androida to nazwy pakietów (ang. *package names*), takie unikalne nazwy wewnętrzne, którym odpowiada jedna lub więcej nazw czytelnych (czasem różniących się w&nbsp;zależności od języka).  
Przykładowo: nazwa wewnętrzna Tindera to `com.tinder`, ale już Signal (na szczęście nieobecny na tej liście) ma `org.thoughtcrime.securesms`. Nazwę można sprawdzić, odwiedzając [stronkę aplikacji](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms&hl=en-US) w&nbsp;bazie PlayStore i&nbsp;patrząc na link w&nbsp;górnym pasku."
%}

Mogę sobie przykładowo wyszukać na liście słowo `tinder` -- wyskakuje nazwa wewnętrzna `com.tinder`. Wchodząc na PlayStore'a i&nbsp;patrząc w&nbsp;link, mogę zyskać pewność, że istotnie, to oficjalna strona apki Tinder. Nie żadnej podróbki.

Tu z&nbsp;kolei pojawia się ciekawa możliwość. Każda aplikacja ma obowiązek informować, do jakich danych sięga i&nbsp;jakie udostępnia obcym podmiotom. W&nbsp;przypadku danych lokalizacyjnych jest podział na dokładne (zapewne GPS) i&nbsp;przybliżone (zapewne adres IP, dokładny w&nbsp;uproszczeniu co do miasta).

Nieprzypadkowo wybrałem Tindera. Pomijając fakt, że jest znaną aplikacją, ma ciekawą sytuację w&nbsp;swojej polityce prywatności.  
Dostęp do dokładnej lokalizacji jest wymieniony w&nbsp;zakładce mniej groźnej, opisującej zastosowania wewnętrzne apki. Natomiast w&nbsp;zakładce z&nbsp;danymi udostępnianymi obcym podmiotom jest wyłącznie lokalizacja przybliżona.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/gravy-analytics/tinder-dane-lokalizacyjne.jpg" alt="Kolaż ze zrzutów ekranu pokazujący politykę prywatności Tindera. W&nbsp;zakładce na temat dzielenia się danymi widnieje jedynie informacja o&nbsp;danych przybliżonych."/>

Może to oznaczać dwie rzeczy:

* Tinder udostępnia giełdom wyłącznie lokalizację przybliżoną (zapewne odczytaną z&nbsp;adresu IP, czyli w&nbsp;przypadku sieci mobilnej dokładną mniej więcej do miasta);
* Tinder, wbrew publicznej polityce prywatności, udostępnia innym dokładną lokalizację użytkowników.

Która wersja jest prawdziwa? Nie rozstrzygnę, nie mając pod ręką próbki danych z&nbsp;Gravy.

Jest tu natomiast ciekawe wyzwanie dla chętnych mających wgląd w&nbsp;dane: sprawdzić jakąś osobę, przy której źródłem danych jest&nbsp;Tinder. Gdyby odpowiadające jej punkty były ułożone precyzyjniej, niż to możliwe przy adresie IP (czyli na przykład wzdłuż ulicy, którą ktoś jechał), to by oznaczało, że apka udostępnia dokładną lokalizację.

Takie przypadki można porównać z&nbsp;deklaracjami z&nbsp;PlayStore'a i&nbsp;złapać winowajców. Wystarczy jakaś osoba z&nbsp;kopią danych z&nbsp;Gravy chętna na polowanko :smiling_imp:

## Relacje w&nbsp;polskich mediach

Mięso wpisu już za nami, więc teraz można się skupić na wątkach pobocznych. Takich jak sposób pokazania sprawy w&nbsp;mediach.

Jak wspomniałem, na początku całkiem mi umknęła. I&nbsp;to nie tak, że nigdzie o&nbsp;niej nie pisano -- pisano jak najbardziej. Ale **pisano w&nbsp;taki sposób, że wydawała się nieznacząca i&nbsp;lokalna**.

Czas na małą prasówkę. Wyszukałem w&nbsp;DuckDuckGo (bo w&nbsp;Google by mnie zawaliły reklamy) kombinację `"gravy analytics" site:pl` i&nbsp;poczytałem różne artykuły.

### Media mniej techniczne

Wiele mainstreamowych portali zaczerpnęło informacje z&nbsp;[krótkiej notki Polskiej Agencji Prasowej](https://www.pap.pl/aktualnosci/mieli-ukrasc-dane-prawie-150-tys-osob-rosyjscy-hakerzy-w-akcji), opublikowanej 10&nbsp;stycznia o&nbsp;8:58. Skąd to wiem? Czasem oznaczały PAP wprost, czasem zbieżność treści była ogromna. Poza tym tak często działają media od newsów.

Problem z&nbsp;notką jest taki, że skupia się ona tylko na wątku norweskim (bo norweski Unacast, który wchłonął Gravy, zgłosił wyciek w&nbsp;swoim kraju). I&nbsp;ogólnie jest dość lakoniczna. Pojawia się w&nbsp;niej:

* wzmianka, że dane zostały wrzucone na rosyjskim portalu;
* cytat Tobiasa J. z&nbsp;norweskiego urzędu ds. ochrony danych, mówiący o&nbsp;ogromnej skali kradzieży (ale bardzo ogólnie, żadnych liczb);
* nazwa Gravy Analytics i&nbsp;informacja o&nbsp;tym, że pozyskiwali dane;
* informacja, że pod koniec 2024&nbsp;roku firma zawarła ugodę z&nbsp;Federalną Komisją Handlu z&nbsp;USA, bo już wcześniej miała problemy za zbieranie wrażliwych danych.

I to wszystko. Dosłownie kilkanaście linijek, zero linków, brak wyraźnego podkreślenia globalnego charakteru sprawy.

Znane portale zaczęły na potęgę kopiować właśnie tę notkę. Zaś użytkownicy mogli odnieść wrażenie, że to jakiś jeden wyciek z&nbsp;wielu, norweska ciekawostka, rosyjska uszczypliwość. Brak nazw aplikacji, które udostępniały dane. Brak opisów zagrożenia.

{:.post-meta .bigspace-after}
Nie mówiąc już o&nbsp;zupełnym braku porad prywatnościowych; ale na to już straciłem nadzieję w przypadku *mass mediów*.

Przykłady portali kopiujących notkę:

* [Money.pl](https://www.money.pl/gospodarka/incydent-moze-miec-powazne-konsekwencje-dane-norwegow-w-rekach-rosjan-7112737113049856a.html),
* [Onet Podróże](https://podroze.onet.pl/aktualnosci/rosyjscy-hakerzy-ukradli-dane-z-telefonow-norwegow-ogromna-skala/sqjhqqj)
* [Interia](https://wydarzenia.interia.pl/zagranica/news-wielki-atak-rosyjskich-hakerow-w-europejskim-kraju-skala-ogr,nId,7888843)
* [Wp.pl](https://wiadomosci.wp.pl/wykradli-dane-tysiecy-norwegow-potencjalnie-ogromne-zagrozenie-7112623811103456a)
* [Warszawa w&nbsp;Pigułce](https://warszawawpigulce.pl/bezprecedensowy-atak-hakerski-ogromny-wyciek-danych-moze-zagrozic-tysiacom-ludzi-11-01-2025/)

  Tutaj przynajmniej parafrazowanie było nieco bardziej obfite i&nbsp;wyszło 19&nbsp;linijek, do tego drobniejszym tekstem niż na stronie PAP :+1:.  
  Co ciekawe, tydzień później (17.01) wypuścili [kolejny artykuł](https://warszawawpigulce.pl/potezny-atak-hakerski-w-europie-wrazliwe-informacje-z-telefonow-w-niepowolanych-rekach-17-01-2025/). Bardzo podobny do pierwszego, ale ciut dłuższy i&nbsp;dodający wzmiankę, że warto pilnować ustawień dostępu do lokalizacji. Trochę ogólne, ale na tle innych popularnych portali i&nbsp;tak na plus.

* [TVN 24](https://tvn24.pl/biznes/ze-swiata/norwegia-rosyjscy-hakerzy-mieli-ukrasc-dane-prawie-150-tys-norwegow-st8253569).

  Wracamy do powielania notki z&nbsp;PAP. TVN ją wprost oznacza jako źródło, ale, co ciekawe, jako godzinę publikacji mają 6:43 (podobnie parę innych portali). Dwie godziny wcześniej, niż została opublikowana na samej stronie PAP. Jakiś priorytetowy dostęp?

* [RMF24](https://www.rmf24.pl/fakty/swiat/news-dane-wielu-norwegow-wpadly-w-rosyjskie-rece,nId,7888850) -- typowa notka PAP. Pod nagłówkiem była literówka „Opracownie”, już jej nie ma.

  {:.post-meta .bigspace-after}
  Ale w&nbsp;paru innych artykułach [nadal się pojawia](https://duckduckgo.com/?t=ffab&q=%22opracownie%22+site%3Armf24.pl&ia=web) -- tu [przykład](https://web.archive.org/web/20250210004436/https://www.rmf24.pl/regiony/newsamp-12-mln-zlotych-w-grze-cztery-osoby-zatrzymane-poszukiwania-2,nId,7906404).

* [Radio ZET](https://wiadomosci.radiozet.pl/news/europejski-kraj-zaatakowany-przez-rosyjskich-hakerow-skala-moze-byc-ogromna) -- tutaj w&nbsp;miejscu na źródło wpisano „Radio ZET/NRK”, ale treść niemal całkiem się pokrywa z&nbsp;notką PAP.

Spośród mniej technicznych mediów na plus wybił się [artykuł od *pressglobal.pl*](https://pressglobal.pl/Nauka-I-Technologie/czy-handel-danymi-jest-poza-kontrola), będący tłumaczeniem [artykułu](https://www.tagesschau.de/investigativ/br-recherche/standortdaten-apps-datenhandel-100.html) z&nbsp;niemieckiego *Tagesschau*.

{:.post-meta .bigspace-after}
Artykuł został wprawdzie opublikowany w&nbsp;dziale o&nbsp;technologii, ale sam portal należy raczej do tych ogólnych.

Daje on trochę konkretów, przykłady aplikacji niemieckich (Focus, WetterOnline). Dający do myślenia przykład kobiety, której dane zdrowotne ustalono na podstawie lokalizacji -- pewnej kliniki.  
Ponadto artykuł jako jeden z&nbsp;niewielu (również spośród technicznych!) wskazuje na rolę identyfikatora reklamowego. Jest rozmowa z&nbsp;urzędem ochrony danych, jest ogólna sugestia dotycząca patologii branży reklamowej. Oraz informacja, że **z danych mogą korzystać też niemieckie służby wywiadowcze**.

### Stronki bardziej techniczne

Być może lepszym źródłem -- celniej wskazującym zagrożenie i&nbsp;środki zaradcze -- będą portale ściślej związane ze sprawami informatycznymi?  
Istotnie, zrobiły w&nbsp;temacie lepszą robotę, jeśli chodzi o&nbsp;pokazanie światowej skali wycieku. Ale ich porady były na tyle ogólne, że raczej mało kto z&nbsp;nich skorzystał.

[Android.com.pl](https://android.com.pl/tech/870765-atak-rosyjskich-hakerow-norwegia/) po prostu podał dalej notkę PAP. W&nbsp;ramach miłej niespodzianki: dwa linki do innych spraw z&nbsp;wyciekami w&nbsp;tle.

[iMagazine](https://imagazine.pl/2025/01/15/wyciek-danych-gravy-analytics-naraza-miliony-uzytkownikow-iphoneow/) -- zwięźle, ale treściwie. Jest o&nbsp;dużej skali problemu, o&nbsp;możliwości deanonimizacji, przykłady trzech aplikacji. Porada dotycząca usunięcia ID reklamowego teoretycznie jest, ale w&nbsp;formie tak ogólnej, że trudno w&nbsp;tym dostrzec konkretną funkcję do odhaczenia:

> Użytkownicy, którzy wyłączyli śledzenie aplikacji na iPhone’ach, nie byli dotknięci wyciekiem.

[CD Action](https://cdaction.pl/newsy/dane-o-dokladnej-lokalizacji-milionow-osob-trafily-do-sieci-winny-atak-na-serwery-brokera-gravy) -- plus za powołanie się na wątek Baptiste'a i&nbsp;podkreślenie grozy sytuacji (wzmianka o&nbsp;tym, że w&nbsp;danych była lokalizacja osób z&nbsp;baz wojskowych).  
Ale środków zaradczych zero. Do tego z&nbsp;artykułu można wyciągnąć wniosek, że to była wyłącznie norweska sprawa (cytat z&nbsp;oświadczenia złożonego do ich urzędu).

[Antyweb](https://antyweb.pl/gravy-analytics-wyciek-lokalizacja) -- skala sprawy oddana dość wiernie, wymieniają nazwy aplikacji. Jest porada dotycząca ogólnego wyłączenia śledzenia (ale tylko na iPhone'ach).

[OneTech](https://onetech.pl/dane-lokalizacyjne-milionow-uzytkownikow-iphone-i-android-wykradzione-przez-hakerow/) -- dość szybko pojawiają się porady, i&nbsp;to sensowne: najlepiej nie udzielać dostępu do lokalizacji, a&nbsp;jeśli już trzeba, to najwyżej przybliżony. Ale z&nbsp;ostatnią poradą się nieco zagalopowali:

> Warto też zainstalować dobry program antywirusowy. Może nie uchroni przed wszystkim, ale przynajmniej ostrzeże przed niektórymi zagrożeniami.

Rada brzmi z&nbsp;pozoru sensownie, ale w&nbsp;przypadku tej afery nic by nie dała, bo działanie dodatków reklamowych było teoretycznie niezłośliwe. Raczej trudno sobie wyobrazić, że antywirus oflaguje mainstreamowego Tindera czy MyFitnessApp, nieprawdaż?

{% include info.html
type="Ciekawostka"
text="Nawet gdyby jakiś antywirus na smartfona był na tyle miły, że oznaczałby zbieranie danych jako złośliwe zachowanie, miałby bardzo ograniczone możliwości.  
**Na smartfonach antywirusy nie mają szczególnych przywilejów** i&nbsp;często opierają się na prostym rozpoznawaniu niedobrych aplikacji po nazwach. W&nbsp;najlepszym wypadku: mogłyby analizować ruch sieciowy, pozwalając się ustawić jako VPN-y (tylko po to, żeby mieć większy wgląd).  
Ale co by to dało, skoro ruch jest szyfrowany, więc antywirus widziałby jedynie nazwy stron docelowych? A&nbsp;te nazwy (np. `static.losowa-apka.com`) mogą brzmieć jak coś potrzebnego do działania?  
Pomijam już fakt, że czasem to same antywirusy okazują się zbieraczami danych, a&nbsp;pod latarnią bywa najciemniej. Na liście aplikacji z&nbsp;wycieku widnieje choćby Avast (`com.avast.android.mobilesecurity`)."
%}

[IT Hardware](https://ithardware.pl/aktualnosci/najwiekszy_wyciek_rosja_lokalizacja_miliony-37985.html) podaje więcej faktów (jak nazwa forum, na którym udostępniono dane -- XSS), ale nie ma żadnych porad prywatnościowych ani środków zaradczych.  
Artykuł podlinkowali też [na Wykopie](https://wykop.pl/link/7626365/to-moze-byc-najwiekszy-wyciek-w-historii-rosjanie-wykradli-lokalizacje-milionow), ale zebrał mało polubień. Do tego nazwę Gravy Analytics z&nbsp;zajawki przycięło w&nbsp;niefortunnym miejscu, prowokując śmieszkowy komentarz, który zgarnął więcej łap w&nbsp;górę niż artykuł. I&nbsp;na tym wieści o&nbsp;wielkim wycieku się skończyły :roll_eyes:

[Dobre Programy](https://www.dobreprogramy.pl/reklamy-sczytuja-lokalizacje-na-liscie-tinder-i-nie-tylko,7113144273419008a) -- niby też podchodzą pod Onet, ale dali dużo kompletniejszy artykuł niż ten ze strony newsowej. Jest cytowanie artykułu z&nbsp;Wired, nazwy aplikacji, wzmianka o&nbsp;umywaniu rąk przez firmy oznaczone w&nbsp;wycieku.  
Za to w&nbsp;poradach jest o&nbsp;zastrzeganiu numeru PESEL (fajne, ale w&nbsp;tym przypadku bez zastosowania, apki go nie wymagały). Plus porady sensowne, ale ogólnikowe:

> warto co do zasady udostępniać w&nbsp;internecie możliwie mało informacji o&nbsp;sobie, zaś listę uprawnień w&nbsp;aplikacjach ograniczać do minimum

[Numag.pl](https://numag.pl/gigantyczny-wyciek-danych-z-gravy-analytics/) bardzo na plus -- podkreślenie skali, wymienione przykłady aplikacji, informacja o&nbsp;tym, że źródłem są giełdy reklamowe. Porady szczegółowe wprawdzie tylko odnośnie iPhone'a, ale wspominają zarówno o&nbsp;wyłączeniu ID, jak i&nbsp;dostępu do lokalizacji.

### Podsumowanie wątku

Polskie media popularne w&nbsp;moim odczuciu całkiem spaliły temat, przedstawiając go tak, jakby był jakąś lokalną norweską sprawą. Być może to jeden z&nbsp;czynników, przez które cała sprawa przeszła bez echa.

Portale techniczne zrobiły lepszą robotę, ale głównie pod względem opisywania problemu, jego źródeł i&nbsp;skali. Nie wykorzystały natomiast okazji do pokazania, krok po kroku, prostych rozwiązań.

**Prawie nikt nie wspomniał o&nbsp;identyfikatorach reklamowych**. Mimo że ich ucięcie to bardzo proste i&nbsp;intuicyjne rozwiązanie przynajmniej części problemów.

Swoją drogą ogólna cisza medialna wydaje się zjawiskiem nie tylko polskim -- na YouTubie, jeśli uszereguje się filmy znalezione pod hasłem `gravy analytics` [według wyświetleń](https://www.youtube.com/results?search_query=gravy+analytics&sp=CAM%253D), najczęściej oglądany ma nieco poniżej 100&nbsp;tys. wyświetleń. Kolejny po nim nieco ponad 2000, resztę już mało kto oglądał.

W porównaniu z&nbsp;taką na przykład [aferą XZ](/cyfrowy_feudalizm/2024/03/31/xz-backdoor){:.internal}, która dotyczyła *niezrealizowanego* ataku, te zasięgi są śmiesznie małe. Sprawa mogłaby zostać nazwana *Cambridge Analytica 2.0* i&nbsp;wywołać masowy bojkot ekosystemu reklam śledzących. Zamiast tego zgasła jak iskra.

Zmowa milczenia? Celowy *blackout* informacyjny? Wątpię.

Powiedziałbym raczej, że brak popularności wynika ze smutnego faktu, że **ludziom, nawet z&nbsp;branży, spowszedniały informacje o&nbsp;wyciekach danych**. I&nbsp;kiedy słyszy się „Wielki wyciek z&nbsp;firmy X”, zwłaszcza gdy jej nazwa jest nieznana, to łatwo przeoczyć olbrzyma.  
A takie znieczulenie jest, moim zdaniem, jeszcze gorsze niż teoretyczna cenzura.

## Jak się chronić – uzupełnienie

Na początku wpisu napisałem, jak wyłączać identyfikator reklamowy i&nbsp;uprawnienia aplikacji do GPS-a. Te proste działania zaradzą większości problemów, jakie przyniosło Gravy. Jeśli tego jeszcze nie zrobiliście, to zachęcam, żeby wykonać [opisane tam kroki](#na-początek--jak-ochronić-prywatność){:.internal}.

Ale firm analitycznych i&nbsp;brokerów danych jest więcej; dlatego osoby chętne mogą pójść o&nbsp;krok dalej.

{:.post-meta .bigspace-after}
Poniższe porady stworzyłem z&nbsp;myślą o&nbsp;Androidzie, ale część może się odnosić też do jabłkofonów.

Przede wszystkim warto pamiętać o&nbsp;tym, żeby **wyłączać Bluetooth i&nbsp;wyszukiwanie hotspotów, gdy nie korzystamy z&nbsp;tych funkcji**. Można tak sobie ustawić pstryczki na „ściągalnym z&nbsp;góry” menu na ekranie głównym, żeby mieć do nich szybki dostęp, a&nbsp;potem wyrobić sobie nawyk ich wyłączania.

Dlaczego? Ano dlatego, że hotspoty wokół nas oraz tak zwane *beacony Bluetooth* również pomagają [ustalać, w&nbsp;jakiej jesteśmy lokalizacji](/apki/2023/07/15/sledzenie-lokalizacji){:.internal}. Nawet gdy wyłączy się GPS-a.

W przypadku telefonów z&nbsp;Androidem silnie zrośniętych z&nbsp;Google'em warto pamiętać o&nbsp;paru innych rzeczach:

* poza podstawową funkcją Wi-Fi trzeba wyłączyć też osobny pstryczek odpowiadający za używanie hotspotów do lokalizacji;
* usługom Google Play trzeba odbierać dostęp do GPS-a przez osobne menu;
* nie da się domyślnymi narzędziami odbierać dostępu do internetu konkretnym aplikacjom, ale można to zrobić przez apkę-firewalla jak RethinkDNS.

Wszystkie te rzeczy opisałem w&nbsp;[przewodniku po odgooglowywaniu telefonu](/2024/02/03/smartfon-degoogle){:.internal}. Gorąco zachęcam do przeczytania!

I na koniec jeszcze raz, bo nigdy za wiele: trzonem afery, oprócz GPS-a, był identyfikator reklamowy. Rzecz łatwa i&nbsp;szybka do wyłączenia. Jak wiele innych zagadnień -- **prywatność to spektrum, a&nbsp;pierwsze kroki są osiągalne dla każdego**. Mówienie, że nie da się jej chronić, to bzdura.

