---
layout: page
title: Jak używać podstawowych czcionek z Windowsa na Linuksie
description: "Otwarty świat też może pisać Comic Sansem"
---

Kiedy zacząłem pisać ten poradnik, był wrzesień 2025&nbsp;roku. Nieubłaganie zbliżał się październikowy termin [wygaśnięcia wsparcia dla Windowsa 10](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}. A&nbsp;co za tym idzie -- rosła szansa, że nieco więcej osób niż zwykle spróbuje darmowej alternatywy, która zwie się Linux.

Lubię go, cenię i&nbsp;używam na co dzień (dokładniej rzecz biorąc: mój system z&nbsp;wyboru to Linux Mint). Życzę mu jak najlepiej. Ale wiem również, że niektóre jego cechy mogą odstraszać osoby przyzwyczajone do Windowsa. 

Bo jak nazwać sytuację, kiedy dostaje się, w&nbsp;pracy lub życiu, prosty dokument stworzony w&nbsp;programie Microsoft Word, a&nbsp;po otwarciu go w&nbsp;programie LibreOffice (linuksowym odpowiedniku) tekst wygląda inaczej niż w&nbsp;Wordzie?

Może pojawić się myśl: „to jakieś dziadostwo, nie polubimy się”. Złe pierwsze wrażenie.  
A jak jest naprawdę? Inny wygląd wynika z&nbsp;tego, że na Linuksie nie ma paru podstawowych czcionek znanych z&nbsp;Windowsa. **Nie mogą ich _domyślnie_ udostępniać w&nbsp;obawie przed krokami prawnymi Microsoftu -- ale wystarczy parę kliknięć, żeby to obejść**.

W tym poradniku pokażę sposób na zdobywanie czcionek z&nbsp;Worda/Windowsa i&nbsp;używanie ich wewnątrz LibreOffice'a; wnioski łatwo można odnieść też do innych czcionek i&nbsp;linuksowych programów.  
Zapraszam!

{% include info.html
type="Uwaga"
text="Uprzedzając opinie purystów: tak, wiem że formalnie rzecz biorąc czcionka to rzecz fizyczna, a&nbsp;postać elektroniczna to *font*. Ale w&nbsp;mowie potocznej króluje ta pierwsza nazwa, więc to jej będę się trzymał, żeby trafić do szerszego grona :wink:"
%}

## Spis treści

* [Jak poznać, że brakuje czcionek](#jak-poznać-że-brakuje-czcionek)
* [Instalowanie czcionek Microsoftu](#instalowanie-czcionek-microsoftu)
* [Bonus: używanie czcionek bez instalowania](#bonus-używanie-czcionek-bez-instalowania)
* [Na przyszłość](#na-przyszłość)

## Jak poznać, że brakuje czcionek

Spójrzmy na własne oczy na praktyczny przykład. W&nbsp;roli ilustracji użyłem [losowego pliku DOCX](https://auladigital83.files.wordpress.com/2015/09/cuaderno-completo-ejercicios-word2007.docx), swoistego przewodnika po możliwościach Worda. Można go sobie zapisać na dysku i&nbsp;otworzyć w&nbsp;LibreOffisie.

Na stronie 8&nbsp;znajduje się kilka przykładów kultowych microsoftowych czcionek: Arial, Times New Roman oraz Comic Sans.

Jeśli kliknie się na dowolny fragment tekstu, to w&nbsp;górnym pasku wyświetli się nazwa odpowiadającej mu czcionki. I&nbsp;tu kluczowy fakt: **jeśli LibreOffice nie ma dostępu do jakiejś czcionki, to wyświetla jej nazwę kursywą (pochylonymi literami)**. Do tego po najechaniu kursorem na nazwę wyświetli się informacja, że użyto zamiennika.

W takich przypadkach to, co widzimy w&nbsp;dokumencie, to tylko czcionka zastępcza. Niektóre jej cechy mogą być dopasowane do cech tej zalecanej, odczytanych z&nbsp;metadanych, ale zawsze będzie tylko imitacją.

<img src="/assets/tutorials/loffice-czcionki-microsoftu/comic-sans-libreoffice-brak-czcionki.png" alt=""/>

{:.figcaption}
Niby Comic Sans, ale jakiś poważny, a&nbsp;to *m* wręcz nieco gotyckie. Czas to zmienić!

Dla porównania -- tak by wyglądała w&nbsp;górnym pasku nazwa czcionki zainstalowanej i&nbsp;dostępnej.

<img src="/assets/tutorials/loffice-czcionki-microsoftu/libreoffice-czcionka-obecna.png" alt="Zrzut ekranu z&nbsp;programu LibreOffice pokazujący czcionkę Liberation Serif w&nbsp;górnym pasku"/>

## Instalowanie czcionek Microsoftu

A czemu twórcy Linuksa i&nbsp;LibreOffice'a po prostu nie dołączają czcionek do systemu? Może się wydawać, że to przecież bardzo by poprawiło komfort korzystania z&nbsp;niego.  
Niestety to nie takie proste. Zapewne ogranicza ich fakt, że Microsoft, chcąc zachować dominację, mógłby przyczepić się do udostępniania ich czcionek bez licencji.

Twórcy otwartych alternatyw od dawna musieli stawać na głowie i&nbsp;np. tworzyć programy [podzieleni na dwie grupy](https://gitlab.winehq.org/wine/wine/-/wikis/Clean-Room-Guidelines), z&nbsp;których tylko jedna analizowała kod Microsoftu, zaś&nbsp;druga wdrażała wnioski z&nbsp;analiz. W&nbsp;innym wypadku było ryzyko, że ich dojadą za naruszanie praw autorskich.

W przypadku czcionek bariery są na szczęście znacznie niższe. Wystarczy na własną rękę uruchomić instalatora czcionek, kliknąć zgodę na warunki licencji -- i&nbsp;gotowe.

{% include info.html
type="Informacja"
text="Sposób instalacji dopasowałem do swojego systemu Linux Mint (edycja MATE, wersja 22.2). Na innych Linuksach może wyglądać nieco inaczej; bardziej uniwersalny będzie sposób konsolowy.  
Poza tym w&nbsp;opisie sposobu graficznego używam czasem angielskich nazw, ale polskie odpowiedniki powinny jasno wynikać z obrazków i&nbsp;kontekstu."
%}

Na początek trzeba się upewnić, czy mamy połączenie z&nbsp;internetem. Jeśli tak, to do wyboru są dwie ścieżki -- albo proste klikanie, albo uruchomienie na krótką chwilę konsoli. Opiszę tu obie.

{% include details.html summary="Sposób graficzny" %}

Należy kliknąć w&nbsp;logo systemu w&nbsp;dolnym lewym rogu, potem wybrać z&nbsp;menu menedżera oprogramowania. Można chwilę poczekać, aż program sobie zaktualizuje dostępne zasoby.

{:.bigspace}
<img src="/assets/tutorials/loffice-czcionki-microsoftu/mint-software-manager.png" alt=""/>

Po jakimś czasie pojawi się lista programów dostępnych w&nbsp;bazie. Żeby oszczędzić sobie żmudnego przeczesywania, proponuję kliknąć pasek wyszukiwania u&nbsp;góry i&nbsp;zacząć tam wpisywać słowo `mscore`.

{:.bigspace}
<img src="/assets/tutorials/loffice-czcionki-microsoftu/linux-package-manager-mscorefonts.png" alt="Zrzut ekranu z&nbsp;instalatora oprogramowania na Mincie, pokazujący znaleziony pakiet czcionek TTF Microsoftu."/>

Lista zawęzi się do jedynej poszukiwanych rzeczy, pakietu *Ttf-mscorefonts-installer*. Należy kliknąć jego miniaturkę, żeby przejść do informacji szczegółowych.

W górnym prawym rogu przez chwilę powinno kręcić się kółko. Kiedy przestanie, w&nbsp;jego miejscu pojawi się zielony przycisk `Install`. Klikamy go, a&nbsp;następnie klikamy `Continue`.

{:.bigspace}
<img src="/assets/tutorials/loffice-czcionki-microsoftu/mscorefonts-install.png" alt=""/>

Po pewnym czasie wyświetli się okienko dotyczące licencji (EULA)... Bez jej treści :wink: Jakiś błędzik programu. A&nbsp;może *performance* artystyczny sugerujący, że nikt obecnie nie czyta licencji?  
W każdym razie nie wpływa to na resztę programu. Gdyby ktoś serio przejmował się licencją, to może użyć instalatora konsolowego. A&nbsp;wszyscy pozostali mogą zaznaczyć zgodę na niewidoczny tekst, po czym kliknąć `Next`.

{:.figure .bigspace}
<img src="/assets/tutorials/loffice-czcionki-microsoftu/linux-mint-msfonts-install-licencja.png" alt=""/>

Na tym etapie warto jeszcze nie zamykać okna programu, niech instalacja w&nbsp;spokoju się zakończy. Kiedy to się stanie, zielony przycisk u&nbsp;góry zmieni kolor na czerwony.

{% include details-end.html %}

{% include details.html summary="Sposób konsolowy" %}

Konsolę, zwaną też terminalem, można uruchomić kombinacją klawiszy `Ctrl+Alt+T` albo czarną ikoną z&nbsp;dolnego paska. W&nbsp;uruchomiony terminal należy następnie wkleić albo wpisać -- po czym potwierdzić *Enterem* -- takie polecenie:

<div class="black-bg mono nospace">
sudo apt install ttf-mscorefonts-installer
</div>

{:.figcaption}
Dla osób chcących stąd skopiować: żeby wkleić coś w&nbsp;terminal, trzeba nacisnąć kombinację <code>Ctrl+<span class="red">Shift</span>+V</code>. Bez *Shifta* nie zadziała.

W tym momencie konsola może poprosić o&nbsp;wpisanie hasła do komputera. Wpisujemy, potwierdzamy *Enterem*. Wyświetli się również informacja, że zainstalowane zostaną nowe pliki. Zgadzamy się, wciskając `Y` i&nbsp;znów potwierdzając *Enterem*. Po pewnym czasie czcionki powinny zostać zainstalowane.

Mógłbym przysiąc, że swego czasu na tym etapie ponadto pojawiło mi się okno (bardzo w&nbsp;stylu retro) z&nbsp;informacją o&nbsp;licencji. Gdyby tak było, to należy nacisnąć strzałkę w&nbsp;bok, żeby zaznaczyć zgodę, a&nbsp;potem potwierdzić ją *Enterem*.

{% include info.html
type="Uwaga"
text="Wskazane wyżej polecenie konsolowe zadziała na wielu popularnych odmianach Linuksa, które używają menedżera pakietów `apt` (takich jak Debian, Ubuntu, Mint, Zorin...).  
Ale na takiej Fedorze, również popularnej, jest zamiast niego *`yum`*{:.corr-del}`dnf`. Na Archu to `pacman`, niektóre inne Linuksy mają jeszcze innych menedżerów, niektóre nie udostępniają czcionek Microsoftu... Po instrukcje instalacji na takich systemach odsyłam póki co do [innego polskojęzycznego poradnika](https://newsblog.pl/jak-zdobyc-podstawowe-czcionki-microsoft-w-systemie-linux/). Można też spróbować ręcznego kopiowania plików TTF (opisałem pod koniec wpisu)."
%}

{% include details-end.html %}

LibreOffice nie odświeży się automatycznie, więc **po zainstalowaniu brakujących czcionek należy zamknąć i&nbsp;ponownie otworzyć program** (*wszystkie* jego okna, nie tylko to z&nbsp;interesującym nas dokumentem).

Nazwa czcionki w&nbsp;pasku powinna od teraz być zapisana normalnie, bez kursywy. A&nbsp;jej wygląd? Taki jak być powinien -- kochany, memiczny Comic Sans.

{:.bigspace}
<img src="/assets/tutorials/loffice-czcionki-microsoftu/comic-sans-libreoffice-jest-czcionka.png" alt=""/>

{:.post-meta}
Żeby nie było tak różowo -- choć czcionka działa, uważni czytelnicy mogą dostrzec na dalszych stronach m.in. tekst niemieszczący się w&nbsp;polach. To prawda, nadal trafiają się pewne niekompatybilności z&nbsp;Wordem. Ale z&nbsp;każdą wersją jest coraz lepiej.

## Bonus: używanie czcionek bez instalowania

A co, gdybyśmy chcieli korzystać z&nbsp;microsoftowych czcionek w&nbsp;trybie *offline*? Pobrać je tylko raz, na początku, a&nbsp;potem nosić na pendrivie, bez konieczności każdorazowego instalowania przez internet?

Na szczęście kwestia poważnie brzmiącej „instalacji czcionek” na Linuksie jest zakulisowo naprawdę prosta. Sprowadza się do włożenia plików (TTF, OTF itd.) do odpowiedniego systemowego folderu. Jego ścieżka w&nbsp;przypadku naszych czcionek:

```
/usr/share/fonts/truetype
```

Można sobie skopiować ten tekst, po czym uruchomić domyślną przeglądarkę plików Minta. Po lewej stronie górnego paska jest ikonka kartki i&nbsp;ołówka. Klikamy ją, żeby pojawiło się pole tekstowe. Można usunąć stamtąd aktualną ścieżkę, wkleić zamiast niej nasz tekst i&nbsp;nacisnąć *Enter*.

{:.post-meta .bigspace-after}
A gdyby ktoś wolał klikaninę krok po kroku: najpierw `File System` w&nbsp;kolumnie po lewej, żeby przejść do katalogu systemowego. A&nbsp;potem kolejno foldery: *usr*, w&nbsp;nim *share*, w&nbsp;nim *fonts*, w&nbsp;nim *truetype*.

Można sobie skopiować cały folder `msttcorefonts` i&nbsp;zgrać go na pendrive'a czy inny nośnik. To w&nbsp;nim są wszystkie czcionki od Microsoftu.

{:.figure .bigspace}
<img src="/assets/tutorials/loffice-czcionki-microsoftu/linux-mint-lokalizacja-mstcorefonts.png" alt="Zrzut ekranu pokazujący zawartość systemowego folderu z&nbsp;czcionkami, wyróżniony jest na nim folder msttcorefonts."/>

Później, kiedy zasiadamy do komputera z&nbsp;innym Linuksem, pozbawionym MS-owych czcionek:

* kopiujemy sobie zapisany folder z&nbsp;nośnika;
* wchodzimy do tego systemowego folderu co wyżej, w&nbsp;taki sam sposób;
* w&nbsp;górnym menu wybieramy zakładkę `Plik`, a&nbsp;potem opcję `Uruchom jako administrator` (otworzy się nowe okno w&nbsp;trybie superużytkownika)
* wklejamy tam nasz folder `msttcorefonts`,
* zamykamy okno, nim omyłkowo usuniemy coś systemowego :wink:

Następnie można dla pewności uruchomić konsolę i&nbsp;wpisać tam polecenie odświeżające takie wewnętrzne, systemowe przyporządkowanie znaków logicznych do graficznych:

```
fc-cache -f -v
```

Następnie można zamknąć wszystkie okna LibreOffice'a (jeśli jakieś były otwarte) i&nbsp;upewnić się, czy po naszym ręcznym przeniesieniu czcionki działają jak należy.

## Na przyszłość

Zainstalowanie domyślnych czcionek z&nbsp;Windowsa może znacznie poprawić kompatybilność świata linuksowego z&nbsp;wytworami Microsoftu. 

Nie rozwiąże jednak wszystkich problemów. Może się zdarzyć, że ktoś oprócz podstawowych czcionek użyje w&nbsp;dokumencie czegoś bardziej egzotycznego.

Również w&nbsp;pliku z&nbsp;naszego przykładu jest taka sytuacja. Na stronie 20&nbsp;i 21&nbsp;znajdziemy wyśrodkowany fragment tekstu o&nbsp;robotach, napisany czcionką o&nbsp;nazwie *Eurostile*. W&nbsp;pasku jest zapisana kursywą, a&nbsp;zatem LibreOffice nie znajduje jej na dysku i&nbsp;trzeba ją zdobyć na własną rękę. Być może z&nbsp;nieco trudniej dostępnego źródła.

Kiedy w&nbsp;naszym dokumencie może czyhać więcej takich czcionek, przydałby się sposób na znalezienie ich wszystkich. I&nbsp;myślę że mam taki sposób (potraktowanie pliku DOCX jak archiwum, rozpakowanie go, dorwanie się do listy czcionek) -- ale pozwolę sobie to zostawić na osobny samouczek, który tu podlinkuję, kiedy będzie gotowy.

A póki co mam nadzieję, że łatwe rozwiązanie kwestii czcionek przekona część osób do Linuksa. To świat, w&nbsp;którym na start jest parę niedogodności, ale potem ma się całe spokojne życie na własnych warunkach :smile:

