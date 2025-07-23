---
layout: post
title:  "Internetowa inwigilacja 10 – JavaScript, cz.2"
subtitle: "„Co potrafisz?”"
description: "„Co potrafisz?”"
date:   2022-05-03 21:45:00 +0100
tags: [Internet, Inwigilacja, Porady]
firmy: [Reddit]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: 
   path: /assets/posts/javascript-tracking/js-danger-baner.jpg
   width: 1200
   height: 700

image-width: 1200
image-height: 700
---

We wczorajszym wpisie przedstawiłem krótko JavaScript, swoisty język programowania internetu.

Mówiąc prosto: jest osadzony w&nbsp;stronach internetowych, które przeglądamy. Zapewnia im interaktywność, ale oprócz tego **może podpytywać naszą przeglądarkę o&nbsp;dość konkretne informacje**. A&nbsp;potem wysyłać je stronie, z&nbsp;której przybył. A&nbsp;nawet obcym stronom.

Poprzednio pokazałem, że może odczytywać prawie wszystkie informacje opisane we wpisach 1-8 z&nbsp;tej serii. Czyli dane z&nbsp;tak zwanych *nagłówków HTTP*, swoistej wizytówki naszej przeglądarki.

W tym wpisie natomiast przejdę do rzeczy, których dotąd nie było i&nbsp;które może sprawdzić *tylko* JavaScript. W&nbsp;sposób bardzo prosty, często jedną linijką kodu.

{% include info.html
type="Krótko"
text="Jeśli przyszliście tu po rozwiązania, a&nbsp;nie szczyptę wiedzy, to służę :smile:  
Pobieracie dodatek [uBlock Origin](https://ublockorigin.com/). Włączacie w&nbsp;jego ustawieniach blokowanie JavaScriptu.  
Niektóre strony nie będą wtedy działały, to nieuniknione. Gdy na taką traficie, wyłączacie blokowanie i&nbsp;ją odświeżacie."
%}

# Spis treści

* [Życiowy przykład](#życiowy-przykład)
* [Różne oblicza śledzenia](#różne-oblicza-śledzenia)
  * [Wymiary ekranu](#wymiary-ekranu)
  * [Śledzenie myszki i&nbsp;klawiatury](#śledzenie-myszki-iklawiatury)
  * [Pamięć i&nbsp;liczba rdzeni procesora](#pamięć-iliczba-rdzeni-procesora)
  * [Poziom naładowania baterii](#poziom-naładowania-baterii)
  * [Informacje o&nbsp;sieci](#informacje-osieci)
* [Łączenie danych](#łączenie-danych)
* [Jak się przed tym chronić?](#jak-się-przed-tym-chronić)
  * [Całkowite wyłączenie JavaScriptu](#całkowite-wyłączenie-javascriptu)
  * [Korzystanie z&nbsp;publicznych komputerów](#korzystanie-zpublicznych-komputerów)
  * [Wtopienie się w&nbsp;tłum](#wtopienie-się-wtłum)
  * [Sprytniejsze otwieranie narzędzi przeglądarki](#sprytniejsze-otwieranie-narzędzi-przeglądarki)
  * [LibreJS i&nbsp;inne opcje pośrednie](#librejs-iinne-opcje-pośrednie)


## Życiowy przykład

Wyobraźmy sobie, że przeglądamy właśnie jakąś popularną stronkę od zakupów online; własność wielkiej, lecz kontrowersyjnej firmy. Robimy to ze swojego własnego konta, pod które są podpięte nasze dane osobowe.

Nagle nachodzi nas ochota na sprawdzenie, czy w&nbsp;serwisie znajdziemy ogłoszenia dotyczące bardziej kontrowersyjnych rzeczy (jakich? Zostawiam wyobraźni).

**Nie chcemy, żeby strona wiedziała czego szukaliśmy**. Może po rozpoznaniu u&nbsp;nas pewnych zainteresowań bombardowałaby nas reklamami. Albo może słyszeliśmy, że lubi takie informacje sprzedawać ubezpieczycielom, którzy by nas za to wpisali na czarną listę. [Jak w&nbsp;USA](https://www.fastcompany.com/90310803/here-are-the-data-brokers-quietly-buying-and-selling-your-personal-information).

A wcześniej czytaliśmy Ciemną Stronę i&nbsp;wiemy, jak wścibskie potrafią być korporacje. Znamy też parę sposobów na zachowanie prywatności.  
Zatem uruchamiamy całkiem nową, nieużywaną dotąd przeglądarkę, z&nbsp;czystymi ustawieniami. Nasz system operacyjny jest popularny, wiele osób go ma. Łączymy się przez VPN-a, żeby zmienić adres IP. Dla pewności włączamy tryb incognito.

Zmieniliśmy wszystko poza komputerem. Uff. Wchodzimy na naszą stronę aukcyjną i&nbsp;zaczynamy szukać.

Gdyby świat kończył się na informacjach z&nbsp;nagłówków HTTP, omawianych do tej pory, to bylibyśmy bezpieczni. Ale istnieje JavaScript.  
Jest tym, co może sprawić, że informacje i&nbsp;tak trafią do naszych wirtualnych akt. Nawet gdy jedyną rzeczą łączącą wyszukiwania tajne z&nbsp;jawnymi było urządzenie.

Zapnijcie pasy, będzie groźnie :smiling_imp:

<img src="/assets/posts/javascript-tracking/js-danger-baner.jpg" alt="Obrazek pokazujący logo JavaScriptu, czarne literki J i S na żółtym tle. Literkę J podmieniono na czarny hak o podobnym kształcie, z którego właśnie skapuje kropla krwi."/>

{:.post-meta .bigspace-before}
Jeśli chcecie sprawdzić, co JS wie na temat waszej przeglądarki, możecie to zrobić np. przez stronę [BrowserLeaks](https://browserleaks.com/javascript).

## Różne oblicza śledzenia

Sposób, w&nbsp;jaki JavaScript może podpytać o&nbsp;właściwości systemu, opisałem w&nbsp;poprzednim wpisie. Żeby się nie powtarzać: najczęściej po prostu odnosi się do obiektu `navigator`, który każda przeglądarka udostępnia. Tam może znaleźć wiele ciekawych informacji. 

# Wymiary ekranu

JavaScript może odczytywać zarówno wymiary całego ekranu, jak i&nbsp;obszaru, na którym wyświetlana jest strona (to drugie zwykle pod nazwą *viewport*). Są podane w pikselach, w formacie *szerokość × wysokość*.

Nawet wymiary całego ekranu, zwykle powtarzalne (pełno *1920×1080* itp.), mogą być ciekawym sygnałem. Jeśli używamy nietypowego monitora (szerokokątnego, pionowego...), to w&nbsp;jakiś sposób się wyróżniamy.

Jeśli dorzucimy do tego wymiary okna, to już robi się bardzo ciekawie. Porównując je z&nbsp;całym ekranem, JS byłby w&nbsp;stanie **rozpoznawać niestandardowe ustawienia**.

Wymyśliłem na poczekaniu pewien przykład. Mianowicie: wiele systemów operacyjnych (Windows, Linux Mint...) ma w&nbsp;dolnej części ekranu nieruchomy pasek z&nbsp;opcjami.

JavaScript może spojrzeć na różnicę między wysokością okna a&nbsp;wysokością ekranu. W&nbsp;tej różnicy wysokości zawiera się nasz dolny, systemowy pasek, a&nbsp;także pasek górny przeglądarki.

Ale wysokość paska od przeglądarki zwykle jest standardowa! JS może sprawdzić w&nbsp;jakiejś bazie paski typowe dla naszej przeglądarki, w&nbsp;końcu ją zna. A&nbsp;po odjęciu wymiarów przeglądarkowych zostanie wysokość naszego dolnego, systemowego paska.  
Jeśli jego wysokość nie pasuje do typowych wartości -- również zebranych w&nbsp;jakiejś bazie -- to może trafić do naszej „teczki” jako cecha szczególna.

Wysokość strony jest u&nbsp;nas równa lub prawie równa wysokości ekranu? To by świadczyło o&nbsp;tym, że nie mamy żadnego paska. Albo ustawiliśmy sobie, żeby się chował. Odeszliśmy od ustawień typowych dla systemu, wyróżniamy się.

JavaScript może wyłapać kolejne anomalie, porównując wymiary pasków wewnątrz naszej przeglądarki z&nbsp;tymi typowymi. Mamy schowany pasek boczny, obecny u&nbsp;większości użytkowników danej przeglądarki? Wyróżniamy się.

{:.figure .bigspace-before}
<img src="/assets/posts/javascript-tracking/js-wymiary-okien.jpg" alt="Dwa okna w&nbsp;małych, prawie identycznych rozmiarach ustawione jedno pod drugim, na tle tapety ze szczytami gór. Pierwsze należy do Opery, drugie do Brave'a. W&nbsp;obu wyświetla się ta sama strona z&nbsp;informacjami o&nbsp;rozmiarach ekranu. Widać, że więcej pikseli zdaniem strony ma okno Brave'a."/>

{:.figcaption}
Okna dwóch przeglądarek, Opery i&nbsp;Brave'a. Choć ich granice mają podobne wymiary, w&nbsp;Operze obszar strony jest mniejszy. Przez pasek boczny.

Inny przykład -- **wykrywanie, czy otwarliśmy narzędzia przeglądarki**.
Kiedy otwieramy te narzędzia, żeby zajrzeć stronce w&nbsp;bebechy, to w&nbsp;domyślnym trybie wysuwają się z dołu, zmniejszając obszar wyświetlanej strony.  
JavaScript może wypatrywać takich zmian i&nbsp;odgadnąć, co właśnie otwieramy. Nie jest to zresztą teoria -- na Githubie wprost znajdziemy [projekt](https://github.com/sindresorhus/devtools-detect), który oferuje takie możliwości. Dość popularny, ponad 1700&nbsp;gwiazdek.

Otwieranie narzędzi może być dla szpiegowskiej strony sygnałem, że zaraz sama będzie szpiegowana. Niektóre **zmieniają swoje zachowanie, kiedy to wykryją**. Chowają śledzący JavaScript, żeby wyglądać niewinnie.

# Śledzenie myszki i&nbsp;klawiatury

JavaScript może śledzić ruchy kursora naszej myszy. I&nbsp;wie, co nacisnęliśmy na klawiaturze.  
Najpierw uspokoję: skrypt ze strony A&nbsp; *nie jest* w&nbsp;stanie odczytać informacji wpisywanych na stronie B, jak hasło do konta bankowego.

Ale i&nbsp;tak może robić wredne rzeczy na tej stronie, na której się znajduje. Jak choćby przechwytywanie i&nbsp;neutralizowanie klawiszy `PrintScreen` (żebyśmy nie mogli robić zrzutów ekranu) albo `Ctrl`+`C` (żebyśmy nie mogli niczego skopiować).

Wyżej wspomniałem o&nbsp;tym, że po rozmiarze okna strona może poznać, czy ktoś otworzył narzędzia przeglądarki. To samo może odgadnąć, wypatrując kombinacji `Ctrl`+`Shift`+`I`, która je otwiera.

Dlatego, jeśli ktoś chce dyskretnie otworzyć narzędzia przeglądarki, najlepiej przeklikać się myszką przez opcje. Śledzenie myszy nie sięga bowiem poza obszar strony.

{:.figure .bigspace}
<img src="/assets/posts/javascript-tracking/przegladarka-sledzenie-myszki-klawiatury.jpg" alt="Zrzut ekranu okna, w&nbsp;którym otwarta jest strona Google. Na sam obszar strony nałożono czerwony filtr i&nbsp;podpisano go 'Obszar śledzenia myszy'. Reszta okna jest zakryta filtrem żółtym i&nbsp;podpisana 'Obszar śledzenia klawiatury'."/>

A jeśli chodzi o&nbsp;szpiegowanie użytkowników?

Stronka mogłaby trzymać listę typowych skrótów klawiszowych dla danej przeglądarki. Jeśli ktoś **często używa kombinacji niestandardowych**, to mogłaby to sobie zapisywać -- sam na przykład mam niestandardowy skrót, który sobie ustawiłem do usuwania elementów (funkcja dodatku uBlock Origin).

Wróćmy do przykładu z&nbsp;początku wpisu -- chcę poszukać czegoś bardzo osobistego na stronie, na której często bywam. Otwieram nowe okno w trybie incognito i&nbsp;zmieniam adres IP (np. przez opcje Opery).  
Jeśli z&nbsp;przyzwyczajenia użyję swojego nietypowego skrótu klawiszowego, to strona może sprawdzić w&nbsp;zapisanych informacjach, czy ktoś z&nbsp;zarejestrowanych użytkowników tak robił. Też jest z&nbsp;Polski i&nbsp;niedawno wylogował się z&nbsp;konta? Ups, mają mnie.

Inne nieoczekiwane zastosowanie śledzenia klawiatury? **Istnieją formularze, które wysyłają wpisywany tekst na bieżąco**. Zanim w&nbsp;ogóle klikniemy „Wyślij”. Rzekomo po to, żeby obsługa klienta mogła szybciej reagować.

W związku z&nbsp;tym protip dla osób, które mają w&nbsp;zwyczaju pisać wiadomość na brudno („czy was tam poje...”), a&nbsp;potem ją kasować i&nbsp;pisać coś bardziej wyważonego („Dzień dobry, piszę w&nbsp;związku z...”).  
Brudnopisem szanującym prywatność są programy w&nbsp;stylu Notatnika :wink: Nie internetowe formularze.

A ruchy kursora myszki czy analiza stylu pisania to tematy na osobny wpis. Potwierdzę tylko: tak, dużo o&nbsp;nas zdradzają.

# Pamięć i&nbsp;liczba rdzeni procesora

Informacje z&nbsp;naszej internetowej „wizytówki” ukazują co najwyżej przeglądarkę i&nbsp;system operacyjny. JavaScript umie sięgnąć głębiej.

Pierwsza rzecz to zmienna `navigator.deviceMemory`. Wyraża ilość pamięci RAM w&nbsp;naszym komputerze i&nbsp;jest podana w&nbsp;gigabajtach.  
Chrome i&nbsp;inne przeglądarki na silniku Chromium to ujawniają, Firefox nie.

Kolejna sprawa: liczba rdzeni procesora. Zmienna `navigator.hardwareConcurrency`.  
Zazwyczaj parzysta. Od 2&nbsp;przy urządzeniach budżetowych do [nawet 18](https://cpuninja.com/how-many-cpu-cores-need/) przy hardkorowych. A&nbsp;wciąż mówimy o&nbsp;procesorach na rynek konsumencki; procesory robione pod serwery miałyby tego jeszcze więcej.

Większa liczba rdzeni i&nbsp;pamięci może być dla JavaScriptu mocną wskazówką na to, że ma do czynienia z&nbsp;komputerem stacjonarnym. Pomijając już fakt, że jakaś szemrana strona mogłaby na podstawie mocniejszego sprzętu uznać, że trafił się klient do oskubania. I&nbsp;zaproponować wyższe ceny produktów.

Tę informację zdradzają wszystkie przeglądarki, które sprawdzałem. Chromium i&nbsp;Opera bez zaskoczenia. Ale Brave i&nbsp;Firefox, reklamujące się szanowaniem prywatności, również.

{% include info.html
type="Ciekawostka"
text="Niektórych może zaskoczyć liczba rdzeni w&nbsp;telefonach. W&nbsp;słabszych laptopach miewamy zwykle od 2&nbsp;do 4. Zaś przy telefonach -- nawet tych tańszych -- 8&nbsp;nie jest niczym szokującym.  
To dlatego, że rdzeń rdzeniowi nierówny. W&nbsp;telefonach tylko niektóre rdzenie są mocniejsze i&nbsp;włączane przy cięższych zadaniach; reszta stawia na niskie zużycie energii. Taka architektura nosi nazwę *[big.LITTLE](https://en.wikipedia.org/wiki/ARM_big.LITTLE)*."
%}

Jeśli ciekawi nas odrobina historii, to na forum HackerNews znajdziemy [zażartą dyskusję](https://news.ycombinator.com/item?id=26518894) z&nbsp;udziałem człowieka, który doprowadził do tego, że przeglądarki ujawniają informację o&nbsp;liczbie rdzeni.  
Jak sam wspomina w&nbsp;swoim [wpisie](https://eligrey.com/blog/cpu-core-estimation-with-javascript/), motywacją była próba lepszego dopasowania pewnej wymagającej aplikacji do możliwości systemu.

Pisze, że JavaScript i&nbsp;tak mógłby zdobyć informację o&nbsp;liczbie rdzeni. Tylko że nie wprost, lecz przez mierzenie czasu, jaki zajmie komputerowi wykonanie pewnych wymagających obliczeń.

Jest w&nbsp;tym trochę racji; JavaScript mógłby dowiedzieć się wiele, nawet gdyby przeglądarka nie mówiła mu wprost.  
Natomiast moim zdaniem dawny stan rzeczy przynajmniej niósł za sobą pewne konsekwencje. Procesor zaczynał buczeć, strona muliła; użytkownik mógł się zorientować, że coś jest nie tak.

A teraz? JS dostanie swoje dane po cichu. Przeglądarki mogłyby przynajmniej pytać, czy chcemy ujawnić tę informację.

# Poziom naładowania baterii

Zmienne ujawniające informacje o&nbsp;baterii to zbiorczo `Battery Status API`. Mówią o&nbsp;kilku rzeczach: 

* czy nasze urządzenie jest aktualnie podłączone do ładowania;
* jaki jest poziom naładowania baterii (liczba z&nbsp;przedziału od 0&nbsp;do 1, do dwóch miejsc po przecinku.
* jaki jest szacowany czas do pełnego naładowania/rozładowania baterii.

Zwolennicy ponownie twierdzą, że to dla komfortu użytkowników. Jeśli mają słabą baterię, to strona [nie włączy](https://umaar.com/dev-tips/242-considerate-javascript/#load-javascript-when-the-device-has-enough-cpu) jakichś energożernych funkcji, zmniejszy rozdzielczość elementów i&nbsp;tak dalej.

Tylko że takie spojrzenie zakłada pewną niesamodzielność użytkowników. Nie lepiej by było dać gdzieś pstryczek, którym mogą ograniczyć zasoby na własne życzenie? Naprawdę strony muszą to czytać same z&nbsp;siebie?

Poziom baterii potrafi być całkiem mocnym sygnałem **łączącym ze sobą różne przeglądarki i&nbsp;adresy IP na jednym urządzeniu**.  
Wyobraźmy sobie: o&nbsp;pewnej godzinie po stronie X&nbsp;krążyło dość mało użytkowników. Jeszcze mniej -- z&nbsp;ustawionym polskim językiem. I&nbsp;nagle jeden z&nbsp;tych Polaków zniknął ze strony, ale pojawił się inny, również z&nbsp;baterią na poziomie 37% i&nbsp;takim samym czasem do rozładowania. Kim on może być, no kim?

Przeglądarka Brave, choć zbudowana na tym silniku co Chrome, zataja informacje o&nbsp;baterii. Podobnie robi Firefox. Natomiast bardziej „konsumenckie” przeglądarki na bazie silnika Chromium ochoczo to ujawniają.

# Informacje o&nbsp;sieci

Dostępne pod zbiorczą nazwą `Network Information API`.

Oprócz informacji o&nbsp;sprzęcie i&nbsp;baterii, JS może podpytać o&nbsp;[jakość połączenia z&nbsp;internetem](https://developer.mozilla.org/en-US/docs/Web/API/Network_Information_API). Oficjalnego powodu możecie się domyślać -- dla komfortu użytkowników! Żeby można było do nich dopasować zasobożerność strony. W&nbsp;praktyce to kolejne źródło informacji, którymi możemy się wyróżniać.

Podpytane przeglądarki mogą ujawnić między innymi przybliżony „poziom” sieci (*3G*, *4G*...) oraz jej rodzaj (np. komórkową), aktualną i&nbsp;maksymalną przepustowość łącza w&nbsp;megabitach na sekundę (`downlink` i&nbsp;`downlinkMax`), czas pełnego obiegu danych (`rtt`, od *round-trip time*) oraz informację o&nbsp;tym, czy mamy włączony tryb oszczędzania danych (`saveData`).

Wyobraźmy sobie, że zwykle korzystamy z&nbsp;wolnego mobilnego internetu, który często nam zmienia adres IP. Pewnego dnia odwiedzamy kogoś znajomego z&nbsp;wypasionym łączem szerokopasmowym.

Jeśli wejdziemy na swoje konto na wspomnianej wścibskiej stronie z&nbsp;zakupami, która dobrze nas zna, to szybkość naszego łącza w&nbsp;tym dniu będzie się wyróżniała.  
Strona będzie miała pewność, że podczas tej wizyty nie byliśmy u&nbsp;siebie. Pewność, której nie dałby jej sam adres IP, bo ten zmienia nam się często.

Ponownie: Brave i&nbsp;Firefox zatajają większość informacji z&nbsp;tej kategorii, przeglądarkowy mainstream ujawnia wszystko. Safari wyjątkowo z&nbsp;rigczem, zataja.

## Łączenie danych

Na koniec zwróćmy uwagę na to, że omawiane informacje nie występują w&nbsp;izolacji i&nbsp;można je łączyć w&nbsp;bardziej wyrafinowane kombinacje.

Jeśli z&nbsp;jakiejś strony korzystamy często, zalogowani na swoje konto, to JavaScript na dłuższą metę prześle o&nbsp;nas sporo danych. Właściciele strony mogą nas analizować. W&nbsp;dłuższym okresie wyłapią pewne typowe cechy.

Przykład? Załóżmy że zwykle przeglądamy strony, korzystając z&nbsp;komórki podpiętej do większego monitora. Strona jest w&nbsp;stanie to wychwycić:

* o&nbsp;wymiary ekranu po prostu zapyta. Spore, ewidentnie nie komórkowe;
* z&nbsp;drugiej strony pamięć i&nbsp;liczba rdzeni nie powalają, co sugeruje słabsze urządzenie;
* do tego czasem zapomnimy wpiąć ładowarkę, a&nbsp;wtedy strona odczyta, że ciągniemy z&nbsp;baterii.
* no i&nbsp;informacje o&nbsp;sieci mówią wprost: `cellular`.

Na tej podstawie **trafimy do mało licznej przegródki** „Preferencje: telefon + duży monitor”. Nie jest to sam w&nbsp;sobie jakiś unikalny sygnał. Ale jako wstępny odsiew albo sygnał wzmacniający sprawdzi się świetnie.

Nawet jeśli się wylogujemy, zmienimy adres IP, parametry naszej komórki są typowe, zaś monitorów takich jak nasz jest wiele -- możemy zostać rozpoznani. Dane z&nbsp;osobna nas nie zdradzają, ale ich połączenie już mocno zawęża krąg poszukiwanych.

Do tego chwilę przed tym, jak weszliśmy na stronkę anonimowo, z&nbsp;innego adresu IP, swoją aktywność na niej wstrzymał Adam Znany z&nbsp;tej samej rzadkiej przegródki.  
Czyżbyśmy byli nim?

A żeby nie było, że tu *science-fiction* tworzę -- polecam [odkrycie pewnego użytkownika](https://smitop.com/post/whiteops-data/) pokazujące, ile informacji próbowało zebrać przez JavaScript popularne **forum Reddit, zapewne korzystając z&nbsp;usług firmy HUMAN**.  
Niektóre z tych rzeczy to spoilery dotyczące przyszłego wpisu o&nbsp;JS-ie. 

## Jak się przed tym chronić?

Niuansów związanych z&nbsp;JavaScriptem jest multum. A&nbsp;przypominam, że pisałem tutaj o&nbsp;tych najłatwiej dostępnych, które przeglądarka ujawnia sama.

Ogólnie powiem tak: **to walka z&nbsp;wiatrakami**.  
Jasne, możemy łatać luki w&nbsp;naszej prywatności jedną po drugiej. Podsuwać stronom fałszywe informacje o&nbsp;naszym komputerze.  
Ale firmy śledzące nie siedzą biernie i&nbsp;doskonalą metody inwigilacji; któraś w&nbsp;końcu może nas złapać na kłamstwie. A&nbsp;wtedy, zamiast zlewać się z&nbsp;tłumem, staniemy się szczególnie rozpoznawalni.

Również przeglądarki nie zawsze będą po naszej stronie. W&nbsp;ich interesie leży przede wszystkim, żeby ludzie ich używali. Zatem domyślnie będą blokowały dość zachowawczo, nie chcąc się narażać na późniejsze skargi, że ludziom coś nie działa. I&nbsp;dodawały nowe, potencjalnie śledzące funkcje.

Ale to w&nbsp;żadnym razie nie znaczy, że trzeba się poddać! Po prostu, zamiast łatać jedną lukę po drugiej, proponuję pójść w&nbsp;rozwiązania bezkompromisowe.

# Całkowite wyłączenie JavaScriptu

Jesteśmy zwykłym użytkownikiem, który czasem chce zaznać trochę rozrywki. Czasem odwiedzamy też strony wścibskich amerykańskich korporacji. Nie chcemy ciągle być na bieżąco z&nbsp;metodami śledzenia, jak z&nbsp;jakimiś trendami w&nbsp;(*tfu*) modzie.

Ale równocześnie zgadzamy się z tym, że byłoby fajnie żyć bez świadomości, że jesteśmy pod lupą jakiegoś zbieracza danych.

Jeśli powyższy opis do nas pasuje, proponuję rozwiązanie łatwe, a&nbsp;skuteczne. **Mieć domyślnie wyłączony JavaScript. I&nbsp;włączać go jednym kliknięciem, kiedy sytuacja tego wymaga**. Ze świadomością, że wtedy odwiedzana strona może poznać sporo naszych danych.

Powiem uczciwie: do włączania JS-a będziemy zmuszani dość często.  
Bez niego czasem jakiś guzik wykona tylko połowę roboty po kliknięciu; to znowu podczas przewijania strony jej elementy się rozjadą (bo używała JS-a do ich ustawiania). Sposobów, w&nbsp;jakie coś może przestać działać, jest wiele.

Jeśli chodzi o&nbsp;sam sposób na wyłączanie -- proponuję robić to dodatkiem [uBlock Origin](https://ublockorigin.com/).  
Polecałem go już przy paru poprzednich wpisach, stworzyłem też [instrukcję instalacji]({% post_url 2021-10-21-ublock-origin %}){:.internal}. A&nbsp;skoro i&nbsp;tak warto go mieć, to możemy równie dobrze uczynić go naszym wyłącznikiem od JS-a. Działa też na mobilnym Firefoksie.

Przede wszystkim włączamy w&nbsp;ustawieniach, żeby JS był domyślnie blokowany. Najpierw wybieramy ikonę dodatku z&nbsp;górnego paska przeglądarki (warto go tam przypiąć), następnie klikamy ikonę zębatki (gdyby jej nie było, to klikamy `Więcej`, aż się rozwinie).  
Otworzy się osobne okno z&nbsp;opcjami. Wybieramy z&nbsp;nich wyłączenie JavaScriptu.

{:.bigspace}
<img src="/assets/posts/javascript-tracking/ubo-javascript-blokowanie.jpg" alt="Dwa rzuty ekranu pokazujące fragmenty okien dodatku uBlock Origin. Na pierwszym z&nbsp;nich wyróżniono kolorową ramką ikonę dodatku na górnym pasku oraz ikonę zębatki, od opcji. Na drugim widać zaznaczoną opcję pozwalającą wyłączyć JavaScript."/>

A kiedy trafimy na stronę, która bez skryptów nam nie zadziała?  
Klikamy ikonę dodatku, potem przekreślony znaczek z&nbsp;nawiasami ostrymi po prawej stronie. Gdy się "odkreśli", to znaczy że włączyliśmy JS-a. Powyżej pojawi się duży przycisk, który po kliknięciu odświeży stronę.

{:.figure .bigspace}
<img src="/assets/posts/javascript-tracking/ubo-javascript-odblokowanie.jpg" alt="Zrzut ekranu z&nbsp;okna dodatku uBlock Origin. Czerwonymi ramkami oznaczono trzy elementy. Numerem jeden podpisano ikonę dodatku na górnym pasku, numerem dwa przekreśloną ikonkę, numerem trzy ikonkę ze strzałkami, standardowo oznaczającą odświeżenie strony."/>

Przełączanie JS-a możemy również podpiąć w&nbsp;opcjach dodatku pod jakiś skrót klawiszowy.  
Więcej informacji znajdziecie [na stronie uBO](https://github.com/gorhill/uBlock/wiki/Per-site-switches#no-scripting).

Beztroskie surfowanie, a&nbsp;w razie czego kliknięcie dwóch rzeczy. Wiele osób sobie z&nbsp;tym poradzi.  
Ale mniej „komputerowi” dziadkowie/wujkowie mogliby nie docenić naszej troski, gdybyśmy szykowali im przeglądarkę i&nbsp;domyślnie wyłączyli JS-a. Dlatego proponuję zrobić to tylko za ich zgodą i&nbsp;po krótkim przeszkoleniu.

{% include info.html
type="Uwaga"
text="Czasem po wyłączeniu JavaScriptu możecie zwątpić, czy na pewno się udało, bo niektóre animacje nadal działają.  
Przykład: [blog techniczny Mozilli](https://hacks.mozilla.org/). Jeśli używacie komputera z&nbsp;myszką i&nbsp;najedziecie kursorem na napis *HACKS*, to literka *K* się przekręci. Nawet jeśli macie wyłączony JavaScript.  
Na szczęście to złudzenie; niektóre animacje po prostu nie zależą od JavaScriptu, tylko opierają się na tak zwanych *arkuszach styli CSS*. Po bliższym spojrzeniu widzimy, że ta literka była otoczona osobnym stylem."
trailer="<p class='bigspace-before'><img src='/assets/posts/javascript-tracking/mozilla-hacks-css.jpg' alt='Zrzut ekranu pokazujący ekran przeglądarki. Widać tam napis HACKS. Pod spodem widać narzędzia przeglądania, ukazujące że literka K&nbsp;jest otoczona osobnymi tagami.'/></p>"
%}

# Korzystanie z&nbsp;publicznych komputerów

Mamy też rozwiązanie na poważniejsze przypadki -- gdy chcemy szukać informacji legalnych, ale bardzo osobistych. A&nbsp;stronka jednak JavaScriptu wymaga.

Może na przykład na coś zachorowaliśmy i&nbsp;chcemy o&nbsp;tym poczytać. Ale ubezpieczyciel, gdyby się dowiedział, przyciąłby nam nasz dystopijny *social credit score*.

W takim wypadku idźmy na całość!
 
Warto się przejść do jakiejś kafejki internetowej, biblioteki publicznej albo uczelnianej czytelni. Znam niejedną, do której dało się wejść bez żadnego zostawiania dokumentu. A&nbsp;nawet gdyby był potrzebny, to i&nbsp;tak prywatne firmy nie mają na tyle władzy, żeby dzwonić do bibliotek i&nbsp;pytać o&nbsp;dane osobowe.

Dla pewności nie bierzemy telefonu albo wyłączamy w&nbsp;nim łapanie hotspotów i&nbsp;geolokalizację. Nie chcemy, żeby jakaś wścibska apka powiązała z&nbsp;nami taki sam adres IP, z&nbsp;jakiego robiliśmy anonimowe wyszukiwanie.

Potem siadamy i&nbsp;przeglądamy. Korzystając z&nbsp;obcego komputera, mamy inny adres IP, inne parametry urządzenia... Prawie wszystko inne. Teraz nawet wścibski JavaScript może nie być w&nbsp;stanie nas rozpoznać.
 
Trzeba tylko pamiętać, żeby podczas surfowania **nie logować się na żadne swoje konta**, nie odwiedzać swojego osobistego bloga. Nie robić rzeczy, które by powiązały wyszukiwania z&nbsp;jakimś konkretnym człowiekiem.

Pamiętajmy, że miejsca publiczne, nawet jeśli są poza wpływami większych firm, mają z&nbsp;kolei swoich administratorów. Być może znudzonych i&nbsp;wścibskich.

# Wtopienie się w&nbsp;tłum

A jeśli już musimy odwiedzić jakąś stronę z&nbsp;JavaScriptem? A&nbsp;przy tym to nic na tyle drażliwego, żeby dreptać do biblioteki?

W takim wypadku starajmy się minimalizować informacje, jakie ukazuje nasza przeglądarka. Jednocześnie nie odchodząc zanadto od domyślnych ustawień.

* Korzystamy z&nbsp;przeglądarki względnie popularnej.
* I&nbsp;z jej względnie nowej wersji. Raz, że zlejemy się z&nbsp;tłumem ludzi aktualizujących na bieżąco. Dwa, że nówka powinna być bardziej doszlifowana.
* ...Ale **najlepiej nie z&nbsp;Chrome'a, Chromium, Opery, Edge'a**...

  Są najpopularniejsze, ale też bardziej konsumenckie. Otwierają dla JavaScriptu coraz to nowe możliwości, których ten może potem nadużyć w&nbsp;celu profilowania.  
  Moim zdaniem najlepiej korzystać z&nbsp;[Firefoksa](https://www.mozilla.org/pl/firefox/new/) i&nbsp;[Brave'a](https://brave.com/) albo czegoś na ich bazie.  
  Będziemy rzadsi niż chrome'owcy, jasne. Ale dużo opcji prywatnościowych będzie włączonych domyślnie. Więc z&nbsp;jednej strony blokujemy część mocy JS-a, a&nbsp;z drugiej nie wyróżniamy się spośród innych użytkowników Brave'a/FF.

Rzeczy poniżej to niuanse i&nbsp;bzdety w&nbsp;porównaniu z&nbsp;tymi wyżej. Ale zawsze pozwalają nieco zmniejszyć ilość ujawnianych informacji.

* Urządzenie naładowane do pełna i&nbsp;podłączone do prądu  
  (kontra wobec `Battery API`).
* Ekran/monitor w&nbsp;dość typowych rozmiarach; okno przeglądarki ustawione na cały ekran; nie chowamy żadnych domyślnych pasków  
  (kontra wobec informacji o&nbsp;ekranie).
* Nie żyć ponad stan :wink: Procesor, pamięć i&nbsp;łącze internetowe mieć jak najbardziej przeciętne; przynajmniej w&nbsp;skali swojej okolicy  
  (kontra wobec informacji o&nbsp;sprzęcie/połączeniu).

Jeśli ktoś korzysta z&nbsp;iPhone'a, to mam złe wieści -- **jakiej przeglądarki się nie wybierze, za kulisami będzie silnik od Apple**. A&nbsp;ta firma pod względem „uprywatniania” przeglądarki nie jest jakoś szczególnie aktywna.

# Sprytniejsze otwieranie narzędzi przeglądarki

Tu coś dla osób, które chcą zaglądać za kulisy szemranych stron.

Pokazałem w&nbsp;tym wpisie, w&nbsp;jaki sposób strona może się zorientować, że otworzyliśmy narzędzia przeglądarki:

* użyliśmy konkretnego skrótu klawiszowego,
* nagle zmieniły się nam rozmiary okna.

Żeby nie ujawniać tych informacji, najlepiej **otwierać narzędzia przeglądarki z&nbsp;wyprzedzeniem, w&nbsp;osobnym oknie**. Otwieramy je na jakiejś bezpiecznej stronie, przed odwiedzeniem szpiegującej. Potem wybieramy opcję z&nbsp;menu po prawej stronie.

{:.figure .bigspace}
<img src="/assets/posts/javascript-tracking/devtools-osobne-okno.jpg" alt="Zrzut ekranu z&nbsp;narzędzi przeglądarki, pokazujący rozwinięte menu i&nbsp;wybraną opcję otwierania w&nbsp;osobnym oknie."/>

# LibreJS i&nbsp;inne opcje pośrednie

A może dałoby się w&nbsp;jakiś sposób **wyłączyć wścibskie części JavaScriptu, a&nbsp;pozostawić te przydatne**?

Z takiego założenia wyszli ludzie z&nbsp;Free Software Foundation, proponując [podzbiór JavaScriptu](https://www.gnu.org/philosophy/javascript-trap.html) prosty, czytelny i&nbsp;niegroźny dla użytkowników. Stworzyli również [LibreJS](https://www.gnu.org/software/librejs/) -- dodatek do Firefoksa pozwalający wyłapywać mniej sympatyczne wersje JS-a.

Tylko jedna sprawa. Jeśli ktoś jeszcze nie słyszał o&nbsp;tym ruchu, to warto wspomnieć, że są dość... bezkompromisowi.  
Jako nieprzyjazność dla użytkowników rozumieją również rzeczy mocno zakorzenione we współczesnej kulturze tworzenia JS-a. Takie jak zmniejszanie rozmiaru kodu przez usuwanie z&nbsp;niego spacji.

Z tego względu raczej nie ma co liczyć na szersze poparcie dla wizji LibreJS. Ale sam pomysł stworzenia „nieszkodliwego” podzbioru JavaScriptu, który nasza przeglądarka by dopuszczała, jak najbardziej ma ręce i&nbsp;nogi.  
Osoby zainteresowane programowaniem i&nbsp;„naprawieniem internetu” mogą **obserwować zarówno LJS, jak też inne podobne inicjatywy**.

Mam nadzieję, że w&nbsp;tryby internetowej machiny śledzącej będą coraz częściej wpadały drobiny żwiru. Nawet jeśli jedna nic nie zmieni, to w&nbsp;większych ilościach mogą rozwalić niejeden mechanizm.

W kolejnym wpisie przyjrzymy się tej machinie jeszcze dokładniej. Ciepłego maja życzę! :sunglasses:

