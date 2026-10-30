---
layout: page
title: "Jak ułatwić sobie życie z trybem ulotnym (live USB)"
description: "Żeby zyskać wyższy poziom prywatności, trzeba się czasem zmienić"
---

Tryb ulotny polega na tym, że ładuje się system z&nbsp;pendrive'a prosto do pamięci. Można go uruchomić niezależnie od tego, czy i&nbsp;jaki główny system mamy zainstalowany na dysku. Ten ładowany do pamięci raczej nie wchodzi mu w&nbsp;drogę.

Ten miniporadnik to uzupełnienie wpisu, w&nbsp;którym skupiam się przede wszystkim na [zaletach trybu ulotnego pod kątem ochrony prywatności](/2026/10/29/systemy-live-prywatnosc){:.internal}.

{% include info.html
type="Uwaga"
text="Tekst na razie nie jest spójnym wpisem, tylko zbiorem luźnych informacji. Będę go stopniowo rozbudowywał i&nbsp;porządkował."
%}

## Schematy działania

Poniżej, w&nbsp;rozwijanych zakładkach, znajduje się parę schematów porównujących ruch plików na systemie klasycznym i&nbsp;ulotnym. To z&nbsp;tego wynika parę cech trybu ulotnego, które można próbować zmienić i&nbsp;dostosować, żeby lepiej się spisywał.

{% include details.html summary="Tryb klasyczny" %}

{:.bigspace-before}
W ten sposób większość osób używa swojego systemu. Jest zainstalowany na stałe, na dysku, i&nbsp;ładuje się po zwykłym wciśnięciu przycisku zasilania.

Faza uruchamiania systemu:

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/live-usb-wprowadzenie/komputer-klasyczne-uruchamianie-schemat.png" alt="Schemat pokazujący ruch plików między pamięcią, dyskiem a&nbsp;pendrive'em"/>

{% include details.html summary="Źródła ikon na schematach" css="figcaption" %}
Ikony ze strony Flaticon: [dysk SSD](https://www.flaticon.com/free-icon/ssd_4854407) od *Hilmy Abiyyu A.*, [pamięć RAM](https://www.flaticon.com/free-icon/computer_16007225) od *JK-Icon*, [pendrive](https://www.flaticon.com/free-icon/pendrive_167505) od *Magnific*, [okrągła strzałka](https://www.flaticon.com/free-icon/clockwise-arrow_2268489). Oficjalne logo systemu Linux Mint. Przeróbki moje.
{% include details-end.html %}

Faza korzystania z&nbsp;systemu:

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/live-usb-wprowadzenie/komputer-klasyczne-korzystanie-schemat.png" alt="Schemat pokazujący ruch plików między pamięcią, dyskiem a&nbsp;pendrive'em"/>

{% include details-end.html %}

{% include details.html summary="Tryb ulotny" %}

{:.bigspace-before}
Polega na włożeniu specjalnie przygotowanego pendrive'a do portu USB, wciśnięciu przycisku zasilania w&nbsp;połączeniu z&nbsp;innym klawiszem, a&nbsp;następnie wybraniu, że chce się załadować system z&nbsp;pendrive'a, a&nbsp;nie dysku.

Faza uruchamiania systemu:

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/live-usb-wprowadzenie/tryb-live-uruchamianie-schemat.png" alt="Schemat pokazujący ruch plików między pamięcią, dyskiem a&nbsp;pendrive'em"/>

Faza korzystania z&nbsp;systemu:

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/live-usb-wprowadzenie/tryb-live-korzystanie-schemat.png" alt="Schemat pokazujący ruch plików między pamięcią, dyskiem a&nbsp;pendrive'em"/>

{% include details-end.html %}

Co warto zapamiętać?

* W&nbsp;obu przypadkach (systemu zwykłego i&nbsp;ulotnego) **do pamięci trafia tylko część systemu, a&nbsp;reszta jest ładowana na raty z&nbsp;jakiegoś nośnika**. W&nbsp;przypadku zwykłego trybu ten nośnik to zwykle dysk twardy; w&nbsp;trybie ulotnym to pendrive. Tak przynajmniej jest domyślnie.
* Dysk twardy jest zwykle dostępny nawet w&nbsp;trybie ulotnym; po prostu jest traktowany jak nośnik zewnętrzny. Żeby przenieść na niego jakieś pliki, trzeba je tam celowo skopiować, nie są na nim zapisywane domyślnie.
* Po wyłączeniu systemu zniknie wszystko, co było w&nbsp;pamięci. To właśnie *ulotność*.

## Usprawienia i&nbsp;rozwiązywanie problemów

W tym miejscu opiszę krótko, jakie rzeczy można zmienić, żeby tryb ulotny lepiej działał (albo w&nbsp;ogóle działał). Będę przy tym odsyłał do innych swoich poradników, które obszerniej poruszają konkretne sprawy.

### Kopiowanie całego systemu do pamięci

Gdy używa się trybu ulotnego, zwykle tylko część systemu jest kopiowana z&nbsp;pendrive'a do pamięci. Reszta zostaje wyłącznie na pendrivie i&nbsp;jest z&nbsp;niego ładowana, gdy pojawi się taka potrzeba.

{:.post-meta .bigspace-after}
Żeby lepiej to sobie wyobrazić, zachęcam do sprawdzenia [schematów z&nbsp;początku wpisu](#schematy-działania){:.internal}.

Taki podział ról prowadzi do pewnej niedogodności -- **pendrive zwykle musi być wpięty do portu USB przez cały czas**. W&nbsp;niektórych przypadkach (PorteuX) można na niego zgrywać pliki, w&nbsp;innych (system z&nbsp;Ventoya) nie można. Niezależnie od tego, wyciągnięcie go skutkowałoby błędami.

Żeby to zmienić, można kazać systemowi kopiować się do pamięci RAM w&nbsp;całości, a&nbsp;nie tylko w&nbsp;części. Włączanie systemu trwa wtedy dłużej i&nbsp;zajmuje on więcej miejsca w&nbsp;pamięci... Ale za to można swobodnie wypiąć pendrive'a.

Ten nakaz sprowadza się nieraz do prostej opcji, której nazwa zależy od systemu.

{% include details.html summary="Pełne kopiowanie do pamięci na różnych Linuksach" %}

* Na popularnych Linuksach z&nbsp;„rodziny Debiana” (**Mint, Zorin**...) podczas uruchamiania systemu należy wejść w&nbsp;tak zwane *menu bootloadera*, wyświetlić listę opcji i&nbsp;dopisać do nich `toram`. Cały proces dokładniej opisałem [w tym przewodniku, na przykładzie Minta](/tutorials/live-squashfs-problem#rozwiązanie-właściwe--opcja-toram){:.internal}.

  Tę opcję trzeba ustawiać przy każdym uruchomieniu. A&nbsp;da się na stałe? Tak. Jeśli dany Linux jest udostępniany jako plik `.iso`, to należałoby go rozpakować, wprowadzić zmiany w&nbsp;odpowiednim pliku z&nbsp;ustawieniami i&nbsp;ponownie spakować całość do pierwotnej postaci. Jeszcze nie miałem okazji tego opisać.

  {:.post-meta .bigspace-after}
  Można przy tym zignorować porady z&nbsp;internetu mówiące o&nbsp;edytowaniu pliku z&nbsp;ustawieniami *po uruchomieniu systemu*. O&nbsp;ile by to zadziałało w&nbsp;przypadku systemu na dysku, o&nbsp;tyle w&nbsp;trybie ulotnym również ten plik jest czyszczony po każdym wyłączeniu.

* Na **Fedorze** jest ponoć bardzo podobnie jak na systemach opisanych wyżej, tyle że zamiast `toram` trzeba wpisać `rd.live.ram=1`.
* Niektóre systemy, zwłaszcza dostosowane do pendrive'ów, mają własne, prostsze ustawienia odpowiedzialne za kopiowanie do pamięci.

  Przykładowo: po stworzeniu sprawnego pendrive'a z&nbsp;wgranym systemem **PorteuX**, można otworzyć plik `PENDRIVE/porteux/porteux.cfg` i&nbsp;dopisać tam w&nbsp;osobnej linijce tekst `copy2ram`. Gdy mamy taką linijkę w&nbsp;pliku, to przy kolejnych uruchomieniach system będzie ładował się do pamięci.

  {:.post-meta .bispace-after}
  Inne nazwy ustawień Porteuksa i&nbsp;sposoby korzystania z&nbsp;nich są opisane w&nbsp;pliku `PENDRIVE/boot/docs/cheatcodes.txt`.

{% include details-end.html %}
