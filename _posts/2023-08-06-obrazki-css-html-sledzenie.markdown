---
layout: post
title: "Internetowa inwigilacja plus 4 – śledzenie przez obrazki"
subtitle: "„Wybierz obrazek, a powiem ci kim jesteś”"
description: "„Wybierz obrazek, a powiem ci kim jesteś”"
date:   2023-08-06 8:00:00 +0100
tags: [Internet, Inwigilacja, Podstawy]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image:
  path: /assets/posts/inwigilacja/przez-obrazki/internet-obrazki-sledzenie-baner.jpg
  width: 1200
  height: 700
  alt: "Przerobiony mem złożony z dwóch paneli. Na górnym widać trzy przyciski, nad każdym z nich . Na dolnym panelu zestresowana postać, mająca logo Firefoksa zamiast górnej części głowy, ociera spocone czoło"
---

Już od dawna nie tworzyłem nowych wpisów z&nbsp;serii „Internetowa inwigilacja”. Aż się za nią nieco stęskniłem :smile:  
Dlatego teraz, gdy ulewa pokrzyżowała mi weekendowe plany, postanowiłem trochę nadgonić.

W tym wpisie skupimy się na metodach, które nazywam umownie „śledzeniem przez obrazki”. Polegają na proponowaniu naszej przeglądarce kilku różnych wariantów obrazków albo na umieszczaniu ich w&nbsp;taktycznych miejscach.

**Na podstawie tego, jakie obrazki ostatecznie pobierze przeglądarka, można wywnioskować o&nbsp;nas parę rzeczy**.

Co istotne, te metody wykorzystują najprostsze, standardowe elementy. Pozwalają wyciągnąć informacje nawet od tej garstki osób, która szczególnie dba o&nbsp;prywatność i&nbsp;wyłącza interaktywne funkcje (kod JavaScript).

Zapraszam do lektury! Będzie przystępnie, nawet dla osób nieznających poprzednich wpisów z&nbsp;serii.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/przez-obrazki/internet-obrazki-sledzenie.jpg" alt="Przerobiony mem złożony z&nbsp;dwóch paneli. Na górnym widać trzy przyciski, nad każdym z&nbsp;nich . Na dolnym panelu zestresowana postać, mająca logo Firefoksa zamiast górnej części głowy, ociera spocone czoło."/>

## Spis treści

* [Kto tym razem nas śledzi?](#kto-tym-razem-nas-śledzi)
* [Etapy pobierania strony](#etapy-pobierania-strony)
* [Obrazki jako narzędzie śledzenia](#obrazki-jako-narzędzie-śledzenia)
* [Obrazki leniwie ładowane](#obrazki-leniwie-ładowane)
* [Element \<picture\>](#element-picture)
* [Style CSS](#style-css)
* [Jak się chronić](#jak-się chronić)

## Kto tym razem nas śledzi?

Zacznijmy od tego, że w&nbsp;tej serii pokazywałem dotąd trzy główne rodzaje przeciwników, mogących zbierać o&nbsp;nas informacje:

1. Właściciele stronek, które odwiedzamy;
2. Organizacje, których drobne elementy „goszczą” na odwiedzanych przez nas stronach.

   To autorzy *trackerów* takich jak Google Analytics, Facebook Pixel oraz innych małych elementów, które można umieścić na swojej stronie.

3. Właściciele infrastruktury internetowej.

   To na przykład firmy telekomunikacyjne dające nam łączność z&nbsp;siecią, właściciele publicznych hotspotów itp.

Tym razem **głównym zagrożeniem jest dla nas przypadek pierwszy -- właściciele bezpośrednio odwiedzanych stron**.

Gdyby strona nie miała włączonego szyfrowania (`HTTPS`-a), to przeciwnik numer 3&nbsp;również mógłby zdobyć te same informacje co właściciel strony.

Ale bardzo możliwe, że nie umiałby ich zinterpretować. Nie wiedziałby na przykład, że fakt pobrania przez nas obrazka `img157.jpg` ma szczególne znaczenie. Dlatego zignorujemy ten przypadek.

## Etapy pobierania strony

Przypomnijmy sobie teraz, etap po etapie, kulisy typowych interakcji podczas przeglądania stron internetowych. Po jednej stronie jesteśmy my i&nbsp;nasza przeglądarka. Po drugiej cudzy komputer (serwer), przechowujący interesującą nas stronę.

### Etap pierwszy -- prośba o&nbsp;stronkę

Najpierw nasza przeglądarka wysyła cudzemu serwerowi prośbę o&nbsp;stronę.

{:.post-meta .bigspace-after}
We współczesnym internecie, gdzie powszechna jest [szyfrowana komunikacja]({% post_url 2022-08-13-https %}){:.internal}, dochodzi jeszcze ustalanie szyfrów. Ale to bez znaczenia dla wpisu, więc to pominę.

Ta prośba zawiera parę [podstawowych informacji o&nbsp;nas]({% post_url 2021-01-11-internetowa-inwigilacja-1-podstawy %}){:.internal}. Jak swego rodzaju wizytówka. Jest tam nasz adres IP, ustawiony język, rodzaj i&nbsp;wersja przeglądarki, może pliki cookies otrzymane wcześniej od odwiedzanej strony...

Nasza prośba dociera do serwera. O&nbsp;ile nie postanowi nas dyskryminować (na przykład na podstawie tego, że mamy europejski adres IP), to otrzymamy stronkę, o&nbsp;którą prosiliśmy. A&nbsp;nasze dane tak czy siak może sobie zapisać.

<img src="/assets/posts/inwigilacja/internet/internet-basic-http-headers.jpg" alt="Schemat pokazujący interakcję między laptopem a&nbsp;serwerem. Składa się z dwóch niezależnych obrazków. Na pierwszym widać strzałkę odchodzącą od laptopa do serwera, a&nbsp;nad nią ikonkę paczki z&nbsp;paroma napisami, symbolizującą dane. Pod spodem ta sama ikonka stoi obok serwera, a&nbsp;od niego odchodzi strzałka w&nbsp;stronę laptopa. Nad nią widać ikonkę używaną w&nbsp;systemie Linux do oznaczania plików ze stronami internetowymi."/>

{:.figcaption}
Źródła obrazków: Flaticon, Emojipedia, ikony systemu Linux Mint. Przeróbki moje.

### Etap drugi -- pobranie brakujących elementów

Nasza przeglądarka zapoznaje się z otrzymanym plikiem. Często jest raczej niewielki, to sam „szkielet” strony. Zawiera tylko podstawową treść i&nbsp;odniesienia do innych elementów. Takich jak:

* obrazki,
* niestandardowe czcionki,
* arkusze styli (nadające stronie wygląd),
* elementy interaktywne w&nbsp;języku JavaScript,
* ...i wiele innych możliwych rzeczy.

W źródle strony wygląda to na przykład tak:

```html
<img src="/obrazki/kot1.jpg"/>
``` 

{:.figcaption}
Element obrazkowy w&nbsp;kodzie HTML. Mówi przeglądarce, że w&nbsp;danym miejscu powinien być obrazek `kot1.jpg`. Do pobrania z&nbsp;tego samego źródła, co zdradza ukośnik na początku.

Przeglądarka zaczyna wysyłać serwerowi osobne prośby o&nbsp;każdy z&nbsp;takich elementów.  
„Wyślesz mi arkusz `stylowka.css`?„. „I jeszcze obrazek `kot.jpg`?”. „Aha, i&nbsp;jeszcze `kot2.jpg`?”.

<img src="/assets/posts/inwigilacja/internet/internet-images.jpg" alt="Schemat pokazujący dwie interakacje. W&nbsp;tej u&nbsp;góry odchodzi strzałka, nad którą widać miniaturkę emoji kota, a&nbsp;po nim znak zapytania. Obok jest emotka tygrysa, po niej również znak zapytania. Pod spodem widać strzałkę odchodzącą od serwera. Nad nią również są obie wspomniane ikonki, ale na białym tle, jak to z&nbsp;ikonek plików na komputerze."/>

### Etap trzeci (opcjonalny) -- komunikacja przez JavaScript

Gdybyśmy mieli stronkę złożoną z&nbsp;samego tekstu i&nbsp;obrazków -- „stronkę martwą” -- to po pobraniu wszystkich jej elementów nic więcej by się nie działo. Ot, czytalibyśmy sobie.

Jeśli na stronie znajduje się interaktywny kod JavaScript, to może on zapytać [o&nbsp;więcej, znacznie więcej informacji]({% post_url 2022-05-03-javascript2 %}){:.internal}. Takich jak parametry naszej karty graficznej, karty dźwiękowej, wymiary ekranu, naciśnięte klawisze oraz położenie kursora myszki...

Co więcej, może kontynuować komunikację z&nbsp;serwerem, od którego mamy stronę. I&nbsp;wysyłać mu na bieżąco różne informacje:

> „Przesyłam dokładne parametry karty graficznej użytkownika”.  
„Użytkownik właśnie przewinął stronę do połowy”.  
„Użytkownik nacisnął klawisze `Ctrl+P`, możliwe że próbuje wydrukować stronę”.

{:.bigspace-after}
<img src="/assets/posts/inwigilacja/internet/internet-javascript.jpg" alt="Schemat pokazujący, jak od laptopa w&nbsp;stronę serwera wychodzi żółta strzałka podpisana JS (JavaScript). Nad nią widać ikonkę przypominającą miniaturkę samego laptopa oraz napis Info."/>

Brzmi groźnie? JavaScript może mocno naruszać prywatność, dlatego osoby wyczulone go wyłączają -- poprzez dodatki do przeglądarki, jak NoScript albo [uBlock Origin]({% post_url 2021-10-21-ublock-origin %}){:.internal}.

## Obrazki jako narzędzie śledzenia

Ale, jak się okazuje, **istnieje szereg metod śledzenia dotyczących etapu drugiego, czyli pobierania elementów brakujących**.

Pozwalają uzyskać więcej informacji, niż da się odczytać z&nbsp;samej „wizytówki” z&nbsp;kroku pierwszego. Dużo mniej niż JS. Ale za to działają również na te osoby, które JS-a wyłączą.

Nie wiem, czy takie metody mają swoją oficjalną nazwę. Nazywam je umownie „śledzeniem przez obrazki”. Albo „śledzeniem przez decyzje przeglądarki”.  
Ich uniwersalna zasada działania jest prosta i&nbsp;opiera się na dwóch fundamentach:

1. Prosząc stronę o&nbsp;obrazki, nasza przeglądarka wysyła swoje podstawowe dane.

   Właściwie mógłby tu wystarczyć sam adres IP, reszta to uzupełnienie.  
   Dzięki temu faktowi właściciel strony może jasno ustalić -- osoba, która odwiedziła konkretny wpis i&nbsp;pobrała obrazek `1-mobile.jpg` to ta sama osoba, która pobrała chwilę później `14-mobile.jpg`. I&nbsp;tak dalej.
 
2. Da się, bez użycia JavaScriptu, **nakłonić przeglądarkę do wybrania obrazków zgodnych z&nbsp;jej ustawieniami**.

   Stronka, zamiast narzucać przeglądarce konkretny obrazek, może jej podsunąć kilka opcji. „Jeśli twój ekran jest duży, pobierz obrazek `1-large`. Jeśli mniejszy, pobierz `1-mobile`”. A&nbsp;przeglądarka posłucha sugestii.

{% include info.html
type="Ciekawostka"
text="Choć mówimy tu o&nbsp;obrazkach, nie muszą one przedstawiać niczego konkretnego ani zrozumiałego dla użytkowników.  
Jeśli jedynym celem obrazka jest sprawienie, żeby przeglądarka o&nbsp;niego poprosiła i&nbsp;zostawiła przy tym dane, to można użyć wariantu minimum. Obrazka o&nbsp;wymiarach 1x1, czyli pojedynczego piksela. A&nbsp;do tego wystylizować go w&nbsp;taki sposób, żeby był niewidzialny.  
Stąd zresztą wzięła się nazwa **piksel śledzący**."
%}

Niektóre metody z&nbsp;tego wpisu (nie wszystkie) działałyby w&nbsp;przypadku różnorodnych elementów, niekoniecznie obrazków. Ale obrazki są najprostszym przykładem, więc to na nich się skupimy. Spójrzmy teraz na różne przykłady nadużyć.

## Obrazki leniwie ładowane

Obrazki to elementy stosunkowo ciężkie (u&nbsp;mnie nieraz pojedynczy ma 50-100 kB, mimo że wszystkie mocno kompresuję; na niektórych stronach mają wielomegabajtowe).

A czasem się przecież zdarza, że ktoś wejdzie na jakąś stronkę przypadkiem. Nawet nie przewinie ekranu w&nbsp;dół, tylko od razu naciśnie `Wstecz`.  
Gdyby na tej stronie było kilkanaście obrazków, to po co je pobierać? Zbędne obciążenie i&nbsp;dla czytelnika (bo np. zużywa dane mobilne), i&nbsp;dla serwera właścicieli.

Z tego względu stworzono dość przydatną funkcję tak zwanego **leniwego ładowania obrazków** (ang. *lazy loading*). „Leniwego”, bo przeglądarka pobiera obrazek dopiero wtedy, gdy ten zbliży się do naszego pola widzenia. Nie wcześniej, bo nie ma co się przemęczać.

Obecnie nie potrzeba JavaScriptu, żeby włączyć leniwe ładowanie. Wystarczy dodać prostą instrukcję.

```html
<img src="/obrazki/kot1.jpg" />
<img src="/obrazki/kot2.jpg" loading="lazy" />
```

{:.figcaption}
Obrazek numer jeden zacznie się ładować od razu.  
Ten pod nim -- dopiero po tym, jak się do niego zbliżymy.

Ale pamiętajmy, że to serwer daje nam obrazki na życzenie. Może być wścibski i&nbsp;przypisywać do nas pobrane rzeczy. Po tym, jak pobierzemy jedną z jego stron, zaczyna nam liczyć powiązane obrazki.

* Nasz adres IP pobrał jeden lub dwa obrazki? Czyli tylko wyświetlił stronę i z&nbsp;niej wyszedł.  
  Bo jeden obrazek jest zawsze w&nbsp;banerze strony, a&nbsp;drugi u&nbsp;góry, tuż pod nagłówkiem.
* Pobrał trzy? Czyli przeczytał jakieś 20% artykułu  
  (na tej wysokości był kolejny obrazek).
* Pobrał cztery? Przeczytał 50% artykułu.
* Pobrał pięć? 90% artykułu.

Co do ostatnich 10% trudno wnioskować, bo więcej obrazków tam nie ma. Ale powyższe informacje wystarczą, żeby ustalić, na ile dany czytelnik się wciągnął.

Osobiście eksperymentowałem z&nbsp;leniwym ładowaniem w&nbsp;paru wpisach. Ale bez obaw, nie w&nbsp;celu śledzenia (i&nbsp;tak nie mam dostępu do serwera ani jego historii) :smile:

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/internet/lazy-loading-demo.jpg" alt="Lista obrazków z&nbsp;jednego ze wpisów z&nbsp;Ciemnej Strony, pod postacią screena z&nbsp;narzędzi przeglądarki Firefoksa"/>

{:.figcaption}
Obrazki leniwie ładowane z&nbsp;mojego wpisu na temat [cenzury stron internetowych]({% post_url 2022-09-12-dns-ip-cenzura %}){:.internal}.  
Źródło: narzędzia przeglądarki Firefox, zakładka `Sieć`.

Osoby wścibskie mogłyby celowo rozmieścić na swojej stronie leniwie ładowane obrazki. Albo nawet dodać je [do wysłanego nam maila](https://stackoverflow.com/questions/5448381/tracking-email-with-php-and-image). I&nbsp;na tej podstawie mierzyć nasz stopień przeczytania tekstu.

Co więcej, serwer z&nbsp;obrazkami **pozna również dokładny czas wysłania próśb**. W&nbsp;ten sposób jego właściciele zdobędą informację, że np. jakiś artykuł czytaliśmy równym tempem 15&nbsp;minut. Albo zatrzymaliśmy się na dłużej gdzieś między trzecim a&nbsp;czwartym obrazkiem i&nbsp;dopiero potem doczytaliśmy.

W ten sposób serwer może też wykrywać anomalie. Poprosiliśmy o&nbsp;stronę i&nbsp;parę plików uzupełniających, ale *o ani jeden* obrazek? Nawet te z&nbsp;samej góry, które każdemu powinny się pobrać?  
Możliwe, że używamy dodatku blokującego multimedia powyżej pewnego rozmiaru. Takiego jak uBlock Origin. Stronka doda informację o&nbsp;tym do naszej kartoteki.

### Scenariusz przykładowy

Wyobraźmy sobie, w&nbsp;jakiej sytuacji ktoś może użyć tej metody. Przedstawiam dwa warianty:

* Stalkerski.

  Znajoma osoba ma własną stronę internetową i&nbsp;dostęp do jej serwera. Podsyła nam link do konkretnego artykułu na stronie. I&nbsp;chce kontrolować, czy go przeczytamy.

* Korporacyjny.

  Bardzo podobny, tyle że informacje zbierane są od wielu osób. Zbieracz to na przykład komercyjny blog dostępny online. Mamy u&nbsp;nich konto czytelnika, wysyłają nam newslettery na maila.

Przede wszystkim strona śledząca musi ustalić, że jakiś odwiedzający ją czytelnik X&nbsp;to my. Ale to łatwe. Zwłaszcza jeśli jesteśmy zalogowani na konto.  
Nawet jeśli nie mamy konta, to mogą nam wysłać nieco inny link niż innym osobom (chociażby przez dodanie do niego [parametru]({% post_url 2021-04-09-internetowa-inwigilacja-parametry %}){:.internal}, np. `?a=123`; dowolnego, byle nie miała takiego żadna inna osoba).

W każdym razie wchodzimy na stronkę, a&nbsp;ta wie, że to my. Czytamy treść. A&nbsp;po stronie serwera gromadzą się informacje:

> „Użytkownik nr 123&nbsp;pobrał obrazek na wysokości 20% treści”.  
„Użytkownik nr 123&nbsp;pobrał obrazek na wysokości 50% treści”. 

Skupmy się na przykładzie stalkerskim. Mówimy wścibskiej osobie, że przeczytaliśmy wszystko. Ale ta na swoim serwerze widzi, że nasza przeglądarka pobrała tylko elementy z&nbsp;samej góry... Czyli raczej wciskamy kit :wink:

Przewinęliśmy szybko na sam dół i&nbsp;opuściliśmy stronę? Też się dowie. Po tym, że prośby o&nbsp;obrazki zostały wysłane w&nbsp;krótkich odstępach czasu (ale we właściwej kolejności).

{:.post-meta .bigspace-after}
Stalker(-ka) nie dowie się natomiast, czy po wstępnym przewinięciu tekstu wróciliśmy i&nbsp;go czytaliśmy na spokojnie. Bo obrazki już zostały pobrane, więc strona wystrzelała się z możliwości śledzenia tą metodą.

## Element \<picture\>

Element [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture) to część współczesnego formatu HTML. Oficjalna i&nbsp;standaryzowana.  
W praktyce: możemy dodać do swojej strony taki element, a&nbsp;każda współczesna przeglądarka już będzie wiedziała, co z&nbsp;nim zrobić. *Jak fani na pewnym koncercie rapowym.*{:.corr-del}

A co zrobi konkretnie z&nbsp;tym? Spojrzy na zawartą w nim listę obrazków. Przy każdym z&nbsp;nich znajdą się wytyczne mówiące, jaki obrazek załadować w&nbsp;zależności od cech przeglądarki.

> „Jeśli ta przeglądarka wspiera format AVIF, pobierz `kot.avif`”.  
„Jeśli wspiera AVIF, a&nbsp;szerokość okna jest większa niż 1000, pobierz `kot-large.avif`”.

...I tak dalej. Będzie tam również klasyczny obrazek (`<img>`), czyli wariant na wszystkie inne przypadki.

To przydatna funkcja, bo rzeczy czytelne na komputerach mogą się prezentować gorzej na smartfonach. Jeśli chcemy dać smartfoniarzom bardziej „pionowe”, ściśnięte wersje jakichś schematów, to taki element będzie idealny.

Co nie zmienia faktu, że daje możliwość rozdzielania użytkowników na podgrupy. A&nbsp;to nie sprzyja anonimowości. Dostając informację, że użytkownik X&nbsp;pobrał taki plik, a&nbsp;nie inny, strona czegoś się o&nbsp;nim dowie.

Korzystając z&nbsp;elementu `<picture>`, można na przykład:

* Określić wymiary naszego ekranu.

  Tutaj mamy spory potencjał do nadużyć. **W normalnych warunkach taką informację dałoby się zdobyć tylko przez JavaScript**.  
  Wścibska strona może dodać wiele opcji. Obrazek `1.jpg`, dla okna o&nbsp;szerokości 1000; `2.jpg`, dla szerokości 800. A&nbsp;serwer tylko patrzy, który z&nbsp;plików pobierzemy, i&nbsp;na tej podstawie poznaje wymiary naszego ekranu.

  Ta informacja nie jest może bezcenna. Ale w&nbsp;połączeniu z&nbsp;innymi (język, rodzaj przeglądarki) może pomóc nas potem rozpoznać. Nawet gdy zmienimy adres IP.

* Ustalić, że jakaś przeglądarka przedstawia się jako inna.

  Mamy na przykład nowego Firefoksa, ale w&nbsp;swojej wizytówce przedstawiamy się jako stary Chrome.  
  Ale nasza przeglądarka poprosiła o&nbsp;obrazek w&nbsp;formacie AVIF. A&nbsp;to coś nowszego, stary Chrome by wybrał inną opcję. Jest anomalia w&nbsp;zachowaniu, a&nbsp;to może budzić podejrzenia.

* Ustalić gęstość pikseli naszego ekranu.

  Można podsunąć inne obrazki ludziom z&nbsp;tak zwanymi ekranami *High-DPI* (*HiDPI*). Zazwyczaj to cecha nieco nowszego sprzętu, więc może pośrednio coś ujawniać o naszej zamożności. Zwłaszcza w&nbsp;połączeniu z&nbsp;wymiarami ekranu -- ultraszerokie *High-DPI* są [rzadkie i&nbsp;drogie](https://www.reddit.com/r/ultrawidemasterrace/comments/9mtltg/hidpi_ultrawide_is_there_such_a_thing/).

## Style CSS

Wyżej mieliśmy przykład podsuwania przeglądarce kilku opcji w&nbsp;najzwyklejszym kodzie HTML. Jeszcze więcej śledzenia można upchnąć w&nbsp;arkuszach styli CSS.
 
To popularny format, obecny niemal na każdej stronie. Zawiera regułki mówiące, jak powinny *wyglądać* różne elementy strony. Przykładowo: wszystkie linki powinny być zielone, a&nbsp;nie niebieskie; odstępy między akapitami mają mieć zawsze 3&nbsp;linijki... I&nbsp;tak dalej.

Pamiętamy fundamenty śledzenia przez obrazki? Po pierwsze, musimy być w&nbsp;stanie kazać przeglądarce pobrać obrazek. CSS jak najbardziej na to pozwala, przez regułkę `url`:

```css
{ background: url('adres/obrazka/1.jpg') }
```

Po drugie, musimy być w&nbsp;stanie dać przeglądarce kilka opcji, żeby wybrała najbardziej odpowiednią dla siebie.  
Też da się zrobić! W&nbsp;plikach CSS możemy umieszczać tak zwane *zapytania dotyczące mediów* (ang. *media queries*). Przeglądarka wybierze tylko te reguły, które do niej pasują:

```css
@media (min-width: 30em) and (max-width: 50em) {
  background: url('adres/obrazka/1.jpg')
}
```

{:.figcaption}
Tutaj przykład użycia zapytania do wyciągnięcia szczegółów na temat użytkownika; obrazek pobierze się wtedy i&nbsp;tylko wtedy, kiedy okno przeglądarki mieści się w&nbsp;określonych wymiarach.

Same obrazki podsuwane przeglądarce mogą być zupełnie identyczne z&nbsp;wyglądu; dla stron śledzących liczy się tylko to, żeby były to różne pliki, o&nbsp;różnych *nazwach*. A&nbsp;serwer już sobie będzie notował, o&nbsp;co poprosił użytkownik.

W ten sposób można wykryć różne rzeczy dotyczące trybów działania urządzenia. Za [listą Mozilli](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries):

* czy mamy włączony systemowy tryb ciemny,
* czy mamy tryb kolorów kontrastowych,
* czy mamy urządzenie bez kursora (np. dotykowe),
* czy używamy ekranu monochromatycznego,
* czy urządzenie wspiera szybkie odświeżanie (np. animacje),
* ...i jeszcze więcej.

Pod każdą z&nbsp;opcji typu ON/OFF można podpiąć dwa obrazki -- osobny dla włączonej, osobny dla wyłączonej. Gdy możliwości są trzy, to podsuwa się trzy obrazki. I&nbsp;tak dalej. Serwer będzie sobie patrzył, które z&nbsp;nich pobraliśmy. Dowie się trochę na temat urządzenia.

Wyróżnimy się, zwłaszcza jeśli używamy czegoś niestandardowego.  
Nietypowe ustawienie wynikające np. z&nbsp;problemów ze wzrokiem? Stronka łatwo nas rozpozna spośród tłumu. I&nbsp;może jeszcze podsunie reklamy laserowej korekty.

A to nie koniec! Oprócz prostego wykrywania typu ON/OFF można również tworzyć bardziej złożone reguły, pozwalające np. ustalić dokładne wymiary okna. Jak wspomniany wcześniej element `<picture>`. Śledzące zastosowania CSS-a fajnie opisali [na *fingerprint.com*](https://fingerprint.com/blog/disabling-javascript-wont-stop-fingerprinting#media-queries).

### Drukowanie

Co więcej, arkusze CSS mogą zawierać regułę `@print`. Odnosi się do przypadku, kiedy coś drukujemy (do pliku PDF albo na papierze). Czasem się przydaje, choćby na tym blogu. Ciemne tło i&nbsp;jasna czcionka nie sprzyjają drukarkom.

A czy może służyć śledzeniu? Postanowiłem to zbadać.  
W stylach testowego bloga dodałem link do obrazka, mającego stanowić tło w&nbsp;wersji drukowanej. I&nbsp;uruchomiłem narzędzia przeglądarki (`Ctrl+Shift+I`, potem zakładka `Sieć`), żeby patrzeć co się pobiera.

Obrazka testowego nie pobrało po zwykłym odwiedzeniu strony z&nbsp;bloga. Ale po naciśnięciu `Ctrl+P`, skrótu od drukowania, już się znalazł na liście pobranych plików.  
Wniosek? Dzięki użyciu tej regułki **strony mogą ustalić, czy drukowaliśmy ich treść**.

## Jak się chronić

Przede wszystkim pamiętajmy, że **jeśli mamy włączony JavaScript, to metody z&nbsp;tego wpisu są bez znaczenia**.

JS jest w&nbsp;stanie odczytać wszystkie opisane informacje (o&nbsp;stopniu przeczytania strony, o&nbsp;wymiarach ekranu, o&nbsp;innych rzeczach). I&nbsp;wiele innych. Jest w&nbsp;stanie je na bieżąco wysyłać wścibskiej stronce.  
Jest zatem dużo, dużo groźniejszy. Skupianie się na rzeczach egzotycznych, kiedy JS hula w&nbsp;przeglądarce, nie ma najmniejszego sensu. 

Ale jeśli już go wyłączyliśmy? W&nbsp;takim razie nie zaszkodzi dodać parę szlifów przeciw metodom na bazie HTML-a i&nbsp;CSS-a. Tak dla sportu.

### Odkrywanie cech przeglądarki 

Można **trzymać u&nbsp;siebie jedną „nudną” przeglądarkę** do surfowania po mniej zaufanej, reklamowej sieci. Bez trybu ciemnego, bez nietypowych bajerów. Konfiguracja domyślna.

Jeśli chodzi o&nbsp;zabezpieczenie przed ujawnianiem wymiarów ekranu -- przeglądarka Tor Browser rządzi.  
Korzysta [jedynie z&nbsp;kilku standardowych wymiarów okna](https://support.torproject.org/tbb/maximized-torbrowser-window/), odpowiadających najczęstszym urządzeniom. Jeśli nasze aktualne okno jest większe niż standardowe, to zapycha różnicę pustą białą przestrzenią.

Nie mamy Tora albo nie możemy go użyć (bo np. strona wykrywa i&nbsp;nie wpuszcza)? Albo nie chcemy?  
Pozostaje używanie przeglądarki w&nbsp;trybie pełnego ekranu. No i&nbsp;warto, żeby sam ekran był czymś względnie standardowym. Odepnijmy ultraszeroki monitor-potwora, zostawmy sobie laptopa. Chyba że chcemy się pochwalić podglądaczom.

### Leniwe ładowanie

Przy leniwie ładowanych obrazkach może nam pomóc Firefox, który [wyłącza tę funkcję, gdy mamy wyłączony JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#lazy). Wprost przy tym piszą o&nbsp;ochronie przed śledzeniem.

Obrazki w&nbsp;mailach? Tutaj pomoże odpowiedni program lub strona od maili. Tutanota, z&nbsp;której korzystam, automatycznie blokuje pobieranie obrazków z&nbsp;zewnątrz i&nbsp;robi to tylko na moje życzenie. Włączam je, gdy ufam nadawcy.

A jeśli nasza przeglądarka/mail nas nie chroni i&nbsp;musimy się narazić na obrazki ładowane na raty?  
Osobiście uważam, że **najprostszym, niewyróżniającym nas sposobem byłoby przewinięcie strony**. Choć raz, żeby wszystko się pobrało, a&nbsp;„obrazkowe pole minowe” zostało rozbrojone.

Możemy niby korzystać z&nbsp;przeglądarki, która wszystko ładuje od razu i&nbsp;olewa atrybut `lazy`. Albo jest stara i&nbsp;go nie wspiera. Albo ustawić w&nbsp;dodatku uBlock Origin, żeby nie pobierało elementów większych niż pewna wartość (czyli zwykle: żadnych obrazków).  
Tyle że wszystkie te rozwiązania są w obecnych czasach nietypowe i&nbsp;tylko by nas wyróżniły. A&nbsp;przejechanie wzrokiem po stronie to zachowanie względnie typowe.

Na tym skończę. Jak widzimy, nie potrzeba JavaScriptu do budowania naszego cyfrowego profilu. Wystarczy podsuwanie wielu obrazków i&nbsp;analizowanie, co wybrała nasza przeglądarka.

Życzę, żebyście jeszcze niejedne obrazki zobaczyli w&nbsp;internecie. Śmieszne, memiczne albo dające do myślenia... Ale jak najmniej śledzących.

