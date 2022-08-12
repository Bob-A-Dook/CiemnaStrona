---
layout: post
title:  "Internetowa inwigilacja – wielkie podsumowanie"
subtitle: "„Czy jesteś w stanie wygrać?”"
description: "„Czy jesteś w stanie wygrać?”"
date:   2022-08-12 11:37:00 +0100
tags: [Centralizacja, Internet, Inwigilacja, Porady]
firmy: [Facebook, Google, Reddit, Twitter]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: "inwigilacja_podsumowanie/allsing-baner.jpg"
image-width: 1200
image-height: 700
---

Serię „Internetowa inwigilacja” tworzę już od ponad półtora roku. Zebrało się do tej pory jedenaście wpisów omawiających metody, z&nbsp;jakich korzystają właściciele stron internetowych, żeby zbierać o&nbsp;nas informacje. 

Zwykle robią to w&nbsp;celach reklamowych. Ale w&nbsp;praktyce każda raz stworzona baza danych (nasza „teczka”) może zostać nadużyta. Również przez obcych.  
Przykład: baza danych, która [wyciekła kiedyś Facebookowi](https://niebezpiecznik.pl/post/facebook-wyciek-dane-533-milionow-uzytkownikow/), zawierała numery telefonów, daty urodzenia, ogólne miejsce zamieszkania. Idealny punkt wyjścia dla oszustów działających metodą „na wnuczka”.

Czas uporządkować luźne strzępki informacji o&nbsp;śledzeniu! Żeby lepiej nam zapadły w&nbsp;pamięć, przyjmę konwencję gry planszowej.

To gra o&nbsp;wysoką stawkę. Jeśli wygramy, pomożemy bliskiej osobie i&nbsp;zyskamy możliwość życia na własnych zasadach.  
Jeśli przegramy, wszystkie nasze dane wyciekną na widok publiczny i&nbsp;zostaniemy wykluczeni ze społeczeństwa.

Grę czas zacząć! :fire:

{% include info.html
type="Uwaga"
text="Informacje będą tu raczej płytkie, ale różnorodne. **Znajomość moich poprzednich wpisów nie jest wymagana**, ale zawierają więcej szczegółów. W&nbsp;odpowiednich miejscach będę do nich odsyłał.  
Jeśli kogoś ciekawią wyłącznie porady dotyczące realnego świata, to można przeskoczyć prosto do [ostatniej części wpisu](#jak-wygrać)."
%}

# Spis treści

* [Tło fabularne](#tło-fabularne)
* [Reguły gry](#reguły-gry)
* [Wysyłane informacje](#wysyłane-informacje)
  * [Adres IP](#adres-ip)
  * [Nagłówki HTTP](#nagłówki-http)
  * [Pliki cookies](#pliki-cookies)
  * [ETag](#etag)
  * [JavaScript](#javascript)
  * [Elementy osadzone](#elementy-osadzone)
  * [Linki śledzące](#linki-śledzące)
  * [Przekierowania](#przekierowania)
* [Nasze wyposażenie](#nasze-wyposażenie)
* [Plansza](#plansza)
  * [Ścisłe terytorium AllSinga](#ścisłe-terytorium-allsinga)
  * [Domena AllSinga](#domena-allsinga)
  * [Terytorium neutralne](#terytorium-neutralne)
  * [Terytorium przyjazne](#terytorium-przyjazne)
* [Jak wygrać](#jak-wygrać)
* [Koniec serii?](#koniec-serii)



## Tło fabularne

Akcja rozgrywa się w&nbsp;alternatywnej rzeczywistości, mniej więcej w&nbsp;naszych czasach.  
Jesteśmy zwykłym, szarym człowiekiem, płci dowolnej, krótko po studiach. Mieszkamy w&nbsp;wynajętym mieszkaniu. Powoli odkładamy na coś własnego.

Mamy też **konto na platformie AllSing** (nazwa zmyślona), aktywne od kilku lat. Założyliśmy je niejako z&nbsp;konieczności. Tam byli nasi znajomi, grupy związane ze studiami, oferty pracy. Platforma zna nasze imię, nazwisko, numer telefonu, zainteresowania.

Koncern, do którego należy platforma, również nazywa się AllSing. To duża firma założona na terenie jednego ze światowych mocarstw i&nbsp;mocno przez nie finansowana. Kilka ciekawostek o&nbsp;nich:

* Zaczynali jako startup Allsingly (tak to już jest, że startupy lubią się [kończyć na *-ly*](https://www.quora.com/Why-do-so-many-startup-names-end-with-ly-able-and-ify?share=1)).
* Ich strona do teraz zresztą nazywa się *allsing.ly*.

  {:.post-meta .bigspace-after}
  Niektóre nazwy firm i&nbsp;domen w&nbsp;tym wpisie są zmyślone i&nbsp;nie odpowiadają faktycznym stronom. Nawet jeśli takowe istnieją albo powstaną.  

* Rozległy profil działalności. Mają kilka wielkich portali: o&nbsp;newsach, o&nbsp;zdrowiu, z&nbsp;ofertami pracy, randkowy. Wchodzą też w&nbsp;świat fizyczny.
* Oficjalnie ich nazwa ma być częścią sloganu. *Let's all sing together*. Prezes lubi podkreślać, że łączą ludzi na całym świecie. 
* AllSing brzmi trochę jak *all-seeing*. Po angielsku: *wszystkowidzący*.  
  Nieprzypadkowo. Trzon ich działalności internetowej opiera się bowiem na zbieraniu danych i&nbsp;profilowaniu użytkowników.  

  <img width="200px" src="/assets/posts/inwigilacja_podsumowanie/allsingly_logo.jpg" alt="Logo AllSinga, wyglądające jak czarna nutka z&nbsp;okiem. Otacza ją czerwona obwódka. Całość sprawia niepokojące wrażenie."/>

  {:.figcaption}
  Logo Allsinga, wymyślone przeze mnie. Połączenie nutki z&nbsp;egipskim Okiem Ra.

Ich marsz po coraz to nowe zdobycze stale przyspiesza.  
Kiedyś mieli ich pod lupą niektórzy politycy, ale przestali, odkąd firma zwiększyła wydatki na lobbing.  
Pojawiały się krytyczne artykuły, ale dziwnym trafem przycichły, kiedy AllSing wraz z&nbsp;paroma innymi kolosami wykupił media.

Pozostał tajemniczy ruch oporu pod kryptonimem *STFU*, którego symbolem jest emota z&nbsp;zamkniętymi na zamek ustami. Twierdzą, że AllSing zmienia świat w&nbsp;dystopię.  
Do tej pory nimi gardziliśmy jako ludzie sukcesu (no... albo chociaż aspirujący). Bo jak to tak, *prywatną firmę* szkalować?

Ale teraz stajemy przed nieciekawą sytuacją w&nbsp;naszym życiu. Bliska nam osoba, pracująca dotąd w&nbsp;moderacji AllSinga, jest w&nbsp;śpiączce. Nieszczęśliwy wypadek.

Chcemy teraz pomóc jej rodzinie, zbadać możliwości opieki, zorganizować zbiórkę, cokolwiek. Opieka medyczna kosztuje, odkąd monopol uzyskała spółka AllSing Health.

Postanawiamy zrobić to, co umiemy dobrze, czyli poszukać informacji w&nbsp;internecie.

Problem w&nbsp;tym, że AllSing powierza analizę danych automatom. A&nbsp;one nie odróżniają szukania informacji dla kogoś innego od szukania ich dla siebie. I&nbsp;łatwo wyłapują jednostki ich zdaniem słabe.  
**Sam fakt, że odwiedzaliśmy strony poświęcone chorobom i&nbsp;zasiłkom, obniży nasz ranking społeczny**. Miałoby to przykre konsekwencje:

* Nie dostaniemy kredytu na własne mieszkanie (bo banki korzystają z&nbsp;danych AllSinga przy ustalaniu zdolności kredytowej). Zaś stawki czynszu podnoszone przez AllSing Development nas kiedyś zgniotą.
* Na platformie AllSing Jobs oznaczą nas po cichu jako pracownika niepewnego, co oznacza koniec kariery.
* Na platformie AllSing Dating po cichu zostaniemy zepchnięci na sam dół hierarchii. Hajtniemy się co najwyżej z&nbsp;którymś z&nbsp;botów robiących sztuczny ruch.

Wniosek: musimy poszukać informacji, ale w&nbsp;taki sposób, żeby platforma nie powiązała tego z&nbsp;naszym kontem. Może nawet zajrzymy na stronki ruchu oporu?

## Reguły gry

W tej grze mamy za zadanie odwiedzać punkty na planszy -- strony internetowe z&nbsp;potrzebnymi nam informacjami. W&nbsp;każdej turze możemy przeskakiwać na dowolne pole. W&nbsp;końcu internet obejmuje cały świat.

Możemy też zajrzeć do którejś ze stref specjalnych -- naszego prywatnego maila albo na fora przeciwników AllSinga.

Zdobywamy punkty, kiedy uda nam się anonimowo uzyskać informacje. Tracimy je, kiedy AllSing rozpozna, że to my coś przeglądamy i&nbsp;doda swoje obserwacje do naszej „teczki”.

Nasza gra zawiera element losowy. Niektóre strony leżą na planszy grafiką do dołu. **Dopiero po ich odwiedzeniu zobaczymy, czy były bezpieczne, czy też szpiegowskie**. W&nbsp;prawdziwym internecie też zwykle jesteśmy pierwszymi, którzy wysyłają informacje. I&nbsp;możemy się naciąć.

Na wypadek śledzenia możemy (i powinniśmy!) się zabezpieczać, dobierając sprzęt, sposób połączenia z&nbsp;internetem oraz dodatki do przeglądarki. Więcej o&nbsp;tym w&nbsp;dalszej części.

A tymczasem zapoznajmy się z&nbsp;potencjalnymi pułapkami -- informacjami, których AllSing może użyć przeciwko nam. Oraz sposobami, w&nbsp;jakie może je pozyskać.

## Wysyłane informacje

Wysyłane przez nas informacje proponuję podzielić na dwie główne kategorie:

1. Podstawowe informacje, które wysyłamy *absolutnie każdej* odwiedzanej stronie. To adres IP oraz tak zwane *nagłówki HTTP*.
2. Informacje, jakie wyciąga od nas kod JavaScript na niektórych stronach. Są wysyłane dopiero po tym, jak pobierzemy stronę, a&nbsp;przeglądarka wykona skrypt.

Przedstawiam autorski schemat pełnej interakcji, z&nbsp;nagłówkami HTTP i&nbsp;JavaScriptem. Po lewej my. Po prawej cudzy komputer, z&nbsp;którym się kontaktujemy.

<img src="/assets/posts/javascript-tracking/internet-schemat.jpg" width="500px" alt="Schemat złożony z&nbsp;dwóch pasków, jeden pod drugim. Na pierwszym z&nbsp;nich laptop wysyła serwerowi informacje i&nbsp;otrzymuje w&nbsp;zamian stronę internetową z&nbsp;napisem JS."/>

<img src="/assets/posts/javascript-tracking/javascript-schemat.jpg" width="500px" alt="Ciąg dalszy poprzedniego schematu. Od laptopa odchodzi strzałka podpisana JS i&nbsp;zawierająca jego małą ikonę. Symbolizuje to, że JavaScript wysłał serwerowi informacje"/>

{:.figcaption}
Ikona nad pierwszą strzałką od góry symbolizuje wysłane nagłówki HTTP. Ta nad drugą -- otrzymaną stronę internetową z&nbsp;JavaScriptem.  
Źródło ikon: Flaticon. [Laptop](https://www.flaticon.com/free-icons/computer) od *vectorsmarket15*, [serwer](https://www.flaticon.com/free-icons/server) od *Smashicons*, [strzałka](https://www.flaticon.com/free-icons/down-arrow) od Freepik. Aranżacja moja.

Ogólna zasada jest taka, że **unikamy jak ognia noszenia ze sobą unikalnych identyfikatorów** -- informacji znanych AllSingowi, które mają określoną wartość dla nas, a&nbsp;inną dla innych osób.

Nie zawsze mamy wybór, czasem musimy taki identyfikator przyjąć. Grunt, żeby działo się to przez jak najkrótszy czas. Najlepiej tylko na czas odwiedzenia jednej strony.

Spójrzmy dokładniej na niektóre potencjalne pułapki. Nie wymyśliłem ich na potrzeby gry; wszystkie są naszą codziennością.

### Adres IP

Przypisany punktowi, przez który łączymy się z&nbsp;internetem -- na przykład routerowi.

To informacja, która *musi* być prawdziwa. Inaczej nie dostaniemy strony, o&nbsp;którą prosiliśmy -- tak jak nie dostalibyśmy listu z&nbsp;odpowiedzią, gdybyśmy podali zmyślony adres nadawcy.

Nasz domowy adres IP jest w&nbsp;tej grze stały i&nbsp;niezmienny. Taki mamy i&nbsp;już. To najgorszy przypadek, bo **wtedy działa jak nasz unikalny identyfikator**. AllSing zawsze będzie wiedział, że użytkownik spod adresu *12.345.678* to osoba o&nbsp;konkretnym imieniu i&nbsp;nazwisku.

Na szczęście mamy też telefon komórkowy. Używając go do przeglądania internetu, co jakiś czas dostajemy nowy adres IP. Możemy też używać go jako własnego hotspota. Ale uważajmy -- co turę mają miejsce zdarzenia losowe, a&nbsp;wśród nich również oddanie telefonu do naprawy :wink:

A jeśli nawet mamy tylko stałe IP z&nbsp;domowego routera, to wciąż nie wszystko stracone:

1. Można połączyć się z&nbsp;internetem przez jakiegoś publicznego hotspota, na przykład z&nbsp;kawiarni. Będziemy mieli inne IP, dzielone z&nbsp;wieloma całkiem obcymi osobami.
2. Można **skorzystać z&nbsp;tzw. pośrednika sieciowego** (najprostszego *proxy*, nieco bardziej wypasionego VPN-a albo pancernego Tor Browsera).  
   Weźmie naszą prośbę o&nbsp;stronkę i&nbsp;wyśle ją dalej we własnym imieniu, nie ujawniając odbiorcy naszego adresu.

W życiu prawdziwym, żeby sprawdzić swój adres IP, możemy choćby odwiedzić wyszukiwarkę DuckDuckGo i&nbsp;wpisać tam `ip address` (tutaj [gotowy link](https://duckduckgo.com/?q=ip+address&t=lm&ia=answer)).  
Zaraz pod paskiem wyszukiwania wyświetli się adres IP i&nbsp;przybliżona lokalizacja.

Więcej informacji na temat adresów IP omówiłem w&nbsp;swoim [wpisie]({% post_url 2021-06-12-adres-ip %}){:.internal} (ogólnie: wszystkie linki wyglądające w&nbsp;ten sposób odsyłają do wpisów z&nbsp;Ciemnej Strony).

### Nagłówki HTTP

Za każdym razem, kiedy chcemy odwiedzić jakąś stronę, nasza przeglądarka o&nbsp;nią „prosi”. Wysyłając parę podstawowych informacji o&nbsp;nas, które będę nazywał naszą *wizytówką* (oficjalna nazwa: *nagłówki HTTP*). Są wśród nich:

* *[User Agent]({% post_url 2021-06-11-user-agent %})*{:.internal}

  (nazwa systemu operacyjnego + nazwa i&nbsp;wersja przeglądarki).

* *[Referer]({% post_url 2021-01-12-internetowa-inwigilacja-2-referer %})*{:.internal}

  (jeśli odwiedzamy stronę B&nbsp;przez kliknięcie w&nbsp;link na stronie A, to będzie tu informacja o&nbsp;tym, z&nbsp;jakiej strony przychodzimy).

* *Hostname*

  (często po prostu link do strony, na którą wchodzimy. Ale w&nbsp;tym linku mogą znajdować się również dodatkowe, identyfikujące nas [parametry]({% post_url 2021-04-09-internetowa-inwigilacja-parametry %}){:.internal}).

* [Pliki cookies]({% post_url 2021-10-22-pliki-cookies %}){:.internal} oraz *ETagi*

  (tylko przy niektórych stronach; ich dokładniejszy opis poniżej).

* Inne informacje, takie jak ustawiony język, data, godzina.

Wszystkie te elementy można modyfikować przez ustawienia przeglądarki albo odpowiednie dodatki. Oczywiście w&nbsp;granicach rozsądku.

Większość informacji jest dość ogólna. Żeby nas nie identyfikowały, warto korzystać z&nbsp;przeglądarki jak najbardziej zlewającej się z&nbsp;tłumem (popularna, dość nowa wersja, ustawiony język zgodny ze strefą czasową itp.).  
W praktyce: **korzystajmy z&nbsp;przeglądarki zaufanej, która nas nie śledzi, i&nbsp;aktualizujmy ją na bieżąco**.

{% include info.html
type="Porada"
text="Jeśli chcemy zobaczyć, jakie nagłówki HTTP wysyłamy stronie, to możemy to łatwo zrobić. Naciskamy `Ctrl+Shift+I`, żeby otworzyć narzędzia przeglądarki. Tam klikamy zakładkę `Sieć` u&nbsp;góry, klikamy na jedną z&nbsp;pozycji z&nbsp;listy elementów (jeśli jest ich mało, to naciskamy `F5` dla odświeżenia).  
W dziale `Nagłówki żądania` znajdziemy listę wysłanych przez nas informacji. 
"
%}

Niektórym z&nbsp;tych elementow poświęcę więcej czasu. Poczynając od plików cookies. Zasługują tu na osobne omówienie, ponieważ umożliwiają jednoznaczną identyfikację.

### Pliki cookies

To krótkie, unikalne dla nas fragmenty tekstu, które nasza przeglądarka otrzymała od AllSinga, gdy się tam ostatnio logowaliśmy.

**Identyfikują nas jako konkretnego użytkownika**. Co ma swoje zastosowanie. Dzięki nim nie musimy się logować za każdym razem, kiedy odwiedzamy zamknięte części platformy AllSing. O&nbsp;ile używamy tej samej przeglądarki co poprzednio -- każda „trzyma” bowiem odrębne ciasteczka.  
To taki odpowiednik korporacyjnego identyfikatora na smyczce. Okażemy, to wejdziemy.

{:.bigspace}
<img src="/assets/posts/inwigilacja_podsumowanie/allsingly_cookie.jpg" alt="Ciastko z&nbsp;kawałkami czekolady z&nbsp;nałożoną na nie ikoną AllSinga" width="200px"/>

Kiedy odwiedzamy dowolną stronę w&nbsp;domenie *allsing.ly*:

* *<span class="red">allsing.ly</span>*,
* *health.<span class="red">allsing.ly</span>*,
* *<span class="red">allsing.ly</span>/settings/my_info*,
* *news.<span class="red">allsing.ly</span>/poland/latest/*,

to przeglądarka automatycznie, za kulisami, dołącza do naszej „wizytówki” również ciasteczka odpowiadające *allsing.ly*.

AllSing je odbiera, sprawdza jakiemu użytkownikowi odpowiadają i&nbsp;serwuje nam rzeczy dopasowane do naszego konta.  
Na niektórych podstronach AllSinga poznamy, że jesteśmy zalogowani, po małym awatarze w&nbsp;górnym prawym rogu strony. Ale parę podstron przyjmuje pliki cookies po cichu, nie ujawniając że nas poznali. A&nbsp;poznali na pewno. I&nbsp;zapisują sobie, jakie części ich portalu zwiedzamy.

Pliki cookies możemy łatwo usuwać przez opcje przeglądarki. Albo tymczasowo je zignorować, włączając *tryb incognito*.

Ale jeśli je stracimy, musimy od nowa się zalogować na portalu *allsing.ly*, żeby móc go zwiedzać. Gdy to zrobimy, dostajemy nowe. Prowadzi to do prostego wniosku -- **nie da się anonimowo przeglądać, ze swojego konta, stron wymagających logowania**. Możemy co najwyżej założyć do tego celu fałszywe konto.

Ciasteczka mają też drugie, gorsze dla nas zastosowanie, kiedy w&nbsp;grę wchodzą elementy „gościnne” od AllSinga. O&nbsp;tym za chwilę.

### ETag

To metoda dość podobna do ciasteczek. Też polega na przyznaniu nam unikalnego identyfikatora, który przeglądarka ochoczo okazuje stronce, jeśli już ją wcześniej odwiedzaliśmy.  
Jest wysyłany jako część nagłówków HTTP, tak jak ciasteczka.

Oficjalnie wiąże się z&nbsp;[pamięcią podręczną]({% post_url 2021-12-24-caching %}){:.internal}. Pomaga oszczędzić przeglądarce niepotrzebnego, wielokrotnego pobierania elementów, np. obrazków.

Przeglądarka, pobierając obrazek z&nbsp;*ETagiem*, zapisuje sobie odpowiadający mu ciąg znaków. Przy kolejnych wizytach okazuje go stronce.  
„Hej, mam obrazek o&nbsp;takim numerze. Jeśli się zmienił po waszej stronie, to wyślijcie mi nową wersję. Jeśli nie, to zignorujcie tę wiadomość”.

Grzeczne strony rozdawałyby te same pary *ETag + obrazek* wszystkim użytkownikom. Niegrzeczne dają każdemu użytkownikowi coś innego. Zatem kiedy przeglądarka wysyła konkretny numer, to strona po nim rozpozna, że to użytkownik A, a&nbsp;nie B, i&nbsp;odczyta z&nbsp;bazy odpowiednie informacje o&nbsp;nas. Nawet jeśli zmieniliśmy adres IP i&nbsp;ukryliśmy ciasteczka. 

Dobry opis tej metody (po angielsku) znajdziemy [tutaj](https://levelup.gitconnected.com/no-cookies-no-problem-using-etags-for-user-tracking-3e745544176b). W&nbsp;świecie rzeczywistym używały ich między innymi Spotify, Slideshare, Etsy (platforma z&nbsp;rękodziełem), Hulu (streaming). Za co [dostały pozwem](https://www.extremetech.com/internet/91966-aol-spotify-gigaom-etsy-kissmetrics-sued-over-undeletable-tracking-cookies). 

Ochrona przed ETagiem jest na szczęście dość prosta -- **kiedy czyścimy ciasteczka, to czyśćmy również pamięć podręczną**. Nie odznaczajmy tej opcji.

### JavaScript

[Język programowania internetu]({% post_url 2022-05-02-javascript1 %}){:.internal}, któremu poświęciłem aż trzy wpisy. W&nbsp;skrócie JS. Zapewnia stronom interaktywność, nietypowe animacje itp.

Kiedy chodzimy po stronach AllSinga, upakowanych JS-em po brzegi, nieraz przyspiesza nagle wentylator w&nbsp;naszym komputerze. Słychać, że procesor czasem nie ma łatwo. Ale staramy się to ignorować, zrzucając winę na ich bajery graficzne.

Tymczasem tak naprawdę to nie grafika tak męczy nasz komputer. Winne są skrypty profilujące. Nasz komputer **dostaje do wykonania niewidoczne dla nas zadania** -- raz tworzy kompozycje obrazkowe z&nbsp;pikseli, to znowu kompresuje i&nbsp;edytuje pliki dźwiękowe.

Efekty końcowe różnią się między komputerami. Ale zwykle są takie same albo prawie takie same dla tego samego komputera. Co oznacza, że po ściśnięciu ich w&nbsp;jeden ciąg znaków można otrzymać nasz unikalny identyfikator. Nazywany „odciskiem palca przeglądarki” (ang. *browser fingerprint*).

AllSing już od dawna ma odciski naszych urządzeń w&nbsp;bazie. Zatem jeśli trafimy na jakikolwiek skrypt śledzący od nich, to ten wykona całe profilowanie, otrzyma ciąg znaków, porówna z&nbsp;bazą. Odgadnie, że zapewne jesteśmy konkretnym użytkownikiem ich portalu.

Jesteśmy w&nbsp;tej grze zwykłym człowiekiem, nie Terminatorem. Dlatego zakładamy, że nie przechytrzymy JS-a. Jeśli pozwolimy skryptowi się uruchomić -- a&nbsp;będzie to skrypt od AllSinga -- to **zawsze, bez wyjątku, rozpozna nasze urządzenie wśród tysięcy innych**.

Istnieje kilka sposobów na zmniejszenie tego ryzyka; różniących się w zależności od tego, na ile JavaScript jest zakorzeniony w&nbsp;stronie.

Zdradzę na razie, że jednym z&nbsp;nich jest całkowite wyłączenie. To opcja nuklearna, bo JavaScript jest integralną częścią internetu. Wiele stron działa bez niego nieprawidłowo; nie tylko te od AllSinga.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja_podsumowanie/strony-js.jpg" alt="Dwieikony. Identyczne, poza tym że jedna jest czerwona, a&nbsp;druga zielona. Pośrodku każdej z&nbsp;nich znajduje się skrót JS, od JavaScript."/>

{:.figcaption}
Takimi ikonami oznaczam strony internetowe, które potrzebują JavaScriptu do działania. Na czerwono te, które należą do AllSinga.

{% include info.html
type="Przykłady"
text="Reddit, znane forum, stosowało [całą kolekcję](https://smitop.com/post/whiteops-data/) różnych metod profilowania przez JavaScript. Niektóre ocierały się o&nbsp;hakerstwo.  
Forum StackOverflow, źródło popularne szczególnie wśród programistów, profilowało użytkowników [przez właściwości karty dźwiękowej](https://meta.stackexchange.com/questions/331960/why-is-stack-overflow-trying-to-start-audio).  
Profilowanie [przez grafikę](https://cba.upc.edu/downloads/category/11-articles?download=1045:%5BARTICLE%5DTowards_accurate_detection_of_obfuscated_web_tracking.pdf&start=480) wykryto w&nbsp;2017 roku na 10% z&nbsp;10 000&nbsp;najpopularniejszych stron."
%}

### Elementy osadzone

Nie jest to odrębny sposób rozpoznawania nas, lecz pewna ogólna zasada działania internetu, która *utrudnia*{:.corr-del} urozmaica nam rozrywkę.

Bo widzicie, każda strona A&nbsp;może gościć u&nbsp;siebie elementy ze strony B. Załóżmy że jesteśmy na fikcyjnej stronie *koteły.pl*, pełnej obrazków. Mogą być nam serwowane na dwa sposoby:

```html
<img src="/obrazki/kot.jpg"/>
<img src="https://allsing.ly/gallery/kot.jpg"/>
```

Pierwsza linijka to obrazek umieszczony na tej samej stronie A&nbsp;(*koteły.pl*), którą właśnie odwiedzamy. Przypadek typowy i&nbsp;niegroźny.

Druga linijka to obrazek pobierany ze strony zewnętrznej, B&nbsp;(AllSinga), do którego strona A&nbsp;tylko odsyła. Jest swego rodzaju gościem.  
Kiedy nasza przeglądarka widzi, że źrodłem elementu jest link do obcej strony B, to wysyła tej stronie prośbę o&nbsp;dany element.

Elementy gościnne to często niegroźne pliki -- czcionki, filmiki, obrazki. Czasem symboliczne, rozmiaru 1&nbsp;na&nbsp;1, czyli piksele (stąd nazwa *piksel śledzący*).  
Groźne jest w&nbsp;nich jednak ich pochodzenie. Prosząc o&nbsp;nie AllSinga, przeglądarka wyśle nasze informacje podstawowe. Najgorszymi potencjalnymi identyfikatorami będą adres IP oraz pliki cookies.

Może się jednak zdarzyć, że elementem gościnnym będzie skrypt. Uruchomi się u&nbsp;nas, sprofiluje nas i&nbsp;wyśle informacje AllSingowi. A&nbsp;pamiętajmy, uruchomienie = stuprocentowo pewne rozpoznanie urządzenia.

Wniosek: elementy z&nbsp;zewnątrz mogą być groźne albo bardzo groźne. Co gorsza, są bardzo powszechne. Wielu właścicieli stron, nie znając zagrożeń, dodaje do nich pozytywki AllSinga, widżety, fikuśne czcionki i&nbsp;inne bzdety od nich.

Na szczęście da się blokować pobieranie szpiegowskich elementów zewnętrznych, korzystając z&nbsp;dodatków takich jak uBlock Origin albo Privacy Badger.

W naszej grze stronki z&nbsp;elementami obcymi przedstawiam jako normalne ikony stron, tylko że z&nbsp;dodatkowym elementem w&nbsp;górnym lewym rogu. Jeśli element ma kolor czerwony, to znaczy że pochodzi od AllSinga.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja_podsumowanie/strony-elementy-zewnetrzne.jpg" alt="Cztery ikony odpowiadające stronom internetowym. Każda z&nbsp;nich ma w&nbsp;lewym górnym rogu niewielki element. Kolejno od prawej: zielony obrazek, czerwony obrazek, literki A&nbsp;na czerwonym tle (małą i&nbsp;wielką), skrót JS od nazwy JavaScript."/>

{:.figcaption}
Ikony stron zawierających elementy ze stron obcych. Od lewej: niegroźny obrazek, obrazek od AllSinga, czcionki AllSinga, skrypt AllSinga.

{% include info.html
type="Przykłady"
text="Niedawno mieliśmy aferkę ze stronami szpitali w&nbsp;USA, goszczącymi u&nbsp;siebie elementy od Facebooka. Integracja była na tyle mocna, że niektóre przyciski [wysyłały Fejsowi informacje](https://themarkup.org/pixel-hunt/2022/06/16/facebook-is-receiving-sensitive-medical-information-from-hospital-websites) o&nbsp;tym, jaki link odwiedza konkretna osoba. A&nbsp;w tym linku -- nazwy chorób, o&nbsp;jakich czyta.  
Niedawno przez Europę przetoczyła się [fala kar](https://news.ycombinator.com/item?id=31856023) za korzystanie z&nbsp;Google Analytics i&nbsp;Fonts, przez które dane użytkowników były automatycznie przekazywane do USA (których prawo sprzyja profilowaniu ludzi)."
%}

### Linki śledzące

Podczas naszej podróży przez internet będziemy często klikali w&nbsp;linki. Niektóre z&nbsp;nich mogą być pułapką.

Jeśli jesteśmy w&nbsp;miejscu, w&nbsp;które tylko my możemy zajrzeć -- na przykład czytamy wiadomość prywatną lub maila specjalnie do nas, albo jesteśmy zalogowani na swoje konto -- to uważajmy na [linki z&nbsp;parametrami]({% post_url 2021-04-09-internetowa-inwigilacja-parametry %}){:.internal}.

Załóżmy na przykład, że na prywatną skrzynkę dostaliśmy maila z&nbsp;linkiem:

<div class="black-bg mono bigspace">
https://www.allsing.ly/pl/zdrowie/spiaczka-farmakologiczna?<span class="red">user=1897426177</span>&view=gallery
</div>

Po znaku zapytania zaczynają się parametry. Tu mamy dwa. `view=gallery` oraz `user=1897426177`. Pierwszy jest niegroźny. A&nbsp;drugi nas zidentyfikuje.

W filmach szpiegowskich często pojawia się sposób na zdemaskowanie kogoś przez podanie każdej osobie nieco innych informacji i&nbsp;obserwowanie, co dokładnie wycieknie. W&nbsp;ten sposób wiadomo, kto je wyniósł na zewnątrz.

Tak samo mogą robić platformy. Każdemu użytkownikowi pokazują nieco inny link, z&nbsp;innym ciągiem liczb w&nbsp;parametrze (a poza tym prowadzący do tej samej strony). Kiedy potem znajdą taki link na zewnętrznej stronie, na przykład na jakimś forum, to wiedzą kto go wyniósł.

Mogą również sami rozsyłać linki ludziom i&nbsp;potem sprawdzać po parametrach, którzy z&nbsp;nich je kliknęli.  
Ktoś otrzymał link do propagandowych materiałów AllSinga, ale nie odnotowaliśmy odwiedzin osoby z&nbsp;tym parametrem? Skubany widocznie olał sprawę. Obniżmy mu ranking społeczny.

{% include info.html
type="Przykład"
text="W życiu prawdziwym dziwne, potencjalnie śledzące linki wykorzystywały [Twitter](https://nitter.net/luca/status/1432780065109155855) i&nbsp;[Facebook](https://stackoverflow.com/questions/64092454/what-is-the-purpose-of-the-new-cft-0-and-tn-parameters-in-facebook-po).   
Problem linków śledzących urósł do tego stopnia, że Firefox zaczął [usuwać znane parametry śledzące](https://www.ghacks.net/2022/06/29/firefox-remove-known-tracking-parameters-from-urls-in-all-modes/) z&nbsp;linków; wystarczy włączyć odpowiednią opcję. Robi to również Brave.  
Facebook, być może w&nbsp;odpowiedzi na to, ponoć przepchnął identyfikator bezpośrednio do ścieżki w&nbsp;linku. Nie da się go usunąć, nie czyniąc samego linka bezużytecznym.  
Moje eksperymenty nie potwierdzają, żeby każdy użytkownik Facebooka dostawał swój unikalny link. Ale nie wykluczam, że platforma się do tego przymierza."
%}

### Przekierowania

Każda strona internetowa X&nbsp;może zawierać element mówiący coś w&nbsp;stylu „Nie mam tego, czego szukasz. Musisz przejść na inną stronę, Y”. Przeglądarka słucha takich wskazówek i&nbsp;automatycznie przechodzi na stronę Y.

Ale nadal obowiązuje tu podstawowa zasada internetu -- za każdym razem, kiedy prosimy o&nbsp;jakąś stronę, wysyłamy jej parę informacji o&nbsp;sobie. Zatem nasze informacje zdobędą obie odwiedzane strony. Najpierw X, potem Y.

Niektórzy celowo, zamiast wrzucić link prosto do źródła (niezależnego od nich), stawiają nam na drodze takie mini-stronki przekierowujące, żeby zebrały o&nbsp;nas informacje. Często wykorzystuje się do tego celu popularne skracarki linków, jak *bit.ly*.

Ktoś powie „Ale przecież widzę w&nbsp;co klikam, nie nabiorę się”.  
Na pewno? Popatrzmy na ten link:

[https://www.ciemnastrona.com.pl](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.ughVnEvJKsxskMcmQ-Q8lAHaHi%26pid%3DApi&f=1).

Wygląda jak link do Ciemnej Strony? A&nbsp;jednak prowadzi w&nbsp;inne miejsce -- jeśli w&nbsp;niego klikniecie, zostaniecie strollowani. **Tekst linku nie musi odpowiadać jego lokalizacji docelowej**. Równie dobrze, zamiast trollingu, pod tym linkiem mogło się chować śledzące przekierowanie. 

Co gorsza, strony z&nbsp;przekierowaniami mogą być pełnoprawnymi stronami internetowymi. Mogą również zawierać zewnętrzne elementy (żeby ich strona-matka mogła nas poznać po plikach cookies), a&nbsp;nawet JavaScript (żeby mogła nas poznać po sprzętowym odcisku palca).

Pod tym względem [szczególnie wredny jest Twitter]({% post_url 2021-03-26-internetowa-inwigilacja-3-przekierowania %}){:.internal}, który wszystkie linki na swojej platformie zamienia na linki zaczynające się od *t.co*. Klikając w&nbsp;nie, przechodzimy przez jego podstronki. Dzięki temu łatwo wie, w&nbsp;co klikali konkretni użytkownicy.

## Nasze wyposażenie

Podczas gry możemy dobierać różne zestawy urządzeń i&nbsp;programów, żeby lepiej lub gorzej chronić prywatność:

1. Urządzenie.

   Do wyboru mamy swoją komórkę, swojego laptopa oraz komputer w&nbsp;bibliotece. Oba nasze urządzenia są już sprofilowane i&nbsp;AllScript je rozpozna, jeśli tylko pozwolimy mu uruchomić JavaScript.  
   Skrypty możemy bez obaw uruchamiać jedynie przez komputer w&nbsp;bibliotece. Oczywiście pod żadnym pozorem nie logujemy się przez niego na nasze konto na AllSingu. Wada: spacer do biblioteki zużywa wiele punktów akcji.

2. Hotspota.

   Do wyboru mamy: domowy router (stałe, niezmienne IP), internet przez komórkę (IP zmienia się co jakiś czas), hotspoty w&nbsp;kawiarni lub w&nbsp;bibliotece (IP stałe, ale dzielone z&nbsp;wieloma osobami).  
   Dodatkowo wszędzie możemy użyć VPN-a. Pozwoli zamaskować nawet stałe domowe IP. Nie chroni natomiast przed rozpoznaniem poprzez ciasteczka albo JavaScript.

3. Przeglądarkę.

   Prywatnościowe: Firefox i&nbsp;Brave.  
   Ultrabezpieczna, ale powolna: Tor Browser  
   (pozwala zmieniać IP, daje też ochronny rzut kością przeciw profilowaniu przez JavaScript).  
   Aktywnie działające przeciw prywatności: Chrome i&nbsp;AllSing Browser.

4. Dodatki do przeglądarki.

   Wszelkie znane ze świata rzeczywistego: uBlock Origin, Privacy Badger, NoScript, Universal Bypass.  
   Przepuszczające AllSinga, [bo im zapłacił](https://www.theguardian.com/technology/2016/feb/25/adblock-plus-opens-up-acceptable-ads-work): Adblock, AdblockPlus, klasyczny uBlock.  
   Ze świata fikcyjnego mamy AllSing Assistant. Ale nie polecam, bo śledzi.

   Dodatki blokujące są o tyle fajne, że **blokują pobieranie drobniejszych, zewnętrznych elementów śledzących**. Nie pomogą przeciw stronom samego AllSinga, ale ochronią na stronkach cudzych, goszczących u&nbsp;siebie elementy od giganta.

Żeby gra nie była zbyt prosta, możemy dodać pewne zdarzenia losowe. Na przykład jakiś dodatek zostanie podkupiony przez AllSinga, gubimy telefon, zamykają na kilka dni bibliotekę itp. Zostawiam je Waszej wyobraźni.

Z kolei w&nbsp;życiu prawdziwym polecam po prostu chwycić dobry zestaw ochronny i&nbsp;się go trzymać :wink: Praktyczniejsze rady pod koniec wpisu.

## Plansza

Arena walki z&nbsp;AllSingiem ma u&nbsp;nas formę planszy o&nbsp;określonej liczbie pól. Na każdym z&nbsp;nich może się znajdować jakaś strona internetowa, którą możemy odwiedzić.

<img src="/assets/posts/inwigilacja_podsumowanie/allsing-plansza.jpg" alt="Plansza do gry"/>

{:.figcaption}
Tak wygląda fragment naszej planszy. Ikony ze strefy środkowej, skalistej, w&nbsp;praktyce są zakryte i&nbsp;nie wiemy, co się pod nimi kryje.  
Źródło oryginalnych tekstur: nieśmiertelni *Heroesi 3*.

W zależności od poziomu zagrożenia, strefę gry dzielimy na kilka obszarów:

1. Ścisłe terytorium AllSinga,
2. Strony w&nbsp;domenie *allsing.ly*,
3. Neutralna część internetu,
4. Przyjazna część internetu.

Omówię je w&nbsp;kolejności od najgorszych (góra, wulkany) do przyjaznych. Ale niech Was to nie zwiedzie; macki AllSinga sięgają najdalszych końców planszy.

### Ścisłe terytorium AllSinga

Nazwijmy je pieszczotliwie „wewnętrznym kręgiem piekieł”. To podstrony dostępne jedynie dla zalogowanych kont, do tego mających dłuższy staż na platformie.

Zacznę od tego miejsca, ponieważ obejmuje przypadek beznadziejny -- **nie jesteśmy w&nbsp;stanie zachować tutaj anonimowości**.

Po pierwsze: cały czas nosimy ze sobą pliki cookies od AllSinga, unikalny identyfikator. Usuniemy je? To nie wejdziemy na konto. Wpiszemy swój login i&nbsp;hasło? To otrzymamy nowe cookies i&nbsp;na konto wejdziemy, ale AllSing będzie doskonale wiedział, kim jesteśmy.

Po drugie: JavaScript. Aktywny zawsze, na każdej stronie AllSinga. Bez niego strony nie zadziałają. A, jak się umówiliśmy, jest w&nbsp;stanie zawsze rozpoznać nasze urządzenie.

W związku z&nbsp;tym jedynym sposobem na prywatność w&nbsp;tym miejscu byłoby założenie całkiem nowego konta. Na inny numer telefonu, z&nbsp;całkiem innego komputera oraz hotspota. Jak osobna tożsamość.

Ale to wciąż nie daje gwarancji. Zwłaszcza jeśli nie chodzi o&nbsp;jednorazowe zalogowanie, tylko musimy przez pewien czas na portalu pobyć, trzymać poziom aktywności i&nbsp;nabić punkty reputacji.

Bo widzicie -- AllSing już nas świetnie poznał przez te lata. Ma w&nbsp;bazie nie tylko rzeczy techniczne, jak pliki cookies, ale także nasze zwyczaje i&nbsp;zachowania. To tak zwana **analiza behawioralna**.  
Im dłużej będziemy korzystali z&nbsp;fejkowego konta, tym większe ryzyko, że zostanie powiązane z&nbsp;tym głównym przez jakiś nasz manieryzm:

* użyjemy określonego zestawu emotek, który w&nbsp;bazie AllSinga wykorzystywały tylko nieliczne osoby;
* piszemy z&nbsp;określoną szybkością;
* używamy określonych zwrotów, rzadszych wśród szerszej populacji (jak przyjemnie brzmiące *de facto*) albo popełniamy nietypowe błędy ortograficzne;
* nasze fejkowe konto jest aktywne tylko wtedy, kiedy nie jest aktywne konto główne.

I tak dalej, i&nbsp;tak dalej; być może żadna z&nbsp;tych cech nie ujawnia nas jednoznacznie, ale ich połączenie jest w&nbsp;stanie to zrobić. Analiza behawioralna to potęga. Zresztą sam mam małą serię pokazującą, jakie cechy [można łatwo odczytać]({% post_url 2021-05-14-messenger-analiza %}){:.internal} z&nbsp;historii wiadomości z&nbsp;Facebooka.

Wniosek? Omijajmy to miejsce, kiedy tylko się da. Niestety, żeby nie było za łatwo, gra będzie co pewien czas wymagała odwiedzin. W&nbsp;końcu to tu przeniosło się życie.

Kolejna sprawa -- może nas najść ochota, żeby skopiować stąd jakiś link i&nbsp;wrzucić na forum publiczne przeciwników AllSinga. Uważajmy! **Do linków mogą dodawać parametry identyfikujące użytkownika. Nieczytelne dla postronnych, ale czytelne dla AllSinga**.

Ich tajniacy na bieżąco przeczesują nieżyczliwe im strony. Znajdując nasz link, mogą skopiować z&nbsp;niego parametr śledzący. Łatwo nas wyszukają w&nbsp;bazie, rozpoznają i&nbsp;dodadzą do czarnej listy.

### Domena AllSinga

Ten obszar obejmuje różne strony w&nbsp;posiadaniu naszej ulubionej korporacyjki: *health.allsing.ly*, *news.allsingl.ly* oraz wiele innych. Również spoza ich głównej domeny -- mają na przykład portal z&nbsp;muzyką, *yousing.tv*.

Nie jest to ścisły krąg piekieł -- nie musimy się logować ani wykonywać zadań, które by ujawniły naszą tożsamość -- ale wciąż trzeba bardzo uważać.

Każda z&nbsp;tych stron wymaga do działania JavaScriptu. Jak pamiętamy, jedynym sposobem na ukrycie tożsamości jest w&nbsp;takim wypadku skorzystanie z&nbsp;osobnego urządzenia, jak komputer w&nbsp;bibliotece.

### Terytorium neutralne

To zdecydowanie największy obszar, więc warto nauczyć się sprawnie po nim nawigować. Można tu znaleźć sporo cennych informacji.

Największym, dość częstym zagrożeniem są **elementy zewnętrzne od AllSinga**. W&nbsp;końcu za każdym razem, kiedy się na nie natkniemy, nasza przeglądarka wyśle AllSingowi wizytówkę. A&nbsp;razem z&nbsp;nią być może identyfikujące nas ciasteczka lub *ETagi*.

Wśród tych elementów mogą być również skrypty. Pamiętacie, jakie przyjęliśmy założenie? Jeśli AllSing uruchomi swój JavaScript, to koniec. Zostaniemy rozpoznani. Nie pomoże ani zmieniony adres IP, ani wyczyszczone ciasteczka.

Na terytorium neutralnym możemy przyjąć jedną z&nbsp;wybranych strategii:

* Brawurową  
  
  Nie zmieniamy IP, ciasteczek ani urządzenia. Liczymy na to, że strona nie będzie zawierała niczego od AllSinga. Ani obrazków, ani czcionek, ani skryptów. Sensu to nie ma, ale adrenalinka jest.

* „Proszę, tylko nie JavaScript”
 
  Zmieniamy IP, chowamy ciasteczka i&nbsp;*ETagi* (przez usunięcie/tryb incognito).  
  Będziemy chronieni przed zwykłymi obrazkami i&nbsp;czcionkami śledzącymi. Ale jeśli nadziejemy się na JS-a, to będziemy bezradni.

* „Żadnych obcych”

  Korzystając z&nbsp;dodatku do przeglądarki, blokujemy znane złośliwe elementy zewnętrzne. Opcja chyba najbardziej praktyczna. Ale istnieją nieliczne strony, które wykryją naszego blokera i&nbsp;nas nie wpuszczą. Marnujemy wtedy punkty akcji.

* Opcja nuklearna

  Zmieniamy IP, usuwamy pliki cookies, blokujemy elementy zewnętrzne, całkiem blokujemy JavaScript.  
  Mamy pewność, że żaden skrypt czy obrazek nas nie sprofiluje. Jest jednak spora szansa, że trafimy na stronę, która bez JS-a nie zadziała. Wtedy jak wyżej: zmarnowane punkty akcji.

* *Anonymous*

  Korzystamy z&nbsp;komputera w&nbsp;bibliotece, używanego codziennie przez wiele osób. Póki nie wchodzimy na swoje główne konto, AllSing nie połapie się, kim jesteśmy. Nie musimy nawet wyłączać JavaScriptu.  
  Jedna wada tego rozwiązania: zużywamy dużo punktów akcji na spacer do biblioteki. Poza tym może się trafić zdarzenie losowe, które nam ją zamknie.

### Terytorium przyjazne

Tutaj znajdują się strony na pewno niezależne od AllSinga, a&nbsp;także te, które są mu wrogie. Pomińmy zwykłe strony -- które po prostu odwiedzamy, zyskując niewielką ilość punktów -- i&nbsp;skupmy się na dwóch lokacjach specjalnych: skrzynce mailowej oraz forach ruchu oporu.

#### Mail

<img width="70" style="display:inline-block" src="/assets/posts/inwigilacja_podsumowanie/mail-icon.jpg" alt="Ikona emoji pokazująca kopertę z&nbsp;unoszącymi się nad nią trzema sercami"/>

Mamy anonimowe konto mailowe na platformie STFUmail, niezależnej od AllSinga. Specjalnie wybraliśmy go zamiast ich produktu, Singmaila.

Czasem znajdziemy na skrzynce dodatkowe informacje; również ze stron AllSinga, które zasubskrybowaliśmy (anonimowo, więc nie mają pojęcia, że nasze konto *citizen8@stfumail.com* to konkretny użytkownik AllSinga).

Istnieją jednak sposoby na zdemaskowanie nas poprzez maila. Pomijam te bardziej hakerskie, jak *phishing*; wystarczy, że AllSing skorzysta z&nbsp;omówionych wcześniej podstaw działania internetu.

Po pierwsze: **maile mogą zawierać obrazki z&nbsp;zewnątrz**. Zatem AllSing może wysłać nam spreparowanego maila z&nbsp;obrazkiem specjalnie dla nas, pochodzącym z&nbsp;ich strony.  
Kiedy otworzymy takiego maila, to nasza przeglądarka poprosi *allsing.ly* o&nbsp;brakujący obrazek, tradycyjnie ujawniając adres IP (który może nas identyfikować) i&nbsp;ciasteczka (które zidentyfikują nas na pewno).  
Jedno automatyczne sprawdzenie w&nbsp;bazie i&nbsp;już powiążą nasz adres mailowy z&nbsp;naszym prawdziwym imieniem i&nbsp;nazwiskiem.

Rozwiązanie? Korzystajmy ze skrzynki, która automatycznie blokuje pobieranie obrazków z&nbsp;zewnątrz (albo pobiera je „na siebie”, działając w&nbsp;roli pośrednika). Jeśli takowej nie mamy, to pozostaje zmiana adresu IP, w&nbsp;dowolny z&nbsp;opisanych wyżej sposobów, i&nbsp;wyczyszczenie ciastek.

Innym sposobem na infiltrację są **linki z&nbsp;parametrami**. W&nbsp;przypadku maili są szczególnie wredne, ponieważ z&nbsp;założenia tylko my mamy dostęp do naszej skrzynki. Więc jeśli na naszego *citizen8* wysyłają linki z&nbsp;ciągiem *567234* -- który tylko my dostaniemy -- to będą mogli zapisywać sobie, jakie stronki to konto mailowe odwiedzało. 

Nawet jeśli dbamy o&nbsp;anonimowość i&nbsp;AllSing uzyska co najwyżej informację o&nbsp;tym, że linki klika osoba spod adresu *citizen8@stfumail.com* (nie znając jej tożsamości), to nadal może prowadzić dla tego konta osobną teczkę.  
A jeśli kiedyś skojarzy to konto mailowe z&nbsp;konkretnym użytkownikiem na ich platformie -- przez jakieś nasze potknięcie -- to dane z&nbsp;teczki *citizen8* dołączą do naszej, już imiennej.

# Strony ruchu oporu

<img style="display:inline-block" src="/assets/posts/inwigilacja_podsumowanie/ruch-oporu-strona.jpg" alt="Ikona emoty z&nbsp;ustami zamkniętymi na zamek błyskawiczny, w&nbsp;tle typowa biała ikona odpowiadająca stronie internetowej"/>

Te strony zdecydowanie nie lubią AllSinga. Są dla nas kopalnią wartościowych informacji... Ale czy bezpieczną?

AllSing wysyła na takie niesprzyjające mu fora swoich pracowników i&nbsp;wyznawców. Wielu z&nbsp;nich nie jest szczególnie bystrych i&nbsp;tylko w&nbsp;toporny sposób bronią firmy.  
Niektórzy są jednak cwani i&nbsp;udają przeciwników megakorporacji, jednocześnie podrzucając linki demaskujące.

Korzystają w&nbsp;tym celu ze **skracarki linków i&nbsp;przekierowań**.

Mianowicie: AllSing ma własną stronkę od skracania linków, *bul.ly* (o dziwo w&nbsp;internecie naprawdę taka istnieje! Ale ja mówię o&nbsp;fikcyjnej).

Ich tajniak wrzuca przykładowo komentarz, w&nbsp;którym pisze „Ooo, kolejny skandal u&nbsp;AllSinga!”. I&nbsp;link wyglądający jakby prowadził do stronki *prawda-o-allsingu.com*.  
Ufamy tej stronie, więc klikamy. Istotnie przechodząc do *prawdy...*, ale po drodze zahaczając o&nbsp;stronkę podległą AllSingowi, która zgarnia nasze informacje.

Przez takie pułapki **warto zabezpieczać się również na stronach zaufanych**. Przez zabezpieczenia rozumiem tu rzeczy ogólne -- zmianę adresu IP, czyszczenie ciasteczek, blokowanie elementów zewnętrznych. Nigdy nie wiadomo, na jaką stronę nas poniesie.

Również linki niebędące pułapkami i&nbsp;dodane przez samych uczestników ruchu oporu mogą nas wkopać! Stronka mogła bowiem nie wyłączyć przekazywania refererów przez swoje linki. A&nbsp;**referer zdradza, z&nbsp;jakiej strony przyszliśmy**.

Wyobraźmy sobie zatem, że przeglądamy zaufanego bloga *allsing-to-potwory.pl*. Znajdujemy tam linka do strony AllSinga -- niegroźnej, jakiegoś losowego artykułu newsowego. Klikamy, nie zabezpieczając się.

AllSing oczywiście nas rozpozna dzięki ciasteczkom, ale tym razem akurat to by nam nie przeszkadzało.  
Problem w&nbsp;tym, że dzięki refererowi odczyta też, że przychodzimy ze strony *allsing-to-potwory.pl*. Wniosek: czytaliśmy ją. A&nbsp;to stronka zakazana, więc po cichu oznaczą nasze konto jako element niepożądany.

Jak widzimy, zagrożenia mogą czaić się w&nbsp;różnych, nawet nieoczekiwanych miejscach. Ale w&nbsp;tej grze, jak i&nbsp;w życiu, nie jesteśmy bezradni. Skoro już wiemy, czym dysponuje strona śledząca i&nbsp;znamy swoje możliwości, czas nakreślić strategię.  
Przeciw zmyślonemu AllSingowi, jak i&nbsp;całkiem realnym molochom.

## Jak wygrać

Na koniec wyrwę nas z&nbsp;klimatu gry i&nbsp;rzucę więcej nazw z&nbsp;prawdziwego świata. W&nbsp;końcu to poradnik dotyczący prywatności.

Zacznę od tego, że **największym luksusem byłoby odizolowanie social mediów od reszty naszej aktywności**. Jak najpełniejsze.

Przykład: szerszy internet przeglądamy wyłącznie przez laptopa i&nbsp;domowego hotspota.  
Zaś konta w&nbsp;social mediach odwiedzamy tylko przez komórkę i&nbsp;internet mobilny (najlepiej przez przeglądarkę, nie apkę; ta druga może zbierać więcej danych).

Nie mieszamy tych dwóch światów. Jeśli będziemy korzystali z&nbsp;osobnych urządzeń i&nbsp;adresów IP, to jest mała szansa, że platformy powiążą naszą aktywność w&nbsp;szerszym internecie z&nbsp;aktywnością na ich własnych stronach. 

Oczywiście wiem, że **nie każdy ma taki luksus, więc teraz coś realniejszego**. Jeśli na jednym urządzeniu mieszamy różne formy aktywności, to przynajmniej zadbajmy o&nbsp;trzy fundamentalne rzeczy:

1. Bierzemy zaufaną przeglądarkę, blokującą niektóre metody śledzenia.

   [Brave](https://brave.com/pl/) dla ludzi lubiących działanie Chrome'a.  
   [Firefox](https://www.mozilla.org/pl/firefox/new/), jeśli cenimy mniejszych graczy (na komórce jako jeden z&nbsp;niewielu wspiera uBlock Origin).  
   [Tor Browser](https://www.torproject.org/download/) dla szczególnie wymagających.     
   Korzystamy z&nbsp;najnowszej wersji, bo tak będzie robiło więcej osób. Zlejemy się z&nbsp;tłumem.

2. Instalujemy na niej dodatek [uBlock Origin](https://ublockorigin.com/). Więcej informacji w&nbsp;[moim wpisie]({% post_url 2021-10-21-ublock-origin %}){:.internal}.

   O&nbsp;ile przeglądarka to nie Chrome ani Edge, które będą [aktywnie utrudniały]({% post_url 2022-05-11-google-manifest-v3 %}){:.internal} uBO pracę, to w&nbsp;ten sposób rozwiążemy problem śledzących elementów zewnętrznych.  
  Dodatek blokuje bowiem pobieranie bzdetów od znanych śledzących graczy. Ich listy są na bieżąco aktualizowane.

3. Trzymamy na komputerze zapasową, „normicką” przeglądarkę na wszelki wypadek.

   Może to być na przykład Chromium albo [Opera](https://www.opera.com/pl). Samego Chrome'a odradzam.  
   Tej zapasowej przeglądarki użyjemy w&nbsp;razie gdyby coś nie działało (to rzadkość, ale mogą się trafić strony mocniej scalone z&nbsp;elementami śledzącymi, nie wpuszczające z&nbsp;blokerami reklam itp.).

Te trzy drobne zmiany **pozwolą rozwiązać sprawę mniejszych elementów śledzących**, osadzonych na cudzych stronach. Wielu osobom może to wystarczyć. Ale bezpieczeństwa nigdy za wiele, więc porad mam więcej:

* Poświęćmy chwilę czasu na niewyrażenie zgód.

  Pod presją GDPR/RODO firmy od reklam śledzących zaczęły pytać o&nbsp;zgodę. Ale czasem stosują manipulację, ukrywając przed nami możliwość odmowy.  
  Często wyskakują nam szablonowe banery zawierające dwie opcje -- „Akceptuj wszystko” jaskrawszym kolorem oraz „Moje preferencje” kolorem szarym. Warto kliknąć w&nbsp;to drugie, zobaczyć czy nie ma tam zakładki „Uzasadniony interes”. Jeśli jest, to można tam odhaczyć zgody na śledzenie. 

* ...Albo zniszczmy baner.

  Osobiście używam czasem funkcji uBlock Origin, pozwalającej niszczyć kliknięty element. Podpiąłem ją pod skrót klawiszowy. Wystarczy że go nacisnę, najadę kursorem na baner i&nbsp;go usunę, żeby przestał zasłaniać mi stronę :sunglasses:

* Nie wierzmy zanadto w&nbsp;tryb incognito.

  Może i&nbsp;daje pewną ochronę przed plikami cookies, ale trwalszy efekt osiągniemy, regularnie je czyszcząc. Incognito zostawmy na sytuacje lżejsze. Kiedy chcemy np. obejrzeć filmik na YouTubie, ale nie chcemy żeby zaczęło polecać nam podobne.

* Zmieniajmy co jakiś czas adres IP.

  Bardzo możliwe, że zmienia nam się samoistnie. [Sprawdzajmy](https://duckduckgo.com/?q=ip+address&t=lm&ia=answer) co jakiś czas.  
  A&nbsp;jeśli nie, to możemy się łączyć przez jakiegoś zaufanego VPN-a. Przeglądarka Tor Browser również ma zmianę IP w&nbsp;pakiecie, ale bywa blokowana. Ewentualnie możemy się przejść po mieście i&nbsp;złapać hotspota na czas prywatnych wyszukiwań.

* Czyśćmy co pewien czas pliki cookies.

  Zaznaczając też pozostałe opcje, jak „Wyczyść pamięć podręczną”!

* Zwracajmy uwagę na to, w&nbsp;co klikamy.

  Najeżdżamy kursorem na link i&nbsp;patrzymy, co nam się wyświetla w&nbsp;lewym dolnym rogu. Jeśli zawiera znak zapytania, to znaczy że ma parametry, być może śledzące. Jeśli ma krótki adres (jak *bit.ly*) i&nbsp;zawiera ciąg znaków, to zapewne jest to przekierowanie śledzące.

  Niestety, żeby nie było zbyt prosto, czasem strony [podmieniają nam link](https://blog.seanmcelroy.com/2012/07/16/cnn-lies-to-every-one-of-its-web-viewers/) w&nbsp;momencie kliknięcia, korzystając z&nbsp;JavaScriptu. Widzimy jedno, a&nbsp;wchodzimy w&nbsp;coś innego.

  Dlatego bezpiecznym rozwiązaniem jest skopiowanie adresu linka.  
  Klikamy prawym przyciskiem myszy albo przytrzymujemy palcem. Potem opcja `Kopiuj adres odnośnika` (na niektórych przeglądarkach `adres linku`). Wklejamy go do paska adresu.

* Jeśli mamy do czynienia z&nbsp;parametrami w&nbsp;linku...
  
  Póki korzystamy ze wspomnianych wyżej przeglądarek, to jest szansa, że oczyszczą link ze znanych śmieci śledzących. Ale jeśli chcemy mieć pewność...

  Kopiujemy link do paska, metodą jak w&nbsp;punkcie wyżej.  
  Na próbę usuńmy wszystkie parametry (od `?` do końca) i&nbsp;spróbujmy odwiedzić stronę. Jeśli to nie działa, to przywróćmy część z&nbsp;nich (gdy jest ich więcej, są oddzielane znakami `&`).  
  Ogólnie kandydatami na parametry śledzące są dłuższe ciągi liczb lub znaków, więc to od nich zacznijmy usuwanie.  
  
  Jeśli odkryjemy, że jakieś parametry można bezpiecznie usuwać, to sobie to zapamiętajmy.

  Inna opcja to korzystanie z&nbsp;dodatku takiego jak [ClearURLs](https://github.com/ClearURLs/Addon), który automatycznie usuwa znane parametry śledzące z&nbsp;linków. Najlepszą reklamą dla nich jest fakt, że został kiedyś usunięty przez Google z&nbsp;bazy dodatków. A&nbsp;po protestach przywrócony.

* Jeśli link jest przekierowaniem śledzącym...

  ...To możemy skorzystać ze stronki-pośrednika jak [GetLinkInfo](https://www.getlinkinfo.com/). Wklejamy tam link, a&nbsp;ona odwiedzi przekierowanie za nas i&nbsp;powie nam, dokąd prowadziło. Możemy przejść prosto do celu.

  Na niektóre portale znaleziono też osobne sposoby. Na przykład żeby uniknąć linków śledzących Twittera, można skorzystać z&nbsp;[Nittera](https://nitter.net/), powielającego ich treści.  
  Wszystkie linki *t.co...* są tam zastąpione przez oryginalne linki dodane przez autorów. Co nie znaczy, że nie śledzą. Twitterowcy czasem sami korzystają ze skracarek.

  A&nbsp;jeśli już musimy sami wejść w&nbsp;przekierowanie, to przynajmniej zachowajmy ostrożność. Najlepiej -- wyłączony JavaScript, zmieniony adres IP, wyczyszczone pliki cookies.

* Jeśli nie chcemy ujawnić stronie B, że przychodzimy po kliknięciu linku na stronie A...

  W&nbsp;tym celu musimy pilnować, żeby nie wysłać referera. Niestety nasza przeglądarka domyślnie go dodaje.  
  Sposób partyzancki: zamiast klikać link, możemy po prostu skopiować go do paska adresu i&nbsp;potwierdzić wybór. W&nbsp;ten sposób nie wysyłamy referera.  
  Można również skorzystać z&nbsp;osobnego dodatku ucinającego referery, jak Referer Modifier.

* (Jeśli nam się chce) chodźmy po internecie z&nbsp;wyłączonym JavaScriptem.

  Są od tego specjalne dodatki, ale ja używam uBlock Origin. W&nbsp;razie potrzeby, jeśli strona nie działa, paroma kliknięciami włączymy skrypty. Uprzedzam: będziemy musieli to robić dość często. Świat stoi na JS-ie.

* Unikajmy podawania danych wrażliwych.

  Numer karty, zdjęcie dowodu, numer telefonu -- każda z&nbsp;tych rzeczy albo może nam mocno dokopać, albo jednoznacznie nas identyfikuje w&nbsp;świecie rzeczywistym. Jeśli jakaś prywatna organizacja o&nbsp;to pyta, to za wszelką cenę starajmy się uniknąć podawania tej informacji.

* Minimalizujmy liczbę używanych dodatków.

  Ostrzeżenie rychło w&nbsp;czas, kiedy tyle ich Wam podrzuciłem! :smiling_imp:  
  Ale cóż. Zdarzały się już przykłady [podkupienia dodatku](https://github.com/jspenguin2017/Snippets/issues/2) przez złoczyńców. A&nbsp;wiele z&nbsp;nich mogłoby wyrządzić spore szkody w&nbsp;nieodpowiednich rękach.  
  Dlatego, jeśli nie chcemy lub nie umiemy samodzielnie weryfikować ich kodu, warto zaufać tylko kilku wybranym.  

  W&nbsp;przypadku uBlock Origin pewną gwarancję daje nam to, że jest jednym z&nbsp;dodatków [ręcznie weryfikowanych](https://support.mozilla.org/kb/recommended-extensions-program) przez Mozillę.

* Jeśli jesteśmy właścicielami stron...

  Analitykę i&nbsp;bajery hostujmy w&nbsp;miarę możliwości u&nbsp;siebie. Wstrzymajmy się przed dodawaniem Google Fonts, Google Analytics, pikseli Facebooka itp. Niech chociaż parę zakamarków internetu będzie od nich wolnych.  
  Warto ustawić, na przykład w&nbsp;części `head` każdej naszej strony, opcję wyłączającą referery:

  <div class="black-bg mono">&lt;meta name="referrer" content="same-origin"/&gt;</div>

  Możemy też ochronić użytkowników przed ukrytymi przekierowaniami, nie pozwalając ukrywać w komentarzach linków pod innym tekstem niż prawdziwa nazwa strony.
  
  Poza tym możemy dodać skrypt, który będzie informował użytkowników dodających komentarze, że właśnie wkleili link z&nbsp;parametrem śledzącym, mogącym ich identyfikować. Zapewne opierałby się na którejś z&nbsp;publicznie dostępnych list. [Jak ta](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt).
  Taką usuwarką dysponuje np. podforum *Privacy* na Reddicie.

To tyle z&nbsp;moich pomysłów. Jeśli ktoś ma szczególnie bojowy nastrój, to może oprócz tego poczytać o&nbsp;sposobach, w&nbsp;jakie JavaScript profiluje ludzi, i&nbsp;spróbować opracować własne kontry. A&nbsp;zamiast uBO użyć dodatku [Ad Nauseam](https://adnauseam.io/), który jest na nim oparty, ale wysyła stronom śledzącym fałszywe dane.

## Koniec serii?

To podsumowanie kończy moją najdłuższą serię, „Internetową inwigilację”. Jej tworzenie było samą frajdą, mam nadzieję że równie przyjemnie się czytało :smile:

...Ale to taki koniec nie do końca!  
Nadal będę dodawał do serii wpisy, bo metody inwigilacji stale się rozwijają. Po prostu teraz przejdziemy od rzeczy codziennych i&nbsp;mainstreamowych do nieco bardziej subtelnych.

Chowanie się przed wzrokiem wścibskich telekomów. Analiza ruchu sieciowego. Bardziej kreatywne metody śledzenia. Wszystko to -- i&nbsp;pewnie trochę więcej -- w&nbsp;Internetowej Inwigilacji Plus. Pierwszy wpis już dodaję.

Planuję też rozpocząć serię o&nbsp;aplikacjach mobilnych. Jeśli uważacie, że włos się jeży od metod śledzenia przez internet, to poczekajcie tylko, aż zobaczymy możliwości aplikacji. Szpiegów dobrowolnie wpuszczonych do naszych telefonów.

Będzie się działo! Zapraszam do kolejnych wpisów.

