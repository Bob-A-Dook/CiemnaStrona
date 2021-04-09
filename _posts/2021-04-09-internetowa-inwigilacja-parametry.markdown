---
layout: post
title:  "Internetowa inwigilacja 4 – parametry w linkach"
subtitle: "„Chcesz coś dodać?”"
date:   2021-04-09 01:22:00 +0100
tags: [Internet, Inwigilacja, Porady]
firmy: [Twitter, Facebook, Google]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
---

W pierwszym wpisie z&nbsp;tej serii pokazałem po raz pierwszy nagłówki HTTP -- informacje, jakie nasza przeglądarka wysyła stronom internetowym, kiedy surfujemy po sieci.  
Porównałem je do etykiety naklejanej na poczcie na listy i&nbsp;paczki.

Drugi wpis skupił się na jednej z&nbsp;tych informacji, *refererze* -- mówiącym stronie B, na którą przechodzimy, że kliknęliśmy link do niej na stronie A.

Poprzedni wpis omówił metodę stosowaną m.in. przez Twittera i&nbsp;polegającą na podmianie linków na *przekierowania*. Zamiast bezpośredniego przejścia z&nbsp;A do B musieliśmy iść przez stronę pośrednią C, przy okazji pokazując jej naszą etykietę z danymi.

Temat tego wpisu jest trzecim z kolei związanym z linkami. Ale na szczęście ostatnim, jeśli już zaczęły Was nudzić!  
Pokażę tutaj **parametry -- informacje opcjonalne, jakie strony mogą dyskretnie dodawać do linków**. Oczywiście również w&nbsp;celu śledzenia.

## Parametry w&nbsp;praktyce

Oto link do strony, na której teraz jesteś:

<div class="black-bg"><strong id="params">Masz wyłączony JavaScript!</strong></div>

Przyjrzyj mu się. Potem kliknij <a href="?strona=ciemna_strona&seria=internetowa_inwigilacja">tutaj</a>, żeby załadować stronę ponownie. Co się zmieniło?

<p style="margin-bottom:100px"/>

Spostrzegawcze oko zauważy, że to cały czas ten sam link, tylko że na końcu dodało tekst `?nazwa=ciemna_strona&seria=internetowa_inwigilacja`.

Wszystko po znaku zapytania to właśnie **parametry**, czyli elementy opcjonalne dodawane do linków.  
Parametry mają prostą budowę:

* Są dodawane do linku po znaku zapytania;
* Mają format par `nazwa=wartość`;
* Pary są od siebie oddzielone znakami `&`.

Zatem w&nbsp;przypadku tego linku wyżej mamy dwa parametry:

1. o nazwie `strona` i&nbsp;wartości `ciemna_strona`;
2. o nazwie `seria` i&nbsp;wartości `internetowa_inwigilacja`.

{% include info.html type="Porada" text="Nie ma co psuć sobie wzroku, przeglądając parametry gołym okiem. Można je łatwo wyświetlić w&nbsp;narzędziach przeglądarki.  
Naciskamy `Ctrl+Shift+I`, wybieramy zakładkę `Sieć` u&nbsp;góry. Odświeżamy stronę. Po załadowaniu listy elementów klikamy na dowolny z&nbsp;nich. Na dole, w&nbsp;zakładce `Parametry`, zobaczymy parametry w&nbsp;czytelnej formie:" trailer="<p class='figure'><img src='/assets/posts/linki-parametry/dev-tools-parametry.webp' width='500px' alt='Zrzut ekranu z Inspektora pokazujący listę z dwoma parametrami z linka do aktualnej strony oraz ich wartościami.'/></p>" %}

Parametry z&nbsp;założenia są elementami opcjonalnymi. Czyli: grzeczne serwery nie powinny się obrażać, jeśli za znakiem zapytania znajdą jakieś bzdury. Powinny to zignorować.  
(Mój wewnętrzny troll już widzi potencjał na wpychanie tam spamu :smiling_imp:).

## Śledzenie przez parametry

No i&nbsp;OK, te parametry to ciekawy detal. Ale wiemy, o&nbsp;czym jest ten blog, prawda? Więc teraz czas na ich ciemną stronę.

Przede wszystkim umożliwiają **bardzo dokładne śledzenie**.

Znacie może popularny szpiegowski trik polegający na tym, że każdemu z&nbsp;potencjalnych zdrajców podrzuca się inne informacje? Kiedy te potem wyciekną, to będzie wiadomo, która z&nbsp;podejrzanych osób się wygadała.

Podobnie jest z&nbsp;parametrami. Jeśli strona jakimiś metodami zidentyfikuje użytkownika (na przykład przez JavaScript, który omówię za kilka wpisów), to może stworzyć **link specjalnie dla niego, z&nbsp;unikalnym identyfikatorem** wepchniętym w&nbsp;parametry.

Kiedy ofiara go kliknie, to trafi na tę samą stronę, na którą by trafiła, gdyby link nie zawierał parametrów. Niczego nie zauważy.  
Ale w momencie połączenia serwer dostanie komplet informacji, w&nbsp;tym parametry. Wie, czego w&nbsp;nich wypatrywać. Znajdzie tam informacje, że to konkretna osoba przyszła w&nbsp;odwiedziny...

Nie trzeba zresztą aż tak dokładnej identyfikacji. Czasem wystarczy podrzucić kilka różnych linków na różne strony albo wysłać w różnych mailach.

Kiedy użytkownicy będą w&nbsp;nie klikali, to po parametrach poznamy, z&nbsp;jakich źródeł do nas przychodzą (nawet jeśli będą ukrywali referery!). A&nbsp;jeśli ich dane z&nbsp;„etykiety” są dość unikalne, to można ich nawet rozpoznać.

Spójrzmy, kto w&nbsp;praktyce używa parametrów. Pewnie nie zdziwi nas widok samych znanych graczy:

* parametry śledzące od Google'a zaczynają się często na *utm* (`utm_source`, `utm_medium`...);
* Facebooka -- od `fbclid`;
  
  Zresztą Facebook niczego się nie wstydzi i&nbsp;[sam o&nbsp;tych parametrach wspomina](https://www.facebook.com/business/help/1016122818401732) w&nbsp;swoich materiałach dla firm.

* Instagrama -- od `igshid`.
* Amazona...
  
  Ci to dorzucają całe mnóstwo, w&nbsp;tym wyszukiwane słowa kluczowe, dział, identyfikator:  
  `?s=amazonbasics&srs=10112675011&ie=UTF8&qid=1489067885&sr=8-1&keywords=usb-c`

Dzięki parametrom wszystkie te organizacje mogą łatwo monitorować, w&nbsp;jaki sposób przemieszczamy się po ich stronach. I&nbsp;mówić stronom zewnętrznym, że to od nich przychodzimy.

# Przypadek Facebooka

Spójrzmy dokładniej na jeszcze jeden przykład z&nbsp;Facebooka. Wspominałem [w pewnym wpisie]({% post_url 2021-02-11-bierzemy-co-nasze-odzyskiwanie-danych-z-facebooka %}), w&nbsp;jaki sposób można tam pobierać i&nbsp;przeglądać swoje dane.

Tak to wygląda, kiedy wejdziemy w&nbsp;tryb przeglądania i&nbsp;chcemy wejść w&nbsp;całą listę swoich aktywności:

{:.figure .bigspace}
<img src="/assets/posts/linki-parametry/fb-aktywnosc-poza.webp" alt="Zrzut ekranu z Facebooka, z zakładki przeglądania swoich informacji. Jest tu pięć opcji, które można kliknąć. Jedna z nich, 'Posty z aplikacji i witryn', jest otoczona czerwoną ramką."/>

Pod zaznaczonym polem ukrywa się link:

<div class="black-bg mono">https://www.facebook.com/MOJA_NAZWA_KONTA/allactivity<span class="red">?category_key=allapps&privacy_source=access_hub&entry_point=ayi_hub</span></div>


Link prowadzi do podstrony `allactivity`. Zawiera trzy parametry:

* `category_key` o&nbsp;wartości `allapps`;
* `privacy_source` o&nbsp;wartości `access_hub`;
* `entry_point` o&nbsp;wartości `ayi_hub`.

Domyślam się, że skrót `ayi` rozwija się w&nbsp;`Access Your Information`, czyli nazwę zakładki z&nbsp;informacjami.

Mogę tylko zgadywać, co serwery Facebooka robią z&nbsp;tymi parametrami. W&nbsp;niewinnym przypadku po prostu jakoś sobie optymalizuje stronkę, żeby np. nie ładować czegoś niepotrzebnego.

Ale gdyby chciał, to mógłby też łatwo sobie notować, kto korzystał z&nbsp;dobrodziejstw RODO i&nbsp;interesował się swoimi informacjami. Albo liczyć, jaki ogólnie jest w&nbsp;narodzie trend ku sprawdzaniu swojej prywatności.

Brzmi jak teoria spiskowa? Może, ale kiedyś Facebook już kusił ludzi darmową apką, która potem wysyłała mu listę innych zainstalowanych aplikacji. Dzięki temu [wykrywał na bieżąco](https://businessinsider.com.pl/technologie/nowe-technologie/facebook-onavo-aplikacja-wycofana-z-rynku/2k1bhhr), czy wyrasta mu konkurencja. I&nbsp;**wykupił WhatsAppa, nim ten urósł w&nbsp;siłę**.

{% include info.html type="Ciekawostka" text="Już od jakiegoś czasu ich nie widziałem, ale kiedyś Facebook potrafił dodawać do różnych nowinek na tablicy parametr `cft[0]`, którego wartością był dłuuuuugi ciąg znaków. Inny dla każdego posta, ale taki sam dla wszystkich linków z&nbsp;tego posta (czyli np. obrazka, linku do profilu autora, linku z&nbsp;treści...).  
Jakiś unikalny identyfikator?  
Chcąc poszukać, o&nbsp;co chodzi z&nbsp;tymi parametrami, wpisałem w&nbsp;wyszukiwarkę *cft[0] in facebook*. Okazało się, że [ktoś już o&nbsp;to zapytał](https://stackoverflow.com/questions/64092454/what-is-the-purpose-of-the-new-cft-0-and-tn-parameters-in-facebook-po), ale nie dostał żadnej odpowiedzi.  
Dowiedziałem się jedynie, że według autora to `__cft[0]__` to coś względnie nowego, z&nbsp;maja 2020 r." %}

# Parametry + przekierowania

Nawiążę teraz do poprzedniego wpisu, o&nbsp;podmianie linków i&nbsp;przekierowaniach. Twitter dla każdego linku tworzył osobną mini-stronkę. Jak się okazuje, nie trzeba być tak rozrzutnym.

Dzięki parametrom można naszykować jedną i&nbsp;tę samą stronę dla wszystkich przekierowań. A&nbsp;adresy stron, do których mają zostać przekierowani ludzie, upychać w&nbsp;parametrach.

Tutaj przykład z&nbsp;chatu platformy Steam znaleziony na [stronie dodatku Link Cleaner](https://addons.mozilla.org/en-US/firefox/addon/link-cleaner/):

<div class="black-bg mono">https://steamcommunity.com/linkfilter/<span class="red">?url=https://getfedora.org/</span></div>

Link prowadzi do podstrony `linkfilter` w&nbsp;domenie *steamcommunity.com*.  
Ma jeden parametr: `url`, o&nbsp;wartości `https://getfedora.org/`. To link docelowy.

**Steam oczekuje, że będzie tak:**

1. Klikniemy w&nbsp;ten ich podmieniony link;
2. Przeniesie nas do strony *linkfilter*.  

   Oprócz parametrów serwer dostanie teraz naszą etykietę z informacjami (w tym zapewne m.in. pliki cookies Steama, identyfikujące nasze konto). Będzie wiedział, że ta konkretna osoba kliknęła w&nbsp;ten konkretny link.
  
3. Serwer przeanalizuje parametr *url*.
4. Przekieruje nas do strony z&nbsp;tego parametru.  
  
   Albo i&nbsp;nie. Jeśli strona mu się nie spodoba, to może nas nie przepuścić; poza tym mógłby zapisać sobie w&nbsp;bazie, że ten konkretny użytkownik klika w&nbsp;nieodpowiednie linki.

A jak będzie, jeśli dysponujemy odpowiednim dodatkiem do przeglądarki? Wtedy wszystko odbędzie się w nieco inny sposób, przyjaźniejszy dla nas.

**Jeśli przechytrzymy Steama:**

1. Klikamy w&nbsp;ten podmieniony link.
2. Włącza się dodatek i&nbsp;znajduje w&nbsp;linku parametr z&nbsp;nazwą innej strony.  

   (Może już mieć zapisane w&nbsp;kodzie, żeby przy linkach ze *steamcommunity.com* patrzeć na parametr *url*; może też przeszukiwać parametry wszystkich linków)

3. Każe przeglądarce iść prosto do tej strony.

   W&nbsp;ten sposób Steam się nie dowiaduje, że kliknęliśmy w&nbsp;link. A&nbsp;jeśli go blokował, to nie ma to znaczenia -- bo idziemy bezpośrednio do celu, a&nbsp;nie przez Steamowe przekierowanie.

(W ostateczności moglibyśmy nawet wykonać to ręcznie, kopiując link z parametrów do paska).

# Podsumowanie linków

Możemy zauważyć, że wszystkie trzy sprawy związane z&nbsp;linkami (referer, przekierowania, parametry) nieco się ze sobą łączą:

* jeśli kliknięty link robi nam przekierowanie, to wysyłamy swoje informacje stronkom, którym może nie chcieliśmy;
* wśród tych informacji jest referer, który zdradza gdzie byliśmy.
* w&nbsp;dodatku zarówno w&nbsp;refererze, jak i&nbsp;w klikniętym linku mogą być parametry, które mówią o&nbsp;nas jeszcze więcej.

Myślę, że ta porcja informacji wystarczająco obniżyła naszą ufność do parametrów.  
W poprzednich wpisach mówiłem, że referera można zwykle usuwać bez obaw, a&nbsp;przekierowania da się obejść. A&nbsp;co zrobić z&nbsp;parametrami?

## A&nbsp;może by tak usuwać?

Skoro łatwo je rozpoznać, bo zawsze zaczynają się po znaku zapytania... to włączmy gdzieś regułkę ucinającą wszystko po takim znaku. I&nbsp;po problemie!

...Tylko że niestety nie. W&nbsp;przeciwieństwie do referera, parametry są bardzo aktywnie używane. **Jeśli je zablokujemy, spory kawałek internetu przestanie nam działać tak jak powinien**.

Najpierw przykład z&nbsp;YouTube'a. Kiedy udostępniamy komuś link do filmu -- klikając przycisk `Udostępnij`, a&nbsp;nie po prostu kopiując adres obecnej strony -- to możemy wskazać konkretny moment, od którego zacznie się film.

{:.figure .bigspace}
<img src="/assets/posts/linki-parametry/youtube-wybor-czasu.webp" alt="Zrzut ekranu z YouTube'a pokazujący ekran udostępniania. Czerwonym kolorem podkreślony parametr t na końcu linku do udostępniania, odpowiadający 42. minucie filmu."/>

Wtedy do linku zostanie dodany parametr `t`. Jego wartość to liczba sekund od rozpoczęcia filmu.

Gdybyśmy ucinali wszystkie parametry i przesłali link bez nich, to strona nadal będzie działała, ale film będzie nam się wyświetlał zawsze od początku, a&nbsp;nie od wskazanego miejsca.

Innym razem parametry są wręcz niezbędne i&nbsp;strona bez nich nie działa. Przykładem Hacker News, bodaj moje ulubione anglojęzyczne forum dyskusyjne. Link do jednej z&nbsp;dyskusji kończy się parametrem `id=26274035`.

Jeśli usuniemy z&nbsp;linku parametry, czyli wszystko po znaku zapytania, to zostaniemy praktycznie z niczym. A po wejściu w&nbsp;taki link wyświetli nam błąd:

{:.bigspace}
<img src="/assets/posts/linki-parametry/po-co-parametry.webp" alt="Fragmenty dwóch screenów. Jeden pokazuje stronę Hackernews, kiedy w pasku adresu jest pełen link. Parametr id jest w nim podkreślony na czerwono. Drugi pokazuje tę samą stronę bez parametrów. Widać wyświetlony komunikat o błędzie."/>

Jak widać, **bez parametru _id_ z&nbsp;określoną wartością nie dostaniemy tego, na co liczyliśmy**. Gdybyśmy automatycznie usuwali wszystkie parametry, to strona by w&nbsp;ogóle nie działała.

A Hacker News nie jest tutaj wyjątkiem. Jest wiele innych stron, dla których parametry mają znaczenie. Formularze, zakupy online... do wyboru, do koloru.

W związku z&nbsp;tym parametry są integralną częścią internetu i&nbsp;opcja nuklearna raczej nie zadziała. Każdy przypadek jest inny.

Pewnym rozwiązaniem jest tworzenie i&nbsp;aktualizowanie na bieżąco list z&nbsp;nazwami parametrów, które służą tylko do śledzenia. Żeby je potem usuwać bez obaw. Takie listy prowadzą m.in. twórcy dodatków do przeglądarek.

## Dodatki do przeglądarek

Dodatków jest na szczęście sporo. Wystarczy wejść na stronę odpowiednią dla swojej przeglądarki i&nbsp;je sobie zainstalować.

Wśród nich wyróżniają się natomiast dwa -- *ClearURLs* i&nbsp;*NeatURL*  
Pod względem ocen i&nbsp;opinii na forach idą praktycznie łeb w&nbsp;łeb. Oba sprawnie usuwają znane parametry śledzące.

Różnice między nimi? *ClearURLs* jest częściej aktualizowany, ale listy parametrów do usunięcia zapewnia społeczność.  
Z kolei *NeatURL* jest mniej aktywny, ale pozwala dodawać własne reguły usuwające. Więc może nam wiernie służyć, nawet gdyby społeczność straciła zainteresowanie.

Sam jako zwolennik odrobiny majsterkowania wybrałem **Neat URL**.  
Ma wersje dla [Firefoxa](https://addons.mozilla.org/en-US/firefox/addon/neat-url/) i&nbsp;dla [Chrome'a](https://chrome.google.com/webstore/detail/neat-url/jchobbjgibcahbheicfocecmhocglkco).

Oczywiście możecie wypróbować oba i&nbsp;wybrać ten, który lepiej Wam pasuje!  
Tutaj z&nbsp;kolei jest *ClearURLs* [na Firefoxa](https://addons.mozilla.org/en-US/firefox/addon/clearurls/) i&nbsp;[na Chrome'a](https://chrome.google.com/webstore/detail/clearurls/lckanjgmijmafbedllaakclkaicjfmnk/).

{% include info.html type="Niedobry Google" text="Niedawno miała miejsce aferka z&nbsp;udziałem ClearURLs i&nbsp;Google'a.  
Dodatek **został usunięty przez Google z&nbsp;Chrome Web Store'a** (ich archiwum dodatków do przeglądarki) z&nbsp;dość naciąganych przyczyn. Po [burzliwej dyskusji](https://github.com/ClearURLs/Addon/issues/102) i&nbsp;odwołaniu się przez autora został przywrócony.  
Tym niemniej cała sytuacja pokazuje, jak dużą władzę nad przeglądarką ma Google. Kiedy pobieramy dodatki, to je „instalujemy” (z nazwy), ale nie ma to nic wspólnego z&nbsp;trwałą instalacją normalnych programów.  
Wystarczy że Google przełączy po swojej stronie jeden pstryczek, a&nbsp;nasz dodatek do Chrome'a przestaje działać."%}

## Podsumowanie

Parametry to dość ciekawy przykład tego, że **granica między śledzeniem a&nbsp;normalnymi funkcjami internetu bywa rozmyta**. I&nbsp;nie jest to ostatni przykład. Podobnie jest z&nbsp;innymi danymi, jakie wysyła nasza przeglądarka i&nbsp;jakie jeszcze poznamy.

W takiej sytuacji możemy oczywiście zdać się na autorów bezpiecznych przeglądarek i&nbsp;dodatków blokujących. I&nbsp;wierzyć, że będą na bieżąco aktualizowali listy blokowanych rzeczy.

Ale to tylko ludzie, a&nbsp;przeciwko sobie mają kilka wielkich organizacji. Kiedy zablokują jakiś element śledzący, to ich adwersarze mogą łatwo zmienić jego nazwę. Albo nawet wyłączyć ich dodatek.  
Prywatność domyślna, za kulisami i&nbsp;bez kiwnięcia palcem ze strony użytkowników, to moim zdaniem utopia.

Dlatego **jedyną trwalszą ochroną jest moim zdaniem własna wiedza**.

Żeby osoba chcąca prywatności wiedziała przynajmniej, żeby korzystać z&nbsp;jak najsilniejszej blokady. A&nbsp;kiedy jakieś strony nie będą działały, to żeby umiała tę blokadę tymczasowo wyłączyć.

Nie wydaje mi się, żeby to przerastało ludzi -- w&nbsp;końcu już teraz podobnie wygląda sytuacja z&nbsp;*ad blockerami*. A&nbsp;w różnych korpo szkolenia z&nbsp;ochrony przed *phishingiem* są powszechne.  
Takie „ABC” prywatności w&nbsp;sieci nie wydaje się poza zasięgiem, a&nbsp;dużo by zmieniło.

Ale koniec rozważań, robota czeka :smile:

W kolejnym wpisie będzie chwila uspokojenia od linków i&nbsp;powrót do „etykiety” (nagłówków HTTP).  
Omówię rzecz ciekawą, ale nieco mniejszego kalibru -- *user agenta*, czyli informacje o&nbsp;urządzeniu i&nbsp;przeglądarce. Do zobaczenia! 

<script>
var params = window.location.href;
document.getElementById("params").innerHTML = params;
</script>
