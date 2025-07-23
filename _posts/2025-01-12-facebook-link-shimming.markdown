---
layout: post
title: "Podstawione linki Facebooka"
subtitle: "Mały klik dla człowieka, wielki wgląd w życie ludzkości."
description: "Mały klik dla człowieka, wielki wgląd w życie ludzkości."
date:   2025-01-12 15:13:10 +0100
tags: [Inwigilacja, Porady]
firmy: [Facebook]
category: facebook_dane
category_readable: "Kochajmy się jak bracia, analizujmy się jak Facebooki"
image:
  path: /assets/posts/inwigilacja/fb_link_shimming/facebook-link-shimming-baner.jpg
  width: 1200
  height: 700
  alt: "Zdjęcie ryby żabnicy. Na końcu jej wabika widać link do Youtube'a, a tuż za paszczą logo Facebooka."
---

Facebook nie należy do czołówki uwielbianych portali. Przez kilka lat narażał się jednej stronie politycznej, teraz zmienił front i&nbsp;naraża się drugiej. Zaś powszechność automatycznie generowanego spamu to czynnik odstraszający niezależnie od polityki.

Dorzucę do tego tygla jeszcze inną kontrowersję, na tle prywatnościowym.  
Mianowicie: w&nbsp;momencie kliknięcia w&nbsp;niektóre linki na stronie *facebook.com* dochodzi do ich podmiany na takie, które **dają Facebookowi pełniejszy wgląd w&nbsp;nasze zachowania, a&nbsp;także możliwość wybiórczej cenzury**.

To istotne rozwinięcie metod, które dotąd opisywałem -- do tradycyjnych parametrów śledzących doszły przekierowania przez stronę zależną, a&nbsp;nawet maskowanie całej akcji przez kod JavaScript. Facebook poszedł na całość w&nbsp;kwestii użytych sztuczek.

Dzięki temu ich linki są wdzięcznym obiektem do analizy. Podsumuję różne metody, jakie zostały w&nbsp;nich wykorzystane i&nbsp;pokażę, jak się ochronić. W&nbsp;sposób, mam nadzieję, zrozumiały dla wszystkich.  
Zapraszam!

{:.post-meta .bigspace-after}
Ku swojemu zdziwieniu znalazłem artykuły sugerujące, że ta metoda jest na Facebooku od dawna. Z&nbsp;jakiegoś powodu nie miałem z&nbsp;nią wcześniej styczności (choć kopiowałem linki).  
W każdym razie, stara czy nowa -- bez znaczenia. Pokonamy ją. 

<img src="/assets/posts/inwigilacja/fb_link_shimming/facebook-link-shimming-baner.jpg" alt="Zdjęcie ryby żabnicy. Na końcu jej wabika widać link do Youtube'a, a&nbsp;tuż za paszczą logo Facebooka."/>

{:.figcaption}
Źródło: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Representatives_of_ceratioid_families.jpg), na podstawie artykułu Masaki Miya i&nbsp;in. Przeróbki moje.

## Spis treści

* [Praktyczny przykład](#praktyczny-przykład)
* [Szpiegolinki krok po kroku](#szpiegolinki-krok-po-kroku)
  * [Dyskretna podmiana linków](#dyskretna-podmiana-linków)
  * [Przechwytywanie przez Facebooka](#przechwytywanie-przez-facebooka)
  * [Parametry śledzące](#parametry-śledzące)
* [Jak to obejść?](#jak-to-obejść)

## Praktyczny przykład

Na początek można sobie otworzyć na komputerze, w&nbsp;ogólnej przeglądarce, stronę *facebook.com* (musi być strona, a&nbsp;nie aplikacja, bo ta działa inaczej).

Tam trzeba znaleźć jakiś link prowadzący **do strony zewnętrznej, poza Facebooka**. Może być na przykład [ten losowy](https://www.facebook.com/ZaufanaTrzeciaStrona/posts/pfbid0eBdNwuiLds7mhJivGuKo4wcQQ3Z4KGcXoWB2iMSSYWh5Y4DBKGenTfzrxcwXD5FVl) z&nbsp;Zaufanej Trzeciej Strony. Linkujący do prezentacji o&nbsp;nieaktywności Fejsa w&nbsp;sprawie powszechnych oszustw. Kolejna ciekawa patologia, gdyby komuś nie wystarczyły linki śledzące :wink:

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/fb_link_shimming/z3s-post-facebook-link.jpg" alt="Screen posta facebookowego Zaufanej Trzeciej Strony, w&nbsp;którym linkują do filmu na temat oszustw na Facebooku" width="70%"/>

A wracając do linków -- w&nbsp;treści posta znajduje się link do YouTube'a, widoczny w&nbsp;całości:

<pre class="black-bg mono">
https://www.youtube.com/watch?v=AastpuFMHEU
</pre>

Jeśli po raz pierwszy najadę na niego myszką (nie klikając), to przeglądarka wyświetli w&nbsp;lewym dolnym rogu ekranu, dokąd on prowadzi.  
Co ciekawe, będzie wyglądał ciut inaczej niż ten z&nbsp;posta. Będzie dłuższy, wzbogacony o&nbsp;parametr śledzący `fbclid`. Dodam dla jasności: dodany przez Facebooka, a&nbsp;nie Z3S.

<pre class="black-bg mono">
https://www.youtube.com/watch?v=AastpuFMHEU<span class="red">&fbclid=DUŻO_ZNAKÓW</span>
</pre>

...Tylko że ten parametr to stare dzieje, w&nbsp;światku prywatnościowym jest dobrze znany. [Również na tym blogu]({%post_url 2022-09-14-facebook-linki-trackery %}#linki-do-stron-zewnętrznych){:.internal}. Gdyby to tylko o&nbsp;niego chodziło, to nie byłoby tutaj nic ciekawego.

Ciekawiej robi się natomiast, jeśli klikniemy na link z&nbsp;posta prawym przyciskiem myszy. Wybierzemy opcję `Kopiuj odnośnik` (albo *link*, albo coś podobnego). A&nbsp;następnie wkleimy skopiowany link do Notatnika lub innego programu:

<div class="bigspace black-bg mono">
<span style="color:#964fa0">https://l.facebook.com/l.php?u=</span>https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAastpuFMHEU<span class="red">%26fbclid%3DDUŻO_ZNAKÓW</span><span style="color:#964fa0">&h=TEŻ_DUŻO_ZNAKÓW&__tn__=-UK-R&c[0]=ZNÓW_DUŻO_ZNAKÓW</span>
</div>


Ależ się zmienił! Jest teraz naszpikowany paroma rzeczami, które umożliwiają wzmożone gromadzenie danych. Omówię je krok po kroku.

<details class="framed">
<summary><strong>Sprawdzanie linków na smartfonie</strong></summary>

<p>Na telefonie może być trudniej sprawdzić działanie linków, bo Facebook przegania użytkowników urządzeń mobilnych na aplikację (gdzie ma większe możliwości zbierania danych). A&nbsp;kiedy jesteśmy w&nbsp;aplikacji, to nie ma opcji kopiowania linków. Przytrzymanie na którymś z&nbsp;nich palca po prostu go otwiera.</p>

<p class="post-meta bigspace-after">Dodam przy okazji, że w&nbsp;obrębie samej aplikacji Facebook nawet nie musiałby stosować podmiany linków. I&nbsp;tak widzi więcej. Po kliknięciu w&nbsp;link do strony zewnętrznej apka Facebooka otwiera bowiem <a href="" class="internal">fałszywą przeglądarkę</a>. Wygląda to tak, jakbyśmy przeszli do szerszego internetu. A&nbsp;w rzeczywistości nadal tkwimy wewnątrz apki Facebooka (która może dodawać od siebie kod śledzący).</p>

<p>Łatwiej po prostu sprawdzić wszystko na kompie. Ale jeśli ktoś ma tylko smartfona, to można zrobić tak:</p>

<ul>
  <li>otworzyć przeglądarkę (Firefox, Chrome itd.),</li>
  <li>wejść w&nbsp;ustawienia i&nbsp;wybrać opcję <code class="language-plaintext highlighter-rouge">Wersja na komputery</code>,</li>
  <li>odwiedzić <em>facebook.com</em> (powinna się teraz wyświetlić pełna wersja strony, ciut za duża na ekran mobilny),</li>
  <li>znaleźć link, przytrzymać na nim palec i&nbsp;wybrać opcję skopiowania.</li>
</ul>
</details>

## Szpiegolinki krok po kroku

### Dyskretna podmiana linków

Zanim w&nbsp;ogóle zagłębimy się w&nbsp;budowę linku, może nas ciekawić fakt, że po skopiowaniu dostaliśmy coś innego niż wskazywała przeglądarka.

I nie była to zwykła, banalna niezgodność tekstu z&nbsp;linkiem (jak wyżej w&nbsp;tym wpisie, pod słowami „ten losowy”). W&nbsp;takim wypadku nadal istniałaby zgodność między tym, co pokazuje przeglądarka w&nbsp;rogu, a&nbsp;docelową lokalizacją. Tutaj ta zgodność zanikła.

Wniosek? **Link przed kliknięciem prowadził w&nbsp;inne miejsce niż po kliknięciu. Facebook go podmienił**.

A na taką podmianę jest (chyba) tylko jeden sposób -- [JavaScript]({%post_url 2022-05-02-javascript1 %}){:.internal}. Bardzo popularny język programowania, który ma niemalże monopol w&nbsp;internecie i&nbsp;jest obecny na większości współczesnych stron.  
W domyśle ma być używany do nieco przyjaźniejszych celów. Jak nadanie stronom pewnej interaktywności, ładowanie elementów na bieżąco w&nbsp;miarę przewijania strony... Ale, ze względu na wgląd w&nbsp;wiele funkcji przeglądarki, szybko stał się narzędziem profilowania.

Pod różne elementy strony -- również linki -- da się podpinać *funkcje*. Kod, który uruchomi się w&nbsp;momencie jakiegoś działania. Coś w&nbsp;tym stylu (zapisane pseudokodem):

```
link_X -> po_kliknięciu:
    nowy_link = podmień_link( link_X )
    link_X = nowy_link
```

Link domyślnie prowadzi w&nbsp;miejsce A, co pokazuje przeglądarka. Ale po kliknięciu aktywuje się regułka podmieniająca, zmieniając lokalizację na B.  
Podmianka nosi oficjalnie nazwę [*link shimming*](https://www.glew.io/articles/what-are-facebook-link-shims-and-how-do-they-affect-your-data). Jest wredna... ale sama w&nbsp;sobie daje tylko maskowanie, a&nbsp;nie zbieractwo danych. To dopiero będzie.

### Przechwytywanie przez Facebooka

Pierwszym, co rzuca się w&nbsp;oczy w&nbsp;nowym linku, jest jego początek. Już nie `www.youtube.com`, tylko `l.facebook.com`. Inny trzon strony, czyli *domena*, oznacza jedno -- **link nie prowadzi do YouTube'a, tylko do innej strony Facebooka**. Nasz docelowy link, w&nbsp;nieco zmienionej postaci, został wepchnięty gdzieś w&nbsp;głąb tego nowego.

> Ale przecież jak w&nbsp;niego kliknę, to przejdzie do YouTube'a!

Owszem, ale nie od razu. Najpierw przeglądarka poprosi `l.facebook.com` o&nbsp;zawartość tkwiącą pod danym linkiem. W&nbsp;odpowiedzi dostanie [przekierowanie]({%post_url 2021-03-26-internetowa-inwigilacja-3-przekierowania %}){:.internal}, czyli instrukcję mówiącą, żeby teraz poprosiła `youtube.com` o&nbsp;odpowiednią stronkę.

{% include info.html
type="Inni winowajcy"
text="Przekierowania w&nbsp;żadnym razie nie są unikalną cechą Facebooka. Występują również na YouTubie, do tego od niepamiętnych czasów na Twitterze (skracarka `t.co`; opisana zresztą we wpisie z&nbsp;linku wyżej).  
Facebook wyróżnia się natomiast na niekorzyść tym, że podmienia linki. Na Twitterze występuje niezgodność między linkiem w&nbsp;treści a&nbsp;linkiem faktycznym... Ale przynajmniej wchodzimy w&nbsp;to, co pokazuje przeglądarka w&nbsp;dolnym rogu. Bez niespodzianek."
%}

Przekierowanie pozwala obejść typowe zachowanie przeglądarki.  
Normalnie, po kliknięciu w&nbsp;link, od razu prosi ona o&nbsp;nową stronę, zaś strony obecnie wyświetlanej o&nbsp;tym nie informuje.  
Ale kiedy tą „nową stroną” zostaje podpucha Facebooka, to mogą łatwo przechwycić brakującą informację: „mój użytkownik A&nbsp;właśnie kliknął w&nbsp;link do strony Y”.

#### Zastosowanie śledzące

W ten sposób Facebook może **monitorować, w&nbsp;skali pojedynczych osób i&nbsp;całych populacji, klikanie w&nbsp;linki**.

Na poziomie społeczeństw będą widzieli, co jest na czasie, co rośnie w&nbsp;siłę. Już kiedyś w podobny sposób (tyle że przez [aplikację Onavo](https://cyberdefence24.pl/vpn-onavo-protect-od-facebooka-zbiera-informacje-o-uzytkownikach), stającą na drodze przepływu danych w&nbsp;smartfonie) wyłapali zawczasu, że WhatsApp wyrasta na konkurencję dla ich Messengera. Po czym go kupili.

Na poziomie jednostek będą mogli z&nbsp;kolei jeszcze lepiej widzieć, co kogo interesuje. Już wcześniej Facebook widział:

* jakie fanpejdże, profile itd. odwiedzamy w&nbsp;obrębie ich platformy,
* jakie strony *zewnętrzne* odwiedzamy -- ale tylko jeśli zaszła któraś z&nbsp;dwóch rzeczy:

  * właściciele tych stron dobrowolnie dodali do siebie [element śledzący]({%post_url 2021-12-08-cookies-piksele-sledzace %}){:.internal} Facebook Pixel,
  * używaliśmy apki Facebooka.  
    Apka otwiera bowiem linki we własnej [podstawionej przeglądarce]({%post_url 2023-08-08-wbudowane-przegladarki %}){:.internal}, więc zachowuje wgląd w&nbsp;odwiedzone treści.

Przekierowania uzupełniają lukę, martwe pole w&nbsp;ich przenikliwym wzroku. Widzą dzięki nim również odwiedziny na cudzych stronach wykonane przez ogólną przeglądarkę, a&nbsp;nie apkę. Nawet jeśli te strony nie dodały u&nbsp;siebie FB Pixeli.

...Ale czy nie mogli tego osiągnąć w inny sposób? Ktoś mógłby zapytać:

{:.bigspace}
> A&nbsp;po co przekierowanie? Skoro JavaScript i&nbsp;tak się uruchamia w&nbsp;momencie kliknięcia w&nbsp;link, to nie mógłby po prostu wysłać Facebookowi informacji, że to zrobiliśmy?

Sensowne pytanie! JavaScript jak najbardziej może przesyłać informacje.  
Nie wydaje się to również jakimś większym obciążeniem dla Facebooka -- danych do wysłania jest mało. ID użytkownika plus ID klikniętego linku, tyle. Do tego nie byłoby to słane jakoś nagminnie na tle innych działań, jak przewijanie strony.

...A jednak mamy przekierowania. Być może jest coś, co mi umyka. Jakaś techniczna cecha ich infrastruktury, która zniechęca do śledzenia kliknięć przez JS-a.

#### Zastosowanie cenzorskie

Możliwe również, że wybrali akurat przekierowania ze względu na ich drugą zdolność --  **umożliwiają łatwą cenzurę wybranych stron**.

Jak wspomniałem, normalny link byłby sprawą ściśle między naszą przeglądarką a&nbsp;stronką, do której tenże link prowadzi. Klikamy, przeglądarka prosi o&nbsp;stronę spod linku, ładuje jej zawartość. Zero udziału Fejsa.  
Ale teraz Facebook dosłownie wstawia się między nas a&nbsp;stronkę. I&nbsp;może umieścić na `l.facebook.com` taką regułkę:

* odczytaj wartość parametru `u` (URL, czyli link do strony docelowej);
* jeśli ta wartość jest na liście stron zakazanych, to wyświetl informację o&nbsp;braku strony;
* jeśli jej tam nie ma, to przekieruj do tej strony.

Jedna krótka, niezmienna regułka. A&nbsp;listę stron zakazanych mogliby aktualizować na bieżąco, bez ujawniania jej internautom.

Nie jest to żadna moja paranoja; Facebook [pisał o&nbsp;tym wprost](https://www.facebook.com/notes/facebook-security/link-shim-protecting-the-people-who-use-facebook-from-malicious-urls/10150492832835766/), choć oczywiście w&nbsp;superlatywach.  
Również strony z&nbsp;branży marketingu internetowego [opisały nieoficjalne możliwości](https://www.glew.io/articles/what-are-facebook-link-shims-and-how-do-they-affect-your-data) przekierowań, tyle że stawiając je w&nbsp;korzystnym świetle:

> If your website is legitimate and safe, you have nothing to worry about.

Wbrew tym słowom [rzeczywistość pokazała](https://news.ycombinator.com/item?id=10793360), że warto zachować sceptycyzm :wink:

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/fb_link_shimming/facebook-przekierowanie-cenzura.jpg" alt="Zrzut ekranu z&nbsp;informacją o&nbsp;Facebooka, że nie radzi odwiedzać strony SaveTheInternet, bo jest z&nbsp;nią problem."/> 

{:.figcaption}
Taki straszak wyświetlał się ludziom chcącym poczytać indyjską stronę nagłaśniającą kwestię ataków na neutralność sieci i&nbsp;faworyzowania wielkich graczy. Takich jak Facebook.

### Parametry śledzące

Na koniec klasyka, która skutecznie uzupełnia poprzednie rzeczy. [Parametry śledzące]({%post_url 2021-04-09-internetowa-inwigilacja-parametry %}){:.internal}.

Do każdego linku po znaku zapytania można dodać dodatkowe informacje. Są rozdzielane znakami `&` i&nbsp;mają postać `nazwa=wartość`.  
Nie wpływają zwykle na działanie samego linku, ale mogą zawierać -- czasem w&nbsp;skompresowanej postaci -- dowolne informacje. Takie jak identyfikatory użytkowników, wzmianki o&nbsp;tym, z&nbsp;jakiej strony przychodzą itd.

Jeden z&nbsp;nich to klasyczny, istniejący od dawna `fbclid`. Jest dodawany prosto do linku do zewnętrznej strony (czyli do tego prowadzącego np. na *youtube.com*). Poniżej kilka sposobów na jego wykorzystanie:

* Skoro jest dodawany do końcowego linku, to strona zewnętrzna też go otrzyma i&nbsp;będzie mogła ustalić, że przychodzimy na nią z&nbsp;Facebooka.

  Trafiały się już stronki oszustów, które traktowały takich użytkowników [gorzej niż innych](https://news.ycombinator.com/item?id=21728988).

* Ponadto, jeśli na tej stronie znajdują się gościnnie elementy reklamowe od Facebooka, to będą mogły odczytać identyfikator (bo widzą to samo, co strona-gospodarz), wyszukać go w&nbsp;bazie i&nbsp;wyświetlić na tej podstawie reklamy.
* Jeśli ktoś skopiuje link i&nbsp;wyśle go do innej osoby -- nawet poza Facebookiem -- to zarówno platforma, jak i&nbsp;odwiedzana strona, mogą powiązać te osoby ze sobą.

  Sytuacje, gdy najpierw z&nbsp;identyfikatorem `abcd638…` przychodzi jedna osoba, a&nbsp;potem inna, z&nbsp;całkiem innego urządzenia, a&nbsp;do tego na przykład [przez Messengera]({%post_url 2023-08-08-wbudowane-przegladarki %}#ustalanie-marki-czyjegośtelefonu){:.internal}, mogą się wyróżniać.
 
  {:.post-meta .bigspace-after}
  Ma to oczywiście swoje ograniczenia; jeśli ktoś wrzuci link na publiczne forum, to liczba odwiedzających z&nbsp;tym samym identyfikatorem zostanie sztucznie zawyżona.

A to dopiero ten pierwszy parametr. Oprócz niego **do linków z&nbsp;przekierowaniem są dodawane jeszcze trzy inne**: `__tn__`, `f` oraz `c[0]`.

Można sobie przyjąć taką intuicyjną regułkę: im dłuższy ciąg znaków oraz im większy ich możliwy zakres (cyfry, litery...), tym więcej informacji się tam zmieści. 

Patrząc w&nbsp;ten sposób, parametr `__tn__` wydaje się niegroźny na tle innych. Jest krótki, przewidywalny, przyjmuje niewielki zakres wartości.

Pozostałe dwa są natomiast długimi ciągami znaków. Gdyby ktoś chciał, to mógłby tam wbić na przykład informacje identyfikujące użytkownika, znacznik czasu (moment kliknięcia w&nbsp;link) lub informacje o&nbsp;poście, w&nbsp;którym link się pojawił. 

To moje gdybanie, bo nie znam znaczenia parametrów. I&nbsp;raczej łatwo go nie poznam.

<details class="bigspace framed">
<summary><strong>Omówienie utrudnień</strong></summary>
<p>Teoretycznie sens parametrów mógłby tkwić gdzieś w&nbsp;kodzie JavaScript z&nbsp;Facebooka, który w&nbsp;końcu konstruuje linki na etapie podmianki. A&nbsp;każda przeglądarka daje łatwy wgląd do tego kodu. Czyżby rozwiązanie zagadki było tuż przed moimi oczami?</p>
<p>Problem w&nbsp;tym, że kod jest ściśnięty, <em>zminifikowany</em> (to powszechny zabieg twórców portali, oszczędzający nieco przesył danych).<br />
Po pierwsze: spacje i&nbsp;znaki końca linijek są usunięte. Ale to akurat można względnie łatwo odwrócić. Gorzej, że nazwy zmiennych są zastąpione pojedynczymi literami i&nbsp;musiałbym dużo główkować, żeby odczytać sens kodu.</p>
<p>Taka trochę inżynieria wsteczna dla internetu. A&nbsp;że znajomość JavaScriptu jest u&nbsp;mnie podstawowa, to wyzwanie mnie przerosło.<br />
Nie miałem też żadnej gwarancji, że trafiłbym na coś ciekawego. Równie dobrze w&nbsp;kodzie dodającym parametry mogło być jedynie przyporządkowanie w&nbsp;takim (zmyślonym) stylu:</p>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{ 
  linkID_1234: 'abdakdhja',
  linkID_3456: 'zycmnalsr'
}
</code></pre></div></div>
<p>…Gdzie <code class="language-plaintext highlighter-rouge">abdakdhja</code> i&nbsp;spółka to jakieś niepodpisane identyfikatory, pobrane z&nbsp;bazy Facebooka podczas ładowania strony.</p>
</details>

Mając do czynienia z&nbsp;czymś nieznanym, ale potencjalnie groźnym, lepiej dmuchać na zimne. Na szczęście między te wszystkie dziwne rzeczy jest wciśnięty nasz link docelowy, ten którego chcemy. I&nbsp;da się go wyłuskać.

## Jak to obejść?

Zwyczajne parametry śledzące dało się po prostu usunąć „z palca”. Tym razem trzeba się nieco bardziej namęczyć.  
Ale nie jest źle, to kwestia kilku kroków. Pokażę teraz różne sposoby.

### Ręcznie i&nbsp;krok po kroku

Można skopiować link do jakiegoś Notatnika, po czym wyszukać w&nbsp;nim znaki `&`. Wszystko od ostatniego znalezionego znaku do końca (włącznie z&nbsp;nim) -- usunąć.

<div class="bigspace black-bg mono">
https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAastpuFMHEU%26fbclid%3DDUŻO_ZNAKÓW<span class="red">&h=TEŻ_DUŻO_ZNAKÓW&__tn__=-UK-R&c[0]=ZNÓW_DUŻO_ZNAKÓW</span>
</div>

Potem wyszukujemy `u=`, czyli ostatnią rzecz przed właściwym linkiem (upewniamy się na oko, że tuż po tym zaczyna się `https`). Usuwamy ten tekst oraz wszystko przed nim.

<div class="bigspace black-bg mono">
<span class="red">https://l.facebook.com/l.php?u=</span>https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAastpuFMHEU%26fbclid%3DDUŻO_ZNAKÓW
</div>

Teraz będzie najbardziej żmudna część, bo uzyskany link ma postać „zabezpieczoną”. Wyłączono specjalność [niektórych znaków](https://docs.microfocus.com/OMi/10.62/Content/OMi/ExtGuide/ExtApps/URL_encoding.htm), jak ukośniki czy dwukropki; zamiast nich są zamienniki, jak `%3F` zamiast `?`.

Konwersja na postać „tradycyjną” nie jest trudna, ale mogłaby być upierdliwa przy użyciu samego znajdowania i&nbsp;zamieniania znaków. Proponuję zamiast tego użyć przeglądarki:

* otworzyć narzędzia przeglądarkowe  
  (na Firefoksie: kliknięcie trzech kresek w&nbsp;górnym rogu, `Więcej narzędzi > Narzędzia dla twórców witryn`; albo skrót klawiszowy `Ctrl+Shift+I`),
* kliknąć u&nbsp;góry zakładkę `Konsola`,
* wpisać tam `unescape('X')`, gdzie zamiast `X` wklejamy nasz link, po czym skopiować rezultat.

  <img src="/assets/posts/inwigilacja/fb_link_shimming/devtools-unescape.jpg" alt="Oczyszczony link po użyciu funkcji unescape w&nbsp;narzędziach przeglądarki" width="100%"/>

  {:.post-meta .bigspace-after}
  Pamiętajcie o&nbsp;cudzysłowach przed i&nbsp;po, są ważne!  
  Poza tym możliwe, że przeglądarka poprosi o&nbsp;wpisanie jakiegoś tekstu, żeby odblokować możliwość wklejania.

<details class="framed bigspace">
<summary><strong>Alternatywny sposób</strong></summary>
<p>Krok związany ze sprowadzeniem linków do tradycyjnej postaci można wykonać w&nbsp;inny sposób.</p>
<p>Jeśli nie chcemy zaglądać w&nbsp;narzędzia przeglądarki, a&nbsp;przy tym nie obawiamy się powierzania naszych linków obcej stronce, to można skorzystać z&nbsp;którejś z&nbsp;gotowych stronek z&nbsp;drobnymi narzędziami, jak popularna <a href="https://www.browserling.com/tools/url-decode">Browserling</a>.</p>
<p>…Ale proponuję zachować zasadę ograniczonego zaufania. Stronę warto <strong>odwiedzić w&nbsp;trybie prywatnym</strong> (żeby nie mogła zapisywać informacji na później).<br />
Poza tym po odwiedzeniu proponuję <strong>rozłączyć się z&nbsp;internetem</strong>.</p>
<p>Dopiero wtedy wklejamy nasz link. Jeśli narzędzie nie ma nic do ukrycia, to bezproblemowo powinno zadziałać offline. Jeśli nie działa, to proponuję z&nbsp;niego zrezygnować.</p>
<p>Mając czysty link, możemy go skopiować, po czym zamknąć stronę. Nie będzie nam już potrzebna. Można teraz ponownie włączyć internet, mając względną pewność, że nie mieli technicznej możliwości zapisania linku.</p>
<p class="post-meta bigspace-after">Dodam na wszelki wypadek, że istnieją strzępki kodu JavaScript działające chwilę po wyłączeniu przeglądarki, zwane <em>wątkami usługowymi</em>. Zamknięcie trybu prywatnego powinno automatycznie je usuwać, ale nie daję gwarancji. Dlatego zawsze lepiej czyścić link po swojej stronie.</p>
</details>

Na koniec można usunąć tradycyjny parametr śledzący -- wszystko od `&fbclid` albo `?fbclid` (zależnie od tego, czy był to jedyny parametr) aż do końca.

<div class="bigspace-before black-bg mono">
https://www.youtube.com/watch?v=AastpuFMHEU<span class="red">&fbclid=DUŻO_ZNAKÓW</span>
</div>

{:.post-meta .bigspace-after}
Wedle moich obserwacji Facebook dodaje swój chłam na końcu. Ale gdyby jakimś cudem były po nim inne, cenniejsce parametry, to usuwamy do najbliższego znaku `&` zamiast do końca.

Zostaniemy z&nbsp;oczyszczonym linkiem, który pozwoli całkowicie ominąć Facebooka i&nbsp;odwiedzić oczekiwaną stronkę bezpośrednio.

### Bonus: skrypt pomocniczy

Stworzyłem też krótki, pomocny skrypt Pythona, który pozwala zautomatyzować powyższe kroki i&nbsp;czyścić linki szybko, całkiem *offline*, nawet bez narzędzi przeglądarkowych.

{% include pyscript.html
name="fblink.py"
link="/assets/skrypty/fblink.py"
info="Mając Pythona na komputerze, wystarczy uruchomić ten skrypt (przez kliknięcie, przez domyślny edytor IDLE, obojętne).  
Wyświetli się prośba o&nbsp;wklejenie linku. Wklejamy ten nieoczyszczony z&nbsp;Facebooka, a&nbsp;pod spodem pojawi się jego wersja bez przekierowania i&nbsp;parametrów śledzących."
%}

### Podsumowanie

Mając oczyszczony link, możemy go wkleić do górnego paska przeglądarki. W&nbsp;ten sposób pójdziemy prosto do oczekiwanej strony, nie zahaczając o&nbsp;terytoria Facebooka.  
Gratulacje, najwredniejsze linki śledzące zostały przechytrzone :smile:

Rozwiązaniem jeszcze trwalszym może być natomiast ograniczenie czasu spędzanego na Fejsie. W&nbsp;ten sposób rzadziej będziemy nadziewać się na linki. Zaś zyskany czas można poświęcić na spotkania z&nbsp;ludźmi w&nbsp;realu.

Życząc takich pomyślnych spotkań, kończę ten wpis. Do zobaczenia w&nbsp;kolejnych!



