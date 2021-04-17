---
layout: post
title:  "Internetowa inwigilacja 3 – przekierowania"
description: "Podmiana linków i zastąpienie ich przekierowaniami – sposób na śledzenie użytkowników."
subtitle: "„Do kogo idziesz?”"
date:   2021-03-26 00:00:15 +0100
tags: [Internet, Inwigilacja, Centralizacja, Porady]
firmy: [Twitter, Google]
category: internetowa_inwigilacja
category_readable: "Internetowa&nbsp;inwigilacja"
---

W poprzednich częściach „Internetowej inwigilacji” porównałem informacje, jakie wysyłamy innym stronom internetowym, do etykiet naklejanych na paczki i&nbsp;listy.

Przyjrzeliśmy się również refererowi, jednej z&nbsp;tych informacji -- zdradzającej stronie B, że przybywamy na nią po kliknięciu w&nbsp;link na stronie A.

W tym odcinku nadal trzymamy się tematu linków. Tym razem nie omówię kolejnych rodzajów informacji, jakie mogą się znaleźć na naszej etykiecie, tylko **sztuczkę**, dzięki której istniejące informacje mogą trafić do innej strony.

To trochę jak odwrócony referer -- on mówił, skąd przychodzimy. Zaś dzięki podmianie linków i przekierowaniom **strona A&nbsp;może się dowiedzieć, że odchodzimy z&nbsp;niej na stronę B**.

Gwiazdą wieczoru będzie Twitter, który takie coś uskutecznia.

{% include info.html type="Podstawy" text="Ogólnie wpis nie wymaga żadnej wiedzy o&nbsp;Twitterze.  
Wystarczy wiedzieć, że to amerykański portal społecznościowy. Można na nim tworzyć krótkie, widoczne dla każdego wpisy zwane *tweetami* (liczące na dzień dzisiejszy maksymalnie 280 znaków). Tweety mogą zawierać linki, obrazki i&nbsp;inne dodatki." %}

## Wprowadzenie

Wyobraźmy sobie, że jest stronka, na którą użytkownicy sami mogą wrzucać treść, w&nbsp;tym linki (podobieństwo do Twittera przypadkowe i&nbsp;niezamierzone!).

A właściciele strony chcą ich jak najdokładniej inwigilować. W&nbsp;jaki sposób mogą to robić?

W przypadku dodawanych treści to łatwe. W&nbsp;końcu mają władzę nad serwerami. Jeśli jakiś użytkownik chce coś dodać, musi to najpierw wysłać na serwer.

A wtedy właściciele zapisują: „Użytkownik nr *05467* dnia tego a&nbsp;tego dodał wpis z&nbsp;linkiem do *www.ciemnastrona.com.pl*”.

Ale monitorowanie, kto potem w&nbsp;te linki kliknie? To już trudniejsza sprawa.

## Typowe linki

Przeglądarki mają własną metodę postępowania z&nbsp;linkami. Nawet jeśli jesteśmy na stronie A, to po kliknięciu w&nbsp;link do strony B&nbsp;przeglądarka po prostu opuszcza A&nbsp;i wysyła B&nbsp;informację, że chce ją odwiedzić.

{:.figure}
<img src='/assets/posts/przekierowania/distracted-boyfriend-mem.webp' alt="Znany mem pokazujący chłopaka idącego za rękę z&nbsp;dziewczyną, który ogląda się za inną dziewczyną. A&nbsp;ta, z&nbsp;którą szedł, patrzy na niego ze złością. Na postać chłopaka nałożone jest logo Firefoksa. Na postać dziewczyny, z&nbsp;którą szedł, napis facebook.com. A&nbsp;na postać dziewczyny, za którą się ogląda -- ciemnastrona.com.pl."/>

{:.figcaption}
Mem nie jest w&nbsp;100% trafny -- strona A&nbsp;tak łatwo się nie dowie, że przeglądarka przechodzi na B.

Strona A&nbsp;nie może zmienić działania przeglądarki. Ale może stosować sztuczki, żeby mimo to ustalić, w&nbsp;co klikają jej użytkownicy.

Spójrzmy najpierw na schemat. Gdyby Twitter zachowywał się jak typowe strony, to interakcje z&nbsp;linkami wyglądałyby w&nbsp;taki sposób:

<img src='/assets/posts/przekierowania/linki-demo1.webp' alt="Schemat pokazujący dwa prostokątne pola odpowiadające dwóm stronom internetowym. U&nbsp;góry widać pole jasnoniebieskie, ozdobione po lewej stronie dużym logiem Twittera. Wewnątrz pola znajduje się zrzut ekranu tweeta. Widać na nim link, wyróżniony tu ciemnoniebieską obwódką. Dolne prostokątne pole, jasnopomarańczowe, zawiera zrzut ekranu z&nbsp;forum Hacker News, z&nbsp;podstrony do którego prowadził wyróżniony link. Po lewej stronie pole jest ozdobione logiem tego forum. Oba pola są połączone grubą, ciemnoniebieską strzałką. Jest przy niej ikona paczki -- miniatura obrazka z&nbsp;pierwszego wpisu z&nbsp;tej serii, symbolizująca nagłówki HTTP."/>

{:.figcaption}
Treść tweeta to lekki spoiler odnośnie jednego z najbliższych wpisów.

1. Klikamy link do strony B&nbsp;(tu: forum Hacker News) umieszczony w&nbsp;czyimś tweecie.
2. Nasza przeglądarka opuszcza Twittera i&nbsp;wysyła stronie B&nbsp;prośbę o&nbsp;przesłanie treści.

   Przy okazji wysyłamy stronie B&nbsp;nagłówki HTTP (naszą „etykietę”) z&nbsp;pewnymi informacjami o&nbsp;sobie -- no ale tak już jest w&nbsp;tym internecie.

3. Przeglądarka otrzymuje i&nbsp;wyświetla stronę B.

W każdym razie -- normalnie Twitter by nie wiedział o&nbsp;tym, że przeszliśmy na inną stronę.

## Śledzące linki Twittera

Ale rzeczywistość jest inna, a&nbsp;ptaszysko jest wścibskie. Gdyby strony zawierały tylko tradycyjne linki, to by nie wiedziały, czy i&nbsp;kiedy w&nbsp;nie klikamy. **Dlatego je podmieniają**. 

Metodą, która umożliwia łatwą podmiankę jest **przekierowanie**. To instrukcja dla przeglądarki, że ma teraz przejść na inną stronkę. Taki odpowiednik spławienia kontrolera zza płota. „A niee, z&nbsp;tym to idź pan do sąsiada”.

Chytra sztuczka Twittera zaczyna się już na etapie, kiedy ktoś dodaje nową treść:

1. Ktoś pisze na Twitterze (stronie A) nowego tweeta, zawierającego link do strony B.
2. Twitter wykrywa link. Tworzy dla niego mini-stronkę C&nbsp;pod adresem *t.co*, której jedyną zawartością jest przekierowanie do strony B. Podmienia pierwotny link tak, żeby do niej prowadził.

   Nie ma tu najmniejszego znaczenia, że tekst linku wygląda nadal, jakby prowadził pod *news.ycombinator...* Tak naprawdę to *t.co...*, własność Twittera.  
**Tekst linku i&nbsp;strona, do której prowadzi to kompletnie odrębne sprawy**. Zresztą sam na blogu często ukrywam linki pod zwykłymi słowami.

Dzięki temu, że Twitter podmienił źródło linku na samym początku, będzie on zawsze prowadził na ich podstawioną stronkę. Nawet gdyby ktoś udostępnił tweeta poza Twitterem.

Etap drugi, czyli interakcja z&nbsp;podmienionym linkiem, wygląda tak:

{:.bigspace}
<img src='/assets/posts/przekierowania/linki-demo2.webp' alt="Rozbudowana wersja poprzedniego schematu. Z&nbsp;pola odpowiadającego Twitterowi wychodzi przerywana linia zakończona grotem, zmierzająca do jego loga. Obok grotu strzałki narysowany jest symbol nagłówków HTTP. Druga przerywana linia odchodzi z&nbsp;loga Twittera i&nbsp;kieruje się do małego pola ze skróconym adresem zaczynającym się na t.co. To pole ma taki sam kolor tła jak to duże dlas Twittera. Dopiero z&nbsp;tego pola odchodzi duża strzałka połączona z&nbsp;polem Hacker News."/>

1. Ktoś klika w&nbsp;link z&nbsp;tweeta.

   Chce wejść na stronę B, ale nie wie, że link prowadzi do mini-stronki C.

2. Prosząc o&nbsp;stronę spod tego adresu, nasza przeglądarka **wysyła do *t.co* (Twittera) pełen zestaw informacji z&nbsp;nagłówków**.
3. W&nbsp;zamian otrzymuje mini-stronkę C.
4. ...Ale nie ma na niej nic poza przekierowaniem do strony B. Zatem przeglądarka ponownie wysyła komplet nagłówków, ale tym razem do strony B.
5. Przeglądarka otrzymuje i&nbsp;wyświetla stronę B.

Zatem nadal wysłaliśmy naszą „etykietę” stronie B&nbsp;i na nią przeszliśmy. Różnica jest taka, że te same informacje zna teraz również Twitter.

## Ciemna strona przekierowań

Na Twitterze sami się nie kryją z&nbsp;podmienianiem linków, nazywając to swoją usługą:

> Our link service measures information **such as** how many times a&nbsp;link has been clicked  
(...)  
A link converted by Twitter’s link service is checked against a&nbsp;list of potentially dangerous sites.  
(...)  
You cannot opt out of link shortening. 

{:.figcaption}
Źródło: [informacje z&nbsp;Twittera](https://help.twitter.com/en/using-twitter/url-shortener) o&nbsp;ich przycinaczu linków.

Wiecie, czemu zaznaczyłem *"such as"*? Bo taki zwrot sugeruje, że to tylko przykład. A&nbsp;analizować mogą zapewne, co im się żywnie podoba.

Sprawa z&nbsp;ochroną przed innymi stronami też jest trochę szemrana. Wyobraźmy sobie -- tak czysto teoretycznie -- że Twitter wpada kiedyś w&nbsp;ręce jakiegoś dyktatora (z dowolnej strony spektrum politycznego).

Dyktator wiedziałby dokładnie, które linki prowadzą na które strony. A mając kontrolę nad przekierowaniami, **mógłby jednym pstryczkiem wyłączyć wszystkie linki z&nbsp;Twittera prowadzące do stron, które go krytykują**. Takich jak np. *krytyka-dyktatora.com*.

Wystarczyłoby podmienić odpowiednie mini-stronki z&nbsp;serii *t.co*. Żeby zamiast przekierowania zawierały np. materiały propagandowe.

Użytkownicy nieobeznani z&nbsp;takimi trikami mogliby wtedy pomyśleć, że to ze stronką *krytyka-dyktatora* jest coś nie tak -- w&nbsp;końcu linki do tej strony na Twitterze miały jej normalną nazwę. Kliknęli, a&nbsp;tu informacja o&nbsp;zagrożeniu wyskakuje!

Mogłoby im nie przyjść do głowy, że to władca Twittera stosuje cenzurę. Jeden pstryczek, jedna strona odcięta. Nic nie wymknie się poza Twittera bez jego wiedzy. Uroki scentralizowanej władzy.

<img src='/assets/posts/przekierowania/twitter-tco.webp' alt="Rysunek pokazuje logo Twittera otoczone z każdej strony półprzezroczystą, zielonkawą sferą wyglądającą jak pole siłowe. Sfera jest podpisaną nazwą twitterowego przycinacza linków."/>

{:.figcaption}
Źródło obrazka: [Reddit](https://www.reddit.com/r/blender/comments/7ij4ir/geodesic_force_field/). Przeróbka moja.

{% include info.html type="Ciekawostka" text="W&nbsp;USA skierowali nawet [pozew zbiorowy](https://www.dailydot.com/debug/twitter-short-url-lawsuit/) przeciw Twitterowi, argumentując że wysyłanie po kryjomu danych o&nbsp;klikniętych linkach narusza kalifornijskie przepisy o&nbsp;ochronie prywatności (odpowiednik polskiego RODO)."%}

Wziąłem Twittera za przykład, ale oczywiście nie jest jedyną stroną, która działa w&nbsp;taki sposób. Różne przycinacze linków **wprost oferują możliwości analizowania ruchu** każdemu, kto by tylko chciał sobie popatrzeć:

> \[Bitly\] collects over 20 data points with every click, from geographic data down to the local city level to referral channels to device type.  
(...)  
Droplr is also the only URL shortener to track every link forever.  
(...)  
free URL shortener, tiny.cc, also provides basic free link tracking. 

{:.figcaption}
Źródło: [droplr.com](https://droplr.com/how-to/productivity-tools/4-best-url-shorteners-for-link-tracking/)

Możemy monitorować swoje linki za darmo, na zawsze, do tego zbierać szeroki zakres danych. Cudownie :roll_eyes:

Analitycy mają prawdziwy arsenał. Ale my również nie jesteśmy bezradni, jeśli nie chcemy zdradzać informacji podczas klikania w&nbsp;zamaskowane linki. Zaprezentuję teraz nasze możliwości.

## Jak to przechytrzyć?

Przede wszystkim patrzmy czasem, w&nbsp;co klikamy. Nawet jeśli tekst linku mówi *dobrastronka.cool*, to pod tekstem może się kryć link do *niedobrastronka.fuj*.

Najprostszą metodą, żeby to sprawdzić, jest **najechanie kursorem na link i&nbsp;spojrzenie w&nbsp;lewy dolny róg przeglądarki**. Wyświetli się tam, dokąd on naprawdę prowadzi.  
(W przypadku urządzeń mobilnych przytrzymujemy palec na linku. Ostrożnie, żeby nie kliknąć!).

Kiedy już wiemy, czy mamy do czynienia z&nbsp;podmienionym linkiem, możemy go przechytrzyć.

# Kopiowanie tekstu

Jeśli widzimy pełen adres strony w&nbsp;formie tekstu, ale ukryty pod nim link prowadzi w&nbsp;inne miejsce, to możemy, zamiast klikać link, **po prostu skopiować tekst i&nbsp;wkleić go w&nbsp;pasek przeglądarki**. W&nbsp;ten sposób przejdziemy prosto na tę stronkę, na którą chcieliśmy. Bez pośredników.

(Jeśli uważnie czytaliście wpis o&nbsp;refererze, to być może zauważyliście, że tam też wklejenie linka w&nbsp;pasek ucinało część informacji. Taka uniwersalna metoda).

{% include info.html type="Porada" text="Czasami widoczny adres strony jest przycięty, ale pokazuje się w całości po najechaniu kursorem. Tak jest w&nbsp;przypadku tego linka z&nbsp;Twittera (obrazek poniżej; widać, że po najechaniu pokazują się obie brakujące cyfry).  
Jeśli boimy się techniki, to możemy skopiować do paska przeglądarki tę część, którą się da, a&nbsp;resztę wyświetlić i&nbsp;dopisać ręcznie.  
Ale lepiej kliknąć link prawym przyciskiem, wybrać `Zbadaj element` i&nbsp;skopiować potrzebny tekst prosto z&nbsp;kodu strony (w razie potrzeby klikając w&nbsp;strzałki, żeby rozwinąć elementy)." trailer="<p class='figure'><img src='/assets/posts/przekierowania/twitter-link-prawdziwy.webp' alt='Mały zrzut ekranu pokazujący fragment linka z&nbsp;poprzednich przykładów z&nbsp;Twittera. Pod tekstem, który jest częściowo ucięty, widać pasek z&nbsp;tekstem na szarym tle, który pokazał się po najechaniu kursorem na link. Ten tekst zawiera link w&nbsp;całości, razem z&nbsp;uciętymi cyframi.' width='500px'/></p>"%}

No, ale czasem szczęście nam nie sprzyja. Widzimy tylko skrócony link, bez żadnej wskazówki dokąd prowadzi. Albo używamy urządzenia mobilnego i&nbsp;ciężko zajrzeć w&nbsp;kod strony.

Jeśli nie klikniemy w&nbsp;skrócony link, to się nie dowiemy, co się za nim kryje.  
Ale jeśli klikniemy, to stronka A&nbsp;się dowie, że to zrobiliśmy.

I tak źle, i&nbsp;tak niedobrze. Czy jest jakieś rozwiązanie?

# GetLinkInfo

Otóż jest -- ale wymaga odrobiny spychologii. **Jeśli ktoś musi w&nbsp;ten link wejść, to niech to będzie ktoś inny**. Na przykład [strona GetLinkInfo.com](https://www.getlinkinfo.com).

Najpierw klikamy prawym przyciskiem na link (na mobilnym: przytrzymujemy palec) i&nbsp;wybieramy `Kopiuj adres odnośnika`. W&nbsp;ten sposób skopiujemy do schowka ten skrócony adres, *t.co...* w&nbsp;przypadku Twittera.

Potem odwiedzamy *getlinkinfo.com*, wklejamy adres w&nbsp;puste pole i&nbsp;klikamy przycisk `Get Link Info`. Ich serwery wezmą na klatę podrobiony link, odwiedzą go i&nbsp;pokażą nam, dokąd prowadził (zaznaczyłem na czerwono):

{:.figure .bigspace}
<img src='/assets/posts/przekierowania/getlinkinfo-wynik.webp' alt="Zrzut ekranu ze strony GetLinkInfo. W&nbsp;środkowym pasku wklejony skrócony adres strony. Pod nim widać listę wyświetlonych informacji. Wśród nich zaznaczona czerwoną ramką informacja nazwana 'Effective URL' -- o&nbsp;adresie, do którego tak naprawdę prowadził link."/>

Teraz wystarczy tylko w&nbsp;niego kliknąć... Albo go skopiować i&nbsp;wkleić w&nbsp;pasek przeglądarki (żeby nie wysyłać w&nbsp;refererze informacji, że przybywamy z&nbsp;*getlinkinfo.com* :sunglasses:).

Metoda jest uniwersalna i&nbsp;powinna skutecznie działać, kiedy musimy wejść w&nbsp;nieznane, skrócone linki. Warto dodać GetLinkInfo gdzieś do zakładek.

# Dodatek Universal Bypass

**(Dodano 8.04.2021 r.)**

{% include web-extension.html
info="Dodatek do przeglądarki <strong>Universal Bypass</strong> odkryłem jakiś czas po stworzeniu wpisu. Jest darmowy i&nbsp;otwartoźródłowy.<br/>To może być najprzyjaźniejsze rozwiązanie do obchodzenia popularnych przekierowań (<i>t.co</i>, <i>bit.ly</i>…), ponieważ nie wymaga każdorazowego odwiedzania GetLinkInfo. Wszystko dzieje się w tle."
firefox="Możecie zainstalować go bez problemu <a href='https://addons.mozilla.org/en-US/firefox/addon/universal-bypass/'>z&nbsp;oficjalnego archiwum dodatków</a>."
chrome = "Bypassa <strong>nie ma</strong> w&nbsp;uniwersalnym archiwum Chrome'a. Więcej informacji w&nbsp;ramce poniżej. Jeśli Was to nie zraża, to twórcy <a href='https://universal-bypass.org/install'>opisują na stronce</a>, w&nbsp;jaki sposób zainstalować Bypassa ręcznie.<br/>(Ale i&nbsp;tak nalepiej zmienić Chrome'a; robienie z&nbsp;niego przeglądarki chroniącej prywatność to jak robienie wyścigówki z&nbsp;malucha)."
inne-pc="Dostępna jest wersja <a href='https://microsoftedge.microsoft.com/addons/detail/ckiidekccfgninkobmmofopbbdgdclgg'>na Edge'a</a>.<br/>Poza tym wszystkie przeglądarki oparte na Chromium (Brave, Vivaldi, Opera…) powinny dać radę. Może jednak być konieczna ręczna instalacja dodatku."
android="Wspiera go podobno Kiwi Browser (nie testowałem). Inne przeglądarki niestety kuleją ze wspieraniem dodatków."
%}

{% include info.html type="Niedobry Google" text="Dlaczego wspomnianego dodatku Universal Bypass nie ma na Chrome'ie? Okazuje się, że to **Google go usunął odgórną decyzją**. Jako wyjaśnienie podają, że może służyć do omijania płatności na stronach.  
Tylko że ciężko spotkać się z takim zastosowaniem przekierowań, dużo częściej są używane do śledzenia. Brzmi to jak wymówka. No ale takie uroki monopolu..."
trailer="
<blockquote>Google took it down for apparently 'circumventing paywalls.' I&nbsp;have clarified that Universal Bypass is more of an adblocker and asked for details of where paywalls are circumvented, but it's Google, so of course I&nbsp;didn't get a response.
</blockquote>
<p class='figcaption' style='margin-bottom:0px'>Źródło: <a href='https://universal-bypass.org/faq'>strona Universal Bypass</a>
</p>"%}

Widać zatem, że nie jesteśmy bezbronni w walce z przekierowaniami. Jest od tego dodatek. Jeśli nie chcemy dodatku (albo przeglądarka go blokuje), to stronka *GetLinkInfo*. Jeśli jesteśmy tradycjonalistami i da się skopiować adres, to wklejanie w pasek.

Ale póki co życzę nam, żeby te myki nie były potrzebne, a&nbsp;wszystkie linki -- jak drogi do Rzymu -- od razu prowadziły tam, dokąd powinny.

Do zobaczenia w&nbsp;kolejnym wpisie!
