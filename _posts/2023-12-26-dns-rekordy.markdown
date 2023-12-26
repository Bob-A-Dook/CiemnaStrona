---
layout: post
title: "DNS jako publiczna skrytka"
subtitle: "Notatki na drogowskazie."
description: "Notatki na drogowskazie."
date:   2023-12-26 16:23:00 +0100
tags: [DNS, Internet, Konsola, Podstawy]
image:
  path: /assets/posts/internet/dns/rekordy-dns/rekordy-dns-baner.jpg
  width: 1200
  height: 700
  alt: "Zdjęcie drogowskazu zakrytego różnymi nalepkami. Zamiast jednej z nazw miejscowości widać napis ciemnastrona.com.pl. Karteczki naklejone na znak są podpisane 'Rekordy DNS'."
---

Niedawno trafiłem na ciekawy, krótki wpis na stronce The Den (*theden.sh*), poświęcony [nietuzinkowemu sposobowi na przechowywanie danych](https://thoughts.theden.sh/posts/dns-txt-record-fun/).

Nietypową skrytką byłby tutaj DNS. Ta część internetu, którą można porównać do książki telefonicznej lub do precyzyjnego drogowskazu.  
Każda osoba mająca własną domenę może modyfikować te informacje, które jej dotyczą. Autor proponuje **modyfikację, która jest jak doklejenie na drogowskazie albo na stronie książki karteczki z&nbsp;informacjami**. 

Wpis z&nbsp;The Den jest całkiem przystępny dla osób, które miały okazję korzystać z&nbsp;programów konsolowych. Ale dla innych będzie wyglądał jak ciąg niezrozumiałych pojęć oraz inkantacji.

Postanowiłem zatem „przetłumaczyć” wpis dla mniej konsolowych hobbystów. Raz: może więcej osob go doceni. Dwa: w&nbsp;ten sposób lepiej ułożę fundamenty we własnej głowie. Tak jak już kiedyś zrobiłem w&nbsp;przypadku artykułu na temat [pewnej cyfrowej blokady]({% post_url 2023-04-26-imx-deblobbing-konsola %}){:.internal}.

Zapraszam!

{:.figure .bigspace-before}
<img src="/assets/posts/internet/dns/rekordy-dns/rekordy-dns-baner.jpg" alt="Zdjęcie drogowskazu na północy Wielkiej Brytanii, prawie w&nbsp;całości zakrytego różnymi nalepkami. Obrazek jest przerobiony, zamiast jednej z&nbsp;nazw miejscowości widać napis ciemnastrona.com.pl. Karteczki naklejone na znak są podpisane 'Rekordy DNS'."/>

{:.figcaption}
Źródła: [*Daily Record*](https://www.dailyrecord.co.uk/news/scottish-news/john-o-groats-signpost-obliterated-13276289), Flaticon, przeróbki moje. Szczegóły pod koniec wpisu.

### Spis treści

* [DNS i&nbsp;rekordy](#dns-irekordy)
  * [Dig i&nbsp;zaglądanie do rekordów DNS-a](#dig-izaglądanie-do-rekordów-dns-a)
  * [Nie tylko adresy IP](#nie-tylko-adresy-ip)
* [Omówienie wpisu z&nbsp;The Den](#omówienie-wpisu-zthe-den)
  * [Początek](#początek)
  * [Etap szyfrowania](#etap-szyfrowania)
  * [Umieszczanie danych w&nbsp;DNS-ie](#umieszczanie-danych-wdns-ie)
  * [Odszyfrowywanie danych](#odszyfrowywanie-danych)
* [Podsumowanie](#podsumowanie)


## DNS i&nbsp;rekordy

Wpis kręci się wokół DNS-a, więc na początek napiszę o&nbsp;nim parę słów.

To jeden z&nbsp;filarów współczesnego internetu. Choć mało kto o&nbsp;nim wie, DNS cały czas działa w&nbsp;tle, mówiąc przeglądarkom, dokąd mają iść. Ujawnia na ich prośbę, jaki adres „komputerowy” (IP) odpowiada czytelnemu adresowi „ludzkiemu” (jak *ciemnastrona.com.pl*).

DNS bierze udział w&nbsp;najprostszych, codziennych wędrówkach po sieci.  
Gdy klikniemy w&nbsp;przeglądarce link do jakiejś strony, której nigdy (bądź od jakiegoś czasu) nie odwiedzaliśmy, to przeglądarka nie będzie go znała. I&nbsp;zapyta jakiegoś DNS-a.

*Jakiegoś*, bo nie ma jednego, centralnego, globalnego systemu. **Istnieje [wiele różnych](https://public-dns.info/), niezależnych od siebie serwerów DNS**.  
W praktyce przeglądarka często zwraca się do tych sugerowanych przez hotspota, z&nbsp;którym jest połączony komputer. Chyba że ustawi się coś innego w&nbsp;opcjach.

{% include info.html
type="Powiązane wpisy"
text="DNS już parę razy gościł na łamach tego bloga.  
Raz wspominałem o&nbsp;jego powiązaniach z&nbsp;internetową prywatnością. Czasem jej szkodzi, bo ukazuje firmom telekomunikacyjnym, jakie ktoś odwiedzał strony. Czasem pomaga -- odgrywa kluczową rolę w nowej, raczkującej metodzie [szyfrowania (meta-)danych](/internetowa_inwigilacja/2022/08/14/dns-dot-doh){:.internal}.  
Innym razem pisałem o&nbsp;tym, że [może być narzędziem cenzury](/2022/09/12/dns-ip-cenzura){:.internal}. Na życzenie swoich właścicieli okłamującym internautów, że jakaś strona nie istnieje."
%}

DNS to jednak nie tylko wyrocznia mówiąca, jakie IP odpowiada danej stronie. Może przechowywać więcej rodzajów informacji. 

### Dig i&nbsp;zaglądanie do rekordów DNS-a

Typowe przeglądarki, jak Firefox, to świetna sprawa dla osób ciekawych świata. Pozwalają łatwo zajrzeć za kulisy odwiedzanych stron internetowych.

Jakiś ciekawy element, niestandardowa animacja? Można kliknąć prawym przyciskiem myszy i&nbsp;wybrać opcję `Zbadaj` albo `Zbadaj element`. I&nbsp;wczytać się w kod strony (czasem całkiem czytelny). Eksperymentować, zmieniać wartości. Zobaczyć, jak działa ten świat :relaxed:.

W przypadku DNS-a niestety nie ma tak dobrze.  
Przeglądarka ukrywa interakcje z&nbsp;nim przed użytkownikami i&nbsp;nie daje równie łatwego wglądu „pod maskę”. Na plus wyróżnia się tutaj Firefox, bo przynajmniej [daje taki wgląd *dodatkom przeglądarkowym*](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/dns). Ale to jednak nie do końca to samo.

Na szczęście istnieją inne **programy, które pozwalają prosić DNS-a o&nbsp;różne rzeczy**. Jednym z&nbsp;najbardziej znanych jest `dig` (skrót od [*Domain Information Groper*](https://en.wikipedia.org/wiki/Dig_(command)#History)).

W najprostszym przypadku można użyć komendy:

```
dig DOMENA
```

Gdzie DOMENA oznacza czytelną nazwę „trzonu” strony. Na przykład *google.com* -- znana wszystkim wyszukiwarka i&nbsp;jeden z&nbsp;głównych szwarccharakterów na tym blogu.

Wyświetli się lista informacji, jakie `dig` uzyskał od DNS-a na temat podanej domeny. O&nbsp;ile strona funkcjonuje i&nbsp;nie jest przez pytanego DNS-a cenzurowana, to wyświetli się takie coś:

{:.figure .bigspace}
<img src="/assets/posts/internet/dns/rekordy-dns/dns-google-odpowiedz.jpg" alt="Fragment odpowiedzi otrzymanej od DNS-a. Posiada ona nagłówek 'Sekcja odpowiedzi', a&nbsp;pod spodem widać jedną linijkę tekstu. Na jej końcu znajduje się adres IP, złożony z&nbsp;czterech liczb rozdzielanych kropkami"/>

Liczby i kropki na końcu to adres IP. To właśnie jego otrzymują przeglądarki po zapytaniu DNS-a. Po czym wysyłają pod niego prośbę o&nbsp;stronę, już do samego Google'a.

### Nie tylko adresy IP

...Ale to tylko najbardziej podstawowe zastosowanie. Literka `A` w&nbsp;wyniku wskazuje konkretny rodzaj rekordu -- odpowiadający adresom IP, a&nbsp;dokładniej IPv4. To tylko jeden z&nbsp;wielu dostępnych rodzajów!

Można rozszerzyć wcześniejszą komendę, dopisując do niej rodzaj rekordu:

```
dig DOMENA REKORD
```

Można spróbować tam wpisać `any`, żeby zdobyć wszystkie możliwe rekordy, ale nie każdy DNS to wspiera. Można też wpisać jakiś konkretniejszy rodzaj [z dostępnej listy](https://en.wikipedia.org/wiki/List_of_DNS_record_types).

Poniżej rekordy, jakie DNS pokazuje w&nbsp;odpowiedzi na różne prośby `dig`a związane ze stronką *theden.sh*:

{:.bigspace-before}
<img src="/assets/posts/internet/dns/rekordy-dns/dns-rekordy-przyklad.jpg" alt="Tabelka złożona z dwóch najważniejszych kolumn. Pierwsza z nich ma tytuł Komenda i widać nad nią ikonę laptopa. Znajdują się w niej trzy warianty komendy dig theden.sh, dla różnych nazw rekordów. Kolumna druga, nad którą jest ikona serwera, jest zatytułowana Odpowiedź."/>

{:.figcaption}
Odpowiedź DNS-a na zapytanie ogólne `any` to [nawiązanie](https://blog.cloudflare.com/rfc8482-saying-goodbye-to-any/) do jednego z&nbsp;internetowych standardów, RFC8482. Sprowadza się z&nbsp;grubsza do: „Nie muszę odpowiadać na to zapytanie”.

## Omówienie wpisu z&nbsp;The Den

Podstawy DNS-a i&nbsp;rekordów przybliżyłem, więc przejdę teraz do wpisu z&nbsp;The Den. Mówiąc ogólnie: autor wpadł na pomysł, żeby użyć rekordów `TXT` (przeznaczonych na ogólne informacje w&nbsp;formie tekstu) i&nbsp;chować w&nbsp;nich różne rzeczy.

{% include info.html
type="Ciekawostka"
text="[Ikonka *theden.sh*](https://thoughts.theden.sh/favicon.ico) to gratka dla użytkowników Firefoksa -- jest animowana!  
Firefox to jedna z&nbsp;bardzo nielicznych przeglądarek wspierających animowane ikony w&nbsp;zakładkach. Większość użytkowników zobaczy tylko statyczny, nieruchomy obrazek. A&nbsp;fanom Lisa będzie mrugało, jak kursor w&nbsp;konsoli."
trailer="<p class='bigspace-before'><img src='/assets/posts/internet/dns/rekordy-dns/favicon-animacja.jpg' alt='Dwa zrzuty ekranu pokazujące tę samą ikonkę. Na jednym z&nbsp;nich w&nbsp;jej dolnej części wyświetla się zielony pasek'/></p>"
%}

### Początek

Wstęp omówię bardzo pobieżnie, bo to głównie luźne przemyślenia i&nbsp;eksperymenty autora. Nie mają wpływu na samo mięso wpisu, czyli chowanie informacji w&nbsp;DNS-ie.

Na początku autor zastanawia się, *jak dużo danych* może tam umieścić. Najpierw cytuje oficjalny standard i&nbsp;na jego podstawie ustala, że może sobie pozwolić na 255&nbsp;bajtów w&nbsp;pojedynczym rekordzie `TXT`.

```
1. TXT "Krótki ciąg znaków 1"
2. TXT "Krótki ciąg znaków 2"
...
```

W komentarzach z&nbsp;HN znalazłem informację, że w&nbsp;rzeczywistości [maksimum jest znacznie większe](https://news.ycombinator.com/item?id=38420508). Bo liczba 255&nbsp;nie odnosi się do całego rekordu `TXT`, tylko do *ciągu znaków*, a&nbsp;rekord może zawierać ich więcej.  
Nie weryfikowałem, kto ma rację, ale przedstawiam tu obie wersje.

Potem autor trochę eksperymentuje ze skryptami w&nbsp;języku Python, żeby zobaczyć, ile mógłby zyskać dzięki kompresji.  
Używa do niej modułu `zlib`. Rozmiar danych znacznie maleje, ale bardzo możliwe, że DNS by ich nie przyjął. Przez kompresję przestał to być „grzeczny” format tekstowy. Mogłyby wystąpić błędy podczas przetwarzania.

Dlatego autor w&nbsp;drugiej kolejności używa modułu `base64`, który (kosztem pewnego zwiększenia rozmiaru) potrafi każdy ciąg zer i&nbsp;jedynek przedstawić jako ciąg znaków „grzecznych”, które już nie powinny nigdzie sprawiać problemu.

Wniosek autora? W&nbsp;pojedynczym rekordzie dałoby się całkiem sporo zmieścić.  
Ale to taka obserwacja poboczna. Sednem wpisu było zaszyfrowanie jakiegoś tekstu, umieszczenie go na DNS-ie, a potem odczytanie. Prawie wszystko z użyciem zwięzłych poleceń konsolowych.

### Etap szyfrowania

Najpierw autor zapewne uruchomił swoją zaufaną konsolę, w&nbsp;którą można wpisywać polecenia tekstowe. Zapewne na Linuksie -- więc przykro mi, ale użytkownicy Windowsa mogą nie być w stanie powtórzyć u siebie komend. Chyba że [zainstalują dodatkowe rzeczy](https://www.youtube.com/watch?v=1ap3hL-UR9I).

Następnie zaszyfrował dane, używając do tego takiej komendy:

```
echo -n 'mySuperSecretPassword1!!1!!' | openssl enc -e -aes-256-cbc -a -salt -pbkdf2
```
Dla osób, które nie mają styczności z&nbsp;konsolą, może to brzmieć jak czarna magia. Dlatego na spokojnie to objaśnię.

1. Pionowe kreski `|`, czyli „rury” (ang. *pipes*), **służą do łączenia programów w&nbsp;efektowne _combosy_**.  
Jeśli między programami stoi rura, to wynik programu po lewej stronie trafi do tego po prawej. Wynik ostatniego programu w&nbsp;tym łańcuszku trafi do *wyjścia standardowego*. Czyli w&nbsp;praktyce: wyświetli się w&nbsp;konsoli.

2. Każdy z&nbsp;programów składa się ze swojej nazwy (najbardziej po lewej) oraz *argumentów* rozdzielanych spacjami. **Argumenty to dodatkowe informacje mówiące programowi, jak ma działać**. Odpowiednik klikania pstryczków w&nbsp;ustawieniach jakiejś apki.

Te dwie podstawy tu wystarczą. Są dwa programy połączone rurą, reszta to argumenty określające ich działanie. A&nbsp;że obrazek wyraża więcej niż tysiąc słów, to służę schematem:

{:.figure-bigspace}
<img src="/assets/posts/internet/dns/rekordy-dns/dns-szyfrowanie-schemat.jpg" alt="Schemat pokazujący szyfrowanie tekstu jako dwie maszynki do mięsa. Pierwsza jest podpisana echo, a&nbsp;druga openssl. Strzałki pokazują kierunek przepływu danych, a&nbsp;obok nich są dopisane argumenty. Na samym dole widać zaszyfrowany tekst wewnątrz miniaturki konsoli" />

{:.figcaption}
W roli programów: maszynki do mięsa. 

Argumenty dla każdego programu są inne, bo każdy ma własną konwencję. Aby poznać możliwe argumenty, można wpisać w&nbsp;konsolę nazwę programu, a po niej `-h` albo `--help`. Często (nie zawsze) coś podpowie.  
W tym konkretnym przykładzie mamy:

* `echo` z&nbsp;dwoma argumentami: `-n` i&nbsp;tekstem do zaszyfrowania. 

  Konsola nie jest miejscem, w&nbsp;którym można wpisywać wszystko, co się tylko chce. Muszą to być nazwy programów, argumenty do nich albo inne, specjalne operatory (jak rury).  
  Jeśli zatem chce się wprowadzić do konsoli tekst, to trzeba to zrobić przez jakiś program. I&nbsp;tylko od tego jest tutaj `echo`.  
  Z&nbsp;kolei argument `-n` mówi „echu”, żeby nie dodawało na końcu oznaczenia końca linii, jak to domyślnie robi.

* `openssl` otrzymuje tekst do zaszyfrowania. Poza tym ma aż sześć dodatkowych parametrów.

  Pierwszy argument to `enc`, mówiący żeby użyć konkretnego podprogramiku (bo *openssl* to cały pakiet). Z kolei `-e` mówi, żeby działać w&nbsp;trybie szyfrowania.  
  `-a` mówi, żeby zastosować kodowanie Base64 (wspomniane wyżej; sprowadza tekst do postaci 64&nbsp;najprostszych, „bezpiecznych” znaków).  
  Pozostałe parametry -- `-aes-256-cbc`, `-pbkdf2` i `-salt` -- precyzują metody szyfrowania. Niestety mało wiem o&nbsp;kryptografii i&nbsp;trudno mi ocenić, czemu autor wybrał akurat ten zestaw. Na HN ktoś napisał, że [to niezbyt bezpieczna kombinacja](https://news.ycombinator.com/item?id=38421885).
  
Posumowując: poprzez `echo` autor wprowadza do konsoli swój tekst. Następnie rura podaje go do `openssl`-a, żeby go zaszyfrować. Wyświetla się pytanie o&nbsp;hasło, autor wpisuje *hackerman*. Potem jeszcze raz. Pod spodem wyświetla się jego tekst, już w&nbsp;zaszyfrowanej postaci.

### Umieszczanie danych w&nbsp;DNS-ie

Po zaszyfrowaniu danych autor pisze:

> I&nbsp;stored the encrypted secret on the TXT record under pass.theden.sh

Ma na myśli, że skopiował zaszyfrowany tekst z&nbsp;poprzedniego punktu. Potem zapewne zalogował się na swoje konto u&nbsp;rejestratora domen (firmy, od której nabył *theden.sh*). Kliknął opcję dodania nowego rekordu typu `TXT`, wkleił do niego swój szyfr. I&nbsp;to wszystko.

{:.post-meta .bigspace-after}
Być może zrobił to przez program, ale nie sądzę -- sam pod koniec wpisu twierdzi, że świat byłby lepszy, gdyby rejestratorzy udostępniali API (dawali możliwość edycji przez programy, a&nbsp;nie tylko ręcznie).

{% include info.html
type="Ciekawostka"
text="Wnikliwi zauważą, że strona bloga to *thoughts.theden.sh*, zaś tekst umieścił na *pass.theden.sh*. Dlaczego?  
To dlatego, że autor jest właścicielem domeny głównej, *theden.sh*. Z&nbsp;tego tytułu może również wydzielać jej [subdomeny](https://pl.wikipedia.org/wiki/Subdomena). A&nbsp;każda z&nbsp;nich może mieć własne rekordy DNS, inne niż ta główna.  
Co więcej, odkrycie wszystkich subdomen cudzej domeny nie jest wcale taką prostą sprawą. Osoby analizujące powiązania korzystają w&nbsp;tym celu [z&nbsp;różnych trików](https://security.stackexchange.com/questions/35078/how-can-i-find-subdomains-of-a-site)."
%}

Od teraz każdy Smith, Kowalski czy inny obywatel świata może zwrócić się do swojego DNS-a z&nbsp;prośbą o rekordy tekstowe dla (sub-)domeny *pass.theden.sh*. O&nbsp;ile jego DNS nie ma strony The Den na cenzurowanym, to je odeśle.  
A wśród nich ten nowy, świeżo dodany, z&nbsp;zaszyfrowanym tekstem.

### Odszyfrowywanie danych

Po umieszczeniu tekstu wewnątrz DNS-a autor demonstruje, w jaki sposób mógłby do niego sięgnąć z dowolnego miejsca, używając jednolinijkowej komendy. Jeszcze bardziej zakręconej niż poprzednia:

```
dig pass.theden.sh TXT +short | sed 's/^"\(.*\)"$/\1/' | openssl aes-256-cbc -a -d -salt -pbkdf2
```

Ta  sprawia niestety, że polecenie może być trudniejsze do zrozumienia. Zatem ponownie rozbiję je na części! Są tu trzy programy, jeden po drugim, połączone „rurami” -- `dig`, `sed` i `openssl`. Cała reszta to rzeczy, jakie autor do nich wrzuca.

{:.bigspace}
<img src="/assets/posts/internet/dns/rekordy-dns/dns-deszyfrowanie-schemat.jpg" alt="Schemat pokazujący pobieranie rekordu tekstowego z&nbsp;DNS-a i&nbsp;odszyfrowanie go jednym konsolowym poleceniem. Widać na nim trzy programy, stylizowane na rysunkowe maszynki do mięsa, oraz strzałki pokazujące przepływ informacji."/>

A jeśli chodzi o same programy, mamy tutaj:

* omawiany już `dig`

  Pobiera rekordy odpowiadające subdomenie *pass.theden.sh*, należącej do *theden.sh*.  
  Argumenty to `TXT` (żeby pobrać tylko rekordy tekstowe) oraz `+short`, żeby wyświetlić same wartości.  
  Autor ma u&nbsp;siebie tylko jeden rekord, więc program zwróci jeden tekst, otoczony podwójnymi cudzysłowami.

* `sed`

  Komenda brzmi groźnie, zwłaszcza jeśli ktoś nie miał styczności z&nbsp;wyrażeniami regularnymi.  
  Ale sens jest prosty: „weź cały tekst, wraz z&nbsp;cudzysłowami po brzegach, i&nbsp;zastąp go samym wnętrzem bez cudzysłowów”. To potrzebne, żeby kolejny program z&nbsp;łańcuszka mógł ten tekst przyjąć.

  <details class="bigspace-after">
  <summary><strong>Dokładniejsze omówienie komendy sed (dla zainteresowanych)</strong></summary>
  <p class="bigspace-before">Pierwsza litera, <code class="language-plaintext highlighter-rouge">s</code>, wskazuje tryb (<em>substition</em>, czyli znajdź+zamień). Ma <a href="https://www.gnu.org/software/sed/manual/html_node/The-_0022s_0022-Command.html">składnię</a> <code class="language-plaintext highlighter-rouge">s/ZNAJDŹ/ZAMIEŃ_NA/</code> (plus ew. parametry dodatkowe, których w&nbsp;tym przypadku nie ma).</p>

  <p>W polu <em>Znajdź</em> jest ciąg <code class="language-plaintext highlighter-rouge">^"\(.*\)"$</code>.<br/>Znak <code class="language-plaintext highlighter-rouge">^</code> oznacza początek tekstu, zaś <code class="language-plaintext highlighter-rouge">$</code> jego koniec. Czyli <code class="language-plaintext highlighter-rouge">^"</code> oraz <code class="language-plaintext highlighter-rouge">"$</code> odpowiadają za złapanie cudzysłowów na brzegach.<br />
<code class="language-plaintext highlighter-rouge">.*</code> oznacza „weź wszystko od tego miejsca do kolejnej pasującej rzeczy” (czyli tutaj: do cudzysłowu zamykającego).</p>

  <p>Nawiasy sprawiają z&nbsp;kolei, że to wszystko, co się między nimi złapie, zostanie przypisane do grupy numerowanej. W&nbsp;polu <em>Zamień na…</em> można się do tej grupy odnieść, właśnie poprzez <code class="language-plaintext highlighter-rouge">\1</code> (gdyby grup było więcej, to dałoby się wyjść poza jedynkę).</p>
  </details>

* `openssl`

  Komenda bardzo podobna jak przy szyfrowaniu, bo ma być jego *odwrotnością*.  
  Jest tu jednak parę różnic. Zamiast podprogramiku `enc` zostaje użyty `aes-256-cbc` (nazwa odnosi się do użytego szyfru; wcześniej była identyczna, ale jako parametr).  
  Parametr `-d`, od *decrypt*, włącza tryb odszyfrowywania.

Na ostatnim etapie wyświetli się prośba o&nbsp;wpisanie hasła. Po wpisaniu *hackerman*, ustawionego wcześniej przez autora, ukaże się pierwotny, odszyfrowany tekst.

Wniosek: można użyć DNS-a jako swojej małej skrytki, a&nbsp;nawet zintegrować go z&nbsp;różnymi konsolowymi skryptami. Jedynie etap umieszczania tam danych może wymagać ręcznego działania.

## Podsumowanie

Bardzo lubię takie eksperymenty myślowe jak wpis z&nbsp;The Den. Od razu nabieram wtedy inspiracji do wymyślania własnych rzeczy!

I tak na przykład -- wyobrażam sobie coś, co mogłoby nosić nazwę DNSitter. Jak Twitter (świętej pamięci, bo to już X), tylko że wewnątrz DNS-a. Co pewien czas można dodawać nowy, krótki rekord `TXT` z&nbsp;jakimś swoim przemyśleniem.  
Nawet gdyby niczego nie kompresować i&nbsp;trzymać się limitu 255&nbsp;bajtów na rekord, to i&nbsp;tak będzie hojniejszy niż [dawne 140&nbsp;znaki Twittera](https://www.fastcompany.com/3060165/a-brief-history-of-twitters-140-character-limit)!

{% include info.html
type="Uwaga"
text="Warto przy tym pamiętać, że podobno DNS może [mieszać kolejność wysyłanych rekordów](https://superuser.com/questions/657789/format-of-txt-data-in-dns-record). Dlatego, żeby ułożyć jakąś spójną opowieść z&nbsp;rekordów `TXT`, należałoby je jakoś numerować." 
%}

DNS-a można również użyć **w roli tablicy ogłoszeń -- choćby na czarną godzinę**.  
Co by było, gdybym stracił swój hosting od Githuba/Microsoftu? Na przykład za regularne nabijanie się z perły korpoświata, Doliny Krzemowej?

Nadal pozostałaby mi domena. W&nbsp;końcu kupiłem ją całkiem niezależnie, od dostawcy europejskiego. A&nbsp;wraz z&nbsp;nią -- swoją małą skrytkę na rekordy.  
Do czasu znalezienia nowego nosiciela mógłbym opisać całą historię w&nbsp;rekordach TXT. A&nbsp;zaciekawione osoby mogłyby wtedy użyć komendy `dig`, żeby zobaczyć, w&nbsp;czym rzecz.

Póki co jest stabilnie, więc i&nbsp;status pozytywny:

{:.figure .bigspace}
<img src="/assets/posts/internet/dns/rekordy-dns/ciemnastrona-dns-odpowiedz.jpg" alt="Zrzut ekranu z&nbsp;konsoli, pokazujący wpisane w&nbsp;nią polecenie 'dig txt ciemnastrona.com.pl +short'. Pod spodem widać treść dwóch rekordów tekstowych, z&nbsp;których jeden to nazwa strony, a&nbsp;drugi mówi 'U mnie wszystko OK! Udanego dnia i&nbsp;smacznej kawusi'."/>

Tak jak pan DNS powiedział -- smacznej kawusi i&nbsp;do zobaczenia! :smile:

{% include info.html
type="Źródła obrazków"
text="Ikony z serwisu Flaticon użyte na schematach:"
trailer="
<ul id='obrazki'>
  <li>Ikony <a href='https://www.flaticon.com/free-icon/down-arrow_2268142'>czerwonej</a> i <a href='https://www.flaticon.com/free-icon/arrow-right_2267911'>zielonej</a> strzałki autorstwa Creative Stall Premium;</li>
  <li>
<a href='https://www.flaticon.com/free-icon/meat-grinder_836411'>Maszynka do mięsa</a> autorstwa Freepik;</li>
</ul>

"
%}

