---
layout: post
title:  "Internetowa inwigilacja 9 – JavaScript, cz.1"
subtitle: "„Na pewno mówisz prawdę?”"
description: "„Na pewno mówisz prawdę?”"
date:   2022-05-02 16:45:00 +0100
tags: [Internet, Inwigilacja, Podstawy]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
---

W większości wpisów z&nbsp;serii „Internetowa inwigilacja” pisałem o&nbsp;tym, co wysyła nasza przeglądarka przy każdym kontakcie z&nbsp;właścicielami odwiedzanych stron. Zanim w&nbsp;ogóle otrzymamy „zamówioną” stronę internetową.

A teraz -- po ponad roku, odkąd zacząłem pisać -- ta strona wreszcie do nas dotarła. Ładna, współczesna, animowana. Interaktywna. 

Ta interaktywność potrafi jednak być pułapką. Za kulisami często odpowiada za nią **JavaScript -- język programowania internetu**.  
Który ma różne sposoby, żeby wybadać kim jesteśmy. Sprawdzić, czy wysyłane przez nas informacje zgadzają się z&nbsp;rzeczywistością. A&nbsp;na koniec powiadomić o&nbsp;swoich wnioskach stronę-matkę.

To bardzo złe wieści dla naszej prywatności, ale całkiem niezłe dla tych czytelników, którzy już czuli rutynę. JavaScript przynosi dużo nowości, egzotyki, nietypowych metod śledzenia. Poznajmy go!

Bardziej kreatywne zastosowania zostawię na kolejne wpisy, a&nbsp;teraz zobaczymy prostsze informacje. Taki wpis przejściowy.  
Ale niech was to nie zwiedzie. Nawet pierwszy rzut oka na możliwości JavaScriptu może wystarczyć, żeby zrobiło nam się odrobinę nieswojo.

{:.post-meta .bigspace-below}
Wpis zawiera parę przykładów kodu, ale swobodnie można go przeczytać z&nbsp;zerową znajomością JavaScriptu.

## JavaScript w&nbsp;kontekście

Wróćmy na chwilę do naszej analogii pocztowej, przewijającej się przez całą serię. Streszczając:

* Nasza przeglądarka jest jak poczta; my tylko mówimy, z&nbsp;kim się chcemy skontaktować, a&nbsp;oni wszystko ogarniają za kulisami.
* Jeśli chcemy otrzymać od kogoś odpowiedź (*stronę internetową*), musimy najpierw sami wysłać list z&nbsp;prośbą.
* Na każdy taki list jest naklejona etykieta/wizytówka z&nbsp;podstawowymi informacjami na nasz temat (*nagłówki HTTP*).  
Widnieje na niej nasz pseudonim (*user agent*), adres (*adres IP*) i&nbsp;parę innych bajerów.
* Możemy otrzymać odpowiedź w&nbsp;formie listu lub paczki z&nbsp;dowolną zawartością. Może tam być między innymi JavaScript.

Ten JavaScript to często niegroźny interaktywny gadżet. Otrzymamy go i&nbsp;zostaje z&nbsp;nami. Tak jak wbudowana pozytywka z&nbsp;niektórych kartek z&nbsp;życzeniami, która potrafi grać melodyjkę.

Czasem jednak trafi się „zły” JavaScript. Na przykład taki, który **jest w&nbsp;stanie wysyłać nasze dane osobie, od której go dostaliśmy**. Bez naszej zgody i&nbsp;wiedzy.

Gdybyśmy szukali analogii z&nbsp;życia, to można traktować go jak AirTaga lub innego rodzaju nadajnik śledzący, wysyłający komuś naszą lokalizację. Albo tresowanego gołębia pocztowego, który po otwarciu klatki podkrada nam coś z&nbsp;biurka i&nbsp;leci z&nbsp;tym do swojego właściciela.

Dla wzrokowców naszykowałem parę schematów. Na początku mamy normalną, zdrową komunikację. Po lewej nasz laptop, po prawej serwer.

<img src="/assets/posts/javascript-tracking/internet-schemat.jpg" alt="Schemat złożony z&nbsp;dwóch pasków. Na obu z&nbsp;nich po prawej stronie znajduje się laptop, a&nbsp;po lewej serwer. Na pierwszym pasku widać strzałkę idącą od laptopa do serwera, a&nbsp;nad nią ikonę paczki z&nbsp;naklejoną etykietą. Na pasku pod spodem ta sama paczka leży obok ikony serwera, a&nbsp;od serwera w&nbsp;stronę laptopa odchodzi strzałka z&nbsp;ikoną kartki z&nbsp;niebieskim globem, częściowo zakryta żółtym prostokątem z&nbsp;napisem 'JS'."/>

{:.figcaption}
Ikonki z&nbsp;serwisu Flaticon: [laptop](https://www.flaticon.com/free-icons/laptop) autorstwa *vectorsmarket15*, [serwer](https://www.flaticon.com/free-icons/server) autorstwa *Smashicons*, [strzałka](https://www.flaticon.com/free-icons/down-arrow) autorstwa *Freepik*. Aranżacja moja.

Dostaliśmy stronkę w&nbsp;zamian za wizytówkę/etykietę z podstawowymi danymi. Można lekko kręcić nosem, bo z&nbsp;poprzednich wpisów już wiemy, ile da się z nich odczytać... No ale taki jest internet. Coś za coś.

Jednak jeśli trafi nam się „wścibski” JavaScript, to może odczytać parę informacji z&nbsp;naszego komputera i&nbsp;jeszcze raz skontaktować się z nadawcą. Zazwyczaj wysyłając dokładniejsze szczegóły niż te, które sami ujawniliśmy w&nbsp;pierwszym kroku.

<img src="/assets/posts/javascript-tracking/javascript-schemat.jpg" alt="Kolejny schemat złożony z&nbsp;dwóch pasków, ponownie na każdym z&nbsp;nich znajduje się laptop i&nbsp;serwer. Na ekran laptopa nałożono ikonę kartki z&nbsp;globem symbolizującą stronę internetową. Na pierwszym pasku widać żółtą strzałkę wychodzącą od laptopa do serwera, a&nbsp;nad nią ikonę z podpisem 'info' i&nbsp;miniaturką laptopa. Blisko początku strzałki widać napis 'JS'. Drugi pasek schematu nie zawiera strzałki, natomiast obok serwera widać dwie ikony: paczki z&nbsp;poprzedniego schematu oraz ikonę 'info' z&nbsp;górnego paska."/>

A jak wygląda ten cały JavaScript i&nbsp;co kryje się pod ikonką *INFO* z&nbsp;obrazka? Temu poświęcimy aktualny wpis.

# Szczypta kodu

JavaScript to jeden z&nbsp;wielu języków programowania. Jest zwięzły, ma stosunkowo prostą składnię, jest bardzo elastyczny. I&nbsp;zawiera różne niuanse, które przystosowują go do tworzenia interaktywnych dokumentów.

{% include info.html type="Ciekawostka"
text ="Gdzieś mogło Wam się obić o&nbsp;uszy, że oprócz JavaScriptu istnieje też taki język jak Java.  
Te dwa języki nieraz się ludziom mylą. Do tego stopnia, że popularne są anegdoty o&nbsp;rekruterach, którzy dopiero na rozmowie kwalifikacyjnej odkrywali, że właśnie zmarnowali swój i&nbsp;cudzy czas.   
A samo podobieństwo nazw podobno wynika z&nbsp;[układów między firmami](https://stackoverflow.com/questions/2018731/why-is-javascript-called-javascript-since-it-has-nothing-to-do-with-java). Pierwotnie JS nazywał się *Mocha*, ale jego twórcy zaczęli współpracę z&nbsp;firmą Sun, właścicielami Javy. Zaś ci, w&nbsp;zamian za pewne korzyści, chcieli zmiany nazwy na taką, która promowałaby ich produkt.
"%}

Spośród dziesiątków innych języków programowania ten wyróżnia się jednym: postawiły na niego przeglądarki. Dlatego można go uznać za *język programowania internetu*.
 
Chcemy zobaczyć, jak on wygląda? Proszę bardzo, krótki przykład inspirowany moim dawnym wpisem na temat parametrów w&nbsp;linkach. Nie musicie tego zapamiętywać.

```javascript
var full_link = window.location.href;
document.getElementById("params").innerHTML = full_link;
```

* `window` i&nbsp;`document`, zaznaczone fioletowym kolorem, to zmienne z&nbsp;domysłu udostępnione przez przeglądarkę. My tylko do nich sięgamy.
* `var` oznacza, że tworzymy jakąś własną zmienną, tutaj o&nbsp;nazwie *full_link*.
* Kropki pozwalają uzyskać dostęp do „wnętrza” różnych elementów albo do ich „zdolności”. Można je łączyć w&nbsp;zwięzłe łańcuszki.

Jeśli chodzi o&nbsp;ogólne działanie:

1. pierwsza linijka „pyta” przeglądarkę, jaki jest link do oglądanej właśnie strony;
2. druga linijka każe znaleźć na obecnej stronie element z&nbsp;właściwością `id="params"` i&nbsp;wstawić do jego wnętrza link z&nbsp;poprzedniej linijki.

Dla naszych potrzeb wystarczy informacja, że **JavaScript ma możliwość podpytywania przeglądarki o&nbsp;pewne informacje, a&nbsp;przeglądarka ochoczo się nimi dzieli**.

Zamiast drugiej linijki, umieszczającej link na stronie, moglibyśmy oczywiście mieć kod wysyłający go komuś wścibskiemu. Wrócę do tego pod koniec wpisu.

## JavaScript jako łapacz kłamczuchów

# Zdobywanie informacji z&nbsp;nagłówków 

JavaScript ma dostęp do większości rzeczy z&nbsp;naszej „etykiety” (*nagłówków HTTP*), o&nbsp;których już wspominałem w&nbsp;ramach „Internetowej inwigilacji”:

* referera,
* informacji o&nbsp;urządzeniu (*user agenta*),
* parametrów zawartych w&nbsp;linku,
* plików cookies,
* ...i innych danych z&nbsp;„wizytówki”.

Nie ma dostępu do adresu IP; mówiąc bardzo ogólnie, tkwi on na nieco innym poziomie niż reszta danych.

Ale -- zapyta ktoś -- czy w&nbsp;ogóle warto się tym przejmować? Nasz komputer i&nbsp;tak to ujawnia przy pierwszym kontakcie. Więc co to zmieni, że potem JavaScript odczyta to samo?  
Faktycznie; jeśli kontrolujemy serwer, na którym znajduje się strona, to możemy poznać te informacje jeszcze wcześniej. Ale nie każdy administrator strony posiada taką kontrolę.

Tak jest chociażby z&nbsp;blogiem, który właśnie czytacie -- moje pliki znajdują się na serwerach Githuba, a&nbsp;ja nie mam wglądu w&nbsp;to, kto o&nbsp;nie prosił. Nie będę wiedział, czy liczba czytelników jest jedno- czy dwucyfrowa :wink:

Ale gdyby nagle zachciało mi się zbierać informacje o&nbsp;ludziach, mógłbym dodać do swojej strony skrypty analityczne. Wysyłające informacje do jeszcze innego serwisu, gdzie już mógłbym je podejrzeć.

Możemy z&nbsp;tego wynieść naukę, że **brak władzy właściciela nad serwerem nie jest dla nas gwarancją prywatności**. Nadal miałby sposób, żeby podejrzeć informacje o&nbsp;nas.


# Podpytywanie przeglądarki o&nbsp;możliwości

Jak wspomniałem przy pierwszym przykładzie JS-a, przeglądarki udostępniają mu pewne funkcje albo informacje na życzenie.  
Wystarczy krótki fragment kodu, żeby na przykład wypisać na stronie wszystkie możliwości, jakimi chwali się nasza przeglądarka (`navigator`):

```javascript
for (i in navigator)
{
  document.write('<br />navigator.' + i + ' = ' + navigator[i]);
}
```

{:.figcaption}
Źródło: *[quirksmode.org](https://www.quirksmode.org/js/detect.html)*.

Jeśli zajrzycie na podlinkowaną stronę, zobaczycie dość obszerną listę możliwości. 61&nbsp;w przypadku mojego nowego nabytku, przeglądarki Brave.

Warto zauważyć, że przeglądarka przeglądarce nierówna. **Niektóre udostępniają funkcje, których próżno szukać w&nbsp;innych**.  
Wchodząc na powyższą stronę z&nbsp;różnych przeglądarek, możemy zaobserwować, czym się wyróżniają. Jakiejś szczególnej dyskrecji to nie ma:

* Firefox udostępnia JavaScriptowi funkcję `navigator.mozGetUserMedia`  
  (*moz* jak *Mozilla*, czyli ich firma-właściciel),
* Brave udostępnia `navigator.brave`.

Różnice występowałyby także między nowszymi i&nbsp;starszymi wersjami tej samej przeglądarki -- w&nbsp;końcu każda z&nbsp;nich dodaje na bieżąco nowe funkcje.

W swoim [starym wpisie]({% post_url 2021-06-11-user-agent %}){:.internal} na temat *user agenta* (czyli m.in. informacji o&nbsp;tym, jakiej używamy przeglądarki) ostrzegałem przed samodzielną zmianą i&nbsp;wpisywaniem przeglądarki całkiem innej niż nasza:

{:.bigspace}
> krótkie ostrzeżenie -- zbyt brawurowa zmiana *user agenta* może nawet osłabić naszą prywatność.

Wynikało to właśnie z&nbsp;faktu, że istnieje JS. Gdyby mógł zerkać do jakiejś wielkiej listy przeglądarek oraz ich funkcji, **byłby w&nbsp;stanie dość łatwo zweryfikować, przez co ktoś _naprawdę_ przegląda stronę**.

A fakt, że dana przeglądarka przedstawiała się jako inna, byłby bardzo mocnym czynnikiem wyróżniającym kogoś z tłumu.  
Jeśli nie chcemy się wyróżniać, to już lepiej być nieco rzadszym, ale standardowym Firefoksem, niż *TYM* lisem chytrusem, który przedstawia się jako Chrome.

{:.figure}
<img src="/assets/posts/javascript-tracking/javascript-unmask.jpg" alt="Dwa przerobione panele z&nbsp;kreskówki Scooby Doo. Pierwszy z&nbsp;nich pokazuje postać w&nbsp;masce ducha, przed którą stoi blondyn Fred. Na masce widnieje logo Chrome'a, zaś na koszulce Freda napis JS. Na drugim panelu, już po ściągnięciu maski, Fred trzyma ją w&nbsp;dłoni i&nbsp;widać prawdziwą twarz drugiej postaci. Jest nią logo przeglądarki Firefox." width="500px"/> 

{:.figcaption}
Popularny mem na podstawie kreskówki Scooby Doo, przeróbka moja.

# Dawanie przeglądarce zadań

Same nazwy funkcji to tylko wierzchołek góry lodowej.

Nawet gdyby jakaś przeglądarka bardziej się przyłożyła do udawania innej -- i&nbsp;na przykład udostępniała funkcje-wydmuszki o&nbsp;takich samych nazwach -- JavaScript wciąż miałby możliwość powiedzieć „sprawdzam”.  
Może na przykład kazać przeglądarce stworzyć jakiś element, a&nbsp;potem coś z&nbsp;nim zrobić.

```javascript
!!document.createElement('canvas').getContext
```

{:.figcaption}
Źródło: [artykuł](https://docs.microsoft.com/en-us/archive/msdn-magazine/2011/september/building-apps-with-html5-no-browser-left-behind-an-html5-adoption-strategy) jeszcze z&nbsp;2011 roku.

W tym przykładzie zadanie dla przeglądarki składa się z&nbsp;dwóch kroków:

1. Musi stworzyć element `canvas`; element specjalny, który został dodany do standardu HTML nieco później  
   (i służy do tego, żeby umieszczać na nim elementy graficzne; sama nazwa *canvas* to po angielsku *płótno*).  
2. Musi użyć funkcji `getContext`, którą ten element powinien mieć.

Jeśli przeglądarka jest starsza i&nbsp;nie wie nic o&nbsp;elemencie `canvas` ani jego możliwościach, to jej odpowiedzią będzie komputerowy odpowiednik „lol, ale o&nbsp;co ci chodzi?”. A&nbsp;skrypt, który kazał wykonać zadanie uświadomi sobie, że ma do czynienia ze starowinką.

Przykład z&nbsp;elementem *canvas* ma już swoje lata i&nbsp;obecnie praktycznie każda przeglądarka zdałaby ten test. Ale standardy stale idą naprzód. Kiedyś *canvas* było nowością, w&nbsp;przyszłości może to być jakieś *metaverseCanvas*.

# Wysłanie informacji w&nbsp;świat

Gdyby działanie JavaScriptu było ograniczone do strony, w&nbsp;której jest osadzony, to wszystko byłoby w&nbsp;porządku. Dawałby nam interaktywność, nie szpiegując nas przy tym.

Ale jest inaczej. Stronki internetowe coraz częściej są ładowane dynamicznie; autorzy przeglądarek i samego JS-a dokładają starań, żeby komunikacja była jak najprostsza. Aktualnie **wysłanie informacji w&nbsp;świat to kwestia kilku linijek kodu**.

Przedstawiam nieco dłuższy fragment JS-a. Jak zwykle nie trzeba go rozumieć, zresztą większość to szablonowy tekst:

```javascript
let xhr = new XMLHttpRequest();

let json = JSON.stringify( informacje_o_nas );

xhr.open("POST", stronka_nasza_lub_obca)
xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

xhr.send(json);
```

{:.figcaption}
Źródło: *[javascript.info](https://javascript.info/xmlhttprequest)*, z&nbsp;moimi drobnymi zmianami.

Wystarczą nam trzy fakty:

1. `XMLHttpRequest` to kolejna rzecz domyślnie udostępniana przez przeglądarkę. Daje możliwość wysyłania informacji przez JS-a.
2. `JSON` to dość zwięzły i&nbsp;czytelny format danych. Ogólnie wygląda jak zwykły tekst z&nbsp;nawiasami i&nbsp;apostrofami.
3. Zmienna `informacje_o_nas` może zawierać dowolne rzeczy, jakie odczytał JavaScript. Zaś zmienna `stronka_nasza_lub_obca` to adres, pod który te informacje zostaną wysłane. 

Pięć linijek nie licząc pustych. Ewentualnie jedna dodatkowa, jeśli ma to wszystko trafić w&nbsp;ręce całkiem obcej stronki.  
Tyle wystarczy, żeby nasze informacje poleciały gdzieś w&nbsp;szeroki świat.

## Parę słów na koniec

Widzimy, że JavaScript pod względem potencjału śledzącego jest co najmniej równy nagłówkom HTTP, które do tej pory omawiałem. Potrafi odczytać wszystkie te same informacje (poza adresem IP), a&nbsp;nawet zweryfikować ich prawdziwość. Swoje odkrycia może wysłać innym.

W kolejnych wpisach zobaczymy, że to dopiero początek jego możliwości. 

Na koniec pozwolę sobie na lekką dygresję. Choć ogólnie można się cieszyć, że świat idzie do przodu, w&nbsp;przypadku JavaScriptu ma to swoje wady. 

Pierwsza sprawa: ludzie chcą coraz to nowszych bajerów. Albo menedżerowie wmawiają programistom, że tak jest; wychodzi na to samo.  
Jeśli jakaś przeglądarka przestanie dodawać bajery, to stanie się mniej popularna. Zatem **trwa przeglądarkowy wyścig szczurów**. Dodają coraz więcej funkcji, bo muszą, bo robią tak inni. Wielu tych funkcji, jak zobaczymy, można nadużyć do celów śledzenia.

Druga sprawa: rosnąca „aplikacjoza”. Zamiast nieruchomych, stałych stronek -- internetowy odpowiednik aplikacji. Rzeczy większe, animowane, interaktywne. Strony ładowane na raty, żeby dało się je przewijać w&nbsp;nieskończoność.  
Nieraz wszystko to powolne i&nbsp;dziadowskie... no ale trendy!

W takich warunkach popularność JavaScriptu będzie jedynie rosła. A&nbsp;prąd, wbrew któremu będą musiały iść osoby stawiające szacunek dla użytkowników nad nowoczesnością, może być niestety coraz silniejszy.

Ale nie ma co się poddawać! Gdy nie ma siły, żeby iść pod prąd, to można na chwilę się rozluźnić i&nbsp;dać się ponieść. Na przykład do kolejnego wpisu :wink:
