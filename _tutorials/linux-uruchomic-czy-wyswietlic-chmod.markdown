---
layout: page
title: Linux i ukrywanie okna „uruchomić czy wyświetlić plik?”
description: "Kto pyta, nie błądzi. Ale to pytanie bywa irytujące."
---

Oto kolejny miniwpis rozwiązujący drobny (acz dla niektórych uciążliwy) problem z&nbsp;systemami na bazie Linuksa.

Sytuacja jest taka: korzystam z&nbsp;przeglądarki plików na swoim linuksowym systemie. U&nbsp;mnie to Mint MATE, czasem Mint Cinnamon. Ale to raczej bez znaczenia.  
Wszystko ładnie działa. Mogę bezproblemowo klikać i&nbsp;otwierać różne pliki: dokumenty, filmy, muzykę.

W którymś momencie napotykam jakiś plik tekstowy. Może instrukcję z&nbsp;popularnym tytułem `README`? Może jakieś luźne notatki w&nbsp;formacie `.txt`? Obojętne.  
Po kliknięciu, zamiast prostej zawartości pliku, pojawia się taki komunikat:

{:.bigspace-before}
<img src="/assets/tutorials/linux-uruchomic-czy-wyswietlic/mint-komunikat-wykonywalnosc-plikow.png" alt="Zrzut ekranu komunikatu mówiącego: 'Uruchomić plik X&nbsp;czy wyświetlić jego zawartość? Plik X&nbsp;jest wykonywalnym plikiem tekstowym'." />

> Uruchomić plik X czy wyświetlić jego zawartość?  
X jest wykonywalnym plikiem tekstowyym

{% include details.html summary="Wersja angielska" %}
> Do you want to run {nazwa_pliku} or display its contents?  
{Nazwa_pliku} is an executable text file.
{% include details-end.html %}

Jakie uruchamianie, o&nbsp;co chodzi? Klikam `Wyświetl` i&nbsp;zawartość pliku pokazuje się w&nbsp;domyślnym edytorze.

Na krótszą metą wystarczy zwykłe wybieranie tej opcji. Ale na dłuższą może to być irytujące, bo komunikat pojawia się po *każdym* kliknięciu pliku.  
Z czego wynika i&nbsp;jak się go pozbyć?

## Spis treści

* [Parę dziwnych wzorców](#parę-dziwnych-wzorców)
* [Prawdziwa przyczyna](#prawdziwa-przyczyna)
* [Rozwiązanie doraźne -- ukrycie komunikatu](#rozwiązanie-doraźne--ukrycie-komunikatu)
* [Wyłączanie wykonywalności pliku](#wyłączanie-wykonywalności-pliku)
* [Masowe wyłączenie wykonywalności](#masowe-wyłączenie-wykonywalności)
* [Podsumowanie](#podsumowanie)

{:.post-meta}
Jeśli kogoś nie interesuje kontekst i przyczyna komunikatu, to można przeskoczyć prosto do [rozwiązań](#rozwiązanie-doraźne--ukrycie-komunikatu){:.internal}.

## Parę dziwnych wzorców

Gdybym trochę pogrzebał, to doszedłbym może do wniosku, że sprawa nie dotyczy dokumentów (jak DOCX czy PDF) ani plików multimedialnych (jak MP4). Takie pliki po kliknięciu otwierają się od razu.  
Okno z&nbsp;pytaniem pojawia się jedynie przy próbie otwarcia **prostych _plików tekstowych_**.

Szeroko pojętych. Mogą do nich należeć wspomniane pliki `.txt`, ale również „kod źródłowy” wpisów na bloga w&nbsp;formacie `.markdown`. Albo kod miażdżącej większości programów komputerowych.

Gdybym pokopał jeszcze bardziej, to być może natrafiłbym na wspólny mianownik -- wszystkie pliki, przy których wyświetla się komunikat, były kiedyś **skopiowane z&nbsp;pendrive'a**.

{:.post-meta}
W żadnym razie nie jest to jedyna możliwa przyczyna komunikatu; ale to dość prawdopodobny sposób, w&nbsp;jaki sprawa może dotknąć zwykłych ludzi.

## Prawdziwa przyczyna

Skąd te dziwne prawidłowości? Nie będę dłużej trzymał w&nbsp;niepewności -- problem wynika z&nbsp;**różnych systemów plików** na Linuksie i&nbsp;na niektórych pendrive'ach.

Choć pliki w&nbsp;oczach użytkowników wyglądają tak samo -- są wyświetlane w&nbsp;tym samym interfejsie przeglądarki plików, mają te same ikony -- w&nbsp;rzeczywistości mogą pod nimi stać całkiem różne fundamenty.

System plików na Linuksie (zwykle EXT) obsługuje dodatkowe dane na temat uprawnień przypisane do plików. Ten na niektórych nośnikach (np. FAT albo NTFS) ich nie wspiera.

{:.post-meta .bigspace-after}
Na temat samych uprawnień nie będę się rozpisywał. Tylko w&nbsp;skrócie: dla każdego pliku lub folderu można określić kilka podstawowych rzeczy, jakie można lub jakich nie można z&nbsp;nim robić.

Skopiowanie plików z&nbsp;pendrive'a wiąże się z&nbsp;przejściem między tymi dwoma światami: od nieznającego uprawnień do znającego.  
Nie dostając informacji o&nbsp;uprawnieniach, Linux sam ją uzupełnia. Domyślnie włącza plikom skopiowanym z&nbsp;pendrive'a jedno z&nbsp;takich uprawnień -- **wykonywalność**. Możliwość ich uruchamiania jako programów.

{% include info.html
type="Ciekawostka"
text="Nie ma tu jednak żelaznej reguły „pendrive = dodana wykonywalność”.  
Mam dwa pendrive'y z tej samej firmy ISY, kupione w popularnym sklepie AGD. Jeden z&nbsp;nich przerobiłem na nośnik [systemu PorteuX](https://github.com/porteux/porteux), drugiego nie ruszałem.  
Widać różnicę. Do plików ze zwykłego jest dodawana wykonywalność, do tych z&nbsp;systemowego nie."
trailer="<p class='figure bigspace-before'><img src='/assets/tutorials/linux-uruchomic-czy-wyswietlic/isy-pendrive-systemy-plikow.png' alt='Zrzut ekranu konsoli pokazujący informacje na temat dwóch nośników USB o tej samej nazwie ISY. Widać, że mają dwa różne systemy plików.'/><br/>
<span class='figcaption'>Może w takim razie sposobem na dziwne komunikaty byłoby przerobienie swoich pendrive'ów na instalacyjne? Żarcik taki. Choć PorteuX naprawdę jest ciekawy.</span></p>"
%}

A dlaczego komunikat pojawia się tylko przy plikach tekstowych?  
To już kwestia działania samej przeglądarki plików -- jej twórcy wiedzą, że czasem takie pliki to skrypty, które ktoś mógłby chcieć uruchomić kliknięciem. Dlatego przy nich dają dwie możliwości, przy innych plikach nie.

Gdyby jednak użyć w&nbsp;konsoli polecenia pokazującego informacje o&nbsp;plikach, to okazałoby się, że wykonywalność jest włączona dla *wszystkich* plików z&nbsp;pendrive'a. Również grzecznych obrazków czy PDF-ów:

{:.bigspace-before}
<img src="/assets/tutorials/linux-uruchomic-czy-wyswietlic/linux-ls-wykonywalnosc-plikow.png" alt="Zrzut ekranu pokazujący wynik programu ls. Wyróżniono literkę x&nbsp;przy nazwach plików PDF i&nbsp;PNG, wskazującą na ich wykonywalność"/>

## Rozwiązanie doraźne -- ukrycie komunikatu

Żeby komunikat z&nbsp;pytaniem przestał się pojawiać, można:

* uruchomić przeglądarkę plików,
* wybrać z&nbsp;górnego paska zakładkę `Edycja`,
* wybrać opcję `Preferencje` (powinna być na dole),
* w&nbsp;wyświetlonym oknie kliknąć zakładkę `Zachowanie` u&nbsp;góry,
* Pod nagłówkiem `Wykonywalne pliki tekstowe` zaznaczyć opcję, żeby **wyświetlało** je po kliknięciu.

{:.bigspace-before}
<img src="/assets/tutorials/linux-uruchomic-czy-wyswietlic/linux-mint-wykonywalnosc-wylaczanie-komunikatow.png" alt="Kolaż pokazujący krok po kroku elementy, jakie należy kliknąć, żeby zawsze domyślnie wyświetlać pliki"/>

{:.figcaption}
Zrzut ekranu dla wariantu Mint MATE, ale dla Cinnamona jest praktycznie to samo (tyle że zakładki są w&nbsp;kolumnie po lewej zamiast u&nbsp;góry).

Szybko, łatwo, przez klikaninę. Komunikaty przestaną nas niepokoić.

## Wyłączanie wykonywalności pliku

Sposób graficzny nie rozwiązuje problemu, tylko go ukrywa -- sprawia, że irytujący komunikat przestaje się pojawiać.

Ale same pliki nadal będą miały w&nbsp;uprawnieniach włączoną wykonywalność. Będą w&nbsp;oczach Linuksów czymś innym niż wcześniej. Może to nie mieć znaczenia, ale może też odbić się czkawką, zwłaszcza jeśli je wyślemy gdzieś w&nbsp;świat.

{:.post-meta .bigspace-after}
Sam się na to nadziałem, bo swego czasu puściłem na serwer z&nbsp;kodem tego bloga aktualizację zawierającą pliki z&nbsp;pendrive'a.  
Choć nie wpłynęło to na jego działanie, serwer potraktował różnice w&nbsp;uprawnieniach jak zmiany w&nbsp;plikach. Aktualizacja wyglądała w&nbsp;podsumowaniu na większą niż w&nbsp;rzeczywistości.

Jak zaradzić takim niechcianym różnicom i&nbsp;*wyłączyć* wykonywalność? Tak naprawdę, również za kulisami?

Przy pojedynczych plikach rozwiązanie jest na szczęście bardzo proste. Wystarczy:

* kliknąć plik prawym przyciskiem myszy,
* wybrać z&nbsp;rozwijanego menu opcję `Właściwości` (zapewne na dole),
* w&nbsp;oknie, które się otworzy, wybrać u&nbsp;góry zakładkę `Uprawnienia`,
* odhaczyć u&nbsp;dołu opcję odpowiedzialną za wykonywalność.

{:.bigspace}
<img src="/assets/tutorials/linux-uruchomic-czy-wyswietlic/linux-mint-wylaczanie-wykonywalnosci.png" alt="Kolaż pokazujący krok po krokuopcje, jake należy kliknąć, żeby wyłączyć wykonywalność konkretnego pliku"/>

Ale uwaga -- **nie każdy Linux pozwala kontrolować uprawnienia przez takie menu**. Jeśli nigdzie nie widać pstryczków, to przydatniejszy może się okazać sposób konsolowy.

W tym celu należy uruchomić konsolę w tym samym folderze co plik (na Mincie i&nbsp;paru innych: zakładka `Plik` z&nbsp;górnego paska, potem `Otwórz w terminalu`). Gdy konsola się pojawi, trzeba w&nbsp;nią wpisać:

```
chmod -x PLIK
```

Programik `chmod` odpowiada za sterowanie uprawnieniami plików.  
Opcja `-x` każe mu wyłączyć wykonywalność. Zaś zamiast słowa `PLIK` ma być nazwa (albo ścieżka) tego naszego, przy którym wyświetla się komunikat.

{:.post-meta}
Porada: na Mincie można chwytać ikony plików wewnątrz ich przeglądarki, przenosić je do wnętrza konsoli i&nbsp;upuszczać. Automatycznie wstawiają się wtedy ich pełne ścieżki.  
Dając taką pełną ścieżkę, dałoby się użyć konsoli z&nbsp;dowolnego miejsca, niekoniecznie z&nbsp;tego samego folderu co plik.

## Masowe wyłączenie wykonywalności

Kiedy plików z&nbsp;niechcianą wykonywalnością jest wiele -- zwłaszcza rozrzuconych po zagnieżdżonych w&nbsp;sobie folderach -- to nie ma sensu gmerać w&nbsp;ustawieniach każdego z&nbsp;nich z&nbsp;osobna. Przydałaby się szybka opcja, która wyłączy wszystko naraz.

Nie znalazłem póki co informacji o&nbsp;domyślnie zainstalowanym, graficznym interfejsie do takich zmian (może pomysł do podsunięcia opiekunom Linuksów?).  
Jest za to takie przydatne polecenie konsolowe, którego należy użyć na folderze *nadrzędnym* z&nbsp;problematycznymi plikami:

```
chmod -R -x+X FOLDER
```

* `-R` oznacza, że program powinien odwiedzać kolejno podfoldery zawarte w&nbsp;tym wskazanym (a&nbsp;także ich podfoldery itd.), aż odwiedzi absolutnie wszystko.
* `-x+X` wyłącza wykonywalność plików, ale włącza ją dla folderów.

  Ta druga rzecz jest istotna, bo w&nbsp;przypadku folderów bez tej opcji nie byłoby możliwości zaglądania do zawartych w&nbsp;nich plików.

* `FOLDER` odnosi się do folderu, w&nbsp;którym znajdują się pliki z&nbsp;niechcianą wykonywalnością.

  Gdybyśmy chcieli użyć komendy w&nbsp;tym samym folderze, w&nbsp;którym jesteśmy, to można zamiast nazwy folderu wpisać pojedynczą kropkę (`.`).

## Podsumowanie

Komunikaty dotyczące wykonywalności plików na Linuksie pojawiają się w&nbsp;dość szczególnych warunkach, na które nie każda osoba się natknie. Dotyczą zwykle kopiowania plików tekstowych z&nbsp;nośnika o&nbsp;innym systemie plików.

Jeśli już się trafią, to bywają irytujące, bo pojawiają się przy każdej próbie interakcji z&nbsp;plikami.

Na szczęście rozwiązania są bardzo proste: można albo ukryć komunikaty na poziomie przeglądarki, albo na różne sposoby wyłączyć wykonywalność plików. Wszystkie te rzeczy, za wyjątkiem masowego wyłączenia, można zrobić przez czytelny graficzny interfejs.

To kolejna z&nbsp;drobnych spraw, które mogą nieco uwierać osoby przechodzące na Linuksa. Mam nadzieję, że ten poradnik pozwoli wygładzić zadziora i&nbsp;skuteczniej cieszyć się tym, co w&nbsp;Linuksie dobre :sunglasses:
