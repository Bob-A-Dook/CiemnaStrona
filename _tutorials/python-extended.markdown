---
layout: page
title: Przyjemniejsza praca z Pythonem
description: "Samouczek o tym, jak sprawnie używać Pythona na Windowsie. Skróty klawiszowe, własny folder na skrypty, PowerShell i pliki BAT."
---

Do swoich wpisów dorzucam czasem autorskie skrypty Pythona, które pozwalają Wam sprawdzić pewne rzeczy na własną rękę.

Podstawy instalacji Pythona i&nbsp;otwierania skryptów w&nbsp;domyślnym, załączonym edytorze IDLE pokazałem w&nbsp;[podstawowym samouczku](tutorials/using-python){:.internal}.

{:.post-meta .bigspace-after}
A dlaczego IDLE? Ano dlatego, że wiele skryptów nie jest przystosowanych do uruchamiania przez podwójne kliknięcie myszką. Na ekranie na krótko pojawia się czarne okno, a potem znika. 

Przyznam, że praca z&nbsp;Pythonem w&nbsp;IDLE może być na początku toporna.  
Za każdym razem musimy kopiować skrypty do folderu, w którym chcemy ich użyć. A&nbsp;potem jeszcze musimy włączać edytor i&nbsp;wyklikać drogę do odpowiedniego pliku.

Na szczęście jest kilka sposobów na znaczne ułatwienie sobie pracy. Będziemy w&nbsp;stanie łatwo otwierać skrypty, wzywać je z&nbsp;dowolnego miejsca, uruchamiać prostymi kombinacjami klawiszy.  
Co więcej, **to całkiem bezpieczne i&nbsp;nie wymaga dotykania żadnych funkcji systemu**. Wystarczy stworzyć parę plików i&nbsp;folderów.

Przekonałem Was? Jeśli tak, to zapraszam do lektury! Porady ułożyłem w&nbsp;kolejności od najprzydatniejszych do całkowicie opcjonalnych.

Jeśli chcecie sprawdzać wszystko na przykładzie, to możecie pobrać <a href="/assets/tutorials/python-basics/witaj.py" download>mój skrypt <i>witaj.py</i></a>{:.internal}.

## 0. Znajdowanie folderu Pythona

Zanim zaczniemy ułatwiać sobie życie, trzeba ustalić, gdzie Python przechowuje różne swoje moduły.

Sposobów na to jest mnóstwo -- póki efektem naszych działań będzie odnalezienie folderu Pythona, to każdy z&nbsp;nich jest dobry.

Zademonstruję tu parę z&nbsp;nich, używając screenów z&nbsp;Windowsa jako przykładów.

# Wyklikanie sobie drogi

Sposób graficzny na przykładzie **Windowsa** (na innych systemach niestety będzie inaczej). Powinien działać niezależnie od tego, w&nbsp;jakim folderze zainstalujemy Pythona.

Otwieramy menu Start (ikona w lewym dolnym rogu).

Przewijając listę po lewej, znajdujemy tam zakładkę `Python`. Rozwijamy ją, wyświetlając m.in. IDLE.  
Klikamy tę opcję prawym przyciskiem myszy, najeżdżamy na opcję `Więcej`, a&nbsp;potem klikamy `Otwórz lokalizację pliku`:

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-1-python-lokalizacja.webp" width="400px" alt="Pasek z opcjami systemu Windows. Widać rozwiniętą zakładkę o nazwie Python, pod nią zakreśloną opcję 'Więcej', a na końcu zakreśloną opcję 'Otwórz lokalizację pliku'."/>

Włączy się okno Eksploratora Windows z&nbsp;kilkoma skrótami do różnych elementów Pythona. Klikamy dowolny z&nbsp;nich prawym przyciskiem i&nbsp;znów wybieramy `Otwórz lokalizację pliku`.

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-2-python-lokalizacja.webp" alt="Fragment okna Eksploratora Plików systemu Windows. W górnym z nich zaznaczony jest skrót do programu IDLE, a na dole widać rozwijane menu z wyróżnioną opcją 'Otwórz lokalizację pliku'."/>

Powinien nam się otworzyć folder główny Pythona, zawierający między innymi takie rzeczy:

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-3-python-folder.webp" alt="Fragment okna programu Eksplorator Windows. Widać tutaj listę podfolderów i plików znajdujących się w folderze o nazwie Python."/>

Spoiler: później skorzystamy z&nbsp;podfolderów *Lib*, *libs* oraz *Scripts*.

Teraz fajna sztuczka, o&nbsp;której sam wcześniej nie wiedziałem. Kliknijcie w&nbsp;puste pole **w&nbsp;prawej części górnego paska** (ale przed strzałką w dół na jego skraju):

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-4-sciezka.webp" width="400px" alt="Górny pasek Eksploratora. Puste miejsce po prawej stronie od ostatniego elementu otoczono czerwoną ramką. Jest w nią wpisane słowo 'KLIK'."/>

W ten sposób pełna ścieżka do folderu zaznaczy się Wam na niebiesko, w&nbsp;formie tekstu. Wystarczy jedno `Ctrl+C`, żeby ją skopiować. Przyda się później w&nbsp;paru miejscach!

# Zapytanie przez IDLE

Alternatywa dla sposobu powyżej. Bardziej „hakerska”, bo wymaga włączenia IDLE i&nbsp;skopiowania całych dwóch linijek kodu! Zaleta: to sposób uniwersalny i&nbsp;powinien zadziałać na wszystkich systemach (**Windows, Linux, MacOS...**).

Otwieramy IDLE w&nbsp;taki sposób, w&nbsp;jaki tylko chcemy. Powinien się włączyć w&nbsp;trybie interaktywnym. W&nbsp;ostatniej linijce, za trzema strzałkami (`>>>`), możemy wpisywać swoje komendy. 

Wpisujemy (albo kopiujemy stąd i&nbsp;wklejamy):

```python
import sys
```

Potwierdzamy, naciskając `Enter`. Potem wpisujemy:

```python
for p in sys.path: print(p)
```

To pętla, więc tym razem musimy wcisnąć `Enter` dwa razy.  
Wyświetli się lista różnych folderów Pythona, coś w tym stylu:

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-5-sciezka-przez-idle.webp" alt="Zrzut ekranu z edytora IDLE, pokazujący pięć ścieżek do plików na dysku C Windowsa, wyświetlonych na niebiesko, jedna pod drugą"/>

Główny folder Pythona to najkrótsza ścieżka, kończąca się słowem `Python` i&nbsp;numerem wersji (zaznaczyłem na obrazku). Możemy ją skopiować.

## 1. Ustawienie IDLE jako programu otwierającego skrypty

Pierwsze kroki z&nbsp;Pythonem na Windowsie mogą być nieintuicyjne. Mówię to jako wielki fan tego języka.

Przyczynę opisałem wyżej -- jeśli po prostu dwukrotnie klikniemy skrypt, to często tylko mignie nam okienko. Może zadziała, ale nie zdążymy odczytać żadnych komunikatów. Dlatego otwieramy skrypt przez IDLE, a tam z kolei czeka nas klikanina.

Jeśli pobieracie tylko parę skryptów raz na ruski rok (np. ode mnie), to taka klikanina jest do przyjęcia. Ale jeśli musicie otwierać je częściej, to staje się to uciążliwe.

Ale mam dobrą wiadomość -- **można łatwo sprawić, że dwukrotne kliknięcie dowolnego pliku _py_ od razu go otworzy w&nbsp;IDLE**. +100 do komfortu pracy.

To do dzieła! Klikamy prawym przyciskiem na jakikolwiek plik *py* i&nbsp;wybieramy `Otwórz za pomocą > Wybierz inną aplikację`.

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-1-wybor-aplikacji.webp" alt="Kolaż złożony z trzech przyciętych zrzutów ekranu. Pierwszy pokazuje samą nazwę pliku, drugi to rozwijane menu z zaznaczoną opcją 'Otwórz za pomocą' a trzeci to zaznaczona opcja 'Wybierz inną aplikację'."/>

Klikamy `Więcej aplikacji`, żeby rozwinąć listę. Przewijamy na sam dół.  
Tam najpierw zaznaczamy opcję, żeby zawsze otwierać pliki w&nbsp;taki sposób. A&nbsp;potem klikamy `Wyszukaj inną aplikację...`:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-2-wybor-aplikacji.webp" alt="Zrzuty ekranu pokazujące fragmenty dwóch okienek i trzy elementy podpisane cyframi od 1 do 3. 1 to opcja 'Więcej aplikacji', 2 to opcja 'Zawsze otwieraj pliki py przy użyciu tej aplikacji', a 3 to opcja 'Wyszukaj inną aplikację na tym komputerze'."/>

Włączy się okno wyboru pliku. Możemy się przeklikać do naszego folderu Pythona. Ale nie musimy. Jeśli w [poprzednim kroku](#0-znajdowanie-folderu-pythona) skopiowaliśmy sobie ścieżkę, to teraz można ją wkleić.

Żeby to zrobić, klikamy po prawej stronie paska, żeby przełączył się w&nbsp;tryb tekstu:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-3-sciezki.webp" alt="Pasek górny Eksploratora Plików systemu Windows, pokazany w dwóch wariantach. U góry mamy ścieżkę jako ciąg folderów połączonych strzałkami, a po prawej stronie nałożono czerwonymi literami napis KLIK. U dołu w tym samym pasku mamy już ścieżkę jako tekst, połączoną ukośnikami i zaznaczoną kolorem niebieskim."/>

Naciskamy `Ctrl+V`, wklejając tam nasz adres do folderu Pythona. Potwierdzamy `Enter`em.

W folderze Pythona, do którego trafimy, interesuje nas podfolder `Lib`, a&nbsp;w nim `idlelib`.  
Otwieramy go, a&nbsp;z listy plików wybieramy `idle.bat`:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-4-wybor-idle.webp" alt="Fragment okna Eksploratora Plików, pokazujący że aktualna ścieżka to folder idlelib w folderze Python. Pod spodem widać listę plików, jeden pod drugim. Zaznaczony jest plik idle.bat"/>

Potwierdzamy nasz wybór:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-4-wybor-idle2.webp" alt="Dolna część okna wyboru plików, pokazująca że zaznaczonym plikiem jest idle.bat. Widać również wyróżnioną opcję 'Otwórz'."/>

I zrobione! Od teraz, przeglądając pliki w&nbsp;Eksploratorze, możemy po prostu dwukrotnie klikać skrypty Pythona, żeby wyświetlać je w&nbsp;IDLE'u.

## 2. Uruchamianie skryptów z&nbsp;dowolnego folderu

Do tej pory musieliśmy kopiować skrypty do tego samego folderu, w&nbsp;którym chcemy ich użyć. Na dłuższą metę to niepraktyczne, więc mam kolejny ułatwiacz życia. Sprawimy, żeby dało się **trzymać skrypty w&nbsp;jednym miejscu i&nbsp;uruchamiać przez samo wpisanie ich nazwy**.

Żeby to zrobić, trzeba sprawić, żeby Python zawsze „widział” nasz skrypt. Na szczęście to nic trudnego. Wystarczy go włożyć do któregoś ze specjalnych folderów. 

Otwieramy ustalony wcześniej główny folder Pythona. Wybieramy w&nbsp;nim podfolder `libs`, a&nbsp;potem `site_packages`.

{:.post-meta .bigspace-after}
**Uwaga!** Zwracajcie uwagę na nazwy. W&nbsp;folderze macie zarówno *libs*, jak też *Lib*.

Mój folder `site_packages` wyglądał tak (praktycznie zaraz po instalacji, dodałem tylko jeden moduł):

{:.bigspace}
<img src="/assets/tutorials/python-extended/3-1-site-packages.webp" alt="Wnętrze folderu site packages, pokazujące pliki oraz foldery domyślnie tam umieszczone przez Pythona."/>

To jeden z&nbsp;folderów, w&nbsp;których Python szuka swoich skryptów. Możemy wziąć nasz skrypt *witaj.py* -- albo wszelkie inne -- i&nbsp;**po prostu je tutaj dorzucić**.

Co nam to dało? Od teraz nasz skrypt jest dostępny z&nbsp;każdego miejsca w&nbsp;systemie!  
Możemy go na przykład importować, wpisując w&nbsp;IDLE jego nazwę bez końcówki *.py* -- w&nbsp;naszym przypadku `import witaj`.  
W&nbsp;jakim folderze byśmy nie byli, odpali nam nasz kod:

{:.bigspace}
<img src="/assets/tutorials/python-extended/3-2-witaj-import.webp" alt="Konsola z IDLE z wpisaną komendą 'import witaj' i wyświetlonymi poniżej słowami 'Witaj po ciemnej stronie'."/>

Nie każdy skrypt jest jednak przystosowany do importowania. Jeśli chcemy w&nbsp;pełni wykorzystać jego dostępność z&nbsp;każdego miejsca, to **warto odejść od IDLE'a na rzecz PowerShella** (lub podobnych konsol).

Ten drugi jest silniej zintegrowany z&nbsp;Windowsem, można go szybko uruchomić w&nbsp;każdym folderze. Wygląda to tak:

* Uruchamiamy domyślny Eksplorator Plików.
* Chodzimy po folderach, aż znajdziemy plik/folder, z&nbsp;którym chcemy coś zrobić.
* Wybieramy z&nbsp;górnego paska `Plik`, a&nbsp;następnie `Otwórz program Windows PowerShell`.

I tyle! Pojawi się okno PowerShella, a&nbsp;folderem aktywnym będzie ten, w&nbsp;którym byliśmy, klikając w opcję. Wpisujemy:

```
python -m witaj
```

Pamiętajmy o&nbsp;`-m`, bo bez tego nie zadziała. A&nbsp;jeśli działa, to wyświetli nasz kod:

{:.bigspace}
<img src="/assets/tutorials/python-extended/3-3-witaj-powershell.webp" width="400px" alt="PowerShell z wpisaną powyższą komendą i wyświetlonymi pod nią słowami 'Witaj po ciemnej stronie'."/>

W ten sposób, po prostu dorzucając skrypty do konkretnego folderu, mamy do nich szybki dostęp. Możemy pozostać przy domyślnym pythonowym `site_packages`, i jedynie przypiąć gdzieś skrót do tego folderu.

Ale możemy też wydzielić osobny folder na swoje pythonowe skrypty. Pokażę to w&nbsp;kolejnym kroku.

## 3. Stworzenie własnego folderu na skrypty

Wrzucanie wszystkiego do folderu `site_packages` ma pewną wadę -- nasze autorskie skrypty są wymieszane z&nbsp;tymi pobieranymi z&nbsp;zewnątrz. Łatwo o&nbsp;bałagan. 

Co by było, gdybyśmy chcieli przenieść swoje skrypty na inny komputer? Musielibyśmy ich specjalnie wypatrywać. Niedobrze.  
A gdybyśmy po prostu brali cały folder `site_packages` i&nbsp;go kopiowali z&nbsp;jednej instalacji Pythona do drugiej? Też źle. Niektóre większe moduły by mogły nie działać, bo potrzebują też innych rzeczy.

Są rozwiązania prowizoryczne, takie jak wyróżnianie swoich skryptów nietypowymi nazwami (np. dawanie inicjałów na początku).  
Ale **można też wydzielić na nie osobny folder**. Dzięki temu będzie nam łatwiej je znaleźć, zmieniać i&nbsp;porządkować. Zróbmy to!

Najpierw tworzymy nowy folder, gdzie tylko chcemy -- u&nbsp;mnie `C:\Skrypty`. Kopiujemy ścieżkę do tego folderu (np. sposobem z&nbsp;poprzednich punktów).

Teraz trzeba dać znać Pythonowi, że ma patrzeć do naszego folderu. Przechodzimy do `site_packages` i tworzymy tam nowy plik tekstowy. O&nbsp;dowolnej nazwie, bo liczy się tylko treść i&nbsp;rozszerzenie. Ja go nazwałem *moje.txt*.

Otwieramy ten plik w&nbsp;Notatniku i&nbsp;wklejamy tam ścieżkę do naszego folderu. Zapisujemy. Zmieniamy rozszerzenie pliku z&nbsp;*.txt* na *.pth*. Całość wygląda tak:

{:.bigspace}
<img src="/assets/tutorials/python-extended/4-1-pth-file.webp" alt="Kolaż pokazujący kawałek folderu site_packages z dodanym plikiem pth, a także sam ten plik otwarty w notatniku. Zawiera jedną linijkę: C, dwukropek, ukośnik lewy, Skrypty."/>

{:.figcaption}
Jeden plik, w&nbsp;nim jedna ścieżka. To wszystko.

Sprawdzamy czy działa. Powtarzamy krok z&nbsp;punktu&nbsp;0, czyli wpisujemy w&nbsp;IDLE linijka po linijce:

```python
import sys
for p in sys.path: print(p)
```

Tym razem na liście powinno wyświetlić również ścieżkę do naszego folderu:

{:.bigspace}
<img src="/assets/tutorials/python-extended/4-2-wlasny-folder.webp" alt="Zrzut ekranu z IDLE pokazujący konsolę, a w niej wpisaną powyższą komendę. Widać, że pierwszy wyświetlony folder to 'C, skrypty'."/>

Od teraz możemy do niego dorzucać wszystkie swoje skrypty.

{% include info.html
type="Uwaga"
text="Jeśli ścieżka do nowego folderu się nie pojawia, to możecie wyłączyć IDLE i&nbsp;włączyć go ponownie. Być może się nie zaktualizowało od poprzedniej sesji."%}

## 4. Szybkie włączanie PowerShella

Do tej pory pokazywałem, że można włączyć PowerShella przez klikanie menu z&nbsp;górnego rogu Eksploratora. Ale jeśli mamy go używać częściej, w&nbsp;różnych folderach, to warto poznać szybsze metody.

{:.post-meta .bigspace-after}
(Wielkie dzięki dla [tego](https://superuser.com/questions/1339064/keyboard-shortcut-to-open-powershell-from-the-desktop) i&nbsp;[tego](https://superuser.com/questions/1309679/open-powershell-as-administrator-at-current-file-explorer-directory-keyboard-sho) wątku ze StackOverflow).

Przede wszystkim podczas używania Eksploratora można nacisnąć `Shift + prawy przycisk myszy` na obszarze z&nbsp;listą plików.  
Kiedy klikamy z&nbsp;*Shiftem*, to **pokazuje się jedna dodatkowa opcja** -- *Uruchom w&nbsp;programie Windows PowerShell*.

Wada tej metody? Trzeba uważać, żeby zamiast pustej przestrzeni nie kliknąć jakiegoś pliku, bo pokazałyby się inne opcje. A&nbsp;to może być trudne, jeśli folder jest zapchany plikami.

Poza tym da się jeszcze szybciej! Skrótami klawiszowymi, które niestety zależą od ustawionego języka Windowsa.  
W&nbsp;polskiej wersji naciskamy `Alt+P+O`, w&nbsp;angielskiej `Alt+F+O` (*O* jak *Open*).  
Dzięki temu mamy PowerShella w&nbsp;sekundę, w&nbsp;dowolnym folderze!

{% include info.html type="Porada"
text="Jeśli macie wersję Windowsa w&nbsp;innym języku, to możecie po prostu przytrzymać `Alt` przez dłuższą chwilę, żeby wyświetliły się litery odpowiadające różnym elementom Eksploratora.  
Potem patrzycie, jakie klawisze odpowiadają opcji `Plik` i&nbsp;otwieraniu PowerShella. To te klawisze musicie nacisnąć w&nbsp;swojej wersji."
trailer="<p class='bigspace' style='margin-bottom:0px'><img src='/assets/tutorials/python-extended/5-1-skroty-powershell.webp' alt='Zrzut ekranu z Eksploratora, pokazujący rozwiniętą zakładkę Plik z górnego rogu oraz parę pierwszych opcji. W ich rogach wyświetlają się literki na tle przypominającym klawisze z klawiatury' width='400px'/></p>"%}

Z&nbsp;kolei żeby **szybko włączyć PowerShella w domyślnym folderze** -- bez otwierania Eksploratora Plików -- naciskamy `Przycisk z ikoną Windowsa + X`, żeby wyświetlić okno z&nbsp;opcjami. A&nbsp;następnie `I` (literę podkreśloną w&nbsp;nazwie odpowiadającej PowerShellowi).

Przydaje się to, jeśli chcemy szybko odpalić przez PS skrypt, który robi zawsze to samo, niezależnie od folderów. U&nbsp;mnie jest to na przykład skrypt otwierający w&nbsp;Firefoksie kilka stron z&nbsp;prognozą pogody.

## 5. Skrócenie komend dzięki plikowi BAT

Wyczerpaliśmy najłatwiejsze zmiany, teraz zrobi się dziwniej.

Niby wszystko jest cudownie, możemy odpalać skrypty z&nbsp;każdego folderu... Ale za każdym razem musimy wpisywać `python -m nazwa_skryptu`.

To co najmniej 11 znaków ze spacjami, nawet jeśli skrypt będzie miał najkrótszą jednoliterową nazwę. Z&nbsp;czasem może się znudzić!

Czy da się to przyspieszyć jeszcze bardziej? Bez grzebania w&nbsp;systemie i&nbsp;zmieniania czegoś na stałe?

Odpowiedź: tak. Da się zejść **do jednego znaku** w PowerShellu.  
Ale w&nbsp;tym celu trzeba zrobić lekką incepcję i&nbsp;stworzyć *skrypt Windowsa odpalający skrypt Pythona*.

Okazuje się, że Windows w tzw. *zmiennej PATH* przechowuje listę folderów, do których ma szybki dostęp. To do jednego z&nbsp;nich trzeba się wprosić.  
Mam dobrą wiadomość: jeśli podczas instalacji zaznaczyliśmy odpowiednią opcję, to **nie musimy w&nbsp;niczym grzebać, Python sam dodał do _PATH_ kilka folderów**. Proponuję dorzucić się do jednego z nich, `Scripts`.

{% include info.html type="Porada" text="Jeśli chcecie się upewnić, że Python dodał folder *Scripts* do *PATH*, to wyświetlcie w&nbsp;PowerShellu zawartość *PATH*. Wpiszcie:"
trailer="<div class='black-bg mono'>$env:path -split \";\"</div>
<p>A gdyby nie było tam nic od Pythona, to możemy zainstalować go ponownie. Tym razem zaznaczając opcję dodania go do zmiennych systemowych.</p>" %}

Przechodzimy zatem do folderu `Scripts` w głównym folderze Pythona.  
Tak jak wcześniej tworzyliśmy dla Pythona plik *.pth* ze ścieżką do folderu, tak teraz stworzymy plik *.bat* -- skrót do konkretnego skryptu przeznaczony dla PowerShella.

Tworzymy plik o&nbsp;takiej nazwie, jaka nam pasuje, na przykład *z.txt* (to tę nazwę będziemy wpisywać, żeby odpalić skrypt). Wpisujemy w&nbsp;pliku:

```
@ECHO OFF
python -m witaj
```

Pierwsza linijka jest tu po to, żeby skrypt *.bat* nie wyświetlał niczego od siebie, a&nbsp;jedynie rzeczy od Pythona.  
A druga linijka to dokładnie taka komenda, jaką sami byśmy wpisali, żeby uruchomić skrypt Pythona przez PowerShell.

Całość wygląda tak:

{:.bigspace}
<img src="/assets/tutorials/python-extended/6-2-bat-file.webp" alt="Kolaż z trzech okien Windowsa. U góry widać pełną ścieżkę do folderu Scripts, poniżej jego zawartość z jednym dodanym plikiem 'z.txt'. Na samym dole znajduje się okno pokazujące plik z.txt otwarty w Notatniku, z podanym wyżej tekstem."/>

Zmieniamy nazwę pliku na *z.bat*. Od teraz po otwarciu PowerShella dałoby się po prostu nacisnąć `z` i&nbsp;`Enter`, żeby odpalić nasz skrypt. Jednoliterkowiec! :metal:

{:.bigspace}
<img src="/assets/tutorials/python-extended/6-3-witaj-bat.webp" width="300px" alt="Zrzut ekranu z PowerShella pokazujący wpisaną komendę 'z' i wyświetlone pod spodem słowa 'Witaj po ciemnej stronie'."/>

Gdybyśmy chcieli jeszcze bardziej ułatwić pracę -- na przykład uruchamiać coś jednym klawiszem, bez włączania PowerShella -- to już by mogło wymagać grzebania w&nbsp;systemie albo instalacji dodatków, takich jak *AutoHotKey*. Dlatego na tym etapie się zatrzymam.

{% include info.html type="Porada" text="Jeśli chcecie, żeby wasze pliki BAT miały bardziej opisowe nazwy zamiast jednoliterkowych, a&nbsp;przy tym chcecie dość szybko je wpisywać, to istnieje przydatna opcja.  
Jeśli Wasz plik jest w którymś z folderów z `PATH`, to po wpisaniu w&nbsp;PowerShellu pierwszych liter nazwy możecie nacisnąć `Tab`. Wstawi Wam pełną nazwę pliku.  
Upewnijcie się tylko, że nazwa Waszego pliku nie koliduje z&nbsp;innymi programami dostępnymi przez PATH. Polecam dać coś mało ogólnego, np. dodać na końcu nazwy swoje inicjały."%}

## Podsumowanie

W tym wpisie przeszliśmy długą drogę. Od świeżaków kopiujących skrypty i&nbsp;żmudnie klikających w&nbsp;okienka, gdy chcą ich użyć...  
Aż po „hakierów”, którym wystarczy pięć klawiszy (tu: `Alt`+`P`+`O`, literka, `Enter`), żeby przeczesać skryptem dowolny, aktualnie odwiedzany folder.

Porada o&nbsp;szybkim otwieraniu skryptów w IDLE powinna przydać się każdemu, w&nbsp;tym moim czytelnikom.  
Natomiast te o&nbsp;ułatwianiu pracy mogą pomóc przy codziennych żmudnych zadaniach.

A jeśli nie używacie skryptów? Gorąco zachęcam, żeby je poznać. To jedna z&nbsp;tych rzeczy, które dają kontrolę nad swoją pracą. I&nbsp;sporo radochy, bo w&nbsp;końcu tworzymy je dla własnego pożytku.

Jeśli czujecie się zawaleni powtarzalną robotą, to życzę gorąco, żeby skrypty pomogły Wam odetchnąć. I&nbsp;wydrzeć trochę swojego czasu z&nbsp;rąk *lyderów byznesu*, którzy naobiecywali klientom cudów i&nbsp;teraz zawalają Was robotą.

A jeśli też darzycie ich antypatią? Zapraszam do czytania moich wpisów :smile:

{% include info.html type="Dygresja" text="Moje słowa raczej nic nie zmienią, ale **Linux (u mnie: Mint) jest dużo przyjemniejszy w&nbsp;pracy z&nbsp;Pythonem niż Windows**.  
Nie trzeba specjalnie zmieniać nazw plików, żeby móc je edytować w&nbsp;notatniku.  
Nie trzeba szukać IDLE'a po folderach. Jest domyślną opcją do otwierania plików *py*.  
Nie trzeba dopisywać żadnego *ECHO OFF*. Skrypty Linuxa (*.sh*, odpowiednik *.bat*) nie wyświetlają nic od siebie i&nbsp;wystarczy wpisać do nich samą nazwę komendy.  
...Zresztą w&nbsp;ogóle nie trzeba plików pośrednich. Wystarczy szybka zmiana, żeby każdy plik (w tym skrypty Pythona) dało się odpalać przez samo wpisanie jego nazwy."%}
