---
layout: post
title: "Usługi Google Play. Uzurpator na tronie-smartfonie"
subtitle: "Kiedyś władza należała do ciebie. Odebrali ci ją."
description: "Kiedyś władza należała do ciebie. Odebrali ci ją."
tags: [Android, Apki, Centralizacja, Inwigilacja]
firmy: [Google]
date:   2026-06-03 21:00:00 +0100
category: google
category_readable: "Google – kolorowy czarny charakter"
image:
  path: /assets/posts/google/uslugi-google-play/uslugi-google-play-uzurpator-baner.jpg
  width: 1200
  height: 700
  alt: "Kadr z anime One Piece pokazujący ciemną postać z wysoką koroną siedzącą na tronie. Na górną część tronu nałożono logo Androida, a na postać logo Usług Google Play."
---

Twój smartfon miał być twoim królestwem. Krainą możliwości, w&nbsp;której twoje słowo jest rozkazem. Chcesz uwiecznić wspomnienia aparatem albo sprawdzić drogę? Wystarczy jeden gest ręki -- jak machnięcie królewskim berłem.

Prawdziwi władcy mają wgląd w&nbsp;to, jak działa ich królestwo. Tak też było -- **system Android stworzony przez Google'a przebił się dzięki swojej otwartości**. Przyciągał majsterkujące osoby i&nbsp;wolne duchy nielubiące korporacyjnego sztywniactwa (reprezentowanego przez Microsoft).

...Ale lata mijały, a&nbsp;Android się zamykał „dla bezpieczeństwa”. Niekiedy było to tylko pretekstem do utrwalania monopolu Google'a na tańszych smartfonach.

Na powierzchni nie zmieniło się tak wiele... Ale jeśli spróbujesz ruszyć pewną aplikację zwaną **Usługami Google Play** -- to zaczną piętrzyć się problemy. Bo one, wbrew nazwie, nie usługują. Są uzurpatorem rządzącym twoim smartfonem.

> Uzurpator -- osoba, która niesłusznie uznaje, że ma prawo do jakiegoś stanowiska, tytułu, godności, funkcji

{:.figcaption}
Źródło: [słownik języka polskiego PAN](https://wsjp.pl/haslo/podglad/76513/uzurpator)

W tym wpisie będę miał (nie-)przyjemność przybliżyć Usługi, wrośnięte w&nbsp;trzewia smartfona jak złośliwy guz. Omówię też różne sposoby, w&nbsp;jakie można z&nbsp;nimi walczyć o&nbsp;władzę.

Będzie raczej powierzchownie, ale przystępnie, popularyzatorsko. Dla urozmaicenia sięgnę po porównania królewsko-zamkowe.  
Zapraszam!

{:.bigspace-before}
<img src="/assets/posts/google/uslugi-google-play/uslugi-google-play-uzurpator-baner.jpg" alt="Kadr z&nbsp;anime One Piece pokazujący ciemną postać z&nbsp;wysoką koroną siedzącą na tronie. Na górną część tronu nałożono logo Androida, a&nbsp;na postać logo Usług Google Play." />

{:.figcaption}
Źródło: anime *One Piece*, logo Androida i&nbsp;Usług Google Play. Przeróbki moje.

{% include info.html
type="Krótsza wersja"
text="Wpis jest długi, a&nbsp;zdolność do skupiania uwagi coraz rzadsza :wink:  
Jeśli ktoś woli informacje w&nbsp;pigułce, bez opisów i&nbsp;analogii, to zapraszam do [wersji skróconej](/miniposts/uslugi-google-android-same-schematy.html){:.internal}. Są tam same schematy pokazujące etapy walki o&nbsp;Androida (plus rozwijane, zwięzłe opisy)."
%}

## Spis treści

* [Usługi Google Play](#usługi-google-play)
  * [Ciemne strony Usług](#ciemne-strony-usług)
  * [Możliwości użytkowników](#możliwości-użytkowników)
* [Wyłączenie Usług i&nbsp;pierwsze kłopoty](#wyłączenie-usług-ipierwsze-kłopoty)
* [Przejęcie dolnych warstw systemu](#przejęcie-dolnych-warstw-systemu)
  * [Problem pierwszy: bootloader](#problem-pierwszy-bootloader)
  * [Potężny problem z&nbsp;Play Integrity](#potężny-problem-zplay-integrity)
  * [Wyścig zbrojeń](#wyścig-zbrojeń)
* [GrapheneOS](#grapheneos)
* [Play Integrity i&nbsp;weryfikacja sprzętowa](#play-integrity-iweryfikacja-sprzętowa)
* [Przyszłe zagrożenia](#przyszłe-zagrożenia)
* [Co można zrobić?](#co-można-zrobić)

## Usługi Google Play

Na wielu smartfonach, niezależnie od producenta, różne aplikacje od korporacji Google ([skazanego monopolisty](/google/2024/08/07/google-antymonopol-wyrok){:.internal}) są zainstalowane domyślnie i&nbsp;straszą nas od pierwszego uruchomienia. Jedną z&nbsp;nich są wspomniane Usługi Google Play.

Usługi nie istnieją w&nbsp;próżni, a&nbsp;do zrozumienia ich roli może się przydać trochę kontekstu. Dlatego mam tu schemat pokazujący sytuację na przeciętnym smartfonie z&nbsp;Androidem:

{:.bigspace-before}
<img src="/assets/posts/google/uslugi-google-play/1-android-warstwy-google-play-dziala.png" alt="Trzy warstwy systemu Android w&nbsp;trybie domyślnym, przy włączonych Usługach Google Play. Najniższa warstwa, zawierająca Usługi, oznaczona jako niedostępna."/>

{:.figcaption}
Źródła elementów użytych na schematach [pod koniec wpisu](#źródła-schematów){:.internal}.

Warstwy schematu, podpisane po prawej, odpowiadają warstwom typowego Androida. Są tu dwie przykładowe aplikacje -- Firefox oraz Sklep Google Play.
W dolnej części schematu są z&nbsp;kolei nasze Usługi -- **komunikujące się zarówno z&nbsp;apką Sklep, jak i&nbsp;korporacją Google**.


{% include details.html summary="Usługi Google Play to coś innego niż Sklep Google Play" %}

{:.bigspace-before}
Wiele osób myli te dwie rzeczy, więc pozwolę sobie wypunktować różnice:

* Sklep Google Play to nazwa *bazy aplikacji* kontrolowanej przez Google'a.

  Jest dostępna również w&nbsp;internecie pod adresem *[play.google.com](https://play.google.com)*.

* Apka o&nbsp;tej samej nazwie odpowiada za **pobieranie aplikacji z&nbsp;tej bazy**.  
  (Mówię tu o&nbsp;nazwie publicznej; wewnętrzna to `com.android.vending`).

  {:.post-meta .bigspace-after}
  Warto też wiedzieć, że za instalację odpowiada już sam Android i&nbsp;można ją wykonać na własną rękę, bez udziału Sklepu. Mimo że Google [próbuje to obrzydzać](/google/2025/10/02/google-play-store-weryfikacja-tozsamosci){:.internal}.
 
* Zarówno baza, jak i&nbsp;apka mają tę samą czterokolorową ikonę, przypominającą grot strzałki o&nbsp;zaokrąglonych wierzchołkach.
* Apka jest przeznaczona *dla użytkowników* -- ma swój interfejs, da się ją włączyć przez opcje lub ikonę na ekranie głównym itd.

**Usługi są natomiast przeznaczone dla innych aplikacji, a&nbsp;nie użytkowników**. To zbiór funkcji, z&nbsp;których inne apki (w&nbsp;tym Sklep) mogą korzystać. Mają ikonę pojedynczego czterokolorowego puzzla, zaś ich nazwa wewnętrzna to `com.google.android.gms`.

Można wprawdzie kontrolować niektóre ich zachowania przez ustawienia smartfona (zakładka `Google`), ale to jedyna część widoczna dla użytkowników. Same nie zapewniają własnego interfejsu.

{% include details-end.html %}

### Ciemne strony Usług

Usługi zapewniają [udogodnienia](https://en.wikipedia.org/wiki/Google_Play_Services), takie jak możliwość osadzania Map Google'a w&nbsp;innych aplikacjach. Ale też rzeczy patologiczne, jak **unikalny identyfikator reklamowy AAID**. Elementy śledzące, dodane przez firmy reklamowe do apek, mogą go sobie sprawdzać i&nbsp;używać do rozpoznawania użytkowników.

Takie identyfikatory, w&nbsp;połączeniu z&nbsp;danymi z&nbsp;GPS-a, są masowo przetwarzane przez brokerów i&nbsp;[rok temu im wyciekły](/2025/03/23/gravy-analytics-wyciek){:.internal}, ujawniając miliony ludzkich lokalizacji. Dlatego uważam, że absolutnie każdy powinien wyłączyć ID reklamowe (porady pod linkiem, to bardzo proste).

A to zaledwie ta najbardziej oczywista rzecz. Mając wgląd w&nbsp;fundamenty systemu -- i&nbsp;nie dając prawie żadnego wglądu w&nbsp;siebie -- Usługi mogą naruszać prywatność na znacznie więcej sposobów.

Inny przykład nadużyć? Opcja skanowania nazw oraz innych danych hotspotów wokół nas. W&nbsp;ten sposób Google może ustalić naszą lokalizację nawet przy wyłączonym GPS-ie... I&nbsp;Wi&#8209;Fi. Bo to skanowanie to [odrębna funkcja, ukryta w&nbsp;opcjach](/2024/02/03/smartfon-degoogle#wy%C5%82%C4%85czenie-ci%C4%85g%C5%82ego-skanowania-hotspot%C3%B3w){:.internal}.

{:.post-meta .bigspace-before}
Pominę już fakt, że nasz smartfon robi dla korpo darmową robotę i&nbsp;utrwala ich monopol, aktualizując im bazy hotspotów, którymi nie dzielą się publicznie.

{% include details.html summary="Analogia zamkowa" %}

{:.bigspace-before}
Na smartfonie z&nbsp;Androidem jesteśmy jak władcy teoretyczni. Siedzimy na tronie, mamy komnaty, cośtam możemy rozkazywać...

Prawdziwe życie toczy się jednak wokół komnat uzurpatora. Przychodzą do niego dziwne, zakapturzone postaci i&nbsp;wsuwają listy pod jego drzwi. W&nbsp;zamian odbierają inne, zaplombowane i&nbsp;zapewne pełne informacji o&nbsp;królestwie.

{:.post-meta .bigspace-after}
Warto zapamiętać, że nie widzą uzurpatora na oczy, tylko komunikują się pod drzwiami. Ma to spore znaczenie na późniejszych etapach.

Niejedna osoba toleruje ten stan rzeczy i&nbsp;brak realnej władzy, bo uzurpator dzieli się czasem błyskotkami. Wręcza na przykład misternie wykonane mapy, streszcza wiadomości w&nbsp;zrozumiałej postaci...

...A że zdobył te mapy, rozdając tajemnice naszego królestwa? Na zasadzie wymiany ze swoimi odpowiednikami z&nbsp;innych królestw, którzy też je gromadzą? Na ten fakt niektórzy wolą pozostać ślepi.

{% include details-end.html %}

### Możliwości użytkowników

Jako użytkownicy możemy poruszać się po obszarze zielonym Androida -- bawić się pstryczkami (systemowymi ustawieniami) i&nbsp;do pewnego stopnia kontrolować aplikacje, ich uprawnienia, powiadomienia itd.

Przeciw zwykłym, szarym apkom (jak przysłowiowa apka-latarka grzebiąca w&nbsp;SMS-ach) takie zabezpieczenia wystarczą. Ale Usługi, jako coś wrośniętego w&nbsp;smartfona, to całkiem inna bestia.

Można niby odebrać im uprawnienia, ale trzeba to zrobić [przez głębiej ukryte menu](/2024/02/03/smartfon-degoogle#odbieranie-us%C5%82ugom-pozwole%C5%84){:.internal}. Poza tym zawsze jest ryzyko, że to obejdą, jak w&nbsp;opisanym wyżej przypadku skanowania Wi-Fi.

Fałszywych danych również im się nie poda, bo na domyślnym Androidzie **nie możemy zaglądać do plików wewnętrznych aplikacji ani do głębszych rejonów systemu**.

{:.post-meta .bigspace-after}
Głębsze warstwy nazwałem tu *jądrem systemu*. Wbrew oficjalnej definicji, bo formalnie jądrem Androida jest poczciwy Linux.  
Swoją drogą -- zielona głowa robota w&nbsp;tym głębszym rejonie to logo Androida i&nbsp;symbolizuje czysty, niezmieniany system.

Jaka opcja pozostaje użytkownikom chcącym mieć pewność, że Usługi ich nie przechytrzą? Tylko ich wyłączenie, bo odinstalować się nie da.  
To wprawdzie zabieg łatwo odwracalny, ale można mieć nadzieję, że tak na chama to się nie reaktywują.

## Wyłączenie Usług i&nbsp;pierwsze kłopoty

Ktoś może w&nbsp;końcu nie wytrzymać i&nbsp;skorzystać z&nbsp;tej kuszącej opcji: wejść w&nbsp;Ustawienia, potem Aplikacje, znaleźć tam Usługi i&nbsp;je zwyczajnie wyłączyć pstryczkiem.

Od razu rozpęta się pandemonium. Zaczną pojawiać się liczne powiadomienia mówiące, że aplikacje A, B, C&nbsp;i inne nie zadziałają bez Usług. Nawet zwykły Zegar zacznie się buntować.

{% include details.html summary="Część tych powiadomień to fałszywe alarmy i&nbsp;wystarczy je wyłączyć" %}

{:.bigspace-before}
Google tak jakoś zaprojektował Androida, że każda nieudana próba znalezienia Usług jest eskalowana do poziomu poważnie brzmiącego komunikatu.  
W rzeczywistości szanujące się aplikacje powinny wyłapywać takie błędy i&nbsp;jakoś dostosowywać się do sytuacji.

{:.post-meta .bigspace-after}
Zwłaszcza jeśli Usług używały tylko po to, żeby sięgnąć do ID reklamowego.

Przykład aplikacji jojczących, ale działających normalnie? Wspomniany Zegar. Tricount (do podliczania wydatków na wyjazdach). Aplikacja jednej z&nbsp;linii kolejowych.

Żeby wyciszyć irytujące powiadomienia, można:

* zapamiętać pokazującą się nazwę aplikacji,
* odwiedzić Ustawienia, potem Aplikacje,
* jeśli szukanej nazwy nie ma na liście, to wybrać opcję pokazywania apek systemowych w&nbsp;górnym prawym rogu,
* znaleźć na liście jojczącą aplikację i&nbsp;ją kliknąć,
* wybrać zakładkę Powiadomienia i&nbsp;wyłączyć pokazywanie wybranych (albo wszystkich) powiadomień od tej apki.

W ten sposób niektóre aplikacje przestaną histeryzować i&nbsp;będą działały normalnie bez Usług.

{% include details-end.html %}

Oprócz nich jest niestety wiele apek, które faktycznie polegają na Usługach i&nbsp;bez nich nie zadziałają. Jak większość bzdetów od Google'a, w&nbsp;tym nasz przykładowy Sklep (instalator i&nbsp;aktualizator aplikacji).

{:.bigspace}
<img src="/assets/posts/google/uslugi-google-play/2-android-warstwy-google-play-wylaczone.png" alt="Trzy warstwy systemu Android przy wyłączonych Usługach Google Play. Ikona Google i&nbsp;ich aplikacje są wyszarzone, nie działają."/>

Zewnętrzne aplikacje też niestety zaczną się wykładać.  
Kiedyś nie działała Mapa Turystyczna, mimo że opiera się na otwartej OpenStreetMapie, a&nbsp;nie Mapach Google'a (może coś się zmieniło od tej pory). Nie działa podobno mapka wbudowana w&nbsp;Ubera czy Lyfta. Nie zadziałają różne aplikacje bankowe... Długo by wymieniać.

{% include details.html summary="Analogia zamkowa" %}

{:.bigspace-before}
Wyłączenie Usług jest jak postawienie barier przed wszystkimi drzwiami do komnat uzurpatora (bo wtargnąć niestety się nie da). Odcięcie go od możliwości kontaktu z&nbsp;zewnętrznymi agentami.

Po fakcie okazuje się niestety, że miał wielu stronników.

Niektórzy to klakierzy, którzy tylko jojczą, że tragedia się dzieje, ale ostatecznie się podporządkują. Są też jednak tacy, którzy nadal próbują wsuwać listy pod drzwi uzurpatora, a&nbsp;nie otrzymując odpowiedzi, całkiem odmawiają współpracy.

Tak to już bywa, że władza tylko formalnie jest w&nbsp;rękach jednego człowieka. W&nbsp;praktyce jest rozproszona po różnych ośrodkach i&nbsp;trzeba albo je udobruchać, albo wymienić cały dwór. „Na układy nie ma rady”.

{% include details-end.html %}

Ogólnie: **wyłączenie Usług demaskuje patologiczną zależność innych korposów od Google'a**.

Co ważne i&nbsp;warte podkreślenia: ta zależność *nie była nieunikniona*.  
Usługi są nakładką na prawdziwego Androida i&nbsp;mało co tworzą od zera. Dało się je obejść i&nbsp;tworzyć apki rozmawiające bezpośrednio z&nbsp;mechanizmami systemu. Albo przynajmniej realizujące plan B&nbsp;w razie braku Usług.

...Ale twórcy aplikacji, również ci więksi, woleli oprzeć się na Usługach, wziąć je za pewnik. I&nbsp;nawet nie myśleć o&nbsp;smartfonach bez Google'a :roll_eyes:

{% include info.html
type="Ciekawy przypadek Huaweia"
text="Nie trzeba być małym graczem ani majsterkującym buntownikiem, żeby odczuć brak Usług. Doświadczył tego chiński gigant Huawei, kiedy Google odciął ich od swoich aplikacji na polecenie rządu USA.  
W efekcie życie ze smartfonem Huawei jest jak świadome wyłączenie Usług Google'a, ze wszystkimi tego zaletami i&nbsp;wadami. Plus, nie ukrywajmy, to zmiana jednego szpiegującego korpo na inne."
%}

**Osobiście świadomie zatrzymałem się na tym etapie** -- wyłączyłem Usługi, wyciszyłem narzekające powiadomienia, pożegnałem się z&nbsp;apkami odmawiającymi współpracy (w&nbsp;tym wieloma popularnymi). I&nbsp;olałem bełkotliwe głosy z&nbsp;internetu, nazywające takie podejście *luddyzmem*.

{% include details.html summary="Jak obchodzę brak Usług Google'a" %}

* Zamiast Sklepu Play używam dwóch aplikacji:

  * Aurora Store do zdobywania aplikacji oficjalnych, zamkniętych, z&nbsp;baz Google'a (używa kont-marionetek do pobierania z&nbsp;oficjalnego Sklepu).
  * F-Droida do zdobywania alternatyw o&nbsp;otwartym kodzie źródłowym (ufam im, bo mają rygorystyczny proces oceniania).

* Apki podstawowe, jak Telefon, Aparat itd. można zastąpić otwartymi zamiennikami z&nbsp;serii Fossify (pobieram z&nbsp;F-Droida).
* Dobrym zamiennikiem dla Google Maps są Organic Maps, działające offline i&nbsp;oparte na OpenStreetMapie.
* Niektóre apki, również od dużych platform, działają normalnie bez Usług (przykładem Messenger, na którego czasem niestety jestem skazany).
* Wielu serwisów i&nbsp;mediów społecznościowych (Gmaila, Reddita, Facebooka...) da się używać przez strony internetowe, a&nbsp;nie aplikacje.

  {:.post-meta .bigspace-after}
  Czasem warto pójść nieoficjalną drogą. Serwis X/Twitter można np. czytać przez różne instancje Nittera, takie jak *xcancel.com*.

W przypadku, gdy nie istniało żadne sensowne obejście, po prostu zrezygnowałem z&nbsp;niektórych rzeczy. I&nbsp;myślę że na tym nie straciłem :wink:

{% include details-end.html %}

Niektórzy chcą jednak iść o&nbsp;krok dalej i&nbsp;mieć obie rzeczy naraz -- kontrolę nad systemem, ale i&nbsp;działające popularne aplikacje.

## Przejęcie dolnych warstw systemu

Choć producenci smartfonów zwykle się z&nbsp;tym nie afiszują, czasem możliwe jest **obalenie systemowych barier i&nbsp;podporządkowanie sobie dolnej warstwy**. Wtrącenie uzurpatora do lochu i&nbsp;przejęcie jego komnat.

> Break free from the facade of their tyranny  
Pull them down from their thrones of authority  
Rise up and take back what you are owed  
Listen now, we refuse to be controlled

{:.figcaption}
Źródło: *Bury Tomorrow*, „*Boltcutter*”.

Można wyróżnić dwa sposoby przejęcia władzy nad smartfonem:

* **_rootowanie_ telefonu**

  Intuicyjnie: sprawienie, że dolna warstwa stanie się zielona i&nbsp;dostępna. 
Samego *rootowania* nie będę tu opisywał, nie mając doświadczeń w&nbsp;temacie. Poza tym bardzo dobrze (i&nbsp;po polsku!) [robi to blog „Wolność w&nbsp;kieszeni”](https://wolnoscwkieszeni.pl/uwolnic-smartfona-1/).

* **wgranie alternatywnego systemu (_custom ROM-a_)**

  Takie systemy często są oparte na Androidzie, ale dają użytkownikom więcej wolności. Dolna warstwa nie jest zwykle otwarta (bo jednak daje to pewne zabezpieczenie), ale chętne osoby mogą ją łatwo *zrootować* dla pełni kontroli.

{:.bigspace-before}
<img src="/assets/posts/google/uslugi-google-play/3-android-warstwy-root-albo-custom-rom.png" alt="Trzy warstwy systemu alternatywnego wobec Androida. Najniższa warstwa jest teraz oznaczona jako dostępna, ale ikona Google i&nbsp;ich aplikacje są wyszarzone, nie działają."/>

{:.figcaption}
Na alternatywnym systemie dolna warstwa jest zwykle żółta, ale łatwo ją zazielenić.  
A czemu Usługi Google na szaro? To wyjaśnię za moment.

### Problem pierwszy: bootloader

Oba sposoby przejmowania systemu łączy to, że najpierw trzeba „wykonać podkop”, żeby zyskać możliwość załadowania własnych rzeczy.  
Oficjalnie taki podkop nazywa się „otwarciem _bootloadera_”, gdzie *bootloader* to część odpowiedzialna za ładowanie systemu, w&nbsp;której działanie się ingeruje.

Nie jest to jakąś magią od strony technicznej, a&nbsp;szczegółowe instrukcje można znaleźć na stronkach przyjaznych użytkownikom. Jeden link dałem wyżej.

Problem w&nbsp;tym, że nie każdy producent daje lekką ręką możliwość takiej ingerencji: niektórzy rzucają kłody pod nogi, niektórzy całkiem blokują. Na Githubie można znaleźć [ranking producentów i&nbsp;modeli](https://github.com/zenfyrdev/bootloader-unlock-wall-of-shame), oceniający ich pod kątem łatwości wymiany podstaw systemów.

### Potężny problem z&nbsp;Play Integrity

Gdy już się uda przejąć dolną warstwę, to możliwe staje się pełne usunięcie Usług albo karmienie ich fałszywymi danymi. W&nbsp;ten sposób aplikacje powinny działać normalnie (bo Usługi przecież istnieją), ale bez dostępu do danych, prawda?

Czasem tak, ale niestety można się naciąć. Jak na schemacie wyżej. To dlatego, że Usługi zawierają funkcję o&nbsp;nazwie **Play Integrity**.

Mówiąc intuicyjnie: Usługi „skanują” na prośbę aplikacji przestrzeń wokół siebie, szukając dowodów na to, że znajdują się w&nbsp;nietypowych warunkach. Że nie są „zanurzone w&nbsp;domyślnej czerwieni”, że tak nawiążę do pierwszych schematów.

{:.post-meta .bigspace-after}
Póki co mówię tutaj o&nbsp;weryfikacji na poziomie podstawowym. O&nbsp;jej gorszym rodzaju będzie później.

Swoimi wnioskami dzielą się z&nbsp;pytającymi je aplikacjami. Te zaś, słysząc o&nbsp;nietypowym systemie, mogą odmówić działania. Tak robiły lub robią nadal: aplikacje bankowe, niektóre gry, apka McDonalda, mObywatel (który, co ciekawe i&nbsp;na plus, działał po zwykłym wyłączeniu Usług na domyślnym systemie). I&nbsp;pewnie wiele innych.

{% include info.html
type="Ciekawostka"
text="Mechanizm Play Integrity nazywał się kilka lat temu SafetyNet. Takiej nazwy użyłem, wspominając o&nbsp;nim na blogu [po raz pierwszy](/google/2021/10/30/google-skandale-wprowadzenie#android-system-operacyjny){:.internal}.  
Dosłownie oznaczało to: „sieć bezpieczeństwa”. Taka, którą można zarzucić na użytkownika, żeby nie zagrażał interesom firm od aplikacji :wink:"
%}

### Wyścig zbrojeń

Czy posiadanie dolnej warstwy nie miało przypadkiem dawać kontroli? Może dałoby się przechytrzyć Usługi, zmieniając ich otoczenie?

Istotnie, cały czas trwa wyścig zbrojeń między Usługami i&nbsp;ich wykrywaczem ingerencji a&nbsp;aplikacjami, które próbują te ingerencje ukryć.  
Istnieje cały ekosystem obejść i&nbsp;zamienników. Przykładowo:

* [MicroG](https://github.com/microg/GmsCore) to alternatywa dla Usług, naśladująca niektóre ich funkcje;
* Różne programy takie jak [Magisk](https://github.com/topjohnwu/Magisk) czy uzupełniający go [Play Integrity Fix](https://github.com/KOWX712/PlayIntegrityFix/) próbują ukrywać przed Usługami fakt, że system jest zmodyfikowany.

Czasem obejścia działają i&nbsp;pozwalają odpalić niepokorne aplikacje na zmodyfikowanym systemie. Nie ma jednak gwarancji, że tak się stanie.

{% include details.html summary="Analogia zamkowa" %}

{:.bigspace-before}
*Rootowanie* albo instalacja alternatywnego systemu jest jak zebranie sojuszników, wtargnięcie do komnat uzurpatora tajnym podziemnym przejściem i&nbsp;ich siłowe przejęcie.

Gdyby wtrąciło się uzurpatora do lochu i&nbsp;nie zrobiło nic więcej, to znów mielibyśmy scenariusz z&nbsp;buntem jego zaufanych ludzi. Dlatego zamiast tego albo robi się z&nbsp;niego zakładnika (obstawiając go strażnikami), albo podstawia zamiennika.

Żadna z&nbsp;metod nie jest niestety pewna.  
Ludzie z&nbsp;zewnątrz mogą poznać, że zamiennik nie ogarnia wszystkiego w&nbsp;ten sam sposob.  
Z kolei w&nbsp;przypadku pilnowania uzurpatora może on zaalarmować kontaktujących się z&nbsp;nim ludzi, jaka jest sytuacja i&nbsp;że nie ma już władzy. Widząc to, jego zawzięci stronnicy ponownie odmówią współpracy.

{% include details-end.html %}

{% include details.html summary="Masochizm fanów omijania Usług (subiektywna opinia)" %}

{:.bigspace-before}
Jak najbardziej kibicuję autorom opisanych obejść i&nbsp;chylę przed nimi czoła... Ale nieco mi zgrzyta kultura, jaka narosła wokół przechytrzania Usług.

Część światka prywatnościowego delektuje się zwycięstwami. Triumfalnie informuje o&nbsp;każdym sukcesie, udanym obejściu Google'a i&nbsp;uruchomieniu aplikacji na zmienionym systemie. A&nbsp;po pewnym czasie luka, którą się chwalili, zostaje załatana i&nbsp;trzeba szukać nowych.

W moich oczach to trochę tak, jakby Google i&nbsp;autorzy aplikacji zależnych byli zbirami, regularnie napadającymi majsterkowiczów w&nbsp;zaułku. A&nbsp;oni się cieszą, że się wymknęli. „Tym razem zastawił przejście koszami, ale przecisnąłem się bokiem i&nbsp;mu uciekłem”.

No i&nbsp;fajnie... Ale może zamiast cieszyć się z&nbsp;ucieczek, lepiej włożyć energię w&nbsp;neutralizowanie zbira? Przez nagłaśnianie tematu, przybliżanie go ludziom, zorganizowaną krytykę apek zdających się na Play Integrity? Przedstawianie tego jako dyskryminacji i&nbsp;działań antykonkurencyjnych?  
Świata nie zmieni się samym komputerkiem.

{% include details-end.html %}

## GrapheneOS

Wśród alternatywnych systemów istnieje jeden, który wyróżnia się na tle pozostałych. Zapewnia najwyższy poziom cyberbezpieczeństwa -- co zresztą jest głównym aspektem, na którym skupiają się jego twórcy.

{:.post-meta .bigspace-after}
Złośliwi mogliby powiedzieć, że to ludzie, którzy wszystkie punkty umiejętności włożyli w&nbsp;zdolności techniczne, kosztem komunikacyjnych (sprzeczki, wbijanie szpil innym projektom). Mimo to ich lubię; trochę jak Doktora House'a.

Ten system to świetny kontrargument na przypadki, kiedy coś staje się zależne od Google'a, powołując się na bezpieczeństwo. Graphene zwyczajnie jest pod tym względem lepszy. Jeśli ktoś stawia na Google'a, a&nbsp;jego wyklucza, to pokazuje wewnętrzną sprzeczność swoich działań.

W kontekście tego wpisu ważniejsze jest natomiast to, że Graphene podchodzi do Usług inaczej niż pozostali. Zamiast je wymieniać albo zostawiać w&nbsp;zmienionym otoczeniu, stosują **_sandboxing Usług_**. Dosłownie „zamknięcie w&nbsp;piaskownicy”, w&nbsp;praktyce odizolowanie.

Intuicyjnie można powiedzieć, że to jak zamknięcie Usług w&nbsp;makiecie systemu (albo jaskini Platona, jeśli ktoś kojarzy). Karmienie ich wiarygodnymi, spójnymi wewnętrznie danymi, które jednak nie pokażą im rzeczywistości.

{% include details.html summary="Analogia zamkowa" %}

{:.bigspace-before}
Można powiedzieć, że Graphene wykorzystuje fakt, że uzurpator komunikuje się przez liściki wkładane pod drzwiami. I&nbsp;robi przebudowę zamku w&nbsp;taki sposób, żeby nie tykać jego komnat.

Zamiast go zamykać w&nbsp;lochu i&nbsp;podstawiać zamiennika albo otaczać go strażnikami -- buduje wokół niego dyskretne atrapy.

Kiedy uzurpator idzie do pokoju po mapy, to je znajdzie bez przeszkód. Ale będą to podróbki bez ważnych lokalizacji (prawdziwy składzik na zamkowe mapy został przeniesiony).

Przed prawdziwymi drzwiami do jego komnat stają inne, fałszywe. A&nbsp;sługa siedzący za nimi przechwytuje listy, podmienia na niegroźne i&nbsp;podaje je dalej pod drzwiami uzurpatora.

...I tak dalej. Życie uzurpatora się nie zmieniło, ale stało się czymś oderwanym od prawdziwego życia zamku.

{% include details-end.html %}

{:.bigspace}
<img src="/assets/posts/google/uslugi-google-play/4-android-warstwy-graphene-os.png" alt="Trzy warstwy systemu GrapheneOS. Usługi Google są odgrodzone od reszty systemu i&nbsp;widać po kolorach, że działają prawidłowo"/>

{% include info.html
type="Uwaga"
text="Nim ktoś się podjara, warto dodać, że na chwilę obecną Graphene działa **tylko na smartfonach Pixel**. Produkowanych przez Google'a... Ale, paradoksalnie, względnie łatwych do *odgooglowania*.  
Na pocieszenie -- niedawno ludzie od Graphene'a [nawiązali współpracę z&nbsp;Motorolą](https://news.ycombinator.com/item?id=47214645) (Mobility, czyli własnością Lenovo, a&nbsp;nie amerykańską Solutions). Może to zmienić stan rzeczy i&nbsp;sprowadzić Graphene'a na popularniejsze smartfony."
%}

Z punktu widzenia użytkowników wiele rzeczy działa jak na typowym Androidzie, nie ma za to masowego wykradania danych. Czyżby zwycięstwo?  
...Niestety nie. Google ma jeszcze asa w&nbsp;rękawie.

## Play Integrity i&nbsp;weryfikacja sprzętowa

W głębinach smartfona tkwi **niezależny, odizolowany chip kryptograficzny**. Bywa znany pod niejedną angielską nazwą, taką jak ogólna *TEE (Trusted Execution Environment)* czy *Secure Element*.

Osobiście wolę jednak nazwę **enklawa**. Lepiej oddaje kluczową cechę tego chipa, czyli izolację, a&nbsp;nie jakieś abstrakcyjne zaufania czy bezpieczeństwa. 

{:.post-meta .bigspace-after}
Bonus: kojarzy się z&nbsp;pamiętnymi złolami z&nbsp;„*Fallouta 2*”.

Enklawy mają swoje pozytywne zastosowania przy ochronie danych. Przykładowo: mogą przechowywać informacje wrażliwe, takie jak wzorzec odcisku palca, jeśli ktoś ustawi taki tryb odblokowania ekranu.

Problem jednak w&nbsp;tym, że ich możliwości są nadużywane. Enklawy biorą udział w&nbsp;procesie kontrolowanego uruchamiania systemu (to tzw. *secure boot*). Zapisują w&nbsp;sobie jego stan, [ściskając dane do krótkich ciągóœ znaków](/2021/02/28/hash-podstawy){:.internal}.

Potem mogą okazywać te informacje na żądanie. **Mówić pytającym Usługom, czy są na fabrycznym Androidzie, czy też na zmienionym systemie**. Ten poziom weryfikacji nosi nazwę wewnętrzną `MEETS_DEVICE_INTEGRITY` (albo `MEETS_STRONG_INTEGRITY`, jeśli do tego Android ma wszystkie aktualizacje).

{:.bigspace}
<img src="/assets/posts/google/uslugi-google-play/5-android-warstwy-graphene-os-pokonany-trusted-computing.png" alt="Cztery warstwy systemu Graphene OS i&nbsp;przepływ informacji między Usługami Google a&nbsp;kryptograficznym chipem. Ikona Google i&nbsp;ich aplikacje są wyszarzone, nie działają"/>

Wcześniej wspominałem o&nbsp;obejściach. To może znowu by warto ich użyć?  
Tu niestety nie pomogą. Enklawy oznaczają przekazywane informacje swoim cyfrowym podpisem, który:

* jest niemożliwy do podrobienia (mocna kryptografia);
* może być nakładany tylko przez enklawę (narzędzie znajduje się w&nbsp;jej wnętrzu i&nbsp;nigdy nie jest udostępniane innym);
* jednoznacznie ujawnia pytającym, że to oficjalna informacja od enklawy (oczekiwany wzorzec podpisu jest publicznie znany; jego znajomość nijak nie ułatwia jego podrobienia).

Wisienka na torcie? Ci, którzy stosują taką weryfikację, uzależniając się od Usług Google, mogliby korzystać zamiast tego [z opcji wbudowanej w&nbsp;Androida](https://grapheneos.org/articles/attestation-compatibility-guide), która dopuszczałaby inne *niezrootowane* systemy. Ale wybierają zależność.

{% include details.html summary="Analogia zamkowa" %}

{:.bigspace-before}
Fundamenty naszego zamku stoją na skale. W&nbsp;jaskiniach wewnątrz tej skały mieszka tajemnicza Wyrocznia, które wiele wie i&nbsp;wiele widziała.  
Nie da się do niej dostać i&nbsp;można się z&nbsp;nią porozumiewać jedynie przez wrzucanie kartki z&nbsp;konkretnymi pytaniami do wąskiej szczeliny. Potem czeka się na odpowiedź.

Wyrocznia wie, jak powinien wyglądać zamek. Przy każdej jego przebudowie całym ciałem odczuwa drgania. Wie, że coś się zmieniło.

Jeśli uzurpator nie wierzy sobie i&nbsp;czuje, że może być oszukiwany -- pyta wyroczni, czy zamek został zmieniony. Otrzymuje odpowiedź w&nbsp;zaplombowanej kopercie. Na plombie widnieje odcisk niemal nieskończenie misternej pieczęci.

Gdyby ktoś naruszył kopertę, to uzurpator by to zobaczył. Pieczęci nie podrobi ani on, ani nikt inny, wydaje się technologią wręcz kosmiczną.  
Zna natomiast dokładnie jej oczekiwany wygląd i&nbsp;zawsze rozpozna, czy dostał oryginalną kopertę od Wyroczni. W&nbsp;tej kopercie zawsze znajdzie prawdziwą odpowiedź.

{% include details-end.html %}

{% include info.html
type="Powiązane wpisy"
text="To ogólne zjawisko -- użycie odizolowanych enklaw, cyfrowych podpisów i&nbsp;szyfrów do narzucania kontroli -- jest znane pod nazwą [_trusted computing_](/cyfrowy_feudalizm/2024/10/22/trusted-computing-kajdany){:.internal}. Przestrzegano przed tym już ponad 20&nbsp;lat temu (zaś były szef Microsoftu to promował krótko po zamachu z&nbsp;11&nbsp;września).  
Poza tym Google już kiedyś chciał użyć tych metod do podzielenia cyfrowego świata. Ich propozycja nosiła nazwę [Web Environment Integrity](/google/2023/07/29/web-environment-integrity){:.internal} i&nbsp;pozwoliłaby każdej stronie internetowej weryfikować „mainstreamowość” systemu próbującego ją odwiedzić."
%}

## Przyszłe zagrożenia

Ktoś może doczytać do tego etapu, ale nie widzieć zagrożenia dla siebie. „No dobra, Usługi zbierają dane i&nbsp;nie pozwolą mi zmienić systemu. Okej. Ale ja nie chcę go zmieniać, poza tym częściej używam komputera”.

Tyle że nikt nie jest bezpieczny. Google zaczął niedawno eksperymentować z&nbsp;nowym trybem zabezpieczenia ReCAPTCHA. Nowa wersja może wymagać [użycia smartfona do zeskanowania kodu QR](https://privatecaptcha.com/blog/google-cloud-fraud-defence-wei/). **Nawet kiedy korzysta się z&nbsp;kompa**.  
A że po zeskanowaniu kod trafia do Usług -- to brak smartfona z&nbsp;Usługami (i&nbsp;pewnie przechodzącego pomyślnie Play Integrity) może oznaczać odcięcie od stron, które wdrożyły u&nbsp;siebie ten mechanizm.

Jeszcze gorsze jest widmo **współpracy rządów z&nbsp;korpo** i&nbsp;przeforsowania aplikacji, bez której trudno działać w&nbsp;społeczeństwie. Mniej niż dwa lata temu [straszyłem taką wizją](/cyfrowy_feudalizm/2024/10/22/trusted-computing-kajdany#dystopijne-scenariusze){:.internal}:

> Gdyby obywatele musieli na mocy przepisów mieć jakąś aplikację, zaś aplikacja dopuszczałaby poprzez *trusted computing* tylko nieliczne, najpopularniejsze systemy od dużych firm – to mamy gotowy przepis na dystopijne, zmonopolizowane państwo.

A teraz... No cóż, właśnie powstaje Europejski Portfel Tożsamości Cyfrowej (EUDI). Póki co promowany jako ułatwienie, a&nbsp;nie wymóg.

Jego kod źródłowy jest wprawdzie otwarty i&nbsp;rozwijany publicznie -- tak serio, a&nbsp;nie komicznie [jak polski mObywatel](https://xcancel.com/InfZakladowy/status/2014040530049442014#m) -- ale niewiele to zmienia.  
Bo w&nbsp;tym otwartym kodzie wprost pojawiają się, mimo potężnego oporu komentujących, fragmenty sugerujące, że zadziała [tylko na urządzeniach przechodzących weryfikację Play Integrity](https://github.com/eu-digital-identity-wallet/av-doc-technical-specification/discussions/19).

Można również znaleźć w&nbsp;sieci [dokumentację cyfrowego portfela niemieckiego](https://bmi.usercontent.opencode.de/eudi-wallet/wallet-development-documentation-public/v0.8.0/Guidelines/appAttestation/#requirements), w&nbsp;którym omawiają parę kwestii związanych z&nbsp;weryfikacją. Wyraźnie sugerują, że będą się trzymali Usług Google Play.

{:.post-meta .bigspace-after}
Mimo że -- podkreślę raz jeszcze, bo to ważne -- mogliby użyć funkcji wbudowanych w&nbsp;samego Androida.

Jak w&nbsp;takich warunkach ma przetrwać jakakolwiek konkurencja wobec Google'a? Nawet jeśli ktoś nie chce walczyć o&nbsp;swobodę majsterkowania (bo tego nie robi) -- może powalczyć *przeciw monopolizacji*.

## Co można zrobić?

Proponuję **głośno protestować i&nbsp;nagłaśniać patologie wokół Usług**. Nie spoczywać na laurach z&nbsp;myślą, że jakoś to będzie, że Magiskiem się przymaskuje, że tajne klucze wyciekną. Dotąd niektórzy dawali się kopać zbirowi, ale teraz już naprawdę trzeba wołać o&nbsp;pomoc, bo ten sięga po nóż.

Proponuję założyć, że weryfikacja będzie coraz szczelniejsza. Bo wszelkiej maści uzurpatorom zależy na kontroli i&nbsp;nie odpuszczą, póki jej nie zacieśnią.

{:.post-meta .bigspace-after}
W przygotowaniu na czarny scenariusz można rozważyć używanie dwóch tańszych smartfonów -- jeden prywatniejszy, z&nbsp;kartą SIM, bez Usług Google'a. Drugi mainstreamowy, bez karty SIM, używany przez hotspoty w&nbsp;razie konieczności.

Można **odchodzić od Google'a i&nbsp;namawiać do tego innych**. Wykorzystać to, że przez najbliższe półtora roku infosfera może łatwo wchłaniać treści przeciwne patologiom cyfrowym:

* Niechęć do imperializmu USA i&nbsp;powiązanych z&nbsp;nimi krajów bije rekordy, dzięki czemu argumenty za suwerennością trafiają na podatny grunt.

  Zaczęło działać sporo kont [promujących federalizację Europy](/2025/12/31/podsumowanie-2025-roku#2026rokiem-promowania-federalizacji){:.internal}. Niezależnie od stosunku do nich (sam jestem sceptyczny) -- można potraktować komentarze pod ich wpisami jak darmowy megafon dla swoich antykorporacyjnych przemyśleń.

* Forsowanie AI sprawia, że na świecie rodzi się oddolny opór. Google jest zaś jednym z&nbsp;naczelnych forsujących, warto to podkreślać.
* W&nbsp;2027 roku odbędą się w&nbsp;Polsce wybory do parlamentu. Idealny czas, żeby ponaciskać na polityków i&nbsp;proponować wymiankę: głosy za czyny :wink:

To okno może się zamknąć po wyborach, zwłaszcza amerykańskich. Jest ryzyko, że ktoś wtedy powie: „teraz jest dobra władza, znów lubimy Ameryczkę”. I&nbsp;spróbują cofnąć postępy w&nbsp;zakresie suwerenności.

Zamykanie cyfrowego świata jest jak przykrywanie garnka pokrywką. Jeśli robi to ręka zbyt silna, żeby stawić jej opór, to można przynajmniej doprowadzać nastroje do wrzenia. Żeby po przykryciu wszystko wykipiało.

I na tej metaforze zakończę wpis. Do zobaczenia w&nbsp;kolejnych!


{% include details.html summary="Źródła ikon na schematach" %}

<a id="źródła-schematów"/>

* [Ikona błędu](https://www.flaticon.com/free-icon/close_9068699) (autor(-ka): Fathema Khanom) ze strony Flaticon.
* [Ikona chipa](https://www.flaticon.com/free-icon/chip_8970072) ze strony Flaticon (autorstwa: *Maan Icons*).
* Oficjalne ikony Firefoksa, Usług, Sklepu, Androida, GrapheneOS i&nbsp;firmy Google -- z&nbsp;Wikimedia Commons.

{% include details-end.html %}


