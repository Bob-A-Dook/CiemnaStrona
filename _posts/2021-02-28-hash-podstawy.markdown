---
layout: post
title:  "O haszach bez tagów*"
subtitle: "Czyli o tym, jak komputer porównuje rzeczy."
date:   2021-02-28 16:40:37 +0100
tags: [Podstawy]
---

{:.post-meta .bigspace}
\* Oprócz jednego tagu „Podstawy”.

Kojarzycie pewnie, czym są hasztagi? Albo haszysz, na przykład z&nbsp;Maroka?  
Jeśli tak, to fajnie. Ale dzisiaj będzie o&nbsp;czymś zupełnie innym.

Hash (czyt. hasz) w&nbsp;znaczeniu komputerowym. Będę tu używał spolszczonego zapisu, bo jest dwuznaczny i&nbsp;kojarzy się z&nbsp;tym marokańskim znaczeniem :sunglasses:

Wydaje się czymś bardzo tajemniczym i&nbsp;niezrozumiałym. Ale jednocześnie to jeden z&nbsp;fundamentów współczesnej informatyki. W&nbsp;życiu codziennym sprawa jest prosta -- **haszy używa się do porównywania, czy dwie rzeczy są takie same**. Nic mniej i&nbsp;nic więcej.

Sprawdzanie, czy wpisaliśmy prawidłowe hasło? Albo czy już jesteśmy w&nbsp;bazie danych? Blokowanie programów, do których mógł zostać dodany wirus? Podpisy cyfrowe? Kryptowaluty?  
Za kulisami wszystkich tych rzeczy stoją hasze. Prosta rzecz o&nbsp;wielu zastosowaniach.

Hasz jest dla nas interesujący również z&nbsp;punktu widzenia prywatności.

Niedługo będę pisał o&nbsp;wredniejszych sposobach identyfikacji -- skryptach, które analizują subtelne cechy przeglądarki i&nbsp;przypisują nam jakiś numer. A&nbsp;później porównują go ze swoją bazą, żeby nas rozpoznać w&nbsp;różnych zakątkach internetu. **Hasz jest fundamentem ich działania**.

Z tego względu warto go poznać, zanim przejdziemy dalej. Mogę Wam obiecać, że jeszcze nieraz będę odsyłał do tego wpisu.

## Czym jest hasz?

Nie będę tu o&nbsp;nim pisał od strony technicznej, bo: a) wpis byłby długi i&nbsp;męczący; i&nbsp;b) sam nie pojmuję szczegółów, za dużo matmy. Ale znam wystarczająco wiele ogólników.

Bardziej oficjalną (ale wciąż w&nbsp;miarę przystępną) definicję znajdziecie na przykład [na Wikipedii](https://pl.wikipedia.org/wiki/Funkcja_skr%C3%B3tu).

W praktyce haszowanie polega na tym, że mamy funkcję. Czyli fragment kodu. Kiedy użyjemy tej funkcji na jakichś danych, to je przetworzy i&nbsp;wypluje pewien ciąg znaków.

Ma dwie kluczowe właściwości:

* Póki wrzucamy dokładnie takie same dane, otrzymujemy dokładnie taką samą rzecz.
* ...Ale **jeśli wrzucimy inne dane, to wypluje coś całkiem innego**.

  {:.figure}
  <img src="/assets/posts/haszowanie/python-hash.webp" alt="Konsola interaktywna Pythona, linijka po linijce. Widać że po użyciu funkcji hash na tekście 'Ciemna strona' wyświetliło dwa razy taką samą długą liczbę. Ale kiedy użyto jej na tekście z&nbsp;literą 'o' zmienioną na '0', to liczba jest całkiem inna." width="400px"/>

  {:.figcaption}
  Wystarczyła zmiana jednej litery, żeby funkcja haszująca dała zupełnie inny wynik.

Te dwie cechy sprawiają, że obliczone hasze są idealne do porównywania, czy dwie rzeczy są dokładnie tym samym.

Poza tym funkcja haszująca **działa tylko w&nbsp;jedną stronę**. Praktycznie nie da się na podstawie uzyskanego hasza ustalić, jakie dane mieliśmy na początku.

Dzięki tej własności możemy bez obaw, jawnie, wymieniać się haszami. Nie dojdzie do tego, że ktoś z&nbsp;nich wyczyta pierwotne informacje -- takie jak nasze hasła albo treść magisterki.  
(Metody odwracania haszy istnieją, ale, nawet dla krótkich haseł, są [niesamowicie niewydajne](https://pl.wikipedia.org/wiki/T%C4%99czowe_tablice)).

Jako wisienka na torcie jeszcze to, że [hasz ma stałą długość](https://crypto.stackexchange.com/questions/2144/does-the-sha-hash-function-always-generate-a-fixed-length-hash), niezależnie od rozmiaru danych wejściowych. Możemy więc łatwo ścisnąć treść całego listu, całej książki, a&nbsp;nawet całej biblioteki w&nbsp;krótki hasz. I&nbsp;przesłać znajomym w&nbsp;jednej wiadomości, na pewno się ucieszą.

{% include info.html type="Ciekawostka" text="Funkcje haszujące występują w&nbsp;wielu różnych odmianach.  
Na przykład ta z&nbsp;Pythona daje inny wynik za każdym razem, kiedy go uruchomimy. Byłaby nieprzydatna do zadań wymagających stabilności, np. do weryfikacji haseł.  
Od takich przypadków są wersje, które zawsze dają taki sam wynik. Ich przykład zawiera [ten wpis](https://nitratine.net/blog/post/how-to-hash-passwords-in-python/).  
Istnieją również bardziej egzotyczne wersje, takie jak *SimHash* -- tworzy hasze tym bardziej podobne, im bardziej podobne były dane początkowe. Przydaje się np. w&nbsp;wyszukiwarkach obrazków."%}

## Haszowanie w&nbsp;praktyce

We wstępie zasugerowałem kilka zastosowań haszy, które mogłyby nas zainteresować. Tutaj to nieco rozwinę.  
Ich przykłady w&nbsp;naturze:

* Tworzenie wydajnych programów

  Często program musi zrobić coś złożonego z&nbsp;każdym z&nbsp;wielu elementów. Ale co, jeśli sporo z&nbsp;nich ma identyczne właściwości? Nie ma sensu za każdym razem liczyć wszystkiego od nowa -- **można policzyć raz, zapamiętać wynik i&nbsp;przechować go na później**!  
  W&nbsp;tej sytuacji często stosuje się hasze, ponieważ sprowadzają kilka wartości do jednej liczby. Po każdym wykonaniu działań na nowej rzeczy zapisujemy gdzieś parę `hasz-wynik`.  
  A&nbsp;kiedy trafi się kolejna rzecz, to szybko liczymy jej hasz i&nbsp;patrzymy, czy mamy dla niego zapisany wynik. Jeśli nie, to obrabiamy tę rzecz od zera. Jeśli tak, to po prostu bierzemy gotowy wynik. Oszczędność czasu może być ogromna!

* Wykrywanie, czy ktoś majstrował przy plikach.
  
  Popularne aplikacje i&nbsp;programy wydają się łakomym kąskiem dla hakerów -- można do nich dodać złośliwy kod, umieścić gdzieś w&nbsp;internecie, a&nbsp;potem linkować do tej wersji w&nbsp;różnych miejscach. Może ktoś się nabierze!  
  Hasze pozwalają się przed tym zabezpieczyć. Kiedy autor oryginalnej aplikacji wypuszcza nową wersję, może również obliczyć jej hasz i&nbsp;umieścić go w&nbsp;jakiejś centralnej bazie.  
  Gdyby ktoś zmienił cokolwiek w&nbsp;kodzie programu i&nbsp;go udostępnił, to **zawirusowana wersja będzie miała zupełnie inny hasz niż oryginał**. Jeśli system operacyjny w&nbsp;jakiś sposób porównuje hasze ze wspomnianą bazą, to będzie mógł wykryć majsterkowanie, zablokować taką aplikację i&nbsp;ostrzec użytkownika.

* Logowanie do stronek

  Kiedy zakładamy konto na jakiejś platformie, prawie zawsze ustalamy do niego hasło.  
  Gdyby jej właściciele nie dbali o&nbsp;bezpieczeństwo, to mogliby przechowywać nazwę użytkownika razem z&nbsp;hasłem jako tekst. Wtedy, gdyby ich baza danych wyciekła, każdy mógłby skopiować nazwę i&nbsp;hasło. I&nbsp;po prostu się zalogować jako my.  
  Strony bardziej dbające o&nbsp;bezpieczeństwo przechowują zamiast tego hasze. Przy każdym naszym logowaniu serwer przekształca hasło w&nbsp;hasz i&nbsp;sprawdza, czy ma go przy naszej nazwie użytkownika. Jeśli tak, to nas przepuszcza.  
  Gdyby w&nbsp;takim przypadku nastąpił wyciek bazy, to nie byłby taki groźny. **Mając nazwę użytkownika i&nbsp;hasz, włamywacz i&nbsp;tak nie będzie wiedział, co wpisać w&nbsp;polu „Hasło”**!

* Inwigilacja podczas ruchu w&nbsp;internecie

  No i&nbsp;niestety ciemna strona haszowania.  
  Nawiązując do naszej serii o&nbsp;internetowej inwigilacji -- wyobraźmy sobie, że przy każdym kontakcie ze stroną A&nbsp;wysyłamy jej pakiet informacji: adres IP + informacje o&nbsp;urządzeniu + ustawienia językowe + coś charakterystycznego.  
  Nie wiemy, że strona A&nbsp;przesyła te informacje jakiejś organizacji gromadzącej dane -- dajmy na to SpyCorp.  
SpyCorp nie ma nas w&nbsp;bazie, ale oblicza hasz naszych informacji i&nbsp;go do niej dodaje, wraz z&nbsp;informacją że ktoś z&nbsp;takim haszem był na stronie A.  
  Potem odwiedzamy stronę B, o&nbsp;czymś zupełnie innym. Ona również spiskuje przeciw nam i&nbsp;wysyła nasze informacje do SpyCorp. Nie zmieniły się od czasu wizyty na stronie A. Więc kiedy SpyCorp oblicza hasz, to odkrywa, że już go ma w&nbsp;bazie. Teraz **wie, że odwiedziliśmy zarówno B, jak i&nbsp;A**. Może zrobić z&nbsp;tą wiedzą różne rzeczy.
  
## Bonus: jak i&nbsp;po co sprawdzać hasz?

Okej. Wiemy już czym jest hasz, że jest absolutnie powszechny. Pewnie jeszcze go spotkamy. Ale po co mamy umieć go sprawdzać, jeśli nie planujemy tworzyć żadnej platformy?

Możliwe że faktycznie nigdy go nie użyjecie. Dlatego oznaczyłem tę część jako *bonus*. Ale mam dwa mniej lub bardziej naciągane pomysły, kiedy porównywanie haszy może się przydać.

Jeśli chcecie przejść prosto do nich, to <a href="#sprawdzanie-programów">są tutaj</a>.

# Jak to zrobić na Windowsie?

Najpierw o&nbsp;tym, w&nbsp;jaki sposób można sprawdzić hasz. Pokażę na przykładzie Windowsa.

Otwieracie Eksplorator (ikona <img style="display:inline-block" src="/assets/posts/haszowanie/eksplorator-ikona.webp" alt="Żółta ikona Eksploratora Windowsa"/>).

Potem przechodzicie do dowolnego folderu z&nbsp;jakimś plikiem.  
Na potrzeby pokazu stworzyłem folder *hash_test*, a&nbsp;w&nbsp;nim jedną rzecz -- *plik testowy.txt*, zawierający jedynie słowa „Jakiś tekst”:

{:.bigspace}
<img src="/assets/posts/haszowanie/hasz-plik-pokaz.webp" alt="Zrzut ekranu dwóch okien Windowsa. Pierwsze pokazuje dużą ikonę pliku tekstowego w&nbsp;Eksploratorze. Drugie pokazuje otwarty program Notatnik, z&nbsp;widocznym tekstem 'Jakiś tekst'."/>

Klikacie w&nbsp;zakładkę `Plik` w&nbsp;lewym górnym rogu, a&nbsp;następnie na `Otwórz program Windows PowerShell`:

{:.figure .bigspace}
<img src="/assets/posts/haszowanie/powershell-menu.webp" alt="Menu Eksploratora. Druga opcja od góry, 'Otwórz program Windows PowerShell', jest otoczona czerwoną ramką."/>

Otworzy się konsola. Możecie w&nbsp;nią, za znakiem `>`, wpisywać różne rzeczy. A&nbsp;komputer będzie je robił.

Jeśli chcemy po prostu zobaczyć, jaki hasz ma plik, to najprościej tam wpisać:

<div class="black-bg mono">Get-FileHash '<span class="red">PLIK</span>'</div>

gdzie zamiast <span class="red">PLIK</span> wpisujemy nazwę naszego pliku. Potwierdzamy, naciskając `Enter`. W&nbsp;moim przypadku wychodzi coś takiego:

{:.figure .bigspace}
<img src="/assets/posts/haszowanie/plik-testowy-hash.webp" alt="Zrzut ekranu PowerShella. Na ciemnoniebieskim tle widać u&nbsp;góry, za strzałką, wpisany tekst 'Get-FileHash plik testowy.txt'. Tekst poniżej zawiera tekst SHA256 pod nagłówkiem 'Algorithm' oraz długi ciąg liter i&nbsp;cyfr pod nagłówkiem 'Hash'."/>

Zobaczymy hasz wraz z&nbsp;dodatkowymi informacjami o&nbsp;użytym algorytmie. Możemy go sobie zaznaczyć i&nbsp;skopiować przez `Ctrl+C`.

Domyślnie Windows używa funkcji SHA256. Ale w&nbsp;naturze często spotykamy też inne wersje, w&nbsp;tym MD5.  
Żeby obliczyć hasz metodą MD5, wystarczy dodać jedną rzecz. Wpisujemy wtedy:

<div class="black-bg mono">Get-FileHash -Algorithm MD5 '<span class="red">PLIK</span>'</div>

{:.figcaption}
Żródło: [Dokumentacja od Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.1).


{% include info.html type="Uwaga" text="Pamiętajcie o&nbsp;pojedynczych cudzysłowach przed i&nbsp;po nazwie pliku. Gdybyście ich nie dali, a&nbsp;w nazwie pliku byłyby jakieś spacje, to wyskoczy błąd." %}

Jeśli natomiast chcemy **porównać hasz pliku z&nbsp;innym haszem, który sami wkleimy**, to używamy komendy:

<div class="black-bg mono">(Get-FileHash '<span class="red">PLIK</span>').Hash -eq '<span class="red">HASH</span>'</div>

{:.figcaption}
Źródło: [odpowiedź ze StackOverflow](https://stackoverflow.com/questions/63396620/how-can-i-compare-a-filess-sha256-hash-in-powershell-to-a-known-value).

Albo, dla MD5:

<div class="black-bg mono">(Get-FileHash -Algorithm MD5 '<span class="red">PLIK</span>').Hash -eq '<span class="red">HASH</span>'</div>

<span class="red">PLIK</span> to ponownie nazwa pliku, którego hasz określamy. A&nbsp;<span class="red">HASH</span> to jakiś inny hasz, który sami wklejamy w&nbsp;PowerShella.

Jeśli plik ma taki sam hasz co ten, który sami podaliśmy, to wyświetli nam napis `True`.

# Jak to zrobić na innych systemach?

Z **OS X (systemem Apple'a)** nie mam doświadczenia, więc muszę polegać na wpisach innych. Według [tego wpisu](https://www.modmy.com/how-verify-file-hashes-macos) musimy otworzyć Terminal (odpowiednik PowerShella), a&nbsp;tam wpisać:

* `shasum -a 256 'PLIK'`, żeby policzyć metodą SHA256;
* `md5 PLIK`, żeby policzyć metodą MD5.

Potem możemy porównać wynik z&nbsp;innym haszem „na oko”.

Brzmi łatwo i&nbsp;przyjemnie. Problem w&nbsp;tym, że podobno trudniej jest otworzyć Terminal w&nbsp;folderze, w&nbsp;którym aktualnie jesteśmy i&nbsp;w którym jest nasz plik. Taką opcję [trzeba specjalnie włączyć](https://www.stugon.com/open-terminal-in-current-folder-location-mac/).

...Albo, jeśli nam się nie chce, można (podobno) przeciągnąć plik do Terminala, żeby wstawiło nam pełną ścieżkę do niego. Wtedy nie ma znaczenia, że Terminal nie otworzył się w&nbsp;tym samym miejscu co plik.

**Linux** pod tym względem jest przyjemniejszy -- a&nbsp;przynajmniej mój Mint, bo ogólnie dystrybucji (tzn. wersji systemu) jest mnóstwo. Wyjaśnię na jego przykładzie, używając angielskich nazw.

Wystarczy w&nbsp;nim przejść do określonego folderu, używając odpowiednika Eksploratora. Potem można kliknąć prawym przyciskiem i&nbsp;wybrać `Open in Terminal`.

Tam wpisujemy:

* `sha256sum PLIK`, żeby policzyło SHA256;
* `md5sum PLIK`, żeby policzyło MD5.

A jeśli chcemy porównać hasze, to [można użyć](https://askubuntu.com/questions/442960/how-to-automate-comparison-of-md5sum-hash-values-for-a-large-number-of-files) takiego zaklęcia: `md5sum -c <<< "HASH *PLIK"`.  
(niestety trzeba pamiętać o&nbsp;trzech strzałkach i&nbsp;cudzysłowach; gdyby w&nbsp;nazwie pliku były spacje, to dodatkowo otaczamy ją cudzysłowami pojedynczymi; gwiazdkę można pominąć, jeśli tworzymy hasz dla pliku tekstowego).

Jeśli hasz się zgadza z&nbsp;tym podanym, to wyświetli nazwę pliku i&nbsp;`OK`.

{% include info.html type="Porada" text="W przypadku Terminala na Linuksie trzeba pamiętać o&nbsp;dodatkowych Shiftach! Kopiujemy tekst przez `Ctrl+Shift+C`, a&nbsp;wklejamy przez `Ctrl+Shift+V`." %}

A teraz czas na praktyczne zastosowania.

# Sprawdzanie programów

Wyobraźmy sobie, że pobraliśmy jakiś program z&nbsp;nieznanej, dość szemranej strony. Albo, jeśli nie wyobrażamy sobie takiej sytuacji, że pobrał go jakiś rodzic/wujek.

Chcemy się upewnić, czy program jest bezpieczny. Przeszukujemy internet i&nbsp;znajdujemy stronę jego twórcy. Wydaje się rzetelna, ocen sporo, pozytywne.

Ale **czy wersja, którą mamy z&nbsp;innego źródła, nie została zmodyfikowana**? Czy to te same programy?

Moglibyśmy dla pewności pobrać program po raz drugi, tym razem z&nbsp;oficjalnej strony. To byłoby rozsądne. Ale załóżmy, że nie wchodzi w&nbsp;grę. Może internet szwankuje i&nbsp;nie chcemy zużywać danych mobilnych? Może link do pobierania na oryginalnej stronie jest nieaktywny?

Czyli zostajemy z&nbsp;treścią strony oryginalnej, programem ze strony niepewnej.  
Jak zweryfikować, czy pobrany program nie jest zawirusowany?

Odpowiedź: patrzymy na stronę autora i&nbsp;wypatrujemy tej samej wersji programu, jaką pobraliśmy z&nbsp;dziwnej strony (np. wersję 2.12 czy coś). Jeśli znajdziemy przy niej tekst w&nbsp;stylu *„MD5 Hash”* albo *„MD5 Checksum”* i&nbsp;długi ciąg znaków, to mamy punkt zaczepienia.

Kopiujemy hasz ze strony. Następnie przechodzimy do folderu z&nbsp;pobranym programem i&nbsp;odpalamy PowerShella.  
Wpisujemy `(Get-FileHash -Algorithm MD5 'PLIK').Hash -eq 'HASH'`, dając nazwę programu zamiast `PLIK` i&nbsp;wklejając skopiowany hasz w&nbsp;miejsce `HASH`.

Jeśli wyświetli nam `True`, to znaczy że program ma ten sam hasz. To ta sama wersja, co z&nbsp;oryginalnej strony! Zatem pozory mylą, szemrana strona nie dodała żadnej niespodzianki od siebie.

...Ale pozostaje jeszcze kwestia zaufania do autora. Może tylko wydaje się miły, ale stworzył szkodliwy program i&nbsp;umieścił u&nbsp;siebie na stronie, skąd inni go skopiowali? Mógł dodać informacje o&nbsp;haszu, żeby robić bardziej profesjonalne wrażenie.

Pamiętajmy: **hasz nic nie mówi o&nbsp;tym, czy źródło jest wiarygodne. Mówi tylko, czy dwie rzeczy są takie same**.

Hasz byłby taki sam dla dwóch identycznych, prawilnych programów. Ale byłby też taki sam dla dwóch identycznych wirusów. To tak ku przestrodze.

# Przekazywanie wiadomości „na raty”

Haszy możecie też użyć, żeby **przekazać pewną informację bez ujawnienia od razu jej treści**. Na przykład w&nbsp;celu asekuracji (czyli, mówiąc potocznie, jako dupochronu).

Powiedzmy, że macie przeczucia co do jakiejś sprawy z&nbsp;życia, która może rypnąć. Dowolnej. Na przykład wierzycie, że Żwirek spiskuje przeciw Muchomorkowi.

Z jednej strony nie chcecie mówić o&nbsp;tym wprost, na wypadek gdyby te przeczucia jednak były mylne. Gra Pascala i&nbsp;te sprawy.

Z drugiej -- jeśli przyznacie się dopiero po fakcie, że to przeczuwaliście, to nie zostaniecie wzięci na serio. Nie chcecie też słać anonimów i&nbsp;potem przekonywać, że były od was.

Jak to rozwiązać?

Odpowiedź: zapisujecie swoje przeczucia w&nbsp;jakimś pliku tekstowym. Robicie `Get-FileHash 'WASZ_PLIK'`, żeby uzyskać jego hasz.

Plik tekstowy odkładacie w&nbsp;bezpieczne miejsce i&nbsp;**pod żadnym pozorem go nie zmieniacie. Ani spacji**.

Natomiast **sam hasz kopiujecie i&nbsp;wysyłacie** osobom, których dotyczy sytuacja. Zapewne zbierając szereg reakcji „WTF”, ale co tam.

Jeśli Wasze przewidywania okażą się błędne, to możecie nigdy nie wracać do sprawy tego dziwnego tekstu, który wysłaliście.  
Jeśli natomiast były słuszne, to dosyłacie też oryginalny plik. I&nbsp;pokazujecie, że odpalenie na nim `Get-FileHash` daje dokładnie ten sam hasz, który wysłaliście wcześniej.

Wniosek: przemyślenia opisane w&nbsp;pliku mieliście jeszcze przed całym zajściem. Wiedzieliście, co się kroi.

{% include info.html type="Ciekawostka" text="Niedawno taką metodę zastosowały trzy znane portale o&nbsp;cyberbezpieczeństwie: Niebezpiecznik, Zaufana Trzecia Strona oraz Informatyk Zakładowy.  
Wiedzieli, że mogą pojawić się przeciw nim oskarżenia, które chcieli od razu zdementować.  
20 lutego każda z tych stron wrzuciła na swoje konto społecznościowe [sam hasz](https://www.facebook.com/niebezpiecznik/posts/10157705388896821).  
A 2&nbsp;marca [pełną treść oświadczenia](https://www.facebook.com/niebezpiecznik/posts/10157729024811821)." %}

Wadą rozwiązania jest to, że inni muszą mieć przynajmniej podstawowe pojęcie o&nbsp;haszach (a przynajmniej wiedzieć, że są nie do podrobienia). *Drugą wadą*{:.corr-del}Zaletą to, że zapewne zostaniecie uznani za nerdów.

I z&nbsp;tymi nerdowskimi metodami Was zostawiam. Miłego haszowania i&nbsp;do zobaczenia przy kolejnych wpisach! :smile:
