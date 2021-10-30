---
layout: post
title: "Internetowa inwigilacja 7 – wstęp do plików cookies"
subtitle: "„Masz coś ode mnie?”"
date:   2021-10-22 01:35:00 +0100
tags: [Internet, Inwigilacja, Podstawy, Porady]
firmy: [Amazon, Facebook, Google]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: "pliki-cookie/straznik-polaczone.jpg"
image-width: 1023
image-height: 520
---

W ramach „Internetowej inwigilacji” piszę póki co o&nbsp;nagłówkach HTTP -- swoistej *wizytówce* z&nbsp;informacjami, które za kulisami wysyła stronom internetowym nasza przeglądarka.

W tych wpisach przyjąłem pewną analogię -- **Internet jest jak sieć placówek pocztowych. Przesyłają między sobą listy i&nbsp;paczki z&nbsp;dowolną zawartością**.

Nagłówki HTTP to odpowiednik etykiet naklejonych na te przesyłki. Zawierają adres nadawcy oraz informacje o&nbsp;tym, jak obchodzić się z&nbsp;przesyłką. Każdy, kto dostanie przesyłkę, może je odczytać.

Powoli zbliżamy się do końca, jeśli chodzi o&nbsp;informacje z&nbsp;tych „etykiet”. Czas na jedną szczególnie kluczową. Do tego stopnia, że chyba każdy choć raz usłyszał to pojęcie.

Czas na pliki cookies (z angielskiego „ciasteczka”).

W tym wpisie skupię się na jednym z&nbsp;dwóch głownych rodzajów: **na ciasteczkach od stron bezpośrednio odwiedzanych** (ang. *first-party cookies*).

Drugi rodzaj (*third-party cookies*; ciasteczka od stron zewnętrznych) zostawimy na przyszły wpis.

## O&nbsp;ciasteczkach po ludzku

Pliki cookies pełnią kluczową rolę w&nbsp;śledzeniu użytkowników, więc warto dobrze je poznać. Dlatego zaczniemy od przykładów na pobudzenie wyobraźni.

Mówiąc najprościej: **to strzępki danych, które strony internetowe „dają” naszej przeglądarce**. Ta zapisuje je na dysku. A&nbsp;przy kolejnych kontaktach pokazuje je tym samym stronom, od których je dostała.

# Do czego służą

Zastosowań ciasteczek jest mnóstwo. Jednym z&nbsp;częstszych jest umożliwienie nam logowania się na nasze profile/konta.

W tym wypadku **pliki cookies są jak identyfikator noszony na smyczce**, taki *badge* w&nbsp;korpojęzyku.

Podczas pierwszych odwiedzin na terenie firmy jesteśmy jeszcze obcy, nie wszędzie nas wpuszczają.

{:.figure .bigspace}
<img src="/assets/posts/pliki-cookie/straznik-nie-wpuszcza.jpg" alt="Przeróbka pewnego mema. Widać ochroniarza w&nbsp;czarnym ubraniu zastawiającego ciałem drzwi. Na jego twarz naklejono logo Facebooka, a&nbsp;na klatkę piersiową pole z&nbsp;komunikatem mówiącym 'Zaloguj się'."/>

Ale jeśli nas zatrudnią (*zalogujemy się*), to dostajemy własny identyfikator (*ciasteczko*). Od tej pory, nosząc go przy sobie, możemy swobodnie wchodzić do różnych firmowych pomieszczeń (*na podstrony*).

{:.figure .bigspace}
<img src="/assets/posts/pliki-cookie/straznik-wpuszcza.jpg" alt="Przeróbka drugiego panelu z&nbsp;mema. Na pierwszym planie doklejono rękę trzymającą kilka ciasteczek. Na drugim planie ochroniarz uchyla drzwi. Zamiast twrzy ma naklejone logo Facebooka."/>

Oczywiście ciasteczka służą nie tylko do rozróżnienia „swój czy obcy”. Mogą zawierać dowolną informację:

* listę wybranych przez nas produktów

  (wtedy są jak koszyk na zakupy, do którego dokładamy różne rzeczy);

* ile zebraliśmy punktów  
  
  (jak karta stałego klienta, na której nabija się pieczątki);

* do której należymy grupy  

  (jak opaska w&nbsp;hotelu, dająca różne przywileje dla różnych grup);

* ...i wiele, wiele innych.

Jedna rzecz jest uniwersalna. Każde ciasteczko to jakaś informacja, którą dostajemy od strony internetowej.  
Potem, kiedy ją pokazujemy tej samej stronie, zapewne będziemy traktowani inaczej, niż gdybyśmy jej nie mieli.

Czasem spotykam zwrot „ciasteczka cię śledzą”. Nie. To straszny skrót myślowy. **To tylko tekst i&nbsp;same nie są do niczego zdolne**. Są równie martwe jak ten identyfikator na smyczce.

Ewentualne śledzenie następuje po stronie osób (*serwerów*), którym pokazujemy nasze ciasteczka. To one, otrzymując tę informację, mogą robić różne rzeczy.

# Jak są przechowywane

Niektórzy, pisząc o&nbsp;przechowywaniu plików cookies, korzystają z&nbsp;analogii *słoja z&nbsp;ciasteczkami*. Ale moim zdaniem nie do końca oddaje ona rzeczywistość.

W słoju wszystko jest trzymane razem, wymieszane ze sobą. Tymczasem pliki cookies są ściśle podzielone według tego, od jakich stron pochodzą.

Zamiast słoja wolę porównanie do **szafy z&nbsp;ciasteczkami**. Takiej z&nbsp;wieloma przegrodami. Zresztą podobnych używa się na poczcie, więc pasuje też do naszej głównej analogii.

{:.bigspace}
<img src="/assets/posts/pliki-cookie/szafa-cookies.jpg" alt="Zdjęcie pokazujące szafę na dokumenty z&nbsp;wieloma przegrodami." height="300px">

Inne możliwe skojarzenie to kalendarz adwentowy. Wiele małych, odrębnych przegródek, w&nbsp;każdej coś słodkiego.

Nasuwa się pytanie: czy strona internetowa A&nbsp;może podejrzeć ciasteczka przeznaczone dla strony B? Albo podrzucić coś do przegródki dla strony B?

Na szczęście nie. Każda ma własną przegródkę i&nbsp;**nie może w&nbsp;żaden sposób ingerować w&nbsp;pliki cookies dla innych stron**. Przeglądarka tego pilnuje.

Tym niemniej strona B&nbsp;może być swoistym „gościem” na stronie A. Wtedy może dawać ciasteczka we własnym imieniu.  
To tak zwane *third-party cookies*, które dokładniej omówię w&nbsp;kolejnym wpisie.

{% include info.html type="Ciekawostka" trailer="Czasem odpowiednie ciasteczko to wszystko, czego potrzeba do wejścia na konto, więc lepiej trzymać je w&nbsp;tajemnicy.
<p>
Istnieje coś takiego jak <strong>kradzież ciasteczek</strong>, czyli skopiowanie ich i&nbsp;próba wejścia z&nbsp;nimi na nasze konta. Dlatego, dopuszczając obcą osobę do naszego komputera, lepiej jej patrzmy na ręce (nawet jeśli nie otwiera niczego poza przeglądarką plików).
</p><p>
Niektóre strony stosują dodatkowe zabezpieczenia i&nbsp;oprócz ciasteczek patrzą na inne informacje od nas, takie jak <em>user agent</em> albo <em>adres IP</em> (omawiane w&nbsp;poprzednich wpisach). Jeśli widzą coś nietypowego, to nas nie wpuszczają.
</p><p>
To zabezpieczenie to taki odpowiednik czujnej osoby z&nbsp;recepcji. Widzi oficjalnego <em>badge'a</em>, ale pamięta że do tej pory pokazywała go ruda dziewczyna, a&nbsp;nie łysy brodacz. Czyli coś się nie zgadza.
</p>"
%}

# Jak się ich używa

Czas na bardziej całościowy przykład.

Wróćmy do analogii pocztowej. Tak może wyglądać przykładowa komunikacja z&nbsp;wykorzystaniem ciasteczek:

1. Prosimy personel w&nbsp;okienku (*przeglądarkę*) o&nbsp;kontakt z&nbsp;jakimś adresatem/stroną (*wysłanie żądania*). 
2. Personel poczty zerka, czy ten adresat ma swoją przegródkę w&nbsp;szafie. Na razie nie.
3. Wysyła adresatowi naszą przesyłkę.
4. Adresat odsyła coś od siebie.

   Do koperty przyklejona jest informacja dla poczty, np. „proszę do wszystkich przesyłek dla mnie dopisywać `hasło=okoń`”. Poczta zakłada tej stronie jej własną przegródkę w&nbsp;szafie i&nbsp;umieszcza w&nbsp;niej tę informację.

5. Od tej pory za każdym razem, gdy prosimy o&nbsp;wysłanie czegoś tej stronie, pracownik dopisuje na kopercie ustalone hasło.
6. Dzieje się tak aż do odwołania. Które może nastąpić na kilka sposobów:

   * wprost poprosimy o&nbsp;usunięcie zawartości szafy (*wyczyszczenie plików cookies*);
   * strona „nadpisze” hasło (np. prześle dopisek „od teraz proszę pisać `hasło=panga`”);
   * minie termin ważności, jeśli jakiś był (np. przy wzmiance o&nbsp;haśle mogła być też adnotacja „proszę dopisywać to hasło tylko do dnia 11.11.2021”)

## Pliki cookies w&nbsp;praktyce

Dość już analogii i&nbsp;pobudzania wyobraźni, czas na prawdziwy przykład z&nbsp;przeglądarki. 

Żeby odpocząć od różnych portali społecznościowych, wziąłem na warsztat stronkę FlixBusa.

Przede wszystkim przed wejściem na nią usunąłem wszystkie ciasteczka (opcja `Usuń historię przeglądania`), żeby być na świeżo.

Następnie otworzyłem sobie narzędzia przeglądarki (skrót `Ctrl+Shift+I`) i&nbsp;zakładkę `Sieć`, żeby widzieć dokładnie, jakie dane wysyłały sobie strona i&nbsp;przeglądarka.

# Pierwsza wizyta

Po tych przygotowaniach wszedłem na stronę. Na liście wyświetliły się różne pliki, jakie pobrała moja przeglądarka. Kliknąłem na pierwszy od góry, czyli główną stronę. Potem zerkałem w&nbsp;zakładki `Nagłówki` i&nbsp;`Ciasteczka`.

{:.bigspace}
<img src="/assets/posts/pliki-cookie/firefox-pliki-cookies.jpg" alt="Połączone zrzuty ekranu z narzędzi przeglądarki Firefoksa. Cyframi 1, 2 i 3 oznaczyłem, co trzeba było kliknąć."/>

Znalazłem tam takie informacje (edytowane dla przejrzystości):

{:.figure .bigspace}
<img src="/assets/posts/pliki-cookie/cookies-otrzymane.jpg" alt="Lista plików cookies. Listę elementów wysłanych zastąpiłem tekstem mówiącym, że nie ma tam nic o plikach cookies. Na liście elementów otrzymanych zaznaczyłem dwa elementy."/>

Przy pierwszym kontakcie nasza przeglądarka nie wysłała nic związanego z&nbsp;ciasteczkami.  
Za to dostała dwa w&nbsp;nagłówkach odpowiedzi od FlixBusa! (Oznaczyłem je zieloną ramką). O&nbsp;tajemniczych nazwach *AWSALB* oraz *AWSALBCORS*.

Można również wyświetlić dokładniejsze informacje o&nbsp;tych ciasteczkach:

{:.figure .bigspace}
<img src="/assets/posts/pliki-cookie/cookies-szczegoly.jpg" alt="Szczegółowe informacje dotyczące dwóch plików cookies."/>

Widać w&nbsp;tym miejscu, że oba z&nbsp;nich zawierają datę wygaśnięcia (`expires`) oraz wartość (`value`), będącą w&nbsp;tym wypadku ciągiem losowych znaków.

Widać też, że ciasteczka są identyczne pod względem atrybutów, ale ciasteczko *AWSALBCORS* zawiera dwa dodatkowe: `samesite` i&nbsp;`secure`.

Co ciekawe, gdybyśmy weszli w&nbsp;jeszcze inną zakładkę `Dane > Ciasteczka`, to znaleźlibyśmy ich jeszcze więcej!  
Łącznie **strona FlixBusa dała mojej przeglądarce 8 ciasteczek**.

Dlaczego w&nbsp;zakładce `Sieć` widać tylko dwa, a&nbsp;w zakładce `Ciasteczka` więcej?

To dlatego, że pozostałe ciasteczka nie zostały wysłane do nas w&nbsp;nagłówkach, tylko najwidoczniej wstawione **przez kod JavaScript**.  
Daje on stronom interaktywność i&nbsp;jeszcze o&nbsp;nim opowiem w&nbsp;przyszłym wpisie. Ale póki co zapamiętajmy tylko, że pliki cookies możemy otrzymać na różne sposoby.

Za kulisami wszystkie 8 ciasteczek nasza przeglądarka włożyła do swojej „szafy z&nbsp;przegródkami”. Pliku *cookies.sqlite*, czyli bazy danych gdzieś w&nbsp;wewnętrznym folderze Firefoksa.

Tyle przy pierwszej wizycie. A&nbsp;jeśli teraz wejdziemy na stronę ponownie (albo np. ją odświeżymy, naciskając `F5`), to co nam się ukaże w&nbsp;informacjach o&nbsp;*cookies*?

# Druga wizyta

Znowu otrzymujemy w&nbsp;nagłówkach od Flixbusa dwa ciasteczka, *AWSALB* i&nbsp;*AWSALBCORS*. Ale oprócz tego nasza przeglądarka wysłała coś od siebie!

{:.figure .bigspace}
<img src="/assets/posts/pliki-cookie/cookies-szczegoly-druga-wizyta.jpg" alt="Pliki cookies przesłane stronie przez moją przeglądarkę podczas drugiej wizyty. Niektóre z nich, takie jak to o nazwie sp, mają nazwy złożone z długich ciągów znaków."/>

U mnie ciasteczka wysłane nieco się różnią od otrzymanych, bo o&nbsp;jeden raz za dużo je wyczyściłem między wizytami. *Mea culpa*.

Ale w&nbsp;normalnym wypadku **to te same 8 ciasteczek, które przeglądarka poprzednio umieściła „w szafie”**.

Po ich otrzymaniu serwer Flixbusa może potraktować nas inaczej niż kogoś, kogo wcześniej nie widział. Ale przede wszystkim -- jeśli coś teraz kupimy, to będzie mógł za kulisami powiązać informacje.

*„Osoba z&nbsp;takim samym `sp` kupiła parę dni temu bilet do Berlina. A&nbsp;teraz do Budapesztu”*.  
(To tylko przykład; nie wiem czy którekolwiek z&nbsp;ciasteczek jest tu identyfikatorem. Ale każde z&nbsp;długim ciągiem znaków mogłoby nim być).

I tak to się żyje w&nbsp;tym internecie. Kiedy chodzimy po stronach, to za kulisami nasza przeglądarka cały czas otrzymuje, kopiuje, wysyła i&nbsp;kasuje ciasteczka.

A strony coś z&nbsp;nimi robią. Oficjalnie muszą mówić, co takiego. A&nbsp;nam pozostaje wierzyć na słowo.

{% include info.html type="Ciekawostka"
trailer="Zaciekawiły mnie te ciasteczka z&nbsp;FlixBusa, więc trochę o&nbsp;nich poczytałem.
<p>Okazuje się, że <code>AWSALB</code> to dwa połączone skróty:</p>
<ul>
<li><em>Amazon Web Services</em> (oddział Amazona wynajmujący serwery);</li> <li><em>Application Load Balancer</em> (program pozwalający odciążyć strony, gdy mają wielu odwiedzających).</li>
</ul>
<p>Więcej o&nbsp;tych ciasteczkach oraz o&nbsp;ich celu <a href='https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html'>pisze sam Amazon</a>.</p>
<p>Z kolei ciasteczko <code>ab_bucket</code> zapewne mówi, do jakiej grupy testowej trafiliśmy. <em>A/B testing</em> polega na wysyłaniu różnym użytkownikom różnych wersji strony i&nbsp;patrzeniu, co zrobią; <em>bucket</em> (dosł. „wiadro”) to ogólne określenie na grupę, do której coś przydzielono.</p>
<p>Wniosek: nazwy i&nbsp;skróty często sporo nam mówią!</p>
"%}

## Ciemne strony plików cookies

Ciemnych stron będzie dużo więcej, kiedy przejdziemy do ciasteczek od „stron-gości” :wink:  
Ale nawet te zwykłe, wymieniane tylko między nami i&nbsp;stroną A, potrafią wiele o&nbsp;nas zdradzić.

Przede wszystkim ciasteczka **są dla strony ostatecznym identyfikatorem**, pewniejszym niż wszelkie inne informacje. Każdy dostaje własny, unikalny.

Po wczytaniu się w&nbsp;poprzednie wpisy z&nbsp;„Internetowej inwigilacji” ktoś może wpaść na pomysł: 

{:.bigspace}
> Zmienię sobie IP i&nbsp;wejdę na swoje konto na Facebooku! Nie poznają mnie.

Niestety tak to nie działa. **Bez odpowiednich plików cookies nie wejdziemy na swoje konto**.

Gdybyśmy spróbowali np. odwiedzić nasze konto przez nową przeglądarkę, Y, to po prostu pokaże się ekran logowania. Musimy wpisać login i&nbsp;hasło. A&nbsp;po zalogowaniu dostajemy nowe ciasteczka.  
Zaś serwer może sobie zanotować „Aha, czyli użytkownik *bob.adook.725364* oprócz przeglądarki X&nbsp;używa też Y”.

Z jednej strony trudno sobie wyobrazić inne rozwiązanie problemu prywatnych kont. Strona musi skądś wiedzieć, kogo wpuścić na dane konto. Potrzeba jakiegoś identyfikatora.

A efekt uboczny -- że dzięki ciasteczkom wie dokładnie, co na niej robiliśmy? Nie byłoby to problemem przy mniejszych stronach, gdzie i&nbsp;tak po zalogowaniu nie zostawimy wielu informacji.
 
Ale spędzając godziny na stronach gigantów -- jak Facebook, Google czy Amazon -- zostawiamy dużo cennych danych o&nbsp;sobie, przypisanych do naszej tożsamości.

W ten sposób **wielkie firmy stają się _de facto_ odrębnymi królestwami** w&nbsp;szerszym internecie. Nawet gdyby mniejsze firmy profilujące całkiem wyginęły, to giganci pozostaną.  
A ludzie będą krążyć po ich stronach i&nbsp;usypywać z&nbsp;ciasteczek historię wszystkiego, co na nich robili.

## Jak sobie z&nbsp;nimi radzić

Jednym z&nbsp;przypadków, kiedy możemy chcieć unikać ciasteczek od odwiedzanej strony, jest chęć zachowania anonimowości. Żeby nie powiązać czegoś z&nbsp;naszym istniejącym kontem.

Przykład? Chcemy jednorazowo sprawdzić na YouTubie parę filmów, żeby lepiej zrozumieć obcy światopogląd. Ale nie chcemy, żeby YT zapisał to jako nasze zainteresowania i&nbsp;podsuwał nam to częściej.

Inny przykład? Jakąś stronę możemy odwiedzić tylko parę razy, a&nbsp;potem nas nie wpuszcza. Ale jeśli sprawdza to na podstawie plików cookies, to po ich usunięciu zresetujemy sobie licznik.

Przypomnę, że przy stronach wymagających logowania nic nie zdziałamy. **Nie da się ich odwiedzić anonimowo**. Bez ciasteczka nie wejdziemy, a&nbsp;ciasteczko nas identyfikuje. W&nbsp;tym wypadku pozostaje logowanie przy użyciu alternatywnego konta.

Jeśli jednak nasza strona nie wymaga logowania, żeby z&nbsp;niej korzystać -- jak YouTube -- to jest kilka sposobów.

# Tryb incognito

Obecny chyba w&nbsp;każdej przeglądarce.

W Firefoksie włączamy go przez `Ctrl`+`Shift`+`P`.  
W Chromium przez `Ctrl`+`Shift`+`N`.  
W obu tych przeglądarkach -- a&nbsp;także w&nbsp;pozostałych -- powinien być również dostępny poprzez menu w&nbsp;górnym prawym rogu.

Niektórzy znają go jedynie z&nbsp;tego, że nie zapisuje historii (więc jest dobry do przeglądania pewnych stronek na wspólnym rodzinnym komputerze).

Ale oprócz tego ma inną zaletę, cenniejszą dla nas. **Nie korzysta z&nbsp;zapisanych plików cookies**. Tworzy sobie dla nich nową, tymczasową bazę na czas jednej sesji, a&nbsp;potem ją usuwa.

W praktyce oznacza to, że **strony odwiedzane w&nbsp;trybie incognito nie dowiedzą się od nas, że już je odwiedzaliśmy**.  
Mogą próbować to odgadnąć na podstawie innych informacji. Ale nasza przeglądarka nie powie im tego wprost.

{% include info.html type="Ciekawostka"
text="Na urządzeniach mobilnych z&nbsp;Androidem przydać się może przeglądarka *[Firefox Focus](https://www.mozilla.org/en-US/firefox/browsers/mobile/focus/)*. Zachowuje się tak, jakby tryb incognito był przez cały czas aktywny, regularnie usuwa pliki cookies.  
Jest jednak dość niszowa, przez regularne czystki wymaga częstego logowania od nowa i, w&nbsp;przeciwieństwie do głównego mobilnego Firefoksa, nie obsługuje dodatków. Dlatego podaję ją tylko jako ciekawostkę."
%}

# Dodatek do przeglądarki

Pliki cookies profilujące odwiedzających znajdziemy czasem nawet na stronkach, na które nie trzeba się logować. Albo które w&nbsp;ogóle nie zapewniają opcji logowania.

Na takie wypadki warto zainstalować mocnego *ad blockera*, takiego jak [uBlock Origin](https://ublockorigin.com/) (**koniecznie Origin**; jest też sam *uBlock*, ale to nie o&nbsp;niego chodzi!).

Nie powinien przeszkadzać w&nbsp;działaniu strony, bo blokuje tylko wybrane elementy ze swojej bazy rzeczy złośliwych. A&nbsp;w wielu przypadkach pomoże.

uBO jest zresztą do tego stopnia fajnym narzędziem, że poświęciłem mu całe dwa wpisy.  
Najlepiej zacząć od [tego krótszego]({% post_url 2021-10-21-ublock-origin %}){:.internal}, na temat instalacji.

## Podsumowanie

Poznaliśmy ogólną zasadę działania plików cookies -- rzeczy, bez której znany nam internet by zapewne nie działał. A&nbsp;jednocześnie jednego z&nbsp;głównych narzędzi inwigilacji.

W obecnej formie ciężko z&nbsp;nimi cokolwiek zrobić. Możemy co najwyżej pamiętać, że kiedy jesteśmy zalogowani i&nbsp;chodzimy po podstronach czegoś większego (jak *facebook.com*), to możemy zapomnieć o&nbsp;prywatności.

Ale jak to się dzieje, że ten sam Facebook czy Google są w&nbsp;stanie poznać naszą aktywność **również poza swoimi stronami**?

W tym miejscu wkracza fascynujący temat ciasteczek zewnętrznych (*third-party cookies*). To im poświęcę kolejny wpis.

Do zobaczenia! 
