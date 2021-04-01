---
layout: page
title: Pierwsze kroki z Pythonem
---

Niektóre wpisy z&nbsp;Ciemnej Strony zawierają linki do skryptów w&nbsp;języku Python. Dzięki nim możecie na własne oczy zobaczyć pewne rzeczy.

Zakładam, że nie mieliście do czynienia z&nbsp;Pythonem i&nbsp;mieć nie chcecie, niezbyt Was interesuje. Chcecie po prostu zobaczyć efekt. Rozumiem to :smile:

Ale skrypty się same nie odpalą. Musimy przynajmniej zainstalować Pythona i&nbsp;zobaczyć, jak je włączać. Całość trwa maksymalnie kilka minut i&nbsp;jest bardzo prosta. 

**Uwaga:** Pokazuję tutaj informacje dla Windowsa. Na innych systemach jest inaczej, ale czasem nawet prościej.

## Instalowanie Pythona

Najpierw odwiedzamy [oficjalną stronę Pythona](https://www.python.org/downloads/).  
Powinno samo Wam podpowiedzieć najnowszą wersję:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/1-download.webp" alt="Zrzut ekranu ze strony Pythona."/>

Pobieracie instalator -- w&nbsp;przypadku Windowsa będzie miał końcówkę *.exe*. Znajdujecie go w&nbsp;folderze z&nbsp;pobranymi rzeczami i&nbsp;włączacie podwójnym kliknięciem.

{% include info.html type="Porada" text="Nie musicie nawet chodzić po folderach. Od razu po pobraniu, pozostając w&nbsp;przeglądarce, kliknijcie w&nbsp;ikonę pobrania z&nbsp;górnego paska (u mnie na przykładzie Firefoksa). Wyświetli się miniaturka pobranego pliku.  
Tutaj możecie po prostu kliknąć nazwę pliku *exe*, żeby go odpalić." trailer="<p class='figure'>
<img src='/assets/tutorials/python-basics/2-run.webp' alt=''/></p>"%}

Po włączeniu instalatora **najpierw zaznaczcie dolną opcję**, dodanie Pythona do zmiennych systemowych:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/3-installer.webp" alt=""/>

Nie jest to obowiązkowe, ale ogromnie ułatwia życie -- gdybyśmy tego nie zrobili, to musielibyśmy czasem podawać pełną ścieżkę do jego plików.

Opcję instalowania dla wszystkich użytkowników możecie wyłączyć. Zwłaszcza jeśli po prostu korzystacie z&nbsp;własnego komputera, na którym jesteście jedynym użytkownikiem.

Potem **klikacie "Install Now", domyślną opcję instalacji**.

Inna opcja to instalacja tylko wybranych rzeczy. Ale ją odradzam. Wszystko z&nbsp;domyślnego pakietu się przyda. Szczególnie IDLE (edytor) i&nbsp;PIP (program do pobierania dodatków).

{% include info.html type="Porada" text="Jeśli coś źle zaznaczyliście podczas instalacji, to nie musicie od nowa pobierać Pythona. Możecie ponownie kliknąć plik *exe* z&nbsp;instalatorem. Pojawi się możliwość zmiany ustawień."%}

Całość powinna zająć krótką chwilę. A&nbsp;otwiera przed Wami cały świat skryptów.

## Korzystanie ze skryptów

Każdy z&nbsp;moich skryptów zawsze zapewniam w&nbsp;formie pojedynczego pliku tekstowego z&nbsp;końcówką *py*. Każdy z&nbsp;nich wykonuje tylko jedną, ściśle określoną rzecz.

Jeśli ma jakieś szczególne wymagania (np. potrzebuje dodatkowych modułów), to zawsze o&nbsp;tym wspominam.

Na potrzeby wprowadzenia naszykowałem dla Was <a href="/assets/tutorials/python-basics/witaj.py" download>skrypt przykładowy: <i>witaj.py</i></a>.

Cała jego zawartość to:

```python
print('Witaj po ciemnej stronie!')
```

Po odpaleniu wyświetli dokładnie te słowa. Jest więc niegroźny i&nbsp;nic nie może zmienić. Idealny na start.

Pobierzcie go, umieśćcie w&nbsp;dowolnym folderze i&nbsp;otwórzcie ten folder.

Niestety Windows nie jest do końca przyjazny, jeśli chodzi o&nbsp;uruchamianie skryptów. **Gdybyśmy po prostu go dwukrotnie kliknęli, to nic się nie stanie**. Na chwilę mignie czarne okno, a&nbsp;potem zniknie.

Przyznam, że niefajne pierwsze wrażenie. Ale na szczęście skrypty działają, tylko po prostu trzeba je otworzyć w&nbsp;inny sposób -- na przykład przez IDLE, domyślny edytor Pythona.

Aby go otworzyć, wchodzimy w&nbsp;menu Start (ikona w&nbsp;lewym dolnym rogu). Zakładki są tam ułożone alfabetycznie. Znajdujemy zakładkę `Python...` i&nbsp;ją rozwijamy:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/4-idle-run.webp" alt=""/>

Klikamy na `IDLE...`. Włączymy w&nbsp;ten sposób edytor IDLE w&nbsp;trybie ogólnym, interaktywnym:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/5-idle1.webp" alt=""/>

Żeby otworzyć w&nbsp;nim teraz konkretny skrypt, wybieramy z&nbsp;górnego menu `File`, potem `Open` (albo naciskamy `Ctrl+O`, jak *"Open"*).

Pojawi się domyślne menu Windowsa od wybierania plików. Dzielnie przeklikujemy się do naszego skryptu *witaj.py* i&nbsp;go wybieramy. IDLE wyświetli go w&nbsp;drugim ze swoich trybów, trybie edycji:

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/6-idle2.webp" alt=""/>

Teraz możemy przejrzeć sobie treść skryptu, co w&nbsp;tym przypadku nie zajmie dużo czasu.

Naciskamy `F5`, żeby odpalić skrypt. Wyświetli się kolejne okno w&nbsp;trybie interaktywnym, pokazujące komunikaty. Wyświetlą Wam się słowa „Witaj po ciemnej stronie!”.

{:.figure .bigspace}
<img src="/assets/tutorials/python-basics/7-idle3.webp" alt=""/>

Czyli wszystko działa, a&nbsp;świat Pythona stoi otworem.

Jeśli chcecie pójść o krok dalej i trochę ułatwić sobie pracę ze skryptami, to zapraszam do [rozszerzonego samouczka]({{site.url}}/tutorials/python-extended).

# A&nbsp;jeśli nie działa?

W tym prostym przykładzie musicie się bardzo postarać, żeby coś nie zadziałało :wink:

Ogólnie warto pamiętać, że w&nbsp;Pythonie różne znaki (zwłaszcza spacje!) odgrywają kluczową rolę. Jeśli przypadkiem coś naciśniecie, przeglądając skrypt w&nbsp;trybie edycji, to może przestać działać.

Rozwiązanie? W&nbsp;przypadku skryptów ode mnie najłatwiej **po prostu pobrać skrypt jeszcze raz**. Nie otwierać go w&nbsp;niczym innym, nawet w&nbsp;żadnym Notatniku, tylko od razu przez IDLE. Nie zmieniać niczego, ani literki, i&nbsp;po prostu odpalić `F5`.

# Czy potrzeba czegoś więcej?

Staram się, żeby każdy skrypt był niezależną całością. Ale nie zawsze jest to realne.

Dlatego niektóre skrypty **mogą wymagać dodatkowych modułów**. Jeśli tak jest, to zawsze o&nbsp;tym wspominam. Sam skrypt też powinien wyświetlać odpowiedni komunikat, jeśli mu czegoś brakuje.

Stworzyłem również krótki [samouczek na temat pobierania zewnętrznych modułów]({{site.url}}/tutorials/using-pip).  
Skorzystajcie z&nbsp;niego, jeśli zetkniecie się z&nbsp;czymś, co potrzebuje dodatków.

# Czy to bezpieczne?

Dobrze, że pytacie! :smile: Przy pobieraniu nieznanych programów sceptycyzm zawsze na propsie.

Od siebie mogę jedynie powiedzieć: **zadbałem o&nbsp;bezpieczeństwo**.

W tym sensie, że żaden ze skryptów ode mnie to nie wirus. Nie łączy się z&nbsp;internetem. Unika „mieczy obosiecznych” -- funkcji, które grzebią przy systemie.

Poza tym skrypty są bardzo zachowawcze i&nbsp;nie usuwają folderów (nawet tych tworzonych przez siebie; w&nbsp;końcu w&nbsp;międzyczasie mogliście tam nieuważnie wrzucić własne cenne pliki).

Ale w&nbsp;świecie komputerów wszystko jest względne. Do tego stopnia, że nawet twórcy [QubesOS](https://www.qubes-os.org/), systemu skupionego w&nbsp;100% na bezpieczeństwie, nazywają go jedynie *"a reasonably secure operating system"*.

Ktoś kiedyś może przejąć moje konto i&nbsp;podmienić skrypty. Albo dodać złośliwy kod do samego Pythona, przez co niegroźne rzeczy staną się groźne. Innym razem niegroźne skrypty mogą zostać użyte do ataku, jeśli podrzuci im się zawirusowany plik.

W takich realiach trudno o&nbsp;absolutne gwarancje. Ale kod jest na widoku, a&nbsp;każda znająca się na tym osoba może go zweryfikować. To zawsze coś.
