---
layout: page
title: "Jak instalować rzeczy na systemach Linux Mint, Zorin, Debian i Ubuntu"
description: "System bez programów jest niczym. A jak je zdobyć?"
---

Linux to otwarty i&nbsp;darmowy system operacyjny, stanowiący [coraz atrakcyjniejszą alternatywę](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal} dla dominującego Windowsa.  
Wyróżnia się głównie tym, że bardziej szanuje wolność i&nbsp;prywatność swoich użytkowników. A&nbsp;że ten blog skupia się na cyfrowej prywatności, to Linux gości w&nbsp;różnych samouczkach. Takich jak ten.

Pokażę tu, **w jaki sposób instaluje się różne rzeczy na Linuksach z&nbsp;„rodziny” Debiana**, wykorzystujących pliki DEB. Do tej grupy należą najpopularniejsze Linuksy, takie jak: Mint, Zorin, Debian czy Ubuntu.

Do kogo kieruję wpis? Do osób chcących nabrać intuicji w&nbsp;sprawach instalacyjnych i&nbsp;nie kopiować na oślep poleceń z&nbsp;internetu.

Omówię po ludzku podstawowe mechanizmy, programy z&nbsp;interfejsem graficznym, instalatory konsolowe i&nbsp;parę pułapek, w&nbsp;jakie można wpaść.  
Będzie też o&nbsp;instalowaniu *offline*, bez internetu -- co może się przydać podczas używania systemu w&nbsp;trybie *live* („systemowym *incognito*”).

Zapraszam!

{% include info.html
type="Uwaga"
text="Nie omawiam instalowania na innych Linuksach, takich jak Fedora i&nbsp;jej pochodne (tam używa się plików RPM) czy wszelkie Linuksy dla osób lubiących majsterkować. Tym niemniej: pierwsza część samouczka jest na tyle ogólna i&nbsp;uniwersalna, że zachęcam do jej przeczytania."
%}

## Spis treści

{:.post-meta .bigspace-after}
Wpis jest naprawdę długi. Jeśli komuś nie zależy na kontekście, tylko rozwiązaniach, to można przeskoczyć prosto do omówienia programów: [graficznych](#programy-zinterfejsem-graficznym){:.internal} albo [konsolowych](#instalacja-konsolowa-przez-apt-a){:.internal}.

* [Ogólnie o&nbsp;instalowaniu](#ogólnie-oinstalowaniu)
  * [Instalacja ma kilka etapów](#instalacja-ma-kilka-etapów)
  * [Piramidki zależności](#piramidki-zależności)
  * [Kwestia uprawnień administratora](#kwestia-uprawnień-administratora)
* [Instalowanie na Linuksach opartych na Debianie](#instalowanie-na-linuksach-opartych-na-debianie)
  * [Podział ról](#podział-ról)
  * [Kwestia plików i&nbsp;ich źródeł](#kwestia-plików-iich-źródeł)
  * [Programy z&nbsp;interfejsem graficznym](#programy-zinterfejsem-graficznym)
  * [Instalacja konsolowa przez APT-a](#instalacja-konsolowa-przez-apt-a)
  * [Instalowanie z&nbsp;plików](#instalowanie-zplików)
* [Rozwiązywanie błędów](#rozwiązywanie-błędów)
  * [„Pakiet nie ma kandydata do instalacji”](#pakiet-nie-ma-kandydata-do-instalacji)
  * [„Zatrzymano uszkodzone pakiety”](#zatrzymano-uszkodzone-pakiety)
  * [„Niespełnione zależności”](#niespełnione-zależności)
  * [Brak pliku Release (na Mincie z&nbsp;pendrive'a)](#brak-pliku-release-na-mincie-zpendrivea)
  * [„Nie udało się otworzyć pliku blokady”](#nie-udało-się-otworzyć-pliku-blokady)
* [Bonus: instalowanie offline](#bonus-instalowanie-offline)
  * [Etap pierwszy: pobieranie](#etap-pierwszy-pobieranie)
  * [Etap drugi: instalacja](#etap-drugi-instalacja)

## Ogólnie o&nbsp;instalowaniu

Zwrot „system Linux” jest strasznie nieprecyzyjny. Na bazie Linuksa powstała cała galaktyka systemów, w&nbsp;tym kilka wielkich rodzin. Ich częścią wspólną jest jedynie *jądro systemu*, jego misterne wnętrze.

Podobne rozdrobnienie panuje w&nbsp;kwestii instalowania rzeczy z&nbsp;zewnątrz. Linuksy łączy tu ogólny motyw: jakiś program, który pozwala łatwo pobierać moduły z&nbsp;zaprzyjaźnionej bazy i&nbsp;czynić je częścią systemu.

A jaki to program, jakich używa formatów i&nbsp;jakiej bazy? Na tym poziomie pojawiają się różnice.

Najpierw opiszę te bardziej uniwersalne kwestie, które łączą Linuksy ponad podziałami. Oczywiście odnoszą się również do Linuksów „debianowatych”.

### Instalacja ma kilka etapów

Instalacja z&nbsp;punktu widzenia użytkowników bywa prosta. Uruchamia się program, chwilę czeka aż coś sobie załaduje. Wyszukuje się coś po nazwie, klika `Instaluj` i&nbsp;czeka, aż nowe rzeczy zostaną zainstalowane. 

Wszystko wygląda jak jeden płynny proces. A&nbsp;tymczasem pod spodem zachodzi kilka rozłącznych etapów:

1. odświeżenie listy plików dostępnych w&nbsp;internetowych bazach;
2. pobranie z&nbsp;internetu pakietów z&nbsp;rzeczami do zainstalowania;
3. instalacja właściwa.

Odnośnie punktu 1&nbsp;-- świeży system ma zapisane jedynie ogólne adresy baz. Ich zawartość czasem się zmienia, pojawiają się nowe wersje programów... Dlatego wiele menedżerów po uruchomieniu *odświeża pamięć podręczną*. Po ludzku: aktualizuje informacje o&nbsp;dostępnych rzeczach.

Do punktu 2&nbsp;nie mam uwag, jest dość oczywisty.

Odnośnie punktu 3&nbsp;-- na tym etapie następuje wypakowanie plików z&nbsp;wnętrza pakietu i&nbsp;ułożenie ich we wskazanych miejscach. Często są też aktualizowane różne systemowe listy, jak lista programów z&nbsp;własnymi ikonami.

{% include info.html
type="Analogia smartfonowa"
text="Cały proces instalacji bardzo przypomina ten znany choćby [ze smartfonów](/google/2025/10/02/google-play-store-weryfikacja-tozsamosci#instalowanie-aplikacji-na-androidzie){:.internal}. Tyle że zamiast kontrolowanej przez Google'a bazy Sklep Play i&nbsp;stale dociskanej śruby mamy przyjaźniejsze źródła. I&nbsp;można łatwo zdobywać pliki spoza oficjalnych baz -- nikt nie próbuje tego demonizować tak jak Google."
%}

### Piramidki zależności

Warto też wiedzieć, czym są **zależności** (ang. *dependencies*). To różne programy i&nbsp;biblioteki, których wymaga do działania instalowana rzecz.

{:.post-meta .bigspace-after}
Przykładowo: program OpenSnitch, pozwalający wyłapywać podejrzany ruch sieciowy, wymaga do działania m.in. modułów *PyQT* (od interfejsu graficznego) oraz *Libnetfilter*.

Te moduły również mogą opierać się na swoich zależnościach, one z&nbsp;kolei na swoich... I&nbsp;tak dalej.  
Można to przedstawić jako piramidkę. Zielone rzeczy już mamy zainstalowane, czerwonych jeszcze nie. Jeśli jakiś klocek leży pod innym, to jest jego zależnością.

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/zaleznosci-podstawa.png" alt="Schemat pokazujący piramidkę zbudowaną z&nbsp;prostokątów o&nbsp;różnych rozmiarach. Te na dole są zielone, te wyżej czerwone i&nbsp;półprzezroczyste."/>

{:.figcaption}
Źródło: nieśmiertelny [komiks XKCD](https://xkcd.com/2347/). Przeróbki moje.

Na bardziej doszlifowanych Linuksach **nie trzeba się martwić zależnościami, programy ogarniają je za nas** i&nbsp;„budują piramidkę od podstaw”.

{:.post-meta}
Wyjątkiem jest sytuacja, kiedy instalujemy coś ręcznie, *offline*, i&nbsp;sami musimy zadbać o&nbsp;zdobycie zależności. Jeszcze do tego wrócę.

### Kwestia uprawnień administratora

W wielu przypadkach **instalowane rzeczy trafiają do folderów systemowych**; nawet proste czcionki lądują w&nbsp;`/usr/share/fonts`. Ingerowanie w&nbsp;takie foldery wymaga uprawnień administratora (językiem linuksowym: *roota*).

Z tego względu nie ma co się dziwić, jeśli program sterujący instalacją poprosi przed nią o&nbsp;*uwierzytelnienie*, czyli potwierdzenie uprawnień (albo nie poprosi, za to wyświetli błąd).  
**Potwierdzamy je przez wpisanie hasła**, jeśli mamy jakieś ustawione.

To normalne, warto się do tego przyzwyczaić. Po instalacji większość programów będzie już śmigała bez uprawnień admina, bo samo *czytanie* plików systemowych ich nie wymaga.

{:.post-meta .bigspace-after}
Jeśli ktoś chce instalować bez pełni uprawnień (bo np. ktoś inny jest adminem, a&nbsp;osoba instalująca tylko gościem), to zapewne będzie trzeba instalować pliki w&nbsp;jakimś niestandardowym, niesystemowym miejscu. Takiego przypadku tu nie omawiam, zakładam pełnię kontroli nad systemem.

## Instalowanie na Linuksach opartych na Debianie

Wyżej były rzeczy uniwersalne, teraz już wchodzimy na teren „rodu Debiana”, jednego z&nbsp;najbardziej wpływowych na Linuksach. Przypomnę: należą do niego Linuksy takie jak Mint, LMDE, Zorin, Ubuntu.

### Podział ról

Na Linuksach „debianowatych” **panuje podział ról** -- nie ma jednego wielkiego instalatora, tylko kilka osobnych programów, które ze sobą współpracują.  
Sytuację można porównać do działów jakiejś fikcyjnej firmy:

* instalatory graficzne

  „Dział obsługi klienta”, który ma ładnie się prezentować, przyjmować prośby i&nbsp;przekazywać je tym od działania. W&nbsp;praktyce intuicyjne, graficzne menu, przez które można wyszukiwać i&nbsp;instalować programy.

* program APT

  „Dział zaopatrzenia”, który przywozi rzeczy na miejsce i&nbsp;je inwentaryzuje. W&nbsp;praktyce: APT ustala, czego potrzeba i&nbsp;pobiera to z&nbsp;internetu.  
  Można powiedzieć, że realizuje bezpośrednio [ogólne etapy](#instalacja-ma-kilka-etapów){:.internal} numer 1&nbsp;i 2. Ostatni krok zostawia DPKG.

* program DPKG

  „Dział montażu”, ludzie od fizycznej roboty. Odpowiada za *instalację właściwą* wskazanych plików (etap ogólny numer 3), umieszcza je w&nbsp;oczekiwanych folderach. Zwykle działa na polecenie APT-a, ale można go też kontrolować bezpośrednio.

Świetną właściwością APT-a (z&nbsp;której korzystają też oparte na nim interfejsy) jest to, że **automatycznie ustala i&nbsp;pobiera potrzebne zależności**. Dzięki temu zdobywamy wszystko, co potrzebne do działania programów.

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/zaleznosci-schemat-instalacja-pelna.png" alt="Zmiana piramidki zależności po instalacji pakietów pobranych przez apt-get. Zdobyty został tylko pakiet na wierzchołku, reszta nadal jest zaciemniona."/>

{:.figcaption}
Przykładowa instalacja przez APT-a -- albo oparte na nim interfejsy -- jakiegoś pakietu X.  
Część nadal czerwona, bo nie były to zależności bezpośrednie, więc nie zostały pobrane.

### Kwestia plików i&nbsp;ich źródeł

Wyżej wspomniałem o&nbsp;plikach. W&nbsp;przypadku Linuksów opartych na Debianie jednym z&nbsp;głównych formatów związanych z&nbsp;instalacją są **pliki DEB** (czasem będę też pisał `.deb`).  
To one są pobierane przez APT-a, a&nbsp;potem przetwarzane przez DPKG. Każdy z&nbsp;nich może zawierać dowolną ilość rzeczy, od sporych programów po pomocnicze biblioteki, a&nbsp;nawet pojedyncze czcionki.

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/pliki-deb-ilustracja.png" alt="Dwa pliki DEB wewnątrz menedżera plików" />

{:.figcaption}
Przykładowe pliki DEB w&nbsp;przeglądarce plików systemu Zorin.  
Moduł `plocate` to program dla użytkowników; `liburing2` to biblioteka, której potrzebuje do działania. Automatycznie instalowana, jako zależność, gdy instalujemy `plocate`.

Program APT, główny „zdobywca rzeczy”, pobiera je wyłącznie z&nbsp;dozwolonych źródeł, które ma na swojej liście (zwanych *repozytoriami*).  
Ta domyślna lista różni się nawet między systemami z&nbsp;tego samego „rodu Debiana”. Można wyróżnić dwa dominujące źródła:

1. Bazy Debiana  
   Korzystają z&nbsp;nich systemy takie jak Debian czy LMDE (*Linux Mint Debian Edition*; odmiana Minta).

2. Bazy firmy Canonical (twórców Ubuntu)  
   Korzystają z&nbsp;nich: Ubuntu, Zorin, pozostałe odmiany Minta.

Można również **własnoręcznie dodawać bazy do listy**.  
Jeśli ich twórcy zadbali o&nbsp;zgodność, to cała instalacja z&nbsp;punktu widzenia użytkowników będzie przebiegała dokładnie tak samo, jakby instalowali z&nbsp;oficjalnych baz. Zwiększy się jedynie liczba rzeczy dostępnych na liście.

{:.post-meta .bigspace-after}
Przykładem większego projektu, który udostępnia rzeczy przez własną bazę, jest [przeglądarka Brave](https://linuxcapable.com/how-to-install-brave-browser-on-ubuntu-linux/).

W tym wpisie źródła właściwie nie mają znaczenia; w&nbsp;przykładach używam tego, co system domyślnie zapewnia. Warto natomiast zapamiętać, że nie zapewnia wszystkiego, ale alternatywy są na wyciągnięcie ręki.

Czasem zdarza się również, że ktoś **udostępnia pliki DEB bezpośrednio, poza bazami**. Nadal można je instalować, zaś ewentualne zależności powinny zostać automatycznie pobrane z&nbsp;internetu (o&nbsp;ile używa się APT-a albo opartych na nim interfejsów).

{:.post-meta}
Przykładem tak rozpowszechnianego programu jest [OpenSnitch](https://github.com/evilsocket/opensnitch/releases). W&nbsp;opisie można znaleźć linki m.in. do plików DEB.

### Programy z&nbsp;interfejsem graficznym

Wiele osób jest nieprzyzwyczajonych do konsoli i&nbsp;woli instalować wszystko przez zwykłe, klikalne menu. Popularne Linuksy wychodzą tej potrzebie naprzeciw, choć z&nbsp;różnym skutkiem.

W tej części omówię krótko dostępne programy. Zazwyczaj nie trzeba ich instalować, są od początku częścią systemu.

{:.post-meta .bigspace-after}
Przypominajka: [wyżej](#podział-ról){:.internal} omówiłem miejsce tych programów-nakładek w&nbsp;hierarchii.  
Przyznam uczciwie, że sprawdzałem tylko Minta i&nbsp;Zorina, dlatego zdominują tę część.

{% include details.html summary="Programy na Mincie" %}

{:.bigspace-before}
Mint rozpieszcza użytkowników i&nbsp;zapewnia kilka programów pozwalających instalować rzeczy z&nbsp;zewnątrz. Wszystkie korzystają za kulisami z&nbsp;APT-a.

Głównym programem od instalowania rzeczy jest **Menedżer Oprogramowania** (ang. *Software Manager*).  
Można go uruchomić nawet wtedy, gdy nie do końca wiemy, czego chcemy -- umożliwia eksplorację, przeszukiwanie baz, a&nbsp;potem wybranie znalezionej rzeczy i&nbsp;jej szybkie zainstalowanie.

Aby go użyć, można:

1. połączyć się z&nbsp;internetem,
2. kliknąć ikonę Minta w&nbsp;dolnym lewym rogu,
3. kliknąć pole `Menedżer Oprogramowania`,
4. po otwarciu programu wyszukać po tekście interesujący nas pakiet i&nbsp;kliknąć odpowiadający mu kafelek,
5. kliknąć przycisk `Instaluj`.

{:.bigspace}
<img src="/assets/tutorials/linux/apt-instalowanie/mint-instalowanie-programow-interfejs-graficzny.png" alt="Zrzuty ekranu pokazujące menu Minta oraz okno jego Menedżera Oprogramowania"/>

A co, jeśli mamy na dysku pobrany skądś plik `.deb` i&nbsp;go dwukrotnie klikniemy? W&nbsp;takim wypadku włączy się program o&nbsp;nazwie **_Captain_**. Wyświetli listę zależności, jakich wymaga dany pakiet. Jeśli potwierdzimy chęć instalacji, to wszystko pobierze i&nbsp;zainstaluje, zwracając się do APT-a.

{:.post-meta .bigspace-after}
Jego nazwa nie jest oczywista, bo nie pojawia się nigdzie wewnątrz okna; musiałem sprawdzić [programem `xprop`](/miniposts/linux-mint-engrampa-strace.html#ustalenie-nazwy-programu-xprop){:.internal}, żeby ją poznać.

Choć Captain bardzo ułatwia instalację plików z&nbsp;zewnątrz, ma też wady. Jeśli zaznaczy się wiele plików DEB i&nbsp;je otworzy, to każdy z&nbsp;nich dostanie osobne okno. Lepsze wydawałoby się jedno okno, porządkujące zaznaczone pakiety (np. jako drzewko) i&nbsp;pozwalające na ich masową instalację.

{% include info.html
type="Ciekawostka"
text="Miałem przyjemność [zaproponować drobną poprawkę](https://github.com/linuxmint/captain/pull/23) do programu Captain. Jeśli zostanie przyjęta, to okno nie pozostanie wygaszone w&nbsp;razie nieudanej instalacji. Pozostaje czekać, aż twórcy Minta znajdą chwilkę czasu na jej zaakceptowanie."
%}

Parę innych programów wbudowanych w&nbsp;Minta ma możliwość instalowania rzeczy z&nbsp;wąskiej listy, związanych ze swoją „działką”.  
Przykładowo: program od ustawień językowych (nazwa wewnętrzna `mintlocale`; [bohater innego mojego samouczka](/tutorials/linux-mint-jezyk-polski-system.html){:.internal}) pozwala pobierać przez swój interfejs pakiety z&nbsp;tłumaczeniami różnych programów.

{% include details-end.html %}

{% include details.html summary="GNOME Software na Zorinie (ku przestrodze!)" %}

{:.bigspace-before}
Na Zorinie domyślnie zainstalowanym programem od instalowania innych programów jest **_GNOME Software_**. Osobiście za nim nie przepadam, parę przyczyn zaraz wymienię. Ta najgorsza w&nbsp;kontekście tego wpisu: [nie pozwala szukać w&nbsp;bazach plików DEB](https://forum.zorin.com/t/apt-repository-applications-do-not-appear-in-software-center/22154/7).

Pokazuje jedynie rzeczy udostępniane w&nbsp;nowszych formatach „kontenerowych”, jak Flatpak. A&nbsp;że posługują się nim raczej większe projekty *open source*, pełnoprawne programy itd., to mnóstwa drobniejszych rzeczy się przez *GNOME Software* zwyczajnie nie znajdzie.

{% include info.html
type="Ciekawostka"
text="Nazwa programu bierze się stąd, że jest częścią tak zwanego *środowiska GNOME*. Tworzą je (niezwiązani z&nbsp;Zorinem) ludzie mocno przekonani do swoich racji, nieraz wycinający lubiane funkcje w&nbsp;imię tworzenia współczesnego interfejsu.  
Spotykają się przez to z&nbsp;[falami krytyki](https://medium.com/@fulalas/gnome-the-insanity-never-ends-f84a77ec3e13). Uważałem ją kiedyś za jojczenie purystów... Ale im bardziej poznaję świat Linuksów, tym lepiej ją rozumiem."
%}

*GNOME Software* nie jest tak całkiem wrogi plikom `.deb` i&nbsp;obsługuje przynajmniej klikanie plików ręcznie pobranych. Tyle że... **Jeśli nie mamy łączności z&nbsp;internetem, to instalacja po cichu się nie powiedzie**. Nawet jeśli klikniemy niezależny plik DEB, któremu nie brakuje żadnych zależności.  
Po kliknięciu przycisk instalujący zmieni stan i&nbsp;taki pozostanie, nie wyświetlając żadnej informacji zwrotnej:

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/gnome-software-instalacja-bez-internetu.png" alt="Dwa stany przycisku od instalacji w&nbsp;programie GNOME Software Manager: aktywny i&nbsp;zawieszony"/>

{:.post-meta .bigspace-after}
Tak zawiesza się przycisk na Zorinie 18&nbsp;(świeżo załadowanym z&nbsp;pendrive'a) przy próbie zainstalowania modułu `liburing2`, gdy nie ma internetu.  
Mam nadzieję, że w&nbsp;przyszłych wersjach się to poprawi.

A jeśli już się połączymy z&nbsp;tym internetem? To nadal **wywali błąd, jeśli klikniemy plik posiadający brakujące zależności**. Nawet gdy te zależności leżą obok w&nbsp;tym samym folderze:

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/plocate-ilustracja-nieudanej-instalacji.png" alt="Zrzuty ekranu pokazujące dwa pliki DEB obok siebie i&nbsp;komunikat o&nbsp;błędzie mówiący, że jednego z&nbsp;nich nie znaleziono"/>

{:.figcaption}
Polski mieszany z&nbsp;angielskim to tylko tymczasowa niedogodność, łatwa do naprawienia.

Błąd by zniknął, gdyby zaktualizować listy APT-a. Tyle że program nawet nie sugeruje takiej opcji i&nbsp;trzeba by to zrobić na własną rękę. Czy to się nie kłóci z&nbsp;ideą graficznego interfejsu ułatwiającego życie?

No to może pokazać te zależności wprost -- zaznaczając wiele plików DEB naraz (główny oraz zależności) i&nbsp;wybierając opcję ich otwarcia?  
Lipa. Otworzy się tylko jedno okno, dotyczące jednego pakietu. 

W obliczu tylu wad programu proponuję nie kopać się z&nbsp;koniem i&nbsp;pliki DEB instalować na Zorinie [przez konsolę](#instalacja-konsolowa-przez-apt-a){:.internal}. Albo zainstalować jakiś graficzny zamiennik, jak *GDebi* (wspomniany niżej).  
Zorin niestety spycha w&nbsp;stronę APT-a, utrwalając stereotyp o&nbsp;Linuksie dla konsolowców.

{% include details-end.html %}

{% include details.html summary="Inne programy z&nbsp;interfejsem graficznym" %}

{:.post-meta .bigspace-after}
Nie korzystałem z&nbsp;żadnego z&nbsp;tych  programów, tylko cytuję znalezione informacje. Mogą być nieaktualne, podchodźcie do nich krytycznie.

Z systemem Ubuntu nie jestem na bieżąco. Albo trzymają się *GNOME Software*, którego krytykuję wyżej, albo rozwijają coś własnego. Ale nawet w&nbsp;tym drugim przypadku nie liczyłbym na łatwą pracę z&nbsp;plikami DEB (Ubuntu bardzo promuje własny format o&nbsp;nazwie *Snap*).

{:.post-meta .bigspace-after}
Dość powiedzieć, że przez pewien czas w&nbsp;ogóle [nie wspierali instalacji przez klikanie plików DEB](https://linuxconfig.org/ubuntu-26-04-no-app-deb-files). Jak jest teraz? Nie wiem, nie sprawdzałem, ale ostrzegę.

Na klasycznym Debianie za instalowanie odpowiada [*Synaptic*](https://github.com/mvo5/synaptic/wiki).

Istnieje również niezależny program od instalowania, zwący się [*GDebi*](https://pl.wikipedia.org/wiki/GDebi), podobno fajny.

Wszystkie wymienione programy łączy ogólna zasada działania -- czeka się chwilę na aktualizację baz, wyszukuje interesujący nas moduł/pakiet, po czym instaluje go kliknięciem.

{% include details-end.html %}

### Instalacja konsolowa przez APT-a

Instalacja konsolowa polega na tym, że uruchamia się program o&nbsp;nazwie Terminal, wpisuje albo wkleja w&nbsp;niego komendę, a&nbsp;potem czeka, aż wskazana rzecz się zainstaluje.

{:.post-meta .bigspace-after}
W tym trybie potrzebna jest łączność z&nbsp;internetem; instalację *offline* omawiam później.  
Jak coś tekst wkleja się nietypowym skrótem <code>Ctrl+<span class="red">Shift</span>+V</code>.

Najprostszej instalacji konsolowej odpowiadają takie dwie linijki:

<pre class="black-bg mono">sudo apt update<br/>sudo apt install PAKIET</pre>

Linijka pierwsza odpowiada [etapowi ogólnemu](#instalacja-ma-kilka-etapów){:.internal} numer 1. Odświeża listę dostępnych rzeczy -- co ma spore znaczenie, bo przy nieaktualnych listach mogą wyskakiwać [błędy](#pakiet-nie-ma-kandydata-do-instalacji){:.internal}. Nie trzeba jej używać za każdym razem, ale dla pewności można.

Linijka druga odpowiada etapom ogólnym 2&nbsp;i 3. Instaluje wskazany `PAKIET` -- musi to być pełna, wewnętrzna nazwa pakietu, który chcemy zainstalować. Zakładam, że tę nazwę gdzieś ktoś podał (na forum, w&nbsp;instrukcji...) i&nbsp;nie trzeba jej ustalać.

...I to w&nbsp;sumie tyle! Po użyciu komendy powinno poprosić o&nbsp;podanie hasła admina ([normalna rzecz](#kwestia-uprawnień-administratora){:.internal}). Potem zapewne o&nbsp;potwierdzenie, że chcemy zainstalować ileśtam megabajtów nowych rzeczy. Robi się to przez wciśnięcie odpowiedniego klawisza (`T` na spolszczonym systemie, `Y` na angielskim), a&nbsp;po nim klawisza `Enter`.

Kiedy potwierdzimy, to konsola zapełni się tekstem. Ostatnie linijki powinny wspominać o&nbsp;przetwarzaczach (ang. *triggers*), a&nbsp;linijkę niżej powinien migać kursor, sugerując gotowość do przyjmowania dalszych komend.

Można spojrzeć szybko na ostatnie linijki i&nbsp;wyłapać, czy nie ma żadnych błędów. Gdyby były, to można przejść do [możliwych rozwiązań](#rozwiązywanie-błędów){:.internal}.

W rozwijanych zakładkach parę nieobowiązkowych poszerzaczy wiedzy.

{% include details.html summary="apt kontra apt-get" %}

{:.bigspace-before}
W przykładzie użyłem programu konsolowego `apt`. Warto jednak wiedzieć, że APT to **cały pakiet programów, z&nbsp;których dwa są bardzo podobne**:

* starszy `apt-get`, typowo od instalacji,
* nowszy `apt`, ogólniejszy.

Na szczęście w&nbsp;przypadku najprostszej instalacji różnica między programami zanika -- `apt install` i&nbsp;`apt-get install` prowadzą do tego samego efektu; można je stosować zamiennie.

{:.post-meta .bigspace-after}
Obowiązkowe krycie tyłka: *prawie* zawsze, z&nbsp;tego co wiem, akceptuję istnienie wyjątków *et cetera*.

Jeśli jednak wyjdzie się poza komendy od instalowania, to przybywa różnic. W&nbsp;szczególności `apt(-get) download` ma parę swoich dziwactw, o&nbsp;których jeszcze wspomnę.

Co praktycznego warto zapamiętać? Żeby **nie mieszać _alkoholi_{:.corr-del} programów**. Jeśli znalazło się w&nbsp;internecie przykład, gdy ktoś używa `apt-get`, to raczej tego się trzymać i&nbsp;nie zmieniać go na `apt` w&nbsp;ramach własnej inwencji.  
A jeśli tworzy się porady dla innych osób -- to nie zmieniać *last minute* jednego programu na drugi, jakby były synonimami.

{:.post-meta}
Sam się na tym przejechałem; możecie się uczyć na moich błędach :wink:

{% include details-end.html %}

{% include details.html summary="Ustalanie nazw pakietów" %}

{:.bigspace-before}
Wyżej założyłem, że znamy pełną nazwę jakiegoś pakietu/modułu, który chcemy zdobyć.  
Tak często jest; instrukcje instalacji albo porady na forach nieraz zawierają gotowe polecenia pokroju `sudo apt install NAZWA`, które wystarczy skopiować. Społeczność linuksowa lubi i&nbsp;umie pomagać.

Warto jednak wiedzieć, że ogólnie **nazwa modułu nie zawsze odpowiada nazwie zawartości**. Nawet przy rzeczach znanych.  
Przykłady? Czcionka *Comic Sans* jest w&nbsp;pakiecie `ttf-mscorefonts-installer`. Przeglądarka Brave jest w&nbsp;pakiecie o&nbsp;nazwie `brave-browser`.

{:.post-meta .bigspace-after}
Pomijam już to, że Brave nie jest dostępna przez domyślne bazy, tylko swoje własne. To dlatego, że częściej pobiera się ją jako Flatpaka niż plik DEB.

{% include info.html
type="Ciekawostka"
text="Takie różnice w&nbsp;nazwach bywają czasem używane przez hakerów do **_squattingu_** -- wypuszczania złośliwych paczek, np. z&nbsp;wirusami, o&nbsp;nazwach zbliżonych do oryginałów. W&nbsp;nadziei na to, że ludzie instalujący w&nbsp;ciemno się nabiorą."
trailer="<p class='post-meta'>Ludzie obsługujący główne bazy z&nbsp;pakietami DEB robią jakąśtam kontrolę bezpieczeństwa, ale wiadomo, że czasem coś się może przemknąć. Nawet Play Store od Google'a, lansowany jako bezpieczny, ma niemało wirusów.</p>"
%}

Co zrobić, jeśli znamy nazwę jakiejś rzeczy, ale nie wiemy, jakiego pakietu jest częścią?

Można zapytać rzetelniejszego Ej-Aja albo przeszukać internety. Pomocna może być tutaj (niezależna, nieoficjalna) stronka [*pkgs.org*](https://pkgs.org/).  
Zawiera przyporządkowanie nazw rzeczy do pakietów (również DEB), w&nbsp;jakich są rozpowszechniane.

Inna opcja, gdy nazwa pakietu *zawiera* nazwę rzeczy plus coś jeszcze?  
Po zaktualizowaniu listy rzeczy (`sudo apt update`) można poszukać fragmentu nazwy w&nbsp;bazie (`apt search TEKST`). A&nbsp;potem sprawdzić, czy pakiet pasujący nazwą faktycznie odpowiada temu, czego szukamy.

{% include details-end.html %}

### Instalowanie z&nbsp;plików

Jeśli już mamy na dysku pobrany plik `.deb`, zdobyty z&nbsp;tego czy innego źródła, to można go zainstalować przez APT-a:

```
sudo apt update
sudo apt install PLIK.deb
```

Warto jednak wiedzieć, że w&nbsp;tym przypadku należy mieć łączność z&nbsp;internetem, zaś ewentualne zależności zostaną pobrane z&nbsp;baz APT-a, a&nbsp;nie wzięte z&nbsp;folderów. Nawet jeśli leżą obok instalowanego pliku.

{% include details.html summary="Inne niedogodności" %}

{:.bigspace-before}
Zazwyczaj konsola automatycznie podpowiada nazwy plików po naciśnięciu klawisza `Tab`. Nie w&nbsp;tym wypadku. Gdyby zaczęło się wpisywać `sudo apt install PIERWSZE_LITERY` i&nbsp;wcisnęło `Tab`, to niczego nie podpowie. 

Jak zatem uniknąć przepisywania pełnej nazwy pakietu do konsoli? Można chwycić plik DEB i&nbsp;upuścić go wewnątrz okna konsoli -- automatycznie wstawi się wtedy jego pełna ścieżka.

Kolejna pułapka: jeśli użyje się tylko drugiej linijki, bez aktualizowania baz, zaś instalowany plik ma brakujące zależności, to wyświetli [błąd zatrzymanych pakietów](#zatrzymano-uszkodzone-pakiety){:.internal} („*You have held broken packages*”). Ale przynajmniej nie zablokuje to innych instalacji.

Inna przeszkadzajka? Jeśli użyje się polecenia na prostym pliku bez żadnych zależności, to zostanie zainstalowany, ale może się wyświetlić mylące ostrzeżenie mówiące coś o&nbsp;pobieraniu. Można je olać.

{% include details-end.html %}

Można też użyć programu **DPKG**, pomijając internet i&nbsp;mechanizmy APT-a.  
Może to przynieść niespodziewane skutki, więc **odradzam to mniej wprawionym**. Ale samą metodę warto poznać.

Ogólna komenda to:

<div class="black-bg mono">sudo dpkg -i PLIK.deb</div>

Albo, jeśli chcemy zainstalować *wszystkie* pliki z&nbsp;aktywnego folderu:

<div class="black-bg mono nospace">sudo dpkg -i *.deb</div>

{:.post-meta .bigspace-after}
Warto zaznaczyć, że gwiazdka to znak specjalny wewnątrz konsoli; ta komenda by nie zadziałała, gdyby np. użyć jej przez Pythona bez ustawienia odpowiedniej zmiennej.

Bezpośrednie używanie DPKG może niestety wpędzić użytkowników w&nbsp;pułapkę. A&nbsp;to dlatego, że **ten program nie pobiera brakujących zależności**. Jeśli na jakieś się natknie podczas próby instalacji, to wystąpi [błąd niespełnionych zależności](#niespełnione-zależności){:.internal}, blokujący *wszelkie* możliwości instalacji do czasu jego rozwiązania.

Czy zatem instalacja przez DPKG ma jakiekolwiek zalety? Tak -- pozwala uniknąć aktualizowania list APT-a i&nbsp;łączności z&nbsp;siecią, co najlepiej pasuje do [instalacji w&nbsp;trybie *offline*](#bonus-instalowanie-offline){:.internal} albo na komputerach odizolowanych.

## Rozwiązywanie błędów

Instalowanie działa jak złoto... Póki działa. Ale czasem zdarza się, że z&nbsp;jakiejś przyczyny pojawi się ciut niejasny komunikat o&nbsp;błędzie. APT ma swoje dziwactwa.  
Co gorsza, interfejs graficzny może obsługiwać te błędy po swojemu. Robi się wtedy głuchy telefon.

W tym miejscu zebrałem kilka błędów, na które osobiście się nadziałem. Na pierwszy rzut oka niejasnych, ale bardzo łatwych do rozwiązania.

### „Pakiet nie ma kandydata do instalacji”

Po angielsku *Package X&nbsp;has no release candidates*. To taki błąd:

{:.figure .bigspace}
<img src="/assets/tutorials/linux/apt-instalowanie/brak-kandydata-do-instalacji.png" alt="Komunikat w konsoli Zorina, mówiący że pakiet plocate nie ma kandydata do instalacji" />

Komunikat o&nbsp;błędzie wymienia możliwe przyczyny; osobiście zetknąłem się z&nbsp;nim w&nbsp;przypadku, gdy APT miał nieaktualne listy. Łatwo się z&nbsp;tym zetknąć, gdy eksperymentuje się ze świeżym systemem z&nbsp;pendrive'a.

Żeby to naprawić, trzeba połączyć się z&nbsp;internetem i&nbsp;wykonać ręcznie [ogólny etap 1](#ogólnie-oinstalowaniu){:.internal}, czyli aktualizację listy dostępnych rzeczy.  
Na przykład taką komendą:

<div class="black-bg mono nospace">sudo apt update</div>

{:.figcaption}
Interfejsy graficzne czasem wykonują to w&nbsp;tle; możliwe, że po połączeniu się z&nbsp;internetem i&nbsp;uruchomieniu programu od pobierania błąd zniknie również w&nbsp;konsoli. Tak przynajmniej jest w&nbsp;przypadku Menedżera Oprogramowania na Mincie.

### „Zatrzymano uszkodzone pakiety”

Po angielsku *You have held broken packages*. Wygląda to tak:

{:.figure .bigspace}
<img src="/assets/tutorials/linux/apt-instalowanie/blad-zatrzymane-pakiety.png" alt="Konsola na Zorinie z&nbsp;komunikatem mówiącym o zatrzymaniu uszkodzonych pakietów"/>

Taki błąd może się pojawić, gdy użyjemy APT-a do zainstalowania pakietu prosto z&nbsp;pliku (`sudo apt install PLIK.deb`), ale nie znajdzie on niezbędnych zależności.

Brzmi groźnie, ale bez obaw, nic się nie uszkodziło! Przyczyną zwykle są nieaktualne listy pakietów. Trzeba się upewnić, że działa połączenie z&nbsp;internetem, po czym zrobić ich aktualizację:

<div class="black-bg mono nospace">sudo apt update</div>

### „Niespełnione zależności”

{:.post-meta .bigspace-after}
Jeśli widać linijkę mówiącą o&nbsp;niespełnionych zależnościach, ale sam błąd zawiera słowa *You have held broken packages* -- to znaczy że mamy nie ten opisywany, tylko [zwykłe nieaktualne listy](#zatrzymano-uszkodzone-pakiety){:.internal}.

Po angielsku *Unmet dependencies*.  
Być może błąd ma różne przyczyny, ale najczęściej pojawiał mi się wtedy, kiedy próbowałem coś zainstalować bezpośrednio przez DPKG, nie mając niezbędnych zależności.

Pierwszą oznaką błędu był komunikat od DPKG:

{:.bigspace}
<img src="/assets/tutorials/linux/apt-instalowanie/niespelnione-zaleznosci-blad.png" alt="Konsola na systemie Zorin. Ostatnia linijka mówi o niespełnionych zależnościach i doradza użycie pewnej komendy"/>

**Ten sam błąd będzie odtąd wyskakiwał podczas _wszelkich_ prób instalacji** (również innych modułów, również przez APT-a i&nbsp;niektóre programy graficzne). Do czasu jego rozwiązania niczego nie zainstalujemy.

Z czego wynika błąd? Ano z&nbsp;tego, że DPKG nie umie pobierać zależności. Nie mając ich pod ręką, szykuje do instalacji tylko nadrzędny pakiet, zauważa braki, po czym ogłasza kapitulację i&nbsp;oznacza cały stan jako wadliwy. A&nbsp;inne programy reagują na to alergicznie.

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/zaleznosci-schemat-instalacja-niepelna.png" alt="Zmiana piramidki zależności po instalacji pakietów pobranych przez apt-get. Zdobyty został tylko pakiet na wierzchołku, reszta nadal jest zaciemniona."/>

{:.figcaption}
To dlatego nazywam cały błąd „błędem wiszącego wierzchołka”.

Genezę błędu oraz inne potencjalne sposoby jego rozwiązania na Mincie opisałem [w&nbsp;osobnym wpisie](/tutorials/linux-blad-package-system-is-broken){:.internal}, tu będzie krótko.

Szybkim rozwiązaniem powinno być użycie komendy sugerowanej przez konsolę (ale z&nbsp;uprawnieniami admina; bez nich wyskoczyłby [błąd pliku blokady](#nie-udało-się-otworzyć-pliku-blokady){:.internal}):

```
sudo apt --fix-broken install
```

### Brak pliku Release (na Mincie z&nbsp;pendrive'a)

Jeśli uruchomi się Minta z&nbsp;pendrive'a (po instalacji na dysku ponoć błąd znika), to podczas rutynowej aktualizacji ([ogólny etap 1](#instalacja-ma-kilka-etap%C3%B3w){:.internal}) mogą się pojawiać komunikaty ze słowem *cdrom*, mówiące o&nbsp;braku jakiegoś pliku *Release*:

{:.fgure .bigspace-before}
<img src="/assets/tutorials/linux-mint-jezyk-polski/linux-mint-lang-install-cdrom-error.png" alt="Zrzut ekranu pokazujący informację o&nbsp;błędzie podczas pobierania informacji o&nbsp;repozytoriach"/>

{:.figcaption}
Tu akurat obrazek z&nbsp;wnętrza programu od instalowania pakietów językowych; mylnie traktuje ten błąd jak brak łączności.

Na chwilę obecną **można je ignorować**, zwykle wszystko działa mimo ich wyświetlenia. Według autorów Minta to drobiazg; [efekt uboczny](https://github.com/linuxmint/mintcommon/issues/77) jakiegoś obejścia, którego używają, żeby instalować sterowniki.

{:.post-meta .bigspace-after}
Nie wykluczam jednak, że może się trafić jakiś szczególnie panikarski program, który po napotkaniu tego błędu przerwie działanie.  
Dlatego w&nbsp;komentarzu spróbowałem łagodnie lobbować za jego usunięciem, zobaczymy czy się uda.

### „Nie udało się otworzyć pliku blokady”

Takie coś pojawia się głównie wtedy, gdy **spróbuje się coś zainstalować bez uprawnień admina**. Bez nich nie można ingerować w&nbsp;pliki systemowe, co prowadzi do niepowodzenia.

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/dpkg-plik-blokady-brak-admina.png" alt="Konsola z&nbsp;komunikatem o&nbsp;błędzie: 'nie udało się otworzyć pliku blokady'."/>

{:.figcaption}
Tu na przykładzie programu `strace`... Który już miałem zainstalowany! Ale błąd zachodzi na samym początku, więc APT nawet tego nie sprawdził.  
Mieszanie języków typowe dla Zorina świeżo z&nbsp;pendrive'a; po doinstalowaniu pakietu spolszczającego się poprawia.

Rozwiązanie? Jeśli instalujemy przez konsolę, to **użyć tego samego polecenia co poprzednio, ale dopisać na jego początku `sudo` i&nbsp;spację** (np. `sudo apt install X`).

{:.post-meta .bigspace-after}
Jeśli to nie pomoże, to możliwe że ma się system z&nbsp;jakimiś nietypowo ustawionymi uprawnieniami. W&nbsp;każdym razie: to w&nbsp;uprawnieniach proponuję szukać przyczyny.

## Bonus: instalowanie offline

W tym miejscu pokażę, w&nbsp;jaki sposób można **pobrać pliki DEB tylko raz, a&nbsp;potem je sobie zapisać i&nbsp;instalować z&nbsp;nich rzeczy bez łączności z&nbsp;siecią**.

Ta możliwość szczególnie się przydaje, kiedy chce się wiele razy „stawiać świeży system”. Być może szykuje się kompy z&nbsp;Linuksem dla całej firmy/rodziny? Albo może chce się korzystać z&nbsp;Minta w&nbsp;trybie *live* dla większej prywatności?
 
Niezależnie od motywacji, należy wtedy rozbić proces instalacji na dwa odrębne etapy, oddalone od siebie w&nbsp;czasie:

1. pobranie i&nbsp;zapisanie aktualnych pakietów,
2. instalowanie zapisanych pakietów.

{% include info.html
type="Uwaga"
text="Przy korzystaniu z&nbsp;opisanej tu metody **raczej nie uda się przenosić pakietów między systemami**.  
Jeśli pobraliśmy pliki DEB na Zorinie&nbsp;17, to bardzo możliwe, że nie uda się ich zainstalować na Zorinie&nbsp;18 albo jakimś Mincie, bo wystąpią niezgodności.  
Zakładam tutaj, że pobieranie i&nbsp;instalowanie odbywa się na tej samej wersji systemu."
%}

### Etap pierwszy: pobieranie

Interfejsy graficzne, które sprawdzałem, nie dawały możliwości samego pobierania plików bez ich instalacji. Dlatego sięgnąłem do konsoli.

{:.post-meta .bigspace-after}
Gdyby komuś nie przeszkadzało, że coś się zainstaluje, to niżej mam też alternatywny sposób niewymagający konsoli.

W roli komend pobierających proponuję użyć tych linijek:

<div class="black-bg mono">sudo apt update<br/>apt download PAKIET</div>

{:.figcaption}
`PAKIET` to tradycyjnie pełna, wewnętrzna nazwa pakietu DEB.  
Pobieranie bez `sudo`, bo nie wymaga admina (i&nbsp;warto go nie nadużywać).

{% include info.html
type="Uwaga"
text="W tym wypadku **należy się trzymać komendy konsolowej `apt` i&nbsp;jej nie zmieniać**. Nieco niżej, w&nbsp;rozwijanej zakładce, szczegóły dla zainteresowanych."
%}

Po użyciu polecenia w&nbsp;aktywnym folderze pojawi się spakowane archiwum w&nbsp;formacie `.tar.gz`. To taki odpowiednik popularnego pliku ZIP. Zawiera **zarówno pobieraną rzecz, jak i&nbsp;wszystkie jej zależności**.

Można rozpakować to archiwum przez zwykłego menedżera plików, klikając je prawym przyciskiem myszy i&nbsp;wybierając opcję `Wypakuj tutaj`.  
W środku będą różne pliki DEB -- główny oraz zależności. Należy je sobie przenieść w&nbsp;jedno miejsce, choćby na pendrive'a.

{:.post-meta .bigspace-after}
Powinien tam być również plik o&nbsp;nazwie `INSTALL`; można go olać.

W rozwijanych zakładkach informacje dodatkowe -- o&nbsp;konieczności używania programu `apt` oraz bezkonsolowy sposób na zdobycie plików.

{% include details.html summary="Różnice między apt i&nbsp;apt-get (tym razem istotne)" %}

{:.bigspace-before}
W przypadku instalacji oba programy działały tak samo, ale **przy pobieraniu są między nimi istotne różnice** -- każdy z&nbsp;nich ma inne ograniczenia: 

* `apt download` pozwala pobierać jedną komendą najwyżej jeden pakiet DEB, ale za to zdobywa go ze wszystkimi zależnościami;
* `apt-get download` może pobrać więcej, ale nie zdobywa automatycznie zależności wskazanego pliku.

{:.post-meta .bigspace-after}
Krótko: `apt download X Y` nie zadziała; `apt-get download X Y` zadziała, ale pliki mogą być złe.

Niepobieranie zależności sprawia, że przy `apt-get` można wpaść w&nbsp;pułapkę -- pobierze się pliki, zapisze, spróbuje później zainstalować... A&nbsp;tu [„błąd wiszącego wierzchołka”](#niespełnione-zależności){:.internal}, blokujący na pewien czas wszelkie możliwości instalowania. Dlatego proponuję zawsze używać `apt download`.

{:.post-meta .bigspace-after}
Pewnym wyjątkiem może być sytuacja, gdy pobieramy bardzo lekkie pakiety DEB, nieposiadające zależności. Sam proponowałem taką metodę we [wpisie o&nbsp;ustawianiu języka polskiego na Mincie](/tutorials/linux-mint-jezyk-polski-system#instalacja-polskich-pakietów-językowych){:.internal}. Dodałem tam jednak ostrzeżenie mówiące, żeby nie stosować jej w&nbsp;innych przypadkach.

Co zatem zrobić, jeśli mamy do pobrania kilka osobnych pakietów, a&nbsp;nie chcemy używać dla każdego osobnej komendy? Jeśli nie jest ich jakoś wiele, to można to rozpisać w&nbsp;konsoli:

<pre class="black-bg mono nospace">
apt download PAKIET_1 && apt download PAKIET_2 && …
</pre>

{:.post-meta}
Podkreślę: nie trzeba wymieniać zależności, zostaną pobrane automatycznie. Wystarczą nazwy rzeczy nadrzędnych.

{% include details-end.html %}

{% include details.html summary="Sposób bez konsoli – branie ze składzika po instalacji" %}

{:.bigspace-before}
Pliki DEB można zdobyć również poprzez klikaninę; wykorzystując fakt, że po pobraniu przez APT pliki DEB zazwyczaj trafiają do tymczasowego składzika, zwanego po angielsku *cache*.

{% include info.html
type="Dygresja językowa"
text="*Cache* tłumaczy się na polski jako „pamięć podręczna”. Ale to pamięć w&nbsp;sensie ogólnym, bez związku z&nbsp;(drogim) RAM-em.  
Angielskie *cache* odnosi się do każdego przypadku, gdy coś, co może się przydać, jest odkładane na później. Czy to na dysku, czy wewnątrz procesora, czy gdziekolwiek indziej.  
Żeby uniknąć zamieszania, będę to nazywał swojsko -- składzikiem."
%}

Wspomniany składzik znajdziemy w&nbsp;folderze `/var/cache/apt/archives`. W&nbsp;środku znajdują się dwie rzeczy -- folder *partial* i plik *lock* -- których nie należy ruszać.  
Całą resztę, czyli pliki DEB odpowiadające zainstalowanym rzeczom, można sobie skopiować.

{:.bigspace-before}
<img src="/assets/tutorials/linux/apt-instalowanie/apt-cache-bez-plikow-partal-lock.png" alt="Wnętrze menedżera plików. Dwa pliki DEB są zaznaczone, zaś partial i lock nie są."/>

{% include info.html
type="Uwaga"
text="Jeśli komuś w&nbsp;tym miejscu nie gromadzą się pliki, to możliwe, że ma inaczej skonfigurowanego APT-a i&nbsp;trzeba coś zmienić w&nbsp;ustawieniach. Albo że interfejs graficzny wychodzi przed szereg i&nbsp;każe czyścić te pliki.  
Ale na świeżym, domyślnym Mincie i&nbsp;Zorinie, po użyciu `sudo apt install`, działa to zgodnie z&nbsp;opisem."
%}

Zaleta tej metody? Nie trzeba się bawić w&nbsp;rozpakowywanie żadnych plików `.tar.gz`; można po prostu skopiować wszystkie pliki DEB na jakiegoś pendrive'a i&nbsp;nosić je ze sobą.

Warto jedynie pamiętać, że wewnątrz skrytki wszystkie pliki są wymieszane, nierozdzielone według modułów.  
Pozostaje rozdzielać je ręcznie, np. według daty modyfikacji. Albo czyścić składzik między instalacjami:

<div class="black-bg mono nospace">sudo apt clean</div>

{% include details-end.html %}

### Etap drugi: instalacja

Po zapisaniu plików DEB przychodzi w&nbsp;końcu moment, gdy chce się je zainstalować. Być może podczas kolejnej sesji w&nbsp;trybie *live*, być może na świeżo postawionym Linuksie jakiegoś członka rodziny.

Wspominałem wcześniej, że programy graficzne słabo sobie radzą z&nbsp;tym zadaniem, dlatego zdam się na konsolkę.  
Należy odwiedzić folder, w&nbsp;którym znajdują się wszystkie zdobyte pliki DEB, a&nbsp;potem użyć komendy:

```
sudo dpkg -i *.deb
```

Bierze ona *wszystkie* pliki z&nbsp;aktywnego folderu kończące się na `.deb` i&nbsp;instaluje je na komputerze. Jeśli są między nimi zależności, to pakiety zostaną zainstalowane w&nbsp;odpowiedniej kolejności.

{:.post-meta .bigspace-after}
Jeśli natomiast brakowało jakichś zależności, to na tym etapie `dpkg` może się przytkać i&nbsp;wyświetlić [błąd niespełnionych zależności](#niespełnione-zależności){:.internal}. Ale jeśli w&nbsp;poprzednim kroku pobraliśmy pliki przez `sudo apt download`, jak sugerowałem, to wszystko powinno być OK.

...I to tyle, przekazałem co wiedziałem :smile:  
Mam nadzieję, że choć parę osób uniknie dzięki tym wskazówkom problemów na tle instalacyjnym i&nbsp;będzie mogło się cieszyć swoimi Linuksami.

