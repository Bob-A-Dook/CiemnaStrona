---
layout: post
title: "Internetowa inwigilacja plus 5 – historia przeglądania"
subtitle: "„Wiem, gdzie bywasz”"
description: "„Wiem, gdzie bywasz”"
date:   2023-08-19 21:22:00 +0100
tags: [Internet, Inwigilacja]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image:
  path: /assets/posts/inwigilacja/historia-przegladania/historia-przegladania-baner.jpg
  width: 1200
  height: 700
  alt: "Obraz pokazujący dolną komorę klepsydry częściowo zasłoniętą napisem Top Secret. Wysypują się z niej dwa strumienie piasku, niebieski i fioletowy, nad którymi widać linki do różnych stron w zbliżonych kolorach. W tle widać liczne patrzące oczy"
---

Niejedna osoba utonęła w&nbsp;odmętach internetu. Zaczęła przechodzić ze strony na stronę, trafiając w&nbsp;dziwne miejsca. Gdy potem, niczym w&nbsp;„Kac Vegas”, chce odtworzyć przebieg zdarzeń, może zawsze spojrzeć do swojej historii przeglądania.

To lista wszystkich odwiedzonych przez nas stron internetowych, wraz z&nbsp;dokładną datą i&nbsp;godziną odwiedzin. Sięga daty ostatniego czyszczenia. A&nbsp;że niektórzy w&nbsp;ogóle nie czyszczą historii... :wink:

Internet jest wszechobecny, więc historia przeglądania bywa częściową historią naszego życia!  
Ukazuje zmiany zainteresowań, szukanie prezentów, hobby. Wyszukiwania, które trudno by było wytłumaczyć policji (cóż... wciągnęła nas powieść kryminalna i&nbsp;chcieliśmy zweryfikować fakty).

Co w&nbsp;takim razie powiecie na to, że **losowe strony internetowe są w&nbsp;stanie poznać część tej historii**? Nawet gdy dotyczy stronek poza ich kontrolą? Potencjalnie wrażliwych?

Oficjalnie przeglądarka przed tym zabezpiecza... Ale niektórzy są naprawdę sprytni. Zapraszam na przegląd ich przebiegłych metod!

{% include info.html
type="Uwaga"
text="Uczciwie uprzedzam, że wiele metod z&nbsp;tego wpisu to raczej eksperymenty myślowe. Jest niewielka szansa, że spotkamy je na żywo.  
Prawie na pewno nie użyją ich większe korpo znane z&nbsp;inwigilacji. Za łatwe do wykrycia dla badaczy. Za duże ryzyko, jeśli do wykrycia dojdzie."
%}

## Spis treści

* [Bezpośrednie zaglądanie odpada](#bezpośrednie-zaglądanie-odpada)
* [Styl linków zdradza wszystko?](#styl-linków-zdradza-wszystko)
* [Sami się wkopujemy](#sami-się-wkopujemy)
  * [Linki jako test psychologiczny](#linki-jako-test-psychologiczny)
  * [Linki jako Captcha](#linki-jako-captcha)
  * [Linki jako asteroidy](#linki-jako-asteroidy)
  * [Linki w&nbsp;rzeczywistości wirtualnej?](#linki-wrzeczywistości-wirtualnej)
* [Jak się chronić](#jak-się-chronić)


## Bezpośrednie zaglądanie odpada

Zacznijmy od tego, że **strony internetowe nie są w&nbsp;stanie zajrzeć do historii oficjalną drogą**. Nie istnieje żadna komenda, którą mogłyby tak po prostu wysłać naszej przeglądarce.

„Przeglądarko, daj mi listę wszystkich stron, jakie odwiedziłaś w&nbsp;tym miesiącu”. Nie, to nie przejdzie. Nawet Chrome, który zwykle rozdaje nasze informacje na lewo i&nbsp;prawo, nas w&nbsp;tym przypadku ochroni.

Przykładowa strona A&nbsp;może natomiast gromadzić coś w rodzaju własnej historii. Listę jej własnych podstron (albo stron ściśle powiązanych), jakie odwiedziliśmy.

{% include info.html
type="Powiązane wątki"
text="To szczególnie łatwe, jeśli dostaliśmy od niej [pliki cookies](/internetowa_inwigilacja/2021/10/22/pliki-cookies){:.internal}. Są jak identyfikator albo dowód osobisty, który okazujemy stronom na życzenie.  
Ale nawet ich czyszczenie nie pomaga, bo w&nbsp;roli identyfikatora można użyć wielu innych informacji. Poświęciłem im zresztą większość serii „Internetowa inwigilacja”."
%}

W tym wpisie jednak nie skupimy się na takim przypadku, lecz na rzeczy groźniejszej. Zbieraniu (okrężną drogą) *historii dotyczącej innych stron*.  
W tym przypadku strona A&nbsp;się dowiaduje, że byliśmy na stronach B, C, D... Niezwiązanych z&nbsp;nią kompletnie.

## Styl linków zdradza wszystko?

Nasza przeglądarka oferuje nam pewne graficzne udogodnienie. Przydatne zwłaszcza wtedy, kiedy musimy odwiedzić większą liczbę linków (przykład: chcemy pobrać wszystkie pliki PDF z&nbsp;listy).

**Linki do stron, które już są w&nbsp;naszej historii, będą miały inny kolor niż pozostałe**. Prawie zawsze.

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/historia-przegladania/linki-odwiedzone-porownanie.jpg" alt="Dwa linki, jeden pod drugim. Mają postać podkreślonego tekstu. Pierwszy z&nbsp;nich ma treść 'Link nieodwiedzony' i&nbsp;jest niebieski. Drugi ma treść 'link odwiedzony' i&nbsp;jest fioletowy"/>

{:.figcaption}
Domyślny wygląd linków odwiedzonych i&nbsp;nieodwiedzonych.

{% include info.html
type="Uwaga"
text="Tutaj warto podkreślić -- link zaznaczy się jako odwiedzony tylko wtedy, gdy *dokładnie* jego odwiedzaliśmy.  
Załóżmy, że odwiedziliśmy bezpośrednio jakiś konkretny wpis z&nbsp;Ciemnej Strony. Bo ktoś go nam podlinkował. Ale nie byliśmy na stronie głównej.  
W tej sytuacji link do wpisu będzie widoczny jako odwiedzony. Ten do strony głównej nie zmieni wyglądu. Mimo że oba prowadzą do tej samej domeny (*ciemnastrona.com.pl*)."
%}


Możemy sobie pomyśleć, że to jakiś bajer wyłącznie na poziomie przeglądarki. Zna w&nbsp;końcu naszą historię. Może też dowolnie zmieniać elementy odwiedzanych stron. Więc po prostu zmienia kolor linków.  
Gdyby tak było, to wszystko OK. Zmiana byłaby widoczna tylko dla naszych oczu, a&nbsp;strony internetowe nie miałyby do tych informacji dostępu.

Tylko że **strony nie są tak całkiem pozbawione wpływu na linki. Mogą wpływać na ich wygląd**. Mówić przeglądarce: „Chcę, żeby wszystkie odwiedzone linki były u&nbsp;mnie czerwone, a&nbsp;nie niebieskie”. Co ma sens, bo pozwala dopasować ich wygląd do motywu kolorystycznego strony.

Od strony technicznej autorzy stron mogą to robić, ustawiając w&nbsp;arkuszach styli CSS (zwykle osobnych plikach) wartości pod tak zwanym [selektorem `:visited`](https://www.w3schools.com/cssref/sel_visited.php). Brzmi groźnie, wygląda prosto:

<div class="black-bg mono">
a:visited {<br/>
<span style="margin-left:20px">color: red;</span><br/>
}
</div>

{:.figcaption}
Jeśli dodamy coś takiego do arkusza CSS naszej strony, to naszym gościom wszystkie odwiedzone linki (elementy o&nbsp;nazwie `a`) będą barwiły się na czerwono.

### Zagrożenie

Skoro linki kliknięte się wyrożniają, posiadają inną wartość jakiejś rzeczy... To pojawia się potencjalne zagrożenie. 

Autor strony mógłby stworzyć ogromną listę wszelkich interesujących go linków. Do różnych stron -- światopoglądowych, medycznych, niegrzecznych. I&nbsp;umieścić ją na stronie, niewidoczną dla użytkowników. Taką niewidzialność też można łatwo ustawić przez arkusze styli.

Poza tym na stronie mógłby być interaktywny kod, JavaScript. I&nbsp;mógłby poprosić: „Przeglądarko. Daj mi te linki z&nbsp;listy, dla których `:visited` ma wartość True”.

Dostając je, dostałby listę odwiedzonych przez nas stron.

Wystarczyłoby, że raz odwiedzimy taką złowrogą stronę. Gdzieś poza naszym wzrokiem powstanie wielka lista tysięcy linków. Kod ustali, które z&nbsp;nich już zostały odwiedzone i&nbsp;wyśle te informacje swoim właścicielom.  
A my, nieświadomi, jeszcze trochę posurfujemy po sieci i&nbsp;pójdziemy spać. 

Brzmi groźnie? Ale na szczęście to tylko teoretyczne zagrożenie. **Przeglądarki nie dają stronom dostępu do wartości parametru `visited`**.

### Bardziej subtelna stylizacja

Twórca strony nie może zapytać wprost, czy dany link był odwiedzony. Ale może go stylizować. Gdyby mógł to robić bez ograniczeń, nadając linkom dowolne atrybuty, to mógłby łatwo uzyskać poszukiwane informacje.

Mógłby na przykład ustawić linkom odwiedzonym inny atrybut `margin`. Określając, na ile odsuwają od siebie inne elementy.

A potem umieściłby na stronie kod patrzący *nie na same linki, tylko na elementy sąsiednie*. Któryś jest przesunięty? To znaczy, że link obok niego został odwiedzony.

Ze względu na takie zagrożenie **możliwość stylizowania linków ograniczono do atrybutów, które nie wpływają na układ elementów sąsiadujących**. Czyli w&nbsp;praktyce do różnych [elementów kolorystycznych](https://www.w3schools.com/cssref/sel_visited.php):

* `color`,
* `background-color`,
* `border-color`,
* i&nbsp;paru innych.

Czy to dało nam bezpieczeństwo? Nie do końca.  
Całkiem niedawno, w&nbsp;2021 roku, pewien użytkownik zgłosił twórcom przeglądarki Chromium istotną lukę. Opierała się na [wykorzystaniu przejść kolorystycznych](https://bugs.chromium.org/p/chromium/issues/detail?id=1205981).

Linkom odwiedzonym i&nbsp;nieodwiedzonym nadano różne kolory (np. czerwony i&nbsp;pomarańczowy). Potem kazano wszystkim zrobić efekt przejścia do czerwieni. Tylko jeden ich rodzaj to robił. A&nbsp;kod obecny na stronie mógł to wyłapywać.

Tym niemniej, poza nielicznymi wpadkami przeglądarek -- obecnie trudno jest odczytać naszą historię poprzez wygląd linków. Zagrożenie ma wartość głównie muzealną.

Co nie znaczy, że ta historyczna wiedza jest bezużyteczna! Do teraz powstają nowe przeglądarki, budowane od podstaw. Współczesnym przykładem [Ladybird](https://awesomekling.github.io/Ladybird-a-new-cross-platform-browser-project/).   
Gdyby ich twórcy dziwili się, że nie można dowolnie stylizować linków i&nbsp;chcieli to zmienić... To znajomość historycznych zagrożeń pozwoliłaby ich przekonać, że te ograniczenia jednak mają swój sens.

Poza tym samej stylizacji nadal można nadużyć. Tyle że w&nbsp;jeszcze bardziej okrężny sposób. Ale zanim to omówię, poznajmy jeszcze jeden ważny fakt.

### Tekst linków można swobodnie zmieniać

Strona, do której prowadzi link, może być zupełnie inna niż tekst samego linku. Sam to często stosuję, również w&nbsp;tym wpisie. Wplatam linki w&nbsp;zwykły tekst. Tu na przykład mamy [stronę główną bloga](/).

Tekst pod moimi linkami zwykle składa się z polskich liter, czasem cyfr, rzadziej znaków specjalnych.  
Ale nie musi tak być. Zestaw dostępnych znaków jest olbrzymi i&nbsp;znajdziemy tam rzeczy, których byśmy się nie spodziewali.

Przykładem chociażby emoji. Kojarzą się z kolorowym obrazkiem... Ale niektóre z&nbsp;nich istnieją w&nbsp;postaci bardziej pierwotnej. Jako [tekst zrozumiały dla komputera](https://unicode.org/emoji/charts/full-emoji-list.html) (mamy je tutaj w&nbsp;kolumnie *Browser*; pozostałe kolumny to obrazki używane przez konkretne organizacje).

Tutaj mamy na przykład emotkę anioła... A&nbsp;zarazem kolejny link do mojej strony głównej: [😇](/).  
Ta emota **nie jest obrazkiem, lecz tekstem**. Znakiem o&nbsp;kodzie Unicode `U+1F607`.

W podobny sposób można ukrywać linki pod znakami wyglądającymi jak figury geometryczne. Na przykład prostokąty wypełnione jednolitym kolorem. Niektórzy użyli tego w&nbsp;praktyce.

## Sami się wkopujemy

Podsumujmy zebrane dotąd fakty:

* autor strony nie jest w&nbsp;stanie w&nbsp;żaden sposób odczytać, które linki pokazują się użytkownikowi jako kliknięte;
* ale jest w&nbsp;stanie wpływać na kolor tych linków oraz ich tekst;
* tekst linków może zawierać rzeczy spoza alfabetu, jak niektóre figury geometryczne.

Niektórzy wpadli w&nbsp;tym miejscu na iście szatańskie pomysły -- **postanowili sprawić, żeby użytkownicy sami wskazali, które strony z&nbsp;listy odwiedzili**. Żeby się wkopali.  
Toporny przykład:

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/historia-przegladania/naiwna-lista-odwiedzonych-stron.jpg" alt="Lista pięciu linków umieszczonych jeden pod drugim. Nad nimi widać polecenie 'Zaznacz fioletowe linki' oraz podtytuł 'Nie bój się, to całkiem bezpieczne'. Każdy z&nbsp;linków ma po swojej lewej stronie pole, które można kliknąć. Pierwszy i&nbsp;ostatni (do Ciemnej Strony i&nbsp;jednej z&nbsp;podstron Rejestr.io) są fioletowe, ponieważ były wcześniej odwiedzone"/>

{:.figcaption}
Prototyp listy do zbierania naszej historii.

Zapewne istnieją ludzie, którzy nawet w&nbsp;takim układzie zaznaczyliby odpowiednie linki i&nbsp;potwierdzili guzikiem :wink:
Ale niektórzy by się przestraszyli. Dlatego opracowano też warianty usypiające czujność.

Każdy z&nbsp;nich będzie za kulisami właśnie taką listą jak ta wyżej. Tylko że odpowiednio wystylizowaną i&nbsp;ubraną w&nbsp;jakąś wiarygodną historyjkę.

### Linki jako test psychologiczny

Ten przykład opracował niejaki [TinSnail](https://tinsnail.neocities.org/). Polega na tym, że użytkownikom wyświetla się ogromna siatka prostokątów. U&nbsp;góry widać prośbę o&nbsp;kliknięcie tych, które są czerwone.

Tylko że każdy prostokąt jest tak naprawdę *tekstem*. Pojedynczym znakiem ▇ ([`U+2587`](https://unicodeplus.com/U+2587)), wyglądającym jak zamalowany prostokąt. A&nbsp;pod nim ukrywa się link do jakiejś anglojęzycznej stronki, głównie z&nbsp;zakresu takich o&nbsp;programowaniu.

Do tego mamy regułkę w&nbsp;arkuszu CSS, mówiącą żeby linki odwiedzone kolorowało na czerwono. Efekt? Odwiedzone przez nas strony są ukryte pod czerwonymi prostokątami.  
U mnie na przykład jeden z&nbsp;nich odpowiadał stronie *news.ycombinator.com*. To HackerNews, forum które czytuję.

<img src="/assets/posts/inwigilacja/historia-przegladania/historia-przegladania-siatka-kulisy.jpg" alt="Trzy małe fragmenty zrzutów ekranu. Pierwszy pokazuje fragment arkusza CSS i&nbsp;ustawiony kolor czerwony dla odwiedzonych linków. Drugi pokazuje linki, jeden pod drugim, z&nbsp;których każdy ma jako tekst pojedynczy znak wypełnionego prostokąta. Ostatni pokazuje, jak to wygląda na stronie"/>

{:.figcaption}
Trzy oblicza strony TinSnaila -- arkusz CSS nadający kolor odwiedzonym linkom. Linki jako prostokąty w&nbsp;kodzie HTML. I&nbsp;wygląd dla użytkowników.

Za każdym razem, kiedy klikniemy któryś z&nbsp;linków, zapisuje to sobie kod JavaScript obecny na stronie. W&nbsp;ten sposób poznaje naszą historię przeglądania. Od nas samych.

Nie mógłby wprost zapytać przeglądarki: „które prostokąty są czerwone?” (bo ta, jak pisałem, nie ujawnia wartości `visited`).  
Natomiast „które prostokąty kliknął użytkownik?”. To już mu wolno. Efekt taki sam.

### Linki jako Captcha

Ten przykład znajdziemy na stronce [*varun.ch*](https://varun.ch/history). Oprócz tego warto zerknąć na [dyskusję](https://news.ycombinator.com/item?id=36949988) z&nbsp;tego roku na forum HackerNews.

Metoda jest podobna do tej od TinSnaila. Tylko że nie wyświetla ogromnej siatki, lecz mniejszą liczbę pól. Prosi o&nbsp;kliknięcie tych kolorowych, komunikatem bardzo w&nbsp;stylu typowej Captchy.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/historia-przegladania/varun-ch-captcha-historia.jpg" alt="Zrzut ekranu pokazujący na niebieskim tle napis (po angielsku): 'Czy jesteś robotem? Wybierz czarne pola, żeby przejść dalej'. Niżej widać siatkę 16&nbsp;białych lub czarnych kwadratów" width="50%"/>

Sprytnym pomysłem jest też dodanie w&nbsp;niektórych miejscach paru *pól kontrolnych*. Są kolorowe -- a&nbsp;kod strony o&nbsp;tym wie i&nbsp;tego pilnuje. Jeśli użytkownik ich nie kliknie, to wyświetli się informacja, że nie rozwiązał Captchy. Pozwala to uwiarygodnić cały pomysł.

Mała liczba pól z&nbsp;jednej strony zwiększa wiarygodność, ale też spowalnia gromadzenie danych. W&nbsp;ten sposób nie pozna się czyjejś historii od razu.

### Linki jako asteroidy

W jaki sposób poznać więcej odwiedzonych stron, a&nbsp;jednocześnie nie odstraszać użytkownika wielką szachownicą? Można zrobić coś dynamicznego, angażującego. I&nbsp;podsuwać linki na bieżąco!

Pewien autor stworzył [interaktywną grę typu *space shooter*](https://lcamtuf.blogspot.com/2013/05/some-harmless-old-fashioned-fun-with-css.html). Oficjalnie chodzi w&nbsp;niej o&nbsp;strzelanie do asteroidów.

W tym wypadku linki są wystylizowane na kółka. Linki nieodwiedzone zlewają się z tłem. Odwiedzone mają inny kolor, wyróżniający się na czarnym tle. Kod JavaScript porusza nimi wszystkimi po ekranie.

A ludzie klikają te kolorowe, ochoczo w&nbsp;ten sposób donosząc, co się kryje w&nbsp;ich historii.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/historia-przegladania/asteroidy-wiele.jpg" alt="Zrzut ekranu pokazujący czarne tło i&nbsp;widoczne na nim zamalowane, kolorowe koła. U&nbsp;góry widać punktację oraz polecenie każące bronić naszego statku kosmicznego." width="70%"/>

Podobnie jak przy Captchy, tak i&nbsp;tutaj mamy trochę asteroidów kontrolnych (niebędących linkami). Naprawdę nas zniszczą, jeśli się ich nie kliknie.

Ale w&nbsp;drugą stronę to nie działa. Gdybyśmy klikali w&nbsp;ciemno, pustą przestrzeń, to nabijemy sobie linków, których w&nbsp;historii nie mamy. A&nbsp;strona nie ma jak tego sprawdzić. Bo, pamiętajmy, nie ma bezpośredniego wglądu do wartości `visible`.

### Linki w&nbsp;rzeczywistości wirtualnej?

Tutaj akurat mój czysto teoretyczny pomysł, motywowany tymi powyższymi.

Wyobraźmy sobie, że rozwinęły się i&nbsp;spopularyzowały strony wspierające VR (rzeczywistość wirtualną). Użytkownik, z&nbsp;goglami na oczach, postrzega je jako trójwymiarową przestrzeń wokół siebie.

Gdyby takie strony miały dostęp do informacji o&nbsp;tym, na czym skupia się wzrok użytkownika, to mogłyby jej nadużyć. I&nbsp;co pewien czas wsuwać jakiś link w&nbsp;jego pole widzenia.

Linki nieodwiedzone byłyby niewidzialne. A&nbsp;odwiedzone -- jaskrawe.  
Nagłe pojawienie się czegoś takiego sprawi, że użytkownik odruchowo ucieknie wzrokiem w&nbsp;konkretną stronę. A&nbsp;strona internetowa dostanie tę informację i&nbsp;sobie zapisze, że znalazła link z&nbsp;historii przeglądania.

VR ogólnie wydaje się kopalnią danych biometrycznych i&nbsp;zagrożeniem dla prywatności. Historia przeglądania byłaby jak pojedyncza cegiełka w&nbsp;Wielkim *Bracie*{:.corr-del} Murze.

## Jak się chronić

Jak wspomniałem na początku, to zagrożenie jest akurat średnio realne i&nbsp;nie ma potrzeby się nakręcać. Na pewno nie zrobią tego większe firmy, bo za duże ryzyko. Być może mogłoby czegoś takiego próbować lokalne forum jakiejś sekty (żeby ustalić, że członkowie nie wchodzili na coś z&nbsp;indeksu stron zakazanych).

Najlepiej unikać sekt! Ale jeśli już trafimy na sytuację, gdy mamy dwie tożsamości, których wolimy nie mieszać... Dobrze mieć od każdej z&nbsp;nich całkiem osobną przeglądarkę. To ochroni nas przed stronami gapiącymi się w historię.

{:.post-meta .bigspace-after}
A w ogólniejszym przypadku -- najlepiej, żeby każda z tych przeglądarek korzystała z osobnej sieci/hotspota. Jeszcze lepiej -- mieć je na osobnych urządzeniach. Im pełniejsze rozdzielenie tożsamości, tym lepiej.

Poza tym dobrą praktyką jest **częste czyszczenie historii przeglądania**.  
Nawet gdyby strony wyświetliły nam różne ukryte linki do kliknięcia... To ich nie zobaczymy. Wszystkie będą miały ten sam kolor. Bo wszystkie będą nieobecne w historii.

### Dla twórców przeglądarek

Gdyby ktoś tworzył nową przeglądarkę, to możemy zrobić jej mały audyt i&nbsp;zobaczyć, czy możliwość stylizowania linków nie wykracza przypadkiem poza kolory. Jeśli tak, to można zgłosić potencjalne zagrożenie.

Najfajniej, gdyby przeglądarki miały od kolorowania linków całkiem osobny kod niż ten od ogólnego CSS-a.  
W&nbsp;ten sposób minimalizowałyby ryzyko, że wejdzie jakaś nowinka stylistyczna (patrz: przejścia kolorystyczne, opisane wyżej), a&nbsp;zagrożenie sprzed lat powróci.

Niektóre przeglądarki pozwalają wyłączać kolorowanie linków. To też fajna opcja, jeśli nie boimy się zmian ustawień.

W przypadku **Firefoksa** wpisujemy w&nbsp;górny pasek adresu `about:config`. Czytamy ostrzeżenie. Następnie znajdujemy opcję `layout.css.visited_links_enabled` (wystarczy wpisać początek nazwy).  
Zmieniamy jej wartość na `False`. Wszystkie linki staną się takie same. I&nbsp;dla nas, i&nbsp;dla potencjalnych podglądaczy.

### Dla autorów stron

Nie mamy wpływu na to, jak linki do naszej strony wyświetlają się na stronach cudzych... Ale możemy sprawić, żeby same linki do naszych podstron, obecne w&nbsp;historii naszych gości, nie były dla nich powodem do wstydu.

Pomoże to nie tylko przeciw karkołomnym przykładom z&nbsp;tego wpisu. Ale również w sytuacji, kiedy jakaś osoba fizycznie zerka im do historii.

W tym celu można stosować **dynamiczne ładowanie elementów**. Link do strony zawsze pozostanie ten sam i&nbsp;niewiele ujawni. Ale użytkownicy, klikając różne rzeczy na naszej stronie (albo ją przewijając), będą dostawali od nas treść.

Przykładowo taki Facebook ładuje dynamicznie stronę główną. Gdyby patrzeć na samą historię, to cały czas widzielibyśmy *www.facebook.com* (w&nbsp;wersji na komputery). W&nbsp;rzeczywistości ktoś mógł długo siedzieć na stronie i&nbsp;czytać najróżniejsze rzeczy. Od poczciwych po wywrotowe.

{% include info.html
type="Uwaga"
text="Gdybyśmy na poważnie myśleli o&nbsp;ochronie czytelników przed kimś, kto gapi im się w&nbsp;historię (ale nie ma np. opcji wpuszczenia wirusa do komputera), to warto pomyśleć również o&nbsp;obrazkach. Wścibskie osoby mogą je [wyciągać z&nbsp;pamięci podręcznej](/2021/12/24/caching){:.internal}, jak dokumenty ze śmietnika.  
Jeśli mamy na stronie jakiś obrazek, który pojawia się tylko przy bardziej kontrowersyjnych treściach, to sama jego obecność w&nbsp;pamięci wzbudzi podejrzenia.  
Lepiej ustawić, żeby go nie zapisywało do *cache'a*. Albo powielić w&nbsp;innych, neutralnych sekcjach naszej strony. Albo w&nbsp;ogóle go nie serwować."
%}

Na tych poradach kończę wpis. Wyczyśćcie teraz historię, żeby nikt się nie dowiedział, że go czytaliście :smile:

