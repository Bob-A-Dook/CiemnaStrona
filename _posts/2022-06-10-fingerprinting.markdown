---
layout: post
title:  "Internetowa inwigilacja 11 – JavaScript, cz.3"
subtitle: "„Jak wyglądasz pod lupą?”"
description: "„Jak wyglądasz pod lupą?”"
date:   2022-06-10 17:15:00 +0100
tags: [Internet, Inwigilacja, Porady]
firmy: [Facebook, Google, Reddit]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: "javascript-tracking/js-fingerprint-baner.jpg"
image-width: 1200
image-height: 700
---

Witajcie w&nbsp;trzecim i&nbsp;ostatnim wpisie poświęconym JavaScriptowi -- językowi programowania internetu! A&nbsp;we wścibskich rękach *lingua franca* śledzenia internautów.

W [pierwszym wpisie]({% post_url 2022-05-02-javascript1 %}){:.internal} na temat JS-a poznaliśmy jego wygląd i&nbsp;ogólne działanie. Okazało się, że może zdobywać praktycznie wszystkie informacje wymienione w&nbsp;ośmiu wcześniejszych wpisach. A&nbsp;także wysyłać je w&nbsp;świat, na przykład swoim wścibskim autorom.

[Wpis drugi]({% post_url 2022-05-03-javascript2 %}){:.internal} pokazał, że jego możliwości są jeszcze większe i&nbsp;że może podpytywać o&nbsp;cechy naszego procesora, pamięci, internetu...  
Rozpoznając nas nawet po tym, jak zmienimy przeglądarkę i&nbsp;adres IP. Na szczęście nie były to metody stuprocentowo skuteczne.

Tym razem natomiast przejdziemy do metod szczególnie wrednych, które potrafią wychwycić cechy zdecydowanie nas wyróżniające i&nbsp;przypisać nam unikalny identyfikator.

Metody z&nbsp;taką mocą rozpoznawania ludzi, że mówi się na nie *fingerprinting* -- dosłownie *pobieranie odcisku palca*.

Zapraszam do lektury!

<img src="/assets/posts/javascript-tracking/js-fingerprint-baner.jpg" alt="Czarne litery J&nbsp;i S&nbsp;na żółtym tle, logo języka JavaScript. Literę J&nbsp;przerobiono tak, że wygląda jak czarny hak, z&nbsp;którego kapie krew. Z&nbsp;kolei litera S&nbsp;znajduje się na tle wielkiego odcisku palca."/>

# Spis treści

* [Śledzenie to codzienność](#śledzenie-to-codzienność)
  * [Przykład informacji z&nbsp;IAB](#przykład-informacji-ziab)
  * [Śledzenie jest łatwe](#śledzenie-jest-łatwe)
* [Różne oblicza fingerprintingu](#różne-oblicza-fingerprintingu)
  * [Wykrywanie dodatków](#wykrywanie-dodatków)
  * [Canvas](#canvas)
  * [Czcionki](#czcionki)
  * [WebGL](#webgl)
  * [Web Audio](#web-audio)
  * [Właściwości silnika JavaScriptu](#właściwości-silnika-javascriptu)
* [Jak się chronić](#jak-się-chronić)
  * [Unikanie zamiast walki](#unikanie-zamiast-walki)
  * [Niszczenie banerów](#niszczenie-banerów)
* [Podsumowanie](#podsumowanie)

## Śledzenie to codzienność

Spora część wpisów o&nbsp;JavaScripcie zawiera opisy różnych mechanizmów śledzących. Od niektórych może się włos jeżyć na głowie.

Ale nie zdziwiłbym się również, gdyby niektórzy czytelnicy powoli się wyłączali, mając wrażenie, że brniemy już w&nbsp;jakieś *science fiction* albo filmy szpiegowskie. Dlatego proponuję zrobić tu krótką przerwę na oswojenie się z faktem, że te metody są codziennością.

Spójrzmy najpierw na dowody anegdotyczne. Kilka egzotycznych metod śledzenia, które omówię w&nbsp;tym wpisie, znalezionych w&nbsp;internetach:

* Na ogromnym forum Reddit wykryto śledzący skrypt od firmy *HUMAN*. Wykorzystujący JavaScript do sprawdzenia [wielu dokładnych informacji](https://smitop.com/post/whiteops-data/) o&nbsp;komputerze. A&nbsp;nawet wykorzystujący luki w&nbsp;zabezpieczeniach, jak wirus.
* Na stronie StackOverflow -- najpopularniejszym forum z&nbsp;pytaniami i&nbsp;odpowiedziami dla programistów -- znaleziono [skrypt profilujący](https://meta.stackexchange.com/questions/331960/why-is-stack-overflow-trying-to-start-audio) na podstawie karty dźwiękowej.
* Przykłady [profilowania przez WebGL](https://jonatron.github.io/webgl-fingerprinting/) na największych stronach, wraz z&nbsp;fragmentami kodu, zebrał pewien autor na swojej stronce. Jeśli wierzyć jego przykładom, znajdziemy tam między innymi firmy Amazon, Yahoo, Instagram.

Niepokojące są również szersze trendy:
 
* Już w&nbsp;2014 roku, gdy śledzenia było mniej, w&nbsp;artykule *[The Web never forgets...](https://securehomes.esat.kuleuven.be/~gacar/persistent/)* opisano, że skrypty profilujące na podstawie grafiki wykryto na około 5,5% ze 100&nbsp;tysięcy najpopularniejszych stron internetowych.
* W&nbsp;[artykule naukowym](https://cba.upc.edu/downloads/category/11-articles?download=1045:[ARTICLE]Towards_accurate_detection_of_obfuscated_web_tracking.pdf&start=480) z&nbsp;2017 roku jest już mowa o&nbsp;użyciu podobnych metod śledzenia na ponad 10% z&nbsp;najpopularniejszych 10&nbsp;tysiący stron.

Jest to zatem rzecz częsta, popularna i&nbsp;-- niestety -- możliwe że tylko zyskująca na popularności.

W niektórych przypadkach skrypty profilujące miały ponoć służyć nie do celów reklamowo-śledzących, tylko do ochrony przed botami -- żeby wykryć, że osoba Y&nbsp;wchodząca na stronę jest tak naprawdę osobą X, po zmianie paru informacji, która chwilę wcześniej podkradała dane z&nbsp;bazy.

Ale niech nas to nie uspokaja. Po pierwsze, jeśli te dane są wysyłane w&nbsp;świat, nie mamy pewności co do ich dalszych losów.  
Po drugie: reklamodawcy i&nbsp;firmy analityczne też są doskonale świadomi możliwości JavaScriptu.  
Posłuchajmy sami jednego z&nbsp;większych graczy, czyli IAB.

# Przykład informacji z&nbsp;IAB

IAB, czyli *[Interactive Advertising Bureau](https://www.iab.org.pl/o-nas/)*. Organizacja reprezentująca firmy zajmujące się reklamą internetową, często opartą na profilowaniu użytkowników. Ujednolica pewne rozwiązania, takie jak wyskakujące okna pytające nas o&nbsp;zgodę na zbieranie informacji.

Wokół tych banerów narosły zresztą pewne kontrowersje, ponieważ pstryczki pozwalające nie wyrazić zgody na profilowanie są ukryte dość głęboko, wbrew zaleceniom GDPR/RODO. Systemu IAB nie polubił belgijski urząd ds. ochrony danych, [uznając go za sprzeczny z&nbsp;prawem](https://panoptykon.org/system-sledzacej-reklamy-IAB-nielegalny).

Z banerami IAB możemy zetknąć się na przykład po wejściu na strony należące do grupy Wirtualna Polska, takie jak pewien [artykuł](https://www.money.pl/gospodarka/skad-tak-drogi-gaz-wplyw-na-to-ma-splot-kilku-czynnikow-wyjasniamy-co-poszlo-nie-tak-6720716277488512a.html) ze strony Money.pl.

{:.figure .bigspace}
<img src="/assets/posts/javascript-tracking/wp-iab-baner.jpg" alt="Zrzut ekranu pokazujący baner strony Wirtualna Polska. Nagłówek mówi, że szanują prywatność, zaś treść opowiada o&nbsp;danych zbieranych przez stronę"/>

Jeśli wcześniej nie pozwalaliśmy im na zbieranie informacji, to treść się rozmyje i&nbsp;wyskoczy baner proszący o&nbsp;udzielenie zgody. Jeśli nie wyskoczy, to można spróbować odwiedzić stronę w&nbsp;trybie incognito.

Zamiast klikać na banerze wyróżnione *Zgódź się*, możemy kliknąć w&nbsp;*Listę partnerów IAB*, żeby zobaczyć dokładniejsze opcje. Mamy tutaj dokładniejsze opisy rzeczy, na które chcą naszej zgody. W&nbsp;punkcie numer 15&nbsp;piszą o&nbsp;tworzeniu:

> (...) identyfikatora przy użyciu danych zebranych poprzez aktywne skanowanie (...) np. **zainstalowanych czcionek lub rozdzielczości ekranu**

To dobry przykład na to, że metody profilowania przez JavaScript nie są czymś egzotycznym, używanym tylko w&nbsp;ciemnych zaułkach internetu. Nie; te informacje o&nbsp;wymiarach okna (z poprzedniego wpisu) czy o&nbsp;zainstalowanych czcionkach (z tego wpisu) są znane i&nbsp;często stosowane. Również przez branżę reklamową, na dużych i&nbsp;znanych stronach. Wobec nas.

# Śledzenie jest łatwe

Niektóre z&nbsp;metod śledzenia przez JavaScript -- szczególnie te, które opiszę w&nbsp;tym wpisie -- mogą wydawać się skomplikowane. Możemy w&nbsp;związku z&nbsp;tym mieć wątpliwości, czy to realne zagrożenie. Naprawdę jest na świecie tylu ludzi, którzy nic nie robią, tylko profilują?

Odpowiedź: tak, to realne. Dodanie do swojej strony opcji śledzenia może być kwestią paru kliknięć.  
Wystarczy dołączyć do którejś z&nbsp;sieci reklamowych i&nbsp;wykonać kilka instrukcji. Takich jak dodanie do źródła strony *kilku linijek* odpowiedzialnych za pobranie i&nbsp;włączenie cudzego skryptu. Który już zrobi resztę.

Istnieją firmy, których cała działalność opiera się na opracowywaniu metod profilowania. To oni robią te bardziej pomysłowe, złożone rzeczy. Następnie pakują swoje rozwiązania w&nbsp;skrypty, które łatwo spiąć z&nbsp;inną stroną. I&nbsp;sprzedają je innym.

Dlatego zupełnie nie ma co się dziwić, gdybyśmy znaleźli skrypt śledzący na przykład na stronie sieci supermarketów. Jasne, raczej nie mają własnych etatowych „programistów śledczych”. Ale **mogli kupić skrypty profilujące od kogoś innego i&nbsp;zapłacić za wdrożenie**.

Kolejna sprawa: czy takie metody mogą być skuteczne? W&nbsp;końcu to wiele różnych danych, sygnałów. Być może firmy same potykałyby się o&nbsp;własne nogi, próbując z&nbsp;tego wyciągnąć coś sensownego?

Odpowiedź: tak, to skuteczne. W&nbsp;świecie komputerów istnieje bardzo popularna metoda zwana *haszowaniem*. Pozwala ścisnąć wiele różnych wartości do jednego ciągu znaków. Co więcej, istnieją odmiany takie jak *MinHash* -- otrzymane ciągi znaków są tym bardziej do siebie podobne, im bardziej podobne były dane początkowe.

Zatem ustalenie odpowiedzi na pytanie „Czy użytkownik X&nbsp;to ta sama osoba co użytkownik Y?” może się sprowadzać do zebrania informacji przez skrypt, ściśnięcia ich w&nbsp;jedną liczbę, porównania z&nbsp;liczbami wcześniej zebranymi. **Wszystko w&nbsp;pełni automatycznie**.  
Nie ma co liczyć na to, że zadanie przerośnie naszych adwersarzy!

## Różne oblicza fingerprintingu

Mam nadzieję, że utwierdziliśmy się już w&nbsp;przekonaniu, że to nie *science fiction*, tylko nasza codzienność. Lekkie napięcie zbudowane -- jak w&nbsp;horrorach, gdy wiemy że będzie straszno, a&nbsp;do tego w&nbsp;pierwszych sekundach wyświetla się napis „Film oparty na faktach”.

Spójrzmy na szczególnie wredne metody profilowania.

# Wykrywanie dodatków

Wiele dodatków do przeglądarek zmienia w&nbsp;jakiś sposób strony internetowe. Na przykład stylizując w&nbsp;określony sposób ich elementy albo nawet dodając coś charakterystycznego od siebie:

* Przykład mi najbliższy: mój dodatek `SelSword`, który stworzyłem w&nbsp;celu [zaznaczania komentarzy trolli]({% post_url 2022-04-15-trolle-rosja-ukraina %}){:.internal}. Kliknięty komentarz z&nbsp;Twittera albo Facebooka otacza czerwoną ramką.
* Drugi przykład: uBlock Origin z&nbsp;włączonym blokowaniem obrazków. W&nbsp;takim wypadku miejsce, w&nbsp;którym powinien być obrazek, zostaje otoczone kropkowaną ramką.
* Inny przykład, z&nbsp;artykułu naukowego: dodatek pozwalający zapisywać niektóre treści, który dodaje pod nimi specjalny przycisk.

{:.bigspace}
<img src="/assets/posts/javascript-tracking/extension-effects.jpg" alt="Trzy zrzuty ekranu pokazujące efekt działania dodatków. U&nbsp;góry widać komentarz otoczony czerwoną ramką, pod nim linki do pobrania aplikacji, które zamiast obrazków mają czerwone przerywane obwódki. Na dole tweet z&nbsp;dodanym przyciskiem pozwalającym go zapisać w&nbsp;aplikacji Pocket."/>

Takie graficzne zmiany mogą być dla nas wygodne, bo widzimy, czy nasz dodatek działa.  
Ale jest pewien problem -- jeśli coś widzimy, to znaczy, że zapewne pojawiło się w&nbsp;kodzie HTML strony. A&nbsp;JavaScript ma wgląd w&nbsp;cały ten kod.

Na przykład czerwona ramka dodawana przez `SelSword` jest widoczna w&nbsp;kodzie jako:

<div class="black-bg mono">style="border: 2px solid red;"</div>

JS może wykryć takie elementy obce na stronie. A&nbsp;jeśli ma dostęp do jakiejś wielkiej bazy, zawierającej typowe elementy zmieniane przez dodatki, to **jest w&nbsp;stanie określić, z&nbsp;jakich konkretnych dodatków korzystaliśmy**.

Jeśli nasz zestaw jest nietypowy, to może się to stać bardzo silnym znakiem rozpoznawczym. Z&nbsp;tego względu dobrze mieć tych dodatków jak najmniej; wyłącznie zaufane, najlepiej nie ingerujące w&nbsp;treść każdej napotkanej strony.

# Canvas

Element `canvas` (ang. „płótno”, w&nbsp;sensie malarskim) z&nbsp;pozoru wydaje się niegroźny; to jeden z&nbsp;możliwych elementów podstawowych, z&nbsp;których można ułożyć stronę internetową. Na równi z&nbsp;akapitem, tabelką, przyciskiem i&nbsp;innymi rzeczami tego typu. Sam w&nbsp;sobie nie ma wyglądu, chyba że go wystylizujemy (tu np. dodałem obramowanie):

{:.bigspace}
<canvas id="myCanvas" width="200" height="100" style="border: 1px solid #4bc9c8"></canvas>

Pełni natomiast dość konkretną funkcję -- kod JavaScript może na nim umieszczać elementy graficzne. Koła, linie i&nbsp;tym podobne. **Może również wyciągać z&nbsp;niego stworzone obrazki, piksel po pikselu**. Jak zobaczymy, to ta właściwość umożliwia śledzenie.

Gdyby element *canvas* był używany zgodnie z&nbsp;przeznaczeniem, mógłby służyć do prostych interaktywnych wizualizacji, którymi steruje użytkownik. Ale wścibskie strony znalazły własne zastosowanie.

Spójrzmy na nagłówek mojego bloga w&nbsp;dwóch różnych przeglądarkach:

{:.bigspace}
<img src="/assets/posts/javascript-tracking/emotki-naglowek-porownanie.jpg" alt="Dwa zrzuty ekranu pokazujące nagłówek Ciemnej Strony, emotkę po lewej i&nbsp;tytuł po prawej. Są ustawione jeden pod drugim."/>

Ten u&nbsp;góry został otwarty w&nbsp;przeglądarce Brave, ten z&nbsp;dołu w&nbsp;Firefoksie. W&nbsp;obu przypadkach powiększenie ustawione na domyślne (100%), pełne okno.

Nagłówki wydają się prawie identyczne, prawda? Ale zróbmy zbliżenie na lewe oko emotki.

{:.bigspace}
<img src="/assets/posts/javascript-tracking/oko-piksele.jpg" alt="Zbliżenia na oko emotki z&nbsp;loga strony. Widać na nich poszczególne piksele i&nbsp;widać, że te na brzegach oczu różnią się od siebie." width="350px"/>

Teraz już widać różnice. Zwłaszcza w&nbsp;pikselach na brzegach; to tam zachodzi *antialiasing*, czyli lekkie zlewanie krawędzi z&nbsp;tłem, żeby wydawała się gładsza. Brave i&nbsp;Firefox korzystają z&nbsp;różnych silników, więc i&nbsp;efekt końcowy jest inny.

Bo widzicie... Grafika to złożona sprawa. Zaczyna się od prostej instrukcji graficznej, mówiącej komputerowi „stwórz linię”. Kończy się na pikselach wyświetlonych na ekranie.

Po drodze mamy wszelkie konwersje, transfery do karty graficznej, zaokrąglanie liczb, wygładzanie kantów... W&nbsp;efekcie **istnieją subtelne różnice między tym samym obrazkiem u&nbsp;dwóch różnych użytkowników**. Zaś jeden i&nbsp;ten sam użytkownik ma zwykle podobne piksele.

Możemy zmienić swój adres IP, wyczyścić pliki cookies, wylogować się z&nbsp;konta. Ale dopóki cały czas używamy tej samej kombinacji sprzętu, systemu i&nbsp;przeglądarki, wychodzą nam te same piksele. Jesteśmy rozpoznawalni.

Możecie sami sprawdzić, [jaki odcisk palca zostawicie na płótnie](https://browserleaks.com/canvas#how-does-it-work) przez stronę BrowserLeaks. Polecam też rozwinąć zakładkę *How Does It Work* i&nbsp;spojrzeć na ich przykładowy kod. Nawet jeśli jest uproszczony, to widać, że takie profilowanie nie jest jakąś wyższą matematyką. To względnie przystępna sprawa.

{%include info.html
type="Ciekawostka"
text="Firmą przodującą w&nbsp;„śledzeniu przez płótno” jest AddThis; ich elementy śledzące znajdowały się ponoć w&nbsp;wielu różnych miejscach, w&nbsp;tym na stronie _YouP*rn_ (autocenzura wyłącznie z&nbsp;obawy przed deindeksacją).  
A także... [na stronie Białego Domu](https://www.eff.org/deeplinks/2014/07/white-house-website-includes-unique-non-cookie-tracker-despite-privacy-policy)."
%}

# Czcionki

Sprawa dość mocno związana z&nbsp;poprzednią. Mianowicie: JavaScript, oprócz kształtów, może również kazać przeglądarce umieścić tekst w&nbsp;jakimś elemencie.

Pierwszy sposób na profilowanie to wspomniane już różnice w&nbsp;pikselach; zwłaszcza na brzegach, tam gdzie działa wygładzanie. Dodawanie tekstu można w&nbsp;ten sposób uczynić częścią *canvas fingerprintingu*, żeby poprawić jego dokładność.

Ale czcionki można wykorzystać do jeszcze dokładniejszego profilowania -- **określić, jakie dokładnie trzymamy na swoim systemie**.

Bo widzicie -- wszystkie zainstalowane programy zwykle czerpią czcionki z&nbsp;jednego, zbiorczego folderu, żeby się nie dublować.  
Kiedyś chciałem napisać pewnej osobie życzenia w&nbsp;Gimpie, czcionką w&nbsp;kocie łapy. W&nbsp;tym celu ją pobrałem i&nbsp;włożyłem do specjalnego folderu na swoim komputerze.  
Ale w&nbsp;ten sposób stała się widoczna również dla pozostałych programów, w&nbsp;tym przeglądarki.

I teraz, kiedy odwiedzam wścibską stronę, może się zdarzyć coś takiego:

* JavaScript wydaje mojej przeglądarce polecenie:
  „Napisz w&nbsp;tym miejscu *Hejo* czcionką *CatFont*”;
* przeglądarka to robi;
* JavaScript sprawdza, jaka jest szerokość elementu po dodaniu do niego tekstu. Jeśli zgadza się ze spodziewaną, to znaczy, że mamy czcionkę *CatFont* na komputerze.
* Następnie każe napisać ten sam tekst czcionką *DogFont*.
* ...Ale jej już nie mamy, więc zamiast tego przeglądarka tworzy napis czcionką domyślną.
* JavaScript to mierzy i&nbsp;widzi, że szerokość mu się nie zgadza. Wniosek: nie mamy tej czcionki.

Powtarzając tę metodę wiele tysięcy razy, **JavaScript może dokładnie ustalić, jakie czcionki zainstalowaliśmy u&nbsp;siebie na systemie**. A&nbsp;ta cecha -- zwłaszcza jeśli robimy coś związanego z&nbsp;grafiką i&nbsp;często dodajemy nowe czcionki -- może bardzo mocno nas wyróżniać.

# WebGL

Kolejna graficzna rzecz!

Współczesne przeglądarki, szczególnie Chrome, lubią dodawać nowe bajery. Jednym z&nbsp;nich jest możliwość **wyświetlania zaawansowanej grafiki w&nbsp;przeglądarce przez _WebGL_** (gdzie *WebGL* to przeniesienie w&nbsp;realia internetu bardzo popularnego pakietu *OpenGL*. *GL* od *Graphics Library*).

Grafika w&nbsp;czasie rzeczywistym -- taka jak sceny w&nbsp;grach komputerowych -- jest dość wymagająca. Zatem przeglądarka usuwa się z&nbsp;drogi, dając stronie bezpośredni dostęp do pewnych funkcji procesora i&nbsp;karty graficznej.

A JavaScript może wykorzystać te informacje do dokładniejszego profilowania. W&nbsp;praktyce wykorzystuje WebGL w&nbsp;dwojaki sposób:

* Podpytuje przeglądarkę o&nbsp;parametry karty graficznej, dostępne rozszerzenia itp. Jest tych informacji naprawdę sporo.
* Każe przeglądarce zrobić coś związanego z&nbsp;grafiką, na podobnej zasadzie jak przy *canvas fingerprintingu*. Identyczny efekt końcowy oznacza zapewne identycznego użytkownika.

Jeśli chcemy zobaczyć pełną listę rzeczy, jakie ujawnia nasza przeglądarka, to polecam [podstronę o&nbsp;WebGL](https://browserleaks.com/webgl) na Browser Leaks.

Warto się w&nbsp;szczególności upewnić, czy nie ujawniamy pola `Unmasked Renderer` -- to pełna nazwa naszej karty graficznej. Chrome i&nbsp;podobne mu przeglądarki to ujawniają.

{:.figure .bigspace-before}
<img src="/assets/posts/javascript-tracking/webgl-fingerprint.jpg" alt="Zrzut ekranu pokazujący fragment tabelki ze strony BrowserLeaks, zawierającej dwa częściowo zakryte hasze, a&nbsp;pod nimi żółto-pomarańczowy trójkąt na szarym tle, użyty do zbadania możliwości przeglądarki"/>

{:.figcaption}
Źródło: *Browser Leaks*. Hasze zakryte przeze mnie.

Z nowszych, tegorocznych spraw: twórcy innej stronki testującej naszą anonimowość, AmIUnique, zbadali pewną [metodę profilowania](https://blog.amiunique.org/an-explicative-article-on-drawnapart-a-gpu-fingerprinting-technique/), której nadali kryptonim *DrawnApart*.

Jest ona o&nbsp;tyle niepokojąca, że ustala wnikliwie pewne cechy naszej karty graficznej, które mogą się różnić nawet między tymi samym jej modelami.

Czyli jeśli używam karty graficznej zintegrowanej z&nbsp;procesorem -- dajmy na to Intel i5-4590 -- a&nbsp;ktoś inny używa tej samej karty, przeglądarki oraz hotspota, to *nadal dałoby się nas od siebie odróżnić*, na podstawie subtelnych różnic fabrycznych między naszymi kartami.

# Web Audio

Wielu z&nbsp;nas lubi sobie posłuchać jakiegoś dobrego bangerka. Dlatego nasze komputery, oprócz procesorów i&nbsp;kart graficznych, dysponują również kartami dźwiękowymi.

{:.post-meta .bigspace}
Swoją drogą: do wpisu polecam coś z&nbsp;gatunku *dark synth*, jak *[Red Horizon](https://www.youtube.com/watch?v=mKmBx5-6ays)* (link do YT). Ma ten dystopijny klimacik.

Tym kartom również wyszli naprzeciw twórcy przeglądarek, dając JavaScriptowi możliwość bezpośredniej komunikacji z&nbsp;nimi. Możliwość oczywiście nadużytą do celów śledzenia. 

W kwestii opisu metody zdam się na ludzi od *FingerprintJS*. Mówiąc ogólnie, polega ona na podaniu komputerowi kilku parametrów, żeby najpierw wygenerował falę dźwiękową, a&nbsp;potem ją skompresował.

Efekt jego działań różni się w&nbsp;zależności od przeglądarki, ale zapewne będzie taki sam dla tej samej kombinacji sprzętu, systemu i&nbsp;przeglądarki. Zatem: kolejny identyfikator do kolekcji.

{:.bigspace-before}
<img src="/assets/posts/javascript-tracking/audio-fingerprint.jpg" alt="Wykres pokazujący cztery oscylujące linie w&nbsp;różnych kolorach, odpowiadające różnym kombinacjom systemu i&nbsp;przeglądarki" width="500px"/>

{:.figcaption}
Źródło: [artykuł](https://fingerprintjs.com/blog/audio-fingerprinting/) FingerprintJS. Nie widać żółtej linii, bo mój wykres pokrywa się niemal w&nbsp;100% z&nbsp;tym dla Firefoksa na Windowsie.

Metoda profilowania przez dźwięk, jak już wspomniałem, została znaleziona między innymi na znanym forum StackOverflow.

# Właściwości silnika JavaScriptu

Skrypt śledzący z&nbsp;Reddita, prawdziwa skarbnica śledzącego JavaScriptu, [zawierał](https://smitop.com/post/whiteops-data/) tajemniczy komentarz: *haha jit go brrrrr*.  
Sam autor wpisu analizującego kod nie miał stuprocentowej pewności, do czego to służy, ale podejrzewał coś z&nbsp;silnikiem przetwarzającym kod.

{% include info.html
type="Tłumaczenie mema"
text="Wyobraźcie sobie bardzo śmiesznego mema. I&nbsp;zacznijcie się śmiać.  
A tak na serio: *haha X&nbsp;go brrr* (gdzie zamiast *brrr* mamy czasem inny dźwięk) pierwotnie pojawia się w memie o&nbsp;drukowaniu kasy. Potem został on uogólniony do każdej sytuacji, kiedy jedna postać ma na coś proste, choć toporne rozwiązanie, a&nbsp;drugą to wkurza.  
Istnieje na przykład [wersja z&nbsp;Aleksandrem Wielkim](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2Fngxago603qu41.jpg&f=1&nofb=1) i&nbsp;węzłem gordyjskim.  
„Niee, nie możesz tego tak po prostu przeciąć”. „Haha, miecz robi *ciach, ciach*”."
%}

Ale koniec z&nbsp;memami. Bardziej niż *go brrr* interesuje nas *JIT*.  
To zapewne skrót od *Just In Time*; metody, jaką JavaScript wykorzystuje do przekształcania naszego kodu w&nbsp;coś czytelnego dla komputera.

Zachęciło mnie to, żeby powpisywać `jit javascript fingerprinting` i&nbsp;podobne rzeczy w&nbsp;wyszukiwarkę. I&nbsp;w ten sposób natrafiłem na artykuł na temat [profilowania na podstawie JavaScriptu](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_01B-4_Schwarz_paper.pdf).

Okazuje się bowiem, że **można nas profilować według zachowania JavaScriptu, wyciągając ciekawe fakty na temat naszego procesora**.

Wspominałem wcześniej o&nbsp;grafice: na początku mamy prostą, czytelną dla komputera regułkę tworzącą, a&nbsp;po wszystkich przeróbkach otrzymujemy piksele wyświetlone na monitorze. Czytelne dla nas.

Przy przekształcaniu języka jest na odwrót. Zaczynamy od czytelnego kodu JavaScript, napisanego przez człowieka. A&nbsp;po różnych przekształceniach kończymy z&nbsp;enigmatycznymi instrukcjami przeznaczonymi dla komputera.

Wszystkie te przekształcenia mają na celu sprawienie, żeby kod szybciej działał, lepsze dopasowanie go do możliwości procesora.  
W skrajnych przypadkach, pokazanych w&nbsp;artykule, dwa prawie identyczne fragmenty kodu dają różne zestawy instrukcji. W&nbsp;zależności od tego, czy procesor jest przystosowany do pracy z&nbsp;blokami 32- czy 64-bitowymi:

{:.bigspace-before}
<img src="/assets/posts/javascript-tracking/javascript-isa.jpg" alt="Zrzut ekranu pokazujący dwa zestawy komend czytelnych dla komputera. Mają enigmatyczne nazwy, takie jak 'vaddss'. Widać, że w&nbsp;zestawie drugim jest mniej komend."/>

{:.figcaption}
Jedno i&nbsp;drugie brzmi dla mnie jak marsjański; ale widać, że pierwszy marsjański nieco się różni od drugiego.  
Źródło: [artykuł](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_01B-4_Schwarz_paper.pdf) z&nbsp;2019 roku.

A to tylko jedna z&nbsp;możliwości. Artykuł porusza również inne kwestie, takie jak zachowanie modułu zarządzającego pamięcią. Ogólne działanie zapewne podobne; znajdowanie punktów granicznych, w&nbsp;których coś (czas trwania, instrukcje...) ulega istotnej zmianie.

Odpowiednio dobierając zadania, można ustalić kilka istotnych właściwości, jakie posiada nasz sprzęt. I&nbsp;dorzucić je do naszego odcisku palca.

Myślę, że na dziś nam starczy. A&nbsp;jeśli komuś mało, to zachęcam do zastanowienia się, ile punktów do analizy zyskałyby firmy, gdyby w&nbsp;sieci spopularyzowała się wirtualna rzeczywistość (wymagająca stałego monitorowania ruchów ciała i&nbsp;gałek ocznych).

## Jak się chronić

Przede wszystkim instalujemy dodatek [uBlock Origin](https://ublockorigin.com/) -- blokuje pliki z&nbsp;*zewnętrznych* witryn, zgłoszonych przez użytkowników jako podejrzane. W&nbsp;tym również JavaScript śledzący od firm takich jak wspomniana AddThis. Jakąś część śledzenia w&nbsp;ten sposób wytniemy z&nbsp;życia.

A co, jeśli JavaScript znajduje się *bezpośrednio* na odwiedzanej stronie, wkomponowany w&nbsp;jej elementy, i&nbsp;nie jest pobierany z&nbsp;zewnątrz?

Jakimś sposobem jest korzystanie z&nbsp;przeglądarek, które mają swoje zasługi w&nbsp;walce z&nbsp;profilowaniem i&nbsp;nie dodają na ślepo wszystkich nowinek. Polecam [Firefoksa](https://www.mozilla.org/en-US/exp/firefox/new/) albo [Brave'a](https://brave.com/download/). Nie polecam Chrome'a, bo aktywnie [działa na szkodę dodatków blokujących]({% post_url 2022-05-11-google-manifest-v3 %}){:.internal}.

W przypadku **Firefoksa** można włączyć [funkcję dodatkowej ochrony](https://support.mozilla.org/en-US/kb/firefox-protection-against-fingerprinting).

{:.figure .bigspace}
<img src="/assets/posts/javascript-tracking/firefox-anti-fingerprinting.jpg" alt="Zrzut ekranu z&nbsp;ustawień Firefoksa, pokazujący co należy kliknąć, żeby włączyć dodatkową ochronę"/>

W tym trybie przeglądarka staje się lisem kłamczuchem i&nbsp;podaje stronom nieprawdziwe informacje, żeby ułatwić nam zlanie się z&nbsp;tłumem.

Niestety wymaga to pewnych wyrzeczeń. Przykład: zmienia nam strefę czasową, więc mogą przestać działać automatyczne podpowiedzi podczas np. kupowania biletów kolejowych online.

Wytrawni gracze mogą korzystać z&nbsp;[Tor Browsera](https://www.torproject.org/download/). To nie tylko anonimowe IP; Tor dba również o&nbsp;wiele innych aspektów anonimizacji. Ale do codziennego użytku może być nieprzyjemny, bo jest raczej powolny i&nbsp;niejedna strona go blokuje.

# Unikanie zamiast walki
 
W każdym razie, niezależnie od jakości przeglądarki, powtórzę nieco kontrowersyjną poradę z&nbsp;poprzedniego wpisu.  
A brzmi ona: **jeśli zależy nam na zwycięstwie w&nbsp;tej grze, to najlepiej w&nbsp;nią nie grać**.

Nawet jeśli ufamy swojej przeglądarce. Zawsze może się pojawić jakaś metoda profilowania, której jej twórcy nie wychwycą; a&nbsp;fakt, że nasza przeglądarka próbowała jej unikać, tylko nas wyróżni.  
Dlatego, chcąc naprawdę chronić prywatność, **wyłączmy JavaScript całkowicie**. Wiele odwiedzanych stron nie będzie działało, ale na niektóre może się udać wejść.

A jeśli mamy do sprawdzenia coś, czego naprawdę nie chcemy ujawniać internetowym korporacjom, to warto się przejść do miejsca publicznego i&nbsp;skorzystać z&nbsp;tamtejszych komputerów. Pamiętając, żeby nie logować się na żadne swoje konto.

{% include info.html
type="Porada"
text="Specjalnym przypadkiem jest Google oraz inne firmy mające jednocześnie apki mobilne oraz strony, na których czegoś szukamy.  
Idąc do biblioteki w&nbsp;tajemnicy przed nimi, najlepiej nie brać ze sobą telefonu (albo przynajmniej włączyć w&nbsp;nim tryb samolotowy).  
Dlaczego? Bo moglibyśmy nieświadomie się połączyć z bibliotecznym hotspotem. Po czym nasz telefon, w&nbsp;ramach rutynowej aktualizacji apek, pobrałby coś od nich. Przy okazji mógłby „podpisać” się tym samym adresem IP, z&nbsp;którego właśnie robimy nasze prywatne wyszukiwania na ich stronach."
%}

A jeśli jesteśmy gotowi całkiem wyłączyć JavaScript?  
Można to zrobić przez opcje wspomnianego uBlock Origin. Skoro i&nbsp;tak go używamy przeciw plikom śledzącym ze stron zewnętrznych, to można również skorzystać z&nbsp;pozostałych jego możliwości.

# Niszczenie banerów

A jeśli nie chce nam się specjalnie iść do biblioteki ani użerać się z&nbsp;częstym włączaniem JS-a, gdy strona bez niego nie działa?

W takim wypadku pozostaje wziąć ryzyko na siebie; natomiast mam jedną propozycję, która może nieco ułatwić nam życie.

Mianowicie: uBO posiada dość rzadko opisywaną **funkcję niszczenia elementów**, oznaczoną ikonką błyskawicy. W&nbsp;tym trybie klikamy jakiś element na stronce, a&nbsp;on znika. Można ustawić własny skrót klawiszowy włączający tę opcję -- osobiście wybrałem `Ctrl`&nbsp;+&nbsp;`,` (przecinek).

Pamiętacie baner od IAB, który pokazałem na początku? Strony chcące działać zgodnie z&nbsp;GDPR/RODO nie powinny zbierać od nas żadnych danych (również przez JavaScript), dopóki nie klikniemy, że wyrażamy na to zgodę. Jeśli wyłapiemy, że robią inaczej, to mamy prawo ich zgłosić.

A co się stanie, jeśli po prostu zniszczymy baner zaraz po tym jak wyskoczy? Zapewne zniknie, pozwalając nam przeglądać stronę. A&nbsp;żadnej zgody oficjalnie nie wyraziliśmy, więc nie powinno być śledzenia :smiling_imp:

W przypadku ustawienia skrótu klawiszowego niszczenie banerów to kwestia sekund. Wystarczy:

* Nacisnąć ustawiony skrót;
* Najechać kursorem myszy na wkurzający element (oznaczy się kolorem);
* Naciskać `Delete`, dopóki nie znikną wszystkie niechciane elementy;
* Nacisnąć `Esc`, żeby wyjść z&nbsp;trybu usuwania.

Potem można w&nbsp;spokoju przeglądać stronkę, o&nbsp;ile nie korzysta z&nbsp;wredniejszych metod antyblokerowych. Metoda niecodzienna, ale może dzięki temu skuteczna. Polecam!

## Podsumowanie

Tym wpisem kończę trylogię na temat JavaScriptu. Nie oznacza to w&nbsp;żadnym razie, że wyczerpałem temat -- metody śledzenia ogranicza jedynie ludzka kreatywność. A&nbsp;coraz to nowe funkcje, promowane przez firmę Google i&nbsp;ich Chrome'a, z&nbsp;pewnością będą na bieżąco wykorzystywane do celów profilowania :smile:

Powoli zbliżamy się też do końca „Internetowej inwigilacji”.

Wiemy już całkiem sporo o&nbsp;mechanizmach, z&nbsp;jakich korzystają firmy, żeby kompletować nasze cyfrowe teczki. Od informacji ujawnianych przy pierwszym kontakcie aż po te wymagające wnikliwego testowania naszego urządzenia.

W kolejnym wpisie zbiorę to w&nbsp;całość i&nbsp;podsumuję w&nbsp;jeden poradnik po ochronie internetowej prywatności. Będzie to również oficjalne zamknięcie serii; tej głównej, bo stworzę jeszcze niejeden wpis uzupełniający.

Do zobaczenia!
