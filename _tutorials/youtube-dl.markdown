---
layout: page
title: Instalowanie i używanie youtube-dl oraz yt-dlp
description: "Kompletujemy własną biblioteczkę filmową."
---

YouTube trzyma wszystkie treści na swoich serwerach, a&nbsp;my je sobie streamujemy, nieraz wielokrotnie. Nigdy nie trafiają do nas na stałe.

Tak wygląda typowy, zaplanowany dla nas scenariusz.  
Istnieje jednak wiele sytuacji, kiedy wolelibyśmy mieć ich filmiki u&nbsp;siebie:

* Znaleźliśmy filmik, który bardzo nam się podoba, ale może niedługo zniknąć.

  W&nbsp;przypadku YouTube'a to nagminne. Znikają amatorskie teledyski ze scenami z&nbsp;komercyjnych produkcji. Filmiki o&nbsp;kontrowersyjnych (ale nie foliarskich) tematach. A&nbsp;czasem po prostu losowe rzeczy, kiedy automat okaże się nadgorliwy.

* Nie chcemy być zależni od łączności z&nbsp;internetem.

  Być może wyruszamy w&nbsp;podróż? Dostęp do internetu może być niepewny albo drogi, jeśli korzystamy z&nbsp;danych mobilnych. Dlatego jest nam na rękę, żeby skompletować biblioteczkę przed wyjazdem.

* Nie chcemy karmić Google'a historią tego, ile razy coś oglądaliśmy, kiedy robiliśmy pauzy i&nbsp;tak dalej. Już i&nbsp;tak za dobrze nas zna.
* Chcemy być wierni przysłowiu „Lepszy wróbel w&nbsp;garści...”.

Niezależnie od naszych powodów, **rozwiązaniem jest _youtube-dl_ albo jego alternatywa, _yt-dlp_**.  
Bardzo wszechstronny program konsolowy, którym da się pobierać filmiki z&nbsp;YouTube'a ([i&nbsp;wielu innych stron](https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md)).

A ponieważ konsola może być dla wielu osób czymś nowym, napisałem ten przyjazny samouczek pokazujący, jak się z tym programikiem obchodzić.

{% include info.html
type="Aktualizacja 2023"
text="Niedawno kontrowersyjny wyrok niemieckiego sądu doprowadził do [ukarania stronki hostującej YtDl](https://torrentfreak.com/youtube-dl-hosting-ban-paves-the-way-to-privatized-censorship-230411/).  
Walczyli o to producenci: Sony Entertainment, Warner Music Group oraz Universal Music. Wcześniej próbowali również strącić kod źródłowy programu, ale im się nie udało.  
Od tego czasu coraz częściej [poleca się zamiennik](https://news.ycombinator.com/item?id=37270747). Nosi nazwę `yt-dlp`, obsługuje się go tak samo jak poprzednika. Dopasowałem do niego część instrukcji z tego samouczka.  
Poza tym stworzyłem osobny samouczek dotyczący *[instalacji na smartfonie](/tutorials/yt-dlp-android)*{:.internal} z systemem Android (w apce Termux)."
%}

{% include info.html
type="Uwaga"
text="Jeśli na konsolę reagujemy alergicznie i&nbsp;za żadną cenę nie chcemy z&nbsp;niej skorzystać, to istnieją również programy z&nbsp;graficznym interfejsem. Dobrze oceniany jest na przykład [ten od użytkownika *jely2002*](https://github.com/jely2002/youtube-dl-gui).  
Warto jednak pamiętać, że będzie aktualny tylko dopóty, dopóki twórcy się chce. Nie mamy gwarancji, że będzie na bieżąco ze zmianami w&nbsp;podstawowej, konsolowej wersyjce."
%}

## Instalacja na Windowsie

{:.post-meta .bigspace-after}
Gdyby ktoś z&nbsp;jakiegoś powodu wolał się trzymać klasycznego *youtube-dl*, to różnice są bardzo niewielkie. Po prostu pobiera się [program z&nbsp;innego źródła](https://github.com/ytdl-org/youtube-dl). A&nbsp;potem, korzystając z&nbsp;niego w konsoli, wpisuje się *youtube-dl* zamiast *yt-dlp*.

Zaczynajmy!

Najpierw pobieramy plik EXE. Ten dla `yt-dlp` -- nowszej, mniej problematycznej wersji -- znajdziemy [tutaj](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe).

### Ustalanie folderu dla pliku

Gdy już mamy plik na dysku, to warto ustalić, do jakiego specjalnego folderu go wrzucić, żeby dał się przywoływać z dowolnego miejsca. Opcji jest kilka.

* Możemy spróbować do `C:\Windows`. Zwykle jest domyślnie aktywny, przynajmniej na Windowsie&nbsp;10. Tylko trzeba kliknąć, że mamy uprawnienia administratora.

* Można też wyklikać drogę do `C:\Użytkownicy\NAZWA\AppData\Local\Microsoft\WindowsApps`.

  Przy czym `Użytkownicy` będą się nazywali inaczej, jeśli mamy ustawiony inny język systemu. Zamiast `NAZWA` będziemy mieli swój login. A po drodze warto włączyć wyświetlanie ukrytych folderów, żeby ujrzeć `AppData`.

A jeśli chcemy zobaczyć wszystkie możliwości, to warto podejrzeć zmienne systemowe.  
W tym celu włączamy konsolę *PowerShell*. Możemy to zrobić na kilka sposobów:

* Przez menu startowe.  
  Klikamy ikonę Windowsa w&nbsp;dolnym lewym rogu, przewijamy do zakładki `Windows PowerShell`, klikamy.

* Z&nbsp;klawiatury.  
  Naciskamy jednocześnie klawisz z&nbsp;ikoną Windowsa (dolna część klawiatury) oraz przycisk `X`. Następnie naciskamy `I` (jak *Irena*).

* Przez Eksplorator Plików.  
  Możemy przejść do dowolnego folderu i&nbsp;wybrać z&nbsp;górnego paska `Plik`, a&nbsp;następnie `Otwórz program Windows PowerShell`.

Gdy pojawi się konsola, to wpisujemy w&nbsp;nią:

```
$env:path -split ";"
```

Potwierdzamy *Enterem*. Wyświetlą nam się, jeden pod drugim, foldery z&nbsp;kategorii `PATH`.

To coś w&nbsp;rodzaju przegródek szybkiego dostępu. Kiedy mamy w&nbsp;tych folderach jakieś pliki EXE, to możemy je łatwo uruchamiać. Wystarczy wpisać w&nbsp;PowerShella samą ich nazwę zamiast pełnej ścieżki.

Zatem otwieramy Eksploratora, bierzemy nasz pobrany wyżej plik EXE i&nbsp;przenosimy go do któregoś z&nbsp;folderów z&nbsp;listy (**za wyjątkiem `System32`**! Odradzają to na stronie projektu).

Od teraz, kiedy wpiszemy w&nbsp;PowerShella `yt-dlp`, powinno nam wyświetlać, że działa (ale potrzebuje linka):

{:.figure .bigspace}
<img src="/assets/tutorials/youtube-dl/youtube-dl-ekran.jpg" alt="Okno konsoli z&nbsp;wpisanym tekstem 'youtube-dl'. Pod spodem widać informację, że trzeba podać co najmniej jeden adres uRL."/>

### Alternatywna metoda instalacji

Powyższy sposób -- polegający na umieszczeniu pliku w odpowiednim folderze -- jest bardzo intuicyjny. I&nbsp;działa.

Tym niemniej instalacja przez `pip` (moduł Pythona) ma nieco więcej zalet.  
Pozwala szybko i&nbsp;łatwo aktualizować program, gdyby coś przestało działać wskutek zmian YouTube'a. Wystarczy jedna komenda w konsoli zamiast pobierania nowego EXE i&nbsp;zastąpienia nim starego.

Gdybyście byli gotowi spróbować, to polecam [opis na stronie *yt-dlp*](https://github.com/yt-dlp/yt-dlp/wiki/Installation). To dosłownie parę komend konsolowych.

## Instalacja na Linuksie

Dawniej polecałbym instalowanie i aktualizowanie przez PIP, opisane parę linijek wyżej.  
Obecnie jednak sprawy nieco się pogmatwały, bo różne Linuksy zaczęły traktować Pythona systemowego jak osobną wersję, której lepiej nie modyfikować. Po wpisaniu typowej komendy instalującej najnowszą wersję pojawiłby się błąd *Externally managed environment*. Ten problem występuję między innymi na Mincie, czyli Linuksie którego używam.

{:.post-meta .bigspace-after}
Mint to zresztą ciekawy przypadek, bo jako jeden z&nbsp;niewielu systemów zawiera `yt-dlp` w&nbsp;pakiecie, domyślnie zainstalowany na systemie... Tyle że nie ma co się cieszyć, bo to przestarzała wersja, raczej nieprzydatna do pobierania rzeczy z&nbsp;popularnych serwisów, na których stale coś się zmienia.

Jedna z zalecanych propozycji rozwiązania problemu (używanie Pythona przez środowiska wirtualne) wydaje mi się mało komfortowa dla naszego programiku. Jego atutem powinna być łatwa dostępność: widzi się film, kopiuje link do konsoli, zdobywa film.  
Jest też metoda nieco brawurowa i&nbsp;wiążąca się z&nbsp;ryzykiem; opisałem ją [pod koniec wpisu](#externally-managed-environment-przy-próbie-aktualizacji){:.internal}.

W tej części pokażę coś pomiędzy: metodę bezawaryjną, ale nieco okrężną, podobną do tej z&nbsp;Windowsa -- pobranie pliku z&nbsp;oficjalnej strony. Gdyby pojawiła się potrzeba aktualizacji, to trzeba wszystko wykonać od nowa dla nowszej wersji i&nbsp;zastąpić nią starszą.

{% include details.html summary="Instalacja krok po kroku" %}

* Odwiedzamy [listę wydań na stronie projektu](https://github.com/yt-dlp/yt-dlp/releases), wybieramy najnowsze i&nbsp;pobieramy plik o&nbsp;nazwie `yt-dlp_linux`.

  Jest tam parę podobnych, zawierających w nazwie tekst *aarch* oraz *arm*. Jeśli jednak mamy typowego laptopa, to te pozostałe nas nie interesują.

* Włączamy plikowi wykonywalność (uprawnienie do działania jako program) -- wystarczy to zrobić raz.

  Na niektórych Linuksach można kliknąć plik prawym przyciskiem myszy, wybrać `Właściwości`, przejść w zakładkę `Uprawnienia` i&nbsp;tam zaznaczyć opcję `Pozwól na uruchamianie pliku jako programu` albo coś zbliżonego.

  Inna, uniwersalna opcja? Sposób konsolowy. Uruchamiamy terminal w&nbsp;tym samym folderze co plik (np. klikając pustą przestrzeń obok pliku prawym przyciskiem myszy i&nbsp;wybierając `Otwórz w terminalu`).  
  Następnie wpisujemy `chmod +x yt-dlp_linux` (zamiast ręcznie wpisywać nazwę, w&nbsp;przypadku Minta można chwycić plik i&nbsp;upuścić go wewnątrz terminala).

* Uruchamiamy program.

  Tutaj klikanie pliku przez interfejs graficzny może nie działać, więc lepiej otworzyć terminal w&nbsp;tym samym folderze. Od teraz będzie można używać programu zgodnie z&nbsp;przykładami z&nbsp;dalszej części wpisu. Jedyna różnica: we wszystkich poleceniach zamiast `yt-dlp` należy wpisywać na początku `./yt-dlp_linux`.

Osoby chcące wołać program samą jego nazwą, bez konieczności wchodzenia do jego folderu i&nbsp;dopisywania `./` na początku, mogą go skopiować do folderu szybkiego dostępu, jak `/usr/bin`. Polecenie kopiujące:

<pre class="black-bg mono">
sudo cp yt-dlp_linux /usr/bin
</pre>

{:.post-meta}
Zapewne wyświetli się prośba o podanie hasła administratora. Po skopiowaniu pliku wystarczy wpisywać `yt-dlp_linux`, żeby wołać program z dowolnego miejsca.  
Jeśli jesteście na Mincie: pamiętajcie, żeby nie zawołać przez pomyłkę systemowego, przestarzałego `yt-dlp`. Dla pewności można zmienić temu nowszemu nazwę jeszcze przed skopiowaniem.

{% include details-end.html %}

## Instalacja na Androidzie

Gdyby ktoś chciał używać `yt-dlp` również na urządzeniu mobilnym, to mam dobrą wiadomość -- na systemie Android to całkiem możliwe! Żeby nie zajmować tu miejsca, wydzieliłem instrukcje [do osobnego samouczka](/tutorials/yt-dlp-android){:.internal}.

## Zdobywanie linków

Gdy już mamy konsolę i&nbsp;wiemy że działa, możemy pobierać do woli.

{:.post-meta .bigspace-after}
W związku ze wspomnianą na początku sądową nagonką, zmieniłem nieco treść samouczka. Pierwsza część pokazuje teraz ogólną metodę zdobywania linków z YouTube'a. Gdy na przykład chcemy je wysłać znajomym.  
Część druga pokazuje używanie `yt-dlp` w *ogólnym* przypadku. W domyśle: na którejś z wielu stron, które nie mają z tym problemu.  
Obie części są całkowicie ze sobą niezwiązane :smile:

Najpierw musimy odwiedzić YouTube'a, żeby zdobyć link do filmu. Jako przykładu użyję **satyrycznej reklamy *GmailMan* sprzed 10 lat**.  
Wykonał ją Microsoft, żeby reklamować swoje usługi, a&nbsp;przy tym dać prztyczka w&nbsp;nos Google'owi i&nbsp;jego zwyczajowi zbierania danych z&nbsp;maili.

Zgadzam się z&nbsp;jej sednem; ale jest w&nbsp;tym pewna ironia losu, patrząc na to, że sami od teraz [wymagają posiadania u&nbsp;siebie konta](https://www.theregister.com/2022/02/18/windows_11_insider_msa/), żebyśmy mogli w&nbsp;ogóle używać Windowsa.

Wracając do rzeczy! Po wejściu na stronkę klikamy dwukrotnie link z&nbsp;paska i go kopiujemy:

{:.figure .bigspace}
<img src="/assets/tutorials/youtube-dl/gmail-man-kopiowanie-linka.jpg" alt="Zrzut ekranu z&nbsp;YouTube'a. Widoczna stopklatka z&nbsp;filmiku pokazuje uśmiechniętego mężczyznę trzymającego koperty w&nbsp;kształcie ikony Gmaila. Adres strony z&nbsp;górnego paska wyróżniono czerwoną ramką, a&nbsp;pod spodem dodano napis 'Control plus C'." />

Wygląda tak:

{:.bigspace}
```
https://www.youtube.com/watch?v=9x4_dozWkq0
```

Na tym kończy się część dotycząca YouTube'a. Zdobyty link można wysłać znajomym.  
Zaś wszystko poniżej dotyczy bliżej nieokreślonych, lubiących się z programikiem filmów.

## Korzystanie z programu

Aby pobierać filmik, wystarczy wpisać w&nbsp;konsoli `yt-dlp` (w&nbsp;starej wersji `youtube-dl`), potem spację, a&nbsp;potem wkleić link do filmu. Zostanie pobrany do tego samego folderu, w&nbsp;którym odpaliliśmy PowerShella, w&nbsp;najlepszej dostępnej jakości.

```
yt-dlp LINK_DO_FILMU
```

Czasem jednak nie potrzebujemy najbardziej odpicowanej wersji. W&nbsp;tej sytuacji możemy sobie wyświetlić listę dostępnych formatów, dopisując `-F`:

```
yt-dlp -F LINK_DO_FILMU
```

Pokaże nam się coś w&nbsp;tym stylu:

{:.figure .bigspace}
<img src="/assets/tutorials/youtube-dl/youtube-dl-formaty.jpg" alt="Lista formatów wyświetlonych jeden pod drugim" />

Po lewej stronie mamy liczby odpowiadające poszczególnym formatom, a&nbsp;po prawej stronie ich opisy. Żeby pobrać któryś z&nbsp;nich, wpisujemy `-f`, a&nbsp;potem liczbę odpowiadającą danej wersji. Czyli na przykład:

```
yt-dlp -f 242 LINK_DO_FILMU
```

**Uwaga:** Zwracajmy uwagę na opisy plików. Czasem, szczególnie w&nbsp;górnej części listy, mamy pliki będące samym dźwiękiem albo obrazem (*audio only* i&nbsp;*video only*). Gotowe kombinacje obrazu i&nbsp;dźwięku znajdziemy na końcu listy.

Oprócz liczb mamy też parę gotowych komend. Chcemy sam dźwięk (przydatne przy piosenkach)? Żaden problem, nie trzeba nawet wyświetlać listy formatów! Wpisujemy `-f bestaudio`.

```
yt-dlp -f bestaudio LINK_DO_FILMU
```

A jeśli chcemy jakieś nietypowe połączenie? Na przykład najniższą jakość obrazu i&nbsp;najwyższą dźwięku? Wpisujemy `-f`, liczbę odpowiadającą plikowi wideo, plusa i&nbsp;liczbę odpowiadającą plikowi audio (kolejność ważna!).

Patrzę na listę szczegółów i&nbsp;widzę, że najmniejszy obraz ma rozdzielczość *256x144*, odpowiada mu liczba 278. A&nbsp;pliku audio nie wypatruję, tylko wpisuję gotowca:

```
yt-dlp -f 278+bestaudio LINK_DO_FILMU
```

To tylko ułamek możliwości tego programiku. Pozwala też m.in. na pobieranie całych playlist. Ale z&nbsp;tej funkcji akurat nie miałem potrzeby korzystać, więc na jej temat się nie wypowiem.

{% include info.html
type="Porada"
text="Ten program zapisuje pobierane filmiki do aktywnego folderu. Dlatego, jeśli chcemy je na przykład zapisać do folderu *Wideo*, to musimy właśnie tam otworzyć naszą konsolę.  
W przypadku Windowsa wystarczy włączyć Eksploratora, przejść do tego folderu, a&nbsp;potem uruchomić tam PowerShella przez menu `Plik` z&nbsp;górnego paska.  
„Hakierzy” mogą też poruszać się po folderach, korzystając z&nbsp;komendy konsolowej `cd`."
%}

## Rozwiązywanie błędów

Nasz programik musi niestety stale gonić YouTube'a oraz jego wewnętrzne mechanizmy, które nieraz się zmieniają. Nie unikniemy przez to sytuacji, kiedy raz na jakiś czas wyskoczy nam błąd.

Ale bez obaw! Zwykle jest więcej osób mających taki problem jak my, a naprawienie nieraz sprowadza się do pobrania nowszej wersji. A potem na długi czas mamy spokój.

Ogólna zasada -- jeśli w konsoli wyświetlił nam się tekst, to patrzymy co mamy na dole, po słowie `ERROR:`. Treść takiego komunikatu można wkleić w wyszukiwarkę, żeby poszukać rozwiązania.

A parę powszechnych przypadków omówię dla naszej wygody w tym miejscu.

### Zawieszenie programu

Jeśli zerwie nam połączenie, to programik może się zawiesić. Licznik stoi w&nbsp;miejscu, niczego nie pobiera.

W takiej sytuacji otwieramy to samo okno konsoli, w&nbsp;którym pracował. Po czym:

* najpierw naciskamy `Ctrl`+`C`, żeby przerwać aktualną komendę;
* następnie strzałkę do góry, żeby ponownie wyświetliła się poprzednia komenda (`yt-dlp`...);
* potwierdzamy, wciskając `Enter`.

I *voila*! Jeśli już mamy łączność, to zacznie nam pobierać od miejsca, w&nbsp;którym poprzednio się zatrzymało.

### Odmowa dostępu

Wyświetla się jako `HTTP Error 403: Forbidden`.

Czasami to chwilowy zgrzyt i&nbsp;wystarczy spróbować ponownie. Strzałka w&nbsp;górę, żeby ponownie wyświetlić komendę. *Enter*, żeby ją wykonać. Zazwyczaj mi wtedy działa.

Innym razem sam filmik ma jakieś ograniczenia. Na przykład te wprowadzone przez Google, żeby wyciągnąć od nas zdjęcie dowodu albo numer konta. Zwykle omijam je szerokim łukiem, więc chwilowo nie wiem, czy jest jakieś proste obejście.

### Film niedostępny/usunięty

W takim przypadku wyświetli nam się komunikat `Video unavailable`.  
Oznacza to zapewne, że film został usunięty w&nbsp;przedziale czasowym między wejściem na stronę a&nbsp;rozpoczęciem pobierania. Może usunął go autor, może automatyczna moderacja.

Wyjątkowy pech. Zdarzyło mi się to dosłownie raz, niedawno.

A Wasz film? Jeśli macie nadal otwartą stronę, to zapewne jesteście w stanie go nadal oglądać (serwis jeszcze będzie przez chwilę podtrzymywał połączenie, zanim usunie sam plik). Być może możecie go nawet odzyskać z pamięci podręcznej.

W każdym razie w takiej sytuacji gra się toczy o wysoką stawkę -- **gdy zamkniecie okno przeglądarki z tym filmem, to możecie już go nie zobaczyć**. Jeśli jest fajny, ale nie umielibyście go wyłuskać z pamięci podręcznej, to może warto nawet odpalić jakieś *OBS Studio* i nagrać ekran wraz z dźwiękiem :wink:

### Externally managed environment przy próbie aktualizacji

Ten błąd może się pojawić, jeśli spróbujemy zainstalować albo zaktualizować *yt-dlp* przez Pythona, a&nbsp;dokładniej przez PIP-a, jeden z jego modułów.  
Oznacza, że twórcy systemu celowo utrudnili możliwość modyfikacji systemowego Pythona. Tak jest na przykład na systemie Linux Mint.

W tym konkretnym przypadku istnieje rozwiązanie grzeczne, choć nieco okrężne (opisane w części [„Instalacja na Linuksie”](#instalacja-na-linuksie){:.internal}), a&nbsp;także szybkie i&nbsp;potencjalnie ryzykowne, które umieszczę tutaj.

W dniu pisania tej porady (30.07.2025) mogę po prostu olać ostrzeżenia, wpisując w konsoli groźnie brzmiący tekst:

```
pip install --break-system-packages -U yt-dlp
```

W przypadku Minta olanie ryzyka wydaje mi się uzasadnione --`yt-dlp` to duży i&nbsp;znany projekt; zachowuje się grzecznie i&nbsp;nie wpycha nosa w&nbsp;kluczowe pliki. Choć jest wśród pakietów systemowych, nie stanowi żadnego filara, a&nbsp;jedynie narzędzie pomocnicze jednego z&nbsp;załączonych programów do streamowania.

Nie mogę jednak ręczyć za inne systemy ani obiecać, że na Mincie coś się nie zmieni. Gdyby twórcy wbrew godności człowieka uznali, że zrobią z&nbsp;tego programu fundament systemu, to wykonanie polecenia wyżej mogłoby coś popsuć. Czujcie się ostrzeżeni :smiling_imp:

### Inne błędy

Z czasem trafi się jakiś nieoczekiwany błąd. Może wynikać z&nbsp;tego, że **co jakiś czas YouTube wprowadza większe zmiany za kulisami, przez co psuje _youtube-dl_ i _yt-dlp_**.

Ale autorzy zwykle szybko nadganiają. Wtedy po prostu bierzemy od nich najnowszą wersję i&nbsp;zastępujemy nią poprzednią.

To równocześnie jeden z&nbsp;argumentów przemawiających za tym, żeby korzystać z wersji konsolowej, a nie graficznej. Łatwiej być na bieżąco.

Wszelkie nakładki graficzne może i&nbsp;są przyjaźniejsze, ale nadal zależą od podstawowego, konsolowego programu. Gdy Google coś popsuje, to najpierw źródło musi naprawić to u&nbsp;siebie, a&nbsp;potem autorzy wersji graficznej (którzy mogą np. być akurat na wakacjach) po swojej stronie.

### „Unable to extract uploader_id”

{:.post-meta .bigspace-after}
**Uwaga:** Ten błąd w moim przypadku dotyczył klasycznego *youtube-dl*. Nie usuwam go stąd, bo ma wartość archiwalną. Ale samo rozwiązanie nie będzie skuteczne, jeśli taki błąd komuś wyskoczy przy nowym *yt-dlp*.

W moim przypadku dotknął wersji `2021.12.17`, czyli najnowszej dostępnej na stronie *youtube-dl*. Być może nie aktualizują wersji przez to, że organizacje branżowe próbowały im robić problemy. Ale kod na szczęście zmieniają na bieżąco.

W tym wypadku zwykła aktualizacja nie działa, bo numer działającej i&nbsp;niedziałającej wersji jest taki sam. Ale rozwiązanie opisali [w&nbsp;dyskusji na Githubie](https://github.com/ytdl-org/youtube-dl/issues/31904).

Ogólnie: trzeba zdobyć wersję najnowszą i&nbsp;siłowo zastąpić nią wersję poprzednią.

W przypadku „instalacji” przez włożenie pliku EXE do folderu pomogłoby zapewne zdobycie jego nowszej wersji i zastąpienie nią starej (mimo że formalnie mają ten sam numer wersji), ale tego nie testowałem.

Osobiście instalowałem wcześniej `youtube-dl` przez Pythona, a dokładniej `pip`. W&nbsp;takim wypadku pomogło wpisanie komendy:

<div class="black-bg mono">
pip install --force-reinstall 'https://github.com/ytdl-org/youtube-dl/archive/refs/heads/master.tar.gz'
</div>

...I się naprawiło!

Jeśli mamy Linuksa, na którym `pip` odpowiada starszemu Pythonowi&nbsp;2, to wpisalibyśmy zamiast niego `pip3`.

Jeśli instalowaliśmy dla całego systemu, to przed komendą trzeba jeszcze dopisać `sudo` i&nbsp;spację, a&nbsp;potem podać hasło.

{:.post-meta .bigspace-after}
Niektórzy ogólnie [przestrzegają](https://stackoverflow.com/questions/21055859/what-are-the-risks-of-running-sudo-pip) przed takim trybem instalowania, zwłaszcza gdy nie do końca ufamy instalowanym programom.

I to tyle! Życzę szybkich pobrań i&nbsp;miłego oglądania!

