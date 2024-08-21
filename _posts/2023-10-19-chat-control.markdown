---
layout: post
title: "Kontrola czatów, cnotliwy Tumblr i szyfrowy wyścig zbrojeń"
subtitle: "Kolejny rok, kolejna walka o prywatność."
description: "Kolejny rok, kolejna walka o prywatność."
date:   2023-10-19 20:00:32 +0100
tags: [AI, Inwigilacja, Open Source, Podstawy, Porady]
firmy: [Apple, Tumblr]
image:
  path: /assets/posts/inwigilacja/chat-control/chat-control-baner.jpg
  width: 1200
  height: 700
  alt: "Kadry z anime połączone w jeden kolaż. W górnej części w tle widzimy postać w krawacie, ze złowieszczym uśmiechem, trzymającą w dłoniach sznurki od lalek. W dolnej części widać ludzkie postaci w kombinezonach zwierząt, idące jedna za drugą, z rękami w kajdanach. Na głowy mają nałożone ikony komunikatorów Signal, Messenger i WhatsApp, a jedna ma ikonę koperty z literkę E, jak e-mail."
---

Co pewien czas politycy, krajowi albo światowi, próbują nam zaserwować jakieś niesmaczne danie. Choć z&nbsp;wierzchu wygląda sensownie.

Menu na dziś to **kontrola czatów**. W&nbsp;praktyce -- groźba niesłusznego oskarżenia przez tępy automat. Polana sosem troski o&nbsp;dobro dzieci.

W tym wpisie pokażę ciemne strony nowych przepisów:

* spore ryzyko fałszywych oskarżeń, zilustrowane historią portalu Tumblr;
* niską skuteczność wobec złoczyńców wyższego poziomu;
* groźbę rozszerzenia obserwacji na inne sfery życia.

{% include info.html
type="Uwaga"
text="Jak zawsze, gdy jakiś wpis porusza kwestię szyfrów -- przypominam, że jestem w&nbsp;tym temacie hobbystą-amatorem.  
Wpis możecie potraktować jako punkt wyjścia do zbierania dalszych informacji. Ale nie opierajcie na nim swojej prywatności. Nie chcę jej mieć na sumieniu :wink:"
%}

## Spis treści

* [Czym jest kontrola czatów?](#czym-jest-kontrola-czatów)
  * [Czy na pewno „unijny pomysł”?](#czy-na-pewno-unijny-pomysł)
  * [Kontrola od strony technicznej](#kontrola-od-strony-technicznej)
* [Realna głupota sztucznej inteligencji](#realna-głupota-sztucznej-inteligencji)
  * [Pruderyjny Tumblr](#pruderyjny-tumblr)
  * [Pandora Gate dla każdego?](#pandora-gate-dla-każdego)
* [Kto chce, ten zaszyfruje](#kto-chce-ten-zaszyfruje)
* [Dystopijny wyścig zbrojeń](#dystopijny-wyścig-zbrojeń)
* [Bonus: szybkie maskowanie tekstu](#bonus-szybkie-maskowanie-tekstu)
* [Źródła obrazków](#źródła-obrazków)

## Czym jest kontrola czatów?

Kontrola czatów (będę czasem skracał do KC) to przepisy mające obowiązywać na terenie Unii. Zaproponowane przez Ylvę Johansson z&nbsp;Komisji Europejskiej, we współpracy z&nbsp;zewnętrzną (pozarządową) grupą [lobbującą za zacieśnieniem kontroli](https://balkaninsight.com/2023/09/25/who-benefits-inside-the-eus-fight-over-scanning-for-child-sex-content/).

Wyszukując słów `kontrola czatów`, możemy znaleźć wzmianki o&nbsp;tym, że przepisy już weszły w&nbsp;życie.  
Ale zapewne mowa o&nbsp;wersji pierwszej, z&nbsp;2021 roku. Która jedynie zalecała autorom komunikatorów analizę treści. Obecnie **pod głosowanie w&nbsp;grudniu ma trafić wersja druga, zmieniająca to w&nbsp;obowiązek**.

Obowiązek nałożony na autorów programów od komunikacji (jak maile, Messenger, WhatsApp...).  
Nie będą mogli zostawiać użytkowników samym sobie. Będą musieli analizować ich komunikację.  
Jeśli wykryją coś, co może być przykładem wykorzystania nieletnich, to powinni to zgłosić odpowiednim służbom.

Brzmi sensownie? Problem w&nbsp;tym, że wykrywanie z&nbsp;założenia ma się opierać na automatycznych systemach. Które za nic nie są gotowe do takiego zadania. O&nbsp;czym pisze wprost [grupa naukowców](https://www.patrick-breyer.de/wp-content/uploads/2023/07/Open-Letter-CSA-Scientific-community.pdf), która podpisała petycję przeciw KC.

Inni, jak chociażby [szwedzka firma Mullvad od VPN-ów](https://mullvad.net/en/chatcontrol/campaign), zwracają uwagę na możliwość późniejszego łatwego nadużycia infrastruktury kontrolującej.

Dokładniejsze streszczenie sprawy, w&nbsp;formie najważniejszych punktów i&nbsp;dat, znajdziemy na [stronie Patricka Breyera](https://www.patrick-breyer.de/en/posts/chat-control/).

### Czy na pewno „unijny pomysł”?

Źródła wspominające o&nbsp;kontroli czatów nieraz mówią, że to „Unia narzuca obowiązek śledzenia”. Jest w&nbsp;tym ziarnko prawdy, bo pomysł faktycznie wypłynął z&nbsp;Komisji Europejskiej.

...Ale już nieraz się zdarzało, że KE wychodziła z&nbsp;czymś kontrowersyjnym.  
Jak [umowa handlowa TTIP](https://en.wikipedia.org/wiki/Transatlantic_Trade_and_Investment_Partnership), obniżająca unijne standardy, byle wpuścić produkty z&nbsp;USA. Jak dawniej [ACTA](https://pl.wikipedia.org/wiki/Anti-Counterfeiting_Trade_Agreement#Proces_ratyfikacji_w_Europie).

I nieraz się zdarzało, że pomysły były ubijane przez kolejne instancje. Choćby przez Parlament Europejski, który też jest przecież „unijny”.  
Również ten nowy pomysł [ma swoich przeciwników](https://stopchatcontrol.eu/) w&nbsp;unijnych instytucjach. A&nbsp;także w&nbsp;[służbach krajów członkowskich](https://berthub.eu/articles/posts/client-side-scanning-dutch-parliament/).

Jeśli kontrola czatu wejdzie w&nbsp;życie, to będę mógł szczerze przyznać, że Unia mnie zawiodła na tym polu.

Ale jeśli nie? Jeśli demokracja zadziała, a&nbsp;projekt zostanie ubity *dzięki unijnym instytucjom*?  
O tym już będzie ciszej. Ale w&nbsp;świadomości ludzi pozostanie mem „Unia próbowała nas wszystkich śledzić”. Takie sentymenty, zwłaszcza w&nbsp;Polsce, mogą potem wykorzystywać do swojej gry Rosjanie i&nbsp;inni.

Dlatego skłaniam się ku temu, żeby -- jeszcze, póki co, asekuracyjnie -- nazywać winowajców „grupą polityków”, a&nbsp;nie Unią. Wydżwięk podobny, ale nie sprzyja budowaniu nieufności.

No ale to taka dygresja. I&nbsp;tak każdy będzie pisał swoje, świata nie zmienię :roll_eyes:  
Przejdźmy do konkretniejszych spraw.

### Kontrola od strony technicznej

Wiele komunikatorów chroni nas obecnie przed podglądaczami z&nbsp;zewnątrz -- jak teoretyczni hakerzy i&nbsp;ich fałszywe hotspoty. Ale częściej jednak oficjalne firmy telekomunikacyjne.

Cała komunikacja jest szyfrowana. Nadal można dość łatwo przechwycić cyfrowy odpowiednik listów lecących w&nbsp;świat. Ale nie zajrzy się do ich wnętrza.

Jako przykładu użyję komunikatora Signal. Ta apka, choć bezpieczna, nie jest jakoś wybitnie buntownicza. Na żądanie władz zapewne by przekazali wszystko, co związane z&nbsp;konkretnymi osobami.

...Ale to „wszystko” nie byłoby imponujące. Bo Signal został tak zaprojektowany, żeby mieć jak najmniej wglądu.  
Zaszyfrowane wiadomości, których szyfrów nikt nie powinien złamać, łącznie z&nbsp;samym Signalem. Parę prostych metadanych, jak godziny wysłania. Tylko tyle dostałyby służby.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/chat-control/szyfrowanie-signal-podstawa.jpg" alt="Schemat pokazujący komunikację między dwiema osobami przy udziale apki Signal"/>

{:.figcaption}
Źródła schematów: głównie ikony z&nbsp;Linuksa, loga programów, Emojipedia, Flaticon.  
Szczegóły pod koniec wpisu. Przeróbki każdorazowo moje.

Plan oparty na zaglądaniu do naszej korespondencji, przechwyconej albo zdobytej drogą prawną, spaliłby na panewce. Choćby ktoś bardzo chciał, matma stojąca za szyframi jest bezwzględna.

Dlatego koncepcja kontroli czatu opiera się na **nałożeniu wymogów bezpośrednio na autorów aplikacji**.  
Szyfrowanie mamy nadal. Ale zanim treść zostanie zaszyfrowana i&nbsp;bezpiecznie przesłana, przeczesze ją algorytm. Jeśli coś wykryje, to zaalarmuje służby.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/chat-control/szyfrowanie-signal-chat-control.jpg" alt="Schemat pokazujący, jak wewnątrz apki Signal osadzono wrogi algorytm, oznaczony tu ikoną wszechwidzącego oka. Od aplikacji odchodzą dwie strzałki. Jedna z&nbsp;nich jest identyczna jak na poprzednim schemacie, skierowana w&nbsp;stronę apki drugiej osoby, znajduje się nad nią ikona zamniętej pancernej skrzyni. Nad drugą strzałką, czerwoną i&nbsp;prowadzącą na ukos ku górze w&nbsp;stronę znaku zapytania, widać ikonę wykrzyknika."/>

{:.figcaption}
Signal tym razem na fioletowo, bo zmieniła się jego natura.

Schemat praktycznie by się nie zmienił, gdyby -- zamiast ostrzegania służb -- był tu obowiązek dzielenia się z&nbsp;nimi pierwotnymi treściami. Ot, zamiast znaku ostrzegawczego byłaby druga szyfrowana skrzynka, wysyłana na policję.

Z pozoru zdanie się na automat daje nieco więcej prywatności. W&nbsp;niepowołane ręce poleci tylko to, co uzna on za złe, a&nbsp;nie cała korespondencja.  
Problem w&nbsp;tym, że jego rozumienie zła może być mocno wadliwe.

## Realna głupota sztucznej inteligencji

Pisałem już na tym blogu o&nbsp;tym, ile krwi napsuli użytkownikom YouTube'a [niedoskonali, automatyczni cenzorzy]({% post_url 2022-04-18-youtube-ai-reklamy %}){:.internal}. Zresztą kto ogląda filmy, ten widzi, że twórcy często stosują autocenzurę na wyrost, byle uniknąć kar.

Mam również nieco ogólniejszy wpis, [o nieracjonalnej wierze niektórych menedżerów w&nbsp;AI]({% post_url 2023-05-18-korpo-ai-spinacze %}){:.internal}.  
Często nie wiedzą nic o&nbsp;technice. Ale mają *mindset*, *drive* i&nbsp;*motivation*.

Bardzo by chcieli, żeby wizja automatyzacji się spełniła. Więc łykają bajki o&nbsp;możliwościach algorytmów. Zastępują nimi część personelu.  
I nieraz się przekonują, że słowo „inteligencja” było bardzo na wyrost. Zwłaszcza gdy pojawi się coś wykraczającego poza schemat.

Efekt taki jak w&nbsp;przykładzie ze wspomnianego wpisu. Ktoś zastąpi operatorów kamery automatem. A&nbsp;ten podczas jednego meczu skupi się na łysinie sędziego zamiast na piłce.

### Pruderyjny Tumblr

Albo może spójrzmy na coś bardziej pasującego do kontekstu. Przykład portalu Tumblr. Kiedyś słynął jako miejsce bardzo wyzwolone, uwielbiane przez artystów i&nbsp;mniejszości wszelkiego rodzaju. Każdy mógł tam znaleźć grafiki dla siebie, również niegrzeczne.

Ale w&nbsp;2018 roku strona zrobiła ostry zwrot ku reklamodawcom z&nbsp;USA. A&nbsp;ci, jakby odwołując się do purytańskich korzeni, zagrzmieli: „nasze reklamy nigdy nie staną obok tej moralnej zgnilizny!”.

Tumblr [szybko pochylił głowę](https://staff.tumblr.com/post/180758987165/a-better-more-positive-tumblr) i&nbsp;zaczął wyrzucać sztukę dla dorosłych do swojego cyfrowego getta. Wykrywając ją właśnie za pomocą automatów, marketingowo nazwanych AI.

Mimo trwających czystek zrobiło się wesoło. Bo **wadliwy algorytm Tumblra był jak nastolatek, któremu wszystko się kojarzy**. Którego wszystko deprymuje.  
Podtekst miały dla niego między innymi pokraczne rysunkowe lwy. Otagował je jako niegrzeczne zdjęcie.

<img src="/assets/posts/inwigilacja/chat-control/tumblr-nagie-lwy.jpg" alt="Kolaż złożony z&nbsp;trzech elementów. U&nbsp;góry po lewej mamy odręczny, pokolorowany rysunek pokazujący kilka ujęć lwów. Po prawej widać panel z&nbsp;mangi, na którym zarumieniony młody mężczyzna, na którego czoło nałożono logo Tumblra, robi przestraszoną minę. Krzyczy do kogoś, że nie może nosić tak obcisłych ubrań. Pod spodem mamy komunikat z&nbsp;portalu Tumblr, na czerwonym tle, mówiący że post został oznaczony jako treść dla dorosłych."/>

{:.figcaption}
Źródła: post użytkownika Sketchshark z&nbsp;Tumblra, manga *Deadman Wonderland*. Przeróbki moje.

Niemoralnych rzeczy dopatrzył się również w&nbsp;gołych ramionach.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/chat-control/tumblr-nagie-ramiona.jpg" alt="Kolaż złożony z&nbsp;trzech elementów. U&nbsp;góry mamy fragment mema pokazujący brodatego mężczyznę w&nbsp;szarym t-shircie ze wzorem, z&nbsp;rękami splecionymi za głową, mówiącego coś do dziewczyny w bluzce. Pod spodem widać komunikat Tumblra o&nbsp;tym, że post został oflagowany. Na dole mamy czarno-biały panel z&nbsp;mangi, na którym zarumieniony młody człowiek leży w&nbsp;łóżku i&nbsp;mówi po angielsku 'Zmień te cholerne ciuchy'. Na głowę ma nałożone logo Tumblra."/>

{:.figcaption}
Źródła: Twitter, *Deadman Wonderland*.

Inny przykład -- **miniaturka artykułu o&nbsp;tym, że wadliwy policyjny algorytm oznaczał zdjęcia pustyni jako nagość**. No cóż, Tumblr chyba się z&nbsp;nim zgodził, bo też to oflagował.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/chat-control/tumblr-naga-pustynia.jpg" alt="Zrzut ekranu pokazujący w&nbsp;górnej części komunikat Tumblra na czerwonym tle, mówiący o&nbsp;oflagowaniu udostępnionego wpisu. Poniżej widac zdjęcie pustynnych wydm podpisane nazwę portalu gizmodo.com, a&nbsp;pod zdjęciem widać nagłówek i&nbsp;streszczenie artykułu. Mówią o&nbsp;tym, że brytyjska policja ma algorytm, którego zadaniem będzie wyłapywanie zdjęć nieletnich. Ale póki co uznaje za nagość nawet pustynię."/>

Inne przykłady? [Zdjęcie kurczaka](https://nitter.cz/motherboard/status/1071509826847588352#m) w&nbsp;folii, zabawkowych żołnierzyków, rysunkowego skorpiona w&nbsp;kasku. Robotów. Fraktali. I&nbsp;[wiele innych rzeczy](https://nitter.cz/carolinethegeek/status/1069712323923726336#m).

Sprawa doczekała się nawet prześmiewczego hasztaga na Twitterze, [*#TooSexyForTumblr*](https://nitter.cz/search?q=%23TooSexyForTumblr), gromadzącego inne przykłady wpadek tego Ej-Aj.

{:.post-meta}
Gdyby linki nie działały, to można w&nbsp;nich zmienić *nitter.cz* na *twitter.com*.

### Pandora Gate dla każdego?

Śmieszki śmieszkami, dopóki jedyną konsekwencją jest ukrycie paru fotek. Oraz kilka minut sławy, kiedy się tym faktem podzielimy na forum publicznym.

Gorzej, jeśli przez fałszywe oskarżenie trafimy na listę podejrzanych i&nbsp;celownik tłumu.

Niedawno na polskim YouTubie miała miejsce afera nazwana Pandora Gate. Kilku znanych youtuberów zalecało się do nieletnich. Może nawet dosypywali środki usypiające do drinków. Inni od lat wiedzieli i&nbsp;ich kryli.

Niektóre dowody były niepodważalne. Ale oprócz tego oberwało się całkiem niewinnej osobie.  
Ktoś, nie chcąc ujawnić pełnych danych, napisał że przestępstwa dopuściła się też „osoba na G.”. A&nbsp;tłum połączył sobie kropki -- tyle że na początku źle -- i&nbsp;zasypał groźbami kompletnie niewinnego tworcę. 

Jedna litera nazwiska. Tyle wystarczyło. A&nbsp;tutaj mamy konkretne oskarżenie przekazane na policję. Od automatu, ale nie każdy wie o&nbsp;jego niedoskonałościach.

Ktoś powie, że wpadki w stylu Tumblra były dawno, że od tego czasu algorytmy się poprawiły?  
Tym gorzej. Kiedy algorytm myli się notorycznie, ludziom łatwiej uwierzyć w&nbsp;cudzą niewinność. **Kiedy myli się raz na miliard przypadków -- każda niesłusznie oznaczona osoba może być osamotniona w&nbsp;swojej walce**.

Wyobrażam sobie nawet scenariusz, kiedy błędnej klasyfikacji mógłby dokonać i&nbsp;algorytm, i&nbsp;człowiek z&nbsp;drugiej linii. 

* Znów mamy pandemię i teleporady medyczne.
* Czyjeś dziecko ma wypadek na rowerze, rani się w&nbsp;okolicy pachwiny. Rana kiepsko się goi, więc rodzic wysyła lekarzowi zdjęcie urazu.
* Algorytm wyłapuje to zdjęcie i&nbsp;wysyła twórcom do ręcznej weryfikacji.
* Ci patrzą. Jest nagość, jest dziecko -- lepiej to przekazać policji.
* Informacja trafia na lokalną komendę. Zaczyna się śledztwo.

  A&nbsp;że rodzic znany, bo społeczność mała, to ktoś z&nbsp;policjantów dzieli się informacją ze znajomymi. Plotka wychodzi poza komendę, wywołuje oburzenie.

* Sprawa się wyjaśnia, nie ma zarzutów karnych.

  Ale w&nbsp;oczach lokalsów ktoś ma zniszczoną reputację. Bo „gdyby nie miał nic na sumieniu, to by go nie wzywali”.

A cały czas mówimy tutaj o&nbsp;obrazkach. W&nbsp;tej kwestii komputery są nieco lepsze, trudniej o&nbsp;pomyłkę wyuczonego algorytmu. **Proponowana kontrola czatu ma natomiast dotyczyć również tekstu i&nbsp;wyłapywać próby manipulacji nieletnimi**.

Ej-Aj temu nie podoła.

Algorytm nie będzie wiedział, ile kto ma lat. Ale może sobie skorelować, że w&nbsp;czacie jakiegoś zboczeńca widział sporo zdrobnień i&nbsp;komplementów. I&nbsp;ciach, jakaś pełnoletnia parka trafia na komisariat.

## Kto chce, ten zaszyfruje

Można mocno kwestionować również skuteczność kontroli czatu w&nbsp;łapaniu prawdziwych złoczyńców.

**Jeśli niektóre aplikacje zaczną ich monitorować, to po prostu przejdą na inne aplikacje**. O&nbsp;ile jeszcze tego nie zrobili.

Obstawiałbym (bez twardych danych), że mało który złodupiec, poza płotkami, korzysta ze zwykłych komunikatorów.  
Grubsze ryby raczej wiedzą, co im grozi w&nbsp;razie odkrycia, i&nbsp;od dawna dbają o&nbsp;anonimowość.

To właściwie wyczerpuje temat z&nbsp;mojej strony. Ale w&nbsp;ramach eksperymentu myślowego wyobraźmy sobie świat, w&nbsp;którym musimy używać oficjalnych programów do komunikacji. A&nbsp;one nas podglądają.

Przypomnijmy sobie schemat takiej sytuacji:

{:.bigspace}
<img src="/assets/posts/inwigilacja/chat-control/szyfrowanie-signal-chat-control.jpg" alt="Schemat pokazujący, jak wewnątrz apki Signal osadzono wrogi algorytm, oznaczony tu ikoną wszechwidzącego oka. Od aplikacji odchodzą dwie strzałki. Jedna z&nbsp;nich jest identyczna jak na poprzednim schemacie, skierowana w&nbsp;stronę apki drugiej osoby, znajduje się nad nią ikona zamniętej pancernej skrzyni. Nad drugą strzałką, czerwoną i&nbsp;prowadzącą na ukos ku górze w&nbsp;stronę znaku zapytania, widać ikonę wykrzyknika."/>

Musimy użyć czatu, a&nbsp;czat jest na podsłuchu. Ale przecież oprócz niego mamy inne programy. Zaś aplikacje, przynajmniej na smartfonach, są całkiem niezależne. [Nie mogą do siebie zaglądać](https://developer.android.com/training/data-storage/app-specific).

Jeśli aplikacja zawiera podsłuch, można poza nią (choćby „w realu”) **uzgodnić z&nbsp;odbiorcą hasło. I&nbsp;przed wysłaniem wrażliwych rzeczy szyfrować je w&nbsp;innej, zaufanej apce**.

Tę zaszyfrowaną treść przenosimy z&nbsp;apki zaufanej do wścibskiej. Można przez `Kopiuj/Wklej`, można zapisać do pliku i&nbsp;potem go załadować. Obojętne.

Aplikacja-podglądacz nie zdoła zajrzeć do szyfrowanej treści. Może co najwyżej wysłać ją naszemu odbiorcy. A&nbsp;ten weźmie plik i&nbsp;otworzy go, korzystając z&nbsp;hasła, które sobie uzgodniliśmy.

Oto schemat obejścia cenzora. Jako zaufanej apki użyłem tutaj Firefoksa:

<img src="/assets/posts/inwigilacja/chat-control/szyfrowanie-firefox-system-signal.jpg" alt="Schemat pokazujący szyfrowanie plików w&nbsp;innej aplikacji niż komunikator. Składa się z&nbsp;dwóch trapezów symbolizujących aplikacje, stojących na podstawie podpisanej 'System operacyjny'. Apka po lewej ma na sobie logo Firefoksa, ta po prawej logo Signala. Widzimy, że wewnątrz Firefoksa zwykła wiadomość z&nbsp;tekstem 'Hej' zmienia się w&nbsp;skrzynkę ze znakiem serduszka. Strzałki pokazują, jak ta sama skrzynka trafia, idąc dołem przez system operacyjny, do wnętrza Signala, a&nbsp;następnie wylatuje poza schemat, zamknięta wewnątrz drugiej skrzynki."/>

### Hat.sh – kapelusz zakrywający tajemnice

A dlaczego Firefoksa? Przecież znalazłoby się wiele innych, łatwych w&nbsp;obsłudze szyfratorów/deszyfratorów.

Ale przeglądarki mają tę zaletę, że działają na wielu systemach. Często mają również wbudowane własne narzędzia od szyfrów. Choć mnie osobiście urzekło coś innego, niewbudowanego.

To projekt [Hat.sh](https://github.com/sh-dv/hat.sh). Będę go w&nbsp;skrócie nazywał Hat.  
Ma postać lekkiej stronki internetowej. W&nbsp;najprostszym przypadku:

1. wybieramy między szyfrowaniem a&nbsp;deszyfracją;
2. ładujemy wybrane przez siebie pliki;
3. wpisujemy hasło;
4. otrzymujemy zaszyfrowane/odszyfrowane pliki.

Hat zapewnia, że działa całkiem offline i&nbsp;nie wysyła danych. Chętni mogą zajrzeć w&nbsp;kod źródłowy.  
Dla pewności całkiem wyłączyłem internet krótko po odwiedzeniu strony, nim zacząłem korzystać z&nbsp;interfejsu. Hat nadal robił swoje w&nbsp;obu trybach.

Fajne narzędzie, może się jeszcze przydać przy innych wpisach. Dlatego instrukcje na temat korzystania z&nbsp;niego wydzieliłem do [osobnego samouczka](/tutorials/hat-sh-szyfrowanie){:.internal}.

## Dystopijny wyścig zbrojeń

OK. Czyli kontrola czatu może wyłapywać niewinnych i&nbsp;nie działać na winnych.  
Spójrzmy na jeszcze jedno zagrożenie. **Pokusy związane z nadużyciami i&nbsp;poszerzaniem zakresu śledzenia**.

Pokusa numer jeden -- mając infrastrukturę, można łatwo ją wzbogacać o&nbsp;nowe filtry, niezwiązane z&nbsp;dziećmi.  
Wykrywanie treści antyrządowych, niezadowolenia społecznego, opozycyjnych myśli. Idealna zabawka dla rządów autorytarnych, gdyby kiedyś doszły do władzy.

Wyżej na schemacie widzimy, że można użyć jednej aplikacji do obejścia ograniczeń obecnych w&nbsp;innej.  
Politycy mogą to dojrzeć. I, zamiast uznać swoją wizję za bezcelową, ulec pokusie numer dwa. Spróbować wcisnąć śledzenie na bardziej pierwotne poziomy.

W pierwszej kolejności mogliby uderzyć do twórców systemów operacyjnych i&nbsp;to na nie przerzucić obowiązek monitorowania. *De facto* wystarczyłoby nakłonić Apple, Microsoft i&nbsp;Google, bo mają miażdżącą przewagę na rynku.

Zapewne poszłoby z&nbsp;nimi szybko. W&nbsp;końcu Apple już od 2021&nbsp;roku próbował na własną rękę [wprowadzić monitoring treści](https://cyberdefence24.pl/bezpieczenstwo-informacyjne/apple-w-ogniu-krytyki-za-csam-to-forma-cenzury). Ale wycofał się po protestach użytkowników.

W takiej sytuacji nie miałoby znaczenia, na ile ufamy aplikacjom. **Warstwy wyższe są zależne od niższych. System, będąc fundamentem dla aplikacji, ma nad nimi władzę**. Widziałby wszystko.

W takiej sytuacji ludzie chcący choć namiastki prywatności mogliby się zwrócić ku alternatywnym systemom, takim jak Linux w&nbsp;różnych postaciach. Zapewne przeżyłby renesans. A&nbsp;że jest rozproszony i&nbsp;niezależny od konkretnej firmy, to trudniej byłoby naciskać na jego twórców.

Tyle że w&nbsp;tej sytuacji politycy zeszliby jeszcze niżej. Do producentów *hardware'u* -- złożonych fizycznych elementów, na których opiera się współczesna elektronika. Obserwator umieszczony na tym poziomie widziałby wszystko, co robi nasze urządzenie. Dla większości osób byłby niemożliwy do usunięcia.

{:.bigspace}
<img src="/assets/posts/inwigilacja/chat-control/szyfrowanie-hardware-game-over.jpg" alt="Schemat rozszerzający poprzednie piramidki o&nbsp;dwie niższe warstwy. Jedna jest podpisana jedynie trzema kropkami, a&nbsp;ta pod nią, najniższa, jako 'hardware'. Widać tam ikonę procesora, częściowo zakrytą przez ikonę wszechwidzącego oka. Odchodzi od niego na obie strony czerwona ramka, otaczająca cały schemat."/>

Wizja ingerencji na tym poziomie to nie *science fiction*. Już teraz mamy chipy, które niekoniecznie służą użytkownikom: 

* „komputery w&nbsp;komputerze”, jak nieprzenikniony [Intel Management Engine]({% post_url 2021-07-27-intel-management-engine %}){:.internal} zagnieżdżony w&nbsp;procesorach Intela;
* mniejsze chipy niezależne od reszty systemu. Zdolne ujawniać pytającym, czy nasz system był w&nbsp;jakiś sposób modyfikowany względem stanu domyślnego.

  Google planował oprzeć na nich swoje rozwiązanie, nazwane [Web Environment Integrity]({% post_url 2023-07-29-web-environment-integrity %}){:.internal}. Zdolne zamienić internet w&nbsp;coś na kształt grodzonych osiedli deweloperskich, wpuszczających tylko aprobowane urządzenia.

**Gdyby śledzenie zeszło na poziom fizycznego sprzętu, to raczej koniec gry**. W&nbsp;tym segmencie jest niewiele alternatyw.

A gdyby nawet ktoś opracował sposób na obejście ograniczeń, to tylko promil ludności umiałby coś zrobić.  
Bo sposób nie polegałby już na prostym „pobierzcie i&nbsp;zainstalujcie X”. Zaczynałby się od słów „weźcie mikroskop i&nbsp;lutownicę...”.

I tym dystopijnym akcentem kończę część główną. Mam nadzieję, że dość jasno pokazałem swoje nastawienie względem kontroli czatów :wink: Zachęcam do zrobienia hałasu w&nbsp;internecie albo dołączania do petycji przeciw zmianom.

Dla chętnych mam jeszcze szybki i&nbsp;prosty -- ale bardziej dla zabawy niż na serio -- sposób na uczynienie czatów nieco mniej czytelnymi.

## Bonus: szybkie maskowanie tekstu

Dzięki Hatowi mamy pełnoprawne szyfry, ale ma to wadę od strony praktycznej -- otrzymujemy pliki binarne. Surowe bloki zer i&nbsp;jedynek.

Raczej w&nbsp;żaden czat tego nie wkleimy, bo te wymagają formy tekstowej.  
Pozostanie nam dodawanie zaszyfrowanych plików jako załączników. Do przeżycia przy zdjęciach. Ale męczące przy zwykłych wiadomościach tekstowych. 

Ale -- **jeśli nie wysyłamy wrażliwych rzeczy -- można użyć szybkiego i&nbsp;powierzchownego zamaskowania tekstu. Przez zmianę kodowania**.

Współczesne przeglądarki mają taką opcję w&nbsp;pakiecie. Wystarczy zero umiejętności koderskich oraz kilka sekund, żeby zmienić wiadomości w&nbsp;postać nieczytelną dla człowieka. A&nbsp;po stronie odbiorcy -- żeby odzyskać pierwotną postać.

Użyjemy do tego funkcji [`btoa` oraz `atob`](https://stackoverflow.com/questions/23223718/failed-to-execute-btoa-on-window-the-string-to-be-encoded-contains-characte), wbudowanych w&nbsp;przeglądarki. Pozwalają przekształcić tekst do postaci nazwanej [*Base64*](https://www.akshaykhot.com/base64-encoding-explained/).

Siadamy sobie do komputera, uruchamiamy przeglądarkę (sprawdzałem na Firefoksie i&nbsp;Chromium). Naciskamy klawisze `Ctrl+Shift+I` (jak Irena).  
Otworzą się narzędzia przeglądarki. Wybieramy u&nbsp;góry zakładkę `Konsola`. Tam możemy sobie wpisywać różne komendy. Żeby zakodować tekst w&nbsp;formie *Base64*, wpisujemy:

<pre class="black-bg  mono">
btoa(unescape(encodeURIComponent("<span class="red">NASZ TEKST</span>")))
</pre>

{:.post-meta .bigspace-after}
Gdybyśmy nie używali polskich znaków, to wystarczyłoby samo `btoa("TEKST")`.  
Można użyć cudzysłowów pojedynczych albo podwójnych. Obojętne, byle takie same nie znajdowały się *wewnątrz* naszego tekstu.

Pod spodem albo obok powinien się wyświetlić nasz tekst w&nbsp;nowym kodowaniu:

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/chat-control/base64-kodowanie.jpg" alt="Dwie linijki konsoli. W&nbsp;górnej widać wiadomość o&nbsp;treści 'Piąteczka, mistrzu!' oraz emotkę dłoni zbijających piątkę. Pod spodem widać tę wiadomość w&nbsp;kodowaniu base64, złożonym z&nbsp;liter oraz liczb, z&nbsp;kilkoma znakami równości na końcu"/>

Zakodowaną wiadomość możemy sobie skopiować do czatu i&nbsp;komuś wysłać.  
Po odebraniu druga osoba otwiera u&nbsp;siebie konsolę i wkleja zakodowaną treść w&nbsp;odwrotność wcześniejszej funkcji. Zobaczy tekst od nas.

<pre class="black-bg  mono">
decodeURIComponent(escape(atob("<span class="red">ZAKODOWANY TEKST</span>")))
</pre>

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/chat-control/base64-dekodowanie.jpg" alt="Dwie linijki konsoli. W&nbsp;górnej widać wiadomość zakodowaną w formacie base64 wewnątrz funkcji dekodującej. Pod spodem mamy oryginalną treść wiadomości."/>

{% include info.html
type="Uwaga"
text="Dla jasności -- **_Base64_ to nie jest szyfr. Komputery byłyby w&nbsp;stanie łatwo wykryć, że wiadomość zawiera to kodowanie i&nbsp;je odwrócić**.  
Osoby chętne mogłyby dorzucić na wierzch [trochę innych przekształceń](https://stackoverflow.com/questions/6795714/what-is-a-good-method-for-obfuscating-a-base-64-string) i&nbsp;utrudnić im zadanie. Ale to nadal kwestia czasu i&nbsp;pracy. Gdyby podglądaczom zależało, to odczytają.  
Z tego względu B64 można użyć bardziej w&nbsp;ramach obywatelskiego nieposłuszeństwa. Żeby hipotetyczny podglądacz musiał nieco mocniej wysilić procesor :smiling_imp:"
%}

## Źródła obrazków

* plik tekstowy z&nbsp;systemu Linux;
* pudło z&nbsp;sercem z&nbsp;gry „Portal”;
* kłódki i&nbsp;kluczyki z&nbsp;Emojipedii;
* [ostrzeżenie](https://www.flaticon.com/free-icon/exclamation_10308557?term=warning&related_id=10308557) -- Fatema Khanom z&nbsp;serwisu Flaticon;
* oficjalne ikonki Signala i&nbsp;Firefoksa.

