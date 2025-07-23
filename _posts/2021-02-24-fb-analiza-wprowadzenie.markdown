---
layout: post
title:  "Bobby kontra JSON – dane od Facebooka"
description: "Dzięki danym pobranym z Facebooka stworzyłem swoją oś czasu z różnych interakcji na tym portalu."
date:   2021-02-24 19:32:00 +0100
tags: [Analiza danych, Porady]
firmy: [Facebook]
category: facebook_dane
category_readable: "Kochajmy się jak bracia, analizujmy się jak Facebooki"
---

W <a href="/facebook_dane/2021/02/11/nasze-dane-facebooka">poprzednim wpisie</a> opisałem, jak pobrać swoje dane z&nbsp;Facebooka. Kiedy już znajdą się u&nbsp;mnie na dysku, mogę je w&nbsp;fajny sposób analizować.

Na gwoźdź programu, czyli wiadomości z&nbsp;Messengera, jeszcze chwilę poczekamy. Cierpliwości! :wink:

Póki co oswoimy się z&nbsp;JSON-em (formatem danych), rozwiążemy podstawowe problemy i&nbsp;połączymy informacje z&nbsp;różnych plików od Fejsa we własną oś czasu, pokazującą między innymi, czego szukaliśmy i&nbsp;jakie profile odwiedzaliśmy.

{% include info.html type="Dla niecierpliwych" text="Wpis zawiera trochę fragmentów kodu. Jeśli Was nie interesują, swobodnie można je przeskakiwać. Nie są potrzebne do zrozumienia całości.  
Jeśli wolicie całkiem ominąć sprawy techniczne, to możecie zacząć <a href='#ciekawostki-z-moich-danych'>od wniosków z&nbsp;analizy</a>.  
Jeśli natomiast chcecie sam skrypt do tworzenia własnej „osi czasu”, to znajdziecie go <a href='#twoja-oś-czasu'>na końcu strony</a>.  
**Uwaga:** Skrypt jest dopasowany tylko do danych z&nbsp;kategorii „Informacje o&nbsp;Tobie”. Nie jest w&nbsp;stanie obrobić innych, w&nbsp;tym w&nbsp;szczególności wiadomości z&nbsp;Messengera." %}

## Reklamy na Facebooku -- wprowadzenie

Na początek krótka motywacja dla całej tej analizy.

Facebook na swojej stronie (czyli *www.facebook.com*; w&nbsp;aplikacji może to działać inaczej) potrafi umieszczać reklamy w&nbsp;różnych miejscach. Czasem na stałe w&nbsp;górnym rogu, czasem wymieszane z&nbsp;normalnymi wpisami na tablicy. 

Przykładowa reklama -- tu dziwnie uboga -- wygląda tak:

{:.figure .bigspace}
<img src="/assets/posts/fb-analiza-wprowadzenie/google-reklama-fb.webp" alt="Reklama na Facebooku sponsorowana przez Google, zawierająca tekst 'Darmowe kursy online zaprojektowane z&nbsp;myślą o&nbsp;rzowoju kariery. Wybierz lekcję lub zacznij cały kurs'. Wpis nie zawiera żadnych linków. Jeden z&nbsp;użytkowników w&nbsp;komentarzu pyta 'I gdzie ten kurs?'."/>

W jej prawym górnym rogu znajduje się ikona trzech kropek (1). Po kliknięciu w&nbsp;nią wyświetli się lista opcji. Wybieramy ostatnią, `Dlaczego widzę tę reklamę?` (2).

{:.figure .bigspace}
<img src="/assets/posts/fb-analiza-wprowadzenie/reklama-info.webp" alt="Rozwinięte okienko z&nbsp;opcjami. W&nbsp;prawym górnym rogu ikona trzech kropek oznaczona jako 1. Wśród opcji cyfrą 2 oznaczona przedostatnia, o&nbsp;treści 'Dlaczego widzę tę reklamę?'."/>

Wyświetlą się informacje o&nbsp;tym, na jakiej podstawie trafiła nam się akurat taka reklama. W&nbsp;moim przypadku zadecydował wiek, lokalizacja, język i&nbsp;zainteresowania:

{:.figure .bigspace}
<img src="/assets/posts/fb-analiza-wprowadzenie/google-reklama-dlaczego.webp" alt="Okno o&nbsp;nagłówku 'Dlaczego widzisz tę reklamę'. Wymienione cztery powody: wśród moich zainteresowań według Facebooka jest Hacker News, znam język polski, jestem osobą w&nbsp;wieku od 18 do 60 lat, moja podstawowa lokalizacja to Polska."/>

W tym przypadku moje zainteresowania odnoszą się po prostu do polubionej stronki (uprzedzając pytania -- to forum stronki ogólnoinformatycznej. *Hacker* w&nbsp;znaczeniu zbliżonym do majsterkowicza, nie włamywacza).

Ale nieraz te moje rzekome zainteresowania potrafią mnie zdziwić. Dlaczego akurat takie?

To właśnie motywacja, jaka mi przyświecała. Spojrzeć na te same dane, na jakie patrzyły algorytmy Fejsa i&nbsp;spróbować zrozumieć, dlaczego przypisano mi określone rzeczy. Ale to cel na dłuższą metę.

Ten wpis opisuje pierwszy krok w&nbsp;tę stronę. Patrzę na względnie suche dane dotyczące wyświetleń i&nbsp;wyszukań. Pokazuję, że w&nbsp;połączeniu z&nbsp;datami nawet one potrafią opowiedzieć pewną historię.

## Przygotowanie danych

Na początku pobrałem dane, zgodnie z&nbsp;<a href="/facebook_dane/2021/02/11/nasze-dane-facebooka.html#jak-pobrać-swoje-dane-od-fejsika">metodą z&nbsp;poprzedniego wpisu</a>. Do tej analizy wziąłem z&nbsp;Facebooka **tylko dział „Informacje o&nbsp;Tobie”, z&nbsp;samego dołu listy plików do pobrania**:

{:.figure .bigspace}
<img src="/assets/posts/fb-analiza-wprowadzenie/fb-informacje-o-tobie.webp" alt="Lista danych do pobrania z&nbsp;Facebooka, zebranych pod nagłówkiem 'Informacje o&nbsp;Tobie'. Wśród nich: reklamy i&nbsp;firmy, historia wyszukiwania, lokalizacja, informacje o&nbsp;Tobie, informacje dotyczące logowania, twoje tematy, nagranie głosowe i&nbsp;transkrypcja."/>


Format JSON, zakres dat od początku do końca, jakość mediów niska (tu bez znaczenia, bo to sam tekst).

Pliki pobrałem dnia 24.02. Zawierające je archiwum jest bardzo małe i&nbsp;lekkie. Mój plik *zip* „waży” łącznie około 150 kB, w&nbsp;porównaniu z&nbsp;ponad 2 GB wszystkich danych. 

Pobranego *zipa* ułożyłem w&nbsp;osobnym folderze i&nbsp;rozpakowałem. Tak są w&nbsp;nim rozmieszczone pliki:

{:.figure}
<img src="/assets/posts/fb-analiza-wprowadzenie/folder-fb-zawartosc.webp" alt="lista 28 plików i&nbsp;7 folderów zawartych w&nbsp;pobranym pliku zip. Pokazana na czarnym tle, w&nbsp;formie prostego drzewka z&nbsp;kresek."/>

{:.figcaption}
Wizualizacja układu plików wykonana programem `tree` na Linuksie.

28 plików rozbitych na 7 folderów. Głównie JSON-y. Do tego w&nbsp;folderze na transkrypcje jeden plik tekstowy z&nbsp;informacją o&nbsp;braku danych. Bo z&nbsp;żadnych transkrypcji nie korzystałem.

Po pierwszym kontakcie zacząłem grzebać w&nbsp;plikach i&nbsp;wypatrywać powtarzających się rzeczy.

O JSON-ie ogólnie nie musicie nic wiedzieć, poza tym że jest dość czytelny i&nbsp;przyjazny. Wnętrze przykładowego pliku *.json* wygląda tak:

{:.figure .bigspace}
<img src="/assets/posts/fb-analiza-wprowadzenie/facebook-json-przyklad.webp" alt="Fragment pliku 'visited.json' otwarty w&nbsp;notatniku. Widać hierarchię elementów. Dorysowany prostokąt o&nbsp;bordowych brzegach otacza tekst, w&nbsp;którym zamiast polskich znaków są ciągi ukośników, cyfr i&nbsp;liter. Prostokąt o&nbsp;pomarańczowych brzegach otacza liczbę obok nazwy 'timestamp'."/>

Pomarańczowym kolorem otoczyłem liczbę zwaną *znacznikiem czasu* (dosł. *stemplem z czasem*), kluczową dla naszej analizy. Bordowym przykład tekstu, który niestety nie uznaje polskich liter. Te i&nbsp;inne kwestie muszę rozwiązać, zanim będę w&nbsp;stanie wyciągnąć z&nbsp;danych coś sensownego.

# Znacznik czasu

Te liczby przy atrybucie `timestamp`, jak nazwa wskazuje, pewnie mówią nam coś o&nbsp;czasie. Są dla nas bardzo ważne. Ale w&nbsp;jaki sposób przekształcić je na daty?

Po wpisywaniu w wyszukiwarkę haseł w&nbsp;stylu „*python timestamp to date*” wypatrzyłem rozwiązanie. Wystarczy załadować moduł od dat i&nbsp;stworzyć krótką funkcyjkę:

```python
from datetime import datetime
def _convert_timestamp( timestamp ):
    return datetime.fromtimestamp( timestamp )
```

{% include info.html type="Ciekawostka" text="Co by się stało, gdybyśmy jako znacznik czasu przyjęli *0* i&nbsp;odpalili naszą funkcję? Zobaczymy wtedy, **co jest dla komputerów początkiem czasu**, takim *punktem zero* dla dat!  
Okazuje się, że nasze `_convert_timestamp(0)` dałoby datę... **1.01.1970 r.**! To nasza *data zerowa*.  
Dlaczego taka? [Z prozaicznych powodów](https://unix.stackexchange.com/questions/26205/why-does-unix-time-start-at-1970-01-01) -- ponoć to we wczesnych latach 70. określano standardy dla komputerów. Dla autorów wygodna była data: *a)* jak najokrąglejsza i&nbsp;*b)* nie sięgająca zbyt daleko w&nbsp;przeszłość.  
Jeśli czasem zdarzyło Wam się spotkać absurdalne daty i&nbsp;gdzieś było w&nbsp;nich 1970, to już wiecie, skąd się to wzięło.   
Zresztą, żeby daleko nie szukać, sam się z&nbsp;tym niedawno zetknąłem podczas jakiejś czkawki Messengera:" trailer="<p class='figure'><img src='/assets/posts/fb-analiza-wprowadzenie/cofamy-czas.webp' alt='Fragment okna Messengera, pokazujący napis seen by ocenzurowano at 1 January 1970 at 01:00'/></p>" %}

# Kodowanie znaków

Mamy daty, czas uzyskać tekst.

Zwykle, kiedy otwierałem w&nbsp;Pythonie pliki JSON, nie było żadnych problemów z&nbsp;kodowaniem. Po prostu działało, miałem polskie litery i&nbsp;inne znaki. Dlaczego tutaj jest inaczej?

Jak się okazało, Facebook włożył dużo mniej serca w&nbsp;oddawanie danych użytkownikom niż w&nbsp;obrabianie ich pod kątem reklam. Takie kodowanie to [ponoć ewidentny błąd](https://stackoverflow.com/questions/50008296/facebook-json-badly-encoded) z&nbsp;ich strony:

>I can indeed confirm that the Facebook download data is incorrectly encoded (...). The original data is UTF-8 encoded but was decoded as Latin -1 instead. I’ll make sure to file a&nbsp;bug report. 

Proponowane rozwiązanie jest na szczęście krótkie i&nbsp;treściwe:

```python
def _fix_fb_text_encoding(text):
    return text.encode('latin_1').decode('utf-8')
```

# Wyświetlanie znaków emoji

Oprócz polskich znaków na FB mamy też pełno różnych emotek. Wyglądają ładnie, ale za kulisami są utrapieniem (tym razem nie z&nbsp;winy Fejsa).

Zacznijmy od tego, że są „większe”. Jeśli je zapisać w&nbsp;formie bajtów:

* Polska litera *ą* to `\xc4\x85`.
* Emotka puszczająca oko (:wink:) to `\xf0\x9f\x98\x89`.

Ten dziwny zapis może nam nic nie mówić, ale widać co dłuższe.

A to jeszcze nic! Np. [piracka flaga](https://emojipedia.org/pirate-flag/) to dwie osobne emoty -- czarna flaga i&nbsp;czaszka -- postawione obok siebie. A&nbsp;także dwa znaki pomocnicze, które nie są wyświetlane.

Z tych i&nbsp;może innych powodów **niektóre programy nie radzą sobie z&nbsp;emotami**. Na przykład najprostszy terminal Windowsa.  
Mój IDLE w&nbsp;wersji 3.6.9, domyślny edytor Pythona, również nie daje rady i&nbsp;przy próbie wyświetlenia emoty wyrzuca błąd `UnicodeEncodeError` (choć podobno w&nbsp;nowych wersjach to poprawili).

Emoty na Facebooku lubią być wszędzie, w&nbsp;każdej nazwie. A&nbsp;ja mogę sobie prosić, ale nigdy nie wiem, w&nbsp;czym ktoś odpali mój skrypt. Dlatego postanowiłem to prowizorycznie załatać:

```python
try:
    print( emoji_text )
except UnicodeEncodeError:
    print(bytes( emoji_text, 'utf-8'))
```

Gdyby program miał się rozkraczyć podczas wyświetlania tekstu, to zamieni emoji na zapis „bajtowy”, ten z&nbsp;iksami i&nbsp;ukośnikami. Może i&nbsp;nieczytelne, ale nie wymaga pobierania żadnych dodatków. A&nbsp;kontekst widać.

# Nieregularność w&nbsp;danych

Bez wchodzenia w&nbsp;szczegóły: dane w&nbsp;formacie JSON są pogrupowane w&nbsp;słowniki (oznaczone nawiasami wąsatymi, `{}`) i&nbsp;listy (nawiasy kwadratowe, `[]`). Jedne elementy mogą być zawarte w&nbsp;drugich -- w&nbsp;liście słownik, w&nbsp;tym słowniku kolejne listy itd.

Żeby wyciągnąć z&nbsp;tego dane, trzeba robić to co w&nbsp;„Incepcji” -- zagłębiać się poziom po poziomie w&nbsp;kolejne warstwy, aż znajdziemy szukany element.

W moim przypadku tym elementem było słowo *timestamp*. Gdyby wszystkie pliki miały podobną budowę, to mógłbym się po prostu zatrzymać po dotarciu do niego i&nbsp;zgarnąć wszystko wokół. Niestety tak nie jest:

* W&nbsp;niektórych plikach dane są podzielone na podgrupy (np. osobno odwiedziny na profilach, osobno na wydarzeniach);
* W&nbsp;pliku *your_search_history.json* na tym poziomie co znacznik czasu jest element *data*, w&nbsp;nim jeszcze parę zagnieżdżonych rzeczy. Te wartościowe najgłębiej.  
  Do tego jest tam element *attachments*, który w&nbsp;ogóle wydaje się niepotrzebny, bo zawiera to samo co *data*.
* W&nbsp;pliku *your_off-facebook_activity* mamy na odwrót -- nazwę strony na wyższym poziomie, a&nbsp;zdarzenia (wraz z&nbsp;ich znacznikami czasu) niżej. Czekając na znacznik, przegapilibyśmy istotne informacje.

Na pewno dałoby się stworzyć jakiś elastyczny program -- zapamiętujący informacje z&nbsp;wyższych poziomów podczas schodzenia w&nbsp;głąb albo nawet odgadujący ich rodzaj.

Ale to zrobię później. Jestem leniwym człowiekiem, więc po prostu nie dzielę na podkategorie, traktując każdy plik jak jedną odrębną. Dodałem też osobne funkcje do obróbki tych dwóch plików, które wyłamują się ze schematu. 

## Ciekawostki z moich danych

Po rozwiązaniu problemów mogłem sobie sprawniej przeglądać dane -- czasem skryptem, czasem po prostu otwierając JSON-y.

W ten sposób dowiedziałem się kilku rzeczy, które może nie znajdą miejsca na osi czasu, ale nadają się na ciekawostki:

* Pliki z&nbsp;podfolderu *security_and_login_information* dotyczą głównie spraw technicznych.

  Są tam adresy IP, pliki cookies, informacje o&nbsp;naszych urządzeniach... Bardziej pasują do „Internetowej inwigilacji” niż do tej serii, więc póki co je pominę.

* Przy danych o&nbsp;odwiedzonych profilach Facebook **pokazuje tylko jedne, najnowsze odwiedziny**.

  Upadł zatem mój pomysł na liczenie, ile razy obejrzało się czyjś profil lub stronę. Nie pośmieszkujemy z&nbsp;obsesyjnego przeglądania :frowning_face:  
  ...Ale! Informacje o&nbsp;jednorazowych wizytach również da się wykorzystać, piszę o&nbsp;tym niżej.

* Informacje o&nbsp;powiadomieniach i&nbsp;rzeczach wyświetlonych na tablicy (*notification.json* i&nbsp;*viewed.json*) **są trzymane przez FB tylko przez 90 dni**.

  Powiadomienia moim zdaniem to głównie spam, więc niewielka strata.  
  A&nbsp;wyświetlonych rzeczy szkoda. Dzięki nim moglibyśmy lepiej rozumieć działanie Facebooka. Dlatego od teraz planuję „zamykanie kwartału” i&nbsp;archiwizowanie co 3 miesiące swoich danych.

* Z&nbsp;zaskoczeń: Facebook zbiera historię ustawień językowych (plik *preferences.json*).

  Czyli jeśli na jakiś czas zmieniliśmy język na hiszpański, potem na angielski, potem na polski, to będzie to odnotowane na zawsze w&nbsp;kartotece, razem z&nbsp;datami.

* Informacje o&nbsp;zainteresowaniach z&nbsp;*ads_interests.json* to cała kopalnia zaskoczeń. **Niektóre dalekie od prawdy**, a&nbsp;niektóre to zupełny zonk.

  Dowiedziałem się na przykład, że interesują mnie tematy: *Coaching*, *Dizziness*, *Most*, *Dominika*, *Ramię*, *Staw (akwen)*, *Zatoka (geografia)* :roll_eyes:  
  Reklam mostów jeszcze na profilu nie widziałem. Szkoda, kupowałbym.

* Jest też JSON z&nbsp;listą reklamodawców, którzy załadowali plik z&nbsp;informacjami o&nbsp;mnie.

  **Dziwnie tam dużo zestawów samochód + miasto**: *Acura of Rochester*, *Audi Columbia*, *Chrysler Dodge Jeep Ram of Calallen* (to ostatnie kojarzy mi się z&nbsp;jakimś brytyjskim szlachcicem) i wiele innych.

* ...Z drugiej strony przypisane mi szersze tematy (*your_topics.json*) były zadziwiająco trafne.

  Może wrzucają tam tylko pewniejsze, powtarzające się rzeczy.

* Informacje o&nbsp;aktywności poza Facebookiem (*your_off-facebook_activity.json*) mówią z&nbsp;kolei o&nbsp;tym, **kto przekazał Facebookowi dane o&nbsp;tym, że byliśmy na ich stronach**.

  Nie robią tego wprost, mailem czy faksem, tylko przez dodanie do swoich stronek elementów „społecznościowych” od FB.  
  U&nbsp;mnie takich interakcji jest tylko 25 (Firefox + dodatki uBlock Origin i Privacy Badger chyba robią swoje :sunglasses:). Ale **niektóre osoby mają ich kilkaset**.

* Najbardziej tajemniczy element to dla mnie książki adresowe (*address_books.json*).
  
  Jest tam kilkanaście osób. Niektórych mam w&nbsp;znajomych (nawet bliższych), z&nbsp;niektórymi wymieniłem tylko pojedyncze wiadomości. Prawie do nikogo nie mam numeru telefonu, więc pierwsze skojarzenie odpada. Sprawa do zbadania.

Zajrzyjcie w&nbsp;swoje pliki, też na pewno znajdziecie coś ciekawego :wink: To tak osobiste sprawy, że trudno mi uogólniać.

## Moja oś czasu

Czas na gwóźdź programu. Po rozwiązaniu problemów z&nbsp;danymi trochę wszystko uogólniłem, uprościłem i&nbsp;zebrałem w&nbsp;jeden skrypt Pythona.

Oprócz tego zdecydowałem się nie uwzględniać danych z trzech plików, mimo że też zawierały znaczniki czasu:

* *notifications.json* -- bo nie widziałem w powiadomieniach cennych informacji;
* *used_ip_addresses.json* -- bo powtarzają się z innymi informacjami;
* *viewed.json* -- bo to, że coś nam się wyświetliło na tablicy, nie wynika z naszego bezpośredniego działania.

Zostawiłem w skrypcie opcję łatwego włączenia tych plików do analizy, gdybym zmienił zdanie.

Gotowy skrypt zbiera listę moich działań z&nbsp;pozostałych plików -- o&nbsp;ile tylko zawierały znaczniki czasu -- i&nbsp;układa je w&nbsp;sposób chronologiczny. Powstaje taka **oś czasu, tylko że o&nbsp;mnie, a&nbsp;nie o&nbsp;innych**.

W podobny sposób może nas za kulisami postrzegać Facebook (chociaż oczywiście ma więcej danych; przypominam, że na razie użyłem tylko 150 kB z&nbsp;ponad 2 GB).

Mój skrypt, po odpaleniu w&nbsp;folderze z&nbsp;danymi, tworzy plik tekstowy z&nbsp;prostymi informacjami ułożonymi według dat. **3014 wydarzeń z mojego facebookowego życia**.

Tu fragment mojej tekstowej osi czasu:

{:.figure .bigspace}
<img src="/assets/posts/fb-analiza-wprowadzenie/os-czasu-przyklad.webp" alt="Zrzut ekranu z&nbsp;Notatnika, pokazujący oś czasu. Po lewej stronie znajdują się daty, z&nbsp;dokładnością do sekund. Po prawej stronie, odpowiednio wcięte, odpowiadające tym datom działania. Nagłówki tych działań to „WYSZUKANE” albo „ODWIEDZONA STRONA/PROFIL”. Łącznie widać informacje dla trzech wyszukań, potem odwiedzonej strony, kolejnego wyszukania i&nbsp;innej odwiedzonej strony."/>

Dzięki połączeniu dwóch rodzajów informacji ukazuje się tutaj krótka historia z&nbsp;mojego życia:

1. Nie miałem co robić po północy 9.01 (w noc z&nbsp;piątku na sobotę, jeśli wierzyć kalendarzowi).
2. Szukałem strony, która mi się kojarzyła. Wpisałem w&nbsp;wyszukiwarkę Fejsa fragment jej nazwy.
3. Chyba nic się nie pojawiło, bo wyszukałem ponownie, po dopisaniu jednego słowa.
4. Pewnie zobaczyłem coś w&nbsp;podpowiedziach, bo przeszedłem na inną stronkę o&nbsp;zbliżonej nazwie. Spędziłem na niej ok. 7 minut.
5. Potem pewnie kliknąłem w&nbsp;inną podpowiedź (bo w&nbsp;wyszukiwaniach mam pełną nazwę strony, co do litery).
6. Trafiłem na stronę, której szukałem na początku.

Ogranicza mnie oczywiście to, że widzę tylko najnowsze odwiedziny na stronie. Ale mimo wszystko da się całkiem znośnie wykorzystać te dane.

Inna historia to wizyta w&nbsp;Hiszpanii w&nbsp;2020 r. W&nbsp;pierwszych dniach, kiedy byliśmy na odludziu, zero aktywności. Potem wyszukiwanie i&nbsp;zwiedzanie lokalnych grup polskich. Interakcje z&nbsp;zewnętrznymi stronami biur podróży (których szukaliśmy na szybko).  
**Dane układają się w spójną historię**, jeśli się je umieści w&nbsp;szerszym kontekście.

## Ciemna strona danych

Takie przypominajki z&nbsp;danych dałoby się też wykorzystać w&nbsp;bardziej złowieszczy sposób.

Przyjmijmy, że jest pewien człowiek płci dowolnej. Nazwijmy go Anonek. Pewnego dnia ktoś napisał komentarz, który Anonka strasznie wkurzył. Na przykład szkalujący pizzę hawajską. Anonek z&nbsp;gniewu aż wszedł na profil tej osoby, planując zemstę.

Jednak być może nie udało mu się odegrać. Omyłkowo się wylogował, potem wyczyściło mu historię przeglądarki. Nie pamiętał już imienia osoby, na której chciał się zemścić. A&nbsp;profili przeglądał bardzo wiele, więc nawet gdyby pobrał dane, nie chciałoby mu się grzebać w&nbsp;samym *visited.json* w&nbsp;surowej formie.  
W normalnych warunkach, nie mając punktu zaczepienia, może by odpuścił.

Ale, korzystając z&nbsp;naszej osi czasu, mógłby wyszukać inne zdarzenie, które miało miejsce w&nbsp;tamtym czasie. Może na przykład pamięta, że tamtego dnia szukał przez FB fanklubów hawajskiej?

Otwiera więc plik z&nbsp;osią czasu w&nbsp;Notatniku i&nbsp;wyszukuje „*hawaj*”, żeby znaleźć ten dzień. Patrzy na wydarzenia z&nbsp;tagiem *ODWIEDZONA STRONA/PROFIL* z&nbsp;tego samego dnia.

Znajduje jakiś profil. Nazwa użytkownika jest inna niż zapamiętał. Tamten szkalujący łotr zmienił nazwę konta, żeby przed nim uciec! Gdyby Anonek szukał tradycyjnymi metodami, to by go nie znalazł.

Oprócz nazwy użytkownika jest też pole `uri`. To link do konta na Facebooku. Wiele osób zmienia nazwę swojego konta, ale **identyfikator często pozostawiają taki jak poprzednio**.

Anonek kopiuje link do przeglądarki i&nbsp;wchodzi na profil wroga. Po miesiącach frustracji może się zemścić.

{% include info.html type="Porada" text="Co zrobić, jeśli na FB mignie Wam jakaś dawno niewidziana znajoma, której nazwisko nijak się Wam nie kojarzy (bo np. w&nbsp;międzyczasie wyszła za mąż)? Jak szybko ustalić tożsamość?  
Możecie najechać kursorem na jej imię i&nbsp;spojrzeć w&nbsp;lewy dolny róg przeglądarki. Pojawi się tam link do profilu. Jeśli macie szczęście, to się nie zmienił od założenia konta i&nbsp;nadal zawiera nazwisko panieńskie." %}

## Twoja oś czasu

Na koniec mój skrypt w&nbsp;Pythonie, efekt działań z&nbsp;tego wpisu:

{% include pyscript.html name="fb_data_timeline.py" link="/assets/posts/fb-analiza-wprowadzenie/skrypty/fb_data_timeline.py" info="Instrukcja:
<ul style='margin-top:0px;margin-bottom:0px'>
<li>Najpierw <a href='/facebook_dane/2021/02/11/nasze-dane-facebooka.html'>pobieramy swoje dane z&nbsp;Facebooka</a>.</li>
<li>Uzyskany plik <i>zip</i> dajemy do jakiegoś folderu. Możemy go rozpakować, ale nie musimy.</li>
<li>W tym samym folderze umieszczamy mój skrypt i&nbsp;go odpalamy.</li>
<li>Jeśli wszystko dobrze poszło, powstanie plik tekstowy <i>fb_moja_os_czasu.txt</i>. Można go otworzyć np. w&nbsp;Notatniku. Zawiera listę różnych naszych działań ułożonych chronologicznie.</li></ul>"%}

Oddaję skrypt w&nbsp;Twoje ręce, możesz używać i&nbsp;modyfikować do woli. Teraz Twoja oś czasu jest Twoja.

To tyle na dziś. W&nbsp;kolejnym wpisie mój „konik”, czyli analiza tekstu (wiadomości z&nbsp;Messengera). Będzie się działo! :metal:

