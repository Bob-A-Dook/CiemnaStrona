---
layout: post
title:  "Clearnet, deepnet i darknet. Różne oblicza internetu"
subtitle: "Nie bójmy się ciemności."
description: "Nie bójmy się ciemności"
date:   2023-06-02 8:17:20 +0100
tags: [Internet, Media, Podstawy, Tor]
firmy: [Google]
image:
  path: /assets/posts/tor/clearnet-darknet/clearnet-darknet-baner.jpg
  width: 1200
  height: 700
  alt: "Przeróbka mema. Tło jest podzielone na dwie części, szaroburą podpisaną Clearnet i świetlistą, podpisaną Darknet. Po szarej siedzi zapłakany człowiek wyglądający jak nędzarz. Po świetlistej stoi postać w szacie, z logiem Tor Browsera zamiast głowy, i wyciąga do niego dłoń.."
---

<div class="black-bg mono bigspace-after" id="special-pic">
Żyjesz w&nbsp;clearnecie.
</div>

<script>
var img = '<img src="/assets/posts/tor/clearnet-darknet/morfeusz-neo-pigulki.jpg" alt="Mem satyryczny nawiązujący do filmu Matrix, złożony z&nbsp;czterech kadrów. Na pierwszym Morfeusz mówi do Neo, że jeśli weźmie niebieską pigułkę, do jego życie nadal będzie do kitu. Na drugim Neo pyta, czym jest czerwona. Na trzecim Morfeusz odpowiada jedynie, że ma truskawkowy smak. Na czwartym Neo po nią sięga."/>' +
          '<p class="figcaption"><a href="#rzeczy-ukryte-na-widoku">Powrót do opisu ukrytego obrazka</a></p>';
var link = window.location.href;
if (link.endsWith('?tajnykod=1234567')) {
  document.getElementById("special-pic").outerHTML = img
}

</script>

Internet jest ogromny. Do tego stopnia, że można go nieironicznie uznać za wirtualny świat -- nawet jeśli weźmiemy pod uwagę tylko najzwyklejsze, codziennie odwiedzane strony. I&nbsp;pominiemy obiecywane nam cukierkowe *metawersa*.

A ponieważ jest stworzony przez ludzi, wiele jego aspektów jest odbiciem realnego społeczeństwa. Strony mogą być jak prywatne domy kolekcjonerów-hobbystów. Kluby pasjonatów. Tandetne galerie handlowe, zoptymalizowane pod napędzanie konsumpcji.

No i&nbsp;boczne alejki, gdzie po zapukaniu do drzwi i&nbsp;podaniu tajnego hasła można zamówić rzeczy sprzeczne z&nbsp;prawem. A&nbsp;czasem nawet z&nbsp;etyką.  
W mediach ten ostatni rodzaj miejsc nazywa się często *darknetem*. „Ciemna strona internetu, pełna przestępców i&nbsp;zła, do której mogą wejść tylko użytkownicy Tora” (*The Onion Router*; przeglądarka anonimizująca).

Problem w&nbsp;tym, że ta wizja miesza pojęcia techniczne z&nbsp;kwestiami etycznymi. I&nbsp;uderza w&nbsp;przeglądarkę, która sama w&nbsp;sobie jest narzędziem neutralnym i&nbsp;przydatnym. I&nbsp;fajnym.  
W tym wpisie obalę parę medialnych mitów i&nbsp;po ludzku omówię, czym są te różne dziwne *nety*. Zobaczymy, że podział jest umowny, a&nbsp;najciemniej bywa pod latarnią.

{:.figure .bigspace}
<img src="/assets/posts/tor/clearnet-darknet/clearnet-darknet-baner.jpg" alt="Przeróbka mema. Tło jest podzielone na dwie wyraźne strefy - jedną szaroburą, z&nbsp;unoszącymi się muchami; drugą jasną i świetlistą. Po stronie szarej siedzi rysunkowy człowiek ze łzami w&nbsp;oczach, wyglądający na nędzarza. Po stronie świetlistej stoi postać w&nbsp;szacie wyciągająca do niego rękę. Zamiast głowy ma fioletową cebulę, logo przeglądarki Tor Browser."/>

{% include info.html
type="Nim zaczniemy"
text="Uprzedzam, że to nie przewodnik po działaniu Tora. Na to jeszcze przyjdzie czas, kiedy sam się douczę :wink:  
Skupiam się tu na wyjaśnianiu pojęć *clearnetu*, *deepnetu* i&nbsp;*darknetu*, zaś o&nbsp;cebulowym routerku będzie tylko ogólnikowo."
%}

### Spis treści

* [Medialne mity](#medialne-mity)
  * [Najciemniej pod latarnią?](#najciemniej-pod-latarnią?)
  * [Skutki demonizowania](#skutki-demonizowania)
* [Clearnet](#clearnet)
* [Deepnet](#deepnet)
  * [Plik robots.txt](#plik-robots.txt)
  * [Deepnetujemy swój profil](#deepnetujemy-swój-profil)
  * [Deepnet a&nbsp;logowanie](#deepnet-alogowanie)
* [Darknet](#darknet)
* [Tor Browser](#tor-browser)
  * [Strony typu Onion](#strony-typu-onion)
  * [Jasne strony darknetu](#jasne-strony-darknetu)
* [„Wszyscy siedzimy w&nbsp;darknecie”](#wszyscy-siedzimy-wdarknecie)
* [Podsumowanie](#podsumowanie)


## Medialne mity

Jako przykład medialnego mieszania pojęć przedstawiam artykuł fundacji Orange, [„Czym jest Darknet, dark web oraz deep web? Jak chronić dziecko przed ciemną stroną internetu?”](https://fundacja.orange.pl/strefa-wiedzy/post/czym-jest-darknet-dark-web-oraz-deep-web-jak-chronic-dziecko-przed-ciemna-strona-internetu). 

{:.bigspace}
> Zarówno Deep web, jak i&nbsp;Dark web to sieci niedostępne dla wszystkich użytkowników, ani za pomocą standardowych przeglądarek internetowych. (...)  
Deep web zazwyczaj jest używany do legalnych działań, które wymagają anonimowości w&nbsp;sieci, natomiast Dark web jest często wykorzystywany do nielegalnych celów.

Znajdziemy tu dwa przekręcone fakty.  
Pierwszym jest pisanie, że *deepnet* jest niedostępny za pomocą zwykłych przeglądarek. Drugim -- wiązanie go z&nbsp;anonimowością.  
Jak zobaczymy, **_deepnet_ to znaczna większość internetu. Jest czymś całkiem powszechnym**. I&nbsp;nie ma w&nbsp;nim nic tajemniczego.

Nawet w&nbsp;[artykule ze strony ICANN](https://www.icann.org/en/blogs/details/the-dark-web-the-land-of-hidden-services-27-6-2017-en) -- organizacji zajmującej się domenami internetowymi -- znajdziemy wymieszanie pojęć.  
W zakładce na temat *darknetu* napisali tylko parę zdań. Zaś druga, znacznie większa zakładka o&nbsp;*deepnecie* wspomina o&nbsp;zagadnieniach, które lepiej by chyba pasowały do tej pierwszej.

{:.bigspace}
> Some Deep Websites are unconventional marketplaces that offer a&nbsp;disturbing range of products or services (...) You can also use the Deep Web to anonymously share information

Pomijając mijanie się z&nbsp;definicją, oba źródła robią też coś, co mi osobiście nie leży. Łączenie pojęć z&nbsp;kwestiami legalności, jakby to było oczywiste. A&nbsp;tymczasem **_deepnet_ i&nbsp;_darknet_ to pojęcia związane z&nbsp;techniką, a&nbsp;nie legalnością czy moralnością**.

To trochę jak z&nbsp;kompasami politycznymi -- jedna oś prawo-lewo to za mało, żeby rzetelnie przedstawić sprawę. Przydadzą się co najmniej dwie. Jedna od spraw technicznych, całkiem osobna od legalności.  
Jak najbardziej istnieją takie rzeczy jak prywatnościowy darknet „w służbie dobra”. Albo przestępstwa w&nbsp;publicznym, mainstreamowym internecie. Zaryzykowałbym nawet stwierdzenie, że te drugie są całkiem częste.

### Najciemniej pod latarnią?

Na temat darknetu powstała niejedna miejska legenda. Że są tam nagrania morderstw na żywo. Że można wynająć zabójców.

A przecież nagrania okrutnych morderstw łatwo znaleźć w&nbsp;całkiem zwykłej, publicznej części internetu. Zbrodnia na żywo od niejakiego [Luki M.](https://en.wikipedia.org/wiki/Murder_of_Jun_Lin) została wrzucona na stronę niszową, ale dostępną przez zwykłą przeglądarkę. Łatwo też trafić np. na wyczyn maniaków z&nbsp;Dniepropetrowska.

Wiele nagrań z&nbsp;wypadków lub egzekucji było dostępnych na Rotten albo Liveleaku -- już niedziałających, ale wcześniej hulających przez kilkanaście lat. Publicznie dostępnych.

Wynajęcie zabójców przez darknet? Nawet jeśli takie ogłoszenie się trafi, to często będzie zwykłą próbą naciągnięcia zdesperowanych ludzi na kasę. Co ma sens -- w&nbsp;końcu raczej nie zgłoszą takiego oszustwa na policję :wink:

Niszczenie ludzi znajdziemy natomiast w&nbsp;całkiem publicznej sieci. W&nbsp;USA w&nbsp;niektórych kręgach propaguje się *swatting* -- ustalali czyjś adres, dzwonili na policję i&nbsp;informowali, że pod tym adresem uzbrojony napastnik wziął zakładników. Amerykańscy gieroje wpadali z&nbsp;bronią. W&nbsp;paru przypadkach [doprowadziło to do śmierci niewinnych ludzi](https://en.wikipedia.org/wiki/Swatting#Injuries_or_deaths_due_to_swatting).

Wszystkie powyższe rzeczy, i&nbsp;wiele innych, to jak najbardziej mroczne sprawy. Ale nie darknetowe.  
Gdyby pokazać w&nbsp;liczbach bezwzględnych, ile brudu tkwi w&nbsp;poszczególnych warstwach internetu, to podejrzewam że najwięcej byłoby go w&nbsp;publicznie dostępnej części. Chociażby przez to, że jest znacznie większa.

### Skutki demonizowania

Mieszając ideę anonimowego przeglądania z&nbsp;przestępstwami, media robią jej zły PR. Rykoszetem mogą obrywać niewinne rzeczy. Jak przeglądarka Tor Browser albo samo słowo *darknet*.

Czas na parę sekund besztania Google'a, bowiem miała u&nbsp;nich miejsce pewna dziwna sytuacja. Pewnego dnia nagle i&nbsp;nieodwołalnie zamknęli grupę dyskusyjną o&nbsp;nazwie `Darknet`, założoną w&nbsp;jednym z&nbsp;ich serwisów, Google Groups.

Problem? Nie była to grupa o&nbsp;otchłaniach internetu -- dotyczyła jedynie **programów do analizy obrazu, mających tę niefortunną nazwę**. Która była wariacją na temat *ConvNets*, pewnej ogólnej metody.

Dla formalności dodam, że nie wiem, czy blokada nastąpiła przez samą nazwę. Mogło być też tak, że nazwa skusiła jakiegoś trolla, ten podrzucił na grupkę nielegalne materiały, Google ją zamknął.  
Ale, niezależnie od przyczyny, szkoda została wyrządzona, [cenne dyskusje przepadły](https://news.ycombinator.com/item?id=19598107).

Ale uznajmy, że to naciągany przykład. Dlatego mam kolejny -- nie tak dawną dyskusję na Reddicie o&nbsp;tym, że [ktoś został zwolniony za jednorazowe połączenie z&nbsp;siecią Tor](https://www.reddit.com/r/cscareerquestions/comments/rsdg0r/til_pressing_altshiftn_in_brave_browser_will/). Może nawet przypadkowe.

Osoba ta używała przeglądarki Brave, która posiada opcję oglądania stron w&nbsp;trybie anonimowym, przez protokół Tor. Włącza się ją kombinacją klawiszy `Alt+Shift+N`.

A z&nbsp;punktu widzenia mało ogarniętych menedżerów było to chodzenie po ciemnych zakamarkach internetu, tam gdzie są przestępcy. A&nbsp;zatem pospiesznie zwolnili winowajcę (obstawiam, że historia działa się w&nbsp;USA, gdzie pracownicy są wymiennym mięsem).

{:.post-meta .bigspace-after}
Pamiętajmy, że to Reddit, ludzie mogą wrzucać zmyślone historyjki. Ale, czytając komentarze, znajdziemy całkiem realne przykłady krótkowzroczności menedżerów. Nawet gdyby ta konkretna historia się nie wydarzyła, to jest całkiem możliwe, że kogoś dotknie.

Tak to może być, kiedy ludzie decydujący o&nbsp;innych uwierzą w&nbsp;medialne bzdurki. Żeby nie być jak oni i&nbsp;wiedzieć coś o&nbsp;świecie, omówmy sobie po ludzku różne warstwy naszego internetu.

## Clearnet

Pierwsze oblicze internetu. To najzwyklejsze strony, które możemy znaleźć w&nbsp;wyszukiwarce, odwiedzić, poczytać.  
Wpisujemy w&nbsp;DuckDuckGo (albo nawet wścibskiego Google'a!) słowa `carbonara przepis` i&nbsp;wyskoczą nam wszelkiej maści blogi z&nbsp;przepisami kulinarnymi. Wpiszemy coś innego, jak `szkolny wielki brat`, to może wyskoczy Ciemna Strona. Bez przepisów.

A jednak, choć *clearnet* jest codziennością, pojęcie to widuję w&nbsp;mediach rzadziej niż *deepnet* czy *darknet*. Dlaczego?  
Moja nieco cyniczna interpretacja -- dlatego, że w&nbsp;codzienności nie ma sensacji. Bardziej klikalne jest to, co związane ze zbrodniami, sprawami łóżkowymi, albo chociaż jakąś tajemniczością. Clearnet to proza życia, więc nie budzi zainteresowania.

W każdym razie, według definicji, **_clearnet_ to te strony internetowe, które są indeksowane przez wyszukiwarki**.

A czym jest indeksowanie?  
Mam tutaj analogię botaniczną -- botanik znajduje nową, jeszcze nieopisaną roślinę. Żeby ją opisać, przyjmuje jakiś umowny *klucz*. Kwitnie czy nie? Jakie ma liście? W&nbsp;jakim rośnie klimacie?

Stopniowo uzupełnia informacje i&nbsp;dorzuca je do wielkiego światowego katalogu. A&nbsp;efekt końcowy jest taki, że inni ludzie będą mogli zajrzeć do indeksu roślin i&nbsp;znaleźć nówkę pod hasłem `kwiaty łąkowe Europy`.

Indeks przeglądarkowy jest pod tym względem podobny. Tylko że zamiast botanika mamy programy zwane *crawlerami*. Odwiedzają strony internetowe. Analizują ich tekst, obrazki, wydajność, powiązania z&nbsp;innymi stronami. Zapisują to, według przyjętego klucza, do swojej wewnętrznej bazy.

A efekt końcowy jest taki, że niektóre stronki będą nam wyskakiwały na liście wyników po wpisaniu hasła `carbonara przepis`.

{% include info.html
type="Ciekawostka"
text="Niedawno miał miejsce wyciek danych firmy Yandex, odpowiedzialnej za jedną z&nbsp;bardziej znanych wyszukiwarek. Dzięki temu zyskaliśmy możliwość zerknięcia za kulisy, sprawdzenia jakim „kluczem” przy doborze treści się kierują. Jeśli kogoś interesuje temat, to można [poczytać dyskusje](https://news.ycombinator.com/item?id=34577480)."
%}

## Deepnet

{:.post-meta .bigspace-after}
W tym miejscu porzucę analogię botaniczną, bo nie do końca pasuje -- nie ma na przykład opcji, żeby roślina nie zgodziła się na wpisanie jej do atlasu!

Niektórzy przypisują *deepnetowi* jakieś ciemne sprawki albo anonimizację. Ale mocno mijają się z techniczną definicją -- bo według niej **_deepnet_ to ta część internetu, która nie jest indeksowana**. I&nbsp;tyle, definicja nic nie mówi o&nbsp;zawartości stron.

Samo indeksowanie opisałem wyżej, porównując je do botanicznej klasyfikacji. Ale dlaczego niektóre strony nie są indeksowane? Przykładowe przyczyny:
 
* Strona jest na czarnej liście wyszukiwarki.

  Być może poprzedni właściciel próbował budować reputację na sztucznym ruchu i&nbsp;dostał karę. A&nbsp;nowy, po odkupieniu domeny, nadal tej karze podlega.

  Warto zaznaczyć, że każda wyszukiwarka może podchodzić do tematu po swojemu. Jak najbardziej może się zdarzyć, że ktoś jest w&nbsp;niełasce u&nbsp;Google'a, ale DuckDuckGo już by takową stronę wyszukało.

* Boty od wyszukiwarki jeszcze nie odkryły nowej strony.
* Właściciele strony proszą o&nbsp;to, żeby jej nie indeksować.

Ostatni punkt wyjaśnijmy sobie nieco dokładniej. Istnieje pewien umowny sposób, w&nbsp;jaki strony mogą wyrażać niechęć do ich indeksowania. Jest nim wpisanie odpowiednich rzeczy do pliku tekstowego nazwanego `robots.txt`, umieszczonego na tym samym serwerze co plik ze stroną.

{:.post-meta .bigspace-after}
**Aktualizacja:** jeśli wierzyć niektórym [komentarzom](https://news.ycombinator.com/item?id=36804706), zdarza się że strona i&nbsp;tak trafi do indeksu. Dla pewności można ustawić na każdej podstronce specjalne tagi, jak `noindex`. Tutaj skupię się jednak na *robotach*.

### Plik robots.txt

Wiele odwiedzanych przez nas stron ma coś takiego, zresztą sami możemy sprawdzić! W&nbsp;tym celu odwiedzamy interesującą nas stronę, patrzymy na nazwę jej domeny (czyli to, co przeglądarki często wyróżniają w&nbsp;pasku ciemnym kolorem). A&nbsp;następnie usuwamy wszystko, co po tej nazwie i&nbsp;dopisujemy po ukośniku `robots.txt`:

{:.bigspace}
<img src="/assets/posts/tor/clearnet-darknet/robots-txt-jak-znalezc.jpg" alt="Zrzuty ekranu pokazujące górny pasek przeglądarki. W&nbsp;pierwszym przypadku widzimy adres strony na Wikipedii, a&nbsp;w drugim po nazwie domeny dopisano słowa robots.txt"/>

Jeśli strona ma taki plik, to zobaczymy jego zawartość. Znajdziemy w&nbsp;nim [zestaw instrukcji](https://yoast.com/ultimate-guide-robots-txt/) w&nbsp;określonym formacie, przeznaczonych dla botów indeksujących.

To coś w&nbsp;rodzaju regulaminu na placu zabaw. Mówią na przykład, że dana strona sobie nie życzy, żeby przeszukiwały ją *crawlery*, których „wizytówka” zawiera tekst `Google`. Albo że wszystkie *crawlery* powinny zignorować niektóre podstrony.

Czasem trafiają tam również komentarze od autorów stron, wyjaśniające dlaczego zbanowali niektóre boty. Przykładem choćby nasza Wikipedia.

{% include info.html
type="Ciekawostka"
text="Czasem pliki `robots.txt` mogą być całkiem ciekawe. Niektórzy umieszczają w&nbsp;nich [smaczki dla zainteresowanych](https://www.wearedevelopers.com/magazine/the-funniest-robots-txt-files-only-developers-will-understand), przemyślenia, oferty pracy... A&nbsp;nawet grafikę. Tylko że siłą rzeczy w&nbsp;formie samego tekstu, jako *ASCII Art*. Przykład znajdziemy na końcu [instrukcji z&nbsp;*nike.com*](https://www.nike.com/robots.txt)."
%}

Kiedy stronę odwiedza grzeczny bot, to w&nbsp;pierwszej kolejności zagląda do `robots.txt`. Odczytuje, co mu wolno. Jeśli natrafi na polecenie „nie indeksuj mnie”, to odpuszcza. Strona nie jest indeksowana, czyli trafia do deepnetu. Oczywiście mogą istnieć boty niegrzeczne, które po prostu oleją takie instrukcje.

Widzimy zatem, że pojęcie deepnetu jest względne. Stronka może zabraniać indeksowania niektórym serwisom, ale pozwalać na nie innym.

Mamy też potwierdzenie, że słowa z&nbsp;artykułu Orange, który cytowałem na początku -- że deepnet nie jest dostępny z&nbsp;użyciem zwykłej przeglądarki (Firefoksa, Chrome'a itp.) -- są nieprawdziwe.  
Do deepnetu może należeć najzwyklejsza, prosta strona. Ktoś podrzuca link do niej, klikamy, normalnie się ładuje. Jej „deepnetowość” polega wyłącznie na tym, że na własną prośbę nie pojawi się w wyszukiwarkach.

### Deepnetujemy swój profil

Jeśli masz konto na Facebooku, czytelniczko lub czytelniku, to też **możesz łatwo przepchnąć swój profil do deepnetu**!

W tym celu wchodzisz w&nbsp;ustawienia konta, klikając swoje zdjęcie profilowe w&nbsp;prawym górnym rogu (mówię tu o&nbsp;wersji na komputery). Następnie wybierasz `Ustawienia i prywatność`, potem `Ustawienia`, potem `Prywatność`. Na koniec zaznaczasz opcję mówiącą o&nbsp;tym, żeby nie indeksowało Twojego konta w&nbsp;znanych wyszukiwarkach.

{:.post-meta .bigspace-after}
Instrukcje mogą się zmienić, gdyby Facebook zmienił kiedyś swoją stronę -- zaczerpnąłem je z&nbsp;[oficjalnej stronki](https://pl-pl.facebook.com/help/468080906543413/).

A czy takie ukrycie ma jakiś sens?  
Moim zdaniem tak! Zapewnia odrobinę ochrony przed mniej subtelnymi stalkerami -- takimi, którzy potrafią co najwyżej wpisać Twoje imię i&nbsp;nazwisko w&nbsp;Google, a&nbsp;następnie patrzeć, czy wyskoczyło coś związanego z&nbsp;mediami społecznościowymi.

{% include info.html
type="Porada"
text="Ale uwaga! Gdyby wpisali nasze imię i&nbsp;nazwisko w&nbsp;wewnętrzną wyszukiwarkę Facebooka, to już by znaleźli profil. Osoby chcące lepiej się ukryć powinny pokusić się również o&nbsp;zmianę nazwy konta. A&nbsp;także prowadzącego do niego linku; on również zawiera czasem imię i&nbsp;nazwisko."
trailer="<p>Nieprawdziwa nazwa była kiedyś wbrew regulaminowi platformy, i&nbsp;może nadal jest... Ale w&nbsp;najgorszym wypadku czeka nas ban konta, czyli też nic strasznego.</p>"
%}



### Deepnet a&nbsp;logowanie

Do *deepnetu* przyjęło się zaliczać nie tylko strony publicznie dostępne, które zabraniają się indeksować. To również wszelkie stronki wymagające logowania. Nasze konta bankowe, grupy na mediach społecznościowych, niejedno forum. Patrząc w&nbsp;ten sposób, **_deepnet_ byłby zdecydowanie największą częścią współczesnego internetu**.

Ale w&nbsp;tym miejscu nasza definicja -- do tej pory wyraźnie rozdzielająca dwa rodzaje stron -- moim zdaniem nieco się rozmywa. Mamy przypadki, kiedy strona jak najbardziej jest dostępna w&nbsp;wyszukiwarce, a&nbsp;więc indeksowana, ale stoi w&nbsp;rozkroku między światami. Przykładem wspomniany wyżej Facebook.

Strona *facebook.com* jak najbardziej jest widoczna w wyszukiwarce.  
Ale jeśli ją odwiedzimy bez odpowiednich plików cookies, wskazujących kim jesteśmy, to zobaczymy jedynie prośbę o&nbsp;login i&nbsp;hasło. Dopiero po zalogowaniu pokaże się coś więcej.  
Do czego zatem należy strona główna Facebooka? Clearnetu czy deepnetu?

{:.post-meta .bigspace-after}
Sprawa sięga zresztą nieco głębiej! Możemy być na Facebooku, ale nadal nie widzieć niektórych treści (jak posty na grupach, do których nie należymy; zdjęcia na profilach osób, których nie mamy w&nbsp;znajomych). Tak jakby istniał osobny, wewnętrzny clearnet i&nbsp;deepnet Facebooka.

Z kolei wiele stron portalu Github wygląda bardzo podobnie dla osób zalogowanych i&nbsp;niezalogowanych; jedyną różnicą u&nbsp;zalogowanych bywa górny pasek z&nbsp;nazwą konta i&nbsp;paroma opcjami. Czy to wystarczy, żeby zaliczyć cały portal do deepnetu?

Dalszą polemikę zostawię sobie na koniec wpisu. Chciałem tylko pokazać, że w&nbsp;świecie cyfrowym granice bywają płynne.

Na razie możemy sobie przyjąć taki podział: *clearnet* to strony, które są jednocześnie widoczne w&nbsp;wyszukiwarkach i&nbsp;zawierają coś więcej niż ekran logowania. *Deepnet* to wszystkie pozostałe.  
Teraz pozostaje nam jeszcze *darknet*, czyli pewna konkretna część *deepnetu*.

## Darknet

Nazwa brzmi nieco groźnie, nieprawdaż? *Dark* może po angielsku oznaczać *mroczny*, co kojarzy się z tymi medialnymi opowieściami o&nbsp;złoczyńcach i&nbsp;czarnych rynkach.

A tymczasem prawda jest dość prozaiczna. Poczynając od nazwy. Pojęcie *darknet* [istniało już w&nbsp;latach 70.](https://en.wikipedia.org/wiki/Darknet) i&nbsp;odnosiło się do tych serwerów, które były częścią sieci, ale nie odpowiadały na zapytania, nie wchodziły w&nbsp;interakcje.  
*Dark* oznacza nie tylko mrok w&nbsp;sensie negatywnym. Ale również zwyczajną ciemność, taką jak po wyłączeniu światła. Nieaktywność.

Od tego czasu definicja nieco się zmieniła i&nbsp;oznacza teraz **strony wymagające specjalnej konfiguracji albo korzystania z&nbsp;osobnych protokołów, żeby się do nich dostać**. Po ludzku -- nie da się tak po prostu wziąć ich adresu i&nbsp;go wkleić w&nbsp;pierwszą lepszą przeglądarkę.

Choć brzmi to bardzo restrykcyjnie, moim zdaniem pod darknet dałoby się podciągnąć zadziwiająco wiele rzeczy. Pod koniec wpisu pokażę parę przykładów do przemyślenia. Ale w&nbsp;mediach utarło się, że [darknet równa się Tor](https://news.ycombinator.com/item?id=10445538):

{:.bigspace}
>  It's strange how **they always identify \"Darknet\" as Tor**. There are other darknets like SIPRnet, JWICS, etc, and basically anything non-government groups want to spin up for their own purposes.

Tym razem nie będę szedł pod prąd i&nbsp;też użyję Tora w roli przykładu. Ale pamiętajmy, że tak naprawdę darknetów może być wiele.

## Tor Browser

Zacznijmy od ważnej rzeczy -- kiedy jedna osoba pisze drugiej „użyj Tora”, to w&nbsp;praktyce zwykle ma na myśli przeglądarkę Tor Browser.

Ale **Tor to coś ogólniejszego niż Tor Browser**. To *protokół*, metoda działania. Jeśli porównamy protokół Tora z&nbsp;typowym internetem:

* Nasz typowy internet stawia na szybkość. Przesyłane dane pokonują jak najkrótszą odległość.

* Tor stawia na anonimowość. Wysyłane dane przechodzą przez kilka „węzłów przesiadkowych” w&nbsp;różnych krajach. W&nbsp;ten sposób trudniej wyśledzić, kto je wysłał.

Ten protokół jest publicznie dostępny, więc mogą z&nbsp;niego korzystać dowolne programy. Nawet mieliśmy wcześniej przykład, kiedy jeden pracownik przejechał się na wersji umieszczonej w&nbsp;przeglądarce Brave.  
Twórcy Tora połączyli go z otwartym kodem Firefoksa... I tak powstał *Chocapic*{:.corr-del} Tor Browser, przeglądarka internetowa.

{% include info.html
type="Powiązane wpisy"
text="O tej przeglądarce wspominałem już w&nbsp;paru wpisach, pokazując jak można jej użyć do ominięcia [*geofencingu*](/internetowa_inwigilacja/2021/06/11/adres-ip#tor-browser){:.internal} (np. niewpuszczania europejskich adresów IP) albo [niektórych blokad](/2022/09/12/dns-ip-cenzura#vpn--tor){:.internal} stron internetowych.  
Była to tylko część jego możliwości; również ten wpis nie pokaże ich w&nbsp;całości, lecz tylko dołoży do układanki parę faktów.
"%}

**Tor Browsera można używać jak najzwyklejszej przeglądarki** i&nbsp;chodzić po stronach całkowicie *clearnetowych*. Jedyna różnica polega na tym, że Wasz prawdziwy adres IP jest ukryty przed oczami odwiedzanych stron, do tego działa parę bajerów chroniących prywatność. No i&nbsp;że przy każdym połączeniu „skaczecie” najpierw po świecie, przez co przeglądanie jest nieco wolniejsze.

{:.figure .bigspace-before}
<img src="/assets/posts/tor/clearnet-darknet/tor-ciemna-strona.jpg" alt="Górny pasek głównej listy wpisów z&nbsp;Ciemnej Strony, otwarty w&nbsp;przeglądarce Tor Browser"/>

{:.figcaption}
Mój skromny blog oglądany przez Tora.  
Ciekawostka: pusta przestrzeń po bokach to zabezpieczenie przed identyfikacją po rozmiarze okna.

### Strony typu Onion

Jeśli ktoś chce -- i&nbsp;tylko wtedy, bo nic na siłę -- to może odwiedzić przez Tora również inny, specjalny rodzaj stron, zwanych *onion services* (dawniej: *hidden services*). **To właśnie je media utożsamiają z&nbsp;_darknetem_**.

Spójrzmy tutaj na przykład -- [opis ich działania](https://tb-manual.torproject.org/onion-services/) na stronie głównej projektu Tor. Tu jego publicznie dostępny, *clearnetowy* adres: 

<div class="black-bg mono bigspace-before">
<span class="red">https://tb-manual.torproject.org</span>/onion-services/</div>

{:.figcaption}
Kolorem czerwonym wyróżniłem nazwę domeny.

Możemy go sobie zaznaczyć i&nbsp;wkleić w&nbsp;pasek popularnej przeglądarki. Strona normalnie nam się załaduje, o&nbsp;ile nasz dostawca internetu jej nie blokuje.  
Ale jeśli używamy Tor Browsera, to ten rozpozna, że stronka ma również wersję „cebulową”. W&nbsp;rogu wyświetli nam się napis `.onion available`.

{:.figure .bigspace}
<img src="/assets/posts/tor/clearnet-darknet/onion-services-alternative.jpg" alt="Komunikat wyświetlony przez Tor Browser, mówiący że odwiedzana strona ma swój odpowiednik typu Onion, pod spodem opcja przejścia w&nbsp;to miejsce" />

Możemy go kliknąć, żeby przejść na ukrytą wersję strony. Wygląd ten sam, adres inny:

<div class="black-bg mono bigspace">
<span class="red">http://dsbqrprgkqqifztta6h3w7i2htjhnq7d3qkh3c7gvc35e66rrcv66did.onion</span>/onion-services/index.html</div>

Gdybyśmy go wkleili do jakiejś mainstreamowej przeglądarki, nieznającej protokołu Tor, to byłaby lipa. Wyskoczyłby komunikat, że strona jest nieznana.

{% include info.html
type="Ciekawostka"
text="Wnikliwi zauważą, że adres zaczyna się od `http`, bez `s` na końcu.  
Ktoś mógłby się przestraszyć, bo w&nbsp;końcu w&nbsp;normalnym przypadku oznaczałoby to brak [szyfrowanego połączenia](/internetowa_inwigilacja/2022/08/13/https){:.internal}. Każdy podglądacz by widział, jakie dane wymieniamy ze stroną.  
Ale na szczęście nie jest tak źle! Połączenie z&nbsp;cebulowymi stronami [jest szyfrowane](https://security.stackexchange.com/a/105654) w&nbsp;inny sposób, dzięki protokołowi Tora.
"%}

I to tyle! Tak właśnie wygląda *darknet* związany z&nbsp;Torem. Stronki kończące się na `.onion`, które załadują się (prawie) wyłącznie w&nbsp;przeglądarce Tor Browser. Kiedy się z nimi łączymy, to nasza prawdziwa tożsamość jest mocno chroniona.

Ich zresztą też -- cebulowe stronki to rozwiązanie [chroniące „tożsamość” stron internetowych](https://community.torproject.org/onion-services/overview/), ich adres IP. Agresorom jest bardzo trudno je znaleźć i&nbsp;ubić.

## Jasne strony darknetu

A co można znaleźć w&nbsp;tym cebulowym *darknecie*? Pominę tu rzeczy mniej legalne, bo nie chcę być częścią medialnego szumu. Zamiast tego spójrzmy na przykłady, kiedy z&nbsp;dobrodziejstw anonimowej sieci skorzystali gracze znani lub dobrzy.

* W&nbsp;2014 roku twórca muzyki elektronicznej, Aphex Twin, [opublikował informacje o&nbsp;nowej płycie](https://twitter.com/AphexTwin/status/501383043643621376) właśnie na cebulowej stronce (już nieaktywnej).

* Na bazie Tora działa [SecureDrop](https://securedrop.org/), dający możliwość anonimowego przesyłania informacji różnym organizacjom medialnym.

  To sensowne rozwiązanie dla osób chcących np. ujawnić lokalną korupcję. Korzystanie z&nbsp;publicznej sieci byłoby groźne, bo złoczyńcy mogliby podpytać znajomków z&nbsp;firmy telekomunikacyjnej o&nbsp;personalia samotnych bohaterów. Tor częściowo przed tym chroni (acz nie całkiem, bo telekomy zwykle widzą sam fakt, że *coś* w&nbsp;nim robiliśmy).

* Swój adres `.onion` ma [Facebook](https://en.wikipedia.org/wiki/Facebook_onion_address), od 2014&nbsp;roku.

  Może to początkowo dziwić, patrząc na to że Facebook słynie ze zbierania danych.  
  Ale, jeśli się nad tym zastanowimy, wcale nie tracą na cebulce. Kiedy jesteśmy zalogowani na swoje konto, to Fejs i&nbsp;tak widzi naszą aktywność, nie ma na to rady.

  A&nbsp;do tego zyskuje szersze grono użytkowników -- ludzi ceniących prywatność oraz takich, których kraj blokuje Facebooka (Tor, jako pośrednik sieciowy, pozwala ominąć blokady stron).

* Ma go również Twitter.

  Motywacja pewnie jak wyżej. Po ostatnich zmianach kadrowych ktoś nie dopilnował sprawy i&nbsp;[cebulkowa wersja przestała działać](https://www.theverge.com/2023/3/7/23629504/twitter-tor-onion-site-security-certificate-expired) przez nieodnowienie certyfikatu na czas.

* ...I [wiele innych stron](https://en.wikipedia.org/wiki/List_of_Tor_onion_services).

Wcześniej widzieliśmy, że w&nbsp;clearnecie może być pełno mroku, a&nbsp;rzeczy ukryte są największą częścią internetu. Do burzenia światopoglądu doliczmy sobie teraz fakt, że mamy niemało dobra w&nbsp;anonimowym darknecie :wink:

## „Wszyscy siedzimy w&nbsp;darknecie”

{:.post-meta .bigspace-after}
Ta część to już moje subiektywne przemyślenia i&nbsp;kwestionowanie definicji. 

Jeśli dobrze rozumiem definicję, *darknet* jest podzbiorem *deepnetu*, a&nbsp;więc z&nbsp;założenia wyklucza się z&nbsp;clearnetem.

Ale na chwilę odejdźmy od ścisłej definicji. Intuicyjnie na darknet można patrzeć tak: „to strony, które ci się nie załadują, jeśli nie używasz czegoś nietypowego”.

A do takiego opisu pasowałoby moim zdaniem zadziwiająco wiele rzeczy, bo strony internetowe lubią rozgraniczać. Przykłady?

* Wersje stron przeznaczone dla *crawlerów*. 

  Automaty dostają czasem inne treści niż użytkownicy zwykłych przeglądarek. A&nbsp;są czymś absolutnie powszechnym -- według nowych danych stanowią [przeciętnie nawet 40% całego ruchu w&nbsp;internecie](https://www.securitymagazine.com/articles/99339-47-of-all-internet-traffic-came-from-bots-in-2022)  
  Mają specjalną konfigurację, widzą inny internet niż my. Czasem są większością w&nbsp;internecie. Czy w&nbsp;takich warunkach nie dałoby się przewrotnie stwierdzić, że to my, ludzie, mamy swój mniejszościowy darknet?

* Blokowanie adresów IP z&nbsp;wybranych krajów.

  Stosowane choćby przez stronki z&nbsp;USA, które nie lubią europejskich przepisów dotyczących ochrony danych.  
  Dla wielu osób zmiana adresu IP może być niemożliwa, więc nie zobaczą strony. A&nbsp;niektórzy zrobią specjalną konfigurację, jak włączenie VPN-a, i&nbsp;ją ujrzą.  
  Czy takie stronki nie są swego rodzaju darknetem?

### Rzeczy ukryte na widoku

Co więcej, może się nawet zdarzyć, że **strona pokazuje całkiem inną treść osobom znającym odpowiednik tajnego hasła**.

Przykładem jest odwiedzenie strony, gdy mamy w&nbsp;linku parametry o&nbsp;specjalnym znaczeniu.

{% include info.html
type="Wyjaśnienie"
text="Ogólnie: [parametry](/internetowa_inwigilacja/2021/04/09/internetowa-inwigilacja-parametry){:.internal} to tekst rozpoczynający się od znaku zapytania, który można dodać na końcu linku do strony.  
Często (nie zawsze) parametry nie mają wpływu na sam link i&nbsp;odwiedzana strona normalnie się bez nich załaduje. Ale jeśli są, to właściciel strony może na nie zerknąć. I&nbsp;na tej podstawie zachować się wobec nas inaczej niż wobec innych."
%}

Poniżej masz parametr, który możesz stąd skopiować i&nbsp;wkleić w pasek adresu swojej przeglądarki. Na samym końcu obecnego linku, bez żadnych spacji.

<div class="black-bg mono">
?tajnykod=1234567</div>

{% include info.html
type="Uwaga"
text="Żeby zadziałało, upewnij się, że w&nbsp;Twoim linku nie ma krzyżyka (`#`), który pojawia się, jeśli np. klikniesz w&nbsp;element spisu treści. Jeśli jest, to najpierw usuń jego i&nbsp;wszystko po nim, a&nbsp;dopiero potem wklej parametr."
%}

Jeśli w&nbsp;Twojej przeglądarce jest włączony kod JavaScript, to na początku tego wpisu, zamiast słów o&nbsp;siedzeniu w&nbsp;clearnecie, zobaczysz coś innego. 

{:.post-meta .bigspace-after}
Będzie tam też link pozwalający tu wrócić i&nbsp;uniknąć przewijania strony. Komfort czytelników przede wszystkim! :wink:

Ktoś powie: no dobra, ale to tylko tekst dodany do linku. Mała szansa, żeby ktoś to odkrył... Ale nie ma tu nietypowych konfiguracji czy protokołów, więc niezbyt podchodzi pod definicję *darknetu*.

Ale co byśmy powiedzieli, gdyby ktoś:

1. wziął publicznie dostępny kod źródłowy jakiejś przeglądarki (na przykład Chromium albo Firefoksa), 
2. dodał do niego regułkę sprawiającą, że podczas odwiedzania jakiejś strony będzie dodawało do linku tajne hasło,
3. utworzył z&nbsp;tego kodu przeglądarkę i&nbsp;zainstalował ją na wybranych komputerach?

W ten sposób, bez użycia żadnych nietypowych protokołów, mamy pełnoprawny efekt *darknetu* -- tylko wybrane urządzenia są w stanie zobaczyć ukryte treści na jakiejś stronie. Zwykli użytkownicy widzą coś innego.

{:.post-meta}
W moim przypadku nie jest to aż tak ukryte, bo nie mam wglądu do serwera. Korzystam z&nbsp;kodu JavaScript na stronie, widocznego dla wnikliwych. Ale w&nbsp;normalnej sytuacji parametry byłyby czytane na serwerze, poza oczami innych.

## Podsumowanie

Wizja mrocznych internetowych głębin przemawia do wyobraźni. Nic dziwnego, że media chętnie się do niej odwołują. Ale wywołują niemało szkód, zlepiając różne rzeczy w&nbsp;jedno. *Darknet, Tor, przestępstwa*. Te trzy rzeczy strasznie często pokazują razem.

Mam nadzieję, że mój wpis pokazał, że rzeczywistość jest bardziej złożona. Tor, warstwy internetu oraz sprawy legalności to trzy osobne zbiory, które nie muszą się przecinać.

Możemy używać Tora do zwykłego łażenia po publicznym clearnecie. Możemy znaleźć w&nbsp;tymże clearnecie rzeczy nielegalne, korzystając z&nbsp;pierwszej lepszej przeglądarki. Zaś deepnet, wbrew egzotycznej nazwie, to coś absolutnie powszechnego i&nbsp;nawet facebookowe profile mogą tam trafić.

Owszem, gdzieś istnieje styk trzech zbiorów. Tam Tor spotyka się z darknetem (strony typu *.onion*), a&nbsp;równocześnie z&nbsp;czymś nielegalnym.  
Ale takie miejsca nie są normą. Jeśli sami ich nie szukamy, to pewnie nigdy na naszej drodze nie staną. Dlatego nie ma sensu demonizować Tor Browsera oraz zapewnianej przez niego anonimowości. Bo kto wie, może nam się kiedyś przydać.

