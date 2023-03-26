---
layout: post
title:  "Acropalypse. Gdy wystają nam prywatne dane"
subtitle: "Obrazek to nie tylko piksele, ucinacz nie zawsze ucina."
description: "Obrazek to nie tylko piksele, ucinacz nie zawsze ucina"
date:   2023-03-24 20:00:00 +0100
tags: [Afera, Inwigilacja, Podstawy, Porady]
firmy: [Google, Microsoft]
image:
  path: /assets/posts/apki/acropalypse-baner.jpg
  width: 1200
  height: 700
  alt: "Zdjęcie rzymskiej rzeźby pokazującej brodatego mężczyznę. Jego twarz jest jaśniejsza niż reszta i otoczona ramką jak do przycinania obrazu, a półnagie ciało jest przyciemnione. Pod spodem widać stylizowany napis Acropalypse."
---

Zapewne większości z&nbsp;nas zdarzyło się wysłać komuś *screenshota*, nazywanego krócej *screenem* albo, po polsku, *zrzutem ekranu*. W&nbsp;ten sposób możemy łatwo podzielić się z&nbsp;innym człowiekiem tym, co widzimy u&nbsp;siebie na ekranie.

Ale czasem kopia całego naszego ekranu to za dużo, a&nbsp;interesująca jest tylko niewielka część. Po co dzielić się górnym paskiem telefonu? Nie ma tam nic cennego -- co najwyżej ktoś pośmieszkuje, jeśli według licznika zostało nam 3% baterii. 

Na szczęście zwykle łatwo możemy przyciąć screeny przed wysłaniem.  
Włączamy jakiś domyślny systemowy program, zaznaczamy obszar na większym obrazku. Na naszych oczach reszta obrazka znika, a&nbsp;w podglądzie widzimy już tylko nasz wycinek. Wysyłamy go swoim odbiorcom.

I tutaj właśnie pojawił się problem. Niedawno wyszło na jaw, że domyślne funkcje wbudowane w&nbsp;Pixele (telefony Google'a) oraz system Windows **nie zawsze usuwały przycięte rzeczy, zostawiając w&nbsp;pliku z&nbsp;obrazkiem potencjalnie prywatne dane**.

W tym wpisie w&nbsp;jak najprzystępniejszy sposób omówię całą sprawę. Zapraszam! :smile:

{:.bigspace-before}
<img src="/assets/posts/apki/acropalypse/acropalypse-baner.jpg" alt="Przerobiony obrazek pokazujący rzymską statuę półleżącego brodatego mężczyzny, trzymającego w&nbsp;ręku róg obfitości. Jego twarz otacza jasna ramka o&nbsp;czerwonych rogach, zaś reszta obrazka, na której widać jego półnagie ciało, jest przyciemniona, tak jakby tylko twarz miała zostać wycięta z&nbsp;obrazka. U&nbsp;dołu widać napis Acropalypse."/>

{:.figcaption}
Źródło: [Wikipedia, zdjęcie Erin Silversmith](https://commons.wikimedia.org/w/index.php?curid=135990) oraz [post Simona Aaronsa](https://nitter.cz/ItsSimonTime/status/1636857478263750656). Przeróbki moje.  
P.S. Brodacz to bóg Tiberinus, a&nbsp;to coś w&nbsp;jego dłoni to róg obfitości :wink:

## O&nbsp;obrazkach słów kilka

Żeby wpis miał jakąkolwiek wartość edukacyjną, pozwolę sobie dodać parę podstawowych, bardzo luźnych informacji na temat obrazków i&nbsp;kodowania. Bez obaw, będzie bezboleśnie!

{:.post-meta .bigspace-after}
A jeśli ktoś już to wszystko wie -- albo wiedzieć nie chce -- to może przeskoczyć [prosto do aferki](#google-pixel-ipoczątek-historii){:.internal}.

Za podstawową „jednostkę budulcową” obrazka możemy uznać **piksel**. Zazwyczaj przedstawia się go w&nbsp;postaci RGB (ang. *Red, Green, Blue*).  
Na czym to polega? Ano na tym, że każdemu pikselowi odpowiadają trzy liczby. Wskazują, jakie jest w&nbsp;nim natężenie kolorów: czerwonego, zielonego i&nbsp;niebieskiego. 0&nbsp;to najmniejsza możliwa wartość koloru, zaś 255&nbsp;-- największa.

Załóżmy, że mamy taki minimalistyczny obrazek:

{:.figure .bigspace}
<img src="/assets/posts/apki/acropalypse/acropalypse-piksele.jpg" alt="Cztery kwadratowe piksele ustawione w&nbsp;jednej linii. Pierwsze trzy mają taki sam seledynowy kolor, zaś ostatni ma kolor czerwony"/>

Składa się on z&nbsp;trzech pikseli `(0,255,209)` oraz jednego piksela `(255,0,0)` (czystej czerwieni).

Chcemy zapisać ten obrazek jako szereg instrukcji, które pozwolą różnym programom wyświetlać go na ekranie. W&nbsp;najprostszym przypadku opiszemy go piksel po pikselu, od lewej do prawej:

<div class="black-bg mono bigspace">
1. Masz piksel w&nbsp;kolorze (0,255,209)<br/>
2. Masz piksel w&nbsp;kolorze (0,255,209)<br/>
3. Masz piksel w&nbsp;kolorze (0,255,209)<br/>
4. Masz piksel w&nbsp;kolorze (255,0,0)
</div>

Taki sposób jest jednak strasznie niewydajny, kilka razy się powtarzamy!

Dlatego zastosujmy jakąś bida-kompresję. Na przykład zapisując nasz obrazek w&nbsp;tak zwanym kodowaniu [*Run-Length Encoding*](https://pl.wikipedia.org/wiki/RLE).  
Polega ono na tym, że w&nbsp;każdej instrukcji umieszczamy informację o&nbsp;tym, *ile mamy pod rząd* pikseli w&nbsp;jednym kolorze:

<div class="black-bg mono bigspace">
1. Masz 3&nbsp;piksele w&nbsp;kolorze (0,255,209)<br/>
2. Masz 1&nbsp;piksel w&nbsp;kolorze (255,0,0)
</div>

Na pierwszy rzut oka widać, że metoda druga jest bardziej zwięzła, prawda? :wink: A&nbsp;będzie tym bardziej wydajna, im więcej mamy identycznych pikseli pod rząd. Jedynym wymogiem jest to, żeby programy odczytujące obrazek „rozumiały” nasze instrukcje.

Wniosek jest prosty -- kompresja się opłaca, zwłaszcza w&nbsp;obecnych czasach, gdy obrazki przesyła się na masową skalę. Dlatego **od dawna są czymś więcej niż prostą listą pikseli**. Ba, w&nbsp;praktyce bywają naszpikowane hardkorowymi metodami kompresji.

Cały czas opracowuje się nowe formaty, lepiej dopasowane do współczesnych obrazków. *HEIF*, *WEBP*, *JPEG-XL*... Dlatego gdyby ktoś zapytał, czym są za kulisami obrazki, to dobrą odpowiedzią wydaje się „to zależy”.

W naszym przypadku problemy nie dotyczą jednak tych nowych formatów, tylko leciwego już (i&nbsp;bardzo popularnego) *PNG*. Który, choć stary, jest również dość złożony.

### Problem fałszywego zakończenia

{% include info.html
type="Uwaga"
text="Opis problemu w&nbsp;moim wykonaniu będzie bardzo luźny i&nbsp;nieścisły. Raczej nijak się ma do tego, jak naprawdę działa format PNG. Chodzi mi po prostu o&nbsp;pokazanie pewnej intuicji, modelu myślowego. Kto pragnie ścisłej wiedzy, ten może przeczytać [post Davida Buchanana](https://www.da.vidbuchanan.co.uk/blog/hello-png.html)."
%}

Ktoś z&nbsp;twórców formatu PNG uznał -- z&nbsp;tego czy innego powodu, ale obstawiam że dla większej elastyczności -- że obrazek PNG nie będzie się tak po prostu kończył na ostatnim pikselu.

Wyobraźmy sobie, że zawiera osobną instrukcję. Mówiącą, że już koniec, można przestać czytać plik.  
Problem w&nbsp;tym, że **po tej instrukcji może się znajdować więcej danych**.

<div class="black-bg mono bigspace">
...<br/>
3. Masz piksel w&nbsp;kolorze (0,255,209)<br/>
4. Masz piksel w&nbsp;kolorze (255,0,0)<br/>
5. <span class="red">KONIEC</span><br/>
6. Masz piksel w&nbsp;kolorze (66,66,66)<br/>
...
</div>

Każdy sensowny program będzie czytał ten plik „linijka po linijce”. Zatrzyma się na punkcie 5&nbsp;-- bo po co dalej pracować, kiedy każą przestać?  
Wyświetli nam to, czego się spodziewaliśmy. A&nbsp;my nie będziemy mieli najmniejszego pojęcia, że w&nbsp;obrazku ukrywa się coś jeszcze.

Ktoś z&nbsp;Google'a, zapewne nie znając niuansów formatu, wpadł w&nbsp;pułapkę. I&nbsp;teraz oficjalnie przechodzimy do naszej aferki.

## Google Pixel i&nbsp;początek historii

Wszystko odkryła dwójka badaczy zajmujących się cyberbezpieczeństwem -- David Buchanan i&nbsp;Simon Aarons. Zgłosili sprawę Google'owi, a&nbsp;kiedy firma już naprawiła lukę, to dokładniej ją opisali.

Otrzymała ona kryptonim *Acropalypse*, czasem dla czytelności zapisują ją również *aCropalypse*. To połączenie słów *crop* (przycięcie/kadrowanie obrazka) oraz *apocalypse* (apokalipsa).

17 marca Aarons opublikował [krótki opis zagrożenia](https://nitter.cz/ItsSimonTime/status/1636857478263750656) na Twitterze. Dzień później podał również link do [stronki](https://www.da.vidbuchanan.co.uk/blog/hello-png.html) pozwalającej osobiście sprawdzić, czy nasze zdjęcia mają ukryte dane.

Problem dotyczył aplikacji systemowej Markup -- domyślnie zainstalowanej na telefonach marki Pixel, produkowanych przez Google'a. Służy ona do prostej obróbki obrazków.

Aplikacja, **zamiast zapisać wycinek do nowego pliku, wstawiała go na początek poprzedniego**. Jak pokazałem wyżej, z&nbsp;punktu widzenia użytkownika nowy obrazek działał normalnie, bo większość apek czyta dane tylko do czasu, aż napotkają instrukcję kończącą. A&nbsp;reszta pikseli spokojnie sobie tkwi w&nbsp;obrazku.

Gdyby ktoś wszedł w&nbsp;posiadanie takiego nadpisanego obrazka, to mógłby użyć specjalnego programu do odzyskiwania danych. I&nbsp;wyciągnąć sporą część oryginału, sprzed przycięcia, wraz z&nbsp;wrażliwymi danymi:

{:.bigspace-before}
<img src="/assets/posts/apki/acropalypse/acropalypse-discord-schemat.jpg" alt="Schemat pokazujący w&nbsp;górnej części post na platformie Discord, w&nbsp;którym ktoś chwali się nową kartą, a&nbsp;pod spodem widać zdjęcie tej karty. Od tego miejsca odchodzi w&nbsp;dół strzałka, podpisana 'Pobranie zdjęcia i&nbsp;użycie specjalnego programu'. W&nbsp;dolnej części widzimy pełen obrazek, z&nbsp;widocznymi danymi dotyczącymi karty"/>

{:.figcaption}
Źródło: [schemat Aaronsa](https://nitter.cz/ItsSimonTime/status/1636857478263750656), przeróbki moje.

Całe zagrożenie nie jest ponoć takie stare, bo wiąże się ze zmianą wprowadzoną przez Google [w wersji 10&nbsp;Androida](https://issuetracker.google.com/issues/180526528?pli=1).  
Zmienili tam działanie pewnej funkcji zapisującej. Zamiast nadpisywać pliki, po prostu wrzucała nowe dane na początek istniejących. Apka Markup z&nbsp;tej funkcji korzystała, zapisując pliki PNG.

W ten sposób powstał nam swoisty łańcuszek niefortunnych zdarzeń.  
Nikt nie wychwycił, że rozmiar obrazu po przycięciu jest identyczny albo prawie identyczny jak rozmiar oryginału. Ani że obrazek zawiera dane nawet po oficjalnym znaczniku kończącym (co wychwyciłby choćby program `exiftool`).

### Intuicyjnie o&nbsp;artefaktach

A skąd wzięły się te dziwne kolorowe kreski na obrazku (fachowo zwane [*artefaktami*](https://pl.wikipedia.org/wiki/Artefakt_(informatyka)))?

Intuicyjnie możemy sobie wyobrazić, że „naklejamy” nowy mniejszy obrazek na początek naszego starego, przez co wartości częściowo się nakładają. I&nbsp;zostajemy z&nbsp;czymś takim:

<div class="black-bg mono bigspace">
...<br/>
1. Masz piksel w&nbsp;kolorze (0,255,209)<br/>
2. Masz piksel w&nbsp;kolorze (0,255,209)<br/>
3. <span class="red">KONIEC</span> 5, 209)<br/>
4. Masz piksel w&nbsp;kolorze (255,0,0)<br/>
...
</div>

Widzimy, że mocno popsuła nam się linijka 3.

Obstawiam, że wiele normalnych programów nie wyrzuci żadnego błędu. Bo zatrzymają się na instrukcji `KONIEC` i&nbsp;nie zrobią dalszego kroku w&nbsp;przepaść -- tam, gdzie zderzyłyby się z&nbsp;błędami w&nbsp;formacie.

Programy specjalnie dopasowane do takich sytuacji, jak ten napisany przez badaczy, będą czytały dalej. Ale nie odzyskają wszystkiego, bo, jak widzimy, wartość została częściowo nadpisana. Nie da się w&nbsp;całości ustalić, co tam było.

W praktyce tymi nakładającymi się rzeczami nie będą oczywiście pojedyncze piksele, tylko jakieś bardziej złożone struktury, z&nbsp;których korzysta PNG. Ale efekt końcowy będzie zbliżony -- przez chwilę mamy syf i&nbsp;chaos (*artefakty*), a&nbsp;potem już normalne, czytelne piksele.

Jeśli mamy szczęście, to artefakty zakryją nam akurat te poufne informacje, które wolelibyśmy pozostawić uciętymi.

## Windows dołącza do gry

Ktoś mógłby powiedzieć, że telefony Pixel, w&nbsp;dodatku o&nbsp;określonej wersji, to przypadek dość rzadki, więc raczej mało komu zaszkodził. Do tego wiele serwisów i&nbsp;portali społecznościowych od dawna kompresuje obrazki, czego nie przetrwałyby żadne nadmierne piksele.

Platforma Discord, podana przez badaczy jako przykład, również od jakiegoś czasu [czyści obrazki](https://nitter.cz/BgJxSIaS1XLRWcl/status/1636907518881419264).  
Telefony inne niż Pixele niekoniecznie korzystają z&nbsp;feralnej funkcji. Autor alternatywnego systemu GrapheneOS [wprost napisał](https://nitter.cz/GrapheneOS/status/1638402307560816647#m), że nie dotyczy ich to zagrożenie.

Czy zatem luka dotyczy nielicznych i&nbsp;została załatana, mamy szczęśliwe zakończenie? Wręcz przeciwnie, napięcie rośnie :smiling_imp:.

Odkrycie sprawiło, że badacze zaczęli się rozglądać za podobnymi lukami bezpieczeństwa.  
Jeden z&nbsp;nich, Chris Blume, [napisał 21&nbsp;marca na Twitterze](https://nitter.cz/ProgramMax/status/1638217206180741121), że widzi podobne nieścisłości w&nbsp;rozmiarach plików edytowanych przez Narzędzie Wycinania.

To **domyślny program do screenshotów, dołączony od dawna do systemu Windows**. A&nbsp;zatem znacznie bardziej popularny.

{:.post-meta .bigspace-after}
Uwaga: nie sprawdzałem tego osobiście, ale ponoć mowa tu o&nbsp;programiku *Snipping Tool* z&nbsp;Windowsa&nbsp;11 oraz *Snip & Sketch* z Windowsa&nbsp;10;  błąd nie dotyczy natomiast dawnego *Snipping Toola* z&nbsp;Windowsa&nbsp;10 i&nbsp;poprzednich.

David Buchanan przyjrzał się tej sprawie. I&nbsp;[zareagował dość żywiołowo](https://nitter.cz/David3141593/status/1638222624084951040). Pozwolę sobie zacytować (z&nbsp;mikrocenzurą, coby mi bloga nie strącili):

{:.bigspace-after}
{% include comment.html
author="David Buchanan"
source="twitter"
text="holy F*CK.  
Windows Snipping Tool is vulnerable to Acropalypse too.  
An entirely unrelated codebase.  
The same exploit script works with minor changes (the pixel format is RGBA not RGB)  
Tested myself on Windows 11
"%}

Przyczyny podobne jak u&nbsp;Google'a. Systemowe funkcje do zapisywania plików nie zawsze działały intuicyjnie, ktoś oparł na nich systemowe narzędzie do screenów, format PNG nie protestował, testy nie wyłapały różnic w&nbsp;rozmiarze plików.  
Całość dokładniej opisał inny badacz, [Steven Murdoch](https://nitter.cz/sjmurdoch/status/1638623990817103888).

Ludzie z&nbsp;Windowsa dowiedzieli się o&nbsp;sprawie i&nbsp;podobno załatali wszystko [aktualizacją](https://nitter.cz/David3141593/status/1638669234480742400#m) z&nbsp;22&nbsp;marca.  
Nie zmienia to faktu, że we wcześniej zrobionych screenach już mogą tkwić sekrety. Zaś nasza aferka oficjalnie wyszła poza jakiegoś niszowego Pixela i&nbsp;stała się czymś znacznie ogólniejszym, mogącym dotykać większe grono użytkowników.

### Kwestia Worda 

Skoro już jesteśmy przy Microsofcie, to rozwinę wątek. Pewien użytkownik Twittera zwrócił uwagę na to, że również z&nbsp;dokumentami Worda trzeba uważać, bo pierwotny obrazek [może pozostać w&nbsp;pliku](https://nitter.cz/Oddvarmoe/status/1638683677960945664#m) wraz z&nbsp;wersją przyciętą. Wskazuje tam również ustawienie, które pozwoliłoby się przed tym chronić.

Od siebie dodam, że do wnętrza takich dokumentów wbrew pozorom łatwo się dobrać. Można je rozpakować jak zwykły plik ZIP -- co w&nbsp;przypadku Windowsa może wymagać zmiany rozszerzenia z&nbsp;`.docx` na `.zip`. A&nbsp;po rozpakowaniu wnętrze pliku stoi otworem, wraz ze wszystkimi obrazkami.

{% include info.html
type="Ciekawostka"
text="Znany jest przypadek co najmniej jednej osoby (prezenterki telewizyjnej), która miała przykrości przez przycięte zdjęcie -- choć akurat przez metadane, a&nbsp;nie piksele po znaczniku kończącym.  
Na swoim blogu umieściła zdjęcie twarzy, ale ktoś pobrał plik i&nbsp;odkrył, że znajdowała się w&nbsp;nim miniaturka fotki oryginalnej, sprzed przycięcia, nieusunięta przez Photoshopa. Fotki, dodajmy, częściowo nagiej.  
Pewien użytkownik wspomina ten przypadek w&nbsp;wątku pod pierwszym tweetem Aaronsa."
%}

## Inne wątki

Sprawa nadal się rozwija. Na fali odkrycia zapewne przybyło badaczy prześwietlających inne programy. Wszystko, co nie nadpisywało całkowicie pliku PNG, tylko „nakładało” nowy obrazek na jego początek, również może być podatne na Acropalypse. 

Z tego względu zainteresowani mogą dalej śledzić rozwój wypadków -- hasło `acropalypse` jest na szczęście bardzo unikalne, więc łatwo je znaleźć.

Dla ułatwienia podsyłam parę miejsc, w&nbsp;które warto zerkać:

* wyniki ze strony [HackerNews](https://hn.algolia.com/?q=acropalypse);
* wyniki z&nbsp;[Nittera](https://nitter.cz/search?f=tweets&q=acropalypse&since=&until=&near=) (gdyby link nie działał, można wpisać hasło w&nbsp;wyszukiwarkę Twittera).

## Czy to dla nas groźne?

Choć Acropalypse jak najbardziej może ujawniać niektóre dane, warto zaznaczyć, że na szczęście byłby groźny tylko w&nbsp;szczególnych okolicznościach. **Muszą zajść wszystkie naraz**:

1. Poza wyciętym obszarem jest coś prywatnego, czego byśmy nie chcieli ujawniać;
2. Otwieramy plik konkretnym programem (Narzędzie Wycinania na Windowsie, Markup na Pixelu, ew. jakieś dotąd nieodkryte kombinacje), przycinamy go i&nbsp;zapisujemy pod taką samą nazwą

   (nie mam tu 100% pewności, ale zapewne błąd nie miałby miejsca przy samym *łapaniu pierwszego screena*, jedynie przy otwieraniu i&nbsp;przycinaniu wcześniej zapisanego pliku obrazkowego);

3. Dane spoza wycinka nie zostaną przykryte artefaktami (kwestia być może losowa);
4. Końcowy obrazek nie zostanie poddany dalszym przekształceniom, konwersji itp.

Ostatni punkt wymaga odrobiny wyjaśnienia.  
Wiele serwisów (Facebook, Google Photos) dla oszczędności miejsca kompresuje obrazki, które na nich umieszczamy. W&nbsp;tym celu dość mocno je przekształcają, czasem zmieniają format. A&nbsp;to daje nam sporą szansę, że sekrety ukryte w&nbsp;obrazkach staną się niemożliwe do odczytania.

Gdybyśmy natomiast trzymali obrazki gdzieś, gdzie pozostają w&nbsp;stanie niezmiennym (dysk własnego urządzenia, Discord sprzed paru lat czy choćby Dysk Google'a), to sekrety jak najbardziej byłyby dostępne.

Te punkty wydają się dość gęstym sitem przesiewowym. Nie wykluczam, że niektóre mogą być łatwe do spełnienia (pkt.&nbsp;1 -- przycinamy *specjalnie po to*, żeby coś ukryć; pkt.&nbsp;2 -- domyślny program jest najłatwiej dostępny). Ale żeby zaszło wszystko naraz, to już musielibyśmy mieć pecha.

W związku z&nbsp;tym **osobiście wątpię, żeby wiele osób bezpośrednio ucierpiało przez Acropalypse**. Ale świat jest wielki, więc gdzieś zapewne trafią się takie przypadki.  
Najgorsze jest to, że zagrożenie działa wstecz. Kiedy pechowy screen raz zostanie zapisany na dysku, to można do niego wrócić w&nbsp;dowolnym momencie. Zapewne różnej maści zbieracze danych już zaktualizowali skrypty i&nbsp;przeszukują swoje kolekcje, szukając nowych tropów.

## Podsumowanie i&nbsp;porady

Sprawa *Acropalypse* może być dla nas przestrogą -- zagrożenia dla prywatności mogą przyjść z&nbsp;najmniej spodziewanej strony. I&nbsp;działać wstecz, więc rzecz wrzucona przed laty do internetu może nas kiedyś ugryźć.

W tej sprawie wyróżniłbym kilku głównych „winowajców”:

* złożoność współczesnych formatów,
* niefrasobliwe wprowadzanie zmian w&nbsp;„złączkach” między systemem a&nbsp;programami,
* dziurawy proces testowania i&nbsp;weryfikacji u&nbsp;Google'a i&nbsp;Microsoftu.

Pierwszy punkt może być trudny do naprawienia, ale firmy jak najbardziej mogłyby co nieco uszczelnić po swojej stronie. Tym niemniej, zamiast na nich polegać, warto samodzielnie zadbać o&nbsp;bezpieczeństwo.

Na pewno nie zaszkodzi **minimalizacja danych na jak najwcześniejszym etapie**. Skoro programy mogą nas zawodzić, to na nich nie polegajmy.

W praktyce: zadbajmy o&nbsp;to, żeby już na *początkowym screenshocie* nie było nic cennego ani tajnego. Chcąc dodać zdjęcie swojej twarzy, nie wycinamy go z&nbsp;rozebranej fotki. Robimy całkiem osobne zdjęcie.

Chcemy zrobić screena pokazującego tylko fragment ekranu, zaś obok jest coś wrażliwego? Zmniejszamy okno, ustawiamy rozmiar powiększenia (w&nbsp;przeglądarkach -- opcje z&nbsp;prawego górnego rogu, obok słowa `Powiększenie`). Następnie naciskamy `Alt+PrintScreen`, żeby zrobić zdjęcie *wyłącznie* naszego aktywnego okna, a&nbsp;nie całego ekranu.

Jeśli szczególnie się obawiamy, to można otworzyć plik w&nbsp;programie graficznym, a&nbsp;następnie zapisać go w&nbsp;innym formacie niż początkowy. Mało co poza samymi pikselami -- czyli tym, co chcemy -- przetrwa taką konwersję.

{% include info.html
type="Powiązane wpisy"
text="Warto przy tym pamiętać o&nbsp;innych potencjalnych pułapkach związanych z&nbsp;plikami, które miałem przyjemność opisać na blogu.  
Pułapka pierwsza -- w&nbsp;zdjęciach mogą być czasem [zaszyte dane z&nbsp;GPS-a](/2021/02/10/gdzie-jestem-zapytaj-moich-zdjec){:.internal}, jasno pokazujące miejsca, w&nbsp;których je zrobiono.  
Pułapka druga -- gdy edytujemy niektóre formaty plików, jak PDF, [nie wystarczy zakrycie tekstu czarnym prostokątem](/2021/10/29/zakrywanie-danych){:.internal}. Bo cały tekst nadal będzie pod spodem, łatwy do skopiowania.
"%}

Życzę Wam fotek bez tajemnic i&nbsp;(jakkolwiek to brzmi) żeby nikt Wam nie przywracał rzeczy uciętych :smile:


