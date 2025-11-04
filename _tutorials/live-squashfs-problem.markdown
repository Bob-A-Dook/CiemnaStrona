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

Kolejnym krokiem -- nadal niezobowiązującym, ale już dającym opcję trwałej instalacji -- jest **uruchomienie w&nbsp;_trybie live_**. Na przykład [przez Ventoya](/tutorials/ventoy){:.internal}.

To taki odpowiednik wersji demo w&nbsp;grach komputerowych. Streszczając: tryb polega na włożeniu stworzonego wcześniej pendrive'a instalacyjnego do portu USB. Podczas uruchamiania komputera naciska się pewną kombinację klawiszy, wybiera z&nbsp;listy Linuksa... I&nbsp;już. Szczegóły pod linkiem wyżej.

Ładuje się, działa. Można sobie wszystko wypróbować. Przeglądać internet. Podpinać inne urządzenia i&nbsp;patrzeć, czy się lubią z&nbsp;systemem.

...Ale jeśli ma się pecha, mogą wystąpić różne dziwne błędy:

* Firefox nagle wyświetli komunikat, że zakładka przestała działać.
* Próba otwarcia niektórych programów sprawi, że pojawi się wirujące kółko, po czym zniknie.
* Nie będzie się dało wyłączyć systemu klikaniem w&nbsp;opcje, a&nbsp;naciśnięcie przycisku zasilania -- choć zadziała -- wyświetli falę błędów. Powtarzać będą się w&nbsp;nich słowa: `SQUASHFS error`.

{:.figure .bigspace-before}
<img src="/assets/tutorials/squashfs-pendrive-blad/squashfs-error-log.png" alt="Zawartość konsoli, w&nbsp;której widać na czerwono treść różnych błędów, w&nbsp;których powtarzają się słowa 'Squashfs error'."/>

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
Ale zaznaczam, że **metoda jest niepewna, zwłaszcza przy bardziej złożonych programach**. Taki na przykład Firefox, uruchomiony przed wypięciem pendrive'a, potrafił działać z&nbsp;niektórymi stronami, a&nbsp;na kolejnej (być może wymagającej załadowania czegoś więcej) spektakularnie się zawiesić.

### Rozwiązanie właściwe -- opcja toram

Źródłem problemu jest to, że pliki są rozdzielone między pendrive'a a&nbsp;pamięć RAM. Logicznym rozwiązaniem może być zatem przerzucenie *wszystkiego* do RAM-u, żeby pendrive przestał być potrzebny.

{:.post-meta .bigspace-after}
Oczywiście należy się najpierw upewnić, że mamy w rezerwie kilka GB pamięci. W&nbsp;przypadku Linuksów takich jak Mint sam system zajmie ok. 4&nbsp;GB, więc komputer powinien mieć *co najmniej* 8&nbsp;GB.

Podczas uruchamiania Minta z&nbsp;pendrive'a powinno się wyświetlić [któreś z&nbsp;dwóch okien](https://test-multi.readthedocs.io/en/latest/boot_options.html) -- albo okno Minta, zawierające jego logo, albo proste czarno-białe okno programu GRUB. W&nbsp;każdym przypadku będzie tam lista kilku sposobów na uruchomienie systemu.

Na tym etapie należy nacisnąć klawisz `E`, jeśli to okno GRUB-a, albo `Tab`, jeśli to okno Minta. Wejdziemy wtedy w tryb edycji ustawień.

{% include info.html
type="Uwaga"
text="Przed naciśnięciem klawisza **należy się upewnić, że mamy zaznaczoną opcję zwykłego uruchomienia** (zwykle pierwsza od góry). Każdej z&nbsp;opcji odpowiada bowiem inne menu z&nbsp;parametrami."
%}

Wypatrujemy linijki zawierającej pod koniec taki fragment:

<div class="black-bg mono">
quiet splash --
</div>

Należy w&nbsp;którymś miejscu dopisać tam `toram` (dosł. „\[ładowanie\] do RAM-u”), oddzielając to spacjami od innych opcji. Przykładowo tu:

<div class="black-bg mono">
quiet splash <span class="corr-ins">toram</span> --
</div>

Na koniec naciskamy `F10`, jeśli jesteśmy w oknie GRUB-a (albo `Enter`, jeśli to okno Minta), żeby uruchomić system z&nbsp;ustawioną nową opcją. Uprzedzam lojalnie, że zajmie to więcej czasu niż zwykle, nawet kilka minut.

{% include info.html
type="Porada"
text="Chcąc potwierdzić zmianę w trybie GRUB-a, ktoś może odruchowo nacisnąć `Enter`. Nie pytajcie, skąd wiem :wink:  
Po jego naciśnięciu nie nastąpi oczekiwane uruchomienie. Zamiast tego tekst po kursorze przeskoczy o&nbsp;jedną linijkę w&nbsp;dół. Aby to naprawić, można od razu nacisnąć `Backspace`, żeby tekst wrócił do odpowiedniej linijki."
%}

### Sprawdzanie, czy zadziałało

Na pierwszy rzut oka nie widać, czy załadowanie systemu do pamięci RAM faktycznie się udało i&nbsp;czy wypięcie pendrive'a nie przyniesie znajomego błędu.  
Logika dyktuje natomiast, że kiedy zgrało się do pamięci więcej rzeczy, to będzie bardziej zapełniona niż zwykle. Stopień zapełnienia można zaś łatwo podejrzeć przez Monitor Systemu.

Żeby go uruchomić, należy kliknąć logo Minta w&nbsp;dolnym lewym rogu ekranu, a&nbsp;następnie kafelek `System Monitor` -- w&nbsp;domyślnym widoku powinien być w&nbsp;prawym dolnym rogu.

{:.post-meta .bigspacr-after}
Jeśli menu zostało przełączone w&nbsp;tryb listy programów, to wchodzimy w&nbsp;zakładkę `System Tools` i&nbsp;tam klikamy `System Monitor`.

{:.figure .bigspace}
<img src="/assets/tutorials/squashfs-pendrive-blad/linux-mint-system-monitor.png" alt="Zrzut ekranu pokazujący menu wyświetlone powyżej dolnego paska i&nbsp;wybrany kafelek System Monitor."/>

W oknie Monitora odwiedzamy zakładkę `Resources` i&nbsp;patrzymy na wykres kołowy zużycia pamięci. W&nbsp;przypadku trybu `toram` system zajmuje niemal 4&nbsp;GB, czyli znacznie więcej niż okolice jednego gigabajta w&nbsp;zwykłym trybie (oczywiście dokładna liczba zależy od wersji Minta, a&nbsp;nawet od komputera).

{:.bigspace}
<img src="/assets/tutorials/squashfs-pendrive-blad/system-monitor-live-usb-zuzycie-pamieci.png" alt="Zrzut ekranu pokazujący fragment Monitora Systemowego obrazujący zużycie pamięci RAM."/>

Czyli raczej wszystko się załadowało. Można teraz wziąć głęboki wdech. Wydech. I&nbsp;wyciągnąć pendrive'a. Kliknąć sobie ikonę Firefoksa, otworzyć parę programów. Wszystko powinno działać. Pendrive'a instalacyjnego można gdzieś odłożyć, ciesząc się dodatkowym wolnym portem USB.

{:.post-meta .bigspace-after}
Włączanie w trybie `toram` to również jedyny (chyba?) sposób na zrzucenie nowych Linuksów na tego samego pendrive'a, z&nbsp;którego załadowało się system. Próbowałem kiedyś prościej (wypięcie → wpięcie → zgranie), ale [efektem był błąd `Invalid magic number`](/tutorials/linux-blad-invalid-magic-number){:.internal}.

## Inne przypadki błędu

Parę osób na oficjalnym forum pisze, że [doświadczyło błędu SquashFS](https://forums.linuxmint.com/viewtopic.php?p=2470661#p2470661) w&nbsp;innym kontekście niż ten, który tu opisuję. Błąd wyskakuje im po (teoretycznie udanym) zainstalowaniu systemu na stałe.

Nie miałem do czynienia z&nbsp;tym błędem, ale skoro już siedzę pod dobrymi słowami kluczowymi, to mogę tu dorzucić szybkie rozwiązanie.

Ludzie piszą, że można to rozwiązać, włączając tryb *live* i&nbsp;instalując system jeszcze raz. Wyświetli się okno wyboru: albo ponowne uruchomienie, albo dalsze korzystania z&nbsp;trybu *live*. Należy wybrać dalsze korzystanie.  
Następnie należy wybrać z&nbsp;menu w&nbsp;dolnym rogu opcję wyłączenia systemu. Pendrive'a wyjąć dopiero po tym, jak wyświetli się prośba o&nbsp;wyjęcie nośnika (`Please remove the installation medium`). Od teraz przy kolejnym uruchomieniu Linux powininien śmigać.

A jak wygląda sprawa błędów `SQUASHFS` na innych Linuksach, których jest multum?

Metoda ładowania wszystkiego do RAM-u opisana w&nbsp;tym wpisie nie jest niestety uniwersalna dla wszystkich Linuksów.  
Przykładowo na systemie Fedora (sprawdzałem tylko wariant KDE Plasma) do opcji uruchamiania wchodzi się tak samo, ale zamiast `toram` należy tam wpisać `rd.live.ram=1`. Na innych systemach może być jeszcze inaczej, niektóre mogą w&nbsp;ogóle nie wspierać ładowania do RAM-u.

{:.post-meta .bigspace-after}
Za rozwiązanie dziękuję [tej odpowiedzi z forum Fedory](https://discussion.fedoraproject.org/t/booting-a-liveos-image-fully-into-ram/78840).

Widzę tu niszę na kolejne samouczki, dopasowane do innych Linuksów i&nbsp;pozwalające szerszemu gronu cieszyć się trybem *live* bez obowiązkowego pendrive'a wystającego z&nbsp;boku.  
Ale skupiam się na Mincie, więc inne Linuksy to sprawa na bliżej nieokreśloną przyszłość :wink:
