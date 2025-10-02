---
layout: post
title: "„Dowodzik proszę”. Wojna Google'a z niezależnymi aplikacjami?"
subtitle: "Kontrola imperium zaczyna sięgać wolnych terytoriów."
description: "Kontrola imperium zaczyna sięgać wolnych terytoriów."
date:   2025-10-02 18:00:34 +0100
tags: [Android, Apki, Centralizacja]
firmy: [Apple, Google]
category: google
category_readable: "Google – kolorowy czarny charakter"
image:
  path: /assets/posts/google/play-store-tozsamosc/google-sideloading-swiadoma-zgoda-baner.jpg
  width: 1200
  height: 700
  alt: "Przeróbka mema o świadomej zgodzie. Nad głową mężczyzny widać opcję „instaluj z tego źródła”, nad głową kobiety włączony pstryczek. Logo firmy Google unoszące się obok mówi „Nie”."
---

Od pewnego czasu nie dodaję wpisów na stronie głównej bloga. Nie oznacza to jednak spadku zainteresowania. Skupiam się po prostu na poradnikach dotyczących [pierwszych kroków](/tutorials/ventoy){:.internal} z&nbsp;systemem Linux (które w&nbsp;swoim czasie połączę w&nbsp;jeden większy).

Jest jednak pewna afera, dla której zrobiłem wyjątek i&nbsp;stworzyłem pełnoprawny wpis. Właśnie ten tutaj.

Oto koncern Google, kontrolujący system smartfonowy Android, chce wprowadzić **obowiązkową weryfikację tożsamości dla osób publikujących aplikacje**. Nie tylko w&nbsp;ich bazie Play Store, lecz również poza nią.  
Niebawem testy pilotażowe. Od 2026&nbsp;roku rozwiązanie ma wejść w&nbsp;wybranych krajach, zaś rok później na całym świecie.

Oficjalnym powodem -- jak to często w&nbsp;przypadku Google'a -- jest troska o&nbsp;bezpieczeństwo. Realnymi konsekwencjami -- również jak to u&nbsp;nich -- będzie zamykanie dotąd otwartych drzwi i&nbsp;zacieśnianie kontroli.

W tym wpisie opiszę sprawę, przybliżając przy okazji parę niuansów związanych z&nbsp;instalowaniem aplikacji na Androidzie.

Zapraszam!

{:.bigspace-before}
<img src="/assets/posts/google/play-store-tozsamosc/google-sideloading-swiadoma-zgoda-baner.jpg" alt="Przeróbka mema o&nbsp;świadomej zgodzie. Nad głową mężczyzny widać opcję „instaluj z&nbsp;tego źródła”, nad głową kobiety włączony pstryczek. Logo firmy Google unoszące się obok mówi „Nie”." />

{:.figcaption}
Źródła: [mem](https://imgflip.com/memegenerator/323520777/Consent-Jesus) o&nbsp;świadomej zgodzie, logo Google'a, elementy interfejsu Androida. Przeróbki moje.

## Spis treści

* [Wpływ Google'a na smartfony](#wpływ-googlea-na-smartfony)
* [Instalowanie aplikacji na Androidzie](#instalowanie-aplikacji-na-androidzie)
  * [Przez Google Play](#przez-google-play)
  * [Instalacja z&nbsp;innych źródeł](#instalacja-zinnych-źródeł)
  * [Co się zmieni](#co-się-zmieni)
* [„Chodzi o&nbsp;bezpieczeństwo”](#chodzi-obezpieczeństwo)
* [Kontrola w&nbsp;świecie protestów](#kontrola-wświecie-protestów)
* [Co można zrobić?](#co-można-zrobić)
  * [Nagłaśniać!](#nagłaśniać)
  * [Wyłączyć Usługi Google'a](#wyłączyć-usługi-googlea)
  * [Podczepić się pod inne aplikacje](#podczepić-się-pod-inne-aplikacje)

## Wpływ Google'a na smartfony

Idąc do każdego większego sklepu z&nbsp;elektroniką, można napotkać wiele smartfonów od różnych producentów. Xiaomi, Huawei, iPhone, OnePlus... Aż się może wydawać, że panuje zdrowa konkurencja i&nbsp;mamy bogaty wybór.

W rzeczywistości jednak ta galaktyka możliwości opiera się niemal wyłącznie *na skorupach czterech żółwi*{:.corr-del} na dwóch dominujących systemach operacyjnych. Jednym z&nbsp;nich jest Android, nad którym pieczę sprawuje Google. Drugi z&nbsp;nich to iOS, obecny na iPhone'ach, czyli smartfonach firmy Apple.

Jabłkofony od Apple od zawsze mocniej ograniczały możliwości użytkowników (jeszcze do tego wrócę), są natomiast całkiem poza kontrolą Google'a. Dlatego planowane zmiany kompletnie ich nie dotyczą.

Android jest z&nbsp;kolei systemem dużo popularniejszym na świecie. Popularność tę zyskał w&nbsp;dużej mierze dzięki swojej otwartości -- jego kod źródłowy jest darmowy i&nbsp;publicznie dostępny, jako tzw. [AOSP (_Android Open Source Project_)](https://source.android.com/). Producenci smartfonów mogą tworzyć na jego bazie własne systemy.

{:.post-meta .bigspace-after}
Otwarty Android jest niestety coraz mniej przydatny dla małych twórców, zwłaszcza że stopniowo usuwane są z&nbsp;niego funkcje, jak np. podstawowe apki od dzwonienia i&nbsp;kontaktów. Ale to osobna historia.

Można znaleźć smartfony, których domyślny system jest wprawdzie oparty na kodzie Androida, ale poza tym nie korzystają z&nbsp;rzeczy od Google'a. To na przykład prywatnościowe smartfony od Mureny.  
Ciekawym przypadkiem jest Huawei. Wielkie korpo, które jednak ze względu na sankcje było zmuszone odciąć się od Google'a. Ich nowsze smartfony zawierają już ich własny, autorski [system](https://en.wikipedia.org/wiki/HarmonyOS), ale wszystkie poprzednie edycje to Android  bez usług Google'a.

Wspomniane przypadki „Androida bez Google'a” (z&nbsp;wyboru albo przymusu) również nie powinny zostać dotknięte zmianami. Jest to jednak mniejszość w&nbsp;smartfonowym świecie.

Producenci wiedzą, że ludzie przywykli do obecności Google'a i&nbsp;sami dążą do tego, żeby mieć na swoich smartfonach domyślnie zainstalowane apki od giganta. W&nbsp;tym celu podpisują umowy, stając się tzw. **certyfikowanymi partnerami Google'a**. 

To właśnie smartfony od tych producentów dotknie planowana zmiana. I&nbsp;to niestety znaczna większość urządzeń dostępnych w&nbsp;sklepach. Na [oficjalnej liście](https://www.android.com/certified/partners/#tab-panel-brands) znajdziemy: Samsunga, Xiaomi, Motorolę, Oppo, OnePlusa, Nokię, Fairphone'a...

Podsumowując: **zmiany dotkną większości smartfonów z&nbsp;Androidem**, a&nbsp;zatem większości smartfonów na świecie. A&nbsp;jakie to zmiany?

## Instalowanie aplikacji na Androidzie

Dla lepszego zrozumienia tematu przyda nam się parę podstawowych faktów na ten temat instalowania aplikacji na Androidzie. Dlatego już je serwuję.

### Przez Google Play

Dla niektórych osób instalacja na Androidzie opiera się na tym, że odwiedzają jakąś stronę internetową i&nbsp;znajdują tam takie dwa guziki:

{:.figure .bigspace}
<img src="/assets/posts/google/play-store-tozsamosc/play-store-app-store.png" alt="Przyciski z&nbsp;linkami do baz Play Store oraz App Store." />

Mając Androida, stuka się w&nbsp;przycisk z&nbsp;*Google Play*. W&nbsp;tym momencie uruchamia się aplikacja o&nbsp;tej samej nazwie, zainstalowana domyślnie na telefonie. Jeśli ktoś nie ma jej podpiętej do konta Google, to **pojawia się wymóg zalogowania**. Google będzie dokładnie widział, jakie apki sprawdza i&nbsp;pobiera konkretna osoba.

Po zalogowaniu następuje połączenie ze Sklepem Play (ang. *Play Store*), czyli wielką bazą aplikacji kontrolowaną przez Google'a. Ładuje się strona odpowiadającą tej konkretnej apce, która odesłała w&nbsp;to miejsce.

Na tej stronie wyróżnia się przycisk pozwalający zainstalować apkę.  
Stuknięcie palcem, wyrażenie zgód (których niektórzy niestety nie czytają uważnie), chwila czekania -- po czym ikona nowej aplikacji pojawia się na ekranie smartfona. Można z&nbsp;niej korzystać.

### Instalacja z&nbsp;innych źródeł

Wiele stron, zwłaszcza dużych, umieszcza u&nbsp;siebie jedynie odsyłacz do Play Store'a. Można przez to odnieść wrażenie, że to jedyny sposób na zdobywanie aplikacji na Androidzie.  
Ale to nieprawda. W&nbsp;rzeczywistości **Play Store jest ułatwieniem, ale nie koniecznością**.

Tak naprawdę instalacja polega w&nbsp;uproszczeniu na:

1. pobraniu pliku APK,
2. instalacji tego pliku przez system.

{:.post-meta .bigspace-after}
Pomijam tu pakiety, czyli tzw. *APK bundles*, z&nbsp;którymi jest ciut więcej zachodu, ale reguła podobna.

Play Store odpowiada za krok 1, ale potem odsuwa się w&nbsp;cień i&nbsp;zostawia główną robotę systemowi. Nie ma tu żadnej magii, którą tylko apka od Google'a mogłaby wykonać i&nbsp;którą strach powierzać innym.

Równie dobrze ktoś mógłby użyć alternatywnego sklepu/źródła, takiego jak [F-Droid](https://f-droid.org/). Działa w&nbsp;bardzo podobny sposób jak Play Store.

Dałoby się też osobiście pobrać plik APK z&nbsp;internetu (oczywiście sprawdzając reputację źródła). Jak na przykład ten [ze strony komunikatora Signal](https://signal.org/android/apk/). Albo nawet: pobrać ten plik na komputer, a&nbsp;stamtąd zrzucić przez kabelek na smartfona.  
Po otwarciu smartfonowej przeglądarki plików można go odnaleźć i&nbsp;kliknąć. System spyta, czy chcemy go zainstalować. Jeśli się zgodzimy, to apka trafi po chwili na ekran główny.

W każdym z&nbsp;tych przypadków wyświetli się **pytanie, czy chcemy instalować aplikację z&nbsp;nieużywanego wcześniej źródła**. Wystarczy raz, na początku, wyrazić zgodę.

{% include info.html
type="Analogia"
text="Play Store jest jak usługa transportu materiałów. Popularna, ale wykonywana przez wścibskiego kierowcę. 
Można je również zdobyć na własną rękę.  
Na miejscu u&nbsp;nas czeka majster-instalator. Jeśli widzi, że sami dowieźliśmy, to jedynie pyta, czy jakość będzie dobra. Gdy się potwierdzi, to bierze się do pracy."
%}

Niektórzy nazywają instalację z&nbsp;innych źródeł niż Play Store **_sideloadingiem_**. Uważam tę nazwę za niefortunną, bo to w&nbsp;dosłownym tłumaczeniu „ładowanie od boku”. Lekkie skojarzenie z&nbsp;jakimś obejściem, kombinowaniem, skradaniem.

A to przecież po prostu klasyczna, zwykła *instalacja*. Tak, jak się to od wielu lat robiło, nawet na poważnym byznesowym systemie Windows. Nie ma w&nbsp;tym żadnej pokątności.  
Powiem więcej -- to taki prawdziwy, czysty sposób, gdzie jest tylko instalator i&nbsp;system, bez polegania na kontach, łączności i&nbsp;firmie-pośredniku. Mogliby go nazywać *trueloadingiem*.

{:.bigspace-before}
<img src="/assets/posts/google/play-store-tozsamosc/fullmetal-alchemist-from-the-front.jpg" alt="Kolaż z&nbsp;mangi Fullmetal Alchemist. Pokazuje postać stojącą na wprost schodów i&nbsp;bramy, mówiącą że król nie wchodzi do swojego zamku tylnymi drzwiami. Obok widać salutujących żołnierzy." />

{:.figcaption}
Źródło: Hiromu Arakawa, *Fullmetal Alchemist*, rozdział 97. Tłumaczenie fanowskie grupy *Franky House*. Aranżacja moja.

Dotąd publikacja apek poza Play Store'em była równie łatwa jak ich instalacja. Twórcy mogli po prostu stworzyć plik APK i&nbsp;go umieścić na swojej stronie internetowej. Ale to ma się zmienić, bo Google planuje wymagać od *wszystkich* twórców weryfikacji tożsamości. 

### Co się zmieni

Choć plany Google'a jeszcze nie całkiem się skrystalizowały, opublikowali właśnie [więcej szczegółów](https://www.androidauthority.com/how-android-app-verification-works-3603559/) na temat nowego trybu instalacji.

**Z punktu widzenia użytkowników**:

* W&nbsp;momencie próby zainstalowania aplikacji (również spoza Play Store'a) nastąpi sprawdzenie, czy jej twórcy są na liście zweryfikowanych.

  Ta lista siłą rzeczy będzie dynamiczna, bo aplikacji stale przybywa. Dlatego, o&nbsp;ile nie trafimy na apkę z&nbsp;listy popularnych, na tym etapie nastąpi kontakt z&nbsp;zewnętrznym serwerem. Instalacja **może nie działać w&nbsp;przypadku braku internetu**.

* Jeśli aplikacji nie będzie na liście, to użytkownicy zobaczą informację w&nbsp;stylu: 

  > Uwaga! Próbujesz zainstalować aplikację od niezweryfikowanego twórcy

Czy ostrzeżenie będzie możliwe do łatwego przeklikania (tak jak wspomniany wcześniej komunikat o&nbsp;instalacji z&nbsp;nieznanego źródła)? A&nbsp;może będzie barierą nie do obejścia?

Gdzie zostanie upchnięty program odpowiedzialny za weryfikację? W&nbsp;samym Androidzie, w&nbsp;Usługach Google (aplikacji zrośniętej z&nbsp;systemem), a&nbsp;może tu i&nbsp;tu? 

Nie znam niestety odpowiedzi na te pytania. W&nbsp;najnowszym artykule ich nie znalazłem, możliwe że sam Google dopiero to dopracowuje.

Zwrócę natomiast uwagę na podpunkt pierwszy. Niezależnie od szczegółów technicznych, prawie na pewno gdzieś pojawi się funkcja, która **najpierw coś sprawdza u&nbsp;Google'a, a&nbsp;potem zwraca odpowiedź pozytywną/negatywną**.

A to może tworzyć niebezpieczny precedens. Choć formalnie rzeczą sprawdzaną ma być „czy twórca tej apki potwierdził tożsamość?”, to Google mógłby z&nbsp;czasem rozszerzać kryteria, tworząc *de facto* listę aplikacji zakazanych.

**Z punktu widzenia twórców** pojawi się z&nbsp;kolei obowiązek zarejestrowania się na platformie, którą Google w&nbsp;tym celu stworzył (o&nbsp;ile jeszcze nie są zarejestrowani w&nbsp;głównym Play Storze).

{:.post-meta .bigspace-after}
Hobbyści dostali niby możliwość rozpowszechniania apek osobnym kanałem, ale musieliby ręcznie zatwierdzać każde urządzenie, które chce zainstalować ich apkę. Jest to więc skrajnie niepraktyczne, a&nbsp;większość zostanie zepchnięta w&nbsp;stronę głównej platformy.

W ramach weryfikacji będzie trzeba podesłać [szereg rzeczy](https://support.google.com/googleplay/android-developer/answer/15633622?hl=en), w&nbsp;tym adres mailowy, numer telefonu i&nbsp;zapewne zdjęcie dokumentu tożsamości. W&nbsp;przypadku organizacji -- jakieś inne potwierdzenie, że to my jej szefujemy.

Bez wykonania tych kroków nie trafi się do bazy zweryfikowanych apek. A&nbsp;to oznacza wspomniany wyżej komunikat i&nbsp;dalsze, nieokreślone jeszcze utrudnienia.

## „Chodzi o&nbsp;bezpieczeństwo”

Na chwilę oddam głos drugiej stronie. Google twierdzi, że wprowadza zmiany z&nbsp;tego względu, że ludzie często instalują apki z&nbsp;nieznanych źródeł, trafiając na złośliwe podróbki i&nbsp;tracąc pieniądze. Wymóg zgłaszania tożsamości przez twórców aplikacji ma temu rzekomo zapobiec.

{:.figure .bigspace-before}
<img src="/assets/posts/google/play-store-tozsamosc/android-korpobelkot.png" alt="Zrzut ekranu pokazujący nagłówek ze strony Androida, mówiący po angielsku: 'Wzmacnianie zabezpieczeń na Androidzie, żeby pozostał otwarty i&nbsp;bezpieczny'." />

{:.figcaption}
Źródło: [oficjalny komunikat Google'a](https://developer.android.com/developer-verification).  
Jak to zawsze u&nbsp;nich: „to dla twojego dobra”. „Będziesz bezpieczny i&nbsp;szczęśliwy”.

Gdyby jednak bliżej się temu przyjrzeć, cała argumentacja pada na pysk.

Po pierwsze: **weryfikacja Play Store'a nie jest niezawodna** i&nbsp;już się zdarzało, że ludzie pobierali tym oficjalnym kanałem jawne oszustwa. Mimo że wszyscy twórcy publikujący tam apki *już teraz* muszą weryfikować tożsamość.  
Przykładowo: 331&nbsp;złośliwych aplikacji [pobranych kilkadziesiąt milionów razy](https://www.forbes.com/sites/daveywinder/2025/03/18/60-million-malicious-google-play-downloads-as-331-apps-bypass-security/) z&nbsp;oficjalnego Play Store'a. Historia z&nbsp;marca, więc nie jest żadną ripostą na nowe plany Google'a. Taka jest po prostu rzeczywistość w&nbsp;ich bazie.

{:.post-meta .bigspace-after}
A mowa tu o&nbsp;jawnych wirusach i&nbsp;oszustwach; pomijam przypadki, gdy przykładowo elementy reklamowe w&nbsp;oficjalnych, popularnych apkach wysyłały obcym firmom [dokładne dane o&nbsp;lokalizacji](/2025/03/23/gravy-analytics-wyciek){:.internal}.

Po drugie: istnieją bezpieczniejsze źródła, którym ta zmiana dokopie.  
Wspomniany już F-Droid ma znacznie mniej aplikacji niż Play Store. Jest natomiast dużo bardziej wybredny -- dopuszcza tylko otwarty kod źródłowy, z&nbsp;którego buduje apki po swojej stronie, analizując je ponadto pod kątem ewentualnych naruszeń.

{% include info.html
type="Anegdotka"
text="Podejście F-Droida sprawdziło się w praktyce.  
Kiedy aplikacje z&nbsp;serii Simple Mobile Tools zostały cichaczem przejęte przez firmę reklamową i&nbsp;wzbogacone o&nbsp;elementy zbierające dane, to Play Store radośnie przyjął aktualizację (bo dla Google'a inwazyjne reklamy śledzące nie zaliczają się do złośliwych).  
F-Droid z kolei ją [zablokował](https://forum.f-droid.org/t/simple-mobile-apps-update/24384), a&nbsp;ostatnią dostępną u&nbsp;nich wersją jest ta sprzed zmian na gorsze."
%}

...A teraz w&nbsp;ten niezależny, działający ekosystem wbija się Google. Olewa to, że bezpieczeństwo jest większe niż u&nbsp;nich i&nbsp;forsuje wymóg weryfikacji tożsamości. A&nbsp;to może się nie spodobać wielu niezależnym autorom, którzy cenią anonimowość i&nbsp;nie lubią wielkich monopolistów (zwłaszcza [z wyrokami](/google/2024/08/07/google-antymonopol-wyrok){:.internal}, jak Google).

F-Droid odniósł się [bardzo krytycznie](https://f-droid.org/2025/09/29/google-developer-registration-decree.html) do planowanych zmian, przywołując jeszcze więcej przykładów słabości Play Store'a i&nbsp;tego, że tak naprawdę Google już ma wystarczająco narzędzi do walki ze złymi aplikacjami (w&nbsp;tym możliwość ich usuwania po instalacji -- Play Protect).

Po trzecie: półświatek naprawdę nie ma problemu ze znalezieniem jakiegoś spłukanego nieszczęśnika, który zgodzi się zostać słupem. Poświadczy za aplikację własną tożsamością, apka zacznie przechodzić weryfikację i&nbsp;naciągnie ludzi na kasę. Nawet jeśli policja dorwie słupa, mocodawcy się zwiną z&nbsp;zarobionymi pieniędzmi.

{:.post-meta .bigspace-after}
Pomijając już fakt, że wtedy Google mógłby spojrzeć na statystyki, ogłosić „tam nadal jest wiele oszukańczych aplikacji!” i&nbsp;zacieśnić kontrolę jeszcze bardziej. Na przykład przez zastąpienie „listy apek znanych twórców” swoją subiektywną „listą apek zaakceptowanych”.

## Kontrola w&nbsp;świecie protestów

Patrząc na kraje, w&nbsp;których za rok Google chce wprowadzić nowe ograniczenia (w&nbsp;ramach pilotażu), trudno nie powiedzieć sobie pod nosem: „niezłą ekipę żeście zmontowali”. To Brazylia, Indonezja, Singapur i&nbsp;Tajlandia.

Oficjalna logika jest taka, że w&nbsp;tych krajach ludzie dość często są oszukiwani, instalując apki z&nbsp;szemranych źródeł. Ale dziwnym trafem łączy je coś jeszcze -- szukając w&nbsp;DuckDuckGo pod hasłem `{nazwa_kraju} protests`, można trafić na dość dystopijne opowieści.

W Brazylii właśnie trwają [wielkie protesty](https://theweek.com/world-news/brazil-bolsonaro-bandit-bill-protest) przeciw ustawie zwanej *bandit bill*, która pozwoliłaby uniknąć odpowiedzialności watażce, który zorganizował przewrót po przegranych wyborach. Wcześniej miały też miejsce protesty [przeciw blokadzie X/Twittera](https://apnews.com/article/brazil-musk-x-moraes-bolsonaro-sao-paulo-protest-demonstration-e8f4ed59ec397aed9810d058af8dbc0c).

W Tajlandii niedawno miały miejsce [protesty przeciw ichniejszej premierce](https://www.reuters.com/world/asia-pacific/thai-protesters-call-prime-minister-paetongtarns-resignation-2025-06-28/), kiedy wyszło na jaw, że dogadywała się z&nbsp;byłym przywódcą Kambodży, zachowując przy tym dość poddańczy ton i&nbsp;wyzywając krajowych dowódców wojskowych.

Protesty w&nbsp;Indonezji trwają [od wielu miesięcy](https://en.wikipedia.org/wiki/2025_Indonesian_protests), natomiast w&nbsp;ostatnim czasie doszło do ich [nasilenia](https://edition.cnn.com/2025/09/01/asia/indonesia-protests-explainer-intl-hnk) po tym, jak jednego z&nbsp;protestujących rozjechano opancerzonym samochodem. Od tego czasu ofiar tylko przybyło.

Nic nie znalazłem o&nbsp;większych protestach w&nbsp;Singapurze, ale może to dlatego, że [ściśle kontrolują obywateli](https://monitor.civicus.org/explore/singapore-government-continues-its-crackdown-on-anti-death-penalty-activism-and-other-forms-of-expression/), wymagając między innymi policyjnej zgody *nawet na pokojowe protesty*. Tegoroczne, przeciw karze śmierci, po prostu skutecznie wygasili.

Przypadkowy dobór krajów? Możliwe; obecnie mamy ciekawe czasy, a&nbsp;protestów na świecie niemało. Ale warto spojrzeć, co mogą spowodować działania Google'a w&nbsp;takich realiach.

{:.post-meta .bigspace-after}
Łączenie spraw aplikacji z&nbsp;protestami nie jest jakimś moim skojarzeniem z&nbsp;czapy; niebawem przytoczę historię z&nbsp;Hongkongu. 

{% include info.html
type="Ciekawostka"
text="Jednym z&nbsp;symboli walki, w&nbsp;Indonezji i&nbsp;nie tylko, jest piracka flaga z&nbsp;mangi i&nbsp;anime *One Piece* -- bodaj najpopularniejszej japońskiej serii na świecie. Patrząc pobieżnie, jest to przygodowa opowieść o&nbsp;piratach. Ale im dalej w&nbsp;las, tym wyraźniej pokazuje aluzje do stanu świata i&nbsp;walkę wolności z&nbsp;kontrolą.  
Paru indonezyjskim politykom nie spodobało się wywieszanie flag i&nbsp;publicznie [nazwali to zdradą stanu](https://animehunch.com/public-display-of-one-pieces-straw-hat-flag-labelled-treason-by-indonesian-government/). Gdyby powstała apka dająca protestującym możliwość koordynacji -- może nawet z&nbsp;ikonką tej flagi -- to ci sami politycy raczej by się nie zawahali przed pisaniem do Google'a, żeby ją ubił wszelkimi możliwymi sposobami."
trailer="<p class='figure bigspace-before'><img src='/assets/posts/google/play-store-tozsamosc/indonezja-flaga-one-piece.jpg' alt='Fragment zdjęcia pokazujący flagę z&nbsp;trupią czaszką w&nbsp;słomianym kapeluszu przyczepioną do tira'/></p>
<p class='figcaption nospace'>Źródło: <a href='https://en.wikipedia.org/wiki/Straw_Hat_Pirates%27_Jolly_Roger'>Wikipedia</a></p>"
%}

Wyobraźmy sobie, że jakaś osoba z&nbsp;kraju dotkniętego protestami, która umie programować, czuje rewolucyjny zryw. I&nbsp;myśli o&nbsp;publikacji apki, którą wrzuci na znane forum, żeby ułatwić koordynację i&nbsp;działania przeciw skorumpowanej władzy.

Ale w&nbsp;tym momencie widzi, że musi ujawnić swoją tożsamość Google'owi. I&nbsp;ta myśl działa jak kubeł zimnej wody. Rząd na pewno zwróci się do Google'a o&nbsp;ujawnienie danych. Co, jeśli je udostępnią? Ostatecznie apka nie powstaje.

Takich przypadków raczej nie znajdziemy w&nbsp;statystykach. To **efekt mrożący**, sprawiający że ludzie nie działają w&nbsp;słusznej sprawie, widząc nieuchronność konsekwencji. Podobny patologiczny efekt ma w&nbsp;życiu publicznym [groźba oberwania pozwem](/corponomicon/2025/03/17/slapp-efekt-mrozacy){:.internal}.

Ten efekt zachodziłby nawet w&nbsp;przypadku, gdyby Google zachował faktyczną neutralność i&nbsp;tylko wymagał weryfikacji, nie usuwając żadnych aplikacji na żądanie.

### Czym grozi pełna kontrola? Kazus Apple

A co by było, gdyby spełniła się moja główna obawa, czyli przekształcenie listy twórców zweryfikowanych w&nbsp;subiektywną listę dopuszczonych?

Wspomniałem na początku, że system iOS od Apple, w&nbsp;przeciwieństwie do Androida, stawiał na ograniczanie możliwości użytkowników. I&nbsp;choć sama kontrola budzi moje negatywne uczucia, to trzeba przyznać, że dostarczyła ciekawych historii ku przestrodze.

Przykładem usunięcie [mapy z&nbsp;oznaczeniami zgonów](https://www.cnet.com/tech/services-and-software/apple-removes-iphone-app-that-reports-us-drone-strikes/) spowodowanych przez ataki amerykańskich dronów.  
Na początku nazywała się *Drone+*, potem nazwę zmieniono na *Metadata+* -- zapewne aluzja do hasła [„zabijamy ludzi na podstawie metadanych”](https://www.justsecurity.org/10311/michael-hayden-kill-people-based-metadata/). Autorem był dziennikarz pracujący dla *Intercepta*, dane pochodziły ze zbioru *Bureau of Investigative Journalism* -- zatem rzetelne dziennikarstwo śledcze, a&nbsp;nie jakaś propaganda przeciw USA.

A jednak apka została usunięta przez Apple z&nbsp;bazy App Store. A&nbsp;że to jedyny sposób rozpowszechniania aplikacji na ich smartfonach -- to zniknęła dla wszystkich użytkowników.

Inny przykład, bliższy tematyce sprzed chwili? Kiedyś Apple [usunęło aplikację](https://www.komputerswiat.pl/aktualnosci/inne/apple-wycofuje-aplikacje-zwiazana-z-protestami-w-hong-kongu/zte0lc6), której używały rzesze osób protestujących w&nbsp;Hongkongu do dzielenia się informacjami o&nbsp;położeniu policji.

W archiwalnych materiałach widać, jak niektórzy protestujący walczyli o&nbsp;swoje (niby przeciw lokalnym władzom, ale w&nbsp;praktyce przeciw Chinom). Prosili świat o&nbsp;pomoc, wielu machało amerykańskimi flagami. Nie miało to jednak znaczenia, świat milczał. Zaś Apple usunęło apkę. W&nbsp;jednej chwili stała się niedostępna dla protestujących ajfoniarzy.

Obecnie, gdy trwa spór USA z&nbsp;Chinami, można się zastanowić. Czy z&nbsp;takiej perspektywy działanie Apple -- sabotowanie ruchów wyzwoleńczych we wrogim reżimie -- nie zakrawa o&nbsp;zdradę interesu amerykańskiego? Obawiam się jednak, że to pytanie retoryczne, a&nbsp;na karę czy upomnienie giganta nie ma co liczyć.

{:.post-meta .bigspace-after}
Nie jest to zresztą pierwszy raz, gdy Apple [idzie na rękę rządowi Chin](https://applecensorship.com/news/banned-apps-in-china-are-apps-at-risk-in-hong-kong) i&nbsp;blokuje co zechcą.

To tylko kilka przykładów, ale pokazują, do czego jest zdolna firma mogąca gasić apki jednym pstryknięciem. Nowy wymóg sprawdzania tożsamości też może z&nbsp;czasem doprowadzić do oddania takiej kontroli w&nbsp;ręce Google'a.

## Co można zrobić?

### Nagłaśniać!

Przede wszystkim -- **protestujmy głośno przeciw zmianom**. Nawet jeśli sprawa tu i&nbsp;teraz nie dotyczy aplikacji, z&nbsp;których korzystamy, może stać się furtką do wpychania nowych zmian, szkodliwych dla ekosystemu spoza oficjalnego Play Store'a.  
Można podkreślać, że Android zyskał obecną pozycję dzięki otwartości, a&nbsp;zatem odchodzenie od niej jest oszukaniem wszystkich użytkowników i&nbsp;twórców aplikacji.

Zauważyłem, że światek komputerowy lubi czasem spoczywać na laurach, gdy widzi techniczne obejścia problemu. „Aaa, jeśli zrobią mi na złość, to *zrootuję* telefon”.  
Ale wydaje mi się to niepraktyczne. To trochę tak, jakby z&nbsp;własnego wyboru dawać się kopać zbirowi w&nbsp;alejce. Myśląc sobie: „Jestem mistrzem swojego ciała. Tu zablokuję ramieniem. A&nbsp;tu rozluźnię ciało w&nbsp;momencie uderzenia, nie odczuję. To dla mnie nic”.

No i&nbsp;fajnie. Tyle że napastnik może w&nbsp;końcu wyjąć nóż i&nbsp;żadna duma z&nbsp;własnych technicznych umiejętności wtedy nie pomoże. A&nbsp;od początku dało się wezwać pomoc.  
Dlatego w&nbsp;pierwszej kolejności stawiałbym na informowanie. Można nagłaśniać sprawę w&nbsp;mediach społecznościowych, oznaczając polityków i&nbsp;organizacje.

Jeśli ktoś umie po angielsku, to może [zwrócić się](https://digital-markets-act.ec.europa.eu/contact-dma-team_en) do zespołu odpowiedzialnego za europejską *Ustawę o&nbsp;rynkach cyfrowych (DMA)*. Te przepisy z&nbsp;założenia uderzają w&nbsp;gigantów i&nbsp;centralizację, więc ich twórcy nie powinni się bać Google'a.

Poniżej tak czy siak dodam parę technicznych obejść na wypadek, gdyby świat zaczął się domykać. Można już teraz przećwiczyć sobie parę działań.

### Wyłączyć Usługi Google'a

Zmiana ma dotknąć oficjalnych partnerów, a&nbsp;zatem smartfonów z&nbsp;domyślnie zainstalowanymi apkami Google'a. A&nbsp;to sugeruje, że kod odpowiedzialny za weryfikację mógłby się ukrywać wewnątrz aplikacji o&nbsp;nazwie Usługi Google Play.

{:.post-meta .bigspace-after}
Nie mam pewności, czy tak będzie; nie znalazłem tej informacji nawet w&nbsp;nowych obwieszczeniach, a&nbsp;sprawa się wciąż klaruje.

Choć Usługi wydają się czymś niemalże systemowym (domyślnie zainstalowane, ingerujące w&nbsp;wiele procesów), mimo wszystko pozostają aplikacją. [Można je wyłączyć](/2024/02/03/smartfon-degoogle#fina%C5%82owy-boss--us%C5%82ugi-google-play){:.internal} (a&nbsp;w razie czego włączyć ponownie).

A czy po wyłączeniu Usług niezależna aplikacja zostanie tak po prostu zainstalowana? Czy też pozostanie zablokowana na głębszym, systemowym poziomie?  
Tego jeszcze nie wiem, na dwoje babka wróżyła. Ale gdyby brak Usług oznaczał brak weryfikacji, to można spróbować to zrobić.

{% include info.html
type="Uwaga"
text="Wyłączenie Usług sprawi, że zaczną wyświetlać się liczne powiadomienia „aplikacja X&nbsp;wymaga Usług Google Play”.  
Niektóre z&nbsp;nich to straszaki -- treść komunikatu jest automatycznie tworzona przez system i&nbsp;niekoniecznie odpowiada rzeczywistości, zaś apka działa. Tak jest z&nbsp;Tricountem (do rozliczeń pieniężnych w&nbsp;grupach) i&nbsp;pewną apką od transportu, której nie wspomnę z&nbsp;nazwy. Swego czasu nawet [mObywatel](/cyfrowy_feudalizm/2025/06/05/mobywatel-problemy){:.internal} śmigał mi po wyłączeniu Usług."
trailer="<p class='bigspace-before'>Wciąż jednak pozostaje trochę aplikacji, które faktycznie bez Usług nie ruszą. Dlatego ich wyłączanie to kwestia bardzo indywidualna i&nbsp;trzeba sobie osobiście odpowiedzieć na pytanie, czy jesteśmy na to gotowi.</p>"
%}

### Podczepić się pod inne aplikacje

Jeśli system nie dopuści czyjejś niezależnej aplikacji, to można zamiast tego podczepić się pod istniejącą, ogólniejszego przeznaczenia, której twórca przeszedł weryfikację i&nbsp;która umożliwia ładowanie danych z&nbsp;zewnątrz. Możliwości jest wiele, omówię tu kilka.

Można postawić na **stronę internetową** otwieraną w&nbsp;przeglądarce. Obecnie przeglądarki są trochę jak małe systemy operacyjne i&nbsp;dają dostęp do wielu funkcji systemu. Ma to sporo możliwych wad [od strony prywatności](/serie/internetowa_inwigilacja/){:.internal}, ale akurat do zastępowania smartfonowych aplikacji by się przydało.

{% include info.html
type="Ciekawostka"
text="Czasem można nawet używać takich stron-apek bez internetu.  
Przykładowo stronkę [*hat.sh*](/tutorials/hat-sh-szyfrowanie){:.internal}, zawierającą prosty i&nbsp;skuteczny szyfrator/deszyfrator, można zapisać dodatkiem SingleFile do pojedynczego pliku działającego bez łączności z&nbsp;siecią.  
Do jego otwarcia potrzeba jedynie przeglądarki zdolnej ładować pliki z&nbsp;„dysku” smartfona (co niestety wyklucza Firefoksa) i&nbsp;obsługującej JavaScript (co wyklucza uproszczony podgląd Androida)."
%}

W podobny sposób, chcąc podzielić się trasami i&nbsp;ważnymi punktami na mapie, można postawić na **pliki GPX**. To uniwersalny standard. Takie pliki można na przykład [załadować w&nbsp;apce Organic Maps](https://organicmaps.app/news/2023-06-07/gpx-import-is-now-supported-in-organic-maps/) (otwartoźródłowej, działającej offline po pobraniu map) i&nbsp;zyskać w&nbsp;ten sposób mapę dopasowaną do swoich potrzeb.

Rozwiązaniem nieco bardziej technicznym -- ale i&nbsp;wszechstronnym -- jest [Termux](/tutorials/termux){:.internal}. To w&nbsp;skrócie konsola, w&nbsp;której można uruchamiać programy w&nbsp;wielu znanych językach, a&nbsp;także (po instalacji dodatkowego modułu) zyskać dostęp do funkcji smartfona, takich jak GPS czy schowek.

Sam Termux raczej nie zostanie tak łatwo zablokowany, bo ma zweryfikowanego twórcę, a&nbsp;do tego jest powszechnie używany na świecie. A&nbsp;przy odrobinie kreatywności można odtworzyć wewnątrz niego -- przez jakieś skrypty Pythona itp. -- możliwości niemal każdej dostępnej aplikacji.

{:.post-meta .bigspace-after}
Da się nawet obejść ograniczenia domyślnego, minimalistycznego interfejsu tekstowego, instalując [środowisko graficzne](https://wiki.termux.com/wiki/Graphical_Environment).

To tyle z pomysłów, mam nadzieję że nie będą w przyszłości potrzebne. Póki co życzę nam wszystkim powodzenia w&nbsp;starciu z&nbsp;coraz to nowymi pomysłami diabolicznego Wujka G. :metal:


