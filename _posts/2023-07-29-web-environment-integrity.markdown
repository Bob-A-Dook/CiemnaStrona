---
layout: post
title:  "Web Environment Integrity – Google kontra wolny internet"
subtitle: "Jesteśmy nietypowi? Chrome na nas naskarży"
description: "Jesteśmy nietypowi? Chrome na nas naskarży"
date:   2023-07-29 21:37:08 +0100
tags: [Centralizacja, DRM, Hardware]
firmy: [Apple, Google, Mozilla]
category: google
category_readable: "Google – kolorowy czarny charakter"
image: 
   path: /assets/posts/google/web_environment_integrity/web-integrity-baner.jpg
   width: 1200
   height: 700
   alt: "Obrazek pokazujący kontury chłopca i psa, zwróconych bokiem do widza i oddzielonych od siebie półprzezroczystą ścianą. Chłopiec przykłada do niej rękę, a pies łapę. Po stronie chłopca tło jest pełne zer i jedynek, a u góry widać napis Google"
---

Już dawno nie było na tym blogu wpisu *ściśle poświęconego Google'owi*. Oczywiście firma nieraz się pojawiała w&nbsp;negatywnym kontekście, ale bardziej jako ilustracja ogólniejszych zjawisk.

Ale teraz, jak rzadko kiedy, warto skierować całą artylerię *konkretnie na nich*. Ponieważ w&nbsp;ostatnich dniach zaproponowali wbudowanie w&nbsp;swoją przeglądarkę -- Chrome'a -- nowej, dość dystopijnej funkcji.

Jeśli to wejdzie w&nbsp;życie, to przeglądarka będzie mogła na nas donosić. **Gwarantować stronom internetowym, że nasze urządzenia nie były modyfikowane w&nbsp;sposób, który by się tym stronom nie podobał**.

Pomysł dopiero się krystalizuje, ale już budzi sprzeciw.  
W skrajnych przypadkach właściciele stron mogliby nie wpuszczać ludzi mających mniej popularne systemy operacyjne (jak mobilne Linuksy), nietypowe przeglądarki (jak Tor Browser)... A&nbsp;może nawet dodatki do przeglądarek, jak te od blokowania śledzących reklam.

Internet użytkowników może zacząć zanikać na rzecz internetu firm (w&nbsp;domyśle: większych korpo).

Dlaczego to takie ważne? Dlaczego nowej funkcji nie będzie się dało w&nbsp;prosty sposób obejść? I&nbsp;dlaczego działania jednego Google'a uderzają we wszystkich?

Na te pytania -- w&nbsp;sposób jak najprzystępniejszy -- odpowiem w&nbsp;tym wpisie. Zapraszam!

{:.bigspace-before}
<img src="/assets/posts/google/web_environment_integrity/web-integrity-baner.jpg" alt="Obrazek pokazujący kontury chłopca i&nbsp;psa, zwróconych bokiem do widza i&nbsp;oddzielonych od siebie półprzezroczystą ścianą. Chłopiec przykłada do niej dłoń, a&nbsp;pies łapę. Część obrazka, po której stoi chłopiec, jest wypełniona zerami i&nbsp;jedynkami, a&nbsp;w górnej części widać logo firmy Google. Część, po której stoi pies, jest podpisana 'Internet'."/>

{:.figcaption}
Dla niektórych psinka to dodatek do przeglądarki. Dla innych alternatywny system na smartfona. Jedno jest pewne -- do internetu od korporacji nie wejdzie.  
Źródło: plakat filmu „Pod Kopułą” na podstawie książki Stephena Kinga; zera i&nbsp;jedynki z&nbsp;[Pixabay](https://pixabay.com/illustrations/binary-code-privacy-policy-woman-1327493/). Przeróbki moje.


## Spis treści

* [Zarys problemu](#zarys-problemu)
* [Web Environment Integrity – krok po kroku](#web-environment-integrity--krok-po-kroku)
  * [Cyfrowe enklawy](#cyfrowe-enklawy)
  * [Gwarancja podpisana cyfrowo](#gwarancja-podpisana-cyfrowo)
  * [Biurokratyczne uruchomienie](#biurokratyczne-uruchomienie)
  * [Łączymy to w&nbsp;całość](#łączymy-to-wcałość)
* [Dlaczego inni nie oleją Google'a?](#dlaczego-inni-nie-oleją-googlea)
  * [Zależność od Chromium](#zależność-od-chromium)
  * [Sprawa Apple'a](#sprawa-applea)
* [Realne zagrożenie](#realne-zagrożenie)
  * [Niepokojąca łatwość blokowania](#niepokojąca-łatwość-blokowania)
  * [Kwestia etyczna](#kwestia-etyczna)
  * [Wiarygodny scenariusz](#wiarygodny-scenariusz)
* [Jak z&nbsp;tym walczyć](#jak-ztym-walczyć)
* [Źródło obrazków](#źródło-obrazków)


## Zarys problemu

Wszystko zaczęło się od opublikowania przez pracownika Google'a paru luźnych [notatek](https://github.com/RupertBenWiser/Web-Environment-Integrity) dotyczących nowej funkcji. Zasugerował publicznie, że jest testowana w&nbsp;przeglądarce Chromium. Jej nazwa -- *Web Environment Integrity API*. W&nbsp;skrócie **WEI**.

To wystarczyło, żeby wywołać burzę. Bo sama nazwa mogła zapalić czerwoną lampkę w&nbsp;głowach osób śledzących tematy prywatności.  
*Integrity* w&nbsp;rozumieniu Google'a to sposób na weryfikację „zwyczajności” systemu (o&nbsp;tym później). Zaś słowo *Web* sugerowało, że chcą to przenieść do realiów sieci.

Obawy znalazły swoje potwierdzenie w&nbsp;opisie nowej funkcji. Ogólnie: **ma być czymś, co na życzenie stron internetowych sięga w&nbsp;głąb naszego urządzenia. I&nbsp;sprawdza, czy są na nim niepożądane modyfikacje**.

Oczywiście niepożądane przez firmy, nie przez nas. Wszystko ponad naszymi głowami.  
Rozgorzały dyskusje na wielu forach.

* Na Githubie (tam, gdzie wrzucono pomysł). Ta główna, nazwana po prostu [*Don't*](https://github.com/RupertBenWiser/Web-Environment-Integrity/issues/28) (w&nbsp;znaczeniu: „Nie róbcie tego”), zgromadziła ponad 800&nbsp;reakcji popierających sprzeciw autora.
* Największa [dyskusja](https://news.ycombinator.com/item?id=36876301) na forum HackerNews, o&nbsp;wprowadzaniu nowej funkcji do Chromium, zebrała ponad 800&nbsp;komentarzy.
* Jeśli doliczy się do niej [inne dyskusje na temat WEI](https://news.ycombinator.com/item?id=36910146), to zbliżymy się do 4000&nbsp;komentarzy.  
  Wniosek: sprawa *bardzo* mocno kontrowersyjna.

## Web Environment Integrity – krok po kroku

Człowiek kreatywny mógłby w&nbsp;tym momencie pomyśleć: „skoro Chrome na czyjeś życzenie zagląda w&nbsp;głąb naszego komputera/smartfona i&nbsp;stawia diagnozę... To czy nie dałoby się trochę w&nbsp;niej naściemniać? Że wszystko OK, strona może nas wpuścić?”.

Niestety to nie takie proste. Ze względu na trzy rzeczy:

1. istnienie enklaw (niedostępnych fizycznych chipów);
2. cyfrowe podpisy (sposób na zagwarantowanie, że coś pochodzi z&nbsp;konkretnego źródła);
3. weryfikację systemu na etapie uruchamiania.

Omówmy je sobie po kolei. Będzie po ludzku, ale pobieżnie. Niestety musicie mi w&nbsp;paru miejscach uwierzyć na słowo.

### Cyfrowe enklawy

Żeby zrozumieć cały problem, musimy sobie uzmysłowić jedną bardzo ważną rzecz. Może ciut nieintuicyjną. **Wiele urządzeń elektronicznych zawiera chip niedostępny dla użytkowników. Jak by się nie starali, nie uzyskają dostępu do jego zawartości**.

I nie mam tutaj na myśli, że to rzecz niedostępna dla szaraków, ale lepsi wymiatacze mogą złamać zabezpieczenia i&nbsp;podarować zwykłym ludziom *cracka*. Nie; te chipy z&nbsp;założenia mają być maksymalnie odizolowane od systemu. Jak nieprzeniknione, czarne skrzynki.

{% include info.html
type="Uwaga"
text="Pisząc o&nbsp;tych chipach, będę nazywał je *enklawami*, ponieważ to moim zdaniem trafna nazwa (sugeruje izolację, odosobnienie).  
Te niedostępne rejony naszych urządzeń mają jednak wiele nazw. *Trusted enclave* to tylko jedna z&nbsp;wielu, preferowana przez Apple.  
Ale często używa się ogólnej nazwy *TPM* (*Trusted Platform Module*). Firma ARM nazywa swój wariant TrustZone. U&nbsp;Samsunga to Knox. Komputery z&nbsp;Windowsem mają chip Pluton, w&nbsp;procesorach Intela siedzi Intel Management Engine... I&nbsp;tak dalej.  
Wiele nazw, wiele wariantów. Ale powtarza się motyw odizolowanej części systemu. Osoby głodne wiedzy mogą poszukać więcej pod hasłem `trusted computing`.
"
%}

#### Jasna strona enklaw?

Choć chipy poza kontrolą ludzi brzmią dystopijnie, można jakoś racjonalizować ich istnienie. Nawet ludzie skądinąd doświadczeni w&nbsp;sprawach cyfrowej prywatności (jak [twórca internetowy *The Hated One* oraz autor systemu GrapheneOS](https://www.youtube.com/watch?v=yTeAFoQnQPo)) wypowiadali się o&nbsp;nich pozytywnie.

Przykładem ich zastosowań są czytniki linii papilarnych w&nbsp;smartfonach. Kiedy po raz pierwszy „uczymy” urządzenia naszego odcisku palca, to musi gdzieś go sobie zapisać. Żeby potem porównywać z&nbsp;tym wzorcem palec na czytniku.

Wyobraźmy sobie, że zapisuje go do jakiegoś zwykłego folderu. A&nbsp;potem ktoś kradnie nam telefon i&nbsp;zdobywa ten plik. Niewesoła perspektywa, nieprawdaż?

{:.post-meta .bigspace-after}
W tym miejscu nieco upraszczam, bo smartfon trzymałby raczej nie obrazek, lecz zwięzłą postać, do której go „ścisnął”. Tak czy siak to dość wrażliwa rzecz.

Dlatego odcisk zostaje zapisany w&nbsp;enklawie. Nikt się do niego nie dostanie. System może tam co najwyżej wysyłać inne odciski z&nbsp;pytaniem: „czy ten zapisany wygląda tak samo?”.

Inny przykład to zabezpieczenie przed łamaniem kodów PIN.  
Ktoś mógłby podpiąć pod telefon urządzenie próbujące z&nbsp;wielką szybkością wszystkich możliwych kombinacji. `1111`, `1112`... W&nbsp;końcu by trafił.

Ale jeśli w&nbsp;enklawie umieści się jej własny, niezależny zegar, to będzie ona w&nbsp;stanie ściśle kontrolować tempo wprowadzania haseł. Po kilku nieudanych próbach -- blokada na jakiś czas. Koniec z&nbsp;łamaniem haseł na siłę.

### Gwarancja podpisana cyfrowo

Kolejnym elementem układanki jest **cyfrowy podpis**.

Choć nazywa się to „podpisem”, nie musimy od razu sobie wyobrażać pióra lub długopisu w&nbsp;czyjejś dłoni. W&nbsp;świecie komputerów chodzi ogólnie o&nbsp;*oznaczenie niemożliwe do podrobienia*. Oparte o&nbsp;kryptografię, czyli szyfry.

Analogia? Już w&nbsp;średniowieczu królowie mieli sposób na gwarantowanie autentyczności listów. Zamykano je lakiem. A&nbsp;król odciskał na tym laku swoją charakterystyczną [pieczęć](https://e-pieczatki24.pl/pytania/pieczec-lakowa/). Odbiorca znający wygląd pieczęci -- i&nbsp;widzący, że jest nienaruszona -- miał pewność, że dostał list od króla, i&nbsp;że nikt do niego nie zaglądał.

Prowizorka? Łatwo podrobić? To wprowadźmy w&nbsp;te realia współczesną technologię.  
Z jednej strony -- właściciel pieczątki jest w&nbsp;stanie ją przybijać w&nbsp;sposób doskonale powtarzalny, co do nanometrów. Z&nbsp;drugiej -- strona weryfikująca ma najmocniejsze mikroskopy i&nbsp;może z&nbsp;taką samą dokładnością weryfikować pieczęcie.

W takich warunkach mielibyśmy pewność, że korespondencja faktycznie pochodzi od króla. Jeśli do tego założymy, że tylko on ma dostęp do pieczęci, i&nbsp;że trzyma ją w&nbsp;bezpiecznym miejscu (chronionym zamku)... To wszelkie próby podrobienia listów spalą na panewce.

Wróćmy do rzeczywistości cyfrowej. Taki odpowiednik pieczęci tkwi wewnątrz enklawy. Sterujący nią program może dzięki temu podpisywać cyfrowo różne rzeczy. Ich odbiorcy będą mieli gwarancję, że dostali coś od enklawy, a&nbsp;nie podróbkę.

<img src="/assets/posts/google/web_environment_integrity/secure-enclave-schemat.jpg" alt="Schemat pokazujący enklawę jako czarną skrzynkę w&nbsp;przekroju poprzecznym. Po lewej stronie widać rurę łączącą ją z&nbsp;otoczeniem. Na ścianie wisi zegar, a&nbsp;w rogu stoi stół, na którym leżą: przedmiot przypominający odcisk palca oraz notes z&nbsp;listą. Niektóre punkty zawierają przy sobie zielone haczyki, a&nbsp;przy ostatnim stoi czerwony krzyżyk. Pośrodku stoi robot C3PO z&nbsp;klocków Lego, symbolizujący program obsługujący enklawę."/>

{:.figcaption}
Przytulne wnętrze enklawy, koloryzowane.  
Mamy tutaj: niezależny zegar, narzędzie do podpisów cyfrowych, listę kontrolną dla systemu, nasz odcisk palca, minimalną łączność ze światem. I&nbsp;program, który to wszystko obsługuje.  
Źródła obrazków pod koniec wpisu.

### Biurokratyczne uruchomienie

Wiemy już, że enklawa jest niezależna od reszty systemu. I&nbsp;że może składać swoje cyfrowe podpisy, niemożliwe do podrobienia. A&nbsp;teraz spójrzmy, do czego mogłaby je wykorzystać.

Wyobraźmy sobie, że naciskamy przycisk włączający nasz komputer. Odpływamy myślami, podczas gdy coś się wyświetla w&nbsp;rogu ekranu, zaczynają pojawiać się ikony producentów... A&nbsp;potem ekran logowania do naszego systemu.

A za kulisami? Cały łańcuszek zdarzeń. Pierwszy sygnał elektryczny *budzi* naszą płytę główną i&nbsp;wbudowany w&nbsp;nią bardzo mały program. Ten budzi kolejny, nieco większy. I&nbsp;tak dalej, aż ruszy cały nasz system.

A teraz wyobraźmy sobie, że poszczególne etapy uruchamiania są skrupulatnie, wręcz biurokratycznie kontrolowane.

Migawki ze stanu systemu trafiają do enklawy. Ta wie, jak powinien wyglądać niezmieniany system. Wypatruje anomalii. Jeśli jest OK, to daje zielone światło dla kolejnego etapu. Swoje decyzje podpisuje cyfrowo, więc żaden wirus nie da rady skłamać „Ja, enklawa, mówię że jest OK”.

W ten sposób **można zagwarantować, że uruchomiony system nie był modyfikowany, a&nbsp;po jego „rogach” nie chowają się żadne nieznane programy**. Enklawa zostawia sobie odpowiednik raportu z&nbsp;całej weryfikacji.

Po angielsku znamy ten proces jako [*trusted boot*](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/trusted-boot) (gdzie *boot* (*rozruch*) oznacza po prostu włączanie komputera).

### Łączymy to w&nbsp;całość

Mamy już wszystkie cegiełki, więc zbudujmy z&nbsp;nich nasze dzieło. *Web Environment Integrity*.

Na samym, samiuśkim początku producent urządzeń umieszcza w&nbsp;nich enklawy. Każdą wyposaża w&nbsp;narzędzie do cyfrowych podpisów. Jednocześnie udostępnia publicznie informację, jak taki podpis powinien wyglądać.

{:.post-meta .bigspace-after}
Nie jest to tajemnicą. W&nbsp;świecie cyfrowym wiedza na temat wyglądu podpisu nijak nie ułatwi jego podrobienia.

Następnie kupujemy takie urządzenie z&nbsp;enklawą i&nbsp;je uruchamiamy. A&nbsp;że mamy włączony tryb *secure boot*, to każdy etap jest dokładnie weryfikowany. Werdykt z&nbsp;weryfikacji zostaje szczelnie zamknięty w&nbsp;enklawie.

Potem zaczynamy korzystać z&nbsp;przeglądarki Chrome. I&nbsp;tu zaczynają się nadużycia.

* Istnieje strona internetowa, która chce zweryfikować, czy używamy prawilnego (w&nbsp;korpojęzyku: *appropriate*) systemu operacyjnego.
* Wysyła do Chrome'a prostą prośbę. „Sprawdź integralność systemu użytkownika X”.
* Chrome przekazuje prośbę enklawie.
* Program „zamieszkujący” enklawę robi kopię werdyktu z&nbsp;uruchomienia systemu. Oznacza go swoim cyfrowym podpisem.
* Werdykt trafia do Chrome'a, a&nbsp;ten wysyła go stronce.
* Stronka wie, jak powinien wyglądać cyfrowy podpis enklawy. Weryfikuje jego autentyczność. Następnie na podstawie werdyktu wpuszcza nas albo odrzuca.

Możemy kombinować, ale nic nie zdziałamy. Jeśli celowo „zgubimy” werdykt enklawy, to strona pewnie nas nie wpuści. Nie damy rady go podrobić, bo jest cyfrowo podpisany. Jesteśmy w&nbsp;pułapce.

Ogólną koncepcję -- ktoś z&nbsp;zewnątrz pyta naszej enklawy o&nbsp;stan systemu -- określa się mianem **zdalnej atestacji** (ang. *remote attestation*).

Wobec enklaw mam nieco sympatii. Wobec *secure boota* nieco mniej. A&nbsp;zdalna atestacja? Budzi we mnie prawie wyłącznie obawy.  
Też ma ponoć zastosowania bliższe użytkownikom... Ale nadal jest jak wywiad środowiskowy. Potajemne pytanie sąsiadów, czy jesteśmy grzecznymi obywatelami.

## Dlaczego inni nie oleją Google'a?

Wiemy już, na czym polega *Web Environment Integrity*. Wiemy, że go nie przechytrzymy. Ani sami, ani korzystając z&nbsp;programów od mądrych informatycznych głów.

To może w&nbsp;takim razie zostawić Chrome'a z&nbsp;jego fanaberiami? I&nbsp;trzymać się przeglądarek będących po naszej stronie?

Autorzy przeglądarki Vivaldi [ocenili WEI negatywnie](https://vivaldi.com/blog/googles-new-dangerous-web-environment-integrity-spec/). W&nbsp;artykule z&nbsp;25 lipca piszą, że to zagrożenie dla otwartej sieci.  
Również reprezentant Mozilli od Firefoksa [wyraził oficjalny sprzeciw](https://github.com/mozilla/standards-positions/issues/852#issuecomment-1648820747), wymieniając przy okazji przydatne narzędzia, które mogłyby upaść przez WEI.

**Aktualizacja:** 6 sierpnia również autorzy przeglądarki Brave [oficjalnie zapowiedzieli, że nie wesprą WEI](https://brave.com/web-standards-at-brave/9-web-environment-integrity/). Przy okazji wymieniają kilka innych przykładów psucia internetu przez Google'a.

### Zależność od Chromium

Problem w&nbsp;tym, że inne przeglądarki często są zależne od kodu Chromium, tworzonego przez Google'a. A&nbsp;nawet jeśli mają własny, niezależny silnik (jak Firefox), to wciąż są pod presją.

Tę sprawę opisałem nieco obszerniej przy okazji innej kontrowersyjnej funkcji, jaką chciał wprowadzić Google, znacząco osłabiając dodatki do przeglądarek. Pozwolę sobie skopiować stamtąd [schemat zależności między przeglądarkami]({% post_url 2022-05-11-google-manifest-v3 %}#problem-dominacji-chromea){:.internal}.

<img src="/assets/posts/google/chrome/browser-landscape.jpg" alt="Schemat pokazujący zależności między przeglądarkami trzech firm - Google, Apple i&nbsp;Mozilli. Widać, że na przeglądarce Chromium opiera się najwięcej dużych przeglądarek. Firefox od Mozilli oraz Safari od Apple są mniej popularne jako źródło kodu."/>

U góry mamy firmy -- Mozillę, Apple i&nbsp;Google. Linijkę niżej ich podstawowy produkt. W&nbsp;przypadku Google'a jest nim Chromium -- taki fundament, na którym opiera się ich własny Chrome.  
Ale nie tylko, bo korzysta z&nbsp;niego wiele innych przeglądarek. Opera, Vivaldi, Edge od Microsoftu...

Ci wszyscy twórcy mogliby próbować wyłuskiwać z&nbsp;Chromium tylko wybrane rzeczy (jak łatki bezpieczeństwa, poprawki do szybkości działania). I&nbsp;wyrzucać kontrowersyjne, jak nasze WEI.

Ale z&nbsp;czasem ich przeglądarka coraz bardziej by odjeżdżała od Chromium. Google może dodawać nowe funkcje, oparte na starych. Jeśli jakaś nowinka opiera się na WEI, a&nbsp;oni go nie mają... To musieliby tę nowinkę napisać od nowa. A&nbsp;mieli przecież „płynąć z&nbsp;nurtem Chromium”, a&nbsp;nie pod prąd. 

Pozostała dwójka -- Firefox od Mozilli oraz Safari od Apple -- ma własne silniki, więc jest nieco mniej uwiązana. Ale na nich mogą z&nbsp;kolei naciskać użytkownicy.

> Strona banku mi u&nbsp;was nie działa. Że co, wymaga jakiejś atestacji? To ją dodajcie, chcę żeby działało.

### Sprawa Apple'a

Poza tym mam jeszcze jedną niewesołą wiadomość. Choć to Google zwrócił na siebie największą uwagę, pewna osoba nagłośniła fakt, że [Apple wprowadziło wcześniej bardzo podobny system](https://httptoolkit.com/blog/apple-private-access-tokens-attestation/), zwany *Private Access Token* (tutaj [dyskusja](https://news.ycombinator.com/item?id=36862494)).

Strony takie jak Cloudflare czy Fastly (w&nbsp;praktyce -- pośrednicy między nami a&nbsp;wieloma stronami większych firm) mogą sobie zażyczyć dowodu autentyczności od przeglądarki Safari na systemach Apple. Ta przekazuje prośbę systemowi, a&nbsp;system dostarcza dowodu swojej „prawilności”.

O tej sprawie nie było tak głośno. Być może dlatego, że przedstawiano to jako bonus. Możliwość ominięcia wkurzającej, ręcznej weryfikacji typu Captcha. Wejście poza kolejką, trochę jak *priority boarding* w&nbsp;liniach lotniczych. Tyle że za darmo, dopóki mamy urządzenie od Apple wspierające atestację.

WEI budzi większe kontrowersje, bo jest ogólniejsze i&nbsp;nawet nie ukrywa, że ma na celu ograniczanie, a&nbsp;nie wejście poza kolejką. Co nie zmienia faktu, że **Apple też okazał się otwarty na ideę atestacji**. Bardzo możliwe, że nie będzie sojusznikiem otwartego internetu w&nbsp;tym sporze.

## Realne zagrożenie

Ktoś mógłby stwierdzić, że nowa propozycja Google'a to nic nowego, więc afera jest rozdmuchana.

1. Już wcześniej istniały rozwiązania DRM dla treści multimedialnych.

   Po ludzku: kiedy oglądaliśmy przez internet jakiś film, to nasz własny system (w&nbsp;tym m.in. przeglądarka, procesor) zamykał się przed nami, żebyśmy nie mieli opcji skopiowania oglądanych pikseli.

2. Już wcześniej istniały metody wykrywania i&nbsp;blokowania automatów.

   Chociażby złożone zabezpieczenia na Reddicie, kupione od firmy HUMAN. Wykonujące na naszej przeglądarce [szereg testów](https://smitop.com/post/whiteops-data/), z&nbsp;których niektóre ocierały się o&nbsp;hakerstwo.

3. Już wcześniej istniała zdalna atestacja, tyle że dla aplikacji mobilnych.

   Google już wcześniej pozwalał aplikacjom smartfonowym sprawdzić, czy nasz system nie był zmieniany. Nazywali to na początku SafetyNet. Potem zmienili na Play Integrity API.

   {:.post-meta .bigspace-after}
   Wnikliwi mogą zwrócić uwagę na słowo *Integrity*. Google bardzo lubi je traktować jak synonim dla „filtr odsiewający niepokornych obywateli”.

   Miałem już okazję [krytykować SafetyNeta]({% post_url 2021-10-30-google-skandale-wprowadzenie %}#android-system-operacyjny){:.internal} na blogu. Korzystały z&nbsp;tego niektóre gry, aplikacje bankowe, a&nbsp;nawet... apka sieci McDonald's.

Co do zdalnej atestacji -- oczywiście, była ograniczeniem i&nbsp;utrapieniem dla alternatywnych systemów smartfonowych, jak LineageOS.  
Ale, po pierwsze, nie wychodziła poza sprawdzanie samego systemu. Nie oceniała nam aplikacji. A&nbsp;sposób, w jaki Google prezentuje WEI, sugeruje możliwość oceniania przeglądarki. A&nbsp;nawet jej dodatków.

Po drugie: jeśli jakaś apka nie pozwalała z&nbsp;siebie korzystać, to często mogliśmy wejść na odpowiadającą jej stronę internetową. Wiele firm udostępniało taki wariant. A&nbsp;tam, z racji używania ogólnej przeglądarki, mieliśmy nieco więcej kontroli.

A DRM? Jasne, odbiera wolność. Ale jest stosunkowo rzadki. Odnosi się tylko do multimediów i&nbsp;do niektórych stron. Głównie dużych platform, takich jak Netflix.

WEI uderza w&nbsp;to, co dotąd było wolne -- zwykłe, niefilmowe strony internetowe oglądane przez przeglądarkę. Nasz ostatni bastion.  
**Dzięki niemu każdy zakątek internetu mógłby łatwo wprowadzić filtry wymuszające mainstreamowość**. Dotyczy to zarówno urządzeń mobilnych, jak i&nbsp;komputerów. I&nbsp;to uważam za najbardziej alarmujący fakt.

### Niepokojąca łatwość blokowania

Samo istnienie nowej możliwości będzie rodziło patologiczne pokusy.  
Wyobraźmy sobie jakąś naradę, *meeting* w&nbsp;korporacji. W&nbsp;takich miejscach nieraz pojawiają się głupie pomysły.

Pojawia się problem! Użytkownicy omijają nachalną reklamę, używając popularnego dodatku do przeglądarki. Menedżer widzi te niechlubne dane. Ale zamiast dostrzec problem po swojej stronie, próbuje go zakleić łatką.  
Pyta kogoś z&nbsp;działu informatycznego: „Czy da się sprawić, żeby *musieli* to obejrzeć?”.

Dawniej odpowiedź brzmiałaby „nie”. Albo „to skomplikowane”. Jasne, istniały systemy od *blokowania blokerów reklam* albo wykrywania automatów. Ale ich metody były inwazyjne i&nbsp;niedokładne. Jeśli ktoś na porządnie się brał za ich obejście, to zwykle się to udawało.

A teraz? Osoba z&nbsp;działu informatycznego musiałaby niechętnie przyznać, że Chrome pozwala wymusić kontrolę paroma linijkami kodu. A&nbsp;zadowolony menedżer każe wtedy dodać WEI do strony. Nie patrząc na efekty uboczne.

Ta łatwość izolowania stron może szybko i&nbsp;radykalnie zmienić obraz internetu.

### Kwestia etyczna

Za każdym razem, kiedy odwiedzamy strony internetowe, nasza przeglądarka wysyła im trochę informacji. W&nbsp;tym swoistą wizytówkę, w&nbsp;której podaje swoją nazwę i&nbsp;numer wersji. Ta informacja nosi nazwę `User Agent`.  
Ale nie każdy wie, że *user agent* to również oficjalne pojęcie, ułożone wiele lat temu. I&nbsp;oznaczające *po prostu samą przeglądarkę*.

Dosłownie to „agent użytkownika”. Ale nie chodzi o&nbsp;„agenta” w&nbsp;znaczeniu szpiegowskim. Chodzi o&nbsp;sens ogólniejszy -- pośrednika, wykonawcę czyjejś woli. Kogoś, kto działa w&nbsp;cudzym interesie.

Zatem **pierwsze przeglądarki w&nbsp;samej swojej nazwie miały obietnicę. Miały działać w&nbsp;naszym interesie**. Miały być dla nas! Pozwalać nam oglądać internet, ale zostawiać nam kontrolę i&nbsp;ostatnie słowo.

Jak tu oceniać działania Google'a oraz ich inicjatywy osłabiające użytkowników? DRM-y, usuwanie z&nbsp;przeglądarki niektórych opcji... A&nbsp;teraz WEI, czyli przeglądarka-donosiciel.

Pod względem etycznym działania Google'a są sprzeczne z&nbsp;samą ideą przeglądarek. Ale co się dziwić? Kiedyś szczycili się sloganem *Don't be evil*. Potem od niego odeszli.

### Wiarygodny scenariusz

Wyobraźmy sobie sytuację, która ma dużą szansę się wydarzyć.

Ktoś stworzył alternatywny system operacyjny. Fajny, uwzględniający potrzeby użytkowników. Może na przykład coś na bazie Linuksa? Dajmy na to -- KumpeLinux (nazwa zmyślona).

Po dłuższych bojach namówiliśmy znajomą osobę, żeby z&nbsp;tego systemu korzystała. Niepełny sukces, bo wciąż korzysta z&nbsp;Chrome'a i&nbsp;kompletu usług Google'a. Ale zawsze coś. Nawet słyszymy pierwsze pozytywne wrażenia.

Tylko że wchodzi Web Environment Integrity. W&nbsp;dużym banku odbywa się *meeting*. Bank chce mieć dupochron i&nbsp;móc w&nbsp;razie czego stwierdzić „to nie nasza wina, że ci zwinęli pieniądze z&nbsp;konta!”.  
W efekcie wprowadzają WEI na swojej stronie. Jeśli ktoś używa Chrome'a, to zapyta go o&nbsp;system operacyjny. Jeśli ten nie należy do popularniejszych (jak Windows, MacOS, bardziej znane Linuksy), to wyświetli się groźny komunikat:

> Uwaga, wykryto zmodyfikowane urządzenie!  
Może ono zawierać złośliwe oprogramowanie wykradające dane. Upewnij się, że korzystasz z&nbsp;bezpiecznego systemu (jak Microsoft Windows albo MacOS).

Wszystko to sygnowane logiem banku i&nbsp;w oficjalnym oknie Chrome'a. Znajoma osoba informuje nas, że rzuca w&nbsp;diabły ten cały KumpeLinux, bo „bank powiedział, że to jakiś wirus jest”.

Takich głosów pojawia się więcej. Ostatecznie autor KumpeLinuksa ma dość użerania się z&nbsp;fałszywymi oskarżeniami. Porzuca projekt, a&nbsp;świat *open source* na tym traci.  
Żadna niszowa alternatywa dla wielkich, znanych systemów już się nie przebije. Nie będzie konkurencji.

## Jak z&nbsp;tym walczyć

Ci, którzy dostrzegają zagrożenia związane z&nbsp;WEI, mogą potraktować go jak sygnał odstraszający. I&nbsp;trzymać się tych stron, gdzie go nie ma. Taka na przykład Ciemna Strona nigdy nie odrzuci nietypowych przeglądarek. Każdy jest tu mile widziany :wink:

Ale co, jeśli nie chcemy ciągle dawać się spychać do zakamarków sieci? Jeśli chcemy zdrowego, otwartego internetu? W&nbsp;tym wypadku pozostają nam naciski na Google'a. Protesty oraz przekonywanie znajomych.

Można też uderzyć do instytucji europejskich. Podawać WEI jako przykład działań monopolistycznych (użycie dominacji w&nbsp;segmencie przeglądarek do sztucznego blokowania nowych, konkurencyjnych systemów). Nastraszyć Google'a przymusowym podziałem firmy.

### Zrozumiałe argumenty

Problem w&nbsp;tym, że cała kwestia jest dość złożona i&nbsp;abstrakcyjna. Ukryte chipy, cyfrowe podpisy, atestacje, jednorożce? Wiele osób bagatelizuje nawet konkretne zagrożenia dla prywatności, a&nbsp;zwłaszcza coś tak rozmytego.

Jeśli chcemy trafić do ludzi spoza światka komputerowego, to bardzo ważny jest sposób, w&nbsp;jaki przekażemy obawy. Konkrety, bez żargonu. Technikalia *wyłącznie* na życzenie rozmówców. I&nbsp;najlepiej wychodzić od rzeczy im bliższych.

Ktoś obawia się władzy autorytarnej? Warto ugryźć temat od tej strony. „A wiesz, że do przeglądarki Chrome już dodali pierwsze fundamenty pod cyfrową tożsamość?”.

{:.post-meta .bigspace-after}
Jest to pewna nadinterpretacja, bo WEI nie jest wprost z&nbsp;tym związany; ale to prawie pewne, że kontrola dostępu do internetu obejmowałaby *jakąś* formę atestacji.

Ktoś wyczulony na nierówności społeczne? „Przez Google'a i&nbsp;ich nową funkcję strony mogą wpuszczać tylko nowsze urządzenia. Będą wykluczać osoby, których na to nie stać”.  
Można też powiedzieć, że „blokują niestandardowe rzeczy. Jest spora szansa, że przestaną działać narzędzia ułatwiające niewidomym korzystanie z&nbsp;internetu”.

Ktoś nie lubi inwazyjnych reklam? Podkreślamy ten wątek. „Google ułatwi stronom odrzucanie każdego urządzenia, które może blokować reklamy. I&nbsp;w taki sposób, że się tego nie ominie”.

Mam jeszcze jeden pomysł -- można pokazać, że walka z&nbsp;automatyzacją zabije wiele niezależnych, pożytecznych inicjatyw. Jak wyłapywanie rosyjskich trolli.

Bo widzicie... Internet zwiedza wielu zbieraczy danych. Analityków, badaczy i&nbsp;hobbystów.  
Chcąc odkrywać afery, muszą odwiedzać wiele stron. Zbyt wiele do ręcznego przejrzenia, więc automatyzują ich gromadzenie. Co osiągnęli do tej pory?

* Pewien użytkownik zgromadził [wielką kompilację kont]({% post_url 2022-04-15-trolle-rosja-ukraina %}#znajdowanie-trolli){:.internal} działających na Twitterze w&nbsp;sposób sztuczny i&nbsp;nienaturalny. W&nbsp;tym rosyjskich trolli.
* Inna osoba użyła automatycznych metod, żeby wyszukać całą [sieć niepokojących filmów]({% post_url 2022-02-20-youtube-viacom-elsagate%}#interpretacja){:.internal} kierowanych do dzieci.
* Pewni badacze wobec niemrawości Facebooka wzięli sprawy w&nbsp;swoje ręce i&nbsp;zaczęli [zbierać dane na temat politycznych manipulacji]({% post_url 2022-04-15-trolle-rosja-ukraina %}#kapryśne-mocarstwa--facebook-itwitter){:.internal}. Za co Fejsik zastraszył ich pozwem.

Podsumowując: automaty pozwoliły niezależnym osobom uzyskać informacje cenne dla społeczeństwa. Obejść wielkie platformy niechętne do współpracy.

A teraz **Google staje po stronie platform, dając im łatwe blokowanie automatów. W&nbsp;takich realiach wspomniane pożyteczne inicjatywy mogłyby nigdy nie powstać**. Bariera byłaby za wysoka dla hobbystów, a&nbsp;duzi gracze nadal umywaliby ręce.

Tym przykładem zakończę wpis. WEI byłoby zmianą na gorsze. Uderzy w&nbsp;wiele aspektów internetu, nieraz w&nbsp;sposób nieprzewidywalny. Dlatego -- nawet jeśli czujemy znużenie gierkami Google'a -- jeszcze raz stawmy opór.

Bądźmy kreatywni w&nbsp;walce z&nbsp;nowym zagrożeniem. Życzę nam powodzenia! :smile:

## Źródło obrazków

Schemat enklawy:

* [Odcisk palca](https://www.flaticon.com/free-icon/fingerprint_5004424) -- Talha Dogar, serwis Flaticon.
* [Lista kontrolna](https://www.flaticon.com/free-icon/check-list_1721929) -- Freepik, serwis Flaticon.
* [Zegar naścienny](https://www.flaticon.com/free-icon/clock_2784459) -- Freepik, serwis Flaticon.
* C3PO w&nbsp;wersji Lego.
