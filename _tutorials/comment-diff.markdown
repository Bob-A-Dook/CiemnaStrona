---
layout: page
title: Praca ze skryptem Comdiff
description: "Skrypt Pythona pokaże nam to, co Facebook ukrył."
---

Oto instrukcja pracy z&nbsp;moim skryptem, dodanym jako bonus do wpisu [„Facebook i&nbsp;patologie automatycznej moderacji”]({% post_url 2022-12-19-facebook-komentarze-moderacja %}){:.internal}. Pozwala nam porównywać ze sobą komentarze spod tego samego posta na Facebooku, w&nbsp;widoku filtrowanym i&nbsp;niefiltrowanym.  
Jeśli znajdzie przykłady komentarzy ukrytych, to zapisuje porównanie w&nbsp;czytelnej formie do pliku.

{% include info.html
type="Słabości skryptu"
text="Skrypt jest prowizorką do użytku własnego, ma na razie sporo ograniczeń.  
Przede wszystkim **wymaga, żebyśmy odwiedzali stronę Facebooka przez przeglądarkę** i&nbsp;to stamtąd kopiowali posty. Musimy też **korzystać z&nbsp;polskiej lub angielskiej wersji** (bo skrypt znajduje niektóre rzeczy po tekście, zależnym od języka).  
Inne wady?  
Może nie działać na wszystkich wariantach postów z&nbsp;Facebooka, których jest niemało (Facebook mobilny, główny, uproszczony; posty na grupach, tablicy, cudzych stronach...).  
W zapisanym podsumowaniu nie będą się wyświetlały niektóre obrazy, takie jak miniaturki użytkowników. Możliwe też, że w&nbsp;kodzie HTML Facebook dodaje jakieś informacje, które pozwoliłyby zidentyfikować Wasze konto. Najlepiej nie udostępniać publicznie całego podsumowania."
%}

Czujcie się uprzedzeni :smile:

Jeśli macie pytania, wątpliwości lub uwagi o&nbsp;błędach, to piszcie na maila podanego w&nbsp;zakładce `O blogu`.

## Wymagania

Przede wszystkim potrzebujemy mojego skryptu. Można go pobrać <a class="internal" href="/assets/skrypty/comdiff.py" download>stąd</a>.

{% include info.html
type="Uwaga"
text="Wszystkie poniższe instrukcje dotyczą *komputerów*. Od biedy da się używać skryptu również na urządzeniach mobilnych, co opisuję pod koniec."
%}

Poza skryptem będziemy potrzebowali:

* Pythona

  Pobieramy go [z oficjalnej strony](https://www.python.org/downloads/) i&nbsp;łatwo instalujemy.   
  Na Windowsie podczas instalacji klikamy, że chcemy zainstalować wszystko, wraz z&nbsp;modułem `pip`, i&nbsp;dodać Pythona do zmiennych systemowych (ang. *Add to PATH*).

  Na niektórych odmianach systemu Linux powinien być domyślnie dołączony do systemu. Możliwe jednak, że nowszą wersję mamy pod nazwą `pip3`. W&nbsp;takim wypadku to ją wpisujemy zamiast `pip`.

* Bibliotek `lxml` oraz `BeautifulSoup`.

  Po zainstalowaniu Pythona otwieramy konsolę. W&nbsp;Windowsie to na przykład PowerShell albo Windows Terminal (znajdziemy w&nbsp;menu Start). Na Linuksie potrzebny program nazywa się *Terminal*.  
  Wpisujemy:

  <div class="black-bg mono">
  pip install lxml
  </div>

  **Uwaga**: W&nbsp;przypadku LXML-a na niektórych systemach może wyświetlić podczas instalacji komunikat o&nbsp;brakujących bibliotekach. Gdyby tak się stało, korzystamy z&nbsp;[instrukcji z&nbsp;ich strony](https://lxml.de/installation.html).  
  Następnie wpisujemy coś, co już powinno zadziałać szybko i&nbsp;prosto:

  <div class="black-bg mono">
  pip install beautifulsoup4
  </div>

I tyle powinno nam wystarczyć!

## Jak kopiować posty

Znaleźliśmy jakiegoś posta. Podejrzewamy, że część komentarzy pod nim jest ukryta. Co z&nbsp;nim teraz zrobić?

**Musimy zdobyć treść całego posta w&nbsp;formacie HTML**. Nie wystarczy zatem, że po prostu zaznaczymy to, co widzimy na ekranie, i&nbsp;to sobie skopiujemy. Trzeba się dobrać do kodu strony, a&nbsp;sposoby na to są różne.

### Narzędzia przeglądarki

Opcja domyślna, dostępna w&nbsp;każdej przeglądarce, ale nieco bardziej czasochłonna.  
Klikamy prawym przyciskiem myszy na interesujący nas post i&nbsp;wybieramy opcję `Zbadaj element`. Narzędzia same się otworzą.

{% include info.html
type="Porada"
text="Domyślnie narzędzia otwierają się u&nbsp;dołu przeglądarki. To dość nieporęczne, jest mało przestrzeni.  
Żeby to poprawić, możemy kliknąć ikonę w&nbsp;prawym górnym rogu ich okna i&nbsp;stamtąd wybrać, żeby od teraz otwierały się w&nbsp;innym widoku. Polecam otwieranie w&nbsp;osobnym oknie. Nie dość że więcej miejsca, to jeszcze strona nie wykryje, że jakieś narzędzia otwieramy."
%}

Teraz przesuwamy kursorem po linijkach kodu, a&nbsp;na stronie Facebooka kolorem będą zaznaczały się elementy, którym dany kod odpowiada. Zależy nam na tym, żeby objąć jeden post, ale nic więcej.

{:.bigspace}
<img src="/assets/tutorials/comdiff/browser-devtools-zaznaczanie.jpg" alt="Zrzut ekranu pokazujący zaznaczony na niebiesko fragment posta na Facebooku, na temat otwartych alternatyw dla programów graficznych. Pod spodem widzimy zaznaczoną linijkę z narzędzi przeglądarki odpowiadającą temu postowi">

Post powinien być elementem z&nbsp;paroma atrybutami zaczynającymi się od `aria-` oraz jednym `role="article"`. Ale gwarancji nie mamy, bo czasem Facebook serwuje nieco inną wersję strony.

Gdy już znajdziemy odpowiedni element, klikamy prawym przyciskiem myszy odpowiednią linijkę kodu i&nbsp;wybieramy `Kopiuj zewnętrzny HTMl`. I&nbsp;już, post jest w&nbsp;naszym schowku.

### SelSword

Każdorazowe, powtarzalne otwieranie narzędzi i&nbsp;zaznaczanie kodu może być uciążliwe. Zwłaszcza jeśli komentarzy jest wiele, a&nbsp;przeglądarka zacznie nam mulić.

Dlatego stworzyłem dodatek ułatwiający pracę, [SelSword](https://github.com/Bob-A-Dook/SelSword){:.internal}. Nie jest dostępny w&nbsp;oficjalnej bazie dodatków przeglądarkowych, ale możemy łatwo go zainstalować ręcznie (instrukcja w&nbsp;linku z&nbsp;poprzedniego zdania).

Kiedy mamy SelSworda w&nbsp;przeglądarce, **wystarczy dwukrotnie kliknąć tekst posta**. Tego nadrzędnego, nie komentarzy. Powinien otoczyć się czerwoną ramką. To znaczy, że do naszego schowka trafiła jego treść.

## Praca ze skryptem

Kiedy już wiemy jak kopiować posty, to praca ze skryptem jest prosta.

Najpierw go uruchamiamy. Sposób jest obojętny -- można przez domyślny edytor IDLE, można podwójnym kliknięciem, można przez konsolę.

{:.figure .bigspace}
<img src="/assets/tutorials/comdiff/comdiff-okno.jpg" alt="Okno pokazujące czarną konsolę i tekst widoczny po uruchomieniu skryptu Comdiff, informujący o&nbsp;dostępnych opcjach oraz proszący o&nbsp;skopiowanie kodu HTML z&nbsp;Facebooka"/>

Potem znajdujemy na stronie Facebooka interesujący nas post. Żeby nie umknęły nam żadne komentarze, **musimy niestety rozwinąć wszystko ręcznie**. Mój dodatek nie zrobi tego za nas.  

{% include info.html
type="Porada"
text="Na pocieszenie powiem, że kiedy zbieramy komentarze w&nbsp;trybie `Najpopularniejsze`, to nie musimy rozwijać każdego z&nbsp;nich (czyli klikać w&nbsp;pogrubione *Zobacz więcej* na końcu tekstu). **Wystarczy, że takie pełne rozwijanie zrobimy raz**, w&nbsp;widoku `Wszystkie`.  
Skrypt już pozna po linkach, kiedy ma dwie wersje tego samego komentarza, i&nbsp;zawsze wybierze tę rozwiniętą.  
Poza tym warto wybierać post już nieco starszy, do którego nie są na bieżąco dodawane nowe komentarze. Gdyby ktoś dodał coś nowego w&nbsp;czasie kiedy przełączamy się między widokami, to podsumowanie od skryptu nie będzie wiarygodne."
%}

Najpierw rozwijamy tylko listę komentarzy. Potem kopiujemy *cały post*, metodą opisaną wyżej. Otwieramy konsolę z&nbsp;naszym skryptem i&nbsp;naciskamy `Enter`. Skrypt da znać, że skopiował komentarze i&nbsp;czeka na pełną wersję posta.

W tym momencie warto porównać liczbę komentarzy skopiowanych z&nbsp;liczbą wszystkich, umieszczoną przez Facebooka pod postem. **Jeśli jest ich tyle samo, to nie ma sensu rozwijać w&nbsp;nowym widoku**. Facebook niczego nie schował.

Jeśli liczby wskazują, że coś zostało ukryte, to zmieniamy widoczność komentarzy na `Wszystkie`. Znów rozwijamy, tym razem nawet treść poszczególnych komentarzy. Kiedy skończymy, ponownie kopiujemy post.

{:.post-meta .bigspace-after}
Jeśli używamy SelSworda, to po podwójnym kliknięciu posta, który już ma czerwoną ramkę, nie pojawi się nic nowego; ale bez obaw, wszystko działa.

Wracamy do konsoli z&nbsp;naszym skryptem i&nbsp;naciskamy `Enter`. Powinna się wyświetlić informacja o&nbsp;liczbie komentarzy ocenzurowanych, a&nbsp;plik z&nbsp;podsumowaniem trafi do podfolderu `Documents/cenzura` w&nbsp;naszym folderze głównym.

I jeszcze jedna sprawa -- co, jeśli liczba komentarzy w&nbsp;trybie `Wszystkie` nadal jest mniejsza od liczby podawanej przez Facebooka?  
Oznacza to, że brakujące komentarze zostały usunięte definitywnie. Może przez samych autorów, może przez Fejsa.

### Dodatkowe informacje

Na każdym etapie możemy nacisnąć `Q` i&nbsp;`Enter`, żeby opuścić program.

Jeśli na którymś etapie coś sknocimy -- na przykład nie rozwiniemy wszystkich komentarzy, choć chcieliśmy -- to można nacisnąć `Z` i&nbsp;`Enter`, żeby wrócić do poprzedniego etapu. Wtedy po prostu rozwijamy co trzeba i&nbsp;kopiujemy post jeszcze raz.

Poza tym skrypt daje możliwość porównywania plików znajdujących się na dysku. Nie znalazłem zastosowania dla tej opcji, ale może się przydać, gdybyśmy mieli pomocników umiejących kopiować, ale nie lubiących konsoli.

W tym umieszczamy w&nbsp;jednym folderze dwa pliki z&nbsp;roszerzeniem *html* (ważne). Jeden z&nbsp;postem zawierającym wszystkie komentarze, drugi z&nbsp;tym samym postem i&nbsp;schowanymi komentarzami.  
Następnie uruchamiamy skrypt w&nbsp;tym samym folderze i&nbsp;naciskamy w&nbsp;interaktywnym trybie klawisze `F` oraz `Enter`.

Udanego łapania Facebooka na cenzurze! :smile:  
A gdyby ktoś chciał robić to nawet na telefonie i&nbsp;nie bał się konsoli, to zapraszam do dalszego czytania.

## Praca na telefonie

*Comdiff* powinien działać również na telefonach z&nbsp;systemem Android, jeśli użyjemy go przez aplikację Termux. **Problemem jest przeglądarka, bo prawie żadna mobilna nie pozwala dorwać źródła strony**. Dlatego musimy użyć jednej z&nbsp;nielicznych. W&nbsp;moim przykładzie będzie to Kiwi Browser.

{% include info.html
type="Uwaga"
text="Jeśli chcemy zdziałać na telefonie cokolwiek sensownego, trzeba zaznaczyć w&nbsp;przeglądarce (którą siłą rzeczy będzie Kiwi Browser) opcję `Wersja na komputery` (ang. *Desktop site*).  
Dlaczego? Bo w&nbsp;wersjach przeznaczonych dla urządzeń mobilnych, czyli *m.facebook.com* oraz *mbasic.facebook.com* nie jesteśmy w&nbsp;stanie w&nbsp;pełni rozwinąć komentarzy wraz z&nbsp;odpowiedziami."
%}

1. Pobieramy aplikację [F-Droid](https://f-droid.org/).
2. Przez F-Droida instalujemy apki `Termux` oraz `Termux:API`.

   To ważne! Bez tej drugiej apki nie zyskamy dostępu do schowka. Z&nbsp;kolei wersja Termuxa dostępna w&nbsp;domyślnej androidowej bazie, PlayStore, jest nieco okaleczona przez Google.  
   Termux powinien też dostać pozwolenie na dostęp do systemu plików, żebyśmy mogli mu podrzucić nasz skrypt.

3. Otwieramy Termuksa, instalujemy Pythona oraz moduły potrzebne mojemu skryptowi.

   Uprzedzam, że po drodze jest parę niuansów, których nie było przy poprzednich wynalazkach z&nbsp;bloga. Głównie przez fakt, że instalujemy bibliotekę `lxml`, i&nbsp;to na telefonie. Dokładne instrukcje dotyczące instalacji i&nbsp;rozwiązywania problemów [znajdziemy w&nbsp;samouczku dotyczącym Termuksa](/tutorials/termux#lxml){:.internal}.

4. Pobieramy przeglądarkę [Kiwi Browser](https://kiwibrowser.com/) i&nbsp;instalujemy w&nbsp;niej dodatek `SelSword`, opisany wyżej.

    Jak wspomniałem, jest jedną z&nbsp;niewielu pozwalających instalować dodatki. Oprócz tego daje dostęp do narzędzi przeglądarki, ale są niestety dość nieporęczne, więc dodatek wciąż raczej się przyda.

   {:.post-meta .bigspace-after}
   Jeśli nie działa nam Google Play, bo na przykład korzystamy z&nbsp;telefonu Huawei, to znajdujemy Kiwi w&nbsp;jakiejś innej bazie, jak *APK Pure*.

5. Pobieramy mój skrypt i&nbsp;kopiujemy go do folderu Termuksa.

   Jeśli pobraliśmy skrypt przez przeglądarkę, z&nbsp;mojej strony, to powinien trafić do folderu `Downloads`. Zatem powinna zadziałać komenda:

   <div class="black-bg mono">cp /storage/emulated/0/Download/comdiff.py ~</div>

   Pamiętajmy o&nbsp;spacjach! Dla pewności można skopiować całość stąd.  
   Uprzedzam jednak, że nie wiem czy ścieżka będzie taka sama na wszystkich wersjach Androida.

**Gotowe**! Było tych kroków niemało, ale wszystkie na szczęście sprowadzają się do prostej klikaniny.

Od teraz, kiedy przeglądamy stronę Facebooka przez Kiwi Browser -- wersję komputerową, przypomnę -- możemy dwukrotnie nacisnąć palcem na post. Pojawi się wokół niego ramka. Włączamy Termuksa, wpisujemy:

<div class="black-bg mono">python comdiff.py</div>

I naciskamy klawisz potwierdzający. Skrypt powinien działać jak na komputerze, tyle że będzie zapisywał podsumowania ukrytych komentarzy do folderu Termuksa, niewidocznego dla innych aplikacji.

Gdy będziemy chcieli upublicznić folder z&nbsp;nimi, możemy wpisać:

<div class="black-bg mono">cp Documents/cenzura /data/storage/emulated/0</div>

Powinien trafić do głównego publicznego folderu naszego telefonu. A&nbsp;stamtąd możemy go wysłać gdziekolwiek chcemy; czy to przez Bluetooth, czy to przez USB na komputer.

