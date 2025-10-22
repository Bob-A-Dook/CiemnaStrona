---
layout: page
title: Bundler, Jekyll i historia pewnego błędu
description: "Nietypowy splot okoliczności daje nietypowe błędy."
---

Czas na małą opowiastkę z&nbsp;linii frontu. Odkryłem niedawno, że nie działa mi Bundler -- program pozwalający podejrzeć treści na bloga przed ich publikacją.

Wiedząc, że chodzi rzekomo o&nbsp;brakujący plik, nieco pośledziłem Bundlera programem monitorującym interakcje.  
Odkryłem, że źródłem błędu był **brak wykonywalności pliku** (silnika blogowego Jekyll); swoją rolę odgrywał również potencjalnie mylący komunikat o&nbsp;błędzie.

## Kontekst

Mój blog opiera się na popularnym silniku Jekyll, napisanym w&nbsp;języku Ruby.

Przed publikacją mam zwyczaj uruchamiać tryb podglądu, żeby zobaczyć, czy wszystko wygląda i&nbsp;działa jak należy. Używam do tego programu-menedżera o&nbsp;nazwie Bundler.

Rutynowo wpisuję w&nbsp;konsolę:

```
bundle exec jekyll serve
```

Zwykle widzę informację zwrotną, że blog jest dostępny na lokalnym serwerze testowym (wszystko w&nbsp;obrębie mojego komputera, nawet bez łączności z&nbsp;siecią).  
Klikam w&nbsp;konsoli link do wewnętrznego adresu `127.0.0.1:4000` -- a&nbsp;po chwili w&nbsp;domyślnej przeglądarce wyświetla się Ciemna Strona.

Tym razem jednak coś poszło nie tak i&nbsp;zamiast Ciemnej pojawił się komunikat o&nbsp;błędzie:

{:.figure .bigspace}
<img src="/assets/tutorials/strace-bundle-brak-jekylla/bundle-exec-blad-brak-jekylla.png" alt="Zrzut ekranu z&nbsp;konsoli, pokazujący błąd programu Bundle i&nbsp;komunikat o&nbsp;braku modułu Jekyll"/>

> Bundler: command not found: jekyll  
Install missing gem executables with \'bundle install\'

Pokazuje, że nie znalazło modułu `jekyll`. A&nbsp;ja przecież wzywałem Jekylla już nieraz, dokładnie w&nbsp;ten sposób. Wiedziałem, że go mam.

Miałem już kiedyś identyczny błąd; pamiętam, że po prostu skopiowałem wtedy pliki z&nbsp;jakiegoś backupu. Zaczęło działać, nie drążyłem tematu. Tym razem byłem bardziej zmotywowany.

{:.post-meta .bigspace-after}
Zresztą w&nbsp;tamtym czasie mniej interesowałem się debugowaniem i&nbsp;nawet nie wiedziałbym, od czego zacząć.

## Debugowanie programem *strace*

Skoro moim problemem był rzekomy brak pliku (o&nbsp;którym wiedziałem, że go mam), postanowiłem sięgnąć do programu `strace` (czyt. *strejs*).

Jest on swego rodzaju szpiegiem, który śledzi wszystkie interakcje wskazanego programu z&nbsp;jądrem systemu Linux (a&nbsp;takiego używam).  
**Każde otwarcie pliku na Linuksie zostanie odnotowane** przez *strace'a*, bo wymaga takiej interakcji. Mógłbym zobaczyć, gdzie Bundler szukał plików.

Użyłem zatem *strace'a* w&nbsp;trybie śledzenia zarówno samego Bundlera, jak i&nbsp;jego podprocesów (`-f`) oraz zapisywania szczegółowych informacji (`-v`) do pliku nazwanego subiektywnie *nojekyll.txt* (`-o nojekyll.txt`):

```
strace -f -v -o nojekyll.txt bundle exec jekyll serve
```

Po wyskoczeniu błędu program skończył działanie, a&nbsp;*strace* przestał notować. Powstał pokaźny plik z&nbsp;zapiskami, liczący ponad 17&nbsp;MB.  
Przy takich ścianach tekstu trzeba zrobić przesiew informacji.

Mogłem na przykład założyć, że początek pliku to wszelkiego rodzaju ładowanie modułów, czyli rzeczy nieciekawe. Była szansa, że ciekawe rzeczy znajdę bliżej końca, tuż przed wystąpieniem błędu i&nbsp;zakończeniem działania.
Mogłem też filtrować po nazwie, bo interesował mnie konkretny moduł -- `jekyll`. Wyszukałem tę nazwę w&nbsp;zapisanym pliku:

```
grep 'jekyll' nojekyll.txt
```

...I wyskoczyły bardzo ciekawe rzeczy:

{:.figure .bigspace}
<img src="/assets/tutorials/strace-bundle-brak-jekylla/strace-szukanie-jekylla.png" alt="Kilka linijek z&nbsp;konsoli, w&nbsp;których wyróżniono słowo 'jekyll'. Widać, że to próby otwierania plików pod kilkoma różnymi ścieżkami."/>

Widać, że w&nbsp;pierwszej linijce z&nbsp;obrazka (wyróżnionej kolorem) Bundler próbuje zaglądać do tego właściwego pliku, ale zderza się z&nbsp;brakiem pozwolenia (`Permission denied`).  
Potem zagląda też w&nbsp;inne miejsca, ale tam nic nie ma (`No such file or directory`).

Klucz do rozwiązania zagadki krył się w&nbsp;tej pierwszej, wyróżnionej linijce. W&nbsp;słowie `X_OK`. W&nbsp;konwencji wielu systemów litera *X* odpowiada słowu *eXecutable*. „Wykonywalny” (jako program).  
Mając pewne podejrzenie, wyszukałem `X_OK` w&nbsp;internecie. Moje potwierdzenia się przypuściły, [ten skrót odpowiada wykonywalności](https://man.archlinux.org/man/access.2.en).

...A tak się składa, że w&nbsp;ostatnim czasie ingerowałem w&nbsp;tę właściwość.

{:.post-meta .bigspace-after}
Uważne osoby mogą zauważyć, że ścieżka do Jekylla jest niestandardowa -- ale to nie ona była problemem, bo przed włączeniem Bundlera ją zgłaszałem gdzie trzeba. Zresztą widać, że znajdował plik.

## Rozwiązanie zagadki

Sprawa wynikała ze zmian, jakie wprowadziłem niedawno, po napisaniu poradnika na temat [wyłączania irytującego komunikatu](/tutorials/linux-uruchomic-czy-wyswietlic-chmod){:.internal}.

Streszczając: każdy plik na Linuksie jest opisywany przez właściwość zwaną *wykonywalnością* (ang. *executability*). Mówi ona z&nbsp;grubsza, czy dany plik można traktować jak program.

Nie jest to w&nbsp;żadnym razie rzecz uniwersalna. Wiele systemów plików (np. ten na moim pendrivie) nie wspiera tej właściwości. Żeby jakoś pogodzić dwa światy, Linux podczas zgrywania plików z&nbsp;takiego pendrive'a **automatycznie włącza ich wykonywalność**.  
A to prowadzi do nieco irytującego komunikatu, gdy próbuję otworzyć pliki tekstowe w&nbsp;zwykłej przeglądarce plików (a&nbsp;robię to często, nie jestem typem konsolowca).

Inspirując się własnym, podlinkowanym wyżej poradnikiem, wyłączyłem wykonywalność wielu plików naraz (`chmod -R -x+X FOLDER`). Zebrałem je do jednego archiwum ZIP, a&nbsp;to archiwum zgrałem na pendrive'a. Potem je rozpakowałem, przenosząc narzędzia do pracy nad blogiem na inny komputer.

Dzięki temu nie miałem problemu z&nbsp;niechcianym komunikatem. Myślałem, że z&nbsp;działaniem plików też nie (mogę np. używać skryptów Pythona poleceniem `python3 skrypt.py`, nawet gdy nie są wykonywalne).

Jak się okazuje, Bundler (a&nbsp;może cały język Ruby?) idzie jednak z&nbsp;wymaganiami o&nbsp;krok dalej. **Wykonywalny musi być nie tylko uruchamiacz, ale również uruchamiany programik**, Jekyll. I&nbsp;na tym się naciąłem.

A komunikat o&nbsp;braku pliku? Nie do końca trafny. Po prostu po napotkaniu pierwszego błędu (braku pozwolenia) Bundler szukał dalej, nie znajdując niczego. I&nbsp;wspomniał wyłącznie o&nbsp;nieznalezieniu, pomijając pierwszy błąd.

## Naprawa błędu

Skoro przyczyną był brak wykonywalności Jekylla, to rozwiązanie wydawało się proste -- **włączyć mu wykonywalność**.

Można konsolowo:

```
chmod +x ŚCIEŻKA_DO_PLIKU
```

Czyli w&nbsp;moim przypadku:

```
chmod +x /home/mint/.gems/ruby/3.2.0/bin/jekyll
```

Potem ponownie używam `bundle exec jekyll serve`... I&nbsp;śmiga!

{:.figure .bigspace}
<img src="/assets/tutorials/strace-bundle-brak-jekylla/bundle-exec-poprawne-dzialanie.png" alt="Zrzut ekranu z&nbsp;konsoli, pokazujący informację o&nbsp;załadowaniu strony na wewnętrzny serwer."/>

Mogłem sobie wyświetlić wierny podgląd bloga. A&nbsp;potem dokończyć w&nbsp;nim edycję tego wpisu i&nbsp;się nim podzielić :smile:

{% include details.html summary="Sposób graficzny (na Mincie)" %}

{:.bigspace-before}
Na systemie Linux Mint, z&nbsp;którego korzystam, istnieje również prosty sposób na zmianę wykonywalności poprzez zwykłe klikanie. Osoby mniej konsolowe mogłyby to docenić.

W tym celu:

* kopiuję pełną ścieżkę do pliku, ale bez `/jekyll` na końcu,
* uruchamiam przeglądarkę plików i&nbsp;włączam tryb tekstowy górnego paska (przyciskiem z&nbsp;ikoną notesu z&nbsp;ołówkiem),
* wklejam ścieżkę do paska i&nbsp;w ten sposób przechodzę do folderu z&nbsp;plikiem `jekyll`,
* klikam go prawym przyciskiem myszy,
* wybieram opcję `Właściwości` z&nbsp;menu,
* w&nbsp;kolejnym oknie przechodzę do zakładki `Uprawnienia` i&nbsp;tam *włączam* opcję traktowania pliku jak programu (u&nbsp;dołu).

W tym przypadku konsola byłaby dużo szybsza niż klikanie. Ale wiem, że niektóre osoby reagują na nią alergicznie. Niech każdy ma co woli :wink:

{% include details-end.html %}

## Podsumowanie

Wykonywalność plików może prowadzić do denerwujących komunikatów, zwłaszcza jeśli jest przymusowo narzucana podczas kopiowania z&nbsp;pendrive'a o&nbsp;innym systemie plików.  
Ale, jak widać w&nbsp;tym przypadku -- czasem **jej wyłączenie również może prowadzić do nieoczekiwanych błędów**. W&nbsp;tym wypadku potrzebował jej plik z&nbsp;Jekyllem.

Na szczęście linuksowy program `strace` pozwolił w&nbsp;tym przypadku szybko i&nbsp;skutecznie dojść do źródła błędu. Od teraz mam złoty środek -- wykonywalność włączoną tam, gdzie to konieczne, zaś przy pozostałych plikach wyłączoną.

Mam nadzieję, że ta opowieść z&nbsp;frontu pozwoli komuś uniknąć irytującego, enigmatycznego błędu. Albo przynajmniej da trochę rozrywki.

Swoją drogą widzę tu możliwość poprawienia czytelności błędów wewnątrz Bundlera -- mógłby wspominać o&nbsp;braku potrzebnych pozwoleń, a&nbsp;nie o&nbsp;(drugorzędnym) braku plików w&nbsp;alternatywnych miejscach.  
Może w&nbsp;wolnym czasie to zgłoszę jako drobną propozycję poprawki. W&nbsp;końcu świat *open source* to nieustanne szlifowanie i&nbsp;doskonalenie.

Dzięki za przeczytanie i&nbsp;do zobaczenia w&nbsp;kolejnych wpisach!
