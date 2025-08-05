---
layout: page
title: "Linux Mint i błędy w trybie live po odłączeniu pamięci USB"
description: "Co zrobić, żeby błąd SquashFS nie zgniótł pierwszych wrażeń"
---

W związku ze [staczaniem się Windowsa](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal} ku rejonom turbokomercyjno-dziadowskim, sporo osób rozważa zmianę systemu.  
Jako jeden z&nbsp;wielu rozczarowanych, wychodzę tej potrzebie naprzeciw. Gromadzę na blogu samouczki takie jak ten, które ułatwią chętnym przesiadkę z&nbsp;Windowsa na darmową alternatywę -- system Linux Mint.

{:.post-meta .bigspace-after}
A ponieważ uważam się za pragmatycznego sympatyka, uprzedzę wprost -- niektórym (zwłaszcza osobom używającym kompa do gier, oglądania filmów w&nbsp;4K i&nbsp;pracy w&nbsp;programach komercyjnych) Linux może nie podpasować. Tym niemniej spróbować warto.

Istnieje wiele sposobów na zapoznanie się z&nbsp;Mintem, w&nbsp;tym całkiem niezobowiązujące -- od oglądania filmików w&nbsp;internecie, przez [interaktywne platformy jak *Distrosea*](https://distrosea.com/), po instalację w&nbsp;programie zwanym [maszyną wirtualną](/2025/02/10/prywatnosc-maszyny-wirtualne){:.internal} (wtedy Linux jest zaledwie jednym okienkiem wśród innych).

Kolejnym krokiem -- nadal niezobowiązującym, ale już dającym opcję trwałej instalacji -- jest **uruchomienie w&nbsp;_trybie live_**. Taki odpowiednik wersji demo w&nbsp;grach komputerowych. Opiszę go dokładniej w&nbsp;innym wpisie, tutaj tylko streszczenie.

Tryb polega zwykle na tym, że wkłada się stworzonego wcześniej pendrive'a instalacyjnego do portu USB. Podczas uruchamiania komputera naciska się pewną kombinację klawiszy, wybiera opcję uruchomienia Linuksa... I&nbsp;już. Ładuje się, działa. Można sobie wszystko wypróbować. Przeglądać internet. Podpinać inne urządzenia i&nbsp;patrzeć, czy się lubią z&nbsp;systemem.

...Ale jeśli ma się pecha, może wystąpić błąd. Firefox nagle wyświetli komunikat, że zakładka przestała działać. Próba otwarcia niektórych programów sprawi, że pojawi się wirujące kółko, po czym zniknie. Nie będzie się dało wyłączyć systemu klikaniem w&nbsp;opcje, a&nbsp;naciśnięcie przycisku zasilania -- choć zadziała -- wyświetli falę błędów. Powtarzać będą się w&nbsp;nich słowa: `SQUASHFS error`.

{:.figure .bigspace-before}
<img src="/assets/posts/tutorials/squashfs-pendrive-blad/squashfs-error-log.png" alt="Zawartość konsoli, w&nbsp;której widać na czerwono treść różnych błędów, w&nbsp;których powtarzają się słowa 'Squashfs error'."/>

{:.figcaption}
Tu akurat wpisy odczytane z&nbsp;dziennika systemu po nieudanej próbie uruchomienia programu. Po naciśnięciu przycisku zasilania byłyby podobne, ale bez czerwieni.

Takie coś może zrazić do Linuksa. Ale spokojnie -- **przyczyna problemu to najczęściej zwykłe odłączenie pendrive'a instalacyjnego**. Poluzowanie styków.  
Rozwiązanie jest proste. Co więcej: można łatwo sobie ustawić pewną opcję, która powinna całkowicie zapobiec takim błędom na czas sesji w&nbsp;trybie *live*.

O co w&nbsp;tym chodzi? Już wyjaśniam.

## Z&nbsp;czego wynika problem

W *trybie live*, po załadowaniu systemu Linux Mint z&nbsp;pendrive'a, sytuacja wygląda zwykle następująco:

* twardy dysk sobie „śpi” i&nbsp;nic do niego nie zagląda (chyba że sami go wywołamy, np. klikając ikonę w&nbsp;przeglądarce plików),
* podstawowe pliki potrzebne Mintowi do działania są załadowane do pamięci RAM,
* reszta plików nadal tkwi na pendrivie.

Wspomniany w&nbsp;tekście błędu `SQUASHFS` dotyczy właśnie punktu trzeciego, reszty plików. To skrót od `SQUASH Filesystem`. [Skompresowany system plików](https://www.kernel.org/doc/html/latest/filesystems/squashfs.html), z&nbsp;którego można jedynie odczytywać dane. Idealny do przechowywania „kawałków systemu” i&nbsp;wydawania ich na żądanie.

...Tyle że kiedy system wysyła prośbę o&nbsp;dane z&nbsp;pendrive'a, a&nbsp;ten jest odłączony, to siłą rzeczy nie otrzyma niczego. Chwilę poczeka (przez ten czas widzimy wirujące kółko), a&nbsp;potem odpuści po cichu. Jedynie do dziennika systemowego trafi informacja o&nbsp;błędzie. A&nbsp;że na pendrivie było zadziwiająco wiele rzeczy, to skutki rozłączenia będą dotkliwe.

{:.post-meta .bigspace-after}
A dlaczego po ponownym podłączeniu pendrive'a (ręcznym lub samoistnym) się to nie naprawia? Czy twórcy Minta nie mogliby dodać jakiegoś wznawiania poprzedniego stanu po rozłączeniu?  
Tego niestety nie wiem. Zawsze można się do nich zwrócić z&nbsp;informacją o&nbsp;błędzie.

## Rozwiązanie

Wspomniana sytuacja wydaje się mieć proste, intuicyjne rozwiązanie -- **nie wyjmować pendrive'a instalacyjnego podczas przebywania w&nbsp;trybie _live_**. Wtedy system zawsze będzie dostawał pliki, których żąda. Nie wyskoczą błędy.

...Ale łatwo mówić. Choć dla wielu osób *tryb live* to tylko droga do trwałej instalacji albo niezobowiązujące łażenie, niektórzy chcą na nim coś stworzyć. Przykładem ten skromny ja, testujący i&nbsp;zapisujący w&nbsp;notatkach cechy różnych Linuksów.

Byłoby super, gdyby dało się odpiąć pendrive'a instalacyjnego, a&nbsp;potem normalnie korzystać z&nbsp;programów, bez obawy że wszystko przestanie działać i&nbsp;cała sesja przepadnie. Na szczęście jest parę opcji.

### Rozwiązanie nietrwałe -- jak najszybsze włączenie programów

Według moich obserwacji wystarczyło uruchomić niektóre programy jeden raz, żeby zgrały się do pamięci i&nbsp;przestały wymagać komunikacji z&nbsp;pendrive'em.

Jeśli mam proste zadanie -- np. napisać na Mincie parę skryptów w&nbsp;prostym „Notatniku” i&nbsp;zgrać je na nośnik (np. innego pendrive'a) -- to wykonuję następujące rzeczy:

* otwieram edytor tekstowy,
* otwieram przeglądarkę plików,
* podłączam nośnik.

Od teraz nawet gdyby pendrive instalacyjny się wysunął, nie mam problemu z&nbsp;dalszym klepaniem rzeczy w&nbsp;notatniku i&nbsp;przerzucaniem ich na zewnątrz.  
Ale zaznaczam, że nie jest to metoda pewna, zwłaszcza przy bardziej złożonych programach. Taki na przykład Firefox, uruchomiony przed wypięciem pendrive'a, potrafił działać z&nbsp;niektórymi stronami, a&nbsp;na kolejnej (być może wymagającej załadowania czegoś więcej) spektakularnie się zawiesić.

### Rozwiązanie właściwe -- opcja toram

Podczas uruchamiania Minta z&nbsp;pendrive'a powinno się wyświetlić [okno programu Grub](https://linuxmint-user-guide.readthedocs.io/en/latest/grub.html) -- czarne tło, jasne ramki. Do wyboru kilka sposobów na uruchomienie systemu.

Na tym etapie należy nacisnąć klawisz `E`. Wyświetli się wtedy menu ze szczegółowymi ustawieniami.

{:.post-meta .bigspace-after}
Screena niestety nie mam, bo nie da się go łatwo wykonać przy ładowaniu z&nbsp;pendrive'a; musiałbym uruchomić osobnego Minta w&nbsp;maszynie wirtualnej. Jak to zrobię, to dodam obrazki.

Wypatrujemy tam linijki zaczynającej się od słowa `linux` (u&nbsp;mnie trzecia od góry, licząc jedną pustą). Pod jej koniec znajduje się fragment:

<div class="black-bg mono">
quiet splash --
</div>

Należy w&nbsp;którymś miejscu, między spacjami, dopisać tam `toram` (dosł. „\[ładowanie\] do RAM-u”). Przykładowo tu:

<div class="black-bg mono">
quiet splash <span class="corr-ins">toram</span> --
</div>

Na koniec naciskamy `F10`, żeby uruchomić system z&nbsp;ustawioną nową opcją. Uprzedzam lojalnie, że zajmie to więcej czasu niż zwykle, nawet kilka minut.

{% include info.html
type="Porada"
text="Chcąc potwierdzić zmianę, można odruchowo nacisnąć *zły* klawisz `Enter`. Nie pytajcie, skąd wiem :wink:  
Po jego naciśnięciu nie nastąpi oczekiwane uruchomienie. Zamiast tego tekst po kursorze przeskoczy o&nbsp;jedną linijkę w&nbsp;dół. Aby to naprawić, można od razu nacisnąć `Backspace`, żeby tekst wrócił do odpowiedniej linijki."
%}

### Sprawdzanie, czy zadziałało

Na pierwszy rzut oka nie widać, czy załadowanie systemu do pamięci RAM faktycznie się udało i&nbsp;czy wypięcie pendrive'a nie przyniesie znajomego błędu.  
Logika dyktuje natomiast, że kiedy zgrało się do pamięci więcej rzeczy, to będzie bardziej zapełniona niż zwykle. Stopień zapełnienia można zaś łatwo podejrzeć przez Monitor Systemu.

Żeby go uruchomić, należy kliknąć logo Minta w&nbsp;dolnym lewym rogu ekranu, a&nbsp;następnie kafelek `System Monitor` -- w&nbsp;domyślnym widoku powinien być w&nbsp;prawym dolnym rogu.

{:.post-meta .bigspacr-after}
Jeśli menu zostało przełączone w&nbsp;tryb listy programów, to wchodzimy w&nbsp;zakładkę `System Tools` i&nbsp;tam klikamy `System Monitor`.

{:.figure .bigspace}
<img src="/assets/posts/tutorials/squashfs-pendrive-blad/linux-mint-system-monitor.png" alt="Zrzut ekranu pokazujący menu wyświetlone powyżej dolnego paska i&nbsp;wybrany kafelek System Monitor."/>

Następnie patrzymy na wykres kołowy zużycia pamięci. W&nbsp;przypadku trybu `toram` system zajmuje niemal 4&nbsp;GB, czyli znacznie więcej niż w&nbsp;zwykłym trybie (oczywiście dokładna liczba będzie się pewnie zmieniała między wersjami Minta).

{:.bigspace}
<img src="/assets/posts/tutorials/squashfs-pendrive-blad/system-monitor-live-usb-zuzycie-pamieci.png" alt="Zrzut ekranu pokazujący fragment Monitora Systemowego obrazujący zużycie pamięci RAM."/>

Czyli raczej wszystko się załadowało. Można teraz wziąć głęboki wdech. Wydech. I&nbsp;wyciągnąć pendrive'a. Kliknąć sobie ikonę Firefoksa, otworzyć parę programów. Wszystko powinno działać. Pendrive'a instalacyjnego można gdzieś odłożyć, ciesząc się dodatkowym wolnym portem USB.

## Inne przypadki błędu

Parę osób na oficjalnym forum pisze, że [doświadczyło błędu SquashFS](https://forums.linuxmint.com/viewtopic.php?p=2470661#p2470661) w&nbsp;innym kontekście niż ten, który tu opisuję. Błąd wyskakuje im po (teoretycznie udanym) zainstalowaniu systemu na stałe.

Nie miałem do czynienia z&nbsp;tym błędem, ale skoro już siedzę pod dobrymi słowami kluczowymi, to mogę tu dorzucić szybkie rozwiązanie.

Ludzie piszą, że można to rozwiązać, włączając tryb *live* i&nbsp;instalując system jeszcze raz. Wyświetli się okno wyboru: albo ponowne uruchomienie, albo dalsze korzystania z&nbsp;trybu *live*. Należy wybrać dalsze korzystanie.  
Następnie należy wybrać z&nbsp;menu w&nbsp;dolnym rogu opcję wyłączenia systemu. Pendrive'a wyjąć dopiero po tym, jak wyświetli się prośba o&nbsp;wyjęcie nośnika (`Please remove the installation medium`). Od teraz przy kolejnym uruchomieniu Linux powininien śmigać.

A jak wygląda sprawa błędów `SQUASHFS` na innych Linuksach, których jest multum?

Opisana tu metoda ładowania wszystkiego do RAM-u nie jest niestety uniwersalna. Przykładowo na systemie Fedora KDE występuje ten sam problem w&nbsp;przypadku wypięcia pendrive'a. Tak jak na Mincie, można wejść w&nbsp;menu GRUB-a i&nbsp;dopisać tekst `toram` w&nbsp;ustawieniach początkowych.  
Ale na tym podobieństwa się kończą, bo wedle moich obserwacji nic to nie zmieniło. Obserwacje innych na forach wydają się [potwierdzać brak efektów](https://unix.stackexchange.com/questions/683945/fedora-liveusb-how-to-boot-to-ram). Działa podobno inna opcja, ale nie miałem okazji jej sprawdzić.

Widzę tu niszę na kolejne samouczki, dopasowane do innych Linuksów i&nbsp;pozwalające szerszemu gronu cieszyć się trybem *live* bez obowiązkowego pendrive'a wystającego z&nbsp;boku. Ale to sprawa na bliżej nieokreśloną przyszłość :wink:
