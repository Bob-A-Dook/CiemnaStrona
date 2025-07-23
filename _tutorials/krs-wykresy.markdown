---
layout: page
title: Tworzenie wykresów dla danych z KRS-u
description: "Używamy skryptów do zwizualizowania zmian zachodzących w firmach."
---

{:.post-meta .bigspace-after}
Rym w tytule samouczka niezamierzony.

Ten samouczek to instrukcja pracy z&nbsp;moim skryptem Pythona, pozwalającym tworzyć wykresy i&nbsp;grafy powiązań dla odpisów z&nbsp;Krajowego Rejestru Sądowego. 

**Aktualizacja 15.02.2022&nbsp;r.:** Dodałem do skryptu możliwość tworzenia grafów powiązań między firmami. Jeśli chcecie z&nbsp;niej skorzystać, zachęcam do pobrania nowej wersji skryptu.

**Aktualizacja 18.02.2022&nbsp;r.:** Poprawiłem parę błędów, komfort użytkowania przy odpalaniu skryptu przez podwójne kliknięcie, dodałem możliwość układania grafów od lewej do prawej.

Linki do różnych wersji skryptu:

* <a href="/assets/skrypty/krs_visualizer/v2/krs_visualizer.py">wersja najnowsza</a>{:.internal}
  (oprócz osi czasu jest w stanie tworzyć również grafy powiązań)
* <a href="/assets/skrypty/krs_visualizer/v1/krs_visualizer.py">pierwsza wersja</a>{:.internal}

Zachęcam, żeby zawsze korzystać z najnowszej :smile:

## Wymagania

Zanim zaczniemy cokolwiek robić, [pobieramy Pythona z oficjalnej strony](https://www.python.org/downloads/). Instalując go, pamiętamy -- przynajmniej na Windowsie -- żeby zaznaczyć opcję zainstalowania dodatków: *pip* i *IDLE*.

{:.post-meta}
Pierwsze kroki z Pythonem opisałem <a class="internal" href="{{site.url}}/tutorials/using-python">w&nbsp;osobnym samouczku</a>. Zachęcam zainteresowanych do lektury.

# Moduły Pythona

Skrypt potrzebuje do działania trzech zewnętrznych modułów. Dlatego najpierw włączamy naszą zaufaną konsolę  
(jak *PowerShell* w&nbsp;przypadku Windowsa; można go znaleźć w menu *Start* albo nacisnąć `Przycisk z ikoną Windowsa`+`X`, a potem `I` jak *inwigilacja*).

Następnie pobieramy co trzeba:

1. Biblioteki `BeautifulSoup` oraz `lxml` do grzebania w&nbsp;XML-u.  
   Instalujemy je, wpisując w&nbsp;konsolce i potwierdzając *Enterem*:

   <div class="black-bg mono">pip install beautifulsoup4</div>

   A&nbsp;także:

   <div class="black-bg mono">pip install lxml</div>

2. Bibliotekę `Matplotlib` do tworzenia wykresów.

   **Ważne!** Kiedy testowałem skrypt na Windowsie 10, nowsza wersja nie działała. Zgodnie z&nbsp;[pewną odpowiedzią z forum](https://stackoverflow.com/questions/66919838/matplotlib-wont-run-on-windows-10-dll-fails-to-load) pomaga zainstalowanie nieco starszej, *3.3.1*. Dlatego na Windowsie wpisujemy:

   <div class="black-bg mono">pip install matplotlib==3.3.1</div>  
   
   A&nbsp;na innych systemach operacyjnych możemy zamiast tego brać najnowszą:

   <div class="black-bg mono">pip install matplotlib</div>

# Poppler

Poppler to biblioteka służąca do pracy z plikami PDF. Mój skrypt wykorzystuje ją do wyciągania z nich tekstu.  
Nie jest to niestety moduł Pythona, tylko rzecz napisana w&nbsp;innym języku, więc jej pobranie wymaga paru dodatkowych kroków. Ale łatwych, więc bez obaw :smile: 

* **Na Windowsie**:

  Pobieracie ZIP-a z&nbsp;przygotowanymi plikami [z tej strony](https://github.com/oschwartz10612/poppler-windows/releases/download/v21.10.0-0/Release-21.10.0-0.zip) i&nbsp;go rozpakowujecie w&nbsp;tym samym folderze, w&nbsp;którym trzymacie skrypt.

{:.post-meta}
Da się też zainstalować Popplera w&nbsp;miejscu, w&nbsp;którym będzie łatwiej dostępny dla innych programów. Ale to już zostawiam chętnym.

{% include info.html type="Uwaga" text="Gdyby podczas odpalania skryptu wyświetlało Wam komunikat o&nbsp;brakującym pliku *MSVCP140.dll*, to go pobieracie [z oficjalnej strony Microsoftu](https://aka.ms/vs/17/release/vc_redist.x64.exe), klikacie i&nbsp;instalujecie (podlinkowałem wersję 64-bitową, bo zapewne taki macie system).  
Windows to jednak lubi rzucać kłody pod nogi :roll_eyes:"%}

* **Na Linuksie**:

  Postępujecie zgodnie z&nbsp;instrukcjami [z tej odpowiedzi](https://stackoverflow.com/questions/32156047/how-to-install-poppler-in-ubuntu-15-04).  
  Cytując je (na wypadek gdyby link padł), wpisujecie w konsolę:

  <div class="black-bg mono">sudo apt-get install -y poppler-utils</div>

* **Na OSX (komputery Apple)**:

  Nie sprawdzałem, ale podobno w&nbsp;oficjalnych źródłach ma [elegancko przygotowanego Popplera](https://macappstore.org/poppler/). Pobieracie go i&nbsp;instalujecie.

Kiedy już macie wszystkie potrzebne moduły, skrypt oraz PDF-y w&nbsp;jednym miejscu, to możecie produkować wykresy do woli.

# Graphviz / dot

**(opcjonalny; tylko wtedy, jeśli chcemy rysować grafy powiązań między firmami).**

Instrukcje instalacji znajdziemy [na oficjalnej stronie](http://www.graphviz.org/download/).

## Instrukcje korzystania

W najprostszym przypadku po prostu odpalacie skrypt, zdając się na domyślne ustawienia -- na przykład otwierając go w&nbsp;domyślnym edytorze IDLE i&nbsp;naciskając `F5`. Albo w&nbsp;dowolny inny sposób.

**Na samym końcu skryptu znajdziecie parę ustawień**, które możecie zmienić, żeby dostosować swoje wykresy i grafy.

Gdybyście coś zmienili w&nbsp;domyślnych ustawieniach i&nbsp;wyskakiwałby Wam błąd (zapewne gatunku `SyntaxError`), to znaczy że omyłkowo usunęliście jakieś ważne znaki albo spacje.  
W takim wypadku najlepiej pobierzcie mój skrypt od nowa, a&nbsp;zmiany tym razem wprowadzajcie bardzo ostrożnie.

# Tworzenie wykresów

Skrypt za każdym razem wrzuca pliki z&nbsp;wykresami do folderu `Wykresy`, w&nbsp;formacie obrazków JPG (po jednym dla każdego odpisu).

Aby zmienić domyślne ustawienia, ustawiacie inne wartości zmiennych na końcu skryptu (oznaczone odpowiednimi komentarzami).

Pierwszą z&nbsp;tych zmiennych jest folder, w&nbsp;którym skrypt wypatruje plików PDF z&nbsp;KRS-u. Jeśli nic tam nie wpiszecie, będzie szukał w&nbsp;tym samym folderze, w&nbsp;którym go odpalacie:

```python
folder = ""
```

Jeśli natomiast wpiszecie między cudzysłowami nazwę jakiegoś konkretnego folderu (albo wkleicie całą ścieżkę do niego), to skrypt poszuka plików z&nbsp;odpisami właśnie tam.

Kolejne z&nbsp;ustawień to kategorie, dla których skrypt stworzy wykresy. Domyślnie macie:

```python
info = ['nazwa','adres','zarząd','wspólnicy']
```

Nie możecie dopisać własnych zmyślonych nazw kategorii, musicie wybierać spośród tych czterech. Ale możecie zmieniać ich kolejność albo usuwać dowolne z&nbsp;nich.  
Przykładowo, wpisując <span class="black-bg mono">info=[\'adres\',\'wspólnicy\']</span>, otrzymacie wykres jedynie dla zmian adresu i&nbsp;wspólników/udziałowców.

Ostatnie z&nbsp;ustawień to wymiary wykresu:

```python
width, height = 9, 20
```

Liczba `9` odnosi się tu do szerokości, a&nbsp;`20` do wysokości. To wymiary w&nbsp;calach.  
W&nbsp;praktyce możecie je sobie dowolnie zmieniać, gdyby wykres był nieczytelny, a&nbsp;etykiety na siebie nachodziły (taki problem pojawia się zwłaszcza przy spółkach, w&nbsp;których dużo się dzieje).

Po wprowadzeniu takiej zmiany odpalamy ponownie skrypt i&nbsp;możemy się cieszyć wykresem w&nbsp;nowych wymiarach.

# Tworzenie grafów powiązań

W najnowszej wersji skryptu ta opcja jest domyślnie włączona. Więc **po prostu odpalacie skrypt**, a w osobnym folderze `Grafy` powinny pojawić się dwa pliki:

* Plik SVG z grafem powiązań;
* Plik GV.  
  (Bardziej zaawansowani użytkownicy mogą go edytować, żeby na przykład wyróżnić niektóre połączenia, zakryć część danych itp. Po edycji trzeba własnoręcznie użyć na pliku programu `dot`, żeby otrzymać zmieniony graf).

Jeśli chcecie zmienić domyślne ustawienia, to w&nbsp;przypadku grafów macie następujące zmienne:

```python
ONLY_GRAPH_KRS_COMPANIES = False
```

Przy tym ustawieniu na Waszym grafie będą widoczne wszystkie powiązania; również ze spółkami oraz osobami prywatnymi, dla których nie macie odpisów. Takie powiązania **będą oznaczone czerwonawym kolorem**.

Uwaga: skrypt na razie nie jest w&nbsp;stanie odróżnić firm od osób fizycznych.

Jeśli chcecie wyświetlić jedynie powiązania dla tych firm, dla których macie odpisy, to zmieniacie wartość z&nbsp;`False` na `True`.

```python
ARRANGE_GRAPH_LEFT_TO_RIGHT = False
```

Graf domyślnie jest układany od góry do dołu. Jednak czasami jest to nieczytelne i wymaga przewijania ekranu w bok (zwłaszcza gdy mamy „płytką strukturę” z wieloma udziałowcami na pierwszym szczeblu).

W takiej sytuacji zmieniamy wartość z `False` na `True` i&nbsp;odpalamy skrypt ponownie. Powinno być czytelniej.

# Opcje zaawansowane

Użytkownicy zaawansowani i&nbsp;umiejący w Pythona mogą, począwszy od drugiej wersji skryptu, dodawać własne funkcje modyfikujące dane przed wizualizacją:

```python
pre_graph_transform = None
pre_timeline_transform = None
```

`pre_timeline_transform` z&nbsp;założenia działa na danych, z&nbsp;których stworzymy wykresy, a&nbsp;`pre_graph_transform` -- na tych, z&nbsp;których powstają grafy.  
Każdy z nich pracuje na kopii danych, tuż przed wizualizacją, i&nbsp;nie zmienia ich na stałe.

Filtry są przydatne, jeśli chcemy coś zmienić w&nbsp;danych tuż przed wizualizacją -- na przykład zamaskować niektóre nazwiska, odfiltrować część informacji itp.

Tworząc filtry, pamiętajcie:

* Na wejściu macie listę krotek z danymi o&nbsp;firmach (zmienna `companies`);
* Każda krotka ma postać `(krs_id, name, last_date, events)` -- kolejno numer KRS firmy, jej aktualną nazwę, najpóźniejszą znaną nam datę oraz listę zdarzeń z jej „życia”. Każde ze zdarzeń to klasa `KrsEvent`, więc to jej się przyjrzyjcie w razie potrzeby.
* Na wyjściu Wasza funkcja również powinna zwracać listę 4-elementowych krotek, tylko że odpowiednio zmodyfikowaną.

Jeśli chcecie zobaczyć przykład filtra, możecie spojrzeć na moją funkcję `replace_names_with_original`, obecną w skrypcie.  
Domyślnie nie jest używana, ale skorzystałem z niej, tworząc wpis na bloga. Robi z danymi następujące rzeczy:

* Zmienia nazwę firmy (środkowe pole każdej krotki), biorąc z listy zdarzeń nazwę najstarszą.
* Skraca tę nazwę, a także nazwy wszystkich innych firm/wspólników ze zdarzeń, usuwając z nich tekst w stylu `SP. Z O.O.`.

## Ograniczenia

Skrypt do tej pory mi działał, ale na pewno istnieją pliki, z&nbsp;którymi gorzej sobie poradzi. Najlepiej go używać do wstępnego wyłapania ciekawych rzeczy, a&nbsp;potem je weryfikować, zaglądając prosto do PDF-a z&nbsp;odpisem.

No i, na koniec, pamiętajmy że mamy również pewne ograniczenia związane nie tylko ze skryptem, lecz z&nbsp;KRS-em jako takim:

* Nie będzie nam pokazywało wspólników/udziałowców w&nbsp;przypadku niektórych spółek (na przykład akcyjnych, bo tam akcjonariusze często się zmieniają i&nbsp;może ich być bardzo wielu).
* Nawet jeśli mamy ładną spółkę z&nbsp;o.o., to według tego [wpisu o&nbsp;anonimowych spółkach](http://www.lflegal.pl/blog/spolka-anonimowa-jak-ukryc-w-spolnika-w-spolce/) KRS nie udostępnia listy wspólników mających poniżej 5% udziałów.
* Odpisy z KRS-u nie nadają się do wyłapywania wszystkich powiązań danej firmy, ponieważ pokazują tylko jedną stronę relacji (tzn. kto był w danej firmie udziałowcem; nie widzimy natomiast, czy ta firma była udziałowcem w&nbsp;czymś innym).

Miłego wyłapywania firmowych ciekawostek!
