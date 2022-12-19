---
layout: post
title:  "Facebook i patologie automatycznej moderacji"
subtitle: "Świat wokół nas, którego nie zobaczymy."
description: "Świat wokół nas, którego nie zobaczymy."
date:   2022-12-19 11:00:00 +0100
tags: [AI, Cenzura, Internet, Przemyślenia]
firmy: [Facebook]
image:
   path: /assets/posts/fb-cenzura/fb-cenzura-baner.jpg
   width: 1200
   height: 700
   alt: "Obraz przedstawiający dom. U góry normalny, w szarym kolorze. U dołu ten sam obraz, po podświetleniu ultrafioletem, ukazuje płomienie i szkielety w oknie. Góra jest podpisana 'Najpopularniejsze', a dół 'Wszystkie komentarze'."
---

<img src="/assets/posts/fb-cenzura/fb-cenzura-nasz-wielki-dom.jpg" alt="Obraz domu na płótnie. U&nbsp;góry normalny, w&nbsp;szarym kolorze. U&nbsp;dołu ten sam obraz, po podświetleniu ultrafioletem, ukazuje płomienie i&nbsp;szkielety w&nbsp;oknie"/>

{:.figcaption}
Kadry z&nbsp;filmu „Sierota”, przeróbki moje.

> Stanął w&nbsp;ogniu nasz wielki dom  
Dym w&nbsp;korytarzach kręci sznury  
(...)  
Lecz większość śpi nadal, przez sen się uśmiecha  
A kto się zbudzi, nie wierzy w&nbsp;przebudzenie  
Krzyk w&nbsp;wytłumionych salach nie zna ech  
Na rusztach łóżek milczy przerażenie

{:.figcaption}
Jacek Kaczmarski, [„A my nie chcemy uciekać stąd”](https://www.youtube.com/watch?v=YLXvyCJSOwk)  
(w linku wykonanie Przemysława Gintrowskiego).

Wybaczcie mi proszę słowo „przebudzenie”. Wiem że w&nbsp;obecnych czasach może się kojarzyć z&nbsp;bełkotem teoretyków spiskowych. Ale ta piosenka bardzo mi pasowała do grafiki i&nbsp;po prostu musiałem jej użyć :wink:  
A co do samej treści obiecuję, że będzie niespiskowo i&nbsp;praktycznie. Jak zawsze!

Bo widzicie -- mamy na świecie całkiem realny problem z&nbsp;moderowaniem komentarzy na wielkich portalach internetowych. Pomijając niechęć niektórych osób do samej *idei* moderacji, zwyczajnie nie starczyłoby do tego ludzi.  
Zatem na pierwszą linię rzuca się automaty. Wykrywające, usuwające albo chowające wypowiedzi, które są w&nbsp;ich oczach spamem. Rozwiązuje to niektóre problemy, ale też tworzy zupełnie nowe.

Pokażę tutaj, w&nbsp;jaki sposób algorytmy Facebooka chowają niekiedy całkiem ciekawe i&nbsp;wartościowe treści. Przyczyniając się do zamykania ludzi w&nbsp;ich własnych bańkach informacyjnych. I&nbsp;dając amunicję wszelkiej maści spiskowcom i&nbsp;trollom, którzy mogą potem twierdzić, że serwis ukrywa prawdę o&nbsp;świecie.

Na deser będzie też skrypt pozwalający samodzielnie wyłapywać, jakie komentarze Facebook przed nami ukrył.

{% include info.html
type="Streszczenie"
text="Tu coś dla osób, które nie lubią czytać tekstów dłuższych niż tweet i&nbsp;mogłyby nie dotrwać do końca.  
Facebook, zapewne przez wady algorytmów, często ukrywa komentarze pod postami. Żeby je zobaczyć, klikajmy opcję `Najtrafniejsze` i&nbsp;zmieniajmy ją na `Wszystkie`. Można znaleźć fajne rzeczy."
%}

### Spis treści

* [Opcje dotyczące komentarzy](#opcje-dotyczące-komentarzy)
* [Przegląd ukrytych komentarzy](#przegląd-ukrytych-komentarzy)
  * [Przypadek EFF](#przypadek-eff)
  * [Przypadek DuckDuckGo](#przypadek-duckduckgo)
  * [Przypadek Niebezpiecznika](#przypadek-niebezpiecznika)
  * [Przypadek Doniesień z&nbsp;putinowskiej Polski](#przypadek-doniesień-zputinowskiej-polski)
  * [Przypadek Ciekawostkawki](#przypadek-ciekawostkawki)
* [O&nbsp;co w&nbsp;tym wszystkim chodzi?](#oco-wtym-wszystkim-chodzi)
  * [Kwestia uczenia maszynowego](#kwestia-uczenia-maszynowego)
  * [Błędne koło automoderacji](#błędne-koło-automoderacji)
* [Co zrobić?](#co-zrobić)
* [Bonus: wyłapywanie ukrytych komentarzy](#bonus-wyłapywanie-ukrytych-komentarzy)


## Opcje dotyczące komentarzy

Załóżmy, że jesteśmy sobie niedzielnymi użytkownikami Facebooka. Przewijamy *tablicę* (swoją albo jakiejś strony) i&nbsp;dostrzegamy jakiegoś posta. Według podpisu zostawiono pod nim 5&nbsp;komentarzy. Ale kiedy klikniemy, żeby je rozwinąć, widzimy tylko dwa.

Pierwsza myśl -- jeśli w&nbsp;ogóle poświęcimy temu uwagę -- „ktoś je ręcznie usunął”. Zapewne autor posta. Może były spamowe albo obraźliwe?  
Czytamy te dwa komentarze, które zostały. Nic ciekawego, przewijamy dalej. Tak jak miliony innych osób każdego dnia.

A tymczasem prawda jest nieco inna. **Te komentarze wcale nie były usunięte, były tylko ukryte. Przez Facebooka**.

I to raczej nie przez złą wolę czy celowe działanie jakichś ludzi z&nbsp;działu moderacji. Bardziej prawdopodobne wyjaśnienie: ich komputery przeanalizowały treść i&nbsp;wyliczyły... Właściwie nie wiemy co, bo działanie algorytmów jest dla nas nieprzeniknione.

W każdym razie na podstawie tych wyliczeń Fejs ukrył komentarze. A&nbsp;my możemy je odsłonić.  
W tym celu, po pierwszym wyświetleniu listy komentarzy, klikamy na słowo `Najtrafniejsze` (po angielsku `Most relevant` albo `Top comments`), widoczne zaraz pod opcją udostępnienia posta. Rozwinie się lista opcji:

{:.bigspace}
<img src="/assets/posts/fb-cenzura/facebook-komentarze-opcje.jpg" alt="Trzy opcje wyświetlania komentarzy na Facebooku (najtrafniejsze, wszystkie, od najnowszych). Pod każdą z&nbsp;nich znajduje się jej krótki opis."/>

Kiedy z&nbsp;tej listy wybierzemy opcję `Wszystkie komentarze` albo `Najnowsze`, to zapewne zobaczymy ukryte komentarze. Jeśli nadal będzie ich mniej niż według licznika u&nbsp;góry, to znaczy że niektóre zostały usunięte na amen. Może przez autora posta, może przez Facebooka. Ale zwykle zobaczymy coś nowego.

Żeby być uczciwym wobec Facebooka -- nie robią z&nbsp;tego wielkiej tajemnicy. Kiedy przewijamy komentarze, to czasem pojawia się między nimi tekst:

> Wybrano tryb sortowania Najtrafniejsze, więc niektóre odpowiedzi mogły zostać pominięte w&nbsp;wyniku filtrowania.

Dotyczy to jednak dłuższych wymian komentarzy, gdy luki utrudniałyby czytanie dialogu. Wiele innych komentarzy jest niestety chowanych po cichu. 

## Przegląd ukrytych komentarzy

Wiemy już, *jak* odsłaniać komentarze. Spójrzmy teraz, *co* się w&nbsp;nich kryje.

Czasem to rzeczy prozaiczne, faktyczny spam. Gdybyśmy wyłączyli filtr komentarzy pod jakimś mainstreamowym artykułem, to bardzo możliwe, że jedynymi nowinkami byłyby takie wypowiedzi:

{:.bigspace}
{% include comment.html
author="Jakaś Osoba"
source="facebook"
text="**@Jakaś Inna Osoba**{:.red} zobacz haha"
%}

Ale nie dziękujmy jeszcze Facebookowi za to, że chowa przed nami te mądrości. Niestety trafiają się też przypadki bardziej kontrowersyjne.

### Przypadek EFF

Zacznijmy od [profilu *Electronic Frontier Foundation*](https://www.facebook.com/eff/). Jednej z&nbsp;większych organizacji nagłaśniających problemy nadużyć w&nbsp;świecie cyfrowym. Merytorycznej i&nbsp;niespiskowej.

Dygresja: trochę mnie dziwi, że przy ponad 190&nbsp;000 obserwujących rzadko zbierają więcej niż kilkadziesiąt polubień pod postami. Niektóre inne strony, które omawiam w&nbsp;tym wpisie, mają podobne albo kilka razy mniejsze grono odbiorców, ale zaangażowanie dużo większe.

No ale wróćmy do wątku głównego. Po odwiedzeniu ich profilu przewijam w&nbsp;dół i&nbsp;znajduję post z&nbsp;4&nbsp;grudnia 2022, wspominający o&nbsp;platformie [Mastodon](https://joinmastodon.org/) (coraz popularniejszej alternatywie dla Twittera).

{:.bigspace}
{% include info.html
type="Porada"
text="Nie podaję bezpośrednich linków do postów, żebyśmy mogli trochę poćwiczyć szukanie treści.  
Jeśli już minęło sporo czasu od publikacji tego wpisu, to mój przykład z&nbsp;EFF pewnie odpłynął daleko w&nbsp;dół. Żeby łatwo go znaleźć, najpierw wchodzimy na profil EFF. Klikamy w&nbsp;ikonę lupy po prawej stronie, pod nagłówkiem profilu. Wpisujemy `Mastodon`. Potem wybieramy z&nbsp;menu opcję `Wyszukaj \"Mastodon\" na tej stronie`.  
Analogicznie przy kolejnych przykładach. Będę podawał daty dodania postów i&nbsp;słowa pozwalające je znaleźć."
%}

Dzisiaj, 18&nbsp;grudnia, pokazuje mi 7&nbsp;komentarzy przy ustawionym filtrze `Najtrafniejsze`. Widoczny jest jednak tylko komentarz niejakiego Michaela.

{:.bigspace}
{% include info.html
type="Uwaga"
text="Jeśli widzicie więcej komentarzy, to jeszcze o&nbsp;niczym nie przesądza; jak później zobaczymy, możliwe że różnym użytkownikom ukrywa różne treści."
%}

Kiedy zmienimy widoczność na `Wszystkie`, to pojawią się brakujące komentarze. Jak ten:

{:.bigspace-before}
{% include comment.html
source="facebook"
author="Dawn"
text="Twitter twats will laugh at this but we don't want them anyway 🙂"
%}

{:.figcaption}
We wszystkich komentarzach usunąłem albo skróciłem nazwiska i&nbsp;nicki osób prywatnych.

Przy nim akurat mógłby zadziałać prosty filtr „niegrzeczności”, blokujący po złapaniu słowa *twats*.

{:.bigspace}
{% include comment.html
source="facebook"
author="Tom"
text="Twitter is king"
%}

Ten komentarz faktycznie nie miał zbyt wiele treści. Ale tym razem wydźwięk pozytywny (mimo że to miała być lekka prowokacja). Cokolwiek go usunęło, nie był to filtr wulgaryzmów.  
Pod tym komentarzem jest jeszcze kilka, udzielonych w&nbsp;odpowiedzi na te słowa. Ale to akurat logiczne, że ukrycie komentarza-rodzica ukrywa też odpowiedzi, więc nie biorę ich pod uwagę.

Najbardziej kontrowersyjnym ukryciem jest moim zdaniem przypadek trzeci:

{:.bigspace}
{% include comment.html
source="facebook"
author="F.M.A"
text="It's secure from people and corporations who are trying to protect me, and that's all I&nbsp;could possibly ask for."
%}

Komentarz na poziomie, gramatycznie poprawny, nieco antykorporacyjny (*trying to protect me* jest oczywiście ironią). Co więcej, zamieszczająca go osoba ma odznaczenie _Lidera wśród fanów_, czyli często udziela się na stronie.

Ale to odznaczenie nic nie zmienia, komentarz jest domyślnie ukryty. Zresztą patrząc po innych postach EFF, można zobaczyć że **podobny los spotyka wiele komentarzy tej konkretnej osoby**. Czy słusznie? Niektóre komentarze faktycznie są ciut bardziej odjechane, ale nie widziałem nic skandalicznego.

Ten przypadek może być dla nas cenną poszlaką. Być może przy ukrywaniu komentarzy Facebook bierze pod uwagę jakąś abstrakcyjnie rozumianą *reputację użytkowników*.

Pod spodem na profilu EFF znajdziemy jeszcze inny post, z&nbsp;17&nbsp;listopada. Na temat nie tyle Mastodona, co szerszego zjawiska *Fediverse*.  
Tam również są usunięte komentarze. Jeden od tego samego F.M.A. co wcześniej (tym razem nieco bardziej bojowniczy). A&nbsp;także komentarz linkujący do instrukcji przechodzenia na nową platformę:

{:.bigspace}
{% include comment.html
source="facebook"
author="John"
text="[https://fedifinder.glitch.me/](https://fedifinder.glitch.me/){:.red} for help migrating"
%}

Może jakiś użytkownik wypatrywał informacji o&nbsp;alternatywach, chciał zmienić platformę. Ale, nie wiedząc o&nbsp;ukrywaniu komentarzy, właśnie przeoczył pomocny poradnik. Zatem zostanie na Twitterze, zatem podupadnie na zdrowiu psychicznym. Efekt motyla i&nbsp;te sprawy :wink:

### Przypadek DuckDuckGo

DuckDuckGo to przede wszystkim alternatywa dla Google, reklamująca się większym szanowaniem prywatności użytkowników. Czy słusznie -- to osobna sprawa, ale zawsze to kolejny krok z&nbsp;dala od ekosystemu Wujka&nbsp;G.

Pod niektórym postami na [ich profilu](https://www.facebook.com/duckduckgo), które sprawdziłem wyrywkowo, ukryte komentarze faktycznie były głównie spamem, oznaczaniem znajomych i&nbsp;tak dalej.

Ale pod postem nawiązującym do mistrzostw w&nbsp;Katarze (z&nbsp;18&nbsp;listopada, słowa kluczowe `World Cup`) znajdziemy coś ciekawszego. Dwa ukryte linki, podesłane przez osoby bojkotujące zawody. Oto jeden z&nbsp;nich:

{:.figure .bigspace}
<img src="/assets/posts/fb-cenzura/katar-anty-komentarz.jpg" alt="Zrzut ekranu pokazujący komentarz z&nbsp;Facebooka mówiący, że jego autor nie popiera krwawego sportu. Pod spodem znajduje się link do artykułu z&nbsp;Guardiana"/>

Link do *Guardiana*. Nie każdy musi się zgadzać z&nbsp;ich linią redakcyjną; sam mam neutralne podejście, choć cenię niektóre dokonania ich dziennikarstwa śledczego.  
Tak czy siak nie sposób im odmówić, że są gazetą dużą i&nbsp;znaną. To nie jest jakiś link do stronki spiskowej. A&nbsp;jednak komentarz został ukryty.

Nawet gdyby algorytm Facebooka odrzucał z&nbsp;automatu te komentarze, które zawierają sam link i&nbsp;zero treści, to i&nbsp;tak nie dotyczyłoby to tego przypadku. Bo oprócz linku jest parę słów od autora. Krótkich i&nbsp;zrozumiałych.

Co zatem było przyczyną ukrycia? Liczba prób zgłoszenia komentarza? Reputacja autora? Tematyka? Nie dowiemy się.  
A osoby, które jeszcze nie usłyszały o&nbsp;kontrowersjach związanych z&nbsp;mistrzostwami, może nigdy ich nie poznają. Pozostaje im grzeczne przewijanie i&nbsp;konsumowanie treści.

### Przypadek Niebezpiecznika

Spójrzmy na jakąś polską stronę! Na przykład [Niebezpiecznika](https://www.facebook.com/niebezpiecznik), jedną z&nbsp;większych poświęconych cyberbezpieczeństwu. Ale, jako że to nie moja branża, niech będzie sprawa spoza ich codziennej działalności.

Apple wypuściło na swoją platformę Apple TV nowy serial, który w&nbsp;polskim tłumaczeniu nazywa się... właśnie „Niebezpiecznik”.  
W odpowiedzi ten prawdziwy Niebezpiecznik opublikował posta (3 listopada, słowa kluczowe `Apple TV`). Proszą o&nbsp;nagłośnienie sprawy i&nbsp;linkują do artykułu pokazującego, w&nbsp;jaki sposób taka kolizja nazw może zaszkodzić ich marce.

Poukrywane komentarze są różne. Mem z&nbsp;Clintem Eastwoodem, jakieś losowe śmieszki. Komentarz nieironicznie twierdzący, że... powinni się cieszyć zainteresowaniem od Apple :roll_eyes: Ale schowano też konkrety, jak link do strony pozwalającej zgłaszać Apple naruszanie praw autorskich. 

Tak jak wyżej, raczej nie rozpracujemy zasad, jakimi kierował się algorytm.  
Ale ten przykład jest dla nas ciekawy pod innym względem. Ukryto również komentarz, który zebrał 21&nbsp;reakcji (polubień i&nbsp;śmiechów) oraz odpowiedź samego Niebezpiecznika. Co doprowadziło do ukrycia również tejże odpowiedzi.

{% include comment.html
source="facebook"
author="Tomasz"
text="Jeszcze zaraz Was pozwą za używanie ich nazwy."
%}

{:.bigspace-after}
{% include comment.html
source="facebook"
author="Niebezpiecznik"
type="reply"
avatar="/assets/posts/fb-cenzura/niebezpiecznik-awatar.png"
text="**Tomasz** byle nie kazali płacić za reklamę na każdym iPhonie, bo będziemy musieli sprzedać wszystkie bitkojny żeby pokryć taki rachunek 😉"
%}

Gdyby ktoś postawił tezę „*Odpowiedzi od strony-autora zawsze chronią komentarze przed schowaniem*”, to tu mielibyśmy dowód na jej fałszywość.

**Lajki oraz odpowiedzi od autora posta nie chronią przed ukryciem komentarza**. Albo trochę chronią, ale nie zawsze. W&nbsp;każdym razie autorzy raczej nie uratują swoich użytkowników przez wchodzenie z&nbsp;nimi w&nbsp;interakcje.

### Przypadek Doniesień z&nbsp;putinowskiej Polski

Tutaj spojrzymy na wątek, który jest mi dość bliski. Bo sam też o&nbsp;nim pisałem. Chodzi o&nbsp;[sprawę wokół amerykańskiej filii Syngenty]({% post_url 2022-07-27-syngenta-atrazyna %}){:.internal} oraz ich produktu, atrazyny.

W skrócie: substancja ta miała zwyczaj przedostawać się do wód gruntowych i&nbsp;źle wpływać na układ hormonalny organizmów wodnych. Kiedy różni naukowcy zaczęli nagłaśniać sprawę, to koncern, zamiast dokładniej zbadać sprawę, wziął się za niszczenie ich reputacji.

*[Doniesienia z&nbsp;putinowskiej Polski](https://www.facebook.com/PutinowaPolska)* to profil, na którym nie spodziewalibyśmy się tej sprawy. Na co dzień pisze o&nbsp;aferach i&nbsp;skandalach polityczno-militarnych, zwykle z&nbsp;Rosją w&nbsp;tle. A&nbsp;jednak, o&nbsp;dziwo, sprawa żab również trafiła do komentarzy.

Kiedyś mianowicie na *Doniesieniach* zagościła informacja o&nbsp;tym, że sąd nakazał znanemu showmanowi z&nbsp;USA wypłatę odszkodowania. Opublikowano ją 13&nbsp;października, można wyszukać po słowach `była mistyfikacją`.

Chodzi o&nbsp;osobę o inicjałach A.J. Zapewne kojarzycie. Facet miał zwyczaj brać różne informacje, czasem oparte na faktach, i&nbsp;klecić z nich niestworzone teorie spiskowe. Nie wymienię go z&nbsp;nazwiska, żeby nie przyciągnąć foliarzy na bloga :wink:.

Jedna z&nbsp;teorii showmana bazowała właśnie na „żabiej aferze”. W&nbsp;komentarzach pojawiły się zatem zarówno osoby śmieszkujące z&nbsp;interpretacji A.J., jak też ludzie wyjaśniający, o&nbsp;co w&nbsp;tym naprawdę chodziło. **I nie, Facebook nie pousuwał faktów na temat afery**. Wykazał się natomiast kolejną niekonsekwencją. Spójrzmy:

{:.figure .bigspace}
<img src="/assets/posts/fb-cenzura/atrazine-porownanie-cenzura.jpg" alt="Zrzut ekranu z&nbsp;Facebooka pokazujący dwa komentarze, jeden pod drugim. Pierwszy odsyła do artykułu naukowego na temat wpływu atrazyny, ten pod spodem do filmiku n&nbsp;YouTubie, z&nbsp;miniaturą żaby w&nbsp;wodzie i&nbsp;podpisem 'Gay Frogs: A&nbsp;Deep Dive'."/>

Dwa linki od tej samej osoby, w&nbsp;zbliżonym czasie. Pierwszy do artykułu naukowego na stronie uczelni, w&nbsp;domenie *gov*. Drugi do filmiku na YouTubie. Link numer jeden ukryty, ten do YouTube'a przetrwał.

I choć nie mam nic do filmu Okiego -- jest bardzo solidnym omówieniem sprawy! -- to jednak decyzja algorytmu jest ciut dziwna. Sugeruje, że chowanie linków niekoniecznie bazuje na jakiejś *reputacji domen*. I&nbsp;nie chodzi tu raczej o&nbsp;reputację linkującego, bo ten w&nbsp;obu przypadkach był ten sam.

Bardzo podobną niekonsekwencję zobaczymy w&nbsp;ukrywaniu komentarzy twierdzących, że to samo mogłoby spotkać znanego polskiego znachora:

{% include comment.html
author="Jakub"
source="facebook"
text="Z*????*{:.cover} powinien tak skończyć też."
%}

{:.bigspace-after}
{% include comment.html
author="Michal"
source="facebook"
text="**Doniesienia z&nbsp;putinowskiej Polski**{:.red} przydałoby się żeby tak w&nbsp;Polsce J*????*{:.cover} Z*????*{:.cover} też tak potraktowano za naciąganie na suple 😁"
%}

Ten sam wydźwięk. Pierwszy komentarz schowany, drugi nie. Skąd różnica? Czy możliwe, że „powinien tak skończyć” skojarzyło się algorytmowi z&nbsp;jakimiś agresywniejszymi komentarzami i&nbsp;dlatego oberwało?

Możemy też pomyśleć, że krótkie komentarze są gorzej punktowane; na przykład skojarzą się algorytmom z&nbsp;kłótniami internetowymi, zakończonymi zbanowaniem jakiegoś uczestnika.  
Ale Facebook schował również inny komentarz. Który wprawdzie wywołał drobną dyskusję, ale był dość refleksyjny, bez bluzgów. I&nbsp;długi:

{:.bigspace}
{% include comment.html
author="Pol..."
source="facebook"
text="Świat nie jest czarno-biały. Jak napisałem, nie znam gościa, nie bronię go, krytykuję system używający sądów i&nbsp;finansowej kary śmierci do kneblowania ludzi.  
(...)  
dostaniesz nakaz sądowy i&nbsp;pozew na 100mln za oczernianie koncernu. Oczywiście możesz spróbować wynająć naukowców, zrobić badania na tysiącach osób i&nbsp;się obronić przedstawiając wiarygodniejsze badania niż te, którymi dysponuje koncern, ale raczej ci się nie uda. Powstał system, który przypomina wolność słowa w&nbsp;Chinach lub Korei Płn, nie możesz tam pewnych osób krytykować ani nawet publicznie wątpić, bo za słowa zostaniesz zniszczony, nie zostaniesz wyśmiany, zostaniesz zniszczony, zabiorą ci dom, samochód, pieniądze, stracisz rodzinę. Dlatego ten system jest zły, bo zamyka usta nie tylko tym złym, zamyka usta wszystkim."
%}

### Przypadek Ciekawostkawki

Już nam runęło trochę potencjalnych założeń na temat autocenzora z&nbsp;Facebooka, ale możemy pomyśleć sobie jedno -- być może ma jakąś swoją czarną listę linków?

Spójrzmy do miejsca bardziej mainstreamowego. *[Ciekawostkawka](https://www.facebook.com/groups/277362736085803)* -- grupa licząca ponad 250&nbsp;000 użytkowników i&nbsp;służąca wymienianiu się mniej znanymi faktami z&nbsp;życia. Znajdziemy tu pełen przekrój społeczeństwa! Niektóre tamtejsze komentarze to okrutny rak, ale trafia się też szczere złoto.

Tutaj również wrzucono temat wyroku dla showmana z&nbsp;USA. Również śmieszkowano z&nbsp;jego słów o&nbsp;żabach. Jeden użytkownik, chcąc pokazać realną aferę, podlinkował ten sam film Okiego z&nbsp;YouTube'a, który pokazałem wyżej.

Tylko że na *Doniesieniach* link został przepuszczony, w&nbsp;przeciwieństwie do artykułu naukowego od tej samej osoby. **A na Ciekawostkawce został ukryty**. Pozostaje chyba odrzucić kolejne założenie na temat reguł działania automoderacji. To raczej nie była żadna *czarna lista filmów*.

Być może przyczyną była sama postać komentującego z&nbsp;Ciekawostkawki, który kilka razy nagłaśniał na tej grupie kontrowersyjne (ale realne) sprawy? A&nbsp;może nie, bo wiele innych jego komentarzy przepuściło bez filtrowania.

## O&nbsp;co w&nbsp;tym wszystkim chodzi?

### Wytłumaczenie Facebooka

Najpierw oddajmy głos samemu Facebookowi. W&nbsp;zakładce z&nbsp;informacjami sami poruszają [kwestię układania komentarzy pod postami](https://www.facebook.com/help/539680519386145/):

{:.bigspace}
> Wyświetlane komentarze są objęte rankingiem i&nbsp;występuje większe prawdopodobieństwo, że zobaczysz wysokiej jakości komentarze odpowiednie dla siebie. To oznacza większe prawdopodobieństwo, że u&nbsp;góry zobaczysz:  
* Komentarze lub reakcje znajomych.  
* Komentarze ze zweryfikowanych profili i&nbsp;stron.  
* Komentarze z&nbsp;największą liczbą polubień i&nbsp;odpowiedzi.

W zakładce [*making public comments more meaningful*](https://about.fb.com/news/2019/06/making-public-comments-more-meaningful/) przedstawicielka Facebooka pokazuje więcej przykładów. Przy szeregowaniu komentarzy brane są ponoć pod uwagę opinie z&nbsp;losowych ankiet wśród użytkowników. Albo historia interakcji (co było najczęściej lajkowane i&nbsp;wywoływało dyskusję).

Oba teksty sugerują, że jakieś znaczenie ma fakt, czy pod komentarzem napisał coś sam autor posta. Ale, jak widzieliśmy przy Niebezpieczniku, nie jest to reguła absolutna. Potrafiło schować lajkowany komentarz wraz z&nbsp;ich odpowiedzią (mimo że są nie tylko autorami posta, ale też kontem oficjalnie zweryfikowanym).

Informacje od Fejsa dają niby jakiś wgląd w&nbsp;algorytm. Tylko że to wszystko jest wymienione po magicznym słowie *including*, co oznacza że tak naprawdę kryteriów może być znacznie więcej. I&nbsp;zapewne tak jest, bo Facebook bez wątpienia stosuje metody uczenia maszynowego.

### Kwestia uczenia maszynowego

O [metodach uczenia maszynowego, nazywanych AI]({% post_url 2021-03-03-ai-wspolczesni-szamani %}){:.internal} (sztuczną inteligencją), już kiedyś napisałem.  
Mówiąc krótko -- nie mają nic wspólnego z&nbsp;prawdziwą, „świadomą” inteligencją. Jasne, to bardzo złożone metody i&nbsp;są stale doskonalone. Ale to wciąż tylko narzędzie. Tak jak opcja stworzenia wykresu albo autoformatowania w&nbsp;Excelu.

W ramach uczenia maszynowego wrzucamy komputerowi wiele różnych danych. A&nbsp;on je przetwarza i&nbsp;ma za zadanie wychwycić, które z&nbsp;nich często pojawiają się razem.  
„Masz tu przykłady komentarzy, które ludzcy moderatorzy zbanowali. A&nbsp;tu takie, które są w&nbsp;porządku. Znajdź cechy, które pozwalają rozróżnić te grupy”.

Komputer drąży, mieli, znajduje jakieś swoje powiązania. Tylko że kompletnie nie muszą one odpowiadać temu, co pomyślałby żywy, świadomy człowiek. To wypadkowa wielu rzeczy, jak na przykład długość komentarza, data, liczba wszystkich komentarzy danej osoby...

Nie wyobrazimy sobie tego wszystkiego, podobnie jak nie bylibyśmy w&nbsp;stanie przeprowadzić w&nbsp;głowie fizycznej symulacji.  
Ale pozwolę sobie chwilę poteoretyzować. Jeśli komputer chciałby rozdzielić komentarze na różne grupy, to jakie cechy mógłby uznać za istotne?

* Do banowania kont zapewne nieraz dochodzi po kłótniach w&nbsp;komentarzach. Jak kłótnie, to wulgaryzmy. Zatem algorytm mógłby sobie stworzyć nieformalne „czarne listy słów”.

  Efektem ubocznym mogłoby być chowanie wszelkich komentarzy z&nbsp;wulgaryzmami. Nawet jeśli ich wydźwięk był pozytywny (*it's f\*cking delicious*). Albo, co gorsza, jeśli pojawi się jakieś słowo dwuznaczne dla algorytmu („jakie polecacie pedały do roweru górskiego?” na grupce sportowej).

* W&nbsp;czasach Covida było wiele ożywionych dyskusji. Ludzie mogli się licytować na artykuły naukowe, zanim ktoś stracił cierpliwość i&nbsp;dostał bana za agresję.

  Ale algorytm, patrząc na takie przypadki, mógłby uznać *każdy* komentarz z&nbsp;linkiem do strony amerykańskiej agencji ds. zdrowia za coś drażliwego. Mimo że to artykuły naukowe. Jest szansa, że częściej pojawiają się w&nbsp;komentarzach podczas ostrych dyskusji niż przyjaznych rozmów.

* Jeśli algorytm patrzy na polubienia i&nbsp;reakcje, to pierwsze wrażenia mogą zakłamywać obraz.

  Zapewne wiele osób wrzucało linki do kontrowersji wokół Mundialu na grupy fanów piłki.  
  Tylko że obstawiałbym, że ci ludzie nie przyjęli tego ciepło. Nie chcą widzieć ciemnych stron, chcą widzieć kopanie piłki. W&nbsp;takich warunkach komentarze nie zebrałyby lajków, a&nbsp;może nawet doprowadziłyby do zgłoszeń o&nbsp;usunięcie.  
  Na ogólniejszych grupach te skandale mogłyby lepiej się przyjąć, zaskoczyć ludzi, zebrać reakcje. Ale nie zbiorą niczego, jeśli algorytm już do tej pory sobie ubzdurał, że te linki lepiej chować.

Oczywiście wszystkie powyższe przemyślenia musiałbym wyrzucić do kosza, gdyby dla algorytmu miały znaczenie nie tylko cechy komentarzy, ale również mojego własnego konta.  
Czy tak jest? Nie wiem. Jak już podkreślałem, algorytm to trochę czarna skrzynka. Choć słowa „*zobaczysz komentarze odpowiednie dla siebie*” z&nbsp;oficjalnych wyjaśnień Fejsa niestety to sugerują.

Ale wiem coś innego. Gdyby algorytm kierował się cechami naszego konta, to **każdy dostawałby własny, szyty na miarę mikroświat. Tylko że niekompletny w&nbsp;porównaniu z&nbsp;tym prawdziwym**. Odarty z&nbsp;tego, co zdaniem komputerów Facebooka do nas nie pasuje.

### Błędne koło automoderacji

Ktoś mógłby pomyśleć: „Ale o&nbsp;czym my tu w&nbsp;ogóle gadamy? Chcesz widzieć wszystko bez cenzury, to klikaj taką opcję”.  
Na poziomie indywidualnym tak może być. Ale nieprzeniknione algorytmy mogą mieć konsekwencje również na poziomie społecznym, światowym.

Dochodzi do swoistego *sprzężenia zwrotnego*:

* Jakiś rosyjski troll spamuje platformę treściami dezinformacyjnymi.
* Zostaje zgłoszony i&nbsp;zbanowany.
* Algorytm analizuje, co było w&nbsp;jego komentarzach. Staje się wyczulony na pewne treści.

  Gdyby świat był idealny, to tu byśmy skończyli. System moderacji działałby trochę jak układ odpornościowy człowieka. W&nbsp;praktyce oczywiście nie jest tak fajnie.

* Parę teorii spiskowych było przeinaczeniem nieco prawdziwszych afer. Przeczulony algorytm ukrywa również wzmianki o nich. Treści prawdziwe i&nbsp;wartościowe, choć kontrowersyjne.
* Kręgi spiskowe to zauważają i&nbsp;pokazują wyraźne dowody na to, że platforma coś chowa. Nie nazywają tego wadami algorytmu, tylko celowym „ukrywaniem prawdy”.
* Takie argumenty przekonują nawet osoby nieco bardziej umiarkowane. Po zradykalizowaniu zaczynają spamować platformę dezinformacją...

I tak dalej. Krąg się zamyka, świat się radykalizuje.

Gdyby chodziło tylko o&nbsp;komentarze, to jeszcze pół biedy. Ale na podobnie niejasnych zasadach może dochodzić również [do banowania kont -- firmowych i&nbsp;nie tylko](https://itbiznes.pl/felieton/biznes-na-facebooku-blokada/).  
I nie jest to problem samego Facebooka. Również YouTube „szczyci się” [nieprzeniknionymi regułami]({% post_url 2022-04-18-youtube-ai-reklamy %}){:.internal}  usuwania kont i&nbsp;wyłączania opcji zarobkowania.

Wielkie platformy chętnie przygarniają użytkowników, twierdząc że miejsca starczy dla wszystkich. Wabią inwestorów, mówiąc że mają nowoczesne techniki moderacji, że to świetna przestrzeń do zarabiania na reklamach.  
Brakuje refleksji nad tym, że cały ten system jest niestabilny, a&nbsp;jego słabości są cały czas wykorzystywane. Również przez siewców dezinformacji.

W takich realiach wniosek wydaje mi się prosty -- **bycie przeciwko algorytmicznej cenzurze nie jest oznaką myślenia spiskowego. To wręcz racjonalna próba uspokojenia świata**. Który w&nbsp;obecnym układzie tylko coraz bardziej się radykalizuje.

## Co zrobić?

Po stronie Facebooka wystarczyłoby, żeby przestał domyślnie ukrywać pełnoprawne komentarze.

Ktoś powie, że upraszczam? Ale to naprawdę nie takie trudne. Wciąż mogliby łatwo, zwykłym dopasowaniem tekstu, wyłapywać przypadki, gdy komentarz jest jedynie wywołaniem znajomej osoby albo paroma emotami.

A poza takim spamem? Po prostu nie chować. Nie niańczyć użytkowników. Niech ludzie widzą czasem, że świat ma całkiem realne, ciemne strony. Tryb `Wszystkie` powinien być tym domyślnym.

To tyle, jeśli o&nbsp;Facebooka chodzi. A&nbsp;co z&nbsp;użytkownikami?

Osoby piszące komentarze mogłyby się starać, żeby były nieco dłuższe i&nbsp;pozbawione wulgaryzmów. Szansa na ukrycie byłaby raczej mniejsza. A&nbsp;jako efekt uboczny -- internet stałby się nieco bardziej kulturalny :wink:

A my, czytelnicy komentarzy? Rozwiązanie jest póki co proste. Zawsze po rozwinięciu komentarzy klikajmy opcję `Wszystkie`. Zobaczymy świat takim, jakim jest naprawdę.

Jeśli odkryjemy, że jakieś ciekawe komentarze zostały schowane, to możemy o&nbsp;tym napisać własny komentarz pod tym samym postem, przekonując ludzi do odhaczenia filtra.  
Gdyby ktoś się nam dziwił i napisał, że wszystko widzi, to pamiętajmy że filtry mogą różnie działać dla różnych osób.

To tyle na dziś! Chyba że ktoś chce osobiście wyłapać parę przypadków poukrywanych komentarzy. W&nbsp;takim wypadku służę sprawdzonym (choć tylko przez siebie) skryptem ułatwiającym pracę.

## Bonus: wyłapywanie ukrytych komentarzy

W jaki sposób możemy znajdować komentarze, które Facebook przed nami ukrył?

Mówiąc najogólniej: trzeba rozwinąć wszystkie komentarze widoczne w&nbsp;trybie ocenzurowanym. Skopiować je i&nbsp;gdzieś zapisać. Następnie zmienić tryb na nieocenzurowany i&nbsp;znów je porozwijać. Również zapisać. I&nbsp;porównać ze sobą obie wersje.

Oczywiście byłoby to mocno upierdliwe, gdybyśmy chcieli wszystko robić ręcznie. Dlatego stworzyłem skrypt Pythona, który **wykonuje porównywanie i&nbsp;oznaczanie usuniętych komentarzy za nas (rozwijać niestety musimy sami)**.

W najprostszym przypadku:

1. rozwijamy komentarze w&nbsp;trybie `Najtrafniejsze` i&nbsp;kopiujemy post do schowka;
2. włączamy skrypt i&nbsp;naciskamy `Enter`;
3. rozwijamy komentarze w&nbsp;trybie `Wszystkie`, kopiujemy post do schowka;
4. wracamy do okna ze skryptem i&nbsp;naciskamy `Enter`.

I tyle. W&nbsp;aktywnym folderze powstanie nam, w&nbsp;formacie HTML, lista wszystkich komentarzy. Te schowane przez Facebooka będą oznaczone czerwonym brzegiem. Można zobaczyć, co platforma przed nami ukrywa :sunglasses:

Żeby już nie zabierać miejsca w&nbsp;tym wpisie, przeniosłem instrukcję obsługi skryptu do [osobnego samouczka](/tutorials/comment-diff){:.internal}. Zapraszam!

