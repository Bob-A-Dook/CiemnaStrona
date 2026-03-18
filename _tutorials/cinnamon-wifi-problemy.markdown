---
layout: page
title: "Linux, Cinnamon i problem z hotspotami chronionymi hasłem"
description: "Żeby otworzyć drzwi do sieci, potrzeba breloczka z kluczami."
---

Ostatnio korzystałem sobie z&nbsp;systemu PorteuX w&nbsp;wariancie Cinnamon.

Cinnamon odnosi się tu do *środowiska graficznego*, czyli ogólnego wyglądu i&nbsp;zachowania systemu. Jest znany choćby z&nbsp;popularnego, polecanego dla świeżaków systemu Linux Mint.

PorteuX dodawał od siebie lekkość. Korzystając z&nbsp;Minta Cinnamona na tym samym laptopie, miałem lekkie, ale irytujące opóźnienie przy otwieraniu okien. Na Porteuksie było nieodczuwalne.

{:.post-meta .bigspace-after}
Miało to też potwierdzenie w&nbsp;danych -- Monitor Systemu pokazywał aktywność procesora w&nbsp;trybie biernym (bez uruchomionych programów poza nim samym) na stałym poziomie 1-2%. Magia.

I wszystko byłoby pięknie, gdyby nie jeden zgrzyt -- **nie mogłem połączyć się z&nbsp;hotspotem chronionym hasłem**. 

I nie ma znaczenia, że je znałem. Nawet nie mogłem go wpisać, bo problem pojawiał się na etapie kliknięcia nazwy hotspota.  
Zamiast okna pytającego o&nbsp;hasło, w&nbsp;górnym rogu od razu wyskakiwał komunikat o&nbsp;błędzie:

{:.figure .bigspace}
<img src="/assets/tutorials/linux/cinnamon-brak-wifi/linux-cinnamon-blad-polaczenia-wifi.png" alt="Komunikat z&nbsp;ogólnikową informacją o&nbsp;błędzie podczas próby łączenia się z siecią"/>

A że internet to obecnie podstawa, taki problem był dokuczliwy. Poczytałem trochę, poklikałem i&nbsp;go rozwiązałem. A&nbsp;wiedzą, w&nbsp;sposób najprzystępniejszy jak umiem, podzielę się w&nbsp;tym miniwpisie.

{:.post-meta .bigspace-after}
Nawet jeśli konkretny, opisany tu PorteuX załata błąd w&nbsp;przyszłych edycjach, wiedza może się przydać osobom tworzącym albo wykorzystującym inne odmiany Linuksa z&nbsp;Cinnamonem.

## Spis treści

* [Śledztwo](#śledztwo)
* [Rozwiązanie doraźne](#rozwiązanie-doraźne)
* [Rozwiązanie trwalsze](#rozwiązanie-trwalsze)
* [Rozwiązywanie problemów](#rozwiązywanie-problemów)
  * [Brak procesu gnome-keyring-daemon na liście aktywnych](#brak-procesu-gnome-keyring-daemon-na-liście-aktywnych)
  * [System zaczął wolno reagować na kombinacje klawiszy](#system-zaczął-wolno-reagować-na-kombinacje-klawiszy)

## Śledztwo

Komunikat pokazałem wyżej. Kompletnie nic mi nie mówił, nie było się czego złapać. Zwłaszcza że nie za bardzo wiedziałem, jak podpiąć *strace'a* (popularny program monitorujący) pod klikanie nazwy z&nbsp;paska.

Dlatego trochę pogrzebałem, klikając na różne sposoby ikonę internetu z&nbsp;paska systemowego. Szukałem możliwości otwarcia listy hotspotów wewnątrz osobnego okna, a&nbsp;nie ulotnego menu.

Odkryłem, że taką możliwość daje kliknięcie lewym przyciskiem myszy i&nbsp;wybranie opcji `Network Settings`.

{:.figure .bigspace}
<img src="/assets/tutorials/linux/cinnamon-brak-wifi/cinnamon-ustawienia-sieci.png" alt="Zrzut ekranu, na którym wyróżniono ikonę sieci z&nbsp;dolnego paska systemu, a&nbsp;także opcję Ustawienia Sieci z&nbsp;rozwiniętego menu kontekstowego."/>

Otwarło się wtedy nowe okno. Po lewej stronie miałem domyślnie zaznaczoną zakładkę Wi-Fi. Zaś w&nbsp;większym polu po prawej była lista hotspotów wokół mnie.

Kiedy kliknąłem nazwę hotspota wewnątrz tego okna, to również pokazało komunikat o&nbsp;błędzie w&nbsp;górnym rogu.  
Ale poza tym -- przez ułamek sekundy -- mignął też inny tekst, tuż nad listą. Poklikałem więcej razy, żeby wyłapać jego treść. A&nbsp;mówiła ona:

<div class="black-bg mono post-meta">
Connection activation failed: Secrets were required, but not provided.
</div>

{:.figcaption}
Podobny błąd pokazałby się również przy próbie połączenia przez konsolę, tylko że tam miałbym jasną podpowiedź.

Wpisałem treść komunikatu w&nbsp;wyszukiwarkę (na innym Linuksie, bo na tym -- przypomnę -- nie miałem jak się zalogować). W&nbsp;ten sposób odkryłem parę potencjalnych rozwiązań.

## Rozwiązanie doraźne

Opisany problem występuje na szczęście tylko na poziomie interfejsu graficznego. **Nadal można się połączyć przez konsolę**.  
W tym celu można użyć w&nbsp;niej polecenia:

<pre class="black-bg mono nospace">
nmcli device wifi connect "<span class="red">NAZWA_HOTSPOTA</span>" password "<span class="red">HASŁO</span>"
</pre>

{:.figcaption}
Przypomnę: „użycie polecenia” polega na uruchomieniu konsoli/terminala (często ikoną z&nbsp;paska), wpisaniu podanych słów i&nbsp;wciśnięciu klawisza *Enter*. Aby wkleić tam tekst, należy użyć kombinacji `Ctrl+Shift+V`.

Za <span class="red">NAZWA_HOTSPOTA</span> należy podstawić czytelną nazwę widoczną na liście, jak na przykład *Kawiarnia Open*. Nazwa ta, zwłaszcza jeśli zawiera spację, powinna być otoczona cudzysłowami (w&nbsp;innym wypadku wystąpi błąd).

Należy też podać <span class="red">HASŁO</span> do tego hotspota. Zasada z&nbsp;cudzysłowami jak wyżej.

Po użyciu polecenia bezproblemowo połączyło mnie z&nbsp;siecią.

{% include details.html summary="Alternatywa - interaktywne podanie hasła" %}

Zamiast podawać hasło wewnątrz komendy, można zażądać od systemu pola na jego samodzielne wpisanie:

```
nmcli device wifi connect NAZWA_HOTSPOTA --ask
```

Ta forma może przydać się zwłaszcza wtedy, gdy jednocześnie: 

* wielokrotnie uruchamiamy system od zera (norma choćby w&nbsp;przypadku Porteuksa),
* po każdym uruchomieniu chcemy łączyć się z&nbsp;konkretną siecią (np. z&nbsp;domowym hotspotem),
* nie chcemy trzymać hasła na widoku, wewnątrz skryptu.

W takim przypadku wystarczy mieć hasło w&nbsp;głowie, a&nbsp;wspomniane polecenie konsolowe -- w&nbsp;skrypcie uruchamianym po starcie systemu.

{% include details-end.html %}

## Rozwiązanie trwalsze

A co, jeśli kogoś razi konsola albo woli mieć działający system, ze współgrającymi okienkami i&nbsp;bez komunikatów o&nbsp;błędach?

Rozwiązaniem w&nbsp;moim przypadku była **instalacja programu `gnome-keyring` i&nbsp;uruchomienie go w&nbsp;tle**.

To program od przechowywania haseł, takich jak to do Wi-Fi. Nazwa oznacza dosłownie „breloczek na klucze”, więc pozwolę sobie dla urozmaicenia nazywać ten program Brelokiem.

{:.post-meta .bigspace-after}
Rozwiązanie -- jak w&nbsp;wielu innych przypadkach -- znalazłem na stronie projektu Arch Linux. To popularny linuksowy „składak”, a&nbsp;jego użytkownicy stale napotykają i&nbsp;dokumentują przypadki niewspółgrających ze sobą elementów.

Sposób instalowania Breloka różni się między systemami. Tutaj przytoczę sposób dla Porteuksa, którego fundamentem jest Slackware. Programem od instalowania domyślnych modułów jest tam `getpkg`.  
Żeby pobrać Breloka, musiałem użyć takiego polecenia:

```
getpkg -m gnome-keyring
```

W ten sposób pobrało mi moduł i&nbsp;zapisało go jako plik XZM. Wystarczyło go dwukrotnie kliknąć, żeby został zainstalowany. I, co lepsze, od razu zaczął śmigać w&nbsp;tle.

{:.post-meta .bigspace-after}
Gdyby ktoś nie lubił konsoli, to wiele Linuksów daje możliwość instalowania pakietów przez interfejs graficzny. Nieraz można je też znaleźć w&nbsp;internecie, pobrać i&nbsp;zainstalować kliknięciem.

Po zainstalowaniu Breloka mogłem zobaczyć, czy działa. W&nbsp;tym celu wpisałem polecenie znajdujące go wśród aktywnych procesów:

<div class="black-bg mono nospace">
ps -ax | grep keyring
</div>

{:.figcaption}
Gdyby ktoś szczerze nienawidził konsoli, to można podejrzeć procesy również przez program *System Monitor*, zainstalowany na wielu Linuksach.

Powinno mi pokazać na liście taki proces:

{:.post-meta}
```
 NR_PROCESU  ?  Sl  0:00  /usr/bin/gnome-keyring-daemon --start --foreground --components=secrets
```

{:.post-meta .bigspace-after}
Gdyby nic się nie pojawiło, to odsyłam niżej, do części „Rozwiązywanie problemów”.  
Jeśli pokazuje samo `gnome-keyring-daemon --start`, bez pozostałych parametrów -- to nadal powinno działać, ale warto sprawdzić dla pewności.

Kiedy teraz kliknąłem ikonkę Wi-Fi, to wyświetliło mi się oczekiwane okno pytające o&nbsp;hasło:

{:.figure .bigspace}
<img src="/assets/tutorials/linux/cinnamon-brak-wifi/cinnamon-wifi-pytanie-o-haslo.png" alt="Zrzut ekranu pokazujący małe okno z&nbsp;prośbą o&nbsp;wpisanie hasła do Wi-Fi"/>

A po jego wpisaniu połączyło mnie z&nbsp;siecią i&nbsp;wszystko śmigało jak powinno. Sukces!

## Rozwiązywanie problemów

Część główna zakończona. Oba opisane sposoby, graficzny i&nbsp;konsolowy, powinny w&nbsp;większości przypadku pozwolić na łączenie się z&nbsp;zabezpieczonymi hotspotami.  
Gdyby jednak coś było nie tak, to służę opisami paru problemów, z&nbsp;którymi osobiście się zetknąłem.

### Brak procesu `gnome-keyring-daemon` na liście aktywnych

Możliwe, że z&nbsp;tego czy innego powodu instalacja pakietu *gnome-keyring* nie aktywuje od razu procesu Breloczka i&nbsp;nie pojawi się on na liście procesów.  
W takim wypadku można spróbować aktywować go ręcznie:

```
gnome-keyring-daemon --start
```

Gdyby po tym poleceniu wyświetliło informację o&nbsp;nieznanym programie -- to znaczy, że coś poszło nie tak podczas instalacji. Powinna była bowiem przenieść ten program do folderu systemowego, czyniąc go publicznie dostępnym.

Można spróbować w takiej sytuacji zainstalować `gnome-keyring` od nowa, ewnetualnie pozyskując pakiet z&nbsp;innego źródła.

{% include details.html summary="Możliwy komunikat o braku pliku" %}

Gdybym zakończył ręcznie cały proces i&nbsp;aktywował go ponownie, poleceniem takim jak wyżej, to wyświetliłoby mi taki komunikat: 

<div class="black-bg mono post-meta">
couldn't access control socket: /run/user/1000/keyring/control: No such file or directory
</div>

Nie miał on jednak wpływu na dalsze działanie programu, dlatego przytaczam go jedynie jako ciekawostkę.

{% include details-end.html %}

### System zaczął wolno reagować na kombinacje klawiszy

Po instalacji Breloka warto na próbę zrobić zrzut ekranu klawiszem `PrintScreen` i&nbsp;ocenić, czy został wykonany z&nbsp;taką samą szybkością jak zwykle.

{:.post-meta .bigspace-after}
Pewne spowolnienie wydaje się nieuniknione -- w&nbsp;końcu nawet najlżejszy proces działający w&nbsp;tle cośtam od siebie dodaje -- ale mówię tu o&nbsp;opóźnieniu *patologicznym*, liczącym nawet kilkanaście sekund. 

Taki problem mnie dotknął, kiedy użyłem modułu pobranego z&nbsp;innego źródła niż `getpkg`. Dokładniej: na stronce *pkgs.org* znalazłem link do pliku (*gnome-keyring-50.0-x86_64-1.txz*). Pobrałem go, skonwertowałem ręcznie i&nbsp;aktywowałem dwukrotnym kliknięciem.

Niestety **w tym przypadku Brelok popsuł mi działanie systemowych skrótów klawiszowych**. Zaczęło występować znaczne, wielosekundowe opóźnienie między wciśnięciem klawiszy a&nbsp;spodziewaną reakcją. Dotyczyło między innymi: 

* kombinacji otwierającej okno Terminala,
* kombinacji robiącej zrzut (*screenshota*) całego ekranu.

{:.post-meta .bigspace-after}
Skróty proste, wewnątrz programów -- jak `Ctrl+C` do skopiowania folderu z&nbsp;przeglądarki plików -- działały normalnie. To dlatego proponuję użyć screenshotów do testowania, czy wystąpił błąd.

Problem udało mi się naprawić przez metodę uniwersalną typu „wyłącz i&nbsp;włącz ponownie”.

{% include details.html summary="Naprawienie problemu przez restart procesu" %}

{:.bigspace-before}
Czy błąd czymś się wyróżniał na poziomie systemu? Tak. Zauważyłem, że gdybym wyświetlił listę procesów taką komendą:

```
ps -ax | grep keyring
```

...to pokazałoby takie coś:

{:.post-meta}
```
NR_PROCESU  ?  Sl  0:00  /usr/bin/gnome-keyring-daemon --daemonize --login
```

To inne parametry programu niż przy poprawnej instalacji, którą opisałem wcześniej. Z&nbsp;jakiegoś powodu chyba nie lubiły się z&nbsp;systemem.  
Skoro z&nbsp;procesem było coś nie tak, to postanowiłem go ubić:

```
kill NR_PROCESU
```

Następnie aktywowałem proces od zera:

```
gnome-keyring-daemon --start
```

To naprawiło problem. Miałem teraz działające okno z&nbsp;pytaniem o&nbsp;hasło, a&nbsp;jednocześnie brak opóźnienia przy podstawowywych skrótach klawiszowych.

Gdybym teraz jeszcze raz sprawdził listę aktywnych procesów, to zobaczyłbym przy Breloku to samo, co przy aktywacji przez „dobry” moduł. Ten właściwy zestaw parametrów:

{:.post-meta .nospace}
```
/usr/bin/gnome-keyring-daemon --start --foreground --components=secrets
```

{% include details-end.html %}

Gdybym jednak mógł coś doradzić, to proponuję w&nbsp;przypadku dziwnego pakietu, niedziałającego po pierwszej instalacji, spróbować sięgnąć po inny.  
W końcu jeśli pojawiła się jedna oczywista niekompatybilność, to nie można wykluczyć, że idą za nią inne, głębiej ukryte w&nbsp;programie.

I na tym kończę ten wpis -- z&nbsp;lekkim systemem, Cinnamonem pełnym bajerów i&nbsp;do tego działającym internetem. Tak trzeba żyć :sunglasses:

