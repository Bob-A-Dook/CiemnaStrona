---
layout: page
title: Wejście w świat Linuksów z programem Ventoy
description: "Choć kończy się na „toy”, jest czymś więcej niż zabawką"
---

Otwarte, darmowe systemy operacyjne oparte na Linuksie od zawsze były jakąśtam alternatywą dla Windowsa, dominującego na komputerach osobistych. Ale dawniej nadawały się niemal wyłącznie dla wąskiego grona: osób ze smykałką, lubiących majsterkować i&nbsp;znających się na komputerach.

Przez ostatnie kilka(-naście) lat hulał jednak wiatr zmian. Rzeczy, które wcześniej nie działały, śmigają czasem nie gorzej niż na Windowsie. Przykładowo:

* firma Valve zainwestowała w&nbsp;kompatybilność, dzięki czemu granie na Linuksie, również w&nbsp;nowe gry, stało się całkiem realne;
* ludzie odpowiedzialni za trzewia systemu dopracowali sterowniki i&nbsp;podsystemy, sprawiając że wiele sprzętów działa z&nbsp;marszu;
* liczne warianty Linuksa postawiły na komfort użytkowania, dzięki czemu do obsługi systemu wystarczy klikanie myszką, a&nbsp;straszliwa tekstowa konsola stała się opcjonalna.

Również w&nbsp;kwestii instalowania nadeszła wielka zmiana na lepsze.  
Koniec z&nbsp;tworzeniem osobnego nośnika na każdego Linuksa -- czasem z&nbsp;użyciem niejasnych instrukcji. Od teraz **można naszykować jednego pendrive'a, a&nbsp;potem do woli zgrywać na niego Linuksy, jakby były fotkami z&nbsp;ferii**. Niesamowicie ułatwia to wejście w&nbsp;świat otwartych systemów, ich porównywanie i&nbsp;odkrycie tego, który najlepiej nam podpasuje.

Wszystko to umożliwia program **Ventoy**, który mam przyjemność przedstawić w&nbsp;tym poradniku.

Zapraszam do lektury!

{% include info.html
type="Nim zaczniemy"
text="Przewodnik kieruję do osób, które mają najzwyklejszy konsumencki komputer ze sklepu, **w domyśle z&nbsp;zainstalowanym Windowsem 10**.  
Nie kieruję go natomiast do tych, którzy mają komputer wydany przez firmę, z&nbsp;szyfrowanym dyskiem, przypisany do floty... Ogólnie -- korpokompa.  
Takie urządzenia często są celowo zamknięte na modyfikacje, uruchamianie na nich innego systemu byłoby trudne, a&nbsp;porady by się nie sprawdziły. Czujcie się ostrzeżeni.  
Moją grupą docelową nie są też ludzie z&nbsp;komputerami od Apple. Mogę im natomiast polecić do rozważenia system [Asahi Linux](https://asahilinux.org/)."
%}

## Spis treści

* [Na wstępie -- o kontrowersjach](#na-wstępie--okontrowersjach)
* [„Instalacja” Ventoya](#instalacja-ventoya)  
* [Stworzenie pendrive'a instalacyjnego](#stworzenie-pendrivea-instalacyjnego)
  * [Wybór pendrive'a](#wybór-pendrivea)
  * [Stworzenie pen-Ventoya](#stworzenie-pen-ventoya)
  * [Dodawanie i&nbsp;usuwanie Linuksów](#dodawanie-iusuwanie-linuksów)
* [Korzystanie z&nbsp;pen-Ventoya](#korzystanie-zpen-ventoya)
  * [Wyświetlenie menu uruchamiania](#wyświetlenie-menu-uruchamiania)
  * [Załadowanie ekranu Ventoya](#załadowanie-ekranu-ventoya)
  * [Załadowanie wybranego Linuksa](#załadowanie-wybranego-linuksa)

## Na wstępie -- o&nbsp;kontrowersjach

Ventoya lubię, ale jeszcze bardziej lubię osoby czytające moją stronę. Nie chciałbym, żeby coś sobie zrobiły z&nbsp;komputerem.

Dlatego w&nbsp;ramach przejrzystości przyznam na starcie -- **wokół Ventoya było/jest parę kontrowersji**. Niektórzy obawiają się, że mógłby posłużyć do ataku hakerskiego na dużą skalę. Szczegóły opisałem w&nbsp;[osobnym miniwpisie](/miniposts/ventoy-kontrowersje){:.internal}.

Osobiście uważam, że niektóre zarzuty są wyolbrzymione. Poza tym minął ponad rok od nagłośnienia sprawy, świat cyberbezpieczeństwa miał czas na analizę i&nbsp;ustawienie skanerów kodu. Atak w&nbsp;takich warunkach zwyczajnie nie wydaje mi się praktyczny.

Ze swojej strony, w&nbsp;ramach ostrożności, będę tu promował pobranie programu nie ze strony linkowanej przez autora, lecz z&nbsp;platformy Github, gdzie trzyma kod źródłowy.  
Gdyby ktoś zgłosił złośliwy kod, to Github zapewne zablokowałby stronę. Tak, jak to [zrobił](https://news.ycombinator.com/item?id=39871749) w&nbsp;przypadku dawnej aferki XZ.

Jeśli ktoś chce dodatkową gwarancję, to może przed wczytaniem się w&nbsp;samouczek wyszukać słowo `ventoy` na forach typu Reddit czy HN (po angielsku). Ewentualne afery na pewno by tam wyskoczyły. Służę gotowymi linkami:

* [`ventoy` na forum HN (od najnowszych)](https://hn.algolia.com/?dateRange=all&page=0&prefix=false&query=ventoy&sort=byDate&type=story),
* [`ventoy` na Reddicie (od najnowszych)](https://www.reddit.com/search/?q=ventoy&type=posts&sort=new).

Jeśli ktoś nadal czuje obawy, to niestety nie pomogę. Niech poszuka czegoś innego niż Ventoy. A&nbsp;wszystkich innych -- zapraszam do dalszej części :smile:

## „Instalacja” Ventoya

{:.post-meta .bigspace-after}
Cudzysłów stąd, że tak naprawdę wystarczy go pobrać i&nbsp;wypakować z&nbsp;pliku ZIP.

Na początek należy odwiedzić [stronę projektu na Githubie](https://github.com/ventoy/Ventoy).  
Tam należy wychwycić wzrokiem nagłówek *Releases* (na większym ekranie: będzie w&nbsp;kolumnie po prawej). Pod nim znajduje się link do najnowszej, opublikowanej wersji Ventoya:

{:.bigspace-before}
<img src="/assets/tutorials/ventoy/ventoy-github.png" alt="Fragment strony Ventoya na Githubie, pokazujący statystyki projektu, a&nbsp;pod spodem link do najnowszej wersji." />

{:.figcaption}
Ponad 70&nbsp;tysięcy gwiazdek, nieźle :+1: Mimo paru obaw społeczność ceni Ventoya.

Tak jak wspomniałem, samouczek dopasowuję do Windowsa, bo celuję w&nbsp;osoby chcące uciec z&nbsp;jego szponów :wink: Osoby z&nbsp;tym systemem powinny kliknąć plik zawierający w&nbsp;nazwie `windows`, po czym go sobie pobrać:

{:.figure .bigspace}
<img src="/assets/tutorials/ventoy/ventoy-installer-windows.png" alt="Zrzut ekranu pokazujący listę dostępnych plików z&nbsp;wizytówki Ventoya na Githubie. Wyróżniony jest plik dla systemu Windows." />

Po pobraniu należy uruchomić klasycznego Eksploratora (przeglądarkę plików), znaleźć plik ZIP i&nbsp;ewentualnie przełożyć go do jakiegoś osobnego folderu. Ale takiego, żeby potem łatwo było go znaleźć, bo jeszcze tam wrócimy.

Następnie trzeba raz kliknąć ZIP-a *lewym* przyciskiem myszy, żeby się zaznaczył. Potem klikamy *prawym* przyciskiem -- dzięki temu, że plik był zaznaczony, w&nbsp;rozwijanym menu pojawi się opcja `Wyodrębnij wszystkie` (po angielsku zapewne *Extract all*). Wybieramy ją. W&nbsp;kolejnym oknie to potwierdzamy, klikając przycisk `Wyodrębnij`. I&nbsp;czekamy, aż się rozpakuje.

{:.bigspace}
<img src="/assets/tutorials/ventoy/ventoy-instalacja.png" alt="Zrzut ekranu pokazujący zaznaczony plik ZIP z&nbsp;Ventoyem. Na wierzchu widać otwarte menu kontekstowe z&nbsp;zaznaczoną opcją 'Wyodrębnij wszystkie'." />

...I już. Wewnątrz wypakowanego folderu znajduje się program Ventoy, gotów do działania. Teraz czas zdobyć pozostałe składniki -- pustego pendrive'a oraz Linuksy.

## Stworzenie pendrive'a instalacyjnego

### Wybór pendrive'a

Przed skorzystaniem z&nbsp;Ventoya należy naszykować *pustego* pendrive'a. To ważne, bo **stworzenie pendrive'a instalacyjnego wiąże się z&nbsp;jego pełnym wyczyszczeniem**. Wszystkie zapisane na nim pliki znikną bezpowrotnie.

Poza brakiem plików znaczenie ma również objętość pendrive'a. Przeciętny plik ISO z&nbsp;Linuksem („instalator”) zajmuje od 3&nbsp;do 6&nbsp;gigabajtów (GB). Wiedząc to, można obliczyć, jak dużego pendrive'a nam potrzeba.

Jeśli ktoś chce tylko jednego, konkretnego Linuksa, to może wystarczyć 8&nbsp;GB. Ale proponuję nieco pojemniejszy nośnik, 16&nbsp;albo 32&nbsp;GB. Tak na przyszłość, żeby móc dorzucić coś jeszcze, gdyby naszła ochota.

Szybkość transferu danych? Teoretycznie coś zmienia (bo Linux świeżo po załadowaniu z&nbsp;pendrive'a czasem coś jeszcze z&nbsp;niego „dociąga”). Ale wydaje mi się drugorzędna. Podobnie inne bajery podbijające cenę. Tu naprawdę wystarczy tanioszka.

{:.post-meta .bigspace-after}
Zresztą gdyby komuś przeszkadzało doładowywanie rzeczy z&nbsp;pendrive'a, to istnieje też fajna opcja przerzucenia całego systemu [do pamięci RAM](/tutorials/live-squashfs-problem#rozwiązanie-właściwe--opcja-toram){:.internal}. Przynajmniej na Mincie.

Osobiście spróbowałem pendrive'ów ISY z&nbsp;jakiegoś MediaMarkta. Półka cenowa 20-30 zł, pojemność 16-32 GB. Działają, sprawdzone. Więcej mi nie trzeba. Ale to nie reklama :wink:

### Stworzenie pen-Ventoya

{:.post-meta .bigspace-after}
Żeby odróżnić pendrive'a bazowego od tego instalacyjnego, którego uzyskamy, będę umownie nazywał tego drugiego *pen-Ventoyem*.

Ventoy na dysku, pusty pendrive naszykowany? To można je połączyć w&nbsp;pen-Ventoya. To zadanie, które wystarczy wykonać tylko raz i&nbsp;które składa się z&nbsp;paru prostych kroków.

Pustego pendrive'a należy wpiąć do portu USB. Dla pewności można wypiąć wszystkie inne. Żeby nie było ryzyka, że przypadkiem usuniemy sobie dane nie z&nbsp;tego, co chcieliśmy.

Wracamy do folderu Ventoya, który sobie wcześniej wypakowaliśmy z&nbsp;ZIP-a. Wyświetlamy jego zawartość, a&nbsp;następnie klikamy dwukrotnie program `Ventoy2Disk`.

{:.bigspace}
<img src="/assets/tutorials/ventoy/ventoy-uruchamianie.png" alt="Lista folderów i&nbsp;plików wewnątrz folderu z&nbsp;Ventoyem. Wyróżniony jest plik Ventoy2Disk" />

Uruchomi się proste okno. W&nbsp;górnej części powinno wyświetlić nazwę i&nbsp;pojemność wpiętego pendrive'a. Można zdać się na opcje domyślne i&nbsp;po prostu kliknąć przycisk `Install` na dole.

{:.bigspace-before}
<img src="/assets/tutorials/ventoy/ventoy-menu.png" alt="Zrzut ekranu programu Ventoy" />

{:.post-meta .bigspace-after}
Proponuję na początek zdać się na opcje domyślne i&nbsp;ewentualnie wrócić do nich, gdyby coś nie działało -- zawsze można nadpisać pen-Ventoya nowym, z&nbsp;innymi ustawieniami. Później wracam do tego wątku.

Kiedy naciśniemy przycisk na dole, można chwilę poczekać. W&nbsp;okienku po prawej powinna się wyświetlić wersja Ventoya zgrana na pendrive'a -- taka sama jak w&nbsp;tym po lewej. Pen-Ventoy jest gotów do działania!

{% include info.html
type="Ciekawostka"
text="Windows może rozpoznawać pen-Ventoya jako dwa osobne pendrive'y. A&nbsp;ściślej rzecz biorąc: jednego z&nbsp;dwiema partycjami. Nie ma w&nbsp;tym nic dziwnego. W&nbsp;razie czego partycja nazwana *VTOYEFI* jest do użytku wewnętrznego, a&nbsp;instalatory należy wrzucać do tej, która nazywa się po prostu *Ventoy*."
trailer="<p class='bigspace-before'><img src='/assets/tutorials/ventoy/ventoy-dwie-partycje.png' alt='Zrzut ekranu z&nbsp;eksploratora Windowsa, pokazujący Ventoya jako dwie osobne pamięci USB'/></p>"
%}

### Dodawanie i&nbsp;usuwanie Linuksów

Pendrive instalacyjny bez zawartości jest jak pistolet bez amunicji. Albo jak choinka bez ozdób, jeśli ktoś woli pokojowe skojarzenia.

Żeby skorzystać z&nbsp;jego potencjału, trzeba zdobyć co najmniej jeden instalator Linuksa.  
To temat na osobny poradnik, dlatego na potrzeby tego wpisu opiszę jedynie kroki dla systemu Linux Mint. Można go sobie pobrać i&nbsp;uruchomić w&nbsp;ramach treningu, a&nbsp;potem najwyżej dorzucić własnego ulubieńca.

{% include details.html summary="Zdobywanie instalatorów Linuksa (na przykładzie Minta)" %}

Ventoy wspiera kilka formatów, ale najczęściej spotykałem w&nbsp;praktyce pliki ISO. Również Mint jest dostępny w&nbsp;takiej postaci.

{% include info.html
type="Ciekawostka"
text="Ściśle rzecz biorąc, pliki ISO nazywa się *obrazami płyt* (stąd ich ikonka na takim np. Mincie, widoczna niżej).  
Oczywiście nie muszą być na płytach, mogą trafiać na dowolne nośniki. Ikonka to taki relikt dawnych czasów, gdy wypalano różne rzeczy na płytach CD. Gimby nie znają (zresztą gimbów już nie ma; płyty też znikną)."
trailer="<p class='bigspace-before'><img src='/assets/tutorials/ventoy/linux-iso.png' alt='Zrzut ekranu pokazujący plik ISO z&nbsp;Mintem. Jego ikonka wygląda jak płyta CD' /></p>"
%}

Linki do instalatorów można znaleźć na [oficjalnej stronie Minta](https://www.linuxmint.com/download.php).  
Są tam trzy główne warianty. Osobiście używałem MATE i&nbsp;Cinnamona. Oba lubią się z&nbsp;Ventoyem, oba solidne. Można sobie wybrać dowolny z&nbsp;nich, kliknąć `Download`, wybrać jakiś serwer z&nbsp;listy (są też polskie, jak ICM Uniwersytetu Warszawskiego). Poczekać, aż plik zajmujący 3&nbsp;GB z&nbsp;hakiem się pobierze.

{:.post-meta .bigspace-after}
A jak Mint komuś nie podpasuje, to zawsze można łatwo dorzucić i&nbsp;sprawdzić inne ISO. Od tego jest Ventoy. Uprzedzam jednak, że choć wspiera on wiele popularnych Linuksów, niektóre mogą nie działać. Przykładowo: Qubes OS albo Porteux.

{% include details-end.html %}

Gdy już zdobędzie się pliki z&nbsp;Linuksem, to należy je wrzucić na pen-Ventoya. Mam w&nbsp;tej kwestii dobrą nowinę -- **pendrive instalacyjny działa jak... zwykły pendrive**:

* wpinamy go do komputera;
* wyświetla się albo jako jeden pendrive (*Ventoy*), albo dwa (z&nbsp;których jeden nazywa się *Ventoy*; to jego wybieramy);
* klikamy, żeby otworzyć jego zawartość, jak zwykły folder;
* można tam upuszczać albo wklejać nasze pliki-instalatory.

  Tak jak przy zwykłych plikach -- zobaczymy, że po wrzuceniu przykładowego pliku ISO z&nbsp;systemem Linux Mint, ważącego 3&nbsp;GB, dostępne miejsce na pendrivie zmniejsza się z&nbsp;16 do 13&nbsp;GB. I&nbsp;to wystarczy, żeby ten Linux znalazł się na liście dostępnych podczas uruchamiania kompa.

Na pen-Ventoyu zaczyna brakować miejsca? To można otworzyć jego zawartość, kliknąć któryś z&nbsp;plików ISO i&nbsp;albo go przenieść na dysk, albo po prostu usunąć. Zobaczymy, że miejsce się zwolni.

{:.post-meta .bigspace-after}
Niewykluczone, że dałoby się też używać pen-Ventoya jak zwykłego pendrive'a i&nbsp;między plikami ISO trzymać sobie najzwyklejsze zdjęcia itd. Ale osobiście wolę rozdzielać te funkcje i&nbsp;trzymam na pen-Ventoyu wyłącznie instalatory Linuksa, zaś od innych rzeczy mam inne pendrive'y.

## Korzystanie z&nbsp;pen-Ventoya

Droga od włączenia komputera do wyświetlenia ekranu Ventoya (albo ogólniej: zawartości pendrive'a instalacyjnego) jest moim zdaniem najtrudniejszą częścią całego procesu.

Nie dlatego, że jest tutaj coś obiektywnie trudnego czy technicznego -- ale po prostu **niektóre rzeczy różnią się między komputerami różnych producentów**. Dotąd mogłem prowadzić osoby czytające ten wpis jak po sznurku. Ale od teraz trzeba przyjąć plan&nbsp;A, plan&nbsp;B, a&nbsp;nawet dalsze.

Plan A&nbsp;będzie działaniem przez menu Windowsa. Jeśli nam się poszczęści i&nbsp;trafimy na „złotą ścieżkę” -- to wszystko przebiegnie bez komplikacji oraz w&nbsp;taki sam sposób, niezależnie od producenta naszego komputera.

Ale uprzedzam, że bardziej prawdopodobne jest to, że wyskoczy przeszkoda i&nbsp;trzeba będzie spróbować dalszych planów, znajdując informacje odpowiednie dla urządzenia (na poziomie producenta (Acer, Lenovo itd.), albo i&nbsp;modelu).  
W takim wypadku odeślę do [przewodnika po uruchamianiu](/tutorials/secure-boot-menu-uruchamiania){:.internal}. Na razie jest szczątkowy, ale będę go rozbudowywał.

### Wyświetlenie menu uruchamiania

Tak jak obiecałem: na początek sposób uniwersalny, niezależny od producenta, może u&nbsp;kogoś zadziała.

{% include details.html summary="Plan A – przez ekran logowania Windowsa 10" %}

{:.post-meta .bigspace-after}
Źródło: [strona Tailsa](https://tails.net/doc/first_steps/start/pc/index.en.html). Dziękuję pięknie za sposób, którego nie znałem.

Na początek należy wpiąć instalacyjnego pen-Ventoya do portu USB.

Potem należy uruchomić komputer i&nbsp;poczekać, aż włączy się tradycyjny ekran logowania do Windowsa, proszący o&nbsp;PIN/hasło.

W tym momencie **należy nacisnąć i&nbsp;przytrzymać klawisz `Shift`**. Klikamy ikonkę w&nbsp;dolnym prawym rogu, wybieramy opcję `Uruchom ponownie`, potem potwierdzamy -- nie zdejmując palca z&nbsp;klawisza.

Powinno się wyświetlić menu specjalne. Na komputerach nieco nowszych zawiera opcję uruchomienia przez inne urządzenie. Wybieramy ją.

{:.post-meta .bigspace-after}
Jeśli opcja konsekwentnie się nie pojawia -- to pozostaje plan&nbsp;B, opisany nieco niżej. Ale hej, powinien potrwać niewiele dłużej.

Wśród opcji dostępnych w&nbsp;kolejnym menu powinno być coś z&nbsp;`USB` w&nbsp;nazwie. Można to wybrać i&nbsp;poczekać, co się stanie.  
W idealnym scenariuszu pojawi się ekran Ventoya. Jeśli zamiast tego znów wróci ekran Windowsa -- to niestety sposób uniwersalny nie zadziałał i&nbsp;trzeba przejść do planu&nbsp;B.

{:.post-meta}
A gdyby wyświetliło komunikat o&nbsp;naruszeniu bezpieczeństwa -- to problemem jest *secure boot*. Opis kilka akapitów niżej.

{% include details-end.html %}

<a id="plan-b"/>

Nie działa? To jest jeszcze szansa, że mamy komputer, na którym różne specjalne menu startowe są łatwo dostępne i&nbsp;odkrywalne.

{% include details.html summary="Plan B – nadzieja na widoczne menu producenta" %}

Można spróbować uruchomić ponownie komputer i&nbsp;spojrzeć, czy wyświetla jakąś wskazówkę podczas pierwszych sekund od uruchomienia. Coś w&nbsp;stylu: „naciśnij `Esc`, żeby wyświetlić menu”.

Jeśli tak, to można się do niej zastosować, włączyć menu i&nbsp;pochodzić po nim. Różni się między komputerami, ale ogólnie chodzi o&nbsp;to, żeby znaleźć wzrokiem coś w&nbsp;stylu *boot menu* (po polsku „menu rozruchu”, ew. „uruchamiania”).

Jeśli coś takiego znajdziemy, to należy to wybrać. I&nbsp;liczyć na to, że wyświetli się teraz lista możliwych urządzeń, zawierająca coś z&nbsp;USB w&nbsp;nazwie.

{:.post-meta}
Gdyby lista się pojawiła, ale bez pen-Ventoya, to można podłubać w&nbsp;jego ustawieniach. Piszę o&nbsp;tym parę akapitów niżej.

{% include details-end.html %}

Żaden ze sposobów nie działa? No to trzeba poszukać rozwiązania dopasowanego do modelu swojego komputera. [Zapraszam do przewodnika](/tutorials/secure-boot-menu-uruchamiania#menu-uruchamiania){:.internal}, w&nbsp;którym pokazuję gotowce dla paru modeli, a&nbsp;także ogólniejsze porady. Potem można wrócić do tej części.

A co, jeśli menu systemowe z&nbsp;planu B&nbsp;się uruchamia, ale na liście dostępnych metod uruchomienia nie ma w&nbsp;ogóle pendrive'a z&nbsp;Ventoyem? W&nbsp;takim wypadku można spróbować stworzyć pen-Ventoya z&nbsp;innymi opcjami.

{% include details.html summary="Grzebanie w&nbsp;opcjach Ventoya" %}

{% include info.html
type="Uwaga"
text="Nim przejdziemy do zmiany opcji, gorąco zachęcam do wykluczenia innych możliwych przyczyn.  
Przykład z&nbsp;życia -- na laptopie Lenovo Legion musiałem wcisnąć `F12` podczas włączania, żeby pokazała się ta diabelska lista dostępnych metod. Robiłem tak i&nbsp;się pojawiała, ale nie było tam pen-Ventoya. Próbowałem tworzyć nowe, z&nbsp;innymi opcjami.  
Potem się okazało, że... po prostu naciskałem klawisz za późno. Jeśli go mocno przytrzymałem jeszcze *przed* wciśnięciem przycisku zasilania -- wykrywało co trzeba. Moje gmeranie w&nbsp;opcjach Ventoya było czasem straconym."
%}

Ventoy ma szereg opcji, ale osobiście ingerowałem tylko w&nbsp;dwie:

* wspieranie *secure boota*,
* sposób ładowania (MBR/GPT).

{:.figcaption}
<img src="/assets/tutorials/ventoy/ventoy-opcje.png" alt="Zrzut ekranu pokazujący parę opcji programu Ventoy. Włączone jest wspieranie trybu secure boot, a&nbsp;także ładowanie z&nbsp;partycji MBR." />

Kiedy po nie sięgnąć? Proponuję taką regułkę -- tylko wtedy, jeśli uda nam się dojść do etapu, gdy pokazuje się *menu uruchamiania*, ale w&nbsp;ogóle nie wyświetla się pendrive z&nbsp;Ventoyem. Wówczas można wykonać dwa kroki:

1. Wyłączyć opcję wsparcia dla *secure boota*, stworzyć przez Ventoya nowego pendrive'a, spróbować ponownie.

   {:.post-meta .bigspace-after}
   Robiąc to, tracimy pewną opcję obejścia barykad wbudowaną w&nbsp;Ventoya. Ale osobiście preferuję zamiast niej wyłączenie *secure boota* po stronie komputera. Wątek jeszcze się pojawi w&nbsp;dalszej części samouczka.

2. Jeśli nadal nie wykrywa pen-Ventoya, to zmieniamy MBR na GPT, tworzymy nowego pendrive'a, próbujemy ponownie.

Trzymam kciuki, żeby któraś z&nbsp;metod zadziałała! Bo jeśli nie, to pozostanie chyba szukanie w&nbsp;sieci `<MODEL_KOMPUTERA> <NAZWA_LINUKSA> ventoy`.

{% include details-end.html %}

### Załadowanie ekranu Ventoya

Po wybraniu pen-Ventoya z&nbsp;listy (wyświetlonej łatwo albo po lekkich bojach) można trzymać kciuki za to, że pokaże się ekran Ventoya z&nbsp;listą dostępnych Linuksów. Świadczący o&nbsp;tym, że jesteśmy o&nbsp;krok od celu:

{:.figure .bigspace-before}
<img src="/assets/tutorials/ventoy/ventoy-menu-edit.jpg" alt="Zrzut ekranu pokazujący menu startowe Ventoya z listą kilku różnych systemów możliwych do załadowania." />

{:.figcaption}
Źródło: [losowy filmik z&nbsp;YouTube'a](https://www.youtube.com/watch?v=pHMqcF16CfE).

...Czasem jednak zdarza się, że zamiast niego wyskoczy groźny niebieski ekran informujący o&nbsp;blokadzie ze względów bezpieczeństwa:

{:.figure .bigspace-before}
<img src="/assets/tutorials/ventoy/secure-boot-error.png" alt="Biały tekst po angielsku na jednolitym niebieskim tle, mówiący że weryfikacja się nie powiodła i&nbsp;doszło do naruszenia bezpieczeństwa." />

{:.figcaption}
Tradycyjnie: czasem ekran wygląda inaczej, wyżej tylko jedna z&nbsp;możliwości.  
Na pewnym Lenovo miałem np. komunikat `(...) has been blocked by the current security policy`.

„Naruszenie bezpieczeństwa”? Czyżby ten Ventoy jednak był jakimś wirusem? Można palpitacji serca dostać! Ale nie schodźcie jeszcze na zawał, sprawa jest prozaiczna.

Widocznie mamy pecha mieć system z&nbsp;włączonym tak zwanym [*secure bootem*](/cyfrowy_feudalizm/2024/10/22/trusted-computing-kajdany){:.internal}. Funkcją, która znacznie ogranicza nasze możliwości „dla naszego dobra”. Może i&nbsp;chroniąc przed pewnymi kategoriami wirusów, ale i&nbsp;blokując domyślnie alternatywne systemy.

Obejście bariery powinno być łatwe... ale trzeba w&nbsp;tym celu wejść w&nbsp;odpowiednie menu, które -- niestety -- różni się między modelami komputerów.  
Jeśli mamy szczęście, to komputer sam podpowiada, jak je otworzyć (zob. [fragment wyżej](#plan-b){:.internal}). Jeśli nie, to możliwe drogi do menu opisałem w&nbsp;[osobnym samouczku](/tutorials/secure-boot-menu-uruchamiania#secure-boot){:.internal}. Po rozwiązaniu problemu *secure boota* zapraszam z&nbsp;powrotem w&nbsp;to miejsce.

Jeśli ekran Ventoya się załaduje -- gładko albo po paru bojach -- to znaczy że jesteśmy już naprawdę blisko celu! :smile: Można odetchnąć i&nbsp;poklepać się po plecach.

### Załadowanie wybranego Linuksa

Ekran Ventoya zawiera listę dostępnych na nim Linuksów. Należy wybrać spośród nich ten, który chcemy uruchomić, po czym potwierdzić *Enterem*.

Pojawi się kolejny ekran, pytając o&nbsp;tryb uruchamiania. Domyślnie zaznaczony jest zwykły (`Normal`), można tak zostawić.

Od tego momentu zacznie uruchamiać się wybrany Linux. Wygląd kolejnych ekranów, dostępne opcje, niuanse -- to już zależy od niego. Poniżej kilka anegdot.

* Mint działa sprawnie i&nbsp;wyświetla kolejny, już własny, ekran z&nbsp;opcjami.
* Porteux w&nbsp;ogóle mi się nie uruchomił (bo chyba nie lubi się z&nbsp;Ventoyem).
* Fedora w&nbsp;wersji KDE Plasma działa, ale stawia opór.

  Najpierw wyświetla niebieski ekran z&nbsp;odliczaniem do ponownego uruchomienia komputera. Muszę ręcznie wybrać opcję uruchomienia systemu, żeby uniknąć restartu. Również w&nbsp;kolejnym menu muszę zmienić domyślną opcję.

Po załadowaniu interfejsu jesteśmy już wewnątrz naszego Linuksa, w&nbsp;tak zwanym trybie *live USB*. Możemy zwiedzać jego zakamarki.  
W wielu przypadkach w&nbsp;widocznym miejscu pojawia się opcja zainstalowania -- jeśli się ją wybierze, Linux zagości na stałe na dysku, zastępując nasz dotychczasowy system, i&nbsp;nie będzie trzeba go już ładować przez Ventoya.

{:.post-meta .bigspace-after}
Uwaga! Trwała instalacja prawie zawsze wiąże się z&nbsp;wyczyszczeniem wszystkich plików z&nbsp;dysku. Jeśli się na nią zdecydujemy, należy je wcześniej przenieść w&nbsp;bezpieczne miejsce.

Ale dopóki nie zrobimy takiej instalacji, rola Ventoya się nie kończy. Parę rzeczy nadal tkwi na pendrivie i&nbsp;system będzie je sobie ładował na raty. Dlatego **nie należy wysuwać pendrive'a instalacyjnego podczas trybu _live_, bo wyskoczą [błędy](/tutorials/live-squashfs-problem){:.internal}**.

A kiedy już sobie poznamy jednego Linuksa -- to można pobrać i&nbsp;wrzucić na pen-Ventoya kolejnego; może podpasuje jeszcze bardziej. Od teraz testowanie Linuksów i&nbsp;potencjalne opuszczanie Windowsa jest łatwiejsze niż kiedykolwiek.

Mam nadzieję, że wszyscy z&nbsp;powodzeniem dotarli do tego etapu i&nbsp;właśnie wkręcają się w&nbsp;świat Linuksów. Życzę pozytywnych wrażeń! :smile:
