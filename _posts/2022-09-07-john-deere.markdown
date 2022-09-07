---
layout: post
title:  "John Deere. Kiedy to traktor kieruje tobą"
subtitle: "Oręż nowoczesnego rolnika czy kajdany chłopa feudalnego?"
description: "Oręż nowoczesnego rolnika czy kajdany chłopa feudalnego?"
date:   2022-09-07 12:00:00 +0100
tags: [Centralizacja, DRM, Hardware, Rolnictwo]
firmy: [John Deere]
category: cyfrowy_feudalizm
category_readable: "Cyfrowy&nbsp;feudalizm"
image:
  path: /assets/posts/john_deere/john-deere-baner.jpg
  width: 1200
  height: 700
  alt: Traktor John Deere z nałożoną twarzą robota z filmu Sędzia Dredd
---

Jakiś czas temu w&nbsp;Polsce miała miejsce aferka związana z&nbsp;weselem pewnego polityka. Prezentem ślubnym był na nim traktor amerykańskiej firmy John Deere. Zajmującej się produkcją sprzętu rolniczego i&nbsp;uważanej za dość prestiżową.

Ale, jak obiecałem w&nbsp;zakładce informacyjnej swojego bloga, nie będzie tutaj polskiej polityki. Podczepię się natomiast pod słowa *John Deere*, póki nie wyparowały z&nbsp;pamięci społeczeństwa. I&nbsp;napiszę coś na temat tej firmy.

Jej przypadek jest szczególnie ciekawy dla serii „Cyfrowy feudalizm”. Mamy bowiem idealny przykład użycia rozwiązań elektronicznych do zacieśnienia kontroli producenta nad sprzętem.

To krok ku rzeczywistości, w&nbsp;której rolnicy *wynajmują* zamiast *kupować* -- trochę jak za dawnego feudalizmu. Nawet jeśli nie są takiego układu świadomi, a&nbsp;za swój traktor zapłacili setki tysięcy złotych.

Jest to rzeczywistość nieco straszna, ale też fascynująca. Będą tu wątki hakowania własnych traktorów, żeby je naprawić (albo na nich zagrać w&nbsp;*Dooma*), masowe zbieranie danych rolniczych, posłuszne nam traktory open source oraz posłuszne tylko sobie traktory samojezdne.

{:.figure .bigspace-before}
<img src="/assets/posts/john_deere/john-deere-warrior.jpg" alt="Traktor John Deere z&nbsp;włączonymi światłami, zwrócony przodem do zdjęcia. Zamiast jego przedniej części nałożono głowę robota o&nbsp;groźnym wyrazie twarzy. Jego twarz ma taką samą zieloną barwę jak lakier traktora, a&nbsp;oczy są pomarańczowe jak jego światła"/>

{:.figcaption}
John Deere z&nbsp;materiałów promocyjnych plus twarz *ABC Warriora* z&nbsp;„Sędziego Dredda” z&nbsp;1995 r.

# Spis treści

* [O&nbsp;firmie](#ofirmie)
  * [Cyfrowy jelonek](#cyfrowy-jelonek)
* [Problem cyfrowej zależności](#problem-cyfrowej-zależności)
  * [Przykładowy scenariusz](#przykładowy-scenariusz)
  * [Niełatwa naprawa](#niełatwa-naprawa)
* [Prawo do naprawy. Deere kontra rolnicy](#prawo-do-naprawy-deere-kontra-rolnicy)
  * [Amerykańskie realia](#amerykańskie-realia)
  * [Elektroniczna fosa](#elektroniczna-fosa)
  * [„To dla waszego bezpieczeństwa”](#to-dla-waszego-bezpieczeństwa)
* [Deere na wschodzie](#deere-na-wschodzie)
  * [„Pomagamy Ukrainie”](#pomagamy-ukrainie)
  * [Czy mamy się czego obawiać?](#czy-mamy-się-czego-obawiać)
* [Podsumowanie](#podsumowanie)

## O&nbsp;firmie

John Deere to marka, za którą stoi korporacja *Deere and Company*. Pisząc „John Deere”, będę się w&nbsp;tym wpisie odwoływał do całej organizacji.

Firma JD ma długą historię -- jej początki sięgają 1837&nbsp;roku! Od roku 1848&nbsp;ich kwatera główna mieści się w Moline w&nbsp;stanie Illinois, na rolniczych obszarach USA.  
Przeszli długą drogę od lokalnego sklepu do wielkiej korporacji, znajdującej się w pierwszej setce największych w&nbsp;USA.

Motto? Lekka gra słów: *Nothing Runs Like a&nbsp;Deere*.  
Logo? Jelonek uchwycony w&nbsp;skoku. Zmieniało się na przestrzeni lat. Wersję żółto-zieloną mają od roku 2000.

{:.figure .bigspace-before}
<img src="/assets/posts/john_deere/deere-logo.jpg" alt="Sześć obrazków pokazujących logo firmy John Deere, skaczącego jelenia. Każda kolejna wersja wydaje się bardziej minimalistyczna niż poprzednia."/>

{:.figcaption}
Źródło: [strona firmy](https://www.deere.com/en/our-company/history/trademarks/).

Ta [zieleń i&nbsp;żółć](https://usbrandcolors.com/john-deere-colors/) -- choć wydają się kombinacją naturalną, odpowiadającą barwom pól uprawnych w&nbsp;różnych porach roku -- są przez firmę zazdrośnie strzeżone.  
W 1988&nbsp;roku po raz pierwszy je zastrzegli. Do roku 2017&nbsp;[sądzili się 40&nbsp;razy](https://corsearch.com/knowledge-base/article/court-upholds-john-deeres-trademark-for-green-and-yellow-color-combo/) z&nbsp;firmami z&nbsp;branży rolniczej, jeśli te próbowały użyć podobnych kolorów.

Właściciele JD? Aktualnie [w ponad 70%](https://money.cnn.com/quote/shareholders/shareholders.html?symb=DE&subView=institutional) fundusze inwestycyjne i&nbsp;inni inwestorzy instytucjonalni.

[Oddziały firmy](https://www.deere.com/assets/pdfs/common/our-company/about/jd-world-locations.pdf) (uwaga: spory PDF) znajdziemy na całym świecie. W&nbsp;Polsce na przykład mamy dział finansowy i&nbsp;marketingowy w&nbsp;Poznaniu.

Dokumenty z&nbsp;KRS-u pokazują, że polski Deere zaczynał jako wspólne przedsięwzięcie z&nbsp;firmą Rolimpex, ale z&nbsp;czasem zyskał samodzielność.  
Obecnie wszystkie udziały posiada spółka z&nbsp;Luksemburga. Która zapewne podlega tej głównej, amerykańskiej gałęzi.

{:.bigspace-before}
<img src="/assets/posts/john_deere/john-deere-krs.jpg" alt="Wykres pokazujący w&nbsp;formie poziomych słupków, jakie inne organizacje miały udziały w&nbsp;firmie John Deere Spółka z&nbsp;o.o."/>

{:.figcaption}
Źródło: Odpis z&nbsp;KRS-u zwizualizowany [moim autorskim skryptem]({% post_url 2021-12-14-krs-zabawy %}){:.internal}.  
*S.A. R.L* to odpowiednik spółki z&nbsp;o.o. Ostatnia ze zmian była raczej kosmetyczna, zmienili kropkę w&nbsp;nazwie udziałowca na spację.

Oprócz firm oficjalnie posługujących się nazwą John Deere są oczywiście różni oficjalni dealerzy i&nbsp;serwisy.

Czasem znajdziemy ich markę w&nbsp;nieoczekiwanych miejscach:

* Wydano klocki LEGO Technics z&nbsp;ich traktorem.
* Pod ich marką występowała między innymi drużyna e-sportowa rywalizująca w&nbsp;grze *Farming Simulator*.
* Pewien browar wypuścił limitowaną serię piwa we współpracy z&nbsp;nimi.
* Sprzedają też wszelkie możliwe gadżety. Czapki, ręczniki, kolorowanki...

Na ich stronie znajdziemy liczne zapewnienia o&nbsp;odpowiedzialności społecznej. Niczym pozycjonowanie w&nbsp;wyszukiwarce, tyle że pod ranking ESG. *Sustainability*. *Diversity*. *Equity and inclusion*.

# Cyfrowy jelonek

Choć możemy sobie wyobrażać, że życie firmy od sprzętu rolniczego kręci się wokół fabryk i&nbsp;maszyn, rzeczywistość jest nieco inna. Deere od jakiegoś czasu zwraca się ku nowinkom technicznym, chmurze, *big data*, *AI* i&nbsp;tym podobnym sprawom.

Oferują całe pakiety usług polegające na nagrywaniu tras GPS-em, analizowaniu danych rolniczych, automatyzacji pracy. Na tegorocznej konferencji CES 2022&nbsp;przedstawili nawet prototyp swojego nowego, [w pełni samojezdnego](https://ces2022.deere.com/) traktora.

W [wywiadzie dla *Verge*](https://www.theverge.com/22533735/john-deere-cto-hindman-decoder-interview-right-to-repair-tractors) główny dyrektor firmy ds. technicznych sam wspomina, że obecnie **John Deere zatrudnia więcej programistów niż inżynierów**.

Sceptyk mógłby się zastanowić -- czy cały ten pęd ku nowinkom technicznym ma solidne fundamenty? Czy nie jest tylko próbą ściągnięcia inwestorów, niejako doklejoną do głównej działalności?

Deere twierdzi, że jak najbardziej są gotowi na cyfrową transformację. W&nbsp;zakładce [„Wyższy cel”](https://www.deere.com/en/our-company/higher-purpose/) na swojej stronie piszą:

{:.bigspace}
> Our solutions are as sophisticated as a&nbsp;precisely seeded field

*Rozwiązania dopracowane jak dokładnie obsiane pole*.

Myślę że tyle faktów nam wystarczy. John Deere jest wielki i&nbsp;nowoczesny. Brzmi jak same plusy, prawda? Jednak nie po to nazwałem swój blog „Ciemna Strona”, żeby się rozpływać nad wizerunkami kreowanymi przez firmy.

Spójrzmy na trochę mniej radosne sprawy. Wątki na forach, protesty, nagłośnione problemy.

## Problem cyfrowej zależności

# Przykładowy scenariusz

Wyobraźmy sobie, że jesteśmy rolnikami. Mamy spore pole, o&nbsp;które trzeba dbać. Zaorać, obsiać, zapewne skropić jakimś chwastobójem, zebrać plony.

Dotąd całkiem nieźle prosperowaliśmy i&nbsp;kusi nas coś lepszego niż nasz zaprawiony w&nbsp;bojach, warczący traktorek. Racjonalizujemy to sobie tym, że nówka będzie inwestycją, która się zwróci. Podświadomie cieszy też to, że zazdrość zeżre naszego *somsiada*.

A zatem kupujemy wypasiony traktor od Deere'a, za cenę od [kilkudziesięciu do kilkuset tysięcy](https://www.olx.pl/rolnictwo/ciagniki/q-john-deere/) złotych, choć istnieją jeszcze droższe. Starego się pozbywamy. I&nbsp;szarżujemy naszym żółto-zielonym rydwanem po ugorach.

Pierwszy rok jest jak miesiąc miodowy i&nbsp;całkiem miło nam się go spędza. Ale pewnego razu w&nbsp;szczycie sezonu zapala się lampka i&nbsp;wyświetla się nam enigmatyczny kod błędu. Nasz potężny traktor zwalnia i&nbsp;zaczyna się wlec.

Dzwonimy w&nbsp;panice do oficjalnego serwisu, dość znacznie od nas oddalonego. Klapa, przed nami w&nbsp;kolejce do naprawy czekają inni. A&nbsp;sezon trwa, nie możemy sobie pozwolić na zwłokę.

To może spróbować samodzielnej naprawy? Przy starym traktorku się to sprawdzało.  
Jak się okazuje, niestety nie jesteśmy w&nbsp;stanie. Te od Deere'a wymagają firmowych części. **Gdybyśmy spróbowali użyć zamienników, to komputer pokładowy je wykryje i&nbsp;zablokuje możliwość korzystania z&nbsp;traktora**.

Ostatecznie idziemy wybłagać pomoc u&nbsp;sąsiada, z&nbsp;którego bida-traktora wcześniej się śmialiśmy. Co oczywiście będzie nas srogo kosztowało, bo sąsiad jest pamiętliwy. To będzie zły sezon.

Wkurzeni całą sytuacją, zaglądamy do umowy licencyjnej. A&nbsp;tam, pod nagłówkiem  *Limitation of Liability*, znajdziemy napisaną *CAPS LOCKIEM* informację, że [zrzekamy się roszczeń](https://www.deere.com/privacy_and_data/docs/agreement_pdfs/english/2016-10-28-Embedded-Software-EULA.pdf) z&nbsp;tytułu strat, jeśli wynikały one z&nbsp;działania lub awarii oprogramowania. Musimy wszystko przełknąć albo walczyć w&nbsp;sądach.

Czarny scenariusz? A&nbsp;jednak całkiem realny w&nbsp;ramach techniczno-prawnych, jakie narzuca nam firma John Deere.

# Niełatwa naprawa

W naszym problemie nie bylibyśmy odosobnieni. Przedstawiam tutaj parę dowodów anegdotycznych. Pojedyncze iskry niezadowolenia.

Na forum Elektroda znajdziemy kilkaset wątków poświęconych sprzętom JD. Celowo patrzyłem tylko na modele o&nbsp;numerach wyższych niż 6000, ponieważ mam pewność, że to te bardziej wypasione i&nbsp;elektroniczne.

Pierwsza trudność to dostęp do wiedzy. Jakiś użytkownik pytający o&nbsp;pojedynczą część do wymiany dostał między innymi link do całej, płatnej dokumentacji:

{% include comment.html
author="Użytkownik Elektrody 1"
text="Schematów z&nbsp;pierwszego linku nie da się otworzyć. Żeby to zrobić, trzeba się zalogować; a&nbsp;żeby się zalogować, trzeba zapłacić 27&nbsp;USD."
%}

{:.figcaption}
Źródło: [forum Elektroda](https://www.elektroda.pl/rtvforum/topic3914707.html#20159855).  
Drobne zmiany interpunkcyjne, skróty i&nbsp;wyróżnienia w&nbsp;cytatach -- tym i&nbsp;następnych -- moje.

No ale założmy, że jak nie ma rady, to się zapłaci. Czasem jednak wiedza -- na przykład znajomość kodów błędów -- to za mało, żeby użytkownik sam ogarnął sprawę:

{% include comment.html
author="Użytkownik Elektrody 2"
text="Raz jedzie i&nbsp;nie ma problemu, na drugi dzień z&nbsp;miejsca nie ruszy. Błąd *EPC 306057.31 Transmission enable signal faulty*  
(...)  
moja historia zakończyła się tak, że 2&nbsp;dni jeździł i&nbsp;znów przestał. Wymieniony komputer i&nbsp;problem ustał."
%}

{:.figcaption}
Źródło: [Elektroda](https://www.elektroda.pl/rtvforum/topic3689298.html#20017589).
 
Swoją drogą: Deere posiada wiele takich [kodów błędów](https://www.insidetheyard.com/john-deere-fault-codes-list/) na różne okazje.  
Czasem jednak trafi się perełka, na którą kodu nie ma. Taką [bardzo niecodzienną awarię](https://www.youtube.com/watch?v=jqaCP2AwdDA) pokazuje jeden filmik na YouTubie.  
Jest w&nbsp;nim przy okazji trochę krytyki jakości wykonania sprzętu. „Kiedyś jelonki były lepsze”.

Pod hasłem „John Deere” znajdziemy na Elektrodzie również całą dłuższą dyskusję na temat zabezpieczeń DRM. Cyfrowych przeszkadzajek stosowanych przez producenta w&nbsp;celu utrudnienia dostępu. Deere jest podawany jako jeden z&nbsp;przykładów.

{% include comment.html
author="Użytkownik Elektrody 3"
text="Każda wymieniona część wymaga bowiem rejestracji i&nbsp;autoryzacji w&nbsp;komputerze pojazdu. Wymiana samego komputera wymaga rejestracji i&nbsp;autoryzacji wszystkich pozostałych części.  
(...) kombajn po wymianie jednego z&nbsp;komputerów (bodaj sterującego hydrauliką) nie chciał się uruchomić. Najbliższy autoryzowany serwis był oddalony o&nbsp;ponad 250&nbsp;kilometrów, pracownicy mieli zaś terminy zaklepane na tydzień do przodu. Rolnik zmuszony był kupić drugi kombajn by dokończyć żniwa, podczas gdy prawie nowy John Deere stał w&nbsp;stodole."
%}

{:.figcaption}
Źródło: [wątek na temat DRM-a](https://www.elektroda.pl/rtvforum/topic3878512.html) z&nbsp;Elektrody.

A na ostatniej stronie dyskusji znajdziemy komentarz osoby, która czasem pomaga koledze-rolnikowi przy naprawach. Potwierdzający, że również polska rzeczywistość nie jest wolna od takich historii:

{% include comment.html
author="Użytkownik Elektrody 4"
text="Zmorą kombajnów np. jest „komputer” sterujący tym co kombajnista ma pod sobą i&nbsp;za plecami, czyli mechanizm koszący i&nbsp;młócący. Pada podświetlenie ekranu albo digitizer, nie widzisz co się dzieje, paru rzeczy nie ustawisz. Facet byłby w&nbsp;stanie wymienić to sam, bo to raptem kilka śrub i&nbsp;2 wtyczki; ale jedynie co producent oferuje, to wizytę <b>serwisu autoryzowanego, który najbliżej jest w&nbsp;Niemczech i&nbsp;nie ruszy się za mniej niż 5k Euro, i&nbsp;to w&nbsp;jakimś absurdalnym terminie*</b>. Finalnie zboże skosił „na pamięć”, bo swoje pola i&nbsp;maszynę zna"
%}

{:.figcaption}
Źródło tego i&nbsp;kolejnego fragmentu: [post z&nbsp;Elektrody](https://www.elektroda.pl/rtvforum/topic3878512-60.html#19931519).

Tak ma wyglądać ta nowoczesność w&nbsp;domu i&nbsp;zagrodzie? Dobrze, że przynajmniej w&nbsp;tym przypadku człowiek mógł jednak wsiąść za kółko w&nbsp;sytuacji awaryjnej. Gdyby to była któraś z&nbsp;tych całkiem samojezdnych maszyn, to byłoby pozamiatane.

Autor ma również parę uwag na temat możliwych przyczyn takiej sytuacji:

{:.bigspace}
{% include comment.html
author=" "
text="<b>zapewne wyglądało fajnie, gdy paru krawaciarzy pokazywało sobie prezentacje z&nbsp;wykresami spodziewanych zysków</b>. Tyle że dla nich to tylko maszyna, która postoi sobie tydzień i&nbsp;poczeka na serwis, dla jej własciciela to utrata zysków za własne plony, kary za niewywiązanie się z&nbsp;umów, przepłacenie kogoś kto umówioną robotę wykona za niego -- o&nbsp;ile uda mu się kogoś z&nbsp;wolnymi mocami przerobowymi znaleźć."
%}

Przykłady można mnożyć. Takie pojedyncze iskry niezadowolenia błyskały również w&nbsp;USA. Aż namnożyło się ich tyle, że wznieciły płomienie rebelii. Zrzeszonej pod hasłem walki o&nbsp;*prawo do naprawy* (ang. *right to repair*).  
W USA już od kilku lat trwają głośne sądowe batalie z&nbsp;Deere'em. Przyjrzyjmy się im.

## Prawo do naprawy. Deere kontra rolnicy

Amerykańscy rolnicy nie są w&nbsp;ciemię bici i&nbsp;próbowali jakoś walczyć z&nbsp;zależnością od producenta. Na chwilę jeszcze zostanę w&nbsp;świecie analogowym i&nbsp;pokażę ich prawnicze boje.

# Amerykańskie realia

Uprzedźmy szablonowy zarzut z&nbsp;internetowych komentarzy. „Mamy wolny rynek! Ktoś tym rolnikom każe trzymać się Deere'a?”.

Może na przykład brak alternatyw? Na rynku amerykańskim ta firma miała niedawno [ponad 50% udziałów w&nbsp;segmencie dużych ciągników i&nbsp;ponad 60% w&nbsp;segmencie kombajnów](https://www.farm-equipment.com/articles/15962-).

Doszło nawet do tego, że amerykański urząd antymonopolowy [zablokował](https://www.justice.gov/opa/pr/deere-abandons-proposed-acquisition-precision-planting-monsanto) odkupienie przez Deere'a firmy Precision Planting LLC -- rolniczego działu kontrowersyjnej firmy Monsanto.  
Uzasadniali to tym, że przejęcie doprowadziłoby do całkowitej monopolizacji w&nbsp;segmencie maszyn od zasiewu precyzyjnego. Deere tworzył bowiem dedykowane maszyny do tego celu, zaś Precision Planting nakładki do istniejących.  
Ostatecznie PP nabyła inna korporacja, mniejszy konkurent Deere'a. A&nbsp;JD krótko po tym [pozwał](https://www.reuters.com/article/us-deere-patentinfringement-idUSKCN1IX5L7) zarówno nowych właścicieli, jak i&nbsp;swój niedoszły nabytek.

Poza procentowymi udziałami dochodzi bardziej subtelna kwestia geograficznej dostępności części i&nbsp;napraw. Już pod niejednym artykułem widziałem komentarze takie [jak ten](https://www.youtube.com/watch?v=UEm31xgzqLE&lc=UgwPI6OXc0W9akf7rel4AaABAg) (tłumaczenie moje):

{:.bigspace}
> Czasami najbliższy sklep znajduje się 20-30 minut jazdy od nas, zaś konkurencja Deere'a jeszcze dalej. I&nbsp;mówię tu o&nbsp;jeździe z&nbsp;prędkością 120&nbsp;km/h, przy prawie zerowym ruchu na drodze. Mają „na pewno nie monopol, słowo” w&nbsp;wielu miejscach, w&nbsp;których intensywnie korzysta się z&nbsp;traktorów. I&nbsp;są jedyną realistyczną opcją.

Jasne, to tylko anegdotyczne przykłady. Nie potwierdzę ich na razie danymi, bo musiałbym poświęcić tygodnie na wczytywanie się w&nbsp;sprawę, szukanie źródeł itp. Czego nie chcę, bo parę innych tematów bardziej mnie kusi.

Ale nawet jeśli nie przekonują nas argumenty sugerujące dominację JD, dopuśćmy przynajmniej możliwość, że rolnicy są świadomymi ludźmi. Z&nbsp;jakiegoś powodu jednak poświęcają czas na walkę z Deere'em, zamiast po prostu pójść do konkurencji.

# Elektroniczna fosa

W sprawie Deere'a duże znaczenie ma fakt, że uzależnili maszyny od komputera. Oprogramowanie rządzi się bowiem odrębnymi przepisami niż śrubki i&nbsp;zębatki. Dotyczy go prawo autorskie. Dostaje się na nie licencję, która narzuca ograniczenia.

Gdy bez wspomnianej licencji nie możemy korzystać z&nbsp;komputera, zaś bez komputera nie skorzystamy z&nbsp;urządzenia, to można dojść do dość ponurego wniosku -- **tych traktorów nie da się nabyć na własność. Można jedynie dostać na nie licencję**. Mocnymi słowami skwitował to Kyle Wiens, założyciel znanej firmy od napraw smartfonów:

{:.bigspace-after}
> It’s John Deere’s tractor, folks. You’re just driving it

Rolnicy walczący o&nbsp;możliwość naprawy musieli na początek dowieść, że grzebanie w&nbsp;oprogramowaniu traktora nie byłoby jego hakowaniem, a&nbsp;zatem przestępstwem. W&nbsp;USA regulują takie sprawy dość rygorystyczne przepisy znane pod zbiorczą nazwą *DMCA* (*Digital Millenium Copyright Act*).

Tę bitwę wygrali. Na poziomie federalnym [wprowadzono w&nbsp;2015 roku wyjątek]( https://www.forbes.com/sites/jasonbloomberg/2017/04/30/john-deeres-digital-transformation-runs-afoul-of-right-to-repair-movement/) od surowych przepisów antyhakerskich. Właściciele mogli majstrować przy pojazdach, o&nbsp;ile było to w&nbsp;celach prywatnych i&nbsp;niekomercyjnych.

Deere się nadął, naindyczył i&nbsp;próbował skontrować nowe przywileje rolników własnymi ograniczeniami:

1. Podkreślili, że przepis daje możliwość majstrowania jedynie właścicielom i&nbsp;nie mogą upoważniać do tego zewnętrznych warsztatów. Czyli *de facto* tych, którzy byliby w&nbsp;stanie naprawić ich traktory.
2. Zastrzegli sobie prawo do kontrolowania dostępu do informacji potrzebnych do naprawy pojazdów.

   Argumentowali to między innymi troską o&nbsp;zgodność z&nbsp;przepisami dotyczącymi emisji spalin. Sprytny zabieg z&nbsp;ich strony, ponieważ to całkiem osobne przepisy. Niezależne od prawa autorskiego, które przestało być im na rękę.

3. Zmienili warunki licencyjne. Nabywcy ich pojazdów musieli zobowiązać się do korzystania z&nbsp;certyfikowanych programów do diagnostyki i&nbsp;napraw.  
   Oczywiście dealerzy Deere'a trzymali wspomniane produkty po swojej stronie i&nbsp;ani myśleli się nimi dzielić.

Ogniska buntu jednak nie zgasły, a&nbsp;walka toczyła się dalej na poziomie poszczególnych stanów.

W przypadku Kalifornii [wynik był niekorzystny](https://www.vice.com/en/article/kz5qgw/california-farm-bureau-john-deere-tractor-hacking-right-to-repair), bo grupa formalnie reprezentująca rolników ugięła się i przystała na wersję proponowaną przez Deere'a.  
JD zobowiązał się udostępnić do stycznia 2021 roku instrukcje i&nbsp;narzędzia diagnostyczne. Ale w&nbsp;zamian utrzymali w&nbsp;mocy zakaz majstrowania przy cyfrowych blokadach. Czyli w&nbsp;praktyce mało co się zmieniło.

Ale walka trwała, a&nbsp;Deere mógł odnieść wrażenie, że duch czasów jest zwrócony przeciwko nim. W&nbsp;2021 roku zostało wydane prezydenckie [rozporządzenie wykonawcze](https://www.theverge.com/2021/7/9/22570826/president-joe-biden-executive-order-right-to-repair) nakazujące wziąć się porządniej za kwestię prawa do samodzielnej naprawy. Wprost zostaje w&nbsp;nim wymieniony przypadek sprzętów rolniczych.

Na początku 2022&nbsp;roku do kolekcji pozwów zbiorowych przeciw Deere'owi dołączyły [dwa kolejne](https://www.theregister.com/2022/01/25/john_deere_right_to_repair_lawsuits/), zarzucające im, że ich sztuczne ograniczenia naruszają przepisy antymonopolowe. W&nbsp;ich treści przytoczono fakt, że Deere **z działalności związanej z&nbsp;naprawami zarabia od 3&nbsp;do 6&nbsp;razy więcej niż ze sprzedaży maszyn**.  
Deere ogłosił wtedy, że od maja udostępni ludziom narzędzia diagnostyczne, do której dotąd miały wgląd tylko licencjonowane serwisy. Kolejne ustępstwo, ale bez rewolucji.

Tymczasem [łączna liczba pozwów przekroczyła&nbsp;10](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2022/06/02/right-repair-lawsuits-john-deere).

{% include info.html
type="Przydatne pojęcie"
text="Takie sztuczne bariery, które nie pozwalają zaistnieć konkurencji i&nbsp;uwiązują klientów do konkretnej firmy, po angielsku nazywa się powszechnie *moats* (dosł. *fosy*, jak te wokół zamków; po polsku zapewne *bariery wejścia*).  
Dzięki postawieniu na elektronikę Deere nie miał problemów z&nbsp;tym, żeby raz za razem iść na kompromis w&nbsp;kwestii fizycznych instrukcji oraz części. Ich fosa i&nbsp;tak już od jakiegoś czasu była cyfrowa. Mając wyłączność na komputery, mają pełną kontrolę."
%}

A jak żyli z&nbsp;tymi zakazami i&nbsp;blokadami rolnicy oraz niezależne warsztaty? W&nbsp;końcu spór ciągnął się przez wiele lat.  
Odpowiedź: niektórzy z&nbsp;nich **pobierali zagraniczną, piracką wersję oprogramowania do serwisowania traktorów**. Ryzykując utratę gwarancji, ale zyskując choć trochę autonomii. Od strony prawnej byli kryci dzięki wspomnianemu wcześniej wyjątkowi od przepisów *DMCA*.

Do sprawy tych programów niedługo wrócę. A&nbsp;w międzyczasie zainteresowani mogą poczytać opis po polsku w&nbsp;wykonaniu [Sekuraka](https://sekurak.pl/w-usa-crackuja-traktory-za-pomoca-polskiego-i-ukrainskiego-softu/) albo [Zaufanej Trzeciej Strony](https://zaufanatrzeciastrona.pl/post/hakowanie-warunkiem-przezycia-o-lamaniu-zabezpieczen-ktore-ratuje-pacjentow/#attachment_35917) (ten drugi fajnie porusza szerszą kwestię hakowania motywowanego etyką).

# „To dla waszego bezpieczeństwa”

Posłuchajmy też drugiej strony. Deere argumentuje bowiem, że są ważne przyczyny, dla których ogranicza możliwość samodzielnego majstrowania przy traktorach. Uważa, że rolnicy wykorzystaliby to do złych celów:

* Nieuprawnione modyfikacje mogłyby sprawić, że ktoś przekroczy limity prędkości.

  ...Hmm, ale czy nie mamy od tego przepisów ruchu drogowego?  
  Gdyby ktoś wziął udział w&nbsp;nocnych, nielegalnych wyścigach traktorów, to zapewne zostałby złapany w&nbsp;taki sam sposób jak klasyczni użytkownicy tuningowanych aut.

* Mogłyby też sprawić, że obejdziemy ograniczenia emisji CO<sub>2</sub>.

  Jak wyżej. Kwestia łapania za nadmierne emisje już jest uregulowana w&nbsp;prawie.

Można odnieść wrażenie, że Deere trochę wychodzi przed szereg, chce być *bardziej prawy niż prawo*. Oczywiście możliwe również, że po prostu nie chcą luzować kontroli. W&nbsp;końcu zarabiają na swojej siatce dealerów.

Ochrona rolników przed samymi sobą to jedno. Ale Deere twierdzi, że  ich elektroniczne blokady chronią również przed hakerami.  
Ich maszyny są podłączone do globalnej sieci. Wyobraźmy sobie tylko -- jakiś niegodziwy haker przejmuje kontrolę nad całą flotą traktorów, świat staje w&nbsp;obliczu niespotykanego kryzysu żywnościowego.

„Tam w&nbsp;internecie są źli ludzie. Z&nbsp;nami jesteście bezpieczni. Nie wychodźcie poza te kraty”.

Wnikliwy obserwator mógłby zapytać: „No dobra, zagrożenie hakerskie. Aaale... czy ono przypadkiem nie wynika z&nbsp;tego, że daliście traktorom łączność z&nbsp;internetem?”. Tym niemniej argument miał jakieś ręce i&nbsp;nogi.  
Uciął je jednak w&nbsp;dość spektakularny sposób australijski haker o&nbsp;pseudonimie Sick Codes. Już od jakiegoś czasu skupiał się na maszynach Deere'a i&nbsp;walczył z&nbsp;jego zabezpieczeniami, żeby sprawdzić ich solidność.

Po drodze odkrył między innymi, że **każdy mógł łatwo uzyskać dostęp do danych właścicieli traktorów. [Łącznie z&nbsp;ich adresami](https://www.youtube.com/watch?v=hqablgjQ02g)**. Wynikało to ze słabych zabezpieczeń bazy łączącej numery identyfikacyjne traktorów z&nbsp;informacjami szczegółowymi. Wystarczyło ustawienie prostych automatycznych regułek pytających o&nbsp;kolejne numery, żeby wyciągnąć wszystko.  
Szczegóły techniczne -- dla osób, które rozumieją te sprawy -- opisał [na swojej stronie](https://sick.codes/leaky-john-deere-apis-serious-food-supply-chain-vulnerabilities-discovered-by-sick-codes-kevin-kenney-willie-cade/).

Kiedy próbował zgłosić lukę, odkrył że firma nie posiada oficjalnego kanału na takie sprawy. W&nbsp;mailu próbowali go najpierw skierować do działu obsługi social mediów. Kiedy napisał, że to raczej nie będzie najlepsze miejsce, dostał wreszcie jakiegoś maila wewnętrznego. Powoli i&nbsp;opornie.

Po zgłoszeniu firma zbagatelizowała sprawę w&nbsp;oficjalnym komunikacie, twierdząc wbrew faktom, że nie było dostępu do żadnych osobistych informacji. Co więcej, przed wydaniem artykułu nagłaśniającego sprawę opublikowali -- *z oficjalnego konta* -- tweeta w&nbsp;prześmiewczym stylu:

{% include comment.html
source="twitter"
author="John Deere"
text="Prognoza na ten tydzień: od trzech do ośmiu centymetrów nonsensu."
%}

{:.figcaption}
Źródło: [tweet JD](https://nitter.net/JohnDeere/status/1383925815092518918#m), tłumaczenie i&nbsp;konwersja moje.  
Gdyby Nitter nie działał, to zmieńcie *nitter.net* z&nbsp;adresu na *twitter.com*.

A jednocześnie wrzucili ogłoszenie, że [poszukują speca](https://www.youtube.com/watch?v=rB_SleNKBus) od spraw cyberbezpieczeństwa. Dość pilnie, co sugeruje capslockowe *RIGHT NOW*.

W tym roku nastąpił kolejny przełom.  
Sick Codes przełamał zabezpieczenia i&nbsp;zyskał pełną kontrolę nad komputerem pokładowym w&nbsp;traktorze Deere'a.  
I, jak na każdego prawilnego hakera przystało, uruchomił na nim grę Doom. A&nbsp;właściwie jej moda utrzymanego w&nbsp;klimatach rolniczych.

{:.figure .bigspace-before}
<img src="/assets/posts/john_deere/john-deere-doom.jpg" alt="Zdjęcie pokazujące terminal z&nbsp;traktora John Deere, na którym wyświetlony jest obraz z&nbsp;gry Doom, starej strzelanki w&nbsp;widoku pierwszoosobowym"/>

{:.figcaption}
Źródło: [filmik](https://nitter.net/sickcodes/status/1558878687642402816#m) od Sick Codes.

Podczas swojej paruletniej przygody Sick Codes dokładnie poznał systemy operacyjne i&nbsp;programy napędzające maszyny Deere'a. *Dopracowane jak dokładnie obsiane pole*. Odkrył parę ciekawych faktów:

* Część traktorów napędza stara wersja systemu Windows CE, powszechnie uznawanego za słabo zabezpieczony.
* Inne napędza system Linux, w&nbsp;wersji komercyjnej oferowanej przez firmę Wind River. Również stary.
* Każda część systemu ma dostęp do wszystkiego, brak podziału na strefy bezpieczeństwa (*everything runs as root*).

Czyli po ludzku: żeby włamać się do systemów, nie trzeba by było cudów nauki. Są stare, więc już rozpracowane, a&nbsp;sposobów na włamanie jest więcej niż przy nowych. Zaś po włamaniu łatwo przejąć kontrolę.  
Okazuje się, że ta potężna krata, którą John Deere chciał nas osłonić przed złym światem, była zrobiona z&nbsp;cienkich trzcin. Zdeterminowany napastnik i&nbsp;tak by ją sforsował.

Jak w&nbsp;tym świetle oceniać zapewnienia Deere'a o&nbsp;tym, że ich zabezpieczenia to ostatni bastion chroniący nas przed potencjalnym kryzysem żywnościowym?

## Deere na wschodzie

Sprawy toczące się w&nbsp;USA mogą nas ciekawić, ale dość łatwo je potraktować jak egzotyczną ciekawostkę. Czas zatem na spory przeskok geograficzny i&nbsp;sprawy związane z&nbsp;Ukrainą, a&nbsp;nawet Polską.

# „Pomagamy Ukrainie”

Pod twittem Sick Codesa na temat złamania zabezpieczeń Deere'a znajdziemy o&nbsp;dziwo paru użytkowników wyciągających to przeciwko autorowi. „Rosja będzie ci wdzięczna”.  
Skąd takie teksty? To dlatego, że John Deere miał niedawno swój krótki epizod w&nbsp;trwającej wojnie Rosji z&nbsp;Ukrainą.

Główny artykuł z CNN (tutaj jego omówienie z&nbsp;*[The Register](https://www.theregister.com/2022/05/02/ukrainian_tractors_deere)*) wspomina, że ukraińska firma Agrotek-Invest -- autoryzowany dealer Johna Deere'a -- została okradziona przez Czeczenów. Zabrali sprzęt rolniczy wart 5&nbsp;milionów dolarów.

Dealer zgłosił to producentowi. A&nbsp;John Deere wyśledził wywiezione traktory przez GPS, a&nbsp;następnie zdalnie je zablokował. Zarówno artykuł CNN, jak i&nbsp;opowiadające o&nbsp;sprawie wątki z&nbsp;Twittera przedstawiają to jako rzecz pozytywną, wkład w&nbsp;wojnę po słusznej stronie.

Ogólny, pozytywny dla firmy przekaz uzupełniają też prywatne twitty, pokazujące zdjęcia traktorów ciągnących porzucone rosyjskie czołgi. Nie brak jednak sceptyków.

{:.figure .bigspace}
<img src="/assets/posts/john_deere/john-deere-ukraina.jpg" alt="Tweet pokazujący kilka zdjęć, na których żółto-zielone traktory John Deere holują porzucone rosyjskie czołgi. Pod spodem znajduje się jakiś usunięty tweet, a&nbsp;pod nim odpowiedź, w&nbsp;której autor pisze, że część zdjęć może być ustawiona w&nbsp;celach PR-owych, choć nie kwestionuje ich prawdziwości."/>

Jasne, rozumiem. Mgliste obawy przed centralizacją schodzą na dalszy plan, gdy porównamy to z&nbsp;rabunkami albo barbarzyńskim ostrzeliwaniem pól pociskami, do którego posunęli się Rosjanie.  
Ale nie bądźmy dziećmi. Proponuję nie dać się ponieść wizji opiekuńczej firmy, która wymierza sprawiedliwość złoczyńcom. Parę argumentów sprowadzających na ziemię:

1. Te traktory zostały skradzione od dealera.

   Z&nbsp;tego co rozumiem, z&nbsp;punktu widzenia Deere'a nie był to zatem gest uprzejmości wobec jakiegoś losowego ukraińskiego rolnika. Było to raczej bliższe ochronie własnych interesów.

2. Jest niemała szansa, że traktory i&nbsp;tak zostały zhakowane i&nbsp;przejęte.

   Nawet gdyby Sick Codes nie obszedł publicznie zabezpieczeń. W&nbsp;końcu już wcześniej, niezależnie od niego, pewne zabezpieczenia Deere'a obchodzili sami rolnicy. A&nbsp;sprzęt drogi, więc Rosjanom opłacałoby się wynajęcie jakiegoś hakera.

A skoro o&nbsp;tym mowa... Poprzednio wstrzymałem się z ujawnieniem, skąd rolnicy amerykańscy brali piracką wersję oprogramowania. A&nbsp;prawda jest taka, że pochodzi ona [z&nbsp;Polski i&nbsp;Ukrainy](https://sekurak.pl/w-usa-crackuja-traktory-za-pomoca-polskiego-i-ukrainskiego-softu/).  
To pewien dowód na to, że model producenta jednak tak nie do końca się tu przyjął. No i&nbsp;piękny przypadek współpracy wschodu i&nbsp;zachodu ponad podziałami. Tylko że nieco mniej atrakcyjny PR-owo dla Deere'a.

Podsumowując: krytykowanie Sick Codesa uważam za odwracanie kota ogonem, bo on tylko nagłośnia problem obecny od dawna. Zaś JD korzysta z&nbsp;sytuacji, ocieplając wizerunek swojej kontroli nad sprzętem.

Kontroli, która -- kiedy spojrzymy poza sytuację ukraińską -- powinna nas cholernie niepokoić. **Deere jest w&nbsp;stanie zdalnie zablokować maszyny**.  
Tutaj dotyczyło to dealera, więc nie mogę powiedzieć na sto procent, czy zachowuje taką samą kontrolę po tym, jak sprzęt zostaje sprzedany użytkownikom.

Ale jeśli tak jest albo będzie?  
Wystarczyłaby komenda wysłana z&nbsp;centrali firmy -- niekoniecznie w&nbsp;złych intencjach, ale choćby przez błąd programisty -- a&nbsp;traktory zostaną uziemione, produkcja żywności stanie. Takie awarie elektroniki już się zdarzały, choćby w&nbsp;przypadku [zamków do drzwi](https://www.theregister.com/2017/08/11/lockstate_bricks_smart_locks_with_dumb_firmware_upgrade/).

Stąpamy po kruchym gruncie. 

# Czy mamy się czego obawiać?

Przyznaję szczerze, że rolnikiem nie jestem i&nbsp;o temacie wiem tyle, co wyczytałem. Podejrzewam, że spora część moich czytelników może powiedzieć to samo.  
Znalazłem też [informację](https://www.statista.com/topics/3668/european-tractor-market/#topicHeader__wrapper), że kilka lat temu udziały Deere'a w&nbsp;rynku europejskim nie przekraczały okolic 19%. Być może zatem dominacja cybertraktorów nam nie grozi, a&nbsp;sytuacja jest stabilna? Warto się tym przejmować?

Pamiętajmy jednak, że precedensy mają znaczenie. Jeśli inni producenci zobaczą, że model Deere'a się sprawdza i&nbsp;nikt się nie sprzeciwia takim praktykom, to go skopiują.  
Wtedy czeka nas wysyp kolejnych „kupionych, ale wynajmowanych” traktorów. Potencjalnie słabo zabezpieczonych, cały czas wpiętych do sieci.

Poza tym możliwe, że w&nbsp;dłuższym horyzoncie czasowym udział Deere'a będzie tylko rósł wraz z&nbsp;upadkami konkurencyjnych firm. W&nbsp;Polsce mamy chociażby lukę po Ursusie:

{:.figure .bigspace}
<img src="/assets/posts/john_deere/john-deere-ursus.jpg" alt="Zrzut ekranu tweeta pokazującego dwa zdjęcia polskich polityków na tle traktorów John Deere oraz opisujący, że jeszcze w&nbsp;2016 roku Ursu miał milionowe zyski, a&nbsp;obecnie jest w&nbsp;upadłości, zaś politycy robią zdjęcia z&nbsp;traktorami Johna Deere'a. Dane uzytkowników, oczy i&nbsp;aluzje polityczne zostały zakryte."/>

Osobna kwestia -- niezwiązana z&nbsp;prawem do naprawy, więc nie poruszana dotąd w&nbsp;tym wpisie -- to połączenie z&nbsp;chmurą i masowe zbieranie danych rolniczych.  
Dał mi do myślenia pewien [komentarz](https://www.youtube.com/watch?v=UEm31xgzqLE&lc=Ugz9U6B2pXSmi9qPMc14AaABAg) z&nbsp;YouTube'a (gdyby link się kiedyś zmienił: to ten zaczynający się od słów „*I think of John Deere as the Apple...*”). Tak, perełki można znaleźć w&nbsp;najmniej spodziewanych miejscach.

Gromadzenie danych dotyczących wymiarów pól, zasiewów, zbiorów itp. jest promowane jako rozwiązanie umożliwiające rolnikom poprawienie wydajności.  
Ale pamiętajmy, że najwięcej skorzysta na tym Deere, bo wszystkie dane lecą do jego chmury. Zastrzega sobie prawo do [dzielenia się nimi](https://www.deere.com/en/privacy-and-data/data-services/index.html):

> We may also share in aggregate, statistical form, non-personal information with our partners, affiliates or advertisers.

OK. Brak danych poszczególnych osób, tylko zagregowane. Ale mam wrażenie, że to nadal kopalnia informacji.

Wyobrażam sobie na przykład, że jakiś fundusz rozpozna po danych na temat rozmiarów pól i&nbsp;upraw, że jakiś region dynamicznie się rozwija. I&nbsp;podkupią tereny wokół niego, żeby później je sprzedawać po zawyżonych cenach.

Poza tym w&nbsp;ten sposób giełdowi potentaci mogliby zobaczyć, że w&nbsp;jakimś kraju jest nieurodzaj. **Dowiedzieliby się o tym w&nbsp;pierwszej kolejności, wcześniej niż władze tegoż kraju**. Bo tuż po tym, jak kombajny przejadą przez pola.  
Wiedząc o&nbsp;nieurodzaju, fundusze mogłyby zacząć grać na spadki, widząc pewny zysk. Zaś eksporterzy, wiedząc że kraj będzie zmuszony uzupełnić u&nbsp;nich zapasy, mogą celowo podwyższać ceny.

Możliwości nadużyć jest sporo i&nbsp;wszystkie mrożą krew w&nbsp;żyłach. To trochę jak zawłaszczenie rolnictwa przez finansjerę.  
**Nie wszyscy jesteśmy rolnikami, ale wszyscy musimy jeść**. Dlatego myślę, że jak najbardziej leży w&nbsp;naszym interesie kwestionowanie ryzykownych wizji przyszłości.

## Podsumowanie

Sprawa Deere'a pokazuje nam, że współczesne rolnictwo idzie za trendami technologicznymi obecnymi w&nbsp;innych branżach. Które, niestety, mają pełno ciemnych stron.

Ciągła łączność internetowa i&nbsp;zależność od centrali, zbieranie danych na masową skalę, odbieranie kontroli nabywcom. A&nbsp;przy tym dziadowanie na zabezpieczeniach. W&nbsp;takich warunkach zorganizowany atak hakerski mógłby skutecznie rozwalić bezpieczeństwo żywnościowe.

Kojarzy mi się to nieco ze słabością upraw monokulturowych. Pojawi się jedna rzecz, na którą gatunek jest mało odporny, a&nbsp;pogrom gotowy. Przed takim scenariuszem może nas ochronić zróżnicowanie i&nbsp;odejście od centralizacji.

Jednocześnie nie szedłbym w&nbsp;interpretacje spiskowe. Istotnie, cyfrowe transformacje w&nbsp;takim wydaniu prowadzą do rozmycia pojęcia własności. Ale rozum sugeruje, że wynikają zapewne z&nbsp;chęci maksymalizacji zysków, a&nbsp;nie z&nbsp;rozkazów jednego szwajcarskiego *think-tanku*.

Jeśli też wolicie podejście racjonalne, to polecam kilka polskich i&nbsp;angielskich terminów ekonomicznych. Pomogą znaleźć na forach czy Twitterze więcej podobnych aferek.

* Wyciąganie pieniędzy nawet po sprzedaniu produktu? *Rent-seeking*.
* Trzymanie ludzi w&nbsp;obrębie własnych, niekompatybilnych z&nbsp;resztą świata ekosystemów? *Walled gardens*.
* Dominacja nad rynkiem i&nbsp;dyktowanie (niekorzystnych) warunków? *Monopole*, *oligopole*, *kartele*.
* Wspomniane już sztuczne bariery blokujące konkurencję? *Moats* oraz *competition*.

{% include info.html
type="Podobne wpisy"
text="W moim wpisie na temat <a href='/cyfrowy_feudalizm/2021/06/12/mcdonalds-maszyny'>maszyn do lodów</a>{:.internal} w&nbsp;restauracjach McDonalds's znajdziemy podobną zależność od autoryzowanych serwisów. Łatwe uleganie awariom, niezrozumiałe kody błędów, licencja narzucająca konkretną firmę od napraw.  
Z kolei wpis na temat <a href='/cyfrowy_feudalizm/2021/07/26/intel-management-engine'>Intel Management Engine</a>{:.internal} pokazuje korporacyjny taniec na ostrzu noża -- wprowadzanie do produktów elementu elektronicznego, który daje firmie zyski (tu: od potentatów filmowych chcących zabezpieczeń antypirackich). I&nbsp;który jednocześnie może być furtką dla hakerów."
%}

Centralizacja to globalny trend, więc trudno z&nbsp;tym walczyć. Ale, jeśli ktoś tu jest rolnikiem, zawsze może głosować portfelem. Trzymać się analogowych sprzętów. Dawać producentom sygnały, że ceni niezawodność bardziej niż bajery. Wyłączyć dzielenie się danymi.
  
Kto wie, być może kiedyś w&nbsp;odpowiedzi na zachłanność firm upowszechnią się nawet [traktory open source](https://civileats.com/2022/04/27/right-to-repair-open-source-tractors-john-deere-oggun-farms-profitability-technology/) z&nbsp;wymiennymi, standardowymi częściami, wspomagane [otwartymi systemami GPS](https://www.youtube.com/watch?v=iN2cZ8avHag)?  

Nie będą miały ładnej zielono-żółtej barwy, żeby nie dostać pozwem od Deere'a. Nie będą pewnie oferowały analizowania danych w&nbsp;chmurze, sztucznej inteligencji ani samojezdności, przynajmniej na początku. Nie zrobią ich oficjalnego modelu z&nbsp;klocków LEGO.  
Ale mimo to -- a&nbsp;może właśnie dlatego -- warto dać im szansę.

