---
layout: page
title: Linux, MATE i białe prostokąty zamiast ikon w przeglądarce plików 
description: "Nawet zwykłym plikom tekstowym nie zaszkodzi trochę upiększenia."
---

W tym miniwpisie opiszę, jak rozwiązać problem białych, szpetnych prostokątów, które pojawiały się w przeglądarce plików Caja zamiast ikonek milszych dla oka.

## Opis problemu

Moim ulubionym wariantem Linuksa do codziennych zadań jest Mint. Konkretniej -- Mint MATE, gdzie MATE to nazwa *środowiska graficznego*; filaru odpowiedzialnego za ogólny wygląd i&nbsp;zachowanie systemu, jego menu itd.

Częścią środowiska jest często jakaś domyślna przeglądarka plików. Nie inaczej jest na MATE, gdzie nazywa się ona **Caja**.

{:.post-meta .bigspace-after}
Wiele osób może być nieświadomych tej nazwy, bo ikona na Mincie jest podpisana po prostu jako „Przeglądarka plików”. Ale zakładka informacyjna w&nbsp;samym programie ujawnia jego prawdziwą nazwę.

Caja na Mincie mnie rozpieściła i&nbsp;przyzwyczaiła do różnych udogodnień. Takich jak eleganckie ikony dla różnych rodzajów plików.  
Zdziwiłem się zatem, kiedy na innym Linuksie było gorzej. O&nbsp;ile miniatury obrazków działały jak należy, o&nbsp;tyle prawie wszystkie rodzaje **plików tekstowych** miały biały prostokąt zamiast ikon:

{:.bigspace-before}
<img src="/assets/tutorials/linux/caja-ikony-plikow/caja-niewidoczne-ikonki-plikow.png" alt="Trzy pliki wewnątrz przeglądarki. Tylko jeden ma swoją ikonę, a&nbsp;pozostałe dwa to białe prostokąty" />

{:.figcaption}
Widać, że wyjątkiem posiadającym ikony były pliki ze sformatowanym tekstem typu Markdown; prawie żadne inne skrypty i pliki tekstowe ich nie miały.

## Rozwiązanie

Wystarczy parę kliknięć w menu, żeby zyskać ikony bardziej cieszące oko.

Najpierw należy uruchomić program Caja, wybrać z&nbsp;górnego paska `Edit` (*Edycja*). Następnie należy wybrać opcję `Preferences` z&nbsp;rozwijanego menu (powinna być na samym dole):

{:.bigspace}
<img src="/assets/tutorials/linux/caja-ikony-plikow/caja-ustawienia.png" alt="Zrzut ekranu pokazujący opcję z&nbsp;górnego paska programu Caja oraz opcję wybraną z&nbsp;menu" />

Potem należy wybrać z&nbsp;górnego paska zakładkę `Preview` (*Podgląd*) i&nbsp;wyłowić wzrokiem opcję podpisaną `Show text in icons` (*Pokazuj tekst wewnątrz ikon*). Na prawo od niej znajduje się krótkie rozwijane menu, z&nbsp;którego należy wybrać opcję `Never` (*Nigdy*).

{:.bigspace}
<img src="/assets/tutorials/linux/caja-ikony-plikow/caja-zmiana-wygladu-miniatur-plikow.png" alt="Zrzut ekranu pokazujący wyłączoną opcję podglądu tekstu wewnątrz programu Caja" />

Zmiany powinny zajść od razu. Jeśli teraz wyjdziesz z&nbsp;menu, to pliki tekstowe, dotąd jednolicie białe, powinny rozświetlić się kolorami.

{:.bigspace}
<img src="/assets/tutorials/linux/caja-ikony-plikow/caja-widoczne-ikonki-plikow.png" alt="Trzy pliki wewnątrz przeglądarki. Każdy ma swoją ikonę: skrypt Pythona żółto-niebieskie węże, a&nbsp;zwykły plik tekstowy parę poziomych kresek na jasnym tle." />

{% include details.html summary="Sposób konsolowy" %}

Problem można również rozwiązać przez konsolę. W&nbsp;tym celu należy w&nbsp;nią wkleić (przez `Ctrl+Shift+V` albo prawoklik i&nbsp;opcję z&nbsp;menu):

```
dconf write /org/mate/caja/preferences/show-icon-text "'never'"
```

Więcej na temat ustawień Dconf i&nbsp;ustalania konsolowych odpowiedników dla różnych opcji z&nbsp;menu napisałem [w tym poradniku](/tutorials/linux-dconf-skryptowanie){:.internal}.

{% include details-end.html %}

Problem rozwiązany, na tym kończę część główną. Jeśli chcesz się dowiedzieć, dlaczego rozwiązaniem było *wyłączenie* tekstu i&nbsp;co jest źródłem problemu -- zapraszam dalej.

## Bonus: przyczyna dziwnego wyglądu ikon

Caja nie jest programem zbudowanym tak całkiem od podstaw. Opiera się na znanej bibliotece **GTK**, która jest rozwijana przez całkiem inną ekipę. To kolekcja różnych szablonów, funkcji i&nbsp;udogodnień. Klocków, z&nbsp;których można budować interfejsy graficzne.

Jedną z&nbsp;takich funkcji był **podgląd dokumentów tekstowych**.

Wielu z nas się przyzwyczaiło, że domyślną ikoną plików-obrazków są ich miniaturki. Podgląd od GTK robił to samo dla plików tekstowych, wyświetlając początek ich zawartości, co ułatwiało m.in. ich szybkie rozróżnianie. Caja również z&nbsp;tego korzystała.

Ekipa od GTK postanowiła jednak napierać do przodu i&nbsp;wypuścić nowe wersje biblioteki, ze zmienionymi fundamentami działania. Funkcja podglądu nie do końca im się chyba lubiła z&nbsp;nowymi funkcjami... Więc stała się ofiarą rewolucji. Wzięli ją i&nbsp;usunęli.

Różne programy oparte na GTK musiały od teraz wypełnić pustkę we własnym zakresie. W&nbsp;programie Caja opcja podglądu została nieruszona, bo jego twórca miał nadzieję, że wskrzesi dawną funkcję.

To się chyba nie udało -- na chwilę obecną próba użycia podglądu doprowadza do błędu, zaś błąd sprawia, że plik zyskuje ikonę zastępczą, uniwersalną, nie sugerującą niczego. Biały prostokąt.

{:.post-meta .bigspace-after}
Informacje wyłuskałem z&nbsp;tej [dyskusji](https://bbs.archlinux.org/viewtopic.php?id=273679) z&nbsp;forum Arch Linuksa, kolejnej ze [społeczności Ubuntu](https://ubuntu-mate.community/t/caja-shows-blank-icon-for-all-source-files-c-c-go-python/18827/8) oraz z&nbsp;wymiany zdań [na Githubie](https://github.com/mate-desktop/caja/issues/1047) (stronie z&nbsp;kodem źródłowym programu Caja).

Czy tak będzie już zawsze? W&nbsp;obecnej sytuacji zarysowują się dwa możliwe rozwiązania:
 
* doraźne -- jeśli podgląd tekstu nie działa, to wyświetlać zamiast niego ikonę domyślną dla danego rodzaju pliku;
* ambitne -- znaleźć wewnątrz dawnego GTK kod odpowiedzialny za tworzenie podglądu i&nbsp;zintegrować go z&nbsp;kodem przeglądarki Caja.

Jeśli ktoś czuje się na siłach i&nbsp;chce coś zrobić dla świata otwartego oprogramowania -- to oto ma ku temu okazję :wink:
