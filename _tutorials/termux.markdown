---
layout: page
title: Praca z aplikacją Termux
description: "Robimy z telefonu narzędzie pracy."
---

{:.figure .bigspace-after}
<img src="/assets/tutorials/termux/termux-ciemna-edit.jpg" alt="Zrzut ekranu pokazujący nazwę programu Termux, w&nbsp;formie ascii art, wewnątrz konsoli tego programu. Pod spodem widać dopisek 'Ukłony od ciemnastrona.com.pl' i&nbsp;uśmiechniętą emotkę"/>

To nie tyle spójny samouczek, co zbiór luźnych informacji na temat Termuksa -- aplikacji na Androida dającej możliwość korzystania z&nbsp;konsoli i&nbsp;skryptów na naszym własnym telefonie.

Wymienione tu porady i&nbsp;problemy są dość uniwersalne, więc nie chciałem ich powtarzać w&nbsp;każdym jednym wpisie i&nbsp;zebrałem je tutaj. Będę do nich odsyłał z&nbsp;innych wpisów.

## Instalacja

Zanim przejdę do instalacji, dwie kluczowe rzeczy:

1. Instrukcja dotyczy **wyłącznie telefonów z&nbsp;systemem Android**.

   To system docelowy dla Termuksa. Być może powstały jakieś wersje dla systemu iOS albo bardziej niszowych, alternatywnych systemów (jak mobilny Linux), ale nie miałem z&nbsp;nimi styczności.

2. Google jest niedobrym monopolistą ([już oficjalnie](/google/2024/08/07/google-antymonopol-wyrok){:.internal}).

   Są też właścicielami Play Store'a -- oficjalnej i&nbsp;najpopularniejszej bazy z&nbsp;aplikacjami na Androida. Naszego Termuksa [potraktowali niesprawiedliwie](https://github.com/termux-play-store), zakazując mu dodawania niektórych funkcji, bardzo przydatnych dla majsterkujących użytkowników.

Ze względu na punkt drugi **apka Termux dostępna przez Play Store jest wybrakowana**.  
Jasne, można jej użyć, jeśli chcemy tylko poćwiczyć w&nbsp;podróży korzystanie z&nbsp;programów konsolowych. Ale gdybyśmy chcieli skorzystać z&nbsp;pełni możliwości telefonu, mocno polecam pobranie wersji z&nbsp;innego źródła niż Play Store.

### F-Droid na ratunek

„Inne źródło niż Play Store”? W&nbsp;porządku. Ale przydałoby się, żeby to źródło nie zaserwowało nam jakiejś apki z&nbsp;wirusami, która wykradnie nasze tajemnice z&nbsp;telefonu.

Takim źródłem jest F-Droid -- baza przechowująca aplikacje *open source*.  
Jest to źródło dość popularne i&nbsp;wiele osób ma je na oku, więc szybko by wyszło na jaw, gdyby ktoś próbował czegoś szemranego.

Instalacja *prawdziwego* Termuksa w&nbsp;takim wypadku przebiega następująco:

1. Najpierw pobieramy apkę F-Droid [z&nbsp;oficjalnego źródła](https://f-droid.org/).
2. Następnie ją uruchamiamy i&nbsp;znajdujemy przez wyszukiwarkę apkę Termux. Instalujemy.
3. Na koniec instalujemy, również przez F-Droida, `Termux:API`.

   To funkcje rozszerzające Termuksa. Pozwalają mu między innymi uzyskać dostęp do schowka, mikrofonu, czujników telefonu -- oczywiście tylko wtedy, kiedy wyrazimy zgodę.

Kiedy już zrobimy te trzy rzeczy, świat Termuksa stanie przed nami otworem :smile:

## Możliwości i&nbsp;ograniczenia

Co można robić, mając Termuksa?  
Wszystkich zastosowań nie wymienię, bo są niezliczone! Jak dotąd opisałem na blogu:

* [walkę z&nbsp;trollami]({% post_url 2022-04-15-trolle-rosja-ukraina %}){:.internal} (kopiowanie danych ze schowka + ich obróbka + otwieranie strony w&nbsp;domyślnej przeglądarce),
* [chowanie plików]({% post_url 2022-11-16-apki-pliki %}#bonus-ukrywanie-plików-przez-termuksa){:.internal} poza zasięgiem innych (niesystemowych) aplikacji,
* robienie prowizorycznego [backupu swoich SMS-ów]({% post_url 2022-12-02-apki-historia-sms %}){:.internal},
* pobieranie filmików i&nbsp;muzyki z&nbsp;użyciem [yt-dlp](/tutorials/yt-dlp-android){:.internal}.

A będzie tego więcej :wink:

Poza tym, ogólniej: można korzystać z&nbsp;wielu przydatnych programów konsolowych znanych z&nbsp;systemu Linux.  
Wiele fajnych samouczków można znaleźć w&nbsp;sieci pod hasłem `bash tutorial`. Choć nie były tworzone z&nbsp;myślą o&nbsp;Termuksie, nieraz zadziałają również na nim.

Mało? Można zainstalować więcej programów z&nbsp;oficjalnej bazy. Dostępny jest chociażby język programowania Python, wraz z&nbsp;wieloma stworzonymi w&nbsp;nim pakietami (jak chociażby Matplotlib od wizualizacji danych).

A gdyby ktoś jeszcze czuł niedosyt, to po zainstalowaniu `Termux:API` zyska dostęp do programów zintegrowanych z&nbsp;funkcjami smartfona. Warto poznać ich [oficjalną listę](https://wiki.termux.com/wiki/Termux:API).

### Ograniczenia

Termux wygląda jak konsola, a&nbsp;na systemach Linux i&nbsp;Windows konsola jest niejako uprzywilejowana. Z&nbsp;tego względu można zapomnieć o&nbsp;kluczowym fakcie -- **Termux na Androidzie jest zaledwie szeregową aplikacją, jedną spośród wielu**. Nie jest ani trochę bliżej systemu niż jakieś Spotify, Duolingo czy Flo.

Z tego względu nie jest w&nbsp;stanie zaglądać do wewnętrznych plików systemu ani do innych aplikacji. Nie zadziałają na nim przykładowo:

* komendy ingerujące w&nbsp;ruch internetowy,
* komendy zawierające `sudo` (działanie w&nbsp;trybie administratora),
* programy zaglądające do plików innych programów  
  (jak choćby mój drobny [skrypt]({% post_url 2021-12-24-caching %}#bonus-skrypt-do-grzebania-wpamięci-podręcznej){:.internal} od grzebania w&nbsp;pamięci podręcznej przeglądarki).

Większe możliwości -- również wewnątrz Termuksa -- można zyskać poprzez *zrootowanie* swojego telefonu.

{% include details.html summary="Rootowanie telefonu (dla chętnych i&nbsp;bardziej zaawansowanych)" %}

{:.bigspace-before}
Rootowanie polega z&nbsp;grubsza na uzyskaniu na smartfonie z&nbsp;Androidem uprawnień administratora (czyli właśnie *roota*); wyższego poziomu niż ten, który ma się domyślnie.

To działanie mniej radykalne niż wymiana całego systemu, ale wciąż dające większą kontrolę nad smartfonem. W&nbsp;takich warunkach Termux pod względem możliwości zbliży się do prawdziwej linuksowej konsoli.

Żeby zrootować telefon, należy najpierw *odblokować bootloadera*. Po ludzku: wyłączyć ogranicznik, które pozwala ładować jedynie domyślny, niezmieniony system.

I tu pojawia się haczyk, bo dostępność tej opcji zależy od producenta. U&nbsp;niektórych jest łatwo, inni wymagają zalogowania się na konto klienta i&nbsp;przesłania wniosku, jeszcze inni całkiem blokują bootloadera.

Osobiście nie rootowałem telefonu, zadowalając się jego [odgooglowaniem](/2024/02/03/smartfon-degoogle){:.internal}. Dlatego nie pomogę osobiście, ale mogę polecić dwa źródła:

* [„lista hańby”](https://github.com/zenfyrdev/bootloader-unlock-wall-of-shame) (po angielsku), wskazująca smartfony, na których dostęp do bootloadera jest utrudniony lub zablokowany subiektywną decyzją producenta.
* przystępny [poradnik z&nbsp;bloga *Wolność w kieszeni*](https://wolnoscwkieszeni.pl/uwolnic-smartfona-2/), opisujący proces rootowania po polsku i&nbsp;krok po kroku.

{% include details-end.html %}

Innym ograniczeniem jest fakt, że **domyślnie nie zadziała żaden interfejs graficzny** (na przykład moduł Tkinter z&nbsp;Pythona czy interaktywna edycja obrazków przez pakiet OpenCV).

Brak grafiki częściowo da się obejść, instalując pomocniczą apkę i&nbsp;wykonując [instrukcje ze strony Termuksa](https://wiki.termux.com/wiki/Graphical_Environment). Ale osobiście nie testowałem tej opcji.

## Python

Nie będzie potrzebny osobom używającym gotowych programów. Ja jednak chciałem wzbogacić Termuksa o&nbsp;własne skrypty od przetwarzania stron internetowych. A&nbsp;że piszę je w&nbsp;języku Python, to go potrzebowałem.

### Instalacja

Gdy już mamy Termuksa, instalowanie Pythona powinno być bardzo proste. Wpisujemy w&nbsp;konsolę:

<div class="bigspace black-bg mono">pkg install python</div>

{:.post-meta}
Na tym etapie może (a&nbsp;przynajmniej kiedyś mógł) wyskoczyć błąd związany z&nbsp;brakującym repozytorium. To nic strasznego. Zapraszam do części [„Rozwiązywanie problemów”](#instalowanie-przez-pkg-nie-działa){:.internal}.

### LXML

Biblioteka do sprawnej pracy z&nbsp;formatem XML. **Wiele moich skryptów jej nie potrzebuje**.

Do tej pory starałem się unikać jej oraz innych modułów opartych na innych językach niż Python. Ale stopniowo zaczynam poruszać na blogu kwestie przetwarzania bardziej złożonych plików, jak kod źródłowy dużych portali społecznościowych. Powoli staje się potrzebna.

Przede wszystkim zaktualizujmy swoje biblioteki do najnowszej wersji, żeby nie było między nimi rozbieżności. Wpisujemy w&nbsp;Termuksa:

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

Na Termuksie ważne, żeby to były właśnie te; wiele internetowych porad i&nbsp;samouczków odnosi się do zwykłego Linuksa i&nbsp;wspomina o&nbsp;wersjach z&nbsp;przyrostkiem *-dev*. Ale w&nbsp;bazach Termuksa ich po prostu nie mają, są zamiast nich te wymienione.

Kiedy już mamy u&nbsp;siebie Clanga, trzy potrzebne biblioteki oraz samego Pythona, możemy się pokusić o&nbsp;zainstalowanie LXML-a. Najprościej byłoby wpisać:

<div class="bigspace black-bg mono">
pip install lxml
</div>

**Ale uwaga**! W&nbsp;przypadku LXML-a po wyświetleniu *building wheel for LXML* zacznie się kompilacja, która długo potrwa, nawet całe godziny. Możemy na ten czas zostawić Termuksa w&nbsp;spokoju.  
Nie mamy cierpliwości? To możemy wybrać wersję LXML-a wolniejszą w&nbsp;działaniu, ale szybszą w&nbsp;instalacji. W&nbsp;tym celu wpisujemy:

<div class="bigspace black-bg mono">
CFLAGS='-O0' pip install lxml
</div>

Komenda `CFLAGS` oznacza, że chcemy szybkie przerobienie programu, kosztem ewentualnego nieco wolniejszego działania. Ale większej różnicy nam to nie zrobi.  
Dla jasności: pierwszy znak po myślniczku to duże&nbsp;O (jak *optymalizacja*), a&nbsp;drugi to zero.

Gdyby na tym etapie wyświetliło nam długi błąd, zawierający fragment:

{:.bigspace}
> command 'arm-linux-androideabi-clang' failed with exit status 1

...To znaczy że nie mamy u&nbsp;siebie Clanga. Instalujemy go jak wyżej.

{:.post-meta}
Wiele informacji z&nbsp;tej części zdobyłem dzięki [dyskusji](https://github.com/neovim/pynvim/issues/267) z&nbsp;wątku dotyczącego programu Neovim. Dziękuję jej uczestnikom!

## Rozwiązywanie problemów

### Pliki pobrane przez Termuksa są niedostępne

Wyobraźmy sobie, że pobieramy przez Termuksa jakiś dowolny plik. Na przykład obrazek albo filmik (polecam przez *yt-dlp*).

Nie znajdujemy go jednak w&nbsp;galerii, nigdzie go nie widać. Co się stało?

Po prostu Termux, jako niezależna aplikacja, ma prywatną przestrzeń na pliki. Zaś Android jest tak skonstruowany, że aplikacje -- również te z&nbsp;pozoru zżyte z&nbsp;systemem, jak Galeria -- nie mają do takich przestrzeni wglądu.

Żeby jakiś plik z&nbsp;Termuksa stał się ogólnodostępny, należy najpierw udzielić Termuksowi pozwolenia na dostęp do plików, a&nbsp;następnie **przenieść wybrany plik do przestrzeni publicznej**. W&nbsp;tym celu można użyć polecenia:

```
mv PLIK /sdcard
```

{:.post-meta .bigspace-after}
Gdyby nie działało, można wpisać `/storage/emulated/0` zamiast `/sdcard`.  
Żeby nie wpisywać nazwy pliku ręcznie, można wpisać pierwsze litery, a&nbsp;potem nacisnąć ikonkę dwóch strzałek z&nbsp;miniklawiatury wbudowanej w&nbsp;Termuksa.

### Odmowa dostępu do publicznych plików

Jeśli udzieli się Termuksowi pozwolenia na dostęp do plików, to można łatwo przechodzić do folderu `/storage/emulated/0` (czasem dostępnego pod skrótem `/sdcard`) i&nbsp;pracować z&nbsp;obecnymi tam plikami publicznymi: obrazkami, muzyką, pobranymi rzeczami itd.

Po jednej z&nbsp;aktualizacji zaczęło mi to szwankować; mimo pozwolenia Termux wyświetlał odmowę dostępu (`Permission denied`).

Rozwiązanie na szczęście jest proste: wystarczy klasyczna akcja typu wyłącz-włącz godna *IT Crowd*. Trzeba odebrać przez opcje Androida pozwolenie na dostęp do plików, a&nbsp;następnie udzielić go ponownie.

{:.post-meta .bigspace-after}
Jeśli ktoś nigdy nie bawił się pozwoleniami: trzeba wejść w&nbsp;ustawienia, potem `Aplikacje`, rozwinąć listę i&nbsp;wybrać z&nbsp;niej Termuksa, kliknąć zakładkę `Uprawnienia`. Tam będzie pstryczek od dostępu do plików.

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

