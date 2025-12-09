---
layout: page
title: Linux i ustawienia Dconf. Przejście od menu do konsoli
description: "Menu graficzne są przyjemne, ale konsola też może taka być."
---

Systemy na bazie Linuksa to świetna alternatywa dla Windowsa, ale krąży wokół nich parę głupich stereotypów. Jak ten: „Linux jest dla nerdów i&nbsp;trzeba na nim używać konsoli nawet do najprostszych rzeczy”.

To mit. Obecnie istnieje wiele przyjaznych systemów na bazie Linuksa (jak choćby Linux Mint), które pozwalają zmieniać większość ustawień przez przystępne, uporządkowane menu graficzne.

Nie jest natomiast mitem, że konsola ułatwia życie. Pozwala osiągnąć w&nbsp;sekundę to, co wymagałoby paru minut klikania w&nbsp;menu. Dlatego staram się pokazywać obie metody, graficzną i&nbsp;konsolową, obok siebie. Jak we [wpisie o&nbsp;ustawianiu języka polskiego](/tutorials/linux-mint-jezyk-polski-system.html){:.internal}.

Tak będzie również tutaj. Pokażę, **jak ustalić komendy konsolowe odpowiadające ustawieniom z&nbsp;menu** (a&nbsp;przynajmniej tym, które są zapisywane w&nbsp;systemowej bazie).

W ten sposób mam nadzieję podarować czytelni(-cz)kom uniwersalny sposób na dostosowanie systemu pod siebie.

Będzie prosto i&nbsp;przystępnie. Nie trzeba znać konsoli, wystarczy gotowość do czytania (nie taka oczywistość w&nbsp;dobie TikToka!) i&nbsp;kopiowania podsuwanych przeze mnie poleceń.

{% include info.html
type="Drobne uwagi"
text="Zrzuty ekranu z&nbsp;tego wpisu pochodzą z&nbsp;minimalistycznego systemu PorteuX. Na innych, popularniejszych Linuksach interfejs będzie wyglądał inaczej/lepiej.  
Jeśli ktoś czyta na wąskim ekranie, to część kodu nie zmieści się na szerokość. Ciemne pola można w&nbsp;takim wypadku przewijać w&nbsp;poziomie."
%}

## Konsola i&nbsp;Dconf -- pierwsze kroki

Wpis kręci się wokół konsoli, zwanej też Terminalem, więc można zacząć od jej uruchomienia :wink:

W tym celu można kliknąć ikonę z&nbsp;paska (powiedziałbym „dolnego”, ale na niektórych Linuksach jest domyślnie boczny). Taką czarną, nieraz z&nbsp;dolarkiem w&nbsp;rogu. Często działa też skrót klawiszowy `Ctrl+Alt+T`.

Pojawi się okno z&nbsp;nazwą użytkownika i&nbsp;migającym kursorem. Można tu wpisywać polecenia dla komputera, a&nbsp;ten będzie je wykonywał.

Proponuję najpierw zobaczyć, czy nasz system ma w&nbsp;ogóle ustawienia w&nbsp;formacie pasującym do tego samouczka.  
W tym celu trzeba wpisać w&nbsp;konsolę:

```
dconf
```

Następnie należy nacisnąć `Enter`.

{:.post-meta .bigspace-after}
Takie coś -- wpisanie polecenia i&nbsp;potwierdzenie klawiszem -- to *użycie (albo wykonanie) polecenia (albo komendy)*. Tak to od teraz będę określał.

Jeśli pojawi się tekst zaczynający się od takich linijek:

{:.post-meta}
```
error: no command specified

Usage:
  dconf COMMAND [ARGS...]
```

...To znaczy, że nasz Linux ma Dconfa, centralną bazę ustawień :smile: Wszystko OK, można jechać dalej.

Jeśli wyskoczy informacja, że polecenie `dconf` jest nieznane, to znaczy że Dconfa niestety nie mamy. Przykro mi! Ale nadal zapraszam do doczytania samouczka, bo parę rzeczy będzie uniwersalnych.

{% include info.html
type="Porada"
text="Domyślnie do konsoli wkleja się rzeczy skrótem `Ctrl+Shift+V`, a&nbsp;kopiuje przez `Ctrl+Shift+C`. Sporo osób się na tym nacina.  
Osoby bardziej myszkowe będą miały łatwiej; po kliknięciu obszaru konsoli prawym przyciskiem myszy, mogą po prostu wybrać opcję kopiowania/wklejania z&nbsp;menu."
%}

### O&nbsp;programie Dconf

Każdy pstryczek, jaki da się zmieniać przez czytelne menu, ma jakiś swój zakulisowy odpowiednik. Zapewne jakiś plik, w&nbsp;którym znajduje się etykieta, zaś obok niej -- wartość.  
Programy wczytują te ustawienia i&nbsp;zmieniają na ich podstawie swoje zachowanie.

W dawnych czasach niemal każdy program trzymał własne pliki z&nbsp;ustawieniami. Ale było to nieporęczne, więc niektórzy twórcy Linuksów pokusili się o standaryzację.

Tak powstał **_Dconf_ -- centralna baza z&nbsp;ustawieniami**. Coś w&nbsp;stylu rejestru Windowsa, ale prostsze i&nbsp;pod wieloma względami czytelniejsze.

Nie każdy program korzysta z&nbsp;tej bazy, nawet jeśli jest dostępna. Przykładowo duże i&nbsp;niezależne, jak Firefox, raczej zarządzają własnymi ustawieniami i&nbsp;nie integrują się z&nbsp;systemem.

Jest natomiast spora szansa, że jeśli mamy Dconfa, to korzystają z&nbsp;niego **programy systemowe**. Wszelkiej maści menu od sterowania zasilaniem, systemowymi skrótami klawiszowymi, zachowaniem myszki...

Takie programy można łatwo kontrolować, „rozmawiając” przez konsolę bezpośrednio z&nbsp;Dconfem. Ale jakich słów użyć? Już pokazuję, jak się tego dowiedzieć.

## Co się zmieniło?

Jestem wielkim fanem praktycznych przykładów, dlatego oprę ten wpis na własnej historii. **Użyję Dconfa do zmiany ustawienia zasilania**.

Kontekst? Domyślnie mój laptop na Porteuksie MATE miał włączone przyciemnianie ekranu, kiedy zaczynał ciągnąć prąd z&nbsp;baterii zamiast z&nbsp;kabla. Miało to zaletę (możliwość dłuższego korzystania), ale czasem irytowało.  
Postanowiłem stworzyć sobie skrypt, który wyłącza mi na życzenie tryb oszczędny.

{:.post-meta .bigspace-after}
U siebie zmieniam właściwie dwie opcje, ale dla uproszczenia skupię się tu na jednej.

Gdybym chciał zmienić ustawienie metodą klasyczną, to kliknąłbym w&nbsp;ikonę na pasku, wybrał zakładkę `System`, potem `Preferences`, `Hardware` i&nbsp;`Power Management`.  
W otwartym w&nbsp;ten sposób menu wszedłbym w&nbsp;zakładkę `On Battery Power` i&nbsp;zmienił tam opcję odpowiedzialną za przyciemnianie.

{:.post-meta}
Ale jeszcze się wstrzymajmy z klikaniem, na razie tylko gdybam.

{:.bigspace}
<img src="/assets/tutorials/linux/dconf/porteux-bateria-brak-przyciemniania-ekranu.png" alt="Kolaż pokazujący różne okna, jakie należy kliknąć, żeby wyłączyć przyciemnanie ekranu na Porteuksie"/>

Fakt, przed jakim stałem: „gdy kliknę tę opcję, coś się zmieni na poziomie pierwotnym”. Założenie: to może być zmiana wewnątrz Dconfa.  
Skoro zmiana i&nbsp;skoro Dconf, to zarysowało się rozwiązanie -- **porównać stan Dconfa przed zmianą ze stanem po zmianie**.

Najpierw stan przed zmianą. Mam okno z&nbsp;ustawieniami pod ręką, opcję *jeszcze niewyłączoną*. Przechodzę do konsoli i&nbsp;robię **zrzut wszystkich ustawień Dconfa do pliku**:

```
dconf dump / > dc1
```

{% include details.html summary="Omówienie komendy" %}

Zacznę od rzeczy przed strzałką. Ogólnie mamy tu `dconf dump ŚCIEŻKA`, gdzie `dconf` to program nadrzędny, `dump` to jego podprogram. Całość mówi „zrób zrzut tej części bazy”, albo inaczej: „pokaż mi wszystkie ustawienia, jakie masz w&nbsp;tym miejscu”.

„To miejsce”, czyli `ŚCIEŻKA`, odwołuje się do hierarchii wewnątrz Dconfa. Wstawiając tu sam ukośnik (`/`), wskazuję, żeby zacząć zrzut od samej góry. Czyli w&nbsp;praktyce mówię: „zrób zrzut *wszystkich* ustawień”.

Normalnie ustawienia te wyświetliłyby się w konsoli. Ale dzięki strzałce (`>`) trafią zamiast tego do pliku o&nbsp;nazwie wskazanej po jej prawej stronie.

Z kolei `dc1` to czysto subiektywna nazwa pliku, do którego chcę zapisać zrzut. Na Linuksie nie trzeba dodawać końcówki w&nbsp;stylu `.txt`. I&nbsp;tak wyjdzie plik tekstowy, a&nbsp;do tego bez końcówki będzie można łatwiej edytować nazwę w kolejnym punkcie.

{% include details-end.html %}

Po wykonaniu zrzutu wracam do graficznego menu. Odznaczam tam niechcianą opcję -- ustawiam, żeby nie przyciemniało ekranu. Mogę też zamknąć menu graficzne, nie będzie mi potrzebne.

Teraz czas na kolejny zrzut przez konsolę (ważne: do pliku o&nbsp;innej nazwie niż poprzednio!).

```
dconf dump / > dc2
```

{% include info.html
type="Porada"
text="Zamiast wpisywać wszystko od nowa, można nacisnąć wewnątrz konsoli **klawisz ze strzałką w&nbsp;górę**. W&nbsp;ten sposób wstawi się poprzednio użyta komenda. Wystarczy teraz zmienić nazwę pliku wyjściowego, zmieniając ostatnią cyfrę."
%}

Potem porównanie zrzutów. W&nbsp;roli porównywacza program `diff` (od *difference*):

```
diff dc1 dc2
```

Powinna pojawić się linijka w&nbsp;tym stylu:

{:.post-meta}
```
311a312
> idle-dim-battery=false
```

Liczba u&nbsp;góry nie ma większego znaczenia; liczą się linijki rozpoczynające się od strzałek.

Czy to tego szukałem? Trzeba się zdać na znajomość angielskiego.  
Jest `battery`, `idle` to bezczynność, `dim` to przyciemnianie. Wartość `false` -- czyli przyciemnienie zostało zapewne *wyłączone*. Pasuje idealnie!

{% include details.html summary="Gdyby pokazały się inne rzeczy" %}
Jeśli po użyciu polecenia `diff` nic się nie pokazało, to znaczy że nasza zmiana wykonana przez klikanie menu nie pociągnęła za sobą zmian w&nbsp;Dconfie. **Zapewne badany program zapisuje ustawienia gdzie indziej**.

Ustalenie miejsca, w&nbsp;którym to robi, może być ciutkę bardziej upierdliwe, ale nadal do przeżycia. W&nbsp;takim wypadku zapraszam do [miniwpisu o programie *strace*](/miniposts/linux-mint-mate-klawiatura.html){:.internal}.

Czasem, jeśli zmiana opcji stworzyła nową kategorię, oprócz linijki z&nbsp;wartością pojawi się ścieżka zawierająca ukośniki i&nbsp;nawiasy kwadratowe po bokach; na razie można się nią nie przejmować, jeszcze o&nbsp;niej wspomnę.

Czasem może się też pojawić więcej linijek, które niekoniecznie dotyczą naszego ustawienia.

Przykładowo: jeśli niektóre sugerują coś związanego z&nbsp;rozmiarem lub ustawieniem okien (jak np. `size=(1002, 716)`), to można je zignorować. Wynikają zapewne z&nbsp;tego, że między zrzutami ustawień lekko zmieniliśmy rozmiar okna. A&nbsp;Dconf zapamiętuje nawet takie detale.

To dlatego gorąco radzę, żeby zrobić zrzut tuż przed zmianą i&nbsp;tuż po niej, nie ruszając niczego innego. Będzie mniej szumu w&nbsp;danych.

{% include details-end.html %}

## Ustalenie pełnej ścieżki

Znamy nazwę i wartość nowego ustawienia. To już o&nbsp;krok od sukcesu... Tylko że to tak, jakbyśmy ustalili, jakie konkretne słowa powiedzieć konkretnemu człowiekowi. A&nbsp;nie wiemy, pod jakim adresem go znaleźć.

Przed nami jeszcze ustalenie **kategorii (ścieżki wewnątrz Dconfa)**.  
W praktyce: chcemy znaleźć pierwszy tekst w&nbsp;**nawiasach kwadratowych** nad nowo dodanym ustawieniem.

Można to zrobić przez dopisanie do komendy porównującej pliki argumentu `-U 10`. Wyśwetli on wtedy *kontekst*: po 10&nbsp;linijek przed zmianą i&nbsp;po zmianie:

```
diff -U 10 dc1 dc2
```

Jedziemy wzrokiem od nazwy ustawienia (`idle-dim-battery`) w&nbsp;górę. Jeśli nie widać jeszcze niczego z&nbsp;nawiasami kwadratowymi -- to trzeba poszerzyć kontekst, zwiększając liczbę linijek.

W końcu naszym oczom powinna się ukazać pełna ścieżka do zmienionego ustawienia. Zaznaczyłem na czerwono ją oraz ustawienie, od którego wyszliśmy:

<div class="black-bg mono">
<br/>
 <span class="red">[org/mate/power-manager]</span><br/>
 ...inne linijki...<br/>
 icon-policy='always'<br/>
<span class="red">+idle-dim-battery=false</span><br/>
 sleep-computer-ac=1800<br/>
 sleep-display-ac=600<br/>
 <br/>
 [org/mate/screenshot]<br/>
 border-effect='none'</div>

{% include details.html summary="Sposób alternatywny" %}

Jeśli podgląd przez program `diff` nie do końca nam pasuje, to można też otworzyć zrzut numer dwa w&nbsp;programie `less`:

```
less dc2
```

Potem można nacisnąć ukośnik (`/`) (żeby przejść w&nbsp;tryb wyszukiwania) i&nbsp;wkleić po nim charakterystyczny fragment znalezionej nazwy ustawienia. Tu na przykład `idle-dim`.

Potem można przewinąć ekran myszą albo strzałką w&nbsp;górę, aż pokaże się pełna ścieżka.

Żeby wyjść z&nbsp;tego podglądu, należy nacisnąć `Q` (niejedna osoba pozostała uwięziona wewnątrz *lessa*!).

{% include details-end.html %}

## Przekształcenie na polecenie konsolowe

Mając pełną ścieżkę, nazwę i&nbsp;wartość ustawienia, stoimy przed taką konstrukcją:

<div class="black-bg mono bigspace-before">
[<span style="color:#88334e">org/mate/power-manager</span>]<br/>
...<br/>
<span style="color:#e47648">idle-dim-battery</span>=<span style="color:#be102e">false</span></div>

{:.figcaption}
Kolory dodałem dla czytelności, w&nbsp;konsoli oczywiście paleta jest biało-czarna.

Można to teraz przekształcić na **bezpośrednie polecenie dla Dconfa**, każące mu ustawić konkretną wartość. 
Jego ogólna postać jest taka:

<pre class="black-bg mono bigspace">
dconf write <strong>/</strong><span style="color:#88334e">ŚCIEŻKA</span><strong>/</strong><span style="color:#e47648">NAZWA</span> <span style="color:#be102e">WARTOŚĆ</span></pre>

Mogę kopiować fragmenty tekstu ze zrzutu Dconfa i&nbsp;wklejać je do jakiegoś osobnego pliku tekstowego, dopisując parę znaków ręcznie. Stopniowo ułoży mi się komenda.

{:.post-meta .bigspace-after}
Uczulam na **ukośnik na początku ścieżki** oraz spację (zamiast `=`) między nazwą a&nbsp;wartością!  
Poza tym przypominajka: żeby coś skopiować z&nbsp;konsoli, trzeba użyć kombinacji <code>Ctrl+<span class="red">Shift</span>+C</code>.

Efekt końcowy:

<pre class="black-bg mono bigspace">
dconf write /<span style="color:#88334e">org/mate/power-manager</span>/<span style="color:#e47648">idle-dim-battery</span> <span style="color:#be102e">false</span>
</pre>

Użycie tej linijki wewnątrz konsoli albo skryptu konsolowego pozwoli osiągnąć w&nbsp;sekundę ten sam efekt co dłuższe klikanie w&nbsp;menu.  
Można ją sobie zapisać w bezpiecznym miejscu.

## Na co uważać

Tutaj było łatwo, bo ustawiałem tylko prostą wartość `false` (zmienną zero-jedynkową). Pewne niuanse pojawiają się, kiedy wartością jest tekst (otoczony cudzysłowami) albo lista (między nawiasami kwadratowymi; nie mylić z&nbsp;tymi w&nbsp;ścieżce Dconfa z&nbsp;przykładu).

{% include details.html summary="Co zrobić przy innych wartościach" %}

{:.bigspace-before}
Jeśli wartością jest tekst między cudzysłowami pojedynczymi, to należy **otoczyć go dodatkowo cudzysłowami podwójnymi**.

Czyli na przykład ustawienie z&nbsp;Dconfa:  
`button-power='shutdown'`

wyglądałoby w&nbsp;skrypcie tak:  
`button-power "'shutdown'"`.

Dlaczego tak jest? Bo końcowy Dconf *musi* otrzymać dokładnie to, co wyświetla się w zrzucie ustawień. Czyli tutaj: tekst otoczony cudzysłowami.  
A podajemy mu ten tekst przez konsolę, która robi po drodze różne przekształcenia i&nbsp;**usuwa najbardziej zewnętrzną parę cudzysłowów** (jeśli jakaś jest).

Użycie dwóch par pozwala sprostać tym ograniczeniom. Konsola zerwie sobie jedną, druga zostanie dla Dconfa.

{:.post-meta .bigspace-after}
Można pomyśleć intuicyjnie, że otaczanie cudzysłowami jest jak opakowanie czegoś w&nbsp;karton. Jeden zawsze zostanie zdarty w&nbsp;konsolowym transporcie.  
A kiedy mamy karton w&nbsp;kartonie, to nawet po zdarciu tego zewnętrznego klient-Dconf dostanie elegancko zapakowaną zawartość.

A dlaczego używam różnych rodzajów cudzysłowów? Bo gdybym dał pojedyncze i&nbsp;na zewnątrz, i&nbsp;w środku (<code class="red">''shutdown''</code>), to podczas przetwarzania dane zaczęłyby być traktowane jak tekst po `'` otwierającym, a&nbsp;przestały nim być po napotkaniu drugiego. To doprowadziłoby do różnorakich błędów.

Analogicznie przy listach w&nbsp;nawiasach. Przy takiej liście:

`['windowmanager', 'panel', 'filemanager']`

...Nie trzeba się skupiać na cudzysłowach pojedynczych wewnątrz niej. Wystarczy jedna para podwójnych. Na początku i&nbsp;na końcu. Konsola je obedrze, a&nbsp;do Dconfa trafi dokładnie to, co w&nbsp;polu wyżej.

`"['windowmanager', 'panel', 'filemanager']"`

{% include details-end.html %}

Poza tym jest też kwestia tego, *kiedy* warto zmieniać Dconfa przez konsolę.

Przykład pozytywny? Proste, jednorazowe opcje. Gdy na przykład chcemy sobie zrobić prowizoryczny przełącznik między dwoma trybami, z&nbsp;których każdy ma inne ustawienia (zostawiam waszej kreatywności).

Przykład negatywny? **Nie polecam dodawania ikon na pasku przez bezpośrednie zmiany Dconfa**.  
To dlatego, że reguły ich dodawania są ciut bardziej złożone -- ikony są numerowane i&nbsp;ma spore znaczenie, co było dodawane pierwsze, ile ikon mamy obecnie itd.

Gdyby skrypt mówił zawsze i&nbsp;niezmiennie: „dodaj skrót do narzędzia X&nbsp;w czwartej zakładce” -- to mógłby coś popsuć,  gdyby nasz pasek został w&nbsp;jakikolwiek sposób zmieniony względem stanu domyślnego.

## Bonus: przykład praktyczny

Osobiście wkręciłem się w używanie systemów w&nbsp;trybie *live*. Oznacza to, że za każdym razem ładuję z pendrive'a nowy, świeży system z&nbsp;domyślnymi ustawieniami. Taki jak wspomniany już PorteuX w&nbsp;wersji MATE.

A że parę jego domyślnych ustawień wybitnie mi nie leży, to lubię je każdorazowo zmieniać. Gdybym musiał to ciągle robić przez menu graficzne, to bym chyba osiwiał.

Ale dzięki istnieniu sposobu konsolowego po prostu podpatrzyłem, co się zmienia wewnątrz Dconfa. I&nbsp;stworzyłem skrypt, który wydaje mu bezpośrednie polecenia.

{% include details.html summary="Fragment mojego skryptu" %}

```bash
# Kierunek przewijania touchpada w stylu smartfona, nie kółka myszy
dconf write /org/mate/desktop/peripherals/touchpad/natural-scroll true

# Otwieranie konsoli kombinacją Ctrl+Alt+T
dconf write /org/mate/marco/global-keybindings/run-command-terminal "'<Primary><Alt>t'"

# Brak przyciemniania ekranu przy zasilaniu z baterii
dconf write /org/mate/power-manager/backlight-battery-reduce false
dconf write /org/mate/power-manager/idle-dim-battery false
```
{% include details-end.html %}

{:.post-meta .bigspace-after}
Uczulam osoby, które chciałyby skopiować komendy, że zadziała to tylko na Linuksach ze środowiskiem MATE. Na innych, nawet mających Dconfa, byłyby inne ścieżki.

Dzięki temu mogę nosić ze sobą znajome środowisko, nawet jeśli za każdym razem ładuję świeży system. Parę dodatkowych sekund -- i&nbsp;wszystko ustawia się pode mnie.

Polecam takie życie. To jak każdorazowe resetowanie mieszkania do stanu surowego, po czym teleportowanie do niego sprawdzonych sprzętów :smile:

{% include info.html
type="Powiązane wpisy"
text="Wpis jest częścią wielkiej fali poradników ułatwiających przechodzenie na Linuksa. To rodzina systemów znacznie bardziej szanujących użytkowników niz Windows. Ma teraz [niepowtarzalną okazję, żeby się przebić](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal} i&nbsp;zjednać sobie szersze grono.  
Jeśli ktoś chce dać głębszego nura w&nbsp;odkrywanie, co się dzieje w&nbsp;ustawieniach pod powierzchnią, to polecam [wpis na temat języka na Mincie MATE](/miniposts/linux-mint-mate-klawiatura.html){:.internal}. Ostatecznie kończę tam na Dconfie, ale jest przy okazji cała ścieżka rozumowania, która pomogłaby też przy innych plikach z&nbsp;ustawieniami.  
Mam też wpis, w&nbsp;którym próbuję tego samego [na Mincie Cinnamonie, ale bezskutecznie](/miniposts/cinnamon-klawiatura.html){:.internal}. W&nbsp;końcu cały czas się uczę :wink:"
%}
