---
layout: post
title:  "Manifest v3. Jak Google zabija blokowanie reklam"
subtitle: "Zmiana kodu na 3 z przodu. Chrome, domagam się rozwodu"
description: "Zmiana kodu na 3 z przodu. Chrome, domagam się rozwodu"
date:   2022-05-11 9:00:00 +0100
tags: [Centralizacja, Internet, Manipulacja]
firmy: [Apple, Google, Microsoft, Mozilla]
category: google
category_readable: "Google – kolorowy czarny charakter"
image: "manifest/dodatki-egzekucja.jpg"
image-width: 1200
image-height: 700
---

Z przeglądarek internetowych korzystamy wszyscy. Jakoś w&nbsp;końcu czytacie stronę, na której teraz jesteście.

Natomiast wiele osób nie zadowala się domyślną, „łysą” wersją przeglądarki.  
Często instalujemy również jakieś dodatki. Od nauki słówek, od sprawdzania pisowni, od blokowania reklam (dygresja: nie polecam najpopularniejszego, AdBlocka).

Przeglądarka zapewniała nam solidną podstawę, zaś dodatki dawały upragnione możliwości. Internet stał otworem, świat był radosny, trawa soczyście zielona, ptaki ćwierkały.

Ten świat się skończy już w&nbsp;styczniu 2023&nbsp;roku.

Nie każdy to wie, ale za kulisami stopniowo wprowadza się nowy *ład*{:.corr-del} standard, którego będą musiały się trzymać wszystkie dodatki. Tytułowy *Manifest, wersja trzecia*.  
Według oficjalnych komunikatów poprawia bezpieczeństwo -- w&nbsp;praktyce **zarzyna niektóre dodatki, w&nbsp;tym te od blokowania reklam śledzących**.

Choć słowo „standard” brzmi biurokratycznie, nie zafundowały nam tego losu żadne rządy czy Unia. Nie; to inicjatywa całkiem prywatnej korporacji. Na tyle wpływowej, że potrafi poruszyć nawet internetem, z&nbsp;pozoru ostoją swobody i&nbsp;niezależności. **To dzieło firmy Google**.

Zapraszam do krótkiego przybliżenia kwestii *Manifestu v3*. Przy okazji rzucimy okiem na to, w&nbsp;jaki sposób podejmowane są decyzje kształtujące nasz wspólny internet.

{:.bigspace-before}
<img src="/assets/posts/manifest/dodatki-egzekucja.jpg" alt="Przerobiony kadr z&nbsp;filmu Apocalypto. Widać na nim cztery zgarbione postacie pomalowane niebieską farbą i&nbsp;prowadzone przez strażnika po pomoście. W&nbsp;tle widać piramidy w&nbsp;stylu plemion południowej Ameryki. Na twarz strażnika nałożono logo Google, zaś na twarze czterech więżniów ikony dodatków: Privacy Badger, uBlock Origin, Ghostery, SingleFile. Na pomost, po którym wchodzą, są nałożone słowa Manifest v2."/>

{:.figcaption}
Film: „Apocalypto”. Dodatki od lewej: Ghostery (z odwróconą miną), SingleFile, uBlock Origin, Privacy Badger.

## Wprowadzenie

Zacznijmy może od samego pojęcia *Manifest v3*. Nie zdziwiłbym się, gdyby niektórym czytelnikom kojarzyło się to co najwyżej z&nbsp;„Manifestem Komunistycznym”.

Rzecz w&nbsp;tym, że dodatki są całkowicie zależne od przeglądarki. To ona udostępnia im zestaw wybranych możliwości i&nbsp;narzędzi. Zestaw dostępny do tej pory nazywano zbiorczo wersją&nbsp;2.

Teraz Google planuje wprowadzić zmianę na tyle istotną, że zyskamy bonus +1&nbsp;do numeru wersji (co do tej pory rzadko się zdarzało w&nbsp;całej długiej historii Chrome'a). Obecnie dopuszczane są obie wersje, 2&nbsp;i&nbsp;3. Ale **wraz z&nbsp;początkiem 2023&nbsp;roku przeglądarka będzie dopuszczała jedynie wersję&nbsp;3**.

Mam drobną analogię: załóżmy, że w&nbsp;komunikacji miejskiej zamontowana jest teraz wersja 2&nbsp;automatów biletowych. Można w&nbsp;nich płacić i&nbsp;monetami, i&nbsp;dotykowo. W&nbsp;wersji 1&nbsp;dało się tylko monetami.  
W planach jest stopniowa wymiana tych automatów na wersję&nbsp;3, mniejszą i&nbsp;lżejszą, która pozwoli jedynie na płatności dotykowe. Niby krok w&nbsp;przyszłość, ale jednak coś tracimy względem poprzedniej wersji. Podobnie jest z&nbsp;Manifestem.

{% include info.html
type="Ciekawostka"
text="A dlaczego akurat słowo „manifest”, a&nbsp;nie jakiś „interfejs” czy coś takiego? Bo to pojęcie techniczne. Manifestem nazywa się zwyczajowo plik z&nbsp;ważnymi informacjami na temat czegoś, zwykle programu. Samo pojęcie jest [zapożyczeniem](https://en.wikipedia.org/wiki/Manifest_file) z&nbsp;branży transportu morskiego.  
Każdy dodatek do przeglądarki musi zawierać plik *manifest.json*, odczytywany przez nią jako pierwszy. A&nbsp;w nim, zazwyczaj u&nbsp;samej góry, zapisuje się numer wersji. Do tej pory wpisywaliśmy tu&nbsp;2, teraz trzeba będzie&nbsp;3."
trailer="<p class='figure bigspace-before'><img src='/assets/posts/manifest/manifest-deprecated.jpg' alt='Zrzut ekranu z przeglądarki pokazujący pierwsze linijki pliku manifestu. Jest tam zapisana wersja 2. U góry widać również komunikat mówiący, że w 2023 roku wsparcie dla wersji 2 manifestu zostanie wycofane.'/></p>"
%}

Z grubsza znamy kontekst, ale nadal jest sporo niejasności. Napisałem „Google planuje wprowadzić”. Ale dlaczego miałoby to mieć wpływ również na inne przeglądarki? Co on, imperator jakiś?

## Problem dominacji Chrome'a

Zastanawialiście się kiedyś, jak to jest, że przeglądarki nieraz wprowadzają zbliżone funkcje w&nbsp;podobnym czasie? Czy jest między nimi jakaś koordynacja? Kto nadaje kierunek współczesnemu internetowi?

Odpowiedź: **kierunek nadają firmy -- twórcy najpopularniejszych przeglądarek**. Są zrzeszeni w&nbsp;organizacji *[World Wide Web Consortium](https://pl.wikipedia.org/wiki/World_Wide_Web_Consortium)* (w skrócie *W3C*). Co pewien czas się spotykają i&nbsp;ustalają nowe standardy, których powinny się trzymać przeglądarki.

Znaczący członkowie W3C posiadający własne przeglądarki to Apple (silnik WebKit i&nbsp;przeglądarka Safari), Mozilla (Firefox), Google (silnik Chromium, przeglądarka Chrome) oraz Microsoft (przeglądarka Edge, oparta na silniku od Google'a).

Dzięki wspólnemu ustalaniu standardów nie ma dzikiego zachodu, gdzie każdy robi coś inaczej. Zyskujemy pewien porządek we wprowadzaniu nowinek i&nbsp;jest szansa, że zadziałają wszędzie tak samo. W&nbsp;teorii. W&nbsp;praktyce jednak uczestnicy nie są sobie równi.

Stworzyłem drobny schemat pokazujący, która przeglądarka od kogo pochodzi. Dominacja Google'a jest widoczna gołym okiem.

<img src="/assets/posts/manifest/browser-landscape.jpg" alt="Schemat pokazujący, od jakich firm wywodzą się jakie przeglądarki. Znajdują się na nim wyłącznie loga i&nbsp;symbole, a&nbsp;kierunek zmian jest pokazany strzałkami. U&nbsp;góry mamy Google, Apple i&nbsp;Mozillę. Od każdej z&nbsp;nich odchodzi strzałka w&nbsp;doł łącząca się z&nbsp;odpowiednią przeglądarką lub silnikiem: Chromium, WebKitem oraz Firefoksem. Od każdej z&nbsp;tych rzeczy też odchodzi strzałka w&nbsp;dół. Poniżej Chromium mamy 6&nbsp;ikon przeglądarek: Chrome, Edge'a, Brave'a, Opery, Vivaldiego, Kiwi, oraz trzy kropki. Poniżej Firefoksa ikonki dwóch niszowych przeglądarek, Librewolfa i&nbsp;Waterfoksa. Poniżej WebKita mamy ikonę Safari. Widać wyraźnie, że najwięcej przeglądarek bazuje na Chromium."/>

{:.figcaption}
W pierwszym rzędzie firmy, poniżej ich główny produkt, jeszcze niżej przeglądarki zbudowane na bazie tego produktu (albo przez samych twórców, albo na bazie publicznie dostępnego kodu). Pominąłem sporo bardziej niszowych przeglądarek, niech ich fani mi darują.

Niebieskie logo w&nbsp;drugim rzędzie po lewej, jeśli ktoś go jeszcze nie zna, to **Chromium** -- silnik, na bazie którego działa Chrome.  
Z jego kodu korzysta również wiele innych popularnych przeglądarek. Czasem go modyfikują na własne potrzeby, ale większość kodu „spływa z&nbsp;góry”.

Mamy zatem silną centralizację kodu w&nbsp;rękach jednej korporacji. I&nbsp;słabe możliwości ograniczenia jej wpływów. Bowiem organizacja *W3C* ma w&nbsp;sobie więcej z&nbsp;klubu dla szlachty niż z&nbsp;organu nadzoru.  
Nie są w&nbsp;stanie zablokować wielu rzeczy demokratycznym głosowaniem. Jeśli jeden z&nbsp;uczestników się uprze, że chce zrobić coś po swojemu, to tak zrobi.

Google cieszy się pod tym względem szczególnie złą sławą. Już nieraz zgłaszali propozycje, które inni uznawali za nie do przyjęcia (ze względu na przykład na to, że forsowały [prywatne interesy](https://www.theregister.com/2021/04/08/w3c_google_multple_domains/) Google'a).  
Kiedy grzeczna i&nbsp;oficjalna droga nie działała, **Google po prostu dodawał kontrowersyjne funkcje do Chromium**.

Wywierało to presję na pozostałych autorów przeglądarek. Niby są niezależni i&nbsp;nikt im nie każe iść za Google'em. Ale...

1. Media piszące o&nbsp;nowych technologiach często są płytkie i&nbsp;roszczeniowe.

   Nie obchodzi ich to, że jakiś nowy bajer ma szkodliwe efekty uboczne. Widząc różnicę w&nbsp;możliwościach przeglądarek, dzielą się wyrzutami: „Chrome to ma, a&nbsp;wy na co czekacie?”. A&nbsp;pewna grupa gadżeciarzy łyka taką narrację i&nbsp;przekazuje ją dalej. Przeglądarka bez bajerów stopniowo popada w&nbsp;niełaskę odbiorców.

2. Autorzy nie chcą walczyć z&nbsp;własnym silnikiem.

   Jak widać na schemacie, sporo przeglądarek jest opartych na publicznie dostępnym kodzie Chromium.  
   Ich twórcy mogliby usuwać z&nbsp;niego rzeczy niewygodne i&nbsp;zostawiać te przydatniejsze. Teoretycznie. Ale wymagałoby to nakładu pracy, i&nbsp;to przez czas nieokreślony. W&nbsp;końcu Google może dodawać coraz to nowe rzeczy, zależne od tych niechcianych. Z&nbsp;każdą kolejną wersją przeglądarka by coraz bardziej „odjeżdżała” od Chromium, trzeba by ręcznie zapychać różnice.  
   A&nbsp;przecież wielu twórców właśnie po to oparło się na cudzym silniku, żeby oszczędzić sobie tej wiecznej gonitwy.

Większość przeglądarek jest w&nbsp;pułapce punktu numer 2. Z&nbsp;kolei Firefox, posiadając niezależny silnik, ma większą swobodę w&nbsp;robieniu rzeczy po swojemu; ale jego z&nbsp;kolei dopada punkt 1&nbsp;i&nbsp;topniejąca popularność.  
Dlatego również goni Chrome'a i&nbsp;stara się *zachować kompatybilność* -- udostępniać swoim dodatkom to samo, żeby ludziom chciało się je tworzyć.

W takich realiach Google staje się swego rodzaju dyktatorem mody. Zaś pozostali, chcąc nie chcąc, podporządkowują się zmianom.  
Dlatego nie mieli zbyt wiele do powiedzenia, kiedy w&nbsp;2019 roku ogłoszono feralną Wersję 3. Od tego czasu wszystko nieuchronnie ku niej zmierza.

## Co Mv3 oznacza dla dodatków

# Oczekiwania kontra rzeczywistość

Nowy Manifest wprowadzono z&nbsp;pompą, powołując się, jak na Google przystało, na *bezpieczeństwo*:

> In order to **provide better protection** to our users, we need to make changes to the platform as well

{:.figcaption}
Źródło: [blog Google](https://security.googleblog.com/2019/06/improving-security-and-privacy-for.html) o&nbsp;cyberbezpieczeństwie. Wyróżnienie moje.

Zresztą w&nbsp;tym wypadku bezpieczeństwo określają jedynie jako jeden z&nbsp;filarów nowego Manifestu. Pozostałe dwa to wydajność oraz... prywatność.  
A żeby te filary nie były dla nas jakąś abstrakcją, dodali też kolorowy obrazek z&nbsp;kolumienkami.

{:.bigspace-before}
<img src="/assets/posts/manifest/manifest-filary.jpg" alt="Prosty obrazek przedstawiający trzy kolumny w różnych kolorach stojące obok siebie. Widnieją na nich napisy po angielsku: prywatność, bezpieczeństwo, wydajność."/>

{:.figcaption}
Źródło: [strona informacyjna](https://developer.chrome.com/docs/extensions/mv3/intro/platform-vision/) Google'a.

Z zapewnieniami Google'a [polemizuje](https://www.eff.org/deeplinks/2021/12/chrome-users-beware-manifest-v3-deceitful-and-threatening) Electronic Frontier Foundation -- organizacja nagłaśniająca problemy związane z&nbsp;cyfrowym światem.

Bezpieczeństwo?

Być może; w&nbsp;nowej wersji dodatki nie będą mogły pobierać skryptów z&nbsp;zewnętrznych źródeł.  
Ale EFF pokazuje również, że w&nbsp;praktyce ataki przez pobranie kodu nie są częste. Do tego wszelakie złośliwe dodatki zwykle są wyłapywane podczas weryfikacji. Google [we własnym wpisie](https://security.googleblog.com/2019/06/improving-security-and-privacy-for.html) pochwalił się, że blokuje ich 1800&nbsp;na miesiąc.  
Nowe zmiany brzmią zatem dobrze na papierze, ale możliwe że niewiele poprawią.

Co więcej, wygląda na to że Google ubija w ten sposób również dostęp do... własnych skryptów, z których twórcy dodatków mogli korzystać. Takie płyną wnioski z&nbsp;[wątku](https://github.com/google/google-api-javascript-client/issues/713#issuecomment-1099634326) założonego przez ich pracownika.

Szybkość?

Wygląda na to, że uzyskano ją poprzez odrąbanie pewnych rzeczy i&nbsp;narzucenie odgórnych limitów czasu. Które dla niektórych bardziej złożonych dodatków są nierealne.

Uderzyło to mocno w&nbsp;bardzo przydatny dodatek *SingleFile* -- pozwalający zapisać przeglądaną stronę na dysku, w&nbsp;postaci jednego pliku; z&nbsp;obrazkami „wszytymi” bezpośrednio w&nbsp;jego treść.

Tylko że ten dodatek musi dość intensywnie przetwarzać stronę. Do tej pory wykorzystywał w&nbsp;tym celu szereg kreatywnych rozwiązań, między innymi pobieranie w&nbsp;tle. Manifest v3 ogranicza czas pobierania do 5&nbsp;minut, co nie pozwoli na zapisanie szczególnie sporych stron.

Autor dodatku, Gildas Lormeau, stworzył już [wersję pod Manifest v3](https://github.com/gildas-lormeau/SingleFile-Lite). Ale nie szczędzi im uszczypliwości:

> Cechy wyróżniające SingleFile Lite:  
(...)  
większe zużycie pamięci RAM  
mocniejsze obciążanie procesora  
brak opcji automatycznego zapisu  
czas zapisywania ograniczony do 5&nbsp;minut  
(...)  
ograniczone wsparcie dla dynamicznego ładowania czcionek  
(...)  
Zalety płynące z&nbsp;wersji 3&nbsp;Manifestu:  
brak

{:.figcaption}
Źródło: [opis dodatku](https://github.com/gildas-lormeau/SingleFile-Lite). Wszystkie tłumaczenia moje.

Poza tym nie zapominajmy, że zmiany osłabiają dodatki blokujące reklamy. A&nbsp;reklamy są ciężkie. Nawet taka złożona na pozór z&nbsp;samego tekstu potrafi ciągnąć za sobą ponad 1&nbsp;MB&nbsp;kodu z&nbsp;wielu źródeł.  
Zapobiegając ich blokowaniu, Mv3 może *spowalniać* przeciętną wędrówkę po internecie.

Prywatność?

Google twierdzi w&nbsp;oficjalnych komunikatach, że żadnego blokowania nie ma, a&nbsp;prywatność chronią!

> Nie utrudniamy rozwijania dodatków blokujących reklamy ani nie powstrzymujemy użytkowników przed ich blokowaniem. Chcemy pomóc autorom dodatków, w&nbsp;tym blokujących, tworzyć je w&nbsp;sposób chroniący prywatność użytkowników.

{:.figcaption}
Źródło: [blog Google](https://security.googleblog.com/2019/06/improving-security-and-privacy-for.html).

A co uważają o&nbsp;tej sprawie autorzy dodatków blokujących, przez Google niepytani o&nbsp;zdanie? Tej kwestii przyjrzymy się nieco bliżej.

# Pogrom dodatków blokujących reklamy

Spójrzmy do innego oficjalnego [dokumentu](https://developer.chrome.com/docs/extensions/mv3/intro/mv3-overview/) Google'a z&nbsp;2020&nbsp;roku.  
Opisują w&nbsp;nim, co zmieni Mv3. Sporo rzeczy to technikalia i&nbsp;nie będę udawał, że wszystko rozumiem. Natomiast źródłem największych problemów dla dodatków wydaje się zmiana metody komunikacji i&nbsp;związane z&nbsp;tym odgórne limity.

Kiedyś do komunikacji z&nbsp;innymi stronami dodatki mogły używać interfejsu o&nbsp;nazwie `webRequest`. Dawał wiele możliwości. Wraz z&nbsp;wejściem wersji 3&nbsp;będą musiały korzystać z&nbsp;innego, `declarativeNetRequest`, dającego ich znacznie mniej.

Polecam [dyskusję](https://github.com/uBlockOrigin/uBlock-issues/issues/338) na stronie dodatku uBlock Origin. Jest tam trochę techniki, ale da się również wychwycić rzeczy zrozumiałe. I&nbsp;dające do myślenia.

Najważniejszy punkt -- nowoczesne dodatki blokujące stosują reguły dynamiczne. W&nbsp;których da się użyć specjalnych znaków i&nbsp;pojęć, żeby stworzyć swoistą hierarchię blokowania.

```
* * 3p-script block
github.com amazonaws.com * noop
```

{:.figcaption}
Przykład regułek dynamicznych; słowo `noop` ma specjalne znaczenie. Z&nbsp;tego co rozumiem, w&nbsp;tym wypadku blokują skrypty ze stron obcych (linijka&nbsp;1), ale przepuszczają w&nbsp;ramach wyjątku niektóre ze strony *github.com*.

Wersja&nbsp;3 ogranicza liczbę takich reguł do najwyżej&nbsp;5000. Po ich wyczerpaniu pozostają reguły statyczne, w&nbsp;których nie działają znaki specjalne. I&nbsp;będzie można dodać takich reguł najwyżej 30&nbsp;000 (autor uBO sam pisze, że to za mało). Da się również stosować inny rodzaj reguł (*regex*; elastyczne dopasowywanie tekstu), ale tych z&nbsp;kolei można dodać maksymalnie&nbsp;1000.

W ten sposób **możliwości blokowania zostaną znacząco ograniczone, do poziomu najprostszych dodatków**. Chyba że twórcy spróbują się zmieśćić w&nbsp;wyśrubowanych limitach, wpychając w&nbsp;nie jak najwięcej regułek.  
Cały wątek jest pełen główkowania nad tym, w&nbsp;jaki sposób dałoby się to zrobić. Ale to wszystko przypomina wybieranie wody z&nbsp;tonącego okrętu.

Bo nawet gdyby teraz udało się sprytnie wszystko uporządkować i&nbsp;skompresować, to przecież internet nie stoi w&nbsp;miejscu. Dodatki czerpią nazwy stron do blokowania z&nbsp;zewnętrznych, darmowych list, prowadzonych na bieżąco przez ochotników.  
Symbiotyczną zależność między blokerami a&nbsp;listami bardzo fajnie opisał twórca innego dodatku blokującego, [AdGuarda](https://adguard.com/en/blog/how-ad-blocking-is-done.html).

Tak znacząca zmiana w&nbsp;formacie filtrów wymagałaby intensywnej pracy nie tylko po stronie twórców dodatków (które łączą regułki proste w&nbsp;bardziej złożone), ale również ochotników utrzymujących listy. **Musieliby prowadzić je w&nbsp;innym formacie**, żeby sprostać nowym wymogom. A&nbsp;możliwe, że nie nadążą za zmianami.

> \[nowy interfejs\] w&nbsp;obecnym kształcie nie tylko cofa w&nbsp;rozwoju blokery treści, ale również skazuje je na zastój pod względem innowacji.

{:.figcaption}
Źródło: [komentarz](https://github.com/uBlockOrigin/uBlock-issues/issues/338#issuecomment-997983545) *gorhilla*, autora dodatku uBlock Origin.

AdGuard podsumowuje to jeszcze mocniej:

> Swego czasu nie szczędziliśmy gorzkich słów systemowi blokowania w&nbsp;\[przeglądarce\] Safari. I&nbsp;słusznie. Ale przynajmniej, dzięki niezliczonym sztuczkom i&nbsp;„klejeniu na taśmę”, udało nam się znaleźć zadowalające rozwiązanie. W&nbsp;przypadku Chrome'a szczerze mówiąc nie widać światełka pod koniec tunelu.

{:.figcaption}
Źródło: [wpis AdGuarda](https://adguard.com/en/blog/how-ad-blocking-is-done.html).

EFF (która również ma własny dodatek blokujący, *Privacy Badgera*) pisze wprost, że **widzi w&nbsp;tej całej sprawie konflikt interesów**.  
Google jest właścicielem największych internetowych sieci reklamowych. I&nbsp;nadużywa swojej równie dominującej przeglądarki, żeby tę władzę umocnić.

A sam gigant? Powtarza jak mantrę swoje słowa o&nbsp;bezpieczeństwie, prywatności i&nbsp;szybkości. Jest kryty. Zamiast jawnie zadać cios kończący -- stopniowo wypompowuje tlen, aż twórcy dodatków i&nbsp;list nie będą mieli siły walczyć.  
„Ach, peszek. A&nbsp;przecież daliśmy im tyle fajnych możliwości”.

## Reakcje twórców przeglądarek

Widać, że *Wersja 3* to bardzo złe wieści dla dodatków. Do tego stopnia, że jedyną nadzieją dla nich mogą być przeglądarki stojące po ich stronie i&nbsp;celowo zachowujące zgodność z&nbsp;*Wersją&nbsp;2*.

Jednak wiele z&nbsp;nich jest zależnych od Chromium, zaś wprowadzanie zmian byłoby dla nich drogą pod górkę. Dlatego nie dziwota, że niektóre odpuszczają. Niektóre przepraszały użytkowników mniej, niektóre bardziej; nieliczne stawiły opór.

* [Edge](https://docs.microsoft.com/en-us/microsoft-edge/extensions-chromium/developer-guide/manifest-v3)

  Łyknął wszystko, razem z&nbsp;trzema filarkami od Google'a.

  > Microsoft announced the decision to embrace Manifest V3 to help reduce fragmentation of the web for all developers and enhance privacy, security, and performance for end users.

* [Vivaldi](https://vivaldi.com/blog/chromium-ad-blockers-choice/)
  
  Opisali sytuację w&nbsp;sposób sugerujący, że nie trzymają strony Google'a. Natomiast wprost podkreślają, że wcielą zmiany wprowadzone do Chromium również do swojej przeglądarki.

* [Opera](https://forums.opera.com/post/258864)

  Mamy opinię ich pracownika z&nbsp;oficjalnego forum. Planują jeszcze wspierać wersję 2&nbsp;i&nbsp;pozwalać na dodawanie takich dodatków do swojej bazy. Ale jeśli jakiś zostanie wydany w&nbsp;wersji&nbsp;3, to będzie działał z&nbsp;ograniczeniami typowymi dla Chromium.

  > Like Chrome we don't support webRequest API in v3 but we still support it in v2 (also in Opera addons portal) and we don't have strict dates to remove it.

* [Firefox](https://blog.mozilla.org/addons/2021/05/27/manifest-v3-update/)

  Oficjalnie przyjmują nowy Manifest, żeby zachować kompatybilność z&nbsp;Chromium. Ale wspierają też starsze, mniej ograniczające metody. Zatem uBO i&nbsp;inne skuteczne dodatki blokujące powinny u&nbsp;nich śmigać jak wcześniej.  
  To samo podejście zapewne odziedziczą inne przeglądarki oparte na Firefoksie.

* [Brave](https://community.brave.com/t/chrome-extension-manifest-v3/43255)

  Mają wbudowaną własną funkcję blokowania reklam bezpośrednio w&nbsp;przeglądarkę; to poziom głębiej niż wszelkie dodatki, więc zmiana Manifestu na to akurat nie wpłynie.  
  Natomiast jeśli chodzi o&nbsp;dodatki, [zapowiadają](https://www.reddit.com/r/brave_browser/comments/rdab12/comment/ho01cz2/) jak najdłuższe wspieranie M2.

Powiedziałbym, że nie jest wesoło. Mamy przede wszystkim słowa wsparcia, ale zmiany i&nbsp;tak się wkradają.

* Zasadniczo tylko Firefox ma i&nbsp;sporą motywację (reputacja przeglądarki pro-prywatnościowej), i&nbsp;możliwości (osobny silnik), żeby robić rzeczy po swojemu.  
* Brave ma motywację, ale w&nbsp;kwestii dodatków musi działać wbrew swojemu silnikowi.  
* Edge łyknął wszystko, co Google stworzył.
* A&nbsp;reszta wydaje się OK, ale dopiero czas pokaże, jak długo są gotowi walczyć.

Na urządzeniach mobilnych sytuacja z&nbsp;dodatkami zmieni się nieznacznie, bo i&nbsp;tak była bardzo kiepska.  
Kilka wybranych wspiera mobilny Firefox.  
Mniej znana przeglądarka, [Kiwi Browser](https://kiwibrowser.com/), wspiera wszystkie; ale jest na bazie Chromium, więc istnieje ryzyko, że ją również dopadną zmiany. W&nbsp;takim wypadku pozostanie trzymanie się starszej wersji.

## Co możemy zrobić

Jako szeregowi użytkownicy wiele nie wywalczymy, bo sprawa toczy się wysoko nad naszymi głowami, tam gdzie pieniądze płyną strumieniami. Trzeba zdać się na twórców przeglądarek, dodatków i&nbsp;list.

Co nie znaczy, że mamy siedzieć biernie.

Przede wszystkim, jeśli coś nam w&nbsp;przyszłym roku przestanie działać, **nie lećmy z&nbsp;pretensjami do twórców dodatków**.  
Oni naprawdę nie mają na to wszystko wpływu. Co więcej, jak pokazałem, starają się walczyć z&nbsp;tym stanem rzeczy. Ale warunki dyktują im twórcy przeglądarek.

Poza tym warto zagłosować nogami -- **odejdźmy od przeglądarek forsujących nową rzeczywistość**. Czyli na pewno od Chrome'a i&nbsp;Edge'a. Od Chromium również, mimo że było na plus względem Chrome'a. Być może od Opery, Vivaldiego i&nbsp;reszty, jeśli zakończą wsparcie dla wersji 2.

Zamiast nich wybierzmy [Brave'a](https://brave.com/download/) (jeśli jesteśmy przyzwyczajeni do Chrome'a), [Firefoksa](https://www.mozilla.org/pl/firefox/new/) (jeśli cenimy niezależne alternatywy) albo przeglądarki na ich bazie.

Zachęcajmy do tego innych, nagłaśniajmy sprawę. Mało kto wie o&nbsp;tej całej sytuacji, a&nbsp;ludzie jednak lubią swoje dodatki. To dobry moment na pokazanie, że Google nie jest ich przyjacielem.

Ktoś umie programować? Super! Myślę że każdy kod pomagający uratować sytuację będzie na wagę złota.  
Mam w&nbsp;głowie kilka rzeczy, które mogłyby się przydać (ale dla mnie to za wysokie progi):

* Program przeczesujący oficjalne bazy dodatków (*Chrome Web Store* itd.) i&nbsp;wyłapujący te z&nbsp;wersją&nbsp;2; warto je zarchiwizować.

  {:.post-meta}
  **Aktualizacja:** takie dane zbiera już stronka [ChromeStats](https://chrome-stats.com/manifest-v3-migration).

* Stronkę opartą na powyższym rozwiązaniu. Coś w&nbsp;rodzaju „cmentarzyska dodatków” pokazującego, ile z&nbsp;nich nie przetrwało wejścia Wersji&nbsp;3. Coś jak stronka *[Killed by Google](https://killedbygoogle.com/)*.
* Publicznie dostępny kod ułatwiający przeglądarkom obsłużenie zarówno Wersji 2, jak&nbsp;i&nbsp;3.
* Listy dla dodatków blokujących prowadzone w&nbsp;nowym formacie; żeby dało się wycisnąć z&nbsp;ograniczonej puli regułek jak najwięcej.

A na poziomie nieco ogólniejszym -- zachęcam do pewnej refleksji, mniej konsumpcyjnego podejścia.

Dużo złego przyniosło gadżeciarstwo. „Dej, dej, ja chcę mieć”.  
To taka postawa napędza przeglądarkowy wyścig szczurów. Wywierając presję, żeby dodawały nowe funkcje. Wirtualną rzeczywistość, programy biurowe w&nbsp;przeglądarce, coraz lepszy streaming...

Na dłuższą metę prawie żadna organizacja tego nie zapewni, to nierealne. Dlatego uzależniają się od kodu Chromium, tracąc część swojej autonomii.

Gdyby użytkownicy kładli większy nacisk na działania w&nbsp;ich interesie niż na nowinki -- i&nbsp;to okazywali w&nbsp;ankietach, na forach itp. -- to rzeczywistość nieco by się mogła zmienić. I&nbsp;takiej zmiany nam życzę.

Do zobaczenia w&nbsp;kolejnych wpisach!
