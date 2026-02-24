---
layout: post
title: "Podsumowanie 2025 roku"
subtitle: "Rok Linuksa, pracy u podstaw i ludzkiego oporu."
description: "Rok Linuksa, pracy u podstaw i ludzkiego oporu."
tags: [AI, Manipulacja, Open Source, Rolnictwo]
firmy: [Monsanto, Proctorio, OpenAI]
date:   2025-12-31 17:13:10 +0100
image:
  path: /assets/posts/podsumowania/2025/linux-podsumowanie-2025-baner.jpg
  width: 1200
  height: 700
  alt: "Przerobiony obrazek, na którym Mikołaj pokazuje cieszącej się dziewczynce worek prezentów. Z worka wyłania się maskotka systemu Linux oraz loga różnych jego wersji. Na Mikołaja nałożono numer roku 2025, a na dziewczynkę 2026."
---

Witajcie! Kolejny rok zbliża się ku końcowi, więc czas na tradycyjne podsumowanie wydarzeń z&nbsp;bloga i&nbsp;ze świata!

Jeśli chodzi o&nbsp;świat, będzie dziś względnie optymistycznie -- zebrało się bowiem parę małych triumfów ludzi nad korporacjami, zaś w&nbsp;społeczeństwie widać większą niż kiedyś niechęć do branżowych narracji.

Możliwe jednak, że wygrane bitwy to dopiero rozgrzewka, a&nbsp;przyszły rok przyniesie większe walki. Związane chociażby z&nbsp;patologiami wokół „sztucznej inteligencji”, o&nbsp;których tu wspomnę.

Jeśli chodzi o&nbsp;bloga, to można uznać, że trwał na nim **rok systemu Linux** (czy raczej: różnych systemów na bazie Linuksa).  
Miałem okazję zagłębić się w testowanie różnych odmian tej alternatywy dla Windowsa. Nabić parę poziomów doświadczenia w&nbsp;jego obsłudze i&nbsp;podzielić się wiedzą w&nbsp;różnych poradnikach.

Zapraszam na przegląd zdarzeń z&nbsp;bloga i&nbsp;ze świata!

{:.bigspace-before}
<img src="/assets/posts/podsumowania/2025/linux-podsumowanie-2025-baner.jpg" alt="Przerobiony obrazek, na którym Mikołaj pokazuje cieszącej się dziewczynce worek prezentów. Z&nbsp;worka wyłania się maskotka systemu Linux oraz loga różnych jego wersji. Na Mikołaja nałożono numer roku 2025, a&nbsp;na dziewczynkę 2026."/>

{:.figcaption}
Źródło: [zdjęcie z&nbsp;serwisu Freepik](https://www.freepik.com/free-photo/she-is-so-excited-new-christmas-present_12375656.htm), maskotka Linuksa (pingwin Tux), loga różnych systemów na jego bazie. Przeróbki moje.

## Spis treści

* [Wieści z&nbsp;bloga](#wieści-zbloga)
  * [Rok pracy u podstaw](#rok-pracy-upodstaw)
  * [Rok Linuksa? U&nbsp;mnie na pewno!](#rok-linuksa-umnie-na-pewno)
* [Wieści ze świata](#wieści-ze-świata)
  * [Odtajnione dokumenty na temat *???????*{:.cover}](#odtajnione-dokumenty-na-temat-)
  * [AI i&nbsp;współczesna gorączka złota](#ai-iwspółczesna-gorączka-złota)
  * [Proctorio i&nbsp;koniec prześladowania badacza](#proctorio-ikoniec-prześladowania-badacza)
  * [Obrywające korporacje rolno-spożywcze](#obrywające-korporacje-rolno-spożywcze)
* [2026&nbsp;rokiem promowania federalizacji?](#2026rokiem-promowania-federalizacji)
* [Plany na przyszły rok](#plany-na-przyszły-rok)

## Wieści z&nbsp;bloga

### Rok pracy u&nbsp;podstaw

Gdyby oceniać ten rok pod kątem liczby wpisów na stronie głównej, to wypadłby najgorzej od początku istnienia bloga. Między sierpniem a&nbsp;listopadem pojawił się tylko jeden nowy wpis!

Panel aktywności Githuba (na którym trzymam kod źródłowy bloga) pokazuje jednak, że działo się całkiem niemało -- i&nbsp;to dokładnie w&nbsp;tym pozornie martwym okresie:

{:.figure .bigspace}
<img src="/assets/posts/podsumowania/2025/github-aktualizacje-2025.png" alt="Zrzut ekranu z&nbsp;panelu aktywności Githuba"/>

To dlatego, że na pewien czas odłożyłem na bok dłuższe eseje i&nbsp;wziąłem się za tworzenie krótszych poradników oraz minirelacji ze swoich zmagań z&nbsp;cyfrowym światem. Stworzyłem, jeśli dobrze liczę, **13 nowych samouczków i&nbsp;5 minirelacji**.

Były to głównie rzeczy związane z&nbsp;obsługą wspomnianego już darmowego i&nbsp;otwartego systemu **Linux Mint**.

Poza tym nieco doszlifowałem i&nbsp;dopracowałem dawne poradniki. Żeby nie zanudzać, upchnąłem ich przegląd w&nbsp;rozwijanej zakładce, dla zainteresowanych.

{% include details.html summary="Dokładniejsze omówienie zmian" %}

* Dodałem [widok galerii wpisów](/galeria){:.internal}, na razie eksperymentalny.

  To ta sama lista wpisów co na stronie głównej, tylko że z&nbsp;obrazkami („banerami”) -- jak ten z&nbsp;Mikołajem w&nbsp;przypadku obecnego wpisu.  
  Być może taka forma bardziej się spodoba osobom przyzwyczajonym do interfejsów z&nbsp;miniaturkami, jak ten na YouTubie. Co kto lubi!

  {:.post-meta .bigspace-after}
  Przy okazji odkryłem stary błąd: jedna z&nbsp;miniatur mi nie działała przez błąd w&nbsp;ścieżce. Mam też świadomość, że parę najstarszych wpisów jeszcze nie ma swoich miniaturek. Ale to się zmieni :wink:

* Zmodernizowałem nieco [samouczek](/tutorials/youtube-dl){:.internal} dotyczący programu `yt-dlp` (od łatwego pobierania filmów i&nbsp;muzyki z&nbsp;różnych serwisów).

  Poprzednia wersja nieco mąciła, wspominając o&nbsp;starszej wersji programu. Z&nbsp;racji tego, że stopniowo odchodzi ona w&nbsp;niepamięć, zepchnąłem ją do osobnej zakładki. Doprecyzowałem też parę innych rzeczy.

* Zmodernizowałem samouczki dotyczące Pythona.

  Skupiłem się zwłaszcza na obchodzeniu [irytującego komunikatu o&nbsp;środowisku zarządzanym zewnętrznie](/tutorials/python-blad-externally-managed-environment){:.internal}.  
  Wynika on z&nbsp;tego, że popularne Linuksy postanowiły ściśle oddzielić Pythona systemowego od „roboczego”. Nie działa przez to prosta, powszechna komenda od instalowania dodatkowych modułów, zalecana w&nbsp;tysiącach porad dla początkujących.  
  Moim osobistym zdaniem -- ostra rewolucja, która może popsuć wielu osobom początki z&nbsp;Pythonem :roll_eyes: No ale jest jak jest, pozostaje podsuwać rozwiązania.

* Dodałem parę regułek automatycznie usuwających wiszące spójniki w&nbsp;tytułach wpisów.

  Koniec z&nbsp;nieestetycznymi `i` czy `z` wiszącymi na końcu linijki. Mała rzecz, ale cieszy moje pedantyczne oczy.

{% include details-end.html %}

### Rok Linuksa? U&nbsp;mnie na pewno!

Gigant Microsoft w&nbsp;tym roku nieco poleciał w&nbsp;kulki:

* wygasza wsparcie dla Windowsa 10;
* w&nbsp;zamian oferuje Windowsa 11, który nie zadziała na niektórych komputerach przez sztuczne wymogi dotyczące sprzętu;
* obciąża wspomnianego nowego Windowsa telemetrią, nachalnymi reklamami i&nbsp;funkcjami AI;
* ...a do tego now system zawiera irytujące błędy, dotykające najbardzej podstawowych funkcji.

  {:.post-meta .bigspace-after}
  Mój ulubiony przykład: powolna przeglądarka plików, którą dało się naprawić, celowo wywołując błąd usuwający górny pasek -- bo to on był źródłem problemu.  
  Mam czasem wrażenie, że Microsoft skrycie sprzyja Linuksowi i&nbsp;sabotuje sam siebie.

Ten splot czynników -- wraz z&nbsp;malejącą rolą programów biurowych, wynikającą z&nbsp;przepychania wielu rzeczy do internetu -- dał duże szanse otwartej i&nbsp;darmowej alternatywie. Linuksowi.

Jak napisałem we [wpisie, w&nbsp;którym go promuję](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}:

> Ze swojej strony na pewno stworzę parę przewodników po Linuksie i&nbsp;zachęcam innych do tego samego

I jak napisałem, tak zrobiłem. Na blogu zagościły liczne poradniki.

Było o&nbsp;instalowaniu Linuksa z&nbsp;pendrive'a. O&nbsp;rozwiązywaniu popularnych błędów. O&nbsp;ustawianiu języka polskiego, zdobywaniu czcionek Microsoftu w&nbsp;celu poprawienia kompatybilności LibreOffice'a...  
Ogólnie: rzeczy podstawowe, szczególnie przydatne dla osób wchodzących w&nbsp;nowy, otwarty świat równoległy wobec Windowsa.

Odszedłem też od typowego dla siebie skakania po tematach. Każdy post/samouczek rozwiązuje zwykle jeden konkretny problem, z&nbsp;jakim mogą się zderzyć ludzie przechodzący na Linuksa.

I wygląda na to, że wyszukiwarki nawet polubiły taką formę wpisów. Zarówno DuckDuckGo:

{:.figure .bigspace}
<img src="/assets/posts/podsumowania/2025/duckduckgo-linux-mint-ciemna-strona.jpg" alt="Zrzut ekranu z&nbsp;wyszukiwarki DuckDuckGo. Pod hasłem 'libreoffice czcionki z&nbsp;windowsa' wyświetla się post z&nbsp;Ciemnej Strony."/>

Jak i&nbsp;Gugiel:

{:.bigspace-before}
<img src="/assets/posts/podsumowania/2025/google-linux-mint-ciemna-strona.jpg" alt="Zrzut ekranu z&nbsp;wyszukiwarki Google. Widać, że jednym ze źródeł wymienionych pod odpowiedzią podaną przez AI jest Ciemna Strona."/>

{:.figcaption}
Wprawdzie to tylko mały link obok wyniku wyplutego przez AI... Ale przy Google'u trudno liczyć na więcej.

Linux jest na fali. I&nbsp;choć nie wiem, ile osób ostatecznie zjedna -- mając przeciw sobie mechanizmy korporacyjnych powiązań -- bardzo fajnie się czuję, mając swój mały wkład w&nbsp;rewolucję. W&nbsp;przyszłym roku będzie jeszcze większy :sunglasses:

## Wieści ze świata

### Odtajnione dokumenty na temat *???????*{:.cover}

W USA z&nbsp;wielką pompą, na szczeblu rządowym, ogłoszono publikację dokumentów związanych ze skandalem *????????*{:.cover}. Jednak *?????*{:.cover} *??????????????*{:.cover} danych była *???????*{:.cover} czarnymi prostokątami, ocenzurowana.

Popełniono jednak elementarny błąd, o&nbsp;którym [pisałem kiedyś na blogu](/2021/10/29/zakrywanie-danych){:.internal} -- prostokąty po prostu nałożono na tekst wewnątrz plików PDF. W&nbsp;takiej sytuacji w&nbsp;dokumencie pozostaje i&nbsp;tekst, i&nbsp;prostokąty. **Można normalnie zaznaczać i&nbsp;kopiować to, co się pod nimi ukrywa**.

Niekompetencja czy celowy bunt cenzorów? W&nbsp;sumie nieistotne. W&nbsp;każdym razie chętne osoby mogą [zapoznać się z&nbsp;pełniejszymi informacjami](https://news.ycombinator.com/item?id=46368946) niż te zawarte we fragmentach nieocenzurowanych.

Sprawa mnie oczywiście cieszy, bo stoję na stanowisku, że informacje chcą być wolne. Im więcej się ich ujawni, tym lepiej.

Ale czy samo odtajnienie cokolwiek zmienia?  
Powiedzmy sobie wprost: już raczej nie jest żadną tajemnicą ani tabu, że każdy kraj ma swoją **kastę oligarchów**. Dogadują się tylko ze sobą, realizują własne interesy, nie liczą się z innymi. I&nbsp;są przy tym bezkarni.

Obawiam się, że społeczeństwo zostało już doprowadzone do takich podziałów i&nbsp;poczucia bezsilności, że nawet najmocniejsze dowody przestępstw nie pchną ludzi do buntu. „No właśnie się pan dowiedział. I&nbsp;co?”.

{:.bigspace-before}
> Lost in the monochrome as self fades away  
Atrocity walks free at the end of all days  
There is no hope but what we can make  
The last human to stand against fate

{:.figcaption}
Źródło: [*Uberbyte*, *„Last Human”*](https://www.youtube.com/watch?v=HOLnQEv5JcI) (uwaga: YouTube). *Industrial* sprzed kilkunastu lat.

Jeśli znieczuleni ludzie na coś zareagują, to raczej na rzeczy dotykające ich bezpośrednio, godzące w&nbsp;ich życie.

...A tak się składa, że takie rzeczy też się szykują. Przykładem współczesne patologie związane z&nbsp;automatyzacją i&nbsp;elastycznymi algorytmami (nazwanymi marketingowo *sztuczną inteligencją* -- AI).

### AI i&nbsp;współczesna gorączka złota

„AI to rewolucja”. „AI zmienia świat”. Bez wątpienia.  
Wiele wskazuje jednak na to, że nie będzie to zmiana, za którą jej architekci zyskają pomniki i&nbsp;wieczną chwałę.  
Na ten moment nastroje są zgoła inne, zaś pędzący (postę-)pociąg dużo gniecie i&nbsp;niszczy pod swoimi kołami.

Pominę nawet aspekt zastępowania ludzi i&nbsp;„zabierania pracy”, w&nbsp;wielu branżach jednocześnie. To temat-rzeka, zbyt obszerny na krótką notkę.

Wspomnę zamiast tego o&nbsp;**wielkim, nieposkromionym apetycie AI**.

Po pierwsze: apetycie na dane. Pod tym względem złą sławą cieszy się firma Perplexity, której boty [masowo dobijają się do stron](https://news.ycombinator.com/item?id=42790252), powodując niemalże ataki przeciążające (*DDoS*). Obsługa ich zapytań nie jest darmowa -- koszty utrzymania niewinnych, prostych stronek nagle poleciały w&nbsp;górę.

Po drugie: apetyt na podzespoły, w&nbsp;tym pamięć (RAM).

Już teraz niektóre firmy, węsząc większe zyski, całkowicie olały sektor konsumencki i&nbsp;zaczęły zaopatrywać tylko branżę tworzącą modele AI. A&nbsp;to prowadzi do deficytów różnych podzespołów na rynku, wzrostów cen... I&nbsp;niezadowolenia społecznego.

Po trzecie: apetyt na energię. Prognozy [sugerują](https://cdn.xcancel.com/pic/orig/26B30BBF499F7/media%2FG6bEfGXX0AAKZkf.jpg), że samo tylko OpenAI, jeden z&nbsp;liderów, w&nbsp;ciągu 8&nbsp;lat może zwiększyć swoje zapotrzebowanie na energię 125-krotnie. Żłopiąc jej więcej niż współczesne Indie z&nbsp;ponad miliardem ludności.

{% include details.html summary="Uwag parę o&nbsp;hipokryzji i&nbsp;wyrachowaniu OpenAI" %}

Kilka lat temu, gdy pojawiały się pierwsze modele z&nbsp;serii GPT (a&nbsp;o Chacie GPT nikt jeszcze nie mówił), tworząca je organizacja OpenAI była dość zamknięta (wbrew swojej nazwie). Nie ujawniali niczego, co związane z&nbsp;ich modelami.

Mieli jednak wiarygodną wymówkę -- względy bezpieczeństwa. **Twierdzili, że ich modele w&nbsp;złych rękach mogą być groźne, że należy zachować najwyższą ostrożność**. Wprowadzić regulacje i&nbsp;mechanizmy bezpieczeństwa, nim to trafi do ludzi.

A teraz? Jesteśmy kilka generacji dalej, modele znacznie mocniejsze... A&nbsp;OpenAI dostaje pozwami za to, że ich automat nakłonił trochę osób do samobójstwa.  
I będzie ich więcej. Sama firma podaje, że według ich własnych statystyk [ponad milion osób](https://arstechnica.com/ai/2025/10/openai-data-suggests-1-million-users-discuss-suicide-with-chatgpt-weekly/) dzieli się z Chatem myślami samobójczymi.

Co robi w&nbsp;tych warunkach ta och-jakże-odpowiedzialna organizacja, widząc rosnącą zależność niektórych osób od swojego produktu?  
Zapowiada wprowadzenie [funkcji czatów intymnych](https://www.insights.uca.org.au/altman-defends-plan-to-introduce-adult-mode-in-chatgpt-sparking-debate-over-ai-boundaries/). „Bo jest na nie popyt”. 

Można teraz dostrzec w&nbsp;innym świetle ich wcześniejsze zapewnienia o&nbsp;odpowiedzialności. Dopuścić do głowy możliwość, że **promowali regulacje tylko po to, żeby zmonopolizować rynek**. Żeby postawiono bariery prawne, które tylko oni przeskoczą.

{:.post-meta .bigspace-after}
Ale przy tym na tyle niskie, żeby nie psuły im interesów; dlatego byli przeciwni regulacjom unijnym.

A wszelkie słowa o&nbsp;odpowiedzialności? Puste i&nbsp;bezduszne, jak teksty z&nbsp;ich generatorów.

{% include details-end.html %} 

Wszystkie wspomniane wyżej zasoby, jakie żłopie branża AI, są albo zabierane ludziom, albo wiążą się z&nbsp;utrudnieniem ich życia.

Co więcej, nie tylko firmy od sprzętu i&nbsp;tworzenia algorytmów rzuciły się na AI. Prawie każda, której zależy na inwestorach, próbuje się zaprezentować jako pionier. Trwa taka współczesna gorączka złota.

Microsoft zapowiedział, że Windows to od teraz „agentowy system operacyjny”. Czyli po ludzku: nabity elastycznymi algorytmami, próbującymi na siłę ułatwić użytkownikom życie.

{:.post-meta .bigspace-after}
To akurat odbieram pozytywnie, bo to kolejna rzecz -- na fali licznych słabości i&nbsp;niedoróbek Windowsa&nbsp;11 -- która może pchnąć ludzi ku alternatywowm.

Nawet **Firefox** poszedł ku gorszemu. Nowy szef Mozilli zapowiedział, że planuje zrobić z&nbsp;niego „współczesną przeglądarkę AI”.

Ogólnie: napieranie do przodu, za wszelką cenę, na wielu frontach, obiecywanie nieograniczonych zysków. A&nbsp;na przekór tym zapewnieniom już zaczęły się wyłaniać różne przeszkody.  
**To w&nbsp;końcu rypnie**. A&nbsp;patrząc na to, jak entuzjaści AI w&nbsp;swoim wyścigu kompletnie nie liczyli się z&nbsp;ludźmi -- raczej nie będą mogli liczyć na społeczne współczucie.

### Proctorio i&nbsp;koniec prześladowania badacza

Z dobrych wieści -- zakończyła się właśnie kilkuletnia sprawa, która szczególnie mnie oburzała.

Kanadyjski badacz, Ian Linkletter, skrytykował kiedyś publicznie amerykańską firmę **Proctorio**, sprzedającą program do automatycznego nadzorowania zdalnych egzaminów (takie „wczesne AI”).

Zdaniem firmy program był niezawodny. Linkletter dowodził, że jest inaczej.  
Często błędnie oznaczał osoby o&nbsp;nietypowym wyglądzie i&nbsp;zachowaniu jako potencjalnych oszustów, do dalszej weryfikacji. Niektórzy nauczyciele akademiccy, wierzący w&nbsp;nieomylność algorytmu, robili potem nieprzyjemności.

{:.post-meta .bigspace-after}
Miałem okazję wspomnieć o&nbsp;tej sprawie we [wpisie o&nbsp;prywatności maszyn wirtualnych](/2025/02/10/prywatnosc-maszyny-wirtualne){:.internal} (bo często się ich używa do ominięcia wspomnianego programu).

Na swoje nieszczęście Linkletter podał w&nbsp;swojej krytyce linki do filmów marketingowych. Firma wprawdzie sama rozsyłała je pracownikom uczelni, ale przy tym miała je ustawione jako niepubliczne.

Firma Proctorio olała krytykę i zamiast tego pozwała badacza, twierdząc że linkowanie do niejawnych filmów było naruszeniem jej praw autorskich.  
Sprawa toczyła się pięć lat. Po drodze zostały przetestowane możliwości kanadyjskiego sądownictwa i&nbsp;przepisów przeciw pozwom kneblującym (zawiodły na całej linii).

Ale ostatecznie [sprawa zakończyła się ugodą](https://linkletter.org/update-33-the-lawsuit-is-over/), badacz może wrócić do życia. Można sobie poczytać jego bloga i&nbsp;historię batalii.

{:.post-meta .bigspace-after}
Zaś z&nbsp;Proctorio -- nie powiem co robić :wink:

Samo zjawisko pozwów kneblujących (tak zwanych SLAPP-ów; *strategic lawsuits against public participation*) jest niestety dość częste. Czasem opierają się na prawie autorskim, jak tutaj albo w&nbsp;przypadku [sporu z&nbsp;firmą Newag](/2025/01/05/podsumowanie-2024-roku#newag-ici%C4%85g-dalszy-afery){:.internal}, producentem pociągów.

Innymi przepisami używanymi do celów duszenia krytyki są te związane ze zniesławieniem (Kodeks Karny) i&nbsp;naruszeniem dóbr osobistych (Kodeks Cywilny). Więcej napisałem o&nbsp;nich we [wpisie z&nbsp;serii *Corponomicon*](/corponomicon/2025/03/17/slapp-efekt-mrozacy){:.internal}.

{:.figure .bigspace}
<img src="/assets/posts/corponomicon/slapp/grozba-za-propagandyste.jpg" alt="Zrzut ekranu z&nbsp;portalu społecznościowego, na którym pewien człowiek pisze, że po wysłaniu pisma przez pełnomocniczkę pewien człowiek go przeprosił za naruszanie dóbr osobistych. Wyraża też nadzieję, że będzie to przestrogą dla innych internautów"/>

### Obrywające korporacje rolno-spożywcze

Ten rok przyniósł parę ciekawych potyczek między korporacyjnym marketingiem a&nbsp;jego przeciwnikami i&nbsp;demaskatorami.

Swego czasu napisałem o&nbsp;nieetycznym marketingu wokół [mleka zastępczego dla niemowląt](/2024/10/01/nestle-mleko-dla-niemowlat-afryka){:.internal}. Przodowała w&nbsp;tym grupa *Fed is Best*. Zaczęła jako neutralna, twierdząca że zależy im tylko na dobrostanie mam (czymkolwiek by nie karmiły).

Po zdobyciu popularności zaczęli jawnie uderzać w&nbsp;wytyczne Światowej Organziacji Zdrowia, promować mieszanki i&nbsp;zniechęcać do karmienia piersią. 

W styczniu tego roku ich profil został strącony z&nbsp;rowerka przez nieznanych hakerów. Właścicielki odzyskały dostęp, ale wiele treści zniknęło. Obecnie profil jest cieniem siebie.

Trochę żałuję, że nie zdążyłem zarchiwizować licznych komentarzy i&nbsp;pokazać, jakie mechanizmy manipulacji były stosowane na grupie, jak duszono głosy krytyczne. No trudno. 

{% include info.html
type="Ciekawostka"
text="Od czasu opisania afery znalazłem [arcyciekawy artykuł](https://thebreastfeedingfoundation.substack.com/p/the-documented-origin-of-fed-is-best), który opisuje, że za pierwotnym sloganem *Fed is Best* stała firma Abbott oraz agencja Ogilvy; potem inne firmy podchwyciły hasło."
%}

W przypadku firm z&nbsp;branży korporolnictwa (handel nasionami i&nbsp;chemią rolniczą) nie odnotowałem większych upadków; w&nbsp;ich przypadku powiedziałbym raczej, że **ten rok był rokiem precyzyjnego demaskowania**.

Z pewnego czasopisma naukowego wycofano w&nbsp;końcu [artykuł na temat pewnego herbicydu](https://cen.acs.org/research-integrity/misconduct/Glyphosate-study-2000-retracted-amid/103/web/2025/12) ze względu na konflikt interesów jego autorów.  
Ponownie: nie jest to żadna nowość. W&nbsp;mailach wewnętrznych firmy Monsanto, znanych od lat, wprost sugerowano, że to publikacja na zlecenie. Ale dobrze, że wydawnictwo naukowe też się po latach wzięło za zwalczanie patologii.

Swoją cegiełkę do punktowania korpo dorzucił również youtuber działający pod nickiem Veritasium, jeden z&nbsp;najpopularniejszych twórców zajmujących się popularyzacją nauki.

Opublikował w&nbsp;tym roku [film na temat afer wokół firmy Monsanto](https://www.youtube.com/watch?v=CxVXvFOPIyQ), który zebrał 17&nbsp;milionów wyświetleń. Ominął przy tym popularne pułapki czy szarlatanów doklejonych do tematu i&nbsp;zaserwował samo mięso, wskazując realne machlojki.

Co więcej, wprawne oko może dostrzec w&nbsp;komentarzach pod filmem narracje -- a&nbsp;nawet konkretne trollkonta -- jakie punktowałem parę lat wcześniej [w swoim wpisie](/2022/12/24/biotechnologia-trolle-youtube){:.internal}. Pięknie się to wszystko zazębia!

{:.post-meta .bigspace-after}
Oczywiście Veritasium ma też swoje cienie, a&nbsp;pochwała tego filmu nie oznacza z&nbsp;mojej strony rekomendacji ogólnej; wiem, że kiedyś np. bezkrytyczne promowali samojezdne auta firmy Waymo.  
Sam film również miał wady -- niepotrzebnie użyto w&nbsp;nim fragmentów nagrań z&nbsp;rosyjskiej telewizji. Było to tylko kilkanaście sekund migawek z&nbsp;protestów, ale to wystarczyło, żeby dać oponentom amunicję.

{% include details.html summary="I jeszcze aferka Bonus Eventus z&nbsp;jesieni 2024&nbsp;roku" %}

Nie zalicza się to wprawdzie do 2025&nbsp;roku, ale i&nbsp;tak ją tu dodam, bo sprawa jest bardzo ciekawa.

Mianowicie: grupa poważnych portali zajmujących się dziennikarstwem śledczym nagłośniła [aferę Bonus Eventus](https://rsf.org/en/usa-rsf-condemns-agrochemical-industry-s-shameful-practice-profiling-and-slandering-environmental). Zinfiltrowali platformę internetową, na której branża i&nbsp;politycy z&nbsp;amerykańskich agencji odpowiedzialnych za żywność wprost wymieniali się informacjami, narracjami, a&nbsp;nawet danymi krytyków.

Dziennikarze ujawnili między innymi próbki maili propagandowych, jakie regularnie otrzymywali subskrybenci strony. Wśród nich -- trochę nazwisk, które już wcześniej przewijały się w różnych odtajnionych mailach.

Właściciele tych nazwisk dotąd konsekwentnie zaprzeczali swoim branżowym powiązaniom. No to teraz muszą zaprzeczać mocniej :smiling_imp:

{% include details-end.html %}

Ogólnie widać, że nie są to już lata 2015-2019, kiedy korporolnictwo wydawało się chronione niezniszczalną tarczą propagandy.

**Reakcje ludzi -- pod filmem Veritasium i&nbsp;nie tylko -- wydają się mocnym dowodem na to, że nastawienie społeczne się zmienia**. Podobnie jak przy Linuksie -- tworzy się niepowtarzalna okazja, żeby się przebić, uderzyć w gigantów.

U siebie również mam nieco nagromadzonych materiałów na temat korporolnictwa. Kto wie, może pójdę za *Zeitgeistem* i&nbsp;też je dorzucę? :smiling_imp:

## 2026&nbsp;rokiem promowania federalizacji?

W obliczu napięć między USA a&nbsp;resztą świata, w&nbsp;tym Unią Europejską, nie dziwią dążenia Europy ku suwerenności, w&nbsp;tym również cyfrowej. Rozwijanie własnych usług i&nbsp;platform na terenie Unii, uniezależnienie się.

Ogólnie mnie to cieszy; w&nbsp;końcu pokrywa się z&nbsp;wieloma moimi poglądami.

Jestem przeciw *big techom* i&nbsp;cyfrowej kolonizacji. Umiałem docenić regulacje takie jak prywatnościowe GDPR czy antymonopolowe DMA.  
Poza tym zyskiwanie niezależności pewnie by się opierało na świecie *otwartego kodu źródłowego*, który tak przecież chwalę.

Mam jednak problem z&nbsp;tym, że na tle słów o&nbsp;suwerenności zaczęły się uaktywniać konta, które promują bardzo konkretną jej wersję -- **federalizację**. „Stany Zjednoczone Europy”.

Żeby nie było, że sobie to zmyślam -- portal *Politico* również [wspomina, że to szerszy ruch](https://www.politico.eu/article/mario-draghi-push-pragmatic-federalism-get-europe-out-predicament/). Orędownikiem jest między innymi Mario Draghi, były szef Europejskiego Banku Centralnego.

Oto widzę na portalach społecznościowych jednostronne komentarze promujące federalizację, wstawione jako odpowiedzi pod zwykłymi wpisami o&nbsp;Europie ([„Stwórzmy Stany Zjednoczone Europy! Tu i&nbsp;teraz!”](https://xcancel.com/MaBo974/status/1973884861258907818#m)).  
Zostawiają je jednowymiarowe konta, których całe „jestestwo” (nazwa i&nbsp;profil) obraca się wokół federalizacji.

Oto widzę, jak osoba z&nbsp;Polski nazywana przez niektórych płatnym propagandystą -- i&nbsp;ewidentnie działająca dotąd w&nbsp;interesie biznesu zagranicznego, nie Unii -- zaczyna nagle wrzucać treści chwalące jedność Europy, niepasujące do swojej dotychczasowej twórczości.

...I przypominam sobie, jak niedawno portal Wykop był zalewany postami nazywającymi Unię skansenem, zostającym w&nbsp;ogonie innowacji. Posty na jedno kopyto, zbierające nie wiadomo skąd po kilkaset plusów.

Urabianie ludzi, jak smarowanie brytfanny masłem.  
A zaraz po tym wjechało mięcho -- raport wspomnianego wyżej Draghiego. Wspominający, że żeby nie zostać w&nbsp;tyle, Unia powinna osłabić przepisy regulujące AI i&nbsp;ochronę danych. Niejedno korpo się pewnie ucieszyło.

I dochodzę w&nbsp;tym wszystkim do wniosku, że **federalizacja nie jest promowana oddolnie**. Że to jakaś kampania.

A czy to coś złego? Mam mieszane uczucia. Osobiście cenię w Unii kilka warstw „filtrowania” -- unijną i&nbsp;krajową. Dzięki temu, że sito jest gęste, udaje się blokować patologie takie jak pomysł kontroli czatów (wypłynął z&nbsp;USA, poparła go Komisja, utknął na Parlamencie).

Gdyby federalizacja miała w&nbsp;ostateczności zwiększać centralizację i&nbsp;osłabić to filtrowanie -- to nie zyska mojego poparcia. Bo stawianie świata na jednym wąskim filarze [krytykuję od dawna](/serie/cyfrowy_feudalizm/){:.internal}.

Na ten moment zachowuję otwartą głowę, ale przeczucia mam złe. Pozostaje zobaczyć, co przyszły rok przyniesie.

## Plany na przyszły rok

Od strony aferowej będzie więcej o&nbsp;AI (planuję na początku roku opisać patologie, z&nbsp;jakimi mierzą się osoby od tagowania danych). Będzie więcej punktowania propagandy, w&nbsp;tym wspomniane już materiały o&nbsp;korporolnictwie.

Będzie o&nbsp;śledzących zastosowaniach czujników smartfona (chciałem wrzucić w&nbsp;tym roku, ale temat okazał się rozleglejszy niż myślałem -- ostatecznie rozbiję go na dwa wpisy).

W przyszłym roku na pewno wspomnę o&nbsp;zaletach prywatnościowych **trybu ulotnego (_live_)**, czyli ładowania czystego systemu z&nbsp;pendrive'a prosto do pamięci, z&nbsp;pominięciem trwałego zapisu na dysku.

Będzie też o&nbsp;**adresie MAC**, dzięki któremu hotspoty mogą identyfikować nasze urządzenie i&nbsp;wyławiać nas z&nbsp;tłumu. Rzecz wredna, ale często łatwa do maskowania.

{:.post-meta .bigspace-after}
Zarówno tryb *live*, jak i&nbsp;losowy adres MAC to atuty prywatnościowego systemu *Tails*. Będzie dobra okazja, żeby go poznać od podszewki.

Jeśli wena dopisze, to chciałbym też poświęcić nieco uwagi programowi **OpenSnitch**, który pozwala monitorować wszystkie interakcje naszych programów z&nbsp;zewnętrznymi serwisami. A&nbsp;także blokować te niechciane.  
To świetny sposób na podejrzenie, co różne programy wysyłają w&nbsp;świat i&nbsp;na zyskanie odrobiny władzy nad swoim sprzętem. Można nieco się przestraszyć tym, jak „gadatliwy” bywa nawet najspokojniejszy system.

To tyle z&nbsp;zapowiedzi. Życzę sobie i&nbsp;Wam przyjemnego witania 2026&nbsp;roku! :metal:

