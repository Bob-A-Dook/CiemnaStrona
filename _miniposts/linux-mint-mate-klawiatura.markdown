---
layout: page
title: Linux Mint MATE i zagadka polskiej klawiatury
description: "Za każdym ładnym oknem stoi jakiś plik z ustawieniami."
---

Stworzyłem kiedyś wpis na temat [ustawiania języka polskiego](/tutorials/linux-mint-jezyk-polski-system){:.internal} na systemie Linux Mint.  
I niby wszystko fajnie -- ustawienia działały, w&nbsp;każdym przypadku podałem sposób graficzny i&nbsp;konsolowy -- ale te dwa sposoby nie do końca się ze sobą pokrywały.

Przykładem ustawianie **polskiego układu klawiatury**. W&nbsp;przypadku sposobu konsolowego działało polecenie:

```
setxkbmap pl
```

...Ale tylko do czasu wylogowania i&nbsp;ponownego zalogowania, potem trzeba je było powtórzyć. Sposób graficzny sprawiał zaś, że na dolnym pasku na stałe zagościła ikonka pozwalająca się przełączać między układami.

Co można zrobić, żeby sposób konsolowy w&nbsp;stu procentach pokrył się z&nbsp;graficznym? Spróbuję to zbadać w&nbsp;tym miniwpisie, na systemie Linux Mint w&nbsp;wariancie MATE.

{:.post-meta .bigspace-after}
Ogólne wnioski mogą mieć przełożenie również na inne Linuksy -- w&nbsp;szczególności te powiązane z&nbsp;Debianem (jak Zorin czy Ubuntu), na których działa program `dconf`. 

{% include info.html
type="Powiązane wpisy"
text="Tę samą rzecz [próbowałem zbadać na Cinnamonie](/miniposts/cinnamon-klawiatura){:.internal}, innym głównym wariancie Minta.  
Tam jednak odbiłem się na etapie dodawania ikony do dolnego paska, bo nie znalazłem zmian w&nbsp;żadnym konkretnym pliku konfiguracyjnym. Zapewne zachodziła jakaś komunikacja między procesami, której nie ogarniam. Jeszcze."
%}

## Spis treści

* [Śledztwo](#śledztwo)
  * [Ustalenie programu i&nbsp;procesu](#ustalenie-programu-iprocesu)
  * [Sprawdzenie kodu programu (ślepy zaułek)](#sprawdzenie-kodu-programu-ślepy-zaułek)
  * [Analiza programem *strace*](#analiza-programem-strace)
  * [Szperanie w&nbsp;zapiskach *strace'a*](#szperanie-wzapiskach-stracea)
  * [Dconf i&nbsp;analiza ustawień](#dconf-ianaliza-ustawień)
  * [Tworzenie polecenia konsolowego](#tworzenie-polecenia-konsolowego)
* [Podsumowanie](#podsumowanie)

## Śledztwo

Zacząłem od uruchomienia zwykłego okna, przez które na Mincie MATE można zmienić układ klawiatury. To właśnie zrobiliby zwykli użytkownicy, klikając w&nbsp;interfejs. Zgodnie z&nbsp;instrukcją ze wspomnianego na początku wpisu o&nbsp;spolszczaniu.

{:.post-meta .bigspace-after}
Czyli po kolei: ikona Minta w&nbsp;dolnym lewym rogu, `Control Center`, opcja `Keyboard`, zakładka `Layouts`.

<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-keyboard-1-new-layout.png" alt="Kolaż ze zrzutów ekranu pokazujący menu układów klawiatury z&nbsp;wyróżnionym przyciskiem 'Add'."/>

### Ustalenie programu i&nbsp;procesu

Na tym etapie warto było sprawdzić, jaki program tak naprawdę stoi za widocznym oknem. W&nbsp;tym celu uruchomiłem konsolę kombinacją `Ctrl+Alt+T` i&nbsp;wpisałem polecenie:

```
xprop
```

Kiedy je wykonałem, naciskając `Enter`, kursor zmienił się w&nbsp;krzyżyk. Kliknąłem okno z&nbsp;układem klawiatury, żeby wyświetlić dokładne informacje. Pokazały się między innymi takie:

<pre class="black-bg mono post-meta">_NET_WM_PID(CARDINAL) = 2452<br/>WM_CLASS(STRING) = "mate-keyboard-properties"</pre>

Tekst na dole to nazwa programu stojącego za widocznym oknem -- `mate-keyboard-properties`. Zatem gdzieś na moim systemie znajduje się plik o&nbsp;takiej nazwie. Zaś w&nbsp;nim -- cały kod, jaki komputer przetwarza w&nbsp;tle, kiedy pracuję sobie w&nbsp;tym oknie.

Liczba na górze to natomiast **identyfikator procesu**. Unikalne oznaczenie programu działającego w&nbsp;danym momencie.

{% include info.html
type="Analogia"
text="Można powiedzieć, że program to ogólny model samolotu (np. F16), zaś proces to konkretny samolot, który wzbił się w&nbsp;powietrze (potencjalnie jeden z&nbsp;wielu). Podczas lotu zwracają się do niego tylko po numerze."
%}

### Sprawdzenie kodu programu (ślepy zaułek)

Mając nazwę programu, mogłem ustalić, gdzie dokładnie się znajduje. Wyszukałem go takim poleceniem:

```
locate mate-keyboard-properties
```

Wyskoczyły dwie rzeczy:

{:.post-meta}
```
/usr/bin/mate-keyboard-properties  
/usr/share/man/man1/mate-keyboard-properties.1.gz
```

Ta druga miała w&nbsp;tekście *man*, co sugerowało skrót od *manual*, czyli jakąś instrukcję. Nie interesowało mnie to.

Z kolei pierwsza rzecz miała w&nbsp;ścieżce *bin* (skrót od *binary*, czyli dosłownie „zero-jedynkowy”; w&nbsp;praktyce chodzi jednak o&nbsp;program), więc to raczej ona stała za aktywnym oknem.

Spróbowałem odczytać zawartość pliku:

```
less /usr/bin/mate-keyboard-properties
```

W idealnym przypadku byłby to jakiś skrypt Pythona i&nbsp;moim oczom ukazałby się czytelny tekst.  
Okazało się jednak, że w&nbsp;tym przypadku było inaczej. **Był to plik zero-jedynkowy** (przed czym `less` lojalnie mnie ostrzegł). Przeznaczony do czytania przez komputer, nie człowieka.

Mógłbym pogrzebać w&nbsp;internecie za jego kodem źródłowym, ale w&nbsp;ten sposób odszedłbym od idei szperania domyślnymi narzędziami. Zatem uznałem zerkanie w&nbsp;kod programu za ślepy zaułek. Pozostała analiza tego, co robi w&nbsp;praktyce.

### Analiza programem *strace*

Linux posiada świetne narzędzie o&nbsp;nazwie *strace* (czyt. *es-trejs* albo *strejs*), pozwalające podglądać wszystkie interakcje programów z&nbsp;jądrem systemu.

Znając nazwę programu, który chcę śledzić, mógłbym użyć *strace'a* w&nbsp;takiej postaci:

```
strace mate-keyboard-properties
```

...Ale skoro już miałem uruchomione okno, to postanowiłem podczepić się pod nie. Dzięki temu wyniki obserwacji nie byłyby pełne chłamu związanego z&nbsp;*inicjalizacją programu* -- ładowaniem modułów, ikon oraz innych plików pomocniczych przed wyświetleniem okna.

Do podłączenia się pod rzecz działającą przydaje się ID procesu. Ustaliłem je wcześniej -- `2452`.

{:.post-meta .bigspace-after}
**Uwaga:** Przez cały czas, od pierwszego użycia konsoli do teraz, miałem otwarte to samo okno; dlatego mogłem użyć tego samego ID. Gdybym je zamknął, to musiałbym ustalić ID na nowo, bo przy każdym uruchomieniu programu się zmienia.

Ostatecznie użyłem takiego polecenia:

<pre class="black-bg mono nospace">
strace -p 2452&nbsp;-o keyboard.txt -f -v
</pre>

{:.figcaption}
`-p NUMER` śledzi konkretny proces, `-o PLIK` zapisuje wyniki do wskazanego pliku, `-f` śledzi również procesy-dzieci, zaś `-v` każe zbierać szczegółowe informacje.

...Niestety wyświetliło komunikat o&nbsp;błędzie.

<div class="black-bg mono red bigspace-after">
strace: attach: ptrace(PTRACE_SEIZE, 2452): Operation not permitted
</div>

To dlatego, że **Linux wymaga uprawnień administratora, żeby zaglądać do innych uruchomionych programów**. Takie przydatne zabezpieczenie.  
Żeby zyskać te uprawnienia, musiałem dopisać na początku polecenia `sudo`:

<pre class="black-bg mono nospace">
sudo strace -p 2452&nbsp;-o keyboard.txt -f -v
</pre>

{:.figcaption}
Po wykonaniu komendy na typowym Linuksie powinno zapytać o&nbsp;hasło. U&nbsp;mnie nie pytało, bo testowałem w&nbsp;trybie *live USB*.

Dopisałem, uruchomiłem polecenie. Zadziałało już bez błędów, *strace* zaczął śledzić. Następnie wyklikałem we wciąż aktywnym oknie polski układ klawiatury, potem je zamknąłem. Za kulisami powinna zajść jakaś zmiana.

*Strace* również przestał notować. Mogłem przeszukać stworzony przez niego plik w&nbsp;poszukiwaniu tropów.

### Szperanie w&nbsp;zapiskach *strace'a*

Na tym etapie musiałem zadać sobie pytanie -- czego dokładnie szukam?

Skoro ustawienia klawiatury potrafiły przetrwać wylogowanie, to zakładałem, że są czymś trwałym. Czyli zapewne: zapisanym do jakiegoś miejsca na moim systemie. Zapewne do pliku (bo na Linuksie prawie wszystko jest plikiem).

{:.post-meta .bigspace-after}
Nie mogę w&nbsp;sumie powiedzieć „zapisanym na dysku”, bo miałem Linuksa załadowanego z&nbsp;pendrive'a, w&nbsp;trybie *live* -- wszystko działo się wyłącznie w&nbsp;obrębie pamięci RAM.

W takim razie naturalną ścieżką wydawało się **sprawdzenie interakcji z&nbsp;plikami**. Za ich otwieranie odpowiada polecenie (właściwie *wywołanie systemowe*) o&nbsp;nazwie `openat`.  
Poszukałem jego wystąpień w&nbsp;zapisanych wynikach *strace'a*:

```
grep openat keyboard.txt
```

Znalazło mi różne otwierane pliki. Niektóre miały w&nbsp;swojej ścieżce `fonts` i&nbsp;rozszerzenia `.ttf`, czyli były czcionkami -- nieciekawe. Podobnie z&nbsp;tymi, które miały w&nbsp;nazwie `icons`.

Potencjalnie ciekawe były te, które miały w&nbsp;ścieżce `/X11/xkb/` -- sugerowało to jakieś systemowe ustawienia klawiatury.

{:.post-meta .bigspace-after}
Po próbie otwarcia witała mnie jednak informacja *DO NOT EDIT THIS FILE* -- to raczej nie były poszukiwane ustawienia, zaś plik był jedynie czytany.

Najbadziej zaciekawiły mnie natomiast interakcje z&nbsp;takimi plikami:

{:.post-meta}
```
/run/user/1000/dconf/user  
/home/mint/.config/dconf/user
```

To dlatego, że wprost miałem w&nbsp;nazwie `.config`. Czyli konfiguracja -- czyli to, czego szukałem.

### Dconf i&nbsp;analiza ustawień

Wspomniany plik `dconf/user` jest czymś w&nbsp;rodzaju rejestru z&nbsp;Windowsa -- to nie prosty, czytelny, tekstowy plik, lecz uporządkowana baza danych, zbliżona strukturą do drzewka.  
Trzeba z&nbsp;nią „rozmawiać” przez odpowiednie narzędzie. Jest nim programik konsolowy, który sam również nazywa się `dconf`.

Warstwy tej bazy dałoby się eksplorować jedną po drugiej poleceniem `dconf list`:

* `dconf list /` pokazałoby katalogi nadrzędne `com/` i&nbsp;`org/` (ew. parę innych);
* potem `dconf list /com/` pozwoliłoby zajrzeć do pierwszego z&nbsp;nich...

Takie szukanie krok po kroku byłoby jednak strasznie żmudne. Dlatego bardzo przydaje się **polecenie pokazujące całą zawartość bazy naraz**.

Zakładałem, że ręczne wybranie układu klawiatury wpływa na jakieś ustawienie w&nbsp;bazie. Chciałem porównać stan po zmianie z&nbsp;początkowym, przed *jakimikolwiek* zmianami.

Dlatego dla pewności wyłączyłem komputer i&nbsp;załadowałem z&nbsp;pendrive'a nowego, czystego Minta. Od razu po załadowaniu zrobiłem pełen zrzut bazy do pliku nazwanego umownie `dconf0.txt`:

```
dconf dump / > dconf0.txt
```

Następnie uruchomiłem okno z&nbsp;ustawieniami klawiatury, dodałem i&nbsp;wybrałem polski układ. Po czym zrobiłem kolejny zrzut -- tym razem, jak zakładałem, zmienionej bazy (zwróćcie uwagę na inną nazwę pliku):

```
dconf dump / > dconf1.txt
```

Na koniec pozostało porównać oba pliki:

```
diff dconf0.txt dconf1.txt
```

Zobaczyłem, że istotnie zaszły pewne zmiany:

{:.post-meta}
```
> [org/mate/desktop/peripherals/keyboard/kbd]  
> layouts=['pl', 'us']  
>   
> [org/mate/desktop/peripherals/keyboard/preview]  
> height=810  
> width=1440  
> x=240  
> y=135  
```

Strzałki w&nbsp;prawo (`>`) sugerują, że te linijki zostały *dodane* w&nbsp;nowszej wersji. W&nbsp;nawiasach kwadratowych widać tu nazwy kategorii, zaś poniżej ustawienia (w&nbsp;formacie `nazwa=wartość`).

Rzeczy z&nbsp;kategorii drugiej mniej mnie interesowały, bo słowo *preview* sugerowało, że to jakiś podgląd klawiatury.

Przypadek pierwszy wydawał się natomiast strzałem w&nbsp;dziesiątkę:

* kategoria `org/mate/desktop/peripherals/keyboard/kbd`,
* nazwa `layouts`,
* wartość `['pl', 'us']`.

### Tworzenie polecenia konsolowego

Programik `dconf` pozwala nie tylko przeglądać, ale również *edytować* opcje. Mogłem teraz łatwo stworzyć własne polecenie dodające polski układ klawiatury.

Wymagało to jednak paru modyfikacji:

* Musiałem dodać ukośnik (`/`) na początku nazwy kategorii, żeby przedstawić ją jako pełną ścieżkę „od początku”.
* Ustawianą wartość musiałem umieścić w&nbsp;dodatkowych cudzysłowach.

  Inaczej nawiasy kwadratowe byłyby traktowane jako znaki specjalne. Musiałem przy tym użyć podwójnych cudzysłowów, bo pojedyncze już były w&nbsp;środku.

Ostateczne polecenie:

```
dconf write /org/mate/desktop/peripherals/keyboard/kbd/layouts "['pl','us']"
```

Mogę użyć tego w&nbsp;konsoli zaraz po załadowaniu świeżego systemu Mint MATE. Zyskuję przełącznik na dolnym pasku, który po kliknięciu zmienia układ klawiatury z&nbsp;angielskiego na polski (i&nbsp;*vice versa*).

Jeśli nie zależy mi w&nbsp;ogóle na układzie angielskim, to mogę zostawić sam polski (nadal trzymając się formatu listy w&nbsp;nawiasach kwadratowych):

```
dconf write /org/mate/desktop/peripherals/keyboard/kbd/layouts "['pl']"
```

Wówczas nie będzie żadnego przełącznika na pasku (nie byłby potrzebny), za to polskie litery zaczną działać.

Co najważniejsze -- **ta zmiana przetrwa wylogowanie i&nbsp;ponowne zalogowanie**. W&nbsp;przeciwieństwie do poprzedniego `setxkbmap pl`.

{% include info.html
type="Uwaga"
text="Jak sugeruje słowo `mate` widoczne w&nbsp;ścieżce -- polecenie zadziałałoby tylko na wariancie Mint MATE. Nie miałoby przełożenia na Minta Cinnamona ani na inne Linuksy."
%}

## Podsumowanie

Linux bywa bardzo przyjazny dla swoich użytkowników, oferując intuicyjne interfejsy graficzne. Czasem jednak warto poszukać konsolowych odpowiedników, zwłaszcza jeśli chce się coś zautomatyzować.

Podczas mojego małego śledztwa użyłem zestawu kultowych programów -- `xprop`, `strace`, `grep`, `less`, `diff` -- żeby dojść do tego, jakie zmiany zachodzą podczas wybierania polskiego układu klawiatury w&nbsp;Centrum Sterowania.

Okazało się, że zmieniają się wówczas ustawienia w&nbsp;konkretnym pliku. Zmianę da się łatwo odtworzyć w&nbsp;świecie konsoli z&nbsp;użyciem programu `dconf`.

Efektem końcowym jest komenda konsolowa pozwalająca szybko (i&nbsp;trwale!) włączać polski układ klawiatury na systemie Mint MATE.

Opis swoich działań, krok po kroku, zamieszczam tutaj. Mam nadzieję, że pokaże to osobom wchodzącym w&nbsp;świat Linuksa, że zaglądanie za jego kulisy bywa proste i&nbsp;satysfakcjonujące :smile:
