---
layout: page
title: Co zrobić, jeśli nasz Linux nie umie otworzyć pustych plików?
description: "Chciałbym czymś wypełnić pustkę, ale system nie pozwala. Jak żyć?"
---

Od pewnego czasu zapoznaję się z&nbsp;systemem PorteuX -- jednym z&nbsp;wielu na bazie Linuksa (stopniowo zyskującego popularność). Urzekł mnie lekkością, minimalizmem i&nbsp;paroma nietypowymi rozwiązaniami.

{:.post-meta .bigspace-after}
Ogólnie: to system ładowany z&nbsp;pendrive'a, ciut podobny do prywatnościowego Tailsa. Nie chroni tak jak on, bo nie ma m.in. integracji z&nbsp;siecią Tor; daje co najwyżej łatwość rozpoczynania ulotnych sesji. Zyskujemy natomiast większą elastyczność, jeśli chodzi o&nbsp;uruchamianie programów z&nbsp;zewnątrz.

Oprócz zalet PorteuX miał jednak swoje zadziory, które sprawiały, że był w&nbsp;moich oczach w&nbsp;tyle względem Minta, którego używam na co dzień.  
W tym wpisie pokażę, jak wygładziłem jeden z&nbsp;takich zadziorów, którym było **utrudnione otwieranie pustych plików**.

{% include info.html
type="Na innych systemach"
text="Choć opisuję sprawę na przykładzie Porteuksa, informacje z&nbsp;tego wpisu powinny być łatwe do przeniesienia na inne Linuksy, gdyby pojawił się na nich ten sam problem (choć raczej się nie pojawi)."
%}

## Opis i&nbsp;rozwiązanie problemu

Załóżmy, że chcę sobie stworzyć nowy plik tekstowy. Może notatki na jakiś temat, który mi przyszedł do głowy? Krótki opis plików umieszczonych w&nbsp;tym samym folderze? Skrypt?

Bez znaczenia. W&nbsp;każdym razie: klikam prawym przyciskiem myszy pulpit albo pustą przestrzeń wewnątrz przeglądarki plików, żeby przywołać **menu kontekstowe**. Wybieram z&nbsp;niego opcję `Create Document`, a&nbsp;potem `Empty File`. Nowy plik powstaje bez problemu.

{:.figure .bigspace}
<img src="/assets/tutorials/linux/porteux-puste-pliki/porteux-tworzenie-nowego-pliku.png" alt="Zrzut ekranu pokazujący menu kontekstowe z&nbsp;zaznaczoną opcją stworzenia nowego pliku."/>

Teraz dwukrotnie klikam ten plik, żeby go otworzyć i&nbsp;zacząć w&nbsp;nim pracować. Na większości znanych mi Linuksów (Mincie, Fedorze KDE, Zorinie...) w&nbsp;tym momencie otworzyłby się domyślny „Notatnik” (edytor tekstu), umożliwiając zapełnienie pustki jakąś treścią.

...Ale na Porteuksie wyskakuje zamiast tego błąd. Komunikat mówi, że nie mam odpowiedniego programu do pracy z&nbsp;pustymi plikami.

{:.bigspace}
<img src="/assets/tutorials/linux/porteux-puste-pliki/porteux-otwieranie-nowego-pliku-blad.png" alt="Koomunikat o&nbsp;błędzie mówiący, że system nie ma programu do otwierania pustych plików."/>

Czemu są traktowane jak osobna, niewspierana kategoria? Skoro tak łatwo je stworzyć?  
Obstawiam niedopatrzenie twórców, bo z&nbsp;punktu widzenia używalności to mocny minus.

Na szczęście niedogodność nie będzie trwała długo, idą dwa sposoby na jej zażegnanie! Graficzny i&nbsp;konsolowy.

{% include info.html
type="Ciekawostka"
text="Choć zachowanie Porteuksa może budzić zdziwienie, wcale nie jest najgorszym systemem pod względem tworzenia nowych plików.  
Niektóre Linuksy (również bardzo popularny Ubuntu, gdy ostatnio sprawdzałem) w&nbsp;ogóle nie dają opcji stworzenia nowego pliku przez menu kontekstowe! Obawiam się, że może to zniechęcić niejedną osobę przyzwyczajoną do Windowsa."
trailer="<p class='post-meta'>To również jeden z&nbsp;kilku powodów, dla których polecam Minta zamiast Ubuntu.</p>"
%}

### Rozwiązanie przez klikanie

Najpierw należy kliknąć świeżo utworzony plik prawym przyciskiem myszy i&nbsp;wybrać opcję `Open With Other Application`.

{:.figure .bigspace}
<img src="/assets/tutorials/linux/porteux-puste-pliki/porteux-otwieranie-nowego-pliku-rozwiazanie-1.png" alt="Wybieranie z menu kontekstowego opcji otwarcia z użyciem innego programu"/>

Pokaże się lista dostępnych programów (nie wszystkich, ale tych „kompletniejszych”, posiadających własne ikony). Na tej liście należy znaleźć edytor tekstowy; w&nbsp;przypadku Porteuksa MATE nazywał się Pluma.

Następnie należy się upewnić, że zaznaczona jest **opcja zapamiętania aplikacji** w&nbsp;dolnej części okna. Jeśli tak, to należy kliknąć przycisk `Open`. Od teraz puste pliki będą się otwierały w&nbsp;edytorze tekstu. Problem rozwiązany.

{:.bigspace}
<img src="/assets/tutorials/linux/porteux-puste-pliki/porteux-otwieranie-nowego-pliku-rozwiazanie-2.png" alt="Kolaż pokazujący wybranie z listy programu Pluma z ikoną notatki i ołówka, a także zaznaczoną opcję zapisania tego programu."/>

{% include details.html summary="Metoda alternatywna (użycie szablonów)" %}

{:.bigspace-before}
Gdyby ktoś się zawziął, że nie zmieni domyślnych programów, ale nadal chce tworzyć nowe pliki przez menu kontekstowe i&nbsp;je szybko otwierać, to widzę pewne obejście.

Należy naszykować plik tekstowy z&nbsp;minimalną treścią; może być dosłownie jedna literka.  
Następnie trzeba go skopiować do folderu `Templates` (po polsku `Szablony`) w&nbsp;folderze domowym -- tam, gdzie są foldery takie jak `Music`, `Videos` itd.

{:.post-meta .bigspace-after}
Można to zrobić również konsolowo, komendą `cp PLIK ~/Templates`.

Od teraz w&nbsp;menu kontekstowym pod opcją tworzenia pustego pliku pojawi się również opcja stworzenia kopii tego, który dodaliśmy do szablonów.  
Będzie go można otworzyć zwykłym dwuklikiem, bo w&nbsp;oczach systemu jest plikiem tekstowym, a&nbsp;nie pustym.
 
Czy warto bawić się w&nbsp;takie obejścia, zamiast zmieniać domyślny program? Niekoniecznie :wink: Ale szablony tak czy siak się przydają, więc równie dobrze można się z&nbsp;nimi oswoić w&nbsp;taki właśnie sposób.

{% include details-end.html %}

### Sposób konsolowy

Zmiana domyślnego programu nie zajmuje zbyt wiele czasu. Ale i&nbsp;tak może być utrapieniem, zwłaszcza jeśli często ładujemy świeże sesje Porteuksa. W&nbsp;takim przypadku bardzo by pomógł jakiś skrypt, który będzie ustawiał za nas potrzebne rzeczy.

Najpierw robiłem wszystko metodą przez klikanie, ale z&nbsp;czasem odkryłem, gdzie system zapisuje przyporządkowania różnych plików do programów otwierających. A&nbsp;zapisuje je do pliku:

```
~/.config/mimeapps.list
```

Tylda oznacza tu folder domowy, kropka na początku nazwy `.config` wskazuje folder ukryty, zaś `mimeapps.list` to plik tekstowy (ściślej rzecz biorąc: konfiguracyjny, o&nbsp;określonej budowie).

{:.post-meta}
*Typy MIME* to z&nbsp;kolei wewnętrzna nazwa na różne kategorie plików; klasyfikacja ułatwiająca chociażby przydzielanie im programów.

{% include details.html summary="W jaki sposób znalazłem plik konfiguracyjny?" %}

Uniwersalnym sposobem, który polecam każdemu, kto chce ustalić kulisy działania swojego Linuksa:

* włączyłem przez menu kontekstowe okno pozwalające wybrać domyślny program (ale jeszcze nic nie kliknąłem);
* w&nbsp;osobnym oknie uruchomiłem konsolę;
* przez tę konsolę wywołałem program `xprop` (domyślnie zainstalowany na Porteuksie) i&nbsp;kliknąłem okno, żeby poznać różne informacje na jego temat (takie jak *PID*, czyli numer powiązanego procesu systemowego).
* następnie wywowłałem przez konsolę program `strace` (na Porteuksie musiałem go najpierw zainstalować), każąc mu obserwować powyższy proces i&nbsp;zapisywać wyniki do pliku:

  ```
  sudo strace -f -p NR_PROCESU -o PLIK.txt
  ```

* w&nbsp;oknie wyboru programu zaznaczyłem edytor tekstowy i&nbsp;kliknąłem OK, zamykając w&nbsp;ten sposób okno i&nbsp;kończąc monitorowanie;
* przeanalizowałem zapisy *strace'a*, szukając w&nbsp;szczególności interakcji z&nbsp;plikami.

  ```
  grep openat PLIK.txt
  ```

* znalazłem informację, że jednym ze zmienianych plików był wspomniany wyżej `mimeapps.list`;
* następnym razem, na świeżym systemie, porównałem wygląd tego konkretnego pliku przed i&nbsp;po ustawieniu domyślnego programu.

Jeśli kogoś interesują takie metody poznawania systemu, to mam na ten temat więcej miniwpisów, takich jak [ten o&nbsp;kulisach zmiany układu klawiatury](/miniposts/linux-mint-mate-klawiatura){:.internal}.

{% include details-end.html %}

Zaobserwowałem, co pojawia się w&nbsp;tym pliku po klikaniu opisanym na początku wpisu. Dodając identyczne linijki tekstu własnym skryptem, miałbym gotową automatyzację.

Ostatecznie zdecydowałem się to zrobić przez skrypt Pythona, bo łatwiej mi było go uodpornić na przypadki, gdy ktoś np. zmienia plik, w&nbsp;którym już ma własne ustawienia.

{:.post-meta .bigspace-after}
Bezmyślne wrzucanie nowego tekstu do takiego pliku mogłoby coś popsuć, zaś *configparser* używany przez Pythona korzysta z&nbsp;wytrzymalszych struktur.

Oto cała zawartość skryptu:

```python
from pathlib import Path
import configparser

cfgp = configparser.ConfigParser()
openers_list = Path.home() / '.config/mimeapps.list'
cfgp.read( openers_list )
for sec in ('Default Applications', 'Added Associations'):
    try: cfgp[sec]['application/x-zerosize'] = 'pluma.desktop'
    except KeyError:
        cfgp.add_section( sec )
        cfgp[sec]['application/x-zerosize'] = 'pluma.desktop'

with open(openers_list,'w') as cfile:
    cfgp.write( cfile )
```

{% include info.html
type="Uwaga"
text="Skrypt jest dopasowany do edytora tekstowego Pluma, obecnego na Porteuksie MATE; jeśli na naszym komputerze jest inny edytor, to należy ustalić, jaki wywoływacz mu odpowiada, i wstawić go wszędzie zamiast `pluma.desktop`."
%}

Skrypt można sobie zapisać na tego samego pendrive'a, na którym jest PorteuX, do jakiegoś pliku *umilacz.py*, a&nbsp;następnie uruchamiać rutynowo po załadowaniu świeżego systemu (`python umilacz.py`). Z&nbsp;czasem można całkiem zapomnieć o&nbsp;tym, że wstępne ustawienia były jakkolwiek irytujące.

Osobiście uczyniłem ten skrypt częścią większego, który „zmienia Porteuksa w&nbsp;Minta” (np. przenosząc pasek zadań z&nbsp;góry na dół ekranu). Nie ma sensu rezygnować z&nbsp;fajnego systemu przez drobne zadziory, kiedy Linux daje tyle możliwości ich oszlifowania.

Takiego dopasowania Linuksa pod siebie i&nbsp;komfortowego korzystania z&nbsp;niego życzę również Wam, drodzy czytelnicy! Oby do zobaczenia w&nbsp;kolejnych wpisach :smile:
