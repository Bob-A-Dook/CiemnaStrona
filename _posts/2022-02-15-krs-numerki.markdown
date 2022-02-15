---
layout: post
title:  "28 numerków pana Macieja, czyli łańcuszek z KRS-u"
description: "Recykling spółek w praktyce."
subtitle: "Recykling spółek w praktyce."
date:   2022-02-15 01:23:00 +0100
tags: [Analiza danych, KRS, Polskie firmy]
category: krs-msig
category_readable: "Myszkowanie w Monitorze i kopanie w KRS-ie"
image: "krs-numerki/powiazania-oryginalne-nazwy.jpg"  
image-width: 1200  
image-height: 700
---

Witajcie w&nbsp;kolejnym odcinku serii poświęconej cudom i&nbsp;dziwom z&nbsp;Krajowego Rejestru Sądowego!

W poprzednim wpisie pokazywałem, jak zmieniały się w&nbsp;czasie właściwości wybranych firm.  
Moim źródłem informacji były odpisy z&nbsp;KRS-u -- publicznie dostępne pliki PDF zawierające ponumerowane zdarzenia z&nbsp;życia polskich spółek.  
Narzędziem do obróbki danych był z&nbsp;kolei autorski skrypt w&nbsp;języku Python.

Jak mawiają: „Kiedy dysponujesz jedynie młotkiem, wszystko wygląda jak gwóźdź”.  
Po stworzeniu skryptu miałem nową zabawkę i&nbsp;zero dalszych planów. Z&nbsp;ciekawości testowałem ją na wszelkich firmach, jakie mi przyszły do głowy.

Wiele z&nbsp;tych odkryć to materiał na luźne anegdotki, a&nbsp;nie poważniejszą analizę. „Nie uwierzysz, prezes Motoroli miał wpisane imię w&nbsp;polu na nazwisko!” i&nbsp;tym podobne rzeczy.

Natomiast, zupełnym przypadkiem, trafiłem na coś ciekawego.  
**Swoisty łańcuszek 28 firm założonych przez jednego prawnika i&nbsp;przekazanych później nowym właścicielom**. W&nbsp;tym znanym firmom, takim jak Allegro.

Ostudzę zapał: wątpię, żeby to była jakaś afera.

Będzie natomiast luźna eksploracja i&nbsp;zerknięcie za kulisy świata kancelarii i&nbsp;korporacji. Poza tym dodamy do swojego arsenału śledczego możliwość rysowania powiązań między firmami.

## Początki

Jak wspomniałem, wszystko zaczęło się od zbierania odpisów dla różnych zagranicznych firm. Zacząłem od Facebooka (już Mety), Google'a, Amazona, paru polskich gigantów.

Pomyślałem sobie: a&nbsp;może sprawdzę któregoś z&nbsp;bardziej dyskretnych, acz mocnych graczy?  
Jak Blackrock, zarządzający po cichu największymi środkami finansowymi na świecie?  
Albo Cloudflare, który jest obecnie jednym z&nbsp;filarów światowego internetu?

W ten sposób trafiłem na odpis dla firmy **Akamai**. Zajmującej się, mówiąc bardzo ogólnie, internetowym zapleczem dużych firm.

Powstały mi dla nich takie oto wykresy:

{:.bigspace}
<img src="/assets/posts/krs-numerki/lancuszek-firma-akamai.jpg" alt="Trzy wykresy ułożone jeden pod drugim pokazujące, jak zmieniały się w czasie różne aspekty obecnej firmy Akamai: nazwa, wspólnicy oraz zarząd. Jednego dnia zmieniły się wszystkie rzeczy; to miejsce oznaczono żółtą pionową kreską."/>

Celowo przyciąłem obrazek, bo ciekawi nas jedynie górna część.

{% include info.html
type="Uwaga"
text="Datą końcową jest 20.11.2021 r., ponieważ była datą aktualną w&nbsp;dniu, kiedy pobrałem wszystkie odpisy. Trochę mi zeszło przy tworzeniu tego wpisu :wink:"
%}

Najwyższy wykres pokazuje, jak zmieniały się nazwy spółki. 
Spójrzcie na miejsca oznaczone pionowymi żółtymi kreskami. Odpowiadają dacie 31.05.2011 r., miesiąc po założeniu spółki (wybaczcie słabą czytelność i&nbsp;nałożone daty).

Tego dnia wydarzyły się co najmniej trzy rzeczy, widoczne na moich wykresach:

* **Zmiana nazwy**.  
  Z&nbsp;*Veintiuno* na *Akamai Technologies Poland*.

* **Zmiana udziałowców**.  
  Wcześniej były dwie firmy, *Veinte* oraz *Diecinueve*. Zastąpił je holenderski oddział Akamaia.

* **Zmiana zarządu**.  
  Odszedł Maciej G., na jego miejsce weszła inna osoba.

Jeśli znacie hiszpański, to pewnie już coś zwróciło waszą uwagę. Ja nie znam, więc jeszcze niczego nie wyłapałem.

Byłem natomiast ciekaw, kim byli wcześniejsi udziałowcy Akamaia. Znalazłem w&nbsp;odpisie numer KRS dla *Diecinueve*, wpisałem go w&nbsp;oficjalną wyszukiwarkę (przy czym odkryłem, że zmienili nazwę na *Top Brand*), zrobiłem wykresy:

{:.bigspace}
<img src="/assets/posts/krs-numerki/lancuszek-firma-top-brand.jpg" alt="Trzy wykresy ułożone jeden pod drugim, podobnie jak wcześniej dla Akamaia. Widać że jednego dnia zmieniła się nazwa, wspólnicy i zarząd; to miejsce oznaczono żółtą pionową kreską."/>

Znowu zmiana wszystkiego naraz jednego dnia (22.12.2011&nbsp;r.). Znowu dwie firmy o&nbsp;dziwnych nazwach jako pierwsi udziałowcy i&nbsp;Maciej G. jako prezes!

Nazwy brzmiały nieco hiszpańsko, więc wpisałem niektóre z&nbsp;nich w&nbsp;DuckDuckGo. Okazało się, że **wszystkie firmy Macieja G. miały nazwy pochodzące od hiszpańskich liczb**.  
*Veintiuno* to 21 (zresztą fonetycznie lekko się kojarzy z&nbsp;*twenty one*). *Diecinueve* to 19. I&nbsp;tak dalej.

Co więcej, wszystkie później trafiły w&nbsp;ręce zewnętrznych właścicieli.  
Postanowiłem zobaczyć, jak daleko sięga ten łańcuszek.

## W&nbsp;głąb króliczej nory

Zasadniczym utrudnieniem był fakt, że **oficjalna wyszukiwarka KRS-u pozwala szukać tylko aktualnych nazw spółek**.

Z tego względu nic by mi nie dało wpisywanie po kolei hiszpańskich nazw. Wiele z&nbsp;tych firm, podobnie jak początkowe *Veintiuno*, ma już inne nazwy i&nbsp;po prostu by się nie pojawiły.   
Drugi problem: patrząc na odpisy, nie miałbym pewności, czy firma nie ma udziałów w&nbsp;czymś jeszcze innym (KRS pokazuje jedynie, kto ma udziały w niej).

Musiałem zatem połączyć źródła. Coś dokładniej pokazującego powiązania (padło na *Infoveriti.pl*) oraz oficjalną bazę KRS-u, z której brałbym pełne odpisy.

Moja metoda była mocno prowizoryczna. Naszykowałem sobie folder na odpisy z&nbsp;KRS-u, pod ręką miałem również skrypt do tworzenia wykresów. Dla każdego zdobytego odpisu:

* Używałem skryptu, żeby wyświetlić nazwy udziałowców;
* Wyszukiwałem te nazwy przez stronę *krs.infoveriti.pl*;
* Jeśli wyglądało na to, że to kolejna firma z&nbsp;łańcuszka, to kopiowałem jej numer KRS.

{:.bigspace}
<img src="/assets/posts/krs-numerki/krok-1-infoveriti.jpg" alt="Dwa zrzuty ekranu ustawione jeden pod drugim i pokazujące, że na stronie Infoveriti najpierw wpisałem Trece w pole wyszukiwarki, a potem skopiowałem numer KRS."/>

Następnie, już w&nbsp;oficjalnej wyszukiwarce KRS-u:

* Wyszukiwałem ten numer;
* Pobierałem pełen odpis.

{:.bigspace}
<img src="/assets/posts/krs-numerki/krok-2-wyszukiwarka-krs.jpg" alt="Trzy zrzuty ekranu ze strony KRS-u. Oznaczyłem na nich, co po kolei klikałem, żeby uzyskać odpis dla firmy o wyżej zdobytym numerze KRS."/>

I tak dalej. Po drodze okazało się, że same hiszpańskie liczby nie wystarczą, były również hiszpańskie nazwy zakończone dwójką. *Veintiuno 2*, *Diecinueve 2* i&nbsp;tak dalej.

Po drodze sprawdziłem też samego Macieja G. Według moich informacji pracował i&nbsp;-- jak podaje strona -- pracuje do teraz w&nbsp;pewnej kancelarii specjalizującej się w&nbsp;fuzjach i&nbsp;przejęciach, nazwijmy ją GWW.

Idąc wstecz, dotarłem do *Cinco* i&nbsp;*Cuatro*, które już nie trafiły do obcych firm, lecz zostały w&nbsp;rękach wspomnianej kancelarii GWW. Czyli wszystkie numerki zapewne zostały naszykowane na polecenie kancelarii, a&nbsp;pan Maciej działał w&nbsp;roli pełnomocnika. 

*Veintidós*, czyli 22, już nie znalazłem (również szukając według polskiej pisowni), zaś firmy nazwane jak wcześniejsze hiszpańskie liczby (*Uno*, *Dos*, *Tres*) wydawały się niezwiązane z&nbsp;kancelarią GWW.

W związku z&nbsp;tym, po zebraniu odpisów dla 28 firm, uznałem poszukiwania za zakończone.

## Rezultat i wnioski

Po zebraniu wszystkich odpisów pozostała odrobina grzebania przy skrypcie. Musiałem dodać możliwość tworzenia grafu, co jednak okazało się zadziwiająco łatwe, gdy poczytałem o&nbsp;języku DOT.  
Wystarczy w&nbsp;nim jedynie wskazać, co się łączy z&nbsp;czym (czyli: jaka firma ma udziały w&nbsp;innej firmie). A&nbsp;układaniem grafu już się zajmuje za kulisami komputer.

Po paru szlifach wypluło mi taki graf. Przyznacie że ładny? :sunglasses:

{:.bigspace}
<img src="/assets/posts/krs-numerki/powiazania-oryginalne-nazwy.svg" alt="Spory graf pokazujący 28 elips z nazwami firm. Są ze sobą połączone w ten sposób, że od każdych dwóch firm poza najniższymi odchodzą strzałki łączące je z którąś z firm pod nimi. Kształt przypomina dwa łańcuchy albo warkocze odchodzące od dwóch firm u szczytu. Graf jest utrzymany w kolorach Ciemnej Strony."/>

Wewnątrz elips mamy podane nazwy firm, a&nbsp;w nawiasach pod spodem ich numery KRS. Jeśli od firmy A&nbsp;odchodzi strzałka w&nbsp;stronę firmy B, to znaczy że firma A&nbsp;ma w&nbsp;firmie B&nbsp;udziały (czyt. jest w&nbsp;niej wspólnikiem).  
Wszystkie numerki to spółki z&nbsp;o.o., więc dla czytelności pominąłem ten element.

# Interpretacja

Po zobaczeniu tego wszystkiego można się zastanowić: po co? *Komu to potrzebne?*{:.corr-del} Czemu to miało służyć?

Gdybym był dziennikarzem, to bym zapewne wysłał z&nbsp;ciekawości grzeczne maile. Ale jestem blogerem-piwniczakiem, więc zamiast tego spróbuję sam pomyśleć na głos.  
Zastrzegam, że w&nbsp;kwestii firm jestem nieoczytanym neandertalczykiem, acz starającym się myśleć logicznie.

Przede wszystkim zakładam, że Maciej G. działał w&nbsp;imieniu kancelarii, a&nbsp;nie tak po prostu sobie założył 28&nbsp;firm. To jednak kosztowna sprawa -- według [Kodeksu Spółek Handlowych](https://lexlege.pl/ksh/art-154/) minimalny wkład to 5000&nbsp;zł na jedną spółkę.

Z tego samego powodu wątpię, żeby kancelaria założyła spółki, nie mając umówionych nabywców, i&nbsp;dopiero potem próbowała je komuś opchnąć. Raczej już mieli na papierze gwarancję, że po założeniu spółki klient ją od nich odbierze.

A jaki jest sens tej całej akcji?  
Być może to coś w&nbsp;rodzaju aklimatyzacji. Kancelaria zakłada firmę na siebie, a&nbsp;jej przyszły właściciel ma czas się we wszystkim zorientować, sprawdzić czy jest dobrze „wpięta” w&nbsp;system itp. 

Taki odpowiednik napisania posta albo tweeta z&nbsp;widocznością ustawioną na „Tylko ja”. Najpierw sobie zobaczymy, czy wszystko wygląda jak powinno. A&nbsp;jeśli tak, to zmieniamy widoczność na publiczną.

Kolejna sprawa: dlaczego akurat kształt przeplatanki, w&nbsp;której każda firma (poza tymi na początku i końcu) ma udziały w&nbsp;dwóch innych?

Do głowy przychodzi mi tylko to, że chcieli mieć ułatwione oddawanie spółek w&nbsp;cudze ręce.  
Przykładowo *Trece* i&nbsp;*Catorce* mają udziały w&nbsp;*Quince*. Jeśli jedną z&nbsp;nich odda się nowemu właścicielowi, to *Quince* nie zostanie bez wspólnika -- nadal będzie trzymane przez drugą spółkę (zachęcam do zerknięcia na graf).  
Trochę jak podczas przemierzania górskich ferrat: dla asekuracji ma się dwa karabinki, z&nbsp;czego w&nbsp;każdym momencie co najmniej jeden wpięty. 

Ale czemu w&nbsp;takim razie 28 spółek splecionych w&nbsp;warkocze zamiast 28&nbsp;całkiem odrębnych? Na to niestety nie mam odpowiedzi.

Oczywiście możliwe, że moje domysły są całkiem błędne, a&nbsp;cały pomysł z&nbsp;numerkami kancelaria sobie wymyśliła dla zabawy i&nbsp;urozmaicenia. Sam bym tak zrobił na ich miejscu.

# Dalsze losy numerków

Wróćmy na chwilę do punktu wyjścia. Zacząłem od tego, że Veintiuno zostało przekształcone w&nbsp;Akamai.

Dla formalności spójrzmy również, jak zmieniły się nazwy pozostałych numerków (po lewej stronie pierwotna nazwa, po prawej najbardziej aktualna w&nbsp;dniu tworzenia wpisu).

<div class="black-bg mono">
CINCO => GWW CAPITAL<br/>
CUATRO => PHN 7<br/>
NUEVE => EURO-DOM INWESTYCJE<br/>
NUEVE 2 => AIDIGIO<br/>
DIEZ => DOM-STYL DEVELOPMENT W&nbsp;UPADŁOŚCI LIKWIDACYJNEJ<br/>
DIEZ 2 => FOOD EKSPERT<br/>
<span class="red">ONCE => ONCE</span><br/>
ONCE 2 => PLUS TM GROUP<br/>
DOCE => ZDROWIE I<br/>
DOCE 2 => L&W MANAGEMENT W&nbsp;LIKWIDACJI<br/>
CATORCE => GALERIA KWADRAT<br/>
CATORCE 2 => SWGK MARKETING<br/>
<span class="red">TRECE => TRECE</span><br/>
<span class="red">TRECE 2 => TRECE 2</span><br/>
<span class="red">QUINCE => QUINCE</span><br/>
QUINCE 2 => AS INVEST<br/>
DIECISEIS => WIŚNIOWA GÓRA INWESTYCJE<br/>
<span class="red">DIECISEIS 2 => DIECISEIS 2</span><br/>
DIECIOCHO => "ALLEGRO GROUP"<br/>
DIECIOCHO 2 => IMMOBILIO<br/>
DIECISIETE => NETIA BRAND MANAGEMENT<br/>
DIECISIETE 2 => FIRMA SOCHA<br/>
<span class="red">"VEINTE" => "VEINTE"</span><br/>
"VEINTE 2" => GIANT INVEST<br/>
DIECINUEVE => TOP BRAND<br/>
DIECINUEVE 2 => ENERTON<br/>
VEINTIUNO => AKAMAI TECHNOLOGIES POLAND<br/>
VEITIUNO 2 => SĘPIA I<br/>
</div>

Widać w&nbsp;tych nazwach parę ciekawostek.

Na oko mamy tu firmy deweloperskie, paru znanych gigantów (Netia i&nbsp;Allegro) oraz trochę innych firm, o&nbsp;których musiałbym doczytać.

Jakby co to nie ja dorobiłem cudzysłowy w&nbsp;niektórych nazwach. Po prostu tak było w&nbsp;odpisach (na grafie je usunąłem, żeby nie szpeciły).  
Być może to inicjatywa własna osoby, która to wklepywała do systemu?

Kolejna sprawa: jedna literówka w&nbsp;nazwie spółki. Jest *Veitiuno&nbsp;2* zamiast _Vei**n**tiuno&nbsp;2_.

Poza tym widzimy, że niektóre numerki nie zmieniły swoich nazw (choć zawsze zmieniały właścicieli -- udziałowców). Oznaczyłem je osobnym kolorem.  
Te przypadki szczególnie mnie ciekawią. Ktoś, zakładam, odkupił od kancelarii specjalnie przygotowaną firmę, po czym tak po prostu ją sobie trzymał?

Jeśli nazwa się nie zmieniła, to dla porządku spójrzmy chociaż, kto został udziałowcem tych sześciu nietypowych numerków:

<div class="black-bg mono">
ONCE => "TUBEK" SPÓŁKA AKCYJNA<br/>
TRECE => Rodzina D. (osoby prywatne?)<br/>
TRECE 2 => Piotr W. i Marek T. (osoby prywatne?)<br/>
QUINCE => KORN (...) SPÓŁKA JAWNA, potem osoby prywatne<br/>
DIECISEIS 2 => TKM INVESTMENT SP. Z O.O.<br/>
VEINTE => "RYŁKO" SPÓŁKA Z O.O.<br/>
</div>

Z tych wszystkich nowych właścicieli kojarzę jedynie Ryłko -- to ci od butów.

Podsumowując: przyznam się, że nie końca rozumiem te wszystkie roszady.  
Ale przyjemnie się patrzy na to, że świat firm -- z&nbsp;pozoru pełen sztywniactwa i&nbsp;garniturków -- jest tak naprawdę świetną zabawą! Obejmującą zmiany nazw, układanie firm w&nbsp;dziwne kształty i&nbsp;tak dalej :smile:

# Firmy a&nbsp;teoria grafów

Od tej całej sprawy przyszło mi na myśl inne, nieco bardziej abstrakcyjne skojarzenie.

Nasz podwójny łańcuch ze spółek był bardzo charakterystyczny. Wystarczyło tylko dobrać odpowiednie kryterium (tu: patrzenie tylko na nazwy początkowe, a&nbsp;nie aktualne), żeby pojawił się w&nbsp;całej okazałości.

A czy byłby jakiś sposób na automatyczne wychwytywanie takich „ciekawych” kształtów?

Intuicja podpowiada mi, że owszem. Istnieje taka dziedzina jak **teoria grafów** -- ogólnie rzecz biorąc, zajmuje się połączeniami między różnymi rzeczami. Wszystko rozpatruje się jako wierzchołki (czyli stałe obiekty; tutaj np. firmy i&nbsp;osoby) oraz krawędzie (połączenia między wierzchołkami).

Tutaj przykład dla możliwych ustawień komputerów w&nbsp;sieci; tak zwanych topologii. Może istniałyby również „topologie firm”?

<img src="/assets/posts/krs-numerki/topologie-sieci.jpg" alt="Obrazek pokazuje tabelkę o&nbsp;bladozielonym tle. W&nbsp;jej komórkach znajduje się sześć różnych kształtów ułożonych z&nbsp;ikon symbolizujących urządzenia komputerowe."/>

{:.figcaption}
Źródło: [tommyc.prv.pl](http://tommyc.prv.pl/referat5.htm)

Do tego można dorzucić czas jako zmienną, żeby wyszły jeszcze ciekawsze rzeczy.  
Przykładowo nasz łańcuszek byłby grafem o&nbsp;28 wierzchołkach, który stopniowo się „rozrywał” w&nbsp;miarę oddawania kolejnych spółek nowym właścicielom.

Patrząc w&nbsp;taki sposób, moglibyśmy szufladkować skupiska firm jako określone kształty, a&nbsp;potem przeszukiwać bazę pod kątem takich kształtów.  
„Znajdź słońca, które z&nbsp;czasem się rozrastały”; „łańcuchy, przez które przesuwał się kapitał” itp.  
Być może odkryję w&nbsp;ten sposób Amerykę. Ale nie cel się liczy, tylko droga, a&nbsp;ta jest póki co bardzo przyjemna.

Tak czy siak takie eksperymenty wymagałyby zebrania informacji na temat szerszego firmowego ekosystemu, a&nbsp;nie tylko pobierania po jednym odpisie. Czytaj: to sprawa na kolejny wpis :wink:

## Bonus: nowy lepszy skrypt

Tworząc wpis, uaktualniłem przy okazji swój skrypt do obróbki plików z KRS-u. Teraz tworzy również grafy powiązań dla wszystkich odpisów z danego folderu :metal:

Sam skrypt można pobrać <a href="/assets/skrypty/krs_visualizer_v2.py" download>stąd</a>{:.internal}.  
Oprócz niego przyda się również [samouczek]({{site.url}}/tutorials/krs-wykresy){:.internal} pokazujący, jak z niego korzystać.

To na razie wersja mocno eksperymentalna, nie spodziewałbym się cudów.  
W najbliższym czasie dodam do samouczka opisy nowych funkcji dotyczących grafów.

