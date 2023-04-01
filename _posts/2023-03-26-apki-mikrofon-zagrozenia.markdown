---
layout: post
title:  "Apki to pułapki 5 – groźniejsze mikrofony"
subtitle: "Zdradzanie szeptem naszych tajemnic."
description: "Zdradzanie szeptem naszych tajemnic."
date:   2023-03-26 21:21:21 +0100
tags: [Apki, Hardware, Inwigilacja]
firmy: [Amazon, Google]
category: apki
category_readable: "Apki to pułapki"
image:
  path: /assets/posts/apki/mikrofony/mikrofony-baner.jpg
  width: 1200
  height: 700
  alt: "Kolaż. Po lewej stronie fragment kobiecych ust i dłoń trzymająca żółty mikrofon. Po prawej stronie inna kobieta, w stylu komiksowym, nasłuchująca za pomocą szklanki. W tle widać niebieski obraz fali dźwiękowej, a za nią emotę małpki zasłaniającej uszy"

---

{:.bigspace-before}
<img src="/assets/posts/apki/mikrofony/mikrofony-baner.jpg" alt="Kolaż złożony z&nbsp;kilku elementów. Po lewej stronie widać fragment kobiecych ust i&nbsp;dłoń trzymającą żółty mikrofon. Widać, że to zdjęcie prawdziwej postaci. Po prawej widać rysunkową postać nasłuchującą za pomocą szklanki. W&nbsp;tle widać niebieską falę dźwiękową z&nbsp;wyraźną poziomą linią pośrodku. Zza fali wygląda emotka uśmiechniętej małpy zakrywającej dłońmi uszy."/>

{:.figcaption}
Na mikrofonie Tarja Turunen, pierwsza wokalistka Nightwisha :metal:  
Źródła obrazków: nagranie koncertu, Emojipedia, [WikiHow](https://www.wikihow.com/Hear-Through-Walls).

To mój drugi wpis na temat wykorzystania mikrofonów przez aplikacje. Ten [poprzedni]({% post_url 2023-02-15-apki-mikrofon-mity %}){:.internal}, jak na standardy tego bloga, był dość łagodny dla wielkich firm.

Pokazywałem różne argumenty za tym, że apki od Facebooka raczej nie nagrywają mikrofonem w&nbsp;telefonie naszych rozmów.  
Pozwoliłem sobie nawet napisać, że raczej nie robią tego *żadni wielcy gracze*. Za dużo do stracenia, za mało do zyskania.

Ale teraz koniec sielanki.

Poza Facebookiem i&nbsp;spółką mamy też graczy skłonnych do ryzyka, mniej spętanych przepisami. Niektóre rzeczy są lepiej przystosowane do nasłuchiwania niż mobilne apki. Zaś mikrofony mogą słuchać innych rzeczy niż nasz głos.

Ten wpis składa się z dwóch głównych, raczej niezależnych części. W&nbsp;pierwszej obalę parę założeń, na których dotąd opierała się nasza ochrona przed podsłuchem.  
A potem pokażę coś mało znanego, a&nbsp;mrożącego krew w&nbsp;żyłach -- **wykorzystanie niesłyszalnych dźwięków do lokalizowania i&nbsp;rozpoznawania użytkowników**.

### Spis treści

* [Luzujemy założenia](#luzujemy-założenia)
  * [Gdy aplikacje mają większą władzę](#gdy-aplikacje-mają-większą-władzę)
  * [Gdy przeciwnik nie przejmuje się prawem](#gdy-przeciwnik-nie-przejmuje-się-prawem)
  * [Gdy przetwarzanie dźwięku jest łatwe](#gdy-przetwarzanie-dźwięku-jest-łatwe)
* [Szpiedzy podchodzą po cichu](#szpiedzy-podchodzą-po-cichu)
  * [Słyszalność i&nbsp;ultradźwięki](#słyszalność-iultradźwięki)
  * [Dźwięk w&nbsp;służbie śledzenia](#dźwięk-wsłużbie-śledzenia)
  * [Rozpoznawanie słuchanych treści](#rozpoznawanie-słuchanych-treści)
  * [Łączenie urządzeń](#łączenie-urządzeń)
  * [Śledzenie lokalizacji](#śledzenie-lokalizacji)
  * [Deanonimizacja](#deanonimizacja)
* [Jak się chronić](#jak-się chronić)
  * [Asystenci głosowi](#asystenci-głosowi)
  * [Telefony i&nbsp;komputery](#telefony-ikomputery)

## Luzujemy założenia

W poprzednim wpisie pokazałem, że techniczna możliwość nagrywania naszych rozmów przez mikrofon w&nbsp;telefonie -- *nawet potajemnie, przy zablokowanym ekranie* -- [jak najbardziej istniała]({% post_url 2023-02-15-apki-mikrofon-mity %}#mały-praktyczny-eksperyment){:.internal}. Przynajmniej w&nbsp;mojej wersji systemu, Androidzie 10.

{:.post-meta .bigspace-after}
Nowsze wersje są nieco bezpieczniejsze; informują użytkowników, kiedy mikrofon jest w&nbsp;użyciu, wyświetlając ostrzegawczą kropkę.

Ale, mimo istnienia możliwości nasłuchu, gigantom raczej nie opłaca się non stop dobierać nam do mikrofonów. Jesteśmy bezpieczni... ale czy na pewno?

Można powiedzieć, że nasza prywatność „mikrofonowa” opiera się na kilku czynnikach, występujących jednocześnie:

1. Aplikacje są na naszym systemie operacyjnym jedynie gośćmi, a&nbsp;sam system jest po naszej stronie.
2. Autorzy apek nie mogą sobie pozwolić na nielegalne działania.
3. Dane dźwiękowe są zbyt *ciężkie*, żeby mogły być nieustannie wysyłane poza telefon albo analizowane algorytmem uczenia maszynowego.

Kiedy wszystkie założenia są spełnione, to szanse na to, że ktoś nas ciągle podsłuchuje mikrofonem, są raczej nikłe. Ale co będzie, jeśli zostaną naruszone?

{% include info.html
type="Uwaga"
text="Tak jak przy innych wpisach z&nbsp;tej serii, tak i&nbsp;tutaj skupiam się na smartfonach, a&nbsp;konkretniej systemie Android w&nbsp;wersji 10&nbsp;(który mam i&nbsp;mogę wnikliwiej sprawdzać).  
Jeśli Twój system już od dawna chroni przed którymś z&nbsp;opisanych zagrożeń, to tylko się cieszyć! Ale nie bagatelizujmy problemów z&nbsp;innymi urządzeniami."
%}

### Gdy aplikacje mają większą władzę

„System jest po naszej stronie”, założenie pierwsze. Przypomnę tutaj piramidkę smartfonowych warstw:

{:.bigspace}
<img src="/assets/posts/apki/mikrofony/apki_piramida_mikrofony.jpg" alt="Schemat pokazujący hierarchię we współczesnym urządzeniu. Ma kształt odwróconej piramidy. Na samym dole mamy ikonę procesora podpisaną CPU. Odchodzą od niej strzałki do ikonki symbolizującej mikrofon. Cała warstwa jest podpisana 'hardware'. Nad nią w&nbsp;piramidzie mamy kolejno: 'firmware', 'jądro systemu' oraz 'system operacyjny'. Na tej warstwie stoi mniejszy element, podpisany 'Programy' i&nbsp;opatrzony ikoną aplikacji Messenger."/>

Rzeczy znajdujące się wyżej są zależne od tych, które znajdują się niżej. Warstwą, po której możemy się poruszać my, użytkownicy, jest `System operacyjny`.

Przykład -- korzystając z&nbsp;telefonów z&nbsp;systemem Android lub iOS, możemy ustawiać *pozwolenia*. Jednym pstryczkiem dawać lub odbierać aplikacjom dostęp do elementów telefonu, takich jak mikrofon. A&nbsp;one nie są w&nbsp;stanie tego zakazu obejść.

Ale co w&nbsp;przypadku, kiedy twórca naszego systemu jest bardziej przychylny jakiejś aplikacji niż nam? Z&nbsp;czymś takim mamy do czynienia w&nbsp;przypadku **aplikacji systemowych**. Zwykle tkwią głębiej, sięgając jądra systemu, więc nie mamy na nie takiego wpływu jak na resztę.

Jeden przykład poznałem osobiście. Na ekranie głównym mojego telefonu (Huawei, Android 10) pewnego dnia, po jakiejś aktualizacji, tak po prostu pojawiła się nowa ikonka. *[Aplikacja AI Voice](https://consumer.huawei.com/en/support/content/en-us15777381/)*.

Jestem przekonany, że nigdzie nie klikałem, że chcę to instalować. Ot, taki niespodziewany prezent.

Co najgorsze, z&nbsp;automatu miał włączonych wiele pozwoleń -- w&nbsp;tym na dostęp do mikrofonu. Inne aplikacje, jak lubiany przez mnie Termux, miały po instalacji *wyłączone* pozwolenia, musiały dopiero prosić mnie o&nbsp;poszczególne zgody.  
Jest to zresztą ponoć [domyślny stan rzeczy](https://stackoverflow.com/a/41182643), począwszy od wersji 6&nbsp;Androida. 

A jednak ta apka była faworyzowana i&nbsp;przeskoczyła całą kontrolę. Co więcej, miała szeroki zakres uprawnień.

Nie jest to zresztą jakiś wyjątek. Taki program to **asystent głosowy**. Obecny na wielu smartfonach i&nbsp;dodawany przez poducentów -- Apple ma Siri, Samsung ma Bixby, inni mogą korzystać z&nbsp;Google Assistanta.

Asystenci usypiają naszą czujność, jeśli chodzi o&nbsp;udzielanie pozwoleń. W&nbsp;końcu mają nam ułatwiać korzystanie z&nbsp;telefonu... więc to chyba logiczne, że muszą być mocno zintegrowani z&nbsp;jego funkcjami?

Ale to i&nbsp;tak nic. Asystenci na telefonach są mimo wszystko apkami, podlegają choć częściowej naszej kontroli.  
Gorsze są *fizyczne urządzenia* z&nbsp;zainstalowanymi asystentami głosowymi. To często tak zwani *asystenci domowi* (ang. *home assistants*). Mają kształt małych głośniczków. Stoją nieruchomo i&nbsp;przyjmują polecenia głosowe.

To chociażby [urządzenia Google'a](https://support.google.com/assistant/answer/11091714?hl=en) takie jak: Google Home, Nest Mini, Nest Hub. Z&nbsp;kolei Amazon ma swoją Alexę.

{:.figure .bigsspace-before}
<img src="/assets/posts/apki/mikrofony/nightwish-alexa-ad.jpg" alt="Wokalistka zespołu Nightwish, Floor Jansen, stoi uśmiechnięta, zwrócona przodem do widza. W&nbsp;rękach trzyma urządzenie Amazon Alexa, w&nbsp;kształcie małego czarnego głośniczka"/>

{:.figcaption}
Trzecia wokalistka Nightwisha, Floor Jansen, w&nbsp;[reklamie](https://www.facebook.com/nightwish/posts/pfbid0GnjvsB9scgqAR5TR3kioAiMfSGsxenb6kB1zzsVzRqjTx7ea2Pf19Djnn5XyY5Evl) urządzenia Amazon Alexa.  
Bardzo szanuję wokal, nieco mniej dobór partnerów komercyjnych.

W przypadku takich urządzeń nie ma co mówić o&nbsp;piramidce.  
Cała piramidka -- od sprzętu fizycznego po programy -- jest bowiem **pod kontrolą producenta, a&nbsp;my mamy bardzo ograniczone możliwości działania**.

Co gorsza, tacy asystenci są popularni -- w&nbsp;2020 roku takie coś stało [w co piątym brytyjskim domu](https://www.which.co.uk/news/article/are-alexa-and-google-assistant-spying-on-us-aW8TJ6N0wdf8).  
Nieraz są też zintegrowani z&nbsp;różnymi funkcjami automatyki domowej, takimi jak regulowanie temperatury albo otwieranie bramy. Przejmując komuś asystenta, można nie tylko go podsłuchać, ale i&nbsp;przejąć jego „inteligentny” dom.

### Gdy przeciwnik nie przejmuje się prawem

„Nasi adwersarze będą się trzymali legalnych metod”. To założenie raczej prawdziwe w&nbsp;przypadku cyfrowych gigantów. Nie opłaca im się podsłuchiwać na masową skalę, bo w&nbsp;takim wypadku byliby łatwym celem dla prawodawców w&nbsp;różnych krajach.

Ale oprócz nich są też „kowboje” -- młode, dynamiczne firmy z&nbsp;branży reklam śledzących; być może z&nbsp;krajów, gdzie nie martwią się przepisami ochrony danych. Albo zwykli oszuści. Albo służby.

Wiem, że zaangażowanie tych ostatnich wydaje się mało realne. Ale niedawne wydarzenia z&nbsp;całego świata pokazały, że nie trzeba być Jamesem Bondem, żeby zostać celem [bardziej szpiegowskich zabawek](https://zaufanatrzeciastrona.pl/post/zaawansowany-system-podsluchowy-wykryty-na-telefonach-w-polskich-sieciach/). Wystarczy głośno krytykować rządy, które nie lubią krytyki.

Głośnym przykładem z&nbsp;ostatnich lat jest Pegasus -- nie tyle pojedynczy wirus, co [cały pakiet usług](https://payload.pl/czy-pegasus-jest-w-stanie-dalej-dzialac/) pozwalających przejąć kontrolę nad cudzym telefonem i&nbsp;podkradać informacje. Stosowany przez służby państwowe, które są mniej ograniczone prawem niż korporacje.

A przejęcie kontroli nad telefonem oznacza też nieograniczony dostęp do mikrofonu. Zyskujemy podsłuch w&nbsp;tradycyjnym znaczeniu tego słowa.

Ba, telefony nie są jedynym zagrożeniem! Według [dokumentów ujawnionych przez WikiLeaks](https://www.cbsnews.com/news/cia-hacked-samsung-smart-tvs-wikileaks-vault-7/), CIA posiadało narzędzia hakerskie pozwalające przejmować kontrolę nad telewizorami Samsunga i&nbsp;dobierać się do ich mikrofonów.

...Tak, mikrofonów. Nie głośników. W&nbsp;przeciwieństwie do niektórych innych modeli, te od Samsunga mogą przyjmować polecenia głosowe od użytkowników, więc mają w&nbsp;zestawie mikrofony. Wymarzony cel.

### Gdy przetwarzanie dźwięku jest łatwe

Poprzednio rozwodziłem się nad tym, że apka raczej nie wysyłałaby wszystkich nagrań w&nbsp;świat (bo za ciężkie). Miałaby też problem z&nbsp;nieustannym rozpoznawaniem mowy na naszym smartfonie.

Przypomnę: wymagałoby to  dużych modeli uczenia maszynowego.  
Są trudne do ukrycia (zwykle mają więcej megabajtów niż niejedna apka). Do tego szybko zużywałyby baterię, telefon by nam się nagrzewał. Ktoś na świecie by się zorientował i&nbsp;ujawnił cały proceder.

...Tylko że mówiliśmy o&nbsp;pełnoprawnym, nieustannym *rozpoznawaniu mowy*. A&nbsp;to założenie można łatwo poluzować.

Dla nas, ludzi, rozumienie tekstu mówionego jest czymś całkiem naturalnym -- niezależnie od tego, czy ktoś powie jedno słowo, czy też całe zdanie, raczej wyłapiemy sens wypowiedzi.  
Zaś w&nbsp;przypadku elektroniki wystarczy minimalna zmiana wymagań, żeby przejść od czegoś skrajnie trudnego do łatwizny. Co zresztą trafnie pokazuje XKCD:

{:.figure .bigspace-before}
<img src="/assets/posts/apki/mikrofony/tasks-xkcd.png" alt="Panel z&nbsp;komiksu XKCD z&nbsp;ludzikami-patykami. Pokazuje scenę, w&nbsp;której jedna postać stoi, a&nbsp;druga siedzi przy komputerze. Nad głowami postaci są dymki z&nbsp;wypowiedziami. Pierwsza prosi o&nbsp;dodanie funkcji sprawdzającej po zrobieniu zdjęcia, czy wykonano je w&nbsp;parku narodowym. Druga odpowiada, że to proste. Potem pierwsza postać dodaje, żeby sprawdzało też, czy na zdjęciu jest ptak. Druga odpowiada, że potrzebuje grupy badaczy i&nbsp;pięciu lat. Podpis mówi, że w&nbsp;świecie informatyki jest cienka granica między prostym a&nbsp;niemożliwym."/>

{:.figcaption}
Źródło: Randall Munroe, [XKCD](https://xkcd.com/1425/).

W praktyce analiza dźwięku **jest znacznie łatwiejsza, kiedy program porównuje fragmenty nagrań z&nbsp;dźwiękami z&nbsp;zamkniętej listy**.

Ciągłe, złożone analizowanie na bieżąco? Raczej odpada.  
Ale nasłuchiwanie, czy zabrzmiał *jakiś konkretny dźwięk*? A&nbsp;potem włączenie -- na krótki czas -- bardziej hardkorowej analizy? To już o&nbsp;niebo łatwiejsze!

{% include info.html
type="Ciekawostka"
text="Pierwowzór aplikacji Shazam, do rozpoznawania utworów muzycznych, powstał [już w&nbsp;2002&nbsp;roku](https://en.wikipedia.org/wiki/Shazam_(application)). W&nbsp;czasach grubo przed jakimikolwiek smartfonami! Na początku usługa polegała na tym, że dzwoniło się pod wskazany płatny numer i&nbsp;pozwalało automatowi posłuchać muzyki w&nbsp;tle."
%}

W praktyce tak właśnie ułatwiają sobie pracę wspomniani wyżej asystenci głosowi:

1. Tkwią w&nbsp;trybie czuwania i&nbsp;nasłuchują przez mikrofon. Czekają na określone słowa aktywujące (*wake words*).
2. Gdy je wypowiemy, to przechodzą do trybu aktywnego -- dokładniej rozpoznają mowę, żeby zrozumieć nasze polecenia.

Oczywiście ma to swoje ciemne strony.  
Punkt 1&nbsp;wymaga nieustannego słuchania -- w&nbsp;końcu asystent potrzebuje tego do działania!  
Z kolei punkt 2&nbsp;często wiąże się z&nbsp;wysłaniem nagrań naszego głosu w&nbsp;świat, jakiejś obcej firmie. Bo, jak już wiemy, analiza głosu jest wymagającym zadaniem, które warto zostawić mocnym komputerom.

Oba punkty mają swoje uzasadnienie. Ale jednocześnie normalizują w&nbsp;oczach społeczeństwa nasłuch i&nbsp;dzielenie się nagraniami. A&nbsp;wielkie firmy już parę razy nadużyły tej możliwości. Przykładem niech będzie wpadka Google'a.

Jak się okazało, **niektóre nagrania naszych poleceń trafiają do zewnętrznych podwykonawców**. A&nbsp;ci je transkrybują, żeby firma mogła potem szlifować algorytmy.

Jeden z&nbsp;takich podwykonawców [przekazał około 1000&nbsp;nagrań belgijskim mediom](https://siliconangle.com/2019/07/11/privacy-fail-audio-recorded-google-assistant-leaked-belgian-news-outlet/).  
Co ciekawe, w&nbsp;153 spośród nich nie padło hasło aktywujące `OK, Google`. Użytkownicy nie mieli świadomości, że aktywowali asystenta, zaś ich słowa poszły w&nbsp;świat.

Z kolei Alexa, poproszona przez pewnego człowieka o&nbsp;pobranie historii jego nagrań, spełniła polecenie... Tylko że nie do końca, bo udostępniła mu [ponad 1700&nbsp;nagrań innej osoby](https://www.washingtonexaminer.com/news/alexa-cut-it-out-over-1-000-personal-audio-recordings-leaked-to-stranger). 

## Szpiedzy podchodzą po cichu

Fragment o&nbsp;asystentach głosowych może nam dawać do myślenia -- skoro nasłuchiwanie konkretnych rzeczy nie jest takie trudne... to co by było, gdyby aplikacje, zamiast zbierać *wszystko*, wyłapywały tylko jakieś krótkie, ale znaczące dźwięki?

Coś takiego ma miejsce. I&nbsp;jest wykorzystywane w&nbsp;bardzo kreatywny sposób.  
Czas na część drugą tego wpisu -- o&nbsp;wykorzystaniu ultradźwięków i&nbsp;dźwięków na skraju słyszalności. 

> Przyglądam się i&nbsp;widzę, że każdy tu tak: w&nbsp;krąg powszechne brzuchomówstwo panuje, a&nbsp;jam myślał, że kruczenia i&nbsp;burczenia ze strachu! Wsłuchuję się tedy coraz niżej, aż na wysokości pasa słyszę coraz lepiej. I&nbsp;mówią brzuchy: Oj, niedola, niedola, byłażby nam wola!

{:.figcaption}
Stanisław Lem, „Cyberiada” (rozdział o&nbsp;Harmonii Sfer).

### Słyszalność i&nbsp;ultradźwięki

O dźwięku wiem niewiele, więc temat potraktuję momentami pobieżnie, darujcie. W&nbsp;każdym razie -- dźwięk ma taką swoją właściwość zwaną *częstotliwością* (wyrażaną w&nbsp;hercach,&nbsp;Hz).  
Wpływa ona między innymi na to, czy w&nbsp;ogóle go słyszymy.

Człowiek potrafi usłyszeć dźwięki, których częstotliwość mieści się w&nbsp;przedziale od około 20&nbsp;herców do kilkunastu, maksymalnie 20&nbsp;kiloherców (kHZ) z&nbsp;hakiem. Jeśli jest wyższa, to mamy do czynienia z&nbsp;ultradźwiękami, niesłyszalnymi dla człowieka.

Przykładowy test możemy sobie zrobić [przez YouTube'a](https://www.youtube.com/watch?v=qNf9nzvnd1k). Uwaga -- może nie być w&nbsp;stu procentach dokładny, a&nbsp;dźwięk może nagle się ucinać w&nbsp;okolicach 16&nbsp;kHZ ze względu na kompresję stosowaną przez YT.

Tyle jeśli chodzi o&nbsp;ludzkie ucho. A&nbsp;jak to jest z&nbsp;elektroniką konsumencką?

Według ciekawej dyskusji ze Stacka, urządzenia [są w&nbsp;stanie obsługiwać dźwięki na skraju słyszalności](https://electronics.stackexchange.com/questions/59157/over-what-frequency-range-can-the-microphone-of-smartphone-receive-the-sound). Głośniki komputera mogą je tworzyć, zaś mikrofony w&nbsp;smartfonach -- odbierać. Wiele zależy od modelu urządzenia.

{% include info.html
type="Ciekawostka"
text="Zakres słyszalności zmienia się z&nbsp;wiekiem; młodsi ludzie są w&nbsp;stanie usłyszeć dźwięki o&nbsp;wyższej częstotliwości.  
Niektórzy wykorzystali tę właściwość do [walki z&nbsp;kłopotliwą młodzieżą](https://www.today.com/news/controversial-mosquito-sonic-devices-deter-young-people-high-pitched-sounds-t157801) -- wagarowiczami i&nbsp;potencjalnymi wandalami. W&nbsp;miejscach, gdzie nikt nie powinien się kręcić, uruchamiają tak zwane *komary* -- żródła dźwięków o&nbsp;wysokiej częstotliwości. Są nieprzyjemne dla młodszych uszu i&nbsp;raczej niesłyszalne dla starszych. W&nbsp;Wielkiej Brytanii zostały uznane za nieetyczne i&nbsp;zakazane. W&nbsp;USA nadal są w&nbsp;użyciu."
%}

### Dźwięk w&nbsp;służbie śledzenia

Jeśli nasz sprzęt obsługuje większy zakres częstotliwości niż ucho, to może dojść do niepokojącej sytuacji -- **nie słyszymy żadnego dźwięku, ale urządzenia aktywnie ze sobą „rozmawiają” przez głośniki i&nbsp;mikrofony**. Skrycie przekazując sobie informacje.

W pewnym [artykule naukowym](https://web.archive.org/web/20170509095244/http://christian.wressnegger.info/content/projects/sidechannels/2017-eurosp.pdf) badacze z&nbsp;Niemiec wyróżnili cztery rodzaje zagrożeń -- łączenie naszej tożsamości ze słuchanymi treściami, łączenie różnych urządzeń w&nbsp;jeden profil, określanie naszej lokalizacji oraz deanonimizację. Omówię je po kolei.

{:.post-meta}
Od teraz, pisząc „artykuł naukowy”, będę nawiązywał właśnie do PDF-a z&nbsp;linku. 

{:.figure .bigspace-before}
<img src="/assets/posts/apki/mikrofony/ultrasound-tracking-diagram.jpg" alt="Cztery mniejsze schematy ułożone w&nbsp;dwóch rzędach po dwa. Pokazują cztery zagrożenia związane z&nbsp;ultradźwiękami: rozpoznawanie treści, łączenie urządzeń, lokalizowanie użytkownika i&nbsp;deanonimizację. Każdy z&nbsp;nich pokazuje strzałkami kierunek przepływu informacji od użytkownika do adwersarza, oznaczonego emotką uśmiechniętego diabełka."/>

{:.figcaption}
Źródło: artykuł naukowy. Przeróbki i&nbsp;tłumaczenie moje.

Przy okazji przyjmijmy tutaj parę założeń, które będą miały zastosowanie do wszystkich omawianych przypadków:

* Specjalne sygnały niekoniecznie muszą być ultradźwiękami.

  Dźwięki na skraju słyszalności -- a&nbsp;nawet całkiem słyszalne, lecz krótkie pyknięcia -- też spełniałyby się w&nbsp;roli specjalnych sygnałów. Więc progowanie (ucinanie dźwięków powyżej pewnej częstotliwości) niekoniecznie nam pomoże.

* Nasz przeciwnik -- np. firma reklamowa -- ma kontrolę zarówno nad źródłem specjalnych sygnałów, jak i&nbsp;nad aplikacją na naszym telefonie.

  Całkiem możliwe w&nbsp;czasach, gdy niemal każdy oferuje własną apkę, a&nbsp;ludzie masowo to instalują.  
  Oczywiście możliwe są również partnerstwa reklamowe -- jedna firma dogaduje się z&nbsp;drugą, że będzie nadawała konkretny sygnał. A&nbsp;ta druga konfiguruje swoją aplikację, żeby tego sygnału nasłuchiwała.  

* Apka korzysta z&nbsp;naszego mikrofonu.

  To może być najbardziej kontrowersyjne założenie, bo we współczesnych urządzeniach mamy [kropki ostrzegawcze](https://source.android.com/docs/core/permissions/privacy-indicators); nie da się też włączyć mikrofonu dyskretnie, w&nbsp;trybie wygaszonego ekranu.  
  Ale wyobraźmy sobie, że mamy jakąś uzależniającą apkę do nagrywania filmików. Zaraz po włączeniu aktywuje nam aparat i&nbsp;mikrofon, po czym na chwilę zostawia je włączone. Irytuje nas to, ale nie budzi podejrzeń -- bo zakładamy, że może nas co najwyżej nagrać, a&nbsp;przecież nic nie mówimy.

### Rozpoznawanie słuchanych treści

Wyobraźmy sobie, że oglądamy telewizor i&nbsp;jednocześnie korzystamy z&nbsp;apki na telefonie.  
Ale twórca apki oraz nadawca programu to jedna i&nbsp;ta sama organizacja (albo dwie współpracujące).

Telewizor podczas konkretnego programu nadaje co pewien czas określony, niesłyszalny sygnał dźwiękowy. Apka go odbiera. I&nbsp;wysyła twórcom informacje, że właściciel konta X&nbsp;właśnie oglądał program Y.

Śledzenie przez sygnały dźwiękowe [wykorzystała hiszpańska La Liga](https://nakedsecurity.sophos.com/2018/06/15/football-app-tracks-illegal-broadcasts-using-your-microphone-and-gps/).  
Wypuścili aplikację dla fanów piłki nożnej. Ale jedną z&nbsp;jej funkcji było nasłuchiwanie ukrytych sygnałów, miała też dostęp do GPS-a.

Kiedy ludzie oglądali mecz w&nbsp;barze, który nie kupił licencji do publicznego wyświetlania, apka to wychwytywała (odbierając ukryty dźwięk wpleciony w&nbsp;transmisję).  
Wysyłała wtedy firmie współrzędne z&nbsp;GPS-a. A&nbsp;ta mogła później pognębić lokal karami pieniężnymi.

Innym głośnym przypadkiem była indyjska firma **SilverPush**.

Działali na bardzo podobnej zasadzie, ale ogólniejszej -- zamiast stworzyć konkretną apkę, tworzyli [wyspecjalizowane moduły](https://www.theregister.com/2015/11/20/silverpush_soundwave_ad_tracker/) (tak zwane SDK), które inni twórcy mogli za opłatą zintegrować ze swoimi apkami.  
Moduły wyłapywały dźwięki o&nbsp;częstotliwości bliskiej 20&nbsp;kHZ -- czyli nie ultradźwięki, ale na granicy. Obszerny post na ten temat stworzył [Niebezpiecznik](https://niebezpiecznik.pl/post/uwaga-na-nieslyszalne-reklamy-reklamodawcy-wykorzystuja-ultradzwieki-do-tajnej-komunikacji-pomiedzy-telewizorami-a-smartphonami/) w&nbsp;2015 roku.

Apka wyszła też poza Indie. FTC, amerykańska agencja zajmująca się ochroną konsumentów, [wystosowała w&nbsp;2016 roku ostrzeżenie](https://www.ftc.gov/news-events/news/press-releases/2016/03/ftc-issues-warning-letters-app-developers-using-silverpush-code) do 12&nbsp;firm korzystających w&nbsp;swoich apkach z&nbsp;modułów od SilverPusha.

Firma istnieje do dziś i&nbsp;pozyskała niedawno finansowanie. Aktywnie się reklamują jako sposób na profilowanie ludzi we współczesnych czasach.

{:.figure .bigspace-before}
<img src="/assets/posts/apki/mikrofony/silverpush-tweet.jpg" alt="Tweet użytkownika SilverPush, napisany po angielsku i&nbsp;mówiący, że w&nbsp;związku z&nbsp;wycofywaniem ciasteczek (plików cookies) oferują nowe rozwiązanie do śledzenia użytkowników"/>

{:.figcaption}
Źródło: [tweet SilverPush](https://nitter.cz/SilverPush/status/1611305243450695680).  
Gdyby link nie działał, to można zmienić *nitter.cz* na *twitter.com*.

W 2017&nbsp;roku mieliśmy podobną aferkę z&nbsp;[modułami od firmy Alphonso](https://www.nytimes.com/2017/12/28/business/media/alphonso-app-tracking.html), które były dodawane do gier na urządzenia mobilne. Dziennikarze wyłapali ponad 250&nbsp;prawdopodobnych przypadków apek, które je w&nbsp;sobie miały.

### Łączenie urządzeń

Opisana wcześniej metoda działa niezależnie od rodzaju telewizora -- o&nbsp;ile ma wystarczająco dobry głośnik, żeby nie zgubić tajnego sygnału.

Ale każdy telewizor otrzymuje zazwyczaj tę samą transmisję. Nie da się na przykład sprawić, żeby każdy użytkownik dostał coś innego niż reszta.  
...Chyba że mamy współczesne Smart TV, zaś autor wścibskiej apki jest zarazem jego producentem. Albo się z&nbsp;nim dogadał.

Okazuje się, że każdy telewizor od tego producenta ma swój własny, unikalny identyfikator. I&nbsp;go emituje co pewien czas pod postacią niesłyszalnego dźwięku.

A my mamy na telefonie apkę od producenta, której już podaliśmy swoje prawdziwe dane. Co pewien czas apka prosi nas o&nbsp;nagranie ekranu telewizora; rzekomo po to, żeby go skalibrować. Kiedy to robimy, działa nam mikrofon. Apka odbiera po cichu ID telewizora.

W ten sposób producent dowiaduje się, że konkretny telewizor odpowiada konkretnej osobie. Jeśli dodatkowo wysyła on przez sieć historię oglądanych filmów, to producent może mieć w&nbsp;bazie:

{:.bigspace}
> Użytkownik Adam G. oglądał ostatnio filmy/klipy:  
„Szybcy i&nbsp;wściekli”. „Is your phone listening to you? (YouTube)”. „Cute office worker gets \[CENZURA\] on a&nbsp;desk”.

W podobny sposób dałoby się ustalić, że dwie osoby były w&nbsp;jednym miejscu. Wystarczy, że jednocześnie korzystają ze wścibskiej apki, dając jej dostęp do mikrofonu.

Naciągane? Ale załóżmy na przykład, że to apka w&nbsp;stylu Pokemon Go. Popularna, więc wiele osób ją ma. Wymaga użycia kamery wraz z&nbsp;mikrofonem, żeby zobaczyć jakiegoś stworka w&nbsp;3D, nałożonego na krajobraz. I&nbsp;generuje stworki w&nbsp;losowych momentach, dla wszystkich, przez co wielu graczy sięga po telefony w&nbsp;tym samym czasie.

Każda z&nbsp;apek nadaje ciche sygnały ze swoim unikalnym ID, a&nbsp;jednocześnie odbiera te z&nbsp;zewnątrz. Do producenta trafia informacja: „Gracze Anna&nbsp;K. oraz Sandra&nbsp;M. przebywają w&nbsp;tym samym miejscu”.  
Nawet jeśli mają wyłączone GPS-y i&nbsp;pod innymi względami się pilnują.

Jeśli kogoś interesuje temat, to więcej informacji można znaleźć pod hasłem `Ultrasonic Cross-Device Tracking`, albo w&nbsp;skrócie `uXdt`.  
Pewien post z&nbsp;forum Hacker News zawiera z&nbsp;kolei [obszerną listę firm i&nbsp;projektów](https://news.ycombinator.com/item?id=21443767) związanych z&nbsp;biznesem ultradźwiękowym. 

### Śledzenie lokalizacji

Wyżej mieliśmy przypadek sygnału unikalnego na poziomie urządzeń -- elektroniki konsumenckiej.  
Ale źródła tajnych sygnałów w&nbsp;żadnym razie nie muszą być duże. Mogą to być również malutkie nadajniki, bezużyteczne dla konsumentów. Ale przydatne dla wścibskich firm.

Jeśli każdy nadajnik wysyła nieco inny sygnał, to firma mogłaby nakupić spory ich zapas, żeby je rozstawić w&nbsp;różnych miejscach.  
Gdy zbliżymy się do któregoś z&nbsp;nich z&nbsp;włączonym mikrofonem i&nbsp;zainstalowaną wścibską apką, to odbierze ona unikalny sygnał nadajnika. Jej twórca -- bez naszej wiedzy -- dowie się, w&nbsp;jakim miejscu byliśmy. Nawet jeśli wyłączyliśmy GPS-a, Bluetooth, Wi-Fi.

Luźna myśl bez dowodów: gdyby nasze urządzenie miało głośnik zdolny do wytwarzania dźwięków wysokiej częstotliwości, to mogłoby to działać w&nbsp;drugą stronę. To nasze urządzenie nadaje, zaś mikroszpieg odbiera. Metoda raczej [mocno zależna od sprzętu](https://stackoverflow.com/questions/20153280/android-transmit-a-signal-using-ultrasound), ale nie wymagałaby pozwolenia na dostęp do mikrofonu.

Więcej informacji na ten temat można znaleźć, szukając pod hasłem `audio beacon` albo `ultrasonic beacon`. Sam `beacon` to zresztą ogólne pojęcie i&nbsp;dotyczy nie tylko dźwięku, ale też choćby małych nadajników wykorzystujących Bluetooth.

### Deanonimizacja

Jakiś użytkownik przegląda strony internetowe i&nbsp;nie chce, żeby ktoś ustalił jego tożsamość. Używa przeglądarki anonimizującej, jak Tor Browser.

Ale może wpaść, jeśli na telefonie ma apkę od kogoś wścibskiego, zainteresowanego jego tożsamością. I&nbsp;odwiedza stronę internetową naszykowaną przez tego samego złodupca.

Strony mogą odtwarzać pliki wideo i&nbsp;dźwięk, więc nie budzi to podejrzeń naszego użytkownika. Ale apka na jego telefonie odbiera ten sygnał i&nbsp;wysyła wścibskim ludziom dokładniejsze informacje.

„Cel odwiedził stronę-pułapkę. Przesyłam identyfikator jego telefonu oraz dane odczytane z&nbsp;plików”.

Przyznam, że to moim zdaniem nieco naciągane zagrożenie -- jeśli ktoś tak się troszczy o&nbsp;anonimowość, to raczej nie instalowałby apki z&nbsp;niepewnego źródła. A&nbsp;tym bardziej nie pozwalał jej na dostęp do mikrofonu. A&nbsp;gdyby już pozwolił, to zaalarmowałaby go kropka ostrzegająca przed nagrywaniem.

No ale nasz artykuł naukowy jest z&nbsp;2017 roku. Załóżmy, że w&nbsp;czasach dyskretnego nagrywania coś takiego byłoby bardziej realne.

## Jak się chronić

Wszystkie metody ochrony -- i&nbsp;przed nagrywaniem naszych słów, i&nbsp;przed niesłyszalnymi dźwiękami -- opierają się na najzwyklejszym w&nbsp;świecie wyłączeniu mikrofonu. Gdy go nie ma albo jest niedostępny dla programów, to jesteśmy bezpieczeni :smile:

### Asystenci głosowi

**Asystentów -- i&nbsp;telefonicznych, i&nbsp;domowych -- radziłbym po prostu nie używać**. Żadnego Echa czy Alexy. Szczypta wygody zyskanej dzięki takim gadżetom moim zdaniem całkiem blednie wobec ryzyka. A&nbsp;technologiczny hurraoptymizm zostawmy sekcie z&nbsp;Doliny Krzemowej.

Jeśli raczej się ich nie pozbędziemy (bo na przykład ktoś inny z&nbsp;rodziny je lubi), to można chociaż [kontrolować, co zbierają](https://www.which.co.uk/news/article/are-alexa-and-google-assistant-spying-on-us-aW8TJ6N0wdf8#how-to-control-and-manage-your-privacy). Albo [usunąć historię wydawanych poleceń](https://appauthority.com/how-to-delete-everything-youve-ever-said-to-your-digital-assistants-3257/), żeby ktoś się do nich nie dobrał.

Jeśli jest taka możliwość, można też zabezpieczyć asystenta, ustawiając mu własne, [nietypowe słowo aktywujące](https://www.gsmarena.com/bixby_update_is_bringing_text_call_support_in_english_custom_wake_words-news-57638.php) (tu artykuł o&nbsp;tym, że dawał ją Bixby).

Jeśli ktoś bardzo by chciał mieć automatykę domową, sterowane głosem światła czy termostaty -- ale bez podsłuchu w&nbsp;pakiecie -- to można rozejrzeć się za alternatywami *open source*. Istnieją zapewne firmy oferujące montaż takiej elektroniki.

Słowo-klucz do wyszukiwań na forach angielskich: `on-device` albo `local`. Oznacza, że dane byłyby przetwarzane tylko na urządzeniu i&nbsp;nie leciały w&nbsp;świat. Mielibyśmy obieg zamknięty na poziomie naszego domu.

### Telefony i&nbsp;komputery

Na telefonach najprostszym rozwiązaniem jest **wyłączenie aplikacjom pozwolenia na dostęp do mikrofonu**. Wszystkim. Zostawiając co najwyżej ustawienie kompromisowe `Tylko podczas korzystania` systemowej apce Aparat.  
Chcąc wysłać filmik z&nbsp;mniej zaufanej apki, jak Messenger, nagrywajmy go najpierw przez systemową apkę. A&nbsp;potem wybierajmy do wysłania wcześniej nagrany plik.

Osoby szczególnie wyczulone na punkcie prywatności -- jak grono narażone na Pegasusa albo nieufające systemowi na telefonie -- mogłyby teoretycznie skorzystać z&nbsp;urządzenia zawierającego **fizyczny wyłącznik mikrofonu**. On mógłby nas ochronić nawet w&nbsp;przypadku całkowitego przejęcia naszego urządzenia.

Ale -- i&nbsp;to bardzo ważne! -- przez wyłącznik *fizyczny* mam na myśli taki, który przerywa obwód elektryczny. Przez co do mikrofonu nie dopływa prąd i&nbsp;zwyczajnie nie ma prawa działać.

Jeśli mamy na laptopie kombinację klawiszy, po wciśnięciu której pojawia się komunikat o&nbsp;wyłączonym mikrofonie... To nie mamy niestety gwarancji, że faktycznie został wyłączony.  
Ten klawisz może po prostu wysyłać komputerowi sygnał, że czas nałożyć blokadę cyfrową. Ale gdyby ten był przejęty, to mógłby zignorować prośbę o&nbsp;blokowanie. A&nbsp;nam jedynie wyświetlić fałszywą informację, że blokada działa.

W wyłączniki z&nbsp;prawdziwego zdarzenia są wyposażone chociażby [laptopy od Apple](https://support.apple.com/guide/security/hardware-microphone-disconnect-secbbd20b00b/1/web/1) (po zamknięciu ekranu), [smartfony i&nbsp;laptopy firmy Purism](https://puri.sm/learn/hardware-kill-switches/) oraz przystępniejszy cenowo smartfon [Pinephone](https://www.androidpolice.com/2020/08/22/this-smartphone-has-physical-kill-switches-for-its-cameras-microphone-data-bluetooth-and-wi-fi/).

Uprzedzam jednak, że telefony na bazie Linuksa nie są urządzeniami dla każdego, a&nbsp;wiele mainstreamowych rzeczy by na nich nie działało. Najlepiej doczytać o&nbsp;nich na własną rękę.

A jeśli nie chcemy kupować żadnych niszowych urządzeń, nie ufamy mikrofonowi, a&nbsp;do tego nie jesteśmy biegli w&nbsp;sprawach technicznych i&nbsp;nie umiemy sprawdzić, czy nie nagrywa?

Pozostaje wtedy tajemne, niebywałe, przystępne rozwiązanie -- kiedy potrzebujemy prywatności, to nie bierzmy ze sobą smartfona ani innej elektroniki konsumenckiej!  
Korzyść bonusowa -- walka z&nbsp;cyfrowym nałogiem :smile:

