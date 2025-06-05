---
layout: post
title: "2025 – rok dobry dla Linuksa?"
subtitle: "Gdy wielkie okno pęka, nawet pingwin może je rozbić."
description: "Gdy wielkie okno pęka, nawet pingwin może je rozbić."
date:   2025-04-22 08:00:34 +0100
tags: [Linux, Open Source, Podstawy, Przemyślenia]
firmy: [Microsoft]
image:
  path: /assets/posts/open_source/2025-rok-linuksa/linux-windows-breaker.jpg
  width: 1200
  height: 700
  alt: "Wygenerowany obraz pokazujący uśmięchniętego pingwina, który rozbija kopnięciem szklaną szybę podświetloną różowym neonem"
---

„To będzie rok Linuksa”.

Te słowa stały się swoistym memem. Niszowym co prawda na tle piesełów albo pewnego żółtawego oblicza z&nbsp;Polski... Ale też nie całkiem hermetycznym -- **Linux w&nbsp;ostatnich latach zyskał na popularności**.

{:.bigspace-before}
<img src="/assets/posts/open_source/2025-rok-linuksa/linux-windows-breaker.jpg" alt="Wygenerowany obraz pokazujący uśmięchniętego pingwina, który rozbija kopnięciem szklaną szybę podświetloną różowym neonem"/>

{:.figcaption}
Źródło: Bing Create, generator od Microsoftu -- bo bawi mnie używanie przeciw komuś jego własnych narzędzi :smiling_imp:

Mogły o&nbsp;nim usłyszeć nawet osoby traktujące swój komputer i&nbsp;jego system jak nierozłączne. Zwykli ludzie, którzy włączają MacBooka i&nbsp;widzą system MacOS. Włączają laptopa-gotowca ze sklepu i&nbsp;ładuje im się Windows.

...Ale jest szansa, że tym samym osobom załaduje się też jakieś popularne forum internetowe. A&nbsp;tam, nawet na głównej osi czasu, w&nbsp;wątkach nie tylko komputerowych, [pada czasem wzmianka o&nbsp;Linuksie](https://www.reddit.com/r/Polska/comments/1742jx3/a_czy_ty_znasz_linuxa/) -- alternatywnym, otwartym systemie, którego maskotką jest pingwin Tux.

{:.post-meta .bigspace-after}
Ściśle rzecz biorąc: to nie tyle system, co wspólny „silnik” wielu systemów. Ale w&nbsp;tym wpisie traktuję je zbiorczo.

W takich dyskusjach ktoś często ironizuje, że aktualny rok będzie rokiem Linuksa.  
Przesłanie: fani Linuksa są wobec rzeczywistości trochę jak Syzyf wobec głazu albo Achilles wobec żółwia. Każdorazowo liczą, że ich kochany system zyska powszechne uznanie... Po czym nic się nie dzieje i&nbsp;wszystko zostaje po staremu.

Ale *ten* rok (2025), choć pewnie nie postawi spraw na głowie, może przynieść różnym odmianom Linuksa realny wzrost popularności. A&nbsp;to dlatego, że **zachodzi unikalny splot czynników, dobry dla otwartych alternatyw**.

Kończy się wsparcie dla Windowsa 10, a&nbsp;jego następca, Windows 11, nieco sobie nagrabił brakiem zgodności z&nbsp;wieloma komputerami. Nie mówiąc o&nbsp;innych jego niedoskonałościach.  
W tle mamy też rosnący izolacjonizm USA, skłaniający Europę do mocno spóźnionych myśli o&nbsp;niezależności, również cyfrowej.

W tym wpisie przybliżę te czynniki, robiąc przy tym małą reklamę szeroko rozumianemu Linuksowi. Jeśli zainspiruję osoby lubiące pingwina do jego dalszego promowania -- super! Jeśli uda się wciągnąć w&nbsp;ten świat jakieś nowe osoby -- jeszcze lepiej! :smile:

## Spis treści

* [Linux kontra Windows – analogie](#linux-kontra-windows--analogie)
* [Ciemne chmury nad Windowsem](#ciemne-chmury-nad-windowsem)
  * [Koniec wsparcia dla Windowsa 10](#koniec-wsparcia-dla-windowsa-10)
  * [Windows 11&nbsp;i wymóg modułu TPM](#windows-11i-wymóg-modułu-tpm)
  * [Liczne słabości Windowsa 11](#liczne-słabości-windowsa-11)
  * [Inne czynniki](#inne-czynniki)
* [Podsumowanie](#podsumowanie)


## Linux kontra Windows – analogie

Bohaterami tego wpisu są dwa systemy operacyjne -- Linux i&nbsp;Windows.

O Windowsie, rozwijanym przez firmę Microsoft, słyszał chyba każdy, nawet pokolenie smartfonowe. W&nbsp;końcu to najpopularniejszy system operacyjny na świecie. Stosowany w&nbsp;szkołach, mniejszych i&nbsp;większych firmach, do użytku domowego...

{% include info.html
type="Ciekawostka"
text="Jeśli przyjąć za początek tego systemu jego pierwsze wydanie wymienione na Wikipedii, to w&nbsp;tym roku (20&nbsp;listopada) [będzie obchodził swoje 40-lecie](https://pl.wikipedia.org/wiki/Microsoft_Windows)."
%}

Linux jest dużo mniej znany, choć nieco zyskał na popularności. To darmowa i&nbsp;otwarta alternatywa dla Windowsa. Działa jak każdy system: pojawia się tuż po włączeniu urządzenia i&nbsp;śmiga w&nbsp;tle, gdy z&nbsp;tego urządzenia korzystam.

Żeby nie zaschło nam w&nbsp;gardle od suchych faktów, pozwolę sobie na chwilę luźnej gawędy. O&nbsp;tym, **czym oba systemy są _dla mnie_, całkiem subiektywnie**. Mam porównanie, bo używałem obu.

Jeśli chodzi o&nbsp;Linuksa: uważam się za jego sympatyka, ale nie fanatyka. Dużo silniejszymi uczuciami darzę szerszy ruch *open source*, którego jest częścią. Samego Linuksa postrzegam po prostu jak system operacyjny. Coś, przez co przechodzę w&nbsp;drodze do różnych programów, z&nbsp;czasem jak na autopilocie.

Ale nawet patrząc z&nbsp;tego punktu widzenia -- „zwykłe przejście w&nbsp;drodze dokądśtam” -- jestem w&nbsp;stanie wyraźnie postawić Linuksa nad Windowsem. Bo twór Microsoftu robi mi rzeczy, o&nbsp;które nie prosiłem. Zmienia przestrzeń dookoła; zwykle nie dla mnie, tylko po to, żeby jakiś manager z&nbsp;Microsoftu się wykazał.

Trzymając się porównania do przejścia -- **obecny Windows jest jak główna ulica metropolii**. Pokryta plakatami i&nbsp;ekranami, których treść stale się zmienia. Diety pudełkowe, seriale w&nbsp;abonamencie. „Subskrybuj! Kupuj!” (patrz: [reklamy dodane do menu głównego](https://www.rmfmaxx.pl/news/Microsoft-zaczal-wyswietlac-reklamy-w-Windowsie-Jak-je-wylaczyc,77744.html)).  
Wyburzono sprawny przystanek i&nbsp;postawiono zamiast niego minimalistyczną wiatę, która wygląda nowocześnie, ale nie osłania przed słońcem ani deszczem (patrz: [redukcja opcji w&nbsp;menu podręcznym](https://www.benchmark.pl/testy_i_recenzje/jak-zmienic-menu-kontekstowe-windows-11-na-stare-z-windows-10.html)). Bo musi się dziać, musi być dynamizm, coraz więcej szkła i&nbsp;chromu.

Przez nieprzemyślane zmiany ulica się korkuje i&nbsp;[działa wolniej](https://www.reddit.com/search/?q=%22windows+explorer%22+%22slow%22). Przez betonowanie wszystkiego brakuje cienia i&nbsp;robi się piekarnik (patrz: [program od maili przeciążający procesor](https://ithardware.pl/aktualnosci/outlook_procesor_microsoft_blad-40839.html)). Ale włodarzy nie obchodzą podstawy, tylko nowinki.  
Chcą montować inteligentne kamery monitoringu wizyjnego, bo AI jest teraz na czasie, po czym okazuje się, że słabo pilnują nagrań (na Windowsie: [afera wokół funkcji Recall](https://doublepulsar.com/recall-stealing-everything-youve-ever-typed-or-viewed-on-your-own-windows-pc-is-now-possible-da3e12e9465e)). Plakat z&nbsp;geometrycznymi, kolorowymi ludzikami reklamuje nowinkę bezpłciowym sloganem: „mamy na oku twoje bezpieczeństwo”.

{% include info.html
type="Heheszki"
text="Inną cechą łączącą Windowsa z&nbsp;metropolią jest niefrasobliwe podejście do polszczyzny. Po co tłumaczyć plakaty i&nbsp;billboardy, gdy w&nbsp;jednym języku wychodzi taniej, a&nbsp;do tego inglisz jest *fancy*?  
Na stronie Microsoftu podstawowe treści są po angielsku, nieruszone nawet automatem. Są nim natomiast tłumaczone -- niepoprawnie -- nagłówki powtarzające się między stronami. Takie jak pole `Tip` („Porada”), [tłumaczone jako... „Napiwek”](https://web.archive.org/web/20250416200807/https://learn.microsoft.com/pl-pl/microsoft-365-apps/updates/change-update-channels)."
trailer="<p class='bigspace-before figure'><img src='/assets/posts/open_source/2025-rok-linuksa/windows-tip-napiwek.jpg' alt='Zrzut ekranu pokazujący angielski tekst pod nagłówkiem Napiwek'></p>"
%}

**Linux jest z&nbsp;kolei jak droga przytulnymi, bocznymi uliczkami** albo przez park.  
Zapewnia odrobinę eskapizmu i&nbsp;wytchnienia od gonitwy. Nikt nie próbuje niczego mi wcisnąć, szum miasta jest tutaj przytłumiony.

Nadal mogę dojść w&nbsp;wiele tych samych miejsc, co głównymi ulicami. Do tego nie jest to zacofana okolica -- modernizacja zachodzi po prostu pod spodem, w&nbsp;sposób nieinwazyjny dla zwykłego człowieka. Ale infrastruktura jest nowoczesna i&nbsp;fajnie śmiga.  
Za to korporacyjny, kosmopolityczny harmider tu nie wpełznie. Po pierwsze: nie wycisnąłby stąd kasy. Po drugie: nie byłby tu mile widziany.

## Ciemne chmury nad Windowsem

Wyżej były ogólniki, więc teraz czas na parę konkretnych zarzutów wobec Windowsa. Co sprawiło, że jest teraz na słabszej pozycji niż wcześniej, a&nbsp;jego drobniejsza konkurencja ma okazję się wybić?

### Koniec wsparcia dla Windowsa 10

Kiedyś, w&nbsp;2015 roku, Microsoft zapowiadał, że [Windows 10&nbsp;będzie ostatnią numerowaną wersją ich systemu](https://www.tabletowo.pl/microsft-ostatni-windows-10-tak-mialo-byc/). W&nbsp;domyśle: osiągnęli szczyt, więc od teraz czas na niekończące się aktualizacje i&nbsp;dopracowywanie systemu, żeby dążył ku perfekcji.

...Ale potem im się odwidziało. Dlaczego?  
Autor podlinkowanego artykułu spekuluje, że w&nbsp;ten sposób Microsoft mógłby łatwiej rozdzielić użytkowników według tego, czy działa u&nbsp;nich pewien układ elektroniczny (o&nbsp;którym za moment).  
Oczywiście możliwe również, że ktoś w&nbsp;garniaku spojrzał na giełdową kreskę i&nbsp;po prostu uznał, że nowa wersja bardziej ją pociągnie w&nbsp;górę. Kto wie.

W każdym razie: w&nbsp;2021 roku wydano Windowsa 11.

A że nie chcą równoległe utrzymywać dwóch systemów, to od paru lat konsekwentnie wygaszają dziesiątkę. [Oficjalna strona Microsoftu głosi takie coś](https://www.microsoft.com/pl-pl/windows/end-of-support) (wyróżnienia moje):

{:.bigspace}
> **Po 14&nbsp;października 2025&nbsp;r.** firma Microsoft nie będzie już zapewniać bezpłatnych aktualizacji oprogramowania za pośrednictwem usługi Windows Update, pomocy technicznej ani poprawek zabezpieczeń dla systemu Windows 10. Twój komputer będzie nadal działać, ale **zalecamy przejście na system Windows 11**.

W praktyce: na początku wygaszenie wsparcia może być niezauważalne. Ale z&nbsp;każdym kolejnym miesiącem będzie przybywało nowinek technicznych, których twórcy będą celowali już tylko w&nbsp;Windowsa 11. Będzie też przybywało złośliwych programów mogących łatwo przebić zabezpieczenia systemu.

Wydaje się, że w&nbsp;takiej sytuacji zachęty do przejścia na Windowsa 11&nbsp;są spore. Kiedyś Microsoft nawet oferował aktualizację za darmo.

A jednak cały czas większość komputerów trzyma się dziesiątki.  
Co z&nbsp;tymi ludźmi, zacofani jacyś? Nie. Po prostu **Microsoft stawia sztuczne wymagania, przez które wiele sprawnych komputerów nie uruchomi Windowsa 11**.

### Windows 11&nbsp;i wymóg modułu TPM

Windows 11&nbsp;zadziała jedynie na tych komputerach, które zawierają w&nbsp;sobie mały, niedostępny dla użytkowników moduł kryptograficzny -- *Trusted Platform Module*.

Wymóg wydaje się kompletnie arbitralny (po ludzku: wzięty z&nbsp;czapy). Ktoś może mieć całkiem sprawne urządzenie, które sprostałoby niemal wszystkim wymogom jedenastki. Ale jeśli nie ma pod obudową jednego, małego podzespołu... To nic nie ruszy. System odmówi działania.

{:.figure .bigspace-before}
<img src="/assets/posts/open_source/2025-rok-linuksa/windows-tpm-blokada.jpg" alt="Komunikat mówiący, że na systemie nie można uruchomić Windowsa 11"/>

{:.figcaption}
Źródło: [filmik od serwisu *Komputer Świat*](https://www.youtube.com/watch?v=zUS-QyfCHo4).  
W praktyce istniały/istnieją pewne metody obejścia wymogu. Ale dla znacznej większości użytkowników to zbyt wiele zachodu, więc je pominę.

Co gorsza, rozwiązania takie jak TPM, choć formalnie wprowadzane w&nbsp;celu poprawienia cyberbezpieczeństwa, w&nbsp;świecie rzeczywistym bywają stosowane w&nbsp;gorszych celach.

{% include details.html summary="Moduł TPM może być narzędziem kontroli" %}

{:.post-meta .bigspace-after}
Sprawę opisałem dokładniej we wpisie na temat [nurtu *trusted computing*](/cyfrowy_feudalizm/2024/10/22/trusted-computing-kajdany){:.internal}, tutaj jedynie streszczenie.

Wobec rzeczy takich jak TPM (jak odrębne chipy, ale również zamknięte podsystemy kart graficznych, „komputery w&nbsp;komputerze” itd.) stosuję nieformalne pojęcie zbiorcze -- **enklawy**. Obszary silnie niezależne od reszty systemu.

Niezależność od systemu daje też niezależność od użytkowników. Ma to *jakieśtam* uzasadnienie z&nbsp;punktu widzenia cyberbezpieczeństwa -- nawet gdyby do systemu dorwał się haker, to największe sekrety, ukryte wewnątrz enklawy, pozostaną poza jego zasięgiem.

Do tego część enklaw może działać trochę jak niezależni audytorzy. Poddawać inspekcji głębsze warstwy urządzenia i&nbsp;oceniać, czy nie ukryły się tam wirusy.

Problem: mogąc wydawać wyroki, enklawa zyskuje władzę. A&nbsp;władza deprawuje.  
Megafirmy komputerowe, jak Google i&nbsp;Microsoft, zrobiły sobie z&nbsp;enklaw takich własnych, wiernych notariuszy. Wykorzystują je do **poświadczania, że użytkownicy mają na systemie ograniczone możliwości**. A&nbsp;potem oferują takie gwarancje innym gigantom:

* Wielkie wytwórnie chciałyby, żeby nikt nie mógł kopiować ich filmów.

  Enklawy to umożliwiają -- dane są do nich przekazywane w&nbsp;postaci zaszyfrowanej i&nbsp;tam obrabiane. Konwersja na obraz następuje dopiero pod sam koniec, na monitorze, przez co użytkownik nijak ich nie przechwyci.

* Twórcy aplikacji chcą mieć pewność, że dostają prawdziwe informacje na temat cech użytkownika, takich jak jego lokalizacja.

  W&nbsp;świecie smartfonów mogą wykorzystać funkcję Play Integrity od Google'a. Pozwala ona pytać enklawy: „czy to czysty, fabryczny system?”. Odpowiedź „tak/nie” z&nbsp;założenia zawsze będzie prawdziwa, oznaczona niepodrabialnym cyfrowym podpisem.

  Dodajmy do tego gwarancję od Google'a, że taki czysty system blokuje możliwość edytowania lokalizacji -- w&nbsp;ten sposób aplikacja ma pewność, że dostaje na talerzu prawdziwe, niemodyfikowane dane.

  {:.post-meta}
  Dość nieoczekiwanym przykładem apki wykorzystującej Play Integrity (choć nie wiem, czy akurat do zbierania lokalizacji) może być [ta od sieci McDonald's](/google/2021/10/30/google-skandale-wprowadzenie#android-system-operacyjny){:.internal}. Typowe: jeden amerykański gigant dogadany z&nbsp;innym, ręka rękę myje.

A coś ze świata Windowsa? Już kilka lat temu, krótko po wypuszczeniu W11, firma Riot Games [zapowiedziała](https://arstechnica.com/gaming/2021/09/riot-games-anti-cheat-software-will-require-tpm-secure-boot-on-windows-11/), że ich gra wykorzysta TPM-a i&nbsp;wszelkie oferowane przez niego uszczelnienia. Widać korporacyjny popyt na takie cyfrowe bariery.

Podsumowując: TPM-a da się wykorzystać do celów nijak mających się do bezpieczeństwa. Może on sprawiać, że użytkownicy nie mają pełnej kontroli nad sprzętem, a&nbsp;nad ich głowami mogą zachodzić różne zmowy. Na razie to zmowy korporacyjne, ale rządy też mogłyby kiedyś sięgnąć po kontrolę gwarantowaną przez układy w&nbsp;stylu TPM-ów.

{% include details-end.html %}

Ale nawet użytkownicy, których mniej interesuje autonomia, mogą się wkurzać samym niedziałaniem sprzętu.  
Etyka konsumpcjonizmu nakazuje wprawdzie, żeby w&nbsp;tej sytuacji wywalić sprzęt na śmietnik i&nbsp;niezwłocznie kupić nowy (Microsoft [w oficjalnych mailach zachęca: „oddajcie do recyklingu”](https://ithardware.pl/aktualnosci/microsoft_windows_10-40015.html))... Ale ludzie nie są zachwyceni.

Niektórzy mają nadzieję, że MS ustąpi, widząc niezadowolenie. Ale nie liczyłbym na to -- parę miesięcy temu [całkiem usunęli opis metody obejścia](https://www.neowin.net/news/microsoft-quietly-removes-official-windows-11-cputpm-bypass-for-unsupported-pcs/) ze swojej oficjalnej strony, jasno pokazując swoje nastawienie.

To ogromna szansa dla alternatyw, które żadnego wsparcia nie planują ucinać i&nbsp;pozwolą dalej korzystać z&nbsp;urządzeń. A&nbsp;że jedna z&nbsp;nich (MacOS) jest mniej przystępna cenowo, to rośnie szansa, że więcej osób przynajmniej spróbuje Linuksa.

### Liczne słabości Windowsa 11

Choć mało kto to pamięta, na samym początku swojego istnienia Windows 11&nbsp;miał z&nbsp;założenia [być szybszy od dziesiątki](https://www.neowin.net/news/microsoft-windows-11-is-designed-to-get-the-best-out-of-hardware-heres-how/) i&nbsp;poprawić jej niedociągnięcia. Niektórzy chwalili Microsoft za chęć zwrotu ku fundamentom, naprawienia dotychczasowych bolączek, świeży start.

Od tamtego czasu nastąpiła jednak równia pochyła. Być może w&nbsp;pogoni za rosnącą giełdową kreską zredukowano zatrudnienie lub przeniesiono część procesów myślowych do tańszych miejsc?

Nie wiem. W&nbsp;każdym razie nowy Windows jest pełen zadziorów, na które nabijają się użytkownicy.

Jedna z&nbsp;krzywych akcji pojawia się już po pierwszej próbie włączenia systemu. **Microsoft wymaga przy pierwszym logowaniu połączenia z&nbsp;internetem i&nbsp;naciska na założenie u&nbsp;nich konta**.

Wkurzało to ludzi już na Windowsie 10&nbsp;-- w&nbsp;końcu nie każdy ma internet pod ręką, sytuacje są różne. Dało się jednak obejść głupawy wymóg, otwierając konsolę pewną kombinacją klawiszy i&nbsp;wpisując magiczne zaklęcie:

```
oobe\BypassNRO
```

Microsoft jednak chyba nie polubił faktu, że niektórzy pomijali zakładanie konta i&nbsp;[celowo usunął wygodne polecenie](https://spidersweb.pl/2025/03/windows-11-bypassnro.html). Od teraz sposób na pierwsze logowanie bez internetu stał się znacznie bardziej zagmatwany:

{:.figure .bigspace-before}
<img src="/assets/posts/open_source/2025-rok-linuksa/bypass-nro-nie-dziala-spidersweb.jpg" alt="Opis zawiłego sposobu na edytowanie rejestru i&nbsp;zyskanie możliwości uruchomienia Windowsa bez internetu. Pod koniec uwaga, że w&nbsp;każdej chwili Microsoft może sprawić, że sposób przestanie działać."/>

{:.figcaption}
Źródło: artykuł podlinkowany wyżej.  
...A niektórzy twierdzą, że to Linux jest skomplikowany i&nbsp;dla komputerowców :roll_eyes:

W każdym razie -- czy to zakładając konto, czy robiąc fikołki i&nbsp;obchodząc naciski -- w&nbsp;końcu uruchomimy Windowsa.  
Czy warto było? Czekają na nas: domyślnie włączona telemetria (gromadzenie danych i&nbsp;wysyłanie ich do Microsoftu), reklamy innych usług firmy, powiadomienia informujące o&nbsp;nowych bzdurkach do wypróbowania.

I reklamy. Wyżej, w&nbsp;części bardziej gawędziarskiej, wspomniałem o&nbsp;tych wpychanych do menu startowego. Nie wspomniałem natomiast o&nbsp;tym, że ponoć są wyświetlane nawet w&nbsp;tej korporacyjnej wersji systemu, Windows Professional:

{:.figure .bigspace-before}
<img src="/assets/posts/open_source/2025-rok-linuksa/windows-11-pro-reklamy.jpg" alt="Krytyczny tweet pokazujący, że komuś na systemie Windows Professional wyświetliła się reklama gry"/>

{:.figcaption}
Źródło: Twitter/X ([przez *xcancel.com*](https://xcancel.com/MalwareJake/status/1907807303509631440#m)).  
...Ale dla niektórych wciąż to Windows jest *appropriate* i&nbsp;*professional*, a&nbsp;Linux to amatorka :roll_eyes:

Jedźmy dalej. Każda osoba używająca Windowsa zapewne dość szybko skorzysta z&nbsp;Eksploratora (przeglądarki plików). Choć to sam filar systemu, potrafi [działać nieznośnie wolno](https://www.reddit.com/r/Windows11/comments/1botfkq/loving_windows_11_but_this_sluggish_file_explorer/).

{% include info.html
type="Heheszki"
text="I tutaj hit -- żeby temu zapobiec, należy (lub należało) nacisnąć dwukrotnie kombinację klawiszy `Ctrl+F11`, żeby powiększyć i&nbsp;znów zmniejszyć okno.  
W ten sposób, przez jakiś błąd programu, przestanie działać górny pasek... I&nbsp;wszystko nagle stanie się dużo szybsze, bo to w&nbsp;górnym pasku tkwiła rzecz spowalniająca całego Eksploratora.  
Nie wierzyłem, jak czytałem. Ale to prawda."
%}


Coś więcej? Według dużo nowszej dyskusji z&nbsp;forum, powolność Eksploratora się utrzymała. Do tego znany jest przypadek, gdy przez ustawienia językowe [niektórym przestał działać skrót `Ctrl+A`](https://www.reddit.com/r/Windows11/comments/1ifdu6j/comment/mal8p97/). Podstawa podstaw, sposób na zaznaczenie wszystkich rzeczy w&nbsp;aktywnym folderze.

Ktoś chce więcej przykładów niedoróbek? Można sobie [wyszukać w&nbsp;mediach społecznościowych](https://xcancel.com/search?f=tweets&q=%22windows+11%22+%22slow%22) kombinację słów `"windows 11" slow`. Wyskoczą niezliczone relacje od niezadowolonych osób.

Ogólnie: Windows 11&nbsp;to pod wieloma względami piękna katastrofa. Dzięki jego licznym lapsusom nawet niemałe grono osób ze wspieranym sprzętem rozważa odejście ku alternatywom. Do tych, którzy jeszcze siedzą na dziesiątce, kierują ostrzeżenia. „Nie idźcie tu, to pułapka!”.

Ponownie: ogromna szansa dla Linuksa.

### Inne czynniki

Pomijając słabości samego Windowsa, na świecie zaszło też parę innych zmian działających na korzyść Linuksa.

Po pierwsze: **zastępowanie wielu programów platformami internetowymi**.

Kiedyś komputer był właściwie pełnoprawnym biurem zamkniętym w&nbsp;jednym urządzeniu, a&nbsp;wszystkie programy trzymało się u&nbsp;siebie.  
Od tamtego czasu rzeczywistość mocno się zmieniła i&nbsp;teraz nawet giganci, tacy jak Adobe czy sam Microsoft, lubią przenosić swoje programy do *chmury*, czyli w&nbsp;praktyce internetu.

{:.post-meta .bigspace-after}
Istnieją nawet okrojone urządzenia takie jak Chromebooki, które są bliższe minimalistycznym portalom do internetu niż klasycznym laptopom.

Oczywiście firmy nie robią tego z&nbsp;dobroci serca, tylko z&nbsp;chęci kontroli -- w&nbsp;taki sposób mogą łatwiej narzucać ludziom model subskrypcyjny. Samo przenoszenie świata do chmury od dawna jest [krytykowane na moim blogu](/cyfrowy_feudalizm/2021/04/07/cyfrowy-feudalizm-fakty#przenoszenie-wszystkiego-do-chmury){:.internal}.

...Ale odchodzenie od klasycznych programów można też wykorzystać na swoją korzyść. Przerzucanie biura do internetu może bowiem rozwiązać odwieczny problem -- „na Linuksie nie działa mi program potrzebny do pracy”.

W czasach, gdy to przeglądarka staje się nowym systemem operacyjnym, nieco traci znaczenie fakt, że na Linuksie nie działa jakiś program. Dopóki działa przeglądarka, a&nbsp;w przeglądarce internetowa wersja -- nasz otwarty system może pozostać narzędziem pracy.

Po drugie: **myśli Europy o&nbsp;suwerenności**.

Rosnący izolacjonizm Stanów Zjednoczonych wisiał w&nbsp;powietrzu już od lat (proponuję poszukać analiz pod hasłem „koniec globalizacji” -- w&nbsp;znaczeniu politycznym, nie spiskowym).  
Ale od czasu zmiany rządzących sprawy dramatycznie przyspieszyły. Zaczęto kwestionować stabilność dawnego sojusznika, a&nbsp;na terenie Europy coraz częściej mówi się o&nbsp;potrzebie niezależności od nich. Rychło w&nbsp;czas :roll_eyes:

Tę sytuację również można wykorzystać na korzyść otwartych rozwiązań, w&nbsp;tym Linuksa. Będą coraz częstsze debaty o&nbsp;suwerenności, w&nbsp;tym cyfrowej. Czytając o&nbsp;zamiennikach, ludzie trafią na strony takie jak [*european-alternatives.eu*](https://european-alternatives.eu/). Dyskusje w&nbsp;mediach na pewno otrą się o&nbsp;kwestie systemów. 

Być może Unia sypnie nawet funduszami na promowanie alternatyw -- w&nbsp;końcu [ogłosiła nawet prace nad własnym wariantem Linuksa](https://www.webinside.pl/unia-europejska-stawia-na-linuxa-rewolucyjny-projekt-eu-os-oparty-na-fedorze/). A&nbsp;fundusze mogą ściągnąć nowych zainteresowanych, znających parę trików na skuteczne promowanie systemu.

## Podsumowanie

W ciągu najbliższych kilku lat -- a&nbsp;zwłaszcza w&nbsp;tym roku, a&nbsp;zwłaszcza w&nbsp;okolicach jesieni i&nbsp;końca wsparcia dla W10 -- Linux stanie przed unikalną szansą na zjednanie szerszego grona osób.

Jakość Windowsa się pogarsza, jego nowa wersja nie wspiera wielu komputerów, klasyczne programy biurowe nieco straciły na istotności na rzecz internetu, a&nbsp;rzeczy z&nbsp;USA mogą chwilowo być w&nbsp;niełasce.  
Te wszystkie czynniki zachodzą jednocześnie, sprawiając że więcej osób może wyszukać zwrotu, który kiedyś interesował nielicznych: `zamiennik dla Windowsa`.

Społeczność wspierająca otwarte rozwiązania może się postarać, żeby w&nbsp;odpowiedzi wyświetliło się: „Linux”.  
A pod podsuniętymi linkami: przystępne opisy działania, instrukcje i&nbsp;poradniki, również w&nbsp;formie filmików. Obalanie mitów, jak ten mówiący, że Linux wymaga korzystania z&nbsp;konsoli. Fora, na których ludzie pomagają, a&nbsp;odpowiedzi cwaniaczkowate i&nbsp;bufoniaste są blokowane.

Jest jeszcze trochę czasu, żeby to wszystko dopracować i&nbsp;nadgryźć nieco monopol, który przez długi czas wydawał się nie do ruszenia. Ze swojej strony **na pewno stworzę parę przewodników po Linuksie i&nbsp;zachęcam innych do tego samego**. Każda szczypta zachęt pomaga usypać pingwinowi ścieżkę do ludzkich komputerów :smile:

