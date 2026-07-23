---
layout: page
title: "Linux Mint Cinnamon – jak sprawić, żeby ikony na pasku zachowywały się jak na Windowsie"
description: "Nawet zwykłym dolnym paskiem można dostać po tyłku."
---

Linux Mint to jeden z&nbsp;najprzyjaźniejszych systemów na bazie Linuksa. Z&nbsp;kolei Cinnamon to jedna z&nbsp;kilku jego wersji, najbardziej dopieszczona pod względem wyglądu i&nbsp;funkcjonalności. Bardzo dobry wybór dla osób chcących [odejść od Windowsa i&nbsp;jego dziwnych zagrywek](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}.

Mimo ogólnej przystępności Minta, jest na nim parę rzeczy, które mogą na początku drażnić i&nbsp;wydawać się obce. Jedną z&nbsp;nich jest **zachowanie dolnego paska**.

Na Windowsie (a&nbsp;przynajmniej Windowsie 10, nie używałem jedenastki) każde otwarte okno dostaje osobną zakładkę na dolnym pasku, pokazującą jego nazwę oraz ikonę.  
Na Mincie z Cinnamonem jest inaczej; okna należące do tego samego programu są domyślnie grupowane pod jedną, niepodpisaną ikoną. Trzeba na nią najechać kursorem, żeby móc wybrać któreś z&nbsp;nich.

{:.bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-domyslny-dolny-pasek.png" alt="Fragment paska dolnego na Cinnamonie. Pod dwie ikony są podpięte po dwa okna, oznaczone liczbami"/>

Nie będę tego oceniał pod kątem ergonomii. Powiem jedynie: to istotna różnica względem Windowsa, na poziomie fundamentalnym. Może drażnić i&nbsp;odstraszać nowoprzybyłych.

A ja nie chcę rozdrażnienia. Chcę Linuksa zdobywającego serca ludzi.

Dlatego pokażę w&nbsp;tym krótkim samouczku parę sposobów (graficznych i&nbsp;konsolowych) na sprawienie, że pasek na Mincie zacznie się zachowywać jak ten na Windowsie. To naprawdę proste, wystarczy parę kliknięć.

{:.post-meta .bigspace-after}
W tym wpisie trzymam się nazw angielskich, ale ich polskie odpowiedniki powinny być łatwe do ustalenia na podstawie obrazków.

## Spis treści

* [Sposób łatwiejszy](#sposób-łatwiejszy)
  * [Rozgrupowanie okien](#rozgrupowanie-okien)
  * [Wyświetlanie nazw okien obok ikon](#wyświetlanie-nazw-okien-obok-ikon)
  * [Podsumowanie wątku](#podsumowanie-wątku)
  * [Bonus: zmiana ustawień przez plik](#bonus-zmiana-ustawień-przez-plik)
  * [Bonus 2: ustawianie skryptem (dla zaawansowanych)](#bonus-2-ustawianie-skryptem-dla-zaawansowanych)
* [Sposób alternatywny (lepsza zgodność, więcej roboty)](#sposób-alternatywny-lepsza-zgodność-więcej-roboty)
  * [Zmiana apletów na pasku](#zmiana-apletów-na-pasku)
  * [Przemeblowanie paska](#przemeblowanie-paska)

## Sposób łatwiejszy

Choć obszar z&nbsp;ikonami programów wydaje się integralną częścią paska, jest w&nbsp;rzeczywistości czymś częściowo niezależnym. Tak zwanym _apletem_. Nazywa się **pogrupowaną listą okien (ang. _Grouped window list_)**.

Żeby wejść w&nbsp;ustawienia tego elementu, należy kliknąć prawym przyciskiem myszy jego obszar, czyli dowolną z&nbsp;ikon programów albo przestrzeń między nimi.

{:.post-meta .bigspace-after}
Nie klikamy innych części paska, takich jak ikona Minta w&nbsp;rogu, bo to odrębne obszary, posiadające osobne menu.

Nad paskiem pojawi się menu kontekstowe. Należy tam kliknąć zakładkę `Applet preferences`. Menu nieco się rozwinie i&nbsp;powiększy, ukazując jeszcze kilka opcji. Jedna z&nbsp;nich to `Configure…`, klikamy ją.

{:.figure .bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-ustawianie-paska-opcje.png" alt="Menu kontekstowe apletu z&nbsp;dolnego paska. Zaznaczono opcje, których kliknięcie pozwala przejść do ustawień"/>

Po jej kliknięciu pojawi się okno z&nbsp;ustawieniami apletu. Nazwane tak jak on i&nbsp;opatrzone ikoną kilku okien na fioletowym tle. Wystarczy w&nbsp;nim zmienić dwie rzeczy.

### Rozgrupowanie okien

W górnej części okna od ustawień widnieją cztery zakładki; ta domyślnie otwarta powinna nazywać się `General`.

W tej zakładce interesuje nas pierwsze ustawienie od góry, `Group windows by application`. Kiedy je odznaczymy, to otwarte okna nie będą już grupowane pod jedną ikoną. Każde z&nbsp;nich zyska własne miejsce na pasku.

{:.bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-pasek-dolny-brak-grupowania-ikon.png" alt="Okno z&nbsp;ustawieniami apletu od ikon, z&nbsp;odznaczoną opcją ich grupowania"/>

### Wyświetlanie nazw okien obok ikon

Pozostając w&nbsp;tym samym oknie z&nbsp;ustawieniami co wyżej, należy kliknąć zakładkę `Panel` w&nbsp;górnej części. Przeniesie nas to do kolejnego zestawu opcji.

Tam, obok etykiety `Button label`, należy zmienić opcję na `Window title` albo `Application name`, wedle własnych preferencji.

{:.post-meta .bigspace-after}
Osobiście postawiłem na opcję pierwszą, nazwy okien, bo czasem ujawnia więcej -- np. nazwę strony/zakładki obecnie wyświetlanej wewnątrz przeglądarki Firefox.

{:.bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-pasek-dolny-wyswietlanie-nazw.png" alt="Okno z&nbsp;ustawieniami apletu od ikon, z&nbsp;wybraną opcją wyświetlania nazw okien"/>

### Podsumowanie wątku

Po zmianie obu opisanych ustawień dolny pasek zacznie się zachowywać prawie tak jak ten na Windowsie:

{:.bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-zmieniony-dolny-pasek.png" alt="Fragment paska dolnego na Cinnamonie, już z&nbsp;jedną podpisaną zakładką na każde okno"/>

Jest jednak pewna różnica -- ikony odpowiedzialne za uruchamianie programów są wymieszane z&nbsp;listą otwartych okien. Jak na zrzucie ekranu: ikony Firefoksa i&nbsp;konsoli wciśnięte między dwa okna przeglądarki plików i&nbsp;dwa okna notatnika.

Mnie osobiście ten układ jakoś szczególnie nie przeszkadza. Jeśli ktoś chce coś jeszcze bliższego Windowsowi, to może rozważyć wymianę grupowanej listy na dwa osobne aplety. Opisuję to [bliżej końca tego wpisu](#sposób-alternatywny-lepsza-zgodność-więcej-roboty){:.internal}.

Niżej znajdują się natomiast sposoby na szybsze (a&nbsp;nawet automatyczne) wprowadzanie tych samych dwóch zmian, które opisałem wyżej.

### Bonus: zmiana ustawień przez plik

Większości osób zmieniających swój pasek proponuję trzymać się zwykłej klikaniny. Szybka i&nbsp;bezbolesna. Zwłaszcza jeśli ktoś ma Minta zainstalowanego na stałe i&nbsp;chce zmienić opcje tylko raz.

Może się jednak zdarzyć, że ktoś musi zmieniać pasek Cinnamona wielokrotnie -- parę przykładowych sytuacji w&nbsp;rozwijanej zakładce.

{% include details.html summary="Kiedy może być konieczne wielokrotne ustawianie paska?" %}

1. Korzystamy z&nbsp;Minta w&nbsp;trybie ulotnym (*live*), żeby jak najlepiej chronić swoje dane osobowe albo móc swobodniej eksperymentować z&nbsp;systemem.

   Wiąże się to z&nbsp;ładowaniem systemu od zera przy każdym uruchomieniu -- a&nbsp;zatem trzeba go również ustawiać od zera. Ręczne klikanie dzień po dniu byłoby torturą.

2. Mamy do skonfigurowania więcej komputerów.

   Być może cała rodzinka albo firma właśnie jest w&nbsp;trakcie migracji na Linuksa? W&nbsp;każdym razie: jeśli urządzenia trzeba uruchamiać ręcznie, to jest to już wystarczająco żmudne. Niech chociaż konfiguracja będzie szybka.

{% include details-end.html %}

Osoby chcące uniknąć rutyny docenią możliwość szybkiego wgrywania ustawień z&nbsp;pliku. W&nbsp;tej części opiszę, jak to zrobić.

Najpierw należy choć raz, na samym początku, **zmienić ustawienia ręcznie, zgodnie z&nbsp;[instrukcjami](#sposób-łatwiejszy){:.internal} podanymi wyżej**.

Następnie, wewnątrz tego samego okna z&nbsp;ustawieniami, należy kliknąć ikonę trzech kresek w&nbsp;górnym prawym rogu. Stamtąd należy wybrać opcję *eksportowania* pliku. Pojawi się menu odpowiedzialne za jego zapisanie.

Wystarczy teraz wpisać dowolną nazwę dla tworzonego pliku, na przykład `dolny-pasek-ustawienia`. Nie trzeba podawać żadnej końcówki; zostanie automatycznie zapisany jako plik `.json`.

Odtąd można nosić ten plik ze sobą na jakimś pendrivie. A&nbsp;kiedy zechcemy wgrać zawarte w&nbsp;nim ustawienia do apletu, na swoim lub cudzym komputerze, to:

* otwieramy okno z&nbsp;ustawieniami apletu,
* klikamy ikonę trzech kresek w&nbsp;górnym prawym rogu,
* wybieramy opcję *importowania* pliku,
* wybieramy nasz plik JSON.

Wygląd i&nbsp;zachowanie apletu od listy okien powinny zmienić się natychmiast po wgraniu pliku. Nie trzeba nic odświeżać.

### Bonus 2: ustawianie skryptem (dla zaawansowanych)

Najpierw należy uzyskać, sposobem opisanym wyżej, plik JSON z&nbsp;ustawieniami apletu. Można go odtąd nosić ze sobą na pendrivie.

Kiedy załadujemy system, na którym chcemy zmienić działanie paska, można sobie **uruchomić konsolę w&nbsp;folderze z&nbsp;tym plikiem**.

Następnie używamy komendy, aby skopiować plik do folderu z&nbsp;ustawieniami apletu grupującego. Podmieniamy przy tym dotychczasowy plik z&nbsp;ustawieniami, `2.json`:

<pre class="black-bg mono big-wordspace nospace">
cp -f NASZ_PLIK.json ~/.config/cinnamon/spices/grouped-window-list@cinnamon.org/2.json</pre>

{:.figcaption}
Komendę można oczywiście uczynić częścią większego skryptu.  
Tradycyjna przypominajka: gdyby ktoś ją stąd kopiował, to wkleja się ją do konsoli przez <code>Ctrl+<span class="red">Shift</span>+V</code>.

{% include details.html summary="Omówienie komendy" %}

{:.bigspace-before}
Program konsolowy `cp` odpowiada na Linuksie za kopiowanie różnych plików i&nbsp;folderów. Komenda `cp -f NASZ_PLIK.json INNY_PLIK` kopiuje wskazany przez nas plik, zastępując nim jakiś inny plik.

Znaku tyldy (`~`) wewnątrz ścieżki użyłem do wskazania folderu domowego. Na świeżym Mincie z&nbsp;pendrive'a odpowiada jej folder `/home/mint` -- ale ta nazwa nie byłaby przenośna między systemami. Zmienia się nawet po trwałej instalacji Minta (na nazwę użytkownika).

Warto zaznaczyć, że zastępowanie plików nie jest typowym zachowaniem programu `cp`; uzyskaliśmy je tutaj dzięki dopisaniu argumentu `-f` (skrót od *force*; „wymuś”).

Nazwa zastępowanego pliku, `2.json`, wydaje się losowa... Ale tak naprawdę wynika z&nbsp;faktu, że `2` to liczba przydzielona apletowi grupującemu okna. Mówi z&nbsp;grubsza, który jest z&nbsp;kolei na liście wszystkich apletów.

{:.post-meta}
Jest tu jednak pewien niuans: jeśli usuwa się aplety sprzed końca listy, to liczby nie są przeliczane. Przykładowo: po usunięciu naszego apletu grupującego po prostu nie byłoby na liście apletu numer 2. A&nbsp;po jego ponownym dodaniu miałby ostatni numer na liście.

{% include details-end.html %}

{% include info.html
type="Uwaga"
text="**Po użyciu tej komendy aplet z&nbsp;ikonami zapewne zniknie**. To dziwne, ale zrozumiałe zachowanie -- przez ułamek sekundy stracił wszystkie ustawienia, na których polegał.  
Powinien pojawić się ponownie przy kolejnym odświeżeniu Cinnamona, ponownym zalogowaniu itd.  
Żeby je wymusić od razu, można kliknąć prawym przyciskiem myszy dowolny obszar paska (poza apletami), kliknąć zakładkę `Troubleshoot` i&nbsp;wybrać opcję `Restart Cinnamon`.  
Aplet powinien wrócić na swoje miejsce i&nbsp;działać zgodnie z&nbsp;oczekiwaniami."
%}

{% include details.html summary="Trochę luźnych uwag o&nbsp;ustawianiu Linuksa skryptami" %}

{:.bigspace-before}
W tym wypadku ustawienia zmieniane skryptem były czymś na poziomie Cinnamona, zapisanym do pliku JSON o&nbsp;narzuconym przez nich formacie.

Warto jednak wiedzieć, że w&nbsp;wielu innych przypadkach -- na Mincie i&nbsp;nie tylko -- ustawienia zmieniane przez menu są zapisywane wewnątrz [centralnej bazy zwanej `dconf`](/tutorials/linux-dconf-skryptowanie){:.internal}. W&nbsp;podlinkowanym wpisie pokazuję, w&nbsp;jaki sposób można takie opcje wyłapać i&nbsp;przerobić na skrypty, ustawiające to samo automatycznie i&nbsp;oszczędzające klikania.

{:.post-meta .bigspace-after}
Zresztą nawet w&nbsp;tym wpisie, przy metodzie alternatywnej, wskazuję parę ustawień zawartych w&nbsp;bazie. Tyle że ich zmiana nie działała zgodnie z&nbsp;oczekiwaniami.

Same pliki JSON nie są żadną ekstrawagancją i&nbsp;to też dość częsty sposób na przenoszenie ustawień. Poprzez plik `policies.json` można na przykład zmieniać domyślne zachowanie przeglądarki Firefox.

Warto znać takie centralne ustawienia, popularne formaty plików i&nbsp;sposoby na automatyczne wprowadzanie zmian. Zwłaszcza jeśli chce się konfigurować wielokrotnie ten sam komputer (tryb *live*) albo po jednym razie wiele komputerów (szykowanie floty).

{% include details-end.html %}

## Sposób alternatywny (lepsza zgodność, więcej roboty)

Tu sposób dla tych, którzy nie chcą nazw okien wymieszanych z&nbsp;ikonami. Wolą zachowanie *dokładnie takie* jak na Windowsie -- nieruchome i&nbsp;niezmienne ikony programów, zaś po ich prawej stronie gromadzą się otwarte okna.

### Zmiana apletów na pasku

Najpierw należy kliknąć prawym przyciskiem myszy jakąś pustą, niezajętą niczym część paska. Z&nbsp;menu kontekstowego wybieramy `Applets`, przechodząc do listy apletów.

{:.figure .bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/ustawienia-apletow-wlaczanie.png" alt="Menu kontekstowe z&nbsp;wyróżnioną opcją wejścia w&nbsp;ustawienia apletów"/>

Tam znajdujemy nasz aplet `Grouped window list`. Klikamy go, żeby się zaznaczył. A&nbsp;potem klikamy znak minusa na dole, żeby go odpiąć od paska.

{:.bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-grupowana-lista-okien-usuwanie.png" alt="Fragment okna z&nbsp;listą apletów i&nbsp;zaznaczona opcja od usunięcia grupowanej listy z&nbsp;paska"/>

Teraz przyda się czymś wypełnić pustkę. Znajdujemy na liście i&nbsp;**dodajemy (przez kliknięcie znaku plusa)** dwa inne aplety: `Window list` (bez *Grouped* na początku) oraz `Panel launchers`.

Świeżo po dodaniu nowych apletów efekt może rozczarowywać.

Będą wyrównane do prawej strony paska, a&nbsp;nie lewej, jak na Windowsie. Do tego zawarte w&nbsp;nich ikonki będą dość małe. Ale spokojnie, można to łatwo zmienić!

### Przemeblowanie paska

Najpierw sprawmy, żeby aplet z&nbsp;listą okien się pokazał. Jeśli nie mamy żadnych otwartych okien, to uruchamiamy dowolny program, żeby jego nazwa zagościła na pasku. Nie zamykamy jego okna.

Teraz należy wejść w&nbsp;tryb edycji paska. Znowu -- klikamy go prawym przyciskiem w&nbsp;jakimś pustym miejscu, niebędącym apletem. Następnie klikamy przełącznik podpisany `Panel edit mode`: 

{:.figure .bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/panel-edit-mode-wlaczanie.png" alt="Menu kontekstowe z&nbsp;wyróżnioną funkcją edycji paska, zwanego panelem."/>

Od teraz do czasu wyłączenia trybu nie będziemy w&nbsp;stanie aktywować apletów kliknięciami. Możemy je za to przenosić w&nbsp;inne części paska.

Swoją drogą powinny tam być trzy główne obszary:

* lewy, o&nbsp;czerwonym tle;
* środkowy, o&nbsp;zielonym tle;
* prawy, o&nbsp;niebieskim tle.

Kliknijmy sobie przykładowo aplet-uruchamiacza (zawierający same ikonki programów). Po kliknięciu **nie puszczamy przycisku myszy**, tylko przesuwamy sam kursor, przenosząc aplet na lewą stronę.

Najeżdżamy kursorem na obszar po lewej (z&nbsp;czerwonym tłem), cały czas go obserwując. Kiedy obszar odrobinę się rozszerzy, to puszczamy przycisk myszy. Aplet zostanie przeniesiony w&nbsp;nowe miejsce.

{:.bigspace-before}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-pasek-przenoszenie-pierwszego-apletu.png" alt="Ilustracja przenoszenia apletu-uruchamiacza na lewą stronę paska"/>

{:.figcaption}
Można zauważyć, że po upuszczeniu apletu jego ikony automatycznie się powiększą, zyskując właściwy rozmiar. To dlatego, że każdy z&nbsp;trzech obszarów paska ma własne, niezależne ustawienia.

W podobny sposób przeciągamy listę okien, również kładąc ją w&nbsp;obszarze po lewej (ale po prawej stronie apletu z&nbsp;ikonami programów):

{:.bigspace}
<img src="/assets/tutorials/linux/cinnamon-dolny-pasek/cinnamon-pasek-przenoszenie-drugiego-apletu.png" alt="Ilustracja przenoszenia listy okien na lewą stronę paska, gdzie jest już inny aplet"/>

Po przeniesieniu apletów znów otwieramy menu kontekstowe paska i&nbsp;wyłączamy tryb edycji.

Można sobie poklikać i&nbsp;upewnić się, że wszystko działa jak powinno. W&nbsp;ten sposób zyskaliśmy pasek klasyczny: ikona menu, potem ikony przypiętych programów, potem lista otwartych okien. Prawie nie do odróżnienia od Windowsa&nbsp;10.

{% include details.html summary="O problemach z&nbsp;automatyzacją zmian" %}

{:.bigspace-before}
Liczyłem na to, że pasek można zmienić skryptem równie łatwo jak ustawienia pogrupowanej listy. Ale niestety na tym poległem.

Na początku wydawało się to łatwe. Ustawienia paska są zapisywane wewnątrz centralnej bazy *Dconf* (którą można [łatwo modyfikować skryptami](/tutorials/linux-dconf-skryptowanie){:.internal}). Paska dotyczą dwa główne ustawienia:

* `/org/cinnamon/enabled-applets` -- lista wszystkich apletów na wszystkich paskach oraz ich położenie i&nbsp;liczby porządkowe. Składnia własna Cinnamona, dość czytelna.
* `/org/cinnamon/next-applet-id` -- numer poprzednio dodanego apletu plus jeden.

Problem jednak w&nbsp;tym, że kiedy zmieniłem przez `dconf write` obie te wartości, na te skopiowane od siebie, to: lista pogrupowana zniknęła, aplet-uruchamiacz został dodany... Ale lista okien już nie. Wystąpił błąd.

Próbowałem różnych wersji -- zmieniać po jednej rzeczy naraz, stale pilnując zmiennej od ID. Zrobić pauzę między zmianami. Odświeżyć Cinnamona między zmianami. Nie pomogło.

Z tego względu póki co nie mam sposobu na zautomatyzowanie takich zmian. Osoby zainteresowane mogą się wgryźć w&nbsp;kod źródłowy Cinnamona (np. pliki JavaScript z&nbsp;folderu [`.../js/ui`](https://github.com/linuxmint/cinnamon/tree/master/js/ui)) i&nbsp;poszukać rozwiązania.

{:.post-meta}
...Albo zrobić automatyzację naiwną, polegającą na otwarciu okna z&nbsp;ustawieniami i&nbsp;wysyłania do niego symulowanych klawiszy `Tab` i&nbsp;`Enter` w&nbsp;odpowiedniej ilości. Jeśli coś jest głupie, ale działa, to nie jest głupie :wink:

{% include details-end.html %}

To tyle na ten wpis. Dzięki za uwagę i&nbsp;powodzenia w&nbsp;*windowsowaniu* pasków -- sobie, organizacji albo rodzince :smile:

