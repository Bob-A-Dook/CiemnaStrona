---
layout: post
title: "Internetowa inwigilacja plus 8 – profilowanie stron internetowych"
subtitle: "„Wiem, kogo odwiedzasz”"
description: "„Wiem, kogo odwiedzasz”"
date:   2024-06-19 06:00:00 +0100
tags: [Internet, Inwigilacja]
firmy: [Stack Exchange]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image:
  path: /assets/posts/inwigilacja/website-fingerprinting/website-fingerprinting-baner.jpg
  width: 1200
  height: 700
  alt: "Regał z numerowanymi półkami, na których stoją donice. Memiczna postać w dymku z przemyśleniami sumuje kontury kilku z nich, uzyskując numer półki."
---

Wracam do pisania po najdłuższej jak dotąd, ponad dwumiesięcznej przerwie! Nie tylko rekreacyjnej. Dopracowałem też parę ambitniejszych projekcików, którymi jeszcze się podzielę :wink:

Ale najpierw klasyczne wpisy. Zaczynając od tego tutaj, demaskującego kolejne metody z&nbsp;przybornika cyfrowych stalkerów (prywatnych i&nbsp;korporacyjnych).

Rozwinę tu kwestie wokół **ustalania, co robili internauci, _mimo że ich interakcje były szyfrowane_**. Wciąż mogą ich bowiem zdradzić cechy ruchu sieciowego, takie jak ogólne nazwy odwiedzanych stron, kierunek przesyłu danych, ich rozmiar oraz czas wysłania.

W [poprzednim wpisie]({% post_url 2024-03-28-analiza-ruchu %}){:.internal} na ten temat podglądacze byli bierni, tylko obserwowali. Dziś uchylę to założenie.

Znając nazwę strony, jaką odwiedzała ofiara, mogliby również ją odwiedzić i&nbsp;*sprofilować* -- zebrać różne jej podstrony, ustalić łączny rozmiar każdej z&nbsp;nich. Znaleźć cechy odróżniające je od siebie.  
Następnie ich programy mogłyby porównać te wzorce z&nbsp;ruchem swojej ofiary. Ustalając, co *dokładnie* robiła na danej stronie. 

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/website-fingerprinting/website-fingerprinting-baner.jpg" alt="Regał z&nbsp;numerowanymi półkami, na których stoją donice. Memiczna postać dodaje w&nbsp;dymku z&nbsp;przemyśleniami kontury kilku doniczek, uzyskując odpowiadającą im półkę."/>

{:.figcaption}
Źródła: [regał](https://www.freepik.com/free-photo/wooden-plant-shelf-with-mixed-plants_18098563.htm) z&nbsp;serwisu Freepik, liczby z&nbsp;Emojipedii, [mem z&nbsp;Wojakiem](https://www.pinterest.com/pin/541487555207733637/), dymek z&nbsp;LibreOffice Writera. Przeróbki moje.

## Spis treści

* [Przypominajka](#przypominajka)
* [Profilowanie na przykładzie Stack Exchange](#profilowanie-na-przykładzie-stack-exchange)
  * [Scenariusz](#scenariusz)
  * [Pierwszy krok: domena](#pierwszy-krok-domena)
  * [Drugi krok: wytypowanie możliwych podstron](#drugi-krok-wytypowanie-możliwych-podstron)
  * [Trzeci krok: zawężenie listy podstron](#trzeci-krok-zawężenie-listy-podstron)
  * [Czwarty krok: łączenie informacji](#czwarty-krok-łączenie-informacji)
* [Ograniczenia metody](#ograniczenia-metody)
* [Jak chronić siebie](#jak-chronić-siebie)
* [Jak chronić innych](#jak chronić-innych)
  * [Niewinne domeny, winne podstrony](#niewinne-domeny-winne-podstrony)
  * [Jedna domena](#jedna-domena)
  * [Ujednolicanie podstron](#ujednolicanie-podstron)
  * [Parę innych szlifów](#parę innych-szlifów)
* [Zakończenie](#zakończenie)

## Przypominajka

Na początek streszczę parę najważniejszych informacji z&nbsp;poprzedniego wpisu, podlinkowanego wyżej.

W ramach „Internetowej inwigilacji” wyróżniam często dwa rodzaje podglądaczy, różniących się pod względem możliwości wglądu w&nbsp;dane.

Więcej -- ale tylko na swoim terytorium -- widzą właściciele odwiedzanych stron albo elementów gościnnych, jak reklamy śledzące.  
Drugi rodzaj podglądaczy to właściciele infrastruktury internetowej. To oni są antagonistami tego i&nbsp;poprzedniego wpisu. Ich przykłady:

* firma telekomunikacyjna (operator sieci komórkowej),
* właściciel routera, przez który łączymy się z&nbsp;siecią (np. administrator sieci firmowej/uczelnianej; personel kawiarni wyposażonej w&nbsp;hotspota),
* właściciel VPN-a, jeśli z&nbsp;jakiegoś korzystamy.

Następna kwestia: *co* widzą tacy podglądacze.

Przypadkiem skrajnym są strony zaczynające się od `http://`. W&nbsp;wielu przeglądarkach oznaczane ikonką przekreślonej kłódki obok górnego paska wyszukiwania. **Gdy je odwiedzamy, to połączenie nie jest szyfrowane i&nbsp;podglądacz widzi _wszystko_**.

Jest to jednak coraz rzadsza sytuacja, więc nie będę jej brał pod uwagę. Zamiast tego skupię się na popularniejszym rodzaju interakcji, czyli odwiedzaniu stron zaczynających się od `https://`.

Połączenia z&nbsp;nimi są szyfrowane i&nbsp;przeciwnik nie zobaczy, *co* sobie wysyłamy ani jak się sobie „przedstawiamy”. Spod szyfrów nadal jednak wystają pewne rzeczy (jak nazwa domeny, czyli np. `www.ciemnastrona.com.pl`), do których jeszcze wrócę.

## Profilowanie na przykładzie Stack Exchange

Koniec przypominajek, czas na dzisiejsze zagrożenie! **Profilowanie stron internetowych (ang. _website fingerprinting_)**. Wpisując to pojęcie w&nbsp;wyszukiwarkę, można trafić nawet na pełnoprawne [artykuły naukowe](https://arxiv.org/pdf/2302.13763.pdf).

{:.post-meta .bigspace-after}
Warto jednak wpisywać w&nbsp;cudzysłowach -- `"website fingerprinting"` -- bo samo *fingerprinting* to pojęcie szersze i&nbsp;stosowane częściej wobec metod wyciągania informacji [*od przeglądarek*]({% post_url 2022-05-03-javascript2 %}){:.internal}, a&nbsp;nie stron.

Ogólne założenie metody jest proste -- opiera się ona na tym, że wiele stron internetowych nie zmienia się w&nbsp;czasie. Jest spora szansa, że zwiedzając tę samą stronę co podglądana osoba, trafi się na te same treści.

A to oznacza dane o&nbsp;takim samym rozmiarze i&nbsp;„kształcie”. Podglądacz jest jak człowiek otrzymujący od strony po kilka klocków i&nbsp;patrzący, czy pasują do otworów w&nbsp;jego planszy.

Żeby lepiej to zwizualizować, użyję konkretnego przykładu. Będzie nim wielkie forum Stack Exchange. Poświęcone głównie sprawom komputerowym, ale są tam też mniejsze podfora o&nbsp;tematyce wszelakiej. Językach świata, gotowaniu, majsterkowaniu...

{% include info.html
type="Ciekawostka"
text="Stacka nie wybrałem tak całkiem przypadkowo. To forum już łączy się z co najmniej jednym głośnym [zdemaskowaniem](https://www.forbes.com/sites/alexkonrad/2013/10/02/feds-shut-down-silk-road-owner-known-as-dread-pirate-roberts-arrested/) (choć akurat przez coś bliższego stylometrii niż profilowaniu stron).  
Mianowicie: odkryto tożsamość właściciela znanej darknetowej giełdy przez [pytanie o&nbsp;sieć anonimizującą](http://stackoverflow.com/questions/15445285/how-can-i-connect-to-a-tor-hidden-service-using-curl-in-php), jakie zadał kiedyś na podforum StackOverflow. Zadziwiająco dobrze pasowało do jego działalności.  
...A przynajmniej taki powód wskazano jako oficjalny. Niewykluczone, że tożsamość ustalono innymi metodami, a&nbsp;wersję ze Stackiem przyjęto jako wiarygodną narrację."
%}

### Scenariusz

Przykład z&nbsp;życia czas zacząć!

Jest sobie pewna osoba, którą nazwiemy sobie X. Wygląd, historia, zainteresowania -- pozostawiam waszej wyobraźni.  
Powiem tylko, że akurat jest w&nbsp;trakcie podróży. Zbiorkomem, bo nie trzeba tam trzymać rąk na kierownicy i&nbsp;można w&nbsp;spokoju czytać nowinki z&nbsp;różnych grup tematycznych.

Wysiada na dworcu i&nbsp;czeka na dalszy transport. Łączy się z&nbsp;darmowym hotspotem, żeby nieco oszczędzić danych mobilnych.  
Nie wie jednak, że akurat ten konkretny hotspot jest obsługiwany przez znużonego administratora z&nbsp;zamiłowaniem do automatyzacji... I&nbsp;stalkingu.

Wszelkie dane przechodzące przez router są automatycznie analizowane. Jeśli jakieś urządzenie odwiedzi co ciekawsze strony internetowe, to programy admina zaczną zapisywać powiązany z&nbsp;nim ruch do osobnych folderów. Admin będzie potem gmerał sobie w&nbsp;tych danych, oblizując się po gałkach ocznych.

A tak się składa, że wśród domen odwiedzonych podczas tej dworcowej posiadówki była co najmniej jedna, która wzbudziła stalkerskie zainteresowanie.

Założmy, że podglądana osoba X&nbsp;czyta na przykład dwa ciekawe podfora Stacka. Jedno dotyczy przeglądarki anonimizującej Tor Browser, a&nbsp;drugie ogólnego cyberbezpieczeństwa.

### Pierwszy krok: domena

Nazwa domeny oraz jej adres IP, widoczne zazwyczaj mimo szyfrowania, są świetnym punktem wyjścia dla podglądaczy.

Tak się składa, że **na Stacku każde podforum ma swoją osobną subdomenę**. Tej od Tora odpowiada `tor.stackexchange.com`, zaś dyskusje wokół cyberbezpieczeństwa toczą się na `security.stackexchange.com`.

{:.post-meta .bigspace-after}
Tutaj skupię się na przypadku typowym, gdy nazwa strony jest widoczna. Ale nawet gdyby była ukryta (np. na stronach wspierających [ECH]({% post_url 2022-08-13-metadane-esni-ech %}){:.internal}), czasem podglądacz mógłby ją ustalić po [kombinacjach adresów IP](https://blog.apnic.net/2019/08/23/what-can-you-learn-from-an-ip-address/).

W oczach użytkownika link do przykładowej dyskusji, kliknięty w&nbsp;wyszukiwarce, wygląda tak:

<div class="bigspace-before black-bg mono">
https://tor.stackexchange.com<span class="red">/questions/222/how-can-website-fingerprinting-be-prevented</span>
</div>

Podglądacze widzą to, co na biało. Ogólną nazwę i&nbsp;rozmiar danych. Z&nbsp;kolei czerwona część linku, jak i&nbsp;sama treść strony, są zaszyfrowane.

{:.figure .bigspace-before}
<img src='/assets/posts/inwigilacja/website-fingerprinting/wireshark-tor-stack-sni.jpg' alt='Informacja z&nbsp;programu Wireshark pokazująca nazwę domeny, tor.stackexchange.com'/>

{:.figcaption}
Tutaj zrzut z&nbsp;programu Wireshark przechwytującego ruch internetowy; nazwa strony znajduje się w&nbsp;polu *Server Name Indication*.

Gdyby Stack trzymał wszystko na jednej domenie, `stackexchange.com`, to podglądacz zapewne by odpuścił. Za dużo możliwości, do tego większość osób trzyma się pewnie prozaicznych pytań w&nbsp;stylu „jak wyśrodkować przycisk na stronie”.

...Ale kiedy program podglądacza wyłapie to konkretne podforum, poświęcone dbaniu o&nbsp;anonimowość? Potraktuje to jako sygnał, że może tej osobie poświęcić więcej uwagi.

{% include info.html
type="Ciekawostka"
text="Taki wstępny przesiew na podstawie metadanych jest całkiem popularną taktyką w świecie cyfrowej inwigilacji. Nie tylko stalkerskiej, ale i&nbsp;zawodowej, szpiegowskiej.  
Amerykańska agencja NSA opracowała listę stron podejrzanych, których bywalców kwalifikuje się do wzmożonej obserwacji. Co ciekawe, do takich portali zaliczono... [Linux Journal](https://www.linuxjournal.com/content/nsa-linux-journal-extremist-forum-and-its-readers-get-flagged-extra-surveillance), czyli nieszkodliwą hobbystyczną stronkę poświęconą alternatywie dla Windowsa.  
Link prowadzi prosto do niej, gdyby ktoś chciał zerknąć :smiling_imp:"
%}

### Drugi krok: wytypowanie możliwych podstron

Znając domenę, podglądacz może odwiedzić wszystkie strony, które są zebrane pod jej parasolem. Przypomnę analogię: zawartość domeny jest jak wór klocków lub puzzli o&nbsp;różnym kształcie, które nasz antagonista będzie sobie dopasowywał do otworów pozostawionych po swojej ofierze.

A jak duży jest ten wór?  
Na podforum dotyczącym Tora znajdowało się łącznie, gdy ostatnio zerkałem, [5801 wątków](https://tor.stackexchange.com/questions). Na podforum *Security*, o&nbsp;cyberbezpieczeństwie, [jest ich 69&nbsp;029](https://security.stackexchange.com/questions).

Dla człowieka może i&nbsp;dużo, dla komputera -- tyle co nic. Podglądacz może wypuścić na interesującą go stronkę swojego **_crawlera_**, czyli program odwiedzający wskazane strony i&nbsp;zapisujący sobie ich treść.

W przypadku Stacka to o&nbsp;tyle łatwe, że przeglądanie stron nie wymaga logowania. Nawet gdyby istniały jakieś zabezpieczenia utrudniające amatorskie zbieractwo, podglądacz mógłby zapłacić zbieraczom zawodowym. Korzystając z&nbsp;całej sieci komputerów i&nbsp;dużej puli adresów IP, ominęliby blokady i&nbsp;pobrali całą treść.

Do tego automat mógłby wykorzystać na swoją korzyść szablonowy format linków do list zbiorczych:

<pre class="black-bg mono">
https://<span class="red">PODFORUM</span>.stackexchange.com/questions?tab=newest&pagesize=50&page=<span class="red">LICZBA</span>
</pre>

Podstawiając nazwę podforum i&nbsp;kolejne liczby, *crawler* podglądacza prosiłby o&nbsp;kolejne rzeczy i&nbsp;stopniowo zebrałby pełną listę linków do wszystkich wpisów. Wraz z&nbsp;podstawowymi informacjami na temat każdego z&nbsp;nich:

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/website-fingerprinting/stack-watek-link.jpg" alt="Link do pojedynczej dyskusji ze Stacka, przy którym widać liczbę odpowiedzi"/>

Zapamiętajcie sobie wygląd miniaturek wpisów, za chwilę do tego wrócę.

### Trzeci krok: zawężenie listy podstron

Stack posiada jeszcze jedną cechę, która mogłaby pomóc zawęzić liczbę stron do pobrania. To **awatary (obrazki) użytkowników, pobierane ze stronek zewnętrznych**. W&nbsp;wątkach dyskusyjnych, wedle moich obserwacji, pojawiają się tylko w&nbsp;określonych miejscach:

* jeden awatar autora przy pytaniu;
* po jednym awatarze przy każdej z&nbsp;odpowiedzi;
* (opcjonalnie) awatar osoby edytującej, najwyżej jeden na pytanie/odpowiedź.

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/website-fingerprinting/stack-interfejs-awatary.jpg" alt="Zrzut ekranu pokazujący fragmenty paru odpowiedzi na Stacku. Widać pod nimi miniaturowe obrazki użytkowników, otoczone czerwonymi ramkami."/>

{:.figcaption}
Fragment interfejsu Stacka na przykładzie [innej dyskusji na temat Tora](https://tor.stackexchange.com/questions/20885/what-makes-onion-sites-more-safe-than-regular-html-sites), awatary wyróżniłem ramkami.  
Gdyby ktoś edytował któryś wpis, to po lewej stronie autora znalazłby się awatar osoby edytującej.

A teraz wrócę do listy wątków, której screen pokazałem wcześniej. Jedną z&nbsp;informacji przy każdym linku do dyskusji jest **liczba udzielonych odpowiedzi**.

Widząc „3 odpowiedzi” przy miniaturce jakiegoś wątku, podglądacz może zakładać, że jego odwiedzenie wiąże się z&nbsp;pobraniem od 4&nbsp;do 8&nbsp;awatarów (1&nbsp;przy pytaniu, 3&nbsp;przy odpowiedziach, reszta od ewentualnych edycji pytań/odpowiedzi).

A w&nbsp;jaki sposób podglądacz może wyciągnąć z&nbsp;historii ruchu sieciowego, ile awatarów pobrała jego ofiara? Przecież dane są szyfrowane. Łącznie z&nbsp;nazwami plików, więc nie widać nawet, czy coś jest obrazkiem, ikonką samego forum, skryptem czy innym wihajstrem.

Awatary jednak mocno się wyróżniają na tle reszty -- **pochodzą z&nbsp;innych domen**.


{% include info.html
type="Porada"
text="Zachęcam do osobistego weryfikowania wszystkich moich przykładów w&nbsp;narzędziach dostępnych w&nbsp;niemal każdej przeglądarce :smile:  
Wystarczy nacisnąć klawisze `Ctrl+Shift+I`, żeby otworzyć panel z&nbsp;narzędziami. Następnie trzeba kliknąć zakładkę `Sieć` u&nbsp;góry i&nbsp;w razie potrzeby odświeżyć stronę. Po najechaniu kursorem na nazwy pobranych obrazków powinny się wyświetlać ich miniaturki.  
Dla wygodniejszego czytania warto też kliknąć ikonkę w górnym prawym rogu i&nbsp;wybrać wyświetlanie w&nbsp;osobnym oknie. Można je wtedy powiększać i&nbsp;przesuwać wedle uznania."
%}

Wchodząc w&nbsp;podlinkowaną już [dyskusję](https://tor.stackexchange.com/questions/20885/what-makes-onion-sites-more-safe-than-regular-html-sites) o&nbsp;Torze i&nbsp;zerkając w&nbsp;narzędzia przeglądarki, poznałem kilka źródeł awatarów:

* awatary losowe (pod pytaniem i&nbsp;jedną z&nbsp;odpowiedzi) pochodzą z&nbsp;domeny `gravatar.com`,
* awatar autora najnowszej odpowiedzi, przypominający kaczkę, od `lh3.googleusercontent.com`,
* inny awatar od `i.sstatic.net`.

Nie do końca wiem, z&nbsp;czego wynika obecność Google'a. Być może użytkownicy mogą czasem wiązać swoje konto na Stacku z&nbsp;innymi usługami, a&nbsp;Stack korzysta wtedy z&nbsp;innych awatarów niż domyślnie?

W każdym razie -- z&nbsp;tego co zaobserwowałem, **te domeny (poza ostatnią) odpowiadają wyłącznie awatarom**.

Widząc liczbę drobnych plików nadlatujących z&nbsp;powyższych domen, podglądacz może łatwo odgadnąć liczbę awatarów, jakie wyświetliły się ofierze. I&nbsp;zawęzić swoją listę do tych dyskusji, które mają odpowiednią liczbę odpowiedzi. 

### Czwarty krok: łączenie informacji

Ostatnim etapem po zawężeniu listy linków jest odwiedzanie po kolei każdego z&nbsp;nich. I&nbsp;porównywanie otrzymanych danych ze wzorcem. Ułatwia to szereg właściwości Stacka.

Po pierwsze: dyskusja dyskusji nierówna. Niektóre są znacznie obszerniejsze od innych. A&nbsp;dłuższe ściany tekstu oznaczają siłą rzeczy, że plik HTML -- sam szkielet strony, wysłany jako pierwszy po jej odwiedzeniu -- będzie miał nieco większy rozmiar niż te odpowiadające innym dyskusjom.

Po drugie: w&nbsp;dyskusjach można czasem dodawać obrazki. 

Żeby już nie trzymać się tylko Torów i&nbsp;szyfrów -- przedstawiam [epicką dyskusję na temat literki z&nbsp;piłki dla dzieci](https://english.stackexchange.com/questions/395382/which-word-begins-with-y-and-looks-like-an-axe-in-this-picture). Dyskutanci próbują ustalić, dlaczego przy rysunkowej siekierce umieszczono literkę *Y*. Śledztwo sięga Chin i&nbsp;Skandynawii.

...I obejmuje wklejanie licznych obrazków, serwowanych głównie z&nbsp;domeny `i.sstatic.net`. Niektóre mają rozmiar po sto kilkadziesiąt kB, co skutecznie je odróżnia od awatarów. I&nbsp;wyróżnia całą dyskusję spośród innych, bardziej tekstowych.

Same awatary też zresztą się różnią pod względem rozmiaru. Te złożone z&nbsp;prostych geometrycznych kształtów, generowane losowo przez Stacka, mają zwykle nieco ponad 1&nbsp;kB rozmiaru. Pozostałe, będące pełnoprawnymi (choć małymi) obrazkami, ważą ponad 2&nbsp;kB.

No i&nbsp;pozostaje kwestia domen, z&nbsp;których pochodzą awatary. Poprzednio do zawężania listy wystarczyła łączna liczba wszystkich „awatarowych”.  
Na tym etapie dla podglądacza bezcenne będą z&nbsp;kolei ich pełne nazwy. „Dwa obrazki z&nbsp;Gravatara, jeden z&nbsp;`googleusercontent`” to informacja, która może się okazać unikalnym identyfikatorem jakiejś dyskusji.

Łącząc te informacje w&nbsp;całość, **klasyfikator (program analityczny) podglądacza może rozpoznać spośród możliwych dyskusji tę jedną, konkretną, którą odwiedziła wcześniej ofiara**.

Metoda potrafi być niepokojąco dokładna. Na szczęście sytuacja nie zawsze będzie idealna dla podglądaczy.

## Ograniczenia metody

Przeglądarki, systemy operacyjne, internetowe serwisy... to czasem złożone bestie. A&nbsp;duża ilość ruchomych elementów utrudnia profilowanie.

Solą w&nbsp;oku drobniejszych podglądaczy może być na przykład **pamięć podręczna**.

Żeby nie pobierać jednakowych elementów (np. obrazków) wielokrotnie, przeglądarka zapisuje je na jakiś czas na dysku, [we własnym folderze]({% post_url 2021-12-24-caching %}){:.internal}.

Przykład? Logo Ciemnej Strony z&nbsp;górnego paska mojego bloga. Przeglądarka pobierze je raz, przy pierwszym odwiedzeniu bloga. Ale potem, do czasu wyczyszczenia pamięci, już nie będzie o&nbsp;nie prosiła.

Pamięć podręczna może odebrać podglądaczom proste przejście `łączny rozmiar elementów → konkretna strona`. Pojawia się niepewność. Ale niektóre klasyfikatory niestety mogą być na to odporne, przypisując większą wagę tym elementom, które nie trafiają do pamięci.

Drugie utrudnienie (ale tylko na niektórych stronach) -- **losowość i&nbsp;ładowanie dynamiczne**.

W roli ilustracji użyję wielkich portali, jak Facebook czy Tiktok. Choć same podglądają ludzi, są chyba najgorszym koszmarem dla podglądaczy zewnętrznych.

Po pierwsze: wykorzystują niewiele domen. Właściwie tylko główną i&nbsp;parę pomocnicznych, z&nbsp;których serwują na przykład obrazki (jak `fbcdn.net` w&nbsp;przypadku Facebooka).

Po drugie: nie mają stałej postaci. Wyświetlają różne rzeczy w&nbsp;zależności od profilu osoby, która z&nbsp;nich korzysta, zdarzeń na świecie, a&nbsp;może nawet zwykłej losowości.  
Jest też mnóstwo czynników pobudzających napływ danych -- przewinięcie tablicy, kliknięcie jakiejś opcji, nowa wrzutka od obserwowanego profilu...

Do tego znane portale po prostu są wielkie. Jak oceany danych. Praktycznie nie ma szans na ustalenie, że pobrana rzecz o&nbsp;rozmiarze 79&nbsp;kB jest jakimś konkretnym obrazkiem.

Powyższe informacje, choć są pewnym pocieszeniem, nie powinny powodować spoczęcia na laurach. Oznaczają tylko tyle, że machina nie jest wszechmocna. Ale nadal trzeba trochę powalczyć :wink:

## Jak chronić siebie

Choć profilowanie dotyczy stron, na które internauci nie mają bezpośredniego wpływu, sami również mogą puścić trochę światła we wścibskie oczy.

Zasada ogólna -- **trzeba ustawić między sobą a&nbsp;łatwą do sprofilowania stronką jakiegoś pośrednika**.  
Punktem wyjścia do profilowania są nazwy domen. Jeśli staną się niewidoczne, to podglądacz niewiele zdziała. Wór wymieszanych stron do sprawdzenia stałby się wielki jak internet.

Po więcej szczegółów i&nbsp;schematy graficzne odsyłam do [poprzedniego wpisu]({% post_url 2024-03-28-analiza-ruchu %}##jak-się-chronić){:.internal}; poniżej jedynie ogólna przypominajka.

{:.bigspace}
<details>
<summary><strong>Streszczenie metod ochrony (dla chętnych)</strong></summary>

<ul>
  <li>
    <p>HTTPS plus szyfrowanie metadanych (DoH plus ECH)</p>

    <p>W tym przypadku przeciwnik nie widzi nazwy odwiedzanej domeny. Widzi za to adresy IP, rozmiar danych, czas ich wysłania.<br />
Ograniczeniem metody jest to, że musi być wspierana przez odwiedzane strony. A&nbsp;że jest względnie nowa, to póki co nie jest zbyt popularna. Lepiej zakładać jej brak.</p>
  </li>
  <li>
    <p>pośrednik/VPN</p>

    <p>Przeciwnik widzi jedynie adres IP pośrednika i&nbsp;nie wie, jakie części internetu są po jego drugiej stronie. Widzi też rozmiar i&nbsp;czas wysłania danych, ale to może niewiele pomóc.<br />
Wadą rozwiązania jest konieczność zaufania pośrednikowi. Trzeba mu powierzyć prawdziwe nazwy domen i&nbsp;adresy... A&nbsp;nie ma gwarancji, że sam tych danych nie gromadzi.</p>
  </li>
  <li>
    <p>sieć Tor</p>

    <p>Jak VPN na sterydach. Zamiast jednego pośrednika – łańcuszek kilku rozsianych po świecie, z&nbsp;których każdy jest losowo dobierany i&nbsp;ma tylko strzępki informacji. Zewnętrzny podglądacz zobaczyłby tylko adres IP pierwszego z&nbsp;nich.<br />
Co więcej, Tor stosuje dodatkowe mechanizmy ochronne. Dane są wysyłane w&nbsp;nieregularnych, losowych odstępach czasu. Koszmar dla podglądaczy.</p>
  </li>
</ul>
</details>

A co, jeśli nie ma się dostępu do żadnego pośrednika typu Tor/VPN, a&nbsp;jedyną opcją jest bezpośrednie odwiedzanie stron? Można wtedy **skorzystać z&nbsp;większych stron zdolnych wyświetlać cudze treści pod swoim „szyldem”**.

Przykładem są archiwa internetowe jak *archive.org* czy *archive.is*, gromadzące treść przeróżnych stron. Podglądaczom dużo trudniej by było je zmapować, choćby ze względu na ich rozmiar.

Żeby korzystać z&nbsp;archiwów, wystarczy skopiować interesujący nas link i&nbsp;wkleić go w&nbsp;ich wyszukiwarki. Jeśli ktoś już kiedyś zapisał taką stronę do archiwum, to wyświetli się kalendarz z&nbsp;historią poprzednich zapisów. Tam nieraz się znajdzie szukaną treść. A&nbsp;podglądacz łatwo jej nie pozna.

{% include info.html
type="Powiązane wpisy"
text="Podobne obejście opisałem we wpisie na temat [cenzury przez DNS](/2022/09/12/dns-ip-cenzura){:.internal}. To dlatego, że zasada działania jest bardzo podobna -- jakaś menda, widząc nazwy niektórych domen, jakie próbujemy załadować, zachowuje się wobec nas niegrzecznie. Więc tę nazwę ukrywamy, żeby wymusić domyślną grzeczność."
%}

### Rozwiązania pomocnicze

Najpierw podkreślę: **wszystko poza ukrywaniem domen (i&nbsp;adresów IP) to jedynie dodatkowe szlify**. Stosowanie ich bez zadbania o&nbsp;fundamenty wydaje mi się bezcelowe.

Tym niemniej, jeśli ktoś nie ma jak skorzystać z&nbsp;pośrednika albo chce dopracować parę rzeczy... To warto wiedzieć, że odrobinę mogą namieszać niektóre dodatki modyfikujące działanie przeglądarki. Jak [uBlock Origin]({% post_url 2021-10-21-ublock-origin-wiecej %}){:.internal}, bloker śledzących reklam.

W opcjach dodatku można ustawić, żeby nie pobierał obrazków większych niż ustalony rozmiar (w&nbsp;kilobajtach). Ta opcja sprzyja głównie oszczędzaniu danych... Ale ma też niezamierzony wpływ na prywatność.  
Użytkownicy odbiegają od wzorca. Pobierają znacznie mniej danych niż oczekiwałby podglądacz, dzięki czemu ich aktywność może być trudniejsza do sklasyfikowania.

Jeśli korzysta się z pośrednika/Tora/VPN-a, to podglądacz widzi tylko jeden adres IP.  
Można wtedy dodatkowo namieszać, otwierając **kilka podstron w&nbsp;osobnych kartach**. Jedną po drugiej. Nastąpi wtedy większy napływ danych z&nbsp;tego samego adresu i&nbsp;może być trudniej rozpleść, z&nbsp;jakich podstron to pochodzi.

## Jak chronić innych

Właściciele stron raczej nie uchronią się przed odwiedzinami *crawlerów* i&nbsp;mapowaniem swoich stron. Mogą natomiast na kilka sposobów wspomóc swoich użytkowników, czyniąc strony mniej podatnymi na profilowanie przez stalkerów.

### Niewinne domeny, winne podstrony

Domena była pierwszym krokiem w&nbsp;profilowaniu strony. Dlatego, w&nbsp;miarę możliwości, można wybrać sobie jakąś grzeczną nazwę, żeby nie przykuwała uwagi. Dla tego bloga już na to za późno, ale dla was może jeszcze nie :wink:

Dla rozluźnienia wplotę mikrowątek baśniowy. Wyobraźmy sobie, że żyjemy w&nbsp;fikcyjnym Królestwie Gudwajbinii (zmyślona domena nadrzędna: `.gud`).

Jego mieszkańcy są szczęśliwi. Muszą być. Bo jakiekolwiek zwątpienie w&nbsp;dobrobyt skończyłoby się odwiedzinami knechtów i&nbsp;siepaczy o&nbsp;trzeciej nad ranem.  
W takich warunkach antymonarchistyczni blogerzy powinni przede wszystkim pamiętać, żeby ich domena nie ujawniała złych intencji. Nie powinna mieć nazw jak poniższe:

<pre class="black-bg mono">
https://krol-jest-nagi.gud
https://krol-jest-nagi.nowinki.gud
</pre>

Może natomiast nazywać się:

<pre class="black-bg mono">
https://nowinki.gud<span class="red">/krol-jest-nagi</span>
</pre>

...Ponieważ gdy działa HTTPS, to wzrok podglądaczy kończy się na ukośniku po domenie. Nie widzą tego, co na czerwono.

Oczywiście należałoby też zadbać o&nbsp;to, żeby nie dało się z&nbsp;góry uznać *całej* domeny za niepożądaną. Oprócz podstron `/krol-jest-nagi` powinna zawierać również niewinne, jak `/ku-chwale-krola` albo `/rozmyslania-o-niczym`. W&nbsp;ten sposób trudniej by było kogoś ukarać na podstawie samego odwiedzenia domeny.

Inną realną opcją mogłoby być publikowanie tekstów na *cudzych* stronach; na tyle dużych, żeby nie były tak łatwe do zmapowania.  
Przykładem mogą być wspomniane już archiwa internetowe takie jak *archive.is* albo *archive.org*, przechowujące u&nbsp;siebie treści z&nbsp;całego internetu. Ale nawet większe megafora i&nbsp;portale społecznościowe, o&nbsp;ile nie są na usługach monarchy, dałyby radę.

### Jedna domena

W przykładzie z&nbsp;udziałem Stacka istotną rolę odgrywały domeny, z&nbsp;których serwowano awatary. Pozwalały zawęzić przestrzeń do sprawdzenia, a&nbsp;ich nietypowe kombinacje umożliwiały rozróżnianie dyskusji.

Żeby zapobiec takim sytuacjom, warto zadbać o&nbsp;jak najmniejszą liczbę domen, z&nbsp;których ładują się elementy strony. A&nbsp;przynajmniej sprawić, żeby **ich zestaw był identyczny dla każdej podstrony**.

{:.post-meta .bigspace-after}
Przyznaję pokornie, że na moim blogu emotki serwowane są z&nbsp;osobnej domeny niż reszta treści. Ale myślę nad zmianami.

Należałoby też unikać *hotlinkingu*, czyli umieszczania na stronce specjalnych linków każących przeglądarkom pobrać rzeczy z&nbsp;cudzych stron.

Przykładem *hotlinkingu* byłoby okazjonalne umieszczanie elementów obrazkowych typu `<img src="cudza-strona.pl…"/>` w&nbsp;źródle własnej strony. Ktoś mógłby łatwo zmapować, że mamy gdzieś na swoim portalu *tę jedyną* podstronę ładującą obrazek od *cudza-strona.pl*.

Lepsza opcja? Pobranie obrazków z&nbsp;innej strony na swój dysk, wyraźne oznaczenie źródła, umieszczenie ich pod własną domeną.

Z powyższego względu warto też **nie korzystać z&nbsp;elementów osadzonych**, jak tweety albo filmiki z&nbsp;YouTube'a. Działają na podobnej zasadzie jak *hotlinking* obrazków i&nbsp;będą się wyróżniały w&nbsp;historii ruchu sieciowego. Pomijając już fakt, że ich strony źródłowe mogą próbować [wpływać zdalnie na ich treść](https://www.theverge.com/2022/4/6/23012913/twitter-tweet-embeds-deleted-tweets-empty-iframe-broken).

Lepsza opcja? Screeny albo cytaty, a&nbsp;pod nimi link.

### Ujednolicanie podstron

To chyba najtrudniejsza część -- jak sprawić, żeby nie dało się rozróżnić podstron na podstawie rozmiaru ładowanych elementów?

Przycinanie wszystkich elementów do jednego rozmiaru raczej nie wchodzi w&nbsp;grę, więc pozostaje **równać w górę -- dopychać pustymi danymi, aż wszystko osiągnie ten sam rozmiar**. Po angielsku takie dopychanie nosi nazwę `padding`.

Problem w&nbsp;tym, że może być to zbyt uciążliwe dla wielu osób tworzących strony.

Przykład? Jeśli jeden wpis ma sześć obrazków, a&nbsp;inny tylko dwa, to gdzieś do tego drugiego należałoby dodać cztery obrazki-zapychacze. Do tego dopchać każdy z&nbsp;realnych obrazków do maksymalnego rozmiaru.

Strasznie dużo koordynacji. Do tego konieczność istotnego przekształcania swojej strony przy każdej drobnej zmianie.

Mam tu jednak potencjalne rozwiązanie, które ułatwiłoby ujednolicanie stron -- **korzystanie ze stron jednoplikowych, będących pojedynczymi plikami HTML**.

Takie strony nie muszą być gołym tekstem. Elementy dodatkowe, takie jak obrazki czy arkusze styli, można bowiem *zagnieździć bezpośrednio w&nbsp;kodzie HTML*. W&nbsp;przypadku obrazków trzeba je [przekonwertować](https://stackoverflow.com/questions/1207190/embedding-base64-images) do postaci Base64.

Wtedy obrazki zamiast atrybutu

<pre class="black-bg mono">
src="<span class="red">ŚCIEŻKA_DO_PLIKU</span>.jpg"
</pre>

zawierałyby w&nbsp;sobie:

<pre class="black-bg mono">
src="data:image/jpeg;base64,/9j/<span class="red">DŁUGI_CIĄG_ZNAKÓW</span>"
</pre>

Takie sprowadzanie strony do jednego pliku stosuje [dodatek SingleFile](https://github.com/gildas-lormeau/SingleFile/blob/master/README.MD), można podejrzeć jego rozwiązania.

W ostateczności, mając niewielką stronę i możliwość ręcznego dodawania plików HTML, można nawet użyć SingleFile w&nbsp;roli konwertera. Otwierać po kolei swoje stronki, zapisywać z&nbsp;użyciem SingleFile do pojedynczych plików. Podmienić nimi pierwotne strony.

{:.post-meta .bigspace-after}
**Uwaga:** domyślnie SingleFile dodaje na początku pliku komentarz z&nbsp;paroma informacjami, jak data zapisania. Dla pewności można go usunąć.

Efekt rozwiązania? Każda podstrona byłaby jednym, samowystarczalnym plikiem HTML. Dużo łatwiej by było je dopchać pustymi danymi (np. długim komentarzem na końcu), żeby wszystkie miały identyczny rozmiar.

Wada rozwiązania? Wzrost rozmiaru stron. Użytkownicy będą musieli dłużej czekać, aż się wyświetlą, bo nie będzie ładowania na raty. Ale dla niektórych to niewielka cena za ochronę prywatności.

### Parę innych szlifów

W tym miejscu zbiorę parę innych luźnych pomysłów. To dyrdymały na tle najważniejszych kwestii, czyli domen i&nbsp;rozmiaru elementów. Ale zawsze coś.

Gdyby ujednolicanie rozmiaru wszystkich plików HTML było dla kogoś upierdliwe, można przynajmniej dać użytkownikom bezpieczną poczekalnię na swojej wrażliwej stronce.

Mianowicie: umieścić na serwerze takie regułki, żeby każdy użytkownik -- niezależnie od tego, z&nbsp;jakiego publicznego linku przychodzi -- dostawał stronkę o&nbsp;takim samym rozmiarze. Zawierającą **ostrzeżenie i&nbsp;zachętę do skorzystania z&nbsp;Tora lub pośrednika przed załadowaniem dalszej treści**.

Na tym etapie jeszcze byłoby za wcześnie, żeby kogoś oskarżać o&nbsp;szkalowanie króla. Dopiero kliknięcie w&nbsp;link prowadziłoby do właściwej treści. A&nbsp;na tym etapie ludzie już zostali ostrzeżeni, reszta to ich sprawa.

Chętni mogą dodatkowo namieszać, dodając **losowość**. Czasem pobierać jakiś dodatkowy element, a&nbsp;czasem nie. Takie rozwiązanie można umieścić zarówno w&nbsp;kodzie serwera, jak i&nbsp;(poprzez JavaScript) na samych podstronkach.

Taki element nie musi być widoczny dla użytkownika, może być niewielki. Przeglądarka i&nbsp;tak go pobierze, a&nbsp;podglądacze -- zobaczą rozmiar danych. Ale może im być trudniej do czegoś to przypisać.

## Zakończenie

Profilowanie stron internetowych jest zagrożeniem nieco nietypowym jak na tego bloga. Nie wydaje się czymś masowym, z&nbsp;czego notorycznie korzystałyby firmy reklamowe. Ma praktyczne zastosowanie tylko wobec niektórych stron.  
Ale, jeśli już zostanie z&nbsp;powodzeniem zastosowane, może szczególnie mocno uderzyć w&nbsp;osoby, którym zależało na prywatności.

Osobiście nie planuję wprowadzać na swoim blogu jednolitych, jednoplikowych stron czy losowych elementów. Być może komuś na świecie się to przyda. Ale ja, przy mikroskali bloga i&nbsp;luźnych tematach, tylko bym poświęcał minimalizm w&nbsp;imię [larpowania](https://pl.wikipedia.org/wiki/Live_action_role-playing) :wink: 

Rozważam natomiast serwowanie emotek wyłącznie z&nbsp;domeny `ciemnastrona.com.pl` zamiast z&nbsp;`githubassets`. Być może w&nbsp;formie wycinków z&nbsp;jednego obrazka (*sprite'ów*). To akurat by się nie kłóciło z&nbsp;prostotą, a&nbsp;nawet jej sprzyjało. Mniej domen, mniej zależności. Zobaczymy.

Na tę chwilę, gdyby ktoś nie chciał ujawniać Ciemnej w&nbsp;swoich logach, zachęcam do odwiedzania bloga przez Tor Browsera. Działa zacnie. A&nbsp;żaden admin hotspota czy stalker-hobbysta nie zobaczy w&nbsp;logach, że przeczytaliście właśnie wpis numer 92.

Do zobaczenia w&nbsp;kolejnych w&nbsp;drodze do setki! :smile:
