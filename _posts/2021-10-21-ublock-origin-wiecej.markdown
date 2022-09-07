---
layout: post
title: Korzystanie z uBlock Origin
subtitle: "Opanowujemy naszą tarczę."
description: "Opanowujemy naszą tarczę"
date:   2021-10-21 12:10:00 +0100
tags: [Internet, Inwigilacja, Porady]
image: 
   path: /assets/posts/ublock-origin/google-vs-ublock-origin.jpg
   width: 1200
   height: 700

image-width: 900
image-height: 669
---

Witajcie w&nbsp;rozwinięciu [krótkiego wpisu]({% post_url 2021-10-21-ublock-origin %}){:.internal} pokazującego jak zainstalować uBlock Origin -- moim zdaniem **najważniejsze narzędzie do blokowania elementów śledzących**, obecnych na wielu stronach internetowych.

Jeśli jeszcze go nie pobraliście (bo np. macie wątpliwości, których skrócony wpis nie rozwiał), to teraz mam większą szansę Was przekonać.  
A jeśli już go macie, to teraz dowiecie się o&nbsp;nim czegoś więcej.

Zacznijmy od wyjaśnienia potencjalnych wątpliwości.

## Ogólnie o&nbsp;uBlock Origin

# Czy używając go, nie szkodzę drobnym twórcom?

Jak by na to nie patrzeć, uBlock Origin blokuje reklamy. Nie brak w&nbsp;internecie opinii w&nbsp;stylu:

{:.bigspace}
> Blokując reklamy, odbierasz środki do życia ludziom zarabiającym na swojej pasji \[niszowym blogerom itp.\]

Cóż za podłość z&nbsp;mojej strony! :smiling_imp:

Ale czy na pewno?

Zacznijmy od tego, że współczesna „reklama” to nie tylko obrazki wyświetlane na stronie czy linki do sponsorów.  
Gdyby chodziło tylko o&nbsp;to, osobiście nie byłbym im przeciwny (chociaż rozumiem też osoby, które mają serdecznie dość komerchy jako takiej).

W rzeczywistości obrazki to często jedynie wierzchołek góry lodowej. Za nimi ukrywają się skrypty profilujące i&nbsp;całe wielkie, automatyczne systemy reklamowe. Biznes nazywany z&nbsp;angielska *ad tech*.

**„Reklama” to zwykle kod, nad którym właściciele stron nie mają kontroli**. Oni tylko zawierają szablonową umowę, zgodnie z&nbsp;którą udostępniają kawałek swojej strony -- jak billboard. Zaś cały kod jest pobierany z&nbsp;zewnątrz, od jakiegoś dużego reklamodawcy.
  
Ten kod próbuje nas profilować. Zidentyfikować nas po zestawie informacji (nieraz subtelnych, jak cechy karty graficznej) i&nbsp;znaleźć w&nbsp;bazie firmy reklamowej. Sprawdzić, do jakich kategorii jesteśmy przypisani.

Obrazek, wybrany na podstawie tych informacji, wyświetla się dopiero na końcu.

{% include info.html type="Podobne wpisy" text="O informacjach składających się na nasz internetowy odcisk palca piszę więcej w&nbsp;swojej serii, [„Internetowej inwigilacji”](/serie/internetowa_inwigilacja/){:.internal}." %}

W takim układzie kod i&nbsp;obrazek są nierozłączne -- **nie da się zablokować śledzenia, pozostawiając sam obrazek**. Chcąc nie chcąc, musimy ciąć szeroko.

Drobni blogerzy i&nbsp;właściciele stron, gdyby chcieli, mogliby znaleźć inny model zarobkowy.  
Dogadać się z&nbsp;firmami z&nbsp;podobnej branży i&nbsp;umieszczać u&nbsp;siebie zdjęcia ich produktów, bez żadnego kodu.  
Napisać czasem (odpowiednio oznaczony) artykuł sponsorowany.  
Dodać link do bezpośrednich wpłat na swoje konto.

Pomysłów jest multum. Niestety wielu wybrało najłatwiejszą opcję i&nbsp;podpięcie się pod globalne sieci reklamowe.  
Niekoniecznie zyskują na tym „partnerstwie”. Elementy reklamowe zbierają informacje o&nbsp;użytkownikach **nawet jeśli ich nie klikniemy** (a zatem i&nbsp;tak nie przyniesiemy zarobków właścicielom stron).

Jeśli po internecie będzie chodziło wystarczająco wiele osób ze skutecznymi *ad blockerami*, to w&nbsp;świat pójdzie jasny sygnał, że warto zmienić model biznesowy.

Kto wie, może by to wyszło większości na dobre?  
Proste reklamy obrazkowe na stronach, dopasowane do ich tematyki, mogłyby się okazać skuteczniejsze niż te profilujące.  
A pustkę po firmach *ad techowych* mogłyby wypełnić na przykład portale „swatające” właścicieli stron z&nbsp;reklamodawcami.

Dlatego proponuję pozbyć się wahań natury etycznej. Chodząc po internecie z&nbsp;*ad blockerami*, **nie uderzamy w&nbsp;blogerów -- uderzamy w&nbsp;reklamowych gigantów**, którzy mają na swoim koncie liczne szemrane działania. I&nbsp;delikatnie sugerujemy, że warto zmienić system.

No i&nbsp;wreszcie: jeśli jakichś twórców szczególnie lubimy i&nbsp;chcemy widzieć ich reklamy (mimo że nas śledzą), to można łatwo wyłączyć uBO dla wybranych stron. Opisuję to w&nbsp;dalszej części wpisu.

Na tym kończę rozważania etyczne. Jeśli ktoś ma stanowcze, przeciwstawne poglądy na ten temat, to i&nbsp;tak byśmy się nawzajem nie przekonali.

# Czy to bezpieczne?

Nic nie jest w&nbsp;100% pewne, a&nbsp;każdy dodatek do przeglądarki mógłby zostać użyty w&nbsp;złych celach.

Kilka argumentów na korzyść uBO podawałem w&nbsp;krótszej wersji wpisu. Dla przypomnienia:

* ma otwarty kod źródłowy  
(każdy (kto umie w&nbsp;JavaScript) może zweryfikować, czy w&nbsp;programie nie ma czegoś złośliwego);
* [dodatkowa weryfikacja](https://support.mozilla.org/kb/recommended-extensions-program) przez Mozillę, dopuszczającą do mobilnego Firefoksa tylko wybrane dodatki;
* pozwolenia, o&nbsp;jakie prosi dodatek podczas instalacji, są wyjaśnione [na jego stronie](https://github.com/gorhill/uBlock/wiki/Permissions) (a&nbsp;wyjaśnienia brzmią logicznie).

Pytanie, czy to wystarczy. Czasem coś, co brzmi ładnie i&nbsp;ma wielu użytkowników, też potrafi wywijać numery.

Jak choćby popularne AdBlock czy AdblockPlus, które mają swój program *Acceptable Ads*. Który sprowadza się do tego, że reklamodawcy mogą dać twórcom w&nbsp;łapkę, a&nbsp;ci w&nbsp;podzięce wyłączają blokowanie ich reklam.

**Zdarzały się też przypadki, gdy popularny dodatek do przeglądarki został odkupiony od twórcy i&nbsp;„wzbogacony” o&nbsp;niepożądane rzeczy**.

{:.figure}
<img src="/assets/posts/ublock-origin/evil-adblocks.jpg" alt="Obrazek pokazujący wiele postaci ubranych w szaty z kapturami i robiących niepokojące wrażenie. Postacie z tyłu mają maski podobne do czaszek, a na twarze czterech z przodu nałożono loga różnych ad blockerów."/>

{:.figcaption}
Źródło obrazków: manga *Tokyo Ghoul*, rozdział&nbsp;77.  
(Ta pierwsza, o&nbsp;drugiej wolę zapomnieć).  
Przeróbki moje.

Żeby daleko nie szukać: podobny los spotkał zarówno poprzednika, jak i&nbsp;następcę uBO. Ale bez obaw! Te dwie historie pozwolą nam jeszcze bardziej docenić samego Origina.

Poprzednikiem był uBlock (bez *Origin*). Został stworzony przez tego samego autora co uBO, Raymonda Hilla.

Hill, z&nbsp;braku czasu, postanowił w&nbsp;pewnym momencie przekazać stery projektu innej osobie, Chrisowi&nbsp;A.  
Niestety nie nacieszył się odpoczynkiem. Jego następca podjął sporo [kontrowersyjnych decyzji](http://tuxdiary.com/2015/06/14/ublock-origin/), wyglądających na autopromocję i&nbsp;próby zmonetyzowania dodatku.

Rozgoryczony Hill wrócił zatem do gry i&nbsp;rozpoczął nowy projekt, którym był właśnie uBlock Origin. Na swojej stronie umieścił adnotację, że **nie przyjmuje żadnych wpłat**, a&nbsp;chętni mogą wesprzeć kogoś innego -- twórców list znanych elementów śledzących, „dzięki którym uBO istnieje”.

A co się stało z&nbsp;pierwotnym uBlockiem? Został wykupiony przez AdBlocka i&nbsp;włączony do programu *Acceptable Ads*, przez co kompletnie stracił pazurki.

Stary uBlock wygrał na tym pieniężnie, ale to Origin zjednał sobie użytkowników.

{% include info.html
type="Ciekawostka"
text="Jeśli zainstalujecie uBlock Origin i&nbsp;spróbujecie odwiedzić stronę tego poprzedniego uBlocka ([tutaj](http://www.ublock.org/)) to wyskoczy Wam ostrzeżenie, że Wasz dodatek ją zablokował.  
Pewien dowód na to, że panowie od uB i&nbsp;uBO mają ze sobą na pieńku :wink:"
%}

Z kolei „następcą” uBO mógł być Nano Defender i&nbsp;inne dodatki z&nbsp;serii Nano. Stworzone przez inną osobę (nick *jspenguin2017*) na bazie otwartego kodu uBO, ale rozszerzone o&nbsp;inne bajery.

Niestety pewnego razu grupa nieznanych, acz sympatycznych osobników zaproponowała *jspenguinowi*, że odkupią od niego dodatek.  
Autor się zgodził, nie ostrzegając użytkowników, a&nbsp;nowi właściciele rozbudowali Nano o&nbsp;funkcje ukradkiem śledzące aktywność.

{:.figure .bigspace}
<img src="/assets/posts/ublock-origin/walka-adblockow-1.jpg" alt="Przerobiony kadr z&nbsp;mangi pokazujący jedną postać walczącą z&nbsp;trzema innymi i&nbsp;właśnie powalającą jedną z&nbsp;nich. Na twarz samotnej postaci nałożono logo uBlock Origin, a&nbsp;na twarze pozostałych loga innych dodatków: AdBlock Plus, starego uBlocka oraz Nano Defendera."/>

Za całą sytuację *jspenguin* zaczął zbierać srogie baty na forum publicznym.  
Do dyskusji, pod nickiem *gorhill*, w&nbsp;pewnym momencie [włączył się](https://github.com/jspenguin2017/Snippets/issues/2#issuecomment-709988018) Raymond Hill od uBO.

Analizował krok po kroku zmiany wprowadzone w&nbsp;kodzie i&nbsp;doszedł do wniosku, że to coś złośliwego.  
Poświęcił na to czas i&nbsp;wysiłek. Mimo że nie ponosił żadnej winy za to, jak ktoś inny wykorzystał jego publicznie dostępny kod.

Obie sytuacje -- ze starym uBlockiem i&nbsp;Nano -- pokazują pewne strony autora uBO, które szanuję.  
Ktoś z&nbsp;silnym poczuciem odpowiedzialności za swoje dzieło. Dbający o&nbsp;reputację. Zmotywowany czymś innym niż pieniądze.

Oczywiście ludzie się zmieniają, więc nie traktujmy tego jak gwarancji. Ale na chwilę obecną **postać autora możemy policzyć na plus uBO -- raczej łatwo go nie podkupią** :+1:

Podsumowując: z&nbsp;uBO jest jak z&nbsp;wieloma innymi rzeczami w&nbsp;życiu. Nie ufajmy w&nbsp;ciemno, warto przed instalacją się upewnić (np. wyszukać jego nazwę i&nbsp;spojrzeć, czy nie ma jakiegoś skandalu).  
Ale póki co jest po prostu najlepszą opcją.

{:.bigspace}
<img src="/assets/posts/ublock-origin/walka-adblockow-2.jpg" alt="Przerobiony kadr z&nbsp;mangi pokazujący trzy postacie. Dwie z&nbsp;nich, na które nałożono loga starego uBlocka i&nbsp;Nano Defendera, właśnie upadły na ziemię. Trzecia postać, zwycięska, stoi pośrodku, plecami do czytelników, i&nbsp;trzyma w&nbsp;rękach dwa miecze. Na jej twarz nałożone jest logo uBlock Origin."/>

{:.post-meta}
Jeśli bardzo nie lubicie firm od reklamy internetowej -- i&nbsp;jesteście w&nbsp;stanie zainstalować dodatek spoza oficjalnego źródła -- to możecie rozważyć też [Ad&nbsp;Nauseam](https://adnauseam.io/), na bazie uBO. Zbanowany przez Google'a.

## Różne funkcje uBlock Origin

Po instalacji można całkiem zapomnieć o&nbsp;dodatku i&nbsp;pozwolić mu po prostu blokować *trackery* w&nbsp;tle.

Ale jeśli jesteśmy gotowi na kliknięcie paru pstryczków, to możemy jeszcze bardziej umilić sobie żeglugę po spienionych wodach internetu.

Zapraszam do krótkiego samouczka!

# Podstawowe informacje

Po zainstalowaniu dodatku znajdziemy go na górnym pasku, w&nbsp;prawym rogu.

A jeśli się tam nie pojawia, to po wejściu w&nbsp;menu, zakładkę `Dodatki` i&nbsp;znalezieniu jego ikony możemy go kliknąć prawym przyciskiem. Powinna pojawić się opcja *Przypnij do paska* lub coś w&nbsp;tym stylu.

Gdy już na nasz pasek trafi jego ikonka (<img height="16px" style="display:inline-block" src="/assets/posts/ublock-origin/ubo-ikona.jpg" alt="Ikonka uBlock Origin"/>), to możemy ją klikać, żeby wyświetlić główne menu programu:

{:.figure .bigspace}
<img src="/assets/posts/ublock-origin/ubo-interfejs.jpg" alt="Zrzut ekranu pokazujący menu główne uBlock Origin. Przy kilku przyciskach nałożono czerwone cyfry od 1 do 5."/>

Opcje w&nbsp;górnej części menu to pstryczki, które pozwalają włączać i&nbsp;wyłączać różne funkcje.

Po takich zmianach zwykle trzeba odświeżyć stronę. Dla ułatwienia uBO wyświetla wtedy po prawej stronie menu wielki przycisk. Gdy w&nbsp;niego klikniemy, to strona się odświeży i&nbsp;zobaczymy efekt nowych ustawień.

Sam nie korzystam ze wszystkich funkcji. Na obrazku oznaczyłem te z&nbsp;nich, które stosuję najczęściej i&nbsp;które omówię tu dokładniej.

# 1. Włączanie i&nbsp;wyłączanie

Klikając największą ikonę, możemy **całkiem wyłączyć uBlock Origin dla aktualnie przeglądanej strony**.

Ta opcja się przydaje, jeśli trafimy na strony, które wyjątkowo nie współgrają z&nbsp;naszym dodatkiem. Na przykład wykrywają go i&nbsp;nie chcą się załadować; to przypadek skrajny, ale możliwy.

Można jej użyć również w&nbsp;przypadku stron zaufanych, które jesteśmy gotowi przyjąć w&nbsp;oryginalnej postaci.

# 2. Blokowanie dużych elementów

Jedną z&nbsp;wad współczesnego internetu jest to, że wielu autorów stron nie liczy się z&nbsp;ograniczeniami.  
Mają na komputerze duże, wielomegabajtowe zdjęcia? Po prostu wrzucają je na swoje strony, niczego nie kompresując. „Mam szybkie łącze, u&nbsp;mnie działa”.

Takie marnotrawstwo może być dla nas bolesne, szczególnie jeśli korzystamy z&nbsp;internetu mobilnego i&nbsp;możemy odebrać tylko ograniczoną ilość danych.

W takiej sytuacji z&nbsp;pomocą przychodzi funkcja blokowania dużych elementów w&nbsp;uBO. **Jeśli jakiś element będzie „ważył” więcej kB niż ustalona wartość, to nie zostanie pobrany**. Zamiast niego wyświetli się czerwona ramka (i ewentualnie tekst alternatywny).

Maksymalną dopuszczalną wielkość możemy zmieniać w&nbsp;ustawieniach (opcja obok cyfry&nbsp;`5`).  
Osobiście ustawiłem tam 300&nbsp;kB. Dla porównania: na Ciemnej Stronie jeden z&nbsp;większych banerów ([ten z&nbsp;wpisu o&nbsp;bankach](/assets/posts/bank-ochrona/bank-sejf.jpg)) waży nieco ponad 130&nbsp;kB.

{% include info.html type="Ciekawostka"
text="W przypadku Facebooka tekstem alternatywnym są automatyczne opisy zdjęć. Mówiące, co rozpoznały na zdjęciach ich algorytmy.  
Ustawiając w&nbsp;opcjach blokowanie nawet najmniejszych obrazków (gdy wpiszemy 0&nbsp;kB) i&nbsp;odwiedzając FB, możemy łatwo poczytać te opisy. I&nbsp;zobaczyć, czy fejsowe „ej-aj” jest cokolwiek warte."
trailer="<p class='figure'><img src='/assets/posts/ublock-origin/ublock-blokowanie-obrazow-fb.jpg' alt='Zrzut ekranu z&nbsp;Facebooka pokazujący dwie miniaturki wydarzeń. Zamiast oryginalnych zdjęć widać czerwone ramki, a&nbsp;w ich wnętrzu opisy mówiące, że zdjęcia pokazują tekst.'/></p>"
%}

# 3. Wyłączanie kodu JavaScript

JavaScript to kod odpowiadający na stronach internetowych za elementy interaktywne. To dzięki niemu podczas wpisywania informacji pojawiają nam się np. ostrzeżenia mówiące, że nie wypełniliśmy jakiegoś pola.

JS ma jednak ciemne strony. Dzięki dostępowi do wielu informacji o&nbsp;naszym komputerze (takich jak lista czcionek, parametry sprzętu, położenie kursora myszki...) jest w&nbsp;stanie sprofilować nas dokładniej niż inne metody.

Dlatego, jeśli chcemy tylko sobie poczytać wpisy na różnych blogach i&nbsp;statycznych stronkach, warto pstryknąć wyłącznik JavaScriptu. Zobaczymy internet od całkiem innej, spokojniejszej strony!

A na potrzeby wszelkich interaktywnych stron znowu go sobie włączymy. Muszę niestety uprzedzić, że trzeba będzie to robić dość często.

# 4. Niszczenie elementów

Lubię niszczyć, więc to jedna z&nbsp;moich ulubionych funkcji.

Mówiąc krótko: klikamy w&nbsp;ikonę błyskawicy i&nbsp;zmienia nam się kursor. Teraz, **gdy klikniemy jakiś element na stronie, to go „znikniemy”** (oczywiście tylko u&nbsp;siebie; właścicielom strony niczego nie rozwalimy :wink:).

Przydaje się to do wszelkich irytujących rzeczy, ale ma też przyjemny efekt uboczny.

Po wprowadzeniu RODO/GDPR pojawił się obowiązek pytania użytkowników o&nbsp;zgodę na śledzenie. Firmy teoretycznie nie mogą zbierać informacji, dopóki użytkownik nie kliknie, że się na to zgadza.

Ale niektóre się wycwaniły. Na pierwszy rzut oka mają wyłączone zbieranie informacji. Natomiast gdy klikniemy „Więcej”, to znajdziemy wszystkie zgody automatycznie zaznaczone pod kategorią „Uzasadniony interes”.  
Jeśli ich nie odhaczymy, to będą zbierali informacje tak jak wcześniej.

W takiej sytuacji niszczyciel bardzo pomaga. Pojawia nam się okno pytające o&nbsp;zgody na śledzenie? Można po prostu je zniszczyć i&nbsp;czytać dalej. Bez wysiłku, bez wpadnięcia w&nbsp;pułapkę. Żadnej zgody nie kliknęliśmy, więc nie powinni niczego zbierać.

{% include info.html
type="Porada"
text="Czasem elementów do zniszczenia jest wiele (na przykład baner złożony z&nbsp;kilku warstw). A&nbsp;po zwykłym kliknięciu tryb niszczenia się wyłącza i&nbsp;trzeba znowu klikać w&nbsp;błyskawicę.  
Żeby oszczędzić kliknięć, możemy skorzystać ze [świetnego udogodnienia](https://github.com/gorhill/uBlock/wiki/Element-zapper) -- wystarczy najechać kursorem na element, żeby się podświetlił, i&nbsp;nacisnąć `Delete`. Usuniemy go bez opuszczania trybu niszczenia.  
Co więcej, w&nbsp;menu uBO, w&nbsp;zakładce „Skróty”, możemy ustawić skrót klawiszowy włączający tryb usuwania. Warto tu dać coś mało używanego (osobiście wybrałem `Ctrl`+`,`)"
%}

# 5. Ustawienia

Tutaj się udajemy, jeśli nie chcemy za każdym razem czegoś przełączać. Możemy na przykład:

* Ustawić, które opcje mają być domyślnie włączone, a&nbsp;które wyłączone,
* Zmienić rozmiar elementów dopuszczalnych w&nbsp;trybie blokowania,
* Ustawić skróty klawiszowe dla niektórych funkcji,
* Dodać własne reguły filtrujące dla konkretnych stron.

...I wiele innych. Ogólnie, jeśli nie rozumiemy niektórych opcji, można się ograniczyć do zakładki `Ustawienia` i&nbsp;opcji pod nagłówkiem `Działania domyślne` (na dole). Tam możemy wybrać, które podstawowe rzeczy chcemy mieć domyślnie włączone.

## Inne propozycje zmian

OK. Mamy uBlock Origin, trochę wiedzy na jego temat. Umiemy z&nbsp;niego korzystać. Jeśli chcemy wyciągnąć z&nbsp;niego jeszcze więcej, warto zmienić pewne rzeczy niezwiązane z&nbsp;samym dodatkiem. 

# Zrezygnujcie z&nbsp;innych blokerów

Porada może się wydawać podejrzana -- patrząc intuicyjnie, każdy nowy bloker to dodatkowa ochrona. Czyżbym chciał Was w&nbsp;coś wkopać?

Nie. Po prostu z&nbsp;blokerami jest jak z&nbsp;prawdziwymi tarczami. Jeśli mamy jedną solidną, to się skutecznie osłonimy. **Jeśli taszczymy kilka naraz, to tylko będą sobie nawzajem wchodziły w&nbsp;drogę**.

Poza tym każdy z&nbsp;blokerów może z&nbsp;czasem „zejść na złą drogę”, przykłady opisywałem wcześniej w&nbsp;tym wpisie.  
Trzymając tylko jednego, z&nbsp;dobrą reputacją, minimalizujemy to ryzyko.

# Używajcie go na Firefoksie

Współczesne firmy reklamowe nieco się wycwaniły. Żeby ich elementy śledzące nie były blokowane, stosują trik zwany *CNAME cloaking*. Upraszczając: w&nbsp;ten sposób wmawiają przeglądarce odwiedzającej stronę A, że również pochodzą ze strony A&nbsp;(choć tak naprawdę są&nbsp;z&nbsp;B).

Tylko Firefox daje dodatkom możliwość rozpoznania takich trików. Inne przeglądarki, często oparte na silniku Chromium (Chrome, Opera, Vivaldi, Edge), tego nie mają. Przypomnę wykres skuteczności z&nbsp;krótszej wersji wpisu:

{:.figure .bigspace}
<img width="600px" src="/assets/posts/ublock-origin/adblock-skutecznosc.jpg" alt="Pięć wykresów słupkowych dla różnych przeglądarek i&nbsp;dodatków, pokazujących procent blokowanych trackerów. Najwyższe słupki odpowiadają w&nbsp;każdym przypadku uBlock Origin, a&nbsp;najwyższy ze wszystkich jest ten dla nowej wersji uBlock Origin na Firefoksie"/>

Jeśli z&nbsp;tego czy innego powodu nie chcemy używać Firefoksa, to luzik. Inne przeglądarki nie będą tak skuteczne, ale zadziałają.

Natomiast **porządnie rozważmy rezygnację z&nbsp;Chrome'a**.  
To przeglądarka od największego z&nbsp;gigantów reklamowych. Korzystając z&nbsp;niej, co najwyżej zablokujemy mniejsze firmy śledzące, ale Google będzie miał priorytetowy dostęp do naszych danych.

Jeśli bardzo Wam pasuje wygoda Chrome'a i&nbsp;nie dopuszczacie niczego innego, to przynajmniej użyjcie zamiast niego Chromium. Wygląda i&nbsp;działa niemal tak samo, tylko że nie synchronizuje danych z&nbsp;Google.

## Podsumowanie

Dowiedzieliśmy się nieco więcej na temat dodatku uBlock Origin, który skutecznie nas ochroni przed wieloma elementami śledzącymi.

Jeśli sprawy związane z&nbsp;ochroną prywatności nas przytłaczają, to uBO jest takim absolutnym minimum. Poświęćmy te kilka minut i&nbsp;zainstalujmy go w&nbsp;swojej przeglądarce.

Nie pożałujemy. Internet stanie się lżejszy, szybszy, przyjemniejszy w&nbsp;obsłudze. A&nbsp;gdzieś za kulisami wzrosną statystyki blokowania reklam, być może wymuszając na *ad techu* bardziej ludzkie podejście :wink:
