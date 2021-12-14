---
layout: page
title: Tworzenie wykresów dla danych z KRS-u
description: "Używamy skryptów do zwizualizowania zmian zachodzących w firmach."
---

Ten samouczek to instrukcja pracy z&nbsp;moim skryptem Pythona do tworzenia wykresów dla odpisów z KRS-u (rym niezamierzony).

Sam skrypt można pobrać <a href="/assets/skrypty/krs_visualizer.py" download>stąd</a>{:.internal}.

## Wymagania

# Moduły Pythona

Skrypt potrzebuje do działania trzech zewnętrznych modułów. Dlatego włączamy naszą zaufaną konsolę (jak *PowerShell* w&nbsp;przypadku Windowsa) i&nbsp;instalujemy co trzeba:

1. Biblioteki `BeautifulSoup` oraz `lxml` do grzebania w&nbsp;XML-u.  
   Instalujemy je, wpisując w&nbsp;konsolce:

   <div class="black-bg mono">pip install beautifulsoup4</div>

   A&nbsp;także:

   <div class="black-bg mono">pip install lxml</div>

2. Bibliotekę `Matplotlib` do tworzenia wykresów.

   **Ważne!** Kiedy testowałem skrypt na Windowsie 10, nowsza wersja nie działała. Zgodnie z&nbsp;[pewną odpowiedzią z forum](https://stackoverflow.com/questions/66919838/matplotlib-wont-run-on-windows-10-dll-fails-to-load) pomaga zainstalowanie nieco starszej, *3.3.1*.

   <div class="black-bg mono">pip install matplotlib==3.3.1</div>  
   
   A&nbsp;na innych systemach operacyjnych możemy zamiast tego brać najnowszą:

   <div class="black-bg mono">pip install matplotlib</div>

# Poppler

Poppler to biblioteka służąca do pracy z plikami PDF. Mój skrypt wykorzystuje ją do wyciągania z nich tekstu.  
Nie jest to niestety moduł Pythona, tylko rzecz napisana w&nbsp;innym języku, więc jej pobranie wymaga paru dodatkowych kroków. Ale łatwych, więc bez obaw :smile: 

* **Na Windowsie**:

  Pobieracie ZIP-a z&nbsp;przygotowanymi plikami [z tej strony](https://github.com/oschwartz10612/poppler-windows/releases/download/v21.10.0-0/Release-21.10.0-0.zip) i&nbsp;go rozpakowujecie w&nbsp;tym samym folderze, w&nbsp;którym trzymacie skrypt.  
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

## Instrukcje korzystania

Skrypt może tworzyć wykresy dla czterech kategorii:

* nazwa spółki;
* adres;
* zarząd;
* wspólnicy (albo inni udziałowcy).

W najprostszym przypadku po prostu go odpalacie -- na przykład otwierając go w domyślnym edytorze IDLE i naciskając `F5`, albo w dowolny inny sposób.

**Na samym końcu skryptu znajdziecie parę ustawień**, które możecie zmienić, żeby dostosować swoje wykresy.

Pierwszym z&nbsp;nich jest folder, w&nbsp;którym skrypt wypatruje plików PDF z&nbsp;KRS-u. Jeśli nic tam nie wpiszecie, będzie patrzył w&nbsp;tym samym folderze, w&nbsp;którym go odpalacie:

```python
folder = ""
```

Jeśli natomiast wpiszecie między cudzysłowami nazwę jakiegoś konkretnego folderu (albo wkleicie całą ścieżkę do niego), to skrypt poszuka plików z&nbsp;odpisami właśnie tam.

Kolejne z&nbsp;ustawień to kategorie, dla których skrypt stworzy wykresy. Domyślnie macie:

```python
info = ['nazwa','adres','zarząd','wspólnicy']
```

Nie możecie dopisać własnych zmyślonych nazw kategorii, musicie wybierać spośród tych czterech. Ale możecie zmieniać ich kolejność albo usuwać dowolne z&nbsp;nich.  
Przykładowo, wpisując `info=['adres','wspólnicy']`, otrzymacie wykres jedynie dla zmian adresu i&nbsp;wspólników/udziałowców.

Ostatnie z&nbsp;ustawień to wymiary wykresu:

```python
width, height = 9, 20
```

Liczba `9` odnosi się tu do szerokości, a&nbsp;`20` do wysokości. To wymiary w&nbsp;calach. W&nbsp;praktyce możecie je sobie dowolnie zmieniać, gdyby wykres był nieczytelny, a&nbsp;etykiety na siebie nachodziły (taki problem pojawia się zwłaszcza przy spółkach, w&nbsp;których dużo się dzieje).

Po wprowadzeniu takiej zmiany odpalamy ponownie skrypt i&nbsp;możemy się cieszyć wykresem w&nbsp;nowych wymiarach.

Gdybyście coś zmienili w&nbsp;domyślnych ustawieniach i&nbsp;wyskakiwałby Wam błąd (zapewne gatunku `SyntaxError`), to znaczy że omyłkowo usunęliście jakieś ważne znaki albo spacje.  
W takim wypadku najlepiej pobierzcie mój skrypt od nowa, a&nbsp;zmiany tym razem wprowadzajcie bardzo ostrożnie.

## Ograniczenia

Skrypt do tej pory mi działał, ale na pewno istnieją pliki, z&nbsp;którymi gorzej sobie poradzi. Najlepiej go używać do wstępnego wyłapania ciekawych rzeczy, a&nbsp;potem je weryfikować, zaglądając prosto do PDF-a z&nbsp;odpisem.

No i, na koniec, pamiętajmy że mamy również pewne ograniczenia związane nie tylko ze skryptem, lecz z&nbsp;KRS-em jako takim:

* Nie będzie nam pokazywało wspólników w&nbsp;przypadku niektórych spółek (na przykład akcyjnych, bo tam akcjonariusze często się zmieniają i&nbsp;może ich być bardzo wielu).
* Nawet jeśli mamy ładną spółkę z&nbsp;o.o., to według tego [wpisu o&nbsp;anonimowych spółkach](http://www.lflegal.pl/blog/spolka-anonimowa-jak-ukryc-w-spolnika-w-spolce/) KRS nie udostępnia listy wspólników mających poniżej 5% udziałów.
* Odpisy z KRS-u nie nadają się do wyłapywania wszystkich powiązań danej firmy, ponieważ pokazują tylko jedną stronę relacji (tzn. kto był w danej firmie udziałowcem; nie widzimy natomiast, czy ta firma była udziałowcem w czymś innym).
