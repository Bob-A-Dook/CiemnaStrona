---
layout: post
title:  "Nowe i stare linki Facebooka"
subtitle: "Między młotem (cft) a kowadłem (pfbid)."
description: "Między młotem (cft) a kowadłem (pfbid)."
date:   2022-09-14 11:00:00 +0100
tags: [Internet, Inwigilacja]
firmy: [Facebook]
category: facebook_dane
category_readable: "Kochajmy się jak bracia, analizujmy się jak Facebooki"
image:
   path: /assets/posts/facebook_linki/fb-links-baner.jpg
   width: 1200
   height: 700
---

Koncern Meta -- dawniej po prostu Facebook -- niedawno zmienił format niektórych linków na swojej platformie.

Brzmi banalnie? A&nbsp;jednak nie oznaczałbym tej nowinki nalepką „wytwory sezonu ogórkowego”. To coś więcej niż słynna libacja na skwerku.

Facebook nie ma najlepszej reputacji, jeśli chodzi o&nbsp;zerkanie do danych użytkowników. Niektórzy zaczęli **ostrzegać, że linki w&nbsp;nowym formacie pozwolą identyfikować konkretne osoby**. Facebook miałby oko na to, kto udostępnia linki do postów z&nbsp;ich platformy na innych stronach.

Oszczędzę Wam suspensu i&nbsp;od razu napiszę -- **eksperymenty tego nie potwierdziły**. Co nie zmienia faktu, że obecna zmiana może być krokiem ku gorszemu.

Pokażę, o&nbsp;co chodzi w&nbsp;tej całej aferce z&nbsp;linkami. Zobaczymy też, że nawet te istniejące na Facebooku od dawien dawna mogą mieć swoje „szpiegowskie” zastosowania. A&nbsp;na deser będą wskazówki, jak się przed nimi chronić.

{:.bigspace-before}
<img src="/assets/posts/facebook_linki/fb-links-baner-small.jpg" alt="Kolaż złożony z&nbsp;małej planety z&nbsp;okładki Małego Księcia, na której stoi tytułowy bohater. Na planetę nałożono logo Facebooka, literkę F&nbsp;na niebieskim tle. Obok planety unosi się rysunkowa głowa z&nbsp;miną wyrażającą radość. Jej oczy są skierowane na Małego Księcia. Szkła jej okularów są niebieskie jak logo Facebooka. Na jednym z&nbsp;nich widać napis cft i&nbsp;zero w&nbsp;nawiasach kwadratowych, a&nbsp;na drugim pfbid."/>

{:.figcaption}
Źródła: okładka „Małego Księcia”, logo Facebooka, plakat *X-Ray Vision*. Aranżacja moja. 

## Sprawa nowych linków

Spójrzmy na przykładowy link do posta z&nbsp;Facebooka. Tutaj od *Ghacks*. Tej samej strony, która nagłośniła całą sprawę:

{:.bigspace-before}
<div class="black-bg mono">
https://www.facebook.com/ghacksnet/posts/4950751111633509
</div>

{:.figcaption}
**Uwaga**: w&nbsp;tym miejscu oraz w&nbsp;reszcie wpisu odwołuję się do *www.facebook.com*, wersji na komputery; gdybyśmy odwiedzili link przez urządzenie mobilne, to by nas przekierowało do *m.facebook.com*.

Przypatrzmy się temu linkowi dobrze, ma teraz wartość muzealną :wink:  
Gdybyśmy [w niego](https://www.facebook.com/ghacksnet/posts/4950751111633509) weszli, to zobaczymy taki post:

{:.figure .bigspace}
<img src="/assets/posts/facebook_linki/ghacks-post.jpg" alt="Zrzut ekranu pokazujący post ze strony Ghacks na Facebooku. Zawiera on zdjęcie konsoli i&nbsp;informację o&nbsp;nowym programie." width="500"/>

Aby uzyskać linki do konkretnych postów z&nbsp;Facebooka, najeżdża się kursorem na datę (w tym wypadku tekst `24 stycznia 2021`). Ale kiedy to zrobimy, zobaczymy coś zgoła innego, dłuższego. Na przykład to, choć niekoniecznie:

{:.bigspace}
<div class="black-bg mono">
https://www.facebook.com/ghacksnet/posts/<span style="color:#4bc9c8">pfbid0Q4Wc82MvTP8FSLpUHc4vn4jY2YTzhH6D2YZQZXDc5srYrnTXnHkiaZzv4LeRpY4Al</span><span class="red">?__cft__[0]=x&__tn__=%2CO%2CP-R</span>
</div>

Gdyby wejść [w ten link](https://www.facebook.com/ghacksnet/posts/pfbid0Q4Wc82MvTP8FSLpUHc4vn4jY2YTzhH6D2YZQZXDc5srYrnTXnHkiaZzv4LeRpY4Al), to trafimy do tego samego posta co na początku. Zatem Facebook zmienił format linków. Od pewnego czasu wszystkie dodawane do platformy mają tę dłuższą postać.

Tekst od znaku zapytania do końca, na czerwono, to parametry. Jeszcze do nich wrócimy. Literkę *x* wstawiłem tutaj zamiast bardzo długiego ciągu znaków. 

Z kolei fragment na niebiesko to wspomniana zmiana. Nowa postać, jaką mają od pewnego czasu identyfikatory poszczególnych postów na Facebooku.  
Dlaczego wywołała takie poruszenie?

# Czarny scenariusz

O sprawie po raz pierwszy poinformowała strona *Ghacks*, twierdząc że [linki Facebooka są od teraz szyfrowane](https://www.ghacks.net/2022/07/17/facebook-has-started-to-encrypt-links-to-counter-privacy-improving-url-stripping/). Zaś każdemu użytkownikowi wyświetla się unikalny link, inny niż ten dla pozostałych. Stwierdzili wprost, że to w&nbsp;celu śledzenia.

Autor pomylił parę pojęć, ale jego obawy miały swoje podstawy i&nbsp;wywołały lekki szum w&nbsp;mediach.

Mówiąc łopatologicznie -- identyfikator posta jest teraz znacznie dłuższy i&nbsp;może się składać nie tylko z&nbsp;cyfr, ale również liter (możecie porównać na przykładach powyżej).

Nie znam się na liczeniu entropii i&nbsp;tych sprawach, ale wiem jedno. **Po tej zmianie drastycznie zwiększa się ilość informacji, jakie można upchnąć w&nbsp;linku**.  
Jakich informacji? Na przykład o&nbsp;tym, któremu z&nbsp;rzekomych dwóch miliardów użytkowników Facebooka wyświetlił się dany link.

Wyobraźmy sobie, że jakiś Bob Buntowniczy znajduje na Facebooku post wyśmiewający wpływowego polityka. Kopiuje link do posta i&nbsp;zamieszcza go anonimowo na kilku niezależnych stronach.

Ale nie wie, że kopiowany przez niego ciąg znaków jest całkiem inny niż te, jakie wyświetliły się innym użytkownikom Fejsa. Jeśli ktoś od Facebooka zajrzy poza ich portal i&nbsp;znajdzie wrzucone linki, to mógłby sprawdzić w&nbsp;bazie, jakiemu użytkownikowi odpowiadały.

{:.post-meta .bigspace-after}
Nie byłaby to metoda stuprocentowo pewna; może Bob wysłał link Alicji na Messengera, a&nbsp;to Alicja skopiowała go na inne strony. Ujawniałby tylko pierwszą kopiującą osobę.

Być może sam Facebook nic by z&nbsp;tym nie zrobił i&nbsp;tylko siedział na informacjach jak smok na złocie.

Ale ups, oto wyciekła mu baza danych. Jak kiedyś [ta z&nbsp;numerami telefonów](https://niebezpiecznik.pl/post/facebook-wyciek-dane-533-milionow-uzytkownikow/).  
A w&nbsp;międzyczasie wyśmiewany polityk awansował na dyktatora. I&nbsp;teraz sobie sprawdza w&nbsp;tej bazie, jakim konkretnym osobom odpowiadają linki do prześmiewczych postów...

Taka perspektywa mrozi krew w&nbsp;żyłach, więc postanowiłem zbadać temat.

## Weryfikujemy zarzuty

# Prywatny eksperyment

Odwiedziłem profil znanej stronki na Facebooku (konkretniej Festiwalu Pol'and'Rock, ale to akurat detal bez znaczenia). Znalazłem pierwszy post od góry i&nbsp;skopiowałem prowadzący do niego link. Istotnie, miał w&nbsp;sobie *pfbid*. Jak wszystkie od pewnego czasu.

Następnie napisałem do znajomego -- dzięki za pomoc, S! -- z&nbsp;prośbą o&nbsp;znalezienie tego samego posta i&nbsp;sprawdzenie, jaki link mu się pokazuje.

Wysłałem mu *wyłącznie nazwę strony oraz screena pokazującego post*, który mnie interesuje. W&nbsp;żadnym miejscu nie podawałem bezpośredniego odnośnika. Żeby Facebook nie mógł się nim zasugerować.

Znajomy zdobył link i&nbsp;wkleił mi go w&nbsp;wiadomość. Taki sam, jaki pokazywał się mnie. Wniosek: **Facebook nie mógłby użyć wartości _pfbid_ do odróżnienia nas od siebie**.

Ale to dowód anegdotyczny. Może Fejs wdraża zmiany stopniowo, a&nbsp;linki identyfikujące ludzi jeszcze do nas nie dotarły? Reakcję w&nbsp;postaci emotki serca też w&nbsp;końcu dostałem później niż znajomi.

# Opinie innych

Zarówno pod pierwotnym artykułem na Ghacks, jak też w&nbsp;[wątku na forum HackerNews](https://news.ycombinator.com/item?id=32117489), pojawiły się komentarze osób piszących, że widzą taki sam link jak autor i&nbsp;[nie dostali nic innego](https://news.ycombinator.com/item?id=32120262).

Znalazłem też ciekawy [wpis polemizujący z&nbsp;Ghacks](https://ws-dl.blogspot.com/2022/07/2022-07-19-review-of-facebook-has.html). Autor, Michael Nelson, również nie potwierdza, jakoby linki umożliwiały rozróżnianie między ludźmi. Zauważa natomiast trzy bardzo ciekawe rzeczy:

* Zmiana weszła w&nbsp;okolicach 4&nbsp;kwietnia. Odkrył to, przeszukując archiwa internetowe pod kątem tekstu *pfbid*;
* W&nbsp;nowym systemie **może istnieć kilka różnych linków do tego samego posta**.

  Podaje jako przykład trzy różne odnośniki do jednego posta Ghacks. Czarno na białym widzimy, że *pfbid* nie jest stały i&nbsp;unikalny na poziomie posta, jak dawne identyfikatory.

* Zmiana zapewne uderzy w&nbsp;użytkowników archiwów internetowych, utrudniając wyszukiwanie po linkach.

  Przykład? X&nbsp;znajduje na forum link do kontrowersyjnego posta z&nbsp;Facebooka. Próbuje w&nbsp;niego wejść, ale post już został usunięty.  
  No ale na pewno ktoś wrzucił taką perełkę do archiwum, póki jeszcze wisiała? Zatem X&nbsp;wkleja odnośnik w&nbsp;wyszukiwarkę *archive.ph*. Wyświetla się informacja, że nikt nie zarchiwizował takiej strony. X&nbsp;odchodzi z&nbsp;niczym.  
  Mimo że tak naprawdę post jak najbardziej jest w&nbsp;archiwum. Tylko że pod innym linkiem -- takim, jaki widziała osoba archiwizująca w&nbsp;chwili kopiowania. Innym niż ten na forum.

# Wnioski

Jeśli linki nie identyfikują ludzi, ale mają więcej niż jeden wariant... to czym mogą być?

Facebook wysłał do Ghacks oświadczenie, dostępne pod [pierwotnym artykułem](https://www.ghacks.net/2022/07/17/facebook-has-started-to-encrypt-links-to-counter-privacy-improving-url-stripping/). Piszą, że **nowe linki to zabezpieczenie przeciw _scrapingowi_** (automatycznemu pobieraniu danych).

OK. Kłamstwo w&nbsp;tej kwestii byłoby ryzykowne, więc załóżmy że mówią prawdę.  
Ale czy istnieje techniczna możliwość, że kiedyś mogłoby się to rozwinąć w&nbsp;metodę identyfikacji konkretnych osób? Moim zdaniem niestety tak. Policzmy to sobie:

* Dawniej identyfikator posta miał długość 16&nbsp;znaków. Wyłącznie cyfr, co dawało 10&nbsp;możliwych wartości na każdy znak.
* Teraz ma długość 67&nbsp;znaków, nie licząc `pfbid` stojącego zawsze na początku.  
  Oprócz cyfr może się składać z&nbsp;wielkich i&nbsp;małych liter. To łącznie 62&nbsp;możliwości na każdy znak.

  <div class="black-bg mono">
  abcdefghijklmnopqrstuvwxyz<br/>ABCDEFGHIJKLMNOPQRSTUVWXYZ<br/>0123456789
  </div>

[Upewniłem się](https://www.quora.com/What-is-the-mathematical-formula-to-calculate-the-number-of-possible-digits-in-a-numerical-password-containing-4-digits), że w&nbsp;takim wypadku liczba możliwych wariantów to 62<sup>67</sup>. To bardzo duża liczba, ma 121&nbsp;cyfr. Wiele pomieści.

Do tego linki są tak zbudowane, że identyfikator jest umieszczony *po nazwie strony*:

<div class="black-bg mono">
https://www.facebook.com/<span class="red">ghacksnet</span>/posts/pfbid...
</div>

Zatem *pfbid* nie musi mieścić w&nbsp;sobie wszystkich linków dla wszystkich użytkowników, na wszystkich stronach. Tylko znacznie mniejszą liczbę.

To intuicja, bo ekspertem nie jestem. Ale wydaje mi się, że **gdyby Facebook chciał, to mógłby przejść do linków unikalnych na poziomie ludzi**. Rozszerzyć ich rzekomo obronne funkcje. Tu i&nbsp;teraz, bez kolejnej zmiany formatu. A&nbsp;z naszego punktu widzenia zmiana byłaby cicha i&nbsp;niezauważalna.

Co więcej -- **takich identyfikatorów nie dałoby się usuwać**. Spróbowalibyśmy to zmienić na inny ciąg znaków? Popsulibyśmy link, prowadziłby do nieistniejącej strony. Zostawilibyśmy? To by nas identyfikowało.

## Stare linki

Nowe linki zostały z&nbsp;nami jak uśpieni agenci, którzy może okażą kiedyś szpiegowską naturę. A&nbsp;może nie zdążą, nim portal całkiem odpłynie ku Metawersum.

W tej całej aferze wiele osób pomija jednak jedną zasadniczą kwestię -- **Facebook już wcześniej mógł śledzić użytkowników poprzez linki**.

Pokażę tu kilka dodawanych do nich informacji. Mogłyby umożliwić zarówno Facebookowi, jak i&nbsp;jego partnerom rozpoznawanie konkretnych osób.

### Parametry

Najpierw krótko i&nbsp;zwięźle o&nbsp;tym, czym są parametry w&nbsp;linkach.  
Znajdują się na końcu, po znaku zapytania. Są od siebie oddzielone znakami `&`. Każdy z&nbsp;nich ma format `nazwa=wartość`.

<div class="black-bg mono">
https://www.stronka.com/podstronka<span class="red">?param1=liczba1&param2=liczba2</span>
</div>

Gdybyśmy na przykład skopiowali link do jakiegoś wpisu z&nbsp;Ciemnej Strony i&nbsp;dopisali na końcu `?powitanie=hej`, to nic by się nie stało. Serwer by to przyjął, ale olał i&nbsp;po prostu zaserwował wpis, do którego prowadzi nasz odnośnik. To dlatego, że parametry są opcjonalne.

Ale niektóre parametry mają znaczenie. Kiedy serwer je wyłapie, to analizuje zawarte w&nbsp;nich informacje. Pod długim, niezrozumiałym ciągiem znaków może się na przykład ukrywać nazwa konkretnego użytkownika.

Jeśli chcemy dowiedzieć się czegoś więcej w&nbsp;temacie, to zapraszam do [wpisu o&nbsp;parametrach]({% post_url 2021-04-09-internetowa-inwigilacja-parametry %}){:.internal} z&nbsp;„Internetowej inwigilacji”. A&nbsp;teraz przejdźmy do przykładów z&nbsp;samego Facebooka.

### Linki do stron zewnętrznych

Niektóre strony internetowe żyją z&nbsp;Facebookiem w&nbsp;symbiozie. Płacą portalowi za to, że umieści u&nbsp;siebie reklamy odsyłające do ich strony.

Często link ukryty w&nbsp;takiej reklamie zawiera parametry specjalne, zaczynające się od `utm`. Mówią firmie, że dany użytkownik przychodzi z&nbsp;Facebooka. Taki odpowiednik pytania „Skąd pan(-i) o&nbsp;nas usłyszał(-a)” z&nbsp;ankiety, tyle że to cyfrowe i&nbsp;dzieje się w&nbsp;tle. Raczej niegroźna rzecz.

Czasem jednak do linków jest dodawany **parametr `fbclid`, który już wskazuje konkretnego użytkownika**. Nie z&nbsp;imienia i&nbsp;nazwiska. Ale [pokazuje firmie](https://stackoverflow.com/questions/52847475/what-is-fbclid-the-new-facebook-parameter), że pewne jej reklamy klika jedna i&nbsp;ta sama osoba.  
Jeśli ta osoba kiedyś coś kupi po wejściu w&nbsp;link, to numer zyska tożsamość. Firma będzie wiedziała, do czego dany klient ma słabość.

{% include info.html
type="Ciekawostka"
text="Choć parametry z&nbsp;założenia mają być opcjonalne, a&nbsp;serwery powinny ignorować nieznane wartości... rzeczywistość bywa inna.  
Zdarzyło się przez to, że kiedy Facebook dodawał po cichu parametr *fbclid* do umieszczanych u&nbsp;siebie linków -- na początku do wszystkich -- to [odnośniki te przestawały działać](https://news.ycombinator.com/item?id=18275061). Serwery nie wiedziały, co z&nbsp;nimi zrobić."
%}

Autor z&nbsp;Ghacks nie ma racji, pisząc że nowy format linków zastępuje parametry *fbclid*. Te drugie nigdzie się nie ruszyły.  
Zaś nowy, *pfbid*, w&nbsp;ogóle nie dotyczy odnośników prowadzących poza teren Facebooka. Odnosi się wyłącznie do publikowanych na nim postów.

### Linki do postów

Poza nowym *pfbid* są jeszcze dwie rzeczy, które goszczą w&nbsp;linkach prowadzących do postów na Facebooku. Obie z&nbsp;nich to parametry. 

Jednym z&nbsp;tych parametrów jest `__tn__`. Ale wydaje mi się zbyt krótki i&nbsp;powtarzalny, żeby mógł jakoś realnie nas identyfikować.  
Znacznie gorszą sprawą jest parametr `__cft[0]__`. Pozwolę sobie nazywać go krótko „parametrem *cft*”. To ten najdłuższy ciąg znaków, jaki znajdziemy w&nbsp;linku. **Moim zdaniem to jego powinniśmy się najbardziej obawiać**, mógłby nas jednoznacznie identyfikować.

Już od jakiegoś czasu interesuję się tym parametrem. O&nbsp;jego usuwaniu pisałem między innymi we [wpisie o&nbsp;walce z&nbsp;trollami]({% post_url 2022-04-15-trolle-rosja-ukraina%}#wrzucanie-oczyszczonych-linków){:.internal}, a&nbsp;także we wspomnianym wyżej wprowadzeniu do parametrów.

Dotychczasowe fakty, jakie odkryłem na jego temat:

* Ktoś [pytał o&nbsp;niego](https://stackoverflow.com/questions/64092454/what-is-the-purpose-of-the-new-cft-0-and-tn-parameters-in-facebook-po) na słynnym forum StackOverflow, ale nie dostał odpowiedzi.
* Występuje w&nbsp;wersji na komputery (*www.facebook.com*). Nie pojawia się w&nbsp;wersji mobilnej ani uproszczonej (*m.facebook.com* oraz *mbasic.facebook.com*). Linki z&nbsp;tych stron zawierają natomiast nieco inne, krótsze ciągi znaków.
* Dodawany przez Facebooka do niemal wszystkich linków do postów. A&nbsp;także do komentarzy pod nimi.
* Nie jest dodawany m.in. do filmów, te mają format `<PROFIL>/videos/<LICZBA>`. Ani do komentarzy pod nimi.
* Jego wartość ma długość 216&nbsp;znaków.

  {:.post-meta}
**Aktualizacja:** od czasu stworzenia wpisu znalazłem również parametry *cft* z krótszymi wartościami. Raz 110&nbsp;znaków, innym razem 174. Nie znalazłem w&nbsp;tym póki co reguły. Tym niemniej długie ciągi również się trafiają.

* Sam początek regularny, często (zawsze?) zaczyna się od liter *AZ*. Trzecia litera to często coś z&nbsp;dalszej części alfabetu. *U*, *V*, *W*, *X*...  
  Przykład? [Wystąpienia](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=facebook%20cft%20AZ&sort=byDate&type=all) na forum Hacker News.
 
* Reszta tekstu wydaje się losowa. Składa się z&nbsp;liter, cyfr, znaków `_` oraz `-`.
* Zmienia się za każdym razem, kiedy odświeżamy stronę.

  Prosty eksperyment: wejdźmy na komputerze na swój własny profil, skopiujmy gdzieś link do pierwszego posta, naciśnijmy `F5`, porównajmy. Trzon będzie ten sam, ale *cft* każdorazowo się zmieni.  
  Wniosek? Zapewne zawiera w&nbsp;sobie jakiś znacznik czasu. Oczywiście oprócz tego może tam być informacja o&nbsp;konkretnym użytkowniku.

* Przez te wszystkie kreski i&nbsp;nawiasy trudno go znaleźć w&nbsp;wyszukiwarkach, które zwykle wycinają takie elementy. Proponuję szukać poprzez wpisywanie:  
  `"facebook" "cft"`.

* **Można bezpiecznie usuwać go z&nbsp;linków**. Nadal będą prowadziły do tego posta, do którego miały. Z&nbsp;*tn* tak samo.

Ogólnie sprawa tajemnicza i&nbsp;nieco podejrzana. Ale ostatni punkt dodaje otuchy.

## Kwestia marnotrawstwa

Niezależnie od celu linków możemy się zastanowić nad ich sensownością.

W lwiej części przypadków **zapewne niczego cennego Fejsowi nie przyniosły**. Wyobrażam sobie, że wiele osób udostępniło je co najwyżej swoim znajomym przez Messengera. Który i&nbsp;tak jest własnością FB, więc znają tożsamość udostępniaczy.  
Mimo to Facebook od lat napycha do swoich linków nowe rzeczy:

* Nowy identyfikator *pfbid* liczy 72&nbsp;znaki, czyli o&nbsp;56 więcej niż poprzedni.
* Sam parametr *cft* może liczyć w&nbsp;niektórych przypadkach nawet 227&nbsp;znaków (pełna nazwa plus wartość).
* Parametr *tn* to 16&nbsp;znaków (nazwa plus wartość)
* Obecność powyższej dwójki oznacza też znak zapytania i&nbsp;łącznik. 2&nbsp;kolejne znaki.

Łącznie każdy link Facebooka może rozdymać się aż o&nbsp;301 znaków. **Z&nbsp;czego&nbsp;245 -- te związane z&nbsp;parametrami -- da się bezkarnie usuwać**.

Problem w&nbsp;tym, że mało kto o&nbsp;tym wie. I&nbsp;linki są udostępniane w&nbsp;postaci nieoczyszczonej -- na samym Facebooku, Messengerze, stronkach całkiem zewnętrznych.   
Wyobraźmy sobie, ile się tego nazbiera w&nbsp;skali świata. Ile giga- albo terabajtów zostanie zapchanych samymi tylko wartościami *cft* oraz *tn*.

Oczywiście, że w&nbsp;skali świata to kropla w&nbsp;morzu. Nie ma co wyobrażać sobie kominów i&nbsp;dymu pochodzącego za spalanych fejsowych parametrów.
  
Ale firmy lubią nam mówić, że każda, najdrobniejsza rzecz coś zmienia. Jak w&nbsp;takim kontekście ocenić Facebooka? Czy nie dokłada cegiełki do kultu cyfrowego marnotrawstwa?  
Zostawiam to pod rozwagę. A&nbsp;jeśli my nie chcemy marnowania miejsca na dyskach -- albo śledzenia -- to usuwajmy parametry. Poniżej dokładniejsze wskazówki.

## Porady

# Usuwanie śmieciowych parametrów

Mam tu na myśli *cft*, *tn* oraz *fbclid*.  
**Po prostu je usuwamy**, mam nadzieję że pomogłem :smile: Dzięki temu linki będą schludniejsze, a&nbsp;my mniej śledzeni.

Mając link do posta, możemy skopiować go do jakiegoś notatnika, wypatrzyć `__cft` i&nbsp;usunąć wszystko od tego tekstu (wraz z&nbsp;nim) aż do końca.

{% include info.html
type="Uwaga"
text="Rzadko bo rzadko, ale czasem trafiają się parametry `story_fbid=X` oraz `id=X` wskazujące konkretne posty. Więc lepiej nie ciąć tak całkiem wszystkiego, od znaku zapytania do końca.  
Jeśli chcemy zalinkować do konkretnych komentarzy (raczej rzadka potrzeba), musimy ponadto pozostawić parametry `comment_id=X` oraz `reply_comment_id=X`."
%}

W każdym przypadku, zostawiając jakieś parametry, zostawiamy też znak zapytania na początku oraz ewentualne znaki `&` między nimi.

Przy stronach zewnętrznych nie ma jednej reguły, a&nbsp;parametry bywają potrzebne. Ale ogólnie zawsze możemy bezpiecznie usuwać `fbclid=X` oraz parametry zaczynające się od `utm_`.

Nowsze wersje Firefoksa [same usuwają](https://www.engadget.com/firefox-can-now-automatically-remove-tracking-from-ur-ls-115228742.html) znane szkodniki wśród parametrów.

Można również skorzystać z&nbsp;dodatku do przeglądarki takiego jak **ClearURLs**. Korzysta ze znanych list nielubianych parametrów i&nbsp;automatycznie je usuwa, kiedy klikamy w&nbsp;linki. Ma wersje na [Firefoksa](https://addons.mozilla.org/en-US/firefox/addon/clearurls/) oraz na [Chrome'a i&nbsp;oparte na nim przeglądarki](https://chrome.google.com/webstore/detail/neat-url/jchobbjgibcahbheicfocecmhocglkco). 

# Rozwiązanie problemów z&nbsp;pfbid

Jak wspomniałem, chwilowo nowe linki są raczej niegroźne. Poza tym znalazłem na nie pewien trik, który omawiam pod sam koniec.  
Ale na razie załóżmy najgorszy scenariusz. Trik nie działa, a&nbsp;linki po cichu zyskały możliwość identyfikowania użytkowników.

Co w&nbsp;takim wypadku zrobić, jeśli absolutnie musimy udostępnić link z&nbsp;Fejsa, a&nbsp;nie chcemy go wiązać z&nbsp;naszą tożsamością?

Zapewne pomogłoby pozyskanie go przez **fejkowe konto**, trzymane z&nbsp;dala od naszego głównego. Najlepiej odwiedzane przez całkiem osobny komputer, z&nbsp;własnym połączeniem internetowym. Jak taki z&nbsp;czytelni bibliotecznej.

Inna opcja? Zamiast wrzucać bezpośrednie linki, możemy **robić screeny albo cytować tekst posta**, którym chcemy się podzielić. Jeśli chcemy dodatkowo wskazać źródło, to można wrzucić:

* adres profilu, który dodał danego posta;
* datę jego dodania;
* fragment tekstu, który pozwoliłby go wyszukać.

Przy tylu informacjach osoba zainteresowana mogłaby łatwo znaleźć wskazanego posta. A&nbsp;gdyby zainteresowana nie była, to nawet bezpośrednie podesłanie by nie pomogło.

A co mogą zrobić internetowi archiwiści, kiedy linki przestaną być dobry sposobem na znalezienie postów?

Jeśli archiwizujemy treści z&nbsp;FB, to umieszczajmy w&nbsp;jakimś miejscu (na przykład w&nbsp;osobnym wpisie na Twitterze) kontekst związany z&nbsp;danym linkiem. Nazwy postaci, jakiś fragment tekstu itp. Żeby poszukiwacze mieli kilka sposobów dotarcia do źródła.

Przydałaby się też współpraca ze strony archiwów -- możliwość tagowania znalezisk, przeszukiwania po tekście itp. Żeby linki nie były jedynym sposobem uzyskania dostępu.

## Podsumowanie

Widzimy, że nowe linki Facebooka na razie niewiele zmieniają, a&nbsp;sensacja była nieco na wyrost. Ale będą nam wisiały nad głowami jak miecz Damoklesa i&nbsp;możliwe, że jeszcze pokażą ciemną stronę. W&nbsp;takim wypadku pozostaną fejkowe konta albo odsyłanie do źródeł w&nbsp;sposób opisowy.

W związku z&nbsp;całą sytuacją do głowy przyszedł mi pomysł na amatorski system ostrzegający przed taką zmianą.

Można co pewien czas pobierać swoje dane przez domyślne opcje Facebooka. W&nbsp;tym -- wszystkie wrzucone przez siebie posty. Następnie porównywać linki. Patrzeć, czy *pfbid* ulega zmianom. Sprawdzać, czy znajomi widzą to samo.

Chętnie zrobię do tego jakiś skrypt, ale to już temat na ewentualny przyszły wpis.

A skoro o&nbsp;wpisach mowa... to oficjalnie mój wpis numer 50&nbsp;na stronie głównej bloga :smile:  
Kolejny cel -- okrągła setka. Mam nadzieję, że jeszcze się tu spotkamy w&nbsp;drodze do niej!

### Bonus: powrót do dawnego formatu

Przeglądając wątek na HackerNews, znalazłem prawdziwy skarb -- [sposób](https://news.ycombinator.com/item?id=32118393) na skonwertowanie linków w&nbsp;nowym stylu na wersję dawną, pozbawioną *pfbid*. Wymaga szczypty zachodu, więc zostawiłem go na koniec.

Najpierw kopiujemy cały link z&nbsp;*pfbid*. Możemy z&nbsp;niego usunąć parametry.  
Musimy teraz zamienić go na bezpieczną postać, zastępując dwukropek na początku. Można nawet całkiem ręcznie. Zmieniamy `:` na `%3A`.

{:.post-meta .bigspace}
Odkryłem, że tylko zmiana dwukropka była obowiązkowa na moich przeglądarkach. Ale inne przekształcenia, jak zmianę każdego `/` na `%2F`, również można wykonać bez obaw.

Jeśli nie obawiamy się o kwestie prywatności, możemy zamienić niewygodne znaki, używając stronki [takiej jak Utilities Online](https://www.utilities-online.info/urlencode).

Następnie kopiujemy do paska poniższy adres (nazwę go umownie *konwerterem*):

<div class="black-bg mono bigspace">
https://www.facebook.com/plugins/post.php?href=<span class="red">LINK</span>
</div>

Zamiast czerwonego tekstu `LINK` wklejamy nasz bezpieczny link otrzymany wcześniej. I&nbsp;gotowe.

Zobaczmy całość na przykładzie. Przypomnę tu link przykładowy z&nbsp;*pfbid* z&nbsp;początku wpisu:

{:.bigspace}
<div class="black-bg mono">
https://www.facebook.com/ghacksnet/posts/pfbid0Q4Wc82MvTP8FSLpUHc4vn4jY2YTzhH6D2YZQZXDc5srYrnTXnHkiaZzv4LeRpY4Al?__cft__[0]=x&__tn__=%2CO%2CP-R
</div>

Po usunięciu parametrów, zamianie niewygodnych elementów i doklejeniu do linku-konwertera otrzymamy takie coś:

<div class="black-bg mono bigspace">
https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fghacksnet%2Fposts%2Fpfbid0Q4Wc82MvTP8FSLpUHc4vn4jY2YTzhH6D2YZQZXDc5srYrnTXnHkiaZzv4LeRpY4Al
</div>

Kiedy w&nbsp;to wejdziemy, to zobaczymy sam post, bez reszty interfejsu. Nawet jeśli nie jesteśmy zalogowani na konto. A&nbsp;po najechaniu na jego datę dodania zobaczymy link w&nbsp;starym dobrym stylu, z krótszym identyfikatorem.

Można go sobie skopiować na później. Albo nazbierać przykładów i&nbsp;spróbować rozgryźć, jakiego mechanizmu używa FB do konwersji z&nbsp;nowych na stare.

Oczywiście **bardzo możliwe, że z&nbsp;czasem usuną tę furtkę**. Więc cieszmy się nią, póki jest!

