---
layout: page
title: "Jak ustawić język polski na systemie Linux Mint" 
description: "Linuksy nie gęsi, język polski znają."
---

W październiku 2025&nbsp;roku miał nastąpić [koniec wsparcia dla Windowsa 10](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}. Został przesunięty o&nbsp;rok, ale pozostaje nieuchronny. Coraz więcej osób próbuje z&nbsp;tej okazji alternatywy -- Linuksa (a&nbsp;właściwie różnych systemów na jego bazie).

Osobiście polecam wszystkim migrującym osobom system **Linux Mint**. Jest bardzo podobny do Windowsa, ale wolny od trawiących go patologii (reklamy, wpychanie AI, obowiązkowa łączność z&nbsp;internetem). Poza tym jest po prostu dopracowany i&nbsp;przyjazny użytkownikom.

Również ustawienie języka polskiego może być proste i&nbsp;przyjemne. Po pierwszym załadowaniu Minta z&nbsp;pendrive'a (w&nbsp;trybie *live*) klika się ikonkę `Install Linux Mint` w&nbsp;rogu pulpitu. Podczas instalacji zaznacza się polski język i&nbsp;strefę czasową. A&nbsp;kiedy  instalacja się skończy, to mamy Minta po polsku.

...Co jednak mają zrobić osoby, które nie chciałyby jeszcze instalować Minta na stałe, a&nbsp;jedynie sprawdzić poziom spolszczenia w&nbsp;trybie *live*? Albo ci, którzy w&nbsp;czasie instalacji nie wybrali polskiego, a&nbsp;teraz chcą to zmienić?

Z myślą o&nbsp;takich osobach stworzyłem ten samouczek. Pokażę, jakie wykonać kroki, żeby spolszczyć Minta bez zdawania się na główny instalator.  
Przy każdym kroku podaję **dwa sposoby -- graficzny i&nbsp;konsolowy**. Zarówno osoby preferujące klikanie w&nbsp;menu, jak i&nbsp;szybsze tekstowe polecenia, znajdą tu coś dla siebie.

Zapraszam!

## Spis treści

* [Ogólne omówienie](#ogólne-omówienie)
* [Ustawianie polskiej klawiatury](#ustawianie-polskiej-klawiatury)
* [Ustawianie strefy czasowej](#ustawianie-strefy-czasowej)
* [Ustawianie polskiego języka dla systemu](#ustawianie-polskiego-języka-dla-systemu)
  * [Instalacja polskich pakietów językowych](#instalacja-polskich-pakietów-językowych)
  * [Wybór języka polskiego w&nbsp;ustawieniach](#wybór-języka-polskiego-wustawieniach)
  * [Odświeżenie ustawień](#odświeżenie-ustawień)
* [Bonus: spolszczenie jednym skryptem](#bonus-spolszczenie-jednym-skryptem)

## Ogólne omówienie

Spolszczenie rozumiem tu jako ustawienie kilku niezależnych od siebie rzeczy. Są nimi:

* układ klawiatury (polskie literki),
* strefa czasowa,
* język systemu i&nbsp;jego podstawowych programów.

{:.post-meta .bigspace-after}
Jest też kwestia języka większych, niezależnych programów, takich jak Firefox i&nbsp;LibreOffice. Ale o&nbsp;tym napiszę w&nbsp;osobnym samouczku.

Klawiaturę i&nbsp;strefę czasową można zmieniać w&nbsp;każdej chwili bez połączenia z&nbsp;internetem; łączności będzie natomiast wymagała (przynajmniej raz na początku) zmiana języka systemu, bo Mint nie zawiera domyślnie polskich pakietów językowych.

{% include info.html
type="Parę uwag"
text="Samouczek opracowałem, korzystając z&nbsp;systemu **Linux Mint, wersji 22.2, wariantu MATE**. Jeśli używasz Minta Cinnamona, to menu będą wyglądały ciut inaczej, ale powinno być bardzo podobnie. Minta XFCE nie miałem okazji sprawdzić.  
Jeśli natomiast używasz innego Linuksa, to od strony graficznej wszystko może wyglądać inaczej. Sposób konsolowy jest natomiast bardziej uniwersalny i&nbsp;może (ale nie musi) zadziałać też na innych systemach. Nieco rozwijam myśl w&nbsp;zakładce poniżej."
%}

Jeśli ktoś rozważa sposób konsolowy, ale nie ma w&nbsp;tym doświadczenia, to poniżej parę uniwersalnych uwag.

{% include details.html summary="Uniwersalne uwagi dla konsoli" %}

{:.bigspace-before}
Konsolę można uruchomić czarną ikonką z&nbsp;dolnego paska albo przez naciśnięcie kombinacji klawiszy `Ctrl+Alt+T`.

Żeby coś do niej wkleić (choćby polecenia, które będę tu przytaczał), należy albo kliknąć prawym przyciskiem myszy i&nbsp;wybrać opcję wklejenia, albo wcisnąć kombinację klawiszy <code>Ctrl+<span class="red">Shift</span>+V</code>.

Kiedy piszę o&nbsp;„użyciu komendy/polecenia”, to mam na myśli wpisanie albo wklejenie podanego tekstu, a&nbsp;następnie wciśnięcie klawisza `Enter`.

Jeśli chodzi o&nbsp;**użycie metod konsolowych na innych Linuksach**, to powinny działać bez problemu w&nbsp;przypadku systemów z&nbsp;rodziny „debianowatej”, do której należy Mint. W&nbsp;szczególności na Ubuntu, Debianie, Zorinie.

Jeśli jednak wyjdzie się poza ten światek, to pojawiają się niuanse.

* Programu `timedatectl` nie będzie na systemach, które nie korzystają z&nbsp;[*systemd*](https://pl.wikipedia.org/wiki/Systemd).
* Komenda `setxkbmap` nie zadziała na systemach, które zamiast Xorga używają Waylanda.

  Przykładowo na Fedorze w&nbsp;wariancie KDE, którą miałem okazję testować. Sposób oparty na klikaniu menu przebiega tam natomiast bardzo podobnie.

* Instalacja pakietów językowych przez `apt` (albo offline przez `dpkg`) nie będzie możliwa na systemach, które nie są z&nbsp;„rodziny Debiana”.

  Te inne systemy mają własne menedżery pakietów (np. `dnf` na Fedorze), do tego nazwy polskich plików mogą być inne. Najlepiej znaleźć w&nbsp;sieci instrukcję odpowiednią dla swojego systemu.

{% include details-end.html %}

## Ustawianie polskiej klawiatury

Linux Mint świeżo po załadowaniu z&nbsp;pendrive'a nie wspiera polskich znaków (ogonków itd.), zaś kombinacje `Alt+klawisz` albo nie robią nic, albo włączają całkiem inne funkcje. Rzecz irytująca, ale łatwa do zmiany. Wystarczy włączyć polski układ klawiatury.

{% include details.html summary="Zmiana układu klawiatury przez menu" %}

Należy kliknąć ikonę Minta w&nbsp;dolnym lewym rogu, żeby wyświetlić menu. Tam trzeba kliknąć zakładkę `Control Center` z&nbsp;lewej kolumny, a&nbsp;w kolejnym oknie znaleźć i&nbsp;kliknąć ikonę podpisaną `Keyboard`.

Wyświetli się osobne okno. Trzeba kliknąć zakładkę `Layouts`. Pojawi się lista dostępnych układów klawiatury, która domyślnie powinna zawierać tylko angielski. Czas zatem dodać polski! Należy kliknąć przycisk `Add` spod listy.

{:.bigspace}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-keyboard-1-new-layout.png" alt="Kolaż ze zezytów ekranu pokazujący menu układów klawiatury z&nbsp;wyróżnionym przyciskiem 'Add'."/>

Otworzy się kolejne okno, domyślnie w&nbsp;zakładce `By country`. Może być. Z&nbsp;rozwijanej listy z&nbsp;górnego lewego rogu wybieramy `Poland`, a&nbsp;potem klikamy przycisk `Add` w&nbsp;dolnym prawym rogu.

{:.bigspace}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-keyboard-2-adding-pl-layout.png" alt="Kolaż pokazujący zaznaczony polski układ klawiatury i&nbsp;wyróżniony przycisk `Add`."/>

W ten sposób polski układ zostanie dodany do listy -- ale to nie wszystko! Trzeba go jeszcze ustawić jako aktywny. W&nbsp;tym celu klikamy nazwę z&nbsp;listy, a&nbsp;potem przycisk `Move Up`.

{:.bigspace}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-keyboard-3-selecting-pl-layout.png" alt="Kolaż pokazujący język polski na drugim miejscu na liście oraz wyróżniony przycisk `Move up`, który przeniesie go wyżej"/>

**Uwaga dla MATE:** pole na podgląd w&nbsp;dolnej części okna nadal nie będzie przyjmowało polskich liter, to zapewne niedopatrzenie twórców. Ale w&nbsp;innych programach zaczną działać od razu po przesunięciu polskiego na pierwsze miejsce.

**Uwaga dla Cinnamona:** ogólnie ustawianie polskiej klawiatury na Cinnamonie jest bliźniaczo podobne do robienia tego na MATE. Różnica polega na tym, że przesunięcie polskiego na pierwsze miejsce jeszcze go nie włącza. Należy kliknąć ikonę flagi, która się pojawi na dolnym pasku i&nbsp;to stamtąd wybrać język polski. Obrazki [tutaj](/miniposts/cinnamon-klawiatura#zpunktu-widzenia-użytkowników){:.internal}.

{:.post-meta}
Jeśli flaga na Cinnamonie zbyt kogoś rozprasza jaskrawością na ciemnym tle, to można ją kliknąć prawym przyciskiem myszy i&nbsp;wybrać opcję `Remove "Keyboard"`. Usunięcie apletu nie wpłynie na działanie polskich znaków.

{% include details-end.html %}

{% include details.html summary="Zmiana układu klawiatury przez konsolę" %}

Tutaj konsola zdecydowanie wyprzedza sposób graficzny. Wystarczy użyć takiego polecenia, żeby od razu zyskać polskie znaki:

<div class="black-bg mono">
setxkbmap pl
</div>

{:.figcaption .nospace}
Jedna uwaga: układ resetuje się w&nbsp;razie wylogowania i&nbsp;ponownego zalogowania, np. po zmianie języka systemu. Należy go wtedy aktywować ponownie.

{% include details-end.html %}

Po włączeniu polskiej klawiatury można na próbę uruchomić jakiś program pozwalający wpisywać tekst i&nbsp;upewnić się, że kombinacje klawiszy działają, polskie ogonki i&nbsp;inne znaki się pojawiają, a&nbsp;my możemy teraz [zażółcić gęślą jaźń](https://pl.wikipedia.org/wiki/Za%C5%BC%C3%B3%C5%82%C4%87_g%C4%99%C5%9Bl%C4%85_ja%C5%BA%C5%84).

## Ustawianie strefy czasowej

Mint świeżo po załadowaniu z&nbsp;pendrive'a nie ma pojęcia, z&nbsp;jakiego jesteśmy kraju. Pole z&nbsp;datą i&nbsp;godziną w&nbsp;dolnym prawym rogu będzie zapewne pokazywało „punkt zero” stref czasowych. Czyli w&nbsp;praktyce dwie godziny wcześniej niż w&nbsp;Polsce.

{% include info.html
type="Małe utrapienia"
text="Czas przesunięty o&nbsp;dwie godziny w&nbsp;tył nie tylko sprzyja nocnym posiadówkom („przecież jeszcze tak wcześnie...”), ale może też uprzykrzać życie na niektórych stronkach.  
Przykładowo: otwieramy wyszukiwarkę połączeń kolejowych. Nasza przeglądarka bierze (zły) czas od systemu i&nbsp;przekazuje go stronce. Ta automatycznie wstawia ten czas pod polem wyszukiwarki.  
Jeśli teraz klikniemy `Szukaj`, to znajdzie pociągi, które już odjechały. Trzeba by każdorazowo ręcznie zmieniać godzinę, żeby dostać to, co nas interesuje."
%}

{% include details.html summary="Zmiana strefy czasowej przez menu" %}

Należy kliknąć ikonkę Minta w&nbsp;dolnym lewym rogu, następnie zakładkę `Control Center`, stamtąd wybrać `Time and Date`. Pojawi się małe okno z&nbsp;dwiema informacjami: o&nbsp;strefie czasowej i&nbsp;synchronizacji.

Należy kliknąć pole z&nbsp;nazwą strefy czasowej. Wyświetli się mapka świata z&nbsp;najważniejszymi miastami. Tu można wybrać strefę na dwa sposoby:

* kliknąć punkcik na mapie odpowiadający Warszawie,

  W&nbsp;praktyce, zamiast celować w&nbsp;małe punkciki, proponuję najechać na pusty, żółtawy obszar na terenie wschodniej Europy (czerwone koło na screenie niżej).  
  Po pierwszym kliknięciu mapa nieco się przybliży; można wtedy bardziej komfortowo wybrać Warszawę. Rozwijana lista na dole powinna pokazać `Europe/Warsaw`.

* wybrać strefę z&nbsp;rozwijanej listy.

  Listę można oczywiście po prostu przewinąć i&nbsp;kliknąć `Europe/Warsaw`... Ale to trochę by zajęło, bo jest długa (i&nbsp;nie da się w&nbsp;nią wpisywać tekstu).  
  Proponuję najpierw kliknąć na mapce dowolny punkt na terenie Europy. Lista przewinie się ku europejskim rewirom, a&nbsp;wybranie z&nbsp;niej Warszawki to kwestia chwili.

{:.bigspace-before}
<img src="/assets/tutorials/linux-mint-jezyk-polski/mint-strefa-czasowa-mapa.jpg" alt="Zrzut ekranu pokazujący okno wyboru strefy czasowej na Mincie. U&nbsp;góry widać mapę świata z&nbsp;wyróżnionym punktem w&nbsp;okolicy Polski, a&nbsp;na dole rozwijaną listę z&nbsp;zaznaczoną warszawską strefą czasową"/>

{% include details-end.html %}

{% include details.html summary="Zmiana strefy czasowej przez konsolę" %}

Za sterowanie czasem odpowiada na Mincie program `timedatectl` (*time & date control*) i&nbsp;różne jego podprogramiki. Strefę czasową odpowiadającą Polsce można ustawić jednym krótkim poleceniem:

```
timedatectl set-timezone Europe/Warsaw
```

Jeśli teraz użyje się komendy `timedatectl` (samej, bez żadnych dodatkowych rzeczy), to powinno wyświetlić, że mamy polską strefę czasową, czas wschodnioeuropejski (*CEST,&nbsp;+0200*).

{% include details-end.html %}

Możliwe, że godzina widoczna w&nbsp;dolnym prawym rogu nie zaktualizuje się od razu po zmianie ustawień. Ale spokojnie, wystarczy chwilę poczekać.

{% include details.html summary="Wątek prywatnościowy (dla zainteresowanych)" %}
{:.bigspace-before}
W ustawieniach daty i&nbsp;godziny mamy nie tylko strefy, ale również pstryczek odpowiedzialny za **automatyczną synchronizację czasu**. Może on mieć pewne znaczenie dla prywatności.

Jeśli opcja jest włączona (a&nbsp;domyślnie jest), to Mint co pewien czas wysyła domenie `ntp.ubuntu.com` pytania o&nbsp;aktualny czas. Nazwę domeny widzi zapewne dostawca usług internetowych (np. właściciel hotspota albo firma telekomunikacyjna), mający [wgląd w&nbsp;ruch sieciowy](/internetowa_inwigilacja/2024/03/28/analiza-ruchu){:.internal}. Widząc regularny kontakt z&nbsp;taką usługą, może wywnioskować, że dana osoba korzysta z&nbsp;Linuksa.

W obecnych czasach Linuksów jest coraz więcej, a&nbsp;ta informacja nie jest jakimś unikalnym wyróżniaczem. Ale jeśli ktoś chce, to można wyłączyć synchro.

{% include details-end.html %}

## Ustawianie polskiego języka dla systemu

Mint zawiera domyślnie kilka wersji językowych, ale niestety nie ma wśród nich języka polskiego, trzeba go zainstalować. Instalacja ma trzy etapy, które omówię po kolei:

1. pobranie polskiego pakietu językowego,
2. ustawienie języka polskiego dla systemu,
3. odświeżenie ustawień.

### Instalacja polskich pakietów językowych

Żeby wykonać ten krok, **należy mieć łączność z&nbsp;internetem**.

{:.post-meta .bigspace-after}
Przynajmniej raz, na początku. W&nbsp;zakładce dla chętnych pokażę, że po pierwszym zdobyciu instalatorów można zacząć działać offline.

{% include details.html summary="Sposób graficzny" %}

Należy kliknąć ikonę Minta w&nbsp;dolnym lewym rogu, z&nbsp;lewej kolumny wybrać `Control Center`, a&nbsp;następnie `Languages` z&nbsp;dostępnych opcji (trzeba przewinąć kawałek w&nbsp;dół; ikona będzie pod nagłówkiem *Look and Feel*).

Otworzy się okno ustawień językowych. Na razie nie ma co zmieniać języków, bo polskiego nie będzie na liście. Zamiast tego należy kliknąć opcję `Install/Remove Languages`.

{:.bigspace}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-lang-install-1.png" alt="Zrzut ekranu z&nbsp;zakreśloną na czerwoną opcją dodawania lub usuwania języków"/>

Wyświetli się długa lista języków. Należy znaleźć na niej kafelek podpisany `Polish`, kliknąć go, a&nbsp;następnie kliknąć przycisk `Install`.

{:.bigspace}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-lang-install-2.png" alt="Kolaż pokazujący zaznaczony kafelek z&nbsp;językiem polskim oraz wyróżniony przycisk `Install'."/>

Polski trafi na listę języków, ale obok jego nazwy będzie widoczna adnotacja o&nbsp;braku pakietów językowych. Dlatego należy kliknąć kafelek z&nbsp;jego nazwą, a&nbsp;potem przycisk `Install language packs`. Można chwilę poczekać, aż skończy się pobieranie pakietów z&nbsp;internetu.

{:.bigspace}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-lang-install-3.png" alt="Kolaż pokazujący kafelek z&nbsp;językiem polskim oraz informacją o&nbsp;braku pakietów językowych, a&nbsp;pod spodem wyróżniony przycisk instalujący te pakiety."/>

{% include info.html
type="Uwaga"
text="Podczas instalacji może pojawić się błąd mówiący o&nbsp;braku pliku *Release* (oraz wzmianka o&nbsp;źródle `cdrom://`, nawet jeśli żadnej płyty CD nie mamy).  
Można go zignorować i&nbsp;się nie martwić. To taki artefakt trybu *live*, zapewne związany z&nbsp;tym, że część danych jest ładowana z&nbsp;pendrive'a."
trailer="<p><img class='figure bigspace-before' src='/assets/tutorials/linux-mint-jezyk-polski/linux-mint-lang-install-cdrom-error.png' alt='Zrzut ekranu pokazujący informację o&nbsp;błędzie podczas pobierania informacji o&nbsp;repozytoriach' /></p>"
%}

Po chwili powinna pojawić się informacja, że pakiet językowy został zainstalowany. Sukces! :+1: Teraz można przejść do kolejnego kroku, czyli ustawiania polskiego jako języka systemowego.

{% include details-end.html %}

{% include details.html summary="Sposób konsolowy" %}

Najpierw należy zaktualizować dostępne źródła:

<pre class="black-bg mono">
sudo apt-get update
</pre>

Następnie należy wpisać polecenie instalujące kilka polskich pakietów:

<pre class="black-bg mono">
sudo apt-get install language-pack-pl language-pack-pl-base language-pack-gnome-pl language-pack-gnome-pl-base
</pre>

Żeby się upewnić, że zadziałało, można użyć polecenia `localectl list-locales`.  
W konsoli wyświetli się lista, którą można przewijać strzałkami w&nbsp;górę i&nbsp;w dół. Jesli w&nbsp;jej dolnej części wypatrzymy tekst `pl_PL.UTF-8` -- to znaczy, ze mamy język polski.

{:.post-meta .bigspace-after}
Ta lista, a&nbsp;właściwie wyświetlający ją programik `less`, bywa pułapką na niewtajemniczonych. Żeby ją opuścić i&nbsp;wrócić do konsoli, trzeba nacisnąć przycisk `Q`.

{% include details-end.html %}

<a id="pakiety-jezykowe-instalacja-offline"/>
{% include details.html summary="Instalacja konsolowa bez internetu (dla chętnych)" %}

Ktoś chce zminimalizować zależność od internetu i&nbsp;móc na przykład spolszczyć Linuksa nawet na bezludnej wyspie? :sunglasses: Służę rozwiązaniem.

W zakładce parę linijek wyżej opisałem instalowanie przez konsolę pakietów językowych. W&nbsp;poleceniu można zmienić `install` na `download`:

<pre class="black-bg mono nospace">
<span class="corr-del">sudo apt install PAKIETY</span><br/>sudo apt download PAKIETY
</pre>

{:.figcaption}
Na tym etapie internet będzie potrzebny; ale tylko ten jeden raz.

W ten sposób zdobędziemy przenośne instalatory pakietów językowych w&nbsp;formacie `.deb` (jeśli są spakowane w&nbsp;archiwum, to należy je rozpakować, żeby mieć tylko pliki DEB). Wszystkie te instalatory można sobie zgrać na jakiegoś pendrive'a, którego będziemy nosić ze sobą.

{:.post-meta .bigspace-after}
Alternatywny sposób? Jeśli użyliśmy metody graficznej do zainstalowania pakietów, to można zaraz po tym zajrzeć do folderu `/var/cache/apt/archives` i&nbsp;skopiować z&nbsp;niego wszystkie pliki DEB (pomijając inne rzeczy).

Kiedy potem włączymy Minta, to można skopiować instalatory do jakiegoś folderu, uruchomić wewnątrz niego konsolę (np. przez otwarcie folderu w&nbsp;przeglądarce plików, a&nbsp;potem wybranie z&nbsp;górnego paska `File` i&nbsp;`Open in Terminal`). I&nbsp;użyć polecenia:

```
sudo dpkg -i *.deb
```

Zainstaluje to wszystkie pliki DEB obecne w&nbsp;folderze. Prosty sposób na spolszczenie; nawet bez łączności, nawet w&nbsp;ograniczonym trybie *live*.

{:.post-meta .bigspace-after}
Nadal trzeba będzie jednak wykonać kroki związane z&nbsp;ustawieniem języka i&nbsp;ponownym zalogowaniem, opisane niżej.

{% include details-end.html %}

W ten sposób pakiety zostaną zainstalowane. Ale język nie zmieni się na polski sam z&nbsp;siebie, trzeba go ustawić. Co opisuję w&nbsp;kolejnym kroku.

### Wybór języka polskiego w&nbsp;ustawieniach

Po pobraniu pakietów język polski dołączy do listy dostępnych opcji. Wystarczy go teraz ustawić jako język systemowy.  
Można to zrobić graficznie, można konsolowo. Niezależnie od tego, którym sposobem wykonało się instalację pakietów z&nbsp;poprzedniego kroku.

{% include details.html summary="Sposób graficzny" %}

Pozostajemy w&nbsp;tym samym menu z&nbsp;językami, które opisałem w&nbsp;poprzednim kroku. Przy każdym z&nbsp;wymienionych kryteriów klikamy `C.UTF-8` po prawej i&nbsp;wybieramy z&nbsp;listy język polski (od czasu zainstalowania pakietów już dostępny na liście).

{:.bigspace}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-lang-select-1.png" alt="Kolaż pokazujący najpierw przycisk z&nbsp;literą C, następnie kafelek z&nbsp;językiem polskim wybrany z&nbsp;listy, a&nbsp;na koniec ten sam przycisk co na początku, już z&nbsp;napisem 'Język polski'."/>

Gdy wszystkie trzy ustawienia zostaną zmienione na polski, należy kliknąć przycisk `Apply System-wide`, wprowadzający zmiany na poziomie systemu.

{:.bigspace-before}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-lang-select-2.png" alt="Zrzut ekranu pokazujący przycisk mówiący po angielsku 'zastosuj dla całego systemu'"/>

{% include details-end.html %}

{% include details.html summary="Sposób konsolowy" %}

{:.post-meta .bigspace-after}
Dziękuję za informacje stronce [Baeldung](https://www.baeldung.com/linux/localectl-tutorial).

Najpierw warto się upewnić, ze mamy zainstalowany język polski -- sposób w&nbsp;[poprzednim punkcie](#instalacja-polskich-pakietów-językowych){:.internal}, w&nbsp;rozwijanej zakładce o&nbsp;konsoli. Gdy to sobie potwierdzimy, to ustawienie języka jest kwestią jednej linijki:

```
localectl set-locale LANG=pl_PL.UTF-8
```

{% include details-end.html %}

Zmiana języka nie nastąpi samoistnie, trzeba wykonać jeszcze jeden drobny krok. 

### Odświeżenie ustawień

W przeciwieństwie do klawiatury i&nbsp;strefy czasowej, zmiany języka nie zostaną podchwycone od razu. **Należy się wylogować i&nbsp;zalogować ponownie**.  
Można to zrobić bez problemu nawet w&nbsp;trybie sesji *live USB* (w&nbsp;przeciwieństwie do przykładowego restartu systemu, który wyczyściłby pliki).

Podam tu jedynie sposób oparty na klikaniu. Należy:

* kliknąć ikonę Minta w&nbsp;dolnym lewym rogu,
* kliknąć opcję `Logout` z&nbsp;lewej kolumny (druga od dołu),
* potwierdzić w&nbsp;kolejnym oknie przyciskiem `Log Out` (tak, inny zapis), że chcemy to zrobić.

{:.post-meta .bigspace-after}
Wylogować można się również przez konsolę. Ale polecenia różnią się między wersjami Minta, więc dla uproszczenia ich tu nie przytoczę.

Przeniesie nas do okna logowania, gdzie już powinny się pokazać pierwsze oznaki spolszczenia -- na przycisku będzie napis `Zaloguj`. Klikając go, wrócimy do systemu.

Po ponownym zalogowaniu Mint może wyświetlić okno pytające, czy chcemy spolszczyć nazwy ważniejszych folderów (*Dokumenty*, *Muzyka*...) w&nbsp;przeglądarce plików. Można się zgodzić, klikając przycisk `Zaktualizuj nazwy` -- już po polsku -- w&nbsp;dolnym prawym rogu. Czemu nie.

{:.bigspace-before}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-zmiana-jezyka-aktualizacja.png" alt="Zrzut ekranu pokazujący informację o zmianie języka na polski i możliwości przetłumaczenia nazw głównych folderów"/>

{:.figcaption}
Po kliknięciu foldery polskojęzyczne widoczne w&nbsp;przeglądarce plików będą puste; to normalne, a&nbsp;my nie straciliśmy żadnych plików (jeśli jakieś tworzyliśmy). Znajdziemy je w&nbsp;folderach z&nbsp;angielskimi nazwami, np. *Desktop*, w&nbsp;katalogu domowym.

Efektem naszych działań będzie język polski w&nbsp;menu systemu i&nbsp;programach ściśle z&nbsp;nim zintegrowanych (takich jak centrum sterowania czy przeglądarka plików). Również ich pliki pomocy powinny zostać spolszczone, o&nbsp;ile ktoś je zakulisowo przetłumaczył.

{% include info.html
type="Uwaga"
text="Jeśli robiliśmy wszystko metodą przez menu, to zmiana języka na polski dotknie również programu LibreOffice -- zyskamy polską autokorektę oraz interfejs. Instalacja nie spolszczy natomiast menu Firefoksa (a&nbsp;przynajmniej nie zrobiła tego u&nbsp;mnie).  
Językowi polskiemu wewnątrz tych programów poświęcę osobny samouczek i&nbsp;go tu podlinkuję, gdy będzie gotowy."
%}

Na tym kończę część główną, mam nadzieję że Mint po polsku będzie jeszcze przyjaźniejszym systemem niż po angielsku :smile: Reszta wpisu to ciekawostki dla chętnych.

## Bonus: spolszczenie jednym skryptem

Wyżej podzieliłem się różnymi poleceniami konsolowymi. Jeśli ktoś nie boi się konsoli, to może dzięki nim wprowadzać zmiany szybciej niż poprzez menu. Prawdziwa siła komend ukazuje się natomiast wtedy, gdy rzeczy do zrobienia jest więcej.

Można bowiem układać takie komendy jedną pod drugą, linijkę pod linijką -- i&nbsp;uzyskać w&nbsp;ten sposób **skrypt konsolowy**. Po jego uruchomieniu polecenia zostaną wykonane po kolei. A&nbsp;to ogromna oszczędność czasu. Najszybszy sposób na przełączenie całego Minta na język polski.

Można się upewnić, że mamy na naszym Mincie łączność z&nbsp;siecią, a&nbsp;następnie skopiować cały kikulinijkowy blok tekstu widoczny poniżej, wkleić go do konsoli i&nbsp;nacisnąć `Enter`. Potem można podziwiać *hakierskie*, przewijające się ściany tekstu.

<pre class="black-bg mono bigspace-before nospace">
setxkbmap pl
timedatectl set-timezone Europe/Warsaw
sudo apt-get update
sudo apt-get install language-pack-pl language-pack-pl-base language-pack-gnome-pl language-pack-gnome-pl-base
localectl set-locale LANG=pl_PL.UTF-8
</pre>

{:.figcaption}
Ze względu na `sudo` możliwe, że pojawi się prośba o&nbsp;wpisanie hasła; u&nbsp;mnie w&nbsp;trybie *live* nie pyta, ale w&nbsp;przypadku zainstalowanego Linuksa raczej będzie. Bez obaw!

Na koniec trzeba się [wylogować i&nbsp;zalogować ponownie](#odświeżenie-ustawień){:.internal}, żeby podchwyciło zmiany.  
Potem można użyć `setxkbmap pl` ponownie, bo wylogowanie resetuje to ustawienie.

Ktoś nie chce każdorazowo kopiować stąd tekstu? To można zapisać go do pliku, a&nbsp;następnie nosić go ze sobą na pendrivie. I&nbsp;albo z&nbsp;niego kopiować, albo uruchamiać go kliknięciem (jeśli ktoś wie jak).

{:.post-meta}
Jeśli ktoś chce dostosować skrypt do [instalacji offline](#pakiety-jezykowe-instalacja-offline){:.internal}, to należy zamiast linijek trzeciej i&nbsp;czwartej (z&nbsp;`apt-get`) dać jedną -- `sudo dpkg -i *.deb`, taką jak w&nbsp;linkowanej zakładce.  
Oczywiście należy trzymać pobrane pliki DEB w&nbsp;tym samym folderze, w&nbsp;którym uruchamiamy skrypt/konsolę.
