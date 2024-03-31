---
layout: post
title: "Afera wokół XZ. Próba zaminowania cyfrowego świata"
subtitle: "Jedno źródło wszystkich rzek. Może by tu czegoś dolać?"
description: "Jedno źródło wszystkich rzek. Może by tu czegoś dolać?"
date:   2024-03-31 19:00:00 +0100
tags: [Afera, Centralizacja, Open Source, Linux]
category: cyfrowy_feudalizm
category_readable: "Cyfrowy&nbsp;feudalizm"
image:
  path: /assets/posts/centralizacja/xz/xz-backdoor-baner.jpg
  width: 1200
  height: 700
  alt: "Postać z logo tukana zamiast głowy i w koszulce z napisem XZ trzyma na barkach kulę ziemską z napisem SSH. W jej stronę leci kopniak wymierzony przez inną postać, w stroju mnicha Shaolin, z emotą diabełka zamiast głowy"
---

29 marca. Święta, za oknem ciepło, na poranek była zaplanowana uczta. W&nbsp;dobrym humorze siadłem do wieczornego przeglądania ulubionego forum, HN.  
W oczy rzucił mi się wątek u&nbsp;samej góry. Ponad 700&nbsp;komentarzy w&nbsp;kilka godzin (parę dni później ponad 1700). Grubsza akcja.

Jak się okazuje, **wykryto złośliwy kod w&nbsp;nowej wersji programu często używanego na serwerach**. Zagrożenie udało się rozpoznać, nim doprowadziło do większych szkód.  
Teraz trwają analizy. Ukazują póki co wyrafinowany atak, rozwijany *przez lata*. Obejmujący hakerskie triki i&nbsp;psychologiczne usypianie czujności.

Rok temu stworzyłem wielkanocny wpis o&nbsp;[ataku pewnej firmy](/2023/04/10/wielkanoc-tiry-walka.html){:.internal} na jej własnych kierowców. Tym razem coś cyfrowego. Aferkowa Wielkanoc zaczyna być tradycją!

Uczciwie przyznam -- sprawy cyberbezpieczeństwa znam tylko pobieżnie. Mniej niż rzeczy dotyczące prywatności.  
Dlatego będzie to wpis niespecjalistyczny, popularyzatorski. Przybliży świat *open source* i&nbsp;ciemne strony cyfrowego ekosystemu: masową zależność od nielicznych programów oraz nadużywanie dobrej woli ich autorów.

Szukasz głębszego nura w&nbsp;tę sprawę? To polecam strony polskich bezpieczników, jak [analiza Gynvaela Coldwinda](https://gynvael.coldwind.pl/?lang=en&id=782). Albo niektóre inne źródła, które tu podlinkuję.

## Spis treści

* [Wprowadzenie](#wprowadzenie)
  * [Program i&nbsp;narzędzia XZ](#program-inarzędzia-xz)
  * [Cyfrowy łańcuch dostaw](#cyfrowy-łańcuch-dostaw)
* [Atak krok po kroku](#atak-krok-po-kroku)
  * [Problem zmęczonego opiekuna projektu](#problem-zmęczonego-opiekuna-projektu)
  * [Dobry i&nbsp;zły glina](#dobry-izły-glina)
  * [Jia przejmuje stery](#jia-przejmuje-stery)
  * [Jia zdejmuje maskę](#jia-zdejmuje-maskę)
  * [Broń ukryta w&nbsp;testach](#broń-ukryta-wtestach)
  * [Udoskonalenie złośliwego kodu](#udoskonalenie-złośliwego-kodu)
  * [Lobbowanie za przyjęciem nowinek](#lobbowanie-za-przyjęciem-nowinek)
  * [Wykrycie furtki](#wykrycie-furtki)
* [Podsumowanie](#podsumowanie)

## Wprowadzenie

Sprawa dotyczy programu o&nbsp;nazwie XZ oraz jego narzędzi pomocnicznych. Jest obecny na wielu komputerach z&nbsp;systemem Linux. Jak serwery, na których stoi współczesny internet.

Do programu wprowadzono dyskretną zmianę, robiąc z&nbsp;niego potencjalny wytrych. Zamkami, które miał otwierać, miały być rzekomo połączenia przez [SSH](https://www.cloudflare.com/learning/access-management/what-is-ssh/) -- powszechną, szyfrowaną metodę panowania nad serwerami.

Potem pojawiły się głosy, że jest jeszcze gorzej, a&nbsp;atak mógł mieć na celu [nie tylko włamanie, ale i&nbsp;sabotaż](https://bsky.app/profile/filippo.abyssdomain.expert/post/3kowjkx2njy2b) (RCE; uruchomienie złośliwego kodu).  
Czym by się nie okazał; byłby groźny i&nbsp;miałby wielki obszar rażenia.

{:.figure .bigspace-before}
<img src="/assets/posts/centralizacja/xz/xz-backdoor-baner.jpg" alt="Postać z&nbsp;logo tukana zamiast głowy i&nbsp;w koszulce z&nbsp;napisem XZ trzyma na barkach kulę ziemską z&nbsp;napisem SSH. W&nbsp;jej stronę leci kopniak wymierzony przez inną postać, w&nbsp;stroju mnicha Shaolin, z&nbsp;emotą diabełka zamiast głowy."/>

{:.figcaption}
Źródło: Emojipedia, ikona projektu Tukaani, Freepik.  
Autorzy: [siłacz](https://www.freepik.com/free-vector/set-male-females-weight-lifters_4950314.htm) -- *katemangostar*, [kopiąca postać](https://www.freepik.com/free-vector/martial-arts-icons-set-with-fighting-symbols-flat-vector-isolated-illustration_39927010.htm) -- *macrovector*, [kula ziemska](https://www.freepik.com/free-vector/earth-globe-icons-set_4556841.htm) -- *macrovector_official*. Przeróbki moje.

### Program i&nbsp;narzędzia XZ

Główny winowajca, program XZ, odpowiada za pracę z&nbsp;plikami skompresowanymi z&nbsp;rozszerzeniem `.xz`. Ku zdziwieniu niektórych: to całkiem popularny format. Coś jak ZIP ze świata konsumenckiego, tylko że [mieści w&nbsp;sobie jeden plik](https://xz.tukaani.org/format/). 

Sam XZ jest właściwie tylko nakładką, wygodnym interfejsem. Jego fundament nazywa się `liblzma`.  
*Lib* to tutaj skrót od *library*, biblioteka. Zestaw przydatnych funkcji. LZMA oznacza natomiast metodę kompresji.

{:.post-meta .bigspace-after}
Taki podział jest bardzo częsty w&nbsp;świecie *open source*. Osobno bebechy programu, w&nbsp;formie biblioteki. Osobno interfejs dla użytkownika. Dzięki tej modułowości można łatwo wybierać rzeczy dopasowane do swoich potrzeb.

Dla uproszczenia będę stosował w&nbsp;tym wpisie zbiorcze określenie XZ wobec wszystkich narzędzi i&nbsp;bibliotek, jakie powstały z&nbsp;„zatrutego” kodu.

Cały projekt, w&nbsp;ramach którego rozwija się XZ, nosi nazwę [Tukaani](https://tukaani.org/). Logo projektu to rysunkowy tukan z&nbsp;obrazka wyżej. Założycielem i&nbsp;głównym opiekunem projektu jest od 2009&nbsp;roku Lasse C., istotna postać w&nbsp;tej historii.

Dzięki lekkości i&nbsp;wszechstronności jego wynalazki zwróciły uwagę innych projektów. A&nbsp;Lasse, niczym Atlas, dostał na barki cały glob. Ale o&nbsp;tym później.

### Cyfrowy łańcuch dostaw

Istotną częścią całej sprawy są różne powiązania między projektami *open source*. Można powiedzieć, że **kod spływa z&nbsp;góry, od źródła**. W&nbsp;języku angielskim jest ono zresztą nazywane *upstream*, jak źródło rzeki.

Naj początku łańcuszka jest jakiś projekt, jak wspomniany Tuukani. Kod źródłowy jego programów jest na widoku, przechowywany w&nbsp;tak zwanym *repozytorium*. Tak było też z&nbsp;XZ, choć [jego strona](https://github.com/tukaani-project/xz/releases) jest obecnie zawieszona.

{:.figure .bigspace}
<img src="/assets/posts/centralizacja/xz/xz-blokada-repozytorium.jpg" alt="Komunikat mówiący o&nbsp;zawieszeniu dostępu do projektu przez naruszenie warunków serwisu Github"/>

Każdy może czytać kod programów i&nbsp;proponować własne zmiany oraz usprawnienia. Jeśli zostaną zaakceptowane przez osoby opiekujące się projektem -- to w&nbsp;ciągu paru sekund zostaną wdrożone.

Każdy program może się przebić i zwrócić uwagę innych projektów, jak Linuksy. Będę używał kolokwialnie liczby mnogiej, bo **na bazie jednego Linuksa (jądra) powstało wiele systemów**. Zwanych *dystrybucjami*, rozwijanych często niezależnie od siebie.

Twórcy Linuksów biorą przydatne według nich programy i&nbsp;dodają je do swoich systemów. Czasem jako udogodnienia dla użytkowników, a&nbsp;czasem wręcz jako filary systemu. Kod od XZ bywał bliżej tej drugiej kategorii.

Ostatnim ogniwem łańcuszka są właściciele komputerów (tu głównie firmy mające swoje serwery). Decydują się na Linuksa, bo to system wszechstronny i&nbsp;przyjazny w&nbsp;obsłudze. Wybierają którąś z wielu jego wersji, instalują.

Na tych serwerach opiera się sieć, z&nbsp;której korzystają zwykli użytkownicy. Nie mając pojęcia, że świat stoi na Linuksie.

{:.bigspace-before}
<img src="/assets/posts/centralizacja/xz/open-source-linux-zaleznosci.jpg" alt="Schemat zależności. U&nbsp;góry widać pojedynczy plik podpisany XZ. Odchodzą od niego strzałki do ikon kilku wariantów systemu Linux. Od nich z&nbsp;kolei odchodzą strzałki w&nbsp;stronę licznych rysunkowych ikon serwerów."/>

{:.figcaption}
W praktyce nie każda dystrybucja byłaby równie popularna na serwerach.  
Źródło: oficjalne ikony projektów, [serwery](https://www.flaticon.com/free-icon/server_742282) autorstwa *Smashicons* (serwis Flaticon).

Przy takich zależnościach „zatrucie źródła” oznacza, że zagrożenie dotknie bardzo wielu serwerów. Mnóstwo rzeczy zależy od kilku nielicznych, popularnych projektów. Dlatego są łakomym kąskiem dla hakerów.  
Infekowanie popularnych źródeł nazywa się oficjalnie „atakami na łańcuch dostaw” (ang. *supply chain attacks*).
 
Czyżby otwartość kodu na cudzy wkład była wadą? Nie. Powiedziałbym wręcz, że **to dzięki tej otwartości w&nbsp;ogóle udało się wychwycić zagrożenie**.

Gdzieś na świecie istnieją projekty komercyjne, do których również ktoś dodał niespodzianki. Przez brak przejrzystości trudniej jest taki kod przeszukać i&nbsp;wykryć pułapki. Ale to temat na inną opowieść. Na razie wszystko toczy się w świecie *open source*.
## Atak krok po kroku

Cała historia jest moim zdaniem dużo ciekawsza, jeśli wyjdzie się poza technikalia. Jest to wtedy opowieść o&nbsp;presji społecznej, zdobywaniu zaufania i&nbsp;zdradzie.

### Problem zmęczonego opiekuna projektu

Jednym z&nbsp;najciekawszych faktów w&nbsp;sprawie jest to, że **cała akcja rozpoczęła się parę lat temu**. W&nbsp;momencie, kiedy użytkownik określający siebie mianem Jia Tan wkupił się w&nbsp;łaski Lassego C., twórcy XZ.

Tworzenie własnych projektów *open source* może być przyjemną odskocznią. Przykład: ja i&nbsp;ten blog. Do tej pory dał mi dużo radości, a&nbsp;interakcje z&nbsp;innymi ludźmi były niemal wyłącznie pozytywne.

Ale nie każdy ma tak fajnie. Czasem zdarza się, że osoba prowadząca popularny projekt doświadcza presji, żeby dodawać nowe rzeczy.  
Jakiś korpoludek potrzebuje programu, ale nie umiałby samodzielnie go zmodyfikować. Więc naciska na twórców, żeby wprowadzili potrzebne mu zmiany.

Im większy projekt, tym większa presja. U&nbsp;niektórych osób z&nbsp;własnymi projektami rośnie również poczucie odpowiedzialności.  
Gdy zaczynali, projekt mógł być małą, radośnie szlifowaną kulką. Ale presja społeczna potrafi zrobić z&nbsp;niego glob, który muszą trzymać na barkach. Jak tytan [Atlas](https://pl.wikipedia.org/wiki/Atlas_(mitologia)).

Na ten temat powstał nawet bardzo trafny obrazek:

{:.figure .bigspace-before}
<img src="/assets/posts/centralizacja/xz/xkcd-2347-dependency.jpg" alt="Obrazek pokazujący stos klocków ułożonych na sobie, podpisanych 'współczesna cyfrowa infrastruktura'. Prawie cała piramida opiera się na drobnym, pojedynczym klocku, podpisanym jako element utrzymywany przez losową, niedocenianą osobę od 20023&nbsp;roku."/>

{:.figcaption}
Źródło: [XKCD](https://xkcd.com/2347/).

Podobna sytuacja dotknęła Lassego od XZ, którego projekt miał na karku już kilkanaście lat. I&nbsp;zaczynał budzić u&nbsp;autora poczucie wypalenia. Wtedy pojawiła się postać skora do pomocy, przedstawiająca się jako Jia Tan.

Ciekawą [chronologię zdarzeń](https://boehs.org/node/everything-i-know-about-the-xz-backdoor), obejmującą pierwsze kroki JT w&nbsp;świecie *open source*, można znaleźć na stronie *boehs.org*.

### Dobry i&nbsp;zły glina

Znaną metodą prowadzenia przesłuchań jest podział ról na dobrego i&nbsp;złego.  
Jedna postać jest wyjątkowo niesympatyczna, pomiata przesłuchiwanym. Druga zapewnia z&nbsp;kolei ludzkie ciepło i&nbsp;zrozumienie. Dzięki temu osłabia czujność i&nbsp;może wyciągnąć informacje.

Opis z&nbsp;*boehs.org* wydaje się sugerować, że coś takiego zaszło w&nbsp;tym przypadku. Pojawiło się konto, które wywierało presję na Lassego, właściciela całego projektu. 

Interakcje można znaleźć na publicznej liście mailingowej. W&nbsp;[dyskusji z&nbsp;kwietnia 2022&nbsp;roku](https://www.mail-archive.com/xz-devel@tukaani.org/msg00555.html) biorą udział zarówno Jia, jak i&nbsp;niejaki Jigar K. Ten drugi narzeka na opieszałość Lassego:

{:.bigspace-before}
> Patrząc na powolne tempo aktualizacji, niestety miną lata, zanim społeczność w&nbsp;ogóle dostanie tę przydatną poprawkę.

{:.figcaption}
Tłumaczenia wszystkich maili i&nbsp;postów moje.

Jia odpowiada grzecznie, ale wydając się trzymać stronę Lassego:

{:.bigspace}
> Nad tym projektem pracują hobbyści. Nie możemy poświęcać ponad 40&nbsp;godzin tygodniowo na szybkie wypuszczanie rzeczy wysokiej jakości. Dzięki za zrozumienie

Ale Jigar wciąż naciska, wprost sugerując, żeby Jia wziął sprawy w&nbsp;swoje ręce:

{:.bigspace-before}
> Czy są jakieś postępy w&nbsp;tej sprawie? Jia, widzę jakieś niedawne *commity* od ciebie. Dlaczego nie możesz sam wprowadzić zmian?

{:.figcaption}
*Commit* to pojedynczy, często opisany zestaw zmian w&nbsp;kodzie źródłowym. Może mieć dowolny rozmiar, od jednego znaku po całe pliki.

Takie komentarze się powtarzały również w&nbsp;innych wątkach. W&nbsp;jednym z&nbsp;nich Lasse w&nbsp;końcu [nie wytrzymał](https://www.mail-archive.com/xz-devel@tukaani.org/msg00567.html) i&nbsp;wprost napisał, że jest zmęczony całym projektem. Przy okazji wypowiedział słowa, które niestety okazały się prorocze.

{:.bigspace}
> Ostatnio Jia Tan i&nbsp;ja trochę współpracowaliśmy nad XZ Utils poza listą \[mailingową\], **być może odegra w&nbsp;przyszłości większą rolę**, zobaczymy.  
Warto też pamiętać, że to projekt hobbystyczny, za który nikt nie płaci. 

Nawet po tych słowach Jigar nie dawał za wygraną i&nbsp;naciskał na zmiany.

{:.bigspace}
> Dusisz teraz własne repo. Po co czekasz ze zmianą właściciela do wersji 5.4.0? Po co opóźniasz to, czego potrzebuje twoje repo?

„Dej, dej”. Jak pewien znany typ ludzi, gdy wrzuci się coś darmowego na OLX-a. Możliwe, że wobec takiej presji autor nie miał nic przeciwko, żeby Jia zdjął mu z&nbsp;barków nieco ciężaru.

{:.post-meta .bigspace-after}
Nie wykluczam, że Jigar to zwykły dupek, a&nbsp;JT wykorzystał okazję, i&nbsp;że nie współpracowali. Ale późniejszy wątek forsowania aktualizacji stawie te naciski w&nbsp;ciekawym świetle. 

### Jia przejmuje stery

Jia był jak złota rączka, angażując się w&nbsp;najróżniejsze działania związane z&nbsp;XZ. Pewien użytkownik Mastodona [doliczył się](https://hachyderm.io/@joeyh/112180715824680521) 750&nbsp;*commitów* od tej postaci.

W 2023&nbsp;roku opracował nawet logo dla programu, w&nbsp;czterech wariantach kolorystycznych.

{:.figure .bigspace}
<img src="/assets/posts/centralizacja/xz/xz-nowe-logo.jpg" alt="Zrzut ekranu strony projektu Tukaani, widać na nim logo programu XZ. Jako autor wpisany jest Jia Tan." width="60%"/>

Poza tym opracowywał testy i&nbsp;dodawał pliki testowe.  
To ważna część projektów *open source*. Ale nieraz olewana, jeśli twórcy wolą skupić się na bajerach. Poświęcanie uwagi szlifom i&nbsp;fundamentom mogło sugerować, że nowemu współpracownikowi autentycznie zależy na rozwoju projektu.

Z czasem Jia stał się *de facto* motorem napędowym XZ. Na [zarchiwizowanej stronie](https://web.archive.org/web/20240329182405/https://xz.tukaani.org/xz-utils/) można znaleźć informację, że od wersji 5.4.3 to on składał cyfrowy podpis na aktualizowanych plikach.

### Jia zdejmuje maskę

Po zyskaniu zaufania Jia zaczął wprowadzać w&nbsp;tym roku subtelne, groźne zmiany w&nbsp;kodzie.

{:.figure .bigspace-before}
<img src="/assets/posts/centralizacja/xz/jia-historia-aktywnosci.jpg" alt="Schemat pokazujący, w&nbsp;jakich dniach i&nbsp;godzinach Jia wprowadzał zmiany w&nbsp;kodzie. Zmiany złośliwe wyróżniają się tym, że dodano je w&nbsp;środku nocy."/>

{:.figcaption}
Groźne zmiany wyróżniają się tym, że dodano je w&nbsp;innych godzinach niż zwykle. Do wątku naprawienia błędów Valgrinda jeszcze wrócę.  
Źródło: [tweet użytkownika *birchb0y*](https://twitter.com/birchb0y/status/1773871381890924872).

26 lutego dokonał sabotażu „kropką nienawiści”. Przez umieszczenie jej w&nbsp;kodzie powodował błąd, przez który [nie włączał się Landlock](https://old.reddit.com/r/linux/comments/1brhlur/xz_utils_backdoor/kx9b9wc/). Taki dobrowolny ogranicznik stosowany przez XZ, dzięki któremu odbierał sobie dostęp do wrażliwych funkcji systemu.

Oto [historia zmian](https://git.tukaani.org/?p=xz.git;a=commitdiff;h=328c52da8a2bbb81307644efdb58db2c422d9ba7) wprowadzonych tego dnia. Plusy oznaczają dodane linijki kodu.  
Przy tym interfejsie, wśród wielu zmian, łatwo przeoczyć kropkę na początku linijki, zlewającą się z&nbsp;plusem.

{:.figure .bigspace}
<img src="/assets/posts/centralizacja/xz/xz-kropka-sabotaz.jpg" alt="Zrzut ekranu pokazujący kilka linijek dodanych do kodu. Jedna z&nbsp;nich to samotna kropka"/>

### Broń ukryta w&nbsp;testach

Zabójcza kropka była tylko pomocą przy ataku. *Opus magnum* naszego hakera to **wykorzystanie plików testowych do ukrycia swoich narzędzi**. Tak; tych samych plików, które dodawał, wydając się umacniać fundamenty projektu.

Jeden z&nbsp;plików z&nbsp;założenia miał być popsuty, żeby testy sprawdzały działanie XZ przy wadach formatu. Drugi miał normalną treść, rozpakowywał się, działał jak powinien.

Oba zawierały w&nbsp;sobie narzędzia hakera, głównie skrypty w&nbsp;[języku Bash](https://stackoverflow.com/a/28693815). Ukryte w&nbsp;plikach jak bronie partyzantów w&nbsp;skrytce pod ściółką leśną.

{:.bigspace-after}
<details>
<summary><strong>Intuicyjne wyjaśnienie</strong></summary>

<p class="bigspace-before">Ta dwoista natura (normalność, a&nbsp;zarazem złośliwość) wynika z&nbsp;prostego faktu – <strong>każdy plik jest ciągiem zer i&nbsp;jedynek</strong>.<br />
Owszem, istnieje jakiś <em>właściwy</em> sposób ich czytania, przy którym plik zadziała tak, jak oczekują tego użytkownicy. Ale można również brać te same zera i&nbsp;jedynki, robiąc z&nbsp;nimi rzeczy kreatywne.</p>

<p>Przykład? Ktoś może wskazać swojemu programowi jakiś zero-jedynkowy plik i&nbsp;nakazać: “weź sześćdziesiąty piąty element (zero/jedynkę). Potem bierz kolejne, do numeru 72&nbsp;włącznie”. Program po kolei je zbiera i&nbsp;zostaje z&nbsp;ciągiem <code class="language-plaintext highlighter-rouge">01100001</code>.</p>

<p>Następnie autor każe: “zrób z&nbsp;tego literę w&nbsp;podstawowym kodowaniu (ASCII)”. Wynik to <code class="language-plaintext highlighter-rouge">a</code>, bo właśnie taka litera <a href="http://sticksandstones.kstrom.com/appen.html">odpowiada tym zerom i&nbsp;jedynkom</a>.</p>

<p>Te zera i&nbsp;jedynki z&nbsp;założenia nie miały być żadną literą. Były cząstką całkiem innej struktury. Ale jeśli ktoś każe zrobić z&nbsp;nich literę… to program posłucha.</p>

<p>To dlatego atakujący mógł stworzyć pełnoprawny, działający plik XZ. W&nbsp;którym jednocześnie ukrywa sobie różne rzeczy. Po odpowiednich przekształceniach może je sobie wyciagnąć.</p>

<p class="post-meta">Koniec wyjaśnienia</p>
</details>

Jeśli chodzi o&nbsp;zawartość hakerskich skryptów, mało się znam na temacie, więc zdam się tu na [opracowanie Gynvaela Coldwinda](https://gynvael.coldwind.pl/?lang=en&id=782). Jeśli dobrze interpretuję:

* Punktem początkowym jest zwięzły skrypt umieszczony między innymi plikami projektu.

  Według innego komentarza dodany [nie do wersji źródłowej](https://news.ycombinator.com/item?id=39885139), lecz tylko do tej przeznaczonej do rozpowszechnienia.  
  Jest uruchamiany podczas **kompilacji**. Czyli przekształcania kodu do postaci dostosowanej do komputera. Zachodzi ona za każdym razem, gdy ktoś tworzy z&nbsp;kodu źródłowego XZ nową wersję programu.

* Ten zwięzły skrypt „naprawia” jeden z&nbsp;plików testowych, `bad-3-corrupt_lzma2.xz` (poprzez kilka działań typu „znajdź i&nbsp;zamień”).  
  Część naprawionej zawartości pliku to skrypt ukryty tam wcześniej przez hakera.

* Wyciągnięty skrypt zostaje uruchomiony i&nbsp;sięga do drugiego pliku testowego, `large_compressed.lzma`.  
  Tym razem naprzemiennie olewa i&nbsp;wyciąga niektóre jego elementy. Układając z&nbsp;nich sobie kolejny skrypt.

* Na tym etapie kończy się wyciąganie hakerskich narzędzi z&nbsp;plików testowych. Skrypt hakera gmera przy różnych ustawieniach kompilacji, a&nbsp;także wrzuca do wnętrza XZ własny zero-jedynkowy plik, zapewne najgroźniejszą część.
  
  Pełna treść skryptu jest [tutaj](https://www.openwall.com/lists/oss-security/2024/03/29/4/1). Nie będę udawał, że go rozumiem, ale widać że zmienia różne parametry, jak [`CPPFLAGS`](https://stackoverflow.com/questions/2754966/cflags-vs-cppflags).

{% include info.html
type="Ciekawostka"
text="Jak pisze Gynvael Coldwind, w&nbsp;tym miejscu występuje również odwołanie do innych plików testowych, które miałyby w&nbsp;sobie odpowiednie ciągi zer i&nbsp;jedynek. Takich plików nie było w&nbsp;żadnej z&nbsp;zainfekowanych wersji źródła.  
Zgodnie z&nbsp;[hipotezą](https://gynvael.coldwind.pl/?lang=en&id=782#stage2-ext) Coldwinda, Jia zapewne planował dodać je w&nbsp;przyszłości. Pozwoliłyby rozbudowywać kolejne wersje XZ o&nbsp;nowe wredne funkcje."
%}

Ostatecznie następuje normalna kompilacja. Ale przez wprowadzone zmiany powstaje wariant XZ (oraz innych bibliotek) z&nbsp;tak zwanym *backdoorem*. Cyfrową furtką do wykorzystania przez inne, wiedzące o&nbsp;niej programy. W&nbsp;tej postaci trafia do różnych Linuksów.

Nie wiem, na czym dokładnie polega zagrożenie ze strony zmienionego XZ, bo nadal trwają analizy. Ale na pewno robił coś więcej, niż niegroźna kompresja i&nbsp;dekompresja.

### Udoskonalenie złośliwego kodu

Groźna niespodzianka została dodana w&nbsp;wersji 5.6.0. Ale na tym etapie miał swoje wady. Odrobinę porównań między wersjami można znaleźć we wspomnianej analizie Coldwinda.

Jednym z&nbsp;problemów był fakt, że program Valgrind (do analizowania zużycia pamięci) wyłapywał różne błędy i&nbsp;wyświetlał ostrzeżenie na etapie kompilacji.

A to niedobrze dla hakera. Ostrzeżenia, nawet jeśli nie mówią wprost o&nbsp;czymś złym, kłócą się z&nbsp;dyskrecją.

Dlatego... po prostu zgłosił błąd, pytając innych o&nbsp;porady. Oczywiście nie ujawniał swoich intencji. Wspólną pracą, między innymi z&nbsp;ludźmi od&nbsp;linuksowych projektów Red Hat i Fedora, udało się [załatać błędy](https://bugzilla.redhat.com/show_bug.cgi?id=2267598). Jia wypuścił udoskonaloną wersję 5.6.1.  
Nikt się nie połapał, że coś jest na rzeczy.

### Lobbowanie za przyjęciem nowinek

Haker osiągnął swój cel. Nowa wersja XZ była „zaminowana”, a&nbsp;najnowsza była ponadto dyskretniejsza, nie prowadząc do podejrzanych ostrzeżeń.

Kolejnym krokiem było rozpowszechnienie kodu. Sprawienie, żeby różne warianty Linuksa przygarnęły zmodyfikowane wersje.

Jak wspomina ktoś na forum HN, napastnik już wcześniej krążył wokół decyzyjnych osób od różnych Linuksów i&nbsp;zachęcał do przyjęcia nowej, zaminowanej wersji XZ:

{:.bigspace-before}
> autor tej furtki kontaktował się ze mną przez kilka tygodni, chcąc żebym dodał XZ w&nbsp;wersji 5.6.x do Fedory 40&nbsp;i 41, ze względu na jego „świetne nowe funkcje” 

{:.figcaption}
Źródło: [komentarz z&nbsp;HN](https://news.ycombinator.com/item?id=39866275). Fedora to jeden z&nbsp;wielu wariantów systemu Linux, całkiem popularny.

Również na liście mailingowej pojawiło się więcej osób wskazujących, że mają [kłopoty z&nbsp;Valgrindem](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1067708), więc chętnie by przyjęli nową wersję XZ. Naciski nieco podobne do tych wywieranych wcześniej przez Jigara.

{:.bigspace}
> Dodatkowe komunikaty z&nbsp;Valgrinda sprawiają, że nie przechodzi u&nbsp;mnie część testów. Ta nowa wersja powinna to rozwiązać. Chciałbym ją mieć, żeby móc dalej *hakować*{:.corr-del} pracować.

Pod względem skuteczności ten lobbing mógłby zawstydzić nawet [trolle od firmy Monsanto]({% post_url 2022-12-24-biotechnologia-trolle-youtube %}){:.internal}! Nowy promowany XZ trafiał do kolejnych Linuksów.

### Wykrycie furtki

Złośliwy kod wykrył pewien programista, Andres Freund. Łączył się z&nbsp;bazą i&nbsp;zauważył anomalię. Wszystko działało wolniej.

Dostrzegł, że dziwne działanie było związane z&nbsp;programem `sshd`. Służącym do łączenia się z&nbsp;serwerem w&nbsp;szyfrowany sposób.  
To trochę jak wpisywanie hasła do swojego laptopa, żeby wyświetlił się pulpit. Tyle że maszyna może być dużo dalej, a&nbsp;zamiast pulpitu jest tekstowa konsola.

Kiedy dostrzegł, co się święci, dał znać autorom projektów. A&nbsp;po ustalonym czasie [wszczął alarm](https://www.openwall.com/lists/oss-security/2024/03/29/4). To właśnie informacje od niego wywołały poruszenie, o&nbsp;którym napisałem na początku.

Na tym etapie różne dystrybucje Linuksa przywróciły awaryjnie starszą wersję XZ i&nbsp;powiązanych narzędzi. Serwis Github zablokował konta hakera i&nbsp;samego projektu.

Zaś Lasse od XZ -- co widać na innej, niezablokowanej stronie z&nbsp;kodem źródłowym -- zaczął usuwać niekorzystne zmiany, takie jak wspomniana kropka grozy.

Póki repozytorium nie zostało usunięte, widać było komentarze różnych ludzi pod jego adresem. Zarzucające, że niedostatecznie mocno trzymał glob, na którym siedli.

{% include info.html
type="Ciekawostka"
text="W normalnych warunkach SSH oraz XZ byłyby rzeczami niezwiązanymi ze sobą.  
Ale wersja programu OpenSSH na wielu Linuksach jest zmodyfikowana, żeby wspierać inny moduł, `systemd`. Który już [korzysta z&nbsp;XZ](https://twitter.com/metala/status/1773762175682658348), łącząc te dwa światy."

trailer="<p>Swoje odkrycie autor opatrzył ironicznym komentarzem: „<code>systemd</code> uderza ponownie!”.</p>
<p>W światku Linuksa budzi on niemałe <a href='https://blog.erratasec.com/2015/08/about-systemd-controversy.html'>kontrowersje</a>. To zestaw złożonych programów działających w&nbsp;tle i&nbsp;ingerujących w&nbsp;różne funkcje systemu. Czasem zarzuca się im próbę bycia wszystkim naraz, wbrew linuksowej konwencji drobnych i&nbsp;niezależnych programów.</p>"
%}

Póki co wygląda na to, że udało się zapobiec większemu atakowi. Ludziom zaleca się cofnięcie do starszych wersji XZ. Być może nawet do tych sprzed działalności pana J. A&nbsp;na pewno do innych niż 5.6.0 oraz 5.6.1.

Trwa również analizowanie tej bardziej tajemniczej, nieprzejrzystej części złośliwego kodu. Postępy można śledzić chociażby [na forum HN](https://news.ycombinator.com/item?id=39877267). 

## Podsumowanie

Sprawa wokół `xz` nie jest niczym nowym. Choć zaskakuje wyrafinowaniem, jest jednym z&nbsp;wielu ataków na źródła powszechnie używanych programów.  
Innym głośnym przykładem, tyle że z&nbsp;korpoświata, była afera wokół [SolarWinds](https://www.reuters.com/article/us-cyber-solarwinds-microsoft-idUSKBN2AF03R/).

Cała historia potwierdza, że **centralizacja to miecz obosieczny. Również w&nbsp;świecie cyfrowym**.

Z jednej strony pozwala uniknąć powtarzania się, wielokrotnego wymyślania koła od nowa. Rozwój jakiegoś elementu zostawia się specom, a&nbsp;reszta tylko od nich czerpie.

Z drugiej -- to zależność od kogoś innego. Być może nieco mniej groźna w&nbsp;cyfrowym świecie, gdzie łatwo kopiować kod... Ale wciąż pozostaje wkładaniem wszystkich jajek do jednego koszyka. Jak rypnie, to potężnie.

A większość przegapia moment, gdy wiklina koszyka zaczyna się rozłazić. Bo każdy sobie myśli, że inni na pewno uważnie patrzą. Że można olać temat.

### Wątek roszczeniowości

Afera ukazuje również wątek niedocenianych twórców *open source*. Być może Jigar z&nbsp;tej konkretnej historii był akurat podstawionym „złym gliną”, nie wiem. Ale wokół znalazłoby się [wielu innych](https://news.ycombinator.com/item?id=9873125), którzy przejąć projektu nie planują, a&nbsp;są tak samo roszczeniowi.

A twórcy, próbując sprostać oczekiwaniom, z&nbsp;czasem tracą radochę z&nbsp;dzieła, które tak długo dopracowywali.

Dlatego w&nbsp;tym miejscu podzielę się radą.  
Czytelniczko, czytelniku. Jeśli tworzysz publiczny kod albo inne utwory i&nbsp;ktoś wywiera presję, to pamiętaj -- **twoje życie ponad wszystko, masz jedno**.

Póki ludzie kontaktują się w sposób cywilizowany, to super. Można powymieniać się przemyśleniami, posłuchać sugestii.

Ale gdy jakiś Jigar naciska z&nbsp;pasywną agresją, publicznie cię upokarza, pisze „potrzebujemy” albo „wiele osób potrzebuje” -- to robi taki psychologiczny odpowiednik nadymania się jak ropucha. Próbuje wydać się większy. Rozgnieć go.

Nie ma żadnej grupy, żadnego wyższego interesu, nie trzeba trzymać globu. To tylko jakiś „dej-dej” próbuje pogorszyć twoje życie, żeby poprawić własne.  
Uzasadnioną odpowiedzią wobec takiego kogoś jest blokada. Albo „spieprzaj”.

{:.post-meta .bigspace-after}
A na wypadek, gdyby agresor chciał się zemścić za asertywność donosem do pracodawcy -- można prowadzić projekty anonimowo. Bez wiązania ich z&nbsp;prawdziwą tożsamością. 

Stanowczość na pewno ratuje dobrobyt psychiczny. A&nbsp;może nawet, kto tam wie, zapobiegnie wejściu hakera :wink: 
