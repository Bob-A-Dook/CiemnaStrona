---
layout: post
title:  "Monitor Sądowy i Gospodarczy. Kronika błędów i dziwów"
description: "Po co walczyć z wiatrakami, gdy można z Monitorami"
subtitle: "Po co walczyć z wiatrakami, gdy można z Monitorami."
date:   2022-06-17 21:20:00 +0100
tags: [Analiza danych]
category: krs-msig
category_readable: "Myszkowanie w Monitorze i kopanie w KRS-ie"
image: "msig-problemy/msig-dziwy-baner.jpg"
image-width: 1200
image-height: 700
---

Witam w&nbsp;kolejnym odcinku serii o&nbsp;polskich firmach! Cały czas jesteśmy na etapie gromadzenia danych z&nbsp;publicznie dostępnych źródeł -- żeby w&nbsp;przyszłości wyłapywać ciekawostki, jakich nie zdradziłyby nam nawet komercyjne wywiadownie gospodarcze.

W [poprzednim wpisie]({% post_url 2022-05-06-msig-wprowadzenie %}){:.internal} poczyniłem pierwsze kroki w&nbsp;świat Monitora Sądowego i&nbsp;Gospodarczego -- pisma z&nbsp;bieżącymi informacjami z&nbsp;życia polskich firm. W&nbsp;formie suchych danych, czyli najlepszej.  
Zobaczyliśmy platformę, z&nbsp;której można pobrać to zacne pismo, i&nbsp;zerknęliśmy do metadanych w&nbsp;paru tysiącach plików.

Od tamtego czasu liczba moich Monitorów urosła do 2832&nbsp;i sięga teraz początków roku 2011. Zajrzałem też nieco głębiej -- w&nbsp;samą ich treść.

Zobaczymy, że wyciąganie danych z&nbsp;Monitorów to bolesna sprawa. Ale można przy tym odkryć całkiem ciekawe rzeczy:

* **Kilkadziesiąt tysięcy wpisów jest wybrakowanych**. Są całkiem lub prawie całkiem pozbawione treści albo mają luki w&nbsp;tekście.
* Liczba najgorszych przypadków była znacznie większa w&nbsp;2020 roku niż w&nbsp;pozostałych latach.
* Czasem coś się w formacie zmienia, z&nbsp;roku na rok znikają niektóre kategorie błędów (na przykład trzy kreski zamiast niektórych numerów pól). Ale bywa, że na ich miejsce przychodzą nowe.
* Literówki potrafią się trafiać nawet w&nbsp;miejscach, które w&nbsp;każdym rozsądnym świecie byłyby wypełniane przez komputer.
* Mimo błędów nadal można liczyć pewne rzeczy. I&nbsp;zobaczyć na przykład, że w&nbsp;roku 2020&nbsp;**ponad 15-krotnie wzrosła liczba przypadków zawieszenia lub wznowienia działalności**. I&nbsp;jest ich coraz więcej.
* Programy do edycji plików mogą zostawiać w&nbsp;nich swój ślad. Zadziwiająco wiele informacji o&nbsp;tym, co i&nbsp;jak zmieniał użytkownik.

Zapraszam do śmieszno-strasznej wyprawy w&nbsp;głąb Piekielnie Denerwującego Formatu :smile:

# Spis treści

* [Wprowadzenie](#wprowadzenie)
* [W&nbsp;idealnym świecie](#widealnym-świecie)
  * [Odczytywanie spisu treści](#odczytywanie-spisu-treści)
  * [Podział na kolumny i&nbsp;wpisy](#podział-na-kolumny-iwpisy)
  * [Przetwarzanie wpisów](#przetwarzanie-wpisów)
  * [Porządkowanie szczegółów](#porządkowanie-szczegółów)
* [W&nbsp;prawdziwym świecie](#wprawdziwym-świecie)
  * [Kłopotliwa konwersja](#kłopotliwa-konwersja)
  * [Skubane spisy treści](#skubane-spisy-treści)
  * [Kapryśne kolumny](#kapryśne-kolumny)
  * [Nietypowe Monitory, ciąg dalszy](#nietypowe-monitory-ciąg-dalszy)
  * [Nikczemne nagłówki i&nbsp;wpisy-widma](#nikczemne-nagłówki-iwpisy-widma)
  * [Tagi terroru i&nbsp;szokujące szczegóły](#tagi-terroru-iszokujące-szczegóły)
  * [Trzy kreski nicości](#trzy-kreski-nicości)
  * [Zawieszenie spółek](#zawieszenie-spółek)
* [Co dalej](#co-dalej)

## Wprowadzenie

Gwoli przypomnienia: swoje Monitory pobrałem z&nbsp;[oficjalnego źródła](https://ems.ms.gov.pl/msig/przegladaniemonitorow), ze strony Ministerstwa Sprawiedliwości. 

Miałem 2832&nbsp;egzemplarze. Od egzemplarza nr 1&nbsp;z 2011&nbsp;roku do egzemplarza 73&nbsp;z tego roku. Prawie 8&nbsp;gigabajtów na dysku, tylko czekających na obróbkę. Wszystkie w&nbsp;formacie PDF, o&nbsp;którym napiszę tutaj kilka słów, bo będzie dość istotny.

PDF to skrót od *Portable Document Format*. Do życia powołała go korporacja Adobe. To również format, w&nbsp;jakim dostępne są egzemplarze Monitora i&nbsp;wcześniej omawiane odpisy z&nbsp;KRS-u.  
Jego głównym założeniem jest to, żeby na każdym urządzeniu *wyświetlał się dokładnie tak samo*. Tekst ma się nie rozjeżdżać i&nbsp;nie robić niespodzianek, a&nbsp;po wydrukowaniu wyglądać jak na ekranie.

Też miałem trochę założeń i&nbsp;nadziei, kiedy zaczynałem szperać w&nbsp;tych plikach. W&nbsp;pierwszej części wpisu zobaczmy, jak to powinno wyglądać, kiedy wszystko działa. W&nbsp;części drugiej zobaczymy gorzką rzeczywistość. Ale na osłodę będzie parę ciekawostek.

{:.post-meta .bigspace}
Ograniczam technikalia do minimum, więc wpis powinien być dostępny dla każdego. Ale jeśli sprawy plików Cię nudzą, czytelniczko lub czytelniku, to można przeskoczyć prosto do śmieszkowania z&nbsp;[gaf i&nbsp;dziwów](#w-prawdziwym-świecie).

## W&nbsp;idealnym świecie

# Konwersja

Pierwszy krok to wyciągnięcie z&nbsp;plików tekstu. Samo to byłoby ciężką sprawą, gdybym musiał pracować od zera. Na szczęście **tę część już zrobili za mnie twórcy Popplera, zestawu programów do pracy z&nbsp;PDF-ami**.  
Od konwersji do tekstu mają `pdftohtml` -- szybki, lekki i&nbsp;skuteczny programik konsolowy.

Postanowiłem sprowadzić tekst do formatu XML, w&nbsp;którym lepiej mi się pracuje. Ogólnie wystarczy do tego jedna komenda, wpisana w&nbsp;konsoli:

{:.bigspace-before}
<div class="black-bg mono">pdftohtml -xml -i plik.pdf</div>

{:.figcaption}
Parametr *-i* od tego, żeby nie wyciągać obrazków. Czyli w&nbsp;praktyce godła razy kilkaset.

Efektem działania są linijki tekstu wraz z&nbsp;informacjami o&nbsp;położeniu lewej i&nbsp;górnej krawędzi, rozmiarze czcionki, fragmentach pogrubionych.

Popplera można łatwo przywoływać przez Pythona, żeby przetwarzać pliki tysiącami, w&nbsp;sposób powtarzalny.

# Odczytywanie spisu treści

Każdy Monitor liczy od kilkuset do ponad tysiąca stron i&nbsp;ma następującą strukturę:

1. Okładka i&nbsp;ogólne informacje
2. Spis treści
3. Jakieś inne, nieinteresujące mnie ogłoszenia
4. Wpisy z&nbsp;życia firm

   To ich szukam. Dzielą się na dwie sekcje: dla firm nowo założonych oraz dla zmian w&nbsp;firmach istniejących.

5. Indeks (dawniej)
6. Ostatnia strona

W trosce o&nbsp;swój niemłody komputer postanowiłem nie przetwarzać całego pliku jak leci, żeby potem odrzucać większość stron.  
Zamiast tego ładuję tylko kilkanaście pierwszych stron pliku, odczytuję ze spisu treści numery stron, potem przetwarzam wyłącznie te strony.

Może i&nbsp;używam niewydajnego Pythona, ale hej! Zawsze to plus ileśtam do energooszczędności. Poza tym dzięki temu wyłapałem ciekawe rzeczy w&nbsp;spisach treści, o&nbsp;czym później.

# Podział na kolumny i&nbsp;wpisy

Po znalezieniu sekcji z&nbsp;informacjami o&nbsp;firmach trzeba ją jakoś przetworzyć. Przeciętna strona i&nbsp;przeciętny wpis wyglądają tak:

{:.bigspace}
<img src="/assets/posts/msig-problemy/monitor-strona-wpis.jpg" alt="Widok na pojedynczą, niewyraźną stronę Monitora. Widać że wpisy na niej są ułożone w trzy kolumny. Jeden z nich jest zaznaczony ramką, a poniżej widoczny w powiększonej wersji. Widzimy, że składa się z trzech elementów oznaczonych różnymi kolorami i podpisanych pod spodem jako: nagłówek, łącznik oraz zmiany."/>

Tekst w&nbsp;Monitorze jest zawsze ułożony w&nbsp;trzy kolumny. To czytelne, ale dla człowieka; nam zależy na samych danych, więc dla wygody można to wszystko uprościć i&nbsp;„wypłaszczyć” zawartość kolumn i&nbsp;stron w&nbsp;jeden długi blok tekstu.

Potem trzeba jeszcze połączyć linijki. I&nbsp;nie jest to kwestia zwykłego sklejenia ich ze sobą. Trzeba bowiem pamiętać o&nbsp;rozbitych słowach.  
Gdyby na końcu jakiejś linijki było *moni-*, a&nbsp;na początku kolejnej *tor*, to by to trzeba połączyć w&nbsp;jedno słowo, usuwając kreseczkę (oficjalnie: [dywiz](https://pl.wikipedia.org/wiki/Dywiz)).

Ale gdyby kreseczka „dzieląca” pokrywała się z kreską wcześniej obecną w&nbsp;słowie, to już byłby problem. Fikcyjna Kasia Nowak-Słowak stałaby się Kasią NowakSłowak.

Na szczęście w&nbsp;tekście Monitorów odeszli od zaleceń typografii i&nbsp;zawsze dodają kreseczkę; jeśli pokrywa się z&nbsp;istniejącą, to **mamy po prostu dwie pod rząd, jedną można usunąć**. Ogromne ułatwienie. Choć nie mamy go niestety w&nbsp;przypadku dat oraz nazw firm z&nbsp;nagłówka:

<img src="/assets/posts/msig-problemy/dzielenie-wyrazow-trudnosci.jpg" alt="Trzy drobne rzuty ekranu pokazujące różne przypadki podziału słów. W pierwszym przypadku widać pojedynczy dywiz w nagłówku, w drugim przypadku dwa pod rząd w zwykłej nazwie, na koniec data z jednym." width="500px"/>

{:.figcaption}
Jeśli dziwne kreski w ostatnim wpisie budzą Twoją ciekawość, to cierpliwości, jeszcze o&nbsp;nich będzie.

Ledwo co połączymy tekst w&nbsp;jeden blok, a&nbsp;już trzeba go ponownie rozbijać! Najpierw na wpisy, a&nbsp;następnie każdy wpis na pomniejsze wydarzenia.

Warto tu zaznaczyć, że elementy wyraźnie wyróżniające nagłówek -- szare tło i&nbsp;pogrubiona linia -- niestety *są nieobecne w&nbsp;XML-u stworzonym przez Popplera*. Dysponujemy jedynie tekstem i&nbsp;znacznikami wskazującymi pogrubione fragmenty.

Ale w&nbsp;idealnym świecie to żaden problem! Przy tak powtarzalnej numeracji wystarczyłaby regułka w&nbsp;stylu:  
`znacznik pogrubienia + "Poz." + ciąg cyfr`.

Rozbijając w&nbsp;takich miejscach, zdobędziemy długą listę wpisów. Jeśli dotarliśmy do tego etapu, to jest dobrze; nawet gdyby coś było nie tak z&nbsp;pojedynczym wpisem, to nie wpłynie to na resztę.  
Zresztą w&nbsp;idealnym świecie żadnych problemów by nie było.

# Przetwarzanie wpisów

Wpis jest napchany informacjami. Te z&nbsp;nagłówków łatwo wyciągnąć, pozostaje główna część z&nbsp;listą zmian w&nbsp;firmie. Która jest o&nbsp;tyle ciekawa, że może tam być dowolna kombinacja zdarzeń.

W idealnym świecie pozwalają to okiełznać tagi (jak nazywam elementy zapisane pogrubionym tekstem). Nadają wpisowi strukturę i&nbsp;pozwalają zbierać informacje jak po sznurku.

Na każdym poziomie można się natknąć na tag `wpisać` albo `wykreślić`, który mówi nam, czy nasze dane oznaczyć plusem, czy też minusem.  
Poza tym mamy tagi, które można nazwać *strukturalnymi*. Mamy wśród nich wyraźną hierarchię, odpowiadającą budowie KRS-u:

1. dział,
2. rubryka,
3. podrubryka,
4. numer pozycji,
5. podrubryka wewnątrz pozycji.

Przy czym trzy ostatnie rzeczy pojawiają się tylko przy niektórych rodzajach zmian.

Dzięki takiej hierarchii wiemy jasno, co robić. Przechodząc na niższy poziom, gromadzimy coraz dokładniejsze informacje. Przechodząc z&nbsp;niższego na wyższy, możemy wszystkie zebrane informacje gdzieś zapisać i&nbsp;zacząć gromadzenie nowego kompletu. 

Spójrzmy ponownie na przykładowy wpis. Tagi to w&nbsp;nim elementy pogrubione:

{:.figure .bigspace}
<img src="/assets/posts/msig-problemy/wpis-tekst.jpg"/>

Po rozbiciu tego tekstu na najdrobniejsze pary `(tag / tekst)` przerabiamy go krok po kroku.

<details class="bigspace">
<summary>Dokładny opis metody</summary>
<ul>
  <li>
    <p><strong>Dz.3</strong> /</p>

    <p class="post-meta bigspace-after">(ustawiamy 3&nbsp;jako numer działu)</p>
  </li>
  <li>
    <p><strong>Rub.2</strong> / Wzmianki o&nbsp;złożonych dokumentach</p>

    <p class="post-meta bigspace-after">(ustawiamy 2&nbsp;jako numer rubryki, można też zapisać jej nazwę)</p>
  </li>
  <li>
    <p><strong>wpisać:</strong> /</p>

    <p class="post-meta bigspace-after">(ustawiamy aktywny tryb)</p>
  </li>
  <li>
    <p><strong>1</strong> / 1. data złożenia…</p>

    <p class="post-meta bigspace-after">(ustawiamy 1&nbsp;jako numer pozycji, a&nbsp;tekst odkładamy do jakiegoś schowka)</p>
  </li>
  <li>
    <p><strong>1</strong> / 3. OD 01.01.2017…</p>

    <p class="post-meta bigspace-after">(napotkaliśmy numer na tym samym poziomie hierarchii.<br>
Po pierwsze: zapisujemy do naszej wielkiej listy zdarzeń komplet: tryb + dział + rubryka + numer + tekst;<br>
Po drugie: tekst w&nbsp;schowku zastępujemy tym obecnym)</p>
  </li>
  <li>
    <p><strong>1</strong> / 4. OD 01.01.2017…</p>

    <p class="post-meta bigspace-after">Jak wyżej; dodajemy poprzedni tekst do listy zdarzeń, jako drugi element. Dział, rubryka i&nbsp;inne rzeczy takie same.<br>
Poza tym to ostatnia para, więc dodajemy do listy również tekst z&nbsp;niej, jako trzeci element.</p>
  </li>
</ul>
</details>

Kończymy z&nbsp;trzema elementami; każdy z&nbsp;nich z&nbsp;działu 3, rubryki 2, pozycji 1.  
Metodycznie i&nbsp;systematycznie. Nie jest to może najsprytniejszy sposób na przerobienie tych danych, ale jest niezawodny. W&nbsp;idealnym świecie.

# Porządkowanie szczegółów

Po przypisaniu zdarzenia do odpowiednich działów, rubryk i&nbsp;tym podobnych możemy czasem je rozbić na drobniejsze szczegóły i&nbsp;pogrupować.  
W kolejnych krokach, linijka po linijce:

```python
"1. data złożenia 14.03.2018 okres OD 01.01.2017 DO 31.12.2017"
(1, "data złożenia 14.03.2018 okres OD 01.01.2017 DO 31.12.2017")
(1, {"data złożenia": "14.03.2018", "okres": "OD 01.01.2017 DO 31.12.2017"})
```

Nie jest to obowiązkowe, ale może pomóc, jeśli chcemy potem dokładniej przeczesywać dane albo stworzyć w&nbsp;bazie osobną tabelkę na pewne informacje (tu akurat o&nbsp;dokumentach finansowych, ale podobny format mają dane adresowe).

W ten sposób, wychodząc od wielkiego pliku PDF, stopniowo schodzimy coraz głębiej, dodając do naszej bazy wpis za wpisem, zdarzenie za zdarzeniem, szczegół za szczegółem.

OK. To tyle ze świata idealnego i&nbsp;przyjemnego. A&nbsp;teraz przejdźmy do rzeczywistości!

## W&nbsp;prawdziwym świecie

Powiem wprost: **właściwie każde moje założenie okazało się błędne**.

Spis mówi prawdę? Numery zawsze będą pogrubione? Kolejność elementów będzie się zgadzała? A&nbsp;takiego!

Co się sprawdzało przy stu Monitorach, potrafiło efektownie się rozkraczyć przy sto pierwszym. Nie tylko przez moje braki warsztatowe (choć przyznaję się do nich pokornie), ale **również przez liczne błędy w&nbsp;samych plikach**.

W związku z&nbsp;tym przyzwyczaiłem się, że co pewien czas odkładam na bok dziwne przypadki i&nbsp;biorę je „pod lupę”. Po załataniu problemu odpalam skrypt ponownie. Czasem wyskakiwało po tym jeszcze więcej błędów. Ale to akurat dobrze.  
Nie oznaczało to, że ich przybyło -- tylko że coraz lepiej je wykrywam.

W ten sposób, po kilku tygodniach hobbystycznego szlifowania, z&nbsp;czasem wyłoniło się coś znośnego. Będącego w&nbsp;stanie przerobić wszystkie Monitory (choć nie wszystkie wpisy) z&nbsp;ponad 10-letniego okresu.

Oczywiście nawet się nie łudzę, że skrypt zawsze zadziała -- z&nbsp;ciekawości pobrałem parę najstarszych Monitorów i&nbsp;widzę, że od pewnego etapu zaczynają się skany pozbawione tekstu. Hurra.

Ale trzymajmy się tego, co mamy teraz. Przedstawiam wielką listę dziwów i&nbsp;zagwozdek :smile:

# Kłopotliwa konwersja

Dla ludzkich oczu sprawa jest prosta. Patrzymy na tekst, widzimy słowa. Na przykład „z&nbsp;ograniczoną odpowiedzialnością”. Czytanie po prostu działa.

Ale za kulisami często jest inaczej; w&nbsp;trzewiach plików PDF mamy tylko krótkie fragmenty zdań -- czasem nawet pojedyncze literki -- oraz ich położenie na stronie. Żeby zrobić z&nbsp;tego ciągły tekst, programy muszą porównywać ich położenie i&nbsp;łączyć literki w&nbsp;słowa, słowa w&nbsp;zdania.

Prowadzi to do dość zaskakujących przypadków, na przykład spacji wewnątrz słów:

{:.bigspace-before}
<img src="/assets/posts/msig-problemy/msig-rozjechany-tekst.jpg" alt="Dwa zrzuty ekranu. Ten u góry pokazuje krótki wpis z Monitora, a pod nim widać plik XML odpowiadający temu samemu tekstowi. Widać, że zamiast jednego słowa 'Poz' mamy te same literki, ale rozdzielone spacjami."/>

{:.figcaption}
U góry wygląd w&nbsp;programie do czytania PDF-ów, u&nbsp;dołu XML od Popplera.

W Monitorze mamy normalny, czytelny tekst. Ale niektóre kluczowe słowa w&nbsp;pliku XML (takie jak *Poz.*) są podzielone spacjami; skrypt musi zacząć od przeszukania tekstu i&nbsp;ściśnięcia ze sobą ich liter. Pierwsza rozbieżność względem świata idealnego.

A skąd się te spacje wzięły?

Możliwe, że wina częściowo leży po stronie Popplera. Za kulisami PDF składa się z&nbsp;regułek graficznych. Być może najpierw tekst jest ustawiany w&nbsp;większych odstępach, a&nbsp;potem „ściskany” inną regułką? A&nbsp;Poppler jej nie wyłapuje i&nbsp;stąd rozbieżność między tym co widzimy a&nbsp;jego XML-em? Nie mam niestety na tyle czasu i&nbsp;umiejętności, żeby zajrzeć do jego kodu i&nbsp;to zbadać.

Natomiast zastanawia fakt, że takie rzeczy trafiają się tylko w&nbsp;niektórych miejscach, zaś w&nbsp;innych nie. Może to oznaczać, że **prawdopodobnie ktoś ręcznie majstrował przy danym wpisie**.

Nie znam zaplecza KRS-u i&nbsp;Monitora, ale obstawiałbym następujący obieg informacji, od momentu wprowadzenia danych aż po strony Monitora:

1. Ktoś zmienia jakieś informacje dotyczące swojej firmy.  
   W&nbsp;tym celu wpisuje nowe informacje w&nbsp;jakiś formularz (jeden standardowy szablon? A&nbsp;może są różne warianty?). 
2. Informacje trafiają do systemu.  
   Od teraz można je pobrać w&nbsp;formie odpisów KRS.
3. Autorzy Monitora otrzymują swego rodzaju „wydruk” informacji z&nbsp;systemu. Układają to w&nbsp;postać względnie czytelną dla ludzi.

W centrum zdarzeń jest komputer. Zaś komputery są przewidywalne i&nbsp;często przechowują dane jako najprostszy tekst. Bez informacji o&nbsp;jakichś odstępach między słowami, bo dla nich to zupełnie niepotrzebne.

Dlatego, jeśli na końcu wyjdą jakieś zmiany -- zwłaszcza takie dotyczące pojedynczych przypadków, a&nbsp;nie wszystkich wpisów naraz -- to prawdopodobnie zostały wprowadzone przez ludzi. A&nbsp;gdyby coś było bardzo powtarzalne, to zapewne wynika z&nbsp;winy komputera.

Oprócz tekstu rozstrzelonego trafiały się czasem **zduplikowane linijki**. Dla naszych oczu niewidoczne, bo idealnie się nakładają. Identyczne położenie, identyczny tekst, ta sama strona. Dla skryptu kłopotliwe, ale łatwe do usunięcia.

Takie coś mogło powstać na przykład wskutek ręcznego edytowania wpisu, gdyby ktoś nacisnął `Ctrl+C` i&nbsp;potem `Ctrl+V`, wklejając go w&nbsp;tym samym miejscu. Nie znam działania programów do *desktop publishingu*, ale jeśli bazują na warstwach, jak Gimp, to byłoby to całkiem możliwe.

# Skubane spisy treści

„*Zaufaj spisowi treści*, mówili. *Będzie fajnie*, mówili”.

Pomysł, żeby kierować się spisem i&nbsp;nie czytać całego dokumentu, zazwyczaj działał. Ale okazało się, że **numery podane w&nbsp;spisie mogą zawierać błędy**. Musiałem dopisać parę regułek, żeby skrypt nigdy nie wierzył spisowi na ślepo i&nbsp;sprawdzał, czy znajduje się tam gdzie powinien.

Błędy w&nbsp;spisie dotyczyły zarówno numerów stron, jak i&nbsp;numerów wpisów. Występowały w&nbsp;różnych odmianach.

* Najprostszy -- ewidentna literówka. Na przykład strona pierwsza ma numer wyższy niż ostatnia albo numery sekcji nakładają się na siebie.
* Groźniejszy -- literówka wiarygodna. Kiedy wpisy dla firm powinny np. zaczynać się od strony 165, a&nbsp;tak naprawdę są od 156.
* Dziwny -- całkowity brak numerów stron.
* Jeszcze dziwniejszy -- literówka w&nbsp;innej, szablonowej części spisu treści.

{:.bigspace-before}
<img src="/assets/posts/msig-problemy/spis-tresci-dziwy.jpg" alt="Trzy przykłady błędów w numeracji spisów treści w Monitorze. Najpierw mamy zwykłą literówkę w numerze, potem zera zamiast numerów wpisów, a na koniec dwukrotnie powtórzone słowo 'Poz'." width="500px"/>

{:.figcaption}
Literówka z&nbsp;Monitora nr 23&nbsp;z 2021&nbsp;roku.

A ponieważ jesteśmy ludźmi kultury i&nbsp;nie polegamy na dowodach anegdotycznych, przedstawiam trochę statystyk. Różne braki w&nbsp;numeracji stron:

{:.bigspace-before}
<div class="black-bg mono">
<span class="red">(wcześniej niskie jednocyfrowe)</span><br/>
Rok 2018:  6<br/>
Rok 2019:  2<br/>
Rok 2020:  <span class="red">25</span><br/>
Rok 2021:  1<br/>
Rok 2022:  2
</div>

{:.figcaption}
Liczba błędów w&nbsp;numeracji stron w&nbsp;spisie treści.

W roku 2020&nbsp;dość mocno wzrosła liczba błędów w&nbsp;numeracji stron! Może się potwierdzać obserwacja z&nbsp;poprzedniego wpisu, że ten rok był w&nbsp;jakiś sposób przełomowy.

Z kolei błędy w&nbsp;numerach wpisów, również zawartych w&nbsp;spisie treści, zazwyczaj polegały na zamianie miejscami dwóch cyferek albo zgubieniu jednej.  
**To raczej „ludzkie” literówki**, więc mamy argument za tym, że spis treści nie jest przygotowywany ani sprawdzany przez komputer.

Kiedy dopracuję i&nbsp;upowszechnię skrypt, to polecam autorom wypróbować. Co jak co, ale liczenie wpisów działa dobrze i&nbsp;ułatwiłoby końcową korektę :wink:

# Kapryśne kolumny

Po okiełznaniu spisu zabieramy się za nasz trójkolumnowy układ tekstu.  
Ale czy na pewno? Okazuje się, że niektóre elementy nie trzymają się reguł i&nbsp;potrafią zaczynać się w niestandardowych położeniach.

Nie nazwałbym tego błędem, ale na pewno jest pewnym odejściem od normy; zwykle mamy linijkę pod linijką. Nietypowe wymiary pojawiają się w&nbsp;XML-u od Popplera na przykład wtedy, kiedy tekst w&nbsp;Monitorze jest wyjustowany:

{:.bigspace-before}
<img src="/assets/posts/msig-problemy/justowanie-ilustracja.jpg" alt="Dwa zrzuty ekranu ustawione jeden pod drugim. Pierwszy pokazuje edytor tekstowy i linie tekstu o bardzo różnej wartości zmiennej left. Pod spodem widać wpis z Monitora, któremu odpowiadają powyższe linijki. Wyróżnia się tym, że tekst jest wyjustowany i są duże odstępy między słowami"/>

{:.figcaption}
Wartość *left* pokazuje, gdzie zaczyna się dana linijka. Gdyby nie justowanie, mielibyśmy jedynie siedem linijek, jedną pod drugą. 

Spójrzmy na liczbę stron, na których trafiały się elementy niepokorne, zaczynające się w&nbsp;nietypowym położeniu. Tym razem to nie rok 2020&nbsp;przoduje, lecz lata dawniejsze:

{:.bigspace-before}
<div class="black-bg mono">
Rok 2011:  <span class="red">35851</span><br/>
Rok 2012:  <span class="red">21839</span><br/>
Rok 2013:  262<br/>
Rok 2014:  75<br/>
Rok 2015:  265<br/>
<span class="post-meta">(potem podobnie jak w&nbsp;2015)</span>
</div>

{:.figcaption}
Liczba stron, na których były elementy leżące poza standardowymi kolumnami.

Liczba takich stron w&nbsp;dawniejszych latach jest powalająca.

Tak jak wcześniej pisałem -- kiedy mamy do czynienia ze zmianami na wielką skalę, to prawdopodobnie winę ponosi komputer.  
Z ciekawości odpaliłem jeszcze raz [skrypt do gmerania w&nbsp;metadanych]({% post_url 2022-05-06-msig-wprowadzenie %}#metoda){:.internal}, którego użyłem podczas tworzenia poprzedniego wpisu (z tym że wówczas na Monitorach nowszych). Okazało się, że dla lat 2011-2012 wyszły dość ciekawe rzeczy, które później już się nie pojawiały:

* w&nbsp;polu `Page Size` mamy wymiary *576 x&nbsp;841.89* -- inne od późniejszych, wynoszących w&nbsp;zaokrągleniu *595 x&nbsp;842*;
* w&nbsp;polu `Title` (zawierającym nazwę pliku, z&nbsp;którego stworzono PDF-a) pojawiły się pliki z&nbsp;rozszerzeniem *.qxp*. W&nbsp;nowszych Monitorach mamy już *.indd*, format od Adobe.

Wyszukałem, czym jest format *.qxp* i&nbsp;znalazłem informację, że jest wykorzystywany przez [program *QuarkXPress*](https://fileinfo.com/extension/qxp). Bingo!

Mamy zatem mocny dowód na to, że **do roku 2012&nbsp;ludzie z&nbsp;Ministerstwa pracowali w&nbsp;tym programie, a&nbsp;potem przeszli na programy od Adobe**.

Ciekawostką poboczną może być to, że QXP ostrzej sobie poczyna z&nbsp;plikiem, częściej rozbijając tekst na krótsze linijki. A&nbsp;przynajmniej tak to wygląda w&nbsp;„oczach” Popplera. Ma też ustawiony inny rozmiar stron.  
W związku z&nbsp;tym możliwe, że dałoby się ustalić na podstawie samych linijek tekstu, że jakiś plik PDF został stworzony w&nbsp;Quarku. Byłyby jak odcisk palca, tylko że dla programów, a&nbsp;nie [internautów]({% post_url 2022-06-10-fingerprinting %}){:.internal}.

Mamy też znacznie rzadsze przypadki Monitorów, w&nbsp;których układ kolumn w&nbsp;*całym* dokumencie różnił się od tego typowego:

* z&nbsp;roku 2013: nr 228, 234, 240;
* z&nbsp;roku 2017: nr 165;
* z&nbsp;roku 2018: nr 166, 173.

Każda strona miała w&nbsp;nich trzy kolumny, tylko że różniące się szerokością od typowych. Najbardziej prawdopodobna przyczyna to moim zdaniem użycie innych programów niż zazwyczaj, z&nbsp;odmiennymi ustawieniami. Może jakiś komputer się popsuł i&nbsp;pracowano na rezerwowym.

# Nietypowe Monitory, ciąg dalszy

W poprzednim wpisie, patrząc na same metadane, znalazłem 8&nbsp;Monitorów nie pasujących do reszty, z&nbsp;których aż połowę wydano w&nbsp;2020 roku. Postanowiłem bliżej im się przyjrzeć i&nbsp;zobaczyć, czy wyróżniają się również pod względem błędów i&nbsp;dziwów.

Przy sześciu z&nbsp;nich -- nie. Stety-niestety. Okazały się dość typowe. Parę braków miały, ale raczej z&nbsp;gatunku tych powszechniejszych. Albo coś przeoczyłem.

Natomiast dwa pozostałe Monitory potwierdziły swoją wyjątkowość również swoją zawartością:

* **Numer 22&nbsp;z 2020&nbsp;roku**.  
  204&nbsp;strony z&nbsp;nietypowym położeniem elementów.
* **Numer 23&nbsp;z 2020&nbsp;roku**.  
  192&nbsp;strony z&nbsp;nietypowym położeniem elementów.  
  Do tego 2&nbsp;rzadkie przypadki nałożonych na siebie, zduplikowanych linii.

To tym ciekawsze, że w&nbsp;roku 2020&nbsp;mój skrypt wykrył *łącznie* 464&nbsp;przypadki stron odstających od trójkolumnowego standardu. Oraz 2&nbsp;przypadki pokrywającego się tekstu.  
Zatem **te dwa Monitory, wydane jeden po drugim, odpowiadają za prawie 100% nietypowych stron w&nbsp;dokumentach w&nbsp;tamtym roku**.

Obstawiałbym, że ktoś je edytował dość intensywnie; w&nbsp;nietypowym programie (*Adobe InDesign CS6*, jeśli wierzyć metadanym), może również niezgodnie ze wcześniej stosowanymi metodami.  
Niestety nie dowiemy się, kto to był. Jak pisałem w poprzednim wpisie, pole `Author` w&nbsp;metadanych dla obu tych plików było puste.

To był gorący okres dla Ministerstwa Sprawiedliwości, zwłaszcza że mówimy o&nbsp;dwóch egzemplarzach wydanych jeden po drugim. Może mają z&nbsp;tym jakiś związek zmiany kadrowe, które wypatrzyłem w&nbsp;poprzednim wpisie.

Rozwiązania zagadki na chwilę obecną nie mam. Ale możemy co najwyżej się zadziwić, że garść metadanych i&nbsp;linijek tekstu potrafi tak wiele nam ujawniać. Fascynujące, nieprawdaż?

# Nikczemne nagłówki i&nbsp;wpisy-widma

Elegancki, zgodny z&nbsp;kolejnością numer wpisu, a&nbsp;po nim kompletny nagłówek? W&nbsp;świecie idealnym tak było! Wystarczyło znaleźć tag od pogrubionego tekstu, potem słowo *Poz.*, potem liczbę. W&nbsp;ten sposób wyłowilibyśmy każdy wpis. Po słowie *KRS* znalazłby się numer KRS. I&nbsp;tak dalej.

Ale nie. Nawet w&nbsp;miejscach, które uważam za najbardziej szablonowe i&nbsp;powtarzalne, w&nbsp;sam raz do wypełnienia przez komputer, potrafiły pojawić się błędy:

* nagłówki nie zawsze były pogrubione;
* zdarzały się literówki w&nbsp;słowie *Poz.* albo brak spodziewanych spacji;
* czasem oprócz słowa ucięty był cały numer wpisu;
* innym razem numer wpisu się zgadzał, ale wnętrze nagłówka (najczęściej wokół słowa *KRS*) było „nadgryzione”. 

{:.bigspace}
<img src="/assets/posts/msig-problemy/naglowki-problemy.jpg" alt="Kilka przykładów błędów w nagłówkach, oznaczonych czerwonym kolorem. Brakujący numer wpisu na początku, nagłówek zapisany niepogrubionym tekstem, tekst częściowo zakryty innymi słowami."/>


Według moich statystyk błędne nagłówki to już na szczęście raczej melodia przeszłości :+1: Od kilku lat nie mamy na przykład uciętych i&nbsp;niekompletnych numerów wpisów:

<div class="black-bg mono">
<span class="post-meta">W poprzednich latach podobnie</span><br/>
Rok 2015:  4<br/>
Rok 2016:  14<br/>
Rok 2017:  26<br/>
Rok 2018:  25<br/>
Rok 2019:  4<br/>
</div>

{:.figcaption}
Liczba wpisów z&nbsp;nagłówkiem uciętym na początku.

Całkiem wyginęły również błędy związane z&nbsp;brakiem numeru KRS w&nbsp;środku nagłówka:

<div class="black-bg mono">
Rok 2011:  1<br/>
Rok 2012:  4<br/>
Rok 2014:  1<br/>
Rok 2017:  12<br/>
Rok 2018:  37<br/>
Rok 2019:  1<br/>
</div>

{:.figcaption}
Liczba wpisów z&nbsp;niekompletnym środkiem nagłówka.

Ale wstrzymajmy się z&nbsp;zachwytami. W&nbsp;nieco późniejszych latach tak się bowiem zdarzało, że nagłówek był kompletny i&nbsp;elegancki... A&nbsp;**wpisy zawierały wyłącznie pustkę**. Ewentualnie samą informację o&nbsp;rubryce.

<img src="/assets/posts/msig-problemy/puste-wpisy.jpg" alt="Przykład jednego wpisu całkiem pustego oraz jednego zawierającego wyłącznie informację o dziale i rubryce. Miejsca, w których są brakujące dane, oznaczyłem znakami zapytania" width="500px"/>

Błąd najbardziej dotkliwy, czyli wpisy całkiem pozbawione treści, to zdecydowanie rzecz współczesna; przybyły w&nbsp;roku 2018, a&nbsp;najszybszą ekspansję zaliczyły w&nbsp;latach pandemicznych:

<div class="black-bg mono">
Rok 2018:  346<br/>
Rok 2020:  13350<br/>
Rok 2021:  5530
</div>

{:.figcaption}
Liczba wpisów całkiem pozbawionych informacji po nagłówku.

Miejmy nadzieję, że ich zerowa liczba w&nbsp;tym roku już z&nbsp;nami zostanie.

Powoli wygasa również liczba wpisów niepełnych. Które też zaliczyły pewien skok w&nbsp;roku pandemicznym. Ale, o&nbsp;dziwo, wciąż nieporównywalnie mniejszy niż w&nbsp;latach 2015-2017:

<div class="black-bg mono">
<span class="post-meta">(wcześniej jeszcze mniej)</span><br/>
Rok 2014:  26<br/>
Rok 2015:  <span class="red">7285</span><br/>
Rok 2016:  <span class="red">10235</span><br/>
Rok 2017:  <span class="red">11603</span><br/>
Rok 2018:  1180<br/>
Rok 2019:  863<br/>
Rok 2020:  1674<br/>
Rok 2021:  528<br/>
Rok 2022:  77
</div>

{:.figcaption}
Liczba wpisów z&nbsp;nagłówkiem i&nbsp;śladowymi informacjami o&nbsp;rubryce.

Jeśli chodzi o&nbsp;analizę danych, te dwa rodzaje wpisów oznaczają kłopoty.  
Z pustego i&nbsp;Salomon nie naleje, więc stajemy przed brutalną prawdą -- **Monitor Sądowy i&nbsp;Gospodarczy nam zwyczajnie nie da wszystkich potrzebnych informacji**.  
Ale hej, to nie koniec świata!

{:.bigspace-before}
> Lecz jeśli chcemy, te wszystkie dziury *miłością*{:.corr-del} KRS-em da się załatać.

{:.figcaption}
Inspiracja: motyw muzyczny z&nbsp;„Rodziny Zastępczej”.

Znając numery KRS z&nbsp;nagłówków, możemy kiedyś pobrać odpisy dla feralnych firm i&nbsp;zobaczyć, jakich informacji brakowało. Ale to sprawa na kolejny wpis. Tymczasem lećmy dalej; do tekstu tych wpisów, które w&nbsp;ogóle go mają.

# Tagi terroru i&nbsp;szokujące szczegóły

Jeśli już udało się zebrać wpisy, a&nbsp;ich nagłówki były kompletne, to pozostało rozbijanie tekstu na części. Tutaj trafiłem na kilka rodzajów uciążliwości:

* Literówki w&nbsp;nazwach tagów
  (*ub.* zamiast *Rub.*, *pisać* zamiast *wpisać* i&nbsp;tak dalej).
* Pogrubienie czegoś innego niż tag (rzadko).
* Niepotrzebne spacje w&nbsp;tekście.
* Literówki w&nbsp;miejscach innych niż tagi, na przykład w&nbsp;nazwach rubryk.
* Nagłe urwanie tekstu po tagu  
  (przykładowo: mamy *Prub.*, tag oznaczający podrubrykę, a&nbsp;po nim koniec wpisu albo nowy dział).

{:.bigspace-before}
<img src="/assets/posts/msig-problemy/tagi-literowki.jpg" alt="Dwa krótkie przykłady literówek w pogrubionym tekście. Zamiast słowa 'wpisać' w jednym miejscu mamy 'pisać', a w drugim 'wpisć'."/>

{:.figcaption}
Źródło: monitor nr 135&nbsp;z 2018&nbsp;roku.

{:.bigspace}
<img src="/assets/posts/msig-problemy/wpisy-tresc-dziwy.jpg" alt="Pięć kolejnych przykładów błędów, takich jak dziwny tag, literówka w nazwie kategorii, tekst urwany po nazwie rubryki, duża luka pośrodku wpisu"/>

W nazwach rubryk, takich jak „Dane wspólników”, znajdziemy często niepotrzebne spacje. Pod tym względem dominował rok 2017:

<div class="black-bg mono">
<span class="post-meta">(wcześniej podobne jak w&nbsp;2016)</span><br/>
Rok 2016:  471<br/>
Rok 2017:  <span class="red">2336</span><br/>
Rok 2018:  <span class="red">1053</span><br/>
Rok 2019:  600<br/>
Rok 2020:  4<br/>
Rok 2022:  1
</div>

{:.figcaption}
Liczba wpisów ze spacjami wewnątrz nazw rubryk.

Rok 2013&nbsp;był z&nbsp;kolei rokiem literówek: 

<div class="black-bg mono">
Rok 2011:  8<br/>
Rok 2012:  4<br/>
Rok 2013:  <span class="red">789</span><br/>
Rok 2014:  2<br/>
Rok 2015:  8<br/>
<span class="post-meta">(potem też mało, po 2019&nbsp;zero)</span>
</div>

{:.figcaption}
Liczba wpisów z&nbsp;literówkami w&nbsp;nazwach rubryk.

Na szczęście zarówno literówki, jak i&nbsp;spacje wewnątrz tagów stopniowo wygasają. Zostawiając nas z&nbsp;myślą: co w&nbsp;ogóle było ich źródłem? Jakieś dziwne ustawienia systemu? Czy może błędy ludzkie?

Rok 2020&nbsp;ponownie dał o&nbsp;sobie znać również w&nbsp;przypadku tekstu wpisów. To w&nbsp;nim najczęściej występowały wpisy nagle urwane, zostawiające nas ze słowem *PRub.*, strollowanych jak po usłyszeniu żartu o&nbsp;żółtych kuleczkach. 

<div class="black-bg mono">
<span class="post-meta">(wcześniej równie mało)</span><br/>
Rok 2019:  3<br/>
Rok 2020:  <span class="red">136</span><br/>
Rok 2021:  1
</div>

{:.figcaption}
Liczba wpisów nagle urwanych po nazwie rubryki.

Patrząc na te i&nbsp;poprzednie rodzaje błędów, można się cieszyć, że wiele z&nbsp;nich staje się coraz rzadszych. Ale jest coś, w&nbsp;czym rok 2022&nbsp;zdecydowanie króluje -- **liczba niedomkniętych nawiasów**.

<div class="black-bg mono">
<span class="post-meta">(wcześniej ok. 100&nbsp;na rok)</span><br/>
Rok 2017:  111<br/>
Rok 2018:  206<br/>
Rok 2019:  198<br/>
Rok 2020:  161<br/>
Rok 2021:  187<br/>
Rok 2022:  <span class="red">354</span><br/>
</div>

{:.figcaption}
Liczba niedomkniętych nawiasów w&nbsp;tekście wpisu.

# Trzy kreski nicości

W toku rozbijania wpisów na szczegóły dość szybko trafiłem na wpisy „wykreskowane”:

{:.bigspace-before}
<img src="/assets/posts/msig-problemy/tekst-luki.jpg" alt="Wpis, w którym zamiast większości nazw rubryk widać kreski. Dane opisywanej w nim osoby zakryłem dodatkowo prostokątami. Nad wpisem widać nagłówek dla całej sekcji, mówiący 'Przedsiębiorstwa państwowe'." width="500px"/>

{:.figcaption}
Jasnoszare prostokąty na dole dodane przeze mnie; wszystkie kreskowane braki już tam były.

Brakowało w&nbsp;nich jakiejś informacji -- czasem o&nbsp;numerze działu, czasem o&nbsp;jakiejś szczegółowej wartości -- a&nbsp;zamiast niej były trzy kreski. O&nbsp;takie:

<div class="black-bg mono" style="letter-spacing:3px">——-</div>

Długa, długa, krótka. W&nbsp;[alfabecie Morse'a](https://en.wikipedia.org/wiki/Morse_code) byłaby to literka *G*. Jak sami wiecie co.

Jak pomiętamy, powtarzalne zachowanie oznacza zapewne błąd po stronie systemu; być może tak reaguje, kiedy nie wie co wpisać.

Na szczęście większość wpisów z&nbsp;lukami była poza tym kompletna, więc można było odczytać, o&nbsp;jaką firmę i&nbsp;zdarzenia chodzi, a&nbsp;potem to sprawdzić w&nbsp;KRS-ie:

{:.bigspace}
<img src="/assets/posts/msig-problemy/dziwne-wpisy-wyjasnienie.jpg" alt="Obrazek złożony z dwóch zrzutów ekranu. U góry mamy jeden wpis z częściowo brakującymi informacjami, zamiast których są kreski. Numer działu oraz jedną z informacji oznaczyłem kolorem. Pod spodem widać zrzut z odpisu Krajowego Rejestru Sądowego, w których tymi samymi kolorami oznaczyłem rzeczy ze wpisu. Widać, że wpis dotyczył zawieszenia działalności."/>

Braki danych dotyczące Działu 6&nbsp;**najczęściej wiązały się z&nbsp;zawieszaniem albo wznawianiem działalności**. System z&nbsp;jakiegoś powodu nie lubi tej rubryki i&nbsp;ciągle pojawia się ona w&nbsp;Monitorze z&nbsp;kreskami zamiast informacji.  
Potraktowałem ją jak osobny przypadek i&nbsp;oddzieliłem od innych przykładów luk. Zaraz do niej wrócimy.

A na razie skupię się na luce pokazanej na początku, dotyczącej przeważnie dość rzadkiej kategorii przedsiębiorstw państwowych.  
To dość ciekawy przypadek; z&nbsp;jednej strony brak danych, więc wina komputera. Ale z&nbsp;drugiej strony występuje tylko przy konkretnych wpisach.

Może nam to sugerować, że **przedsiębiorstwom państwowym odpowiadała oddzielna część systemu albo ich wpisy były dodawane osobnym kanałem**. I&nbsp;gdzieś po drodze system dostawał czkawki od ich danych.

Luki tego rodzaju, gdy mamy kreski zamiast na przykład numeru rubryki, są już na szczęście w&nbsp;zaniku. Ostatnią mieliśmy w&nbsp;2020 roku:

<div class="black-bg mono">
<span class="post-meta">(wcześniej podobnie)</span><br/>
Rok 2015:  26<br/>
Rok 2016:  32<br/>
Rok 2017:  21<br/>
Rok 2018:  2<br/>
Rok 2019:  3<br/>
Rok 2020:  1
</div>

{:.figcaption}
Liczba wykreskowanych luk zamiast numerów działów (nie licząc tych we wpisach dotyczących zawieszenia firm).

Ale kreski zamiast tagów oraz wpisy związane z&nbsp;zawieszonymi firmami i&nbsp;tak są rzadkie w&nbsp;porównaniu z&nbsp;kreskami obecnymi w&nbsp;zwykłym tekście, czyli w&nbsp;informacjach szczegółowych. Spójrzmy tylko na ich liczbę w&nbsp;podziale na lata:

<div class="black-bg mono">
Rok 2011:  134<br/>
Rok 2012:  7307<br/>
Rok 2013:  8604<br/>
Rok 2014:  8269<br/>
Rok 2015:  <span class="red">98832</span><br/>
Rok 2016:  <span class="red">97461</span><br/>
Rok 2017:  <span class="red">51956</span><br/>
Rok 2018:  66<br/>
<span class="post-meta">(później coraz mniej)</span>
</div>

{:.figcaption}
Liczba wykreskowanych luk zamiast niektórych informacji szczegółowych (nie licząc tych we wpisach o&nbsp;zawieszeniu firm).

W roku 2012&nbsp;ich liczba wprost eksplodowała! W&nbsp;roku 2015&nbsp;ponownie. A&nbsp;potem, w&nbsp;2018 roku, nagle się gwałtownie skurczyła i&nbsp;taka już została.

Wyjaśnienie jest proste; **najczęstszym źródłem takich luk była numeracja pól dotyczących e-maili, stron internetowych i&nbsp;klasyfikacji PKD**. Trzy kreski pojawiały się dosłownie w&nbsp;każdym takim przypadku, więc nie dziwota, że jest ich tak wiele.

{:.bigspace}
<img src="/assets/posts/msig-problemy/pkd-mail-luki.jpg"/>

Być może w&nbsp;2018 roku komuś w&nbsp;końcu przestały podobać się kreski i&nbsp;ustawił problematycznym rubrykom jakiś numer. Większość luk wyparowała z&nbsp;dnia na dzień.

Ale nie zniknęły całkowicie; te, które zostały, są mniej konsekwentne.  
Czasem brakuje numeru lokalu (co akurat ma sens... tylko czemu po prostu go nie olać zamiast wypluwać trzy kreski?). Czasem nazwiska. Na razie nie dostrzegam w&nbsp;tym reguły.

# Zawieszenie spółek

W końcu, po tych wszystkich walkach z&nbsp;błędami, możemy wyłowić ciekawe informacje. Nie patrząc nawet na szczegóły z&nbsp;wnętrza wpisów, tylko na luki oraz numery działów.

Jak widzieliśmy, dział dla spółek zawieszonych rządzi się swoimi prawami.  
Gdyby ktoś chciał policzyć, ile spółek się zawiesiło, to nic by nie dało wyszukiwanie w&nbsp;pliku słów w&nbsp;stylu „zawieszenie”. Ono od dawna zwyczajnie się nie pojawia.

Zwrotem kluczowym dla poszukiwaczy jest zamiast tego „Dz. 6”.  
Bowiem, jak wspomniałem wyżej, rubryka z&nbsp;*trzema kreskami nicości* w&nbsp;połączeniu z&nbsp;numerem działu równym 6&nbsp;oznaczają zawieszenie lub wznowienie działalności. Zawsze.

Wiedząc o&nbsp;tym, można policzyć takie wpisy. I&nbsp;zobaczyć istotną zmianę w&nbsp;roku 2020.

{:.post-meta .bigspace}
Przypomnę, że Monitor dotyczy danych z&nbsp;KRS-u, czyli tylko spółek od jawnej wzwyż. Gdybyśmy chcieli patrzeć, jak zamykają się jednoosobowe działalności, musielibyśmy zajrzeć do CEIDG.

Nie wszystko to zawieszenia, ponieważ niekompletne wpisy dotyczą również wznowień. Natomiast myślę, że dość prawdziwa będzie teza: „w kwestii zawieszania i&nbsp;wznawiania zaczęło się dużo dziać”.

<div class="black-bg mono">
Rok 2011:  85<br/>
Rok 2012:  127<br/>
Rok 2013:  189<br/>
Rok 2014:  205<br/>
Rok 2015:  492<br/>
Rok 2016:  396<br/>
Rok 2017:  327<br/>
Rok 2018:  228<br/>
Rok 2019:  163<br/>
Rok 2020:  <span class="red">3809</span><br/>
Rok 2021:  <span class="red">7657</span><br/>
Rok 2022:  <span class="red">3681</span>
</div>

Średnia dla lat od 2011&nbsp;do 2019&nbsp;wynosi 245&nbsp;zawieszeń/wznowień na rok.  
W 2020&nbsp;mamy ich 3809, czyli **ponad 15&nbsp;razy więcej**. Jakby tego było mało, w&nbsp;2021 liczba wzrosła dwukrotnie. Miejmy nadzieję, że są wśród nich wznowienia!

A w&nbsp;tym roku? Według moich Monitorów już prawie dogoniliśmy stan z&nbsp;końca 2020. A&nbsp;przypominam, że nie jesteśmy nawet w&nbsp;połowie.

## Co dalej

Dzięki za wspólną podróż po meandrycznych drogach Monitora! Jej efektem jest komplet danych na temat firm, od roku&nbsp;2011 do teraz, zapisanych w&nbsp;jednoplikowej bazie danych. Co dalej?

Przede wszystkim chętnie podzieliłbym się skryptem, który pozwolił mi to wszystko przetworzyć i&nbsp;policzyć błędy.  
Ale pozwolę sobie chwilę z&nbsp;tym poczekać -- czuję, że jeszcze przyda się parę szlifów. A&nbsp;nie chcę robić jak CD Projekt i&nbsp;martwić się łataniem wszystkiego po fakcie :wink:

Poza tym, jak zobaczyliśmy w&nbsp;tym omówieniu, niektóre wpisy z&nbsp;Monitora są zwyczajnie puste. Dopóki ich nie uzupełnię informacjami z&nbsp;KRS-u, nie można mówić o&nbsp;kompletnych danych.

**Kolejny wpis będzie dotyczył wielkiej fuzji** -- połączenia skryptu od KRS-u (który jest w&nbsp;stanie wyciągać i&nbsp;wizualizować informacje, ale tylko wybrane) z&nbsp;tym od Monitora (który zbiera znacznie więcej, ale na razie nic z&nbsp;tym nie robi).

Przy okazji spojrzymy na jeden szczególnie wredny przypadek brakujących wpisów i&nbsp;spróbujemy się z&nbsp;nim uporać.

Do zobaczenia!

