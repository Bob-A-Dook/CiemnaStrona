---
layout: post
title: "Tryb prywatny (incognito) bez tajemnic"
subtitle: "Listek figowy czy doskonały kamuflaż?"
description: "Listek figowy czy doskonały kamuflaż?"
date:   2024-09-09 21:00:00 +0100
tags: [Internet, Inwigilacja, Podstawy]
image:
  path: /assets/posts/inwigilacja/tryb-prywatny-incognito/tryb-prywatny-baner.jpg
  width: 1200
  height: 700
  alt: "Przeróbka mema. Dwie dziewczyny śmieją się z chłopaka w kapelusiku i okularkach z ikony trybu incognito. Na koszulkach mają loga Google i Mety."
---

Chyba każda współczesna przeglądarka zawiera tryb prywatny, zwany czasem trybem incognito. Wystarczy jedno kliknięcie w&nbsp;opcjach albo skrót klawiszowy, żeby go włączyć.

Często pojawi się ikonka sugerująca prywatność (na Firefoksie -- maska w&nbsp;stylu Zorro). Motyw kolorystyczny zmieni się na ciemniejszy z&nbsp;odrobiną fioletu. Budzi toto respekt... więc wiele osób, bez wnikania w&nbsp;szczegóły, uznaje swoją prywatność za chronioną i&nbsp;beztrosko surfuje dalej.

Inni idą w&nbsp;drugą skrajność i&nbsp;nazywają cały tryb bublem. Mówią, że można nim co najwyżej ukryć historię przeglądania przed rodzicami. Skądś zresztą się wzięła potoczna nazwa „tryb p*rno”.

{:.post-meta .bigspace-after}
Mikrocenzura, żeby udobruchać różne głupkowate Ej-Aj indeksujące treści.

A prawda, jak to zwykle bywa, leży gdzieś między skrajnościami. W&nbsp;tym wpisie przybliżę prawdziwą naturę trybu prywatnego. Będą liczne nawiązania do wpisów, które się jak dotąd nagromadziły na Ciemnej.

Zapraszam! :smile:

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/tryb-prywatny-incognito/tryb-prywatny-baner.jpg" alt="Przeróbka mema. Dwie dziewczyny śmieją się z chłopaka w&nbsp;kapelusiku i&nbsp;okularkach z&nbsp;ikony trybu incognito. Na koszulki dziewczyn nałożono loga Google i&nbsp;Mety."/>

{:.figcaption}
Źródła: popularny mem, [maska Guya Fawkesa](https://www.flaticon.com/free-icon/guy-fawkes-mask_2302370) ze strony Flaticon autorstwa *photo3idea_studio*, dymek z&nbsp;Libre Office'a. Przeróbki moje.

## Spis treści

* [Powszechne błędne wyobrażenia](#powszechne-błędne-wyobrażenia)
* [Prawdziwa natura trybu prywatnego](#prawdziwa-natura-trybu-prywatnego)
* [Lista zapominanych rzeczy](#lista-zapominanych-rzeczy)
  * [Historia przeglądania](#historia-przeglądania)
  * [Pamięć podręczna](#pamięć-podręczna)
  * [Ciasteczka](#ciasteczka)
  * [Pliki ciastkopodobne](#pliki-ciastkopodobne)
  * [Wątki usługowe](#wątki-usługowe)
  * [Dodatki przeglądarkowe](#dodatki-przeglądarkowe)
* [Luki w&nbsp;trybie prywatnym](#luki-wtrybie-prywatnym)
  * [Adres IP](#adres-ip)
  * [Profilowanie przez JavaScript](#profilowanie-przez-javascript)
  * [Parametry w&nbsp;linkach](#parametry-wlinkach)
  * [Analiza ruchu sieciowego](#analiza-ruchu-sieciowego)
  * [Podsumowanie wątku](#podsumowanie-wątku)
* [Safari i&nbsp;mocniejszy tryb prywatny?](#safari-imocniejszy-tryb-prywatny)
* [Jak korzystać z&nbsp;trybu prywatnego](#jak-korzystać-ztrybu-prywatnego)
  * [Nie logować się na główne konta](#nie-logować-się-na-główne-konta)
  * [Zamaskować adres IP](#zamaskować-adres-ip)
  * [Nie wyrażać zgód na profilowanie](#nie-wyrażać-zgód-na-profilowanie)
  * [Użyć dodatku uBlock Origin](#użyć-dodatku-ublock-origin)
  * [Dla chętnych: ochronić się przed JavaScriptem](#dla-chętnych-ochronić-sięprzed-javascriptem)
* [Podsumowanie](#podsumowanie)


{% include info.html
type="Krótko"
text="Gdyby komuś nie chciało się czytać całości -- tryb prywatny to nietypowy miks. Ukrywa szeroki zakres informacji, czasem subtelnych. Ale nie wpływa na adres IP, czyli dość podstawową cechę identyfikującą.  
Jeśli przed użyciem trybu „zmieni się” adres IP (np. przez użycie innego hotspota niż zwykle), to jego skuteczność znacząco wzrośnie. Jeśli do tego użyje się dodatku blokującego reklamy śledzące i&nbsp;wyłączy się JavaScript, to już w&nbsp;ogóle super.  
A bez tych uzupełniających zmian? Lepiej używać trybu co najwyżej do rzeczy prozaicznych."
%}

## Powszechne błędne wyobrażenia

Niektóre osoby wierzą, że tryb prywatny zapewnia mocną ochronę. Szczególnie jaskrawym przypadkiem jest sprawa z&nbsp;USA, gdzie na Google'a [nałożono karę 5&nbsp;miliardów dolarów](https://www.reuters.com/legal/google-settles-5-billion-consumer-privacy-lawsuit-2023-12-28/).  
Nazwa *trybu incognito* w&nbsp;przeglądarce Chrome oraz jego opis rzekomo wprowadzały ludzi w&nbsp;błąd, dając im błędne oczekiwania, że wszystkie ich dane są chronione.

Jak za Wielkim G&nbsp;nie przepadam, tak ten wyrok budzi u&nbsp;mnie mieszane uczucia. Bo trudno mi uwierzyć, że tryb miał tak dobre opinie.  
W gronie znajomych osób, wielu całkiem niekomputerowych, był raczej uważany za lekkie udogodnienie, bajer. Jeśli ktoś miał skrajną opinię, to raczej w&nbsp;drugą stronę, uważając go za zabawkę do ukrywania historii.

Z jednej strony chce się machnąć ręką. „Paanie, to USA. Idiokracja i&nbsp;prawnicy”. Ale z&nbsp;drugiej -- może to ja żyłem w&nbsp;bańce? Bo doniesienia o&nbsp;wierze ludzi w&nbsp;ten tryb mają potwierdzenie również w&nbsp;[badaniu z&nbsp;Wielkiej Brytanii](https://brave.com/blog/private-mode-is-not-really-private/).  
Przeprowadzili je w&nbsp;2018 roku ludzie od przeglądarki Brave i&nbsp;doszli do wniosku, że użytkownicy mogą wiązać z&nbsp;trybem nierealistyczne oczekiwania.

## Prawdziwa natura trybu prywatnego

Zarówno „prywatny”, jak i&nbsp;„incognito” nie do końca oddają istotę tego trybu. Jego działanie nie polega na tym, że celowo dąży do walki z&nbsp;metodami profilowania stosowanymi w&nbsp;internecie przez firmy reklamowe.

Osobiście, gdybym miał wymyślić nazwę bliższą działaniu, nazwałbym go „trybem ulotnym”, „trybem nietrwałym” albo „trybem czystej kartki”.

Polega po pierwsze na tym, że **przeglądarka „ignoruje swój dorobek” z&nbsp;normalnego trybu** i&nbsp;pozwala przeglądać internet takim, jakim widziałby go całkiem nowy użytkownik, świeżo po jej zainstalowaniu.  
Po drugie: na tym, że **dorobek zgromadzony w&nbsp;trybie prywatnym jest ulotny, tymczasowy**. Zostanie wyrzucony po zakończeniu sesji przeglądania. 

Analogia? To trochę jak rozpoczęcie gry komputerowej od nowa, mimo że dałoby się wczytać którąś z&nbsp;zapisanych migawek. A&nbsp;potem pogranie przez chwilę i&nbsp;wyłączenie gry, bez jej zapisywania.

Inna analogia? To jak zostawienie w&nbsp;domu swojego plecaka, w&nbsp;którym przez lata nagromadziło się różnych identyfikatorów, dokumentów, kart członkowskich. Po czym wyruszenie na krótką wyprawę z&nbsp;całkiem nowym, pustym. Z&nbsp;założeniem, że co się wydarzy na wyprawie, to zostaje na wyprawie.

## Lista zapominanych rzeczy

Wyżej porównałem działanie trybu prywatnego do „zignorowania swojego dorobku”. W&nbsp;przypadku przeglądarek są nim rzeczy, które sobie zapisały na dysku, gdzieś w&nbsp;wewnętrznym folderze, podczas wędrówek po sieci.  
Są one dość zróżnicowane i&nbsp;należą do nich:

* historia przeglądania,
* pamięć podręczna,
* pliki *cookies* („ciasteczka”),
* pliki „ciastkopodobne”,
* wątki usługowe (ang. *service workers*),
* dodatki przeglądarkowe.

Omówię te rzeczy po kolei. Na przykładzie Firefoksa, ale sporo zasad jest uniwersalnych.  
Dla lepszej intuicji przy każdej rzeczy wskażę najpierw, czemu z&nbsp;założenia ma służyć. A&nbsp;potem -- w&nbsp;jaki sposób może być nadużywana do celów rozpoznawania i&nbsp;profilowania użytkowników.

### Historia przeglądania

Do niektórych stron wraca się często. Dlatego przeglądarki sobie notują odwiedzone przez nas adresy i&nbsp;same je potem podpowiadają, choćby po wpisaniu pierwszych literek w&nbsp;górnym pasku.

Historia przeglądania może intuicyjnie wydawać się celem numer jeden dla reklamodawców. Ale tak naprawdę jest dla nich mało przydatna, bo niedostępna. Przeglądarki **nie dają cudzym stronom wglądu do historii**.

Istnieje pewna [baaardzo okrężna metoda]({% post_url 2023-08-19-historia-przegladania %}){:.internal}, pozwalająca poznać część historii. W&nbsp;tym celu strony musiałyby zamaskować linki i&nbsp;podpuścić użytkowników, żeby sami kliknęli te do stron, na których byli. Metoda niepewna i&nbsp;łatwa do wykrycia dla czujniejszych oczu. Dlatego raczej nie skorzystają z&nbsp;niej masowi reklamodawcy.

Czyszczenie historii daje korzyść głównie wtedy, gdy z&nbsp;jednego komputera korzysta więcej osób, jak cała rodzinka. Jedna osoba może dzięki temu mieć pewność, że inni nie zobaczą, co wcześniej przeglądała.

{:.post-meta .bigspace-after}
Pomijam przypadek, gdy ktoś zainstalował na komputerze oprogramowanie śledzące; założmy, że rodzina by sobie tego nie zrobiła.

### Pamięć podręczna

Strony internetowe zawierają często wiele powtarzających się elementów. Przykład: logo Ciemnej Strony, każdorazowo obecne w&nbsp;nagłówku.

Żeby nie pobierać takich elementów wiele razy, przeglądarka zapisuje je sobie w&nbsp;wewnętrznym folderze, w&nbsp;tak zwanej [pamięci podręcznej]({% post_url 2021-12-24-caching %}){:.internal}. Potem, po napotkaniu obrazka o&nbsp;takim samym linku, po prostu bierze go z&nbsp;pamięci, zamiast prosić o&nbsp;niego ponownie. Oszczędność :+1:

Wścibskie strony mogą jednak nadużyć tej funkcji i&nbsp;serwować każdej osobie *nieco inne pliki*. Gdy któraś przeglądarka się przyzna, że już ma plik o&nbsp;identyfikatorze *AHD291K34*, to nieświadomie przyznaje, że odpowiada jej konkretny użytkownik.

{:.post-meta .bigspace-after}
W praktyce identyfikatorem jest tu atrybut zwany `ETag`, którego działanie opisałem w&nbsp;podlinkowanym wpisie.

Nie jest to najczęstsza metoda śledzenia, ale istnieje. Nie ujawniając identyfikatorów z&nbsp;głównego konta, tryb prywatny daje tu realną pomoc.

### Ciasteczka

We współczesnych czasach powszechne jest logowanie się do różnych stron i&nbsp;usług. A&nbsp;żeby strona wiedziała, że ma wyświetlić danej osobie treści z&nbsp;konta Adama G., a&nbsp;nie Kamili J., musi korzystać z&nbsp;jakichś *identyfikatorów* rozróżniających te osoby.

Tym są właśnie tak zwane [*pliki cookies*]({% post_url 2021-10-22-pliki-cookies %}){:.internal}. Drobne pliki tekstowe, zapisywane przez przeglądarkę na dysku i&nbsp;automatycznie okazywane tej samej stronce, od której zostały otrzymane.  
Ich wygląd jest dowolny. Ale w&nbsp;przypadku logowania żelazna zasada jest taka, że użytkownik A&nbsp;musi mieć coś innego niż użytkownik B.

Przypadek logowania ma pełne uzasadnienie. Gorzej, że pliki cookies mogą być wręczane i&nbsp;odczytywane nie tylko przez stronę bezpośrednio odwiedzaną, ale również przez właścicieli mniejszych elementów „goszczących” na tejże stronie.

Są to wtedy tzw. pliki cookies od stron zewnętrznych (ang. [*third-party cookies*]({% post_url 2021-12-08-cookies-piksele-sledzace %}){:.internal}). Narzędzie reklamodawców i&nbsp;**filar współczesnego internetowego śledzenia**. Pozwalają wiązać aktywność jakiejś osoby na stronie A&nbsp;z aktywnością na B, C, D... Przykładami elementów stosujących tę metodę są Facebook Pixel czy Google Analytics.

Włączenie trybu prywatnego sprawia, że przeglądarka nie pokazuje ciastek, jakie zgromadziła w&nbsp;czasie typowej aktywności. Daje zatem *ogromną* korzyść dla prywatności... Chyba że reklamodawcy znajdą sposób, żeby jakoś powiązać ciastka z&nbsp;sesji prywatnej z&nbsp;konkretnym profilem.

### Pliki ciastkopodobne

Strony internetowe potrzebują często **składzików na trwalsze dane** (oficjalny termin to *persistent storage*). Możliwości zapisania ich na komputerze użytkowników i&nbsp;późniejszego odczytania.  
Wydawać by się mogło, że ciasteczka i&nbsp;pamięć podręczna do tego wystarczą. Ale obie metody miały swoje ograniczenia:

1. Pamięć podręczna pozwala przechowywać większe pliki, ale strony długo miały do niej [ograniczony dostęp](https://stackoverflow.com/questions/8155064/how-to-programmatically-empty-browser-cache).
2. Do ciasteczek mają dostęp, ale są one wysyłane przy każdym kontakcie ze stroną.  
   Gdyby twórcy stron próbowali tam upchać więcej danych, to przeglądarki by im to potem odesłały, jak wracający bumerang. Większe obciążenie serwerów, niepotrzebne koszty.

Te ograniczenia sprawiły, że pojawiło się zapotrzebowanie na inny rodzaj składzików na dane. A&nbsp;twórcy przeglądarek wyszli tej potrzebie naprzeciw, tworząc kilka rodzajów takich składzików -- *localStorage*, *sessionStorage*, *IndexedDB*. Albo i&nbsp;więcej.

Niech twórcy stron wybaczą mi ignorancję, ale wrzucę je wszystkie do jednego wora. Jako „pliki ciastkopodobne”, bo **w kontekście śledzenia działają niemal identycznie jak pliki _cookies_**.

Gdy ktoś odwiedza stronę A, to obecny na niej reklamodawca każe przeglądarce zapisać jakiś identyfikator do pliku ciastkopodobnego.  
Gdy ta sama osoba odwiedza stronkę B, na której jest ten sam reklamodawca, to przeglądarka mu wręcza na życzenie to, co wcześniej zapisała. On zaś może sobie zapisać, że osoba odwiedzająca stronkę B&nbsp;była chwilę wcześniej na A.

{% include info.html
type="Ciekawostka"
text="Na plikach ciastkopodobnych może również bazować **wykrywanie trybu prywatnego**. Strona najpierw każe przeglądarce coś do nich zapisać, a&nbsp;zaraz potem próbuje to samo odczytać.  
Jeśli ktoś zaprojektował swój tryb prywatny w&nbsp;taki sposób, że po prostu *wyłącza wszelkie przechowywanie plików*, to na tym etapie przeglądarka wpadnie. Nie będzie w&nbsp;stanie dać stronie rzeczy, o&nbsp;którą ta prosi. Strona uzna to za oznakę włączonego trybu prywatnego i&nbsp;na przykład [odmówi użytkownikom dostępu](https://news.ycombinator.com/item?id=33269391)."
%}

### Wątki usługowe

To tak naprawdę **skrypty w&nbsp;języku JavaScript**, zapisywane wewnątrz przeglądarki jak ciasteczka. Różnica polega na tym, że nie są „martwymi” danymi, lecz „żywym” kodem. Czymś, co może zostać uruchomione i&nbsp;działać w&nbsp;tle.

Ich istnienie jest uzasadnione tym, że pozwalają tworzyć aplikacje działające częściowo lub całkowicie *offline*, bez dostępu do internetu.  
Oczywiście można ich też nadużyć. Omówienie paru kreatywnych metod śledzenia można znaleźć [w tym filmie](https://www.youtube.com/watch?v=2NSU1MkE2mM) (uwaga: YouTube).

Ale abstrahując nawet od innych zagrożeń -- te skrypty mają dostęp do paru [własnych składzików](https://www.w3.org/TR/service-workers/#privacy) na dane. Mogą zatem zostać nadużyte w&nbsp;ten sam sposób co ciastka i&nbsp;rzeczy ciastkowate, zaś ich ukrycie w&nbsp;trybie prywatnym może dać konkretne korzyści.

### Dodatki przeglądarkowe

Dodatków jest mnóstwo i&nbsp;mogą na wszelkie sposoby zmieniać działanie przeglądarki. Ich domyślne wyłączanie w&nbsp;trybie prywatnym (które da się zmienić) to taki trochę miecz obosieczny. Raz daje prywatność, raz odbiera.

* Daje wtedy, kiedy wyłącza dodatki modyfikujące treść stron i&nbsp;dodające np. tłumaczenia/adnotacje.

  Wredne strony mogłyby się „przeskanować” zawartym w&nbsp;sobie kodem. Wychwycić nietypowe elementy i&nbsp;wysłać ich listę swoim właścicielom. Wyróżniałoby to z&nbsp;tłumu osoby używające określonych dodatków. 

* Odbiera wówczas, gdy wyłącza blokery reklam śledzących (jak uBlock Origin, o&nbsp;którym jeszcze wspomnę).

  Ingerują one w&nbsp;ruch sieciowy, utrudniając wysyłanie danych do reklamodawców. Gdy są wyłączone, zaś reklamodawca w&nbsp;jakiś sposób uzyska informacje o&nbsp;prawdziwej tożsamości konta -- to zdoła je sobie wysłać.

## Luki w&nbsp;trybie prywatnym

Było trochę pochwał, więc teraz czas na ograniczenia trybu prywatnego, przez które wydaje się nie do końca zasługiwać na swoją nazwę.

### Adres IP

To moim zdaniem **najważniejsza rzecz, która często przekreśla użyteczność trybu prywatnego**.

Sam w&nbsp;sobie nie jest jakimś potężnym identyfikatorem -- może dlatego, że rzadko kiedy jest jednocześnie przypisany do jednej osoby i&nbsp;niezmienny w&nbsp;czasie.  
Tam, gdzie jest raczej niezmienny (sieci firmowe), tam często korzysta z&nbsp;niego wiele osób. Tam, gdzie jeden adres to jedna osoba (np. smartfony i&nbsp;sieć mobilna), tam co pewien czas operator przydziela nowy.

Spośród identyfikatorów najbardziej wyróżnia go jednak inny fakt -- [adresu IP nie da się sfałszować]({% post_url 2021-06-12-adres-ip %}){:.internal}. Gdyby jakieś urządzenie „podpisywało się” zmyślonym adresem IP, to by nie otrzymywało odpowiedzi. Dokładnie tak, jakby podać fałszywy adres na fizycznej kopercie. Jedynym sposobem na prywatną, ale działającą komunikację jest korzystanie z&nbsp;pośredników, jak VPN-y.

W takich realiach reklamodawcy mogą traktować adres IP jak znakomity *identyfikator pomocniczy użytkowników*. Pomost między tożsamościami.

Przykładowa sytuacja? Ktoś sobie czyta artykuł na portalu gazety, zalogowany na swoje konto. W&nbsp;podpowiedziach widzi inny artykuł. Ciekawy, ale kontrowersyjny.  
Nie chcąc, żeby to powiązano z&nbsp;jego profilem, klika prawym przyciskiem i&nbsp;otwiera nową kartę w&nbsp;trybie prywatnym. W&nbsp;tym momencie jest wylogowany (bo tryb prywatny ukrywa ciasteczka), ale nadal może przeglądać artykuły jako anonimowy gość.

Ale portal medialny od razu skojarzy po adresie: „oho, mam anonima z&nbsp;adresem IP, którego przed sekundą używał zalogowany Andrzej Mruczek”.

Czasem z&nbsp;jednego adresu IP korzysta wiele osób. Dlatego przypadki `zalogowany → anonim (ten sam adres)` nie zawsze są z&nbsp;automatu uznawane za jedną osobę i&nbsp;najpierw trafiają do dalszej analizy.  
Analizator sprawdza listę artykułów, jakie zostały podpowiedziane Andrzejowi. Jest wśród nich ten, który krótko po tym wyświetlił anonim z&nbsp;tego samego adresu. Zbieżność IP, czasu, linków -- to na 90% Andrzej!

### Profilowanie przez JavaScript

Tryb prywatny nie ochroni również przed innym, dużo wredniejszym sposobem śledzenia -- metodami wykorzystującymi JavaScript.

JavaScript nie jest niczym egzotycznym. To popularny język programowania, który można nawet uznać za swoisty *język programowania internetu*. Jeden z&nbsp;niewielu, jakie są w&nbsp;stanie przetwarzać przeglądarki.

Egzotyczne są natomiast [metody śledzenia z&nbsp;jego udziałem]({% post_url 2022-05-03-javascript2 %}){:.internal}. Pytanie o&nbsp;parametry karty graficznej. Nakazywanie przeglądarce, żeby wykonywała różne złożone zadania, rysowała litery i&nbsp;kształty, miksowała dźwięki. Wszystko za kulisami, poza zasięgiem zmysłów internautów.

Na tym samym urządzeniu efekt tych samych działań będzie zwykle podobny. Ale może się różnić między urządzeniami. Można go zatem potraktować jak przybliżony identyfikator i&nbsp;rozpoznać osobę, która wcześniej miała styczność z&nbsp;innymi reklamami. Nawet jeśli od tamtego czasu zmieniła adres IP i&nbsp;wyczyściła ciasteczka.

Tryb prywatny chroni co najwyżej przed paroma możliwościami JS-a, jak analiza dodatków i&nbsp;składzików na dane. **Jest natomiast bezradny wobec profilowania sprzętu**.  
Ale stanę tu w&nbsp;obronie trybu prywatnego -- przed tak inwazyjną metodą nie ochroni praktycznie nic, poza wyłączeniem JavaScriptu lub zmianą urządzenia. Nie wyróżnia się więc na niekorzyść.

{% include info.html
type="Ciekawostka"
text="Istnieje też metoda [profilowania poprzez obrazki i&nbsp;arkusze styli](/internetowa_inwigilacja/2023/08/06/obrazki-css-html-sledzenie){:.internal}. Polega na tym, że strona oferuje przeglądarce wiele obrazków, dla różnych wariantów ustawień (wymiary ekranu, tryb kontrastowy itp.). Przeglądarka pobiera tylko ten, który najlepiej do niej pasuje. Przy okazji ujawnia coś o&nbsp;sobie.  
To metoda o&nbsp;tyle zwodnicza, że daje część możliwości JavaScriptu, a&nbsp;działa nawet wtedy, gdy jest wyłączony. Tryb prywatny przed tym nie chroni, bo profilowanie następuje *w&nbsp;momencie pobrania elementu*. A&nbsp;samo pobieranie działa bez zmian."
%}

### Parametry w&nbsp;linkach

Wyobraźmy sobie, że pewien szary obywatel, Normi Losowski, jest subskrybentem sporego portalu z&nbsp;newsami i&nbsp;regularnie go czyta, zalogowany na swoje konto. Regularnie dostaje też na maila gazetkę z&nbsp;listą artykułów, które mogłyby go zainteresować.

Pewnego razu widzi na tej liście artykuł: „Pizza z&nbsp;ananasem -- nie taka zła?”.  
Tytuł i&nbsp;clickbaitowy obrazek budzą jego ciekawość, aż chce sprawdzić... Ale głupio to łączyć ze swoim głównym kontem, bo jeszcze strona go zaszufladkuje jako zwolennika.

Dlatego klika link prawym przyciskiem myszy, wybiera `Otwórz w nowej karcie w trybie incognito` i&nbsp;zaczyna czytać. Niezalogowany na swoje konto i&nbsp;przekonany, że nie powiążą artykułu z&nbsp;jego tożsamością.

Problem w&nbsp;tym, że pod koniec tego linku -- i&nbsp;wszystkich innych, jakie portal wysyłał Normiemu -- znajduje się fragment: `?czytelnik=normi_losowski`. Inny link dla każdego zarejestrowanego użytkownika, żeby dało się ich rozróżniać.

To tak zwane [parametry śledzące]({% post_url 2021-04-09-internetowa-inwigilacja-parametry %}){:.internal}. Nie dają może gwarancji, że używa ich konkretna osoba (w&nbsp;końcu Normi mógł np. skopiować link z&nbsp;maila i&nbsp;podesłać znajomej)... Ale portal nic nie straci, jeśli tak założy i&nbsp;przypisze informacje do teczki Normiego.  
Tryb prywatny nic tu nie zmienia, bo nie ingeruje w&nbsp;linki.

### Analiza ruchu sieciowego

Wszystkie dotąd wymienione metody są czymś, czego mogą użyć przeciw użytkownikom odwiedzane stronki -- albo goszczący na nich reklamodawcy.

Ale potencjalnych podglądaczy jest więcej. Każdy, kto korzysta z&nbsp;internetu, musi bowiem korzystać z&nbsp;usług jakiegoś operatora. Tego, kto zapewnia router albo sieć mobilną. Ci operatorzy też mogą gromadzić dane.

Z ich punktu widzenia tryb prywatny nie robi *żadnej* różnicy. I&nbsp;tak nie widzieli zwykle informacji, które on ukrywa, bo były zaszyfrowane podczas transportu. [Ich metody śledzenia]({% post_url 2024-03-28-analiza-ruchu %}){:.internal} opierają się zamiast tego na adresach IP, nazwach stronek, może rozmiarze danych.

A tryb prywatny, jak już zasugerowałem wyżej, kompletnie na te rzeczy nie wpływa.

### Podsumowanie wątku

Widać, że tryb prywatny jest dość nierówny, a&nbsp;jego działanie (lub czasem brak) trudno wytłumaczyć chęcią dbania o&nbsp;prywatność.

Czasem czyści rzeczy mało przydatne dla podglądaczy (historia). Z&nbsp;drugiej strony blokuje nawet całkiem subtelne metody (śledzenie przez pamięć podręczną czy pliki ciastkopodobne)... Ale potem z&nbsp;kolei ujawnia informacje umożliwiające łatwą identyfikację, jak adres IP czy wymiary okna. 

Bez sensu? Ależ nie. **Istotą trybu jest jego ulotność, niezapisywanie na dysku. Nieco lepsza prywatność jest tylko efektem ubocznym**.

## Safari i&nbsp;mocniejszy tryb prywatny?

Dla uproszczenia pisałem dotąd o&nbsp;trybie prywatnym w&nbsp;liczbie pojedynczej, bez różnicowania. A&nbsp;przecież przeglądarki są różne.

Apple planuje wprowadzić w&nbsp;swojej przeglądarce, Safari, tryb [Private Browsing 2.0](https://webkit.org/blog/15697/private-browsing-2-0/). Ma on łatać parę wspomnianych wyżej luk, faktycznie zbliżając go do czegoś, co daje prywatność. Ma między innymi:

* Stosować Private Relay.

  To coś w&nbsp;rodzaju rozszerzonego VPN-a, złożonego z&nbsp;*dwóch* pośredników, z&nbsp;których każdy ma tylko część informacji. W&nbsp;każdym razie: ukrywałoby to adres IP, niwelując największą słabość trybu prywatnego.

* Podawać fałszywe, losowe dane w&nbsp;przypadku profilowania przez JavaScript.

  Zadbali przy tym o&nbsp;to, żeby wyglądały one wiarygodnie. Gdy zmieniają losowe piksele na obrazkach tworzonych przez JavaScript, to nie ruszają tych na jednolitym tle, gdzie łatwo byłoby wykryć manipulację.

Brzmi to fajnie, ale zadziała jedynie na Safari, zamkniętej przeglądarce od Apple.  
A problemem jest samo Apple. To również megakorpo, które może i&nbsp;nie poszło w&nbsp;świat reklam, ale pod względem kontroli nad użytkownikami bije na głowę Google'a.

Tak, możesz prywatnie przeglądać sieć. Ale potem twoje własne urządzenie mogłoby [skanować zapisane pliki](https://www.theverge.com/2021/8/10/22613225/apple-csam-scanning-messages-child-safety-features-privacy-controversy-explained), wysyłając centrali fałszywe alarmy (pomysł nie wszedł w&nbsp;życie, ale było blisko). I&nbsp;tego nie zmienisz, bo wiele opcji jest poza zasięgiem użytkowników.

Ale, odchodząc od spraw centralizacji i&nbsp;patrząc pragmatycznie -- istnienie trybu prywatnego od Apple oceniam na plus. Osoby, które by ubóstwiały Jabłko niezależnie od wszystkiego, będą przynajmniej mniej strzyżone przez drapieżne firmy reklamowe.  
Proponuję natomiast nie iść w&nbsp;ich objęcia tylko dlatego, że mają taki bajer.

## Jak korzystać z&nbsp;trybu prywatnego

Znając silne i&nbsp;słabe strony trybu prywatnego, można zapamiętać parę rzeczy, które pozwolą z&nbsp;niego wycisnąć nieco więcej użyteczności.

{:.post-meta .bigspace-after}
Wciąż jednak uważam, że lepszą możliwością, nawet przy stosowaniu wszystkich tych rzeczy, byłoby użycie osobnej przeglądarki, z&nbsp;aktywnym czyszczeniem plików po jej wyłączeniu. Ale jak ktoś z&nbsp;jakiegoś powodu nie może, to niech już zostanie przy trybie prywatnym.

### Nie logować się na główne konta

Niektóre osoby mogłyby pomyśleć, że użyją trybu prywatnego do sprawdzenia czegoś w&nbsp;serwisie, w&nbsp;którym już mają swoje konto. Ale w&nbsp;taki sposób, żeby platforma nie powiązała tych wyszukań z&nbsp;ich kontem.

Włączają tryb, otwierają stronę. Wita ich ekran logowania. No to się logują, wierząc że teraz „na anonimowo”. Tylko że to groźna iluzja.  
**Nie ma czegoś takiego jak anonimowe zalogowanie się na konto**. Logowanie opiera się na tym, że dostaje się *pliki cookies* -- unikalne identyfikatory, przypisane do konkretnego konta. Potem przeglądarka je okazuje stronce przy *każdej* interakcji.

Analogia? To tak, jakby specjalnie zostawić w&nbsp;domu swój firmowy identyfikator przed wyjazdem w&nbsp;Bieszczady. Po czym podjechać do firmy, wyrobić sobie nowy (nadal na swoje prawdziwe dane) i&nbsp;publicznie się z&nbsp;nim obnosić.  
Logując się na prawdziwe konto po włączeniu trybu prywatnego, tak naprawdę niweczy się cały jego sens. Jeśli prywatne logowanie, to na jednorazowe trollkonto.

### Zamaskować adres IP

To ta **najważniejsza rzecz, która pozwala zmienić tryb prywatny z&nbsp;wydmuszki w&nbsp;coś realnego**.

Z pozoru to niełatwe -- jak wspominałem, adres IP zawsze musi być prawdziwy. Ale, jeśli nie jest się pod presją czasu, jest kilka łatwych sposobów na zmianę. W&nbsp;kolejności od najłatwiejszych:

* Włączyć hotspota w&nbsp;swoim telefonie i&nbsp;się przez niego połączyć.

  Ważne: jeśli chwilę wcześniej się go używało, to adres IP może być nadal ten sam co przy sesji nieprywatnej. Lepiej chwilę odczekać, aż operator przydzieli nowy. Aktualny adres można sobie [sprawdzać](https://duckduckgo.com/?q=what+is+my+ip) na stronce DuckDuckGo, wpisując `what is my ip`.

* Użyć internetu przez jakiegoś publicznego hotspota, np. w&nbsp;kawiarni czy na dworcu.
* Użyć VPN-a lub innego pośrednika.

  Nie będę tu reklamował komercyjnych rozwiązań. Jeśli sprawa nie jest wrażliwa, a&nbsp;ew. wpadka przez rozłączenie VPN-a byłaby do przeżycia, to można użyć darmowego, wbudowanego w&nbsp;Operę. Samej Operze nie do końca ufam, ale na sporadyczne wyszukiwania jest OK.

{% include info.html
type="Uwaga"
text="Używając VPN-a, warto też tymczasowo wyłączyć w&nbsp;opcjach [WebRTC](/internetowa_inwigilacja/2023/11/05/webrtc){:.internal} (wideokonferencje). Niektóre wredne stronki mogą tego nadużywać do ujawnienia prawdziwego adresu IP zza pośrednika.  
W dwóch poprzednich przypadkach (własny lub publiczny hotspot) nie ma to znaczenia; adres IP od hotspota powinien być inny niż ten ze wcześniejszej, nieprywatnej sesji." %}

* Użyć przeglądarki Tor Browser.

  Najmocniejsze rozwiązanie w&nbsp;kwestii prywatności. Jak mocniejszy VPN, do tego w&nbsp;pakiecie pewna ochrona przed JavaScriptem. Wady? Wszystko będzie wolniejsze, bo ruch idzie przez kilku pośredników. Do tego niektóre strony się nie załadują.

  A żeby nie było, że piszę nie na temat i&nbsp;wychodzę z tym Torem poza tryb prywatny -- przeglądarka Brave ma rozwiązanie kompromisowe, opcję `Nowe okno prywatne z obsługą sieci Tor`. Nie daje ono takich gwarancji jak Tor Browser i&nbsp;też może być spowalniane/blokowane, ale nie wymaga instalowania osobnej przeglądarki.

### Nie wyrażać zgód na profilowanie

Niektórzy ze światka prywatnościowego nie cierpią rozwiązań innych niż techniczne. „Jeśli śledzenie ma techniczną możliwość zachodzić, to na pewno zachodzi”.  
Ale w&nbsp;szerszym świecie, przynajmniej w&nbsp;teorii, działa też prawo. Żyjąc w&nbsp;Europie, na mocy przepisów GDPR/RODO mamy pewne przywileje względem cyfrowych podglądaczy.

Po wejściu w&nbsp;tryb prywatny na pewno zaczną pojawiać się banery pytające o&nbsp;zgodę na gromadzenie danych. Zamiast klikać „Zgadzam się”, warto wejść w&nbsp;ustawienia (zwykle przycisk obok) i&nbsp;przejrzeć na szybko wzrokiem, czy zgody są wyłączone.  
Dla pewności **należy też wejść w&nbsp;zakładkę `Uzasadniony interes` (jeśli taka jest) i&nbsp;tam również powyłączać pstryczki**. Reklamodawcy często próbują przemycić w&nbsp;tym miejscu zgody. Ale wystarczy kilka kliknięć, żeby je wycofać.

W momencie, gdy wszystkie zgody zostaną cofnięte, dalsze profilowanie byłoby niezgodne z&nbsp;unijnym prawem. Być może niektórzy reklamodawcy mimo to zaryzykują, więc tak czy siak warto się chronić na inne sposoby... Ale zawsze to jakieś wysłanie sygnału. „Przestańcie śledzić. Widzę wasze sztuczki”. Wywieranie presji na branżę.

{% include info.html
type="Fajna inicjatywa"
text="Ekipa z&nbsp;polskiej fundacji i&nbsp;portalu *Internet. Czas działać!* stworzyła [dodatek przeglądarkowy Rentgen](https://www.internet-czas-dzialac.pl/odcinek-33-wtyczka-rentgen/), który pozwala wyłapywać przypadki stron wysyłających dane reklamodawcom jeszcze przed (nie-)wyrażeniem na to zgody. Zawiera też przyjazny interfejs do zgłaszania takich przypadków.  
Polecam osobom, które chciałyby aktywnie wziąć sprawy w&nbsp;swoje ręce i&nbsp;nieco oczyścić internet."
%}

### Użyć dodatku uBlock Origin

To popularny bloker reklam śledzących -- darmowy, dobrej jakości, o&nbsp;otwartym kodzie źródłowym. Raczej bezpieczny, bo wiele osób (w&nbsp;tym firma Mozilla od Firefoksa) czuwa nad tym, żeby nikt nie spróbował go zawirusować. [Od dawna go polecam]({% post_url 2021-10-21-ublock-origin-wiecej %}){:.internal}.

Jego działanie opiera się na blokowaniu wymiany *plików cookies* ze znanymi stronami reklamodawców.  
Nawet gdyby nas przechytrzyli, w&nbsp;ten czy inny sposób, i&nbsp;powiązali aktywność na stronce D&nbsp;(w&nbsp;trybie prywatnym) z&nbsp;tą na stronce A&nbsp;(przez główne konto)... To **i tak nie podzielą się tą informacją ze swoją stroną-matką**.

Dodatek daje zatem „dodatkowe życie”. Jest tylko jeden szkopuł... Domyślnie w&nbsp;trybie prywatnym wszystkie dodatki są wyłączone. Dlatego, żeby móc korzystać z&nbsp;uBO, trzeba wyklikać parę rzeczy w&nbsp;opcjach.

Na przykładzie Firefoksa, ale na innych będzie podobnie:

* trzeba kliknąć trzy kreski w&nbsp;górnym prawym rogu,
* potem wybrać opcję `Dodatki` (ew. `Dodatki i motywy`),
* kliknąć trzy kropki przy nazwie dodatku,
* wybrać opcję `Zarządzaj`,
* w&nbsp;zakładce `Szczegóły` zjechać na dół i&nbsp;włączyć tam opcję podpisaną „Działanie w&nbsp;oknach prywatnych”. 

<img src="/assets/posts/inwigilacja/tryb-prywatny-incognito/firefox-dodatki-tryb-prywatny.jpg" alt="Kolaż ze zrzutów ekranu, pokazujący po kolei, jakie opcje należy kliknąć, żeby uBlock Origin działał w&nbsp;trybie prywatnym"/>

### Dla chętnych: ochronić się przed JavaScriptem

To chyba najtrudniejsza rzecz, bo JavaScript jest we współczesnej sieci wszechobecny. Dlatego podsuwam to tylko jako ciekawostkę.

uBlock Origin, oprócz blokowania śledzących elementów, zawiera w&nbsp;sobie również przełącznik pozwalający łatwo włączać lub wyłączać kod JavaScript na stronach. Żeby nie wyłączać go na każdej stronie z&nbsp;osobna, można wejść w&nbsp;ustawienia dodatku i&nbsp;tam zaznaczyć, żeby domyślnie *wyłączało* JS-a. Instrukcja [tutaj]({%post_url 2021-10-21-ublock-origin-wiecej %}#różne-funkcje-ublock-origin){:.internal}.

Uprzedzam lojalnie, że wiele popularnych stron, zwłaszcza większych platform i&nbsp;portali, nie będzie działało. Ale w&nbsp;takim wypadku wystarczy jedno kliknięcie na ikonę dodatku, potem na opcję, na koniec na przycisk odświeżający stronę, żeby JS-a reaktywować.

Mając wyłączony JavaScript, można też pokusić się o&nbsp;korzystanie z&nbsp;ekranu w&nbsp;pełnych rozmiarach i&nbsp;w&nbsp;zwykłym trybie (bez specjalnych ustawień, jak kontrasty itp.). W&nbsp;ten sposób zyska się ochronę przed profilowaniem przez arkusze styli, które opisałem nieco wyżej jako ciekawostkę.

## Podsumowanie

Nazwa „tryb prywatny” faktycznie jest niefortunna. Jego mechanizm opiera się na *ulotności*, *tymczasowości*, i&nbsp;w tej kwestii daje solidne gwarancje. W&nbsp;pozostałych, bardziej prywatnościowych, już niekoniecznie.

Wystarczy jednak, żeby w&nbsp;parze z&nbsp;włączeniem trybu prywatnego poszło zamaskowanie adresu IP, a&nbsp;staje się całkiem sensowną ochroną przed prostym profilowaniem. Dodać do tego blokowanie JavaScriptu i&nbsp;już naprawdę trudno się do czegoś przyczepić.

Problem w&nbsp;tym, że mało kto zna realne ograniczenia trybu. Wiele osób może wpadać w&nbsp;pułapkę, ufnie go aktywując, po czym logując się na to konto co zwykle.

...Ale **można to zmienić, szerząc świadomość zagrożeń**. Choćby przez udostępnianie tego wpisu, a&nbsp;przynajmniej faktów na temat adresu IP czy wpływu logowania na prywatność. Do czego zachęcam! :smile:


