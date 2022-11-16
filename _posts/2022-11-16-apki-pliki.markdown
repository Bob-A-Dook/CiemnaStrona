---
layout: post
title:  "Apki to pułapki 2 – system plików"
subtitle: "Wspólne pliki, niczyja prywatność."
description: "Wspólne pliki, niczyja prywatność"
date:   2022-11-16 16:22:00 +0100
tags: [Android, Apki, Inwigilacja, Podstawy]
category: apki
category_readable: "Apki to pułapki"
image:
  path: /assets/posts/apki/apki-system-plikow-baner.jpg
  width: 1200
  height: 700
  alt: Dwa schematy dopasowane do siebie kolorami - piramidka pokazująca warstwy systemu oraz drzewko pokazujące układ folderów.

---

Jednym z&nbsp;najczęstszych pozwoleń, o&nbsp;jakie proszą nas mobilne aplikacje -- a&nbsp;na komputerach osobistych nic nawet nie pyta -- jest możliwość odczytywania i&nbsp;zapisywania plików.  
Równie powszechna jest łączność z&nbsp;internetem, która pozwala programom wysyłać informacje w&nbsp;świat.

W takich warunkach pokusa śledzenia wydaje się oczywista.  
Skoro aplikacja może czytać pliki, to po prostu sobie do nich zajrzy, odczyta z&nbsp;nich nasze dane i&nbsp;komuś je wyśle.  
Z jakiegoś zdjęcia faktury pozna nazwę naszej firmy. Z&nbsp;biletów kolejowych w&nbsp;formacie PDF nasze imię, nazwisko i&nbsp;szczegóły podróży.

Tak, to realne zagrożenie. Ale nie chcę zanudzać moich czytelników oczywistościami.

Dlatego dorzućmy sobie dodatkowe ograniczenie -- w&nbsp;tym wpisie **nie rozważam przypadku, kiedy apka zagląda do wnętrza plików**.   
Zakładamy tu, że jedynie wędruje po folderach i&nbsp;patrzy na ogólne informacje. Nazwy plików, ich rozmiar i&nbsp;datę modyfikacji. Tak jak my, kiedy rozglądamy się za jakimś konkretnym plikiem.

Jak zobaczymy, nawet przy takich ograniczeniach programy mogą wyciągnąć naprawdę sporo szczegółów. Zapraszam do lektury!

{% include info.html
type="Uwaga"
text="Tradycyjna przypominajka -- na tym blogu poruszam **tematy wokół prywatności osobistej, a&nbsp;nie cyberbezpieczeństwa**. Nie mam nic do powiedzenia na temat hakerów, ludzi mających fizyczny dostęp do naszego telefonu, użytkowników Pegasusa.  
Poza tym wszystkie moje przykłady będą dotyczyły smartfona Huawei z&nbsp;systemem Android 10. Niektóre informacje mogą nie mieć odniesienia do innych urządzeń."
%}

# Spis treści

* [Wprowadzenie](#wprowadzenie)
* [Termux](#termux)
* [Pliki oczami aplikacji](#pliki-oczami-aplikacji)
* [Ciemne strony systemu plików](#ciemne-strony-systemu-plików)
  * [Odkrywanie zainstalowanych aplikacji](#odkrywanie-zainstalowanych-aplikacji)
  * [Odkrywanie wersji Androida](#odkrywanie-wersji-androida)
  * [Eksplorowanie metodą *brute force*](#eksplorowanie-metodą-brute-force)
* [Identyfikowanie konkretnej osoby](#identyfikowanie-konkretnej-osoby)
* [Jak się chronić](#jak-się-chronić)

## Wprowadzenie

Każdy system układa swoje pliki w&nbsp;nieco inny sposób.

W przypadku typowych komputerów osobistych mówimy o&nbsp;„plikach na dysku”.  
Na smartfonach jest inaczej. Nie ma dysku (nie zmieściłby się), jest pamięć Flash. Również hierarchia plików nieco się różni od tego, co mamy na typowym komputerze z&nbsp;Windowsem.

Ale pewne zasady pozostają uniwersalne. Mamy foldery, a&nbsp;w nich pliki. Albo inne foldery.  
Zajrzyjmy do nich!

### Pliki oczami użytkownika

System Android daje nam możliwość intuicyjnego przeglądania niektórych folderów:

* przez domyślną, od początku zainstalowaną aplikację (u mnie nazywa się `Pliki`).
* po podłączeniu smartfona do komputera przez USB  
  (trzeba też wtedy wybrać na telefonie tryb transferowania plików).

Ale czy to prawdziwy obraz rzeczywistości? Nie -- mamy wgląd tylko w&nbsp;wybrane foldery, ze wspólnej i&nbsp;publicznej części telefonu. **Aplikacje widzą nieco więcej**.

Żeby lepiej to pokazać, potrzebowałem w&nbsp;tym miejscu apki mającej szerokie możliwości zaglądania do plików. A&nbsp;przy tym dającej nam wgląd w&nbsp;to, co sama „widzi”. Na szczęście takowa istnieje. I&nbsp;jest bardzo fajna.

### Termux

Do eksplorowania systemu plików użyłem apki [Termux](https://f-droid.org/packages/com.termux/).

Jest o&nbsp;tyle ciekawa, że stawia na kompletnie inne rzeczy niż większość popularnych apek.  
Te drugie zwykle mają ładny interfejs, zaś wszelkie techniczne detale ukrywają przed oczami użytkowników.

Termux ma wygląd dość spartański -- ot, konsola z&nbsp;czarnym tłem, w&nbsp;którą możemy wpisywać różne polecenia. Ale za to niczego przed nami nie ukrywa. Pozwala zwiedzać system i&nbsp;zobaczyć wnętrze smartfona takim, jakim widzą je inne aplikacje. Bez lukru.

Na potrzeby tego wpisu nie musimy wiedzieć o&nbsp;Termuksie praktycznie nic. Poza tym, że wpisujemy w&nbsp;niego komendy. Do eksploracji wystarczą nam w&nbsp;zasadzie dwie:

1. Komenda `ls` -- wyświetla listę rzeczy (plików i&nbsp;folderów) znajdujących się w&nbsp;aktywnym folderze.

2. Komenda `cd ŚCIEŻKA` -- pozwala przejść do folderu o&nbsp;podanej ścieżce. Jeśli istnieje i&nbsp;jest dostępny, to staje się naszym folderem aktywnym. Do czasu kolejnej zmiany.

Możemy też użyć komendy `exit`, żeby z&nbsp;Termuksa wyjść. Ale jak nas wciągnie, to zapomnimy o&nbsp;jej istnieniu.

Te komendy są kompletnie bezpieczne. Jeśli zrobimy coś głupiego (na przykład spróbujemy przejść do folderu, który nie istnieje), to po prostu wyświetli nam błąd.  
Jako człowiek skłonny do literówek szczególnie to doceniam :wink:

## Pliki oczami aplikacji

W poprzednim wpisie z&nbsp;serii pokazałem z&nbsp;grubsza hierarchię w&nbsp;naszym systemie -- w&nbsp;formie piramidki. Tym razem nie potrzebujemy całej. Odpuścimy sobie zarówno warstwę dodatków, jak i&nbsp;warstwy najniższe, odpowiadające fizycznym elementom.

Zostaje nam system i&nbsp;nasza apka Termux. Dla porównania weźmiemy też jedną inną. Niech będzie Messenger.  
Zostajemy z&nbsp;takim układem:

{:.bigspace}
<img src="/assets/posts/apki/apki-piramida-system-plikow.jpg" alt="Odwrócona piramida złożona z&nbsp;trzech poziomów o&nbsp;różnych kolorach. Najniższy jest podpisany 'jądro systemu'. Warstwa nad nim to 'system operacyjny'. Na niej znajdują się dwa trapezy o&nbsp;identycznych wymiarach. Jeden z&nbsp;nich zawiera pośrodku ikonę aplikacji Termux, a&nbsp;drugi apki Messenger. Po prawej stronie warstwy widać podpis 'Programy'." width="500px"/>

U góry programy, ich fundamentem jest system operacyjny, pod nim jądro systemu.

Zaznaczę, że do pojęcia jądra systemu podchodzę tu mocno nieoficjalnie. Intuicja nade wszystko. Na potrzeby tego wpisu przyjmijmy po prostu, że jest *częścią systemu, do której mamy ograniczony dostęp*.

A teraz nałóżmy sobie na tę hierarchię układ folderów. Przedstawiam Wam system plików widziany „oczami” Termuksa. 

{:.bigspace-before}
<img src="/assets/posts/apki/apki-system-plikow-graf.jpg" alt="Schemat pokazujący hierarchię folderów w&nbsp;systemie Android. Mamy tu cztery obszary. Wychodząc od dołu: jądro systemu, potem system operacyjny, potem na jednej wysokości Messenger i&nbsp;Termux"/>

{:.figcaption}
Schemat lekko edytowany w&nbsp;Gimpie. Gdyby kogoś interesował jego kod źródłowy w&nbsp;Graphvizie, to <a download href="/assets/posts/apki/android_pliki.gv">proszę bardzo</a>.

W elipsach mamy nazwy folderów. Strzałki pokazują hierarchię -- wychodzą od folderów nadrzędnych do ich podfolderów.

Jeśli chodzi o&nbsp;kolory elips-folderów:

* Kolor zielony to folder główny Termuksa.

  To do niego trafiamy po każdym uruchomieniu tej aplikacji.

* Kolor pomarańczowy to foldery częściowo niedostępne.

  Możemy do nich wejść, ale nie możemy się rozglądać. Wpisanie komendy `ls` (od wyświetlenia zawartości folderu) zwraca komunikat *Permission denied*.

* Kolor czerwony to foldery całkiem niedostępne.

  Tutaj, przypominam, dla Termuksa. W&nbsp;przypadku Messengera to jego folder byłby na biało, a&nbsp;termuksowy na czerwono.  
  Do takich folderów nie da się nawet wejść. Od razu wyświetli brak pozwolenia.

Położenie różnych folderów możemy też przedstawiać w&nbsp;zwięzłej formie *ścieżek* -- to je wpisujemy w&nbsp;Termuksa.  
Żeby ustalić pełną (bezwzględną) ścieżkę, zaczynamy od dołu i&nbsp;zbieramy nazwy z&nbsp;elips, łącząc je ukośnikami. Na przykład pełna ścieżka do naszego „zielonego” folderu domowego Termuksa to:

```
/data/data/com.termux/files/home
```

I tak, `com.termux` oraz `com.facebook.orca` to foldery, mimo że mają w&nbsp;nazwach kropki. Jeszcze do nich wrócimy.

{% include info.html
type="Ciekawostka"
text="Wnikliwi użytkownicy Windowsa mogą dostrzec, że ukośniki są zwrócone w&nbsp;przeciwną stronę niż na ich systemie.  
Ale to właśnie taka konwencja jest w&nbsp;wielu kręgach popularniejsza. Stosuje to system MacOS od Apple oraz ich iOS. A&nbsp;także otwarty system GNU/Linux -- na którego jądrze jest zresztą oparty Android."
%}

### System pozwoleń

System Android wykorzystuje *pozwolenia* -- coś w rodzaju pstryczków. Sami decydujemy, czy chcemy dać konkretnej aplikacji dostęp do określonych funkcji smartfona.  
Niektórych pozwoleń udzielamy tylko raz, podczas instalacji, a&nbsp;inne można przyznawać lub wycofywać w&nbsp;dowolnym momencie.

Jedno pozwolenie z&nbsp;tej drugiej kategorii jest związane z&nbsp;plikami -- na moim Huaweiu nosi nazwę `Pamięć`. Reguluje dostęp do wspólnych plików i&nbsp;folderów. Czyli tej części, która podchodzi na schemacie pod system operacyjny. 

To bodajże najczęstsze pozwolenie, jakiego chcą ode mnie aplikacje. Nie szukałem statystyk, ale nie zdziwiłbym się, gdyby było też najczęstszym w&nbsp;skali świata.  
Korzystają z&nbsp;niego w&nbsp;końcu apki pozwalające pracować z&nbsp;plikami zewnętrznymi, dodawać filtry do zdjęć, wyświetlać e-booki...

Pozwolenie możemy w&nbsp;dowolnym momencie wycofywać. W&nbsp;tym celu odwiedzamy `Ustawienia`, potem `Menedżera uprawnień`. Klikając w&nbsp;poszczególne pozwolenia, widzimy listę apek, jakim je przyznaliśmy. To samo menu pozwala cofać pozwolenia.

Jak wygląda cofnięcie pozwolenia z&nbsp;punktu widzenia użytkownika?  
Aplikacje zaczną prosić o&nbsp;jego udzielenie przy dość typowych rzeczach. Jeśli na przykład klikniemy ikonę zdjęcia, chcąc dodać fotkę z&nbsp;galerii do wiadomości pisanej przez Messengera, pojawi się systemowy komunikat:

{:.figure .bigspace}
<img src="/assets/posts/apki/messenger-filesystem-permission.jpg" alt="Komunikat z&nbsp;Androida pytający, czy chcę zezwolić aplikacji Messenger na dostęp do systemu plików" width="350px"/>

A jak to wygląda oczami aplikacji?  
Wyobraźmy sobie, że wszystkie foldery zebrane na schemacie pod kategorią „System operacyjny” stają się pomarańczowymi elipsami. Możemy odwiedzać, ale nie możemy nic robić z&nbsp;plikami. Nawet wyświetlać ich listy.

Podsumowując kwestię pozwoleń:

1. Żadna aplikacja nie ma dostępu do plików podlegających pod jądro (ale może odwiedzać wybrane foldery)
2. Żadna aplikacja nie ma dostępu do folderów prywatnych innych aplikacji.
3. Każda aplikacja mająca pozwolenie o&nbsp;nazwie `Pamięć` ma dostęp do wspólnych plików. Bez tego pozwolenia nadal może odwiedzać wspólne foldery, ale nie może nic w&nbsp;nich robić.

## Ciemne strony systemu plików

Mamy już wszystkie niezbędne fakty. Czas teraz przejść do różnych kreatywnych sposobów, w&nbsp;jakie apki oraz ich twórcy mogą użyć informacji o&nbsp;naszych plikach przeciwko nam.

Przypominam -- **mając dostęp do plików, apki mogą je sobie czytać**. Jeśli mają oprócz tego pozwolenie na korzystanie z&nbsp;internetu (bardzo powszechne), to mogą je ponadto wysłać właścicielom.

W tym wpisie tego nie pokazuję tylko dlatego, że chcę się skupić na mniej oczywistych rzeczach. Ale pod względem zagrożenia to właśnie bezpośrednie kopiowanie treści powinno budzić największe obawy. 

### Odkrywanie zainstalowanych aplikacji

Żadna aplikacja nie jest w&nbsp;stanie wejść do prywatnego folderu obcej aplikacji -- patrz punkt drugi wyżej. Ale jest w&nbsp;stanie ustalić, które ze znanych apek mamy na swoim urządzeniu.

Jeśli spojrzymy na górną część schematu, strefę aplikacji, to zobaczymy dość dziwne nazwy folderów zaczynające się od *com*. To tak zwane nazwy pakietów (ang. *package names*).  
Każda aplikacja zarejestrowana w&nbsp;oficjalnych bazach ma taką własną, wewnętrzną, unikalną nazwę. Nieraz inną niż oficjalna nazwa apki.

Żeby ustalić wewnętrzną nazwę jakiejś aplikacji, można na przykład włączyć przeglądarkę, wyszukać „potoczną” nazwę tej apki na stronie Play Store. Potem patrzymy na link do niej i&nbsp;na wartość parametru `id`. Dla Messengera mamy na przykład:

<div class="black-bg mono nobreak">
https://play.google.com/store/apps/details?id=<span class="red">com.facebook.orca</span>&gl=US
</div>

A dla TikToka:

<div class="black-bg mono nobreak">
https://play.google.com/store/apps/details?id=<span class="red">com.ss.android.ugc.trill</span>&gl=US
</div>

Na czerwono oznaczyłem interesujące nas nazwy pakietów.

I teraz cały myk -- mam u&nbsp;siebie na telefonie Messengera. Nie mam i&nbsp;nigdy nie miałem TikToka.  
Kiedy przez Termuksa spróbuję wejść do odpowiadających tym apkom folderów, to **pokażą mi się różne rzeczy. Zakaz dostępu, jeśli mam daną apkę. Jeśli nie mam, to informacja o&nbsp;braku takiego folderu**.

{:.figure .bigspace-before}
<img src="/assets/posts/apki/termux-brak-dostepu.jpg" alt="Zrzut ekranu z&nbsp;aplikacji Termux, pokazujący dwa różne wyniki dla komendy cd, kiedy próbuję wejść do fodleru Messengera i&nbsp;folderu Tiktoka" width="600px"/>

{:.figcaption}
Screen z&nbsp;apki Termux. Kolorowe tło dodałem w&nbsp;Gimpie.

W ten sposób jakaś wścibska apka mogłaby po kolei sprawdzać nazwy odpowiadające różnym znanym aplikacjom. I&nbsp;na podstawie informacji o&nbsp;zakazach ustalić, które z&nbsp;nich mamy na swoim telefonie.

I takie coś *już miało miejsce*, choć nie wiem czy akurat przy użyciu tej metody. Facebook oferował kiedyś darmową apkę Onavo, działającą jako VPN. Która przy okazji [zbierała dane o&nbsp;innych zainstalowanych aplikacjach](https://www.theverge.com/2019/2/22/18235908/facebook-onavo-vpn-privacy-service-data-collection).  
W ten sposób ustalili, że komunikator WhatsApp, konkurencyjny wobec ich Messengera, zyskuje na popularności. I&nbsp;go kupili.

{% include info.html
type="Inna metoda"
text="Nawet gdyby to załatali, wciąż pozostaje inny sposób na przybliżone poznanie, jakie mamy apki. Być może **zostawiają we wspólnej przestrzeni charakterystyczne pliki**.  
Przykład? Kiedy robimy na telefonie zrzuty ekranu, z&nbsp;angielskiego *screenshoty*, to trafiają do folderu `Screenshots` w&nbsp;znanym nam folderze `Pictures`.  
Każda nazwa pliku zawiera po dacie wykonania nazwę aplikacji, w&nbsp;której dany zrzut ekranu został wykonany. Zatem, jeśli często robimy *screeny*, to po samych ich nazwach dałoby się ustalić, jakie mamy u&nbsp;siebie aplikacje."
%}

### Odkrywanie wersji Androida

Mocno powiązane z&nbsp;poprzednim, bo korzysta z&nbsp;tej samej metody. Tyle że nie odpytuje o&nbsp;foldery prywatne aplikacji, lecz o&nbsp;te wbudowane prosto w&nbsp;nasz system.

Spójrzmy na przykład na [lokalizację bazy z&nbsp;SMS-ami](https://www.fonedog.com/android-data-recovery/android-text-message-folder-location.html) w&nbsp;różnych wersjach Androida:

* W&nbsp;wersji 4.3 i&nbsp;wcześniejszych:  
  `/data/data/com.android.providers/telephony/database`
* Od wersji 4.4:  
  `/data/data/com.android.providers.telephony/database`
* Od wersji 7.0:  
  `/data/user_de/0/com.android.providers.telephony/databases`

Wścibska aplikacja mogłaby po kolei próbować zajrzeć do tych folderów. **Jeśli wyświetli jej odmowę dostępu, a&nbsp;nie informację o&nbsp;nieistniejącym folderze, to znaczy że folder istnieje**. Aplikacja będzie wiedziała z&nbsp;grubsza, jaką mamy wersję Androida.

Słaby sygnał, powiecie? Pewnie tak, ale w&nbsp;połączeniu z&nbsp;innymi może zdradzić więcej. Przez lata w&nbsp;systemie Android mogło się naprawdę sporo pozmieniać.  
Zresztą pokazuję to bardziej jako eksperyment myślowy. Zazwyczaj aplikacje mają łatwiejszy sposób na uzyskanie informacji o&nbsp;systemie. Mogą po prostu zapytać.

Ale jeśli na przykład majsterkowaliśmy ze swoim telefonem, żeby ujawniał apkom nieprawdziwe dane, to warto pamiętać również o&nbsp;dopracowaniu takich detali jak ścieżki w&nbsp;systemie plików. Inaczej kłamstwo na nic i&nbsp;tylko byśmy się wyróżnili.

Ten ogólny motyw -- złapanie naszego urządzenia na kłamstwie poprzez porównanie detali faktycznych z&nbsp;oczekiwanymi -- może się kojarzyć niektórym czytelnikom z&nbsp;dawnym [wpisem na temat *User Agenta*]({% post_url 2021-06-11-user-agent %}){:.internal}, którym przedstawiają się w&nbsp;sieci przeglądarki.  
Pewne reguły śledzenia pozostają uniwersalne. Niezależnie od tego, jak się nazywają i&nbsp;jakich urządzeń dotyczą.

### Eksplorowanie metodą *brute force*

Okej. Apki mogą wykorzystać fakt, że dla folderów istniejących wyświetla się inny komunikat. I&nbsp;ustalić w&nbsp;ten sposób, czy mamy u&nbsp;siebie foldery z&nbsp;konkretnej listy.

Ale to nie wszystko. Gdyby apki były szczególnie zdeterminowane, mogłyby *strzelać w&nbsp;ciemno*. Skupić się na folderze, do którego mogą wejść, ale bez podglądania zawartości. I&nbsp;po kolei prosić o&nbsp;losowe podfoldery z&nbsp;tego folderu.

* „Wpuść mnie do folderu `a`”. Brak takiego folderu.
* „Wpuść mnie do folderu `b`”. Brak takiego folderu.
* ...

Jednocześnie by sobie zapisywały, jaka była ich ostatnia prośba. Dzięki temu nie musiałyby zaczynać od zera przy kolejnej okazji.

Metoda niezwykle żmudna i&nbsp;czasochłonna. Ale jeśli trzymamy gdzieś folder nazwany od naszego imienia i&nbsp;nazwiska, to apka w&nbsp;długim horyzoncie czasowym, po zamęczeniu nam procesora, by go wreszcie odkryła.

Co najgorsze, takie skanowanie **działałoby nawet w&nbsp;przypadku braku pozwolenia**. Wystarczyłby sam dostęp do folderów oznaczonych na schemacie na pomarańczowo.  
Na szczęście tych na czerwono by nie przeskanowali, bo próba wejścia do nich zawsze daje identyczny komunikat o&nbsp;braku pozwolenia.

## Identyfikowanie konkretnej osoby

Powyższe przykłady dotyczyły sytuacji bardziej typowej -- wścibskich firm traktujących nazwy i&nbsp;układ naszych folderów jak jeden z&nbsp;wielu punktów danych.  
Możliwe że jesteśmy im całkiem obojętni jako osoby. Jedna z&nbsp;milionów twarzy, których dane zbierają.

Ale co, jeśli ktoś **specjalnie nas weźmie na celownik**?

Wyobraźmy sobie nieco naciągany przykład. Mamy na studiach zdeterminowanego stalkera albo stalkerkę. Ta osoba potajemnie próbuje się dorwać do naszych prywatnych informacji. I&nbsp;stworzyła właśnie prostą apkę na Androida.

Być może to coś rozrywkowego? Hobbystyczna apka od dzielenia się memami. Pobierania cudzych obrazków i&nbsp;wrzucania własnych.  
A może poważniejszego? Jak sposób na wymianę notatek między studentami, żeby się nie dublowali w&nbsp;wysiłkach?

Stalker(-ka) z&nbsp;zaraźliwym entuzjazmem namawia ludzi z&nbsp;roku do pobierania swojej apki. Ale my nie jesteśmy w&nbsp;ciemię bici, słyszeliśmy o&nbsp;różnych wirusach. Więc podejmujemy parę kroków:

1. Sprawdzamy źródło apki.

   Oficjalny Play Store, nie żadna wysyłana na lewo. Czyli jest dostępna publicznie od jakiegoś czasu, ma użytkowników spoza naszych studiów. Dodaje jej to wiarygodności.

2. Sprawdzamy pozwolenia, o&nbsp;jakie prosi apka.

   Są bardzo minimalistyczne i&nbsp;nie budzą naszych podejrzeń.  
   Dostęp do plików? Pewnie po to, żeby dało się wrzucać własne memy/notatki.  
   Dostęp do internetu? Też zrozumiałe, w&nbsp;końcu musi istnieć jakaś łączność ze wspólną bazą.

3. Idziemy o&nbsp;krok dalej i&nbsp;prosimy znajomą, która nieco siedzi w&nbsp;temacie bezpieczeństwa (ale nie umie jeszcze inżynierii wstecznej), o&nbsp;sprawdzenie tej aplikacji.

   Pobiera, klika, sprawdza funkcje. Jednocześnie monitoruje przez chwilę dane, jakie apka wysyła w&nbsp;świat. Nic podejrzanego.

Już spokojni, pobieramy apkę i zaczynamy z&nbsp;niej korzystać.  
Cały problem polega na tym, że ta może zachowywać się inaczej, kiedy ustali że jesteśmy konkretną osobą.

A w&nbsp;jaki sposób tę tożsamość ustala? Może w&nbsp;bardzo prosty, bez zgadywania. Po prostu na każdym urządzeniu, na którym jest, **wypatruje konkretnego sygnału do działania**. Jak obecność pliku o&nbsp;ustalonej nazwie.  
Czegoś takiego by nie wyłapała obca osoba analizująca ruch. Może by to wyłapały algorytmy przy wrzucaniu apki do Play Store'a. Ale niekoniecznie.

Pewnego dnia stalker(-ka) wysyła nam na czacie plik. *Notatki_przeroboine_1234.pdf*. W&nbsp;środku prawdziwe notatki. Nazwa długa, literówka celowa. Żeby taki plik miał mniejszą szansę na wystąpienie „w naturze”.  
Specjalnie czeka do momentu, kiedy będziemy na uczelni, ale raczej z&nbsp;dala od komputera. Żeby była większa szansa, że od razu pobierzemy notatki na telefon.

A to będzie oznaczało, że w&nbsp;naszym folderze `/storage/emulated/0/Downloads` pojawi się plik o&nbsp;wspomnianej nazwie. Dla apki sygnał, że jest na urządzeniu swojego celu i&nbsp;może teraz robić z&nbsp;plikami ciekawsze rzeczy.

Jak na przykład wyszukanie tylko tych zdjęć, na których dominuje paleta kolorystyczna typowa dla ludzkiej skóry. Czytaj: potencjalnie mniej ubranych. I&nbsp;wysłanie ich do stalkerskiej bazy.  
Albo odczytanie ze zdjęć zaszytych w&nbsp;nich [metadanych EXIF]({% post_url 2021-02-10-gdzie-jestem-zapytaj-moich-zdjec %}){:.internal}. Pokazujących dokładne koordynaty GPS-a w&nbsp;momencie wykonywania zdjęcia.

Oczywiście sam motyw -- wysłanie nam pliku unikalnego dla nas i&nbsp;użycie apki do jego znalezienia -- jest dość uniwersalny. To sposób na wiązanie ze sobą różnych tożsamości i&nbsp;jak najbardziej mogłyby to robić też wielkie firmy. 

Brzmi straszno? :wink:

## Jak się chronić

### Minimalizm przede wszystkim

Z pustego i&nbsp;Salomon nie naleje!  
Dlatego najprostszym sposobem byłoby po prostu nietrzymanie na telefonie szczególnie prywatnych zdjęć i&nbsp;plików. W&nbsp;przypadku zdjęć wyłączamy znaczniki geolokalizacji, żeby nie było w&nbsp;nich danych EXIF.

Po drugie: minimalizujemy liczbę aplikacji na telefonie, korzystamy tylko z&nbsp;tych absolutnie potrzebnych. Najlepiej zdobytych z&nbsp;zaufanego źródła.

W przypadku systemu iOS wybór źródła mamy odgórnie narzucony (AppStore). Oceniam to średnio pozytywnie, jeśli chodzi o&nbsp;wolność użytkownika.  
Większym plusem jest natomiast to, że apki nie mogą zerkać do wspólnej przestrzeni, każda ma odrębną (takie rozdzielanie to tak zwany *sandboxing*).

W przypadku Androida opcji mamy więcej. Możemy na przykład użyć alternatywnej bazy, F-Droid, zawierającej apki o&nbsp;otwartym źródle. Najbardziej mainstreamowy jest z&nbsp;kolei Play Store.

Trzecia sprawa: tym apkom, które już mamy, wyłączamy pozwolenia na dostęp do plików. Jeśli bez tego nie będą działały, to im włączymy pstryczkiem.  
Warto przy tym pamiętać, że nawet jednorazowe i&nbsp;krótkotrwałe zezwolenie wystarczy, żeby złośliwe apki dobrały się do danych.

### Ukrywanie plików

Załóżmy, że wyłączyliśmy apkom dostęp do plików. Ale w&nbsp;sposób nieuchronny zbliża się moment, kiedy będziemy musieli je włączyć jakiejś wścibskiej aplikacji. Na przykład jedziemy właśnie do parku rozrywki, na którego terenie trzeba korzystać z&nbsp;ich dedykowanej szpiegowskiej apki.

Po udzieleniu pozwolenia ten szpieg zyska dostęp do naszych plików. Co zrobić?

W ogólnym przypadku -- **musimy gdzieś przenieść te pliki, poza zasięg aplikacji**. Dość oczywistą opcją wydaje się zgranie ich na inne urządzenia, na przykład laptopa albo jakiś dysk online.

Tylko że nie zawsze mamy przy sobie zaufanego laptopa. A&nbsp;nasza chmurowa skrytka może nie pomieścić naszych danych. Albo sporo nas kosztować przez transfer danych mobilnych. No i&nbsp;sama też może zaglądać do plików.

Na szczęście niektóre telefony mają funkcję, która pozwala stworzyć swego rodzaju zaszyfrowany folder. Będziemy mieli do niego dostęp przez naszą typową przeglądarkę plików. A&nbsp;dla aplikacji będzie poza zasięgiem.

W przypadku Huaweia taka funkcja nazywa się *Sejf*. Żeby ją włączyć, wchodzimy w&nbsp;apkę `Pliki`, klikamy ikonkę sejfu, ustawiamy sobie hasło. Możemy tam ukrywać pliki przed aplikacjami. Ale uwaga, [miewa lub miewał błędy](https://android.stackexchange.com/questions/205790/huawei-file-safe-stuck-not-working).

To tyle na dziś! Dla chętnych mam jeszcze pewien alternatywny sposób wykorzystujący Termuksa. A&nbsp;osoby nietermuksowe mogą zadbać o&nbsp;prywatność i&nbsp;na start powyłączać wszystkim apkom dostęp do plików.  
Nadchodzące chłodne dni będą dobrą okazją, żeby owinąć się w&nbsp;koc i&nbsp;to zrobić :smile:

### Bonus: ukrywanie plików przez Termuksa

Do głowy przyszedł mi jeszcze jeden sposób na chowanie plików. Możemy wykorzystać możliwości Termuksa i&nbsp;fakt, że apki nie mogą zaglądać do siebie nawzajem.

{:.post-meta .bigspace}
**Uwaga:** Pomysł dobry tylko dla osób, które będą umiały potem skopiować sobie pliki z&nbsp;powrotem. Wszystko na własną odpowiedzialność. Ale pocieszę, że powinno być bezpieczne.

Najpierw wrzucamy prywatne pliki do osobnego folderu. Możemy to zrobić chociażby przez najzwyklejszą, systemową przeglądarkę plików.  
Załóżmy, że nasz folder nazywa się `Tajne`, spoczywa w&nbsp;folderze `Downloads`, układ plików mamy jak na głównym schemacie.

Teraz otwieramy Termuksa i&nbsp;wpisujemy:

<div class="black-bg mono">
mv /storage/emulated/0/Download/Tajne ~
</div>

Gdzie `mv` to komenda, która przenosi pliki/foldery z&nbsp;pierwszej ścieżki do drugiej. Zaś tylda `~` to skrót oznaczający ścieżkę do naszego wewnętrznego, domyślnego folderu Termuksa.

Po przeniesieniu folder będzie poza zasięgiem aplikacji innych niż Termux. Możemy z&nbsp;nich skorzystać. A&nbsp;po skorzystaniu wyłączyć im pozwolenia albo całkiem je usunąć.  
Gdy już będzie bezpiecznie, możemy przenieść folder z&nbsp;powrotem do publicznie dostępnej lokacji. Włączamy Termuksa i&nbsp;wpisujemy:

<div class="black-bg mono">
mv ~&nbsp;/storage/emulated/0/Download/Tajne
</div>

Prowizorka, ale działa.

