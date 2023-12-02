---
layout: post
title: "Hasz na przyszłość i ukrywanie na widoku"
subtitle: "Prognoza z opóźnionym zapłonem."
description: "Prognoza z opóźnionym zapłonem."
date:   2023-11-26 11:17:18 +0100
tags: [Podstawy]
image:
  path: /assets/posts/haszowanie/hash-na-przyszlosc-baner.jpg
  width: 1200
  height: 700
  alt: "Szary hasz złożony z liczb i liter na ciemnym tle"
---

Ten wpis będzie nietypowy, bardzo minimalistyczny. Stworzyłem go właściwie tylko po to, żeby umieścić tu krótkie przewidywania związane z&nbsp;czymś, nad czym pracuję.

Oto one -- a&nbsp;właściwie ich hasz (*skrót*) typu SHA1:

{:.bigspace}
<div class="black-bg mono">
9b38746b755852bcae1e56c1e21af5bc471699ba
</div>

To tyle. Oryginalny tekst ujawnię, kiedy przyjdzie na to czas. Albo i&nbsp;nie :wink:

{:.post-meta .bigspace-after}
Zdradzę tylko, że to raczej prozaiczna informacja. Nie ma potrzeby się emocjonować.
 
Ten hasz jest swego rodzaju cyfrową „kapsułą czasu”. **Rzeczą stworzoną tu i&nbsp;teraz, ale przeznaczoną do odczytania w&nbsp;przyszłości**.

## Dlaczego akurat hasz?

Haszowanie polega na ściśnięciu dowolnych danych do krótkiej, zwięzłej postaci, w&nbsp;sposób nieodwracalny. Jest czymś powszechnym i&nbsp;sprowadza się często do wpisania krótkiej linijki kodu. Albo wklejenia tekstu [na odpowiedniej stronie](https://emn178.github.io/online-tools/sha1.html).
 
Otrzymany hasz ma dwie przydatne właściwości:

1. ustalenie na podstawie samego hasza, jaki był pierwotny tekst, jest bardzo trudne albo wręcz niemożliwe (zwłaszcza przy dłuższych tekstach);
2. ta sama metoda haszowania, użyta na tych samych danych, daje zawsze ten sam wynik.

Dzięki pierwszej właściwości nikt nie odczyta moich słów, póki sam ich nie ujawnię.  
A dzięki drugiej -- każdy może zweryfikować, porównując hasze, że napisałem konkretne słowa.

Gdy kiedyś wrzucę oryginalny tekst, to osoby chętne mogą go sobie skopiować i również zahaszować metodą SHA1, taką jak ja. Wyjdzie im ten sam hasz jak powyższy. Wniosek: dnia 26&nbsp;listopada 2023&nbsp;roku miałem konkretne przewidywania.

{% include info.html
type="Powiązane wpisy"
text="Więcej na temat haszowania napisałem w&nbsp;jednym ze swoich [starszych wpisów](/2021/02/28/hash-podstawy){:.internal}.  
Ponadto swoje oświadczenia w&nbsp;formie hasza opublikowały swego czasu, przy okazji [afery wokół Usecrypta](/2021/03/11/usecrypt-afera){:.internal}, trzy polskie portale na temat cyberbezpieczeństwa."
%}

## Ukrywanie na widoku

Publikowanie hasza to jeden z&nbsp;wielu sposobów na przekazywanie informacji w&nbsp;sposób niejawny, lecz weryfikowalny.

Jakimśtam sposobem byłoby nawet zwykłe **robienie aluzji**, które dopiero po fakcie staną się zrozumiałe. *Foreshadowing*, że tak zapożyczę z&nbsp;pisarskiego angielskiego.

Jednak aluzja może się okazać zbyt oczywista. Albo w&nbsp;drugą stronę -- na tyle zagmatwana, że trzeba będzie ją potem tłumaczyć. Jak kiepski dowcip.

Inna możliwość? Wrzucenie na widok publiczny **pliku zabezpieczonego hasłem** (zaszyfrowanego). A&nbsp;dopiero po fakcie udostępnienie hasła.  
Osoby chętne mogłyby wtedy wejść na jakąś stronkę deszyfrującą, jak [*hat.sh*](/tutorials/hat-sh-szyfrowanie){:.internal}, wpisać tam hasło i&nbsp;pobrać odkodowaną treść.

Sensowna opcja. Tylko że przy hasłach do plików trzeba uważać. Jeśli nie będą wystarczająco mocne, ktoś może je złamać metodą [*brute force*](https://pl.wikipedia.org/wiki/Atak_brute_force) -- po prostu próbując w&nbsp;błyskawicznym tempie wszelkich możliwych kombinacji liter.

{% include info.html
type="Ciekawostka"
text="Niedawno ukazał się anglojęzyczny wpis z&nbsp;ciekawym pomysłem na udostępnienie takiego zaszyfrowanego pliku.  
Nie trzeba go zostawiać w&nbsp;miejscu widocznym dla ludzi. Osoba mająca własną domenę może go rownież [umieścić na DNS-ie](https://thoughts.theden.sh/posts/dns-txt-record-fun/). Tam, gdzie podstawowe informacje związane z&nbsp;domeną, czytane częściej przez komputery niż ludzi."
%}

Jeszcze inną opcją byłaby **steganografia**. Ukrycie informacji, w&nbsp;sposób niewidoczny gołym okiem, w&nbsp;jakimś zwykłym pliku.

Przykład? Można zmieniać, w&nbsp;subtelny sposób, niektóre piksele obrazka. Tak, żeby po wykonaniu odpowiednich przekształceń ukazała się ukryta informacja. Czy to w&nbsp;formie graficznej, czy bajtów odpowiadających tekstowi.  
Odkrycie sekretu polegałoby w&nbsp;tym wypadku na opublikowaniu kodu dokonującego takich przekształceń.

{:.post-meta .bigspace-after}
Jeśli kogoś to zaciekawiło, to na YouTubie znajdzie obszerny [filmik](https://www.youtube.com/watch?v=60D-_xH63fg) po polsku od Gynvaela Coldwinda.  
Jeden z&nbsp;komentarzy pod spodem sugeruje, że w&nbsp;praktyce używa się bardziej złożonych metod, jak *przekształcenia falkowe*. Po angielsku *wavelet transforms*, gdyby ktoś chciał poszukać. 

W moim wypadku ta metoda by się jednak nie spisała. Steganografia lubi ciszę.  
Gdybym wrzucił obrazek i&nbsp;napisał „coś tu ukryłem”, to każda wnikliwa osoba mogłaby się na niego rzucić. Odpalać algorytmy, przekształcać go, szukać prawidłowości. Przedwcześnie odkryć sekret.

Ostatecznie postawiłem na hasza. Krótki i&nbsp;zwięzły. Nieodwracalny. Przyjazny dla osób weryfikujących -- wystarczy skopiować i wkleić na stronce haszującej, takiej jak [Online Tools](https://emn178.github.io/online-tools/sha1.html). Nie trzeba pobierać żadnego pliku.

## Czy haszowi można wierzyć?

W tym przypadku jeszcze nie. Bo **umieszczam go na własnej stronie, nad którą mam kontrolę -- mógłbym przy nim majstrować**.  
Jeśli moja prognoza się nie sprawdzi, to mógłbym napisać nową, dopasowaną do przeszłości. Zahaszować ją. Edytować swój wpis i&nbsp;wkleić tam nowego hasza. A&nbsp;potem twierdzić, że od początku taki był.

{% include info.html
type="Ciekawostka"
text="W podobny sposób niektórzy [udawali na Twitterze](https://skeptics.stackexchange.com/questions/22345/did-the-twitter-account-fifndhs-predict-the-exact-world-cup-results-ahead-of-tim) (obecnie X), że trafnie przewidzieli wyniki meczów.  
Nim się odbyły, tworzyli wiele tweetów. Po jednym dla *każdej możliwej kombinacji wyników*. A&nbsp;po meczu usuwali wszystkie poza tym jednym, który był zgodny z&nbsp;rzeczywistością. A&nbsp;że data dodania była wcześniejsza niż mecz, to wychodzili na proroków."
%}

Żebym nie mógł oszukiwać, hasz musi być umieszczony również na zewnętrznej, niezależnej stronce.

Dlatego krótko po publikacji wrzucę ten wpis do internetowego archiwum, [*archive.vn*](https://archive.vn/).  
Każdy może skopiować link do niego z&nbsp;górnego paska, odwiedzić Archiwum i&nbsp;go tam wkleić (w&nbsp;pole u&nbsp;dołu, nie u&nbsp;góry!).

{:.post-meta .bigspace-after}
Gdyby strona nie chciała wpuścić i&nbsp;wyswietlała niekończące się Captche, to warto spróbować innego hotspota albo zmienić DNS-a. Na pewno nie lubią się z tym od firmy Cloudflare.

Po wybraniu najwcześniejszego z&nbsp;dostępnych zrzutów, z&nbsp;26 listopada, ukaże się hasz dodany tego dnia. Archiwum jest poza moim zasięgiem, więc nie mam możliwości mataczenia. Nie żebym zamierzał to robić.

Ty tyle na dziś! Do wątku hasza -- mam nadzieję -- wrócę w&nbsp;przyszłym roku :smile:

