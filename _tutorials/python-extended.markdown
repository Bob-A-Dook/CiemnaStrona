---
layout: page
title: Przyjemniejsza praca z Pythonem
description: "Samouczek o tym, jak sprawnie używać Pythona na Windowsie. Skróty klawiszowe, własny folder na skrypty, PowerShell i pliki BAT."
---

Do swoich wpisów dorzucam czasem autorskie skrypty Pythona, które pozwalają Wam sprawdzić pewne rzeczy na własną rękę.

Podstawy instalacji Pythona i&nbsp;odpalania skryptów pokazałem w&nbsp;<a href="{{site.url}}/tutorials/using-python">podstawowym samouczku</a>.

Przyznam, że praca z&nbsp;Pythonem w&nbsp;IDLE może być na początku toporna. Za każdym razem musimy kopiować skrypty. Żeby je otworzyć, musimy najpierw włączać edytor, a&nbsp;potem nawigować do odpowiedniego pliku.

Na szczęście jest kilka sposobów, które ogromnie ułatwią pracę. Będziemy w&nbsp;stanie łatwo otwierać skrypty, trzymać je w&nbsp;jednym miejscu, odpalać kilkoma klawiszami w&nbsp;dowolnym folderze.

Co więcej, **to całkiem bezpieczne i&nbsp;nie wymaga dotykania żadnych funkcji systemu**. Wystarczy stworzyć parę plików i&nbsp;folderów.

Przekonałem Was? Jeśli tak, to zapraszam do lektury! Porady ułożyłem w&nbsp;kolejności od najprzydatniejszych do całkowicie opcjonalnych.

Jeśli chcecie sprawdzać wszystko na przykładzie, to możecie pobrać <a href="/assets/tutorials/python-basics/witaj.py" download>mój skrypt <i>witaj.py</i></a>.

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
<img src="/assets/tutorials/python-extended/1-1-python-lokalizacja.webp" width="400px"/>

Włączy się okno Eksploratora Windows z&nbsp;kilkoma skrótami do różnych elementów Pythona. Klikamy dowolny z&nbsp;nich prawym przyciskiem i&nbsp;znów wybieramy `Otwórz lokalizację pliku`.

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-2-python-lokalizacja.webp"/>

Powinien nam się otworzyć folder główny Pythona, zawierający między innymi takie rzeczy:

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-3-python-folder.webp"/>

Spoiler: później skorzystamy z&nbsp;podfolderów *Lib*, *libs* oraz *Scripts*.

Teraz fajna sztuczka, o&nbsp;której sam wcześniej nie wiedziałem. Kliknijcie w&nbsp;puste pole **po prawej stronie górnego paska** (ale przed strzałką):

{:.bigspace}
<img src="/assets/tutorials/python-extended/1-4-sciezka.webp" width="400px" alt="Górny pasek Eksploratora. Puste miejsce po prawej stronie od ostatniego elementu otoczono czerwoną ramką. Jest w nią wpisane słowo 'KLIK'."/>

W ten sposób pełna ścieżka do folderu zaznaczy się Wam na niebiesko, w&nbsp;formie tekstu. Wystarczy jedno `Ctrl+C`, żeby ją skopiować. Przyda się później w&nbsp;paru miejscach!

# Zapytanie przez IDLE

Sposób bardziej „hakerski”, bo wymaga skopiowania całych dwóch linijek kodu!  
Zaleta: uniwersalny i&nbsp;powinien zadziałać na wszystkich systemach (**Windows, Linux, MacOS...**).

Otwieramy IDLE w&nbsp;taki sposób, w&nbsp;jaki tylko chcemy. Powinien się włączyć w&nbsp;trybie interaktywnym. W&nbsp;ostatniej linijce, za trzema strzałkami (`>>>`), możemy wpisywać swoje komendy. 

Wpisujemy (albo kopiujemy i&nbsp;wklejamy):

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
<img src="/assets/tutorials/python-extended/1-5-sciezka-przez-idle.webp"/>

Główny folder Pythona to najkrótsza ścieżka, kończąca się słowem `Python` i&nbsp;numerem wersji (zaznaczyłem na obrazku). Możemy ją skopiować.

## 1. Ustawienie IDLE jako programu otwierającego skrypty

Pierwsze kroki z&nbsp;Pythonem na Windowsie mogą być nieintuicyjne.

Skrypt to program. Więc po dwukrotnym kliknięciu powinien się odpalić, prawda? Otóż nie -- jeśli tak zrobimy, to zwykle na krótko wyskoczy czarne okienko. Po czym zniknie, nic nie robiąc.

Nadal możemy otwierać skrypty przez IDLE, domyślny edytor Pythona. Ale w&nbsp;tym celu musimy najpierw włączyć IDLE, a&nbsp;dopiero potem wybrać `Otwórz...` i&nbsp;wyklikać sobie drogę do naszego skryptu.

Jeśli pobieracie tylko parę skryptów raz na ruski rok (np. ode mnie), to taka klikanina jest do przyjęcia. Ale jeśli musicie otwierać je częściej, to staje się to uciążliwe.

Ale mam dobrą wiadomość -- **można łatwo sprawić, że dwukrotne kliknięcie na każdym pliku _py_ od razu go otworzy w&nbsp;IDLE**. +100 do komfortu pracy.

To do dzieła! Klikamy prawym przyciskiem na jakikolwiek plik *py* i&nbsp;wybieramy `Otwórz za pomocą > Wybierz inną aplikację`.

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-1-wybor-aplikacji.webp"/>

Klikamy `Więcej aplikacji`, żeby rozwinąć listę. Przewijamy na sam dół.  
Tam najpierw zaznaczamy opcję, żeby zawsze otwierać pliki w&nbsp;taki sposób. A&nbsp;potem klikamy `Wyszukaj inną aplikację...`:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-2-wybor-aplikacji.webp"/>

Włączy się okno wyboru pliku. Jeśli nie chcemy klikać przez foldery, przyda nam się tutaj **ścieżka do folderu Pythona, skopiowana w&nbsp;poprzednim punkcie**.

Żeby ją wkleić, klikamy po prawej stronie paska, żeby przełączył się w&nbsp;tryb tekstu:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-3-sciezki.webp"/>

Naciskamy `Ctrl+V`, wklejając tam nasz adres do folderu Pythona. Potwierdzamy `Enter`em.

W folderze Pythona, do którego powinniśmy trafić, interesuje nas podfolder `Lib`, a&nbsp;w nim `idlelib`.  
Otwieramy go, a&nbsp;z listy plików wybieramy `idle.bat`:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-4-wybor-idle.webp"/>

Potwierdzamy nasz wybór:

{:.bigspace}
<img src="/assets/tutorials/python-extended/2-4-wybor-idle2.webp"/>

I zrobione! Od teraz, przeglądając pliki w&nbsp;Eksploratorze, możemy po prostu dwukrotnie klikać skrypty Pythona, żeby wyświetlać je w&nbsp;IDLE'u.

## 2. Odpalanie własnych skryptów z&nbsp;każdego miejsca

Do tej pory musieliśmy kopiować skrypty do tego samego folderu, w&nbsp;którym chcemy ich użyć. Na dłuższą metę to niepraktyczne, więc mam kolejny ułatwiacz życia. Sprawimy, żeby dało się je odpalać przez samo wpisanie ich nazwy w&nbsp;PowerShella.

Żeby to zrobić, trzeba sprawić, żeby Python zawsze „widział” nasz skrypt. Na szczęście to nic trudnego, wystarczy go włożyć do jednego konkretnego folderu. 

Otwieramy główny folder Pythona i&nbsp;wybieramy w&nbsp;nim podfolder `libs`, a&nbsp;potem `site_packages`.  
**Uwaga!** Zwracajcie uwagę na nazwy. W&nbsp;folderze macie zarówno *libs*, jak też *Lib*.

Mój folder `site_packages` wygląda tak (praktycznie zaraz po nowej instalacji, dodałem tylko jeden moduł):

{:.bigspace}
<img src="/assets/tutorials/python-extended/3-1-site-packages.webp" alt="Wnętrze folderu site packages."/>

To jeden z&nbsp;folderów, w&nbsp;których Python szuka swoich skryptów. Możemy wziąć nasz skrypt *witaj.py* -- albo wszelkie inne -- i&nbsp;**po prostu je tutaj dorzucić**.

Co nam to dało? Od teraz nasz skrypt jest dostępny z&nbsp;każdego miejsca w&nbsp;systemie!

Możemy od teraz wpisać w&nbsp;IDLE nazwę skryptu bez końcówki *.py*. W&nbsp;naszym przypadku `import witaj`. W&nbsp;jakim folderze byśmy nie byli, odpali nam nasz kod:

{:.bigspace}
<img src="/assets/tutorials/python-extended/3-2-witaj-import.webp" width="400px" alt="Konsola z IDLE z wpisaną komendą 'import witaj' i wyświetlonymi poniżej słowami 'Witaj po ciemnej stronie'."/>

Jeśli chcemy wykorzystać w&nbsp;pełni dostępność skryptu z&nbsp;każdego miejsca, to **warto odejść od IDLE'a na rzecz PowerShella**. PS-a można łatwo odpalić w&nbsp;każdym folderze. Nawet jeśli nie ma tam żadnych skryptów Pythona. IDLE'a nie.

Jak wygląda praca z&nbsp;PowerShellem? Możemy w&nbsp;Eksploratorze przejść do dowolnego folderu, włączyć PowerShella i&nbsp;wpisać:

```
python -m witaj
```

Pamiętajmy o&nbsp;`-m`, bo bez tego nie zadziała. A&nbsp;jeśli działa, to wyświetli nasz kod:

{:.bigspace}
<img src="/assets/tutorials/python-extended/3-3-witaj-powershell.webp" width="400px" alt="PowerShell z wpisaną powyższą komendą i wyświetlonymi pod nią słowami 'Witaj po ciemnej stronie'."/>

W ten sposób, po prostu dorzucając skrypty do konkretnego folderu, mamy do nich szybki dostęp.

Jeśli chcemy pozostać przy dorzucaniu plików do `site_packages`, to można sobie gdzieś przypiąć skrót do tego folderu. Ale możemy też wydzielić osobny folder na swoje pythonowe skrypty. Pokażę to w&nbsp;kolejnym kroku.

## 3. Stworzenie własnego folderu na skrypty

Wrzucanie wszystkiego do `site_packages` ma jedną drobną wadę -- nasze skrypty oraz skrypty pobierane z&nbsp;zewnątrz są w&nbsp;tym folderze wymieszane. Łatwo o&nbsp;bałagan. 

Co by było, gdybyśmy chcieli przenieść swoje skrypty na inny komputer? Trzeba by je specjalnie wybierać.  
A gdybyśmy po prostu brali cały folder `site_packages` i&nbsp;go kopiowali z&nbsp;jednej instalacji Pythona do drugiej? Niektóre większe moduły by mogły nie działać, bo potrzebują też innych rzeczy.

Są rozwiązania prowizoryczne, takie jak wyróżnianie swoich skryptów nietypowymi nazwami (np. dawanie inicjałów na początku).  
Ale **można też wydzielić na nie osobny folder**. Dzięki temu będzie nam łatwiej je znaleźć, zmieniać i&nbsp;porządkować. Zróbmy to!

Najpierw tworzymy nowy folder, gdzie tylko chcemy -- u&nbsp;mnie *C:\Skrypty*. Kopiujemy ścieżkę do tego folderu (np. sposobem z&nbsp;poprzednich punktów).

Potem przechodzimy do `site_packages`. Tam tworzymy nowy plik tekstowy. O&nbsp;dowolnej nazwie, bo liczy się tylko treść i&nbsp;rozszerzenie. Ja go nazwałem *moje.txt*.

Otwieramy ten plik w&nbsp;Notatniku i&nbsp;wklejamy tam ścieżkę do naszego folderu. Zapisujemy. Zmieniamy rozszerzenie pliku z&nbsp;*.txt* na *.pth*. Całość wygląda tak:

<img src="/assets/tutorials/python-extended/4-1-pth-file.webp" alt="Kolaż pokazujący kawałek folderu site_packages z dodanym plikiem pth, a także sam ten plik otwarty w notatniku. Zawiera jedną linijkę, C Skrypty."/>

{:.figcaption}
Jeden plik, w nim jedna ścieżka. To wszystko.

Sprawdzamy czy działa. Powtarzamy krok z&nbsp;punktu 0, czyli wpisujemy w&nbsp;IDLE linijka po linijce:

```python
import sys
for p in sys.path: print(p)
```

Tym razem na liście powinno wyświetlić również ścieżkę do naszego folderu:

{:.bigspace}
<img src="/assets/tutorials/python-extended/4-2-wlasny-folder.webp" width="400px" alt="Zrzut ekranu z IDLE pokazujący konsolę, a w niej wpisaną powyższą komendę. Widać, że pierwszy wyświetlony folder to 'C, skrypty'."/>

Od teraz możemy do niego dorzucać wszystkie swoje skrypty.

{% include info.html type="Uwaga" text="Jeśli ścieżka się nie pojawia, to możecie wyłączyć IDLE i&nbsp;włączyć go ponownie. Być może się nie zaktualizowało od poprzedniej sesji."%}

## 4. Szybkie włączanie PowerShella

Do tej pory pokazywałem, że można włączyć PowerShella przez klikanie menu z&nbsp;górnego rogu Eksploratora. Ale jeśli mamy go używać częściej, w&nbsp;różnych folderach, to warto poznać szybsze metody.

(Wielkie dzięki dla [tego](https://superuser.com/questions/1339064/keyboard-shortcut-to-open-powershell-from-the-desktop) i&nbsp;[tego](https://superuser.com/questions/1309679/open-powershell-as-administrator-at-current-file-explorer-directory-keyboard-sho) wątku ze StackOverflow).

Przede wszystkim podczas używania Eksploratora można nacisnąć `Shift + prawy przycisk myszy` na obszarze z&nbsp;listą plików.  
Kiedy klikamy z&nbsp;*Shiftem*, to **pokazuje się jedna dodatkowa opcja** -- *Uruchom w&nbsp;programie Windows PowerShell*.

Wada tej metody? Trzeba uważać, żeby zamiast pustej przestrzeni nie kliknąć jakiegoś pliku, bo pokazałyby się inne opcje. A&nbsp;to może być trudne, jeśli w&nbsp;folderze mamy ich dużo.

Poza tym da się jeszcze szybciej! Skrótami klawiszowymi, które niestety zależą od ustawionego języka Windowsa.  
W&nbsp;polskiej wersji naciskamy `Alt+P+O`, w&nbsp;angielskiej `Alt+F+O` (*O* jak *Open*).  
Dzięki temu mamy PowerShella w&nbsp;sekundę, w&nbsp;dowolnym folderze!

{% include info.html type="Porada" text="Jeśli macie wersję Windowsa w&nbsp;innym języku, to możecie po prostu przytrzymać `Alt` przez dłuższą chwilę, żeby wyświetliły się litery odpowiadające różnym elementom Eksploratora.  
Potem patrzycie, jakie klawisze odpowiadają opcji `Plik` i&nbsp;otwieraniu PowerShella. To te klawisze musicie nacisnąć w&nbsp;swojej wersji." trailer="<p class='bigspace' style='margin-bottom:0px'><img src='/assets/tutorials/python-extended/5-1-skroty-powershell.webp' alt='Zrzut ekranu z Eksploratora' width='400px'/></p>"%}

Z&nbsp;kolei żeby **szybko włączyć PowerShella w&nbsp;jego domyślnym miejscu** -- bez otwierania Eksploratora Plików -- naciskamy `Przycisk z ikoną Windowsa+X`, żeby wyświetlić okno z&nbsp;opcjami. A&nbsp;następnie `I` (literę podkreśloną w&nbsp;nazwie odpowiadającej PowerShellowi).

Przydaje się to, jeśli chcemy szybko odpalić przez PS skrypt robiący zawsze to samo, niezależnie od folderów. U&nbsp;mnie jest to na przykład skrypt otwierający w&nbsp;Firefoksie kilka stron z&nbsp;pogodą w&nbsp;górach.

## 5. Skrócenie komend dzięki plikowi BAT

Wyczerpaliśmy najłatwiejsze zmiany, teraz zrobi się dziwniej.

Niby wszystko jest cudownie, możemy odpalać skrypty z&nbsp;każdego folderu... Ale za każdym razem musimy wpisywać `python -m nazwa_skryptu`.

To co najmniej 11 znaków ze spacjami, nawet jeśli skrypt będzie miał najkrótszą jednoliterową nazwę. Z&nbsp;czasem może się znudzić!

Czy da się to przyspieszyć jeszcze bardziej? Bez grzebania w&nbsp;systemie i&nbsp;zmieniania czegoś na stałe?

Odpowiedź: tak. Da się zejść **do jednego znaku** w PowerShellu.  
Ale w&nbsp;tym celu trzeba zrobić lekką incepcję i&nbsp;stworzyć **skrypt Windowsa odpalający skrypt Pythona**.

Okazuje się, że Windows w tzw. *zmiennej PATH* przechowuje listę folderów, do których ma szybki dostęp. To tam trzeba się wprosić.  
Mam dobrą wiadomość: **nie musimy w&nbsp;niczym grzebać, Python sam podczas instalacji dodaje do _PATH_ kilka folderów**. Proponuję dorzucić się do jednego z nich, `Scripts`.

{% include info.html type="Porada" text="Jeśli chcecie się upewnić, że Python dodał folder *Scripts* do *PATH*, to wyświetlcie w&nbsp;PowerShellu zawartość *PATH*. Wpiszcie:" trailer="<div class='black-bg mono'>$env:path -split \";\"</div>" %}

Przechodzimy zatem do folderu `Scripts` w głównym folderze Pythona.  
Tak jak wcześniej tworzyliśmy dla Pythona plik *.pth* ze ścieżką do folderu, tak teraz stworzymy plik *.bat* -- skrót do konkretnego skryptu przeznaczony dla PowerShella.

Tworzymy plik o&nbsp;takiej nazwie, jaka nam pasuje, na przykład *z.txt* (to tę nazwę będziemy wpisywać, żeby odpalić skrypt). Wpisujemy w&nbsp;pliku:

```
@ECHO OFF
python -m witaj
```

(Pierwsza linijka jest tu po to, żeby skrypt *.bat* nie wyświetlał niczego od siebie, a&nbsp;jedynie rzeczy od Pythona.  
A druga linijka to dokładnie ta sama komenda, jaką byśmy sami odpalali skrypt Pythona przez PowerShell).

Całość wygląda tak:

{:.bigspace}
<img src="/assets/tutorials/python-extended/6-2-bat-file.webp" alt="Kolaż z trzech okien Windowsa. U góry widać pełną ścieżkę do folderu Scripts, poniżej jego zawartość z jednym dodanym plikiem 'z.txt'. Na samym dole znajduje się okno pokazujące plik z.txt otwarty w Notatniku, z podanym wyżej tekstem."/>

Zmieniamy nazwę pliku na *z.bat*. Od teraz po otwarciu PowerShella dałoby się po prostu nacisnąć `z` i&nbsp;`Enter`, żeby odpalić nasz skrypt. Jednoliterkowiec! :metal:

{:.bigspace}
<img src="/assets/tutorials/python-extended/6-3-witaj-bat.webp" width="300px" alt="Zrzut ekranu z PowerShella pokazujący wpisaną komendę 'z' i wyświetlone pod spodem słowa 'Witaj po ciemnej stronie'."/>

Gdybyśmy chcieli jeszcze bardziej ułatwić pracę, to już by mogło wymagać grzebania w&nbsp;systemie albo instalacji dodatków, takich jak AutoHotKey. Dlatego na tym etapie się zatrzymam.

{% include info.html type="Porada" text="Jeśli chcecie, żeby wasze pliki BAT miały bardziej opisowe nazwy, a&nbsp;nie jednoliterkowce, to da się to zrobić bez większej straty szybkości. Upewnijcie się tylko, że ich nazwy nie będą kolidowały z&nbsp;innymi programami dostępnymi przez PATH.  
Jeśli po wpisaniu w&nbsp;PowerShellu pierwszych liter nazwy naciśniecie `Tab` (a&nbsp;żaden inny plik z&nbsp;PATH się tak samo nie zaczyna), to wstawi Wam pełną nazwę pliku."%}

## Podsumowanie

W tym wpisie przeszliśmy długą drogę. Od świeżaków kopiujących skrypty i&nbsp;żmudnie klikających w&nbsp;okienka, gdy chcą ich użyć...  
Aż po „hakierów”, którym wystarczy pięć klawiszy (tu: `Alt`+`P`+`O`, literka, `Enter`), żeby przeczesać skryptem dowolny folder.

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
