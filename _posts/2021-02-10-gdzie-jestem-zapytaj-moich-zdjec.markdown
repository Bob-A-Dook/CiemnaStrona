---
layout: post
title:  "Gdzie jestem? Zapytaj moich zdjęć"
subtitle: "...czyli dlaczego przed marszem na Kapitol wyłączamy geotagowanie."
description: "Metadane EXIF w zdjęciach mogą zdradzić naszą dokładną lokalizację. Pokazuję przykłady i zagrożenia."
date:   2021-02-10 03:12:18 +0100
tags: [Porady, Inwigilacja, Analiza danych]
---

Wydarzenia z&nbsp;pierwszych dni stycznia 2021 r. -- mówię tu o&nbsp;wtargnięciu do Kapitolu -- pokazały wiele rzeczy. Zwłaszcza jeśli chodzi o&nbsp;obecny stan USA i&nbsp;potęgę informatycznych korporacji.

Ale to większa sprawa, więc wpis o&nbsp;niej jeszcze trochę poczeka. Na razie pokażę wam jedynie krótką historyjkę z&nbsp;morałem, która może nas nauczyć czegoś o&nbsp;prywatności.

Spoiler: **Wszystkie zdjęcia, które wrzucacie do internetu, mogą zawierać Wasze dokładne współrzędne geograficzne**.

## Co stało się zwolennikom Trumpa

Historia jeszcze świeża, więc pewnie wiele osób ją kojarzy. Ale dla formalności krótkie tło wydarzeń:

1. W&nbsp;2018 roku powstaje [Parler](https://en.wikipedia.org/wiki/Parler), portal społecznościowy reklamujący się jako ostoja wolności słowa.
2. Parler stopniowo zyskuje popularność wśród amerykańskiej prawicy. Szczególnie w&nbsp;związku z&nbsp;cenzurowaniem wypowiedzi republikańskiego prezydenta, Donalda Trumpa, przez większe organizacje.
3. Trump przegrywa wybory, nowym prezydentem ma zostać demokrata Joe Biden.
4. 6 stycznia 2021 r. w&nbsp;Waszyngtonie grupa protestujących zwolenników Donalda Trumpa [wchodzi siłą do budynku Kapitolu](https://pl.wikipedia.org/wiki/Atak_na_Kapitol_Stan%C3%B3w_Zjednoczonych).
5. W&nbsp;stronę Parlera padają oskarżenia. Przeciwnicy zarzucają mu, że był jednym z&nbsp;miejsc, w&nbsp;których buntownicy koordynowali swoje działania. Google i&nbsp;Apple blokują możliwość pobierania aplikacji Parlera.
6. Badacze szybko zlatują się pobierać dane, zanim strona upadnie. W&nbsp;tym dowody obciążające ekipę z&nbsp;Kapitolu. Jak się okazuje, strona Parlera była słabo zabezpieczona i&nbsp;można było automatycznie pobrać całą treść.
7. Amazon przestaje zapewniać Parlerowi hosting. Strona znika.

Parler zaliczył fakapa nie tylko w&nbsp;kwestii zabezpieczeń. [Jak się okazało](https://twitter.com/donk_enby/status/1348294151712944128), **nie usuwał ze zdjęć użytkowników informacji o&nbsp;lokalizacji**.

Komplet wypowiedzi i&nbsp;multimediów z&nbsp;kilku lat działania serwisu. Z&nbsp;dokładnie oznaczonym czasem i&nbsp;miejscem, w&nbsp;którym powstały. Żyła złota! Wielu dziennikarzy, badaczy, analityków i&nbsp;hobbystów rzuciło się na te cenne dane.

Efektem ich działań było namierzenie niektórych osób, dokładna rekonstrukcja wydarzeń na Kapitolu i&nbsp;[wizualizacje dające do myślenia](https://gist.github.com/kylemcdonald/8fdabd6526924012c1f5afe538d7dc09).

Mnie natomiast, bardziej niż same wydarzenia, zaciekawiła sprawa danych o&nbsp;lokalizacji zawartych w&nbsp;zdjęciach. Jeśli duża strona społecznościowa ich nie usuwała, to czy możliwe, że inne też tego nie robią? I&nbsp;że nieświadomie, wysyłając innym zdjęcia, często zdradzamy swoje położenie?

## Dane EXIF w&nbsp;praktyce

Na potrzeby tego wpisu włączyłem w&nbsp;telefonie geotagowanie. I&nbsp;zrobiłem takie jedno niewyraźne zdjęcie:

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/test_gimp_resize.jpg" alt="Zdjęcie wykonane w nocy, z punktu kilka metrów nad ruchliwą dwupasmową jezdnią. Widać kilka jadących po niej pojazdów. Po prawej stronie na budynku jest neonowy napis 'Agata'. W tle wysoki budynek o nieregularnym kształcie.">

Co to za miasto? Co to za korpowieża w&nbsp;tle wyglądająca, jakby ktoś grał w&nbsp;Jengę? Niektórzy może rozpoznają.

Domyślna aplikacja, Galeria, daje mi możliwość przeglądania na mapie miejsc, w&nbsp;których dodałem znaczniki. W&nbsp;tym wypadku pokazuje:

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/tel_exif_znacznik.webp" alt="Screenshot prostej mapy pokazujący czerwony znacznik lokalizacji na jezdni. Blisko niego, po lewej stronie, oznaczenie kładki nad drogą. Podpisana nazwa ulicy: Sokolska.">

Czyli miejsce wykonania zdjęcia to **Katowice**. Kładka na ul. Sokolskiej, niedaleko Spodka i&nbsp;Oka Miasta.  
Owszem, nieco mnie przesunęło i&nbsp;wychodzi na to, że zamiast na kładce stałem sobie na środku ruchliwej drogi. Ale to tylko kilkanaście metrów różnicy.

{% include info.html type="Ciekawostka" text="Z kronikarskiego obowiązku: zrobiłem też inne zdjęcie, w&nbsp;trochę dzikszych rejonach. Tam pokazało znacznik ponad kilometr od prawdziwego położenia. Ale może nie czekałem wystarczająco długo po włączeniu i&nbsp;nie złapało dokładnej lokalizacji? W&nbsp;każdym razie lepiej nie liczyć na niedokładność urządzenia.  
Pewien [artykuł](https://www.gps.gov/systems/gps/performance/accuracy/) na stronie rządowej podaje, że dokładność smartfonowych GPS-ów, pod gołym niebem i&nbsp;bez dodatkowego wspomagania, może wynosić do ok. 4,9 m. I&nbsp;na takie coś lepiej się nastawiać."%}

Ktoś mógłby pomyśleć, że te znaczniki to taki bajer telefonu. Że kiedy mamy włączoną lokalizację, to podczas robienia zdjęcia dodaje do osobnej, prywatnej bazy informację o&nbsp;tym, gdzie je zrobiliśmy.

**Ale tak nie jest. Telefon dodaje te informacje bezpośrednio do pliku ze zdjęciem**.

Takie informacje uzupełniające to właśnie metadane EXIF. Mają pewne zastosowanie, kiedy na przykład chcemy ułatwić sobie tagowanie kolekcji zdjęć albo podzielić się ustawieniami aparatu w&nbsp;momencie robienia zdjęcia. Ale dla wielu osób to czarna magia, która może zostać użyta przeciwko nim.

Zresztą spójrzmy sami. Biorę to swoje zdjęcie, otwieram je w&nbsp;zwykłym Eksploratorze Windowsa, klikam prawym przyciskiem, wybieram `Właściwości` z&nbsp;dołu, a&nbsp;potem zakładkę `Szczegóły`. Pokazują się metadane zawarte w&nbsp;pliku, w&nbsp;tym również informacje o&nbsp;lokalizacji:

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/exif_info.webp" alt="Okno Windowsa pokazujące listę informacji o zdjęciu, pogrupowanych pod nagłówkami. Dorysowana czerwona ramka otacza nagłówek 'GPS' oraz wartości 'długość' i  'szerokość' znajdujące się pod nim.">

To współrzędne w&nbsp;tzw. formacie DMS (stopnie, minuty i&nbsp;sekundy długości/szerokości geograficznej).

Domyślne okno Windowsa, z&nbsp;tego co widzę, nie daje możliwości ich skopiowania. Gdyby ktoś chciał, mógłby na tym etapie znaleźć osobny program do odczytywania metadanych.

Ale mogę też otworzyć sobie Google Maps i&nbsp;wklepać liczby „z palca” w&nbsp;pasek wyszukiwarki. Najpierw szerokość, potem długość, oddzielone przecinkiem. Po pierwszej liczbie daję znak stopnia (`°`), po drugiej pojedynczy apostrof, kropkę jako oddzielenie części dziesiętnej:

<div class="black-bg">
50°15'54.7805, 19°1'10.0309
</div>

Gdybym nigdzie nie mógł znaleźć znaku stopnia, to mógłbym otworzyć jakiś internetowy konwerter, na przykład [ten od amerykańskiej agencji FCC](https://www.fcc.gov/media/radio/dms-decimal), wpisać liczby dla szerokości geograficznej w&nbsp;polach dla *latitude* i&nbsp;te dla wysokości w&nbsp;polach dla *longitude*. A&nbsp;na koniec wkleić w&nbsp;Mapy wyliczone wartości: `50.265217, 19.019453`.

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/lat_long_konwersja.webp" alt="Fragment strony internetowej, pokazujący białe pola na pomarańczowym tle. Wpisane są w nie liczby, elementy długości i szerokości geograficznej. W dwóch białych polach poniżej wyświetlają się wartości przeliczone na zapis dziesiętny.">

Po wyszukaniu w&nbsp;Mapsach znacznik pokazuje się dokładnie tam, gdzie umieszczała go aplikacja do zdjęć na moim telefonie. Jako punkt orientacyjny oznaczyłem również pawilon „Agata”, którego neon widać na zdjęciu.

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/lokalizacja_google_maps.webp" alt="Zrzut ekranu z Google Maps. Czerwony znacznik lokalizacji wyświetla się na jezdni obok kładki, tak jak poprzednio na telefonie. Nad prostokątem (budynkiem) na południowy wschód od znacznika widać napis 'Agata'. Jest on otoczony czerwonym prostokątem.">

Wniosek: każda osoba, która dostałaby oryginał mojego zdjęcia, mogłaby się dowiedzieć po danych EXIF, w&nbsp;jakim dokładnie miejscu je zrobiłem.

...No ale przecież tyle razy wrzucało się zdjęcia na Fejsa, Zdjęcia Google'a, Insta, inne aplikacje? A&nbsp;jakoś nie słychać o&nbsp;wyciekach i&nbsp;zagrożeniach? **To tylko dlatego, że te platformy same usuwają metadane z&nbsp;plików**. Gdyby tego nie robiły, to każdy mógłby je odczytać.

Żeby to sprawdzić, najpierw otwarłem zdjęcie w&nbsp;GIMP-ie, zmniejszyłem jego rozmiar i&nbsp;jakość, zapisałem pod inną nazwą. Następnie wysłałem je do samego siebie przez Gmaila, w&nbsp;załączniku. **Dane o&nbsp;lokalizacji nadal w&nbsp;nim były**.

Czyli metadane można łatwo odczytać i&nbsp;niełatwo znikają. A&nbsp;jakie zagrożenia się z&nbsp;tym wiążą? Wymyśliłem dość życiowy przykład.

## Scenariusz z&nbsp;życia

Dwie osoby studiują na jednym kierunku. Jedna z&nbsp;nich to zwykła losowa, nieświadoma osoba. A&nbsp;druga to jakiś stalker (albo stalkerka! Nikogo nie dyskryminuję :wink:). Stalker(-ka) chce się dowiedzieć, gdzie mieszka ofiara. Ale wprost nie zapyta, żeby nie budzić podejrzeń i&nbsp;nie zostawiać śladów.

Czeka zatem do okolic sesji, żeby mieć pretekst. Oczywiście może też łapać dowolny inny dzień, jeśli ofiara się wygadała, że będzie wtedy w&nbsp;domu.

Potem pisze przez Messengera:

<blockquote>
<p>
<strong>Stalker(-ka):</strong> Hej, podeślesz mi jakieś notatki z&nbsp;zeszłego tygodnia?<br/>
<strong>Ofiara:</strong> Hej, pewnie :) Nie mam tylko z&nbsp;wykładu z&nbsp;X, bo mnie nie było.
</p>
<p class="post-meta">
(Robi zdjęcia telefonem i&nbsp;przesyła przez Messengera; ale ten automatycznie usuwa dane EXIF).
</p>
<p>
<strong>S:</strong> Dzięki! ^_^<br/>
<strong>S:</strong> <em>(Po chwili)</em> A&nbsp;możesz mi przesłać na maila? Jeśli to nie kłopot :p Chcę sobie wydrukować, a&nbsp;FB zmniejsza.
</p>
<p class="post-meta">
(Faktycznie zmniejsza, więc jest wiarygodna wymówka. Ale chodzi głównie o&nbsp;to, że oryginały wysłane na maila już będą miały metadane)
</p>
<p>
<strong>S:</strong> Na <em>some_stalker@randomail.com</em><br/>
<strong>O:</strong> <em>(Wysyła maila)</em> Poszło, masz? :)<br/>
<strong>S:</strong> Jest, dzięki!!<br/>
<strong>S:</strong> Stawiam Ci piwo następnym razem :)
</p>
</blockquote>

W ten sposób stalker(-ka) zdobywa zdjęcia z&nbsp;kompletem metadanych, wykonane w&nbsp;domu przyszłej ofiary. Nie budząc jej podejrzeń.

Sprawdza zdjęcie... i&nbsp;sukces! Znaczniki lokalizacji były włączone. Nawet jeśli stalker(-ka) nie umie programować, może przepisać koordynaty i&nbsp;wpisać je w&nbsp;mapy, tak jak zademonstrowałem.

Znacznik pojawia się na działce obok domu jednorodzinnego pod miastem, w&nbsp;którym studiują. Bingo! Kolejna część planu to osobiste odwiedziny :smiling_imp: Resztę zostawiam waszej wyobraźni.

Brzmi realnie? To mogłoby przydarzyć się nam wszystkim. I&nbsp;nawet byśmy nie wiedzieli, skąd ktoś wziął o&nbsp;nas informacje. Moglibyśmy myśleć, że ktoś znajomy się wygadał.

Kiedy przesyłamy zdjęcia na jakąś stronę, to nigdy nie wiemy, czy usunie z&nbsp;nich metadane. A&nbsp;nawet jeśli zwykle usuwa, to czy mamy jakąś gwarancję? Jakiś praktykant może coś popsuć w&nbsp;systemie i&nbsp;przez chwilę będzie działało inaczej.

Nawet komunikator stawiający na prywatność, Signal, nie usuwał kiedyś metadanych! Co stało się zresztą [przedmiotem żywej dyskusji](https://github.com/signalapp/Signal-iOS/issues/1984) (o numerze, o&nbsp;ironio, *1984*).

Ta dyskusja zawiera zresztą komentarze, które uczą nas ciekawych rzeczy:

1. Nawet jeśli dbasz o&nbsp;prywatność, twoja lokalizacja może się wydać przez cudzego selfiaka. Nawet jeśli jesteś Johnem *Wickiem*{:.corr-del}McAfee, znaną postacią w&nbsp;świecie cyberbezpieczeństwa.

   > the threat exists in many situations, including passing along an image received from someone else. (For example, John McAfee's location while in hiding was revealed precisely this way.)

2. Znasz się na technologii? Zawsze może być ten jeden raz, kiedy opuścisz gardę:

   > I'm also reminded of the story of Higinio O. Ochoa III, a&nbsp;hacker that got caught because he used software to remove the EXIF data from an image he wanted to upload, but then accidentally uploaded the original. Even when you know about EXIF, you could still screw up.

Tyle dowodów chyba wystarczy -- metadane mogą być pułapką. Jeśli nie chcemy upublicznić miejsca, w&nbsp;którym robiliśmy zdjęcia, to najlepiej własnoręcznie wyłączyć znaczniki lokalizacji i&nbsp;usunąć te istniejące. *„You've got to be your own hero...”*, jak mawiają infantylne memy. Już pokażę, jak można to zrobić.

## Jak wyłączać i&nbsp;usuwać dane o&nbsp;lokalizacji

# Wyłączanie geotagowania

Na początek wyłączmy dodawanie znaczników lokalizacji. Pokażę na przykładzie swojego smartfona (Huawei, Android 10). W&nbsp;innych urządzeniach może to wyglądać nieco inaczej. Nawet tradycyjne aparaty cyfrowe mogą dodawać znaczniki!

Prawie zawsze gdzieś w&nbsp;opcjach będzie „pstryczek” mówiący coś o&nbsp;lokalizacji. To jego najłatwiej wyłączyć, żeby nas nie tagowało. W&nbsp;przypadku mojego telefonu miałem coś takiego w&nbsp;menu aplikacji Aparat (pod ikoną koła zębatego):

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/tel_aparat_ustawienia_znacznika.webp" alt="Menu z ustawieniami aplikacji Aparat na telefonie. Dorysowany czerwony kwadrat otacza opcję znaczników lokalizacji, którą można włączać lub wyłączać suwakiem.">

Tyle na poziomie aplikacji. Ale z&nbsp;nimi różnie bywa, dla pewności warto też użyć pstryczków systemowych.

Nowsze Androidy pozwalają ustawić szczegółowe pozwolenia aplikacjom. Wszedłem w&nbsp;`Ustawienia` z&nbsp;głównego ekranu, potem `Prywatność` i&nbsp;`Menedżer uprawnień`. Tam miałem zakładkę `Lokalizacja` z&nbsp;ikoną znacznika. Po wejściu w&nbsp;nią mogłem poblokować aplikacjom, w&nbsp;tym Aparatowi, dostęp do danych GPS-a:

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/tel_uprawnienia_aparatu.webp" alt="Ekran Menedżera Uprawnień systemu Android. Widać na nim nagłówek 'Lokalizacja', ikonę aplikacji 'Aparat' oraz trzy opcje: włączenie, włączenie tylko podczas korzystania albo wyłączenie.">

A jeśli chcemy ostatecznie dobić GPS-a, to można też wyłączyć lokalizację dla całego telefonu. W&nbsp;moim przypadku po powrocie do głównego ekranu dało się paroma ruchami „ściągnąć” menu z&nbsp;góry, jak żaluzję. Tam był przełącznik:

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/tel_wylaczona_lokalizacja.webp" alt="Menu główne Anroida, z ikonami odpowiadającymi różnym funkcjom. Dorysowany czerwony prostokąt otacza ikonę znacznika GPS, podpisaną 'Lokalizacja' i mającą szary kolor (co oznacza, że opcja jest wyłączona).">

...I zrobione. O&nbsp;ile nasz system nie jest nieposłuszny lub nie ma jakiejś poważnej luki, to od teraz zdjęcia nie będą zawierały informacji od GPS-a.

# Usuwanie metadanych

Dla każdego systemu wygląda to nieco inaczej.

**Windowsa** już pokazałem -- w&nbsp;tym wypadku otwieracie okno z&nbsp;informacjami o&nbsp;zdjęciu (prawy przycisk na pliku, `Właściwości`, zakładka `Szczegóły`). Potem klikacie na dole opcję `Usuń właściwości oraz informacje osobiste`. I&nbsp;już, metadane znikną!

Dla **Androida** znalazłem porady, które jednak się nie sprawdziły.  
Według nich można otworzyć zdjęcia w&nbsp;domyślnej Galerii, przytrzymać palcem na jednym z&nbsp;nich, żeby pokazały się opcje. W&nbsp;dolnym prawym rogu mamy `Więcej`, a&nbsp;potem `Szczegóły`. Tylko że powinna tu być opcja edycji, a&nbsp;u mnie się nie pojawiła.  
Rozwiązaniem może być apka. Na Reddicie, w&nbsp;wątkach poświęconych prywatności, mignął mi czasem Scrambled Exif.

W kwestii **urządzeń od Apple'a** nie jestem w&nbsp;temacie, ale [ten wpis](https://www.canto.com/blog/remove-metadata-from-photo/) wydaje się solidnym poradnikiem. Reddit poleca również apkę Exif Viewer na iOS.

Z **Linuxami** to pewnie zależy. Mój Mint nie daje domyślnej możliwości usuwania metadanych, więc robiłbym to skryptami (w praktyce nic nie muszę, bo geolokalizacja wyłączona).

## Podsumowanie

Jeśli poprzednio nie wiedzieliście o&nbsp;metadanych, to mam nadzieję, że porcja faktów z&nbsp;tego wpisu wypełniła tę lukę. Nawet jeśli nie planujemy marszu na kapitol ani wysyłania notatek stalkerom, zawsze to jakaś wiedza na przyszłość.

Może przez słuchanie o&nbsp;takich rzeczach tracimy nieco beztroski... ale zyskujemy możliwość brania swoich spraw i&nbsp;danych we własne ręce. Nie ma co żyć beztrosko, kiedy można świadomie!

Aha, i&nbsp;mówiłem na początku, że będzie historyjka z&nbsp;morałem? No to morał:

<div class="black-bg">
Tnij EXIF do zera – nie będzie dla stalkera.
</div>

Z najprzystępniejszych informacji to tyle, dzięki za lekturę! :smile:

A jeśli nie boicie się skryptów, to mam dla Was dwa. Możecie dzięki nim przeglądać i&nbsp;usuwać dane EXIF w&nbsp;wielu zdjęciach naraz, w&nbsp;ciągu paru sekund i&nbsp;na każdym systemie, na jakim działa Python (czyli praktycznie na wszystkich poza mobilnymi (chociaż na Androidzie też się da z&nbsp;odrobiną gimnastyki)).

W takim wypadku czytajcie dalej!

## Bonus: skrypty do sprawdzania i&nbsp;usuwania metadanych

Zanim użyjecie skryptów, trzeba zdobyć Pythona i&nbsp;jeden moduł pomocniczy. Omawiam tu proces dla Windowsa, ale zasady działania dla pozostałych systemów są takie same:

* [Pobierzcie Pythona](https://www.python.org/downloads/) z&nbsp;oficjalnej strony.

   Proces jest bezbolesny, na stronie powinno samo Wam podpowiedzieć najnowszą wersję.  
   Podczas instalacji pamiętajcie o&nbsp;kilku rzeczach:

     * Kiedy zapyta o&nbsp;instalowanie dodatkowych rzeczy, to **zaznaczcie _pip_**;
     * W&nbsp;tym samym oknie najlepiej **zaznaczcie _tcl/tk i&nbsp;IDLE_**;
     * Zaznaczcie **dodaj Pythona do zmiennych środowiskowych** (czy coś w&nbsp;tym stylu).

* Otwórzcie PowerShella. Żeby to zrobić, możecie wejść do menu `Start` w&nbsp;lewym dolnym rogu, zacząć pisać *pow...*, a&nbsp;w podpowiedziach wyskoczy PowerShell.

* Wpiszcie w&nbsp;PowerShella `pip install pillow`.

  *pillow* to inaczej *PIL* -- biblioteka do przetwarzania obrazków. Python nie ma czegoś takiego w&nbsp;pakiecie, więc trzeba pobrać z&nbsp;zewnątrz. Żeby to zrobić, musicie mieć połączenie z&nbsp;internetem.  
   Boicie się instalować nieznane rzeczy z&nbsp;sieci? Bardzo słusznie! :+1: Warto najpierw sprawdzić [oficjalną stronę tej biblioteki na PyPI](https://pypi.org/project/Pillow/), a&nbsp;z niej przejść na [stronę z kodem źródłowym](https://github.com/python-pillow/Pillow).  
I tak bez odrobiny zaufania się nie obejdzie, ale prawie 8200 gwiazdek (pozytywnych ocen) jest jakąś rekomendacją.  
Całe okno po zainstalowaniu PIL-a powinno wyglądać tak:

{:.figure .bigspace}
<img src="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/pip.webp" alt="Obrazek pokazujący okno programu Powershell. W jednej z linijek wpisana komenda 'pip install pillow', pod spodem wypełniony pasek ładowania i informacja, że pobrano 1,9 MB i zainstalowano bibliotekę PIL.">

* Oprócz tego przyda Wam się jakiś obrazek z&nbsp;metadanymi. Możecie na przykład użyć <a href="/assets/skrypty/krs_visualizer.py" download>tego mojego z&nbsp;Katowic</a>.

* Warto też stworzyć osobny folder na testowane obrazki.  
  Jeszcze lepiej by było użyć osobnego komputera / maszyny wirtualnej, jak przy każdym nieznanym kodzie... No ale wiem jak jest.

Teraz macie już wszystko co potrzebne, można odpalać skrypciory :sunglasses:

# Sprawdzanie metadanych

Tak jak pokazywałem, czasem system domyślnie pozwala nam zajrzeć w&nbsp;metadane. Ale skryptem można to zrobić szybciej, przyjemniej i&nbsp;w taki sam sposób na różnych komputerach.

{% include pyscript.html name="get_exif.py" link="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/skrypty/get_exif.py" external="True" info="
<p>Wrzućcie go do tego samego folderu co obrazki, które chcecie sprawdzić. Następnie otwórzcie go w&nbsp;IDLE i&nbsp;odpalcie, np. naciskając <code>F5</code> (wszystko opisałem w podstawowym samouczku, link wyżej).</p>
<p>Aby skrypt działał, trzeba zainstalować moduł dodatkowy <code>pillow</code> (opisałem to dokładniej w&nbsp;drugim podlinkowanym samouczku).</p>
<p>Jeśli wszystko dobrze poszło, po odpaleniu skryptu <strong>w tym samym folderze</strong> powstanie plik <i>metadane_exif.txt</i>.</p>
<p>W&nbsp;tym pliku wyróżnionymi nagłówkami będą nazwy obrazków, w&nbsp;których znaleziono metadane. Pod każdym nagłówkiem będzie ich dokładna lista. A&nbsp;także, w&nbsp;przypadku znalezienia danych z&nbsp;GPS-a, położenie przeliczone na jednostki dziesiętne:</p>
<div class='black-bg mono'>
<p>LOKALIZACJA:<br/>50.265216827222226, 19.01945304861111</p>
</div>
"%}

Wystarczy taką linijkę z&nbsp;liczbami zaznaczyć, skopiować i&nbsp;wkleić na stronkach z&nbsp;mapami :wink: Dowiecie się, ile zdradzają o&nbsp;Was zdjęcia -- zanim wpadną w&nbsp;niepowołane ręce.

# Usuwanie metadanych

Zanim pokażę skrypt -- odrobina historii.

Umiem tylko w&nbsp;Pythona, więc wyszukałem `python how to remove exif`. Wyskoczyły mi [wyniki](https://duckduckgo.com/?q=python+how+to+remove+exif).  
I pierwszy od góry był tradycyjnie [wątek z&nbsp;forum StackOverflow](https://stackoverflow.com/questions/19786301/python-remove-exif-info-from-images). Jedna z&nbsp;odpowiedzi sugerowała użycie takiego kodu:

```python
from PIL import Image
image = Image.open('path/to/image')
image.save('new/path/' + file_name)
```

Trzy linijki. I&nbsp;to nawet nie osobna, wyspecjalizowana komenda, tylko najzwyklejsze załadowanie i&nbsp;ponowne zapisanie obrazka (a metadane gubi po drodze).

Może autorzy PIL-a to geniusze? A&nbsp;może trochę leniuchy, których programy olewają grę wstępną z&nbsp;metadanymi i&nbsp;od razu lecą do bitów obrazka?

W każdym razie fakt pozostaje faktem: **trzy linijki wystarczyły, żeby usunąć dane** i&nbsp;żeby do całej sprawy nie doszło. Takie coś mogło ocalić przed problemami użytkowników Parlera. I&nbsp;pewnie wiele innych osób, może budzących większą sympatię.

OK. Chwila refleksji była, teraz skrypt.

{% include pyscript.html name="remove_exif.py" link="/assets/posts/gdzie-jestem-zapytaj-moich-zdjec/skrypty/remove_exif.py" external="True" info="Instrukcja:
<p>Tak jak poprzednio, wystarczy go upuścić w&nbsp;tym samym folderze co zdjęcia, najlepiej pobieżnie przejrzeć i&nbsp;odpalić.<br/>
Do działania potrzebuje modułu dodatkowego <code>pillow</code> (opis instalacji wyżej).</p>
<p>Skrypt nie nadpisuje zdjęć (żeby przypadkiem czegoś nie usunąć), tylko tworzy ich kopie. W&nbsp;podfolderze o&nbsp;nazwie <code>Bez_metadanych</code>.</p>
<p>Stąd uwaga: gdybyście chcieli odpalić go w&nbsp;folderze, w&nbsp;którym znajduje się dużo ciężkich zdjęć, to sprawdźcie wcześniej ilość miejsca na dysku.</p>"%}

Tak „wykastrowane” zdjęcia z&nbsp;podfolderu można z&nbsp;czystym sumieniem wrzucać w&nbsp;sieć. 

{% include info.html type="Ciekawostka" text="A może jednak nie do końca?  
 Metadane to nie wszystko, namierzyć da się również po elementach widocznych na zdjęciu. Pewien japoński stalker ustalił miejsce pobytu idolki na podstawie [obrazu stacji kolejowej odbitego w&nbsp;jej oczach](https://www.bbc.com/news/world-asia-50000234)."%}

I tym akcentem kończę dzisiejsze przemyślenia o&nbsp;metadanych i&nbsp;stalkerach. Do zobaczenia przy kolejnych okazjach! :smile:
