---
layout: post
title:  "Apki to pułapki 3 – historia SMS-ów"
subtitle: "Ludzie listy piszą. Apki je czytają."
description: "Ludzie listy piszą. Apki je czytają"
date:   2022-12-02 13:20:00 +0100
tags: [Android, Apki, Centralizacja, Inwigilacja, Podstawy]
firmy: [Google]
category: apki
category_readable: "Apki to pułapki"
image:
  path: /assets/posts/apki/sms/apki-sms-baner.jpg
  width: 1200
  height: 700
  alt: "Przerobiona grafika w stylu clipart, pokazująca włamywacza w pasiastym stroju biegnącego z workiem na plecach. Na worek nałożono trzy koperty."

---

SMS&#8209;y są stałą częścią życia prawie wszystkich posiadaczy telefonów.

Choć ich *pisanie* może być coraz rzadsze -- są wypierane przez komunikatory internetowe -- nadal całkiem często je *otrzymujemy*.  
Potwierdzenia odbioru, alerty RCB, kody uwierzytelniające... SMS&#8209;y dostajemy od różnych firm i&nbsp;instytucji, którym podaliśmy swój numer telefonu.

I tutaj pojawia się problem. Wszystkie te wiadomości są zapisywane na naszym telefonie bezterminowo (z tego co wiem). Żeby się ich pozbyć, musielibyśmy sami je usunąć z&nbsp;historii. A&nbsp;mało komu się chce.  
Co by się stało, gdyby zajrzał do nich ktoś niepowołany, ktoś wścibski? Jakie informacje by z&nbsp;nich odczytał?

Temu jest poświęcony mój obecny wpis. Zobaczymy pozwolenia na systemie Android pozwalające zaglądać nam do SMS&#8209;ów, aplikację pozwalającą osobiście to przetestować. Oraz sposoby na ochronę swojej prywatności.

Będzie raczej bez większych zaskoczeń, bo temat nie jest szczególnie skomplikowany. Ale może dostarczy nam paru dodatkowych przemyśleń.

<img src="/assets/posts/apki/sms/apki-sms-baner.jpg" alt="Przerobiona grafika w&nbsp;stylu clipart, pokazująca włamywacza w&nbsp;pasiastym stroju biegnącego z&nbsp;workiem na plecach. Na worek nałożono trzy koperty, z&nbsp;czego jedną z&nbsp;sercem pośrodku, symbolizujące skradzione wiadomości"/>

{:.figcaption}
Źródło: [WebStockReview](https://webstockreview.net/explore/burglar-clipart-cute/), przeróbki moje.

Tradycyjnie już -- nie dotykam tematu hakerów i&nbsp;cyberbezpieczeństwa. Zakładam że aplikacje zbierają dane oficjalnym, legalnym sposobem. Ale potem je wykorzystują do mniej etycznego profilowania.

## Skrzynka z&nbsp;SMS&#8209;ami

Z punktu widzenia użytkownika odbiór wiadomości to sprawa szybka i&nbsp;intuicyjna.

Idziemy sobie spokojnie, kiedy nagle czujemy w&nbsp;kieszeni wibrację. Patrzymy na ekran i&nbsp;widzimy, że przyszła wiadomość -- jest ikona dymka, nazwa nadawcy i&nbsp;początek treści. Po naciśnięciu palcem wyświetla się reszta. Czytamy, wracamy do ekranu głównego, odkładamy telefon.

Do raz otrzymanych wiadomości możemy sobie później wracać, korzystając z&nbsp;domyślnej, systemowej aplikacji. U&nbsp;mnie nazywa się po prostu `Wiadomości`.

SMS&#8209;y są w&nbsp;niej pogrupowane w&nbsp;wątki -- według nazwy odbiorcy -- zapewne dla łatwiejszego czytania. Po przekroczeniu pewnej ilości korespondencji od jednego odbiorcy tworzy się kolejny wątek, niezależny od poprzedniego.

{% include info.html
type="Porada"
text="Pozwolę sobie na błagalny apel w&nbsp;imieniu wielu użytkowników starszych, klasycznych telefonów – jeśli piszecie do kogoś takiego, to nie wysyłajcie wiadomości krótkich, po kilka słów, jak na czacie. Dajcie cały tekst za jednym razem.  
To dlatego, że na *starofonach* nie ma grupowania w&nbsp;wątki. Mikrowiadomości trzeba otwierać i&nbsp;zamykać jedną po drugiej, a&nbsp;potem po kolei kasować (jeśli nie chcemy czyścić całej skrzynki). Na dłuższą metę to męczące."
%}

Gdyby SMS&#8209;y mogła czytać tylko oficjalna aplikacja naszego telefonu, to wpis zakończyłby się w&nbsp;tym miejscu. **I&nbsp;tak podobno jest w&nbsp;przypadku systemu iOS** (na iPhone'ach).

Natomiast na Androidzie aplikacje mogą zaglądać do historii SMS&#8209;ów. W&nbsp;tym celu muszą jednak poprosić nas o&nbsp;pozwolenie. Zwane zakulisowo `READ_SMS`; z&nbsp;gatunku [*runtime permissions*](https://developer.android.com/guide/topics/permissions/overview#runtime), czyli takich, które możemy w&nbsp;dowolnym momencie wyłączać w&nbsp;ustawieniach.

Według [bloga firmy Symantec](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/mobile-privacy-apps) to pozwolenie stosunkowo rzadko wymagane. O&nbsp;dostęp do SMS&#8209;ów prosiło 15&nbsp;procent badanych przez nich, potencjalnie wścibskich apek na Androida.

{:.figure .bigspace}
<img src="/assets/posts/apki/sms/sms-pozwolenie-popularnosc.jpg" alt="Fragment listy pokazującej częstość, z&nbsp;jaką apki proszą o&nbsp;pozwolenia. Są na niej dwie pozycje, historia połączeń oraz SMS&#8209;y."/>

Ale tutaj możemy zadać sobie pytanie -- ile aplikacji potrzebowałoby tego pozwolenia *tak naprawdę, serio-serio*?

### Dwie minuty krytyki

Skorzystam z&nbsp;okazji i&nbsp;zbiorę w&nbsp;tym miejscu trochę krytyki wobec Google. Żeby nieco zrekompensować fakt, że mało ostatnio dodaję do [serii na ich temat](/serie/google){:.internal}.

Głównym źródłem aplikacji na świecie są centralne, publiczne bazy. Jak [Play Store](https://play.google.com/store/games) od tegoż Google.  
W teorii powinny weryfikować, czy apka naprawdę potrzebuje szczególnych uprawnień, jak możliwość czytania SMS&#8209;ów. I&nbsp;usuwać szemrane towarzystwo. Sęk w&nbsp;tym, że nawet naciągany powód wystarczy, żeby dostać pozytywną notę.

Przykład ze wspomnianego badania Symantec?  
O pozwolenie prosi apka-bajer sterująca funkcjami latarki w&nbsp;telefonie. Jako oficjalny powód podali fakt, że dzięki temu uprawnieniu latarka może migać, kiedy przyjdzie do nas wiadomość. Dostali się do bazy.

A po stronie użytkownika? Mamy niestety [jedno i&nbsp;to samo ostrzeżenie dla wszystkich działań związanych z&nbsp;SMS&#8209;ami](https://stackoverflow.com/questions/48634766/why-does-receive-SMS&#8209;and-read-sms-permission-do-not-have-different-prompt-boxes). Pozwolenia całkiem różne -- na wysyłanie i&nbsp;czytanie -- są zebrane w&nbsp;tak zwane *grupy uprawnień*. Kiedy aplikacja potrzebuje dowolnego z&nbsp;nich, to ujrzymy taki komunikat:

{:.bigspace}
<img src="/assets/posts/apki/sms/android-sms-permission.jpg" alt="Komunikat mówiący, że aplikacja prosi o&nbsp;pozwolenie na czytanie SMS&#8209;ów i&nbsp;dający na dole trzy opcje: wyrażenie zgody, niewyrażenie zgody albo niewyrażenie plus żądanie, żeby więcej nie pytać." width="300px"/>

Wyobraźmy sobie, że instalowana apka ma jakiś powód, żeby wysyłać wiadomości. Może na przykład twierdzi, że może wysyłać SMS&#8209;a z&nbsp;powiadomieniem, gdy coś zrobimy. Myślimy sobie: „brzmi sensownie”. I&nbsp;kiedy pokazuje się pytanie jak wyżej, to nasza czujność jest uśpiona. Zezwalamy. Zaś apka zyskuje również możliwość zerkania do naszej skrzynki.

Gdyby to zerkanie wymagało odrębnego, wyrażonego wprost pozwolenia, to może budziłoby ono większe podejrzenia. Byłoby znacznie mniej rodzajów apek, które *tak serio-serio* by go potrzebowały.  
Ba, nie byłoby potrzebne nawet wtedy, gdy aplikacja chce nam wysłać SMS&#8209;a i&nbsp;potem upewnić się że dotarł. Bo takie coś mogą [zrobić osobnym kanałem](https://android.stackexchange.com/a/218890), bez konieczności czytania całej skrzynki (choć niestety wymaga Usług Google, więc alternatywne systemy znów pokrzywdzone).

Jedynymi aplikacjami naprawdę potrzebującymi wglądu do SMS&#8209;ów zostałyby wtedy chyba tylko komunikatory, zbierające wiele rodzajów wiadomości w&nbsp;jednym miejscu. Moim zdaniem i&nbsp;tak opcja niewarta ryzyka.

...No ale jest jak jest. Mamy jedno łączone uprawnienie, zaś jedyną linią obrony dla osób nieświadomych zagrożeń są automatyczni recenzenci z&nbsp;Play Store'a.

A z&nbsp;nimi różnie bywa. Czasem przepuszczą łobuzów, a&nbsp;zablokują coś fajnego.  
Aplikacja Termux -- nieraz przeze mnie polecana -- daje możliwość automatyzowania pewnych funkcji telefonu. Siłą rzeczy potrzebuje różnych dodatkowych pozwoleń. Na szczęście jej kod źródłowy jest publicznie dostępny, w&nbsp;razie nieprawidłowości ktoś by szybko zaalarmował Google.

Mimo to [Termux nie dostał pozwolenia](https://android.stackexchange.com/questions/218888/apps-are-not-allowed-by-google-to-read-sms-messages-but-why-can-they-read-otp-s) na dostęp do SMS&#8209;ów i&nbsp;paru innych rzeczy. W&nbsp;efekcie Play Store zawiera jedynie okrojoną wersję tej aplikacji. Google :roll_eyes:

## Informacje zaszyte w&nbsp;SMS&#8209;ach

No ale dość dygresji. Skoro już wiemy, że Google zły, a&nbsp;Termux dobry... to przechytrzmy tego pierwszego. I&nbsp;użyjmy tego drugiego do sprawdzenia, co widzą aplikacje zaglądające do SMS&#8209;ów. 

Żeby nie rzucać tu technikaliami, proces instalowania Termuksa opisałem na końcu. Tu powiem tylko, że jest prosty. A&nbsp;kiedy już mamy co trzeba, wystarczy wpisywać polecenie `termux-sms-list`, żeby wyświetlać dane dotyczące SMS&#8209;ów.

Nie będę tu omawiał formatu, bo zasadniczo mamy te same informacje co w domyślnej aplikacji naszego telefonu. Różnica jest taka, że SMS&#8209;y nie są pogrupowane w&nbsp;wątki, tylko mają postać jednej płaskiej listy. Informacja o&nbsp;wątku ma natomiast nazwę `threadid` i&nbsp;jest częścią każdego SMS&#8209;a.

Co można z&nbsp;tych SMS&#8209;ów odczytać?

Pozwolę sobie pominąć SMS&#8209;y prywatne, wymienione z&nbsp;innymi ludźmi. Tam może być absolutnie wszystko :wink:  
Spójrzmy natomiast na informacje bardziej usystematyzowane. SMS&#8209;y otrzymane od wszelkiej maści firm i&nbsp;organizacji państwowych. Z&nbsp;nich też da się całkiem sporo wyłuskać.

### Alerty RCB

Poczciwe SMS&#8209;y ostrzegające nas, że idzie burza i&nbsp;warto schować rzeczy z&nbsp;balkonu. Nieraz żadna burza nie przychodzi, ale miło że ktoś o&nbsp;nas pamiętał.

Ale wiedzieliście, że do różnych rejonów trafiają różne wiadomości? Na przykład na obszarach wschodnich można było dostać swego czasu [SMS&#8209;y ostrzegające przed akcjami Łukaszenki](https://wiadomosci.radiozet.pl/Polska/Alert-RCB-dla-migrantow.-Wracaj-do-Minska!-Nie-przyjmuj-tabletek).

A to i&nbsp;tak nic w&nbsp;porównaniu z&nbsp;tym, co się działo w&nbsp;czasach covidowych. Alerty RCB były wysyłane **za każdym razem, kiedy odwiedziliśmy powiat mocniej dotknięty chorobą**.

{:.bigspace}
{% include comment.html
avatar = "/assets/draft_imgs/apki_draft/koperta.jpg"
author="Alert RCB"
text="Uwaga! Zaslon usta i&nbsp;nos. Powiat debicki w&nbsp;czerwonej strefie epidemicznej. Od 17.10 nowe zasady: https://www.gov.pl/zasadybezpieczenstwa"
%}

Kiedy pozbieramy SMS&#8209;y z&nbsp;pewnego konkretnego dnia, to układa się cała historia wyjazdu w&nbsp;Bieszczady w&nbsp;tamtym gorącym okresie (ograniczam się do powiatów z&nbsp;Podkarpacia):

* powiat dębicki,
* powiat ropczycko-sędziszowski,
* powiat strzyżowski,
* powiat brzozowski,
* powiat sanocki,
* powiat leski.

Oznaczmy sobie te powiaty na mapce:

<img src="/assets/posts/apki/sms/bieszczady-droga-smsy.jpg" alt="Mapka z&nbsp;Wikipedii pokazująca województwo podkarpackie w&nbsp;podziale na powiaty. Czerwonym kolorem zaznaczono kilka z&nbsp;nich w&nbsp;południowej części mapki"/>

Patrząc dodatkowo na czas wysłania SMS&#8209;ów, można łatwo dojść do wniosku, że był to przejazd samochodowy, bez robienia dłuższych przerw.

Owszem, taka szczegółowość nie jest w&nbsp;alertach RCB dostępna na co dzień. Tym niemniej mogą być sposobem na ustalenie przybliżonego regionu, w&nbsp;jakim mieszkamy, oraz tras niektórych podróży w&nbsp;czasach pandemicznych.

### Powiadomienia od zagranicznych operatorów

Pociągnijmy dalej wątek podróżniczy. Poza granice kraju -- bo kiedy ją przekraczamy, często dostajemy z&nbsp;automatu jakieś powiadomienie.

Jasne, nie jest to metoda stuprocentowo dokładna. Czasem wystarczy zbliżyć się do granicy, żeby dostać wiadomość od zagranicznego operatora.  
Jest tu ktoś, kogo w&nbsp;polskich górach złapała sieć czeska lub słowacka? Albo, co gorsza, ktoś kto stracił w&nbsp;Bieszczadach majątek przez nagłe przejście na taryfę ukraińską? :smiling_imp:

Wiadomości są natomiast znacznie pewniejszym źródłem, jeśli mówią o&nbsp;kraju otoczonym wodami, takim jak Cypr albo Islandia. Jeśli taki kraj nas witał u&nbsp;siebie, to raczej tam byliśmy. A&nbsp;przynajmniej nasz telefon.

Oto wiadomość, jaką dostałem w&nbsp;czasach pandemii po zarejestrowaniu się w&nbsp;systemie na wjazd do Czech:

{% include comment.html
avatar = "/assets/draft_imgs/apki_draft/koperta.jpg"
text = "NCZI: **IMIĘ I&nbsp;NAZWISKO** Your registration on arrival from abroad has been registered.You meet the 14-day quarantine exemption.You don't have to go through quarantine"
%}

{:.figcaption}
Pisownia oryginalna, tam też nie dawali spacji po kropkach. Przez co dwie rzeczy w&nbsp;domyślnej apce z&nbsp;SMS&#8209;ami błędnie oznacza mi jako linki.

Choć może to brzmieć nieintuicyjnie, **nasze prawdziwe imię i&nbsp;nazwisko to często tajemnica dla aplikacji**. Nie mają łatwego sposobu na ich poznanie, bo podczas zakładania kont (i na Androidzie, i&nbsp;na różnych portalach) zwykle nie musimy nigdzie podawać prawdziwych danych.

Ale SMS&#8209;y łatwo mogą nas ujawnić. Wystarczy że zapiszemy się do jakiejś rzeczy poważnej i&nbsp;urzędowej, gdzie użytkownik *Kubuś Puchatek* by nie przeszedł. Dostaniemy potwierdzenie na skrzynkę. A&nbsp;dla wścibskich aplikacji to tak, jakbyśmy się im przedstawili.

### Konta i&nbsp;subskrypcje

Nieraz zdarza się, że musimy podać numer telefonu przy zakładaniu konta. Dostajemy wtedy jednorazowy kod potwierdzający.

{:.bigspace}
{% include comment.html
avatar = "/assets/draft_imgs/apki_draft/koperta.jpg"
author="BIEDRONKA"
text="Dziekujemy za rejestracje w&nbsp;programie Moja Biedronka. Wprowadz podany kod w&nbsp;formularzu rejestracyjnym na stronie www. KOD: **6-CYFROWY KOD**"
%}

Na szczęście ta liczba raczej by nie wystarczyła do podebrania nam konta. A&nbsp;przynajmniej wtedy, gdy ktoś ma *jedynie* wgląd do SMS&#8209;ów, a&nbsp;usługa wysyłająca nam kod zadbała o&nbsp;bezpieczeństwo. Kod powinien być przypisany do konkretnej sesji w&nbsp;przeglądarce, rozpoczętej specjalnie dla nas, niedostępnej dla obcych.

Ale nie będę tu zgrywał eksperta, bo ocieramy się o&nbsp;kwestie hakerskie, które znam słabo.

Natomiast z&nbsp;punktu widzenia prywatności -- na podstawie takich jednorazowych wiadomości da się ustalić, z&nbsp;jakich usług korzystamy. „Ma Facebooka (i ustawiał na nim zabezpieczenie przez SMS)”. „Ma Signala”. „Ma konto w&nbsp;banku X”. „Ma kartę stałego klienta w&nbsp;Biedronce”.

I choć Biedronka czy Facebook raczej zlewają się z&nbsp;tłumem, to inne przykłady mogą bardziej nas wyróżniać.  
Gdyby wiadomości o&nbsp;założeniu konta przyszły od stron/aplikacji reprezentujących węższe grupy osób (mniejszości seksualne, wyznawców konkretnej religii, osoby z&nbsp;jakąś przypadłością), to takie SMS&#8209;y dawałyby podglądaczom cenne i&nbsp;osobiste informacje.

### Usługi kurierskie

Kiedy zamówimy coś przez internet, to często za dostarczenie paczki odpowiada któryś ze znanych pośredników. I&nbsp;informuje nas SMS-owo o&nbsp;punkcie odbioru. Podając przy tym jego adres.

{% include comment.html
avatar = "/assets/draft_imgs/apki_draft/koperta.jpg"
author = "PP S.A"
text="Przesylka nr **NUMER**, kod odbioru **KOD**, czeka na odbior w&nbsp;sklepie Zabka ul. **ULICA I&nbsp;NR LOKALU**, **NAZWA MIASTA**"
%}

{:.bigspace-after}
{% include comment.html
avatar = "/assets/draft_imgs/apki_draft/koperta.jpg"
author = "DHL"
text="Przesylka nr **NUMER** adres DHL POP ZABKA, **ULICA I&nbsp;NR LOKALU**, **KOD POCZTOWY NAZWA MIASTA**."
%}

To znacznie dokładniejsze dane niż te z&nbsp;alertu RCB, informującego o&nbsp;ogólnym rejonie, do tego tylko czasami.  
Tu natomiast można założyć, że raczej wysyłamy paczki do punktu blisko siebie. Więc ktoś patrzący na takie SMS&#8209;y byłby w&nbsp;stanie nas namierzyć z&nbsp;dokładnością co do osiedla. Albo jeszcze większą.

### Placówki zdrowotne

Może przykład covidowy?

{:.bigspace}
{% include comment.html
avatar = "/assets/draft_imgs/apki_draft/koperta.jpg"
author="e-Zdrowie"
text="Twoje szczepienie (**NAZWA SZCZEPIONKI**):  
**DATA I&nbsp;GODZINA** w&nbsp;punkcie **ULICA I&nbsp;NR LOKALU** w&nbsp;**NAZWA MIASTA**."
%}

Tutaj jak wyżej -- nasze miejsce zamieszkania. Może nieco ogólniejsze niż przy paczkach, bo jednak nie każde osiedle ma swoją przychodnię.

Co gorsza, jest tu informacja związana ze zdrowiem. I&nbsp;informacja dla potencjalnych stalkerów, gdzie i&nbsp;o której mogą się z&nbsp;nami spotkać -- bo skoro na coś się umówiliśmy, to jest niemała szansa, że tam będziemy.

### Zawody sportowe

Zapisaliśmy się na coś, z&nbsp;własnej pasji albo za namową znajomych. Trochę wysiłku, a&nbsp;potem mnóstwo satysfakcji. A&nbsp;na deser SMS z&nbsp;gratulacjami po przekroczeniu linii mety.

Ale ta słodycz może nieco zgorzknieć, jeśli ktoś się do tego SMS&#8209;a dobierze. Bo ten zawiera nasze imię i&nbsp;nazwisko, czas ukończenia zawodów oraz miejsce, jakie zajęliśmy w&nbsp;ogólnej klasyfikacji.

{:.bigspace}
{% include comment.html
avatar = "/assets/draft_imgs/apki_draft/koperta.jpg"
author="+48 737&nbsp;*??? ???*{:.cover}"
text="Wyn. nieof. **NAZWA ZAWODÓW** dla **NAZWISKO I&nbsp;IMIĘ**. Czas **CZAS UKOŃCZENIA**, Msc: **MIEJSCE W&nbsp;KLASYFIKACJI OGÓLNEJ** wiecej na WYNIKI.B4SPORT.PL"
%}

Pomijając fakt, że ujawniamy w&nbsp;ten sposób z&nbsp;grubsza swoją kondycję i&nbsp;zainteresowania, te informacje mogłyby być punktem wyjścia do dalszego stalkingu. Zawsze można potem wejść na listę wyników na stronie organizatora ([przykład](http://www.online.datasport.pl/results3611/index.php)) i&nbsp;wyszukać konkretne imię i&nbsp;nazwisko na liście startowej.

Zwykle będzie tam również nazwa miasta, z&nbsp;którego jesteśmy, a&nbsp;czasem nazwa drużyny. Na podstawie identycznej, nieczęstej nazwy można ustalić, kto jest naszymi znajomymi. A&nbsp;przez nich na przykład znaleźć nasze konto na Facebooku, nawet jeśli używamy pseudonimu. Możliwości nadużyć jest multum.

## Jak się chronić

Jak widać, SMS&#8209;y mogą całkiem sporo o&nbsp;nas zdradzać. Nawet jeśli pominiemy te najbardziej osobiste i&nbsp;ograniczymy się do masówki wysyłanej przez rozmaite firmy.

Przede wszystkim najlepiej **nie dawać aplikacjom pozwolenia na dostęp do skrzynki z&nbsp;SMS&#8209;ami**. Naprawdę nie sądzę, żeby było potrzebne czemukolwiek poza domyślną, systemową apką. Wygoda nie jest warta ryzyka.

Poza tym warto regularnie czyścić skrzynkę. Nawet jeśli nic nie ma u&nbsp;nas pozwolenia -- zawsze może się zdarzyć sytuacja nagła, gdy działamy w&nbsp;pośpiechu i&nbsp;coś instalujemy. A&nbsp;wystarczy chwila i&nbsp;nasze SMS&#8209;y przestają być nasze. W&nbsp;takim razie lepiej ich nie mieć niż polegać na pozwoleniach i&nbsp;potem żałować.

A co zrobić, jeśli przed usunięciem chcemy zrobić sobie kopię zapasową SMS&#8209;ów?

Istnieją zapewne bardziej oficjalne sposoby. Ale że jestem majsterkowiczem, a&nbsp;Termux jest fajny i&nbsp;pokrzywdzony przez Google, to właśnie jego użyję w&nbsp;roli przykładu. Poniżej krótki samouczek. A&nbsp;osoby niechętne mogą po prostu powyłączać pozwolenia i&nbsp;wyczyścić skrzynkę.

## Bonus: chowanie SMS&#8209;ów w&nbsp;Termuksie

### Instalacja

O tej aplikacji już parę razy wspomniałem. Wpisujemy w&nbsp;nią różne komendy, pozwalające na przykład chodzić po folderach i&nbsp;wyświetlać pliki.  
Tym razem natomiast nie wystarczy nam wersja podstawowa. Potrzebujemy rozszerzonych funkcji Termuksa -- w&nbsp;szczególności możliwości zaglądania do skrzynki SMS&#8209;ów.

Jak wspomniałem, oficjalna wersja z&nbsp;Play Store'a jest wybrakowana. Zatem trzeba wykonać trzy kroki, żeby zyskać możliwość czytania SMS&#8209;ów przez Termuksa:

1. Pobrać aplikację [F-Droid](https://f-droid.org/).
2. Zainstalować **przez F-Droida** dwie aplikacje: Termux oraz Termux:API.

   To ważne, bo na Google Play są wybrakowane wersje. A&nbsp;po co dwie apki? Bo Termux:API jest potrzebna, żeby mieć dostęp do rozszerzonych funkcji.

3. Włączyć Termux:API pozwolenie na dostęp do listy SMS&#8209;ów. 

Kiedy już wszystko naszykujemy, jesteśmy w&nbsp;stanie wpisywać w&nbsp;Termuksa komendę odczytującą SMS&#8209;y:

<div class="black-bg mono">
termux-sms-list
</div>

Po chwili powinna się pokazać lista 10&nbsp;wiadomości. 

### Zapisywanie do wspólnego pliku

Zamiast wrzucać niezrozumiałego gotowca, pokażę krok po kroku, w&nbsp;jaki sposób *konstruuję* skrypt.

Trzonem jest nasze polecanie pozwalające zdobywać listę SMS&#8209;ów, `termux-sms-list`.  
Za tym poleceniem można zapisywać różne dodatkowe *argumenty*, które pozwalają kontrolować zachowanie programu. Ich listę znalazłem na [*termux.com*](https://wiki.termux.com/wiki/Termux-sms-list).

* Po pierwsze: jeśli chcemy wszystkie rodzaje wiadomości (SMS&#8209;y, MMS-y...), dopisujemy po naszym trzonie `-t all`.  
* Po drugie: to polecenie domyślnie bierze tylko 10&nbsp;wiadomości. Żeby zgarnąć całą historię, trzeba kazać Termuksowi brać więcej. Zapiszmy na przykład `-l 100000`.

  Liczba oznacza tu, ile wiadomości chcemy brać. Jeśli będzie za duża, to nic nie szkodzi, Termux weźmie tylko tyle SMS&#8209;ów, ile mamy w&nbsp;skrzynce. Można poszaleć z&nbsp;zerami.

Gdybyśmy już teraz użyli naszego polecenia, to by jedynie *wyświetliło dane na ekranie*. I&nbsp;to nie wszystkie, bo Termux przycina tekst, gdy jest za dużo linijek.  
Nie do końca o&nbsp;to nam chodzi. Dlatego czas na ostatni krok i&nbsp;rozszerzenie polecenia o&nbsp;zapisanie wiadomości do pliku. 

A jakiego pliku? Wystarczy zwykły tekstowy. Powiedzmy, że chcemy go nazwać *smsy.txt*.  
Żeby to do niego zapisać efekt działania naszej komendy, wystarczy dodać na samym jej końcu: `> smsy.txt`.  
Dla pewności dałbym dwie strzałki zamiast jednej -- `>>`. W&nbsp;ten sposób nie nadpisujemy treści pliku, tylko dodajemy tekst do istniejącego.

W normalnym przypadku, gdy od razu po zrobieniu kopii zapasowej przenosimy plik w&nbsp;inne miejsce, nie robi to różnicy. Ale chroni nas przed wpadką. Bo gdybyśmy zrobili zrzut SMS&#8209;ów, zapomnieli go przenieść, a&nbsp;potem stworzyli kolejny, to byśmy stracili ten pierwszy. Mając podwójną strzałkę, nie stracimy. Lepiej dmuchać na zimne :wink:

Ostatecznie nasz skrypt wygląda tak:

```
termux-sms-list -t all -l 100000 >> smsy.txt
```

{:.figcaption}
Gdyby nie pokazywało całego tekstu (częste na mobilnych), można przesunąć czarny pasek palcem.

Pamiętajmy o&nbsp;spacjach! Można dla pewności po prostu przekleić cały tekst stąd do Termuksa.

Kiedy tego użyjemy, to w&nbsp;folderze głównym Termuksa (niedostępnym dla innych typowych aplikacji) powinien nam powstać plik *smsy.txt*, zawierający wszystkie nasze wiadomości.

Dla pewności można do niego zajrzeć, na przykład wpisując `less smsy.txt`. Naciskając strzałki w&nbsp;górę i&nbsp;w&nbsp;dół (część Termuksa), możemy przewijać treść. Naciskając `q`, wychodzimy z&nbsp;programu.

Kiedy upewnimy się, że wszystko zrzucone, to możemy usunąć wiadomości ze skrzynki telefonu, przez oficjalną systemową apkę. Inne aplikacje już ich nie zobaczą, bo od teraz istnieje wyłącznie kopia „w&nbsp;brzuchu” Termuksa, poza zasięgiem innych.

{% include info.html
type="Uwaga"
text="Pamiętajmy, żeby nie odinstalowywać teraz Termuksa, bo w&nbsp;ten sposób skasowalibyśmy wszystko, co w&nbsp;nim jest. Również nasze SMS&#8209;y."
%}

### Przenoszenie poza telefon

Wiadomości ukryte w&nbsp;Termuksie są niewidoczne dla obcych, ale i&nbsp;niedostępne dla naszego własnego komputera. Jak je przenieść?

Ktoś bardziej majsterkujący mógłby użyć Termuksa do wysłania ich przez Bluetooth prosto na komputer. Ale my zrobimy to klasycznie, przenosząc plik do wspólnej przestrzeni i&nbsp;zgrywając na komputer przez USB.

**Uwaga:** nim to zrobimy, wyłączmy pozwolenie na dostęp do plików apkom, którym nie ufamy. Nie chcemy, żeby dobrały się do SMS&#8209;ów , kiedy te trafią między publiczne pliki. Pozwolenie musimy natomiast zostawić Termuksowi, żeby był w&nbsp;stanie przenieść plik.

Następnie wpisujemy (uwaga na spacje!) albo kopiujemy stąd:

```
mv smsy.txt /data/storage/emulated/0
```

To polecenie przeniesie plik do folderu głównego na naszej karcie pamięci (publicznie dostępnego). Zamiast `mv` można użyć `cp`, jeśli chcemy jedynie skopiować plik.
 
Teraz podłączamy telefon do komputera przez USB i&nbsp;wybieramy na nim (telefonie) tryb pamięci masowej. Znajdujemy nasz plik, wycinamy z&nbsp;Androida i&nbsp;wklejamy gdzieś na komputerze. Jeśli ktoś woli, to może też wysłać go przez Bluetooth, przez domyślną przeglądarkę plików na telefonie.

Kiedy już zrobimy co trzeba i&nbsp;plik opuści nasz telefon, możemy przybić sobie piątkę. Nasze SMS&#8209;y będą od teraz (oby) wyłącznie w&nbsp;naszych rękach, poza zasięgiem wścibinosów.
