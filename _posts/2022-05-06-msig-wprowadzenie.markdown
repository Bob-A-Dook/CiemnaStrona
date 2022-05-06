---
layout: post
title:  "Monitor Sądowy i Gospodarczy. Pierwsze kroki"
description: "Co nam mówią metadane z Monitorów."
subtitle: "Co nam mówią metadane z Monitorów."
date:   2022-05-06 20:07:00 +0100
tags: [Analiza danych]
firmy: [Adobe]
category: krs-msig
category_readable: "Myszkowanie w Monitorze i kopanie w KRS-ie"
---

Witam w&nbsp;kolejnym wpisie z&nbsp;serii „Myszkowanie w&nbsp;Monitorze i&nbsp;kopanie w&nbsp;KRS-ie” :smile:  
Jeśli jeszcze tej serii nie znacie: patrzę tutaj na publicznie dostępne polskie źródła informacji na temat spółek. Stopniowo rozwijając własne metody ich analizowania i&nbsp;dzieląc się na blogu ciekawostkami.

Dotychczas poświęcałem łamy bloga głównie Krajowemu Rejestrowi Sądowemu. To oficjalna polska baza z&nbsp;informacjami o&nbsp;spółkach (tych większych, od jawnej wzwyż, bo od mniejszych działalności jest CEIDG).

Czas na zmiany. Tym razem spojrzę na drugie ważne źródło informacji -- **Monitor Sądowy i&nbsp;Gospodarczy**. Zobaczymy, w&nbsp;jaki sposób można zbierać Monitory i&nbsp;wstępnie spojrzymy do ich metadanych (ogólnych informacji na temat plików, nie wymagających ich dokładnego przetwarzania).

Spoiler: będzie w&nbsp;nich parę ciekawostek.

{:.post-meta .bigspace-before}
Jak zwykle stosuję język potoczny, spółki nazywam czasem firmami itd. To świadoma decyzja.

## Motywacja

# Dlaczego nie zewnętrzne platformy

W poprzednich wpisach nieraz podkreślałem, że KRS się przydaje, ale pobieraniem pojedynczych odpisów nie zawojujemy świata. Bowiem **nie dałyby nam pełnego obrazu powiązań między firmami**. Nie zobaczymy na przykład, że firma A, którą właśnie oglądamy, kieruje też firmami B&nbsp;i C.

Najszybszym sposobem na uzupełnienie tej luki byłoby skorzystanie z&nbsp;jakiejś strony udostępniającej informacje na temat firm. A&nbsp;jest ich trochę: *rejestr.io*, *infoveriti.pl*, *aleo.com*...

Tylko że korzystanie z&nbsp;komercyjnych platform wiąże się z&nbsp;paroma niedogodnościami:

* Dostęp do danych historycznych zwykle jest płatny.

  Gdybyśmy chcieli zobaczyć, w&nbsp;jakich firmach miała swoje udziały pewna osoba -- ale już nie ma -- to musielibyśmy zapłacić. A&nbsp;wtedy zostałoby nam mniej na ziemniaczki i&nbsp;cebulę w&nbsp;tych ciężkich czasach.

* Trzeba zaufać ich danym.

  Musimy wierzyć im na słowo, że pokazywane dane są spójne i&nbsp;prawdziwe.  
  A&nbsp;przecież błędy się zdarzają; format danych może się nie zgadzać, jedna spółka przez literówkę będzie traktowana jak dwie itd. Pomijając już fakt, że niektórzy mogą się dobijać, żeby ich firmę z&nbsp;bazy usunąć.

* Nie mamy pełnej swobody.

  Korzystając z&nbsp;gotowych platform, możemy jedynie korzystać z&nbsp;narzędzi, jakie nam udostępnili. A&nbsp;co, jeśli mamy pomysł na jakąś nietuzinkową analizę albo wizualizację? Pozostaje negocjowanie dla siebie specjalnych warunków. 

W ten sposób doszedłem do wniosku, że **tylko zdobycie danych u&nbsp;samego źródła da mi pełną wolność**.

# Dlaczego Monitor

„U samego źródła”... Tylko co nim jest? W&nbsp;Polsce informacje o&nbsp;spółkach są rozrzucone po kilku bazach. Główną jest KRS, ale jednak wybrałem Monitor. Dlaczego?

Najpierw krótko przypomnę różnice między dokumentami z&nbsp;KRS-u (odpisami) a&nbsp;egzemplarzami Monitora.

* Jeden odpis z&nbsp;KRS-u pokazuje wszystkie wydarzenia z&nbsp;całego okresu życia jednej konkretnej firmy.  
* Jeden egzemplarz Monitora pokazuje wszystkie wydarzenia z&nbsp;dość krótkiego okresu czasu (do kilku dni) dla wszystkich firm w&nbsp;Polsce .  

Dla wzrokowców mam nieco bidny schemat zrobiony w&nbsp;LibreOffice Calc:

<img src="/assets/posts/msig/krs-msig-roznice.jpg" alt="Dwa identyczne schematy umieszczone jeden pod drugim. W&nbsp;każdym z&nbsp;nich na poziomej osi znajdują się nazwy spółek, od A&nbsp;do D. Na osi pionowej znajdują się daty od 30&nbsp;kwietnia do 2&nbsp;maja. Między osiami widać kilka pól, w&nbsp;które wpisano ponumerowane zdarzenia. Na wykresy naniesiono kolorowe ramki. Ramka nałożona na górny schemat, podpisana KRS, obejmuje nazwę jednej spółki i&nbsp;wszystkie zdarzenia w&nbsp;jej kolumnie. Ramka na dolnym schemacie, podpisana MSiG, obejmuje dwa wiersze i&nbsp;wszystkie zawarte w&nbsp;nich zdarzenia." width="600px"/>

Gdybyśmy chcieli mieć wszystkie zdarzenia dla wszystkich spółek, musielibyśmy zebrać całą tabelkę. Można to zrobić na dwa sposoby:

1. „kolumnami” -- pobrać odpisy KRS dla wszystkich istniejących firm,
2. „wierszami” -- pobrać wszystkie egzemplarze Monitora.

Natomiast, gdybyśmy oprócz tego chcieli być na bieżąco, opcja z&nbsp;KRS-em byłaby niekończącą się walką z&nbsp;wiatrakami. Każdego dnia dzieje się coś nowego. Zatem każdego dnia musielibyśmy pobierać tysiące odpisów. Z&nbsp;których tylko niewielka część zawierałaby coś nowego.

Dlatego Monitory uznałem za lepsze rozwiązanie, jeśli chcę trzymać rękę na pulsie (a chcę). I&nbsp;to na nich skupiłem uwagę.

## Gdzie i&nbsp;jak zdobyć Monitory

Wszystkie Monitory można pobrać ze [strony](https://ems.ms.gov.pl/msig/przegladaniemonitorow) Ministerstwa Finansów. Natomiast nie jest to szczególnie przyjemne.

Kiedy klikniemy na link do wybranego Monitora, pojawia się Captcha -- zdjęcie tekstu, który trzeba przepisać do pola, żeby pobrać plik. Zabezpieczenie przed automatycznym pobieraniem.

{:.figure .bigspace}
<img src="/assets/posts/msig/msig-captcha.jpg" alt="Zrzut ekranu pokazujący okno proszące o&nbsp;przepisanie tekstu z&nbsp;obrazka. W&nbsp;tle widać mocno zaciemnioną treść głównej strony z&nbsp;listą monitorów"/>

I nie byłoby tu problemu, gdyby nie kilka dość irytujących zachowań strony:

1. Pole tekstowe nie skupia się automatycznie; za każdym razem trzeba je kliknąć, zanim zaczniemy wpisywać tekst.
2. Okno nabiera ostrości powoli, przez kilka sekund. Jeśli klikniemy za wcześnie, zanim skończy się ta animacja, to... pobierzemy ponownie poprzedni plik zamiast tego obecnie klikniętego.
3. Nie da się potwierdzić wpisanej Captchy naciśnięciem klawisza; trzeba wziąć myszkę i&nbsp;kliknąć `OK`.

Dodajmy do tego sam fakt, że każdego roku wydawanych jest ponad 200&nbsp;Monitorów. Chcąc zebrać kolekcję z&nbsp;wielu lat, mamy przed sobą strasznie dużo klikaniny. 

Być może osoba kontaktowa mogłaby napisać prośbę o&nbsp;przesłanie wszystkich Monitorów, z&nbsp;pominięciem Captchy? Powołując się na przykład na prawo dostępu do informacji publicznej?  
To jednak wymagałoby kontaktu z&nbsp;ludźmi. Rozwiązanie dość sprzeczne z&nbsp;etosem piwniczaków.

Ktoś skryptowy mógłby z&nbsp;kolei użyć biblioteki `pynput`, napisanej w&nbsp;Pythonie i&nbsp;pozwalającej kontrolować mysz oraz klawiaturę.  
W ten sposób dałoby się rozwiązać problemy 1&nbsp;i 3&nbsp;-- podpiąć ruchy i&nbsp;kliknięcia myszki pod klawiaturę. Osoba pobierająca tylko by przepisywała tekst i&nbsp;naciskała ustalony klawisz, a&nbsp;mysz sama by przeskakiwała i&nbsp;klikała co trzeba.

Jest też rozwiązanie dla przodowników pracy. Cierpliwie klikać nazwę Monitora, pole tekstowe, wpisywać kod, klikać *OK*. I&nbsp;tak setki albo tysiące razy. Żeby nie oszaleć, można sobie puścić w&nbsp;tle muzykę.

Którą opcję wybrałem? Tajemnica :wink: W&nbsp;każdym razie zdobyłem interesujące mnie Monitory. Od egzemplarza nr 1&nbsp;z 2014&nbsp;roku do egzemplarza nr 73&nbsp;z roku 2022. Dałoby się więcej, ale nie czułem potrzeby. Poza tym starsze egzemplarze mają problemy, o&nbsp;których kiedyś wspomnę.

Łącznie 2066&nbsp;plików. Zobaczmy teraz, co można z&nbsp;nich odczytać.

## Myszkowanie w&nbsp;metadanych

# Metoda 

Aby zajrzeć do informacji zawartych w&nbsp;plikach, użyłem niezawodnego **programiku konsolowego _pdfinfo_**. To część Popplera, większego zbioru programów do pracy z&nbsp;plikami PDF.

Kiedy użyjemy *pdfinfo* na jakimś pliku, wyświetli nam jego metadane. Zestaw ogólnych informacji, takich jak autor, program użyty do stworzenia pliku, data stworzenia, data modyfikacji:

{:.figure}
<img src="/assets/posts/msig/msig-pdfinfo.jpg" alt="Zrzut ekranu pokazujący konsolę i&nbsp;wynik użycia programu pdfinfo na konkretnym pliku PDF. Są ustawione jedna pod drugą. Najpierw nazwa pola, potem dwukropek, na końcu wartość."/>

{:.figcaption}
Wyniki z&nbsp;*pdfinfo*. Format `NazwaPola: Wartość`.

Druga sprawa: liczenie tych informacji, żeby znaleźć jakieś ogólne trendy. W&nbsp;tym celu stworzyłem sobie skrypt Pythona, odwołujący się do *pdfinfo* za kulisami. A&nbsp;że bardzo lubię ideę *open source* -- proszę bardzo, oto on.

{% include pyscript.html
name="pdf_metadata_stats.py"
link="/assets/skrypty/pdf_metadata_stats.py"
trailer="
<p>Skrypt wymaga zainstalowania Popplera, a&nbsp;przynajmniej programu <code class='language-plaintext highlighter-rouge'>pdfinfo</code>. W&nbsp;razie czego: to kwestia dosłownie pobrania jednego pliku i&nbsp;umieszczenia go w&nbsp;odpowiednim folderze.<br>
Skrypt sam wyświetla instrukcje, więc mam nadzieję, że każdy by sobie poradził <img class='emoji' title=':wink:' alt=':wink:' src='https://github.githubassets.com/images/icons/emoji/unicode/1f609.png' height='20' width='20'></p>

<p>Instrukcja korzystania: umieszczamy w&nbsp;tym samym folderze co pliki PDF, odpalamy (podwójnym kliknięciem / przez IDLE / przez konsolę...). Gdyby coś nie działało, to powinien nas poinformać.</p>

<p>Niektóre możliwości są dopasowane do Monitorów i&nbsp;bezużyteczne poza nimi (między innymi ustalanie daty rocznej na podstawie nazwy pliku). Natomiast sam program może się sprawdzić jako ogólne narzędzie do przeglądania i&nbsp;liczenia metadanych z&nbsp;PDF-ów.
</p>"
%}

# Odsiew

Nie wszystkie informacje z&nbsp;*pdfinfo* były dla mnie cenne. Niektóre z&nbsp;nich **były identyczne dla wszystkich plików, więc je odsiałem**.

Były wśród nich pola takie jak:

* `JavaScript`  
  (niektórych może zaskoczyć, ale tak, w&nbsp;plikach PDF można osadzać interaktywny kod. W&nbsp;Monitorach go na szczęście nie było).
* `Form`  
  (dla każdego wartość *AcroForm*, czyli domyślny standard od firmy Adobe).
* `Tagged`  
  (czy plik zawiera również dane na temat struktury; żaden z&nbsp;Monitorów ich nie ma, co jest złą wieścią dla szperaczy, archiwistów lub niewidomych korzystających z&nbsp;opcji czytania tekstu).

Kolejna sprawa -- ignorowałem informacje, które dla niemal każdego pliku były inne. Pola: `Pages`, `File size`, `CreationDate`, `ModDate`.

Daty mogłyby być źródłem ciekawych informacji (na przykład na temat odstępów między pierwszą a&nbsp;ostatnią edycją; godzin pracy), ale na chwilę obecną odpuściłem. Jeśli kiedyś do nich wrócę, edytuję wpis.

Zostaliśmy z&nbsp;polami, których wartości były urozmaicone, ale nie do przesady. Natomiast niektóre z&nbsp;nich były dla mnie mniej ciekawe.  
Oto one. Kolejno mamy tu wartość, liczbę jej wystąpień w&nbsp;naszych PDF-ach, pierwszy i&nbsp;ostatni rok wystąpienia.

Pole `Optimized`:

<div class="black-bg mono">
"yes": 1618&nbsp;(lata 2014-2022)<br/>
"no": 448&nbsp;(lata 2014-2021)
</div>

Pole `PDF version`:

<div class="black-bg mono bigspace-after">
"1.6": 1634&nbsp;(lata 2014-2022)<br/>
"1.5": 432&nbsp;(lata 2014-2017)
</div>

Na podstawie tych pól można przypuszczać, że pliki były tworzone przy użyciu różnych programów i&nbsp;ustawień -- wersja i&nbsp;optymalizacja to zwykle coś raz włączonego lub nie, przy czym się nie gmera.

Dałbym plusika twórcom Monitorów za trzymanie się jednej wersji formatu PDF (1.6) od roku 2017&nbsp;oraz wyłącznie zoptymalizowanych PDF-ów od 2021.  
Nawet jeśli to małe różnice dla czytelnika, to przynajmniej świadczą o&nbsp;nieco bardziej jednolitym zapleczu technicznym.

# Wyłapywanie trendów

Patrząc na dane z&nbsp;dwóch kategorii -- `Author` i&nbsp;`Producer` (program użyty do stworzenia pliku) -- można wyłapać pewne trwalsze zmiany za kulisami. Pokazujące, że do roku X&nbsp;było tak, a&nbsp;od roku X&nbsp;-- inaczej.

Spójrzmy na pole `Producer` (wartości częstsze):

<div class="black-bg mono bigspace-after">
"AD 9.0.0 (Windows)": 1294&nbsp;(lata 2014-2020)<br/>
"AD 20.0 (Windows)": 273&nbsp;(lata 2020-2022)<br/>
"AD 21.0 (Windows)": 245&nbsp;(lata 2021-2022)<br/>
"AD 19.0 (Windows)": 145&nbsp;(lata 2018-2020)<br/>
"AD 18.0 (Windows)": 72&nbsp;(w roku 2018)<br/>
"AD 9.0.0 (Windows); modified using iText 2.1.7 by 1T3XT": 27&nbsp;(lata 2014-2016)<br/>
"AD 22.0 (Windows)": 5&nbsp;(w roku 2022)
</div>

Miażdżącą większość mają w&nbsp;tej kategorii różne wersje programu *Acrobat Distiller* (skróciłem go do *AD*):

{:.post-meta .bigspace-after}
Możliwe, że sam Distiller nie był programem, w&nbsp;którym pracowano, lecz wyłącznie tym użytym do stworzenia pliku -- a&nbsp;głównym [mógł być np. InDesign](https://opusdesign.us/wordcount/how-to-create-an-imposed-pdf-with-acrobat-distiller/), używający AD za kulisami.

Liczba po *AD* to każdorazowo wersja programu. Można zauważyć, że **przez długi czas korzystano tylko ze starej wersji 9.0.0**. Pierwsze próby korzystania z&nbsp;nowszych wersji widzimy w&nbsp;2018 roku, a&nbsp;dopiero w&nbsp;2020 ostatecznie z&nbsp;nią skończono.

Wersja 9.0.0 przetrwała w&nbsp;Ministerstwie całkiem długo, patrząc na to, że to program najpóźniej [z 2009&nbsp;roku](https://acrobatusers.com/tutorials/acrobat-distiller-9/). Ustalenie dokładnych dat dla różnych wersji AD zostawiam bardziej wytrwałym czytelnikom.

Kolejna sprawa: obecność w&nbsp;niektórych polach tekstu `modified using iText 2.1.7 by 1T3XT`. *iText* jest całkiem niezależną [biblioteką](https://en.wikipedia.org/wiki/IText) do obróbki PDF-ów. Może to sugerować, że w&nbsp;plikach stworzonych narzędziami Adobe coś trzeba było poprawić i&nbsp;użyto właśnie *iT*.

Wnioski płynące z&nbsp;używanych wersji są raczej na plus -- jeśli uznamy korzystanie z&nbsp;nowszych wersji za oznakę bycia na bieżąco, to od okolic 2020&nbsp;roku się za to wzięli.

Kolejne pole -- `Author` (wartości częstsze):

<div class="black-bg mono">
"R<span class="cover">█████████</span>": 965&nbsp;(lata 2014-2020)<br/>
"M<span class="cover">█████████</span>": 759&nbsp;(lata 2014-2022)<br/>
"Agnieszka.J<span class="cover">█████████</span>": 171&nbsp;(lata 2020-2022)<br/>
"T<span class="cover">█████████</span>": 164&nbsp;(lata 2020-2022)
</div>

{:.figcaption}
Nazwiska zakryte przez mnie; liczbę liter pod zakrytymi prostokątami nieco zmieniłem.

Jeśli komuś się robi nieswojo na widok tych danych, spieszę uspokoić. Samo Ministerstwo **wydaje się nie robić z&nbsp;nazwisk tajemnicy**.  
W niektórych Monitorach znajdziemy informacje o&nbsp;tym, kto podpisał cyfrowo dany plik. Wskazujące tę osobę z&nbsp;imienia i&nbsp;nazwiska. Bezpośrednio na stronach dokumentu.

Co nie zmienia faktu, że lekko by mnie mroziła wizja, że jakiś nawiedzony byznesmen ustali moje dane i&nbsp;będzie się dobijał na moją prywatną skrzynkę, żebym nie publikował informacji o&nbsp;jego upadłości. No ale przyjmijmy, że w&nbsp;Ministerstwie wiedzą co robią.

A teraz popatrzmy na daty przy poszczególnych osobach. Mówią nam sporo.  
Jedna z&nbsp;osób, na M., ma bardzo długi staż przy tworzeniu Monitorów, trwający do teraz. 
Z&nbsp;kolei na miejsce osoby o&nbsp;nazwisku R., która opracowała ich najwięcej ze wszystkich, w&nbsp;2020 roku weszły dwie nowe osoby. Pracują mniej więcej po równo, jeśli patrzeć na liczbę Monitorów.

Metadane w&nbsp;roli komunikatów o&nbsp;zmianach kadrowych? Zdziwiłbym się, ale lata czytania o&nbsp;różnych cyfrowych sprawach mnie znieczuliły :wink:

# Wyłapywanie anomalii

Oprócz opisanych wyżej poszlak zdradzających nam, co się na zapleczu działo, mamy trochę informacji odstających od reszty. I&nbsp;to w&nbsp;całkiem różnych kategoriach.

Niektóre wartości zaznaczyłem kolorem; wrócimy do nich jeszcze.

`Page Size`:

<div class="black-bg mono bigspace-after">
"595 x&nbsp;842 pts (A4)": 1321&nbsp;(lata 2014-2020)<br/>
"595.22 x&nbsp;842 pts (A4)": 742&nbsp;(lata 2017-2022)<br/>
<span class="red">"595.276 x&nbsp;841.89 pts (A4)": 3&nbsp;(w roku 2020)</span>
</div>

`Creator`:

<div class="black-bg mono bigspace-after">
"PScript5.dll Version 5.2.2": 2063&nbsp;(lata 2014-2022)<br/>
<span class="red">"Adobe InDesign CS6 (Windows)": 2&nbsp;(w roku 2020)</span><br/>
<span class="red">"Adobe InDesign 15.0 (Windows)": 1&nbsp;(w roku 2020)</span>
</div>

`Author` (wartości rzadsze):

<div class="black-bg mono">
<span class="red">"BRAK DANYCH": 3&nbsp;(w roku 2020)</span><br/>
"r<span class="cover">█████████</span>": 2&nbsp;(lata 2017-2019)<br/>
"Mateusz.R<span class="cover">█████████</span>": 1&nbsp;(w roku 2022)<br/>
"K<span class="cover">█████████</span>": 1&nbsp;(w roku 2017)
</div>

{:.post-meta .bigspace-after}
Pole *BRAK DANYCH* oznacza, że w&nbsp;wynikach z&nbsp;*pdfinfo* w&nbsp;ogóle nie było takiego pola.

`Producer` (wartości rzadsze):

<div class="black-bg mono bigspace-after">
<span class="red">"Adobe PDF Library 10.0.1": 2&nbsp;(w roku 2020)</span><br/>
"Adobe Acrobat Pro DC 19.21.20061": 1&nbsp;(w roku 2020)<br/>
<span class="red">"Adobe PDF Library 15.0": 1&nbsp;(w roku 2020)</span><br/>
"Acrobat Distiller 10.1.16 (Windows)": 1&nbsp;(w roku 2017)
</div>


{% include info.html
type="Ciekawostka"
text="Jeśli spojrzymy na najczęstszą wartość pola `Creator`, zobaczymy *PScript(...).dll*.  
Pierwsze słowo odnosi się zapewne do *[PostScriptu](https://pl.wikipedia.org/wiki/PostScript)*, czyli języka złożonego z&nbsp;krótkich komend opisujących jak stworzyć dokument. Zwykle ukrytego za kulisami.  
Rozszerzenie *dll* sugeruje z&nbsp;kolei, że to nie jakiś program graficzny, w&nbsp;którym sobie pracujemy, tylko bardziej [narzędzie](https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/dynamic-link-library) wykorzystywane przez inne programy. Trochę jak *pdfinfo* przez mój skrypt.  
Wniosek: skróty i&nbsp;nazwy potrafią wiele ujawniać, jeśli poświęci się czas na ich poznanie."
%}

Niektóre wiersze oznaczyłem czerwonym kolorem. A&nbsp;to dlatego, że **anomalie chodzą grupami -- wszystkie te nietypowe wartości pochodzą z&nbsp;trzech plików**:

* *monitor_2020_22.pdf*
* *monitor_2020_23.pdf*

  (oba stworzono przy użyciu kombinacji Adobe InDesign CS6 + Adobe PDF Library 10.0.1)

* monitor_2020_59.pdf

  (stworzony kombinacją Adobe InDesign 15.0 + Adobe PDF Library 15.0)

W żadnym z&nbsp;tych trzech plików nie było w&nbsp;ogóle pola `Author`, a&nbsp;ich strony miały wymiary 595,276 x&nbsp;841,89 jednostek.  
Widzimy tu ciekawy detal -- zdarza się, że jeden atrybut (tu: liczba po przecinku w&nbsp;rozmiarze stron) jest mocno sprzężony z&nbsp;konkretnym programem. Na podstawie jego wartości dałoby się zawęzić listę programów, jakie mogły posłużyć do stworzenia pliku.

Jeśli chodzi o&nbsp;pozostałe anomalie:

* *monitor_2020_28.pdf* 

  Był jedynym monitorem stworzonym przy użyciu programu Adobe Acrobat Pro DC 19.21.20061. Wyróżniał się też pustym polem `Title`, który zwykle zawiera nazwę dokumentu źródłowego. Wszystko inne dość typowe -- autorem osoba na M., z&nbsp;najdłuższym stażem w&nbsp;tworzeniu.

* *monitor_2017_244.pdf*

  Jedyny, którego autorem była osoba na K., zaś programem użytym do stworzenia -- Acrobat Distiller 10.1.16. Zwykle wersje Distillerów były bardziej „okrągłe”.

* *monitor_2022_69.pdf*

  Jedyny, którego autorem był Mateusz R. Reszta danych typowa.  
  To względnie nowy Monitor, więc możliwe, że to wcale nie anomalia, a&nbsp;pan M.R. jeszcze zagości wśród autorów.

Wśród autorów dwa razy pojawia się również osoba na *r* (z małej litery).  
To dokładnie to samo nazwisko, które odpowiada za największą liczbę Monitorów. Tylko że zapisane małymi literami.

Nie mam doświadczenia z&nbsp;programami od Adobe, ale jeśli są dość podobne do innych biurowych, to nazwą autora jest zwykle nazwa użytkownika ustawiona w&nbsp;komputerze -- jak *admin*, *Gość* albo chociaż *Tata*, jak u&nbsp;jednego mojego wykładowcy.

Jeśli przyjmiemy, że tak jest też w&nbsp;Ministerstwie, zaś autorzy nie uzupełniają pola *Autor* samodzielnie, to oznaczałoby, że **te dwa dokumenty mogły zostać stworzone przez panią R. na innym komputerze niż zwykle**. Były nimi:

* monitor_2017_227.pdf
* monitor_2019_240.pdf

W ten sposób otrzymaliśmy **listę ośmiu nietypowych PDF-ów, z&nbsp;których aż połowę stworzono w&nbsp;2020 roku**. Czyżby pandemia zasiała mały chaos?

Na razie nie wiem, czy ta wiedza mi się do czegokolwiek przyda. Ale kolejnym etapem będzie zaglądanie do treści Monitorów. Być może nietypowe pliki wyróżnią się także pod innymi względami.

## Podsumowanie

Dane to potęga. Metadane mogą być jeszcze większą -- bo mało kto o&nbsp;nich wie. Ludzie beztrosko przenoszą pliki między komputerami, edytują, wysyłają.  
A metadane się gromadzą -- gotowe zdradzić, kto i&nbsp;w jakich godzinach pracował nad plikiem, ilu autorów ma organizacja, jakiego używa sprzętu.

W przypadku Monitorów dane są nieszkodliwe. Raczej.  
Zebrałbym się wręcz na odrobinę optymizmu i&nbsp;powiedział, że trochę im się za kulisami poprawiło. Mają coraz nowsze programy, od pewnego czasu aktualizują wersje na bieżąco.

Na plus również to, że wydają się korzystać z&nbsp;tradycyjnych, nieinternetowych wersji programów. Dzięki temu, gdyby Adobe kiedyś odcięło Polskę od swoich usług ([jak Wenezuelę](https://www.theverge.com/2019/10/7/20904030/adobe-venezuela-photoshop-behance-us-sanctions)), to nadal moglibyśmy tworzyć nasze piękne Monitory.

A my, jako osoby fizyczne? Też możemy z&nbsp;tego wpisu wyciągnąć nauczkę.  
**Warto o&nbsp;metadanych wiedzieć i&nbsp;je czyścić**. Chyba że chcemy, żeby nasze korpo zobaczyło na przykład, że ich ściśle tajny raport opracowaliśmy w&nbsp;środku nocy, parę godzin przed terminem, na komputerze osoby o&nbsp;nicku *Dżagusiaaa* albo *Alvaro Caliente* :smile:

Życzę sprytu i&nbsp;unikania takich wpadek! A&nbsp;Monitory jeszcze zobaczymy w&nbsp;kolejnym, raczej nieodległym wpisie.

