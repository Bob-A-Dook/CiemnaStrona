---
layout: post
title:  "BadTube. Ciemne strony YouTube'a (cz. 2)"
subtitle: "O rządach maszyn i reklamodawców."
description: "O rządach maszyn i reklamodawców"
date:   2022-04-18 18:10:00 +0100
tags: [Centralizacja, Internet, Manipulacja]
firmy: [Google, YouTube]
category: google
category_readable: "Google – kolorowy czarny charakter"
image: "youtube2/google-boty.jpg"
image-width: 1200
image-height: 700
---

Czas na drugi wpis na temat YouTube'a!

Poprzednio [zobaczyliśmy]({% post_url 2022-02-20-youtube-viacom-elsagate %}){:.internal} początki tej popularnej platformy, moment jej wykupienia przez Google'a oraz pierwsze większe kontrowersje.

Jedną z&nbsp;nich była *afera ElsaGate*. YouTube zadziwiająco niechętnie podszedł do usuwania spamowych filmików, kierowanych do najmłodszych i&nbsp;zawierających elementy przemocy oraz fetyszu. Niewykluczone, że miała na to wpływ ich oglądalność i&nbsp;wysokie obłożenie reklamami (będącymi dla YT źródłem zysku).

Pisałem również o&nbsp;tym, że YouTube woli zostawić moderację automatycznym systemom, a&nbsp;nie ludzkim moderatorom. Mimo że -- jak widzieliśmy -- analityk z&nbsp;paroma skryptami potrafił zdziałać całkiem sporo, nawet bez dostępu do kulis YouTube'a.  
Konieczność przy ich rozmiarach? A&nbsp;może chęć oszczędzenia za wszelką cenę na ludzkich moderatorach? 

W tym wpisie dokładniej przyjrzymy się tej wszechobecnej automatyzacji i&nbsp;jej ciemnym stronom. Zobaczymy też wyraźne -- i&nbsp;coraz intensywniejsze -- dociskanie niezależnych twórców i&nbsp;zwrot ku partnerstwom z&nbsp;korporacjami. Tym razem wpis będzie ułożony bardziej tematycznie niż chronologicznie.

Poprzedni wpis obejmował 12&nbsp;lat z&nbsp;życia platformy, ten obejmuje niecałe 5. A&nbsp;jednak, jak zobaczycie, aferek będzie więcej.

<img src="/assets/posts/youtube2/google-boty.jpg" alt="Kadr z&nbsp;filmu animowanego Blame, pokazujący robota z&nbsp;twarzą podobną do człowieka, próbującego wymierzyć cios postaci stojącej na pierwszym planie. Na czole robota naklejono logo YouTube'a, zaś w&nbsp;jego szponiastej dłoni znajduje się napis 'Banned'. Postać na pierwszym planie to popularny mem typo Wojak - krzycząca i&nbsp;płacząca postać w&nbsp;okularach."/>

{:.figcaption}
Źródło: anime „Blame!”, przeróbki moje.

# Spis treści

* [Systemy YouTube'a](#systemy-youtubea)
* [YouTube Rewind 2018](#youtube-rewind-2018)
* [Banowanie i&nbsp;demonetyzacja](#banowanie-idemonetyzacja)
  * [Różne rodzaje kar](#różne-rodzaje-kar)
  * [Demonetyzacja](#demonetyzacja)
  * [Naruszenie Content ID](#naruszenie-content-id)
  * [Bany](#bany)
* [Money, money, money...](#money-money-money)
  * [Wyższa poprzeczka dla monetyzacji](#wyższa-poprzeczka-dla-monetyzacji)
  * [Przymusowe reklamy u&nbsp;wszystkich](#przymusowe-reklamy-uwszystkich)
  * [Zmiana zasad weryfikacji](#zmiana-zasad-weryfikacji)
* [2021&nbsp;– nagroda dla pani prezes](#2021-nagroda-dla-pani-prezes)
* [Wyłączenie negatywnych ocen](#wyłączenie-negatywnych-ocen)
* [Co możemy zrobić](#co-możemy-zrobić)
  * [Ochrona danych](#ochrona-danych)
  * [Youtube-dl](#youtube-dl)
  * [Alternatywne apki i&nbsp;strony](#alternatywne-apki-istrony)
  * [Gdy jesteśmy twórcami](#gdy-jesteśmy-twórcami)
* [Podsumowanie](#podsumowanie)

## Systemy YouTube'a

Zanim przejdziemy do aferek, spójrzmy krótko na automatyzację według YouTube'a. Jest to kilka systemów pełniących osobne funkcje.

Wszystkie swoje systemy nazywają oczywiście *AI*, czyli sztuczną inteligencją. Ale to pojęcie marketingowe. Można myśleć o&nbsp;nich po prostu jak o&nbsp;elastycznych algorytmach, stworzonych na podstawie obszernych danych YouTube'a.

Ma takich automatów kilka:

* Polecarka

  Podczas oglądania podpowiada nam podobne filmy.
  Jej elastyczność (*AI-owatość*?) polega na tym, że dopasowuje się do tego, co do tej pory oglądaliśmy.  
  Bywa też nazywana narzędziem radykalizacji, bo z&nbsp;jakiegoś powodu lubi podsuwać kontrowersje i&nbsp;teorie spiskowe. Które mogą wciągnąć ludzi na dłużej, prowadząc do pokazania [większej liczby reklam](https://www.pcmag.com/news/does-youtubes-algorithm-lead-to-radicalization#:~:text=the%20more%20time). 

* *Content ID*

  System wykrywający w&nbsp;filmikach cudze treści, takie jak piosenki, programy telewizyjne, fragmenty filmów. Z&nbsp;założenia ma służyć ochronie praw autorskich -- ale tylko wybranych treści, [najczęściej od większych organizacji](https://support.google.com/youtube/answer/9245819).  
  Elastyczność tego systemu polega na jego odporności na zmiany -- nawet jeśli ktoś doda jedynie fragment piosenki zamiast całości, YouTube jest w&nbsp;stanie powiązać ją z&nbsp;oryginałem.

* Automatyczna moderacja

  Usuwa filmy niezgodne z&nbsp;zasadami platformy, ale z&nbsp;przyczyn innych niż prawa autorskie. Przemoc, pornografia, te sprawy.  
System nieprzenikniony, bezwzględny i&nbsp;-- jak zobaczymy -- nieraz zawodny.


Nie mamy wglądu w&nbsp;te systemy, więc bardzo możliwe, że każdy z&nbsp;nich składa się za kulisami z&nbsp;większej liczby podsystemów (na przykład osobni cenzorzy od filmów, opisów itp.). Oprócz nich są też różne algorytmy pomocnicze, mniej ciekawe z&nbsp;punktu widzenia tego wpisu.

{% include info.html
type="Ciekawostka"
text="Jednym z&nbsp;automatów mniej znanych szarym widzom jest [wstawiacz reklam](https://support.google.com/youtube/answer/6175006?hl=pl).  
Chodzi o&nbsp;to, że twórcy mogą wybierać, w&nbsp;jakim miejscu wstawić przerwy reklamowe. Jeśli nie chcą ich ustawiać ręcznie, to algorytm zrobi to za nich, szukając w&nbsp;ich filmikach w&nbsp;miarę spokojnych miejsc."
%}

## YouTube Rewind 2018

Poprzednio skończyliśmy na 2017&nbsp;roku, teraz przeskoczymy do ostatnich dni roku 2018.

W tamtych czasach YouTube wydawał każdego grudnia *Rewind* (ang. *przewinięcie*), **filmik streszczający najważniejsze i&nbsp;najpopularniejsze sprawy z&nbsp;danego roku**. Zawierał krótkie występy najpopularniejszych youtuberów, viralowe treści, żarty dla wtajemniczonych, memy i&nbsp;tym podobne. Z&nbsp;założenia mrugnięcie okiem do społeczności, wywołujące banana na ustach.

[Rewind z&nbsp;2018 roku](https://www.youtube.com/watch?v=YbJOTdZBX1g) był przełomowy; ale raczej nie w&nbsp;tym sensie, w&nbsp;jakim chciałby go widzieć Google.

Już na samym początku filmiku pojawia się celebryta, Will „Plaskacz” Smith. Na YouTubie wówczas [od niecałego roku](https://www.nickiswift.com/140760/the-real-reason-youtubes-2018-rewind-video-bombed-so-hard/).  
Nie pojawia się natomiast [paru najpopularniejszych youtuberów](https://www.digitaltrends.com/social-media/youtube-rewind-2018-is-about-to-become-the-most-disliked-video-ever/), takich jak PewDiePie. Popularnych wśród widzów, ale nielubianych przez reklamodawców za kontrowersje. 

Cały filmik trwa 8&nbsp;minut i&nbsp;jest dość chaotyczny. Różne gwiazdki YT mówią, co by chciały dodać do filmu. Zaraz potem ta rzecz się pojawia. Gra wesoła muzyczka.

<img src="/assets/posts/youtube2/youtube-rewind-2018.jpg" alt="Kolaż pokazujący różne sceny z&nbsp;YouTube Rewind. Kadr z&nbsp;Willem Smithem, postacie w&nbsp;kolorowych marynarkach tańczące do muzyki, pannę młodą w&nbsp;towarzystwie rysunkowego kota, trzy osoby topiące szminkę w&nbsp;kotle, cztery osoby w&nbsp;kombinezonach kosmonautów siedzące w&nbsp;kabriolecie na tle Ziemi."/>

{:.figcaption}
Źródło: YouTube Rewind 2018.

Mniej więcej w&nbsp;połowie akcja zwalnia i&nbsp;odbija w&nbsp;typowe, amerykańsko-hollywoodzkie smęty z&nbsp;budującą muzyczką w&nbsp;tle. Postacie siedzą w&nbsp;kółku i&nbsp;po kolei coś mówią.

> Odsłonięcie swoich słabości wymaga wielkiej odwagi. Jestem dumna z&nbsp;tej społeczności.

{:.figcaption}
Tłumaczenie moje.

To aluzja do filmów, w&nbsp;których youtuberzy przyznawali się do wypalenia zawodowego. Związanego z&nbsp;tworzeniem filmów na akord, żeby utrzymać się w&nbsp;rankingu.  
Wielu osobom poświęcenie nie dało roli w&nbsp;Rewindzie -- bo ta była dla Willa Smitha, a&nbsp;nie przysłowiowego Areczka -- ale dostali przynajmniej głaśnięcie po głowie od Wujka Google'a.

A ludzie, którzy tak się przejmują zdrowiem psychicznym podczas Rewinda? Ponoć mówili o&nbsp;tym nieraz. Reklamując przy okazji prywatne programy terapeutyczne. I&nbsp;dostając [200 dolców](https://www.reddit.com/r/OutOfTheLoop/comments/a4txzq/comment/ebhwwds/) za każdego nagonionego klienta.

W filmiku widać też dbałość o&nbsp;*mniejszości*{:.corr-del} wskaźniki ESG. Pozwolę sobie zostawić te fragmenty w&nbsp;oryginale, bo korpomowa brzmi lepiej po angielsku. Mamy drobny hołd wobec kobiet:

{:.bigspace}
> Here's to all women in 2018&nbsp;for finding their voices.

I kultury *drag queen*:

{:.bigspace}
> I&nbsp;think this year's Rewind should celebrate the fierce, fabulous and empowering art of drag.

I na koniec, na dwa głosy:

> We are a&nbsp;family,  
We are a&nbsp;team.  
Family is everything.

:roll_eyes:

Ludzie jednak, ile by się ich nie urabiało, mają pewną granicę tolerancji na sztuczny patos. Tym razem mieli dość i, jak rzymscy cesarze, skierowali kciuki w&nbsp;dół. Rewind 2018&nbsp;pobił rekord, stając się **najgorzej ocenianym filmem na platformie YouTube**. W&nbsp;ciągu niecałego tygodnia zdetronizował dotychczasowego króla.

Samego Rewinda trudno nazwać aferą, ale był pewnym mocnym sygnałem „korporatyzacji” YouTube'a. Rozumianej jako odcięcie się od twórców wychodzących poza szereg, nacisk na PR-owy przekaz, angażowanie celebrytów, tandeta.

## Banowanie i&nbsp;demonetyzacja

Wróćmy tu do kwestii osób z&nbsp;różnych mniejszości.  
YouTube -- czyli Google -- w&nbsp;błysku fleszy wypowiada o&nbsp;nich ciepłe słowa. O&nbsp;pełnym wsparciu, o&nbsp;tym że osoby marginalizowane są szczególnie cenne.
  
Ale zaraz zobaczymy drugą stronę medalu, czyli rozdawanie banów za filmy *popierające mniejszości*. Najpierw jednak szczypta informacji.

# Różne rodzaje kar

Na YouTubie, jak pisałem w&nbsp;poprzednim wpisie, da się zarabiać. Trzeba w&nbsp;tym celu przekroczyć pewien próg popularności.  
Gdy się to osiągnie, pojawia się opcja włączenia tzw. *monetyzacji*. Można dodawać do swoich filmów reklamy i&nbsp;zarabiać trochę za każde ich wyświetlenie.  
Można też być Willem Smithem, któremu włączono monetyzację [od razu po dołączeniu](https://www.nickiswift.com/140760/the-real-reason-youtubes-2018-rewind-video-bombed-so-hard/). Ale to raczej opcja dla niewielu.

Ale nie tylko twórcy mają dostęp do złotego kurka. YouTube w&nbsp;każdej chwili może go zakręcić -- **wyłączyć twórcy możliwość zarabiania na tym filmiku. To tak zwana _demonetyzacja_**.

Demonetyzacja jest kijem, który pozwala YouTube'owi ustawiać niepokornych twórców. „Będziesz grzeczny, albo nic nie dostaniesz”. Zasadniczo jednak nie prowadzi do wykopania kogoś poza platformę.

Z kolei ostrzeżenia i&nbsp;bany idą o&nbsp;krok dalej. Są rozdawane za cięższe przewinienia, czyli dodanie filmów [niezgodnych z&nbsp;regulaminem](https://support.google.com/youtube/answer/2802032?hl=pl) (*Wytycznymi Społeczności*). Przysługują nam trzy przewinienia -- za pierwszym razem dostajemy upomnienie, potem ostrzeżenie numer 1, ostrzeżenie numer 2. Za kolejne przewinienie wyrzucają nas z&nbsp;platformy.

I tak, za przyznawanie tych kar częściowo odpowiadają omylne automaty. Dla których sygnałem może być między innymi to, czy jakiś użytkownik zgłosi nasze konto, co tworzy pole do nadużyć.

Teoretycznie twórcom przysługuje odwołanie, po którym ich sprawie przyjrzy się człowiek, a&nbsp;procedura oceny jest sprawiedliwa. Ale my już kończymy teorię. Teraz rzeczywistość.

# Demonetyzacja

YouTube sam nie ukrywa, że regulamin swoją drogą, a&nbsp;demonetyzacja swoją:

> Takie treści, mimo że mogą być odpowiednie do publikacji w&nbsp;YouTube zgodnie z&nbsp;naszymi Wytycznymi dla społeczności, nie zawsze są odpowiednie dla naszych reklamodawców.

{:.figcaption}
Źródło: [baza informacji YouTube'a](https://www.youtube.com/howyoutubeworks/our-commitments/sharing-revenue/#responsible-advertising).

W takich realiach zyskuje na wiarygodności pewien [wyciek](http://www.twitlonger.com/show/n_1sqbsph) ze spotkania informacyjnego moderatorów. Czyli ludzi, którzy są decydującym głosem w&nbsp;naszej sprawie.

Rzekomo instruowano ich, żeby **w razie wątpliwości skłaniali się ku demonetyzacji -- na niekorzyść twórców**.  
Wyciek porusza również kwestię twórców niewygodnych. Jeśli są popularni wbrew wszelkim chęciom platformy, ale trzymają się regulaminu, a&nbsp;usunięcie ich mogłoby przynieść PR-owy skandal... To można się do nich dobrać właśnie przez demonetyzację.

A przypominam, że mówimy tutaj o&nbsp;instrukcjach dla ludzi. Którzy mają być w&nbsp;naszej sprawie drugą, bardziej empatyczną instancją. Na pierwszej linii są natomiast automaty. Zadziwię kogokolwiek, jeśli powiem że ich działania są nieprzeniknione i&nbsp;niekorzystne dla twórców? Przyjrzyjmy się im.

Jednym z&nbsp;kryteriów ocenianych przez te algorytmiczne czarne skrzynki są słowa zawarte w&nbsp;tytule i&nbsp;opisie filmu. Eksperymenty twórców wykazały, że **użycie słów związanych z&nbsp;mniejszościami to dość pewny sposób na demonetyzację**.

O cudactwach algorytmu opowiada m.in. Andrew Platt w&nbsp;swoim [filmiku z&nbsp;2019 roku](https://www.youtube.com/watch?v=oFyHpBsvcK0). Autor jest o&nbsp;tyle ciekawą postacią, że podszedł do sprawy w&nbsp;sposób bardziej naukowy. Eksperymentował z&nbsp;różnymi słowami kluczowymi, zmieniając tylko jedno naraz, i&nbsp;patrzył na to, którym filmom YouTube utnie finansowanie.

Na tej podstawie zgromadził wielką listę słów, dokumentując ich wpływ na monetyzację. Zielonym kolorem oznaczył filmy normalnie zarabiające, żółtym zdemonetyzowane.  
W trzeciej kolumnie zapisywał gwiazdki -- pokazujące, *ile razy* wyłączano monetyzację (czasem udawało się ją włączyć ponownie). Można je zatem uznać za miernik kontrowersyjności danego zwrotu dla algorytmu.

<img src="/assets/posts/youtube2/youtube-demonetization-words.jpg" alt="Kolaż złożony z&nbsp;komórek z&nbsp;Arkusza Google. Widać na nim różne słowa na zielonym lub żółtym tle, a&nbsp;obok nich gwiazdki, od jednej do kilku."/>

{:.figcaption}
Źródło: [lista Platta](https://docs.google.com/spreadsheets/d/1ozg1Cnm6SdtM4M5rATkANAi07xAzYWaKL7HKxyvoHzk/edit) (uwaga: Arkusz Google).

Streszczając rzeczy moim zdaniem ważniejsze:
* **Wzmianki o&nbsp;LGBT albo ruchu MeToo prowadzą do demonetyzacji**. I&nbsp;to konsekwentnie, bez większego wahania algorytmu (mało gwiazdek w&nbsp;trzeciej kolumnie).
* Przy innych zwrotach nawiązujących do mniejszości seksualnych mamy loterię, ale ogólnie często obrywają demonetyzacją. Na pewno częściej niż Adolf H.
* Czasem jedna literka, dająca liczbę mnogą, stanowi różnicę między łaską a&nbsp;niełaską autocenzora. Podobnie zamiana przymiotnika na rzeczownik.  
Trochę nam to mówi o&nbsp;jego „stabilności”.
* Zapewne istnieje swego rodzaju „karanie przez skojarzenie”. `Dick Cheney` to zwrot demonetyzowany prawdopodobnie tylko przez to, że algorytm ma pieprzne skojarzenia z&nbsp;jego imieniem.

Platt rozwinął temat w&nbsp;[filmiku z&nbsp;2021 roku](https://www.youtube.com/watch?v=_AFVlGnXMsc). Wspomina, że autorzy dostali możliwość oceniania własnych filmów w&nbsp;krótkich ankietach. W&nbsp;ten sposób mogą się dowiedzieć z&nbsp;wyprzedzeniem, czy pchają się ku demonetyzacji.  
...Ale potem ten sam film i&nbsp;tak weryfikują automaty, których ankiety nie obchodzą. Więc w&nbsp;praktyce jedyną zmianą jest odsianie najbardziej jaskrawych przypadków i&nbsp;danie twórcom iluzji kontroli.

{% include info.html
type="Inne źródła"
text="Jeśli nie przeszkadza nam odrobina *showmaństwa* (ale pozytywnego), to możemy też obejrzeć [półgodzinny filmik](https://www.youtube.com/watch?v=ll8zGaWhofU) od kanału „Nerd City”, który opiera się na twórczości Platta i&nbsp;przybliża całą sprawę.  
Oprócz tego możemy poczytać [krótki raport](https://docs.google.com/document/d/18B-X77K72PUCNIV3tGonzeNKNkegFLWuLxQ_evhF3AY/edit) na temat demonetyzacji."
%}

Podsumowując sprawę demonetyzacji: najpierw dowala nam kapryśny automat. Odwołać możemy się jedynie do człowieka, którego szkolono, żeby w&nbsp;razie wahań działał na niekorzyść twórców. Niewesoła perspektywa, prawda?

# Naruszenie Content ID

Kary wymierzane za [naruszenie *Content ID*](https://support.google.com/youtube/answer/6013276) dotyczą konkretnych filmików, a&nbsp;nie całego konta. Pod względem surowości są nieco gorsze niż demonetyzacja. Albo nam dany filmik blokują, albo przekierowują cały zysk z&nbsp;umieszczonych w&nbsp;nim reklam do twórcy oryginału.

Tylko że **twórca oryginału to dla YouTube'a ten, kto pierwszy zarejestruje treść w&nbsp;ich bazie**.

W 2012&nbsp;roku doszło do absurdalnej sytuacji, kiedy YouTube automatycznie [zablokował](https://science.slashdot.org/story/12/08/06/1613211/nasas-own-video-of-curiosity-landing-crashes-into-a-dmca-takedown) filmik wrzucony przez NASA. Którego autorem była... NASA.
  
Zapewne dlatego, że agencja kosmiczna, jako organizacja bardziej naukowa, nie bawiła się w&nbsp;rejestrację filmu w&nbsp;bazie. A&nbsp;jednocześnie pozwoliła mediom go udostępniać.  
Kiedy pracownicy Scripps Local News wrzucili na swój kanał filmik skopiowany od NASA, automatycznie wystąpili o&nbsp;*Content ID* (zapewne tak mieli ustawiony system). W&nbsp;ten sposób w&nbsp;systemie YouTube'a to oni stali się właścicielami. A&nbsp;agencję uznano za piratów i&nbsp;zablokowano ich filmik.

Nawet jeśli takie historie są rzadkie, wywołują swoisty efekt mrożący. Ludzie wolą działać zachowawczo niż użerać się z&nbsp;tym, czym Google im dowali.

Przykład z&nbsp;Polski? Youtuber Dominik Bos wspomina [w swoim filmie](https://www.youtube.com/watch?v=YU7ltFYjq9w) o&nbsp;aktorce, która w&nbsp;„Dzień Dobry TVN” reklamowała nieskuteczne „okulary na depresję”.  
Pokazuje krótki fragment programu i&nbsp;wspomina, że celowo zniekształcił materiał. Mimo że, gdyby chodziło jedynie o&nbsp;zgodność z&nbsp;prawem, swobodnie mógłby go pokazywać.

> Wiadomo, prawo cytatu i&nbsp;tak dalej, ale... Wytłumaczcie to robotom.

# Bany

Ucięcie finansowania, blokowanie filmików. Jasne; to bolesne kary i&nbsp;trochę może nas wkurzać, że decydują o&nbsp;tym automaty... Ale nadal będziemy na platformie, prawda? Możemy się odkuć kolejnymi filmami.

Tylko że **algorytmy decydują również o&nbsp;banowaniu**. Naszym ostatecznym „być albo nie być”.  
Co więcej, robią to na podstawie zawartości samych filmów. Nie jestem jakimś szczególnym *AI*-owcem, ale to jedno mogę powiedzieć z&nbsp;pewnością: analizowanie tytułów i&nbsp;słów kluczowych jest dużo łatwiejszym zagadnieniem niż „rozumienie” tego, co widać na filmach. A&nbsp;widzieliśmy, jak zawodne było to pierwsze.

Zresztą tylko spójrzmy na przykłady banów: 

* Automat odpowiedzialny za wyłapywanie kontrowersyjnych treści zablokował [kanał nauczyciela historii](https://twitter.com/MrAllsopHistory/status/1136326031290376193), bo algorytm przyczepił się do fragmentów pokazujących nazistowską propagandę.
* Blokadą oberwał też kanał dotyczący [naprawy urządzeń elektronicznych](https://www.youtube.com/watch?v=W0mMOHrftgU). Tu już nie wiadomo za co.   Pierwszy komentarz:

  > Obviously Youtube, in their usual style, will never tell us why his channel was deleted.

* W&nbsp;2019 roku **usunęli tysiące filmików z&nbsp;Battlebotami**, czyli walki robotów zbudowanych przez majsterkowiczów. Algorytm sklasyfikował je jako... [walki zwierząt](https://www.cbr.com/youtube-reportedly-deleting-battlebot-videos-citing-animal-fighting-ban/).
* Żona autora pewnego [wątku na forum](https://news.ycombinator.com/item?id=30401241) straciła swoje firmowe konto na YT, zawierające ponad 700&nbsp;filmów.  
Dostała w&nbsp;krótkim czasie trzy ostrzeżenia, co poskutkowało natychmiastowym banem, bez czasu na reakcję. Oficjalnie za *cyber bullying*, choć filmy niczego takiego nie zawierały. I&nbsp;jakoś trzymały się spokojnie przez 7&nbsp;lat.
* W&nbsp;ostatnim czasie [banowano konta popierające Ukrainę](https://news.ycombinator.com/item?id=30467384). Zapewne przez to, że były zgłaszane przez trollkonta, a&nbsp;liczba zgłoszeń to sygnał dla algorytmu.
* I&nbsp;jeszcze więcej, i&nbsp;tak dalej. Polecam odwiedzić dowolny serwis i&nbsp;wyszukiwać zwrotów w&nbsp;stylu `youtube ai banned`.

Kiedy coś tworzymy na YouTubie, nasz los jest w&nbsp;rękach kapryśnej, nieobliczalnej maszyny. Co zresztą jest na tyle stałym elementem interakcji z&nbsp;firmą Google, że można to uznać za ich korporacyjne DNA.

## Money, money, money...

Kolejną ciemną stroną platformy, oprócz automatów, jest stopniowe odwracanie się od twórców na rzecz większych reklamodawców.  
Widzieliśmy to od dawna, ale od pewnego czasu zmiany wydają się coraz gwałtowniejsze, a&nbsp;platforma porzuca dotychczasowy śmieszkowo-kumplowski charakter. Jak wąż wylinkę.

# Wyższa poprzeczka dla monetyzacji

W 2018&nbsp;roku YouTube [zwiększył wymagania](https://support.google.com/youtube/forum/AAAAiuErobUA3DoDo-OGyU/?hl=en&gpf=%23!topic%2Fyoutube%2FA3DoDo-OGyU), jakie muszą spełnić twórcy chcący włączyć zarabianie. Do 4000&nbsp;godzin obejrzanych w&nbsp;ciągu ostatnich 12&nbsp;miesięcy oraz do 1000&nbsp;subskrybentów. Bez wyjątku.

Ten wymóg **ubił kanały, dla których tworzenie filmików było szczególnie czasochłonne**. Takie jak te związane z&nbsp;ręczną animacją. Twórcy muszą pogodzić się z&nbsp;tym, że zamiast zarobku będzie co najwyżej hobby... albo zacząć tworzyć wielominutowy, generowany automatycznie chłam w&nbsp;stylu ElsaGate. To by przyniosło zarobki.

# Przymusowe reklamy u&nbsp;wszystkich

Do tej pory istniała opcja dobrowolnej rezygnacji z&nbsp;reklam w&nbsp;swoich filmach. Nawet jeśli kanał miał bardzo dużo wyświetleń, mógł po prostu nie przystępować do programu monetyzacji.

W ten sposób twórca nic nie zarabiał -- choć zarobki były oddalone o&nbsp;parę kliknięć -- ale jego widzowie nie musieli oglądać reklam. YouTube też coś z&nbsp;tego miał; popularny kanał ściąga użytkowników, którym wyświetlają się propozycje innych filmów. Rośnie szansa, że odwiedzą też filmiki obudowane reklamami i&nbsp;zyskowniejsze dla YT.

Ale jakiemuś menedżerowi z&nbsp;YouTube'a sytuacja zapewne spędzała sen z&nbsp;powiek. „No jak tak można -- móc dać reklamy, ale ich nie dawać?! Nie godzi się”.  
Wprowadzono zmiany. Od 2020 roku reklamy są [wyświetlane u wszystkich](https://www.forbes.com/sites/johnkoetsier/2020/11/18/youtube-will-now-show-ads-on-all-videos-even-if-creators-dont-want-them/). **Jeśli ktoś nie włączy monetyzacji, to po prostu nie zarabia**.

Przeciw temu stanowi rzeczy zbuntowały się duże organizacje -- Blender Foundation (twórcy programu graficznego Blender) oraz MIT OpenCourseware (darmowe kursy oferowane przez Massachussets Institute of Technology, znaną uczelnię).

Blender [na bieżąco informował](https://www.blender.org/media-exposure/youtube-blocks-blender-videos-worldwide/) o&nbsp;swoich przeprawach z&nbsp;Google'em. Ostatecznie, po ogłoszeniu realnych planów odejścia na inną platformę, udało im się wywalczyć wyjątek i&nbsp;brak reklam.

Ale zanim to się stało... Czytelnicy poprzedniego wpisu być może pamiętają, jak kiedyś, podczas sporu z&nbsp;Viacomem, YouTube usuwał niewinne filmiki i&nbsp;wyświetlał informacje oczerniające autorów? (Bo przedstawiające naruszanie praw autorskich jako fakt, a&nbsp;nie możliwość).

Teraz zdarzyło się coś podobnego. Jak pisze Blender:

{:.bigspace}
> Przez to, że nie zaakceptowaliśmy nowych warunków, zamiast naszych filmów wyświetlał się komunikat o błędzie „Film niedostępny w twoim kraju”, który zwykle sygnalizuje problem z prawami autorskimi.

{:.figcaption}
Tłumaczenie moje.

# Zmiana zasad weryfikacji

Konta zweryfikowane to konta szczególnie wpływowe, wyróżnione specjalnym znaczkiem i&nbsp;możliwościami bezpośredniego kontaktu z&nbsp;pracownikami YouTube'a.  
Do tej pory reguły gry były jasne. Kto zdobędzie 100&nbsp;000 subskrybentów, osiągając tym samym naprawdę duże wpływy, ten może wystąpić o&nbsp;weryfikację. 

{:.figure .bigspace}
<img src="/assets/posts/youtube2/youtube-verified.jpg" alt="Mały wycinek ekranu pokazujący tytuł filmiku 'YouTube Rewind 2019, ale ten jest naprawdę dobry'. Obok nazwy autora, PewDiePie, widać okrągły znaczek, dodatkowy wyróżniony na obrazku czerwoną ramką."/>

We wrześniu 2019&nbsp;roku YouTube [zmienił zasady na mniej przejrzyste](https://gamerant.com/youtube-channels-verification-remove/). Jak zawsze po to, żeby chronić.

> we announced changes to the verification badge. The idea behind this update was to **protect** creators from impersonation and address user confusion

{:.figcaption}
Źródło: [wpis](https://blog.youtube/news-and-events/updates-to-youtubes-verification-program/) na blogu YouTube'a. Wyróżnienie moje.

Od teraz, podejmując decyzje o&nbsp;przyznaniu znaczka, YouTube bierze pod uwagę również rozpoznawalność poza samą platformą, podobieństwo nazw do innych kanałów... A&nbsp;właściwie bierze pod uwagę co chce, bo wspomniane kryteria są wymienione po słowie „wliczając”.

Co więcej, nowe prawo ustanowione przez YT działa również wstecz. **Wiele dotąd zweryfikowanych kanałów straciło swój status**. Również takich, które nosiły znaczek od lat.  
Więc sorry, twórcy opijający właśnie 100&nbsp;000 subskrybentów i&nbsp;znaczek jakości. Wasza walka i&nbsp;tak nigdy nie miała sensu, bo Wujaszek was nie lubi i&nbsp;zmienił reguły gry. Od teraz znaczek będzie głównie dla rozpoznawalnych, globalnych marek.

## 2021&nbsp;– nagroda dla pani prezes

Można się zastanowić, skąd bierze się taki zwrot platformy w&nbsp;stronę komerchy. I, jak to w&nbsp;przypadku megakorporacji bywa, warto spojrzeć na sam szczyt hierarchii.

Do tej pory unikałem przywoływania konkretnych osób, traktując Google jak wielką nieodgadnioną masę. Ale teraz będzie krótko o&nbsp;pani prezes YouTube'a, Susan Wojcicki. Nazwisko jakby znajome; i&nbsp;faktycznie, oboje jej dziadkowie byli Polakami.

Na forum HackerNews znalazłem ciekawą [wymianę komentarzy](https://news.ycombinator.com/item?id=26882120), mówiącą o&nbsp;rywalizacji Google Video z&nbsp;YouTube'em (kiedy ten jeszcze był niezależny). Nie jest to oczywiście źródło w&nbsp;100% pewne, ale zawiera szczegóły techniczne, które da się zweryfikować.

W tamtych czasach za Google Video odpowiadała właśnie Susan Wojcicki. Jej koncepcja od samego początku **kręciła się wokół współpracy z&nbsp;dużymi markami**.  
Jak analizuje autor komentarza, to między innymi przez to Google Video dostawało po tyłku. Zaś bardziej zwinny, „społecznościowy” YouTube ich wyprzedzał. Google się wkurzył, sięgnął do kieszeni i&nbsp;po prostu kupił swojego rywala. A&nbsp;do opieki nad nim w&nbsp;2014 roku oddelegowano panią Wojcicki.

Ale ludzie pozostaną ludźmi. Czy możliwe, że pani prezes zachowała z&nbsp;tamtych czasów pewien uraz? Chęć udowodnienia, że to jej pomysł na platformę dla gigantów był tym właściwym? 

Nigdy nie poznamy jej dokładnych myśli. Ale pewną wskazówką *a propos* postrzegania własnej osoby może być sytuacja z&nbsp;2021 roku.  
Wtedy to pani prezes z&nbsp;dumą odebrała od organizacji Freedom Forum Institute [nagrodę za sprzyjanie wolności słowa](https://www.newsweek.com/youtube-ceo-susan-wojcicki-gets-freedom-expression-award-sponsored-youtube-1585147). Gratulacje!

Tylko że... **Konferencja, podczas której przyznano tę nagrodę, była sponsorowana przez YouTube'a**.  
Pani prezes to jednak nie powstrzymało przed dumnym przyjęciem nagrody i&nbsp;wygłoszeniem przemowy mówiącej o&nbsp;odpowiedzialności YouTube'a. Nawiązała również do autocenzora -- wprost chwali się tym, że 90% filmów usunęły automaty.

> We removed nine million videos last quarter and almost all of them – over 90% – we removed with machines, which is good because it means if there’s content that’s violative, we find that really quickly

{:.figcaption}
Źródło: [transkrypcja](https://blog.youtube/news-and-events/susan-wojcicki-and-molly-burke-conversation-about-free-expression/) z&nbsp;oficjalnego bloga Youtube'a.

„With machines. *Which. Is. Good*”.

## Wyłączenie negatywnych ocen

Podejście „zero negatywności”, jakim wykazała się pani Wojcicki, wydaje się przenikać całą organizację. Może dlatego blisko końca 2021&nbsp;roku YouTube **ukrył licznik łapek w&nbsp;dół**.

{:.figure}
<img src="/assets/posts/youtube2/youtube-thumbs-count.jpg" alt="Zrzut ekranu z&nbsp;YouTube'a, pokazującego opcję dodania kciuka w&nbsp;dół lub w&nbsp;górę." />

{:.figcaption}
Nadal mogę sobie kliknąć kciuka w&nbsp;dół; ale ich łączna liczba już nie jest publicznie widoczna.

Jako oficjalny powód podają oczywiście bezpieczeństwo. Wszystko w&nbsp;trosce o&nbsp;mniejszych twórców, którzy mogliby się zrazić negatywnym odzewem. Ach, i&nbsp;piszą że to dopiero początek:

> We want to create an inclusive and respectful environment where creators have the opportunity to succeed and feel safe to express themselves. This is just one of many steps we are taking to continue to **protect** creators from harassment. Our work is not done (...)

{:.figcaption}
Źródło: [oficjalny blog](https://blog.youtube/news-and-events/update-to-youtube/). Wyróżnienie moje.

Nic to, że w&nbsp;praktyce nowi twórcy tacy chronieni nie są. Nadal można klikać łapki w&nbsp;dół, a&nbsp;twórcy mogą podejrzeć ich liczbę przez swoje profile. Zapytajmy siebie szczerze: kto z&nbsp;nich tam nie zerknie z&nbsp;ciekawości? Narażając się dokładnie na ten widok, przed którym troskliwy Jutub chce go chronić?

Poza tym ta „ochrona mniejszych graczy” dziwnym trafem nie ogranicza się do kont nowych albo mniej popularnych. Z licznymi łapkami w dół żegnają się również filmy korporacyjne:

* wspomniany Rewind;
* reklama Pepsi przedstawiająca protesty jako [radosny happening](https://www.nbcnews.com/news/nbcblk/pepsi-ad-kendall-jenner-echoes-black-lives-matter-sparks-anger-n742811) z&nbsp;celebrytami;
* [reklama Gillette](https://www.youtube.com/watch?v=UYaY2Kb_PKI), mentorskim tonem mówiąca mężczyznom, że muszą się zmienić;
* [trailer](https://www.youtube.com/watch?v=a7ZpQadiyqs) gry „Battlefield V”, odchodzący od realizmu na rzecz kiczowatej rozrywki.

Nie odnoszę się do samych filmów. Ale jest faktem, że wywołały kontrowersje i&nbsp;zebrały wiele łap w&nbsp;dół, widocznych publicznie. A&nbsp;teraz ich liczba spadła do zera, została jedynie w&nbsp;kronikach.  
W przypadku przyszłych filmów nie będzie nawet tej historii. Od teraz pod każdą nowinką od dużych reklamodawców będą wyłącznie wyrazy uznania.

{% include info.html
type="Ciekawostka"
text="YouTube wyłączył możliwość dodawania łapek również pod ich oficjalnym komunikatem o&nbsp;tej zmianie. Ale pod pierwszym komentarzem, autorstwa swego rodzaju rzeczniczki, kciuki już były. Głównie skierowane w&nbsp;dół."
%}

## Co możemy zrobić

Czas na chwilę się wynurzyć z&nbsp;brudów wokół YouTube'a i&nbsp;pomyśleć o&nbsp;jakimś aktywnym działaniu.

Samej platformy raczej nie unikniemy -- nawet gdybyśmy chcieli to robić dla zasady. Czasem ktoś znajomy podeśle link, innym razem będzie to jedyne miejsce z&nbsp;interesującymi nas informacjami.

Dlatego, choć YouTube'a raczej nie zmienimy, możemy zmienić swoje podejście do niego.

# Ochrona danych

Moje wpisy na temat YouTube'a skupiają się na rzeczach typowych dla tej platformy. Ale nie zapominajmy, że przede wszystkim to część Google'a. Więc **mamy do czynienia z&nbsp;tym samym masowym zbieraniem danych o&nbsp;naszych zwyczajach**.

I, tak jak w&nbsp;przypadku innych usług giganta, możemy spróbować to wyłączyć. Europejskie przepisy o&nbsp;prywatności dają przynajmniej cień szansy, że firma uszanuje nasze ustawienia, żeby uniknąć kar.  
Aby zmienić ustawienia na korzystniejsze dla nas, wchodzimy na [stronkę](https://myaccount.google.com/u/0/yourdata/youtube?hl=pl) i&nbsp;odznaczamy tam trzy opcje związane z&nbsp;analizowaniem naszych zwyczajów.

{:.figure .bigspace}
<img src="/assets/posts/youtube2/google-zarzadzanie-danymi.jpg" alt="Ekran Google, na którym widać trzy opcje wraz z&nbsp;opisami. Wszystkie suwaki są ustawione na tryb wyłączony i&nbsp;wyróżnione czerwonymi ramkami." width="500px"/>

Poza tym zamiast aplikacji warto używać wersji przeglądarkowej (*www.youtube.com*). To uniwersalna zasada, że **aplikacja ma dostęp do znacznie większych ilości danych**. Używając przeglądarki, ograniczamy ilość przekazywanych informacji.

Jeśli nie chcemy wiązać jakichś oglądanych filmów z&nbsp;naszymi typowymi zwyczajami, to warto odwiedzić YouTube'a w&nbsp;trybie anonimowym/incognito (`Ctrl`+`Shift`+`P` w&nbsp;Firefoksie, `Ctrl`+`Shift`+`N` w Chromie; można też przeklikać się przez opcje).

# Youtube-dl 

YouTube jest nieprzewidywalny, a&nbsp;nasze ulubione filmiki mogą w&nbsp;każdej chwili zniknąć. Sami widzieliśmy, jak kapryśna jest automatyczna cenzura.  
Jeśli chcemy uniknąć tego losu (a przy okazji nie karmić YT statystykami na temat liczby i&nbsp;częstości wyświetleń), to można skorzystać z&nbsp;`youtube-dl`, świetnego programiku konsolowego.

Po zainstalowaniu wystarczy wpisywać proste komendy:

{:.bigspace}
<div class="black-bg mono">youtube-dl <span class="red">link_do_filmiku</span></div>

...a pobrany filmik zostanie zapisany w&nbsp;formie pliku na dysku. Można pobierać filmy w&nbsp;różnej rozdzielczości, a&nbsp;nawet sam dźwięk.  
Wbrew nazwie działa na wielu stronkach, w&nbsp;tym bardziej... prywatnych :wink:

{% include info.html
type="Porada"
text="Szybkość pobierania przez `youtube-dl` jest dość mocno ograniczona. Istnieje jego [szybsza wersja](https://github.com/yt-dlp/yt-dlp), uwolniona od tego limitu, ale jej nie testowałem.  
Oprócz tego, jeśli ktoś bardzo nie lubi konsoli, może skorzystać z&nbsp;nakładek graficznych na ten program. Ale również ich nie sprawdzałem."
%}

Instrukcje instalacji znajdziecie [na stronie projektu](https://github.com/ytdl-org/youtube-dl).  
A ponieważ uważam ten programik za szczególnie przydatne narzędzie w&nbsp;naszym arsenale, naszykowałem również [własny samouczek]({{site.url}}/tutorials/youtube-dl){:.internal} na temat korzystania z&nbsp;*youtube-dl*.

# Alternatywne apki i&nbsp;strony

Kiedy zaczynałem tworzyć ten wpis ponad miesiąc temu, apka Vanced miała być jednym ze sposobów na ominięcie chciwych łap YouTube'a. Dopracowana i&nbsp;pełna funkcji, których brakuje oficjalnej aplikacji.  
Niestety to już nieaktualna sprawa. Niedawno **zamknęli swój projekt przez groźby pozwu ze strony YouTube'a** dotyczące naruszenia praw autorskich.

Pozostała alternatywa z&nbsp;mniejszą liczbą bajerów, [NewPipe](https://newpipe.net/).  
Osobiście nie korzystam z&nbsp;alternatywnych apek (wolę pobrać na dysk i&nbsp;oglądać na większym ekranie). Ale w&nbsp;przypadku NewPipe'a kusi możliwość korzystania z&nbsp;niego bez dawania mu dostępu do konta oraz bez usług Google'a. 

{% include info.html
type="Ciekawostka"
text="Nazwa *Vanced* wzięła się od *Advanced* bez *Ad* (ang. *reklama*).  
Co do *NewPipe'a* nie mam pewności -- ale może *New* jako rym do *You* i&nbsp;*Pipe* jako synonim *Tube* (oba słowa oznaczać mogą „rura”)."
%}

Jeśli chodzi o&nbsp;alternatywne strony, osobiście z&nbsp;nich nie korzystałem, więc ciężko mi coś polecić. Ale podzielę się pewnym istotnym rozróżnieniem.

* Tak zwane *alternatywne frontendy* **zawierają dokładnie te filmy co YouTube**, ponieważ są swego rodzaju pośrednikiem, a&nbsp;swoje zapytania wysyłają do głównego serwisu.
* Oprócz nich są też kompletnie niezależne strony, jak Vimeo czy Peertube. Rzadko kiedy znajdziemy tam te same filmy co na YouTubie. Co może być zarówno wadą, jak i&nbsp;zaletą.  
  Nie zdziwmy się, jeśli wśród ich filmów będzie sporo teorii spiskowych. To efekt tego, że ku takim stronom zwracają się często osoby zbanowane na YT, a&nbsp;przy tym zdeterminowane.  
  Ale to nie wina samych platform i&nbsp;nadal można na nich znaleźć fajne rzeczy. 

# Gdy jesteśmy twórcami

W tej kwestii wiem najmniej, mając zerowe doświadczenie jako youtuber. Zatem pozostaje parę ogólnych, zdroworozsądkowych porad.

Dywersyfikujcie, bądźcie obecni na kilku różnych platformach. Nie stańcie się zależni od YouTube'a, bo prędzej czy później się na tym przejedziecie. Zawsze będziecie mniej atrakcyjni niż Disneye czy Unilevery tego świata.

Jako twórcy możecie też okazać swój sprzeciw wobec profilowania i&nbsp;[wyłączyć u&nbsp;siebie serwowanie reklam spersonalizowanych](https://support.google.com/youtube/answer/9487666?hl=pl&ref_topic=9257896).  
Dodawania reklam jako takiego nie unikniecie, więc proponuję wyjście pragmatyczne. Możecie je włączyć, żeby pieniądze trafiły do Was zamiast do YT. A&nbsp;potem zrobicie z&nbsp;nimi coś zgodnego ze swoimi poglądami :wink:

## Podsumowanie

YouTube przeszedł daleką drogą od platformy z&nbsp;krótkimi filmami, reklamującej się hasłem „*Broadcast Yourself*” (w bardzo luźnym tłumaczeniu: *Twoja własna audycja*). Platformy, na której każdy mógł być sam sobie sterem i&nbsp;reżyserem.

Od kilku lat skręca w&nbsp;inną stronę -- wielkich reklamodawców, wytwórni i&nbsp;korporacji. Twórcy to niepokorne, problematyczne elementy. Tam coś powiedzą niezręcznego, tam zaprotestują, to znów nie okażą należytego entuzjazmu.

W rzeczywistości, ku której zmierza YouTube, taki haniebny indywidualizm jest niemile widziany.  
Mile widziani są *partnerzy biznesowi*, którzy dodają swoje produkcje. I&nbsp;tłum wiecznie nienasyconych widzów, stymulowany jaskrawymi bodźcami. Reagujący na treści dużych partnerów entuzjazmem i&nbsp;nienasyconą konsumpcją.

A na niepokornych czeka dociskanie śruby, spychanie na margines. A&nbsp;na koniec metaliczna, szponiasta łapka automatu banującego.

Dlatego warto oddzielić twórców od platformy -- jak najbardziej można być po ich stronie i&nbsp;niekoniecznie ubóstwiać Wujka Google'a. Jeśli trafimy na filmik wyjątkowy, to warto go pobrać i&nbsp;przechowywać u&nbsp;siebie na dysku, nim go usuną. Żeby mieć jakiś trwalszy skarb w&nbsp;świecie, w&nbsp;którym coraz więcej jest tylko na wynajem.

Życzę jak najwięcej takich skarbów :smile: Do kolejnego wpisu!
