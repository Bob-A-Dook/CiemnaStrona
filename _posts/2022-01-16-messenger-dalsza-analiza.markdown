---
layout: post
title:  "Jak piszesz? Zapytam Messengera"
description: "Liczę średnią szybkość pisania i wyłapuję błędy ortograficzne"
subtitle: "Liczę średnią szybkość pisania i wyłapuję błędy ortograficzne."
date:   2022-01-16 14:00:00 +0100
tags: [Porady, Internet, Analiza danych]
firmy: [Facebook]
category: facebook_dane
category_readable: "Kochajmy się jak bracia, analizujmy się jak Facebooki"
image: "messenger2/messenger-bledy-ortograficzne-baner.jpg"
image-width: 1200
image-height: 700
---

Witam Was w&nbsp;pierwszym wpisie w&nbsp;nowym 2022&nbsp;roku! I&nbsp;zarazem kolejnym poświęconym analizowaniu danych z&nbsp;Facebooka.  
(Ich nadrzędna spółka to teraz Meta, ale będę używał starej nazwy, bo jakoś trudno się przestawić. Tak jak z&nbsp;Woodstockiem i&nbsp;Pol'and'rockiem).

Sporo czasu minęło od poprzedniego wpisu z&nbsp;tej serii, więc przypomnę jej cel.

Chodzi tutaj o&nbsp;to, że pobieram z&nbsp;portalu Facebook dane na swój temat (korzystając z&nbsp;opcji, którą udostępnili; zapewne [pod presją GDPR/RODO](https://www.facebook.com/business/gdpr)). Następnie amatorsko je analizuję i&nbsp;wypatruję ciekawostek.  
Jeśli nawet laik ze skryptem Pythona wyłowi ciekawe informacje, to **co o&nbsp;nas wiedzą w&nbsp;samym Facebooku**?

W poprzednim wpisie skupiłem się na liczeniu podstawowych statystyk dla wiadomości z&nbsp;Messengera. Głównie swoich, choć odczytałem też ciekawe rzeczy o&nbsp;osobach, z&nbsp;którymi najwięcej piszę.  
Patrzyłem między innymi na przeciętną długość wiadomości, godziny ich wysłania, używane w&nbsp;nich emoty.

Tym razem skupię się na dwóch nowych rzeczach.

* Wyłapię „ciągi” złożone z&nbsp;kilku wiadomości pod rząd. W&nbsp;przypadku niektórych z&nbsp;nich pozwoli to liczyć czyjąś przybliżoną szybkość pisania, a&nbsp;nawet wychwytywać wiadomości wklejone.  
* Poza tym użyję publicznie dostępnych list słów -- a&nbsp;nawet książki „Znachor” i&nbsp;paru innych -- żeby znajdować potencjalne błędy ortograficzne :smiling_imp:

Pod koniec wpisu znajdziecie nową wersję skryptu, dzięki któremu możecie przeprowadzić takie analizy również na własnych danych.

Ruszajmy!

# Spis treści

* [Analizowanie ciągów wiadomości](#analizowanie-ciągów-wiadomości)
  * [Liczba różnych ciągów wiadomości](#liczba-różnych-ciągów-wiadomości)
  * [Szybkość pisania](#szybkość-pisania)
  * [Liczba wiadomości wklejonych](#liczba-wiadomości-wklejonych)
* [Wyłapywanie błędów ortograficznych](#wyłapywanie-błędów-ortograficznych)
  * [Krok 1: wyłapywanie najczęstszych błędów](#krok-1-wyłapywanie-najczęstszych-błędów)
  * [Krok 2: znajdowanie nieznanych słów](#krok-2-znajdowanie-nieznanych-słów)
  * [Krok 3: znajdowanie innych błędów ortograficznych](#krok-3-znajdowanie-innych-błędów-ortograficznych)
* [Podsumowanie](#podsumowanie)
* [Bonus: skrypt do analiz](#bonus-skrypt-do-analiz)

## Analizowanie ciągów wiadomości

Ciąg wiadomości rozumiem jako co najmniej jedną wiadomość pod rząd, wysłaną przez jedną i&nbsp;tę samą osobę. Takie *combo*.

Na pierwszy rzut oka nie daje nam to wielu dodatkowych informacji w&nbsp;porównaniu z&nbsp;patrzeniem na same wiadomości. Ale spójrzmy chociażby na tego mema!

{:.figure .bigspace}
<img src="/assets/posts/messenger2/krotkie-wiadomosci.jpg" alt="Zrzut ekranu z&nbsp;Messengera pokazujący krótkie dymki z&nbsp;wiadomościami, ułożone jeden pod drugim. Każdy z&nbsp;dymków zawiera tylko jedno słowo, a&nbsp;łącznie układają się w&nbsp;zdanie „Znajoma osoba, która w&nbsp;taki sposób pisze”. U&nbsp;góry dopisano tekst oznaczający w&nbsp;polskim tłumaczeniu „Wszyscy znamy kogoś takiego”." width="500px"/>

Obrazek z&nbsp;gatunku luźnych odmóżdżaczy. Takich, jakie wrzuca się na spamowe stronki, żeby ludzie oznaczali się w&nbsp;komentarzach, kwitując sprawę ambitnym „haha” albo roześmianymi emotami.

A jednak ma w&nbsp;sobie trochę prawdy -- **liczba wiadomości słanych pod rząd to mocny wyznacznik stylu pisania**.  
Jeśli ktoś raz wykształci określony styl, to raczej nieprędko się go pozbędzie. Wniosek: to cecha, którą by można korelować z&nbsp;innymi, żeby klasyfikować ludzi.

Przeciętną długość wiadomości (mierzoną w&nbsp;słowach i&nbsp;znakach) analizowaliśmy już w&nbsp;poprzednim wpisie.  
Liczba wiadomości wysłana pod rząd to drugi element układanki. Razem pozwoliłyby określić czyjś styl pisania -- czy zwykle podchodzi do wiadomości jak do maili, wysyłając dłuższe bloki? Czy może raczej „strzela krótkimi seriami”?

Zobaczę, jak z&nbsp;tym u&nbsp;mnie!

# Liczba różnych ciągów wiadomości

Poprzednia wersja mojego programu nie była zbyt przystosowana do wychwytywania ciągów wiadomości, bo szukała tylko tych od jednej konkretnej osoby, bez patrzenia na resztę.

Obecnie, po zmianach, działa w&nbsp;następujący sposób:

* Bierze wszystkie konwersacje, dwuosobowe i&nbsp;grupowe, w&nbsp;których brała udział jakaś osoba;
* Po kolei „przejeżdża” wzdłuż konwersacji, patrząc na autorów wiadomości.

  Jeśli znajdzie poszukiwaną osobę, to zaczyna tworzyć nowy ciąg.  
  Dodaje do niego wiadomości, dopóki to ta sama osoba je napisała.  
  Jeśli napotka wiadomość wysłaną przez kogoś innego, to znaczy że ciąg został przerwany. Można go odłożyć do osobnej listy.

* Po zebraniu wszystkich ciągów ze wszystkich konwersacji bierze się za ich analizowanie.

Skorzystałem z&nbsp;tego samego zestawu danych co przy poprzednim wpisie, bo nie chciało mi się pobierać nowych. Mam zatem **zbiór ponad 50 000 wiadomości napisanych na przestrzeni ponad 9 lat**.

Mając różne ciągi, można sobie stworzyć wykres ilustrujący, jak często się pojawiają. Ten dla moich wiadomości wygląda tak:

<img src="/assets/posts/messenger2/messenger-wiadomosci-wykres.jpg" alt="Wykres słupkowy pokazujący liczbę ciągów wiadomości. Oś pozioma to liczba wiadomości wysłanych w&nbsp;jednym ciągu, sięga wartości od 1 do 21. Oś pionowa to liczba wysłanych ciągów, które miały określoną długość. Widać, że im dłuższy ciąg wiadomości, tym rzadziej się pojawia."/>

{:.figcaption}
Wykres dla liczby ciągów o&nbsp;różnej długości. Podpisy osi i&nbsp;kolumn dodałem w&nbsp;osobnym programie.  

Najdłuższych ciągów jest mało w&nbsp;porównaniu z&nbsp;krótszymi, więc są w&nbsp;tej skali nieczytelne. Poniżej macie ich liczbę (w formacie `długość ciągu: liczba wiadomości`).

<div class="black-bg mono">
10: 13, 11: 7, 12: 7, 13: 1, 16: 1, 17: 1, 21: 1
</div>

Moim rekordem jest 1 ciąg złożony z&nbsp;21 wiadomości wysłanych pod rząd -- swoista relacja z&nbsp;podróży wrzucana do grupowej rozmowy (zdjęcia wymieszane z&nbsp;tekstem).

Patrząc na wykres, zauważymy pewną rzecz, która wydaje się dość naturalna -- **im dłuższy jest ciąg wiadomości, tym rzadziej się pojawia**.  
Takie „stopniowe wygasanie” jest czymś bardzo powszechnym w&nbsp;statystyce, w&nbsp;naturze zresztą też. Zainteresowani mogą poczytać o&nbsp;**rozkładach wykładniczych**.

Mając ciągi wiadomości, można zrobić kolejny krok!

# Szybkość pisania

Ilość tekstu, jaką ktoś jest w&nbsp;stanie stworzyć w&nbsp;określonym czasie. Wyrażana w&nbsp;znakach na minutę, słowach na minutę albo innych przekształconych jednostkach.

Uznałem, że to dość ciekawa statystyka. Może być czyjąś cechą charakterystyczną, podobnie jak sama tendencja do tworzenia krótkich bądź długich wiadomości.

W poprzednim punkcie patrzyłem na wszystkie ciągi wiadomości -- niezależnie od tego, czy zawierały tekst, obrazki, nagrania czy inne załączniki z&nbsp;Messengera.

Tym razem interesuje mnie tylko tekst, więc podzieliłem ciągi na krótsze, wycinając z&nbsp;nich wszelkie wiadomości z&nbsp;załącznikami.  
Poza tym wywaliłem też ciągi złożone z&nbsp;jednej wiadomości. Znam tylko godziny ich wysłania, a&nbsp;chcąc określić szybkość muszę również wiedzieć, kiedy ktoś zaczął je pisać.

W ten sposób moim materiałem źródłowym stały się ostatecznie ciągi złożone z&nbsp;co najmniej dwóch wiadomości tekstowych napisanych przez tę samą osobę.  
Czas wysłania pierwszej z&nbsp;nich przyjmuję za punkt początkowy. Przy każdej kolejnej, **dzieląc jej długość przez czas, jaki minął od wysłania poprzedniej, mogłem ustalić czyjąś szybkość pisania**. Oczywiście w&nbsp;przybliżeniu.

...Ale pozostaje pewien ważny szczegół! Zobaczmy na żywym przykładzie:

{:.figure .bigspace}
<img src="/assets/posts/messenger2/messenger-ciagi-wiadomosci.jpg" alt="Zrzut ekranu z&nbsp;Messengera pokazujący najpierw dwie wiadomości pod rząd (oznaczone cyfrą 1), a&nbsp;następnie dwie kolejne, oddzielone różnymi datami i&nbsp;oznaczone cyfrą 2."/>

Mamy tu dwa ciągi wiadomości, oznaczone jako 1 i&nbsp;2.

Ciąg 1 jest w&nbsp;porządku, bo sprowadza się do jednej myśli rozbitej na dwie wiadomości. Można założyć, że autor zaraz po wysłaniu pierwszej zaczął pisać kolejną. A&nbsp;zatem: da się tu zmierzyć szybkość pisania.

Z kolei ciąg 2 jest bardziej problematyczny -- są to niby wiadomości od tej samej osoby, ale wysłano je w&nbsp;różnych dniach (pomińmy już to, że druga z&nbsp;nich to obrazek). 

Wyobraźmy sobie ciąg złożony z&nbsp;dwóch wiadomości, z&nbsp;których druga brzmi „To jak?”. Czyli ma 7 znaków, licząc spację i&nbsp;znak zapytania.  
Gdyby została wysłana 2 godziny (120 minut) po pierwszej, to by nam wyszło 7/120, czyli szybkość około 0,06 znaku na minutę!

Sami przyznacie, że nie do końca oddawałoby to rzeczywistość. 

Dlatego musiałem przyjąć jakiś umowny zakres i&nbsp;odrzucać wartości spoza niego jako zbyt szybkie albo zbyt wolne, żeby moje średnie były nieco bardziej wiarygodne. Ostatecznie **za normę przyjąłem zakres od 100 do 400 znaków na minutę**.

Skąd górna wartość? Zasugerowałem się losowym wpisem [o szybkości pisania na klawiaturze](https://onlinetyping.org/blog/average-typing-speed.php). Znaczna większość badanych, w&nbsp;tym zawodowcy, nie przekraczała szybkości 80 słów na minutę (czyli właśnie 400 znaków, bo popularny przelicznik to 1 słowo = 5 znaków).

A minimum? Musiałem tu wziąć pod uwagę osoby piszące z&nbsp;urządzeń mobilnych, w&nbsp;tym niekoniecznie z&nbsp;wprawą.  
Ktoś zapytał o&nbsp;to na forum Quora. Według osoby ponoć zajmującej się tematem zawodowo, przeciętna szybkość pisania na mobilnych to [25-30 słów na minutę](https://www.quora.com/What-is-the-average-smartphone-users-typing-speed?share=1). Czyli 125-150 znaków.  
Bardziej niż średnia interesowało mnie minimum, więc asekuracyjnie przyjąłem 100 znaków. 

Wszystko to oczywiście subiektywne decyzje; poza tym nie uwzględniam czasu potrzebnego na wstawienie emotek z&nbsp;przybornika. Jak to mawiają: „Kiedyś jeszcze dodam nowe funkcjonalności” :wink:

Może i&nbsp;prowizorka, ale działa! Na podstawie moich wiadomości mieszczących się w&nbsp;zakresie pokazuje mi, że **piszę ze średnią szybkością 184 znaków na minutę**.  
Liczba nie powala, być może przez to, że to miks danych dla klawiatury i&nbsp;smartfona. Ale myślę, że nie jest jakoś bardzo odległa od rzeczywistości.

# Liczba wiadomości wklejonych

Wartości spoza przyjętego zakresu (w znakach na minutę), choć nie są liczone do średnich, nadal mogą nam coś ujawnić!

Wartości skrajnie niskie, oznaczające długie odstępy czasu między wiadomościami, nie wydają się aż takie ciekawe. Wpadłby tutaj każdy przypadek, kiedy jakaś osoba najpierw napisała „Do usłyszenia”, a&nbsp;ileś dni później sama napisała.

Ciekawsze wydają się wartości skrajnie wysokie. Co to znaczy, że ktoś nagle wyprodukował wiadomość w&nbsp;tempie kilku tysięcy znaków na minutę, zawstydzając stenotypistów?

Odpowiedź: w&nbsp;takim przypadku **ktoś zapewne wkleił treść wiadomości**. Jedno `Ctrl+V`, potem `Enter` i&nbsp;mamy dowolnie długi tekst w&nbsp;bardzo krótkim czasie.

Odkryłem, że w&nbsp;moich wiadomościach najczęściej wklejanym długim tekstem były linki i&nbsp;cytaty. Raczej małe zaskoczenie.
  
Druga możliwa przyczyna -- czasem pisałem coś dłuższego, ale jakaś osoba weszła mi w&nbsp;słowo. Wyciąłem pisaną wiadomość, wpisałem krótką odpowiedź na sprawy bieżące, a&nbsp;zaraz po niej wkleiłem poprzednio tworzony tekst, żeby wrócić do wątku.

Trzecia przyczyna -- ktoś mogł specjalnie tworzyć wiadomości „na brudno”, w&nbsp;osobnym programie, i&nbsp;dopiero potem przeklejać je do czatu/Messengera.  
Sam tak nie robiłem, ale wypatrzyłem parę przypadków u&nbsp;innej osoby -- w&nbsp;momencie, w&nbsp;którym zrobiło się poważnie i&nbsp;zaczęły lecieć ściany tekstu.

## Wyłapywanie błędów ortograficznych

# Krok 1: wyłapywanie najczęstszych błędów

Chcę znajdować błędy w&nbsp;języku polskim, powszechnie uważanym za trudny przez swoją sporą elastyczność i&nbsp;możliwość odmieniania słów (tak zwaną *fleksyjność*).

{:.figure}
<img src="/assets/posts/messenger2/polish-is-hard.jpg" alt="Przycięte zdjęcie pokazujące prezentację na konferencji. U&nbsp;góry widać nagłówek „Polish is hard”, a&nbsp;pod nim 98 odmian słowa „grać”."/>

{:.figcaption}
Źródło: [konferencja Euro Clojure 2016](https://dev.solita.fi/img/euroclojure-2016/polish-is-hard.jpg).

Do tego chcę to zmieścić w&nbsp;jednym prostym skrypcie; fajnie też, żebym nie wymagał od użytkowników pobierania gigabajtów dodatkowych słowników. Brzmi jak wyzwanie :sunglasses:

Uznałem, że na początek skupię się na najczęściej popełnianych błędach -- takich jak nieszczęsne pisanie *wogóle* zamiast *w ogóle*.  
Skrypt, nim zrobi coś sprytniejszego, po prostu przejrzy tekst wiadomości i&nbsp;poszuka konkretnych błędów z&nbsp;zamkniętej listy.

Listy najczęstszych błędów w&nbsp;internecie można znaleźć na różnych stronach; osobiście skorzystałem z&nbsp;[tej ze strony *polszczyzna.pl*](https://polszczyzna.pl/najczestsze-bledy-ortograficzne/).

Wprowadzenie listy do skryptu poszło dość szybko. Ale czułem niedosyt. Fajnie by było mieć coś ogólniejszego.

# Krok 2: znajdowanie nieznanych słów

Już w&nbsp;poprzednim wpisie znalazłem przybliżony i&nbsp;mocno niedoskonały sposób, żeby rozbijać wiadomości na słowa, z&nbsp;jakich się składają. Teraz czas trochę za te słowa pochwytać :smiling_imp:

Zacznijmy od podstawowej kwestii: **potrzebujemy jakiejś zamkniętej, w&nbsp;miarę sporej listy słów języka polskiego**. Będzie pełniła rolę wstępnego sita, odsiewającego słowa poprawne od niepoprawnych.

Jako swojej głównej listy użyłem [tej ze strony Słownika Języka Polskiego](https://sjp.pl/slownik/odmiany/sjp-odm-20211220.zip).

Po rozpakowaniu stosunkowo małego pliku ZIP (12 MB) otrzymujemy plik tekstowy ważący 67 MB, wypełniony po brzegi polskimi słowami i&nbsp;wyrażeniami!

Ale, żeby nie było zbyt pięknie, część z&nbsp;nich wydaje się dość niszowa:

{:.bigspace}
<div class="black-bg mono">
ab urbe condita<br/>
ab Urbe condita<br/>
ab urbe conditia<br/>
aba<br/>
ABA<br/>
abachit, abachicie, abachitach, abachitami, abachitem, abachitom, abachitowi, abachitów, abachitu, abachity<br/>
Abacja, Abacją, Abację, Abacji, Abacjo<br/>
Abadan, Abadanem, Abadanie, Abadanowi, Abadanu
</div>

Nie ma tam natomiast popularnych polskich słów-zapychaczy. Jednoliterowców takich jak *i*, *w*, *a*, wielu spójników i&nbsp;innych części mowy. Czyli akurat tego, co na pewno się pojawi w&nbsp;każdej rozmowie między ludźmi :roll_eyes:

Dlatego ta lista to jednak odrobinę za mało.
Żeby wypełnić lukę, zacząłem szukać kolejnego źródła. Interesował mnie język bardziej nieformalny i&nbsp;konwersacyjny, ale przy tym poprawny, więc wszelkie bazy twittów i&nbsp;tym podobnych odpadały.

Zaświtało mi: a&nbsp;może coś z&nbsp;książek? Znalazłem serwis [„Wolne lektury”](https://wolnelektury.pl/), a&nbsp;stamtąd wziąłem kilka książek w&nbsp;formacie TXT. Były to:

* „Ziemia obiecana”,
* „Znachor”,
* „Kariera Nikodema Dyzmy”.

Dwie książki Dołęgi-Mostowicza były moim subiektywnym wyborem, bo je lubię. Ale decyzja była częściowo pragmatyczna -- to jedne z&nbsp;najnowszych książek w&nbsp;zasobach. Z&nbsp;dwudziestolecia międzywojennego, do tego uwspółcześnione. Język powinien być zbliżony do tego stosowanego współcześnie.

A nawet gdyby zaplątały się jakieś archaiczne słowa, to mogłoby to tylko wyjść na dobre! Pamiętam ze swoich rozmów na czacie, że czasem odpowiedzią na „Chodźmy się napić” bywało „Dobrze waszmość prawisz”.

Format TXT idealnie się nadawał do szybkiego załadowania tekstów i&nbsp;rozbicia ich na słowa. Tak też zrobiłem, otrzymując swoją uzupełniającą listę słów. Do skryptu dodałem możliwość ładowania wielu list, żeby jeszcze łatwiej było rozszerzać w&nbsp;przyszłości jego możliwości.

{% include info.html type="Heheszki"
text="Korzystanie z&nbsp;książkowych źródeł miało pewien efekt uboczny -- otóż autorzy bywają kreatywni w&nbsp;wymyślaniu neologizmów. I&nbsp;tak oto na mojej liście, między całkiem zwyczajnymi i&nbsp;pospolitymi słowami, znalazło się *elektryczno-homeopatyczno-wegetariańsko-arszenikowej*:"
trailer="<p class='figure bigspace'><img src='/assets/posts/messenger2/nietypowe-slowa.jpg' alt='Zrzut ekranu pokazujący fragment listy słów. Jest wśród nich słowo „elektryczno-homeopatyczno-wegetariańsko-arszenikowej”.'/></p><p>W moich konwersacjach z&nbsp;Messengera niestety nie pojawiło się ani razu.</p>
"%}

Po załadowaniu obu list skrypt zaczął działać nieco sensowniej. Nadal zdarza mu się oznaczać całkiem normalne słowa jako dziwne, ale do wstępnego przesiewu, którego wynik sami ocenimy, jest w&nbsp;porządku. Wypatrzyłem dzięki niemu trochę swoich literówek (takich jak *sobocir* zamiast *sobocie*, *symie* zamiast *sumie*).
 
Oczywiście żadna z&nbsp;moich list słów by się nie sprawdziła przy słowach bardziej niszowych, takich jak terminologia związana z&nbsp;komputerami. Albo przy nowinkach jak „śpiulkolot” (młodzieżowe słowo roku 2021).

# Krok 3: znajdowanie innych błędów ortograficznych

Znajdowanie słów spoza listy znanych to dobry pierwszy krok, ale sam w&nbsp;sobie nie rozwiązuje sprawy.  
Jak widzieliśmy, wyniki trzeba oceniać na oko, żeby coś w&nbsp;nich znaleźć. Czasem na listę podejrzanych trafią rzeczy całkiem prawidłowe.

Ale pomyślałem sobie: w&nbsp;niektórych miejscach błędy pojawiają się częściej niż w&nbsp;innych. Zwłaszcza tam, gdzie różnym zapisom odpowiada ta sama wymowa. *Ch* zamiast *h*, *rz* zamiast *ż* i&nbsp;tak dalej.

Stąd pomysł: dla każdego słowa z&nbsp;listy nieznanych sprawdzę różne warianty pisowni. **Jeśli jakieś słowo nie znajduje się na liście, ale jego wariant z&nbsp;innym zapisem już tak, to mamy mocnego kandydata na błąd ortograficzny**.

Spójrzmy na przykład na dwa błędnie zapisane słowa -- *chex* i&nbsp;*chandel*. Pierwsze powinno brzmieć *Hex*, od nazwy gry planszowej, a&nbsp;drugie -- *handel*. 

1. W&nbsp;obu przypadkach skrypt odkrywa, że słowa nie ma na liście znanych;
2. Wypatruje w&nbsp;każdym ze słów często mylonych cząstek, znajduje *ch*;
3. Zamienia je na wariant z&nbsp;samym *h* i&nbsp;patrzy, czy taka wersja by była na liście;
4. *Handel* jest na liście. W&nbsp;związku z&nbsp;tym skrypt uznaje *chandel* za błąd ortograficzny.

   Z&nbsp;kolei *Hex* się na liście nie znajduje, bo raczej niewiele jest na niej obcych słów. W&nbsp;związku z&nbsp;tym *chex* pozostaje zwykłym nieznanym słowem -- wśród literówek i&nbsp;słów, które trafiły tam przypadkiem.

Rezultaty najgorsze z&nbsp;naszego punktu widzenia -- gdy skrypt zamiast dobrego słowa zaproponuje błędne -- powinny być raczej rzadkie (ale możliwe; poniżej napisałem o&nbsp;tym ciekawostkę).

Częstszym przypadkiem będzie zaliczenie błędu ortograficznego do zwykłych słów nieznanych. Ale takie działanie, choć nie idealne, nie jest też jakimś wielkim problemem.

A gdy już metoda działa, to działa -- wyłapuje niektóre współczesne koszmarki, takie jak „ludzią” zamiast „ludziom”.

{% include info.html type="Ciekawostka"
text="Póki nie udoskonaliłem listy o&nbsp;słowa z&nbsp;książek, potrafiło dochodzić do śmiesznych sytuacji. Przykład: komputer z&nbsp;całym autorytetem próbował mi wmówić, że zamiast „*są*” powinienem pisać „*som*”.  
Wynikało to z&nbsp;faktu, który wcześniej opisałem -- na liście z&nbsp;SJP nie było wielu powszechnych słów, w&nbsp;tym również „*są*”. Były z&nbsp;kolei niszowe rzeczowniki. „*Som*” to dopełniacz słowa „*soma*”, oznaczającego po grecku „ciało”.  
Pytanie, skąd się wzięło na liście słów polskich. Obstawiam jakieś biblijne zapożyczenia, ale pewności nie mam."
trailer="<div class='black-bg mono'>soma, <span class='red'>som</span>, somach, somami, somą, somę, somie, somo, somom, somy</div>"
%}

## Podsumowanie

Patrząc na te analizy, ktoś mógłby wzruszyć ramionami i&nbsp;zapytać mnie: „Po co?”.

Dla frajdy! Robienie tego było fajną odskocznią na te niby-to-zimowe popołudnia i&nbsp;wieczory, dało mi niemało endorfin. Na tej odpowiedzi możemy poprzestać, bo wyjaśnia wszystko.

Ciekawszym pytaniem byłoby dla mnie to z&nbsp;motywu przewodniego tej serii: „Co wie o&nbsp;nas Facebook?”.

Nie twierdzę, że też nam liczy szybkość pisania czy liczbę błędów. Patrząc na to, jak mu czasem idzie odmienianie polskich imion i&nbsp;nazwisk, nie uważam go za materiał na korektora :wink:

Ale tak naprawdę nie wiemy, co tam za kulisami robi.

Korzysta z&nbsp;elastycznych algorytmów, ściślej nazywanych uczeniem maszynowym, a&nbsp;marketingowo -- sztuczną inteligencją. I&nbsp;prawie na pewno, upychając nas w&nbsp;odpowiedniej przegródce dla reklamodawców, patrzy na treść wiadomości.

W ten sposób, zestawiając wielkie zbiory z&nbsp;Messengera i&nbsp;innych źródeł, może sobie wyliczać korelacje.

Nie mamy pewności, czy nasze krótkie, rwane i&nbsp;czasem niegramatyczne wiadomości nie będą ostatnią kroplą, która przeleje czarę i&nbsp;przerzuci nas do klastra numer 1237 (liczby wymyślam). Który będziemy dzielili raczej z&nbsp;patologią.  
A to może oznaczać, że Fejs będzie nam wciskał reklamy tandety, chwilówek i&nbsp;patostreamów. Ilekroć odwiedzimy swój profil albo powiązane strony.

A może mówię stereotypami? A&nbsp;nasze krótkie, szybkie i&nbsp;niegramatyczne wiadomości skorelują w&nbsp;oczach Fejsa ze sławą i&nbsp;biznesem, profilami kadr menedżerskich?  
Trafimy do klastra numer 1337. Będzie nam wciskało reklamy markowej tandety, kredytów mieszkaniowych i&nbsp;sesji coachingowo-lifestyle'owych.

A może raz ten klaster, raz ten? W&nbsp;zależności od fazy księżyca w&nbsp;dniu, kiedy algorytmy podejmowały decyzję?

W tym sęk -- **bardzo mało wiemy o&nbsp;tym, w&nbsp;jaki sposób Facebook nas klasyfikuje**. Mogę tylko teoretyzować na temat mechanizmu, jakim się kieruje. Ale wiemy na pewno, że efekt końcowy tych klasyfikacji [potrafi być nieprzyjemny](https://panoptykon.org/algorytmy-traumy).

Na chwilę zostawię Messengera w&nbsp;spokoju. Zapewne wrócę z bardziej złożonymi metodami, takimi jak analiza składniowa albo analiza sentymentu (tzn. patrzenie na ogólny bilans pozytywnych i&nbsp;negatywnych zwrotów w&nbsp;różnych wiadomościach).

Ale do tego czasu zajmę się innymi aspektami naszych (a może już Facebooka?) danych. Do zobaczenia w&nbsp;kolejnych wpisach!

## Bonus: skrypt do analiz

To bezpośrednie rozszerzenie mojego poprzedniego skryptu, więc działa niemal identycznie -- po prostu tworzy więcej statystyk i&nbsp;plików z&nbsp;dodatkowymi informacjami.

**Uwaga: Nie mam na razie możliwości przetestowania skryptu na komputerze z Windowsem. Gdyby coś nie działało, to poczekajcie tak z tydzień (do 23.01). Gdy sprawdzę i będzie OK, to zaktualizuję tę notkę.**

1. Instalujecie Pythona, jeśli jeszcze go nie macie.
2. Pobieracie <a download href="/assets/skrypty/messenger_stats_v2.py">nową wersję mojego skryptu</a> i umieszczacie go w&nbsp;tym samym folderze co swoje dane pobrane z&nbsp;Facebooka (w tym wiadomości z&nbsp;Messengera). Możecie je rozpakować albo pozostawić w&nbsp;pliku ZIP.
3. Pobieracie [listę słów od SJP](https://sjp.pl/slownik/odmiany/sjp-odm-20211220.zip). Rozpakowujecie zipa w&nbsp;tym samym folderze, w&nbsp;którym jest skrypt.
4. Pobieracie [plik ZIP z&nbsp;moją listę uzupełniającą](/assets/posts/messenger2/MY_WORDLISTS.zip). Również rozpakowujecie go tam gdzie skrypt. Do powstałego folderu `MY_WORDLISTS` możecie wrzucać własne listy słów.
5. Otwieracie plik ze skryptem, korzystając na przykład z&nbsp;domyślnego edytora IDLE. Odpalacie go (w przypadku IDLE klawiszem `F5`).

   W&nbsp;domyśle skrypt przeanalizuje wiadomości osoby, która brała udział w&nbsp;największej liczbie konwersacji. Czyli zapewne Wasze.

6. W&nbsp;folderze powstanie podfolder nazwany od analizowanej osoby. A&nbsp;w&nbsp;nim kilka plików.

   Najważniejszy to raport w&nbsp;formacie HTML zawierający różne statystyki dotyczące Waszych wiadomości (po kliknięciu zapewne otworzy się w&nbsp;przeglądarce, ale bez obaw, nic nie wysyła do internetu!).  
   Oprócz tego w&nbsp;osobnym podfolderze znajdziecie kilka plików tekstowych: wszystkie wiadomości ułożone chronologicznie, listę słów nieznanych, listę potencjalnych błędów ortograficznych, listę szybko napisanych wiadomości.

...A jeśli, zamiast włąsnych, chcecie sprawdzić wszystkie wiadomości od konkretnej osoby, z&nbsp;którą pisaliście, to wpisujecie jej imię pod koniec skryptu, przy zmiennej `name`, między cudzysłowami.

Miłego łapania ludzi za błędy sprzed lat! (Z nadzieją, że sami ich nie popełniacie. Kocioł garnkowi, drzazga w&nbsp;oku i&nbsp;te sprawy :smiling_imp:).
