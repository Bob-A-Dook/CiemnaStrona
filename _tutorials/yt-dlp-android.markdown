---
layout: page
title: Korzystanie z yt-dlp na systemie Android
description: "Niezależność od cudzych platform. Również na smartfonie."
---

Programik `yt-dlp`, duchowy następca `youtube-dl` (który nadal działa, ale jest nieco mniej aktywnie rozwijany), to prawdziwe dobrodziejstwo. Pozwala nam pobierać pliki wideo i&nbsp;audio z&nbsp;różnych platform, takich jak YouTube, i&nbsp;zapisywać je u&nbsp;siebie na urządzeniu.

Dzięki temu nie jesteśmy na łasce wielkich platform (które w&nbsp;każdej chwili mogą usuwać treści). Jesteśmy niezależni od łączności z&nbsp;internetem. Swoją biblioteczkę możemy zabierać wszędzie, cenne materiały archiwizować.

Z dobrodziejstw `yt-dlp` można korzystać też na smartfonach :metal: Ale w&nbsp;tym przypadku trzeba się nieco zaprzyjaźnić z&nbsp;konsolą. Stworzyłem ten samouczek, żeby pokazać, że to nic strasznego.

## Instalacja

Zacznijmy od tego, że smartfonowy system Android nie ma konsoli tak sam z&nbsp;siebie. Trzeba ją zdobyć.  
Gorąco polecam do tej roli aplikację [Termux](https://termux.dev/en/). Można ją pozyskać na dwa sposoby:

* Najlepiej zainstalować najpierw [F-Droida](https://f-droid.org/), czyli alternatywne źródło aplikacji. W&nbsp;nim wyszukujemy apkę Termux (wystarczy podstawowa; bez `Termux:API` i&nbsp;innych rozszerzeń). Instalujemy ją.
* Można również zainstalować plik APK udostępniany przez twórców Termuksa [na platformie Github](https://github.com/termux/termux-app/releases).

  Najpierw patrzymy na nagłówki z&nbsp;numerem wersji; zatrzymujemy się przy pierwszej od góry, bo jest najnowsza.  
  Potem wybieramy plik APK pasujący do naszego procesora. Nie wiemy, który to? [Największa szansa, że ARM64](https://android.stackexchange.com/questions/216191/what-percentage-of-android-devices-run-on-a-64-bit-architecture). Ale dla pewności można pobrać plik z&nbsp;`universal` w&nbsp;nazwie; zajmuje więcej miejsca, ale obsługuje wszystkie warianty.

Ponieważ instalujemy pliki APK spoza Play Store'a, wyświetlą nam się ostrzeżenia. To normalne, nie ma się czego obawiać. Jeśli ktoś ma wątpliwości, to może sobie poczytać, zweryfikować reputację Termuksa.

{:.post-meta .bigspace-after}
Istnieje również wersja tej apki w&nbsp;oficjalnej bazie Play Store, ale jest przestarzała; twórcy [szczerze odradzają jej instalację](https://github.com/termux/termux-app#user-content-google-play-store-deprecated).

Od strony praktycznej Termux to zwykła, prosta konsola, w&nbsp;którą możemy wpisywać komendy. Kiedy już go zainstalujemy, to potrzebujemy jeszcze Pythona -- języka programowania, na którym nasz program się opiera.  
Wpisujemy w&nbsp;konsolę:

```
pkg install python
```

W ten sposób zainstaluje nam się również `pip`. Taki program od instalowania innych pythonowych rzeczy. Ale gdybyśmy go teraz użyli, to wyskoczyłby zapewne błąd o&nbsp;braku `libexpat` albo paru innych plików. Dlatego wpisujemy teraz:

```
pkg update
```

Zaktualizują nam się różne rzeczy. Możemy teraz wpisać komendę:

```
pip install yt-dlp
```

Zainstalujemy w&nbsp;ten sposób `yt-dlp`. I&nbsp;gotowe!

## Foldery na Androidzie

Zanim zaczniemy pobierać gigabaty czystego złota, warto wspomnieć o&nbsp;jeszcze jednym niuansie na smartfonach.

Mianowicie: domyślnym folderem dla naszej konsoli jest taki, który znajduje się „wewnątrz” Termuksa. Jeśli użyjemy komendy `yt-dlp` zaraz po otwarciu Termuksa, to pobierze multimedia do tego folderu.  
Problem? Aplikacje na smartfonach nie mogą do siebie zaglądać. Zatem nie bylibyśmy w&nbsp;stanie odtworzyć pobranego pliku osobną aplikacją od multimediów.

Dlatego **warto przed każdą sesją pobierania plików zmienić folder na jakiś publicznie dostępny**. Przykładowo możemy wpisać po uruchomieniu Termuksa:

<pre class="black-bg mono">
cd /storage/emulated/0
</pre>

{:.post-meta .bigspace-after}
Pamiętajcie, że spacje są ważne; dla pewności możecie skopiować stąd całą komendę.

Ta komenda tymczasowo (do czasu zamknięcia Termuksa) przeniesie nas do nadrzędnego foldera naszej karty SD.  
To miejsce publiczne; dostępne dla innych uprawnionych apek, jak przeglądarka plików. A&nbsp;także dla komputera, gdybyśmy go podłączyli przez USB.

Powinniśmy mieć w&nbsp;tym miejscu również podfoldery tematyczne. Takie jak `Music`, `Video` i&nbsp;tak dalej. Jeśli chcemy, możemy np. dopisać `/Music` na końcu powyższej ścieżki, żeby przejść do podfolderu z&nbsp;muzyką (o&nbsp;ile takowy mamy).

### Przenoszenie plików

A co zrobić, jeśli już pobraliśmy plik do wnętrza Termuksa? Nic straconego! W&nbsp;takiej sytuacji wystarczy go przenieść do publicznej przestrzeni:

<pre class="black-bg mono">
mv <span class="red">NAZWA_PLIKU</span> /storage/emulated/0
</pre>

Pewnym problemem może być obecność znaków specjalnych w&nbsp;nazwie pliku. Należą do nich również zwykłe, pospolite spacje.

W normalnych warunkach moglibyśmy „wyłączać ich specjalność”, stawiając przed nimi ukośniki. Ale mam prostsze rozwiązanie.  
Wpisujemy `mv`, spację i&nbsp;pierwsze litery nazwy pliku, po czym naciskamy klawisz `Tab` (ikonka dwóch strzałek w&nbsp;dolnym lewym rogu Termuksa, nad klawiaturą Androida).

W ten sposób **autouzupełnianie podrzuci nam nazwę pliku -- już zabezpieczoną ukośnikami**. Wystarczy dopisać od siebie spację i&nbsp;ścieżkę jak wyżej. Po czym potwierdzić.

## Korzystanie

Kiedy już wiemy, jak sobie radzić z&nbsp;folderami, czas zacząć pobieranie.

Otwieramy najzwyklejszą przeglądarkę i&nbsp;odwiedzamy stronkę z&nbsp;konkretnym filmem, który nas interesuje. Z&nbsp;górnego paska kopiujemy link. Po czym wracamy do Termuksa i&nbsp;wpisujemy:

<pre class="black-bg mono">
yt-dlp <span class="red">LINK</span>
</pre>

Zamiast wpisywać `LINK`, przytrzymujemy palec na ekranie i&nbsp;wybieramy opcję wklejenia. Nasz plik zacznie się pobierać w&nbsp;najlepszej dostępnej jakości.

Interesuje nas sam dźwięk, bo to na przykład piosenka? W&nbsp;takim wypadku lekko modyfikujemy komendę:

<pre class="black-bg mono">
yt-dlp -f bestaudio <span class="red">LINK</span>
</pre>

Dokładniejszy przegląd możliwości `yt-dlp`, a&nbsp;także sposoby na rozwiązywanie niektórych problemów, mam w&nbsp;swoim [głównym samouczku na jego temat](/tutorials/youtube-dl#korzystanie-z-programu){:.internal}. Zachęcam do lektury!

Ale przede wszystkim -- przyjemnej uczty multimedialnej! Na własnym urządzeniu, poza wzrokiem korpoplatform.
