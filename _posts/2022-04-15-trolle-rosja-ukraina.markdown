---
layout: post
title:  "Cyfrowy front. Walczymy z trollami wbrew korporacjom"
subtitle: "Gdy Facebook i Twitter nie pomogą, musimy radzić sobie sami."
description: "Gdy Facebook i Twitter nie pomogą, musimy radzić sobie sami"
date:   2022-04-15 15:10:00 +0100
tags: [Centralizacja, Manipulacja, Porady, Ukraina]
firmy: [Facebook, Google, Mozilla, Twitter]
image: "trolle/demon-slayer-trolle-baner.jpg"
image-width: 1200
image-height: 700
---

Dawno się nie widzieliśmy! Poprzedni wpis stworzyłem pod koniec lutego, zapowiadając kolejne „w najbliższym czasie”.

Ale rosyjska inwazja na Ukrainę nieco odsunęła te plany. Jako zbieracz informacji miałem pełne ręce roboty, zapisując zdarzenia na bieżąco, zanim przepadną w&nbsp;odmętach internetu.

Teraz, po ponad miesiącu, wracam do pisania. Przynosząc coś na czasie, czyli wpis związany z&nbsp;wojną. Ale nie fizyczną, bo geopolityka to nie moje rewiry.

Zamiast tego **spojrzymy na wojnę informacyjną -- działalność rosyjskich trolli, czyli kont szerzących propagandę**.  
One również prowadzą swoistą inwazję. Tyle że nie są od nas oddalone o&nbsp;setki kilometrów. Są wśród nas, w&nbsp;tych samych sekcjach komentarzy.

Po krótkim omówieniu sytuacji pokażę kilka sposobów na znajdowanie i&nbsp;zgłaszanie trolli. Od najprostszych, dostępnych dla każdego, po półautomatyczne, wymagające większego zaangażowania. Wcielając je w&nbsp;życie, możemy walczyć na internetowym froncie w&nbsp;sposób systematyczny i&nbsp;zorganizowany.

<img src="/assets/posts/trolle/demon-slayer-trolle-baner.jpg" alt="Kadr z&nbsp;anime pokazujący postać wykonującą znad głowy płomienne cięcie uderzające w&nbsp;kark drugiej postaci. Postać zadająca cios ma twarz zakrytą logiem tego bloga, a&nbsp;postać uderzona ma zamiast twarzy rysunkową twarz typu trollface, tu w&nbsp;wersji przestraszonej."/>

{:.figcaption}
Źródło: anime *Demon Slayer* (jap. *Kimetsu no Yaiba*). Przeróbki moje.

# Spis treści

* [Wprowadzenie – po co?](#wprowadzenie--po-co)
* [Postacie w&nbsp;tej historii](#postacie-wtej-historii)
  * [Agresorzy – trolle](#agresorzy--trolle)
  * [Kapryśne mocarstwa – Facebook i&nbsp;Twitter](#kapryśne-mocarstwa--facebook-itwitter)
  * [Sojusznicy – Brand24, NASK i&nbsp;inni](#sojusznicy--brand24-nask-iinni)
* [Metody walki](#metody-walki)
  * [Znajdowanie trolli](#znajdowanie-trolli)
  * [Zgłaszanie przez platformy (najgorsza opcja)](#zgłaszanie-przez-platformy-najgorsza-opcja)
  * [Wrzucanie linków na zglostrolla.pl](#wrzucanie-linków-na-zglostrollapl)
  * [Wrzucanie oczyszczonych linków](#wrzucanie-oczyszczonych-linków)
  * [Zapisywanie informacji na później](#zapisywanie-informacji-na-później)
  * [Bonus: pomocniczy skrypt Pythona](#bonus-pomocniczy-skrypt-pythona)
  * [Bonus 2: dodatek do przeglądarki](#bonus-2-dodatek-do-przeglądarki)
  * [Walka z&nbsp;trollami przez komórkę](#walka-ztrollami-przez-komórkę)
* [Podsumowanie](#podsumowanie)

## Wprowadzenie -- po co?

Moja motywacja jest prosta jak budowa cepa. Ukraina jest spokojniejszym sąsiadem niż Rosja, więc chciałbym żeby była niepodległa. Trolle chcą wmawiać, że jest na odwrót -- „Rosja to bohater, a&nbsp;Ukraina to wróg”. Zatem nie lubię trolli.

Ale świat nie jest czarno-biały, wątpliwości można mieć zawsze.  
„Czy nagonka na trolle nie pogłębia klimatu polowania na czarownice?”.  
„Czy zgłaszanie nie będzie miało skutku ubocznego -- normalizowania cenzury i&nbsp;oddawania władzy wielkim organizacjom?”.

To sensowne wątpliwości, więc krótko się do nich odniosę.

Jeśli chodzi o&nbsp;polowanie na czarownice, to rozumiem obawy. Widziałem już, jak ruskimi onucami nazywano osoby, które po prostu chciały dyskutować w&nbsp;sposób mniej emocjonalny.  
Natomiast w&nbsp;tym przypadku, mówiąc o&nbsp;trollach, mam na myśli bardzo szczególne konta -- pod względem aktywności, zasięgów, powiązań. Nie nawołuję do emocjonalnej nagonki, tylko do precyzyjnych działań. Przeciw prowokatorom, którzy ów klimat wrogości tworzą.

Kolejna sprawa: cenzura. Jeśli walka z&nbsp;trollami, to pewnie zgłaszanie Facebookowi i&nbsp;spółce. Czy w&nbsp;ten sposób nie wzmacniamy ich władzy?  
Te obawy też mogę uspokoić. **W walce z&nbsp;trollami internetowi giganci są częściej przeszkodą niż sojusznikiem**. Wpis będzie właśnie o&nbsp;tym, w&nbsp;jaki sposób można się organizować i&nbsp;działać niezależnie od nich.

A to, że większe organizacje (rządowe i&nbsp;prywatne) wykorzystują kryzysy do umocnienia wpływów, to zasada stara jak świat. Nasza postawa wobec trolli nic tu nie zmieni, więc nie widzę sensu w&nbsp;przymykaniu na nich oka w&nbsp;myśl zasady „wróg mojego wroga”.

Ostatecznie, jeśli ktoś nie widzi siebie w&nbsp;walce z&nbsp;trollami, może wykorzystać część wiedzy z&nbsp;tego wpisu przeciw innym organizacjom wykorzystującym fałszywe konta. Jak szemrane agencje marketingowe.

A teraz do rzeczy. Jak wygląda cyfrowy front i&nbsp;w jaki sposób można się na nim wykazać?

## Postacie w&nbsp;tej historii

# Agresorzy -- trolle

> Trolling, lying, because ignorance is bliss  
Manipulating, faking identities  
Watch the walls come down  
I'm gonna break you now, put you out, lights out  
And if you have a&nbsp;heart, I'm gonna rip it out  

{:.figcaption}
Dead by April, „Can You See The Red”.

Główni antagoniści. Czasem osoby siedzące w&nbsp;Rosji i&nbsp;wklejające masowo propagandowe komunikaty. Czasem opłacani Polacy. Innym razem -- podkupione lub przejęte stronki, które na co dzień zajmują się inną działalnością.  
Ze wszystkich tych źródeł spływają wiadomości, które mają dotrzeć do jak największego grona odbiorców. **Promując rosyjską politykę zagraniczną, wrogość i&nbsp;nieufność wobec Ukraińców, a&nbsp;czasem zwykły chaos**.

Komunikaty nie zawsze są toporne i&nbsp;całkiem zmyślone. Bywają oparte na faktach, tylko że je wyolbrzymiają i&nbsp;dodają własną narrację. Do tej pory pojawiły się na przykład takie:

* „Nadchodzi wielki kryzys, zabraknie paliwa i&nbsp;potrzebnych produktów”.

  Komunikat wykorzystujący chaotyczną sytuację świeżo po wybuchu wojny. Spowodował panikę, [kolejki](https://www.rmf24.pl/fakty/polska/news-dlugie-kolejki-na-stacjach-orlen-uspokaja-paliwa-nie-zabrakn,nId,5853044) na stacjach benzynowych, brak gotówki w&nbsp;wielu bankomatach.

* „Wśród uchodźców jest wielu agresywnych imigrantów pochodzenia arabskiego”.

  Ilustrowano to zdjęciami osób o&nbsp;śniadej skórze, tyle że zazwyczaj studentów i&nbsp;turystów ewakuujących się z&nbsp;Ukrainy. Do jednej prawdziwej sytuacji (agresywnego mężczyzny, który odgryzł palec ratownikowi) dopisano historię o&nbsp;chaosie na ulicach Przemyśla.   
  Wskutek tych plotek do miasta [przybyły kibolskie gangi](https://www.euractiv.pl/section/migracje/news/przemysl-wojna-rosja-ukraina-putin-kibole-narodowcy-fake-news-medyka/) szukające zaczepki.

* „Działania Rosji mają na celu walkę z&nbsp;nazistami”.

  Podaje się tu przykład batalionu „Azow”, który faktycznie miał swego czasu trochę neonazistów w&nbsp;swoich szeregach. Ale [są mniejszością](https://pl.wikipedia.org/wiki/Pu%C5%82k_%E2%80%9EAzow%E2%80%9D) nawet w&nbsp;samym pułku, tym bardziej w&nbsp;ukraińskiej armii, nie mówiąc o&nbsp;całym kraju.  
  Rosyjska propaganda przedstawia ich z&nbsp;kolei jako znaczącą siłę na skalę całej Ukrainy.

* „Działania Rosji mają na celu powstrzymanie ataków biologicznych”.
  
  Faktami w&nbsp;tej sprawie są między innymi [inwestycje](https://en.wikipedia.org/wiki/National_Endowment_for_Democracy) amerykańskiego NED (organizacji finansującej oddolne działania w&nbsp;interesie USA), istnienie na obszarze Ukrainy kilku laboratoriów.  
  Ale dorabianie do tego historii, jakoby w&nbsp;tych laboratoriach tworzyło się broń biologiczną dla USA, a&nbsp;Rosja próbowała nie dopuścić do jej użycia? Bądźmy poważni :wink:

Czasem trolli zdradza słaba znajomość polskiego i&nbsp;korzystanie z&nbsp;automatycznego tłumaczenia. Tutaj mamy na przykład „WHO told” w&nbsp;nagłówku angielskim (WHO = World Health Organization). Błędnie tłumaczone jako „KTO powiedział” w&nbsp;polskiej wersji:

{:.figure}
<img src="/assets/posts/trolle/troll-who-autotranslate.jpg" alt="Zrzut ekranu z&nbsp;Nittera pokazujący posta z&nbsp;polskim tekstem. Pod spodem znajduje się link do artykułu ze strony Great Game India, z&nbsp;angielskim nagłówkiem, zilustrowanego zdjęciem postaci w&nbsp;kombinezonie ochronnym."/>

{:.figcaption}
Źródło: Post z&nbsp;Twittera, ale oglądany przez Nittera.

Jeśli chodzi o&nbsp;wygląd trolli, nie ma jednej reguły. **Dość popularne jest dodawanie polskich flag, żeby wzbudzić zaufanie**. Na Facebooku do obrazka profilowego, na Twitterze do nazwy konta.

Jeśli treść jest ewidentnie propagandowa, ale zdjęcie pokazuje prawdziwego człowieka, to warto je zapisać i wyszukać. Może się na przykład okazać, że to pani analityk z&nbsp;francuskiego banku, a&nbsp;zdjęcie podkradziono z&nbsp;jej LinkedIna :wink:

<img src="/assets/posts/trolle/troll-image-search.jpg" alt="Kolaż złożony z&nbsp;dwóch obrazków. Na pierwszym widać informacje profilowe z&nbsp;Twittera: zdjęcie schludnie ubranej kobiety, enigmatyczny opis profilu oraz informację, że stworzono go w&nbsp;2016 roku. Dokładne dane są zasłonięte. Drugi obrazek to zrzut ekranu pokazujący wyniki wyszukiwania obrazka w&nbsp;Google. Czerwoną ramką otoczono pierwszy wynik, profil znaleziony na stronie LinkedIn. Fragmenty tekstu sugerują, że to Francuzka, pracownica działu analizy ryzyka."/>

# Kapryśne mocarstwa -- Facebook i&nbsp;Twitter

Dwaj giganci mediów społecznościowych, na których skupię się w&nbsp;tym wpisie.  
Na pozór mogą się wydawać naszymi sojusznikami. W&nbsp;końcu oferują opcje zgłaszania postów i&nbsp;komentarzy. Poza tym twierdzą że coś robią. Czasem pochwalą się, że [zbanowali jakieś grupy](https://www.rmf24.pl/raporty/raport-wojna-z-rosja/news-meta-usuwa-grupy-z-facebooka-nawolywaly-m-in-do-protestow-pr,nId,5946692#crp_state=1) siejące dezinformację.

Tylko że, niestety, wszystko dzieje się za zamkniętymi drzwiami. **Poza okazjonalnym komunikatem PR-owym nie dostajemy wielu informacji**. Jakie konta należały do zbanowanych grup? Jaki przekaz je łączył? Jakie wnioski na przyszłość możemy wyciągnąć? Nie dowiemy się.

Zresztą z&nbsp;tym banowaniem też bywa różnie. Czasem można „spaść z&nbsp;rowerka” przez naprawdę niewinne rzeczy. Innym razem, po zgłoszeniu czegoś poważnego, użytkownicy dostają wiadomość że platforma [nie widzi problemu](https://nitter.net/search?f=tweets&q=facebook+%22standard%C3%B3w%22&e-nativeretweets=on&since=&until=&near=).

Dlaczego tak jest? Scenariusz optymistyczny: platformy wolą przepuścić wielu winnych niż skazać jednego niewinnego.  
Bardziej pesymistyczny: usuwanie użytkowników nie jest dobre dla ich biznesu. To mniej wyświetlonych reklam, mniejsze liczby w&nbsp;materiałach dla inwestorów.  
Facebook szczyci się faktem, że ma ponad 2&nbsp;miliardy użytkowników. Ale co by było, gdyby spora część z&nbsp;nich okazała się fałszywymi kontami? Wyszłoby na jaw, że król jest nagi, użytkownicy odchodzą, inwestorzy nie mają tu czego szukać.

Być może to z&nbsp;tego powodu lubią swoją nieprzejrzystość i&nbsp;zawzięcie jej pilnują. Czasem bardzo kontrowersyjnymi metodami, takimi jak [banowanie kont badaczy](https://techcrunch.com/2021/08/04/facebook-ad-observatory-nyu-researchers/) albo [grożenie im pozwami](https://algorithmwatch.org/en/instagram-research-shut-down-by-facebook/), gdy ci próbowali analizować ich algorytmy i&nbsp;ustalić kryteria, według których udostępniane są różne treści (w tym propaganda polityczna).

A przecież, gdyby giganci chcieli, mieliby aż nadto narzędzi do monitorowania skupisk trolli na swoich platformach. Pod względem inwigilacji bywają naprawdę kreatywni.

Twitter zamienia wszystkie linki wrzucane przez użytkowników na takie, które wymagają przejścia przez jego strony pośrednie. Dzięki temu może „widzieć” na żywo popularność stron. Ostatnio próbował zyskać jeszcze więcej władzy, dając sobie możliwość [ukrywania postów](http://www.kevinmarks.com/twittereditsyou.html) udostępnionych na cudzych, prywatnych stronach. 

A na deser: oba wielkie portale dodają do linków [dziwne ciągi znaków](https://annoying.technology/posts/e6901c0ea272f57d/), których znaczenie [nie jest do końca jasne](https://stackoverflow.com/questions/64092454/what-is-the-purpose-of-the-new-cft-0-and-tn-parameters-in-facebook-po). Być może pozwoliłyby **identyfikować, kim była osoba kopiująca dany link**.

Mania na punkcie kontroli, zatajanie informacji i&nbsp;znikome sukcesy. Wobec takich wad proponuję uznać duże portale za niewygodne i&nbsp;zwrócić się ku pewniejszym graczom.

# Sojusznicy -- Brand24, NASK i&nbsp;inni

Brand24 to polska firma zajmująca się analizą trendów w&nbsp;internecie. Przy współpracy z&nbsp;paroma innymi założyła stronę *[zglostrolla.pl](https://zglostrolla.pl/)*, przez którą można... zgłaszać trolle.  
Na pierwszy rzut oka pomysł niekoniecznie porywający. Autorzy strony, z całym szacunkiem dla nich, raczej nie mają specjalnych chodów u FejsoTwittera. Chcąc zbanować trolle, nadal musieliby je zgłaszać tradycyjną drogą.

Ale pozwólcie na małą analogię wojenną.  
Ban to odpowiednik pokonania jednego żołnierza. Zawsze coś, ale **dużo cenniejsze jest zdobycie danych wywiadowczych**, dzięki którym złapiemy w&nbsp;zasadzkę kilka plutonów.

Jeśli potraktujemy *ZgłośTrolla* i&nbsp;jej autorów jak zaplecze analityczne, a&nbsp;nie maszynkę do banowania, to możemy dojrzeć dwie istotne zalety:

1. Doświadczenie w&nbsp;analizie danych.  

   Trolli jest bardzo wiele, więc skuteczna walka wymaga identyfikowania ich na dużą skalę -- znajdowania całych grup, działających w&nbsp;jednym czasie i&nbsp;powielających podobne komunikaty.  
   Nie wiemy, czy duże platformy dopasowują swoje analizy do naszych realiów i języka. Przy Brand24 wiemy, że [to robią](https://nitter.net/pic/media%2FFMgPoffXoAQKsIZ.jpg%3Fname%3Dorig). Zresztą cała ich działalność opiera się na analizowaniu polskich postów, nastrojów w&nbsp;komentarzach i&nbsp;podobnych rzeczy.

2. Większa jawność działań.  
  
   Brand24 deklaruje, że przekazuje zweryfikowane trolle do NASK, czyli rządowej organizacji zajmującej się cyberprzestrzenią.
  I&nbsp;to działa. NASK prowadzi [publicznie dostępną listę trollkont](https://www.nask.pl/pl/wlaczweryfikacje/4413,WlaczWeryfikacje.html), na której jest już kilkaset profili.

Zgłaszając trolle przez stronkę, nadal nie mamy 100% wglądu w&nbsp;działanie właścicieli. Ale i&nbsp;tak mamy sporo w&nbsp;porównaniu z&nbsp;nieprzeniknionym Twitterem czy Facebookiem.

Oczywiście istnieją też inni potencjalni sojusznicy -- widziałem chociażby ogłoszenie grupy prawników, którzy obiecali zająć się wpisami podpadającymi pod pochwalanie [wojny napastniczej](https://arslege.pl/wojna-napastnicza/k1/a146/).  
Ogólnie **warto zapisywać informacje o&nbsp;trollach i&nbsp;układać u&nbsp;siebie na dysku**. Nigdy nie wiadomo, czy komuś się nie przydadzą.

## Metody walki

Poznaliśmy graczy, więc czas przejść do układania strategii.

# Znajdowanie trolli

Istnieje szansa, że na trolle natkniemy się przypadkiem, na przykład w&nbsp;sekcjach komentarzy. Ale co, jeśli akurat mamy wojowniczy nastrój i&nbsp;chcemy sami je tropić?

Możemy zacząć od wspomnianej wcześniej listy NASK, zawierającej znane trolle, a&nbsp;następnie odwiedzać konta, które udostępniały ich treści. Będzie to raczej łatwiejsze w&nbsp;przypadku Twittera, bo nie ma tam rozróżnienia *prywatny profil versus publiczne komentarze* i&nbsp;wszystko widać jak na dłoni.

**Aktualizacja 18.04.2022:** Pewien [użytkownik](https://nitter.net/SKruszkov/status/1514670298687320067) Twittera o&nbsp;nicku *Sasha Kruszkov* stworzył [wielki raport](https://wetransfer.com/downloads/b3bc42937e4a6bff854a491d2ecb4a6f20220414181925/73a987) (PDF z&nbsp;obrazkami ważący ponad 500&nbsp;MB) o&nbsp;kontach szczególnie aktywnych na Twitterze. Wiele z&nbsp;nich spoza listy NASK.  
Nie wszystkie korzystają z&nbsp;tagów związanych z&nbsp;Ukrainą. Ale możemy odwiedzić te profile, które to robią, i&nbsp;zacząć od nich nasze poszukiwania. W tym celu kopiujemy nazwę użytkownika z raportu i&nbsp;wklejamy w&nbsp;pasek po adresie `https://twitter.com/` albo `https://nitter.net/`.

{% include info.html
type="Porada"
text="Zamiast Twittera polecam używać [Nittera](https://nitter.net/).  
Dzięki niemu **możemy przeszukiwać tweety, nie mając konta na Twitterze**. Ponadto zmienia linki śledzące Twittera na eleganckie linki prosto do źródeł.  
Jeśli chcemy zobaczyć, kto udostępnił jakiegoś tweeta, to można przekleić charakterystyczny fragment tekstu. Potem wklejamy go do wyszukiwarki Nittera i&nbsp;dodajemy cudzysłowy (`\"nasz tekst\"`), żeby szukać dokładnie tego.  
W filtrze (ikona strzałki po prawej) możemy dodatkowo wybrać `retweets`, żeby zobaczyć wyłącznie przypadki udostępnień."
%}

Jeszcze inny sposób: wyjście od słów zamiast od profili. **Wyszukujemy zwroty, które często pojawiają się w&nbsp;komunikatach propagandowych**. Dość pewne przykłady:

<div class="black-bg mono">Biolaby, Banderowcy, UPAina</div>

Teksty mniej pewne (pojawiają się też w&nbsp;normalnym kontekście), ale dość lubiane przez trolle:

<div class="black-bg mono">
batalion Azowa<br/>
pomagać, ale z&nbsp;głową<br/>
odgryzł palec ratownikowi
</div>

Albo „Putin wyzwolił”, „ukraińskie laboratoria”, „ukraina wielki reset”... Ogranicza nas jedynie wyobraźnia :wink: Kto się napatrzył na twórczość trolli lub spiskowych świrków, ten mniej więcej zna ten styl.

Po znalezieniu podejrzanych komentarzy patrzymy na ich autora. Mało informacji na profilu, dużo propagandy? Jeśli tak, to jest duża szansa, że trafiliśmy na trolla.  
Po złapaniu jednego możemy spojrzeć, kto powielał jego treści (*retweety*, udostępnienia) i&nbsp;w ten sposób być może złapać kolejnych.

{% include info.html
type="Ciekawostka"
text="Analizowanie tekstu -- a&nbsp;konkretnie powtarzających się, nietypowych zwrotów, udostępnianych w&nbsp;podobnym czasie -- pozwoliło między innymi [złapać właścicielkę popularnej strony propagandowej](https://www.facebook.com/marcinrey/posts/10221865438009670), nauczycielkę z&nbsp;Sosnowca."
%}

Pod komentarzami możemy oczywiście coś napisać od siebie, ale nie będę się na tym skupiał w&nbsp;tym wpisie. Mam co najwyżej jedną uwagę -- zazwyczaj **znacznie więcej jest osób czytających niż komentujących**. Proponuję pisać z&nbsp;myślą o publiczności; jakbyśmy byli przewodnikami, pokazującymi okaz trolla grupie zwiedzającej zoo.  
Moim zdaniem lepiej publicznie zdemaskować i&nbsp;rozbroić propagandę niż dawać upust emocjom i&nbsp;pisać teksty niskich lotów w&nbsp;stylu „won, ruska onuco”. W&nbsp;oczach postronnych wygląda to tak, jakbyśmy to my byli agresorami.

A teraz przejdźmy do różnych form zgłaszania, lepszych i&nbsp;gorszych.

# Zgłaszanie przez platformy (najgorsza opcja)

Jak wspomniałem, obie platformy dają możliwość zgłaszania komentarzy. Nie mamy żadnych gwarancji co do tego, że będą w&nbsp;tym skuteczne. A&nbsp;nawet jeśli usuną jeden konkretny komentarz, to nie wiemy czy rozszerzą poszukiwania na inne trolle.

Dlatego sposób na zgłaszanie przez ich narzędzia pokażę tu wyłącznie z&nbsp;kronikarskiego obowiązku.

Na Facebooku klikamy ikonę trzech kropek obok posta albo komentarza, wybieramy opcję zgłoszenia, następnie przyczynę. Na Twitterze analogicznie.

{:.figure .bigspace}
<img src="/assets/posts/trolle/fb-zglaszanie-posta.jpg" alt="Zrzut ekranu z&nbsp;Facebooka, pokazujący rozwinięte menu do zgłaszania wpisów i&nbsp;komentarzy. Przy ikonie trzech kropek znajduje się czerwona cyfra jeden, a&nbsp;przy opcji zgłoszenia komentarza cyfra dwa."/>

Poznawszy gorszą metodę, przejdźmy do lepszej.

# Wrzucanie linków na zglostrolla.pl

Tę metodę może stosować każdy. Będziemy mieli większą pewność, że ktoś podejdzie do naszych zgłoszeń z&nbsp;głową, znajdując większe grupki trolli i&nbsp;analizując treść ich komunikatów.

Aby podrzucić stronce jakiś post/komentarz:

1. znajdujemy datę jego zamieszczenia (np. *„4 godziny temu”*),
2. najeżdżamy na nią kursorem i&nbsp;klikamy prawym przyciskiem myszy (a na komórce -- przytrzymujemy na niej palec),
3. wybieramy opcję `Kopiuj link` (albo `Kopiuj adres odnośnika`),
4. otwieramy w&nbsp;przeglądarce stronę *zglostrolla.pl*, wklejamy w&nbsp;formularzu link i&nbsp;wybieramy platformę, potwierdzamy.

{:.figure .bigspace}
<img src="/assets/posts/trolle/zglostrolla.jpg" alt="Zrzut ekranu pokazujący formularz ze strony Zgłoś Trolla."/>

Jeśli chcemy mieć szybszy dostęp do *zglostrolla.pl*, to możemy ją dodać do naszych zakładek.

{:.bigspace}
<img src="/assets/posts/trolle/zglostrolla-zakladki.jpg" alt="Zrzut ekranu porównujący paski główne z&nbsp;Chrome'a i&nbsp;Firefoksa. Na obu z&nbsp;nich po prawej stronie widać zaznaczoną gwiazdkę."/>

<a id="facebook-problem"></a>

{% include info.html
type="Uwaga"
text="Strony mogą mieć wiele wariantów. Osobiście spotkałem się z&nbsp;co najmniej jedną mobilną wersją strony Facebooka, przez którą **nie dało się zdobyć linków do konkretnych komentarzy**; po prostu nigdzie ich nie było. W&nbsp;takiej sytuacji można spróbować przez uproszczoną wersję mobilną (*www.mbasic.facebook.com*) albo włączyć tryb „Strona dla komputerów” i&nbsp;wejść na *www.facebook.com*."
%}

# Wrzucanie oczyszczonych linków

{:.post-meta .bigspace-after}
**To część dla chętnych** -- jeśli będziemy po prostu kopiowali i&nbsp;wrzucali linki, też powinno być OK.

Jak wspominałem, obie wielkie platformy dodają do linków teksty od siebie. Często w&nbsp;formie parametrów, czyli tekstu po znaku zapytania.  
W najlepszym razie to nieszkodliwe śmieci, w&nbsp;najgorszym -- informacja wskazująca nasze konto jako źródło linku.

Brand24 i&nbsp;NASK raczej nic z&nbsp;tych danych nie odczytają na nasz temat. Ale gdyby w&nbsp;jakiś sposób trafiły one do dużych firm -- i&nbsp;faktycznie były śledzące -- to byłoby możliwe ustalenie, że to my byliśmy źródłem.  
Z tego względu jestem za tym, żeby usuwać bzdety z&nbsp;linków wrzucanych na *zglostrolla.pl* i&nbsp;zostawiać tylko rzeczy istotne.

{% include info.html 
type="Powiązane wpisy"
text="O parametrach w&nbsp;linkach [pisałem już](https://www.ciemnastrona.com.pl/internetowa_inwigilacja/2021/04/09/internetowa-inwigilacja-parametry){:.internal} w&nbsp;serii „Internetowa inwigilacja”. Są dość często stosowaną metodą przemycania pewnych informacji o&nbsp;użytkownikach.
"%}

W przypadku Facebooka wypatrujemy w&nbsp;linku tekstu `__cft[0]__=` i&nbsp;usuwamy wszystko po nim. Następnie usuwamy też pojedynczy znak, który stał przed tym tekstem (`?` albo `&`). Resztę zostawiamy.  
Przedstawiam przykładowy zmyślony link. Części, które możemy bez problemu usunąć, oznaczyłem na czerwono. Zwróćmy jednak uwagę na to, że nie możemy usunąć parametru `comment_id`, jest ważny.

{:.bigspace}
<div class="black-bg mono">https://www.facebook.com/groups/222221111113333/posts/111111777/?comment_id=666677779995390<span class="red">&__cft__[0]=AZU5YpcaMXhTtDPbxOhGAgTUUFC8IWoXdlr_NDUaMdo9vUF200qUzk3dGweAALrTEd7rcdMVR_qhgRGY6OSI2ZX_smSSefB9x8cjH0IcSfm3WGYcsDAsa9_MjkvRH123QEO&__tn__=R]-R</span></div>

W przypadku Twittera takie dodatki w&nbsp;linkach są dużo rzadsze, ale podobno [czasem się trafiają](https://nitter.net/luca/status/1432780065109155855). Mamy o&nbsp;tyle łatwiej, że wystarczy usunąć wszystko od znaku zapytania do końca:

{:.bigspace}
<div class="black-bg mono">https://twitter.com/przyklad-ciemnej-strony/status/1434185645297803561<span class="red">?t=ND0xaz45z76pitle0YjG-g&s=19</span>
</div>

Kolejna sprawa -- **linki do Nittera możemy łatwo zamienić na linki do Twittera**. W&nbsp;tym celu zmieniamy `nitter.net` na `twitter.com`. Możemy też usunąć `#m` z&nbsp;końca linku, bo Twitter tego nie dodaje.

Nie wiem, czy taka zmiana jest konieczna. Ale być może analitycy ze *zglostrolla.pl* dają priorytet linkom z&nbsp;głównych platform, a&nbsp;Nitter tylko by motał? W&nbsp;każdym razie nic nie stracimy, przerabiając linki nitterowe na twitterowe.

# Zapisywanie informacji na później

Wszystkie powyższe porady opierają się na założeniu, że podrzucamy linki na *zglostrolla.pl*, a&nbsp;wszelkie analizy zostawiamy właścicielom strony.

Ale kiedyś mogą się pojawić kolejne organizacje lub osoby prywatne, którym przydałyby się nasze linki. Z&nbsp;tego względu warto zapisywać je na później. Choćby do jakiegoś osobnego pliku tekstowego.

Same komentarze również są cenne. Pomijając tekst (który można analizować, żeby wyłapać szerzej zakrojone akcje dezinformacyjne), często są tam linki do innych źródeł, z&nbsp;których trolle korzystają. Dzięki nim można odkryć -- po nitce do kłębka -- bardziej wpływowe strony propagandowe.

Jeśli po prostu zaznaczymy tekst wiadomości i&nbsp;wkleimy go do Notatnika albo podobnego programu, stracimy te cenne linki. Dlatego **lepszym sposobem na zapisywanie treści komentarzy jest sięgnięcie do ich źródła w&nbsp;formacie HTML**.

To bardzo proste; wystarczy kliknąć prawym przyciskiem myszy na część komentarza i&nbsp;wybrać opcję `Zbadaj element`. Otworzą się narzędzia przeglądarki i&nbsp;lista elementów na stronie. Kiedy najedziemy kursorem na jakiś element z&nbsp;listy, to zostanie wyróżniony kolorem.

W ten sposób znajdujemy taki element, żeby kolorowa otoczka obejmowała cały komentarz, ale nic więcej. Klikamy go prawym przyciskiem myszy i&nbsp;wybieramy opcję `Kopiuj zewnętrzny HTML`. Do naszego schowka trafi kod źródłowy komentarza, który możemy gdzieś wkleić.

Systematyczne zgłaszanie, przechodzenie od tropu do tropu, zapisywanie na później. Powoli stajemy się wydajni jak drony Bayraktar :sunglasses:

Ale nadal jest w&nbsp;tym trochę powtarzalnej roboty -- kopiowanie, edytowanie linków, zapisywanie do pliku... A&nbsp;ja chciałbym działać w&nbsp;sposób szybki i&nbsp;łatwy. Dlatego stworzyłem parę narzędzi ułatwiających życie. Jeśli chcecie z&nbsp;nich skorzystać, czytajcie dalej!

# Bonus: pomocniczy skrypt Pythona

Stworzyłem skrypt `antitroll.py`, który automatyzuje wszystkie powyższe kroki -- czyszczenie linków, zapisywanie ich na dysku i otwieranie formularza na stronce do zgłaszania.

{% include pyscript.html
name="antitroll.py"
link="/assets/skrypty/antitroll.py"
trailer="
<p><strong>Skrypt nie potrzebuje do działania niczego poza samym Pythonem</strong>.<br>
Wystarczy że pobierzemy i&nbsp;zainstalujemy ten język z&nbsp;<a href='https://www.python.org/downloads/'>oficjalnej strony</a>. Następnie pobieramy mój skrypt, umieszczamy go w&nbsp;dogodnym dla siebie folderze.</p>

<p>Krótka instrukcja korzystania:</p>

<ol>
  <li>Kopiujemy link do posta, profilu albo komentarza trolla.<br>
Albo cały komentarz, przez narzędzia przeglądarki.</li>
  <li>Uruchamiamy skrypt w&nbsp;dowolny sposób (podwójnym kliknięciem na plik, przez edytor IDLE, przez konsolę…).</li>
</ol>

<p>To wszystko! Efekty działania skryptu:</p>

<ul>
  <li>W domyślnej przeglądarce otworzy nam się stronka <em>zglostrolla.pl</em>, wyśrodkowana na formularzu.</li>
  <li>Do naszego schowka trafi przygotowany link bez śmieciowych parametrów. Wystarczy wkleić go w&nbsp;formularz.</li>
  <li>Ten sam link zostanie zapisany do zbiorczego pliku tekstowego.</li>
  <li>Jeśli kopiowaliśmy cały komentarz przez narzędzia przeglądarki, to jego treść również zostanie zapisana na dysku.</li>
</ul>

<p>Niektóre ustawienia można kontrolować, zmieniając wybrane wartości pod koniec skryptu. W&nbsp;tym celu otwieramy plik w&nbsp;dowolnym edytorze albo nawet w&nbsp;Notatniku.</p>
"
%}

# Bonus 2: dodatek do przeglądarki

Dzięki skryptowi Pythona mogłem szybko pracować ze skopiowanymi linkami/komentarzami. Ale samo kopiowanie komentarzy nadal wymagało kilku kroków.

W obecnych czasach wszystko musi być lekkie i&nbsp;wygodne. Skoro jednym przesunięciem palca można wywalić czyjąś pulę genetyczną do kosza (na Tinderze), to nie godzi się, żeby ubijanie trolli wymagało więcej zachodu!

Dlatego stworzyłem autorski dodatek do przeglądarki, `SelSword`. Pomaga w&nbsp;szybki sposób -- podwójnym kliknięciem -- zaznaczać komentarze i&nbsp;kopiować ich kod źródłowy, w&nbsp;formie strawnej dla Antitrolla.

{:.figure}
<img src="/assets/posts/trolle/selsword-troll.jpg" alt="Zrzut ekranu z&nbsp;Nittera pokazujący komentarz mówiący o&nbsp;tym, jakoby dzięki interwencji Putina udało się powstrzymać laboratoria pracujące nad bronią biologiczną. Jest otoczony cienką czerwoną ramką."/>

{:.figcaption}
Komentarz trolla zaznaczony ramką po podwójnym kliknięciu.

{% include info.html
type="Ciekawostka"
text="Nazwa dodatku to gra słów.  
*Sel* to popularny skrót od *selection*, zaznaczenia. *Sellsword* to najemnik (dosł. *miecz na sprzedaż*)."
%}

{:.post-meta .bigspace-after}
**Uwaga:** Dodatek jest na razie w fazie testów. Nie wspiera na przykład zaznaczania komentarzy na stronach, które zapisaliśmy na dysku (nawet jeśli są z&nbsp;Twittera/Facebooka). Może też nie działać na niektórych przeglądarkach.

Czujcie się ostrzeżeni! A&nbsp;teraz przejdźmy do instalacji i&nbsp;korzystania.

Na początku odwiedzamy [stronę mojego dodatku](https://github.com/Bob-A-Dook/SelSword) na Githubie. Jest tam cały kod źródłowy, możemy się upewnić że jest bezpieczny.  
Znajdujemy zielony przycisk `Code` i&nbsp;wybieramy opcję pobrania wszystkiego w&nbsp;formie pliku ZIP.

Dalsze działania zależą od tego, jaką mamy przeglądarkę.

<details>
 <summary>
  <strong>Chrome, Brave, Edge, Opera oraz inne na silniku Chromium</strong>
 </summary>

<p class="post-meta">Niestety przeglądarki mają tu pewne różnice między sobą, nie testowałem wszystkich. Niektóre nazwy mogą się różnić, ale procedura jest podobna.</p>

<ol>
  <li>Pobieramy dodatek w&nbsp;formie pliku ZIP, rozpakowujemy go gdzieś (większość przeglądarek tego wymaga).</li>
  <li>Otwieramy menu dodatków
(trzy kropki w&nbsp;prawym górnym rogu, w niektórych przeglądarkach <code class="language-plaintext highlighter-rouge">Więcej narzędzi</code>, <code class="language-plaintext highlighter-rouge">Rozszerzenia</code>).</li>
  <li>Włączamy pstryczek podpisany <code class="language-plaintext highlighter-rouge">tryb programisty</code> (albo <code class="language-plaintext highlighter-rouge">tryb dewelopera</code>).</li>
  <li>Pojawią się opcje ładowania dodatków; wybieramy <code class="language-plaintext highlighter-rouge">Załaduj rozpakowane</code> (na Edge'u błędnie przetłumaczone jako „nierozpakowane”).</li>
  <li>Wchodzimy do folderu, w którym wcześniej rozpakowaliśmy pliki i potwierdzamy wybór. Gdyby nie działało, to wybieramy cały plik ZIP.</li>
</ol>
</details>

{:.bigspace-after}
<details>
 <summary>
  <strong>Firefox oraz inne na jego silniku</strong>
 </summary>
<ol>
  <li>Pobieramy dodatek w&nbsp;formie pliku ZIP, rozpakowujemy.</li>
  <li>Wpisujemy <code class="language-plaintext highlighter-rouge">about:debugging</code> w&nbsp;pasku przeglądarki.</li>
  <li>Klikamy opcję <code class="language-plaintext highlighter-rouge">Ten Firefox</code> po lewej.</li>
  <li>Klikamy <code class="language-plaintext highlighter-rouge">Tymczasowo wczytaj dodatek</code> i&nbsp;wybieramy dowolny plik z&nbsp;rozpakowanego folderu, np. <em>manifest.json</em>.<br/><strong>Kroki 2-4 trzeba wykonać przy każdym uruchomieniu Firefoksa</strong>.
</li>
</ol>
</details>

Po załadowaniu dodatku odwiedzacie Twittera, Nittera albo Facebooka. Znajdujecie jakiś trollkomentarz. Dwukrotnie na niego klikacie. Kliknięty element zostanie otoczony czerwoną obwódką, a&nbsp;do Waszego schowka trafi jego treść w&nbsp;formacie HTML.

Wystarczy teraz uruchomić Antitrolla, a&nbsp;ten zrobi swoje.

<img src="/assets/posts/trolle/demon-slayer-dual-script.jpg" alt="Kadr z&nbsp;anime Demon Slayer pokazujący postać z&nbsp;logiem Ciemnej Strony zamiast twarzy. Jest w&nbsp;trakcie wykonywania cięcia dwoma mieczami w&nbsp;stronę zgarbionej, groteskowej postaci, której głowa jest zakryta obrazkiem typu troll face. Na jednym z&nbsp;ramion atakującej postaci widać napis SelSword i&nbsp;ikonkę miecza, a&nbsp;na drugim podpis antitroll.py oraz ikonkę skryptu Pythona."/>

{:.figcaption}
Źródło: Anime *Demon Slayer* plus klasyczny *troll face*. Przeróbki moje.

# Walka z&nbsp;trollami przez komórkę

Zarówno dodatek, jak i&nbsp;skrypt są w&nbsp;stanie robić swoje również na komórce, dzięki fantastycznej apce Termux. Wymaga to jednak dwóch rzeczy: zainstalowania Pythona na Termuksie, a&nbsp;mojego dodatku w&nbsp;przeglądarce Kiwi Browser.

{:.bigspace-before}
<details>
<summary>
<strong>Jak naszykować skrypt w&nbsp;apce Termux</strong>
</summary>
<p>Aby <code class="language-plaintext highlighter-rouge">antitroll</code> zadziałał na telefonie, trzeba:</p>

<ol>
  <li>Posiadać telefon z&nbsp;systemem Android;</li>
  <li>Zainstalować aplikację <em>F-Droid</em>;</li>
  <li>Zainstalować przez <em>F-Droida</em> aplikacje <em>Termux</em> oraz <em>Termux:API</em><br>
(przez działania Google’a wersja z&nbsp;ich domyślnego Play Store’a <a href="https://github.com/termux/termux-packages/wiki/Termux-and-Android-10">nie działa</a>);</li>
  <li>Zainstalować Pythona<br>
(powinno zadziałać wpisanie w&nbsp;Termuksa komendy <code class="language-plaintext highlighter-rouge">pkg install python</code>);</li>
  <li>Umieścić mój skrypt w&nbsp;folderze domyślnie dostępnym dla Pythona.</li>
</ol>
<p>Co do ostatniego punktu. Jeśli nie zmienimy nazwy skryptu i&nbsp;go po prostu pobierzemy ode mnie, to powinien trafić do folderu <code class="language-plaintext highlighter-rouge">Download</code>.</p>
<p>Wówczas, żeby skopiować skrypt do folderu głównego, gdzie będzie zawsze dostępny dla Pythona, musimy wpisać w&nbsp;Termuksie:</p>
<div class="black-bg mono">cp /storage/emulated/0/Download/antitroll.py ~</div>
<p>Pamiętajmy przy tym o&nbsp;spacjach po <code class="language-plaintext highlighter-rouge">cp</code> i&nbsp;przed <code class="language-plaintext highlighter-rouge">~</code>.</p>
<p>Mam nadzieję, że zadziała. Ale wersji Androida jest wiele i&nbsp;nie każda może się lubić z&nbsp;Termuksem.</p>
</details>

{:.bigspace-after}
<details>
<summary>
  <strong>Jak naszykować dodatek w&nbsp;apce Kiwi Browser</strong>
</summary>
 <ol>
  <li>Instalujemy przeglądarkę <em><a href="https://kiwibrowser.com/">Kiwi Browser</a></em> (oparta na silniku Chromium).</li>
  <li>Instalujemy mój dodatek przez jej opcje<br>
(w ten sam sposób co na komputerze; jedyna różnica taka, że <strong>nie rozpakowujemy pliku ZIP</strong> i&nbsp;wybieramy go w menu).</li>
  <li>Używamy tej przeglądarki<br>
(niby oczywiste, ale podkreślę: przez apki Facebooka i&nbsp;Twittera dodatek by nie działał).</li>
</ol>
</details>

Dlaczego Kiwi? Bo niestety **inne mobilne przeglądarki nie dają możliwości instalowania dodatków**. Tak, dotyczy to również mobilnego Firefoksa. Mimo że Mozilla w&nbsp;innych sferach raczej działa na rzecz użytkowników.

Dodatek działa jak na komputerze; dwa razy pod rząd naciskamy element palcem. Jeśli pojawiła się obwódka, to znaczy że się skopiował.  
Następnie otwieramy Termuksa i wpisujemy:

<div class="black-bg mono">python -m antitroll</div>

Zapisze nam trolla do pliku i otworzy stronkę do zgłaszania.

{% include info.html
type="Porada"
text="Nie trzeba za każdym razem wpisywać od nowa tekstu wywołującego skrypt; wystarczy nie wyłączać Termuksa, a potem naciskać przycisk ze strzałką w górę, żeby ponownie przywołać komendę."
%}

Na Twitterze i&nbsp;Nitterze śmiga mi bez zarzutu.  
Zauważyłem natomiast **niepokojącą rzecz na Facebooku**. A&nbsp;dokładniej na *m.facebook.com*, bo to tam przekierowuje urządzenia mobilne.  
Na początku działało jak powinno, ale potem zaczęła mi się wyświetlać inna wersja strony, zawierająca elementy z&nbsp;*WebLite* w&nbsp;nazwie.  
W tej wersji wszystko było ładowane przez nich dynamicznie, bez możliwości łatwego dorwania linków. Gorzej: nigdzie nie było linków do poszczególnych komentarzy, które dałoby się podrzucić analitykom.

Ten problem, wraz ze sposobami na jego obejście, [opisałem nieco wcześniej](#facebook-problem). Przypominam o&nbsp;nim, bo dotyczy właśnie wersji mobilnej. Poza tym jest niepokojącym zjawiskiem utrudniającym walkę z&nbsp;trollami.

## Podsumowanie

W obecnych czasach informacje to klucz do zwycięstwa. Fajnie jest wyłapywać skupiska trolli w&nbsp;sposób szybki, metodyczny, przy użyciu współczesnych narzędzi. Mam nadzieję, że parę pokazanych tu metod się Wam przyda!

Ale, jeśli dotrwaliście do końca, być może widzicie w&nbsp;tej sprawie drugie dno. A&nbsp;mianowicie -- trzeba się mocno natrudzić, żeby ominąć zawodne systemy Facebooka i&nbsp;Twittera, nie być zależnym od widzimisię ich moderatorów.

Jeśli spojrzymy na to, ilu starań wymagało zrobienie z&nbsp;telefonu przydatnego narzędzia do zgłaszania trolli, to wyłania się dość ponury obraz rzeczywistości.

Człowiek współczesny powinien używać urządzeń mobilnych.  
Powinien korzystać z&nbsp;oficjalnych, namaszczonych aplikacji.  
Nie powinien instalować dodatków, które pozwolą mu dopasować przeglądarkę do własnych potrzeb.  
Nie powinien zaglądać za kulisy stron, które ogląda. Powinien widzieć jedynie treść, jaką zapewnili mu autorzy.  
Nie powinien dzielić się danymi znalezionymi na stronie.  
Może je zgłaszać tylko przez oficjalne narzędzia, nie wiedząc co się potem stanie. 

**Człowiek współczesny -- w&nbsp;oczach internetowych korporacji -- nie powinien działać samodzielnie**.  
Ma miziać palcem kolorowe ikonki. Biernie patrzeć i&nbsp;konsumować. Również wschodnią propagandę robiącą mu wodę z&nbsp;mózgu. 

Tymi przemyśleniami kończę. Życzę udanej walki z&nbsp;trollami, ale nie zapominajmy -- na tym świecie istnieją jeszcze gorsze potwory :smile:
