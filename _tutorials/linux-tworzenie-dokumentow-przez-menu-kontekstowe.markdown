---
layout: page
title: "Linux, szablony i tworzenie plików przez menu kontekstowe (jak na Windowsie)"
description: "Ludzie przesiadający się z Windowsa poczują się jak u siebie. Po paru zmianach."
---

W tym roku wygasa wsparcie dla systemu Windows 10&nbsp;i już raczej nie będzie od tego ucieczki.  
Ale co zrobić, kiedy Windows 11&nbsp;jest jak pole minowe (jeśli w&nbsp;ogóle zadziała), a&nbsp;zostając przy dziesiątce, straci się aktualizacje zabezpieczeń?

Odpowiedź -- to [niepowtarzalny moment, żeby spróbować darmowego Linuksa](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}.

Nie mówię, że każdemu podpasuje. Ale można przynajmniej wykonać ten jeden drobny, zapoznawczy krok. Rozważyć przepiłowanie sznura, który przez kawał życia nas wiązał do Windowsa.  
Świat Linuksa na starcie może wydawać się obcy... Ale jest grono entuzjastów, takich jak ja, którzy chętnie pomogą przy przesiadce.

Moja pierwsza porada -- na początek warto sprawdzić system **Linux Mint**. Jest dopracowany i&nbsp;bardzo zbliżony działaniem do Windowsa.

Mimo wszystkich zalet istnieją jednak pewne różnice, które mogą utrudnić życie ludziom przechodzącym z&nbsp;Windowsa na Linuksa. Mam tu na myśli w&nbsp;szczególności osoby wykonujące prace biurowe, przyzwyczajone do obsługi komputera z&nbsp;użyciem myszy.

Skupię się tu na jednej z&nbsp;takich różnic, dotyczącej **tworzenia nowych plików przez menu kontekstowe**.  
Zapraszam!

## Wprowadzenie

Jeśli kliknie się na Windowsie 10&nbsp;jakiś kawałek pustej przestrzeni prawym przyciskiem myszy, to wyświetli się **menu kontekstowe**.

{:.post-meta .bigspace-after}
Dotyczy to klikania i na pulpicie, i wewnątrz Eksploratora (przeglądarki plików).

To menu to lista dostępnych opcji. Jedna z nich nazywa się `Nowy`.  
Jeśli się ją wybierze, to rozwinie się lista kilku rodzajów plików, jakie można stworzyć w&nbsp;danym miejscu. Oto menu z&nbsp;Windowsa 10:

{:.bigspace-before}
<img src="/assets/tutorials/linux/menu-kontekstowe/menu-kontekstowe-windows-tworzenie-dokumentow.png" alt="Zrzut ekranu pokazujący fragment menu kontekstowego z&nbsp;Windowsa 10&nbsp;i opcję stworzenia różnych rodzajów pliku: tekstowego, mapy bitowej, archiwum ZIP oraz dokumentu programu Word"/>

{:.figcaption}
Widok z&nbsp;menu na świeżo zainstalowanym Windowsie, do którego dodałem właściwie tylko starego Worda, bez spolszczenia. Stąd angielska nazwa dokumentu.

Na Mincie takie menu również istnieje, ale na początku ma jedynie opcję tworzenia prostych plików tekstowych. Mimo że domyślnie jest zainstalowany pakiet biurowy LibreOffice, nie widać opcji tworzenia dokumentów.

{:.bigspace-before}
<img src="/assets/tutorials/linux/menu-kontekstowe/mint-cinnamon-menu-kontekstowe-tworzenie-plikow.png" alt="Zrzut ekranu pokazujący fragment menu kontekstowego na systemie Mint Cinnamon. Widać opcję stworzenia pliku tekstowego oraz szary tekst informujący o&nbsp;braku szablonów" />

{:.figcaption}
W tym wpisie przykłady z&nbsp;Minta są po angielsku. Ale ogólnie [ustawienie języka polskiego](/tutorials/linux-mint-jezyk-polski-system.html){:.internal} jest na tym systemie łatwe i&nbsp;przyjemne.

Obstawiam, że brak opcji tworzenia dokumentów w&nbsp;dowolnym miejscu może na początku razić użytkowników Worda i&nbsp;Windowsa. Na szczęście na Mincie można bardzo łatwo zyskać taką opcję.

{% include details.html summary="Ciekawostka o tworzeniu plików na innych Linuksach" %}

{:.bigspace-before}
Kiedy ostatnio sprawdzałem, opcji tworzenia plików przez menu **w ogóle nie było na Ubuntu i&nbsp;Fedorze**, dwóch bardzo popularnych Linuksach (a&nbsp;przynajmniej na ich domyślnych wariantach).

Dlaczego? Bo te wersje opierają się na tak zwanym *środowisku Gnome*. Które może i&nbsp;ładnie wygląda, ale ma bardziej „smartfoniaste” zasady działania i&nbsp;może odstraszyć ludzi migrujących z&nbsp;Windowsa.  
Dlatego osobiście polecam na początek przygody Linuksy „odgnomione”. Nie tylko Minta, choć jego w&nbsp;szczególności.

{% include details-end.html %}

## Szablony na ratunek

Przeglądarka plików na Mincie powinna po uruchomieniu domyślnie pokazywać zawartość *folderu domowego*.

W nim zaś powinien być folder o&nbsp;nazwie `Szablony` (w&nbsp;wersji angielskiej `Templates`). **Po wrzuceniu dowolnych plików do tego folderu, staną się one dostępne przez menu kontekstowe**.

Załóżmy na przykład, że chcę mieć możliwość tworzenia przez menu odpowiednika dokumentów Worda.

W tym celu uruchamiam program LibreOffice Writer, domyślnie dostępny na Mincie. Wyświetli się pusty dokument.  
Mogę go od razu zapisać (w&nbsp;górnym menu opcja `Plik`, potem `Zapisz jako`; można też użyć skrótu klawiszowego `Ctrl+Shift+S`).

Wyświetli się okno z&nbsp;pytaniem o&nbsp;nazwę, rodzaj i lokalizację nowego pliku:

* lokalizacja -- kliknąłem w&nbsp;folder domowy, a&nbsp;następnie w&nbsp;folder `Szablony`;
* nazwa -- obojętna, ale warto dać jakąś zrozumiałą, bo będzie się wyświetlała w&nbsp;menu;
* typ -- wybrałem z&nbsp;rozwijanego menu na dole dokument LibreOffice.

  {:.post-meta .bigspace-after}
  Gdybym chciał, mógłbym również wybrać DOCX i&nbsp;nazwać go dokumentem Worda. Jeśli jednak mam możliwość wyboru, to wolę format własny LibreOffice'a.

<img src="/assets/tutorials/linux/menu-kontekstowe/linux-mint-zapis-dokumentu-w-szablonach.png" alt="Zrzut ekranu pokazujący różne fragmenty okna zapisywania dokumentu przez program LibreOffice"/>

{:.bigspace}
...I to tyle! Po zapisaniu pliku w szablonach mogę tworzyć jego kopie poprzez menu, we wskazanych przez siebie miejscach.

{:.bigspace}
<img src="/assets/tutorials/linux/menu-kontekstowe/mint-cinnamon-menu-kontekstowe-z-szablonem-dokumentu.png" alt="Zrzut ekranu ze zmienionym menu kontekstowym z&nbsp;Minta, zawierającym opcję stworzenia dokumentu LibreOffice'a."/>

{% include info.html
type="Powiązane wpisy"
text="Skoro już jesteśmy przy tworzeniu dokumentów, to wspomnę o&nbsp;pewnej różnicy między programami LibreOffice a&nbsp;Microsoft Word, na której można się na początku przejechać.  
Mianowicie: na Linuksie (Mincie i&nbsp;nie tylko) nie ma domyślnie czcionek, z&nbsp;jakich korzystają codziennie użytkownicy Worda. Dokumenty mogą przez to wyglądać nieco inaczej. Brakujące podstawowe czcionki można na szczęście łatwo zdobyć, co [opisuję w tym wpisie](/tutorials/libre-office-czcionki-worda.html){:.internal}."
%}

W ten sposób sprawa tworzenia dokumentów z&nbsp;pakietu biurowego zostanie rozwiązana.

Ale nie jest to jeszcze pełna zgodność z&nbsp;menu Windowsa, bo ten pozwala tworzyć kilka innych rodzajów pustych plików -- jak archiwa ZIP czy obrazki w&nbsp;formacie BMP.

Z tymi plikami wiąże się parę drobnych pułapek, które też tutaj przybliżę.

## Niuanse związane z&nbsp;tworzeniem pustych plików

Gdyby wybrać z&nbsp;menu Windowsa opcję stworzenia archiwum ZIP, to taki nowopowstały plik można od razu kliknąć, wyświetlając (pustą) listę jego zawartości. Plik jest całkiem pusty; według podglądu ma rozmiar 0&nbsp;bajtów.

Ktoś mógłby pomyśleć, że na Linuksie też stworzy sobie w&nbsp;folderze na szablony nowy, pusty plik i&nbsp;nazwie go `Nowy folder skompresowany (zip)`. I&nbsp;będzie jak na Windowsie.

Taki plik jak najbardziej trafi do menu kontekstowego. Po wybraniu z&nbsp;menu zostanie stworzony.  
Ale jeśli się go kliknie, to uruchomi się zapewne... w&nbsp;notatniku. Nie w&nbsp;programie od archiwów.

Ta różnica wynika z&nbsp;innego mechanizmu działania obu systemów -- **Windows rozróżnia pliki po końcówkach, dla Linuksa często są one mniej istotne niż zawartość**.

A kiedy żadnej zawartości nie ma, to wiele odmian Linuksa klasyfikuje plik jako osobny typ, dosłownie „pusty plik”. Niezależnie od jego nazwy czy końcówki po kropce.

{:.post-meta .bigspace-after}
Nie wykluczam, że niektóre Linuksy zachowują się inaczej, albo że dałoby się to zachowanie zmienić jakimś dodatkiem. Ale w&nbsp;przypadku środowisk MATE i&nbsp;Cinnamon jest właśnie tak jak piszę.  
Gdyby ktoś chciał dać nura w&nbsp;temat, to można poczytać o&nbsp;typach MIME oraz rozpoznawaniu typu pliku po jego pierwszych bajtach.

To inne zachowanie niż na Windowsie. W&nbsp;jaki sposób można je zmienić? Służę paroma obejściami dla konkretnych rodzajów plików.

### Plik BMP

Na Windowsie plik BMP (mapa bitowa) liczy po stworzeniu przez menu 0&nbsp;bajtów. Po kliknięciu otwiera się w domyślnym programie graficznym, takim jak Paint, pokazując jednolitą biel. Jak płótno gotowe do zamalowania.

Na Linuksie ze wspomnianych względów nie stworzy się pliku o&nbsp;rozmiarze zerowym. Można jednak uruchomić wybrany program od grafiki, stworzyć obrazek zawierający tylko białe tło, a&nbsp;następnie zapisać go jako plik BMP w&nbsp;folderze na szablony.

Nie będzie pusty (ba, może być całkiem spory; ponad 5&nbsp;MB przy wymiarach 1920&nbsp;na&nbsp;1080 pikseli)... Ale tworzenie i&nbsp;otwieranie takich plików będzie działało w&nbsp;sposób intuicyjny dla użytkowników Windowsa.

### Archiwum ZIP

Podobny problem jak wyżej, z&nbsp;pustym plikiem otwierającym się w notatniku, pojawia się przy plikach ZIP. Tutaj również rozwiązaniem jest stworzenie w&nbsp;szablonach pliku jak najprostszego, ale nie całkiem pustego.

Program odpowiedzialny za pracę z&nbsp;archiwami ZIP, na Mincie i&nbsp;nie tylko, nazywa się **Engrampa**.  
Można go teoretycznie znaleźć w&nbsp;menu systemowym i&nbsp;wybrać opcję stworzenia nowego archiwum. Ale jeśli nie doda się żadnej zawartości, to żaden plik nie powstanie. Przynajmniej tak mi to działa obecnie, w&nbsp;wersji 1.28.2.

Można to jednak w&nbsp;prosty sposób obejść. Wystarczy podczas tworzenia archiwum wybrać *jakiekolwiek* pliki, które zostaną do niego dodane. Z&nbsp;ostrożności warto tam napchać jakieś bzdety, zamiast sięgać po coś z&nbsp;cenną zawartością. 

Następnie należy:

* odnaleźć stworzony plik ZIP w&nbsp;przeglądarce plików;
* otworzyć go w Engrampie dwukrotnym kliknięciem;
* kliknąć zawarte w&nbsp;nim pliki prawym przyciskiem myszy i&nbsp;wybrać opcję ich usunięcia;
* zapisać zmienione archiwum (`Ctrl+S`);
* przenieść archiwum do folderu na szablony (jeśli jeszcze go tam nie ma).

W ten sposób uzyskamy rzecz najbliższą pustemu plikowi ZIP, jak tylko się da.  
Nie będzie wprawdzie całkiem pusty (u&nbsp;mnie liczy 22&nbsp;bajty), ale za to będzie działał jak na Windowsie. Po jego stworzeniu przez menu kontekstowe będzie można go kliknąć, otwierając pustą listę, gotową do zapełnienia różnymi rzeczami.

{% include info.html 
type="Porada"
text="Skoro już jesteśmy przy pustych plikach ZIP, podzielę się radą.  
Na Windowsie da się kopiować pliki i&nbsp;wklejać je do wnętrza archiwum. Na Linuksie program Engrampa nie daje takiej opcji, jest szara i&nbsp;nieaktywna. Domyślnym sposobem na dodanie nowych plików jest kliknięcie opcji `Edycja` z&nbsp;górnego paska, a&nbsp;potem `Dodaj plik`.  
Istnieje jednak inny, szybszy, mniej oczywisty sposób na zapełnianie pliku ZIP na Linuksie. Można **„chwycić” myszą plik/folder i&nbsp;przenieść go do otwartego okna z&nbsp;Engrampą**. W&nbsp;ten sposób zostanie skopiowany do wnętrza archiwum."
%}

## Słowo na koniec

Kolejna cegiełka dołożona do budowy Linuksa dla ludzi :metal: Teraz czas na wieczorny spacer -- a&nbsp;po powrocie będzie trochę dłubania przy kontynuacji [wpisu na temat trolli z&nbsp;koncernów biotechnologicznych](/2022/12/24/biotechnologia-trolle-youtube){:.internal}.

Zanim pójdę, zostawię tu jeszcze krótkie przemyślenie.

Wiele osób głębiej wciągniętych w&nbsp;świat Linuksa spędza sporo czasu w&nbsp;konsoli, odchodząc od graficznego interfejsu (albo zdając się na coś spersonalizowanego, kafelkującego itd.).

W efekcie typowy interfejs, z&nbsp;gatunku tych, do jakich Windows przyzwyczaił ludzi, pozostaje nie do końca przetestowany. Przykładem brak opcji wklejania plików do Engrampy, który przypadkiem odkryłem i&nbsp;opisałem wyżej.

Gorąco zachęcam ludzi promujących Linuksy do chwilowego wyłączenia bajerów i&nbsp;spojrzenia na system okiem zwykłej osoby, klikającej myszą. Założyć sobie: „nie używam tej opcji, ale przeklikam się na próbę. Czy działa jak powinna?”.  
Zrobić to raz na Windowsie, a&nbsp;potem na Linuksie. Porównywać, jak działają podstawowe rzeczy.

Nawet jeśli wy, drodzy czytelnicy, nie lubicie klikaniny -- wierzcie mi, że na niej stoi świat. Trzeba ją dopracować, żeby Linux mógł go zawojować.
