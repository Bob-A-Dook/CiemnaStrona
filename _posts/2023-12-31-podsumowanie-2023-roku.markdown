---
layout: post
title: "Podsumowanie 2023 roku"
subtitle: "Ofensywa Google'a, dziadowskie przepisy i afera kolejowa."
description: "Ofensywa Google'a, dziadowskie przepisy i afera kolejowa."
date:   2023-12-31 15:37:00 +0100
tags: [Afera, Centralizacja, DRM, Internet, Reklamy]
firmy: [Google, Newag]
image:
  path: /assets/posts/podsumowania/2023/2023-podsumowanie.jpg
  width: 1200
  height: 700
  alt: "Kadr z filmu World War Z, pokazujący armię zombie próbującą przeskoczyć z autobusu na helikopter. Autobus jest podpisany 2023, zombie to 'Problemy roku 2023', a helikopter to 2024."
---

Kolejny rok dobiega końca! Z&nbsp;tej okazji czas na moje tradycyjne, krótkie podsumowanie tego, co przyniósł w&nbsp;kwestii cyfrowej prywatności i&nbsp;wojny ludzi z&nbsp;megakorporacjami.

O niektórych wspomnianych tu rzeczach stworzyłem pełne wpisy. O&nbsp;niektórych nie zdążyłem. Ale wszystkie uważam za istotne.

## Spis treści

* [Zakusy korporacji](#zakusy-korporacji)
  * [Afera wokół firmy Newag](#afera-wokół-firmy-newag)
  * [Google kontra blokery śledzenia](#google-kontra-blokery-śledzenia)
  * [Google kontra Departament Sprawiedliwości](#google-kontra-departament-sprawiedliwości)
  * [Zablokowanie przejęcia Figmy przez Adobe](#zablokowanie-przejęcia-figmy-przez-adobe)
* [Zakusy rządzących](#zakusy-rządzących)
  * [Kontrola czatów](#kontrola-czatów)
  * [Artykuł 45&nbsp;i zaufanie regulowane ustawą](#artykuł-45i-zaufanie-regulowane-ustawą)
* [Co w&nbsp;2024 roku?](#co-w2024-roku)


## Zakusy korporacji

### Afera wokół firmy Newag

Na koniec roku wybuchła prawdziwa bomba -- **Polska doczekała się własnej afery związanej z&nbsp;cyfrowymi blokadami. Zrobiło się o tym głośno również za granicą**.

Polscy spece od analizy kodu, Dragon Sector (będę pisał skrótowo DS), dostali nietypowe zadanie od firmy serwisującej pociągi.  
Firma mimo wszelkich starań nie była w&nbsp;stanie naprawić pociągów firmy Newag. Mieli podejrzenie, że ktoś nałożył ukryte blokady na poziomie cyfrowym. Żeby wyszli na niekompetentnych i&nbsp;musieli stracić kontrakt na rzecz Newagu.

Ludzi z&nbsp;DS-a poproszono o&nbsp;włączenie pociągów i&nbsp;znalezienie przyczyn dziwnych usterek. Zaglądając do oprogramowania sterującego, znaleźli trochę kodu o&nbsp;niepokojącym działaniu:

1. Kod blokujący tabory naprawiane poza oficjalnymi zakładami firmy.  
   Pociąg był wyposażony w&nbsp;odbiornik GPS. Jeśli przez 10&nbsp;dni stał w&nbsp;którejś z&nbsp;określonych lokalizacji, odpowiadających warsztatom konkurencji, to miał się wyłączyć „na amen” i&nbsp;nie dawać się uruchomić.

2. Kod wyświetlający błąd po określonej listopadowej dacie.  
   Nawet jeśli wszystko było sprawne, program przestawał obsługiwać podzespoły, wymuszając naprawę.

{% include info.html
type="Heheszki"
text="Kod zawierał błąd -- działał tylko wówczas, gdy *jednocześnie* dzień miesiąca był równy co najmniej 21, a&nbsp;miesiąc 11 (czyli był listopadem albo grudniem).  
W związku z&nbsp;tym, zamiast stawać na amen po 21.11, pociągi zawieszały się na ostatnie 9-10 dni listopada i&nbsp;grudnia. A&nbsp;wraz z&nbsp;nadejściem Nowego Roku następował cud i&nbsp;się włączały."
%} 

Newag, obwiniony o&nbsp;nieuczciwe działania, zareagował publicznym oburzeniem. Obwiniali atak hakerski, grozili pozwami ekipie DS. W&nbsp;social mediach pojawiły się również konta broniące ich działań, wyglądające jak typowe trolle internetowe.

Ogólnie: czyste aferkowe złoto :smile: Koniecznie muszę dodać tę sprawę do swojej serii [„Cyfrowy feudalizm”](/serie/cyfrowy_feudalizm){:.internal}, bo doskonale tam pasuje. Ale to już w&nbsp;przyszłym roku. Do tego czasu polecam garść innych źródeł:

<details class="bigspace">
<summary><strong>Źródła opisujące aferę (kliknij, żeby rozwinąć)</strong></summary>
<ul>
  <li>
    <p><a href="https://zaufanatrzeciastrona.pl/post/tag/newag/">Artykuły</a> Zaufanej Trzeciej Strony spod tagu <code class="language-plaintext highlighter-rouge">newag</code>.<br />
Przystępne i&nbsp;obszerne opisy całej afery. Nagłośnili ją jako jedni z&nbsp;pierwszych.</p>
  </li>
  <li>
    <p><a href="https://youtu.be/Mv2fWyiPWpM">Film Mateusza Chroboka</a>.<br />
Jeśli ktoś woli formę filmową, to tu znajdzie fajne omówienia. W&nbsp;komentarzach ekipa z&nbsp;DS odpowiada na parę pytań użytkowników.</p>
  </li>
  <li>
    <p><a href="https://media.ccc.de/v/37c3-12142-breaking_drm_in_polish_trains">Prezentacja</a> grupy Dragon Sector na konferencji Chaos Computer Club.</p>
  </li>
  <li>
    <p><a href="https://gynvael.coldwind.pl/?id=777">Artykuł</a> Gynvaela Coldwinda.<br />
Opisuje, na ile wiarygodne są tłumaczenia firmy, jakoby to obcy hakerzy dodali złośliwy kod.</p>
  </li>
  <li>
    <p><a href="https://nitter.cz/Zaufana3Strona/status/1734199429194731561#m">Tweety Zaufanej Trzeciej Strony</a>.<br />
Tutaj z&nbsp;kolei przybliżenie wątku dziwnych kont, które pojawiły się po prasowych doniesieniach.</p>
  </li>
  <li>
    <p><a href="https://news.ycombinator.com/item?id=38788360">Dyskusje na forum Hacker News</a>.<br />
Tu z&nbsp;kolei można poznać opinie międzynarodowej społeczności. Linkuję najnowszą dyskusję, w&nbsp;jednym z&nbsp;komentarzy są linki do wcześniejszych.</p>
  </li>
  <li>
    <p><a href="https://wiadomosci.onet.pl/kraj/skandal-na-kolei-pociag-newagu-stanal-bo-znowu-nadszedl-21-grudnia/41mdspf">Artykuł Onetu</a> z&nbsp;21 grudnia.<br />
Wiedząc o&nbsp;złośliwym kodzie, zainteresowani czekali na dzień 21&nbsp;grudnia, kiedy to miała się włączyć blokada zależna od daty. I&nbsp;faktycznie tak się stało.</p>
  </li>
</ul>
</details>



Pomijając dystopijne aspekty tej afery -- nawet podstawowa infrastruktura może być na łasce chciwych osób z&nbsp;palcami na pstryczkach -- widzę w&nbsp;niej również jasne strony.

Bo teraz **przeciwnicy centralizacji zyskali coś, co można nazwać _argumentum ad Newagum_**.

Sprawa nasza, polska. Głośna, ale przyziemna i&nbsp;dość zrozumiała. „Psuli pociągi, żeby naprawiać tylko u&nbsp;nich”. „Ludzie nie mogli dojechać do pracy, bo producent wyłączył sprzęt”.  
To już nie jakieś egzotyczne drukarki czy smartfony Apple'a, których mało kto używa. To coś namacalnego, nieuczciwego, osłabiającego niejako cały kraj.

To sprawa, do której często można się od teraz odwoływać w&nbsp;internetowych dyskusjach. Uświadamiając ludzi, że wprowadzanie wszędzie komputerów, czujników i&nbsp;łączności z&nbsp;siecią nie zawsze jest postępem. Że w&nbsp;kwestii trwałości i&nbsp;niezależności bywa wręcz regresem.

### Google kontra blokery śledzenia

Google gości na tym blogu często; ma nawet [osobną serię poświęconą swoim przewinieniom](/serie/google){:.internal}. Stale rosnącą (a&nbsp;byłaby kilka razy dłuższa, gdybym nie był leniwy -- mam stosik napoczętych wpisów).

Wujek G&nbsp;zarabia na reklamach, więc to im podporządkowuje swoje produkty, szczególnie przeglądarkę Chrome. To żadna nowość. Ale w&nbsp;tym roku przeszli samych siebie pod względem zmian i&nbsp;propozycji uderzających w blokery reklam śledzących.

Wcześniej planowali wprowadzić w&nbsp;tym roku [Manifest v3]({% post_url 2022-05-11-google-manifest-v3 %}){:.internal}.

Byłaby to zmiana sposobu, w&nbsp;jaki dodatki do przeglądarek mogą wchodzić w&nbsp;interakcje z&nbsp;Chrome'em, przeglądarką od Google'a.  
Ale że wiele przeglądarek z&nbsp;tego kodu korzysta, to zmiana mogłaby sięgnąć dużo dalej. Taki np. Edge od Microsoftu również planował przyjąć cały kod bez zmian.

Sam fakt, że mogą zajść zmiany, to pół biedy. Gorzej, że **byłyby to zmiany na gorsze, osłabiające dodatki blokujące**. Ograniczające między innymi liczbę złożonych regułek, których używają dodatki do blokowania skryptów od firm reklamowych, profilujących użytkowników i&nbsp;gromadzących ich dane. 

Po intensywnych protestach Google odstąpił od pomysłu. Ale latem tego roku przedstawili nowy, znacznie gorszy. [Web Environment Integrity, w&nbsp;skrócie WEI]({% post_url 2023-07-29-web-environment-integrity %}){:.internal}.

Właściciele stron internetowych mogliby wysyłać, poprzez przeglądarkę, zapytania „w głąb systemu”. A&nbsp;konkretniej: do odizolowanych chipów, które lubię nazywać enklawami. Wiele urządzeń obecnie zawiera takie coś.

Treść pytania: „czy ten system to system fabryczny, bez żadnych modyfikacji?”.  
Enklawa zawsze odpowie prawdę. Ani użytkownik, ani żaden program nie ma do niej dostępu. Odpowiedzi się nie sfałszuje, bo enklawa podpisuje ją cyfrowo. Narzędzie do podpisów ukrywa w&nbsp;sobie, niedostępne dla użytkowników.  
A&nbsp;właściciele stron proszący o&nbsp;taką weryfikację będą wiedzieli, jak powinien wyglądać podpis. I&nbsp;nie przyjmą innego.

Jednym zdaniem -- **koniec gry dla hobbystów modyfikujących swój system, jeśli jakaś firma zechce wpuszczać tylko „normalsów”**. A&nbsp;wiele mogłoby to zrobić, bo WEI umożliwia wprowadzenie takiej selekcji w&nbsp;sposób prosty, w&nbsp;kilku linijkach kodu. Pojawiło się ryzyko, że otwarty internet zostanie pocięty licznymi ogrodzeniami. 

Wybuchły jeszcze intensywniejsze protesty niż przy Mv3. Google ogłosił publicznie, że wycofuje się z pomysłu. Ale krótko potem [odkurzyli pomysł Manifestu v3](https://developer.chrome.com/blog/resuming-the-transition-to-mv3/).

...Co więcej, ostro uderzyli w&nbsp;blokowanie reklam na swojej platformie YouTube. Zaczęli każdego dnia zmieniać po kilka razy strukturę strony. Nawet najskuteczniejsze dodatki blokujące nie są w&nbsp;stanie nadążyć.  
W dodatku ludziom korzystającym z&nbsp;blokerów zaczęli wyświetlać komunikat ostrzegawczy mówiący, że po kilku wykryciach dodatku blokującego nastąpi ban konta.

Końca nie widać, ofensywa trwa.

### Google kontra Departament Sprawiedliwości

W tym roku odbyły się przesłuchania w&nbsp;sprawie, w&nbsp;której Google jest oskarżany o&nbsp;działania monopolistyczne i&nbsp;nieuczciwą konkurencję.

Takie procesy, niezależnie od werdyktów, bywają cennym źródłem informacji. Na widok publiczny trafiają różne korporacyjne maile i&nbsp;dokumenty, czasem zawierające mocno obciążające dowody.

{% include info.html
type="Powiązane wpisy"
text="Google nie jest pierwszą korporacją na tym blogu, której machlojki zostały ujawnione podczas rozprawy sądowej.  
Opisywałem już wcześniej brudy, jakie wypłynęły w&nbsp;przypadku potentatów rolniczych: [Syngenty](/2022/07/27/syngenta-atrazyna#walka-zsyngentą){:.internal} oraz [Monsanto](/2022/12/24/monsanto-posilac-roundup#walka-ziarc){:.internal}. Na jaw wyszło nękanie badaczy i&nbsp;publiczne ośmieszanie ich na rzekomo niezależnych stronkach, nakłanianie „swojej” dziennikarki do promowania firmowej wizji i&nbsp;nasyłanie trolli na „obcą”."
%}

A wracając do sprawy Google'a -- na ich temat również wypłynęły ciekawe fakty:

* Ich status domyślnej wyszukiwarki na wszelakich telefonach (Samsungach, iPhone'ach...) nie wynikał wyłącznie z&nbsp;jakości.  
  Po prostu [zapłacili za ten przywilej](https://www.cnbc.com/2023/10/27/google-paid-26-billion-in-2021-to-become-a-default-search-engine.html) dziesiątki miliardów dolarów, budując nieprzekraczalną fosę między sobą a&nbsp;konkurencją.

* Ekipa tworząca przeglądarkę Chrome czasem [celowo ją pogarszała]({% post_url 2023-10-05-antymonopol-chrome-reklamy %}){:.internal} na życzenie działu reklam internetowych.

  Rozważali na przykład usunięcie szybkich podpowiedzi z&nbsp;górnego paska, żeby zagonić ludzi do wyszukiwarki. Poza tym przesunęli na samą górę te podpowiedzi z&nbsp;historii, które odsyłały do *google.com*, a&nbsp;nie prosto do stron źródłowych.  
Dlaczego? Bo dział reklam prosił. Odwiedziny na *google.com* nabijają im statystyk, komfort użytkownika drugorzędny.

Przesłuchania już się skończyły, teraz sąd zaczął analizować dowody. W&nbsp;przyszłym roku ogłosi werdykt. Istnieje możliwość, że firma Google zostanie uznana za monopolistę ubijającego całe firmowe ekosystemy w&nbsp;zarodku. I&nbsp;rozbita na mniejsze, niezwiązane ze sobą działy.


### Zablokowanie przejęcia Figmy przez Adobe

Rok temu [wspomniałem w&nbsp;podsumowaniu]({% post_url 2022-12-31-podsumowanie-2022-roku %}#kupno-figmy-iaferki-wokół-adobe){:.internal} o&nbsp;tym, że Adobe -- gigant od programów do tworzenia treści wszelakich -- nabył za 20&nbsp;miliardów dolarów Figmę. Młodszą, dynamiczną konkurencję.

Wiele osób widziało w&nbsp;Figmie właśnie odskocznię od monopolisty, szansę na alternatywę. Pokładali w&nbsp;niej nadzieję. Ale kiedy Adobe sięgnęło do swoich głębokich kieszeni, to skończyło się konkurowanie.

...Albo i&nbsp;nie? Niedawno antyfani monopoli i&nbsp;centralizacji dostali prezent na Mikołaja. Firmy jednak [porzuciły pomysł połączenia](https://www.figma.com/blog/figma-adobe-abandon-proposed-merger/), czując że nijak nie obejdą przepisów antymonopolowych. Adobe pożarło świat, ale jednak ostała się jakaś wysepka konkurencji.

{:.bigspace}
>  despite thousands of hours spent with regulators (...), we no longer see a&nbsp;path toward regulatory approval of the deal.

Choć Figma wraca do gry, podtrzymuję swoje zdanie z&nbsp;poprzedniego wpisu. Dla zwykłych użytkowników sposobem na niezależność od gigantów nie jest stawianie na mniejsze, drapieżne startupy pompowane przez *venture capital*. **Na dłuższą metę one same chcą zostać gigantami. Albo chociaż im się oddać**.

Pewniejszą alternatywą są programy *open source*. Że co, że gorsze i&nbsp;„nieprofesjonalne”? To można podzielić się na różnych forach rzetelnymi uwagami. Może autorzy poprawią niedoskonałości.  
Poza tym takie programy, choć czasem toporne, nie usunęły użytkownikom tysięcy zdjęć. Chmura Adobe -- ponoć *appropriate* i&nbsp;*professional* na sto pro -- [usunęła](https://www.theverge.com/2020/8/20/21377411/adobe-lightroom-ios-ipados-app-update-pictures-photos-presets-deleted) :roll_eyes:

## Zakusy rządzących

W tym roku nie tylko korporacje uderzały w&nbsp;ludzką wolność i&nbsp;prywatność. Wypłynęło również parę dziwnych inicjatyw ze strony instytucji unijnych.

Nim je przybliżę, nieco kontekstu -- **osobiście jestem przychylny Unii Europejskiej i&nbsp;uważam, że robią sporo dobrego, nieraz stawiając opór gigantom**. Nigdy tej przychylności nie ukrywałem i&nbsp;jest częstym motywem w&nbsp;moich wpisach.

Przykład tego oporu? Ich [DMA (Digital Markets Act)](https://en.wikipedia.org/wiki/Digital_Markets_Act) wreszcie nazywa rzeczy po imieniu -- „*big tech* to osobna kategoria. Są bardziej wrośnięci w&nbsp;życie ludzi niż zwykłe firmy. Dlatego będą traktowani inaczej”.  
Jak dla mnie -- powiew świeżości po bezsensownym wtłaczaniu mikrobiznesów i&nbsp;megakorpo w&nbsp;jedne i&nbsp;te same ramy!

Ale...

Mimo całej swojej sympatii nie mogę być ślepy na działania niektórych instytucji. Czy to przez naciski lobbystów, czy to przez czyjeś niezrozumienie cyfrowych spraw -- czasem próbują przepchnąć rzeczy, które byłyby zwyczajnie szkodliwe dla prywatności i&nbsp;swobód obywatelskich.

### Kontrola czatów

Ten pomysł przybył od amerykańskiej organizacji Thorn. W&nbsp;Europie promowała go Ylva Johansson z&nbsp;Komisji Europejskiej, rzekomo w&nbsp;celu ochrony dzieci przed wykorzystaniem.

Według proponowanych przepisów na każdy komunikator (jak Signal, WhatsApp...) nałożony zostałby obowiązek analizowania treści -- przez algorytmy, nie ludzi. Gdyby algorytm wykrył próby wykorzystania nieletnich, to powinien zawiadomić odpowiednie osoby.

Brzmi szlachetnie? Również pod kątem prywatności ciut lepiej niż dawniejsze sugestie -- bo te postulowały wprowadzenie furtek specjalnie dla rządów, wgląd do *całości* komunikacji.  
Ale lepszy zły pomysł nadal jest zły. Streszczając [mój wpis o&nbsp;kontroli czatów]({% post_url 2023-10-19-chat-control %}){:.internal}:

* Automaty są zawodne.

  Nawet przy zwykłym rozpoznawaniu obrazu zdarzają się wpadki. Przy sprawach subtelniejszych, jak wykrywanie w&nbsp;tekście prób *groomingu* -- tym bardziej. A&nbsp;stawką pomyłki jest tutaj wezwanie na komendę. Nawet jeśli sprawa szybko się wyjaśni, plotki mogą pójść w&nbsp;świat.

* Kto chce, ten łatwo obejdzie ograniczenia.

  Nic nie stoi na przeszkodzi, żeby szybko i&nbsp;łatwo szyfrować pliki w&nbsp;innym programie. A&nbsp;do komunikatorów wrzucać tylko wersję wcześniej zaszyfrowaną. I&nbsp;już, cały system nieskuteczny.

* W&nbsp;przyszłości może dojść do nadużycia systemu.

  „Hej, a&nbsp;może dodamy też skrypty wykrywające treści terrorystyczne?”. „Hej, a&nbsp;może antyrządowe?”. „Hej, w&nbsp;sumie ci dziennikarze piszący o&nbsp;przekrętach władzy to też tacy terroryści. Może jeszcze jakiś filtr na nich?”.

Wisienką na torcie był fakt, że Komisja Europejska wykupiła w&nbsp;internecie reklamy ocieplające pomysł w&nbsp;oczach opinii publicznej. Ale jednocześnie **ustawili, żeby reklamy te nie wyświetlały się grupom skłonnym do sprzeciwu**. Osobom obserwującym określone konta i&nbsp;hasztagi.  
Wśród wykluczonych grup byli nie tylko sympatycy antyunijnych polityków. Najbardziej zszokowało mnie to, że [umieszczono tam](https://noyb.eu/en/noyb-files-complaint-against-eu-commission-over-targeted-chat-control-ads) obserwatorów hasztagu `#Qatargate`. Dotyczącego całkiem realnej, niespiskowej afery korupcyjnej.

Streszczając: Komisja promowała w&nbsp;Europie pomysł z&nbsp;USA, raczej nieskuteczny przeciw przestępcom, ale uderzający w&nbsp;swobodną komunikację. Robiła to chyłkiem, wykluczając tę część społeczeństwa, która mogłaby protestować. Mamy autorytarne bingo? :roll_eyes:

W swoim wpisie wyraziłem nadzieję, że Parlament Europejski postawi się Komisji. I&nbsp;choć sam nie jest wolny od skandali (przykładem wspomniana aferka z&nbsp;Katarem), jest spora szansa na to, że [proponowane prawo nie przejdzie](https://tuta.com/blog/chat-control-criticism).

### Artykuł 45&nbsp;i zaufanie regulowane ustawą

Poza kontrolą czatów promowano też wersję drugą [eIDAS](https://en.wikipedia.org/wiki/EIDAS), przepisów regulujących kwestię cyfrowych dokumentów (pozwalających załatwiać więcej spraw elektronicznie).  
Proponowana wersja druga -- zasugerowana tym razem nie przez Komisję, lecz przez Radę Unii Europejskiej -- zawierała niepokojący [artykuł 45](https://www.eff.org/deeplinks/2023/11/article-45-will-roll-back-web-security-12-years). Żeby zrozumieć zagrożenie, przyda się nieco kontekstu.

Współczesny internet opiera się na szyfrowaniu. Gdy odwiedzamy stronę zaczynające się od `https://`, to nikt nie odczyta danych wymienianych między nami a&nbsp;stroną.  
Można powiedzieć, że wymieniamy się otwartymi kłódkami z&nbsp;serwerem, na którym jest strona. A&nbsp;potem wysyłamy sobie różne rzeczy w&nbsp;pancernych pudłach zamkniętych na te kłódki. 

Ale cały ten system byłby nieszczelny, gdyby wszystkie kłódki były sobie równe.  
Ktoś mógłby stanąć na drodze, między internautami a&nbsp;stronami, i&nbsp;przechwytywać wysyłane kłódki, po czym je podmieniać na takie, do których ma klucz. Po cichu, nie budząc niczyjego niepokoju -- bo nie zmieniałby niczego w&nbsp;samych danych.

Z tego względu każda przeglądarka zawiera w&nbsp;sobie listę „zaufanych producentów kłódek”.  
Mogą się na niej znaleźć tylko wybrane, wyspecjalizowane organizacje. Kiedy ktoś wysyła kłódkę, chcąc szyfrowanej wymiany, to oznacza je certyfikatem od takiego zaufanego producenta, uzupełniając własnym.  
Przeglądarka drobiazgowo analizuje łańcuszek certyfikatów i&nbsp;porównuje ze swoją listą. Jeśli coś jest nie tak, to wyświetla ostrzeżenie.

I tu właśnie wchodzi artykuł 45&nbsp;nowych przepisów -- **nakładałby na twórców przeglądarek obowiązek ufania certyfikatom od określonych organizacji**.  
Gdyby nowe przepisy weszły w&nbsp;niezmienionym kształcie, a&nbsp;przeglądarki by posłuchały, to instytucje „dodane ustawą” -- jeśli tylko by zechciały i&nbsp;zyskały wsparcie firm telekomunikacyjnych -- mogłyby zacząć przechwytywać wysyłane dane, odszyfrowywać je i&nbsp;odczytywać na wielką skalę.

Bubel prawny czy próba celowego nadużycia? Niezależnie od przyczyny, to niepokojąca sprawa. Nagłaśniana przez całkiem znane organizacje, nie tylko niszowe Ciemne Strony. Między innymi przez podlinkowane wyżej EFF i Mozillę od Firefoksa, na stronce [*Last Chance for eIDAS*](https://last-chance-for-eidas.org/). 

{% include info.html
type="Porada"
text="Gdyby ktoś chciał zapamiętać, jak odróżnić eIDAS od kontroli czatów -- to pierwsze dotyczy przeglądarek ogólnego przeznaczenia. To drugie -- komunikatorów, czyli konkretnej kategorii aplikacji."
%}

## Co w&nbsp;2024 roku?

W przyszłym roku szczególnie ciekawi mnie werdykt w&nbsp;sprawie przeciw Google'owi. Czy zostanie rozbity na zbiór mniejszych firm, robiąc wreszcie miejsce dla zdrowszej konkurencji?  
Że tak zacytuję *Forever Young*, słowa z&nbsp;początku piosenki:

{:.bigspace}
> hoping for the best, but expecting the worst...

W każdym razie walka na pewno będzie trwała. Lobbyści, PR-owcy i&nbsp;politycy, czasem ramię w ramię, nie przestaną napierać, jojczeć że ich firmom jest źle, manipulować, szeleścić banknotami.

„Europko, zdejmij mnie te ograniczenia”.  
„Europko, wprowadź ostrzejsze przepisy (żebym tylko ja je spełniał)”.  
„Pani Polsko, nie chce pani kupić tego doskonałego garnka? Za jedyne kilkanaście miliardów!”.  
„Obywatele! Chodźcie pod lupę dla własnego bezpieczeństwa”. 

Ze swojej strony planuję przede wszystkim przebić barierę 100 wpisów, jest już całkiem blisko! Poza tym planuję nagłośnić parę kwestii wokół takiej propagandy jak ta wyżej. Ale nic więcej nie powiem.

Póki co -- życzę owocnego przywitania nowego roku! :smile: Oby lepsze strony tego mijającego przeniosły się na kolejny, a&nbsp;gorsze zostały w&nbsp;przeszłości.

{:.bigspace-before}
<img src="/assets/posts/podsumowania/2023/2023-podsumowanie.jpg" alt="Kadr z&nbsp;filmu World War Z, pokazujący armię zombie próbującą przeskoczyć z&nbsp;autobusu na helikopter. Autobus jest podpisany 2023, zombie to 'Problemy roku 2023', a&nbsp;helikopter to 2024." />

{:.figcaption}
Źródło: kadr z&nbsp;filmu *World War Z*, znaleziony w&nbsp;internecie.
