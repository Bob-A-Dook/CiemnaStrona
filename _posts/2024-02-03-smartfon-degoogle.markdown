---
layout: post
title: "Uwalnianie smartfona od Google'a – ustawienia"
subtitle: "Diagnoza: czterokolorak. Trzeba wyciąć!"
description: "Diagnoza: czterokolorak. Trzeba wyciąć!"
date:   2024-02-03 20:00:00 +0100
tags: [Android, Centralizacja, Inwigilacja, Porady]
firmy: [Google, Motorola]
image:
  path: /assets/posts/google/smartfon-degoogle/degoogle-baner.jpg
  width: 1200
  height: 700
  alt: "Kadr z anime Jojo's Bizarre Adventure, pokazujący przestraszoną postać o siwych włosach patrzącą na swoje ramię. Wyrasta z niego mała twarz ze złośliwą miną. Ma te same kolory, co logo firmy Google"
---

Firmę Google bardzo ceniłem w&nbsp;czasach, gdy byli pionierami. Obecnie budzą moją niechęć.

Do ich współczesnych działań zalicza się [forsowanie rozwiązań](/google/2023/07/29/web-environment-integrity){:.internal}, które podzieliłyby otwarty internet na coś w&nbsp;stylu grodzonych osiedli deweloperskich.  
W USA podczas procesów sądowych wypłynęły nowe dowody na ich nadużycia. Monopolizację rynku, nieuczciwą konkurencję, działanie [wbrew własnym użytkownikom](/google/2023/10/05/antymonopol-chrome-reklamy){:.internal}.

Ten wpis nie będzie jednak o&nbsp;tym. Będzie przyziemny, ale praktyczny. **Pokażę, jak osłabić albo nawet usunąć aplikacje Google'a. Przez zwykłą klikaninę, do której nie trzeba żadnej wiedzy technicznej**.

To część pierwsza, dotycząca ogólnych ustawień. Część druga skupi się na wymianie konkretnych aplikacji.  
Zapraszam do lektury!

{:.figure .bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle/degoogle-baner.jpg" alt="Kadr z&nbsp;anime Jojo's Bizarre Adventure, pokazujący przestraszoną postać o&nbsp;siwych włosach i&nbsp;brodzie patrzącą na swoje ramię, z&nbsp;którego wyrasta mała twarz ze złośliwą miną. Ma te same kolory, co logo firmy Google."/>

{:.figcaption}
Sytuacja jest niewesoła, ale bez obaw. Da się wygrać!  
Źródło: anime *Jojo's Bizarre Adventure: Stardust Crusaders*, odcinek 12. Przeróbki moje.

{% include info.html
type="Uwaga"
text="W tym wpisie nie poruszam tematu *rootowania* i&nbsp;alternatywnych systemów.  
Zdaniem niektórych osób tylko takie techniczne zmiany dają 100% wolności od Google'a. Ja nie obiecuję stu procent, ale nadrabiam przystępnością. Jeśli komuś mało, to ma całe [forum *Degoogle*](https://www.reddit.com/r/degoogle/).  
Sprawa nr 2: wszystko sprawdzałem na Motoroli G22 z&nbsp;systemem Android 12. Możliwe, że na innych smartfonach jest ciut inaczej. Ale wiele porad powinno być uniwersalnych."
%}

## Spis treści

* [Pierwsze kroki](#pierwsze-kroki)
* [Podstawy Androida](#podstawy-androida)
  * [Aplikacje są niepewne](#aplikacje-są-niepewne)
  * [System jest pewniejszy](#system-jest-pewniejszy)
  * [Plan działania](#plan-działania)
* [Wyłączniki systemowe](#wyłączniki-systemowe)
  * [Usuwanie ID reklamowego](#usuwanie-id-reklamowego)
  * [Ogólne opcje prywatnościowe](#ogólne-opcje-prywatnościowe)
  * [Personalizacja pstryczków](#personalizacja-pstryczków)
  * [Wyłączenie ciągłego skanowania hotspotów](#wyłączenie-ciągłego-skanowania-hotspotów)
  * [Dla chętnych: pstryczek od czujników](#dla-chętnych-pstryczek-od-czujników)
* [Instalacja zamienników](#instalacja-zamienników)
* [Odbieranie pozwoleń](#odbieranie-pozwoleń)
  * [Pozwolenie na internet?](#pozwolenie-na-internet)
  * [Pozwolenia specjalne](#pozwolenia-specjalne)
* [Usuwanie i&nbsp;wyłączanie](#usuwanie-iwyłączanie)
* [Finałowy boss – Usługi Google Play](#finałowy-boss--usługi-google-play)
  * [Odbieranie Usługom pozwoleń](#odbieranie-usługom-pozwoleń)
  * [Dla chętnych: wyłączenie Usług](#dla-chętnych--wyłączenie-usług)
* [Podsumowanie](#podsumowanie)


{% include info.html
type="Porada"
text="Wpis jest długi, ale jego główne części są raczej niezależne od siebie. Można je sobie odwiedzać na raty.  
Jedynie część o&nbsp;ogólnych ustawieniach prywatnościowych kłóci się z&nbsp;końcem wpisu, o&nbsp;wyłączeniu Usług Google'a (bo zrobienie tego równa się wyłączeniu i&nbsp;ukryciu pomniejszych ustawień)."
%}

## Pierwsze kroki

Nieraz słyszałem, że macki Google'a na smartfonach sięgają głęboko. Ale nie widziałem tego, siedząc w&nbsp;bańce Huaweia. Pozbawionego usług Wielkiego G&nbsp;ze względu na sankcje ze strony USA.

Szerszy świat pokazał mi smartfon G22 od Motoroli. Rzekomo od niej. Ale równie dobrze mogłaby usunąć wzmianki o&nbsp;sobie. Telefon był kompletnie zdominowany przez Google'a i&nbsp;prawie nie miał niezależnych od niego funkcji.

Czterokolorowa literka G&nbsp;była jak złośliwy, wrośnięty w&nbsp;system, trudny do usunięcia guz. Ale gmerałem w&nbsp;ustawieniach i&nbsp;instalowałem apki-zamienniki, aż uzyskałem coś bardziej szanującego prywatność.

W przypadku Motoroli G22 ekran główny całkiem dobitnie pokazuje, kto na tym telefonie rządzi:

{:.figure .bigspace}
<img src="/assets/posts/google/smartfon-degoogle/google-widget-ikony.jpg" alt="Fragment ekranu głównego smartfona. Widać tutaj pole tekstowe z&nbsp;logiem firmy Google, a&nbsp;pod nim 8&nbsp;ikonek, z&nbsp;których większość również ma cztery firmowe kolory: niebieski, żółty, zielony i&nbsp;czerwony." style="max-width:50%"/>

Skąd takie priorytetowe miejsce dla Google'a? Za ich jakość?  
A może stąd, że płacili miliardy za taki przywilej, co wyszło podczas rozprawy antymonopolowej? [Samsungowi zapłacili 8&nbsp;miliardów](https://www.androidauthority.com/google-samsung-play-store-monopoly-payment-3385238/). Innym producentom podobne kwoty.

Druga rzecz: pod paskiem są ikony kilku podstawowych aplikacji. **Wszystkie albo są apkami Google'a, albo są z&nbsp;nim mocno zrośnięte**.  
Również te bez czterech kolorków. Duo, Telefon i&nbsp;Wiadomości. Mimo że dwie ostatnie wydają się czymś domyślnym, podstawą każdego smartfona.  
Najmniej „googlowy” jest tu Aparat. Ale on również ma domyślnie włączoną integrację z&nbsp;Obiektywem Google.

Potem pokażę, jak je zastąpić. A&nbsp;na tę chwilę, w&nbsp;ramach symbolicznego buntu, można się pozbyć wielkiego paska wyszukiwania (tzw. *widżeta*).  
W tym celu trzeba go nacisnąć palcem i&nbsp;przytrzymać. Wyświetli się siatka pomocnicza pozwalająca usuwać elementy. A&nbsp;w górnej części -- ikonka usuwania. Wystarczy przeciągnąć na nią trzymany pasek, żeby pozbyć się go z&nbsp;ekranu.

{:.bigspace}
<img src="/assets/posts/google/smartfon-degoogle/google-usuwanie-widzeta.jpg" alt="Ekran główny smartfona, na którym jaskrawszymi barwami wyróżniono dwa elementy. Jeden z&nbsp;nich to widżet od Google. Drugi to ikona z&nbsp;napisem Usuń w&nbsp;górnej części ekranu. Są połączone jaskrawą strzałką" style="max-width:50%"/>

Pierwszy mały triumf! W&nbsp;podobny sposób można usunąć skróty do aplikacji.  
Oczywiście taka czystka nie da zbyt wiele poza satysfakcją dla oka. 

## Podstawy Androida

Nie lubię pisać instrukcji do bezrozumnego wykonania. Wolę, gdy moje wpisy coś wyjaśniają. Dlatego najpierw będzie fundament, a&nbsp;potem reszta budowli (konkretne porady).

> **Fundament działania Androida** -- system ma swoje warstwy. Te wyższe są zależne od niższych.

To jednocześnie zaleta i&nbsp;wada. Zaleta, bo aplikacje nie mogą ominąć zakazów nałożonych przez użytkowników. Wada, bo kontrola użytkowników nie sięga do głębin systemu. A&nbsp;kontrola Google'a częściowo już tak.  
Tę sytuację można przedstawić jako piramidkę. Użytkownicy mogą się tu poruszać po środkowej warstwie:

{:.bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle/google_apki_piramida.jpg" alt="Piramida złożona z&nbsp;kilku warstw. Najwyższa jest podpisana 'Apki' i&nbsp;obejmuje cztery trapezy tego samego rozmiaru. Na każdym widać czterokolorowe logo innej aplikacji firmy Google. Poniżej mamy warstwę podpisaną 'System Operacyjny'. Znajduje się tam tabliczka podpisana Ad ID, do której prowadzą złotego koloru rurki od aplikacji u&nbsp;góry. Widać również czerwone przełączniki na rurkach. Jeszcze niżej mamy warstwę podpisaną 'Jądro Systemu'. Jest tam tabliczka podpisana GPS, do której również prowadzą rurki z&nbsp;samej góry." />

{:.figcaption}
Schemat to tylko ogólna ilustracja, dokładne zależności raczej są inne.  
Pojęcie jądra systemu również w&nbsp;znaczeniu nieformalnym: jako głębsza i&nbsp;niedostępna warstwa.  
Źródło: rury z&nbsp;[*kodawarimai.com*](https://kodawarimai.com/pipe-clipart-k.html), oficjalne ikony aplikacji. Przeróbki moje.

Jako użytkownicy możemy się poruszać po warstwie `System operacyjny` i&nbsp;korzystać z&nbsp;różnych przełączników -- czasem odpowiadających za pojedyncze aplikacje, a&nbsp;czasem za ogólniejsze funkcje.

Warstwa niższa, którą nazwałem `Jądrem systemu`, jest domyślnie poza naszym zasięgiem. Nie mamy zatem możliwości usuwania niektórych apek albo np. zmiany niektórych ustawień sieci. Ale bez tego też da się przeżyć :wink:

{:.post-meta .bigspace-after}
Istnieją również opcje pomiędzy systemem a&nbsp;jądrem, takie jak tryb programisty, który liznę w jednym miejscu. Albo tryb debugowania (ADB), którego można użyć po podłączeniu smartfona do komputera. Jego z&nbsp;kolei nie będę tu omawiał.

Co w&nbsp;takiej sytuacji mogą zrobić użytkownicy?

### Aplikacje są niepewne

Dla formalności wspomnę o tym, że czasem można zmienić **ustawienia na poziomie konkretnych aplikacji**. Otworzyć sobie menu apki, znaleźć opcje odpowiedzialne za profilowanie, personalizację reklam i&nbsp;tak dalej. Wyłączyć takie funkcje.

Ale to niepewne rozwiązanie. Każda aplikacja może działać po swojemu. Niejasno opisywać opcje. Naciskać na użytkowników, aż zmienią zdanie. A&nbsp;nawet zaryzykować i&nbsp;całkiem olać brak zgody.

Jak pokazały badania sprzed paru lat, [tylko 3,5% aplikacji prawidłowo obsługiwało zgody użytkowników](https://www.usenix.org/system/files/soups2021-kollnig.pdf). Reszta wciągała prywatne informacje jak odkurzacz.  
Wprawdzie dotyczy to aplikacji wszelakich, nie tylko tych od Google'a, ale dobrze ilustruje problem. Zdawanie się na opcje producentów powinno być najniżej na liście priorytetów.

### System jest pewniejszy

Z powyższego względu **proponuję nie polegać na apkach i&nbsp;zmieniać ustawienia na poziomie systemu**. Apki są od niego zależne i&nbsp;nie obejdą takich ustawień. Na tym poziomie osoby korzystające ze smartfonów mają następujące opcje (w&nbsp;kolejności od najsłabszych):

1. Wyłączenie konkretnym apkom możliwości przesyłania danych w&nbsp;tle.
2. Odebranie konkretnym apkom dostępu do elementów smartfona, np. mikrofonu.
3. Odebranie *wszystkim* apkom dostępu do tegoż elementu.
4. Wyłączanie lub usuwanie aplikacji.

Opcje od 1&nbsp;do 3&nbsp;wystarczą na typowe wścibskie aplikacje, takie jak przysłowiowa [apka-latarka](https://tech.slashdot.org/story/19/09/11/2146205/most-android-flashlight-apps-request-an-absurd-number-of-permissions) z&nbsp;Indii kopiująca listę kontaktów. Można jej tego zakazać, a&nbsp;dostęp do kontaktów zostawić jedynie zaufanej, domyślnej apce od dzwonienia.

Tyle że my tu mamy większy problem. **Przeciwnikiem jest Google. I&nbsp;ta „zaufana” domyślna apka należy właśnie do niego**. Nie wystarczy poleganie na rzeczach domyślnych, trzeba je zmienić na *własne domyślne*.

### Plan działania

Biorąc pod uwagę wszystkie powyższe rzeczy, proponuję następujący plan działania:

* powyłączać aplikacjom Google'a wszystko co się da;
* zainstalować aplikacje alternatywne;
* tylko im zostawić potrzebne pozwolenia;
* usunąć lub wyłączyć jak najwięcej apek Google'a.

Poza tym kilka kroków dla osób chętnych:

* odebrać pozwolenia Usługom Play;
* użyć aplikacji-firewalla i&nbsp;zablokować apkom Google'a połączenia z&nbsp;siecią;
* całkowicie usunąć Usługi Play.

W tym wpisie skupię się na destrukcji, czyli wyłączaniu i&nbsp;usuwaniu :smiling_imp: Uwagi na temat instalowania alternatyw będą natomiast we wpisie numer dwa.

## Wyłączniki systemowe

Istnieje kilka pstryczków, które wystarczy nacisnąć raz, żeby odebrać dostęp wszystkim aplikacjom. To od nich zacznę.

### Usuwanie ID reklamowego

Na rozgrzewkę coś łatwego i&nbsp;jednoznacznie wrogiego użytkownikom. Można ciąć śmiało.

Trzeba wejść w&nbsp;`Ustawienia` (np. przez ikonę zębatki na głównym ekranie), potem w&nbsp;zakładkę `Prywatność`. Powinna być tam opcja `Reklamy`.

To [AAID](https://www.eff.org/deeplinks/2022/05/how-disable-ad-id-tracking-ios-and-android-and-why-you-should-do-it-now). **Unikalny identyfikator, przypisany do telefonu do celów reklamowych**.  
Pod pewnymi względami można go uznać za odpowiednik „ciasteczek” (*plików cookies*) w&nbsp;internecie. Dzięki niemu reklamodawcy mogą powiązać czyjeś działania w&nbsp;apce A&nbsp;z&nbsp;działaniami w&nbsp;apce B.

{:.bigspace}
> Użytkowniczka numer 2130910&nbsp;otwierała regularnie aplikację do śledzenia cyklu miesiączkowego, ale przestała. Obecnie często otwiera aplikację Mniam Dla Mam.  
Diagnoza: ciąża. Zalecane działanie: spam reklamami znanych marek.  
Temat reklam: suplementy, ubranka, szkoły rodzenia. [Azbestowa posypka](https://businessinsider.com.pl/biznes/flagowy-produkt-johnson-and-johnson-powodowal-raka-firma-gotowa-wydac-miliardy/8ms1zf9) od J&J.  
Temat opcjonalny: chwilówki (jeśli szacowana zamożność jest niska).

Zneutralizowanie AAID jest superproste. Wystarczy kliknąć opcję `Usuń identyfikator wyświetlania reklam`.

{:.figure .bigspace}
<img src="/assets/posts/google/smartfon-degoogle/ad-id-usuwanie.jpg" alt="Zrzut ekranu pokazujący opcję usuwania identyfikatora reklamowego" width="400px"/>

Po kliknięciu Google nieco się przestraszy i&nbsp;wyświetli ostrzeżenie:

{:.bigspace}
> Wyświetlanie reklam w&nbsp;aplikacjach nadal będzie możliwe, ale reklamy te mogą być mniej trafne lub mniej interesujące

No straszne! Jakoś się przemogłem i&nbsp;potwierdziłem chęć usunięcia. System to uznał... Ale uspokoił, że gdybym chciał, to wystarczy kliknięcie w&nbsp;opcjach, żeby wygenerować nowy identyfikator. Nie skorzystałem.

### Ogólne opcje prywatnościowe

Poza ID reklamowym istnieje parę subtelniejszych metod gromadzenia o&nbsp;nas danych, rozrzuconych po dwóch menu.

Na początek trzeba wejść w&nbsp;`Ustawienia`. Jeśli na telefonie są włączone Usługi Google Play, to powinna być tu zakładka `Google`. Można w&nbsp;nią kliknąć i&nbsp;powyłączać różne pozwolenia.

W tej zakładce w&nbsp;szczególności zachęcam do [wylogowania się z&nbsp;konta Google](https://nano.komputronik.pl/n/jak-wylogowac-sie-z-konta-google/), jeśli ktoś ma jakieś podłączone. To nic nieodwracalnego, więc bez obaw :wink:  
Uprzedzam jednak, że taki choćby Play Store, domyślne źródło aplikacji, wymaga zalogowania. Ewentualne odpięcie warto zrobić *po* zainstalowaniu potrzebnych apek.

Poza tym jest też menu z&nbsp;opcjami prywatnościowymi. Na początek jak wyżej, trzeba odwiedzić `Ustawienia`. Potem wejść w&nbsp;zakładkę `Prywatność`.  
Warto przejrzeć wszystko z&nbsp;tej zakładki i&nbsp;**wybrać najbardziej restrykcyjne ustawienia**. Wyróżnię tu parę przykładów:

* `Historia lokalizacji Google`

  To draństwo szczególnie warto wyłączyć. W&nbsp;innym wypadku będzie na bieżąco zbierało lokalizację osoby używającej telefonu i&nbsp;ją sobie zapisywało na koncie.

* `Autouzupełnianie z Google`

  Jeśli ktoś ma konto Google przypisane do telefonu, to jest to zgoda na korzystanie z&nbsp;danych z&nbsp;tego konta. Polecam wyłączyć. Ale przede wszystkim nie podpinać konta.

* `Powiadomienia na ekranie blokady`

  Na samego Google'a bezużyteczne. On i&nbsp;tak ma zwykle dostęp do treści. Ale pozwoli uniknąć sytuacji, gdy ktoś np. wyśle prywatnego SMS-a, a&nbsp;ktoś niepowołany zobaczy jego treść na ekranie telefonu leżącego na stoliku.

Nie polegałbym za bardzo na tych ogólnych opcjach, bo prawdziwe zbieranie danych jest ukryte głębiej. Ale zawsze to coś na dobry początek.

### Personalizacja pstryczków

Na chwilę można opuścić `Ustawienia` i&nbsp;wrócić do ekranu głównego. Telefony z&nbsp;Androidem posiadają tu fajną funkcję -- szybkie „pstryczki globalne”.

Będąc na ekranie głównym, można przyłożyć palec do górnej krawędzi i&nbsp;przesunąć w&nbsp;dół, ściągając listę kilku opcji. Po kolejnym pociągnięciu wyświetli się lista na cały ekran. Potem można też przesuwać na boki, wyświetlając jej dalszą część.

Z tego menu można szybko włączać lub wyłączać wybrane funkcje. *Wszystkim* aplikacjom. Niezależnie od tego, czy mają indywidualne pozwolenia. **Warto jak najczęściej wyłączać nieużywane rzeczy**, a&nbsp;menu ułożyć tak, żeby najczęściej używane pstryczki mieć u&nbsp;góry.

Problem w&nbsp;tym, że zauważyłem tu istotną różnicę między Huaweiem a&nbsp;Motorolą. Huawei miał na widoku **pstryczek szczególnie ważny, odpowiedzialny za GPS-a**. Motorola nie.  
W żadnej zakładce, nawet tych dalszych. Według [filmiku](https://www.youtube.com/watch?v=MsLaxP7q3NE) ze stronki *HardReset.info*, powinien tam być. Ale u&nbsp;mnie go nie było.

Okazuje się, że trzeba było nacisnąć ikonę (ołówka?) w&nbsp;lewym dolnym rogu. Wtedy pojawiła się lista wszystkich możliwych kafelków. Mogłem je sobie ustawiać i&nbsp;przenieść ten odpowiedzialny za GPS-a (`Lokalizacja`) na samą górę.

{:.bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle/kafelki-ustawienie.jpg" alt="Zrzut ekranu, na którym zaznaczono ikonkę ołówka pozwalającą przestawiać pstryczki szybkiego dostępu. Pod spodem widać ułożenie ośmiu z&nbsp;nich, podpisanych: internet, hotspot, lokalizacja, tryb samolotowy, Bluetooth, wyłącz czujniki, autoobracanie, latarka" width="600px"/>

{:.figcaption}
Opcja pozwalająca przestawić kafelki oraz ułożenie mojego głównego ekranu.  
Później opiszę, jak zdobyć nietypowy kafel `Wyłącz czujniki`.

{% include info.html
type="Drugie dno sprawy"
text="Najpierw myślałem, że głębsze zakopanie pstryczka od GPS-a to przypadek, losowa decyzja. Ale okazuje się, że raczej stoi za tym większa aferka.  
Według zeznań sądowych [Google świadomie nalegał, żeby chować to ustawienie](https://twitter.com/jason_kint/status/1398356262241320961). Bo po pierwszym wprowadzeniu pstryczka, gdy był na wierzchu, ludzie wyłączali dostęp do lokalizacji częściej, niż Google by chciał.  
Dlatego naciskali na producentów. Według dokumentów udało im się namówić LG do zepchnięcia pstryczka na dalszą stronę. Możliwe, że tak samo było z&nbsp;Motorolą."
%}

### Wyłączenie ciągłego skanowania hotspotów

Wiele osób kiedyś w&nbsp;życiu łączyło się przez hotspota. Czy to dla oszczędzenia danych mobilnych, czy to z&nbsp;braku zasięgu. Kliknęli opcję *Wi-Fi*, wyświetlając listę czytelnych nazw hotspotów. Jak *Netia 123456* albo *iPhone (Bolek)*. Połączyli się z&nbsp;którymś z nich i&nbsp;zyskali internet.

Ale znacznie mniej osób wie, że [Google zbiera takie listy hotspotów](https://security.stackexchange.com/a/137425). Na masową skalę. Gromadzą nie tylko te widoczne, czytelne nazwy, ale również odpowiadające im identyfikatory (BSSID). Dzięki temu [mogą ustalić]({% post_url 2023-07-15-sledzenie-lokalizacji %}#wi-fi){:.internal}, na podstawie samej listy hotspotów w&nbsp;sąsiedztwie, w&nbsp;jakim kto jest miejscu.

Jeszcze mniej osób wie, że **to zbieractwo może działać również wtedy, kiedy Wi-Fi jest wyłączone**. Nieświadomie pozwalają się lokalizować i&nbsp;wykonują darmową pracę na rzecz Google'a, pomagając mu mapować świat hotspotów.

Ustawienie ubijające tę funkcję powinno być gdzieś w&nbsp;zakładce `Google` opisanej wyżej. Nie mam pewności, bo się jej pozbyłem.

Ale można też inaczej -- wejść w&nbsp;`Ustawienia`, potem w&nbsp;`Sieć i internet`. Kliknąć `Wi-Fi` (nie pstryczek, tylko na polu). A&nbsp;potem link mówiący o&nbsp;ustawieniach skanowania Wi-Fi.  
Tam będzie to kluczowe ustawienie. Oraz przyznanie się do winy.

<img src="/assets/posts/google/smartfon-degoogle/skanowanie-wifi.jpg" alt="Zrzuty ekranu pokazujące kolejne etapy wyłączania skanowania Wi-Fi. Na pierwzym zaznaczono czerwoną ramką pole podpisane Wi-Fi w&nbsp;opcjach. Na drugim widać link prowadzący do ustawień skanowania. Na ostatnim widać sam przełącznik od skanowania hotspotów oraz zaznaczoną informację o&nbsp;tym, że działa nawet przy wyłączonym samym Wi-Fi." width="600px"/>

### Dla chętnych: pstryczek od czujników

Kolejnym, jeszcze bardziej ukrytym pstryczkiem, jest ten od czujników -- akcelerometru, żyroskopu, magnetometru i&nbsp;tym podobnych. Osobiście nie czuję potrzeby korzystania z&nbsp;nich, więc zwykle chodzę z&nbsp;wyłączonymi.

Z pozoru wydają się drobnostką. Ale mogą wyciągać całkiem subtelne dane -- o&nbsp;tym, jakim krokiem ktoś się porusza, [jakie ruchy wykonuje](https://arxiv.org/pdf/2109.01118.pdf), jakim jeździ środkiem transportu. Czy ma głos męski, czy damski.

Co więcej, **pozwolenie na dostęp do czujników jest nadawane domyślnie**, a&nbsp;użytkownik nie ma jak tego kontrolować na poziomie konkretnych aplikacji.  
Pozostaje pstryczek „globalny”, zakopany głęboko w&nbsp;opcjach. Żeby go zdobyć, trzeba najpierw [uruchomić *Tryb programisty*](https://www.lifewire.com/how-to-enable-developer-mode-on-android-4684044). Brzmi groźnie, ale to naprawdę prosta sprawa!

W tym celu trzeba wejść w&nbsp;`Ustawienia`, potem w&nbsp;zakładkę `O telefonie` i&nbsp;znaleźć na dole kafelek z&nbsp;napisem `Numer kompilacji`. Trzeba w&nbsp;niego **stuknąć siedem razy pod rząd**, po czym wpisać kod odblokowujący telefon, żeby włączyć tryb.

Po włączeniu trybu można wejść w&nbsp;`Ustawienia`, potem w&nbsp;zakładkę `System`. Będzie tam nowa zakładka, `Opcje programisty`.

Tam, w&nbsp;zakładce `Kafelki szybkich ustawień dla programisty`, czeka opcja `Włącz czujniki`.

{% include info.html
type="Uwaga"
text="Ta opcja sama niczego nie wyłącza, tylko *dodaje do ekranu głównego* pstryczek pozwalający to zrobić. Warto też pamiętać, że musi być on *aktywny* (kliknięty), żeby blokada działała. Na odwrót niż przy większości innych ustawień.  
Poza tym przy wyłączonych czujnikach nie będzie działała żadna aplikacja od robienia zdjęć, inne też mogą mieć subtelne błędy."
%}

## Instalacja zamienników

Tę część opiszę dokładniej we wpisie numer dwa. Ale nie mogłem jej tak po prostu pominąć. Choć wycinanie Google'a to frajda, głupio by było zostać bez aplikacji.  
Bo, przypominam, **apki podstawowe, takie jak Telefon, też zwykle należą do Google'a**. Zanim odbierze im się pozwolenia, warto zdobyć zamienniki.

Proponuję zrobić to w&nbsp;kilku prostych krokach:

* Zainstalować [aplikację F-Droid](https://f-droid.org/) (można przez Play Store, można przez przeglądarkę).

  To alternatywne źródło aplikacji. Wszystkie muszą mieć otwarty kod źródłowy i&nbsp;są sprawdzane pod kątem bezpieczeństwa.

* Wewnątrz F-Droida kliknąć lupkę w&nbsp;dolnym rogu i&nbsp;wpisać `prosty` (jeśli jest ustawiony polski język). 

  W&nbsp;ten sposób wyskoczy trochę apek z&nbsp;serii [Simple Mobile Tools](https://simplemobiletools.com/), o&nbsp;pomarańczowych ikonkach. To zamienniki dla podstawowych aplikacji od Google'a -- SMS-y, Telefon, Aparat, przeglądarka plików, galeria, zegar, kalendarz... Cały niezbędnik smartfoniarzy. Warto je zainstalować.

  {:.post-meta .bigspace-after}
  Za pierwszym razem wyświetli się prośba o&nbsp;pozwolenie na instalowanie aplikacji. To naturalne, wymaga tego Android.

* W&nbsp;razie potrzeby zainstalować parę apek spoza serii Simple.

  Sam przykładowo używam jako odtwarzacza multimediów niezawodnego VLC. Jako programu do otwierania PDF-ów (np. pobranych biletów) -- MuPDF Mini. Oba również z F-Droida.

## Odbieranie pozwoleń

System pozwoleń to główny sposób na okiełznanie aplikacji na telefonie. Dlatego w&nbsp;wielu wpisach na blogu doradzam, żeby udzielać ich jak najmniej. Tylko wybranym apkom. Na jak najkrótszy czas.

Najłatwiej i&nbsp;najszybciej **odbierać pozwolenia przez _menedżera uprawnień_**, w&nbsp;którym lista jest ułożona według rodzajów pozwoleń. Żeby go otworzyć, trzeba wejść w&nbsp;`Ustawienia`, potem nacisnąć `Prywatność`, a&nbsp;potem `Menedżer uprawnień`.

{% include info.html
type="Uwaga"
text="Nie wszystkie pozwolenia będzie się dało odebrać przez to menu.  
Niektóre wymagają jakiejś aplikacji zastępczej. Jeśli dobrze pamiętam, trzeba zdobyć inną aplikację od przeglądania plików, żeby dało się odebrać dostęp do nich apce Files by Google.  
Poza tym **do Usług Google Play nie da się sięgnąć przez to menu**, trzeba przez menu aplikacji. O&nbsp;tym pod koniec."
%}

Odbieranie pozwoleń we wszystkich przypadkach wygląda bardzo podobnie. Klika się nazwę pozwolenia, potem nazwę wybranej aplikacji z&nbsp;listy, a&nbsp;na koniec odpowiedni pstryczek, żeby to pozwolenie nadać, ograniczyć lub całkiem odebrać.  
Jeśli ktoś chce zobaczyć, jakie pozwolenia na nowym smartfonie przyznał sobie Google i&nbsp;jakie odebrałem, to można kliknąć poniżej, żeby rozwinąć listę.

<details class='bigspace'>
<summary><strong>Dokładniejsze omówienie pozwoleń</strong></summary>
<ul>
  <li>
    <p>Aktywność fizyczna</p>

    <p>Domyślnie miały to pozwolenie Mapy Google’a oraz apka Cyfrowa Równowaga.<br />
Odebrałem im obu. Osobiście nie prowadzę statystyk swojej aktywności. Ale gdybym chciał, to tutaj <em>szczególnie</em> wolałbym coś z&nbsp;otwartym kodem, działającego bez internetu.</p>
  </li>
  <li>
    <p>Kalendarz</p>

    <p>Pozwolenia miały cztery apki: Google, Gmail, Kalendarz i&nbsp;Android Auto (ten ostatni <a href="https://www.theverge.com/2021/8/20/22633755/google-android-auto-for-phone-screens-shutting-down-android-12-google-assistant-driving-mode">też od Google'a</a>, choć ikona jednokolorowa).<br />
Odebrałem wszystkim. W&nbsp;przypadku samego Google’a system mnie ostrzegł, że bez tych uprawnień podstawowe funkcje mogą działać nieprawidłowo. Zaryzykowałem.</p>
  </li>
  <li>
    <p>Kontakty</p>

    <p>Tutaj dostęp miało pełno apek – Android Auto, Gmail, Google, Kalendarz, Kontakty, Telefon, Wiadomości.<br />
A to niedobrze, bo kontakty siłą rzeczy przypisują ludzi do (zwykle niezmiennych) numerów telefonów, pozwalając mapować znajomości i&nbsp;odkrywać prawdziwą tożsamość. Zostawiłem tylko Telefonowi i&nbsp;komunikatorom.</p>
  </li>
  <li>
    <p>Lokalizacja</p>

    <p>To pozwolenie ma kilka poziomów: brak zgody, dostęp tylko podczas korzystania, stały dostęp.<br />
<strong>Apka Google (wyszukiwarka) domyślnie miała stały dostęp</strong>. Mimo że bardzo się pilnowałem podczas pierwszej konfiguracji telefonu, żeby nie wyrażać żadnych zgód. Oprócz tego dostęp podczas używania miały Android Auto i&nbsp;Chrome.<br />
Odebrałem wszystkim poza aplikacją <em>Mapy.cz</em>, którą omówię w&nbsp;kolejnym wpisie.</p>
  </li>
  <li>
    <p>Mikrofon</p>

    <p>To również pozwolenie wielopoziomowe. Nie wierzę wprawdzie w&nbsp;teorię o&nbsp;ciągłym nagrywaniu, ale też nie widzę powodu, żeby jakiejś apce to dawać.<br />
Dostęp podczas używania miały: Android Auto, Google, Usługi Google Związane z&nbsp;Mową. Odebrałem wszystkim.<br />
Zostawiłem apkom Telefon (żeby móc dzwonić) i&nbsp;Aparat (żeby nagrywać filmy). W&nbsp;obu przypadkach tylko podczas korzystania.</p>
  </li>
  <li>
    <p>SMS</p>

    <p>Dostęp miały Google, Sklep Google Play, Android Auto, Telefon i&nbsp;Wiadomości. Odebrałem wszystkiemu poza (alternatywnymi) Wiadomościami, żeby móc odbierać SMS-y.</p>
  </li>
  <li>
    <p>Telefon</p>

    <p>Możliwość dzwonienia do innych.<br />
Dostęp miały: Google, Android Auto, Sklep Google Play i&nbsp;parę domyślnych apek. Zostawiłem jedynie apce Telefon.</p>
  </li>
  <li>
    <p>Rejestry połączeń</p>

    <p>Czyli historia wykonanych i&nbsp;odebranych połączeń telefonicznych. Nie widzę żadnych powodów, żeby miało tu dostęp cokolwiek poza jedną apką od dzwonienia.<br />
Dostęp miały: Google, Android Auto i&nbsp;Telefon. Zostawiłem tylko Telefonowi.</p>
  </li>
  <li>
    <p>Urządzenia w&nbsp;pobliżu</p>

    <p>Według opisu chodzi chyba o&nbsp;możliwość streamowania dźwięku do głośników, przenoszenia obrazu na ekrany i&nbsp;tak dalej.<br />
Dostęp miały: Google, Android Auto, Aparat, Duo, Google TV, Ustawienia, YouTube Music. Usunąłem wszystkim.</p>
  </li>
  <li>
    <p>Pliki i&nbsp;Multimedia</p>

    <p>Teoretycznie aplikacja mająca to pozwolenie mogłaby brać treść wszystkich plików i&nbsp;wysyłać je właścicielom. Ale nawet gdyby nie robiła czegoś tak inwazyjnego, <a href="/apki/2022/11/16/apki-pliki" class="internal">same nazwy mogłyby jej sporo powiedzieć</a>.</p>

    <p>Dostęp do <em>wszystkich</em> plików miały: Files by Google i&nbsp;Ustawienia. Do samych multimediów: Wiadomości, Aparat, Zdjęcia (od Google’a), Sklep Google Play. Zostawiłem tylko Aparatowi, odtwarzaczowi mediów, komunikatorom.</p>

    <p>…A przynajmniej chciałem. <strong>nie mogłem wyłączyć dostępu apkom Sklep Google Play oraz Files by Google</strong>. Pstryczki były ciemnoszare, wygaszone. Dopiero po zainstalowaniu zastępczego menedżera plików i&nbsp;wyłączeniu apek od Google'a się ich pozbyłem.</p>
  </li>
</ul>
</details>

Jest tu trochę klikaniny, ale uwierzcie, że warto.

### Pozwolenie na internet?

Pstryczki odbierające dostęp do danych to jedno. Równie fajne byłoby zablokowanie *możliwości ich wysyłania w&nbsp;świat*. Takie „pozwolenie na internet” na poziomie aplikacji.

Niestety Android nie daje takiej możliwości i&nbsp;domyślnie udziela go wszystkim.

...Ale mam dobrą wiadomość! Android udostępnia „gniazdko” na specjalną kategorię apek, VPN-y. Są jak lejek, który zbiera wszelki ruch internetowy płynący ze smartfona i&nbsp;może go zmieniać.  
Niektórzy skorzystali z&nbsp;tej możliwości i&nbsp;stworzyli **_firewalle_ -- aplikacje, które pozwalają kontrolować, co ma łączność z&nbsp;siecią**. VPN-ami są bardziej na papierze. Ale mając to uprzywilejowane miejsce, mogą więcej.

Osobiście zainstalowałem apkę [RethinkDNS](https://rethinkdns.com/app) (darmowa, *open source*) i&nbsp;w ten sposób zyskałem upragnione pstryczki od internetu. Napiszę o&nbsp;niej więcej w&nbsp;drugim wpisie.

<img src="/assets/posts/google/smartfon-degoogle/rethink-dns-blokada-google.jpg" alt="Zrzuty ekranu z&nbsp;aplikacji RethinkDNS. Pierwszy pokazuje, że jest ustawiona jako VPN. Na drugim widać, że dwie aplikacje Google'a zostały zablokowane, a&nbsp;ikonki ich łączności z&nbsp;siecią świecą się na czerwono"/>

### Pozwolenia specjalne

Istnieje szereg pozwoleń, których nie znajdzie się wewnątrz *Menedżera uprawnień*. Mają bardzo szeroki zakres dostępu. A&nbsp;Google z&nbsp;domysłu przyznaje swoim apkom wiele z&nbsp;nich. Zdziwieni? :roll_eyes:

Żeby otworzyć to menu, trzeba kliknąć `Ustawienia`, następnie `Aplikacje` i&nbsp;tam, u&nbsp;dołu, wybrać `Specjalny dostęp do aplikacji`. Wyświetli się lista różnych kategorii. Po kliknięciu dowolnej z&nbsp;nich: lista aplikacji, które mogą mieć takie pozwolenie.

Proponuję **powyłączać, co się tylko da**. W&nbsp;szczególności odciąć od tych danych aplikacje Google'a. Poniżej przykłady opcji szczególnie moim zdaniem wrażliwych.

* `Zezwól aplikacji na sterowanie Wi-Fi`

  Dostęp do listy *gorących*{:.corr-del} hotspotów w&nbsp;twojej okolicy. Jak już pisałem, można tego użyć do ustalania lokalizacji. Co gorsza, to pozwolenie daje też możliwość *edycji* tej listy.

* `Dostęp do danych o użyciu`

  Oficjalny opis: „umożliwia aplikacji śledzenie tego, jakich innych aplikacji używasz i&nbsp;jak często, oraz odczytywanie m.in. informacji o&nbsp;operatorze i&nbsp;ustawień językowych”.

* `Aplikacje do zarządzania multimediami`

  Mając to pozwolenie, apka „może bez pytania modyfikować lub usuwać pliki multimedialne utworzone w&nbsp;innych aplikacjach”.

* `Wyświetlanie nad innymi`

  Brzmi niegroźnie? Ale, ze względu na specyfikę Androida: „aplikacja **będzie widzieć, gdzie klikasz**, lub przełączać to, co widzisz na ekranie”.

* `Powiadomienia na urządzeniu i w aplikacjach`

  Daje możliwość czytania *wszystkich* powiadomień, również tych z&nbsp;cudzych aplikacji. W&nbsp;praktyce dotyczy to np. wiadomości z&nbsp;komunikatorów.

* `Zezwól na modyfikowanie ustawień systemowych`

  Opis nie mówi nic konkretnego, więc [doczytałem](https://stackoverflow.com/a/45639500). Ponoć to szczególnie wrażliwe pozwolenie, więc większość apek nie powinna z&nbsp;niego korzystać. W&nbsp;przypadku Google'a korzystał choćby Aparat.  
W praktyce dzięki niemu aplikacje mogą choćby [reaktywować](https://news.ycombinator.com/item?id=31801542) cofnięte pozwolenia. *Zdecydowanie* warto to wyłączyć.

## Usuwanie i&nbsp;wyłączanie

W obu przypadkach to proste. `Ustawienia`, potem `Aplikacje`, potem wyświetlenie listy wszystkich. Klika się je po kolei i&nbsp;wybiera opcję odinstalowania u góry. Albo wyłączenia, bo czasem jest tylko taka opcja.  
Będą się wyświetlały groźne ostrzeżenia, ale bez obaw; apkę wyłączoną można w razie potrzeby włączyć.

{:.post-meta .bigspace-after}
Jedynie Usług Google Play proponuję nie ruszać zbyt pochopnie. Szczegóły za moment.

Ktoś może się zastanowić -- po co usuwać? Jeśli odebrałem aplikacjom pozwolenia, nawet te zaawansowane, a&nbsp;do tego z&nbsp;nich nie korzystam, to co mi mogą zrobić?

Sam też tak myślałem. Ale po kilku tygodniach od odebrania zgód postanowiłem sprawdzić statystyki zużycia danych (`Ustawienia`, `Aplikacje`, potem wybrać sobie jakąś z&nbsp;listy i&nbsp;kliknąć `Dane komórkowe i Wi-Fi`).

Dane są pokazane w&nbsp;podziale na pierwszy plan (podczas korzystania z&nbsp;apki) oraz na te wysłane w&nbsp;tle, po kryjomu. Naprawdę mało co robiłem na telefonie, a&nbsp;apek Google'a nie tykałem. Ale na tym etapie nie miałem jeszcze *firewalla*, więc apki mogły wysyłać dane. I&nbsp;to robiły:

* Apka Filmy Google Play, nieruszana -- kilkaset kilobajtów wysłanych w&nbsp;tle.
* Apka Fit, nieużywana -- 328&nbsp;kB.
* **Gmail -- nieużywany, ponad 15&nbsp;MB w&nbsp;tle**, śladowe ilości na pierwszym planie.
* Kalendarz -- nieużywany, 1&nbsp;MB w&nbsp;tle.
* YouTube Music -- nie tykałem, i&nbsp;tak ponad 3&nbsp;MB w&nbsp;tle.
* **Klawiatura ekranowa GBoard -- ponad 7&nbsp;MB na pierwszym planie** i&nbsp;301 kB w&nbsp;tle.
* Historia lokalizacji Google (niewidoczna domyślnie; trzeba było wybrać opcję wyświetlania aplikacji systemowych) -- ponad 50&nbsp;kB danych w&nbsp;tle. Mimo że od początku miałem wyłączoną.

Wniosek: brak pozwoleń i&nbsp;olewanie aplikacji to za mało. Jak się da, to najlepiej odinstalować. A&nbsp;wielu się nie dało; mogłem je co najwyżej wyłączyć.

Apki, które udało się całkiem odinstalować:

<div class="black-bg mono">
Arkusze, Dokumenty, Prezentacje, Podcasty Google, Portfel Google, Fit, Google One, Wiadomości Google
</div>

Apki, które mogłem jedynie *wyłączyć*:

<div class="black-bg mono">
Chrome, Duo, Dysk, Files by Google, Filmy Google Play, Gboard, Gmail, Kalendarz, Kontakty, Mapy, Asystent, Sklep Google Play, Telefon, Wiadomości, YouTube, YouTube Music, Zdjęcia.
</div>

## Finałowy boss – Usługi Google Play

Pstryknęliśmy wszystko? Według zakładki `Prywatność` żadna apka nie ma dostępu do wrażliwych rzeczy? Super, jest pełna prywatność! :smile:

...Tyle że nie. Mimo wszystkich wykonanych działań spokój jest pozorny. **Istnieje jedna rzecz, która nadal ma dostęp [do wielu pozwoleń](https://android.stackexchange.com/questions/196248/google-play-services-required-permissions). Ukryta w&nbsp;osobnym, głębiej zakopanym menu**.

To Usługi Google Play (_Play Services_). Finałowy boss tego wpisu, czyhający w&nbsp;głębinach smartfona.

{:.figure .bigspace-before}
<img src="/assets/posts/google/smartfon-degoogle/google-play-services.jpg" alt="Kadr z&nbsp;anime Jojo's Bizarre Adventure, pokazujący brzydką twarz z&nbsp;szyderczą miną, wynurzającą się ze smoły i&nbsp;pokazującą język. Ma cztery kolory, takie jak logo Google (czerwony, zielony, żółty, niebieski), a&nbsp;na jej czoło nałożono logo Usług Google Play."/>

{:.figcaption}
Źródło: ponownie *JJBA: Stardust Crusaders*, odcinek 12.

{% include info.html
type="Uwaga"
text="Warto podkreślić, że Usługi Google Play to coś innego niż (Sklep) Google Play. Ten drugi jest aplikacją. Ze specjalnymi pozwoleniami (jak instalowanie, skanowanie i&nbsp;usuwanie innych aplikacji)... ale nadal aplikacją, którą da się uruchomić.  
Z kolei Usługi to [pakiet różnych rzeczy](https://android.stackexchange.com/tags/google-play-services/info), rozszerzających podstawowe funkcje Androida. Przeznaczony dla *innych aplikacji*, a&nbsp;nie ludzi."
%}

Usługi odpowiadają za parę bajerów, jak automatyczne wpisywanie kodów jednorazowych otrzymanych przez SMS-y. Albo za wyświetlanie Map Google wewnątrz innych aplikacji.

Ceną za te wszystkie udogodnienia jest wpuszczanie Google'a jako pośrednika między siebie a&nbsp;aplikacje. Nie tylko te z&nbsp;jego stajni, ale również cudze (jak Uber, który korzysta z&nbsp;Map Google'a).

Dobra strona: najtrudniejsze jest samo odkrycie, że takie coś istnieje i&nbsp;zbiera dane. Ale samo odbieranie pozwoleń jest całkiem łatwe. Gorąco zachęcam, żeby to zrobić.

### Odbieranie Usługom pozwoleń

Do Usług nie da się dobrać przez *Menedżera Uprawnień*, trzeba inaczej.  
Najpierw wchodzimy w&nbsp;Ustawienia, potem `Aplikacje`, potem `Wyświetl wszystkie aplikacje`. Trzeba znaleźć na długiej liście `Usługi Google Play` i&nbsp;kliknąć `Uprawnienia`. Po czym odhaczyć co się da.

{:.post-meta .bigspace-after}
Nie miałem możliwości wycofania pozwolenia `Aktywność fizyczna`, było na szaro. Ale i&nbsp;tak nie łączyłem z&nbsp;telefonem żadnych zegarków czy opasek, więc mnie to nie dotknęło.

Jeśli Google jakkolwiek boi się konsekwencji, to powinien uszanować brak pozwoleń.  
Ale skoro już zaszliśmy tak daleko, to proponuję wypróbować opcję nuklearną. Wyłączyć Usługi Google Play całkowicie.

### Dla chętnych -- wyłączenie Usług

**Nie jest to opcja dla każdego i&nbsp;mocno zależy od tego, z&nbsp;jakich apek się korzysta**. Jeśli coś potrzebnego do życia wymaga Usług, to nie ma rady, jak tylko je tolerować.  
...Ale żeby sprawdzić, czy jest aż tak źle, warto je na próbę wyłączyć.

Samo wyłączenie jest banalnie proste. Będąc w&nbsp;tym samym menu, o&nbsp;którym wspomniałem wyżej, wystarczy kliknąć opcję `Wyłącz` u&nbsp;góry. Olać ostrzeżenia.

Kiedy to zrobimy, zaleje nas fala alarmujących komunikatów. Różne inne aplikacje [zaczną się buntować](https://news.ycombinator.com/item?id=28973527). Wyświetlać powiadomienia, że bez Usług nie mogą działać prawidłowo. **Nawet Zegar zaczął się skarżyć**.

Kłamstwa i&nbsp;histeria, ale powtarzające się powiadomienia mogą wkurzać. Dlatego je również warto wyłączyć!

W tym celu znowu trzeba wejść w&nbsp;menu `Aplikacje` i&nbsp;wyświetlić pełną listę. Ale tym razem dodatkowo kliknąć kropki w&nbsp;górnym rogu i&nbsp;włączyć opcję wyświetlenia aplikacji systemowych.

Następnie można odczytać z&nbsp;powiadomień nazwy aplikacji, które się skarżą. Po czym klikać każdą z&nbsp;nich na liście, wybierać `Powiadomienia` i&nbsp;je wyłączać. Z&nbsp;czasem aplikacje przestaną lamentować, a&nbsp;na smartfonie zapanuje spokój.

{% include info.html
type="Porada"
text="Jedną z aplikacji [narzekających](https://github.com/signalapp/Signal-Android/issues/12858) na brak Usług był o&nbsp;dziwo komunikator prywatnościowy Signal. Którego powiadomień akurat wolałem nie wyciszać.  
Na szczęście sprawa się łatwo rozwiązała. Signal jojczał, bo został zainstalowany, gdy jeszcze miałem Usługi. Ale kiedy go usunąłem i&nbsp;zainstalowałem ponownie, to wszystko się naprawiło. Podobnie może być w przypadku innych aplikacji."
%}

Dopiero po wyłączeniu Usług osiągnąłem błogi spokój bliski temu na Huaweiu. Ta nuklearna opcja nie jest dla każdego i&nbsp;na pewno niektóre aplikacje przestaną działać (choćby Mapa Turystyczna, jeśli dobrze pamiętam; również w&nbsp;Uberze nie działa miniaturka mapy, ale reszta śmiga).

Na tym etapie można sobie poklikać po aplikacjach i&nbsp;zobaczyć, czy wszystko działa. Jeśli nie, to ponownie aktywować Usługi. A&nbsp;jeśli tak, to wznieść toast za wolność.

## Podsumowanie

Udało się, czterokolorak usunięty!

...Ale czy na długo? Jak [wspominają niektórzy](https://android.stackexchange.com/q/227035), zdarzała się remisja. Wyłączone Usługi Google'a potrafiły samoistnie się reaktywować.

Usługi są czymś na poziomie głębszego systemu, więc tak, mają *techniczną* możliwość wrócić. Przywrócić inne wyłączone apki. Nadać im oraz sobie wszystkie cofnięte pozwolenia. Obejść firewalla i&nbsp;wysłać dane firmie Google.

Nie kłócę się z tym. Ale uważam, że możliwość techniczna nie oznacza, że coś się stanie. Gdyby Google tak ostentacyjnie fikał, to ktoś by to zauważył. A&nbsp;wierzę, że jednak mają w&nbsp;sobie jakąś ostrożność.  
Zwłaszcza teraz, kiedy są pod lupą antymonopolistów.

Bez rootowania -- wymiany głębszych warstw systemu -- można mieć mocne przekonanie, ale nie ma gwarancji. Może być jak w&nbsp;schematycznych horrorach z&nbsp;lat 80., gdy ostatni kadr filmu pokazuje, że pokonane zło jeszcze dycha.

Ale póki co życzę nam wszystkim, żeby ten horror nie miał sequela!
 
