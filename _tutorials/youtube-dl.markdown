---
layout: page
title: Instalowanie i używanie youtube-dl
description: "Kompletujemy własną biblioteczkę filmową."
---

YouTube trzyma wszystkie treści na swoich serwerach, a&nbsp;my je sobie streamujemy, nieraz wielokrotnie. Tak wygląda typowy, zaplanowany dla nas scenariusz.  
Istnieje jednak wiele sytuacji, kiedy wolelibyśmy mieć ich filmiki u&nbsp;siebie:

* Znaleźliśmy filmik, który bardzo nam się podoba, ale może niedługo zniknąć.

  W&nbsp;przypadku YouTube'a to nagminne. Znikają amatorskie teledyski ze scenami z&nbsp;komercyjnych produkcji. Filmiki o&nbsp;kontrowersyjnych (ale nie foliarskich) tematach. A&nbsp;czasem po prostu losowe rzeczy, kiedy automat okaże się nadgorliwy.

* Nie chcemy być zależni od łączności z&nbsp;internetem.

  Być może wyruszamy w&nbsp;podróż? Dostęp do internetu może być niepewny albo drogi, jeśli korzystamy z&nbsp;danych mobilnych. Dlatego jest nam na rękę, żeby skompletować biblioteczkę przed wyjazdem.

* Nie chcemy karmić Google'a historią tego, ile razy coś oglądaliśmy, kiedy robiliśmy pauzy i&nbsp;tak dalej. Już i&nbsp;tak za dobrze nas zna.
* Chcemy być wierni przysłowiu „Lepszy wróbel w&nbsp;garści...”.

Niezależnie od naszych powodów, **rozwiązaniem jest _youtube-dl_**.  
Bardzo wszechstronny program konsolowy do pobierania materiałów z&nbsp;YouTube'a ([i&nbsp;wielu innych stron](https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md)).

A ponieważ konsola może być dla wielu osób czymś nowym, napisałem ten przyjazny samouczek pokazujący, jak się z tym programikiem obchodzić.

{% include info.html
type="Uwaga"
text="Jeśli na konsolę reagujemy alergicznie i&nbsp;za żadną cenę nie chcemy z&nbsp;niej skorzystać, to istnieją również programy z&nbsp;graficznym interfejsem. Dobrze oceniany jest na przykład [ten od użytkownika *jely2002*](https://github.com/jely2002/youtube-dl-gui).  
Warto jednak pamiętać, że będzie aktualny tylko dopóty, dopóki twórcy się chce. Nie mamy gwarancji, że będzie na bieżąco ze zmianami w „podstawce”."
trailer="<p class='bigspace-before'>
Poza tym <i>youtube-dl</i> nieco przycina szybkość pobierania, do poziomu kilkudziesięciu kB/s. Jeśli chcemy pozbyć się ograniczeń, warto rozważyć <i><a href='https://github.com/yt-dlp/yt-dlp'>yt-dlp</a></i>. Zastrzeżenia jak wyżej: może być do tyłu względem wersji podstawowej.</p>"
%}

## Instalacja

Ogólne instrukcje znajdziecie [na oficjalnej stronie projektu](https://github.com/ytdl-org/youtube-dl).

Ale oprócz tego naszykowałem ten nieco bardziej przyjazny poradnik **dla użytkowników Windowsa**.

{% include info.html
type="Porada"
text="Tutaj opisuję sposób instalacji najbardziej intuicyjny dla zwykłego użytkownika. Wystarczy pobrać plik i&nbsp;umieścić go w&nbsp;odpowiednim miejscu. To dobra i&nbsp;działająca metoda.  
Ale, gdybyście chcieli jeszcze szybciej i&nbsp;łatwiej aktualizować Wasz program, to gorąco polecam instalację przez `pip`, również opisaną na stronie *youtube-dl*."
%}

Najpierw pobieramy z&nbsp;podlinkowanej wyżej strony najbardziej aktualny plik EXE. Link podali blisko początku instrukcji.

Włączamy konsolę *PowerShell*. Możemy to zrobić na kilka sposobów:

* Przez menu start.  
* Z&nbsp;klawiatury.

  Naciskamy jednocześnie klawisz z&nbsp;ikoną Windowsa w&nbsp;lewym dolnym rogu oraz przycisk `X`. Następnie naciskamy `I` (jak *Irena*).

* Przez Eksplorator Plików.

  Możemy przejść do dowolnego folderu i&nbsp;wybrać z&nbsp;górnego paska `Plik`, a&nbsp;następnie `Otwórz program Windows PowerShell`.  

Wpisujemy w&nbsp;konsolę i&nbsp;potwierdzamy *Enterem*:

```
$env:path -split ";"
```

W ten sposób wyświetlą nam się, jeden pod drugim, foldery z&nbsp;kategorii `PATH`.  
To coś w&nbsp;rodzaju przegródek szybkiego dostępu. Kiedy mamy w&nbsp;tych folderach jakieś pliki EXE, to możemy je łatwo uruchamiać, wpisując w&nbsp;PowerShella samą ich nazwę zamiast pełnej ścieżki.

Zatem otwieramy Eksploratora, bierzemy nasz pobrany wyżej plik EXE i&nbsp;przenosimy go do któregoś z&nbsp;folderów z&nbsp;listy (**za wyjątkiem `System32`**! Odradzają to na stronie projektu).

Od teraz, kiedy wpiszemy w&nbsp;PowerShella `youtube-dl`, powinno nam wyświetlać, że działa (ale potrzebuje linka):

{:.figure .bigspace}
<img src="/assets/tutorials/youtube-dl/youtube-dl-ekran.jpg" alt="Okno konsoli z&nbsp;wpisanym tekstem 'youtube-dl'. Pod spodem widać informację, że trzeba podać co najmniej jeden adres uRL."/>

## Korzystanie

Gdy już mamy konsolę i&nbsp;wiemy że działa, możemy pobierać do woli.

Najpierw musimy odwiedzić YouTube'a, żeby zdobyć link do filmu. Jako przykładu użyję **satyrycznej reklamy *GmailMan* sprzed 10 lat**.  
Wykonał ją Microsoft, żeby reklamować swoje usługi, a&nbsp;przy tym dać prztyczka w&nbsp;nos Google'owi i&nbsp;jego zwyczajowi zbierania danych z&nbsp;maili.

Zgadzam się z&nbsp;jej sednem; ale jest w&nbsp;tym pewna ironia losu, patrząc na to, że sami od teraz [wymagają](https://www.theregister.com/2022/02/18/windows_11_insider_msa/) posiadania u&nbsp;siebie konta, żebyśmy mogli w&nbsp;ogóle używać Windowsa.

Wracając do rzeczy! Po wejściu na stronkę kopiujemy link z&nbsp;paska:

{:.figure .bigspace}
<img src="/assets/tutorials/youtube-dl/gmail-man-kopiowanie-linka.jpg" alt="Zrzut ekranu z&nbsp;YouTube'a. Widoczna stopklatka z&nbsp;filmiku pokazuje uśmiechniętego mężczyznę trzymającego koperty w&nbsp;kształcie ikony Gmaila. Adres strony z&nbsp;górnego paska wyróżniono czerwoną ramką, a&nbsp;pod spodem dodano napis 'Control plus C'." />

Następnie w&nbsp;konsoli wystarczy wpisać `youtube-dl`, potem spację, a&nbsp;potem wkleić link do filmu. Zostanie pobrany do tego samego folderu, w&nbsp;którym odpaliliśmy PowerShella, w&nbsp;najlepszej dostępnej jakości.

```
youtube-dl https://www.youtube.com/watch?v=9x4_dozWkq0
```

Czasem jednak nie potrzebujemy najbardziej odpicowanej wersji. W&nbsp;tej sytuacji możemy sobie wyświetlić listę dostępnych formatów, dopisując `-F`:

```
youtube-dl -F https://www.youtube.com/watch?v=9x4_dozWkq0
```

Pokaże nam się coś w&nbsp;tym stylu:

{:.figure .bigspace}
<img src="/assets/tutorials/youtube-dl/youtube-dl-formaty.jpg" alt="Lista formatów wyświetlonych jeden pod drugim" />

Po lewej stronie mamy liczby odpowiadające poszczególnym formatom, a&nbsp;po prawej stronie ich opisy. Żeby pobrać któryś z&nbsp;nich, wpisujemy `-f`, a&nbsp;potem liczbę odpowiadającą danej wersji. Czyli na przykład:

```
youtube-dl -f 242 https://www.youtube.com/watch?v=9x4_dozWkq0
```

**Uwaga:** Zwracajmy uwagę na opisy plików. Czasem, szczególnie w&nbsp;górnej części listy, mamy pliki będące samym dźwiękiem albo obrazem (*audio only* i&nbsp;*video only*). Gotowe kombinacje znajdziemy na końcu listy.

Oprócz liczb mamy też parę gotowych komend. Chcemy sam dźwięk (przydatne przy piosenkach)? Żaden problem, nie trzeba nawet wyświetlać listy formatów! Wpisujemy `-f bestaudio`.

```
youtube-dl -f bestaudio https://www.youtube.com/watch?v=9x4_dozWkq0
```

A jeśli chcemy jakieś nietypowe połączenie? Na przykład najniższą jakość obrazu i&nbsp;najwyższą dźwięku? Wpisujemy `-f`, liczbę odpowiadającą plikowi wideo, plusa i&nbsp;liczbę odpowiadającą plikowi audio (kolejność ważna!).

Patrzę na listę szczegółów i&nbsp;widzę, że najmniejszy obraz ma rozdzielczość *256x144*, odpowiada mu liczba 278. A&nbsp;pliku audio nie wypatruję, tylko wpisuję gotowca:

```
youtube-dl -f 278+bestaudio https://www.youtube.com/watch?v=9x4_dozWkq0
```

To tylko ułamek możliwości tego programiku. Pozwala m.in. na pobieranie całych playlist. Ale z&nbsp;tej funkcji akurat nie miałem potrzeby korzystać, więc na jej temat się nie wypowiem.

{% include info.html
type="Porada"
text="Program *youtube-dl* zapisuje pobierane filmiki do aktywnego folderu. Dlatego, jeśli chcemy je na przykład zapisać do folderu *Wideo*, to musimy właśnie tam otworzyć naszą konsolę.  
W przypadku Windowsa wystarczy włączyć Eksploratora, przejść do tego folderu, a&nbsp;potem uruchomić tam PowerShella przez menu `Plik` z&nbsp;górnego paska.  
„Hakierzy” mogą też poruszać się po folderach, korzystając z&nbsp;komendy konsolowej `cd`."
%}

## Rozwiązywanie błędów

Nasz programik musi niestety stale gonić YouTube'a oraz jego wewnętrzne mechanizmy, które nieraz się zmieniają. Nie unikniemy przez to sytuacji, kiedy raz na jakiś czas wyskoczy nam błąd.

Ale bez obaw! Zwykle jest więcej osób mających taki problem jak my, a naprawienie nieraz sprowadza się do pobrania nowszej wersji. A potem na długi czas mamy spokój.

Ogólna zasada -- jeśli w konsoli wyświetlił nam się tekst, to patrzymy co mamy na dole, po słowie `ERROR:`. Treść takiego komunikatu można wkleić w wyszukiwarkę, żeby poszukać rozwiązania.

A parę powszechnych przypadków omówię dla naszej wygody w tym miejscu.

### Zawieszenie programu

Jeśli zerwie nam połączenie, to *youtube-dl* może się zawiesić. Licznik stoi w&nbsp;miejscu, niczego nie pobiera.

W takiej sytuacji otwieramy okno naszej konsoli i:

* najpierw naciskamy `Ctrl`+`C`, żeby przerwać aktualną komendę;
* następnie strzałkę do góry, żeby ponownie wyświetliła się poprzednia komenda (`youtube-dl...`);
* potwierdzamy, wciskając `Enter`.

I *voila*! Jeśli już mamy łączność, to zacznie nam pobierać od miejsca, w&nbsp;którym poprzednio się zatrzymało.

### Odmowa dostępu

Wyświetla się jako `HTTP Error 403: Forbidden`.

Czasami to chwilowy zgrzyt i&nbsp;wystarczy spróbować ponownie. Strzałka w&nbsp;górę, żeby ponownie wyświetlić komendę. *Enter*, żeby ją wykonać. Zazwyczaj mi wtedy działa.

Innym razem sam filmik ma jakieś ograniczenia. Na przykład te wprowadzone przez Google, żeby wyciągnąć od nas zdjęcie dowodu albo numer konta. Zwykle omijam je szerokim łukiem, więc chwilowo nie wiem, czy jest jakieś proste obejście.

### Film niedostępny/usunięty

W takim przypadku *youtube-dl* wyświetli `Video unavailable`.  
Oznacza to zapewne, że film został usunięty między momentem wejścia na jego stronę a momentem skopiowania linka do konsoli.  
Może usunął go autor, może YouTube'owa automatyczna moderacja.

Wyjątkowy pech. Zdarzyło mi się to dosłownie raz, niedawno.

A Wasz film? Jeśli macie nadal otwartą stronę YouTube'a, to zapewne jesteście w stanie go nadal oglądać (serwis jeszcze będzie przez chwilę podtrzymywał połączenie, zanim usunie sam plik). Być może możecie go nawet odzyskać z pamięci podręcznej.

W każdym razie w takiej sytuacji gra się toczy o wysoką stawkę -- **gdy zamkniecie okno YouTube'a z tym filmem, to możecie już go nie zobaczyć**. Jeśli jest fajny, a nie wiecie jak wyłuskać z pamięci podręcznej, to może warto nawet odpalić jakieś *OBS Studio* i nagrać ekran wraz z dźwiękiem :wink:

### Inne błędy

Z czasem trafi się jakiś nieoczekiwany błąd. Może wynikać z&nbsp;tego, że **co jakiś czas YouTube wprowadza większe zmiany za kulisami, przez co psuje _youtube-dl_**.

Ale jego autorzy zwykle szybko nadganiają. Wtedy po prostu bierzemy od nich najnowszą wersję i&nbsp;zastępujemy nią poprzednią.

To równocześnie jeden z&nbsp;argumentów przemawiających za tym, żeby korzystać z wersji konsolowej, a nie graficznej. Łatwiej być na bieżąco.

Wszelkie nakładki graficzne może i&nbsp;są przyjaźniejsze, ale nadal zależą od podstawowego *youtube-dl*. Gdy Google coś popsuje, to najpierw źródło musi naprawić to u siebie, a&nbsp;potem autorzy wersji graficznej (którzy mogą np. być akurat na wakacjach) po swojej stronie.

### „Unable to extract uploader_id”

Ten błąd dotyczy wersji `2021.12.17`, czyli najnowszej dostępnej na stronie *youtube-dl*. Być może nie aktualizują wersji przez to, że organizacje branżowe próbowały im robić problemy. Ale kod na szczęście zmieniają na bieżąco.

W tym wypadku zwykła aktualizacja nie działa, bo numer działającej i&nbsp;niedziałającej wersji jest taki sam. Ale rozwiązanie opisali [w&nbsp;dyskusji na Githubie](https://github.com/ytdl-org/youtube-dl/issues/31904).

Ogólnie: trzeba zdobyć wersję najnowszą i&nbsp;siłowo zastąpić nią wersję poprzednią.

**Dla Windowsa**

Nie mam na razie możliwości tego przetestować, ale możemy spróbować pobrać najnowszy plik *exe* (w&nbsp;sposób opisany na początku) i&nbsp;zastąpić nim nasz stary.  
Tak, mają dokładnie ten sam numer wersji. Ale jest szansa, że nowszy plik jest aktualniejszy i&nbsp;będzie działał.

**Dla systemu Linux**

Osobiście instalowałem `youtube-dl` przez Pythona, zatem wpisuję komendę:

<div class="black-bg mono">
pip install --force-reinstall 'https://github.com/ytdl-org/youtube-dl/archive/refs/heads/master.tar.gz'
</div>

...I śmiga!

Jeśli mamy system, na którym `pip` odpowiada starszemu Pythonowi&nbsp;2, to wpisujemy zamiast niego `pip3`.

Jeśli instalowaliśmy dla całego systemu, to przed komendą trzeba jeszcze dopisać `sudo` i&nbsp;spację, a&nbsp;potem podać hasło.

{:.post-meta}
Niektórzy ogólnie [przestrzegają](https://stackoverflow.com/questions/21055859/what-are-the-risks-of-running-sudo-pip) przed takim trybem instalowania, zwłaszcza gdy nie do końca ufamy instalowanym programom.

