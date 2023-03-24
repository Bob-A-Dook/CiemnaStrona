---
layout: post
title:  "Apki to pułapki 4 – mikrofony"
subtitle: "Po co podsłuchiwać? Są ciekawsze metody."
description: "Po co podsłuchiwać? Są ciekawsze metody."
date:   2023-02-15 17:00:00 +0100
tags: [AI, Apki, Hardware, Inwigilacja]
firmy: [Facebook]
category: apki
category_readable: "Apki to pułapki"
image:
  path: /assets/posts/apki/mikrofony/mikrofony-john-wick-baner.jpg
  width: 1200
  height: 700
  alt: "Przerobiony plakat filmu John Wick, pokazujący tytułowego bohatera w garniturze. Jest w niego wycelowanych kilkanaście pistoletów, które przerobiono na mikrofony"

---

<img src="/assets/posts/apki/mikrofony/mikrofony-john-wick-baner.jpg" alt="Przerobiony kadr z&nbsp;plakatu filmu. W&nbsp;centrum spokojnie stoi mężczyzna w&nbsp;garniturze. Ma długie włosy, poważną minę, lekki zarost i&nbsp;poranioną po bokach twarz. Otacza go półkole kilkunastu wycelowanych w&nbsp;niego pistoletów. Tylko że w&nbsp;ramach przeróbki nałożono na ich lufy różnego rodzaju mikrofony." />

{:.figcaption}
Źródło: plakat filmu *John Wick 2*. Przeróbki moje.

> występ zarejestrowali na sześciuset aparatach powtykanymi w&nbsp;instrumenty mikromikrofonikami, a&nbsp;do bębna włożono mi makromikrofon, (...) przez lupy obejrzeli nas i&nbsp;każdy kąt, a&nbsp;potem naradzali się siedem dni i&nbsp;jeszcze miesiąc. Precyzji analiz nie wysłowisz!

{:.figcaption}
Stanisław Lem, „Cyberiada” (rozdział o&nbsp;Harmonii Sfer).

Co by powiedziała losowa osoba, gdyby ją zapytać, jak wyobraża sobie śledzenie i&nbsp;naruszanie prywatności? Obstawiam, że padłoby słowo „podsłuch”. Albo „nagrywanie”.

Te słowa dość mocno działają na wyobraźnię, a&nbsp;przy tym nie wydają się czymś odległym i&nbsp;abstrakcyjnym. O&nbsp;podsłuchach słyszymy w&nbsp;wiadomościach. Zazdrośni małżonkowie mogą je kupić w&nbsp;sklepach. Na korpogrupach ludzie sobie czasem doradzają, żeby zbierać dowody ukrytym dyktafonem.

Nie powinno nas zatem dziwić, że te same wyobrażenia na temat metod śledzenia przeniesiono do świata elektroniki konsumenckiej.

Czasem te obawy są uzasadnione, zwłaszcza gdy mówimy o&nbsp;śledzeniu konkretnej ofiary. Ale powstało też trochę **mitów, niesłusznie przeceniających rolę mikrofonów w&nbsp;cyfrowym świecie**. W&nbsp;którym zbieraczami naszych danych są giganci reklamowi.

Ten wpis rozprawi się z&nbsp;takim popularnym przekonaniem -- o&nbsp;tym, że aplikacje od Facebooka (zwanego teraz Meta) nas podsłuchują. Wnioski będą na tyle ogólne, że śmiało można je odnieść do innych firm i&nbsp;programów.

Mój kolejny wpis na temat mikrofonów przybliży natomiast te bardziej rzeczywiste zagrożenia z&nbsp;ich strony. Bez obaw, są ciekawsze niż proste podsłuchiwanie :wink:

### Spis treści

* [Podsłuchujący Facebook – wprowadzenie](#podsłuchujący-facebook--wprowadzenie)
* [Mały praktyczny eksperyment](#mały-praktyczny-eksperyment)
* [Argumenty przeciw teorii podsłuchu](#argumenty-przeciw-teorii-podsłuchu)
  * [Kwestia opłacalnych alternatyw](#kwestia-opłacalnych-alternatyw)
  * [Kwestia ryzyka](#kwestia-ryzyka)
  * [Kwestia wykrywalności](#kwestia-wykrywalności)
  * [Kwestia zabezpieczeń](#kwestia-zabezpieczeń)
  * [Kwestia rozmiaru danych](#kwestia-rozmiaru-danych)
  * [Podsumowanie wątku](#podsumowanie-wątku)
* [Jak nie podsłuch, to co?](#jak-nie-podsłuch-to-co)
* [Jak się chronić](#jak-się-chronić)
* [Źródła obrazków](#źródła-obrazków)


## Podsłuchujący Facebook – wprowadzenie

Nieraz zdarzało się, że ludzie rozmawiali ze sobą o&nbsp;swoich planach albo rzeczach, jakie by się im przydały. Po czym po uruchomieniu którejś z&nbsp;aplikacji od firmy Meta (jak Facebook, Messenger czy Instagram) jedna z&nbsp;osób widziała reklamę tej samej rzeczy, której dotyczyła rozmowa.

Wniosek, który pozwolę sobie nazywać *teorią podsłuchu* -- „Facebook mnie podsłuchuje”. Znajdziemy na świecie tysiące takich historii.

Problem w&nbsp;tym, że **prawie na pewno nie podsłuchuje. Ani on, ani inne wielkie firmy**.

I nie mówię tutaj, że są godne zaufania. Kto czyta bloga, ten zna moją niechęć do cybergigantów, a&nbsp;sam Facebook [przewinień ma wiele](https://www.nbcnews.com/tech/social-media/timeline-facebook-s-privacy-issues-its-responses-n859651).  
Nie twierdzę też, że osoby widzące niepokojąco trafne reklamy coś sobie zmyśliły. Bo wiarygodnych historii o&nbsp;stalkerskich reklamach jest pełno.

Ale, jak zaraz zobaczymy, jest sporo argumentów przeciw istnieniu *tej konkretnej* złej trójcy Facebook-reklamy-mikrofon. Od kwestii prawnych po techniczne. Istnieją też wiarygodne, alternatywne wyjaśnienia fenomenu dopasowanych reklam.

W tym wpisie opieram się na własnych przemyśleniach, a&nbsp;także innych źródłach, jak [artykuł naukowy ze Springera](https://link.springer.com/content/pdf/10.1007/978-3-030-22479-0_6.pdf), w&nbsp;którym dwóch niemieckich badaczy  dość wszechstronnie analizuje sprawę.

## Mały praktyczny eksperyment

Historie o&nbsp;podsłuchiwaniu często sprowadzają się do „rozmawialiśmy o&nbsp;czymś, nie używaliśmy telefonów, a&nbsp;jednak potem pokazało bardzo trafne reklamy”.

Załóżmy na chwilę, że faktycznie ma miejsce słuchanie naszych rozmów. Ale, o&nbsp;ile nie jesteśmy kompletnymi nałogowcami, nasz telefon najczęściej ma zablokowany ekran i&nbsp;spoczywa w&nbsp;naszej kieszeni albo na jakimś stoliku.

Czy nagrywanie w&nbsp;takiej sytuacji jest w&nbsp;ogóle możliwe?

Żeby osobiście przetestować mikrofon na swoim telefonie (Huawei, system Android 10), skorzystałem z&nbsp;niezrównanej aplikacji Termux wraz z&nbsp;rozszerzeniem *Termux:API* (więcej o&nbsp;jej instalacji możecie poczytać [w osobnym samouczku](/tutorials/termux#instalujemy-termuksa){:.internal}).

Następnie użyłem komendy pozwalającej nagrywać dźwięk prosto do pliku -- `termux-microphone-record -f mictest` ([dokładniejszy opis](https://wiki.termux.com/wiki/Termux-microphone-record)).  
Po włączeniu nagrywania:

* powiedziałem parę słów;
* nacisnąłem ikonkę domu, żeby przejść do ekranu głównego (i&nbsp;znów parę słów);
* nacisnąłem przycisk z&nbsp;boku telefonu, żeby włączyć blokadę ekranu i&nbsp;go wygasić (po czym parę słów);
* włączyłem ekran (parę słów);
* wprowadziłem kombinację odblokowującą telefon (parę słów);
* otwarłem Termuksa i&nbsp;przerwałem nagrywanie  
  (komendą `termux-microphone-record -q`).

Zajrzałem do otrzymanego pliku. Po cichu miałem nadzieję, że na którymś z&nbsp;etapów przestało nagrywać. Ale nie, nagrały się wszystkie moje wypowiedzi. Również ta przy wyłączonym i&nbsp;zablokowanym ekranie.  
Niestety potwierdził się najbardziej niekorzystny wariant -- **aplikacje jak najbardziej mogą słuchać, również z&nbsp;wnętrza naszej kieszeni**. Skoro Termux może, to inne też.

Jest całkiem możliwe, że takie nagrywanie może trwać tylko przez pewien czas; że gdybym poczekał dłużej po zablokowaniu ekranu, to by je samoistnie przerwało. Gdzieś mi mignęła informacja, że apka jest w&nbsp;stanie jedynie *kontynuować* nagrywanie w&nbsp;tle, ale nie jest w&nbsp;stanie go *włączyć* w&nbsp;tym trybie. 

Ale czy to ma nas pocieszyć?  
Wystarczyłoby, żeby jakaś osoba zerknęła na uzależniającą apkę (jak to robi co kilka minut). Apka wtedy włącza nagrywanie. Osoba, odkładając telefon do kieszeni, wraca do przerwanej rozmowy i&nbsp;mówi na głos jakąś tajemnicę. Apka by ją nagrała.

Na szczęście sama techniczna możliwość to dopiero początek. Spójrzmy na inne aspekty, które mimo wszystko przemawiają na niekorzyść teorii podsłuchu.

## Argumenty przeciw teorii podsłuchu

### Kwestia (braku) opłacalności

Od możliwości do czynów jest daleka droga. Zastanówmy się, czy podejrzani w&nbsp;tej sprawie -- megakorpo od produktów cyfrowych -- mieliby motyw. Czy podsłuchiwanie w&nbsp;ogóle by się im opłacało?

Pierwsza myśl: „Oczywiście! Przecież poznaliby nasze największe sekrety”.

Tylko że Facebook czy Google, szczególnie znani ze wścibstwa, są firmami zarabiającymi na reklamach. Liczą się dla nich informacje, które sugerowałyby nasze zainteresowania, styl życia, skłonność do wydatków. Żeby na tej podstawie mogli podsuwać cudze produkty i&nbsp;zyskiwać nasze kliknięcia.

Rozmowy z&nbsp;życia codziennego niekoniecznie by im to dały. Bezcenne marketingowo „jestem w&nbsp;ciąży” albo „chcę wyjechać do ciepłych krajów” toną w&nbsp;morzu prozy życia:

* domowych „zjemy coś na kolację?”, „jak było w&nbsp;pracy?”;
* zawodowych „musimy opracować ten raport do poniedziałku”, „kończę na dziś, na razie!”;
* miejskich „można uchylić okno?”, „zapłacę kartą”.

A w&nbsp;czasach coraz rzadszych rozmów międzyludzkich podsłuch mógłby wyłapać po prostu ciszę i&nbsp;dźwięki tła :wink:

Podsumowując: w&nbsp;przypadku nagrywania całych dni z&nbsp;życia **stosunek bzdetów do cennych (reklamowo) treści mógłby być dość niekorzystny dla firm**. Nie mam twardych danych, ale bardzo mocne przeczucie.

### Kwestia opłacalnych alternatyw

Dane dźwiękowe są bardzo upierdliwe. Jeśli chodzi o&nbsp;poziom trudności pozyskiwania różnych informacji, to streściłbym to tak:

* Ustalenie, że odwiedziliśmy jakąś stronkę albo grupę na Facebooku? Banalnie łatwe.

  Chodząc po stronkach, cały czas nosimy ze sobą swoistą [„wizytówkę” z&nbsp;danych]({% post_url 2021-10-22-pliki-cookies %}){:.internal}. Facebook wie, że my to my.  
  Zaś odwiedzane przez nas profile są już pewnie oznaczone w&nbsp;ich bazie, jako np. *fani motoryzacji*. Kiedy nasza wizytówka pojawi się w takim miejscu, to od razu trafimy do odpowiedniej szufladki.

*  Ustalenie, że odwiedziliśmy stronkę *poza Facebookiem*? To zależy.

   Jeśli stronka zawiera elementy od samego Facebooka -- banalnie łatwe. Jeśli kliknęliśmy w&nbsp;link na samym Facebooku albo w&nbsp;którejś z&nbsp;ich aplikacji? Też możliwe. W&nbsp;innych wypadkach trudne albo niemożliwe.

* Analizowanie wiadomości, jakie piszemy na Messengerze? Średnio trudne.

  Problemem byłaby odporność na literówki, odsiewanie ironii, łapanie kontekstu. Napisane z&nbsp;rezygnacją „Ech, fajnie byłoby dupnąć tym wszystkim i&nbsp;jechać w Bieszczady :p” to niekoniecznie znak, że czas reklamować pensjonaty.

  Ale gdyby Facebook nie przejmował się niedokładnością i&nbsp;po prostu wychwytywał pewne zbitki słów? Wtedy analiza byłaby znacznie łatwiejsza.

* Analiza nagrań głosowych? Bardzo trudna.

  Najpierw trzeba zamienić dźwięk na tekst, co samo w&nbsp;sobie jest wymagające i&nbsp;podatne na błędy. Masa różnych akcentów, slang, szumy w&nbsp;tle i&nbsp;tak dalej.  
  A&nbsp;potem trzeba ten tekst jeszcze przeanalizować, pokonując wszystkie trudności z&nbsp;punktu wyżej.

{% include info.html
type="Ciekawostka"
text="Pamiętajmy też, że łatwo oceniać skuteczność rozpoznawania mowy według dzisiejszych standardów. A&nbsp;przecież oskarżenia wobec Facebooka sięgają dużo dawniejszych lat.  
To, co szumnie nazywa się teraz sztuczną inteligencją, miało wtedy znacznie gorszą jakość. Do tego stopnia, że śmieszkowanie z&nbsp;tego przeszło do mainstreamu.  
Znajdziemy je choćby w&nbsp;serialu „Krzyk” od MTV i&nbsp;Netflixa, wydanym w&nbsp;2015 roku. Jest tam przykład [nieudanego wybierania głosem](https://youtu.be/z76Ngre8i9I?t=492) numeru na policję :wink:"
%}

### Kwestia ryzyka

Prezes Facebooka, Mark Zuckerberg, podczas zeznawania przed komisją senacką [został wprost zapytany](https://phys.org/pdf442761942.pdf): „Czy Facebook nas nagrywa?”.  
Odpowiedział że nie. Potem rozwinął temat i&nbsp;dodał, że Facebook prosi o&nbsp;pozwolenie na nagrywanie tylko wtedy, kiedy chcemy bezpośrednio z&nbsp;aplikacji nagrywać filmy z&nbsp;dźwiękiem.

I tak, wiem. „Lisek-chytrusek powiedział, że to nie on. A&nbsp;tak naprawdę to był on”. Tylko że tutaj naprawdę ryzyko byłoby zbyt wielkie.

Bo pomyślmy tylko, co mógłby nagrać taki telefon (który przecież nie wie, że jest w&nbsp;jakimś tajnym miejscu i&nbsp;nagrywać nie powinien). Tajemnice adwokackie. Tajemnice przedsiębiorstw. Poufne rozmowy polityków.

Jak zaraz zobaczymy, dość łatwo byłoby wykryć przypadki nagrywania. Wystarczyłaby jedna wpadka, głodny sławy badacz cyberbezpieczeństwa, żeby zebrać dowody przeciw Facebookowi.  
A potwierdzenie takiej afery oznaczałoby dla nich koniec. Zarzuty karne, kompletne zrujnowanie reputacji. I&nbsp;to wszystko po to, żeby używać jednej z&nbsp;najbardziej okrężnych i&nbsp;żmudnych metod zbierania danych? Powątpiewam :wink:

Niektórzy mogliby w&nbsp;tym miejscu przypomnieć, że dokumenty ujawnione przez Edwarda Snowdena pokazały, że Facebook [ściśle współpracował z&nbsp;amerykańskimi agencjami](https://arstechnica.com/tech-policy/2015/03/eu-dont-use-facebook-if-you-want-to-keep-the-nsa-away-from-your-data/). Zatem, mając takie powiązania, być może mógłby olać ryzyko i&nbsp;robić swoje?

Tylko że masowe nagrywanie łatwo wykryć. Wykrycie prowadziłoby do odpływu użytkowników. A&nbsp;to do zmniejszenia skali śledzenia.  
Gdybym był jakimś NSA, to wolałbym się trzymać rzeczy bardziej przyziemnych, zadowolić się dostępem do danych tekstowych. Zachłanność i&nbsp;naciskanie na globalny podsłuch mogłyby spalić cały projekt.

### Kwestia wykrywalności

To, że zainstalujemy u&nbsp;siebie jakąś aplikację, nie oznacza jeszcze, że może ona tak po prostu robić na naszych telefonach co chce. **Jest tylko gościem i&nbsp;może co najwyżej prosić system o&nbsp;pewne rzeczy**.

Przypomnę tutaj piramidkę obrazującą warstwy naszego urządzenia, stworzoną na potrzeby serii „Apki to pułapki”:

{:.bigspace-before}
<img src="/assets/posts/apki/mikrofony/apki_piramida_mikrofony.jpg" alt="Schemat pokazujący hierarchię we współczesnym urządzeniu. Ma kształt odwróconej piramidy. Na samym dole mamy ikonę procesora podpisaną CPU. Odchodzą od niej strzałki do ikonki symbolizującej mikrofon. Cała warstwa jest podpisana 'hardware'. Nad nią w&nbsp;piramidzie mamy kolejno: 'firmware', 'jądro systemu' oraz 'system operacyjny'. Na tej warstwie stoi mniejszy element, podpisany 'Programy' i&nbsp;opatrzony ikoną aplikacji Messenger."/>

{:.figcaption}
Źródło: Flaticon, Emojipedia, Wikimedia Commons (szczegóły [pod koniec wpisu](#źródła-obrazków)).  
Aranżacja i&nbsp;przeróbki moje. Przypominam: pojęcie jądra systemu luźne, nie do końca odpowiada formalnej definicji.

Rzeczy położone wyżej są w&nbsp;pełni zależne od tych położonych niżej.

Jeśli jesteśmy szeregowymi użytkownikami, to nie sięgamy zwykle poniżej warstwy `System operacyjny`. Ale istnieją różni hobbyści, majsterkowicze, amatorscy i&nbsp;zawodowi badacze cyfrowej prywatności.

Takie osoby mogłyby podporządkować sobie niższe warstwy telefonu. Umieścić tam cyfrowe odpowiedniki czujników.  
„Informuj mnie za każdym razem, kiedy nastąpi przepływ danych między apką a&nbsp;mikrofonem”.

Aplikacje nie miałyby pojęcia o&nbsp;istnieniu tego rodzaju czujników -- bo są w&nbsp;wyższych warstwach. Nawet jeśli zapytają dolne warstwy, to te po prostu mogą je okłamać bez konsekwencji. „Niee, nikt nie patrzy, co tam robisz z&nbsp;mikrofonem. *Trust me, bro*”.

{% include info.html
type="Ciekawostka"
text="Istnieją pewne przypadki, kiedy ta sytuacja się odwraca i&nbsp;apki jednak *są* w&nbsp;stanie sobie zagwarantować, że nikt ich nie analizuje, a&nbsp;odwiedzany przez nie system jest mainstreamowy, prosto z&nbsp;fabryki. To różne rzeczy związane z&nbsp;zagadnieniem *trusted computing*. Temat na osobny wpis, ale warto wiedzieć jak najwcześniej."
%}

Ale nawet gdyby badacze, z&nbsp;tego czy innego powodu, nie byli w&nbsp;stanie kontrolować własnego telefonu, to jeszcze nie koniec walki. Bo aplikacja musi w&nbsp;końcu wysłać nasze sekrety swoim twórcom.

Tymi danymi mogą być na przykład nagrania naszych rozmów. Są „martwe”, nieruchome, niezdolne do aktywnego ukrywania się. Podobnie jak piosenka w&nbsp;formacie MP3 nie zaatakuje naszych uszu, póki jej nie odtworzymy.

Badacz może postawić na drodze do internetu własny router lub inne urządzenie, przechwytujące i&nbsp;analizujące ruch. W&nbsp;ten sposób szybko by wyszło na jaw, czy jakaś apka próbuje wysyłać w&nbsp;świat megabajty nagrań, mimo że jej akurat nie używamy.

Do takich analiz nie potrzeba żadnych drogich laboratoriów, bariery wejścia są niskie. Wiele da się osiągnąć bibliotekami *open source* i&nbsp;znajomością komputera.  
A nagroda dla kogoś, kto zdemaskowałby podsłuchy od wielkiego korpo? Wieczna chwała, szacun na dzielni. Otwarte drzwi do ciekawych współprac dla tych, którym na tym zależy.

W takim klimacie **popularne i&nbsp;kontrowersyjne apki Facebooka ściągają na siebie wiele par oczu**. Oczu nieraz im wrogich. Oczu przenikliwych, zdolnych patrzeć na apki na własnych warunkach, jak przez lustro weneckie.

A jednak do teraz nie widziałem, żeby badacze bili na alarm: „tak, te aplikacje podsłuchują nas przez mikrofon”. To dla mnie jeden z&nbsp;najmocniejszych dowodów na to, że jednak nie słuchają.

Tym niemniej niektórzy mogliby uznać fragment wyżej za ślepą wiarę w&nbsp;autorytet, a&nbsp;przecież ludzie mogą być zawodni. Ale oprócz nich mamy też zabezpieczenia cyfrowe.

### Kwestia zabezpieczeń

Skupię się tu na systemie Android, bo jest mi bliższy.

{:.post-meta .bigspace-after}
Jeśli ktoś nie wie -- to system obecny na większości smartfonów. Co nie jest iPhone'em, to ma dużą szansę mieć w&nbsp;sobie Androida.

Dawniej, do wersji 6&nbsp;Androida, mieliśmy Dziki Zachód. Aplikacje mogły tak po prostu sobie nagrywać różne rzeczy mikrofonem. Ale potem się to zmieniło, wraz z&nbsp;uszczelnieniem *systemu pozwoleń*. To użytkownik decyduje, czy danej aplikacji wolno używać mikrofonu.

Pozwolenia odpowiadają z&nbsp;grubsza warstwie `System operacyjny`. Z&nbsp;naszego punktu widzenia to chociażby zwykłe menu z&nbsp;ustawieniami telefonu. Możemy tam zaznaczyć, że nie dajemy aplikacji dostępu do mikrofonu.

{:.figure .bigspace}
<img src="/assets/posts/apki/mikrofony/android-mikrofon-pozwolenie.jpg" alt="Zrzut ekranu pokazujący fragment menu z Androida, pytający czy chcemy pozwolić aplikacji na dostęp do mikrofonu" width="500px"/>

A apka tego zakazu nie przeskoczy, bo **warstwy wyższe są zależne od niższych**. Może co najwyżej prosić nas o&nbsp;pozwolenie na mikrofon, wyświetlając oficjalne systemowe okienko. A&nbsp;my możemy odmawiać.

Czy mogłaby to jakoś obejść i&nbsp;włączyć nagrywanie? Legalnie -- tylko przez uśpienie naszej czujności, bo systemu nie obejdzie.  
Może poprosić o pozwolenie w&nbsp;sytuacji, kiedy nie brzmi ono podejrzanie albo kiedy robimy coś w&nbsp;pośpiechu. Mam dwa przykłady próśb o&nbsp;dostęp do mikrofonu; jedną wiarygodną, drugą mniej:

1. Messenger

   Jeśli spróbujemy nagrać film bezpośrednio przez aplikację, poprosi nas o&nbsp;dostęp do mikrofonu.  
   Brzmi w&nbsp;porządku, w&nbsp;końcu jakoś trzeba nagrać filmy z&nbsp;dźwiękiem. Android, przynajmniej mój, nie ma niestety czegoś takiego jak *pozwolenie tylko na krótkotrwałe nagranie multimediów*.

2. Przeglądarka Kiwi Browser

   Jako jedna z&nbsp;bardzo nielicznych mobilnych przeglądarek pozwala instalować dodatki. Czasem się to przydaje.  
   Ale zaniepokoiło mnie, kiedy chciałem jeden taki dodatek uruchomić, wybierając ręcznie jego folder. Aplikacja poprosiła mnie o&nbsp;dostęp do mikrofonu. Odmówiłem i&nbsp;mogłem dalej normalnie z&nbsp;niej korzystać.  
   Możliwe że chodziło o&nbsp;jakąś niewinną możliwość udzielania poleceń głosowych. Ale, cytując klasyka, niesmak pozostał.

Czy to przez uśpioną czujność, czy to przez pośpiech, możliwe że raz udzielimy apce pozwolenia. Wtedy niestety **pozostanie aktywne, póki sami go nie cofniemy**. Taka słabość systemu Android.  
Ale nawet jeśli aplikacja dostanie pozwolenie na mikrofon, nie oznacza to, że nasz telefon już zmienił się w podsłuch.

Przede wszystkim już od wersji 9&nbsp;(Pie) [nie da się włączyć nagrywania, gdy apka jest w&nbsp;tle](https://www.theverge.com/2018/3/7/17091104/android-p-prevents-apps-using-mic-camera-idle-background). Nadal można ją najpierw włączyć, a&nbsp;potem zablokować ekran, zachowując działanie mikrofonu -- jak ja w&nbsp;moim eksperymencie. Ale nikt nie włączy nam podsłuchu zdalnie, w&nbsp;telefonie nieużywanym przez dłuższy czas.

Od pewnego czasu zabezpieczenia poszły jeszcze dalej. Android [od wersji 12](https://source.android.com/docs/core/permissions/privacy-indicators) dostał **kropkę bezpieczeństwa** -- oznaczenie widoczne w&nbsp;górnej części ekranu, kiedy jakaś apka korzysta z&nbsp;mikrofonu.  
Apple dodało taką kolorową kropkę wcześniej, w&nbsp;2020 roku, w&nbsp;wersji [iOS 14](https://www.forbes.com/sites/kateoflahertyuk/2020/09/21/ios-14-heres-why-theres-an-orange-dot-on-your-iphone/).

Oznaczenia nieco zmieniają reguły gry. Od teraz żadna apka nie powinna być w&nbsp;stanie dyskretnie nas nagrywać.

No dobra. A&nbsp;czy jest opcja, że apka jakoś oszuka system? Przyzna sobie pozwolenie, zmusi mikrofon do ciągłego nagrywania, wyłączy kropki informacyjne?

Zapewne tak, ale w&nbsp;tym celu musiałaby zhakować nam telefon. Oznacza to, że wchodzimy w&nbsp;czarną strefę, gdzie raczej nie spotkamy większych korpo.  
Nie wierzę w&nbsp;ich standardy etyczne. Ale pewien poziom awersji do ryzyka to jednak mają.

### Kwestia rozmiaru danych

Załóżmy, że Facebook wysyłałby sobie na masową skalę nagrania rozmów użytkowników. I&nbsp;zapomnijmy na chwilę o zawodowych badaczach aplikacji. Gdyby w&nbsp;świat szły nagrania, to nawet cywil mógłby się zorientować, że coś jest nie tak.

Po pierwsze, pliki audio są znacznie większe niż dane tekstowe. Po drugie, każdy użytkownik ma wgląd do uproszczonych statystyk pokazujących, ile danych zużyły apki  
(na Androidzie odwiedzamy kolejno opcje: `Ustawienia`, `Sieć komórkowa`, `Wykorzystanie transmisji danych`).

Wśród rzeszy użytkowników Messengera znalazłyby się osoby, które na te dane patrzą, bo chcą na przykład mieścić się w&nbsp;limicie swojego doładowania. I&nbsp;ktoś by się w&nbsp;końcu zorientował. Apki firmy Meta byłyby widoczne z&nbsp;nazwy jako pochłaniacze setek megabajtów danych. Nawet kiedy się z&nbsp;nich nie korzysta. O&nbsp;sprawie zrobiłoby się głośno.

Poza tym te wszystkie ciężkie dane, od setek milionów ludzi, leciałyby na serwery Mety. Musieliby je przetworzyć, wyciągnąć z&nbsp;nich informacje. A&nbsp;to duże zużycie mocy obliczeniowej (czyli prądu, czyli całkiem namacalne koszty!), ryzyko zapychania łącz...

{:.bigspace}
<img src="/assets/posts/apki/mikrofony/messenger-mikrofon-internet.jpg" alt="Schemat pokazujący, jak od mikrofonu do ikony apki Messengera wędrują dane, oznaczone przez ciężarek z&nbsp;narysowanymi nutami. Identyczny ciężarek widać nad strzałką prowadzącą od Messengera do loga firmy Meta."/>

I to wszystko po to, żeby pozyskiwać informacje o&nbsp;użytkownikach jednym z&nbsp;najbardziej okrężnych i&nbsp;niewydajnych sposobów? Wątpię.

Ale to nie wyczerpuje wszystkich możliwości. **Może nagrania są analizowane jeszcze na naszym telefonie, a&nbsp;do Facebooka trafiają jedynie dużo lżejsze wyniki analiz**?

Istnieją metody uczenia maszynowego, określane marketingowo mianem sztucznej inteligencji. Gdzieś w&nbsp;Messengerze lub innej aplikacji mógłby być zagnieżdżony tak zwany *model*. Program wyspecjalizowany w&nbsp;zamianie dźwięku na tekst.  
Gdyby Facebook użył czegoś takiego, to rozwiązałby sprawę wysyłania danych oraz płacenia za prąd. Przerzuciłby koszty na nas.

{:.bigspace}
<img src="/assets/posts/apki/mikrofony/messenger-mikrofon-on-device.jpg" alt="Schemat pokazujący, jak od mikrofonu do ikony apki Messengera wędrują dane, oznaczone przez ciężarek z&nbsp;narysowanymi nutami. Kolejna strzałka prowadzi w&nbsp;dół, do ikony drzewka decyzyjnego. Stamtąd do Messengera wraca strzałka, oznaczona ikoną karteczki z&nbsp;napisem 'Dane'. Na koniec strzałka z&nbsp;taką samą karteczkę prowadzi do loga firmy Meta."/>

...Tylko że to tylko z&nbsp;pozoru brzmi tak różowo. Bo **modele to złożone programy, ciężkie i&nbsp;wymagające**.

Do tego stopnia, że przez dłuższy czas nie było nawet mowy o&nbsp;analizie głosu na urządzeniu. Opcja dyktowania tekstu, zapewniana przez Google, polegała na wysyłaniu do nich nagrań. Tam analizował je jakiś mocarny serwer i&nbsp;odsyłał wyniki.  
Pierwsze modele `on-device` od Google'a, przetwarzające dyktowany tekst na telefonie, weszły [dopiero w&nbsp;2019 roku](https://ai.googleblog.com/2019/03/an-all-neural-on-device-speech.html).

{:.post-meta .bigspace-after}
Dla formalności: fakt, że przesyłanie nagrań było powszechne, nie jest dowodem na możliwość ciągłego podsłuchu. Dyktowanie działało tylko przez chwilę, na życzenie użytkownika, wysyłano krótkie fragmenty. Jest więc znacznie bardziej realne od strony praktycznej.

Ten pierwszy model, którym chwalił się Google, ważył 80&nbsp;MB i&nbsp;był w&nbsp;stanie rozpoznawać tylko język angielski. Więc ewentualne podsłuchiwanie Polaków by odpadało.

To może spójrzmy -- bardzo luźno i&nbsp;nieoficjalnie -- na nowinkę z&nbsp;ostatnich miesięcy. Model zwany Whisper, zamieniający mowę na tekst i&nbsp;obsługujący wiele języków.

Jego najmniejsza „pełna” wersja, *tiny*, znajduje się [tutaj](https://huggingface.co/openai/whisper-tiny/tree/main). Trzon modelu waży 151&nbsp;MB.  
Od biedy da się zejść nieco niżej; pewna osoba „odchudziła” model [do rozmiaru 39&nbsp;MB](https://github.com/bjnortier/whisper-tflite-ios/blob/main/whisper-tflite-ios/resources/whisper.tflite), do formatu `.tflite`, przystosowanego do działania na telefonie. Ale nie ma nic za darmo -- takie odchudzanie odbywa się kosztem jakości rozpoznawania mowy.

A, przypomnę, Whisper potrafi jedynie zamieniać nagrania głosu na tekst. Do celów reklamowych trzeba by jeszcze wyciągnąć z&nbsp;tekstu pojęcia -- albo w&nbsp;sposób szybki, lecz pełen niedoróbek, albo dokładny -- co jednak wymagałoby jeszcze jednego, osobnego modelu.

Na tej podstawie możemy stwierdzić, że Messenger, ważący w&nbsp;całości [52,6 MB](https://apkpure.com/facebook-messenger/com.facebook.orca/download), nie mógłby zawierać w&nbsp;sobie pełnej wersji Whispera ani nawet kilkuletniego modelu Google'a.  **Cała aplikacja jest mniejsza niż sam model rozpoznający mowę**.  
Od biedy zmieściłby się Whisper w&nbsp;wersji `.tflite`, ale nie zostałoby wiele miejsca na inne rzeczy.

Ale może podstawowa apka pobierałaby sobie model później, na raty?  
Jest to możliwe, ale raczej byłoby do wychwycenia. Mówimy o&nbsp;co najmniej kilkudziesięciu megabajtach, których nie dałoby się wyjaśnić pobieraniem multimediów. Dla niektórych to nic, ale bardziej oszczędni użytkownicy by się mogli połapać.

Zwłaszcza że niektórzy co pewien czas czyszczą dane aplikacji. W&nbsp;takim wypadku model pobrany z&nbsp;zewnątrz, niebędący częścią pierwotnej aplikacji, również zostałby usunięty. Apka musiałaby go pobierać od nowa.

W dodatku podczas pracy modelu szybciej rozładowywałaby się bateria. Coś takiego dostrzegłby nawet szeregowy użytkownik, nie mówiąc już o badaczach.

Nie wykluczam całkowicie opcji, że Facebook mógłby wykorzystać jakieś triki, żeby wyciągać dane z&nbsp;nagrań poza telefon. Ale pełnoprawna analiza mowy raczej odpada, podobnie jak wysyłanie surowych nagrań w&nbsp;świat.

### Podsumowanie wątku

Patrząc na wszystkie powyższe fakty, zaryzykuję i&nbsp;stwierdzę, że **duże firmy nie śledzą nas przez dyskretne nagrywanie naszych rozmów**. Zbyt wielkie ryzyko, zbyt mała opłacalność, za wiele przeszkód technicznych do pokonania.

Być może kiedyś wścibskie firmy miały swój złoty czas na podsłuchiwanie. Nie było opcji chroniących prywatność, nie było przepisów RODO/GDPR, a&nbsp;rozpoznawanie mowy było już użyteczne w&nbsp;praktyce.  
Ktoś i&nbsp;tak by je pewnie złapał na tym procederze, więc nie uważam tej opcji za realną. No ale załóżmy, że istniała.

Tym niemniej -- przez ostatnie lata ta furtka się zamknęła. Większe ryzyko prawne oraz mocniejsza ochrona prywatności (nawet jeśli głównie na pokaz) sprawiają, że potajemne sięganie po mikrofon już naprawdę nie powinno się aplikacjom opłacać. Ten jeden raz to my, użytkownicy, jesteśmy bliżsi zwycięstwa.

## Jak nie podsłuch, to co?

Wyżej nawrzucałem trochę argumentów na niekorzyść teorii podsłuchu. Ale przyroda nie znosi pustki. Ubijając jedno wyjaśnienie, przyda się przedstawić alternatywne.

„Okej, pełno dowodów przeciw nagrywaniu. Ale przecież rozmawialiśmy o&nbsp;czymś, a&nbsp;potem to się pojawiło w&nbsp;reklamie. Nie ma bata, musieli podsłuchiwać rozmowę”.

Nad możliwymi wyjaśnieniami rozwodziłem się w&nbsp;swoim innym wpisie, [omawiającym komentarze]({% post_url 2022-11-02-dyskusja-technostrefa-apki %}){:.internal} spod filmu TechnoStrefy z&nbsp;YouTube'a. Przypomnę krótko najbardziej prawdopodobnych winowajców odpowiedzialnych za celne reklamy:

* Pliki cookies.

  Mówią Facebookowi o&nbsp;tym, że odwiedziliśmy konkretną stronę internetową (o&nbsp;ile miała u&nbsp;siebie element zwany Facebook Pixel). Mogą być obecne również na stronach nienależących do Fejsa. Mogą nas złapać nawet wtedy, gdy korzystamy ze zwykłej przeglądarki na innym urządzeniu, a&nbsp;nie z&nbsp;apki na telefonie. 

* Korelowanie po lokalizacji.

  Gdy mamy apkę od Facebooka, to da się ustalić, że byliśmy w&nbsp;konkretnym miejscu. Albo jednym i&nbsp;tym samym miejscu co inna osoba.  
  Czy to przez koordynaty GPS-a, czy to przez korzystanie z&nbsp;tego samego hotspota. Czy to nawet przez Bluetooth. Albo nietypowe nazwy hotspotów wokół nas, nawet jeśli z&nbsp;żadnym się nie połączyliśmy.

* „Zarażanie preferencjami”.

  Jeśli Facebook akurat nie ma na nas reklamowego pomysłu, może po prostu podpatrzeć coś u osoby, z&nbsp;którą ostatnio wchodziliśmy w&nbsp;interakcje, i&nbsp;podsyłać to samo.

  Przykład? Pisaliśmy z&nbsp;kimś, kto akurat odkrył w&nbsp;sobie zajawkę na komiksy. Facebook wie o&nbsp;tej zajawce przez to, co ta osoba klikała. Wie również o&nbsp;tym, że korespondowaliśmy, więc dla nas również szykuje „przez skojarzenie” reklamy komiksów. **I tak byśmy je dostali, niezależnie od innych czynników**.  
  Ale zanim reklamy zdążą nam się pokazać, spotykamy tę osobę na żywo; oczywiście mówi o&nbsp;komiksach. Potem, gdy pokazuje nam się ich reklama, obwiniamy mikrofon. Tymczasem to nie jego wina, zarażenie nastąpiło wcześniej.

Wiele przypadków „podsłuchiwania” dałoby się wyjaśnić zachodzeniem którejś z&nbsp;tych rzeczy. Co do punktu trzeciego nie mam pewności, bo nie mam wglądu w&nbsp;algorytmy Facebooka, ale sam na ich miejscu bym coś takiego dodał. A&nbsp;dwie pierwsze rzeczy to pewniaki.  
Jeszcze obszerniejszą [listę trików Facebooka](https://www.eff.org/deeplinks/2018/04/facebook-doesnt-need-listen-through-your-microphone-serve-you-creepy-ads) stworzyła organizacja EFF.

A jeśli jesteśmy absolutnie przekonani, że ani my, ani rozmówca nie szukaliśmy rzeczy, o&nbsp;której rozmawialiśmy w&nbsp;towarzystwie swoich telefonów? **Możliwe, że nasza trafna reklama to po prostu przypadek**.

Każdemu się chyba zdarzyło pomyśleć o&nbsp;piosence, a&nbsp;chwilę później ją usłyszeć w&nbsp;odbiorniku. Albo spotkać kogoś znajomego w&nbsp;dużym mieście, z&nbsp;dala od naszych typowych rewirów. Niektórzy wygrywają w&nbsp;Lotto.

A my tutaj mamy znacznie węższą przestrzeń możliwości. Facebook już zna nasz ogólny profil zainteresowań, styl życia. Może nas zalewać reklamami rzeczy, które robili inni podobni ludzie.

Może nam się na przykład wydawać, że nasze zainteresowanie rzemiosłem -- pleceniem makram, pszczelarstwem, majsterkowaniem, drukiem 3D -- to nietypowe i&nbsp;fajne hobby.  
Ale Facebook, patrząc w&nbsp;skali świata, widzi wiele osób takich jak my -- znużonych trybikowaniem w&nbsp;korpo. Próbujących uciec w&nbsp;coś co naturalne, namacalne, fizyczne. Podrzucając rzeczy z&nbsp;tego spektrum, w&nbsp;końcu ugodzi nas celną reklamą.

Jako ludzie jesteśmy po prostu przewidywalni. Wiem że to trudne do zaakceptowania. Ale niestety bardziej prawdopodobne niż działanie złego mikrofonu :wink: 

## Jak się chronić

Wyżej rozpisałem się o&nbsp;tym, że giganci raczej nas nie podsłuchują, bo im się to nie opłaca. Ale na świecie jest wielu drobniejszych graczy, poza tym opłacalność może się zmieniać. Tak czy siak warto się chronić.

Pierwsze, proste rozwiązanie dla Androida -- **wyłączmy dostęp do mikrofonu wszystkim apkom**. Może nawet systemowym, jak aparat/kamera. Kiedy mikrofon będzie potrzebny, to po prostu udzielimy apce zgody. Pamiętając, żeby ją wycofać, kiedy już zrobimy swoje.

Nie ma wymówek -- to jeden szybki pstryczek w&nbsp;opcjach, a&nbsp;da nam mnóstwo komfortu.

Chcemy wrzucić filmik do *social mediów* albo komunikatora?  
To nagrajmy go domyślną systemową aplikacją, do pliku. A&nbsp;w cudzej apce wybierzmy opcję załadowania tego pliku. Większość powinna taką mieć.  
Nie korzystajmy z&nbsp;opcji nagrywania bezpośrednio przez komunikator, bo w&nbsp;ten sposób musimy dać mu dostęp do mikrofonu.

Jeśli ktoś mikrofonom zupełnie nie ufa, to może rozejrzeć się za urządzeniami zawierającymi *fizyczny* wyłącznik mikrofonu.  
Ich przykłady to telefony oparte na systemie Linux -- Pinephone i&nbsp;Librem. Ale ostrzegam, że na obecnym etapie są czymś bardziej dla zapaleńców i&nbsp;majsterkowiczów.

No i&nbsp;pamiętajmy, że mikrofony nie są aż takim zagrożeniem w&nbsp;przypadku legalnych, oficjalnych apek mobilnych -- bo ich twórcy po prostu mieliby zbyt wiele do stracenia.

Ale co, jeśli ta legalność, oficjalność lub choćby „apkowatość” zostanie jakoś naruszona? Wtedy już może się zrobić ciekawie. O&nbsp;tym w&nbsp;kolejnym wpisie :smile:

## Źródła obrazków

Piramida warstw systemu:

* Piramida Maslowa autorstwa *Androidmarsexpress* (ze zbiorów Wikimedia Commons, licencja [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0));
* ikona [procesora](https://www.flaticon.com/free-icon/cpu_984391) -- Flaticon, autorstwa Freepik.
* ikona [strzałek](https://www.flaticon.com/free-icon/transaction_7789028) -- Flaticon, autorstwa NextGen;
* ikona [mikrofonu](https://emojipedia.org/microphone/) -- emoji od JoyPixels;
* ikona [sygnału wi-fi](https://www.flaticon.com/free-icon/wifi_2099193) -- Flaticon, autorstwa Freepik;

Schemat przesyłania danych Mecie:

* ikona [uśmiechniętego drzewka decyzyjnego](https://www.flaticon.com/free-icons/decision-tree) -- Flaticon, autorstwa Freepik;
* nutki -- [Emojipedia](https://emojipedia.org/musical-notes/);
* ikona [kettlebella (ciężarka)](https://www.flaticon.com/free-icon/kettlebells_2265020?term=kettlebell&page=1&position=30&origin=search&related_id=2265020) -- Flaticon, autorstwa Amethyst Design.

Elementem wspólnym ikona Messengera oraz logo firmy Meta. Wszelkie przeróbki moje. 

