---
layout: post
title:  "Internetowa inwigilacja 5 – User Agent"
subtitle: "„Kim jesteś?”"
date:   2021-06-11 01:13:00 +0100
tags: [Internet, Inwigilacja, Porady]
firmy: [Facebook, Google, Microsoft, Reddit]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: "user-agent/user-agent-baner.jpg"
image-width: 1600
image-height: 900
---

Zdarzyło Wam się, że jakaś strona rozpoznała Wasze urządzenie? Albo nawet utrudniła Wam życie, bo coś jej w&nbsp;nim nie pasowało?

{:.bigspace}
<img src="/assets/posts/user-agent/user-agent-kolaz.webp" alt="Kolaż pokazujący cztery komunikaty informujące, że nie rozpoznano naszego urządzenia."/>

Skąd odwiedzane strony wiedzą, jakiego używamy urządzenia? Dzięki tzw. *user agentowi*, czyli identyfikatorowi użytkownika.  
To **ciąg znaków mówiący o&nbsp;tym, jakiej używacie przeglądarki i&nbsp;systemu operacyjnego**.

Czasem się to przydaje. Pozwala na przykład dobrać wysyłaną nam stronkę do możliwości urządzenia.

Ale oczywiście *user agent*, zdradzając coś o&nbsp;nas, ma też ciemne strony.  
Po pierwsze, jest dodatkowym punktem danych pozwalającym nas identyfikować.  
Po drugie, **pozwala stronom manipulować ludźmi przez zniechęcanie do niektórych przeglądarek**. Nawet jeśli wszystko by w&nbsp;nich normalnie działało.

W tym wpisie krótko omówię *user agenta*, sposoby w&nbsp;jakie jest nadużywany i&nbsp;metody pozwalające go zamaskować.

## Czym jest *user agent*

Krótko: to tekst mówiący coś o&nbsp;naszej przeglądarce i&nbsp;systemie operacyjnym.

A dokładniej: To jedna z&nbsp;informacji zawartych w&nbsp;nagłówkach HTTP, które opisałem dokładniej w&nbsp;[pierwszym wpisie z&nbsp;serii]({% post_url 2021-01-11-internetowa-inwigilacja-1-podstawy %}).  
To część naszej „etykiety” lub „wizytówki”, którą przeglądarka wysyła wszystkim odwiedzanym przez nas stronom.

*User agent* nie ma odgórnie narzuconej postaci, teoretycznie może być dowolnym tekstem.  
W praktyce powinien zawierać nazwę i&nbsp;wersję przeglądarki oraz systemu operacyjnego.

Twój wygląda tak:

{:.bigspace .black-bg .mono}
<div><strong id="user-agent">Masz wyłączony JavaScript!</strong></div>

Jeśli używasz mainstreamowej przeglądarki, zapewne gdzieś w&nbsp;tekście zauważysz jej nazwę oraz nazwę swojego systemu operacyjnego.

Jest tam też trochę innych bzdetów, które mogą Ci nic nie mówić. Albo nawet kojarzyć się z&nbsp;całkiem innymi przeglądarkami.

Spójrzmy na inny przykład. Jeśli użyję swojej przeglądarki Chromium, mój *user agent* wygląda tak:

<div class="black-bg mono">Mozilla/5.0 (X11; <span class="red">Linux x86_64</span>) AppleWebKit/537.36 (KHTML, like Gecko) <span class="red">Chrome/89.0.4389.90</span> Safari/537.36</div>

{:.figcaption}
*User agent* dla względnie nowego Chromium. Kolorowe oznaczenia dodane przeze mnie.

Widać po nim, że:

* używam 64-bitowego systemu Linux (`Linux x86_64`)
* ...i Chrome'a w&nbsp;wersji 89 (`Chrome/89.0.4389.90`)

Ale co tu robią pozostałe rzeczy?

* `Mozilla` to firma, której własnością jest przeglądarka Firefox. A&nbsp;ja przecież używam Chromium.
* `Safari` z&nbsp;kolei to przeglądarka firmy Apple. A&nbsp;`AppleWebKit` to jej silnik. Nie używam ani jednego, ani drugiego.

Okazuje się, że te wszystkie dodatkowe bzdety są tu dla kompatybilności. Żeby programy patrzące na *UA*, nie rozpoznając niektórych nazw, znalazły przynajmniej cokolwiek znajomego.

{% include info.html type="Ciekawostka" text="
Takie podszywanie się pod inne *user agenty* ma [długą historię](https://humanwhocodes.com/blog/2010/01/12/history-of-the-user-agent-string/) i&nbsp;sięga tak zwanych *wojen przeglądarkowych*."
trailer="
<p>Rozpoczętych, gdy Internet Explorer od Microsoftu dopiero raczkował, a&nbsp;do przeglądania internetu używano głównie Netscape Navigatora.</p>
<p>Żeby napompować sobie popularność, IE podszywał się pod Netscape'a, żeby bez problemu działały na nim wszystkie strony. Kolejne przeglądarki też podszywały się pod dobrze zakorzenionych poprzedników, a&nbsp;przeciętny <i>user agent</i> był coraz dłuższy. Aż dotarliśmy do współczesności.</p>
<p>Subciekawostka: firma odpowiedzialna za Netscape Navigatora to późniejsza Mozilla – twórcy Firefoksa! Co więcej, sama nazwa Mozilla też ma wojenne korzenie.</p>
<p>Na początku był to kryptonim Netscape'a i&nbsp;zarazem skrót od <i>Mosaic killer</i>.<br/>Czemu <i>killer</i>? Bo planowali zdetronizować („zabić”) jeszcze wcześniejszą przeglądarkę, Mosaic.</p>
"%}

## Zastosowania

Najpierw jasne strony, zanim przejdę do ciemnych. Do czego przydają się informacje z&nbsp;*user agenta*?

Mogą na przykład ułatwić nam życie na stronkach z&nbsp;programami do pobrania. Stronka **sama podsuwa nam instalator pasujący do naszego systemu operacyjnego**.  
Przykładem jest [oficjalna strona języka Python](https://www.python.org/), którą już linkowałem przy różnych okazjach.

*User agent* może być również **stosowany jako dodatkowe zabezpieczenie**.

Jeśli ktoś zdobędzie hasło do jakiegoś naszego konta, to jest spora szansa, że wtargnie na nie z&nbsp;własnego komputera i&nbsp;przeglądarki, innych niż nasze.  
Strona może porównać to logowanie z&nbsp;naszymi poprzednimi i&nbsp;uznać je za podejrzane (np. zawsze używamy Linuksa + Firefoxa, a&nbsp;tu nagle zestaw Windows + Edge!).
 
To zabezpieczenie lekko trąci Wielkim Bratem, ale nie jestem jakimś jego przeciwnikiem.

Skoro strony i&nbsp;tak zbierają te informacje (bo, przypominam, wysyłamy je w&nbsp;nagłówkach HTTP przy każdym kontakcie), to przynajmniej niech raz w&nbsp;życiu użyją ich w&nbsp;naszym interesie.

Poza tym komunikaty o&nbsp;podejrzanych logowaniach są jawne. Użytkownicy mogą dzięki temu zobaczyć przebłyski tego, co wiedzą o&nbsp;nich duże firmy. Może się zaskoczą i&nbsp;kiedyś ich to zmotywuje do ochrony prywatności?

# Przykład zabezpieczenia

Jeśli chcecie zobaczyć przykład (i macie Facebooka), to możecie wejść na [facebook.com](https://www.facebook.com) i&nbsp;potem w&nbsp;zakładkę `Ustawienia > Bezpieczeństwo`.

Możecie też przejść tam bezpośrednio, wklejając do paska link:

```
https://www.facebook.com/settings?tab=security
```

Pod nagłówkiem „Miejsce logowania” znajdziemy listę urządzeń i&nbsp;miejsc, z&nbsp;których się logowaliśmy.

Przybliżone lokalizacje (na poziomie miasta; czasem niedokładne) są związane z&nbsp;adresem IP. Będzie o&nbsp;nim w&nbsp;przyszłym wpisie, na razie to pomińmy.

Pozostałe dwie informacje, czyli system i&nbsp;przeglądarka, zostały odczytane właśnie z&nbsp;*user agenta*. Facebook zbiera je i&nbsp;daje znać, jeśli przy którymś logowaniu pojawi się coś nowego.

Ale akurat FB nie jest kryształowy w&nbsp;kwestii *user agenta*. Używa go również do sztucznego ograniczania ruchu, co pokażę poniżej.

## Ciemna strona User Agenta

Możliwość rozpoznawania urządzeń i&nbsp;systemów rodzi czasem negatywne pokusy.

Można łatwo umieścić na serwerze regułkę „dyskryminującą” -- wysyłającą różne strony w&nbsp;zależności od tego, jakie urządzenie o&nbsp;nie poprosiło.

Świat jest pełen dziwów.  
Dlatego gdzieś pewnie istnieje strona wyświetlająca „Tylko dla Chromiarzy” wszystkim przeglądarkom niebędącym Chrome'em.  
Albo „Strefa Apple, biedacy niemili widziani” osobom spoza jabłkowego ekosystemu.

Ale to powyższe tak z&nbsp;przymrużeniem oka. Spójrzmy na całkiem realne przykłady, kiedy *user agenta* używało się do sztucznego dzielenia użytkowników na grupy.

# Microsoft

Ten przykład jest stary, ale dobrze pokazuje samo zjawisko. Mógłby wydarzyć się i&nbsp;dziś.

Kiedyś Microsoft był synonimem pazernego korpo i&nbsp;grał bardzo ostro. Przykład jego wybryku znajdziemy nawet w&nbsp;informacyjnym artykule o&nbsp;*user agencie* z&nbsp;Wikipedii:

>  Aby uzyskać dostęp do pełnej wersji gry [Cut the Rope], należało użyć przeglądarki Internet Explorer 9, a&nbsp;dla użytkowników starszych systemów (...) również zakupić nowszy system operacyjny.  
(...)  
każda z&nbsp;\[konkurencyjnych przeglądarek\] była bardziej kompatybilna od IE9.  
(...)  
Sprawdzanie przeglądarki polegało na UAString (...). Po zmianie UAString użytkownicy mogli skorzystać z&nbsp;gry bez używania przeglądarki Internet Explorer.

{:.figcaption}
Źródło: [Wikipedia](https://pl.wikipedia.org/wiki/User_agent) (skróty i&nbsp;wtrącenia moje).

Gdyby Internet Explorer walczył na gruncie technicznym, to by zajął ostatnie miejsce.  
Dlatego patrzyli na *user agenta* i&nbsp;faworyzowali swoją przeglądarkę. Stworzyli sztuczną barierę, żeby ośmieszyć konkurencję.

# Google

Przykład nieco bardziej współczesny?

Microsoft został zdetronizowany przez Google'a.  
I to nie tylko pod względem dominacji na rynku głównego nurtu. Jak się okazało, kolorowe G&nbsp;podpatrzyło też sztuczki dawnego monopolisty.

Znalazłem na YT fajny [filmik](https://www.youtube.com/watch?v=ELCq63652ig) pokazujący, jak Google stopniowo budował dominację Chrome'a wśród przeglądarek. Wykorzystał do tego inne swoje produkty, takie jak Dysk, Arkusze i&nbsp;podobne usługi.

Autor filmiku wskazuje, że usługi Google'a nieraz bardzo słabo działały na innych przeglądarkach niż Chrome. W&nbsp;tym na Edge'u oferowanym przez Microsoft. **Mimo że Edge już wtedy korzystał z&nbsp;tego samego silnika co Chrome**.

Jeśli w&nbsp;Edge'u zmieniło się *user agenta* i&nbsp;ponownie odwiedziło strony, to problem w&nbsp;magiczny sposób znikał. Wniosek? To nigdy nie był realny problem, tylko sztuczne ograniczenie. Ośmieszanie rywali.

# Facebook

Facebook to kolos, ale nie ma własnej przeglądarki. Nie ma więc powodu, żeby faworyzować którąkolwiek z&nbsp;nich.  
Tym niemniej też używa *user agenta* wbrew naszym interesom. **Przeganiając użytkowników telefonów komórkowych ze stronki na aplikację**.

Nie każdy wie, że Messenger ma również osobną stronkę, *[messenger.com](https://www.messenger.com)*. Jeśli klikniecie w&nbsp;ten link i&nbsp;korzystacie z&nbsp;komputera, to wyświetli Wam się duża wersja Messengera.

A co, jeśli chcemy odwiedzić tę stronę przez urządzenie mobilne?

Wtedy naszym oczom ukazują się zupełnie różne rzeczy, niż gdybyśmy wchodzili przez komputer:

<img src="/assets/posts/user-agent/messenger-login-porownanie.webp" alt="Porównanie głównego ekranu strony messenger.com na komputerze i&nbsp;na telefonie. Widać, że wersja komputerowa ma pola na login i&nbsp;hasło, a&nbsp;wersja mobilna jedynie przycisk odsyłający do sklepu Google Play."/>

{:.figcaption}
Takie ekrany się nam pokazują, jeśli nie jesteśmy zalogowani i&nbsp;wejdziemy na stronę Messengera.  
Po lewej wersja na komputerze, po prawej mobilna.

Bolą mnie te wiszące spójniki.

Ale jeszcze bardziej boli to, że w&nbsp;wersji mobilnej (po prawej stronie) w&nbsp;ogóle nie ma opcji zalogowania się. Jest tylko link do Play Store'a. **Nie otworzymy Messengera przez przeglądarkę, trzeba pobrać aplikację**.

Dlaczego Facebook nas do tego zmusza? Oficjalna wersja pewnie byłaby taka, że aplikacja „jest zoptymalizowana” pod urządzenia mobilne.  
Ale to średnia wymówka. Współczesne strony internetowe potrafią bardzo wiele, a&nbsp;FB ma armię programistów. Gdyby chciał stworzyć Messengera w&nbsp;formie strony mobilnej, to by to zrobił.

Możliwe, że chodzi o&nbsp;coś innego.  
Gdy używamy przeglądarki, strony internetowe są ściśle ograniczone i&nbsp;raczej mało mogą nam zrobić (pomijając różne myki opisane w&nbsp;„Internetowej inwigilacji” :wink:).

A aplikacje? Te są dużo bardziej zżyte z&nbsp;systemem. Jeśli im pozwolimy, to mogą czytać nasze kontakty, zerkać na GPS-a, przeszukiwać pliki...

Niedawno Apple wprowadziło na systemie iOS (czyli Jabłkofonach) dość przejrzyste informacje o&nbsp;tym, czego chcą aplikacje.  
Porównajmy uprawnienia domyślnej [przeglądarki Safari](https://www.apple.com/privacy/labels/) z&nbsp;uprawnieniami Messengera na tym samym systemie:

{:.bigspace}
<img src="/assets/posts/user-agent/messenger-privacy-labels.webp" alt="Dwa zrzuty ekranu ułożone jeden nad drugim. Pierwszy pokazuje uprawnienia, o&nbsp;które prosi Safari. Są jedynie trzy. Drugi zrzut jest dużo większy i&nbsp;wskazuje kilkadziesiąt uprawnień, o&nbsp;które prosi Messenger."/>

Widać różnicę?

Wniosek: Kiedy używamy urządzeń mobilnych, Facebook świadomie i&nbsp;aktywnie zagania nas do aplikacji. Aplikacja prosi o&nbsp;wiele pozwoleń i&nbsp;może zbierać więcej danych niż strona.  
Czy jest w&nbsp;tym jakiś związek? Oceńcie sami.

# Reddit

Reddit to bardzo popularne forum dyskusyjne, dające użytkownikom możliwość zakładania własnych podgrup i&nbsp;dużą swobodę w&nbsp;wyborze ich wyglądu.

Podobnie jak Facebook ze swoim Messengerem, mocno starają się zagonić użytkowników do swojej mobilnej aplikacji.

Często widuję opinie, że korzystanie z&nbsp;ich strony na urządzeniach mobilnych celowo jest nieprzyjemne. Powolne, nieintuicyjne... A&nbsp;jednocześnie cały czas towarzyszy nam baner zachęcający do przejścia na aplikację mobilną.

{:.figure .bigspace}
<img src="/assets/posts/user-agent/reddit-app.webp" alt="Komunikat z&nbsp;Reddita zachęcający do korzystania z&nbsp;niego przez aplikację mobilną." width="400px"/>

## Jak zmienić *user agenta*?

Przykłady pokazują, że wszystko co powie nasz agent może zostać użyte przeciw nam.

W związku z&nbsp;tym może nam zależeć na jego podrobieniu. Szczególnie w&nbsp;dwóch przypadkach:

1. Strona nas blokuje ze względu na naszą przeglądarkę  
   (na przykład nie wyświetla się na urządzeniu mobilym);
2. Nie chcemy zdradzać o sobie informacji.

Zanim cokolwiek zrobimy, krótkie ostrzeżenie -- **zbyt brawurowa zmiana *user agenta* może nawet osłabić naszą prywatność**.

Przez „zbyt brawurową” rozumiem tutaj dwie rzeczy:

* wymyślenie całkiem fikcyjnego ciągu znaków  
  (np. ustawienie `xyz` jako naszego UA; wtedy wręcz wyróżniamy się z&nbsp;tłumu);
* przedstawienie się jako przeglądarka z&nbsp;zupełnie innej rodziny  
  (jeśli np. używamy Firefoksa, ale wysyłamy takiego UA jak Chrome).

Dlaczego to drugie może szkodzić?  
Dlatego, że strony czasem zawierają kod rozpoznający przeglądarkę na podstawie jej właściwości. Więcej będzie o&nbsp;tym we wpisie o&nbsp;JavaScripcie.

Wyobraźmy sobie, że przedstawiamy się jako Chrome. A&nbsp;kod na stronie wykonuje testy i&nbsp;wychodzi mu, że jesteśmy Firefoksem.  
W ten sposób poznali naszą prawdziwą przeglądarkę. Do tego widzą, że próbowaliśmy ich nabrać, maskując *user agenta* (co może być bardziej wrażliwą informacją niż on sam).

# Najprostsze rozwiązanie

Skoro już mamy świadomość zagrożeń, to przejdźmy do rzeczy. 

Najprościej po prostu **zainstalować kilka różnych przeglądarek** i&nbsp;używać ich odpowiednio do naszych potrzeb.

W tych sprawach ilu ludzi, tyle opinii, dlatego niczego nie narzucam.  
Ale zachęcam, żeby mieć przynajmniej jedną przeglądarkę prywatną i&nbsp;jedną mainstreamową. Na każdej zainstalowany dodatek uBlock Origin.

Za pierwszą z nich, tą od prywatności, można przyjąć np. Firefoksa.  
Za drugą, mainstreamową, coś domyślnego z&nbsp;naszego systemu (np. Edge na Windowsie, Safari na MacOS).

Pamiętajmy tylko, **żeby żadną z&nbsp;tych przeglądarek nie był Chrome**, który lubi paplać o&nbsp;nas Google'owi.

Zamiast niego lepiej zainstalować *[Chromium](https://www.chromium.org/getting-involved/download-chromium)*.  
To goły silnik Chrome'a. Ma identyczne działanie, tych samych twórców, wysyła takiego samego UA... Ale nie ma wbudowanych „integracji” śledzących od Google.

A jeśli nie boimy się bardziej niszowych rzeczy -- jest *[Ungoogled Chromium](https://ungoogled-software.github.io/ungoogled-chromium-binaries/)*. To wersja, która z&nbsp;założenia ma być niezależna od usług Google'a. A&nbsp;poza tym ma większość tych samych funkcji co Chrome.


# Na urządzeniu mobilnym

Tutaj nie ma zastosowania porada „po prostu miej wiele przeglądarek”.  
Niestety nie da się łatwo zainstalować wersji komputerowej na telefonie.

Na szczęście rozwiązanie może być proste -- **niektóre przeglądarki same umożliwiają łatwą zmianę**.

Na Androidzie taką funkcję ma na przykład Firefox (w&nbsp;wersji Focus i&nbsp;zwykłej).  
W każdej z&nbsp;nich można kliknąć ikonę ustawień w&nbsp;prawym górnym rogu i&nbsp;zaznaczyć tam opcję „Wersja na komputery”:

{:.figure .bigspace}
<img src="/assets/posts/user-agent/firefox-focus-wersja-na-kompy.webp" alt="Opcje przeglądarki Firefox Focus. Na żółto zakreślona jedna z&nbsp;nich, korzystania z&nbsp;wersji na komputery." width="400px"/>

Za kulisami nasza przeglądarka będzie wysyłała lekko zmienionego *user agenta*. A&nbsp;nam powinny się wyświetlać strony takie jak na komputery.

Czyli, w&nbsp;przypadku Messengera, zobaczymy ekran logowania zamiast przycisku odsyłającego do apki. Możemy przeglądać wiadomości, nie oddając się w&nbsp;całości Fejsowi :metal:

Wada: w&nbsp;tej wersji strony mogą być nieco cięższe, wolniejsze i&nbsp;niedopasowane do rozmiaru ekranu. Wyświetlając je, liczmy się z&nbsp;koniecznością częstego przewijania i&nbsp;przybliżania ekranu.

# Ogólne rozwiązanie

Czasem (pamiętając o&nbsp;ryzyku zdemaskowania) możemy mimo wszystko chcieć się podszyć pod całkiem inną przeglądarkę.

Przykładem jest sytuacja, gdy nie jesteśmy w stanie zainstalować wymaganej przeglądarki.

Może np. chcemy odwiedzić stronę wpuszczającą tylko ludzi z&nbsp;przeglądarką Safari. A&nbsp;to program od Apple. Działa na ich sprzęcie, ale na innych systemach operacyjnych łatwo jej nie odpalimy.

Inny przykład: chcemy używać konkretnej przeglądarki, bo lubimy jej funkcje. Ale strona jej nie wpuszcza.

Sam tego doświadczyłem w&nbsp;pracy. Nie wchodząc w&nbsp;szczegóły: potrzebowałem możliwości łatwego robienia długich screenów i&nbsp;otwierania ramek (*iframe*) w&nbsp;osobnych oknach.  
Dałby mi to Firefox, ale strona przepuszczała tylko Chromium, dużo uboższe pod tym względem. 

Jeśli znajdziemy się w takich sytuacjach i&nbsp;musimy zmienić UA, możemy użyć dodatku do przeglądarki.

{% include web-extension.html firefox="<p>Sprawdza się tutaj <a href='https://addons.mozilla.org/en-US/firefox/addon/uaswitcher/'>User Agent Switcher</a>.</p>"
chrome="<p>Również <a href='https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg'>User Agent Switcher</a>.</p>"
inne-pc="<p><i>User Agent Switcher</i> ma też <a href='https://microsoftedge.microsoft.com/addons/detail/useragent-switcher/ipacohcfiahhblhbpdnnmnolcakgooci'>wersję na Edge'a</a>.</p>" %}

Po zmianie *user agenta* możecie sprawdzić, czy wszystko działa. Choćby przez odświeżenie tej strony i&nbsp;sprawdzenie, jakiego *user agenta* pokazuje teraz [pole na początku wpisu](#czym-jest-user-agent).

## Podsumowanie

Jeśli jakaś strona rozpoznaje nasz system i&nbsp;przeglądarkę, to już wiemy skąd.

*User agent* -- w&nbsp;porównaniu z&nbsp;niektórymi innymi informacjami z&nbsp;nagłówków HTTP -- nie wydaje się szczególnie groźny. Zwłaszcza jeśli idziemy z&nbsp;prądem i&nbsp;używamy po prostu jakiejś popularnej kombinacji systemu i&nbsp;przeglądarki. Zlewamy się wtedy z&nbsp;tłumem.

Warto jednak pamiętać, że UA to część naszego „odcisku palca” -- w&nbsp;połączeniu z&nbsp;innymi informacjami pozwala nas identyfikować.

Jedną z&nbsp;tych informacji (a przy tym bardziej kłopotliwą, bo trudną do zmiany!) jest nasz adres IP. To on będzie tematem kolejnego wpisu.

<script>
document.getElementById('user-agent').innerHTML = navigator.userAgent;
</script>

