---
layout: post
title:  "Statystyki z Messengera"
subtitle: "Co mówią o nas wiadomości."
description: "Co mówią o nas nasze wiadomości"
date:   2021-05-14 20:32:00 +0100
tags: [Analiza danych, Porady]
firmy: [Facebook]
category: facebook_dane
category_readable: "Kochajmy się jak bracia, analizujmy się jak Facebooki"
image: "messenger-analiza/statystyki-baner.jpg"
image-width: 1200
image-height: 889
---

Witajcie w&nbsp;kolejnym wpisie poświęconym analizowaniu rzeczy z&nbsp;Facebooka! :smile: Dawnośmy już tu nie gościli tej serii.

Poprzednio pokazałem, w&nbsp;jaki sposób można pobrać swoje dane z&nbsp;Facebooka. Opisałem też krótko, jakie wiązały się z&nbsp;nimi problemy. A&nbsp;teraz czas na wiadomości z&nbsp;Messengera.

W pierwszej części wpisu opisuję różne ciekawostki ze swoich danych.

W [części drugiej](#przygotowanie-danych) opisuję różne przeszkadzajki, z&nbsp;którymi musiałem się uporać, żeby wyciągnąć te ciekawostki.

Część [trzecia](#skrypt) to link do skryptu, którego użyłem.  
Wystarczy go pobrać i&nbsp;odpalić, żebyście również dla swoich danych stworzyli krótkie podsumowania.

W tym taki sympatyczny histogram dla godzin, w&nbsp;których wysłaliście wiadomości:

<img src="/assets/posts/messenger-analiza/statystyki-baner.jpg"/>

{% include info.html type="Porada" text="Jeśli interesuje Was tylko część z&nbsp;powyższych rzeczy, to możecie swobodnie do niej przeskoczyć. Są od siebie raczej niezależne."%}

Zanim zaczniemy, uprzedzę lojalnie: wpis nie zawiera popularnego w&nbsp;ostatnich latach *data science*. Głównie dlatego, że *data science* tworzy się na laptopach srebrnych, siedząc na pufie w&nbsp;pozycji kwiatu lotosu.  
Ten wpis natomiast powstał na laptopie czarnym, głównie na meblach drewnianych i&nbsp;topornych. Jest tu tylko zwykła statystyka ze średnimi i&nbsp;medianami.

Nie odstraszyłem? To zapraszam do lektury!

## Analiza

Moje statystyki są proste. Liczę różne rzeczy znajdujące się w wiadomościach, czasem patrzę jaki to procent wszystkich rzeczy.

Patrzyłem na kilka kryteriów:

* Długość wiadomości.
* Godziny wysłania wiadomości.
* Użyte ciągi emoji.
* Dodane załączniki.
* Otrzymane reakcje.

Przejdźmy do rzeczy!

**Plik HTML z&nbsp;moimi statystykami** znajdziecie <a href="/assets/posts/messenger-analiza/bob_adook_raport.html" rel="noindex" target="_blank">tutaj</a>.

Nie wstydzę się niczego, zresztą kto wie, czy to moje prawdziwe dane :smiling_imp:. Usunąłem z&nbsp;niego natomiast niektóre daty i&nbsp;listę ludzi dających reakcje.

Parę ogólnych uwag:

Starałem się patrzeć na wartości względne. Co nam powie suchy fakt, że ktoś wysłał 1000 emot? Będzie to miało inne znaczenie, jeśli od takiej osoby mamy łącznie 2000 wiadomości, a&nbsp;inne, jeśli mamy ich 20 000.  
Jeśli przedstawimy to jako procent od łącznej ilości, to łatwiej nam będzie porównywać.

Poza tym sprawdzałem tylko te osoby, od których mam tysiące wiadomości (zarówno z&nbsp;konwersacji pojedynczych, jak i&nbsp;grupowych). Im próba większa, tym wiarygodniejsza.

Czas na trochę poanalizowania siebie i&nbsp;innych.

# Długość wiadomości

Niektórzy wyrzucają serie krótkich wiadomości jak z&nbsp;karabinu, dorzucając treść na bieżąco. Inni podchodzą do nich jak do maili i&nbsp;tworzą dłuższy blok tekstu.  
Statystyka pozwala wyłapać te dwa przypadki.

Rozstrzał jest tutaj naprawdę spory. Od osób używających przeciętnie 6 słów na wiadomość do takich piszących całe elaboraty. A&nbsp;patrzymy na średnie z&nbsp;tysięcy wiadomości, więc to dość wiarygodne dane.

U osób bardziej zwięzłych wychodzi mi średnia 30-40 znaków i&nbsp;5-6 słów na wiadomość.

Ja jestem z&nbsp;tych bardziej rozpisanych. średnio 99 znaków na wiadomość, mediana to 75.  
(w czym jednak nie jestem wyjątkiem, bo jedna osoba miała niemal identyczne statystyki -- jeśli to czytasz, A., to pozdrawiam! :smile:).

Może też zastanawiać różnica między moją średnią a&nbsp;medianą. Gdybym pisał konsekwentnie wiadomości o podobnej długości, to średnia i mediana byłyby równe.

Tymczasem u mnie średnia jest o ponad 1/4 większa. Co to znaczy?  
Widocznie miałem trochę wyjątkowo długich wiadomości (linki? Listy zakupów? Większe dramy?), które jednak nie są reprezentatywne.

Ze swoimi statystykami chowam się przy rekordzistce z&nbsp;medianą 104 znaków i&nbsp;19 słów na wiadomość. Którą zresztą szanuję, bo te wiadomości to często fajne relacje z&nbsp;podróży!

Unikalnych słów użyłem ponad 64 000. Nie wierzyłbym temu bezgranicznie, bo jedno słowo potrafi się pojawić w&nbsp;wielu przypadkach (np. *góra*, *górze*, *górom*...).

Patrząc na to, że polskie słowniki potrafią liczyć [po kilkaset tysięcy haseł w&nbsp;różnych odmianach](https://sjp.pwn.pl/poradnia/haslo/Ile-slow-liczy-jezyk-polski;5606.html), mam tu jeszcze sporo słów do zebrania :wink:

# Godziny wysłania

Mam pełne informacje o datach i&nbsp;godzinach wysłania wiadomości. Skupiłem się na godzinach, żeby wyłapać wśród znajomych sowy i&nbsp;skowronki.

Zrobiłem tutaj wykresy częstości, żeby dało się porównywać dane -- czyli **ile procent wszystkich wiadomości wysłano o&nbsp;określonej godzinie**  
(gdybym brał suchą liczbę wiadomości, przytłoczyłbym innych. W&nbsp;końcu mam kilkadziesiąt tysięcy, a oni kilka).

W przypadku moich danych widać wyraźnie dwie górki. Mniejsza rano, mniej więcej po pełnym dobudzeniu. Druga w&nbsp;godzinach wieczornych i&nbsp;nocnych. To wtedy się uaktywniam.

Niektóre osoby są z&nbsp;kolei bardziej wyważone i&nbsp;można je dorwać o&nbsp;dowolnych godzinach w&nbsp;ciągu dnia.  
Poniżej porównanie takich dwóch wykresów, mojego i&nbsp;cudzego.

<img src="/assets/posts/messenger-analiza/wykresy-porownanie.webp" alt="Dwa wykresy słupkowe ustawione jeden pod drugim. W&nbsp;przypadku górnego najwyższy słupek wypada o&nbsp;godzinie 21, a&nbsp;poranne są względnie niskie. W&nbsp;przypadku dolnego słupki od godziny 11 mają zbliżoną wysokość"/>

Zaznaczam jednak, że moje dane dla innych osób mogą być obarczone błędem, bo zależą od mojego trybu życia. W&nbsp;końcu nie napiszę do kogoś, kiedy sam śpię! A&nbsp;zatem nie dostanę odpowiedzi, która by się liczyła do statystyk.

Odrobinę tutaj pomagają konwersacje grupowe, ponieważ ludzie mogą pisać o&nbsp;różnych godzinach. I&nbsp;jeśli ktoś faktycznie nie śpi, to odpisuje, dając cenne punkty danych.

No i&nbsp;marzenie nadgorliwego menedżera -- mając znacznik czasu, można łatwo sprawdzić, czy ktoś wysłał wiadomość w&nbsp;czasie pracy!

Wprowadziłem osobną statystykę: **jaki procent wszystkich wiadomości został wysłany między poniedziałkiem a&nbsp;piątkiem i&nbsp;między 8:00 a&nbsp;16:00**? Zobaczymy, kto się messengeruje zamiast pracować!

U mnie wyszło 25%, z&nbsp;czego część zapewne w&nbsp;czasie wolnym. Nuuda.  
Ale u&nbsp;rekordzistki to już 70,5%. Bez obaw, M., nie wypaplam nikomu.

Żeby dopracować metodę, mógłbym zebrać listę dni ustawowo wolnych i&nbsp;nie liczyć tego, co napisano w&nbsp;ich trakcie. Ale wciąż nie miałbym sposobu na odjęcie dni urlopowych, które mogą wypadać kiedykolwiek.

Natomiast, jeśli kiedyś korpolobby zniesie kiedyś przepisy o&nbsp;ochronie danych, to mam taką wizję:

> Facebook zakłada usługę *Employee Productivity by Facebook*.  
Korpo w&nbsp;ramach subskrypcji mogą im wysyłać arkusze z grafikiem swoich pracowników sprzed jakiegoś czasu. A&nbsp;w odpowiedzi dostaną elegancki raporcik z&nbsp;informacją, ile wiadomości wysłały te osoby przez Messengera w&nbsp;czasie pracy.  
Potem dowalą im jakieś *review*, *coaching*, *Performance Improvement Plan* albo *immediate termination*, w&nbsp;zależności od przewinienia.  
*Welcome to the future* :smiling_imp:

# Załączniki

W tych przypadkach, na które patrzyłem -- w&nbsp;tym moim własnym -- najczęściej do wiadomości dodaje się zdjęcia i&nbsp;naklejki. Bez większego zaskoczenia.

Ujawnia się natomiast moja awersja do filmów i&nbsp;GIF-ów, są rzadkie (pojawiły się odpowiednio 9&nbsp;i&nbsp;5&nbsp;razy).  
Jakoś nie przekonałem się do tych wszystkich Tenorów i&nbsp;innych bibliotek z&nbsp;GIF-ami. Jeśli wstawiam taki plik, to częściej skopiowany z&nbsp;przeglądarki.

W&nbsp;miarę często podrzucam za to pliki i&nbsp;linki do różnych rzeczy. Może dlatego, że na komputerze to kwestia paru kliknięć? A&nbsp;używam go częściej niż telefonu.

U niektórych te proporcje wyglądają zgoła odwrotnie -- linki i&nbsp;pliki szorują po dnie, są najrzadszym załącznikiem.

Czy może to wynikać z&nbsp;faktu, że takie osoby częściej używają aplikacji na telefonie? Przez co dodanie linka wymagałoby od nich:

* wyjścia z Messengera,
* otwarcia przeglądarki i&nbsp;jakiejś strony,
* skopiowania linka (niektórzy nawet nie wiedzą jak!),
* ponownego otwarcia Messengera,
* wklejenia linka?

Linki mogą się nie lubić z telefonami. Taka hipoteza.

Wyszła mi też ciekawa rzecz -- niektóre z&nbsp;moich starszych wiadomości, skądinąd całkiem zwyczajne i&nbsp;pozbawione załączników, dostały atrybut „Nieznany rodzaj” (czyli nazwę, jaką zostawiłem dla nierozpoznanych).  
Okazało się, że ten atrybut nazywał się `ip` i zawierał... mój adres IP. Nie mam pojęcia, skąd się wziął i&nbsp;czemu akurat w&nbsp;tych wiadomościach. Sprawa do zbadania.

# Reakcje i&nbsp;emoji

**Po reakcjach można poznać, czy ktoś używa Messengera przez telefon**. Wersja komputerowa daje możliwość wybrania jednej z&nbsp;7&nbsp;reakcji. Przez aplikację można wybrać oprócz tego dowolną emoji z&nbsp;przybornika.

Wniosek? Jeśli ktoś daje jako reakcję coś niestandardowego, to wiemy że właśnie używa aplikacji.

{% include info.html type="Ciekawostka" text="Na początku zamiast emoji czerwonego serca **jedną z&nbsp;kilku domyślnych reakcji była buźka z&nbsp;sercami w&nbsp;oczach**. Serce stopniowo ją wyparło.  
Zatem, gdyby w&nbsp;roli reakcji pojawiły się serca w&nbsp;oczach, to nie znaczy że ktoś używa niestandardowych emot. Po prostu pisał w&nbsp;czasach, gdy niektórych jeszcze na świecie nie było. Sam na przykład zebrałem 224 sercookie reakcje.  
Zresztą reakcje jako takie też są względnie nowe, pojawiły się [w 2017 roku](https://about.fb.com/news/2017/03/introducing-message-reactions-and-mentions-for-messenger/)." %}

Kolejna ciekawostka: najwięcej zebrałem reakcji domyślnych (polubienie, śmiejąca się emota, serce, zdziwiona emota). Każda z&nbsp;nich pojawiała się kilkadziesiąt razy więcej niż te niestandardowe.  
Mimo dostępu do pełnego przybornika z&nbsp;emotami, ludzie jednak trzymają się podstaw.

Tyle tytułem reakcji, przejdźmy do emoji w&nbsp;tekście.

W ich przypadku przede wszystkim można sprawdzić, jak często ktoś ich używa. Niektórzy dodają je notorycznie, a&nbsp;inni mają raczej alergiczny stosunek.

I tak rekordzistka z&nbsp;moich konwersacji używa emot w&nbsp;70,4% wiadomości. U&nbsp;mnie też goszczą często, w&nbsp;58,1%.

Kolejna sprawa to rozróżnienie między emotami „tekstowymi” (jak `:D`) a&nbsp;obrazkowymi, wybranymi z&nbsp;przybornika. Dokładniej to opisuję w&nbsp;dalszej części wpisu.

Jaskrawym przykładem jest jedna z&nbsp;moich znajomych, która użycie emot ma całkiem spore (637, w&nbsp;62,5% wiadomości)... ale jest wśród nich dokładnie 0 emot obrazkowych. Wszystko wpisane z&nbsp;klawiatury.

Gdyby kiedyś zaczęła wysyłać obrazkowe, to jest ryzyko, że ktoś się podszywa :wink:

Kolejna rzecz? Powtarzalność. Można sprawdzić, **kto lubi urozmaicenie i&nbsp;często daje różne kombinacje emot**. A&nbsp;kto woli trzymać się kilku takich samych.

Osobiście nie mam duszy do eksperymentów. 418 unikalnych ciągów emoji w&nbsp;całej historii wiadomości (na prawie 33 000 wszystkich).

Dla porównania bardziej *emojionalna* znajoma nabiła 219 unikalnych ciągów na 1815 wszystkich. Gdyby sprawdziła wszystkie swoje dane, to ta liczba na pewno jeszcze by wzrosła.

Niby zwykłe głupie obrazki, a&nbsp;ile radochy z&nbsp;analizy!

A samą analizę może na tym zakończę. Myślę, że pokazałem już, że nawet samo liczenie rzeczy, bez większych bajerów, może zdradzić ciekawe informacje i&nbsp;zwyczaje ludzkie.

Jeśli chcecie stworzyć taki sam raport dla siebie, to [łapcie skrypt](#skrypt).  
A jeśli ciekawią Was kulisy moich analiz, to czytajcie dalej.

## Przygotowanie danych

# Ułożenie folderów

Jeśli aktywnie używamy Facebooka, to **wiadomości prawie na pewno będą największą częścią naszych danych**.  
Głównie przez różnego rodzaju obrazki. Nawet jeśli sami ich nie dodamy, to wystarczy spam w&nbsp;wykonaniu innych, żeby skrzynka szybko się rozrosła.

Jeśli zaznaczyliśmy na Fejsie, że chcemy w&nbsp;pakiecie z&nbsp;naszymi danymi pobrać też wiadomości, to w&nbsp;otrzymanym ZIP-ie znajdziemy folder `messages`.

W nim mamy pięć podfolderów:

<table>
<tr><td>used<wbr>_stickers</td><td>folder z&nbsp;obrazkami dodawanymi do wiadomości jako tzw. naklejki</td></tr>
<tr><td>inbox</td><td>główny folder z&nbsp;konwersacjami</td></tr>
<tr><td>message<wbr>_requests</td><td>konwersacje z&nbsp;facebookowej zakładki „Inne”. Czyli np. wiadomości od osób spoza grona znajomych, na które nie odpowiedzieliśmy</td></tr>
<tr><td>filtered<wbr>_threads</td><td>taki śmietnik na te konwersacje, które sami wybraliśmy, żeby nam się nie wyświetlały. Stopień wyżej od wyciszenia</td></tr>
<tr><td>archived<wbr>_threads</td><td>konwersacje, które opuściliśmy – wiadomości tylko do momentu odejścia</td></tr>
</table>

Przypomnę też krótko, czym jest Messengerowa konwersacja. Nie musi być prywatna, między dwiema osobami. Ma formę *czatu*. Można w&nbsp;dowolnym momencie dodawać nowe osoby albo opuszczać „pokój rozmów”. Każda z&nbsp;osób uczestniczących może dodawać tekst, pliki, nagrania głosowe itp.

W głównych folderach znajdują się podfoldery. Każdy odpowiada jednej konwersacji i&nbsp;zawiera materiały dodatkowe (wysłane w&nbsp;tej konwersacji zdjęcia, GIF-y itp.). A&nbsp;także plik albo pliki w&nbsp;formacie JSON z&nbsp;wiadomościami wymienionymi w&nbsp;konwersacji.

To te pliki JSON analizujemy.

# Budowa plików

Tak wygląda treść przykładowego pliku z&nbsp;konwersacją dwóch osób w&nbsp;formacie JSON:

{:.figure .bigspace}
<img src="/assets/posts/messenger-analiza/json-wiadomosc.webp" alt="Zrzut ekranu z&nbsp;pliku JSON z&nbsp;wiadomościami. Kolorem pomarańczowym otoczono element pierwszy, nazwany 'participants', a zielonym treść jednej z&nbsp;kilku wiadomości z&nbsp;listy."/>

Nawiasy kwadratowe wydzielają proste listy, a&nbsp;nawiasy wąsate -- tzw. słowniki (listy złożone z par nazwa-wartość). Te dwa rodzaje elementów mogą być w&nbsp;sobie zagnieżdżone.

W pliku są dwa najważniejsze elementy: `participants` (uczestnicy) i&nbsp;`messages` (wiadomości). Jest też parę innych rzeczy, ale nie znalazłem dla nich zastosowania.

Zieloną ramką otoczyłem z&nbsp;kolei przykładową wiadomość. Jej atrybuty to:

<table>
<tr><td><code>sender<wbr>_name</code></td><td>Kto wysłał wiadomość.</td></tr>
<tr><td><code>timestamp<wbr>_ms</code></td><td>Znacznik czasu; kiedy wysłano.</td></tr>
<tr><td><code>content</code></td><td>Tekst wiadomości.</td></tr>
<tr><td><code>reactions</code></td><td>Lista reakcji w&nbsp;formie emoji pod wiadomością. Każda z&nbsp;nich ma atrybut <code>reaction</code> (jaka to emota) oraz <code>actor</code> (kto ją wysłał).</td></tr>
<tr><td><code>type</code></td><td>Mówi, czy to wiadomość od kogoś czy komunikat od Messengera.</td></tr>
<tr><td><code>is_<wbr>unsent</code></td><td>Czy wiadomość została usunięta.</td></tr>
</table>

Oprócz tego niektóre wiadomości mogą mieć dodatkowe atrybuty (takie jak załączniki -- zdjęcia, GIFY, pliki, nagranie itp.). Sam nie znam i&nbsp;nie znalazłem ich pełnej listy, więc eksperymentowałem.

# Uczestnicy

Na początku wydawało się kuszące, żeby po wczytaniu pliku nie czytać wszystkiego i&nbsp;sprawdzić pod elementem `participants`, czy ktoś w&nbsp;ogóle tam pisał.  
Niestety, **jeśli ktoś opuścił konwersację, to go na tej liście nie będzie**. A&nbsp;wiadomości takiej osoby pozostaną.

Dlatego dla pewności, zamiast patrzeć na listę spod `participants`, po prostu zbierałem wszystkie wiadomości i&nbsp;odczytywałem ich autorów.

Zatem sposób na jeden z dwóch głównych elementów to zignorowanie :sunglasses:  
A co z&nbsp;samymi wiadomościami? Każda zawiera kilka cennych elementów, które trzeba rozpracować na różne sposoby.

# Daty

Elementy `timestamp_ms` to daty wysłania wiadomości. W&nbsp;takim dość popularnym formacie -- jako liczba jednostek czasu, jakie upłynęły od punktu zero (ustalonego umownie na rok 1970).

Na odczytywanie dat ze znaczników czasu już znalazłem sposób w&nbsp;pierwszym wpisie, ale te są nieco inne. Tutaj mamy `timestamp_ms`. **W&nbsp;milisekundach, a&nbsp;nie sekundach**.

Zatem po prostu dzielę taką liczbę przez *1000*, żeby przeliczyć na sekundy. A&nbsp;potem wrzucam do konwertera, domyślnie dostępnego w&nbsp;Pythonie. Otrzymuję datę wysłania wiadomości.

```python
from datetime import datetime

# A przy czytaniu danych...
timestamp = data[ "timestamp_ms" ] // 1000
date = datetime.fromtimestamp( timestamp )
```

# Emoji

Mogą pojawiać się zarówno w&nbsp;samym tekście wiadomości, jak i&nbsp;na liście otrzymanych reakcji.

Reakcje muszą być „prawilnymi” emoji z&nbsp;zamkniętej listy, więc nie sprawiają kłopotów. Pewien niuans pojawia się za to przy wiadomościach.

Z punktu widzenia użytkownika sprawa jest prosta. Korzystając z&nbsp;Messengera, wpisujemy skrót emoty z klawiatury (np. `:P`, `:|` itp.) albo wybieramy ją z&nbsp;przybornika. Emota się pojawia.

Okazuje się jednak, że Facebook zapisuje te dwie odmiany zupełnie inaczej.  
**Jeśli wpiszemy emoji jako skrót tekstowy, to właśnie tak zapisze się w&nbsp;pliku**. Jeśli wstawimy jako obrazek, to w&nbsp;pliku JSON-a zapisze się kod odpowiadający emoji.

Poniżej przykład (z popsutym kodowaniem Facebooka):

<table style="text-align:center">
<tr><th>Co wstawiamy</th><th>Co widać</th><th>Co widać w&nbsp;danych</th></tr>
<tr><td>:D</td><td><img src="/assets/posts/messenger-analiza/fb-emoji.webp"/></td><td>:D</td></tr>
<tr><td><img src="/assets/posts/messenger-analiza/fb-emoji-kot.webp"/></td><td><img src="/assets/posts/messenger-analiza/fb-emoji-kot.webp"/></td><td class="mono">\u00f0\u009f\u0090\u00b1</td></tr>
</table>

{% include info.html type="Heheszki" trailer="<p>Na Messengerze da się zamiast domyślnego polubienia (kciuka w&nbsp;górę) ustawić własną emotę. Na przykład głowę kota z&nbsp;przykładu.</p>
<p>Jednak, jeśli klikniemy takie nietypowe polubienie, to w&nbsp;pliku z&nbsp;danymi będzie to wyglądało dokładnie tak, jak wiadomość mająca w&nbsp;treści tę jedną emotę.</p>
<p>Doszło przez to do ciekawej sytuacji. <strong>U jednego ze znajomych, pod pewnymi względami tradycjonalisty, najczęściej używaną emotą jest tęcza</strong>.<br/>
Dlaczego? Bo sam z&nbsp;siebie prawie nie dodaje emot obrazkowych. Za to w&nbsp;jednej konwersacji, z&nbsp;motywem „rzygania tęczą”, ktoś ustawił ją jako polubienie. Znajomy dał parę lajków i&nbsp;emota tęczy zdominowała mu statystyki :smiling_imp:</p>" %}

Jak się później okaże, rozróżnienie na emoty tekstowe i&nbsp;obrazkowe może być źródłem cennych informacji.  
Ale bywa to też trochę uciążliwe. Żeby nie przegapić takich tekstowych emot, muszę znajdować ich listę w&nbsp;internetach, żeby potem je rozpoznawać w&nbsp;tekście.  
Czasem te listy, [takie jak ta](https://www.webnots.com/facebook-emoji-keyboard-shortcuts/), zawierają nieprawdziwe informacje (tu na przykład nie działa pingwin).

Kolejna sprawa to złożone emoty. Niektóre z&nbsp;nich, **choć wydają się jednym obrazkiem, za kulisami składają się z&nbsp;kilku pomniejszych znaków**.

To na przykład wszelkie emoty pokazujące postacie o&nbsp;jakimś odcieniu skóry. Tworzy się je przez połączenie emoty głównej z&nbsp;emotą odpowiadającą kolorowi. Jeśli ktoś wyśle ciemnoskórego kciuka w&nbsp;górę, to w&nbsp;danych wygląda to tak, jakby wysłał ogólnego kciuka, a&nbsp;zaraz po nim koło wypełnione ciemnym kolorem.

Na chwilę obecną nie rozwiązałem jeszcze tej sprawy. Znalazłem kod, który pozwala dokładniej grupować emoty, ale wymaga dodatkowego modułu Pythona (więc zdradziłbym ideę „pobierz i&nbsp;odpal”). Do tego działa raczej powoli. Dlatego póki co nastawcie się na rozszczepione emotki.

Ostatnia zagwozdka to dłuższe ciągi emoji.  
Czasem kilka emot wysłanych pod rząd ma po prostu zwiększać efekt (tak jak np. potrójny wykrzyknik w&nbsp;zdaniu).  
Ale niektóre kombinacje mają specjalne znaczenie -- choćby [zestaw oko-usta-oko](https://knowyourmeme.com/memes/eye-mouth-eye-emoji-%F0%9F%91%81%F0%9F%91%84%F0%9F%91%81), który lubią młodsze pokolenia.

Gdybym chciał tu być perfekcjonistą, to bym musiał przechowywać listę takich specjalnych kombinacji. A&nbsp;i tak nie byłoby to stuprocentowo skuteczne.

Na szczęście poprzednia sprawa niejako narzuca rozwiązanie. Nie rozdzielam emoji, bo w&nbsp;obecnym stanie bym przez to rozbijał niektóre z&nbsp;nich na części. Patrzę na całe ich ciągi. Więc trzy uśmieszki jeden po drugim traktuję jak coś innego niż pojedynczy.

# Tekst

Jesli chcę patrzeć tylko na liczbę znaków, to sprawa wydaje się prosta -- główny problem to głupie Facebookowe kodowanie. Ale jeśli już go rozwiązałem, to wystarczy pewnie po prostu zgarnąć tekst?

I tak obecnie robię, ale jest tu wiele możliwości poprawy. Przede wszystkim, kiedy ktoś wrzuca długiego linka, a&nbsp;ja liczę go jako normalny tekst, tu sztucznie zawyżam długość wiadomości. Perfekcyjny analizator by **zbierał i&nbsp;odsiewał linki z&nbsp;tekstu wiadomości**.

Poza tym to, co w&nbsp;JSON-ie widnieje jako tekst wiadomości, bywa jedynie komunikatem.  
*„Dodałeś(aś) do konwersacji X”*. *„Y opuścił(-a) grupę”*.

Takie wiadomości szczególnie by nam nie psuły statystyk, bo są względnie rzadkie na tle całej naszej skrzynki. Mimo to postanowiłem je  odfiltrować. Jeśli wiadomość ma atrybut `users`, to oznacza że jest interakcją. Wtedy jej tekst ustawiam jako inny atrybut. Żeby się wyświetlał w&nbsp;trybie interaktywnym, ale nie psuł statystyk.

**Żeby wyniki były odporniejsze na wahania, liczę dodatkowo medianę**. Pojedyncze wahania w&nbsp;długości tekstu nie są w&nbsp;stanie jej oszukać, ponieważ patrzy tylko na wartości środkowe. Jeśli ktoś parę razy wrzucił wpis liczący tysiące znaków, to nic nie szkodzi.

Oprócz samych znaków patrzę również na słowa. Proces rozbijania zdania na części składowe, czyli *tokeny*, to tzw. *tokenizacja* i&nbsp;w żadnym razie nie jest prostą sprawą, jeśli chcemy mieć dokładność bliską 100%. Przykład:

* Na pewno chcemy rozbić zdania na spacjach, bo te rozdzielają słowa;
* ...Ale gdyby dzielić tylko na spacjach, to zostałyby nam tokeny takie jak `sklep.` ze zdania `jest tam taki sklep.` zakończonego kropką.
* Więc może na spacjach ORAZ kropkach, przecinkach, średnikach itp.?
* W&nbsp;tym przypadku zadziała, ale skróty takie jak *m.in.* rozbije na `m` oraz `in`. Trzeba by mieć listę wyjątków, których nie dzielimy.

Dlatego dokładna tokenizacja wymaga dużo, bardzo dużo pracy. Albo pobrania cięższych modułów.  
Ja poszedłem na łatwiznę i&nbsp;po prostu rozbijam na spacjach i&nbsp;popularnych znakach interpunkcyjnych. A&nbsp;potem biorę tylko te tokeny, które składają się wyłącznie z&nbsp;liter. Na koniec sprowadzam wszystko do małych liter.

```python
import re
TOKENIZER_RE = re.compile('[.,;:()!?/*" ]+')
TOKENIZE = lambda text: TOKENIZER_RE.split( text )

# Później
all_words = [ TOKENIZE(text) for text in msgs_with_text]
all_words = [w.lower() for words in all_words for w in words if w.isalpha()]
```

Gubię w&nbsp;ten sposób liczby i&nbsp;nazwy własne (np. *Dąb* jako nazwisko i&nbsp;*dąb* jako drzewo skończą jako to samo słowo).  
Ale wydaje mi się, że częściej jednak zyskuję, traktując je jako tę samą rzecz.

{% include info.html type="Ciekawostka" text="Mimo wszelkich trudności i&nbsp;tak mamy łatwiej niż Azjaci.  
W przypadku języków chińskiego i&nbsp;japońskiego (może innych też?) nie ma przerw między znakami. Rozbijanie zdań na słowa wymaga czasem sprawdzenia wszystkich możliwych kombinacji, szeregowania ich według prawdopodobieństw itp.  
Więcej o&nbsp;wyzwaniach związanych z&nbsp;chińskim jest na przykład [tutaj](https://manticoresearch.com/2019/07/17/new-way-of-tokenization-of-chinese/)." %}

# Załączniki

To różne rzeczy specjalne dodawane do wiadomości. Mogą to być zdjęcia i&nbsp;inne grafiki, GIF-y, filmy, dowolne pliki, linki przekształcone na format Facebooka...

Zasadniczo nic trudnego. W&nbsp;ich przypadku po prostu przeglądałem interaktywnie dane, aż zobaczyłem, jakim rzeczom odpowiadają różne dodatkowe atrybuty. Na przykład wiadomość z&nbsp;atrybutem `sticker` zawiera naklejkę (obrazek dodany z&nbsp;dostępnych kolekcji Facebooka), `gif` to plik GIF itp.

Na razie po prostu wypisuję, ile rodzajów poszczególnych elementów ktoś wysłał. Ale mogę też kiedyś to rozwinąć i&nbsp;np. wyciągać z&nbsp;archiwum odpowiednie naklejki i&nbsp;dodawać do pliku HTML, żeby powstała lista najczęściej używanych.

Miałem tu również próbkę tego, że Messenger potrafi zmieniać swój format. Poprzednio pracowałem na danych pobranych kilka miesięcy temu. Od tego czasu Facebook wprowadził atrybut `is_unsent`, którego wcześniej nie było.

Efekt? Odpaliłem skrypt i&nbsp;wyszło mi, że najczęściej dodawana rzecz to "atrybut nieznany". W&nbsp;liczbie równej liczbie wszystkich wiadomości. To mnie nauczyło, żeby **nie wierzyć w&nbsp;niezmienność facebookowych formatów**.

# Indeksowanie

Problemy mniej więcej rozwiązane, działa! :smile:

Ale wszystko jest fajnie, dopóki ładuję tylko konwersacje, w&nbsp;których brałem udział (czyli *de facto* wszystko).  
A co, jeśli chcę sprawdzić wiadomości dla innej osoby?

Wtedy jest sporo marnotrawstwa. Program ładuje i&nbsp;sprawdza wszystkie 700+ konwersacji, nawet jeśli wybrana osoba jest tylko w&nbsp;kilku.

Żeby trochę to poprawić, dodałem tzw. *indeks*. Przy pierwszym uruchomieniu program odwiedza każdą konwersację i&nbsp;tworzy listę osób, jakie brały w&nbsp;niej udział.

Potem zapisuje sobie w&nbsp;jednym miejscu (u mnie: do pliku *index.json*), w&nbsp;jakich plikach znajdzie wiadomości poszczególnych osób.

Teraz poszukiwania "rzadszych" osób są dużo szybsze! Wpisuję na przykład, że chcę wszystko od Adama Kowalskiego:

```python
# Na końcu skryptu
name = "Adam Kowalski"
```

Komputer zagląda do indeksu, bierze listę plików, w&nbsp;których ta osoba coś pisała. Wczytuje dane jedynie z&nbsp;nich.

Porównajmy, ile czasu zajmują poszczególne przypadki:

<table>
<tr><td>Stworzenie od zera indeksu dla 782 osób<br/>+ wczytanie 705 konwersacji ze mną:</td><td>5,73&nbsp;s</td></tr>
<tr><td>Wczytanie z&nbsp;indeksu moich konwersacji (705):</td><td>4,5&nbsp;s</td></tr>
<tr><td>Wczytanie z&nbsp;indeksu konwersacji innej osoby (79):</td><td>0,78&nbsp;s</td></tr>
</table>

Wszystko to na dość wątłym laptopie (Windows 10, 64-bitowy, Intel Core i5-3210M 2,5 GHz, 4 GB RAM).

Jak widać, mój bida-indeks trochę przyspieszył sprawy. Czasy i&nbsp;tak nie były jakieś drastyczne, nawet w&nbsp;najgorszym przypadku, ale zawsze to kilka zyskanych sekund życia. Jeśli chcemy analizować wielu znajomych, to oszczędność czasu będzie całkiem spora :wink:

## Skrypt

A tutaj efekt moich prac, skrypt w&nbsp;Pythonie. Dzięki niemu możecie sprawdzić też swoje wiadomości. Albo te wiadomości od innych osób, które trafiły do Waszych wspólnych konwersacji.

{% include pyscript.html name="messenger_stats.py" link="/assets/posts/messenger-analiza/messenger_stats.py" info="
<p>Ten skrypt pozwala analizować wiadomości z&nbsp;Messengera. Wystarczy:</p>
<ul>
  <li>Zainstalować Pythona (instrukcje w&nbsp;samouczku wyżej).</li>
  <li>Pobrać ten skrypt.</li>
  <li>
    <p>Pobrać swoje dane z&nbsp;Facebooka</p>
    <p>Metodę opisałem w&nbsp;pierwszym wpisie z&nbsp;serii. <strong>Koniecznie wybieramy format JSON</strong>. Następnie umieszczamy skrypt w&nbsp;tym samym folderze co zipa z&nbsp;danymi. Nie trzeba go rozpakowywać.</p>
  </li>
  <li>Odpalamy skrypt (instrukcje również w&nbsp;samouczku)</li>
</ul>
<p>I gotowe! Skrypt przejrzy konwersacje i&nbsp;domyślnie wybierze osobę, która brała udział w&nbsp;największej liczbie (czyli zapewne Ciebie). W&nbsp;folderze powstaną trzy pliki:</p>
<p><img src='/assets/posts/messenger-analiza/przed-po.webp' alt='Dwa małe zrzuty ekranu z&nbsp;menedżera plików, połączone strzałką, żeby pokazać stan przed i&nbsp;po użyciu skryptu. U&nbsp;góry widać tylko plik zip z&nbsp;danymi z&nbsp;Messengera i&nbsp;skrypt Pythona. Dolny obrazek pokazuje ponadto trzy pliki: indeks, plik tekstowy z&nbsp;wiadomościami z&nbsp;Messengera oraz raport w&nbsp;formacie HTML.'></p>
<ul>
  <li>Indeks w&nbsp;formacie JSON jest tu dla przyspieszenia wyszukiwań, nie musi nas interesować.</li>
  <li>
    <p>Plik tekstowy zawiera wszystkie wiadomości jednej osoby, ułożone w&nbsp;kolejności chronologicznej.</p>

    <p>Można ten plik otworzyć w&nbsp;zwykłym notatniku i&nbsp;np. wyszukiwać w&nbsp;nim konkretnych słów, żeby zobaczyć, jak często ich używamy.</p>
  </li>
  <li>
    <p>I najważniejsze – podsumowanie statystyk w&nbsp;formacie HTML. Kiedy klikniemy ten plik, powinien się otworzyć w&nbsp;przeglądarce.</p>

    <p>Dla uspokojenia: plik nie łączy się z&nbsp;internetem i&nbsp;<strong>nigdzie nie wysyła Twoich informacji</strong>. Użyłem formatu HTML, bo był najmniej kłopotliwy, jeśli chodzi o&nbsp;dodanie obrazków i&nbsp;wyświetlanie emoji.</p>
  </li>
</ul>
"%}

A co, gdybyśmy chcieli **przeanalizować wiadomości od innej osoby, a&nbsp;nie od siebie**? W&nbsp;takim wypadku otwieramy plik ze skryptem i&nbsp;zjeżdżamy na sam dół.

Tam możemy zmienić `name=""` na nazwę użytkownika, jaką tylko chcemy. Na przykład `name="Justin Case"` (pamiętamy o&nbsp;cudzysłowach!).  
Skrypt poszuka wiadomości dla tego użytkownika i, jeśli coś znajdzie, również stworzy raport i&nbsp;listę chronologiczną.

{% include info.html type="Uwaga" text="Oprócz imienia najlepiej nic nie zmieniać w&nbsp;pliku, ani jednej spacji. Dla Pythona wcięcia mają duże znaczenie. Jeśli tekst nie będzie równo ułożony, może się wyświetlić `SyntaxError`. W&nbsp;takim wypadku, jeśli nie wiecie jak to naprawić, pobierzcie skrypt od nowa :wink:" %}

# Bonus: własne analizy

Moje analizy to tylko mały przykład tego, co da się zrobić! Jeśli chcemy -- i&nbsp;znamy jakieś podstawy Pythona -- możemy sami znaleźć ciekawostki w&nbsp;wiadomościach.

Można to zrobić nawet od razu po odpaleniu skryptu w&nbsp;IDLE. W&nbsp;pamięci pozostanie zmienna `messages`, czyli lista z&nbsp;wiadomościami. Możemy przy niej grzebać, na przykład sprawdzając jeszcze raz liczbę wiadomości...

{:.figure .bigspace}
<img src="/assets/posts/messenger-analiza/msg-len.webp" alt="Zrzut ekranu z&nbsp;interaktywnej konsoli IDLE"/>

Albo wiadomości zawierające reakcje...

{:.figure .bigspace}
<img src="/assets/posts/messenger-analiza/msg-reactions.webp" alt="Zrzut ekranu z&nbsp;interaktywnej konsoli IDLE"/>

Albo w&nbsp;ilu wiadomościach pojawia się słowo „piwo”...

{:.figure .bigspace}
<img src="/assets/posts/messenger-analiza/msg-piwo.webp" alt="Zrzut ekranu z&nbsp;interaktywnej konsoli IDLE"/>

Dokładniej o&nbsp;tym ostatnim przypadku:

* zawsze dajemy `[m for m in messages]`, żeby przeczesywać listę wiadomości;
* do tego na końcu możemy dodawać `if <WARUNEK>`, żeby zbierać tylko część wiadomości
* każda z&nbsp;wiadomości ma tekst, do którego „sięgamy”, wpisując `m.text`. Dlatego możemy dać `if "piwo" in m.text`, żeby sprawdzić czy taki ciąg znaków jest w&nbsp;tekście;
* ale uwaga! W&nbsp;ten sposób by znajdowało też wiadomości z&nbsp;innymi słowami, takie jak „piwonia” albo „spiwor” (*śpiwór* z&nbsp;literówką).  
  Dlatego rozbijam tekst funkcyjką pomocniczą `tok`, która go dzieli na słowa.

Możemy też wyświetlać treść wiadomości, zadbałem o&nbsp;ich czytelne formatowanie. Aby je wyświetlić jedną pod drugą, możemy wpisać:

```python
for m in piwo: print(m)
```

Tryb interaktywny ma jednak wady. Po pierwsze, po zamknięciu IDLE wyniki analiz znikną, o&nbsp;ile wcześniej nie zapiszemy ich do pliku.

Po drugie: zarówno IDLE, jak i&nbsp;PowerShell niezbyt dobrze radzą sobie z&nbsp;emoji. Ten pierwszy do niedawna wywalał błąd, ten drugi wyświetla kwadraty zamiast emot.

Co do błędów wyświetlania -- najlepiej po prostu używać innego programu, wspierającego emoji. Na moim Linuksie (Mint) działa domyślny terminal. Na MacOS podobno też. W&nbsp;przypadku Windowsa można pobrać [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701).

## Co dalej?

Jestem teraz w&nbsp;stanie wyciągać różne rzeczy z&nbsp;wiadomości z&nbsp;Messengera. Widzę dwa możliwe kierunki.

1. Trzymać się Messengera i&nbsp;pójść jeszcze bardziej w&nbsp;analizę tekstu.

   Można spojrzeć na całe konwersacje -- w&nbsp;ten sposób zobaczymy, ile ktoś zwykle wysyła wiadomości pod rząd, jak szybko pisze itp.  
   Poza tym analiza tekstu dopiero się zaczyna. Można otagować słowa jako rzeczowniki, skupić się na tych rzadziej występujących, na nazwach własnych, znajdować ludziom błędy ortograficzne sprzed lat (:smiling_imp:)...

2. Rozbudować oś czasu z&nbsp;poprzedniego wpisu.

   Skoro jestem w&nbsp;stanie odczytywać już wszystkie daty z&nbsp;facebookowych plików, to mogę rozwinąć poprzedni wpis i&nbsp;stworzyć wielką oś czasu. Wiadomości plus inne interakcje.  
   Będzie widać jak na dłoni, jeśli np. o&nbsp;czymś napisaliśmy, potem tego szukaliśmy na FB oraz innych stronach (na których FB też założył swoje „podsłuchy”), a&nbsp;potem napisaliśmy jeszcze innej osobie.

Obie rzeczy wydają się kuszące, którą by tu się zająć? Oczywiście:

{:.figure .bigspace}
<img src="/assets/posts/messenger-analiza/why-not-both.webp" alt="Mem z&nbsp;uśmiechniętą przebiegle dziewczynką podpisany 'Why not both'."/>

Tak jest, oba tematy mnie ciekawią i&nbsp;oba chcę zbadać! :smile: Ale nie zdradzę Wam jeszcze, co będzie następne. Bo sam jeszcze nie wiem.

A póki co -- do zobaczenia i&nbsp;wypatrujcie kolejnych wpisów!

