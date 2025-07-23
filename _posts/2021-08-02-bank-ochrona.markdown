---
layout: post
title: "Ochrona jak w banku"
subtitle: "Kto i jak pilnuje naszych skarbów."
description: "Jak pomóc bankowi pilnować naszych skarbów."
date:   2021-08-02 14:50:00 +0100
tags: [Bankowość, Centralizacja, Podstawy, Porady]
firmy: [Amazon, Google]
image: 
   path: /assets/posts/bank-ochrona/bank-sejf.jpg
   width: 1200
   height: 700

image-width: 1200
image-height: 749
---

{:.post-meta .bigspace}
**Uwaga:** Ten wpis, oprócz spraw prywatnościowych, ociera się o&nbsp;cyberbezpieczeństwo. A&nbsp;to nie moja działka. Traktujcie go jak zestaw luźnych obserwacji, a&nbsp;nie porady.  
Poza tym nie biorę odpowiedzialności za nic, co zrobią potencjalni czytelnicy.  
Do tego w&nbsp;trakcie tworzenia tego wpisu nie ucierpiały żadne zwierzęta.

OK! Tyłek mam chroniony, mogę przejść do rzeczy.

Wycieki danych to niefajna sprawa, ale pewne ich konsekwencje bolą bardziej niż inne. Na przykład utrata pieczołowicie odkładanej kasy.  
Czy możemy ufać swojemu bankowi, że dobrze ją ochroni?

W tym wpisie zebrałem swoje obserwacje i&nbsp;przemyślenia na temat różnych zabezpieczeń, jakie stosują banki (tu na przykładzie PKO BP). Opisuję, co mogę zrobić ze swojej strony, żeby tego nie popsuć.

A na deser będą oczywiście ciemne strony -- przypadki, gdy to banki zawiodły ludzi oraz wątek umacniania monopolistów :wink:

Zanim zaczniemy, jedna uwaga -- oprócz tego, co omawiam, mamy również trochę zabezpieczeń za kulisami (możliwość *chargebacku*, wykrywanie podejrzanych transakcji przez bank, ochronę prawną w&nbsp;przepisach itp.).  
To całkiem pomocne możliwości. Ale w&nbsp;tym wpisie dam im niższy priorytet.  
Zakładam, że **liczenie na to, że jakaś instytucja nas ocali, to ostatnia linia obrony**. Pomóżmy sobie sami.

## Wprowadzenie

Na warsztat wziąłem PKO BP, jednego z&nbsp;większych graczy.

To duży zwierz i&nbsp;oferują pełen wachlarz różnych rzeczy. Kartę, aplikację, przelewy przez internet (przez stronę [iPKO](https://www.ipko.pl/)).

{:.figure .bigspace}
<img src="/assets/posts/bank-ochrona/bank-sejf.jpg" alt="Obrazek pokazujący ogromne, otwarte drzwi do bankowego skarbca, a&nbsp;także zamkniętą kratę stojącą za nimi. Na wrota i&nbsp;na kratę nałożono zrzuty ekranu z&nbsp;różnymi prośbami o&nbsp;weryfikację ze strony banku."/>

**Aplikacji mobilnej nie omówię**, bo z&nbsp;niej nie korzystam. Dlaczego? Zastanowiłem się kiedyś, czy bym chciał, i&nbsp;uznałem że nie.

Pozostaje kilka innych rzeczy, dość różniących się pod względem zagrożenia.

* Bankowość elektroniczna.

  Można przelać pieniądze z&nbsp;jednego konta na inne. A&nbsp;także wyłączyć limity na karcie.  
  Złodziej musiałby jednak znać login i&nbsp;hasło do konta oraz mieć *dodatkowy kod potwierdzający* (o&nbsp;tym później).

* Karta płatnicza.

  Pozwala płacić zbliżeniowo, wypłacać pieniądze z&nbsp;bankomatu, zawiera dane do płatności internetowych.  
  Płatność zbliżeniowa i&nbsp;wypłata z&nbsp;bankomatu wymagają PIN-u.  
  Przy płatności internetowej czasem trzeba przejść przez dodatkowe zabezpieczenia. Ale w&nbsp;najprostszym przypadku wystarczą same dane z&nbsp;przodu karty.

* Fizyczna wizyta w&nbsp;oddziale banku.

  Mając dowód osobisty, można przyjść do banku i&nbsp;wypłacić sobie pieniądze z&nbsp;konta.  
  A&nbsp;także zmienić wszelkie limity na pozostałe transakcje.

Zanim przejdę do szczegółów, jedna uniwersalna porada -- **można ulokować większość pieniędzy w&nbsp;innym miejscu niż konto/rachunek na wydatki bieżące**.

Jednocześnie najlepiej nie mieć przy sobie niczego, co pozwoliłoby złodziejom sięgnąć do tego większego źródła. Loginy i&nbsp;hasła schowane w&nbsp;bezpiecznym miejscu. Karta płatnicza przypisana tylko do mniejszego konta. Będziemy w&nbsp;dużej mierze chronieni.

Nawet gdyby ktoś nas wykiwał, to w&nbsp;najgorszym razie stracimy tylko sumę z&nbsp;mniejszego konta. Nasze główne skarby pozostaną poza zasięgiem oszustów.

Ale i&nbsp;tak lepiej nie stracić niczego niż cokolwiek! Dlatego teraz przejdę do sposobów chronienia swojego częściej używanego konta.

## Bankowość elektroniczna

Tej poświęcę nieco więcej uwagi, bo jest tutaj parę ciekawych rzeczy do pokazania.

Jeśli oprócz moich przemyśleń chcecie oficjalne źródło, to zerknijcie np. na [porady banku na temat bezpieczeństwa](https://www.pkobp.pl/klienci-indywidualni/bankowosc-elektroniczna/bezpieczenstwo-bankowosci-elektronicznej/).

A teraz wyobraźmy sobie, że założyliśmy konto. Podczas pierwszego logowania w&nbsp;PKO BP ustala się kilka rzeczy:

* login i&nbsp;hasło
* obrazek bezpieczeństwa
* dodatkową formę weryfikacji  
  (mogą to być kody wysyłane SMS-em albo przez aplikację).

# Omówienie zabezpieczeń

A teraz odwiedzamy stronę banku któryś raz z&nbsp;rzędu. Wita nas tradycyjne pytanie o&nbsp;login.

{:.figure}
<img class="bigspace" width="400px" src="/assets/posts/bank-ochrona/logowanie-poczatek.jpg" alt="Zrzut ekranu pokazujący formularz logowania do banku. Widać tutaj jedno pole, z&nbsp;miejscem na login."/>

Ale to nie wszystko! Po wpisaniu loginu pojawia się dodatkowo pole pytające o&nbsp;hasło. Obok pojawia się **obrazek bezpieczeństwa**, który ustawialiśmy sami przy pierwszym logowaniu. Czemu on służy?

{:.figure}
<img width="400px" src="/assets/posts/bank-ochrona/logowanie-obrazek-bezpieczenstwa.jpg" alt="Zrzut ekranu pokazujący pole z&nbsp;napisem 'Wpisz hasło'. Po prawej stronie widać wyświetlony nam obrazek (tutaj zamieniony na logo Ciemnej Strony), a&nbsp;pod nim aktualną datę."/>

{:.figcaption}
Obrazek bezpieczeństwa podczas logowania na konto w&nbsp;PKO BP. Zmieniony przeze mnie.

Obstawiam, że to zabezpieczenie przeciw *phishingowi* (wyłudzeniom z&nbsp;użyciem fałszywej strony).

Ktoś może łatwo stworzyć stronę identyczną z&nbsp;wyglądu jak oryginalna bankowa. Wtedy, gdyby pola na login i&nbsp;hasło były od razu w&nbsp;pierwszym oknie, ofiara mogłaby je po prostu wpisać (a&nbsp;one trafiłyby do złodziei).

Dzięki podzieleniu interakcji na etapy (login → sprawdzenie czy pojawia się wcześniej ustawiany obrazek → hasło), bank nas nieco „uczy” czujności. **Sami go weryfikujemy między podaniem loginu a&nbsp;hasła**.  
Tylko nasz prawdziwy bank wie, jaki mamy obrazek. Zatem, gdyby ten się nie wyświetlał albo nie zgadzał, to znaczy że coś jest nie tak. 

Oczywiście to wymaga też naszej czujności. Jeśli dostaniemy fałszywą stronę i&nbsp;nie zwrócimy uwagi na to, że brakuje obrazka albo wyświetla coś innego, to nas okradną.

{% include info.html type="Ciekawostka" text="Zresztą taka metoda na podstawioną stronę i&nbsp;liczenie na naszą nieuwagę to podobno [jedno z&nbsp;najczęstszych oszustw](https://niebezpiecznik.pl/post/uwaga-na-smsy-od-w-sprawie-przesylek/).  
Niedawno było głośno o&nbsp;szwindlu polegającym na fałszywym SMS-ie od OLX, informującym o&nbsp;konieczności dopłacenia za paczkę. W&nbsp;takich wiadomościach były właśnie linki do podrobionych stron.  
Kiedy ofiary zaczynały tam wpisywać dane, to te na żywo leciały do oszustów. A&nbsp;ci po swojej stronie wpisywali je na stronie prawdziwego banku -- tyle że wykonując nie jeden przelew, a&nbsp;pełne przejęcie konta." %}

Jest jeszcze jedno zabezpieczenie! Jeśli używamy innego komputera albo przeglądarki niż zwykle, to bank może nas poprosić o&nbsp;*dodatkowy kod potwierdzający* (który otrzymamy w&nbsp;takiej formie, jaką wcześniej wybraliśmy -- np. jako SMS-a albo kod wyświetlany w&nbsp;aplikacji).

{:.figure}
<img class="bigspace" width="400px" src="/assets/posts/bank-ochrona/logowanie-zmiana-zaufanego.jpg" alt="Zrzut ekranu ze strony PKO BP pokazujące pole proszące o wpisanie z SMS-a kodu dodającego urządzenie do zaufanych."/>

Jak to robi? Trzyma w&nbsp;swojej bazie informacje o&nbsp;tym, jaki identyfikator urządzenia (*user agent*) mieliśmy, gdy go wcześniej odwiedzaliśmy. Jeśli tym razem przyjdziemy z&nbsp;innym, nieznanym, to prosi o&nbsp;weryfikację.

Potem przepuści nas na stronę główną naszego konta. Niezależnie od tego, czy wcześniej wymagał weryfikacji, na pewno będzie jej wymagał teraz, gdybyśmy próbowali:

* podejrzeć większość danych (PESEL, nr dowodu, nr telefonu, adres mailowy);
* podwyższyć limity na karcie;
* dokonać przelewu;
* zobaczyć transakcje starsze niż 3&nbsp;miesiące;
* ...albo zrobić szereg innych rzeczy, których robić nie próbowałem.

I wyśle nam odpowiednie SMS-y. Każdy z nich zawiera na końcu kod, który musimy wpisać w pole.

<img class="bigspace" width="400px" src="/assets/posts/bank-ochrona/smsy-zmiany.jpg" alt="Dwa SMS-y z kodami pozwalającymi zrobić różne rzeczy na stronie banku. Większość danych zakryto."/>

Słowem: prawie wszystko chronione dodatkowym kodem.  
Właściwie jedyne informacje, jakie są tam niezasłonięte, to **nasze imię i&nbsp;nazwisko, podany adres kontaktowy, stan konta i&nbsp;po kilka cyfr z&nbsp;pozostałych numerów**.

Oczywiście złoczyńcy, którzy w&nbsp;ten czy inny sposób zobaczą stronę naszego konta, nadal by mogli coś zrobić z&nbsp;tymi informacjami. W&nbsp;najprostszym przypadku: ocenić po stanie konta, czy warto odwiedzić nasz adres. A&nbsp;potem to zrobić. Z&nbsp;bejsbolami.

W wariancie mniej barbarzyńskim: zadzwonić do nas, podając się za pracowników banku. Podać kilka z&nbsp;tych widocznych cyfr (na przykład fragment numeru PESEL), żeby brzmieć wiarygodnie -- w&nbsp;końcu mało kto się spodziewa, że znają je z&nbsp;konta. Po uśpieniu czujności mogą spróbować coś wyłudzić.

Kolejne zabezpieczenie to licznik czasu. **Jeśli przez 5 minut jesteśmy na jednej stronie, to nas wyloguje**.

{:.figure}
<img class="bigspace" width="400px" src="/assets/posts/bank-ochrona/limit-czasu.jpg" alt="Zrzut ekranu pokazujący białe pole z&nbsp;ikoną zegarka i&nbsp;napisem, że pozostały 23 sekundy do wylogowania."/>

Ta bardziej oczywista sytuacja, przed którą ma to chronić, to pewnie korzystanie z&nbsp;banku na publicznym komputerze i&nbsp;zostawienie się na zalogowanym koncie.

Za kulisami zapewne jest więcej tych zabezpieczeń -- coś związanego z&nbsp;czyszczeniem plików cookies, coś z&nbsp;pamięcią podręczną (np. czy w&nbsp;jakiś sposób pilnują, żeby złodziej nie odczytał z&nbsp;niej naszego obrazka bezpieczeństwa, żeby później go użyć?). Ale ten temat dopiero zgłębiam, więc nie będę się wypowiadał.

# Jak można się chronić

Podsumowując: przy bankowości internetowej najprostsza droga do zaszkodzenia nam wymagałaby loginu, hasła i&nbsp;dostępu do dodatkowego kodu potwierdzającego (czyli np. posiadania naszego telefonu).  
Moim zdaniem powinny pomóc dość oczywiste rzeczy:

* Odwiedzać stronę tylko przez własne zaufane urządzenie i&nbsp;najlepiej przez własną sieć / hotspota (wiem że to drugie nie zawsze jest realne; ale niech chociaż urządzenie będzie własne).
* Nigdzie nie zapisywać danych do logowania; trzymać je tylko w&nbsp;głowie albo w&nbsp;menedżerze haseł.
* Pamiętać prawdziwy adres strony banku i&nbsp;patrzeć, czy ten w&nbsp;przeglądarce się zgadza.
* Pamiętać, jak powinien wyglądać proces logowania i&nbsp;obrazek bezpieczeństwa.

Wszystko to takie oczywiste porady, zresztą widziałem je w&nbsp;poważniejszych źródłach. Mam też kilka bardziej abstrakcyjnych.

Jeśli używamy **bardziej niszowego systemu albo przeglądarki** (np. Linuxa + Opery) i&nbsp;ustawimy takie urządzenie jako zaufane, to być może utrudnimy oszustom „trafienie”.

Dlaczego? Wyobraźmy sobie, że zdobyli nasz login i&nbsp;hasło, bo zapisaliśmy je gdzieś na kartce (karny jeżyk dla nas!). Ale nie wiedzą, jaki mamy komputer, więc muszą próbować na swoim.

Jeśli ich system i&nbsp;przeglądarka okażą się inne niż nasze, to ich zablokuje dodatkowa weryfikacja.  
Tym niemniej, jeśli zarówno oni, jak i&nbsp;my korzystamy z&nbsp;najpowszechniejszego zestawu `Windows 10 + nowy Chrome`, to mają większą szansę na trafienie.

Kolejna sprawa, też z&nbsp;tym związana -- na stronie banku można czasem **czyścić listę urządzeń zaufanych**.  
Trzymajmy tam tylko te, których faktycznie używamy. Jeśli często zmieniamy przeglądarkę (np. aktualizując) i&nbsp;stale dodajemy nową do zaufanych, to oszust „strzelający” z&nbsp;urządzeniem będzie miał większe szanse trafienia.

Poza tym fajnie by było **coś zrobić z&nbsp;tym adresem domu widocznym na stronie**... W&nbsp;żadnym razie nie namawiam do podania fejka (bo na ten adres to jednak wysyłają karty; poza tym jeszcze [kogoś niewinnego by się zasypało spamem](https://forum.pclab.pl/topic/1275454-jak-wymusi%C4%87-nie-przesy%C5%82anie-list%C3%B3w-przez-bank/)).

Ale gdyby ktoś przypadkiem miał wolny prawdziwy adres do dyspozycji, na przykład domek letni na skraju Polski... :wink:

## Karta płatnicza

Jeden drobny przedmiot dający wiele możliwości.

Wyobraźmy sobie, że ją straciliśmy. Na przykład zapomnieliśmy wyjąć z&nbsp;automatu biletowego, zabrać z&nbsp;lady przy kasie, zgubiliśmy cały portfel. Oczywiście kradzież też wchodzi w&nbsp;grę.  
Adwersarze, którzy wejdą w&nbsp;jej posiadanie, mogą próbować nam dokuczyć na kilka sposobów.

# Płatności zbliżeniowe bez PIN-u

Są najprostsze, bo wystarczy mieć kartę i&nbsp;przykładać ją do czytnika. Zero zabezpieczeń.

Ale nie są też szczególnie groźne. Na jedno dotknięcie wykona się płatność zwykle tylko do kwoty 50&nbsp;zł (w&nbsp;czasie pandemii ten limit zwiększono do 100&nbsp;zł).

Można spekulować: a&nbsp;gdyby oszuści zdobyli naszą kartę, naszykowali sobie dziesiątki terminali i&nbsp;po kolei ją do nich przykładali, trzymając się poniżej progu PIN-u?

Na szczęście raczej nie ma takiego zagrożenia. 

Po pierwsze, pytanie o&nbsp;PIN pojawia się nie tylko przy transakacjach przekraczających wspomniany próg, ale również [ogólnie przy co piątej](https://www.elavon.pl/content/dam/elavon/pl-pl/documents/customer-center/news/PSD2PractialImpactGuideFacetoFacePolishFINAL.pdf) (wyszukać `Transakcje zbliżeniowe`), nawet drobniejszej transakcji.

Po drugie, zdobycie własnego terminala to nie taka prosta sprawa. Trzeba założyć firmę i&nbsp;zawrzeć na nią umowy z&nbsp;organizacjami płatniczymi.  
Poza tym kasa nie trafi do właściciela terminala od razu po sczytaniu naszej karty. Przez chwilę tkwi w&nbsp;zawieszeniu. Jeśli pojawi się podejrzenie oszustwa, to jej przekazanie można zablokować.

Wniosek: zakupy zbliżeniowe na nasz koszt to raczej niewielkie zagrożenie.  
Ktoś mógłby co najwyżej kupować sobie parę flaszek na dzień. Stopniowo „wykrwawiając” nas z&nbsp;kasy, dopóki nie zablokujemy karty.

Dlatego **warto od razu ją zablokować**, na przykład przez stronę banku. Żeby złodziejaszek nie zdobył nawet flaszki pocieszenia.

# Płatności i&nbsp;wypłaty z&nbsp;PIN&#8209;em

Mając kartę oraz PIN, przeciwnik zyskuje nowe możliwości. Może wydawać większe kwoty podczas płatności zbliżeniowej albo wypłacić pieniądze z&nbsp;bankomatu.

Żeby się przed tym chronić, powinniśmy przede wszystkim **nie trzymać PIN-u w&nbsp;tym samym miejscu co karty**.  
Na przykład na kartce w&nbsp;tym samym portfelu. Nie. Trzymajmy go tylko w&nbsp;głowie.

Poza tym napastnik ma trzy próby, żeby podać PIN, zanim karta zostanie zablokowana. W&nbsp;akcie desperacji może spróbować strzelać w&nbsp;coś częstego. Utrudnijmy mu trafienie.

Dlatego nie ustawiałbym jako PIN-u najłatwiejszych kombinacji: `1234` albo czterech identycznych cyfr (jak `1111`).

Jeśli jednak zdobędzie PIN -- w&nbsp;ten czy inny sposób -- kolejną linią obrony (zarówno dla płatności zbliżeniowych, jak i&nbsp;dla bankomatów) są limity ustalone dla naszej karty.

Moim zdaniem warto ustawić jak najniższe, dopasowane do naszych przeciętnych wydatków. Dodatkową zaletą takiego zaciskania pasa będzie fakt, że może to zapobiec nieprzemyślanym zakupom :wink:  
A gdy trzeba sypnąć większym groszem, to można po prostu chwilowo zwiększyć limit przez stronę banku. Albo płacić w&nbsp;gotówce noszonej na czarną godzinę.

W przypadku PKO BP limity można zmienić, logując się na konto iPKO. I&nbsp;wybierając `Moje produkty > Karta > (wybrać kartę) > Szczegóły i zarządzanie kartą > zmień limity`.  
Każdą zmianę trzeba następnie potwierdzić w&nbsp;wybrany przez nas sposób (SMS / przez apkę / inny).

# Płatności internetowe

Oprócz chipa, który pomaga przy bankomatach i&nbsp;płatnościach zbliżeniowych, na karcie mamy też kilka wytłoczonych lub zapisanych liczb:

* numer karty,
* imię i&nbsp;nazwisko właściciela,
* datę ważności,
* numer CVV2 (na odwrocie karty).

{:.figure}
<img width="400px" src="/assets/posts/bank-ochrona/karta-przyklad.jpg" alt="Zdjęcie przykładowej karty płatniczej ze strony PKO, z&nbsp;fałszywymi danymi."/>

{:.figcaption}
Zdjęcie karty to przykład ze strony PKO, z&nbsp;fałszywymi danymi; ale i&nbsp;tak zakryłem.

Dzięki tym danym posiadacz karty może kupować różne rzeczy przez internet.

Czasem stykałem się oprócz tego z&nbsp;zabezpieczeniem zwanym **_[3DSecure](https://www.pkobp.pl/klienci-indywidualni/bankowosc-elektroniczna/usluga-3d-secure/)_**.  
Polega ono na tym, że po wpisaniu danych z&nbsp;karty trzeba jeszcze potwierdzić transakcję przez swój bank.  
Cały proces jest dokładnie taki sam, jak przy robieniu przelewu ze swojego konta (tyle że danych odbiorcy nie wpisujemy sami; są już uzupełnione odpowiednio do zakupu).

Niestety nie zawsze jest tak fajnie. Czasem, co odkryłem ku swojemu zdziwieniu, **do kupienia czegoś przez internet mogą wystarczyć dane z&nbsp;przodu karty**. 

Po pierwsze, wspomniane *3DSecure* nie jest wymagane. Co już wcześniej zauważyłem podczas kupowania biletów na RyanAira i&nbsp;WizzAira (jedni wymagali, drudzy nie).  
Bardziej zaskoczyło mnie to, że [numer z&nbsp;odwrotu również nie jest wymagany](https://www.quora.com/How-is-that-possible-that-some-websites-like-booking-com-can-charge-my-debit-card-without-knowing-my-CVV-code-Isnt-that-supposed-to-be-necessary/answer/Rob-Scriven).

Okazuje się, że obie rzeczy są dobrowolne. Tyle że, nie wdrażając *3DSecure* i&nbsp;kodu *CVV2*, firmy rzekomo [biorą na siebie większą odpowiedzialność](https://securionpay.com/blog/3d-secure/) i&nbsp;w przypadku wniesienia reklamacji mamy dużą szansę odzyskania pieniędzy. Większość z&nbsp;nich woli się tak nie narażać i&nbsp;wprowadza zabezpieczenia.  
Ale **taki Amazon już nie**. Z&nbsp;jakiegoś powodu woli brać ewentualne straty na klatę, byle zakupy szły szybciej.

Z jednej strony można to wykorzystać. Gdyby ktoś nieuczciwy odczytał przód naszej karty i&nbsp;coś kupił przez Amazon na nasz koszt, to powinniśmy mieć mocne argumenty w&nbsp;sprawie o&nbsp;odzyskanie kaski.  
Z drugiej: musimy najpierw się zorientować, że nas okradziono. A&nbsp;potem to zgłosić, powalczyć o&nbsp;swoje. Nie każdy ma tyle woli.  
Poza tym przypomnę, że w&nbsp;tym wpisie poleganie na instytucjach to ostatnia linia obrony.

Dlatego, jeśli chcemy wziąć sprawy we własne ręce i&nbsp;chronić się przed „podglądaczami karty”, do głowy przychodzi mi prowizorka: **zaklejenie części danych z&nbsp;przodu karty czarną taśmą**. Żeby wyglądała trochę tak jak na wcześniejszym obrazku.  
O ile nie oddamy komuś karty na dłużej, to nie odczyta danych.

Poza tym to zabezpieczenie tymczasowe i&nbsp;łatwo je odkręcić, gdyby było trzeba. Gdyby ktoś się na przykład obawiał, że zaklejona karta utknie w szczelinie bankomatu, to można po prostu odkleić taśmę przed jej włożeniem.

Kolejna linia obrony to limit dzienny dla płatności internetowych. Ustawiany analogicznie jak te z&nbsp;poprzedniego punktu.  
No i, jeśli już koniecznie chcemy dać się uratować bankowi, jest też opcja reklamacji (*chargebacku*). 

## Wizyta w&nbsp;oddziale banku

Tracąc portfel, często oprócz karty można stracić dowód osobisty.

A dowód to taki klucz uniwersalny do banku.  
Co nam po wszelkich zabezpieczeniach, limitach itp., jeśli ktoś może przejść się do okienka i&nbsp;je po prostu wyłączyć?

Mając sam dowód, bez karty płatniczej, musiałby szukać banku na chybił-trafił (chyba że gdzieś w internecie wiszą dane łączące nasz numer konta z&nbsp;imieniem i&nbsp;nazwiskiem).

Jeśli ma również kartę, bo na przykład zgarnął cały nasz portfel, to tę sprawę ma z&nbsp;głowy -- na karcie jest nazwa banku.

Podobno w&nbsp;bankach patrzą, czy wygląd zgadza się z&nbsp;tym z&nbsp;dowodu. Zatem złodziej, mając nasze zdjęcie z&nbsp;dowodu, może się odpowiednio wystylizować i&nbsp;ruszyć do najbliższego oddziału.

<img src="/assets/posts/bank-ochrona/ff7-przebieranka.jpg" alt="Dwa zrzuty ekranu z&nbsp;Final Fantasy 7 w&nbsp;nowej wersji. Kadr u&nbsp;góry pokazuje głównego bohatera, mężczyznę o&nbsp;blond włosach z&nbsp;mieczem na plecach. Obrazek jest połączony strzałką z&nbsp;innym obrazkiem, na którym widać tę samą postać w&nbsp;blond peruce i&nbsp;dwiema kokardkami na warkoczach."/>

{:.figcaption}
Źródło: Remake *Final Fantasy VII*.


Owszem, podobno w&nbsp;banku jest jakaś weryfikacja „na oko/podpis”. Ale trzymajmy się prawa Murphy'ego -- załóżmy, że akurat przy „naszym” oszuście osoby z&nbsp;okienka będą miały zły dzień i&nbsp;wszystko przepuszczą.

Pierwsze i&nbsp;oczywiste -- **po zgubieniu dowodu jak najszybciej go zastrzegamy**. Można na poziomie ogólnym, można na poziomie banku. W&nbsp;przypadku PKO BP da się to zrobić choćby przez SMS.

Na stronie PKO BP znalazłem informację, że od 2018 r. również podczas osobistej wizyty trzeba [pokazać dodatkowy kod potwierdzający](https://www.pkobp.pl/aktualnosci/autoryzacja-transakcji-kodem-sms-w-placowkach-banku/).  
Niektórzy mogą krytykować -- bo babci utrudnia życie -- ale moim zdaniem to bardzo dobra wiadomość. Nie wystarczyłby jeden plastikowy kartonik, żeby nas okraść ze wszystkiego.

Jeśli jednak założymy, że nie możemy liczyć na żadne zabezpieczenia ze strony banku, a&nbsp;zastrzec dowodu nie zdążymy, to jego utrata = pewna utrata pieniędzy.  
Wtedy człowiekowi ostrożnemu zostaje jedno rozwiązanie -- w&nbsp;miarę możliwości nie nosić przy sobie dowodu.

Dotąd kojarzyłem skądś opinię, że „każdy musi mieć dowód osobisty” (albo będzie kara). Ponoć na szczęście nie jest aż tak źle. Mieć wyrobiony owszem, rzekomo trzeba, ale według [Dziennika Prawnego](https://www.dziennikprawny.pl/pl/a/czy-zawsze-trzeba-miec-przy-sobie-dowod-osobisty) nie trzeba go przy sobie nosić.

{:.bigspace}
> Oczywiście **nie możemy zostać ukarani za brak posiadania dokumentu tożsamości**, (...) do potwierdzenia naszej tożsamości wystarczy także prawo jazdy lub inny dokument ze zdjęciem i&nbsp;kompletem danych. Nie może być to jednak karta identyfikacyjna z&nbsp;zakładu pracy, czy bilet miesięczny. Przydatna będzie jednak legitymacja szkolna lub studencka.

Oprócz tego, o&nbsp;czym Dziennik Prawny tu nie pisze, można trzymać e-Dowód w&nbsp;telefonie (tylko że to z&nbsp;kolei powierzanie tej cennej rzeczy jednemu urządzeniu...).

Piszą za to, że mogłoby być nieprzyjemnie, gdyby policji szwankował system, a&nbsp;my nie mielibyśmy innego dokumentu. Wtedy będzie chwila posiadówki na komendzie, aż ustalą tożsamość.

{:.bigspace}
> jednak czy perspektywa zatrzymania przez policję nie jest czymś w&nbsp;rodzaju kary?

Na to pytanie sami musimy odpowiedzieć. Jeśli mamy któryś z&nbsp;tych innych, mniej wrażliwych dokumentów, to sprawa jak dla mnie jest jasna i&nbsp;najlepiej je nosić zamiast dowodu.

Zresztą tak subiektywnie: gdyby państwo wymagało noszenia przy sobie czegoś wrażliwego, narażając nas na złodziejaszków, to byłby dobry moment na trochę obywatelskiego nieposłuszeństwa :wink:

W ten sposób omówiliśmy trochę zagrożeń zewnętrznych. Czas na ciemniejsze strony samych banków.

## Ciemne strony

Zawsze jakieś muszą być, prawda? W&nbsp;przypadku banków tymi bardziej oczywistymi jest w&nbsp;moich oczach wykłócanie się z&nbsp;klientami i&nbsp;próba przypisania im *rażącego niedbalstwa*. Mniej oczywiste to uzależnianie się od naszych starych znajomych, korporacji z&nbsp;USA.

# Wpadki i&nbsp;opór ze strony banków

W tym wpisie przyjąłem założenie „nie ma co liczyć na bank, pomóżmy sobie sami”.  
Z jednej strony to eksperyment myślowy, ale z&nbsp;drugiej -- miałem pewne przesłanki, żeby jednak nie do końca ufać bankom.

Przede wszystkim same czasem promowały nieodpowiedzialne zachowania. Taki mBank kiedyś w&nbsp;ramach konkursu w&nbsp;mediach społecznościowych poprosił klientów o&nbsp;[pochwalenie się zdjęciami kart](https://niebezpiecznik.pl/post/mbank-poprosil-klientow-o-wrzucenie-zdjec-kart-platniczych-na-instagrama/).

Brzmiałoby to nieco mniej groźnie, gdybyśmy wierzyli że nas chroni kod z&nbsp;tyłu karty... Ale teraz już wiemy, że on wcale nie daje gwarancji. Zwłaszcza gdyby złodziej chciał coś kupić przez Amazona.

Kolejna sprawa to zderzenie prawa z&nbsp;rzeczywistością.  
Oficjalnie bank powinien w&nbsp;ciągu dnia zwrócić nam skradzione pieniądze. Mimo to zdarzało się, że banki powoływały się na *rażące niedbalstwo klienta* -- czyli jedyną furtkę, która pozwala im uniknąć prawnego obowiązku.

Jak podaje Niebezpiecznik, zrobiły tak m.in. [omawiany tutaj PKO BP i&nbsp;Santander](https://niebezpiecznik.pl/post/ukradli-mi-pieniadze-z-konta-i-co-dalej-prawo-swoje-a-banki-swoje/).

PKO BP nazywał rażącym niedbalstwem podanie danych na fałszywej stronie. Czyli *de facto* złapanie się na oszustwo. Mimo że zwykle jako rażące niedbalstwo rozumie się działanie celowe, np. publikowanie szerszemu gronu odbiorców swoich danych bankowych.

W podobny sposób zasłaniał się Santander. Po tym, jak komputer klienta został zainfekowany wirusem i&nbsp;poszły przelewy do oszustów, prawnicy banku stwierdzili w&nbsp;piśmie:

{:.bigspace}
> w&nbsp;zapisach systemowych posiadanych przez bank odnotowano zarejestrowane użycie instrumentu płatniczego oraz jego uwierzytelnienia (użyto NIK-u, PIN-u oraz SMS-kodu). W&nbsp;ocenie banku stanowi to przesłankę do uznania prawidłowej autoryzacji transakcji.

Czyli tak trochę „Konto jest od przelewów. Jeśli ktoś zrobił przelew, to wszystko jest OK”. A&nbsp;że to akurat był wirus? Peszek.

Owszem, według wpisu Niebezpiecznika sądy orzekały często na korzyść klientów. Co nie zmienia faktu, że przed odzyskaniem pieniędzy musieli poświęcić trochę czasu na użeranie się z&nbsp;własnymi bankami.

Czasem odzyskamy forsę łatwo (bo dla banku sprawne rozwiązanie problemu to dobry PR), innym razem po długiej walce (bo jednak bank woli nie pokrywać straty ze swojej kieszeni). Skąd mamy wiedzieć, który scenariusz nam wypadnie?  
Stąd moje podejście -- nim zaczniemy polegać na innych, ochrońmy siebie.

# Utrwalanie duopolu Google i&nbsp;Apple

Aplikacje bankowe wydają się dość wygodnym sposobem płatności.  
Niestety, niektóre z&nbsp;nich pod płaszczykiem bezpieczeństwa utrudniają życie.

To dlatego, że stawiają wymagania telefonom, na których się ich używa. Są je w&nbsp;stanie spełnić tylko urządzenia „grzeczne”, bez modyfikacji, od dobrze zakorzenionych korporacji. A&nbsp;tak się składa, że w&nbsp;niektórych przypadkach ludzie jednak majsterkują:

1. Przypadek pierwszy to *rootowanie* (na iPhone'ach *jailbreak*).  
Mówiąc prosto, każdy smartfon to pełnoprawny komputer. Ale nałożone są na niego pewne sztuczne ograniczenia (ktoś jeszcze pamięta, czym był *sim lock*? To coś podobnego).  
*Rootowanie* pozwala te ograniczenia usunąć, odzyskać część kontroli nad naszą komórką i&nbsp;na przykład zablokować wścibskim domyślnym aplikacjom łączność z&nbsp;internetem.

2. Przypadek drugi to zmiana systemu operacyjnego na telefonie. Na przykład alternatywami dla Androida są GrapheneOS albo LineageOS. Są oparte na publicznym kodzie Androida, więc działają podobnie. Ale dają ludziom funkcje, których pierwotny Android nie daje (np. niezależność od usług Google'a).

3. Przypadek trzeci to całe telefony oparte na innych systemach, głównie Linuksie. Ich przykłady to PinePhone i&nbsp;Librem. Na razie dopiero pojawiają się wersje *beta*, ale docelowo mają dać użytkownikom jak najwięcej kontroli nad własnymi telefonami.

Działania aplikacji bankowych aktywnie utrudniają życie takim projektom.

Po pierwsze, niektóre apki wykrywają *roota* i&nbsp;[czasem nie chcą się uruchomić](https://security.stackexchange.com/questions/121972/bank-complains-about-rooted-android-is-it-really-any-worse-than-a-windows-deskt), jeśli go odkryją. 
I tak, dotyczy to również [aplikacji PKO](https://www.elektroda.pl/rtvforum/topic3587330.html).

Niektóre są jeszcze gorsze -- korzystają z&nbsp;usługi od Google zwanej **SafetyNet**.  
To dogłębna weryfikacja telefonu. Wykrywa wszelkie modyfikacje, takie jak *rootowanie* albo inne systemy. **Jeśli użyje się czegokolwiek innego niż system od producenta, to nie przejdzie się weryfikacji**.  
Co gorsza, SN wykorzystuje fizyczny element wewnątrz telefonu, więc żadnym programem [się jej nie ominie](https://www.androidpolice.com/2020/06/29/googles-dreaded-safetynet-hardware-check-has-been-spotted-in-the-wild/).

Majsterkowanie z&nbsp;własnym telefonem, włączanie w&nbsp;nim nowych opcji to nic złego. Robimy to z&nbsp;własnej woli. To wręcz realizacja podstawowej wolności.

A jednak niektóre banki z&nbsp;tym walczą, dają się skusić rzeczom takim jak SafetyNet. Z&nbsp;ich punktu widzenia to zdjęcie z&nbsp;siebie odpowiedzialności za straty klientów, łatwe wyjście.

Argumentują, że to „ochrona przed hakerami”. Nie wspominają, że ataki hakerskie na telefon to sprawy rzadkie, więc mało kogo tym ratują. A&nbsp;swobodę odejścia od wielkich firm odbierają wszystkim.

Cała sytuacja prowadzi do tego, że -- świadomie lub nie -- **niektóre banki blokują wszystko poza systemami od Google'a i&nbsp;Apple, podtrzymując oligopol**.

Na razie wszelkie alternatywne telefony, jak Librem i&nbsp;PinePhone, dopiero raczkują.  
Ale już teraz widać, że przez działania banków (i podobnych *antymajsterkowiczów*) będą miały pod górkę i&nbsp;być może nigdy się szerzej nie przyjmą.

Jakiś klient je kupi. Ale tu jedna aplikacja nie będzie działała, tam inna. Producent chciałby to naprawić, ale nie ma jak. Autorzy aplikacji nie pójdą mu na rękę (bo za mały gracz), Google nie zluzuje wymagań (bo to konkurencja).

Jeśli klient jest niecierpliwy (a niestety wielu jest), to po prostu zmieni produkt. Gdy zrobi tak więcej osób, to alternatywny producent zamknie interes.  
W takich warunkach leśne dziadki elektroniki nigdy nie odejdą, nawet gdyby pojawił się konkurent z&nbsp;dobrym i&nbsp;świeżym pomysłem.  
Jak przy takim nastawieniu cokolwiek ma się zmienić? :roll_eyes:

Ciemne strony bankowości to również kwestia zachowań monopolistycznych Visy i&nbsp;MasterCarda (oczywiście obu prosto z&nbsp;USA). Ale to sprawa na cały osobny wpis.

{% include info.html type="Podobne wpisy" text="Funkcję podobną do SafetyNet w&nbsp;większych komputerach może pełnić Intel Management Engine, opisany w&nbsp;moim poprzednim wpisie. Tam również fizyczny element wewnątrz urządzenia pozwala zablokować alternatywne rozwiązania." %}

## Podsumowanie

Powyżej trochę popatrzyłem na różne elementy dużego współczesnego banku i&nbsp;sposoby na niestracenie kasy. Mam nadzieję, że parę informacji Was zaciekawiło i&nbsp;wyszło poza ogólne porady.

Szczerze mówiąc, wiele z&nbsp;tych rzeczy wiąże się ze zdrowym rozsądkiem. „Nie zdradzać więcej niż trzeba”. „Nie wkładać wszystkich jajek do jednej kobiałki”.

Mam cień nadziei, że stopniowo to wszystko będzie przenikało do szerszej świadomości, a&nbsp;oszustów spasionych cudzym kosztem czeka zmiana branży. Na przykład na żebraczą.

Jeszcze bardziej liczę na to, że świat bankowości będzie szedł bardziej w&nbsp;stronę otwartych rozwiązań i&nbsp;ułatwień, a&nbsp;mniej w&nbsp;stronę spychania ludzi ku garstce wybranych systemów.
