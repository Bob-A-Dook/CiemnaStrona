---
layout: post
title:  "„Szkolny Big Brother” i jego wada wzroku"
subtitle: "Podglądanie szkolnego wi-fi nikogo nie ocali."
description: "Podglądanie szkolnego wi-fi nikogo nie ocali."
date:   2023-04-13 00:00:20 +0100
tags: [Apki, Internet, Inwigilacja, Podstawy]
image:
  path: /assets/posts/inwigilacja/szkola-big-brother/big-brother-szkola-baner.jpg
  width: 1200
  height: 700
  alt: "Schemat pokazujący strzałkami przepływ danych od telefonu komórkowego do anteny i potem do serwera. W dole widać samotny router, a nad nim ikonę oka ze łzą w kąciku"
---

Niedawno ukazał się [artykuł w&nbsp;„Gazecie Wyborczej”](https://wyborcza.pl/7,75398,29639901,szkolny-big-brother-do-szuflady.html) na temat systemu B3 (po angielsku czytałoby się jak *be free*, „bądź wolny”), przeznaczonego dla szkół.

Artykuł zawiera w&nbsp;opisie słowa: „Ten system może zapobiec samobójstwom dzieci. Ale raporty idą do szuflady”.

Tekst opiera się na założeniu, które może być groźne -- że ciągłe monitorowanie, co dzieci robią w&nbsp;internecie, byłoby drogą ku ich bezpieczeństwu.  
I że szkoły mają do dyspozycji świetny system do ich *śledzenia*{:.corr-del} ochrony. „Oparty o&nbsp;AI”. Który to system jest niestety mało używany, więc czas to zmienić.

Ale, choć spojrzenie na prywatność mam inne, ten wpis nie będzie polemiką. Zamiast tego pokażę w&nbsp;przystępny sposób ograniczenia takich systemów. Bo zarówno sam artykuł, jak i&nbsp;komentarze pod nim, przypisują B3 niestworzone cechy.

Zapraszam!

{% include info.html
type="Uwaga"
text="Osobiście interesuję się tematem cyfrowej prywatności jedynie hobbystycznie, a&nbsp;to temat pełen niuansów. Mój wpis nijak go nie wyczerpuje.  
Ale nie trzeba być fizykiem, żeby nieco wątpić w&nbsp;dziecięce przechwałki. „Mój tata to umie tak wysoko skakać, że doskoczy do Księżyca!”. A&nbsp;mniej więcej do tego sprowadzają się niektóre wyobrażenia na temat skuteczności systemu :wink:"
%}

### Spis treści

* [Szkoła nie widzi zbyt wiele](#szkoła-nie-widzi-zbyt-wiele)
  * [Przypadek skrajny -- szkolne komputery](#przypadek-skrajny--szkolne-komputery)
  * [Pierwsza przeszkoda: dane mobilne](#pierwsza-przeszkoda-dane-mobilne)
  * [Druga przeszkoda: szyfrowanie](#druga-przeszkoda-szyfrowanie)
  * [School-in-the-middle?](#school-in-the-middle)
  * [Metadane – hit czy kit?](#metadane--hit-czy-kit)
* [Uwaga o&nbsp;czytaniu Messengera](#uwaga-oczytaniu-messengera)
* [Firma Aiseclab](#firma-aiseclab)
* [Źródła obrazków](#źródła-obrazków)


## Szkoła nie widzi zbyt wiele

Na wstępie zaznaczę, że nie odnoszę się tu do możliwości *analitycznych* systemu&nbsp;B3.  
Możliwe, że jest w&nbsp;tym całkiem dobry. Że, karmiony strumieniami danych, umiałby wyłapywać w&nbsp;nich ciekawe zależności, sygnały wskazujące nałóg albo myśli samobójcze.

Ale z&nbsp;pustego i&nbsp;Salomon nie naleje. Mam mocne przeczucie, że w&nbsp;szkolnych realiach algorytm nie znalazłby dobrych danych wejściowych.

Artykuł wydaje się sugerować, że do B3 trafiają dane zebrane przez szkolne urządzenia -- komputery szkolne albo sieć wi-fi. Pierwsza opcja jest niezbyt praktyczna, a&nbsp;druga może dawać tylko śladowe informacje.

Zobaczmy, dlaczego tak jest.

{% include info.html
type="Uwaga"
text="Artykuł odnosi się do usługi podpiętej pod konkretną sieć -- OSE. Mógłbym teoretycznie poczytać ich instrukcje i&nbsp;opisać ograniczenia na tej podstawie.  
Ale zamiast tego będzie nieco ogólniej. Pokażę informacje bardziej uniwersalne. Prawdziwe zarówno w&nbsp;przypadku tej konkretnej sieci, jak i&nbsp;pozostałych."
%}

### Przypadek skrajny – szkolne komputery

**Korzystanie z&nbsp;cudzego urządzenia oznacza brak prywatności**. To ogólna zasada, a&nbsp;wyjątki są na tyle nieliczne, że pozwolę sobie je zignorować.

To dlatego, że nie wiemy, co ktoś wcześniej zainstalował na komputerze, do którego siadamy. Może być naszpikowany programami śledzącymi.

Nawet jeśli wysyłamy między sobą szyfrowane wiadomości, to przecież w&nbsp;którymś momencie musi nastąpić odszyfrowanie. Żebyśmy zobaczyli ich tekst na ekranie. A&nbsp;gdzieś na tym etapie program-podglądacz może po prostu chwycić tę treść i&nbsp;do niej zerknąć.

A to tylko jedna z&nbsp;wielu opcji. Programy mogą na bieżąco kopiować obraz widoczny na ekranie, odczytywać z&nbsp;niego tekst. Albo [rejestrować każde naciśnięcie klawiszy](https://pl.wikipedia.org/wiki/Keylogger) i&nbsp;odtwarzać sobie, co napisaliśmy. Wszystko potajemnie.

Werdykt? Gdy uczniowie korzystają z&nbsp;komputerów szkoły, to faktycznie mogłaby widzieć wszystko, co robią.  
Ale techniczna możliwość to tylko pierwszy krok. Poza nią istnieje szereg przeszkód, które raczej skreślają taką formę zbierania danych. I&nbsp;pomińmy nawet kwestie prawne.

* Lekcje informatyki odbywają się tylko parę razy w&nbsp;tygodniu; zakładam optymistycznie, że czasem uczniowie się na nich uczą, a&nbsp;nie tylko mają czas dla siebie :wink:
* Nawet gdy mają czas, to niekoniecznie zaczną czytać o&nbsp;drażliwych tematach, kiedy po bokach siedzą rówieśnicy.

  Czy wyobrażamy sobie na przykład, że jakaś prześladowana osoba zaczyna czytać depresyjne blogi albo opisywać komuś swój stan, kiedy każdy może jej zerknąć w&nbsp;ekran?

* Obecnie czymś absolutnie powszechnym jest korzystanie z&nbsp;telefonów i&nbsp;aplikacji.

  Platformy (jak Instagram, TikTok) są przystosowane do smartfonów. Zaś ich wersje komputerowe są na tyle ograniczone, że mogłyby tylko odstraszać uczniów.

Podsumowując: szkolne komputery mogłyby zdobyć pełno danych. Ale ze względu na realia (wiele osób w&nbsp;jednej sali, interfejsy mniej lubiane przez młodych) drastycznie spada szansa, że zdobędą jakieś informacje o&nbsp;problemach uczniów.

Drugim potencjalnym zbieraczem jest sieć wi-fi. A&nbsp;ta z&nbsp;kolei ma potężne ograniczenia.

### Pierwsza przeszkoda: dane mobilne

Korzystanie z&nbsp;internetu przypomina często korespondencję. Wysyłanie listów między nami a&nbsp;właścicielami strony, na którą zaglądamy.

Zaufane apki korzystające z&nbsp;internetu (przeglądarka, komunikatory...) są jak poczta.  
Mówimy, że chcemy się z&nbsp;kimś skontaktować. Za kulisami szykują naszą prośbę, a&nbsp;po jakimś czasie powinniśmy otrzymać odpowiedź od adresata.  
Szkoła nie ma możliwości przechwycenia danych prosto od apek.

**Infrastrukturę sieciową**, jak routery, można z&nbsp;kolei porównać do firmy kurierskiej. Bierze przesyłki od poczty i&nbsp;zawozi je we wskazane miejsce.  
W naszym modelu **to właśnie w&nbsp;tym miejscu może dochodzić do podglądania**. „Firma może zatrudniać wścibskich listonoszy”.

{:.post-meta .bigspace-after}
Pst, spoiler. Dzięki szyfrom to nie będzie takie proste.

Połączenie się ze szkolnym hotspotem jest jak wskazanie wszystkim naszym placówkom pocztowym: „korzystajcie z&nbsp;usług EduKuriera”.  
Od teraz poczta powierza im naszą korespondencję. A&nbsp;oni teoretycznie mogliby przed dostarczeniem wrzucać ją do systemu B3, analizującego jej zawartość.

W naszym przypadku tym „EduKurierem” -- dostawcą routerów i&nbsp;jednocześnie zbieraczem informacji -- byłaby [Ogólnopolska Sieć Edukacyjna](https://ose.gov.pl/faq/czym-jest-ose) (OSE).

...Ale co, jeśli uczniowie z&nbsp;żadnym hotspotem się nie połączą?

{:.bigspace-before}
{% include comment.html
source="twitter"
author="Jerzy"
text="Pomijając kwestię etyczną, jak rozumiem ten system bada tylko dane przesyłane przez wewnętrzną sieć szkoły. Uczniowie z&nbsp;niej nie korzystają, używając własnych komórek. Czyli właściwie jaki ruch miałby być inwigilowany? 45&nbsp;minut lekcji informatyki przez tydzień?"
%}

{:.figcaption}
Źródło: [dyskusja z&nbsp;Twittera](https://nitter.cz/mk_wronski/status/1645680797041541122#m). Gdyby Nitter nie działał, to można zmienić *nitter.cz* na *twitter.com*.

Obecnie często korzysta się z&nbsp;danych mobilnych. Wtedy to operatorzy sieci, tacy jak Play albo Orange, odpowiadają za nasze internetowe wojaże. Jeśli uczeń nie wybierze ręcznie, że chce korzystać ze szkolnego hotspota, to szkoła nie dostanie zupełnie nic.

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/szkola-big-brother/wifi-off-mobile-on.jpg" alt="Dwie ikony umieszczone obok siebie. Jedna na szaro, nieaktywna, podpisana Wi-Fi. Aktywna na niebiesko, podpisana Dane Mobilne" style="max-width:20%"/>

<img src="/assets/posts/inwigilacja/szkola-big-brother/dane-mobilne-bez-routera.jpg" alt="Rysunkowy schemat pokazujący, jak strzałka odchodzi od telefonu komórkowego w&nbsp;kierunku anteny, a&nbsp;następnie do serwera. W&nbsp;dolnej części schematu widać router z&nbsp;czerwoną obwódką, do którego nie prowadzi żadna strzałka. Jest na niego nałożona ikonka oka ze łzą w&nbsp;kąciku." />

{:.figcaption}
Źródło elementów: Flaticon i&nbsp;Emojipedia. Szczegóły pod koniec wpisu.

Szkoła może co najwyżej zachęcać. Internet szybszy niż w&nbsp;komórce! Mniejsze zużycie danych mobilnych!  
Ale gdy część uczniów się połączy i&nbsp;zacznie zasysać filmy z&nbsp;TikToka, to internet zwolni dla pozostałych. Wtedy **mogą wrócić do swojego internetu mobilnego. A&nbsp;szkoła nie ma nad tym kontroli**.

{:.post-meta}
Chyba że w&nbsp;jakiś sposób OSE dogadałaby się z&nbsp;telekomami i&nbsp;dostawała od nich wszystkie dane. Ale to raczej nierealne. 

### Druga przeszkoda: szyfrowanie

Załóżmy, że jednak udało się zachęcić uczniów do tego szkolnego hotspota. Czy od teraz wszelkie prywatne sprawki polecą do systemu B3 szerokim strumieniem?

Raczej nie. Bo we współczesnym świecie **prawie cała komunikacja internetowa jest szyfrowana**.

Dotyczy to komunikatorów, takich jak Signal czy Messenger. Apek, jak TikTok czy Instagram.  
Nawet kiedy po prostu przeglądamy zakamarki internetu (przez Firefoksa, Brave'a, Tora, Operę...), to odwiedzenie stronki zaczynającej się od `https` oznacza, że nikt nie powinien podejrzeć naszych danych.

Ba, nie tylko danych! Nie zobaczy nawet ogólniejszych informacji, takich jak pełen adres strony. Zobaczmy na przykładzie.

Załóżmy, że uczennica imieniem Magda ma czarne myśli. Odwiedza stronę *blog-juli.pl* (zmyślona, nie było takiej w&nbsp;dniu pisania posta), gdzie pewna Jula dzieli się myślami. Kiedyś były tam porady, z&nbsp;czasem coraz bardziej ponure rzeczy.

Magda czyta szczególnie depresyjny post i&nbsp;dodaje pod nim komentarz mówiący, że też myśli o&nbsp;najgorszym.  
Oto, co mogłyby zobaczyć osoby monitorujące ruch sieciowy, gdyby blog Juli był oparty o&nbsp;HTTP.

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/szkola-big-brother/dane-przyklad-http.jpg" alt="Obrazek pokazujący tekst na niebieskim tle. Wyróżnione są trzy nagłówki. Pod pierwszym, Metadane, widać nazwę strony blog-juli.pl oraz jego adres IP. Pod drugim, Nagłówki HTTP, jest trochę informacji technicznych, w&nbsp;tym pełniejsza nazwa strony, układająca się w słowa 'mam dość życia'. Pod ostatnim, Wysłane Dane, widać przykładową treśc komentarza mówiącą 'Też już mam dość'."/>

{:.figcaption}
Informacje uproszczone, nazwy pól zmieniłem. JSON niepoprawny.

Ale jeśli włączyła u&nbsp;siebie HTTPS (co na niektórych hostingach jest kwestią jednego pstryczka), czyli szyfrowaną wymianę danych, to obserwatorzy widzieliby takie coś:

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/szkola-big-brother/dane-przyklad-https.jpg" alt="Obrazek identyczny jak poprzednio, ale tym razem wszystko poniżej metadanych jest zakryte jednolitym szarym prostokątem. W&nbsp;jego rogu znajduje się ikona kłódki."/>

Dowiedziliby się tylko, że Magda nawiązała ze stronką Juli szyfrowaną korespondencję. A&nbsp;potem już nieprzeniknione, zaszyfrowane bryły. Patrząc tylko na ruch sieciowy, nie widzieliby, jakie podstrony odwiedzała dziewczyna, ani na czym polegały jej interakcje. Widzieliby tylko:

* rozmiar przesyłanych danych,
* czas ich przesłania,
* najogólniejszy adres odwiedzanych stron (domenę).

  A&nbsp;gdyby ktoś używał pośrednika sieciowego (*proxy*, VPN, Tor), to ta ostatnia informacja byłaby bezużyteczna.

I zanim ktoś spróbuje się naindyczać, że brak HTTPS-a by tu pomógł, a&nbsp;zatem może trzeba go zakazać -- myślę że znacznie więcej osób zostałoby poszkodowanych taką zmianą. Przechwycone hasła bankowe, prywatna korespondencja użyta potem do szantażu...

Uderzając w&nbsp;szyfrowanie, pewnie posłałoby się do grobu więcej osób, niż by się znad niego wyciągnęło. Może lepiej się skupić na wsparciu w&nbsp;świecie fizycznym? Albo na walce z&nbsp;efektami, jakie wywierają na psychikę produkty cyfrowych korpo?

{% include info.html
type="Powiązane wpisy"
text="Mam na blogu osobny wpis, [dokładniej omawiający HTTPS-a](/internetowa_inwigilacja/2022/08/13/https){:.internal}.  
To przydatny sposób na podglądaczy z zewnątrz... Ale nie pomoże przeciw stronom, które odwiedzamy. Mam całą serię na temat informacji, jakie mogą o&nbsp;nas zgromadzić. Począwszy od [wpisu o&nbsp;nagłówkach HTTP](/internetowa_inwigilacja/2021/01/11/internetowa-inwigilacja-1-podstawy){:.internal}."
%}

### School-in-the-middle?

Teoretycznie istnieje sposób, w&nbsp;jaki szkoła mogłaby przechytrzyć HTTPS. Ale, jak wszystko do tej pory, metoda ma spore ograniczenia.

Szyfrowana wymiana odbywa się w&nbsp;kilku etapach:

1. Wysyłamy prośbę o&nbsp;szyfrowany kontakt.
2. Jeśli stronka internetowa się zgodzi, to odsyła nam odpowiednik otwartej kłódki.  
   Coś, co samo w&nbsp;sobie nie jest tajemnicą, ale pozwoli chronić tajemnice. Klucz do niej trzyma u&nbsp;siebie.
3. My również odsyłamy swoją kłódeczkę, nie dzieląc się kluczem.
4. Od tej pory wysyłamy sobie rzeczy w&nbsp;pancernych sejfach; każdy zamknięty na kłódkę drugiej strony, którą tylko ona może otworzyć.

{:.post-meta .bigspace-after}
Mój opis to przede wszystkim intuicja; jeśli kogoś interesują technikalia, to fajny opis ma [stronka Moserware](http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html).

Gdyby te wszystkie przesyłki szły przez szkolny router, to ten **mógłby „stanąć na drodze” korespondencji**. Przechwycić kłódkę naszego adresata, wyrzucić ją do kosza, wysłać nam zamiast niej swoją własną (do której ma klucz). To samo w&nbsp;drugą stronę.

Od tej pory mógłby czytać korespondencję obu stron. Taki atak nosi nazwę [MITM](https://pl.wikipedia.org/wiki/Atak_man_in_the_middle). *Man-in-the-Middle*, „Człowiek pośrodku”.  
I nie jest jakąś moją fantazją, tylko [realiami w&nbsp;niektórych organizacjach](https://security.stackexchange.com/questions/107542/is-it-common-practice-for-companies-to-mitm-https-traffic).

Tylko że szans na tajny podsłuch to tu nie ma. Właściciel strony korzystającej z&nbsp;HTTPS dostaje od „producenta kłódek” swoje własne, tylko dla siebie. Oznaczone certyfikatem producenta.  
Zaś zamkniętą listę zaufanych certyfikatów trzyma u&nbsp;siebie nasza przeglądarka.

Jeśli zatem Magda pisała do stronki *blog-juli.pl*, a&nbsp;dostanie w&nbsp;odpowiedzi kłódkę *szkolny-wielki-brat.org*, to jej przeglądarka się zorientuje. I&nbsp;wyświetli wielkie, groźne ostrzeżenie. Czasem da się przez nie przeklikać, ale zwykle odstraszy ludzi.

{:.post-meta .bigspace-after}
Jeśli ktoś chce zobaczyć przykład, to można odwiedzić [demo na stronce *badssl.com*](https://self-signed.badssl.com/).

Szkoła mogłaby teoretycznie wyciszyć ostrzeżenia, prosząc uczniów o&nbsp;dodanie jej certyfikatów do tej przeglądarkowej listy dozwolonych. Tak już robił [co najmniej jeden amerykański college](https://security.stackexchange.com/questions/104576/my-college-is-forcing-me-to-install-their-ssl-certificate-how-to-protect-my-pri).

Ale w&nbsp;wątku widać, jakie wzbudziło to oburzenie. Poza tym wymaga odrobiny zabawy z&nbsp;technikaliami. Wielu uczniów na tym etapie by zapewne uznało, że szkoda zachodu i&nbsp;woli jednak używać danych mobilnych.

Pomińmy już fakt, że to wszystko dotyczy wyłącznie *przeglądarki*. Która siłą rzeczy musi być elastyczna w&nbsp;kwestiach internetu, więc dopuszcza alternatywne certyfikaty.  
Zaś inne aplikacje mogą mieć w&nbsp;siebie wkodowane [instrukcje absolutne](https://approov.io/blog/how-certificate-pinning-helps-thwart-mobile-mitm-attacks). „Ufaj tylko kłódce od *facebook.com*. I&nbsp;żadnej innej”.

### Metadane – hit czy kit?

Szkoła zostanie najprawdopodobniej z&nbsp;samymi ogólnikami. Metadanymi. Czy są w&nbsp;stanie ujawnić cokolwiek o&nbsp;nastroju uczniów?  
Właściwie tylko wtedy, kiedy sama nazwa odwiedzanej strony coś sugeruje. Jak `mam-straszna-depresje.pl` (zmyśliłem, nie patrzyłem czy istnieje).

W innym razie? Ogólnie rzecz biorąc, **z&nbsp;metadanych da się trochę wyczytać. Ale raczej w&nbsp;dłuższym okresie**. Gdy widzimy czyjeś zachowanie dzień w&nbsp;dzień, bo na przykład jesteśmy firmą telekomunikacyjną. 

Szkoła nie ma takiej opcji, bo widzi dzieci tylko przez wycinek ich dnia. I&nbsp;to ten, kiedy mogą nie mieć poczucia prywatności, więc się nie zwierzają ani nie szukają prochów w&nbsp;sieci.

A nawet jeśli coś robią, ale tylko przez większe platformy, to i&nbsp;tak system nie wyłapie nic ciekawego.

* Wiadomość z&nbsp;Messengera. Jedna, druga, dziesiąta, raczej krótkie. Ale szyfrowane, zero wglądu w&nbsp;ich treść.
* `google.com`, czyli wyszukiwarka. Ale nie wiemy, czy ktoś szukał zioła, czy sklepu papierniczego -- o&nbsp;ile z&nbsp;Google'a nie przejdzie na kolejną stronę, o&nbsp;jednoznacznej nazwie.
* `reddit.com`, `wykop.pl`. Wielkie fora o&nbsp;wszystkim. Podglądana osoba czytała wpisy optymistyczne czy nihilistyczne? Nie dowiemy się.

Istnieje *bardzo szczególny przypadek*, kiedy rozmiar danych w&nbsp;połączeniu z&nbsp;nazwą strony mógłby coś ujawnić. Ale musiałaby to być stronka publicznie dostępna i&nbsp;nieduża, możliwa do zmapowania. Jak mój blog.

Załóżmy, że dorzuciłem tu długi, depresyjny filmik (jak [„The Corporation”](https://www.youtube.com/watch?v=Y888wVY5hzw), polecam!). Wyróżniający się rozmiarem wśród tekstu i&nbsp;obrazków.

Osoba analizująca ruch mogłaby zdobyć informację, że jakiś uczeń wszedł na `ciemnastrona.com.pl` i&nbsp;pobrał jednym cięgiem kilkaset MB danych. Potem sama poszperałaby po mojej stronie i&nbsp;odkryła, że jedynie depresyjny filmik pasuje do wzorca. Wniosek: uczeń go obejrzał, trzeba się nim zająć.

Ale to opcja nierealna przy większych platformach albo prywatnej komunikacji.

O ile nie trafią się jakieś ciekawe nazwy domen, a&nbsp;jedynie popularne usługi, szkoła mogłaby co najwyżej oceniać czyjś stopień uzależnienia albo preferowane apki.  
„Wysyła dane cały czas, nawet podczas zajęć. To nałóg”.  
„Dużo Instagrama, może nabawić się kompleksów”.

Ale nie dowie się, co dana osoba ma w&nbsp;głowie. I&nbsp;może dobrze?

## Uwaga o&nbsp;czytaniu Messengera

Wszystkie rzeczy wyżej to teorie, bo nie wczytywałem się w&nbsp;działanie tego konkretnego systemu. Ale pewne rzeczy są niezmiennikami, nie do przeskoczenia.  
Jak wysportowany nie byłby rodzic, nie podskoczy do Księżyca.

Tym bardziej mnie zdziwiło jedno zdanie, które pojawia się w&nbsp;[artykule](https://wyborcza.pl/7,75398,29639901,szkolny-big-brother-do-szuflady.html):

{:.bigspace}
> \[system\] błyskawicznie się zorientuje, o&nbsp;co tak naprawdę chodzi. Wystarczy że uczeń, wysyłając wiadomość, np. na Messengerze, dołączy zdjęcie

Osobom widzącym tę luźną wzmiankę o&nbsp;czytaniu Messengera może się tutaj zapalić czerwona lampka w&nbsp;głowie. I&nbsp;nie dlatego, że to narusza prywatność. Tylko dlatego, że **to praktycznie niemożliwe od strony technicznej**.

Co gorsza, nie jest są to jakieś domysły dziennikarzy; **to słowa samego założyciela firmy**. Autorów systemu.

Jak pisałem wyżej, dane przesyłane przez Messengera oraz większość aplikacji są szyfrowane. Zwyczajnie nie ma możliwości dobrania się do nich przez samo przeglądanie ruchu sieciowego.

Ale, szukając jakiegoś wyjaśnienia, możemy pomyśleć o&nbsp;czymś jeszcze.  
A gdyby szkoła zachęcała uczniów do zainstalowania własnej aplikacji? Czy ta mogłaby wtedy czytać wiadomości z&nbsp;Messengera?

### Apka apce tajniakiem

To całkiem rozsądne pytanie! Zwłaszcza jeśli ktoś wychował się na komputerach osobistych, gdzie jeden program może zaglądać do drugiego. Nieraz *cheaty* do gier opierały się wręcz na aktywnym podmienianiu kodu.

Tylko że **w przypadku aplikacji mobilnych jest inaczej -- jedna apka nie może zaglądać do plików innej**. Każda ma swoją prywatną przegródkę.

Chcąc zajrzeć do pliku -- jakiegokolwiek -- apka prosi system o&nbsp;zgodę.  
Jeśli ma pozwolenie na dostęp do wspólnej przestrzeni, to może czytać umieszczone w&nbsp;niej pliki.

Ale, pomijając celowe majsterkowanie, zwyczajnie nie istnieje coś takiego jak „dostęp do plików prywatnych innej apki”.

{:.post-meta .bigspace-after}
Gdyby ktoś był zainteresowany tematem, to nieco więcej napisałem we [wpisie o&nbsp;plikach]({% post_url 2022-11-16-apki-pliki %}){:.internal} z&nbsp;serii „Apki to pułapki”.

Czyli nie da się przez router. Nie da się przez inną apkę. To jak z&nbsp;tym czytaniem wiadomości Messengera?

Dostęp do nich dałoby się uzyskać tylko na kilka sposobów. Z&nbsp;czego jeden wymaga sporo zachodu i&nbsp;świadomego działania ucznia. Drugi mogłyby wykorzystać osoby z&nbsp;zewnątrz, ale jest nielegalny: 

* Można [celowo zmodyfikować](https://security.stackexchange.com/questions/149325/disable-or-bypass-ssl-pinning-certificate-pinning-on-android-6-0-1) plik z&nbsp;apką, żeby podmienić „akceptowane kłódki” na model, do którego mamy klucz.

  Ale to wymaga świadomego, czasem mozolnego działania. Poza zasięgiem wielu zapalonych majsterkowiczów, a&nbsp;tym bardziej uczniów i&nbsp;szkoły.

* Można -- poprzez Pegasusa albo podobne cudo -- zhakować telefon.

  W&nbsp;ten sposób uderzano w&nbsp;niektórych polityków i&nbsp;aktywistów. Ale szpiegowanie uczniów, zwłaszcza na większą skalę niż dzieci konkretnych osób, nie wchodzi w&nbsp;grę.

Podsumowując: nieco wątpię w&nbsp;tę możliwość swobodnego czytania Messengera. Być może trafiła do artykułu wskutek jakiegoś wyrwania z&nbsp;kontekstu. Albo głuchego telefonu. Albo czegoś.

{% include info.html
type="Ciekawostka"
text="Komuś mogło się obić o&nbsp;uszy, żeby lepiej korzystać z&nbsp;Signala, a&nbsp;nie Messengera, bo ten pierwszy ma *szyfrowanie end-to-end*. Czy to nie sugeruje, że jednak da się dobrać do Messengera?  
Nie, to osobna kwestia. Po prostu korzystając z&nbsp;Messengera, nie jesteśmy chronieni *przed samym Facebookiem*, bo ten ma po drodze wgląd do wiadomości.  
Signal takiego wglądu nie ma, chroni nas nawet przed swoimi autorami.  
Nie zmienia to jednak faktu, że oba komunikatory są odporne na *osoby podglądające z&nbsp;zewnątrz*."
%}

## Firma Aiseclab

Czytając artykuł z&nbsp;gazety, mógłbym łatwo się podjarać i&nbsp;ulec przysłowiowemu *hype'owi*.  
„Nowoczesny system!”. „Kupują go firmy z&nbsp;Fortune&nbsp;500 i&nbsp;agencje rządowe!”. „Szkoły na razie nie mają, ale może wkrótce będą miały!”.

Inwestor entuzjastyczny mógłby w&nbsp;tej sytuacji brać i&nbsp;kupić cokolwiek, co pozwoli mu mieć udziały w&nbsp;odpowiedniej spółce.  
Ale można również inwestować w&nbsp;oparciu o&nbsp;dane. Na przykład zaglądając do [oficjalnej wyszukiwarki KRS-u](https://wyszukiwarka-krs.ms.gov.pl/) i&nbsp;wpisując nazwę firmy.

{:.post-meta .bigspace-after}
Oczywiście nikomu nic nie doradzam ani nie odradzam. Każdy inwestuje za siebie :wink:

Aiseclab Sp. z&nbsp;o.o. Ich numer KRS to 0000549170.

Z rejestru możemy pobrać pełen odpis, czyli historię zdarzeń z&nbsp;życia spółki. A&nbsp;następnie zwizualizować sobie, chociażby [moim skryptem](/tutorials/krs-wykresy){:.internal}, co tam się w&nbsp;niej działo.

Nazwa firmy niezmienna od lat, prezes -- niezmienny. Pewna dynamika była natomiast na liście udziałowców:

{:.bigspace}
<img src="/assets/posts/inwigilacja/szkola-big-brother/aiseclab-krs.jpg" alt="wykres pokazujący historię zmian udziałowców w&nbsp;firmie Aiseclab"/>

Widzimy, że od pewnego czasu niezmiennie jest tu para osób o&nbsp;tym samym nazwisku. Nie rodzeństwo, bo dwa miesiące różnicy, więc obstawiam męża i&nbsp;żonę.  
Od końca lipca 2018&nbsp;r. dołączyła spółka T-Hub.

Zaś od marca 2022&nbsp;roku -- EquiTech. FIZAN, czyli Fundusz Inwestycyjny Zamknięty Aktywów Niepublicznych. Forma dość egzotyczna, więc aż poszukałem o&nbsp;niej [informacji](https://www.linkedin.com/pulse/fizan-co-takiego-i-czy-warto-go-wybra%C4%87-kamila-napiera%C5%82a):

{:.bigspace}
> FIZAN podlegają szczególnym ograniczeniom ustawowym, jak i&nbsp;kontrolnym. Oznacza to tyle, że niewiele jest o&nbsp;nich informacji ogólnodostępnych, ponieważ takie informacje mogą być kierowane wyłącznie do jego uczestników, czyli posiadaczy certyfikatów. \[oferta\] może być skierowana jedynie do 149&nbsp;inwestorów, a&nbsp;minimalna kwota inwestycji, zgodnie z&nbsp;zapisem ustawowym, stanowi równowartość kwoty 40.000 EUR

No cóż, trochę za wysoka dla mnie ta kwota wejścia. Przy tym konkretnym funduszu zastanawia też nieco [wzmianka z&nbsp;2021&nbsp;roku](https://pap-mediaroom.pl/biznes-i-finanse/komunikat-knf-16) na stronie PAP:

{:.bigspace}
> \[KNF nakłada karę na MM Prime\] w&nbsp;wysokości 100&nbsp;000 złotych za niedokonanie wypłaty całości kwoty \[uczestnikom obecnego\] EquiTech Fundusz Inwestycyjny Zamknięty Aktywów Niepublicznych
 
Nieco też mnie zaskoczyło, że można dostać przyrostek „w&nbsp;likwidacji” ([pod koniec 2020&nbsp;roku](http://komunikaty.rp.pl/komunikaty/KomunikatPdf/65953)), a&nbsp;potem jeszcze sobie raźno zdobywać udziały. Taki trochę fundusz-zombie.

Samemu Aiseclabowi pozostaje życzyć więcej szczęścia niż spotkało jego udziałowca. Gdyby byli w&nbsp;stanie czytać wiadomości z&nbsp;uczniowskich Messengerów, to całkiem możliwe, że ich algorytm odnalazłby w&nbsp;nich skarby.

## Źródła obrazków

Schemat pokazujący użycie danych mobilnych zamiast wi-fi:

* [smartfon](https://emojipedia.org/mobile-phone/) -- Emojipedia, wariant JoyPixels;
* [maszt telefoniczny](https://www.flaticon.com/free-icon/antenna_2911949) -- Flaticon (autor: Freepik);
* [router](https://www.flaticon.com/free-icons/router) -- Flaticon (autor: *vectorsmarket*);
* [strzałki](https://www.flaticon.com/free-icons/down-arrow) -- Flaticon (autor: Freepik);
* [serwer](https://www.flaticon.com/free-icons/server) -- Flaticon (autor: Smashicons);
* [oko](https://emojipedia.org/eye/) -- Emojipedia, wariant WhatsAppa;
* [łza](https://emojipedia.org/droplet/) -- Emojipedia, wariant Samsunga;
* kartka -- ikona z&nbsp;systemu Linux Mint.

Modyfikacje moje.



