---
layout: post
title: "Jak nie zakrywać poufnych informacji"
subtitle: "Uczymy się na (cudzych) błędach."
date:   2021-10-29 01:35:00 +0100
tags: [Podstawy, Porady]
image: "zakrywanie-danych/zakryty-tekst.jpg"
image-width: 1200
image-height: 700
---

Ten wpis będzie krótki i&nbsp;treściwy. Do jego stworzenia zainspirowała mnie poboczna dyskusja na forum *Hacker News* dotycząca pewnego artykułu prasowego.

Mianowicie: ktoś w&nbsp;komentarzach podlinkował obrazek, w&nbsp;którym nazwy plików rozmyto w&nbsp;programie graficznym. Ktoś  inny napisał, że lepiej żeby to nie było nic tajnego. Bo przy odrobinie pracy dałoby się odwrócić efekt rozmycia i&nbsp;odczytać tekst.

Już nieraz słyszałem o&nbsp;wpadkach, kiedy **autor wierzył że coś usunął, a&nbsp;jedynie to przykrył**.  
Dlatego powstał ten wpis. Pokażę tu kilka pułapek związanych z&nbsp;ukrywaniem informacji w&nbsp;popularnych plikach graficznych, PDF-ach i&nbsp;im podobnych.

Może się czegoś nauczymy. A&nbsp;jeśli nie, to przynajmniej można spojrzeć na wtopki innych i&nbsp;się cieszyć, że to (jeszcze) nie nasze :smile:

# Zakrywanie informacji na obrazkach

Przedstawiam Wam piękny szary prostokąt w&nbsp;stylu *modern art*:

{:.bigspace}
<img src="/assets/posts/zakrywanie-danych/kontrast-minus-126.jpg" alt="Obrazek wyglądający jak szary prostokąt w&nbsp;jednolitym kolorze"/>

Widzicie tu jakiś tekst? Szczerze wątpię.

A jednak jest! Jeśli pobierzecie obrazek (opcją `Zapisz obraz` albo <a href="/assets/posts/zakrywanie-danych/kontrast-minus-126.jpg" download>stąd</a>), otworzycie go w&nbsp;edytorze GIMP (inne też powinny działać) i&nbsp;podkręcicie kontrast na maksa, tekst będzie całkiem wyraźny.

Proces tworzenia obrazka wyglądał tak:

1. Stworzyłem w&nbsp;Gimpie mały obrazek z&nbsp;tekstem „Test”;
2. Wszedłem w&nbsp;opcję `Kolory > Jasność i kontrast`, **zmieniłem wartość na -126 (najniższa to -127)**;
3. Zapisałem plik jako JPG z&nbsp;jakością 90/100.

Tak to wyglądało:

{:.bigspace}
<img src="/assets/posts/zakrywanie-danych/odwracanie-kontrastu.jpg" alt="Trzy zrzuty ekranu z&nbsp;programu GIMP. Na pierwszym z&nbsp;nich widać tekst o&nbsp;treści 'Test', na drugim szary prostokąt i&nbsp;suwak kontrastu blisko minimum, na trzecim nieco postrzępiony tekst 'Test' i&nbsp;suwak kontrastu na maksimum."/>

Jeden punkt robi różnicę. Gdybym dał suwak kontrastu najniżej, na -127, to tekst zostałby całkiem zniszczony. A&nbsp;przy -126 cały proces był łatwo odwracalny.  
(Tekst jest postrzępiony jedynie dlatego, że nie zapisałem *jotpega* w&nbsp;pełnej jakości).

Pracując z&nbsp;komputerem, nie zawsze warto ufać oczom.

Podobnie jest ze wszystkimi algorytmami zamazującymi, rozmywającymi itp. Choć tekst wydaje się nieczytelny dla naszych oczu, na poziomie pikseli nadal mogą występować subtelne różnice.  
Ktoś zdeterminowany mógłby eksperymentować, aż odkryje zakryte.

W takim razie co robić, żeby tajemnice nie ujrzały światła dziennego? Edytując obrazki, **zakrywamy je jednolitym kolorem**. Nie żadne rozmycia, nie żadne efekty, tylko prostokąt: cztery krawędzie i&nbsp;kolor między nimi.

(w Gimpie wystarczy nacisnąć `R`, żeby przejść do trybu rysowania prostokąta, a&nbsp;potem `Ctrl`+`,`, żeby wypełnić go kolorem).

Ta metoda jest prosta i&nbsp;skuteczna.
Ale -- ważne! -- odnosi się to tylko do prostych obrazków. JPG, PNG itp.  
**Próbując zrobić coś takiego z&nbsp;innymi plikami, takimi jak PDF, wpadlibyśmy w&nbsp;pułapkę**. Już ją opisuję.

# Zakrywanie informacji w&nbsp;PDF-ach

Dokładniej rzecz biorąc: nie tylko w&nbsp;nich. Dotyczy to wszelkich formatów, które przechowują nie tylko piksele, ale również tekst.

Pokażę na przykładzie pliku SVG.
 
Nasz plik zawierał moje bida-logo i&nbsp;napis „Ciemna strona”.  
To bardzo poufny tekst, więc zakryłem go jednolitym, nieprzezroczystym, szarym prostokątem:

<img src="/assets/posts/zakrywanie-danych/niezbyt-zakryty-napis.svg" alt="Grafika wektorowa SVG pokazująca logo Ciemnej Strony, a&nbsp;pod nim słowo 'Ciemna' i&nbsp;drugie słowo, zakryte szarym prostokątem." width="400px"/>

SVG ma wszelkie cechy obrazka -- da się go otworzyć w&nbsp;programach do grafiki; mówi się że to *grafika* wektorowa. A&nbsp;jednak to coś więcej!

Gdyby to był zwykły obrazek, jak JPG, to po zakryciu nikt by nie wiedział, co się pod tym prostokątem ukrywa.  
Ale SVG za kulisami to nie piksele, lecz seria instrukcji. Czasem czytelnych dla człowieka.  
Jeśli zajrzymy do wnętrza mojego pliku, to sami zobaczymy:

{:.figure}
<img src="/assets/posts/zakrywanie-danych/svg-wnetrze.jpg" alt="Treść pliku SVG składającego się z&nbsp;kilku linijek. Jedną z&nbsp;nich otacza pomarańczowa ramka."/>

{:.figcaption}
Bebechy naszego pliku SVG.  
W formie screenshota, żeby tekst nie „wylewał się” poza ekran.

Pomarańczową ramką otoczyłem element odpowiadający szaremu prostokątowi.  
A nad nim? **Wyraźnie widać cały nasz tekst**. 

Jeśli chcecie sami to sprawdzić, możecie <a href="/assets/posts/zakrywanie-danych/niezbyt-zakryty-napis.svg" download>pobrać mój plik</a>.  
Następnie otwieramy go jako tekst, na przykład w&nbsp;Notatniku.  
W tym celu klikamy go prawym przyciskiem myszy, wybieramy `Otwórz za pomocą...` i&nbsp;znajdujemy Notatnik na liście.

**Dokładnie tak samo działają PDF-y**. Każdy dodany element to po prostu nowa instrukcja. Tylko że PDF-y są potem kompresowane, więc nie odczytamy ich gołym okiem, jak plików SVG.

Ale nawet najmniej techniczna osoba może otworzyć PDF-a w&nbsp;programie -- choćby w&nbsp;Adobe Readerze -- zrobić `Ctrl`+`A`, `Ctrl`+`C` i&nbsp;skopiować sobie cały tekst, łącznie z&nbsp;naszymi tajemnicami.

I nie są to teoretyczne rozważania. Wtopki z&nbsp;czarnymi prostokątami już wiele razy się zdarzały. Również ważnym i&nbsp;poważnym.

Polskie instytucje mamy na co dzień, więc pośmiejmy się z&nbsp;zagranicznych:

* australijska [komisja lekarska](https://www.theregister.com/2016/01/17/pdf_redaction_is_hard_nsw_medical_council_finds_out_the_hard_way/) ujawniła dane pewnej lekarki i&nbsp;jej syna;
* prawnicy Paula Manaforta, byłego szefa sztabu wyborczego Donalda Trumpa, ujawnili niechcący utajone szczegóły sprawy (dokument jest [tutaj](https://s3.documentcloud.org/documents/5677512/Manafort-20190108-Dc.pdf)); 
* opinia amerykańskiego sędziego federalnego zdradziła parę informacji na temat [powiązań biznesowych Apple](https://www.abajournal.com/news/article/cut-and-paste_reveals_redacted_info_on_apple_smartphone_market_in_federal_j);
* Z podobnie „utajonej” korespondencji wewnętrznej Facebooka dowiedzieliśmy się, że rozważali sprzedawanie firmom [pełnego dostępu do danych użytkowników](https://mashable.com/article/facebook-considered-selling-data-pdf-fail).

W&nbsp;jaki sposób zapobiec takim gafom?

Jednym ze sposobów jest użycie wbudowanych funkcji redagowania dokumentów. Ma takie coś np. [Adobe Acrobat](https://experienceleague.adobe.com/docs/document-cloud-learn/acrobat-learning/advanced-tasks/redact.html?lang=en). Nadal jest tu jednak miejsce na ludzki błąd, gdybyśmy wybrali nie tę opcję.

Istnieje również rozwiązanie nuklearne, ale pewne.  
Można **skonwertować każdą stronę na obrazek**, a&nbsp;potem ewentualnie połączyć te obrazki w&nbsp;nowego PDF-a.  
Jeden minus taki, że drastycznie urośnie rozmiar pliku. Ale uznajmy, że to do przeżycia.  
Bardziej może nas zaboleć druga sprawa: **w ten sposób niestety stracimy cały tekst**.

Na szczęście można go odzyskać poprzez *OCR* (*Optical Character Recognition*). Na pewno nie będzie w&nbsp;100% dokładny -- a&nbsp;po jego dodaniu ciężkie pliki staną się jeszcze cięższe -- ale odzyskamy choć częściowo możliwość przeszukiwania PDF-a.

W każdym razie po takim przemieleniu w&nbsp;pliku nie zostaną już żadne sekrety :wink:

Gdybyście kiedyś musieli usuwać tajemnice z&nbsp;dokumentów, to życzę powodzenia! A&nbsp;gdyby była wtopa, to pamiętajcie, że zawsze mogło być gorzej. Jak u&nbsp;naszych elitarno-prawniczych Amerykanów.

# Bonus: konkretne programy

Wyżej były ogólniki, a&nbsp;tutaj będą konkretne nazwy!

Zakładam, że zakrywamy coś sekretnego, więc żadne rozwiązania internetowe nie wchodzą w&nbsp;grę. I&nbsp;bardzo dobrze! Klasyczne offline'owe programy w&nbsp;zupełności wystarczą.

Do samego zakrywania obrazków prostokątami wystarczy [GIMP](https://www.gimp.org/) albo nawet Paint. Innych nie używałem, więc nie wiem czy polecić. Natomiast aby zmienić PDF-y tekstowe w&nbsp;obrazkowe, musimy wykonać kilka kroków:

{:.bigspace-before}
**1. Zapisanie każdej strony PDF-a jako osobnego obrazka**

To również można zrobić przez GIMP-a, o&nbsp;ile korzystamy z&nbsp;wersji *2.10* lub nowszej.  
Wtedy po prostu klikamy PDF-a prawym przyciskiem, otwieramy w&nbsp;GIMP-ie. A&nbsp;następnie działamy [zgodnie z&nbsp;tą instrukcją](https://askubuntu.com/a/1098603) (po angielsku).

{:.bigspace}
<details>
<summary>A jeśli nie boimy się konsoli?</summary>

<p>Wtedy warto zainstalować Popplera – zestaw programów konsolowych do pracy z PDF-ami.<br>
(Ma wersje na <a href="https://poppler.freedesktop.org/">Linuxa</a>, na <a href="https://macappstore.org/poppler/">Maca</a> i <a href="https://blog.alivate.com.au/poppler-windows/">na Windowsa</a>).</p>

<p>Jeśli mamy przykładowo PDF-a o nazwie <code class="language-plaintext highlighter-rouge">jakis.pdf</code>, to otwieramy konsolę w tym samym folderze co on i wpisujemy:</p>

<div class="black-bg mono">
pdftocairo -jpeg jakis.pdf
</div>

</details>

Skończymy z&nbsp;plikami *JPG* -- po jednym na jedną stronę. Jeśli jeszcze nie zakrywaliśmy informacji jednolitymi prostokątami, to teraz jest na to dobry czas.

{:.bigspace-before}
**2. Połączenie obrazków w&nbsp;jednego PDF-a**

Czas na połączenie obrazków z&nbsp;poprzedniego kroku. W&nbsp;jednego PDF-a, w&nbsp;którym każdy obrazek jest osobną stroną. Nie widzę łatwego sposobu na zrobienie tego w&nbsp;GIMP-ie, ale to&nbsp;nic!

Na Windowsie wystarczy je wszystkie zaznaczyć, wybrać opcję *Drukuj*, a&nbsp;potem *Drukuj do&nbsp;pliku*.  
Z MacBookami nie mam doświadczenia, ale jeśli wierzyć [tej instrukcji](https://www.howtogeek.com/247879/how-to-combine-images-into-one-pdf-file-on-a-mac/), działa to podobnie.  
Na Linuksie też się da [na kilka sposobów](https://itsfoss.com/convert-multiple-images-pdf-ubuntu-1304/).

{:.bigspace-before}
**3. (Opcjonalnie) Nałożenie tekstu na naszego obrazkowego PDF-a**

OCR nigdy nie będzie w&nbsp;100% dokładny, ale zawsze daje jakąś możliwość przeszukiwania tekstu. Przy obrazkowym PDF-ie byłaby zerowa.

Do nałożenia tekstu możemy użyć komercyjnego programu [ABBYY FineReader](https://pdf.abbyy.com/) (tylko na Windowsa i&nbsp;Maca). Gdy już nam rozpozna co trzeba, wybieramy opcję zapisania pliku jako PDF, z tekstem pod warstwą obrazkową.

{:.bigspace}
<details>
<summary>A jeśli nie boimy się konsoli?</summary>

<p>Można zamiast płatnego programu zainstalować darmowego Tesseracta (tutaj <a href="https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/">nieformalne instrukcje</a>, a tutaj wersja <a href="https://github.com/UB-Mannheim/tesseract/wiki">na Windowsa</a>).</p>

<p>Tesseract czyta tylko obrazki, więc <strong>najlepiej go użyć zaraz po kroku 1</strong>, pomijając krok 2 (łączenie w PDF-a).</p>

<p>W tym celu w tym samym folderze musimy stworzyć plik tekstowy (powiedzmy <code class="language-plaintext highlighter-rouge">obrazki.txt</code>), w którym – linijka pod linijką – będą wymienione pliki z obrazkami, które chcemy połączyć w PDF-a.</p>

<p>Jeśli obrazków jest tylko kilka, możemy nawet stworzyć ten plik ręcznie. Ale lepiej konsolką. Na Windowsie wpisujemy w nią:</p>

<div class="black-bg mono">
dir > obrazki.txt
</div>

<p>Na Linuksie i MacOS:</p>

<div class="black-bg mono">
ls > obrazki.txt
</div>

<p>Usuwamy z pliku tekstowego te nazwy plików, które nie są obrazkami. Upewniamy się, że mamy go w tym samym folderze co obrazki. Po czym odpalamy Tesseracta:</p>

<div class="black-bg mono">
tesseract -l eng obrazki.txt po_ocr pdf
</div>

<p>(Uwaga na spację przed ostatnim <code class="language-plaintext highlighter-rouge">pdf</code>! A zamiast <code class="language-plaintext highlighter-rouge">eng</code> można wpisać inny język lub języki dokumentu, zgodnie z kodami Tesseracta).<br>
Po powyższej komendzie powstanie nam plik <em>po_ocr.pdf</em>.</p>

</details>

Jeśli spróbujemy w&nbsp;naszym końcowym PDF-ie zaznaczyć i&nbsp;skopiować jakiś widoczny tekst, to zobaczymy że to działa -- lepiej lub gorzej.  
Ale jeśli spróbujemy coś skopiować spod miejsc zakrytych prostokątami, to wyjdą nam co najwyżej losowe znaki. Co miało być niemożliwe do odczytania, to takie jest.

To tyle na dziś! Może kiedyś sklecę jakiś własny skrypt, bo wydaje się że jest popyt. A&nbsp;póki co -- do kolejnych wpisów :smile:
