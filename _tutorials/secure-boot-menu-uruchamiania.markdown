---
layout: page
title: "Linux z pendrive'a – jak obejść przeszkody"
description: "Jedyne wyboje na gładkiej drodze do Linuksa"
---

Proces uruchamiania systemów na bazie Linuksa jest o&nbsp;krok od bycia prostym i&nbsp;przyjemnym.

Zdobywanie programów, tworzenie nimi pendrive'ów instalacyjnych, zdobywanie Linuksów, zgrywanie na pendrive'y... Wszystko to zostało na przestrzeni lat naprawdę dopieszczone i&nbsp;uproszczone. Można swobodnie w&nbsp;to wciągać nowe osoby spoza światka nerdowskiego.

{:.post-meta .bigspace-after}
Ba! Istnieją nawet „imprezki instalacyjne”, podczas których można dostać gotowego, naszykowanego pendrive'a z&nbsp;Linuksem.

...Ale potem przychodzi ten moment, gdy trzeba wpiąć pendrive'a do portu USB i&nbsp;wybrać, że chce się włączyć zawarty na nim system.

Na tym etapie trzeba przywołać menu rozruchowe (ang. *boot menu*). Gdy już się je odkryje, wybierze pendrive'a i&nbsp;przejdzie dalej, mogą się pojawić groźnie brzmiące (choć bardzo na wyrost) komunikaty o&nbsp;naruszaniu bezpieczeństwa. Ich obejście wymaga wyłączenia pstryczka w&nbsp;jeszcze innym menu.

Co najgorsze: **na te różne menu nie ma jednego uniwersalnego sposobu**. Każdy producent tworzy je po swojemu.

Etap uruchamiania (czyli *bootowania*) to moim zdaniem największy, niepotrzebny wybój na początku fajnej przygody z&nbsp;Linuksem. Podzielę się tu paroma sposobami i&nbsp;przydatnymi źródłami, dzięki którym jak najmniej osób na tym wyboju podskoczy.

Wpis stworzyłem w&nbsp;domyśle jako uzupełnienie [samouczka dotyczącego Ventoya](/tutorials/ventoy){:.internal}, ale powinien odnosić się również do innych rodzajów pendrive'ów instalacyjnych.

## Spis treści

* [Ogólny opis sytuacji](#ogólny-opis-sytuacji)
* [Menu uruchamiania](#menu-uruchamiania)
* [Secure boot](#secure-boot)
* [Menu BIOS-u/UEFI](#menu-bios-uuefi)
  * [Wyłączanie secure boota](#wyłączanie-secure-boota)
  * [Inne możliwe problemy](#inne-możliwe-problemy)
* [Opisy dla konkretnych urządzeń](#opisy-dla-konkretnych-urządzeń)

## Ogólny opis sytuacji

Na drodze do ładowania systemu można zwykle natknąć się na **dwa ważne rodzaje menu**.

* Menu uruchamiania (rozruchu/*bootowania*)

  To lista możliwych sposobów na uruchomienie systemu. Chodzi mi tu o&nbsp;miejsce, w&nbsp;którym wybieram, że nie chcę ładować domyślnego systemu z&nbsp;dysku, tylko Linuksa z&nbsp;pendrive'a. 

* Menu BIOS-u/UEFI

  Można je nazwać umownie „menu płyty głównej” albo „menu przedsystemowym”.  
  W&nbsp;tym miejscu wyłącza się tryb *secure boota* (dosł. „bezpiecznego rozruchu”), jeśli stoi na drodze do załadowania alternatywnego systemu.  
  Czasami (rzadziej) trzeba też włączyć jakiś pstryczek, żeby w&nbsp;ogóle móc załadować system z&nbsp;pendrive'a.

Czasem mogą też istnieć jakieś menu nadrzędne, które pozwalają przejść do tego pierwszego albo drugiego.

W idealnym przypadku podczas zwykłego włączania komputera przez parę pierwszych sekund pojawia się informacja w&nbsp;stylu „naciśnij klawisz `Esc`, żeby włączyć menu” (w&nbsp;domyśle: takie ogólne i&nbsp;nadrzędne, z&nbsp;którego łatwo przejść do dwóch wyżej wymienionych).

Taki sposób byłby odkrywalny i&nbsp;przejrzysty dla użytkowników. Takie coś zapewniał m.in. stary HP EliteBook, którego miałem przyjemność wypróbować.  
Ale, niestety, nie jest to normą. Czasem trzeba poszukać w&nbsp;sieci, jak wyświetlić na konkretnym komputerze interesujące nas rodzaje menu. I&nbsp;właśnie taką wiedzę chcę zebrać, ułożyć i&nbsp;przystępnie zaserwować w&nbsp;tym wpisie.

{:.post-meta .bigspace-after}
Domyślnie celuję w&nbsp;osoby używające laptopów, a&nbsp;nie stacjonarnych składaków; stąd skupienie na markach producentów.

## Menu uruchamiania

Może wyglądać bardzo różnie w&nbsp;zależności od modelu i&nbsp;producenta, ale powinno sprowadzać się do względnie krótkiej listy dostępnych opcji. Pendrive instalacyjny powinien być na niej czymś ze słowem `USB` w&nbsp;nazwie.  
Niżej parę przykładów.

{:.bigspace-before}
<img src="/assets/tutorials/ventoy/boot-menu-2.jpg" alt="Przykładowe menu uruchamiania, zawierające trzy pozycje, w&nbsp;tym pamięć USB" width="50%"/>

{:.figcaption}
Z mojego doświadczenia -- ten sam pendrive (stworzony programem Ventoy) pojawił się na jednym komputerze pod nazwą `EFI USB Device`, na innym jako `USB Hard Drive`.

<img src="/assets/tutorials/ventoy/boot-menu-1.jpg" alt="Inne przykładowe menu uruchamiania, pokazujące pojedynczą pamięć USB jako dwie osobne pozycje na liście" />

{:.figcaption}
Źródło: [film z&nbsp;Youtube'a](https://www.youtube.com/watch?v=MIT3w-EPA9M) (8:26). Ktoś miał tu pendrive'a z&nbsp;Ventoyem, którego wykrywało jako dwie partycje, musiał wybrać właściwą.

Jak wyświetlić to menu? Wedle moich obserwacji: nieraz trzeba nacisnąć jakiś specjalny klawisz podczas uruchamiania komputera. Może to być na przykład `Esc`, `F2`, `F12`...

{:.post-meta .bigspace-after}
Jak wspomniałem wcześniej, niektóre laptopy wyświetlają ten skrót na ekranie podczas pierwszych sekund uruchamiania. Warto zachować czujność.

Obszerniejszą tabelę z&nbsp;klawiszami odpowiadającymi różnym producentom można znaleźć [na stronie systemu Tails OS](https://tails.net/doc/first_steps/start/pc/index.en.html#animation) (kilka akapitów poniżej podlinkowanej animacji).

W ogólnym przypadku można też poszukać w&nbsp;internecie pod hasłem `{model_komputera} boot menu`, jeśli zna się angielski. W&nbsp;tym języku powinno wyskoczyć znacznie więcej stron, zwykle wyjaśniających w&nbsp;paru linijkach, jaki przycisk prowadzi do menu.

<a id='ustalenie-modelu-komputera'/>
{% include details.html summary="A jak ustalić model komputera?" %}

{:.bigspace-before}
Czasem jest to wprost napisane na naklejce w&nbsp;okolicach klawiatury laptopa -- ale niektórzy ją odrywają.

Kolejna naklejka powinna być na spodniej części laptopa. Można stamtąd odczytać np. `Lenovo IdeaPad C340`. Producentem jest tu Lenovo, *IdeaPad C340* to model laptopa. Ta informacja przyda się do szukania wskazówek w&nbsp;sieci.

{% include details-end.html %}

{% include details.html summary="Przykład konkretny – Lenovo Legion" %}

W przypadku tego laptopa (pozwolę sobie nie podawać pełnej nazwy modelu) musiałem trzymać `F12`, naciskając przycisk uruchamiania. Menu uruchamiania pojawiało się chwilę po tym, jak zniknęło logo Lenovo.

Ale -- co bardzo istotne -- **musiałem nacisnąć klawisz odpowiednio wcześnie**. W&nbsp;innym wypadku menu się pojawiało, ale na liście nie było mojego pendrive'a instalacyjnego. W&nbsp;praktyce odkryłem, że pomaga przytrzymanie klawisza jeszcze *przed* wciśnięciem guzika zasilania.

Co jeszcze ważniejsze -- jeśli wszedłem w&nbsp;menu nadrzędne (otwierane igiełką; szczegóły w&nbsp;dalszej części) i&nbsp;próbowałem stamtąd przejść do menu uruchamiania, to *nigdy* nie wykrywało pendrive'a. Droga przez `F12` była jedyną słuszną. Wygląda mi to na mocne niedopatrzenie po stronie Lenovo.

{% include details-end.html %}

## Secure boot

Czasem menu uruchamiania to dopiero pierwszy krok. Niektórzy po wybraniu z&nbsp;niego pendrive'a stają przed groźnym niebieskim ekranem, mówiącym coś o&nbsp;blokadzie ze względów bezpieczeństwa.

{:.bigspace}
<img src="/assets/tutorials/ventoy/secure-boot-error.png" alt="Ekran z&nbsp;niebieskim tłem i&nbsp;komunikatem mówiącym o&nbsp;błędzie wynikającym z&nbsp;naruszenia bezpieczeństwa" width="80%"/>

...Ale spokojnie. To tylko *secure boot*. Z&nbsp;założenia zmora dla hakerów, w&nbsp;życiu codziennym przeszkadzajka dla alternatywnych systemów.

W tym miejscu pojawiają się dwie ścieżki. Albo spróbować tę blokadę udobruchać (jeśli mamy pendrive'a instalacyjnego stworzonego programem Ventoy), albo ją wyłączyć, choć tymczasowo. Osobiście jestem zwolennikiem drugiego rozwiązania, bo pierwsze jest niepewne. Ale omówię oba.

{% include details.html summary="Udobruchanie blokady (metoda od Ventoya)" %}

{:.post-meta .bigspace-after}
Informacje zaczerpnąłem z&nbsp;[przewodnika](https://www.ventoy.net/en/doc_secure.html) z&nbsp;oficjalnej strony Ventoya. Wszystko można obejrzeć w&nbsp;akcji [na YouTubie](https://www.youtube.com/watch?v=6YR8b2c95AY).

Przede wszystkim na etapie tworzenia pendrive'a należy mieć włączoną opcję wsparcia dla *secure boota* (domyślnie włączona, wystarczy nie ruszać).

Potem, kiedy wyświetli się informacja o&nbsp;zablokowaniu przez *secure boota*, to można spróbować go udobruchać, okazując mu swoiste poświadczenie zaufania. Trzeba, o&nbsp;ile się da:

* nacisnąć dowolny klawisz, żeby wejść w&nbsp;tryb *MOK Managera*,
* wybrać opcję `Enroll key from disk`,
* wybrać opcję *VTOYEFI* (nazwa jednej z&nbsp;partycji Ventoya),
* wybrać z&nbsp;listy plik `ENROLL_THIS_KEY_IN_MOKMANAGER`,
* potwierdzić (`Continue`, potem `Yes`),
* wybrać opcję `Reboot` i&nbsp;czekać na ponowne uruchomienie (oby do ekranu startowego Ventoya).

{% include details-end.html %}

Jeśli nie zdecydujemy się na metodę Ventoya (albo próbowaliśmy, ale nie działa), to można spróbować po prostu tego *secure boota* wyłączyć.

Ktoś może się zaniepokoić. Jak to, wyłączać coś, co ma *secure* („bezpieczne”) w&nbsp;nazwie?

No cóż, to tylko nazwa, a&nbsp;te bywają niedokładne. Również tu bliższe prawdzie byłoby „liniowe uruchamianie”. Chodzi w&nbsp;skrócie o&nbsp;niedopuszczanie anomalii. I&nbsp;choć mogą być nimi wirusy z&nbsp;dolnych warstw systemu, również alternatywne systemy są zaliczane do takich kategorii. Nawet najbezpieczniejsze Linuksy.

Żeby wyłączyć SB (takiego skrótu użyję :smiling_imp:), trzeba zwykle wejść w&nbsp;menu sterujące pierwotnymi funkcjami systemu. Na starszych komputerach zwie się to BIOS, na nowszych UEFI.

## Menu BIOS-u/UEFI

To ważne menu, które lubię nazywać „przedsystemowym”. Pozwala kontrolować najbardziej fundamentalne rzeczy związane z&nbsp;komputerem.

W najlepszym przypadku komputer sam podpowiada w&nbsp;pierwszych sekundach po włączeniu, jaki klawisz nacisnąć. Po naciśnięciu może się pojawić menu nadrzędne, zawierające np. pozycję `BIOS Menu` albo `UEFI Menu`. To tam należy przejść.

Jeśli nie ma żadnej podpowiedzi, to pozostaje poszukać w&nbsp;sieci pod hasłem `{model_komputera} bios menu`. Ogólnie: to menu bywa czasem trudniejsze do znalezienia niż menu uruchamiania z&nbsp;poprzedniej części wpisu.

{% include details.html summary="Przykład konkretny – Lenovo Legion" %}

W przypadku Legiona nie było (wedle mojej wiedzy) skrótu klawiszowego prowadzącego do tego menu.

Zamiast tego **trzeba było włożyć cienką igiełkę w&nbsp;otwór z&nbsp;boku obudowy**, nacisnąć nią ukryty tam przycisk i&nbsp;chwilę przytrzymać. W&nbsp;ten sposób otwierało się ukryte menu.

{:.post-meta}
Cała ta metoda w&nbsp;wewnętrznej terminologii Lenovo nosi nazwę Novo.

{% include details-end.html %}

### Wyłączanie secure boota

Po wejściu w&nbsp;BIOS/UEFI ma się zazwyczaj różne zakładki do dyspozycji. Można między nimi przechodzić, naciskając klawisze strzałek. Pstryczek odpowiedzialny za działanie SB mógłby się znaleźć na przykład w&nbsp;zakładce `Security`.

Pocieszę przynajmniej, że po odnalezieniu tej opcji jej wyłączenie bywa kwestią sekund: zaznaczenia i&nbsp;naciśnięcia klawisza *Enter*. Przejdzie w&nbsp;tryb wyłączony (ang. `Disabled` albo `Off`).  
Można teraz wyjść z&nbsp;BIOS-u/UEFI, zapisując po drodze zmiany. I&nbsp;spróbować ponownie uruchomić system z&nbsp;pendrive'a.

Poniżej przykład ważniejszych elementów menu UEFI na laptopie Lenovo Legion. Znalezienie wyłącznika SB jest łatwe -- należy natomiast **pamiętać o&nbsp;wybraniu opcji `Save and Exit`**, żeby zapisać wprowadzone zmiany.

{:.bigspace-before}
<img src="/assets/tutorials/ventoy/uefi-secure-boot-wylaczanie.png" alt="Kolaż pokazujący różne elementy interfejsu UEFI wiążące się z&nbsp;wyłączaniem trybu secure boot" width="100%"/>

{:.figcaption}
W tym przypadku menu w&nbsp;rogu podpowiada, że należy nacisnąć klawisz `F4`, żeby potwierdzić zmiany.

Przykłady innych możliwych wariantów tego menu i&nbsp;wyłączania przez nie SB można znaleźć na [filmie z&nbsp;kanału Britec](https://www.youtube.com/watch?v=-DKBynugBW8).

{% include details.html summary="Gdyby opcja wyłączenia Secure Boota była nieaktywna" %}

Niedawno pewien bloger opublikował [wpis na temat instalacji Linuksa](https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729) na laptopie Fujitsu Lifebook U729.

Ogólnie wykonywał te same kroki, które tu opisałem, ale po wejściu w&nbsp;menu BIOS-u nie działała opcja wyłączenia Secure Boota. Miała kolor szary i&nbsp;nie dało się jej zmieniać.

Autor musiał uruchomić Windowsa (który był domyślnym systemem na jego laptopie) i&nbsp;zaktualizować przez niego sterowniki od Fujitsu. Następnie uruchomił załączony program DeskUpdate, co zaktualizowało BIOS z&nbsp;wersji 2.17 do 2.31.  
W tej nowej wersji opcja wyłączania SB już była aktywna i&nbsp;zadziałała jak powinna.

Ogólnie, wychodząc poza przypadek konkretnego laptopa: BIOS/UEFI to normalny program, który można aktualizować. I&nbsp;warto się o&nbsp;to pokusić, gdyby coś nie działało.

{% include details-end.html %}

### Inne możliwe problemy

Czasem może się zdarzyć, że menu uruchamiania (przypomnę: to prostsze, z&nbsp;listą dostępnych urządzeń) wyświetla się prawidłowo, ale na liście nie ma naszego pendrive'a.

Może to wynikać z&nbsp;jakiejś niezgodności formatów. W&nbsp;przypadku programu Ventoy doradzam na przykład [spróbowanie paru alternatywnych opcji](/tutorials/ventoy#opcje-ventoya){:.internal} podczas tworzenia pendrive'a instalacyjnego.

Przyczyną problemu (rzadszą) może być również jakaś niekorzystna opcja włączona w&nbsp;menu BIOS-u/UEFI.

W takim wypadku warto w&nbsp;nie wejść i&nbsp;poszukać tam zakładki w&nbsp;stylu *boot options* albo *boot devices*. Może się zdarzyć, że opcja ładowania z&nbsp;pendrive'a jest całkiem wyłączona, a&nbsp;dopiero po jej włączeniu wszystko zacznie działać.

## Opisy dla konkretnych urządzeń

W tej części opiszę przypadki uruchamiania Linuksa na konkretnych urządzeniach, jakie miałem okazję pożyczyć. Może nie najmłodszych, ale sprawnych i&nbsp;wciąż będących w&nbsp;obiegu.  
Dla każdego z&nbsp;nich będzie komplet informacji zahaczających o&nbsp;kategorie z&nbsp;tego wpisu -- dostęp do różnych menu i&nbsp;wyłączanie *secure boota*.

{% include details.html summary="HP Elitebook 820" %}

Na tym komputerze istnieją wszystkie trzy rodzaje menu, jakie tu omówiłem: uruchamiania, BIOS-u i&nbsp;nadrzędne. Do każdego z&nbsp;nich można przejść zaraz po włączeniu laptopa, naciskając odpowiedni klawisz:

* `Esc`, żeby wejść do menu nadrzędnego;
* `F9`, żeby wejść do menu uruchamiania;
* `F10`, żeby wejść do menu BIOS-u.

Najlepiej najpierw nacisnąć wybrany klawisz i, cały czas go trzymając, nacisnąć raz przycisk uruchamiający komputer. Potem trzeba dociskać klawisz jeszcze parę sekund, aż logo HP na chwilę mignie, zniknie i&nbsp;pojawi się ponownie.

{:.post-meta .bigspace-after}
Gdybyśmy próbowali naciskać klawisz *po* przycisku zasilania i&nbsp;nie wstrzelilibyśmy się w&nbsp;wąskie okno czasowe -- to w&nbsp;dolnej części zacznie wirować kółko sygnalizujące ładowanie. Jeśli się pojawiło, to znaczy że jest już za późno i&nbsp;uruchomi się domyślny system.

**Menu nadrzędne** jest typowe i&nbsp;pozwala przejść m.in. do pozostałych dwóch. Nie widzę konieczności korzystania z&nbsp;niego w&nbsp;naszym przypadku.

**Menu uruchamiania** bardziej się przyda, ale pod względem działania również się nie wyróżnia. Po prostu lista, z&nbsp;której powinno się wybrać pendrive'a z&nbsp;Linuksem i&nbsp;potwierdzć klawiszem *Enter*.

Podobnie jak na wielu innych komputerach -- nie załadujemy systemu z&nbsp;pendrive'a, jeśli mamy włączony tryb *secure boot*. Żeby go wyłączyć, trzeba odwiedzić trzeci rodzaj menu, czyli **menu BIOS-u**.

Znajduje się tam kilka zakładek, widocznych u&nbsp;góry. Zaczynamy w&nbsp;opcjach podstawowych (`Main`). Zakładki można zmieniać strzałkami w&nbsp;lewo i&nbsp;prawo; opcję wyłączenia *secure boota* znajdziemy w&nbsp;opcjach zaawansowanych (`Advanced`).

Po wejściu w&nbsp;tę zakładkę należy:

* zaznaczyć (strzałkami w&nbsp;górę/dół) kategorię `Secure Boot Configuration` i&nbsp;potwierdzić klawiszem *Enter*;
* wewnątrz menu, które się otworzy -- zaznaczyć linijkę `Configure Legacy Support and Secure Boot`;
* *Enterem* i&nbsp;strzałkami zmienić wartość opcji na `Legacy Support Disable and Secure Boot Disable`.

Kiedy wyłączymy SB, należy wrócić do pierwszej zakładki, z&nbsp;ogólnymi ustawieniami, i&nbsp;wybrać tam opcję zapisania i&nbsp;wyjścia (`Save Changes and Exit`).

Zapewne pojawi się komunikat informujący, że wyłączyliśmy SB i&nbsp;że należy teraz przepisać wyświetlony kilkucyfrowy kod w&nbsp;celu akceptacji zmian. Przepisujemy, wciskamy *Enter*. Od teraz ładowanie przez pendrive'a powinno działać.

{:.post-meta .bigspace-after}
Nie wykluczam, że za pojawienie się prośby o&nbsp;przepisanie kodu odpowiada opcja `Physical Presence Interface`, którą też dałoby się wyłączyć w&nbsp;menu BIOS-u. Ale taka jednorazowa przeszkoda nie była dla mnie problemem, więc nie ingerowałem w&nbsp;jej działanie.

{% include details-end.html %}

Życzę owocnego uruchamiania Linuksa! Pokonanie jednego wyboju może dać spokój na całe lata :smile:

