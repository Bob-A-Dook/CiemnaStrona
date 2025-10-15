---
layout: page
title: Uruchamianie Linuksa i błąd invalid magic number
description: "Co zrobić, gdy jądra systemu dotknie czarna magia."
---

Eksperymentowałem sobie ostatnio z&nbsp;różnymi systemami na bazie Linuksa. Kiedy ładowałem jeden z&nbsp;nich (przez [Ventoya](/tutorials/ventoy){:.internal}), to zamiast znajomego czarno-białego ekranu z&nbsp;opcjami pokazał się taki błąd:

```
error: invalid magic number.
error: you need to load the kernel first.
```

W tłumaczeniu na polski: „niewłaściwa [liczba magiczna](https://en.wikipedia.org/wiki/Magic_number_(programming)). Musisz najpierw załadować jądro \[systemu\]”.

Tak się składa, że błąd udało się łatwo rozwiązać, bo wiązał się z&nbsp;wadliwym plikiem ISO, z&nbsp;którego ładowałem Linuksa. **Wystarczyło usunąć tego Linuksa z&nbsp;pendrive'a i&nbsp;wgrać go na nowo**.

W sumie na tej krótkiej notce typu „problem-rozwiązanie” mógłbym poprzestać. Ale wspomnę jeszcze o&nbsp;tym, w&nbsp;jaki sposób doszło do błędu, żeby może oszczędzić go innym osobom.

## Historia z&nbsp;życia

### Przyczyna błędu

Jak wspomniałem na początku, korzystałem z&nbsp;Ventoya. Polega to na tym, że mam pendrive'a, na którego mogę wrzucać pliki ISO z&nbsp;Linuksami -- w&nbsp;najprostszy sposób, tak jakby były przykładowo dokumentami albo zdjęciami.

Później wpinam takiego pendrive'a do komputera, włączam menu uruchamiania i&nbsp;wybieram jednego z&nbsp;tych Linuksów. Ładuje się do pamięci, podczas gdy system, który już mam zainstalowany na kompie, odpoczywa sobie na dysku. Nieużywany. To tzw. *tryb live*.

Swego czasu siedziałem przy laptopie, na którym z&nbsp;Ventoya właśnie załadował się Linux A. Na telefonie miałem plik ISO z&nbsp;Linuksem B.  
Chciałbym go zrzucić na pendrive'a z&nbsp;Ventoyem... Który właśnie tkwił w&nbsp;napędzie jako filar uruchomionego Linuksa A.

{:.post-meta .bigspace-after}
System domyślny z&nbsp;dysku nie ma w&nbsp;tej historii znaczenia, nie miałem możliwości z&nbsp;niego skorzystać. Długa historia.

Żeby Ventoy pokazał się jako zwykły pendrive, musiałbym go wypiąć i&nbsp;wpiąć ponownie.  
Wiedziałem, że ogólnie odłączanie pendrive'a w&nbsp;trybie *live* może prowadzić do błędów. To dlatego, że system czasem sobie z&nbsp;niego doładowuje różne rzeczy, zaś w&nbsp;przypadku jego odłączenia traci do nich dostęp.

Ale te błędy -- co ma tu spore znaczenie -- nie dotyczą wszystkiego. Zdarzało mi się już, że przykładowy notatnik (`xed`) działał całkiem sprawnie nawet po odpięciu pendrive'a. Warunkiem było tylko to, żebym go uruchomił *przed* odłączeniem.

Świadomość, że błędy nie są nieuchronne, skłoniła mnie do ryzyka. Wyjąłem pendrive'a z&nbsp;Ventoyem, wpiąłem go ponownie (pokazał się jako zwykły), zgrałem na niego plik.

Trochę jak wyjęcie komuś drabiny spod nóg z&nbsp;nadzieją, że złapie się gałęzi. Szybkie pomajstrowanie przy niej i&nbsp;odstawienie z&nbsp;powrotem :wink:

Wszystko wydawało się działać. Plik skopiował się na Ventoya, nie wyświetliło komunikatu o&nbsp;błędzie.  
...Ale najwidoczniej jednak nie wszystko było w&nbsp;porządku, a&nbsp;podczas kopiowania wystąpił jakiś błąd. Dlatego, gdy później próbowałem ładować z&nbsp;Ventoya najnowszego Linuksa B, to się nie włączał. Inne działały.

### Rozwiązanie

Ostatecznie rozwiązaniem okazało się:

* usunięcie wadliwego pliku ISO z&nbsp;Ventoya;

  (nie działało przez menu graficzne programu Caja, bo plik po kombinacji `Shift+Delete` wracał na miejsce; dlatego ostatecznie włączyłem konsolę w&nbsp;folderze z&nbsp;plikami ISO i&nbsp;usunąłem ten popsuty komendą `rm PLIK`);

* [załadowanie Linuksa A&nbsp;z&nbsp;opcją `toram`](/tutorials/live-squashfs-problem.html){:.internal}

  (trafia wtedy w&nbsp;całości do pamięci, a&nbsp;pendrive'a z&nbsp;Ventoyem można swobodnie odłączyć; nie każdy Linux wspiera taki tryb, ale mój Mint na szczęście wspierał);

* zgranie pliku ISO z&nbsp;Linuksem B&nbsp;z telefonu;
* wrzucenie tego pliku na pendrive'a z&nbsp;Ventoyem.

W ten sposób dostałem nauczkę: nie wyciągać Linuksowi przysłowiowej drabiny spod nóg.

Mam nadzieję, że opowiastka pokaże innym, że czasem błędy nie wynikają z&nbsp;winy alternatywnych systemów, lecz z&nbsp;naszej własnej brawurowej żonglerki.
