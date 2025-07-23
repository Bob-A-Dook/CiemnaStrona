---
layout: post
title: "„Google jest monopolistą”. Kulisy historycznego wyroku"
subtitle: "Spece od szukania nie znaleźli wyjścia z tej sytuacji."
description: "Spece od szukania nie znaleźli wyjścia z tej sytuacji."
date:   2024-08-07 10:00:00 +0100
tags: [Centralizacja, Korpożycie, Reklamy]
firmy: [Apple, Google]
category: google
category_readable: "Google – kolorowy czarny charakter"
image:
  path: /assets/posts/google/wyszukiwanie-monopol-wyrok/google-antymonopolowy-wyrok-baner.jpg
  width: 1200
  height: 700
  alt: "Przerobione zdjęcie pokazujące sędziowski młotek opadający na logo Google"
---

We [wpisie sylwestrowym]({% post_url 2023-12-31-podsumowanie-2023-roku %}){:.internal} wspomniałem, że w&nbsp;2024 roku szczególnie ciekawi mnie finał sprawy sądowej, toczącej się w&nbsp;USA przeciw korporacji Google.

Giganta oskarżono o&nbsp;działania monopolistyczne zakazane w&nbsp;świetle prawa.  
Konkretniej: o&nbsp;zakulisowe umowy i&nbsp;działania, przez które żadna inna firma, choćby miała najlepszą ofertę, nie miałaby szans zostać alternatywą.

Wczoraj sąd ogłosił swoją [decyzję w&nbsp;tej sprawie](https://www.documentcloud.org/documents/25032745-045110819896). Dokument liczy ponad 280&nbsp;stron, ale kluczowa informacja jest na początku strony ósmej:

{:.bigspace-before}
> Po dokładnym rozpatrzeniu zeznań świadków i&nbsp;przedstawionych dowodów, sąd doszedł do następującego wniosku: **Google jest monopolistą, a&nbsp;ich działania miały na celu utrzymanie monopolu**.

{:.figcaption}
Źródło: orzeczenie sędziego Amita Mehty. Tłumaczenie moje.

W tym wpisie przybliżę kilka faktów z&nbsp;rozprawy i&nbsp;wezmę na tapet różne sztuczki, z&nbsp;jakich korzystało nasze czterokolorowe megakorpo, żeby utrzymać swoją dominację.  
Zapraszam!

{:.bigspace-before}
<img src="/assets/posts/google/wyszukiwanie-monopol-wyrok/google-antymonopolowy-wyrok-baner.jpg" alt="Przerobione zdjęcie pokazujące sędziowski młotek opadający na logo Google"/>

{:.figcaption}
Źródło: [zdjęcie](https://www.pexels.com/photo/person-holding-a-gavel-6077422/) Katrin B. z&nbsp;*pexels.com*, przeróbki moje.

## Spis treści

* [Ogólne informacje](#ogólne-informacje)
  * [Fakty na temat sprawy sądowej](#fakty-na-temat-sprawy-sądowej)
  * [Przeglądarka a&nbsp;wyszukiwarka](#przeglądarka-awyszukiwarka)
* [Wątki w&nbsp;sprawie](#wątki-wsprawie)
  * [Celowe pogarszanie Chrome'a](#celowe-pogarszanie-chromea)
  * [Celowe pogarszanie wyszukiwarki](#celowe-pogarszanie-wyszukiwarki)
  * [Uniki i&nbsp;niszczenie potencjalnych dowodów](#uniki-iniszczenie-potencjalnych-dowodów)
  * [Kupienie jedynki na podium](#kupienie-jedynki-na-podium)
  * [Podsumowanie wątku](#podsumowanie-wątku)
* [Co dalej?](#co-dalej)
* [Źródła](#źródła)

## Ogólne informacje

### Fakty na temat sprawy sądowej

Google ma na sumieniu wiele grzeszków i&nbsp;co rusz toczy się jakiś prawny spór z&nbsp;ich udziałem. Na różnych poziomach: regionalnym, krajowym, międzystanowym, unijnym...

Łatwo się w tym wszystkim pogubić. Dlatego najpierw pozwolę sobie jasno doprecyzować, o&nbsp;co tu chodziło.

Oficjalna nazwa sprawy? [**_United States vs Google LLC_**](https://www.justice.gov/atr/case/us-and-plaintiff-states-v-google-llc).

{:.post-meta .bigspace-after}
Z tego co rozumiem: w&nbsp;USA nazywają sprawy sądowe od stron sporu. A&nbsp;że stroną pozywającą był Departament Sprawiedliwości, instytucja państwowa, to jedną ze stron zwyczajowo nazwano *United States*.

Ramy czasowe? Początki oficjalnej sprawy sięgają aż 2020&nbsp;roku. Najwięcej wydarzyło się zeszłej jesieni, bo na przestrzeni nieco ponad dwóch miesięcy trwało przesłuchiwanie świadków. Potem sąd dał sobie czas do namysłu. Teraz werdykt, a&nbsp;na szczegóły kary trzeba jeszcze poczekać.

*Teoretyczny* zakres terytorialny? Całe USA. Google zostało pozwane przez Departament Sprawiedliwości, czyli na poziomie federalnym, ponad pojedynczymi stanami. Za sprawę odpowiadał sąd Dystryktu Kolumbii w&nbsp;Waszyngtonie.

Piszę o zakresie „teoretycznym”, bo USA jest krajem-siedzibą Google'a. Zatem wszelkie zmiany, do jakich zostaną zmuszeni, raczej nie ograniczą się do filii amerykańskiej. Dla Google'a najsensowniejszym rozwiązaniem będzie zapewne zmiana globalna, dotycząca działalności na całym świecie.

Kolejna sprawa to *zakres tematyczny*. **Sprawa z&nbsp;założenia dotyczyła wyszukiwarki**.

Może to nieco zaskakiwać, bo wśród dokumentów sądowych (które jeszcze podlinkuję) przewijają się też wzmianki o&nbsp;reklamach, Chromie, Androidzie... Cały kalejdoskop produktów i&nbsp;firm, także zewnętrznych.  
Ta mnogość wątków wynika z&nbsp;faktu, że wyszukiwarka jest w&nbsp;centrum wszystkiego, ściśle zrośnięta z&nbsp;innymi aspektami Google'a. To wokół niej budowali swój biznes.

{% include info.html
type="Uwaga"
text="Tę sprawę można łatwo pomylić z&nbsp;[inną, nadal trwającą](https://en.wikipedia.org/wiki/United_States_v._Google_LLC_(2023)). Również dotyczącą monopolizacji i&nbsp;również nazwaną _US vs Google LLC_ (strony sporu te same). Dotyczy ona **giełd reklamowych**, czyli innego zyskownego aspektu działalności Google'a. Rozpoczęła się w&nbsp;zeszłym (2023) roku.  
Równolegle toczy się *jeszcze inna sprawa*, [wspomniana przelotnie](/google/2021/10/30/google-skandale-wprowadzenie){:.internal} na tym blogu kilka lat temu. Jej słowa-klucze to *Jedi Blue*, czyli zmowa Google'a z&nbsp;Metą/Facebookiem, oraz *Project NERA* od śledzących funkcji Chrome'a. To z&nbsp;kolei [*Texas vs Google LLC*](https://www.kellerpostman.com/cases/state-of-texas-v-google-litigation/), rozpoczęta w&nbsp;Teksasie w&nbsp;2020&nbsp;roku przez grupę prokuratorów generalnych.  
Google nabroił na tylu frontach, że powoli ciężko to katalogować :wink:"
%}

### Przeglądarka a&nbsp;wyszukiwarka

Do zrozumienia całej sprawy przyda się też ważny fakt techniczny. **Przeglądarka to program (aplikacja). Wyszukiwarka to zewnętrzny serwis. Są od siebie niezależne**.

Zwykle można dowolnie je ze sobą mieszać. Przeglądarka Chrome, wyszukiwarka Ecosia? Proszę bardzo! przeglądarka Opera i&nbsp;wyszukiwarka DuckDuckGo? Vivaldi i&nbsp;Bing? Edge i&nbsp;Google? Do wyboru, do koloru.

I nie mam tutaj na myśli jedynie rzeczy oczywistej: że można wyświetlić w&nbsp;przeglądarce *stronę internetową* dowolnej wyszukiwarki (czyli np. `bing.com`) i&nbsp;coś tam wpisać.  
Mówię o&nbsp;ściślejszej integracji. Wejściu w&nbsp;ustawienia przeglądarki i&nbsp;*zmianie domyślnej wyszukiwarki*. Sprawi to, że wszelkie rzeczy wpisane w&nbsp;górny pasek -- o&nbsp;ile nie są linkami -- będą wyszukiwane właśnie w&nbsp;tej ręcznie ustawionej.

Dla niektórych ta rozdzielność to coś oczywistego, wzruszą ramionami. „Słońce wstaje u&nbsp;nas na wschodzie”.

...Problem w&nbsp;tym, że dla wielu codziennych użytkowników granica bywa niewidoczna, a&nbsp;przynajmniej rozmyta. **Ustawienia domyślne mają kolosalne znaczenie**. A&nbsp;kiedy Google wita użytkowników zaraz od progu, to można ulec iluzji, że nie jest jedynie faworyzowanym gościem, lecz integralną częścią przeglądarki. Albo nawet całego systemu.

Przykład? Przeglądarka Opera, po pierwszym uruchomieniu. Albo otwarciu nowej, pustej karty:

{:.figure .bigspace}
<img src="/assets/posts/google/wyszukiwanie-monopol-wyrok/google-ekran-powitalny-opery.jpg" alt="Górna część ekranu przeglądarki Opera. W&nbsp;górnym pasku nie ma żadnego adresu. Pośrodku widać pole z&nbsp;logo Google, podpisane 'wyszukaj w&nbsp;internecie'."/>

Inny przykład? Ekran główny wielu smartfonów, za wyjątkiem może Huaweiów (bo są w&nbsp;niełasce Google'a przez sankcje). Pierwszą rzeczą witającą użytkowników jest pasek wyszukiwania, ozdobiony oczywiście literką G. We [wpisie na temat *odgooglowania* telefonu]({% post_url 2024-02-03-smartfon-degoogle %}){:.internal} pokazałem, jak go usunąć:

{:.bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle/google-usuwanie-widzeta.jpg" alt="Zrzut ekranu głównego smartfona. Strzałka pokazuje, żeby przesunąć duży pasek wyszukiwania ku ikonce podpisanej 'Usuń'"/>

{:.figcaption}
Przypominajka: trzeba przytrzymać palcem i&nbsp;przeciągnąć na ikonę usuwania.

W każdym razie fakt do zapamiętania: Google jest wszędzie. Ale nie musi tak być. Za jego (wszech-)obecnością nie stoi żadna techniczna konieczność.  
Stoją za tym natomiast pieniążki. Co niebawem pokażę. 

Okej, podwaliny pod wpis położone. Teraz przejdę do wypunktowania różnych rzeczy, jakie pojawiły się wokół całej sprawy.

## Wątki w&nbsp;sprawie

### Dominacja wbrew degradacji

Google jest wielkim graczem, zwłaszcza w&nbsp;segmencie wyszukiwarek. Jak wskazuje strona 18&nbsp;decyzji sądu, w&nbsp;2020 roku zgarniali **prawie 95% wyszukań na urządzeniach mobilnych i&nbsp;84% na innych urządzeniach**.

Ale sam udział w&nbsp;rynku nie przesądza o&nbsp;tym, że coś może zostać uznane za monopol. W&nbsp;końcu ten dawny Google, z&nbsp;początków obecnego tysiąclecia, też miał miażdżącą przewagę. Ale zawdzięczał ją nowatorskiemu na tamte czasy algorytmowi *PageRank*. Po prostu nie miał sobie równych.

W Stanach Zjednoczonych oskarżenie o&nbsp;monopolizację nie jest jakimś „batem na zaradnych przedsiębiorców”. Ma ona swoją definicję, określoną w&nbsp;[Ustawie Shermana](https://pl.wikipedia.org/wiki/Ustawa_Shermana).

Mówiąc krótko: podmiot może sobie dominować. Ale musi robić swoje, tworzyć produkty. **Nie może celowo blokować konkurencji okrężnymi metodami, takimi jak zmowy z&nbsp;innymi gigantami**, układy i&nbsp;układziki, doprowadzanie do „skostnienia” rynku.

Brzmi całkiem rozsądnie? Powiedziałbym wręcz, że wolnorynkowcy mogliby docenić dbanie o&nbsp;zdrową konkurencję, miejsce dla alternatyw, dynamiczny ekosystem.  
Podejście do monopoli bywa tym, co odróżnia ludzi merytorycznych od zwykłych darwinistów, podziwiających bezwględność i&nbsp;władzę. Taka moja refleksja.

A co do samej jakości... Ta już od pewnego czasu [budzi wątpliwości użytkowników](https://www.reddit.com/r/TooAfraidToAsk/comments/q8zlg6/is_it_just_me_or_has_google_web_search_result/), zaś u&nbsp;szczytu wyników wyszukiwania coraz częściej pojawiają się [powtarzalne strony](https://www.reddit.com/r/CasualConversation/comments/10flscb/is_it_just_me_or_is_google_getting_worse_over_the/). Albo chłam i&nbsp;spam.  
Spadek trwa od jakiegoś czasu, zachodził jeszcze przed upowszechnieniem się LLM-ów (nowoczesnych generatorów tekstu). Te jedynie przyspieszyły cały proces.

Kolejna sprawa: konkurencja. Różne firmy próbowały tworzyć wyszukiwarki. Czasem znalazły swoje małe nisze, ale nie zawojowały świata.  
Pomijam już alternatywy od drobniejszych graczy, jak DuckDuckGo czy Kagi. Ale nawet ogromny Microsoft nie mógł dotrzeć do ludzi ze swoim Bingiem.

Jakość spada, udział rośnie, konkurencja stoi w&nbsp;martwym punkcie. Na tym tle pojawiły się wątpliwości, czy Google aby nie zawdzięcza swojej pozycji rzeczom niezależnym od jakości. Dlatego rozpoczęto proces sądowy. I&nbsp;przy okazji otwarto puszkę Pandory. 

### Celowe pogarszanie Chrome'a

Tę sprawę miałem już okazję [dokładniej wyjaśnić na blogu]({% post_url 2023-10-05-antymonopol-chrome-reklamy %}){:.internal}, tutaj tylko ją streszczę.

Ogólnie rzecz biorąc: wyszło na jaw, że ludzie z&nbsp;działu reklam naciskali na ekipę od przeglądarki Chrome, żeby podbili im statystyki odwiedzin na `google.com`, co przełożyłoby się na więcej wyświetleń reklam.  
Pomysły na poprawienie liczb wymagały celowego pogorszenia komfortu korzystania z&nbsp;Chrome'a. Były wśród nich na przykład:

* zmiana kolejności podpowiedzi w&nbsp;górnym pasku -- nawet jeśli strona została wcześniej odwiedzona, wyżej miał trafić wynik wyszukiwania z&nbsp;Google'a;
* usunięcie z&nbsp;górnego paska krótkich, szybkich odpowiedzi; choć były ułatwiaczem życia, nie wiązały się z odwiedzinami na stronie;
* zmiana interfejsu mobilnego, żeby przepchnąć pasek wyszukiwania wyżej, kosztem bezpośrednich linków do stron.

Ta pierwsza propozycja istotnie weszła w&nbsp;życie, prowadząc do wyrazów niezadowolenia na forach publicznych. Ale ludzie zapewne zakładali potknięcie albo nieprzemyślane działanie, nie wiedząc o&nbsp;zakulisowych machinacjach.

### Celowe pogarszanie wyszukiwarki

Ten wątek jest przystępnie opisany na stronie Edwarda Zitrona, w&nbsp;artykule *[The Man Who Killed Google Search](https://www.wheresyoured.at/the-men-who-killed-google/)*. Google wysłał w&nbsp;odpowiedzi swoją polemikę, do której autor się [odniósł](https://www.wheresyoured.at/in-response-to-google/).

Źródłem pierwotnym jest natomiast [wątek mailowy](https://www.justice.gov/d9/2023-11/417581.pdf) ujawniony podczas rozprawy (maile ułożone od najnowszego do najstarszego).

Chodzi o&nbsp;bardzo podobną sprawę jak ta wyżej opisana. Dział reklam i&nbsp;dział finansów naciskały w&nbsp;2019&nbsp;roku na lepsze wyniki. Tym razem oczekiwały ich od ludzi odpowiedzialnych za wyszukiwarkę, czyli m.in. stronę `google.com` i&nbsp;jej kulisy. 

Cała historia jest przedstawiona w&nbsp;artykule jako zderzenie dwóch światów -- rzemieślników-perfekcjonistów oraz maksymalizatorów zysku. Można zauważyć, jak ci drudzy coraz bardziej się rozpychają i&nbsp;zyskują wpływy, a&nbsp;pierwsi popadają w&nbsp;gorycz.

Pojawia się presja na to, żeby zwiększyć przychody z&nbsp;reklam. Co dział od wyszukiwarki mógłby zmienić? Jeden z&nbsp;jego pracowników w&nbsp;mailu do innych wymienia opcje:

* wyłączenia autokorekty pisowni  
  (zapewne po to, żeby użytkownicy musieli wpisać ponownie poprawione hasło, nabijając dwa wyszukania);
* wyłączenia wspomaganego szukania  
  (zapewne po to, żeby wymusić więcej zapytań, nim pojawi się szukana rzecz).

...Ale jednocześnie dystansuje się od tych rozwiązań. Pisze, że rzeczy w&nbsp;tym stylu negatywnie by się odbiły na produkcie. I&nbsp;że przyjmowanie suchej liczby wyszukań za miernik jakości raczej nie skończy się dobrze.

Jego ostrożność raczej nie wygrała. Bowiem po aktualizacji Google'a firmy zajmujące się pozycjonowaniem stron zauważyły, że ludzie częściej odwiedzają strony w&nbsp;stylu spamowym, wcześniej spychane niżej w&nbsp;rankingu. Hipoteza autora: **Google mógł celowo obniżyć jakość, żeby poprawić liczbę kliknięć**.

Parę miesięcy później zmienili oznaczenia reklam na mniej rzucające się w oczy, bardziej zlane z&nbsp;tłem. Skutek? Zapewne więcej (nieświadomych) kliknięć.

Wątek zmian na gorsze dobrze podsumowuje wypowiedź rzemieślnika od wyszukiwarki:

> Myślę, że nasze skupianie się na reklamach zaczyna być niekorzystne dla produktu i&nbsp;dla firmy. (...) Jestem otwarty na argumenty, ale zaczyna mnie martwić, że myślimy wyłącznie o&nbsp;wzroście.

### Uniki i&nbsp;niszczenie potencjalnych dowodów

Już na samym początku okresu składania zeznań, jesienią zeszłego roku, Google zaczął robić problemy. Jego prawnicy naciskali na to, żeby utajnić całą rozprawę. Powoływali się na tajemnice firmy. Ostatecznie nie ugrali wiele poza zakrywaniem niektórych nazw i&nbsp;danych liczbowych w&nbsp;dokumentach publikowanych na stronie Departamentu Sprawiedliwości.

Ponadto dowody pokazały, że Google miało świadomość, że mogą zostać oskarżeni o&nbsp;monopolizację, i&nbsp;[opracowali cały labirynt dupochronów](https://arstechnica.com/tech-policy/2023/09/google-hid-evidence-by-training-workers-to-avoid-words-monopolists-use-doj-says/). 

Po pierwsze: szkolili kadry kierownicze, żeby unikały słów mogących się kojarzyć z&nbsp;zyskiwaniem monopolu, takich jak: „efekty sieciowe”, „uzależnianie”, „odcięcie \[konkurencji\] dopływu tlenu” itp.

Jeszcze gorszą zagrywką było **usuwanie przez Google'a historii czatów**. Mieli wewnętrzne wytyczne o&nbsp;nazwie *Communicate with Care* („komunikuj się ostrożnie”), mówiące żeby wymieniać wrażliwsze informacje na czatach, gdzie historia konwersacji jest automatycznie usuwana w&nbsp;ciągu 24&nbsp;godzin.

Choć już w&nbsp;2019 roku dostali sądowy nakaz przechowywania wewnętrznych wiadomości (na potrzeby nadchodzącego procesu), nie wyłączyli automatycznego czyszczenia historii. Zdaniem sądu: zablokowali w&nbsp;ten sposób dostęp do dowodów, w&nbsp;których mogło być więcej pikantnych faktów.

Co więcej, parę maili znalezionych poza usuwalnymi czatami pokazało, jak sam prezes, Sundar Pichai, w&nbsp;pewnym momencie w&nbsp;2021 roku prosi o&nbsp;przejście z&nbsp;tradycyjnych maili na „tryb bez historii”. Widać, że aktywnie z&nbsp;tej funkcji korzystali.

Sąd rozważał w&nbsp;związku z&nbsp;tymi unikami [nałożenie na Google'a dodatkowych kar](https://fingfx.thomsonreuters.com/gfx/legaldocs/jnpwyayqqpw/US%20v%20Google%20-%20Sanctions%20-%202023-02-23.pdf). Ostatecznie nie skorzystał z&nbsp;tej możliwości; sędzia uzasadnia, że i&nbsp;tak nic by to nie zmieniło w&nbsp;sprawie, reszta dowodów była wystarczająco silna. Ale do końca im tego nie zapomniał. 

> Decyzji sądu \[o nienałożeniu kary\] nie należy traktować jak wyrazu akceptacji dla niezapisywania dowodów (...) Tym razem firma Google uniknęła kary. Następnym razem może nie mieć tyle szczęścia.

{:.figcaption}
Źródło: decyzja sądu, strony 279-280. Skróty i&nbsp;tłumaczenie moje.

### Kupienie jedynki na podium

Jak pisałem wyżej, ustawienia domyślne mają ogromne znaczenie. Wprost to również pisze sędzia w&nbsp;uzasadnieniu wyroku.

O ile domyślne opcje nie są całkiem skaszanione, większość ich nie zmieni.  
Nawet gdyby było to kwestią paru kliknięć. „Może kiedyś”. „Aa, jeszcze coś popsuję”. „Mam ważniejsze rzeczy na głowie”. Różne motywacje, ale skutkiem ta sama bezczynność.

I Google doskonale o&nbsp;tym wie. Dlatego za wszelką cenę walczył o&nbsp;to, żeby być numerem jeden. **Płacił twórcom przeglądarek i&nbsp;systemów mobilnych za ustawienie jego wyszukiwarki jako domyślnej**. W&nbsp;samym 2021&nbsp;roku wydał na to łącznie ponad 26&nbsp;miliardów dolarów.

Płacił dużym i&nbsp;małym. Przykładowo: firmie Mozilla od Firefoksa. Wiele osób go kojarzy. Praktyczna, sprawna, znacznie prywatniejsza alternatywa dla Chrome'a. Jest ponadto oparty na niezależnym silniku, co mogą docenić fani decentralizacji.

...Ale czy wiedzieliście, że pod techniczną niezależnością kryje się finansowe uwiązanie? [Mozilla dostaje od Google setki milionów rocznie](https://www.telepolis.pl/tech/taryfy-promocje-uslugi/mozilla-bedzie-przez-kolejne-lata-zarabiac-dzieki-google). Za to, że utrzymują *google.com* jako domyślną wyszukiwarkę na Firefoksach.

Inny przykład? Umowy zawarte przez Google'a z&nbsp;producentami smartfonów. To stąd ten wielki pasek wyszukiwania na środku ekranu. Google płaci, to dostaje.

Wśród umów o&nbsp;pierwsze miejsce szczególną rolę odgrywał natomiast jeszcze inny układzik. Nie z&nbsp;Mozillą ani Samsungiem. [Tylko z&nbsp;Apple](https://www.theverge.com/2023/10/26/23933206/google-apple-search-deal-safari-18-billion).  
Dlaczego? Bo, w&nbsp;przeciwieństwie do przykładowego Samsunga (inna branża) czy Firefoksa (zbyt mała skala), Apple mogło zrobić coś groźniejszego niż tylko przykładowe faworyzowanie Binga zamiast Google. 

Mogli *wejść w&nbsp;segment wyszukiwarek*, próbować być konkurencją dla Google'a. Mieli i&nbsp;środki, i&nbsp;motywację, żeby rozważyć stworzenie czegoś własnego.  
Co więcej, już wcześniej olali Google Maps i&nbsp;rozwinęli zamiast tego swoje [Apple Maps](https://pl.wikipedia.org/wiki/Apple_Maps) (na bazie świetnej, otwartoźródłowej OpenStreetMap). Pokazali tym samym, że są otwarci na możliwość konkurowania.

Google'a zapewne martwiła perspektywa rozpoznawalnej konkurencji. Dlatego wobec jabłkowych szczególnie otworzył kieszeń. **W 2021&nbsp;roku dali Apple ok. 18&nbsp;miliardów**. Zapewne co roku kwota była podobna.  
Oficjalnie płacili za bycie domyślną wyszukiwarką... Ale były za tym niewypowiedziane słowa. Zniechęcenie Apple do stworzenia alternatywy. Zasianie wątpliwości.

„Prace rozwojowe to zawsze ryzyko. To lata pracy, może się nie opłacić... A&nbsp;po stworzeniu wyszukiwarki dalibyśmy ją na pierwszym miejscu, tracąc 20&nbsp;miliardów od Google'a. Może lepsze te pewne 20&nbsp;miliardów”. Tak mogło rozumować kierownictwo Apple.

A zatem alternatywa nie powstała. Ani od Apple, ani od innych. Nie było nikogo, kto miałby jednocześnie środki, chęci i&nbsp;układy, żeby zdetronizować giganta.

Wątek Apple mógł mieć istotny wpływ na decyzję sądu. Oto na horyzoncie majaczyła szansa na alternatywę, lekkie zawirowanie na rynku przeglądarek. Ale zdechła przez układziki.  
Podręcznikowy przykład zakulisowej zmowy? Pan Sherman od ustawy antymonopolowej mógłby skinąć kapeluszem zza grobu.

### Podsumowanie wątku

Zgromadzone fakty pokazały sądowi prawdziwe oblicze Google'a. Firma zirytowała go próbą utajnienia rozpraw, usuwaniem dowodów. Uwidoczniły się zmowy i&nbsp;próby robienia z&nbsp;cyfrowego świata swojego folwarku.  
Konwersacje mailowe pokazały, jak bardziej etyczni pracownicy ustępowali pod naporem działu reklamowego, czyli maszynek do tworzenia kasy.

No i&nbsp;sąd podjął decyzję. Google oficjalnie dołączył do grona nielegalnych monopolistów. Co jest pewnym wyczynem w&nbsp;USA, największym korporaju.

Całej sprawie dodaje smaczku fakt, że w&nbsp;początkach swojego istnienia Google jako oficjalne hasło, obecne również w regulaminie, przyjął *"Don't be evil"*. „Nie czyń zła”.

Choć słowo *evil* pasuje do wielu organizacji, wówczas w&nbsp;światku komputerowym takim „domyślnym” złem był Microsoft. Synonim chciwego, zaborczego megakorpo. W&nbsp;2001 roku został [oficjalnie ukarany za monopolizację](https://wyborcza.biz/biznes/7,177151,4484142.html) wyrokiem sądu.

Hasło Google'a było zatem subtelną aluzją, szpilką wbitą MS-owi. „Nie będziemy tacy jak oni”.

A teraz, po ponad 20&nbsp;latach... Nie dość, że Google w&nbsp;kilku miejscach usunął szlachetne hasło, zostawiając je tylko pod koniec dokumentu, to jeszcze sam został oskarżony o&nbsp;to samo. Jakie to życie bywa przewrotne :wink:

## Co dalej?

Choć decyzja sądu jest znana i&nbsp;jest już pewne, że Google poniesie karę za swoje zapędy i&nbsp;gierki... Dokładny wymiar tej kary jeszcze nie został określony i&nbsp;[trzeba chwilę poczekać na jej wyznaczenie](https://sherwood.news/power/antitrust-expert-heres-whats-going-to-happen-to-google-next/).

Kara finansowa, niezależnie od wielkości, byłaby dla korporacji jedynie drobnym utrapieniem. Możliwe jednak, że zajdą dalej idące zmiany, a&nbsp;Google straci możliwość zawierania swoich zakulisowych umów na wyłączność. W&nbsp;jeszcze ostrzejszym wariancie kary -- choć według artykułu mało prawdopodobnym -- mogą zostać rozbici na niezależne firmy.

Byłby to koniec koordynacji między reklamami a&nbsp;innymi działami. Ludzie od Chrome'a nie musieliby już słuchać nacisków każących im robić wszystko pod reklamy.

Niektórzy wskazują możliwe efekty uboczne wariantu z&nbsp;zakazem umów. Gdyby przykładowo Google musiał przestać płacić Mozilli za pierwsze miejsce, to nie wiadomo, czy Firefox przetrwa bez kroplówki finansowej.

...Tylko czy takie obawy nie mają w&nbsp;sobie odrobiny wygodnictwa, obrony patologicznych relacji? „Może i&nbsp;znęca się nad rodziną, ale przynajmniej zapewnia im chleb. Może nie zabije? Może jego brak byłby gorszy? Po co siać ferment”.

Korporacje w&nbsp;kampaniach PR-owych uwielbiają się zasłaniać słabszymi:

* Meta od Facebooka robiła kampanię mówiącą, że bez ich reklam poupadają małe europejskie firmy.
* Syngenta w&nbsp;USA [zasłaniała się]({% post_url 2022-07-27-syngenta-atrazyna %}#walka-zsyngentą){:.internal} dobrem rolników, mówiąc że bez ich środka chemicznego rolnictwo padnie (choć w&nbsp;Europie, gdzie był zakazany, jakoś żyło).
* [Bayer twierdził]({% post_url 2022-12-24-biotechnologia-trolle-youtube %}#gmo-sposobem-na-kryzys){:.internal}, że nie może się wycofać z&nbsp;Rosji, bo będzie klęska głodu. [Podobnie Cargill]({% post_url 2024-02-21-protest-rolnikow-cargill-dreyfus-viterra %}#cargill){:.internal}. Ten drugi dodawał też, że produkuje tam mieszanki dla niemowląt. „Przecież nie zagłodzicie dzieci”.
* Mnóstwo megafirm alarmuje, że w&nbsp;razie dokręcenia śruby będą musiały -- ale tak niechętnie, z&nbsp;ciężkim sercem! -- zwolnić pracowników.  
  A&nbsp;potem ich zwalniają tak czy siak, lekko i&nbsp;zdalnie. Nawet gdy ograniczeń nie nałożono, ale za to wynik finansowy się nie spiął.

Do tego Google nadal próbuje utrzymać pokerową twarz. Wywijają się, licząc na skuteczną apelację, a&nbsp;jednocześnie dość cynicznie przekręcają sens wyroku.

{:.bigspace-before}
> Sąd uznaje fakt, że Google oferuje najlepszą wyszukiwarkę, ale wnioskuje o&nbsp;to, żeby nie pozwolić nam na jej łatwe udostępnianie

{:.figcaption}
Źródło: wypowiedź rzecznika firmy, cytowana w&nbsp;popularnych artykułach. Tłumaczenie moje.

Dlatego, jak dla mnie, są niereformowalni. Nie ma co się wahać, można iść na całość z&nbsp;dzieleniem na mniejsze. Ciach i&nbsp;już!

{:.bigspace-before}
<img src="/assets/posts/google/wyszukiwanie-monopol-wyrok/split-google-talk-to-me.jpg" alt="Trzy kadry z&nbsp;filmu Talk to Me z&nbsp;dodanymi napisami. Na pierwszym widać zbliżenie na twarz ciemnoskórej dziewczyny mówiącej 'stoi tuż za tobą'. Na drugim widać chłopaka z&nbsp;logo Google nałożonym na twarz, a&nbsp;za nim logo Departamentu Sprawiedliwości USA. Na trzecim znów dziewczyna, mówi: `rozpłata cię, piękny chłopcze'."/>

{:.figcaption}
Źródło: [scena](https://www.youtube.com/watch?v=dmiwudN-Jso) z&nbsp;horroru *Talk to Me* (uwaga: YouTube). Przeróbki moje.

## Źródła

Mój wpis siłą rzeczy pokazuje subiektywną perspektywę. Tylko te fakty, które najbardziej mnie zaciekawily. Osoby zainteresowane mogę natomiast nakierować na całą skarbnicę informacji.

Po pierwsze: wspomniana już nieraz [decyzja sądu](https://www.documentcloud.org/documents/25032745-045110819896). Zawiera kontekst, uzasadnienie, streszczenie faktów. Język, poza kilkoma miejscami, jest zadziwiająco przystępny.

Cenne są również wszelkie dokumenty sądowe związane z&nbsp;rozprawą. Jak chociażby [oficjalne dowody](https://www.justice.gov/atr/us-and-plaintiff-states-v-google-llc-2020-trial-exhibits), zebrane na stronie Departamentu Sprawiedliwości.  
Są tam fragmenty mailowej korespondencji, wewnętrzne prezentacje, zarysy strategii... Ogólnie źródła wszelkich informacji, od Google'a i&nbsp;nie tylko, które mogłyby potwierdzać istnienie monopolu wyszukiwarkowego.

Same dokumenty zawierają jednak sporo wewnętrznego żargonu i&nbsp;nie zawsze łatwo je umieścić w&nbsp;odpowiednim kontekście. Dlatego bardzo przydają się również przystępniejsze omówienia.

Cenną kroniką batalii sądowej jest stronka [*Big Tech on Trial*](https://www.bigtechontrial.com/). Założona przez Matta Stollera -- dziennikarza zawodowo śledzącego różne zmowy, kartele i&nbsp;monopole w&nbsp;USA.

Jeśli chodzi o&nbsp;relacje w&nbsp;popularnych mediach, to listę artykułów po angielsku, ułożonych w&nbsp;kolejności chronologicznej, można znaleźć na stronie [portalu *Verge*](https://www.theverge.com/23869483/us-v-google-search-antitrust-case-updates).

Zapewne są też przystępne polskie źródła, ale nie miałem okazji z&nbsp;nich korzystać. Zawsze można wyłuskiwać co ciekawsze fakty ze stron angielskich i&nbsp;próbować wyszukać po polsku.

To tyle na dziś! Do kolejnych wpisów :smile:



