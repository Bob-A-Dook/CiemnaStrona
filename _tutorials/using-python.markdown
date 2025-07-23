---
layout: page
title: Pierwsze kroki z Pythonem
description: "Samouczek pokazujący pobieranie, instalację i pierwsze użycie języka programowania Python."
---

Do niektórych wpisów z&nbsp;Ciemnej Strony dodaję autorskie skrypty w&nbsp;języku Python. Dzięki nim możemy chociażby wyświetlać powiązania między firmami, szybko zgłaszać rosyjskie trolle albo usuwać wrażliwe dane ze zdjęć.

Zakładam, drodzy czytelnicy, że nie mieliście do czynienia z&nbsp;Pythonem. I&nbsp;może mieć nie chcecie, niezbyt Was interesuje. Chcecie po prostu użyć jakiegoś skryptu. Rozumiem to :wink:

Ale skrypty się same nie włączą. Żeby z nich skorzystać, musimy przynajmniej zainstalować i&nbsp;uruchomić Pythona. Całość trwa maksymalnie kilka minut i&nbsp;jest bardzo prosta. 

**Uwaga:** Pokazuję tutaj informacje tylko dla wybranych systemów. Na innych instalacja przebiega nieco inaczej, ale zwykle jest równie prosta.

## Instalowanie Pythona

### Na Windowsie

Najpierw odwiedzamy [oficjalną stronę Pythona](https://www.python.org/downloads/). Powinno samo nam podpowiedzieć najnowszą wersję:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/1-download.webp" alt="Zrzut ekranu ze strony Pythona. Na jaskrawym tle widać wersję proponowaną dla naszego systemu operacyjnego."/>

Pobieramy instalator -- w&nbsp;przypadku Windowsa będzie miał końcówkę *.exe*. Znajdujemy ten plik w&nbsp;folderze z&nbsp;pobranymi rzeczami i&nbsp;włączamy podwójnym kliknięciem.

{% include info.html type="Porada" text="Żeby nie szukać instalatora po folderach, można od razu po jego pobraniu kliknąć w&nbsp;ikonę pobranych plików z&nbsp;górnego paska (u mnie na przykładzie Firefoksa). Wyświetli się miniaturka pobranego pliku.  
Tutaj można po prostu kliknąć nazwę pliku *exe*, żeby go odpalić." trailer="<p class='figure'>
<img src='/assets/tutorials/python-basics/2-run.webp' alt='Rozwinięta zakładka z pobranymi plikami w przeglądarce Firefox. Wyróżniono nazwę pobranego pliku exe, w którą należy kliknąć.'/></p>"%}

Po włączeniu instalatora **najpierw zaznaczamy dolną opcję**, dodanie Pythona do *PATH* (zmiennych systemowych):

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/3-installer.webp" alt="Okno instalatora Pythona na Windowsie. Opcja na dole jest zaznaczona czerwoną ramką i widnieje przy niej cyfra 1. Zaznaczona jest też największa z opcji, mówiąca o domyślnej instalacji. Widać przy niej cyfrę 2."/>

Nie jest to obowiązkowe, ale ogromnie ułatwia życie -- dzięki temu jesteśmy w stanie przywoływać Pythona w dowolnym folderze prostą komendą `python`. Gdybyśmy tego nie zrobili, trzeba by zamiast tego podawać pełną ścieżkę do jego głównego pliku.

Opcję instalowania dla wszystkich użytkowników można odhaczyć. Zwłaszcza jeśli po prostu korzystamy z&nbsp;własnego komputera, na którym mamy jedno konto.

Potem **klikamy _Install Now_, domyślną opcję instalacji**.

Inna opcja to zainstalowanie tylko wybranych rzeczy. Ale ją odradzam. Wszystko z&nbsp;domyślnego pakietu się przyda. Szczególnie IDLE (edytor) i&nbsp;PIP (program do pobierania dodatków).

{% include info.html type="Porada"
text="Jeśli coś źle zaznaczymy podczas instalacji, to nie trzeba od nowa pobierać Pythona. Wystarczy ponownie kliknąć plik *exe* z&nbsp;instalatorem. Pojawi się możliwość zmiany ustawień."
%}

Instalacja powinna zająć tylko krótką chwilę, a&nbsp;otwiera przed nami cały świat skryptów.

### Na Linuksie

Pewna różnica względem Windowsa polega na tym, że Linux nie jest tak naprawdę jednym systemem. Istnieją różne jego warianty, nazywane *dystrybucjami*.

Osobiście korzystam z&nbsp;dystrybucji Linux Mint. Która pod względem działania oraz wyglądu jest dość podobna do Windowsa, więc łatwo się przestawić.

Okej. Więc żeby zainstalować Pythona na Mincie... **Zapewne nie musimy nic robić** :wink: Jest domyślnie dołączony do systemu!

Oczywiście może nas najść ochota, żeby zamiast domyślnej wersji skorzystać również z&nbsp;najnowszej. Tu już jest nieco więcej kroków, więc pozwolę sobie podlinkować [fajny poradnik](https://askaholic.io/installing-python-from-source/) po angielsku.

<details>
<summary>Kilka uwag do poradnika (kliknijcie, żeby rozwinąć)</summary>
<ul>
  <li>Plik z oficjalnej strony Pythona nie będzie miał formatu <em>exe</em>, tylko <em>tar.xz</em>.</li>
  <li>Trzeba otworzyć konsolę w tym samym folderze co ten plik.
   <p>W tym celu otwieramy Mintowy odpowiednik eksploratora plików i przechodzimy do odpowiedniego folderu.<br>
Klikamy prawym przyciskiem myszy gdzieś poza ikonami plików i wybieramy opcję <code class="language-plaintext highlighter-rouge">Otwórz w terminalu</code>. Można wybrać tę opcję również przez menu <code class="language-plaintext highlighter-rouge">Plik</code> w górnym lewym rogu.</p>
  </li>
  <li>Wszystkie rzeczy z&nbsp;poradnika pokazane na czarnym tle to komendy. Wpisujemy je w naszej konsoli, bez dolarka na początku.</li>
  <li>Jeśli ufamy w ciemno wersji ze strony Pythona, to możemy pominąć pierwsze punkty poradnika i&nbsp;przeskoczyć od razu do ostatnich dwóch komend z&nbsp;punktu&nbsp;1 (od <code class="language-plaintext highlighter-rouge">tar</code>).</li>
  <li>Do systemu Linux Mint odnoszą się polecenia spod nagłówka <em>Ubuntu</em>.</li>
</ul>
</details>

## Korzystanie ze skryptów

Każdy z&nbsp;moich skryptów zawsze zapewniam w&nbsp;formie pojedynczego pliku tekstowego z&nbsp;końcówką *.py*. Każdy z&nbsp;nich wykonuje tylko jedną, ściśle określoną rzecz.

Jeśli ma jakieś szczególne wymagania (np. potrzebuje dodatkowych modułów), to zawsze o&nbsp;tym wspominam.

Na potrzeby wprowadzenia naszykowałem dla Was <a href="/assets/tutorials/python-basics/witaj.py" download>skrypt przykładowy: <i>witaj.py</i></a>. Cała jego zawartość to:

```python
print('Witaj po ciemnej stronie!')
```

Po odpaleniu wyświetli dokładnie te słowa. Jest więc niegroźny i&nbsp;nic nie może zmienić. Idealny na start, można pobierać śmiało.  
Dalszy sposób korzystania jest bardzo podobny na różnych systemach. Opisuję działania na przykładzie Windowsa, ale Linux niewiele się różni.

### Na Windowsie

Otwieramy Eksploratora i&nbsp;przechodzimy do folderu, w którym jest plik.

Niestety Windows nie jest do końca przyjazny, jeśli chodzi o&nbsp;uruchamianie skryptów. **Gdybyśmy po prostu dwukrotnie kliknęli skrypt, to na chwilę mignie czarne okno, a&nbsp;potem zniknie**. Spróbujcie sami.

Nie zobaczymy przeznaczonego dla nas powitania.  
Gdyby, zamiast powitania, skrypt wyświetlał inny komunikat -- na przykład o konieczności pobrania czegoś -- to też byśmy go nie zobaczyli. Przyznam, że średnio jak na pierwsze wrażenie.

{:.post-meta .bigspace}
**Aktualizacja:** Od czasu napisania samouczka nieco dopracowałem skrypty wrzucane na bloga. O&nbsp;ile wszystko inne będzie OK, to powinny działać nawet po zwykłym podwójnym kliknięciu.

A co zrobić, jeśli skrypty zwyczajnie nie są przystosowane do uruchamiania przez podwójne kliknięcie?  
Po prostu trzeba je otworzyć w&nbsp;inny sposób -- na przykład przez IDLE, domyślny edytor Pythona, który zainstalowaliśmy w&nbsp;poprzednich krokach.

Aby otworzyć IDLE, wchodzimy w&nbsp;*Menu Start* na naszym Windowsie (ikona w&nbsp;lewym dolnym rogu). Są tam różne zakładki, ułożone alfabetycznie. Znajdujemy zakładkę `Python...` i&nbsp;ją rozwijamy:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/4-idle-run.webp" alt="Menu Start z Windowsa, zakładka dla Pythona."/>

Klikamy na `IDLE...`. Włączymy w&nbsp;ten sposób edytor IDLE w&nbsp;trybie ogólnym, interaktywnym:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/5-idle1.webp" alt="IDLE w trybie konsoli. Widać trzy brązowe strzałki, a za nimi puste pole, w które można wpisywać komendy."/>

Żeby otworzyć w&nbsp;nim teraz konkretny skrypt, wybieramy z&nbsp;górnego menu `File`, potem `Open` (albo naciskamy `Ctrl+O`, jak *Open*).

Pojawi się domyślne menu Windowsa od wybierania plików. Dzielnie przeklikujemy się do naszego skryptu *witaj.py* i&nbsp;go wybieramy. IDLE wyświetli go w&nbsp;drugim ze swoich trybów, trybie edycji:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/6-idle2.webp" alt="Otwarte okno IDLE w trybie edycji (pusta przestrzeń, w którą można wpisywać kod." width="500px"/>

Teraz możemy przejrzeć sobie treść skryptu, co w&nbsp;tym przypadku nie zajmie dużo czasu.

Naciskamy `F5`, żeby odpalić skrypt. Wyświetli się kolejne okno w&nbsp;trybie interaktywnym, pokazujące komunikaty. Wyświetlą nam się słowa „Witaj po ciemnej stronie!”.

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/7-idle3.webp" alt="IDLE w trybie konsoli z wyświetlonymi słowami."/>

Czyli wszystko działa, a&nbsp;świat Pythona stoi otworem.

Jeśli chcemy pójść o krok dalej i&nbsp;trochę ułatwić sobie pracę ze skryptami, to zapraszam do [rozszerzonego samouczka](/tutorials/python-extended).

## Pytania i odpowiedzi

### A jeśli nie działa?

W tym prostym przykładzie musielibyśmy się bardzo postarać, żeby coś nie zadziałało :wink:

Ale w innych przypadkach, zakładając że sam nie popełniłem błędów, przyczyną może być na przykład brak jakiegoś potrzebnego pakietu.

Dlatego warto uruchamiać skrypty przez IDLE lub inny program, **a&nbsp;nie podwójnym kliknięciem**. W&nbsp;ten sposób powinniśmy zobaczyć ewentualne komunikaty o&nbsp;błędach.

Inną przyczyną błędu może być nieumyślne naciśnięcie spacji podczas oglądania pliku. W&nbsp;takim wypadku treść komunikatu o&nbsp;błędzie powinna zawierać tekst `Syntax Error`.

W Pythonie spacje odgrywają kluczową rolę. Jeśli przypadkiem jakąś naciśniemy, przeglądając skrypt w&nbsp;trybie edycji, to może nam się przesunąć jakaś linijka kodu, sprawiając że całość przestanie działać.

Rozwiązanie tego błędu?  
W&nbsp;przypadku skryptów ode mnie **najłatwiej dla pewności pobrać skrypt jeszcze raz**. Nie otwierać go w&nbsp;innych programach, nawet w&nbsp;żadnym Notatniku, tylko od razu przez IDLE (albo inny program, jeśli ktoś woli). Nie zmieniać niczego, ani literki, i&nbsp;spróbować uruchomić skrypt.

### Czy potrzeba czegoś poza Pythonem?

Staram się, żeby każdy skrypt był niezależną całością. Ale nie zawsze jest to realne.

Dlatego niektóre skrypty **mogą wymagać dodatkowych modułów**. Jeśli tak jest, to zawsze o&nbsp;tym wspominam. Sam skrypt też powinien wyświetlać odpowiedni komunikat, jeśli mu czegoś brakuje.

Stworzyłem również krótki [samouczek na temat pobierania zewnętrznych modułów](/tutorials/using-pip). Przyda się w&nbsp;przypadku trafienia na skrypt wymagający czegoś poza podstawowym Pythonem.

### Czy to bezpieczne?

Dobrze, że pytacie! :smile: Przy pobieraniu nieznanych programów sceptycyzm zawsze na propsie.

Od siebie mogę jedynie powiedzieć: **zadbałem o&nbsp;bezpieczeństwo**.  
Żaden ze skryptów ode mnie nie jest wirusem. Nie łączy się z&nbsp;internetem. Unika „mieczy obosiecznych” -- funkcji grzebiących przy systemowych plikach.

Poza tym skrypty są bardzo zachowawcze i&nbsp;nie usuwają folderów (nawet tych tworzonych przez siebie; w&nbsp;końcu w&nbsp;międzyczasie mogliście tam nieuważnie wrzucić własne cenne pliki).

Ale w&nbsp;świecie komputerów wszystko jest względne. Do tego stopnia, że nawet twórcy [QubesOS](https://www.qubes-os.org/), systemu skupionego w&nbsp;100% na bezpieczeństwie, nazywają go jedynie *"a&nbsp;reasonably secure operating system"*.

Ktoś mógłby kiedyś przejąć moje konto i&nbsp;podmienić skrypty. Albo dodać złośliwy kod do samego Pythona, przez co niegroźne rzeczy staną się groźne. Innym razem niegroźne skrypty mogą zostać użyte do ataku, jeśli podrzuci im się zawirusowany plik.

W takich realiach trudno o&nbsp;absolutne gwarancje. Ale kod jest na widoku, a&nbsp;każda znająca się na tym osoba może go zweryfikować. To zawsze coś.
