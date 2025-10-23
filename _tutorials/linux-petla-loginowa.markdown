---
layout: page
title: "Co zrobić, gdy Linux nie wpuszcza poza ekran logowania?" 
description: "Długo zwlekałem, ale kiedyś trzeba było posprzątać graty."
---

Oto kolejny krótki wpis, w&nbsp;którym opisuję przeszkadzajkę, na jaką trafiłem przez lata korzystania z&nbsp;systemu Linux Mint. A&nbsp;także sposób na poradzenie sobie z&nbsp;nią.

Mam nadzieję, że takie wpisy pokażą, że wiele problemów na Linuksie jest łatwych do rozwiązania i&nbsp;nieraz nie wynikają one nawet z&nbsp;winy systemu.

Tym razem będzie o&nbsp;**niemożności zalogowania się przez brak miejsca na dysku**.  
Co zrobić, jeśli po wpisaniu hasła na ekranie startowym nasz Linux się nie uruchamia? Czasem wystarczy wejść w&nbsp;awaryjną konsolę i&nbsp;usunąć trochę dzienników systemowych.

A jak? Już piszę.

## Opis problemu

Uruchamiam komputer, na którego dysku zainstalowałem kiedyś zaufany system Linux Mint. Wpisuję swoje hasło, jak to już setki razy robiłem.  
Ekran ciemnieje, a&nbsp;wzrok odruchowo czeka, aż pojawi się tapeta ekranu głównego.

...Ale ta się nie pojawia. Zamiast niej znów wyświetla się ekran logowania.  
Chwila konsternacji. Czyżbym źle wpisał hasło? Próbuję ponownie, i&nbsp;jeszcze raz.

Ale za każdym razem wracam do tego samego ekranu logowania. Jakbym grał w&nbsp;Dniu Świstaka. Pojawia się strach. Czy właśnie straciłem dostęp do całej zawartości swojego systemu?

{:.bigspace-before}
<img src="/assets/tutorials/linux-petla-loginowa/linux-petla-loginowa.jpg" alt="Zrzut ekranu pokazujący pole na hasło użytkownika na ekranie logowania. Obok znajduje się strzałka prowadząca od pola z&nbsp;powrotem ku niemu."/>

{:.figcaption}
Źródło: [losowy filmik](https://www.youtube.com/watch?v=bUxpTtZELkw), okrągła [strzałka](https://www.flaticon.com/free-icon/arrow_14720107) z&nbsp;serwisu *Flaticon* (autor: *onlyhasbi*). Przeróbki moje.

Witajcie w&nbsp;piekle **pętli logowania** (albo loginowej; ang. *login loop*) :smiling_imp: 

{:.post-meta .bigspace-after}
Albo czyśćcu, skoro to swoista poczekalnia przed głównym systemem.

## Przyczyną dawne podziały

Pętla logowania (cytując [tę odpowiedź z&nbsp;forum Minta](https://forums.linuxmint.com/viewtopic.php?p=1769597#p1769597)) może mieć dwie główne przyczyny:

* brak miejsca na pliki na partycji systemowej  
  (czyli tej części dysku twardego, na której tkwią pliki wewnętrzne systemu),
* błędy w&nbsp;ważniejszych plikach środowiska graficznego.

{:.post-meta .bigspace-after}
Mogą też istnieć jakieś inne, bardziej egzotyczne przyczyny. Osobiście słyszałem o&nbsp;dwóch wyżej wymienionych, zetknąłem się tylko z&nbsp;pierwszą.

W moim przypadku przyczyna sięgała daleko wstecz. Czasów, kiedy instalowałem Linuksa na komputerze. Czytałem wtedy różne fora i&nbsp;znalazłem poradę mówiącą, żeby wydzielić sobie **dwie partycje -- mniejszą na system, większą na pliki użytkownika**.

Bo widzicie -- na Linuksie istnieje tak zwany folder domowy, `/home` (oznaczany czasem tyldą, `~`). To miejsce, w&nbsp;którym zwykle zapisuje się pliki użytkownika.  
Dokumenty, zdjęcia, muzykę... A&nbsp;także zmienne ustawienia zainstalowanych programów, [pamięć podręczną](/2021/12/23/caching){:.internal} Firefoksa. I&nbsp;wiele innych rzeczy związanych z&nbsp;codziennym korzystaniem z&nbsp;komputera.

Czasem warto zaktualizować Linuksa do nowej wersji. A&nbsp;to, przynajmniej przy większych aktualizacjach, wymaga kompletnego wyczyszczenia partycji, na której znajdują się pliki systemowe.

Przenosząc folder domowy w&nbsp;osobne miejsce (a&nbsp;tym są właśnie partycje dysku), ukrywam go przed efektami „bombardowania” plików systemowych podczas większych aktualizacji. Zachowuję wszystkie obrazy, dokumenty itd., a&nbsp;zmieniam jedynie system, który tym wszystkim zarządza.

{% include info.html
type="Analogia"
text="Folder `/home` jest tutaj jak książki i&nbsp;inne multimedia zebrane w&nbsp;bibliotece. Mogą trwać niezmiennie przez dziesiątki lat.  
I obojętne są im kolejne, motywowane politycznie, zmiany składu dyrektorskiego w&nbsp;różnych gabinetach (`/bin`, `/etc`...) w&nbsp;drugim skrzydle budynku."
%}

Idąc za tą radą, stworzyłem sobie partycję na pliki systemowe o&nbsp;rozmiarze 20&nbsp;GB. Resztę (poza jakimśtam *swapem* i&nbsp;mniejszymi partycjami) poświęciłem na swój folder `/home`.

## Ciemne strony dwóch partycji

Podział na dwie części przebiegł z&nbsp;początku bezboleśnie.  
Podczas codziennego użytkowania system wydawał się jednością i&nbsp;nie było widać, że gdzieś pod spodem jest rozdzielony na dwa miejsca.

Tyle że przez lata instalowałem różne programy.  
Czasem większe, jak programy od uczenia maszynowego (obecnie nazywanego marketingowo AI). Czasem wpisywałem przed jakimś poleceniem instalacyjnym `sudo`, co prowadziło do instalacji programów między systemowymi (nawet jeśli dało się trzymać folderu użytkownika).

Do tego dochodziły dzienniki systemowe, w&nbsp;których konsekwentnie przybywało informacji.

...I tak oto doprowadziłem do tego, że moje 20&nbsp;GB zostało po prostu wypełnione po brzegi. **Partycja jest czymś stałym i&nbsp;sama się nie rozszerzy**. Brakło miejsca.

{:.bigspace-before}
<img src="/assets/tutorials/linux-petla-loginowa/gparted-partycja-root-pelna.png" alt="Przerobiony zrzut ekranu pokazujący dwie partycje jako prostokąty obok siebie, mniejszy i&nbsp;większy. Mniejszy, podpisany znakiem ukośnika, ma czerwone tło i&nbsp;zawiera kilka rzędów wykrzykników"/>

{:.figcaption}
Źródło: informacje z&nbsp;programu *Gparted* od kontrolowania partycji. Przeróbki moje.

Zakładam, że podczas logowania system musi cośtam stworzyć w&nbsp;swoim wewnętrznym folderze. A&nbsp;nie stworzy niczego, ani bajta, bo miejsce się wyczerpało. A&nbsp;zatem -- wyskakuje błąd i&nbsp;wyrzuca mnie z&nbsp;powrotem do ekranu logowania.

## Rozwiązanie doraźne

Nie mogłem dłużej uciekać od problemu i&nbsp;musiałem oczyścić tę swoją 20-gigabajtową, zagraconą stajnię Augiasza.

Będąc w&nbsp;oknie logowania, mogłem nacisnąć kombinację `Ctrl+Alt+F2`, uruchamiającą konsolę awaryjną.

{:.post-meta .bigspace-after}
Wspomnienie podpowiada, że kiedyś była to kombinacja `Ctrl+Alt+F1`. Ale mogła się zmienić.

Następnie musiałem wpisać nazwę użytkownika i&nbsp;hasło.  
Nazwa to zwykle to, co jest widoczne na ekranie logowania, nad polem tekstowym. Z&nbsp;kolei hasło jest tym samym, które bym w&nbsp;to pole wprowadził.

{:.post-meta .bigspace-after}
**Jeśli podczas wpisywania nie wyświetlają się znaki -- nie szkodzi**. Należy po prostu wpisać swoje i&nbsp;nacisnąć *Enter*.

Włączyła się konsola, w&nbsp;którą mogłem wpisywać tradycyjne polecenia i&nbsp;na przykład usunąć w&nbsp;ten sposób niepotrzebne pliki. W&nbsp;moim przypadku postawiłem na wyczyszczenie dzienników systemowych:

```
journalctl --vacuum-size=5M
```

W ten sposób usunąłem wszystkie logi za wyjątkiem ostatnich 5&nbsp;megabajtów -- liczba dowolna, można zmienić wedle uznania.  
Wyświetliło informację o&nbsp;usunięciu *ponad 500&nbsp;MB logów*. Nieźle, teraz zdecydowanie miałem więcej miejsca!

Użyłem kombinacji `Ctrl+Alt+F7`, żeby wrócić do ekranu logowania.

{:.post-meta .bigspace-after}
Na podlinkowanym wcześniej forum Minta piszą, że jeśli ta nie działa, to można spróbować `Ctrl+Alt+F8`.

Wpisanie hasła. Wdech, wydech. Przycisk potwierdzający.  
Chwila czekania... I&nbsp;ulga. Oto pojawił się znajomy pulpit oraz ikony. Odzyskałem swój komputer.

## Na przyszłość

Osoby, które dopiero wchodzą w&nbsp;świat Linuksa, mogą po prostu **wybrać podczas instalowania opcję domyślną i&nbsp;nie ustawiać żadnych partycji ręcznie**.

{:.post-meta .bigspace-after}
Pomijam tu przypadku nietypowe, np. instalacji na dysku zewnętrznym, gdy jednak trzeba wprost wskazać partycje. Mówię o&nbsp;klasycznym oddaniu dysku komputera Linuksowi na wyłączność.

Przy tej opcji zarówno pliki systemowe, jak i&nbsp;pliki użytkownika zostaną zapisane na jednej wspólnej partycji. W&nbsp;ten sposób powinno być łatwiej kontrolować ilość miejsca, jaka jeszcze pozostała na dysku.

I owszem, zmusza to do odrobinę większej pracy przy aktualizacjach -- ale nie wszystkich. Od jakiegoś czasu Linux Mint [ułatwia drobniejsze aktualizacje](https://blog.linuxmint.com/?p=4629) (np. z&nbsp;22.1 na 22.2) i&nbsp;są kwestią minut.

Osobna partycja na folder `/home` nie niesie za sobą już takich korzyści jak kiedyś. Można się po prostu nastawić na ciut więcej pracy co kilka lat, przy aktualizacji do większej wersji (np. z&nbsp;22.x na 23.x):

* zgrać sobie pliki z&nbsp;folderu `/home` w&nbsp;bezpieczne miejsce, np. na jakiś dysk zewnętrzny;
* „odpalić atomówkę” i&nbsp;wyczyścić całą wspólną partycję podczas wgrania nowszej wersji Linuksa;
* zgrać pliki z&nbsp;dysku zewnętrznego z&nbsp;powrotem do (nowego, pustego) folderu `/home`.
  
  {:.post-meta .bigspace-after}
  Dygresja: czasem jednak warto robić pewien przesiew plików z&nbsp;folderu `/home`, zwłaszcza tych z&nbsp;podfolderu `.config`. Może przykładowo zapisane tam ustawienia Firefoksa już nie do końca pasują do jego nowszej wersji, zawartej w&nbsp;świeżo zaktualizowanym Mincie?

I to tyle. Mam nadzieję, że porady z&nbsp;tego wpisu pozwolą wszystkim czytającym osobom nieco oswoić się z&nbsp;problemem pętli logowania.

Znacznej większości osób nie dotknie on w&nbsp;ogóle, ale jeśli już dotknie -- rozwiązanie bywa proste. Taka cecha otwartego Linuksa :smile:

