---
layout: page
title: Praca z aplikacją Termux
description: "Robimy z telefonu narzędzie pracy."
---

To nie tyle spójny samouczek, co zbiór luźnych informacji na temat Termuksa -- aplikacji na Androida dającej możliwość korzystania z&nbsp;konsoli i&nbsp;skryptów na naszym własnym telefonie.

Wymienione tu porady i&nbsp;problemy są dość uniwersalne, więc nie chciałem ich powtarzać w&nbsp;każdym jednym wpisie i&nbsp;zebrałem je tutaj. Będę do nich odsyłał z&nbsp;innych wpisów.

## Python

### Instalacja

Gdy już mamy Termuksa, instalowanie Pythona powinno być bardzo proste. Wpisujemy w&nbsp;konsolę:

<div class="bigspace black-bg mono">pkg install python</div>

Natomiast może się zdarzyć, że wyskoczy nam błąd związany z&nbsp;brakującym repozytorium. To nic strasznego. Zapraszam do części [„Rozwiązywanie problemów”](#instalowanie-przez-pkg-nie-działa){:.internal}.

### LXML

Biblioteka do sprawnej pracy z&nbsp;formatem XML. **Wiele moich skryptów jej nie potrzebuje**.

Do tej pory starałem się unikać jej oraz innych modułów opartych na innych językach niż Python. Ale stopniowo zaczynam poruszać na blogu kwestie przetwarzania bardziej złożonych plików, jak kod źródłowy dużych portali społecznościowych. Powoli staje się potrzebna.

Przede wszystkim zaktualizujmy swoje biblioteki do najnowszej wersji, żeby nie było między nimi rozbieżności. Wpisujemy w Termuksa:

<div class="black-bg mono">
pkg upgrade
</div>

{% include info.html
type="Porada"
text="Gdyby wyskoczył komunikat o&nbsp;niedziałającym repozytorium, w&nbsp;tym momencie albo po innym użyciu komendy `pkg`, to <a href='#instalowanie-przez-pkg-nie-działa'>rozwiązanie jest dość proste</a>{:.internal}."
%}

Poza tym potrzebujemy *kompilatora* -- czegoś w&nbsp;rodzaju robota kuchennego, który pozwoli nam połączyć zgromadzone składniki w&nbsp;fajnego LXML&#8209;a. Dobrym rozwiązaniem dla Androida jest Clang, ważący na dzień 19&nbsp;grudnia 62&nbsp;MB.

<div class="bigspace black-bg mono">
pkg install clang
</div>

To teraz potrzebujemy jeszcze składników -- [kilku bibliotek](https://github.com/termux/termux-packages/issues/3793):

<div class="bigspace black-bg mono">
pkg install libxml2 libxslt libiconv
</div>

Na Termuksie ważne, żeby to były właśnie te; wiele internetowych instrukcji odnosi się do zwykłego Linuksa i&nbsp;wspomina o&nbsp;wersjach z&nbsp;przyrostkiem *-dev*. Ale w&nbsp;bazach Termuksa ich po prostu nie mają, są inne.  
Wpisujemy komendę i potwierdzamy. 

Kiedy już mamy u&nbsp;siebie Clanga, trzy potrzebne biblioteki oraz samego Pythona, możemy się pokusić o&nbsp;zainstalowanie LXML-a. Najprościej byłoby wpisać:

<div class="bigspace black-bg mono">
pip install lxml
</div>

**Ale uwaga**! W&nbsp;przypadku LXML-a po wyświetleniu *building wheel for LXML* zacznie się kompilacja, która długo potrwa, nawet całe godziny. Możemy na ten czas zostawić Termuksa.

Nie mamy cierpliwości? Możemy również wybrać opcję mniej zoptymalizowaną, ale szybszą. W&nbsp;tym celu wpisujemy:

<div class="bigspace black-bg mono">
CFLAGS='-O0' pip install lxml
</div>

Komenda `CFLAGS` oznacza, że chcemy szybkie przerobienie programu, kosztem ewentualnego nieco wolniejszego działania. Ale większej różnicy nam to nie zrobi.  
Pierwsza litera w&nbsp;wartości to O&nbsp;jak *optymalizacja*, zaś druga to zero.

Gdyby na tym etapie wyświetliło nam długi błąd, zawierający fragment:

{:.bigspace}
> command 'arm-linux-androideabi-clang' failed with exit status 1

...To znaczy że nie mamy u&nbsp;siebie Clanga. Instalujemy go jak wyżej.

{:.post-meta}
Wiele informacji z&nbsp;tej części zdobyłem dzięki [dyskusji](https://github.com/neovim/pynvim/issues/267) z&nbsp;wątku dotyczącego programu Neovim. Dziękuję jej uczestnikom!

## Rozwiązywanie problemów

### Instalowanie przez pkg nie działa

Sam Termux niewiele nam daje bez dodatkowych modułów i&nbsp;bibliotek. Możemy je łatwo instalować, wpisując komendę `pkg install`. Ale co zrobić, kiedy tak podstawowa funkcja nam nie działa?

Po wpisaniu pewnej takiej komendy wyskoczył mi długi błąd, którego główne przesłanie znalazłem na końcu:

{:.bigspace}
> Possible cause: repository is under maintenance or down

Z czego to wynika? Otóż Termux ma u&nbsp;siebie ustalony adres jakiegoś serwera (repozytorium), do którego zwraca się z&nbsp;prośbami o&nbsp;pobranie dodatkowych rzeczy. I&nbsp;niestety **jego dawny serwer -- Bintray -- został wyłączony**. Stąd komunikat o&nbsp;błędzie.

Nie jest to wielki problem, bo można ustawić w&nbsp;Termuksie, żeby brał pliki od kogoś innego. Wydaje mi się, że nowsze wersje Termuksa to naprawiły.  
Tym niemniej przez pewien czas, z&nbsp;punktu widzenia nowych użytkowników, Termux oznaczał dziwne, długie komunikaty o&nbsp;błędach i&nbsp;słabe pierwsze wrażenie. A&nbsp;szkoda.

A jak to zmienić na coś działającego? Bardzo prosto. Wpisujemy komendę:

<div class="bigspace black-bg mono">
termux-change-repo
</div>

Potwierdzamy. Wyświetli się ekran w&nbsp;stylu retro, pozwalający nam najpierw wybrać repozytorium, któremu chcemy zmienić źródło.

Po ekranie poruszamy się strzałkami. Spacją zaznaczamy. A&nbsp;klawiszem potwierdzającym (po prawej stronie naszej klawiaturze ekranowej) -- potwierdzamy swój wybór. To ważne, żeby **najpierw zaznaczyć, a&nbsp;potem potwierdzić**. Inaczej wybralibyśmy zawsze pierwszą opcję.

{% include info.html
type="Uwaga"
text="Poniższe instrukcje odnoszą się do wersji Termuksa, którą miałem u&nbsp;siebie, dlatego piszę w&nbsp;pierwszej osobie. Możliwe, że wersja bardziej współczesna dla czytelników zawiera coś innego."
%}

Domyślnie pierwszy ekran zawierał u&nbsp;mnie trzy kategorie -- repozytorium główne, *Science* oraz *Games*. Wszystkim trzeba było ustawić nowe, działające źródło.

Inną opcją było [usunięcie osobnych repozytoriów od gier i&nbsp;nauki](https://stackoverflow.com/a/73310761); osobiście uznałem, że ich nie potrzebuję. Wystarczyły dwie proste komendy:

<div class="bigspace black-bg mono">
pkg remove game-repo -y<br/>
pkg remove science-repo -y
</div>

Kiedy miałem już tylko jeden rodzaj repozytorium, pozostała zmiana źródła. Zmieniłem opcję domyślną, Bintraya, na coś innego. Tamtego dnia działał mi *Albatross*, więc to jego ustawiłem jako źródło. Ale ogólnie, gdyby któreś nie działało, można po prostu wybrać coś innego z&nbsp;listy.

Po wprowadzeniu zmiany zaczęły działać komendy instalujące różne rzeczy przez `pkg`. 

