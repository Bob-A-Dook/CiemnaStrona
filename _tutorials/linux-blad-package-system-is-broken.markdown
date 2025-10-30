---
layout: page
title: "Linux i błędy „Package system is broken” oraz „Unmet dependencies”"
description: "Zapchane rury na styku programów APT i DPKG"
---

Przedstawiam kolejny mikroporadnik poświęcony konkretnemu, irytującemu problemowi, z&nbsp;jakim mogą się czasem zetknąć osoby korzystające z&nbsp;otwartych systemów na bazie Linuksa.

Dzisiaj będzie o&nbsp;tytułowych komunikatach z&nbsp;błędem, które następują podczas próby instalacji programów. Wynikają z&nbsp;niekompletnej instalacji w&nbsp;przeszłości i&nbsp;pojawiają się rzadko, ale mogą skutecznie popsuć przyjemność korzystania z&nbsp;Linuksa.

Ostatnio spotkałem taki błąd podczas próby zainstalowania [polskich pakietów językowych](/tutorials/linux-mint-jezyk-polski-system){:.internal} przez dość przyjemny interfejs systemu Linux Mint. Najpierw poprawnie zaktualizował swoje informacje (*cache*), a&nbsp;potem rzucił mi w&nbsp;twarz takim komunikatem grozy:

{:.figure .bigspace}
<img src="/assets/tutorials/linux-blad-unmet-dependencies/linux-dpkg-package-system-broken.png" alt="" />

> The package system is broken  
Check if you are using third party repositories. If so disable them...

Brzmi to złowieszczo, tak jakby coś się strasznie popsuło.

I można odnieść wrażenie, że faktycznie tak jest. Gdyby po ujrzeniu błędu spróbowało się zainstalować jakikolwiek pakiet z&nbsp;zewnątrz przez konsolę (`apt install PAKIET`), to pewnie też wyskoczyłby błąd:

<div class="black-bg mono bigspace red post-meta">
Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a&nbsp;solution).
</div>

To może instalacja ręczna? Przez pobranie z&nbsp;sieci i&nbsp;dwukrotne kliknięcie pliku `.deb`?  
Również enigmatyczny błąd (na Mincie wyświetli nam go program Captain, odpowiedzialny za obsługę takich plików):

> Broken dependencies  
To fix this run 'sudo apt-get install -f' in a&nbsp;terminal window.

Nie było to moje pierwsze spotkanie z&nbsp;tym błędem. Ale tym razem miałem więcej motywacji, żeby dokładniej go poznać. I&nbsp;pokonać.

{% include info.html
type="Uwaga"
text="Piszę z&nbsp;perspektywy użytkownika systemu Linux Mint, ale intuicja podpowiada, że wiele przemyśleń powinno mieć przełożenie na inne Linuksy oparte na Debianie, jak Zorin czy Ubuntu. Nie mogę tego jednak zagwarantować.  
Ponadto w&nbsp;moim przypadku błąd wynikał z&nbsp;tego, że podczas próby pierwszej instalacji nie miałem potrzebnych plików (zależności). Przy innych przyczynach opisane tu rozwiązanie może się nie sprawdzić."
%}

## Spis treści

* [Zasięg i&nbsp;waga błędu](#zasięg-iwaga-błędu)
* [Przyczyna błędu](#przyczyna-błędu)
* [Rozwiązanie 1: podążanie za instrukcjami spod błędu](#rozwiązanie-1-podążanie-za-instrukcjami-spod-błędu)
* [Rozwiązanie 2: użycie graficznego Menedżera Oprogramowania](#rozwiązanie-2-użycie-graficznego-menedżera-oprogramowania)
* [Rozwiązanie 3: reset stanu DPKG](#rozwiązanie-3-reset-stanu-dpkg)
* [Parę słów na koniec](#parę-słów-na-koniec)

## Zasięg i&nbsp;waga błędu

Jak pokazałem wyżej -- jeśli błąd pojawi się w&nbsp;jednym miejscu, to od momentu wystąpienia zapewne **pojawi się przy każdej kolejnej próbie instalacji czegoś z&nbsp;zewnątrz**.

Nieważne, czy instalujemy przez interfejs graficzny, czy konsolę. Możemy nawet sięgać po całkiem inne, niezwiązane pakiety. Prawie wszystko skończy się błędem.

{:.post-meta .bigspace-after}
Istnieje wyjątek, również wśród wbudowanych programów; będzie wymieniony przy rozwiązaniach.

Co gorsza, błąd na pewno występuje na Mincie, a&nbsp;prawdopodobnie również na Ubuntu czy Zorinie. Wszystkie te odmiany Linuksa są popularne i&nbsp;często polecane osobom migrującym z&nbsp;Windowsa (co jest teraz [na czasie](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}).

Wszystkie te cechy sprawiają, że warto wziąć błąd na cel, spróbować go zrozumieć i&nbsp;rozbroić. Co niniejszym zrobię.

## Przyczyna błędu

Wymieniłem wyżej kilka popularnych systemów, których dotyka błąd. Ich wspólny mianownik? Wykorzystują do instalacji **znane programy, APT oraz DPKG**.

Na takich systemach programy dzielą się odpowiedzialnością:

* Jest jakaś przystępna graficzna nakładka, pozwalająca instalować różne rzeczy (są nią m.in. ustawienia pakietów językowych z&nbsp;pierwszego screena).
* APT to program, któremu takie graficzne nakładki podzlecają różne zadania. Odpowiada za pobieranie rzeczy (zwykle plików DEB) z&nbsp;internetu oraz wydawanie poleceń DPKG.
* DPKG to wykonawca najniższego szczebla, który odczytuje z&nbsp;plików DEB ich rolę, po czym umieszcza je w&nbsp;odpowiednich miejscach, integrując je z&nbsp;systemem.

Po wystąpieniu błędu nieco poeksperymentowałem i&nbsp;doszedłem do wniosku, że **wynika on z&nbsp;niedokończonych spraw podczas poprzedniej instalacji**.

Był sobie jakiś etap pierwszy, kiedy próbowałem zainstalować pakiet. Jaki? W&nbsp;sumie nieistotne; ważniejszy jest fakt, że instalacja nie doszła do skutku. W&nbsp;zapiskach DPKG pakiet pozostał niedokończonym zadaniem.

Później -- może nawet znacznie później -- nastąpił etap drugi. Spróbowałem zainstalować pakiet językowy przez graficznego instalatora („program od języków”). I&nbsp;tu nastąpił swoisty głuchy telefon:

* program od języków poprosił APT-a o&nbsp;instalację wskazanego pakietu;
* APT zapytał DPKG o&nbsp;aktualny stan rzeczy;
* usłyszał w&nbsp;odpowiedzi o&nbsp;niewykonanych zadaniach;
* zamiast sprawdzić, czy stoją na drodze obecnego zadania -- *spanikował i&nbsp;wyemitował konkretny błąd*{:.red} `Unmet dependencies` („niespełnione zależności”);
* program od języków odebrał ten błąd -- a&nbsp;że nie ma wbudowanej dokładnej obsługi błędów, to wrzucił go do zbiorczego wora o&nbsp;apokaliptycznej nazwie `Package system is broken`.

<img src="/assets/tutorials/linux-blad-unmet-dependencies/mint-blad-package-system-geneza.png" alt="Schemat pokazujący z&nbsp;użyciem strzałek przepływ informacji między programami. Zaczyna się od interfejsów graficznych (przycisku oraz konsoli). Stamtąd strzałki prowadzą do programu APT, od niego do DPKG. Do APT-a prowadzi z&nbsp;powrotem żółta strzałka. Ostatnią strzałką jest czerwona, prowadząca od APT-a do ikony błędu."/>

Wiele różnych programów zderzało się z&nbsp;błędem, bo jego źródłem jest APT, do którego kieruje się większość zadań związanych z&nbsp;instalacją. Program od języków dodawał do tego własną eskalację, ale pierwotnym błędem pozostaje tu `Unmet dependencies`.  
Za faktyczne źródło problemu uważam natomiast **alergiczną reakcję APT-a na dawne niedokończone zadania DPKG**.

{:.post-meta .bigspace-after}
Moim zdaniem -- spora wada z&nbsp;punktu widzenia codziennej używalności. Ale zakładam optymistycznie, że wrażliwość ma jakieś uzasadnienie. Może np. pozwala łatwiej zaradzić błędom na serwerach?

{% include details.html summary="Jak celowo wywołać błąd" %}

{:.bigspace-before}
Użyję tutaj sposobu konsolowego, bo niektóre graficzne interfejsy są dość odporne i&nbsp;trudniej celowo coś popsuć. Dlatego najpierw uruchamiam sobie konsolę skrótem `Ctrl+Alt+T`.

Na początku warto zaktualizować listę dostępnych źródeł:

```
sudo apt update
```

Następnie należy pobrać **sam plik główny jakiegoś większego pakietu**, niewystarczający do pełnej instalacji. Może być taki:

<div class="black-bg mono nospace">
apt-get download kde-spectacle
</div>

{:.figcaption}
Spectacle to narzędzie do screenshotów typowe dla systemów opartych na KDE. Wiele innych korzysta z&nbsp;Gnome'a, więc instalacja na nich wiązałaby się z&nbsp;pobraniem mnóstwa rzeczy.

To ważne, żeby użyć w&nbsp;tym miejscu `apt-get` -- sam `apt` pobrałby cały pakiet razem z&nbsp;jego zależnościami, zaś użyty program jest aktualnie „głupszy” i&nbsp;pobiera jedynie plik główny, niewystarczający do działania.

Następnie można spróbować zainstalować pobrany większy pakiet:

```
sudo dpkg -i kde*.deb
```

Wyskoczy nasz błąd `Unmet dependencies`, związany z&nbsp;brakiem **zależności**. Innych pakietów, mniejszych lub większych, na których opiera się ten instalowany. A&nbsp;ten błąd, jak już widzieliśmy, blokuje wiele innych metod instalacji.

{% include details-end.html %}

{% include details.html summary="Ciekawostki na temat błędu" %}

{:.bigspace-before}
Jeśli już pojawi nam się błąd -- wywołany celowo albo nieświadomie -- to można go sobie poanalizować. I&nbsp;potwierdzić sobie empirycznie, że błąd **zachodzi na styku APT-a i&nbsp;DPKG. Przestaje zachodzić, gdy tylko jeden z&nbsp;nich jest w&nbsp;grze**.

Jak już wiemy, dotyka wielu rzeczy:

* gdyby spróbowało się zainstalować jakiś pakiet językowy, to wyskoczy groźny komunikat wspomniany na początku;
* gdyby dwukrotnie kliknąć jakiś plik DEB, to Captain wyświetli błąd;
* gdyby spróbować coś zainstalować konsolowo, np. `apt install xclip` -- błąd.

Gdyby natomiast użyć polecenia:

```
apt download xsel
```

...To APT pobierze wskazany programik. Bez żadnego błędu -- bo samo pobieranie nie wymaga interakcji z&nbsp;DPKG.

Można teraz użyć „czystego” DPKG do zainstalowania pobranego pliku DEB:

```
sudo dpkg -i xsel*.deb
```

Wyświetli się informacja o&nbsp;poprawnym zainstalowaniu, zaś `xsel` powinien normalnie działać w&nbsp;konsoli. Bo to APT był panikarzem, zaś w&nbsp;takich interakcjach nie bierze udziału.

Nie traktowałbym tej właściwości jak jakiegoś sposobu na rozwiązanie błędu. Ale potencjalne obejście? Być może.

{:.post-meta}
Co ciekawe: nawet jeśli po omówionej tu ręcznej instalacji kliknie się dwukrotnie plik DEB od programu `xsel`, to nadal wyskoczy błąd. Bo dotyczy tamtej dawnej, wcześniej niezakończonej instalacji innego pakietu.

{% include details-end.html %}

Problem opisany, to czas na jego rozwiązanie.

## Rozwiązanie 1: podążanie za instrukcjami spod błędu

O ile sam błąd brzmi groźnie, o&nbsp;tyle w&nbsp;każdym z&nbsp;omawianych tu przypadków było proponowane jakieś rozwiązanie. Program od instalacji pakietów językowych wyświetla na przykład:

{:.bigspace}
> run the following command in a&nbsp;Terminal: apt-get install -f

Trochę mnie drażni taka porada w&nbsp;graficznym programie, bo skoro już ktoś używa takiej nakładki, to może reagować na konsolę bardziej alergicznie niż APT na niedokończone sprawy DPKG. Poza tym utrwala to stereotyp, że na Linuksie bez niej ciężko.

No ale ten jeden raz można się przełamać. Konsolę można uruchomić kombinacją `Ctrl+Alt+T`, można też ikonką z&nbsp;dolnego paska. Następnie można tam wpisać podany tekst:

<div class="black-bg mono nospace">
apt-get install -f
</div>

{:.post-meta .bigspace-after}
Osoby spostrzegawcze mogą zauważyć, że przy tym samym błędzie w&nbsp;konsoli była zalecana ciut inna komenda: `apt --fix-broken install`. Są to synonimy.

...Gdyby ktoś jednak nacisnął teraz `Enter`, wykonując (ang. *run*) całe polecenie, to zderzyłby się z&nbsp;błędem:

<div class="black-bg mono post-meta red bigspace">
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)<br/>
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
</div>

Informacja zawiera wprawdzie mocną sugestię co do przyczyny (`are you root?`), ale nie sądzę, żeby to pojęcie było znane wielu osobom. A&nbsp;zatem -- kolejny wybój na drodze, konieczność zapoznania się z&nbsp;linuksową terminologią, utrwalenie stereotypu.

W każdym razie, po ludzku, **_root_ oznacza administratora**. Potrzebujemy większych uprawnień, bo polecenie zmieni parę rzeczy w&nbsp;plikach systemowych. Żeby je sobie nadać, trzeba dopisać `sudo` na początku komendy:

```
sudo apt-get install -f
```

{:.post-meta .bigspace-after}
Żeby jednak oddać sprawiedliwość Mintowi -- taki program Captain, aktywujący się po kliknięciu plików DEB, jest bardziej pomocny i&nbsp;podsuwa komendę już zawierającą `sudo`.

Powinna się wyświetlić informacja, że w&nbsp;kolejce na instalację czekają różne pakiety, a&nbsp;także pytanie, czy chcemy pobrać X&nbsp;megabajtów, które zajmą Y&nbsp;miejsca na dysku.

Można to potwierdzić klawiszem `Y`, po czym nacisnąć `Enter`. Zaczną się instalować różne rzeczy -- i&nbsp;jest spora szansa (zwłaszcza jeśli mamy te same błędy), że po tym wszystkim `dpkg` się odkorkuje, zaś instalowanie różnych rzeczy zacznie działać.

## Rozwiązanie 2: użycie graficznego Menedżera Oprogramowania

Linux Mint zawiera zestaw różnych przydatnych programów. Jednym z&nbsp;nich jest Menedżer Oprogramowania.

To właściwie graficzna nakładka na APT-a, pozwalająca przeglądać bazy programów oraz je instalować. Coś jak linuksowy odpowiednik Play Store'a (choć tego drugiego nie lubię i&nbsp;uważam za [narzędzie monopolizacji](/google/2025/10/02/google-play-store-weryfikacja-tozsamosci){:.internal}).

Menedżer zapewnia również coś znacznie cenniejszego niż graficzny intefejs -- potrafi wyłapywać przypadki błędów i&nbsp;nie rozsypać się jak konsolowy `apt` czy interfejs od języków. Zamiast tego wykonuje zakulisowo kroki potrzebne do uporządkowania sytuacji.

W praktyce: jeśli otworzymy Menedżera i&nbsp;klikniemy przycisk `Install` przy **dowolnym systemowym pakiecie** (nawet najmniejszym), to wyświetli listę zakolejkowanych pakietów oraz pytanie o&nbsp;zgodę na ich zainstalowanie.

{:.bigspace-before}
<img src="/assets/tutorials/linux-blad-unmet-dependencies/mint-software-manager-naprawa-dpkg.png" alt=""/>

{:.figcaption}
Komunikat nie wspomina, że to pliki, których zabrakło podczas nieudanej instalacji KDE, a&nbsp;nie coś związanego z&nbsp;aktualnie wybranym (którym był tu malutki `xclip`).

Jeśli ją wyrazimy, to pliki zostaną pobrane. Odkorkuje to DPKG i&nbsp;zażegna irytujące komunikaty również dla wszystkich pozostałych metod instalacji.

## Rozwiązanie 3: reset stanu DPKG

Oba poprzednie rozwiązania wymagały zainstalowania tego, co się zakolejkowało. Ale co, jeśli nie chcemy niczego instalować? Bo na przykład uznaliśmy, że utknięte pakiety są nam niepotrzebne albo ich instalacja powodowałaby inny błąd?

W takim wypadku przydałoby się zacząć z&nbsp;czystą kartą. Powiedzieć DPKG: „Mistrzu, wywalamy te pliki. Tych plików nie ma”.

Te, czyli które? Warto sobie na początku ustalić, który pakiet nas blokuje. Można przykładowo spróbować zainstalować losowy program:

```
sudo apt install xclip
```

Wyskoczy oczywiście komunikat o&nbsp;błędzie. Przewijając go do początku, można znaleźć informację:

<div class="black-bg mono bigspace post-meta">
The following packages have unmet dependencies:<br/>
 PAKIET
</div>

Ten konkretny pakiet można następnie spróbować wyczyścić poleceniem konsolowym:

```
sudo dpkg --purge --force-all PAKIET
```

Po usunięciu pakietu blokującego kolejkę instalacja innych rzeczy powinna zacząć działać. O&nbsp;ile mieliście ten sam rodzaj błędu co w&nbsp;moim przypadku.

{% include details.html summary="Więcej informacji" %}

{:.bigspace-before}
W każdej chwili można sobie zajrzeć do pliku, w&nbsp;którym `dpkg` przechowuje informacje na temat stanu różnych swoich pakietów. Jego ścieżka to:

{:.post-meta}
```
/var/lib/dpkg/status
```

Plik można otworzyć w&nbsp;dowolny sposób, choćby przez zwykły linuksowy odpowiednik Notatnika. Dla sytuacji z&nbsp;mojego przykładu znaleźlibyśmy taką informację:

{:.post-meta}
```
Package: kde-spectacle
Status: install ok unpacked
```

Byłby to jedyny plik spośród pakietów znanych DPKG, który ma stan `unpacked` (inne miały u&nbsp;mnie `installed`). Pozwala to łatwo go wyodrębnić jako plik do usunięcia.

Gdyby ktoś kiedyś trafił na dziwniejszą sytuację niż ta względnie jasna u&nbsp;mnie, to zawsze można się wspomagać takimi informacjami i&nbsp;ustalić, gdzie tkwi źródło problemu.

{% include details-end.html %}

{:.post-meta}
Za rozwiązanie dziękuję [tej odpowiedzi ze Stacka](https://stackoverflow.com/a/73444413).

## Parę słów na koniec

Błąd omówiony w&nbsp;tym wpisie może być bardzo irytujący dla codziennych użytkowników, wpychając ich w&nbsp;labirynt niejasnych komunikatów i&nbsp;poleceń konsolowych. Co gorsza, dotyka Linuksów szczególnie polecanych dla grona mniej konsolowego.

Ze względu na te cechy zaliczyłbym błąd do poważniejszych zadziorów, wartych oszlifowania. Może przez autorów Linuksów, może przez ekipę od programów APT i&nbsp;DPKG.

Oto parę luźnych przemyśleń na temat tego, co mógłby zyskać system, żeby wszystko działało w&nbsp;sposób przyjaźniejszy użytkownikom:

* w&nbsp;razie zakorkowania programu DPKG przez jakiś pakiet -- wyraźne diagnozowanie problemu i&nbsp;prosta opcja wyczyszczenia pliku, bez konieczności użycia konsoli;
* automatyczne pobieranie pakietu innym kanałem, jeśli wewnątrz DPKG „utknął” tylko pakiet niezwiązany z&nbsp;obecnie instalowanym;
* wyraźniejsze informowanie przez Menedżera Oprogramowania, że zakolejkowane pliki dotyczą innego pakietu niż ten, który próbujemy instalować;
* lepsze rozpoznawanie błędów na Mincie i&nbsp;niewrzucanie ich do wspólnego worka (albo przynajmniej do worka o&nbsp;mniej groźnej nazwie);
* jeśli już musi być konsola, to niech polecana komenda od razu zawiera `sudo` na początku (jeśli bez tego i&nbsp;tak się nie obędzie).

W wolnym czasie spróbuję ustalić, jak wygląda sprawa na różnych Linuksach i&nbsp;gdzie byłoby fajnie zgłosić propozycje.  
Jeśli na poradnik trafi osoba, która już to wie i&nbsp;ma wtyki (albo nie ma, ale po prostu chce wiecznej chwały w&nbsp;świecie *open source*) -- proszę zgłaszać śmiało :wink: Nie zależy mi na żadnym pierwszeństwie.

Publikuję poradnik z&nbsp;nadzieją, że ktoś wklei w&nbsp;wyszukiwarkę treść błędu, zobaczy tu stosunkowo łatwe rozwiązanie -- i&nbsp;dzięki temu nie zniechęci się do Linuksa, może w&nbsp;przyszłości poleci go znajomym, a&nbsp;alternatywa będzie rosła w&nbsp;siłę :smile:

{:.post-meta .bigspace-after}
W obecnych czasach: prędzej jakiś korporacyjny model językowy po prostu sobie te informacje wchłonie, przetrawi i&nbsp;zaserwuje bez podawania źródła. Niech już mu będzie, byle wieść się niosła.
