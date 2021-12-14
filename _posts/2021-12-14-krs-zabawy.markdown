---
layout: post
title:  "Krajowy Rejestr Sądowy – raj dla szperaczy"
description: "Odkrywamy sekrety firm dzięki wizualizacjom."
subtitle: "Odkrywamy sekrety firm dzięki wizualizacjom."
date:   2021-12-14 13:12:07 +0100
tags: [Analiza danych]
firmy: [Branża modowa, CD Projekt, Uczelnie, Polskie media]
category: krs-msig
category_readable: "Myszkowanie w Monitorze i kopanie w KRS-ie"
image: "krs-zabawy/they-live-baner.jpg"
image-width: 1200
image-height: 700
---

Witajcie w (zapewne) ostatnim wpisie przed Świętami!  
Przedstawię Wam jedną z&nbsp;głównych przyczyn (zaraz po pracce zarobkowej) mojej długiej listopadowej przerwy od blogowania :smile:

Jakiś czas temu, tworząc [wpis na temat komunikatora UseCrypt]({% post_url 2021-07-16-powrot-usecrypta %}){:.internal}, miałem okazję poznać wyszukiwarkę KRS-u (Krajowego Rejestru Sądowego). Urzekła mnie możliwościami, ale nieco zniechęciła formą, w&nbsp;jakiej przedstawiała dane historyczne (tzw. odpisy).

Jakoś udało się wtedy stworzyć wykresy dla kilku spółek, ale metoda była bardzo krucha i&nbsp;nie dałbym rady jej uogólnić na szerszy firmowy ekosystem.  
Zostawiłem to sobie jako zadanie „na kiedyś” -- i&nbsp;to „kiedyś” nadeszło. Powalczyłem z&nbsp;plikami PDF z&nbsp;KRS-u, żeby w&nbsp;czytelniejszy sposób przedstawiać zawarte w&nbsp;nich informacje.

Żeby sprawdzić swoje skrypty, testowałem je na różnych znanych sobie firmach. Napotkałem zarówno drobne ciekawostki, jak i&nbsp;rzeczy, które potężnie mnie zaskoczyły. Jak to, że **KRS przechowuje na widoku numery PESEL przedsiębiorców**.  
Co więcej, **w&nbsp;niektórych dokumentach finansowych skrywały się dane ich autorów**. Nazwiska, które zapewne nie miały ujrzeć światła dziennego.

Zaciekawieni? Idealnie! W&nbsp;takim razie zapraszam na wspólne zwiedzanie zakamarków KRS-u i&nbsp;oglądanie bida-wykresów.

<img src="/assets/posts/krs-zabawy/they-live-fullsize.jpg" alt="Przeróbka mema złożona z&nbsp;czterech paneli. Pierwszy z&nbsp;nich pokazuje mężczyznę o&nbsp;blond włosach, który właśnie szykuje się do założenia okularów przeciwsłonecznych. Drugi pokazuje billboard widziany oczami tego mężczyzny. Widać na nim loga czterech firm lub marek: ptaka CD Projektu, kaczkę Donald.pl, napis Moliera 2 oraz herb podpisany All in UJ. Kolejny panel pokazuje mężczyznę już z&nbsp;założonymi okularami. Na ostatnim panelu widać ten sam billboard, ale tym razem zamiast symboli widać na nim miniatury wykresów."/>

{:.figcaption}
Moja przeróbka mema opartego na filmie *„They Live”*.  
W gościnnej roli marki/organizacje: Donald.pl, Moliera 2, CD Projekt, All in UJ.

# Spis treści

* [Ogólnie o&nbsp;źródłach](#ogólnie-oźródłach)
  * [Wyszukiwarka KRS-u](#wyszukiwarka-krs-u)
  * [Wyszukiwarka dokumentów finansowych](#wyszukiwarka-dokumentów-finansowych)
* [Część praktyczna](#część-praktyczna)
  * [CD Projekt Spółka Akcyjna](#cd-projekt-spółka-akcyjna)
  * [Donald.pl](#donaldpl)
  * [Moliera 2](#moliera-2)
  * [All in UJ](#all-in-uj)
* [Bonus: skrypty pomocnicze](#bonus-skrypty-pomocnicze)
  * [Skrypt do wyciągania PDF-ów](#skrypt-do-wyciągania-pdf-ów)
  * [Skrypt do tworzenia wykresów](#skrypt-do-tworzenia-wykresów)
* [Dalsze kroki](#dalsze-kroki)

## Ogólnie o&nbsp;źródłach

Przez stronę Ministerstwa Sprawiedliwości możemy zajrzeć do **trzech fajnych baz**:
* wyszukiwarki KRS-u,
* wyszukiwarki dokumentów finansowych,
* numerów pisma „Monitor Sądowy i&nbsp;Gospodarczy”.

W tym wpisie korzystam z&nbsp;pierwszych dwóch źródeł, a&nbsp;do ostatniego wracam pod koniec.

# Wyszukiwarka KRS-u
 
KRS jest jak kronika, do której wpisuje się wydarzenia z&nbsp;życia organizacji. Tych nieco „cięższych”, bo od lekkich graczy z&nbsp;małą księgowością mamy inną bazę, CEIDG.

W KRS-ie znajdziemy wszelkie możliwe organizacje. Od małych rodzinnych spółek z&nbsp;o.o., przez stowarzyszenia studenckie i&nbsp;kancelarie prawnicze, aż po wielkie koncerny notowane na giełdzie.

Pobierając informacje z&nbsp;Rejestru, widzimy wszystkie zmiany z&nbsp;życia spółek. Zmiany nazw, adresów, zarządu, współwłaścicieli... I&nbsp;wszystko to za darmo.

{%include info.html type="Ciekawostka"
text="Choć potocznie na organizację możemy mówić „firma” (np. „firma się rozwija...”), to oficjalnie ten termin odnosi się **do nazwy tej organizacji**. Odpowiednika nicku na portalu społecznościowym, który można zmieniać.  
Dlatego taki potworek jak „firma spółki” to nie pleonazm jak „masło maślane”, tylko jak najbardziej poprawny zwrot!  
Terminem bardziej ścisłym na określenie organizacji byłoby „spółka”, „stowarzyszenie” itd. Pozwolę sobie jednak nazywać wszystko firmami, gdy tak mi będzie wygodniej. Niech puryści mi wybaczą. 
"%}

[Oficjalną wyszukiwarkę](https://ekrs.ms.gov.pl/web/wyszukiwarka-krs/strona-glowna/index.html) znajdziemy na stronie Ministerstwa Sprawiedliwości. Możemy w&nbsp;nią wpisywać nazwy spółek, ich numery identyfikacyjne albo inne dane.

{:.bigspace}
<img src="/assets/posts/krs-zabawy/krs-interfejs.jpg" alt="Zrzut ekranu pokazujący interfejs wyszukiwarki KRS-u. Widać tu kilka pól, w&nbsp;które można wpisywać np. nazwę firmy, jej numer KRS, numer NIP itd." width="700px"/>

Jeśli wyszukiwarka znajdzie coś dla nas, to wyskoczy nam lista spółek. Wybieramy jedną, klikamy `Pokaż szczegóły` i&nbsp;zjeżdżamy na dół. Tam możemy pobrać odpis informacji aktualnych albo informacje pełne, czyli wszystkie zdarzenia od czasu założenia tej spółki.  
Interesuje nas to drugie, więc trzeba kliknąć `Pobierz wydruk informacji pełnych`.

{%include info.html type="Porada"
text="Strona KRS-u jest nieco dziwna. Odkryłem, że gdybyśmy po wyświetleniu informacji o&nbsp;jednej spółce wrócili do poprzedniej strony przez opcje przeglądarki (np. klikając ikonę strzałki w&nbsp;lewo w&nbsp;górnym rogu), to potem nie dałoby się przejść do informacji o&nbsp;innej spółce. Wyświetliłoby błąd, że nasza aktywność jest nietypowa.  
Ale jeśli klikniemy przycisk `Powrót do listy` na stronie KRS-u, to już wszystko będzie działało jak należy :roll_eyes:. Polecam ten sposób, jeśli chcemy pobrać więcej PDF-ów pod rząd."
%}

Każdy z&nbsp;pobranych PDF-ów zawiera wszystkie zarejestrowane wydarzenia z&nbsp;życia organizacji (a jeśli dokądś nie sięga, to musiałyby to być naprawdę historyczne dane).

Ale na pewno nie jest tak pięknie, nieprawdaż? Oczywiście że nie! Przeszkodą jest format, w&nbsp;jakim dostajemy odpisy. 

Jest to zestaw szaro-czarnych tabelek. Ale to akurat nie problem, jeśli nie jesteśmy wielkimi estetami. Gorzej, że w tych tabelkach nie ma dat, tylko liczby.  
**Wszystkie daty mamy jedynie na początku pliku**, w&nbsp;czymś w&nbsp;rodzaju indeksu. Mówiącego na przykład, że 1 odpowiada dacie *4.10.2017 r.*, 2 to *11.12.2017 r.* i&nbsp;tak dalej.

{:.bigspace}
<img src="/assets/posts/krs-zabawy/krs-odpis-indeks.jpg" alt="Zrzut ekranu dwóch rubryk z&nbsp;PDF-a z&nbsp;Rejestru Sądowego. Fragment u&nbsp;góry pokazuje liczbę 1 oraz odpowiadająca jej datę. Dolny fragment pokazuje rubrykę ze zmianą w&nbsp;kapitale spółki. Liczba 1 jest wpisana pod nagłówkiem 'wprow.'. Obie liczby, z&nbsp;górnej i&nbsp;dolnej rubryki, są połączone czerwoną linią."/>

Gdybyśmy chcieli przeglądać dokument w&nbsp;sposób tradycyjny, to musielibyśmy skakać wzrokiem od indeksu do zdarzeń i&nbsp;to sobie łączyć w&nbsp;głowie.

Nie mam pojęcia, kto się zdecydował na taki format, ale niestety raczej nie pomaga w&nbsp;analizowaniu, co się działo w&nbsp;świecie firm.

# Wyszukiwarka dokumentów finansowych

Drugim cennym źródłem jest [wyszukiwarka dokumentów finansowych](https://ekrs.ms.gov.pl/rdf/pd/search_df), również obecna na stronie Ministerstwa Sprawiedliwości.

Żeby z&nbsp;niej korzystać, trzeba podać numer KRS spółki, znaleziony na przykład w&nbsp;poprzednim punkcie.

Wyszukiwarka pokazuje nam różne dokumenty, jakie złożyła interesująca nas organizacja. Najczęściej to sprawozdania finansowe. Każdy z&nbsp;tych plików można kliknąć, wybrać `Szczegóły` i&nbsp;pobrać sobie na dysk.

Część jest w&nbsp;formacie PDF, więc można je sobie po prostu otworzyć. Niektóre to pliki XML, ale je również można podejrzeć. Istnieją nawet strony internetowe, które za darmo nam wyświetlają takie sprawozdanie w&nbsp;czytelnej postaci.

Robi się gorzej, jeśli dokument to hybryda: XML z&nbsp;plikiem PDF zaszytym w&nbsp;środku. Jeśli zajrzymy do wnętrza takiego pliku, to -- o&nbsp;ile Notatnik czy inny program nam się nie zawiesi od długiego tekstu -- zobaczymy po prostu wielki blok złożony z&nbsp;liter, cyferek i&nbsp;innych znaków. Wygląda on tak:

{:.bigspace}
<img src="/assets/posts/krs-zabawy/sprawozdanie-zalacznik-pdf.jpg" alt="Zrzut ekranu pokazujący wnętrze pliku XML zawierającego zakodowany załącznik. Widać, że od pewnego miejsca, po tagu Dane Załącznika, zaczyna się bardzo długi ciąg liter i&nbsp;znaków. Zrzut pokazuje tylko jego fragment, a&nbsp;poniżej znajduje się napis 'Dużo takiego tekstu jak wyżej'."/>

Interesujący nas PDF znajduje się między tagami `str:DaneZalacznika`. Dałoby się go wyciągnąć „ręcznie”: kopiując ten wielki blok tekstu, wklejając go na jakąś stronę konwertującą kodowanie *base64* (bo takie jest stosowane), zapisując na dysku z&nbsp;rozszerzeniem *.pdf*. Ale byłaby to żmudna i&nbsp;niewdzięczna robota.

## Część praktyczna 

Podsumowując powyższe przemyślenia: miałem dwa fajne źródła i&nbsp;dość nieprzyjemne formaty, które odbierały mi *smak życia*{:.corr-del}chęć do czytania w&nbsp;sposób klasyczny.

Rozwiązanie? Napełniłem żołądek makaronem w&nbsp;stylu bolognese, zalałem kawą tak czarną, że prawie koloru *vantablack*, puściłem w&nbsp;słuchawkach srogie transiwo (oczywiście z&nbsp;własnego dysku, nie żadnej platformy streamingowej).  
I wziąłem się do tworzenia skryptów w&nbsp;Pythonie.

Dopracowywałem je w&nbsp;czasie wolnym, wieczorami. Zajęcie było dość satysfakcjonujące -- małymi krokami do przodu.  
Efektem działań były dwa skrypty pomocnicze. Jeden od tworzenia wykresów na podstawie odpisów z&nbsp;KRS-u, drugi od wyciągania PDF-ów zaszytych w&nbsp;sprawozdaniach finansowych.  
Oba znajdziecie pod koniec wpisu.

Po zrobieniu sobie narzędzi wziąłem pod lupę kilka spółek. Zobaczmy, co powie nam o&nbsp;nich KRS!

Ale zanim wyruszymy, postawię jeszcze dupochronik.

Świat finansów znam dość słabo i&nbsp;nie wiem, jak interpretować niektóre znaleziska. Pokazując w&nbsp;tym wpisie przykłady firm, **nie próbuję sugerować, że robią cokolwiek szemranego**. To zapewne rzeczy prozaiczne, które po prostu przyciągnęły mój laicki wzrok.  
Pokazuję tu same fakty. A&nbsp;wszelkie interpretacje, drogie Czytelniczki i&nbsp;Czytelnicy, zostawiam wyłącznie Wam :wink: 

# CD Projekt Spółka Akcyjna

Zacznijmy od nich, bo są spółką dość sporą i&nbsp;na czasie, a&nbsp;przy tym odrobinę kontrowersyjną (mam na myśli przecieki ukazujące warunki, jakie u nich panowały, a&nbsp;także wszystkie potknięcia związane z&nbsp;„Cyberpunkiem”, wycofywaniem go ze sklepów itp.).

Jeśli chodzi o&nbsp;ich produkty, kojarzyli mi się oczywiście z&nbsp;trzema częściami „Wiedźmina”, a&nbsp;także wspomnianym „Cyberpunkiem 2077”.

Wiedziałem, że choć sławę zdobyli w&nbsp;ostatniej dekadzie, nie są jakąś młodą firmą. Pamiętam mgliście wzmianki o&nbsp;nich jeszcze z&nbsp;pisma „CD Action”, sprzed czasów pierwszego „Wiedźmina”. Ale po odpaleniu skryptu i&nbsp;stworzeniu wykresów odkryłem, że **firma znana nam jako CD Projekt to przekształcenie dużo starszej spółki -- Optimusa** (powstałego w&nbsp;roku 1988)!

{:.bigspace}
<img src="/assets/posts/krs-zabawy/cd-projekt-nazwy.jpg" alt="Wykres w&nbsp;formie poziomej osi czasu z&nbsp;różnymi nazwami spółki CD Projekt w&nbsp;różnych okresach czasu. Daty znajdują się na dolnej osi wykresu i&nbsp;obejmują przedział od 2001 do teraz. W&nbsp;2011 roku spółka zmieniła nazwę z&nbsp;Optimus S.A. na CD Projekt Red S.A."/>

KRS-owe wpisy dla Optimusa sięgają do roku 2001 (zapewne dlatego, że to wtedy -- według Wikipedii -- większa spółka [podzieliła się na Optimusa i&nbsp;Onet](https://pl.wikipedia.org/wiki/CD_Projekt#Optimus_(1988%E2%80%932011))).  

Patrząc na wykres: do 2002 r. mieliśmy *Optimus Technologie*, potem samo *Optimus*. Potem w&nbsp;2011 roku zmiana na *CD Projekt Red SA*. Rok i&nbsp;prawie pięć miesięcy później na samo *CD Projekt SA*.

Firmy Optimus możecie nie kojarzyć, bo jest stara. Ale jej losy były burzliwe; miała po drodze perypetie ze skarbówką i&nbsp;aresztowanie właściciela w&nbsp;środku nocy.  
W „Pulsie Biznesu” znajdziemy artykuł -- nieco momentami jednostronny, ale zawierający [krótką historię tej firmy](https://www.pb.pl/optimus-mial-szanse-byc-globalnym-mocarzem-642513).

> Optimus zaczął staczać się po równi pochyłej. Notował coraz gorsze wyniki, stracił renomę, klientów, wiarygodność na rynku i&nbsp;w oczach banków. (...) Na przełomie 2008 i&nbsp;2009 r. ledwie dyszący Optimus zawiesił działalność. Pomocną dłoń wyciągnęła spółka CD Projekt Red

{:.figcaption}
Źródło: *Puls Biznesu*. Skróty moje.

Burzliwe życie Optimusa zapisało się nawet w&nbsp;jego KRS-owej historii! Spójrzcie na te schodki śmierci; pokazują, jak szybko zmieniały się stołki w&nbsp;zarządzie, zanim Optimus stał się CD Projektem:

<img src="/assets/posts/krs-zabawy/cd-projekt-wykres-edit.jpg" alt="Wykres pokazujący, jak zmieniała się nazwa obecnego CD Projektu oraz osoby wchodzące w&nbsp;skład jego zarządu."/>

{:.figcaption}
Zmiany zarządu w&nbsp;dawnym Optimusie i&nbsp;obecnym CD Projekcie. Nazwiska zakryłem, bo nie mają większego znaczenia dla wpisu.  
Poza tym wybaczcie nachodzące na siebie daty, ale wolałem już bardziej nie zwiększać obrazka.

{% include info.html
type="Porada"
text="Możecie kliknąć obrazek prawym przyciskiem myszy i&nbsp;wybrać `Pokaż obraz`, żeby zobaczyć go w&nbsp;lepszej rozdzielczości.  
Poza tym, na wszelki wypadek, małe objaśnienie:  
Dolna część wykresu, oś pozioma, zawiera daty. Data ostatnia, po prawej, to ta aktualna w&nbsp;dniu, gdy pobierałem odpis (tu: 9.12.2021 r.). Od tego czasu coś się mogło zmienić.  
Na osi pionowej macie imiona i&nbsp;(zakryte) nazwiska osób. Na wysokości każdej z&nbsp;tych nazw widać odpowiadający jej poziomy słupek; zaczyna się w&nbsp;momencie, kiedy dana osoba/spółka została wpisana do KRS-u. Kończy się na dacie, kiedy została z&nbsp;niego wykreślona."
%}
 
Wykres dla zarządu ma kształt stromych, krótkich schodków, co oznacza że osoby zmieniały się często i&nbsp;mało kto zagrzał miejsce na dłużej.  
Mówiąc konkretniej: w&nbsp;ciągu około 9 lat przez zarząd przewinęły się 24 osoby. Całkiem mocny argument za tym, że nie było u&nbsp;nich zbyt stabilnie.

A potem przyszły czasy wchłonięcia przez CD Projekt i&nbsp;uspokojenie sytuacji. Od tej pory mamy tylko kilka kresek, konsekwentnie ciągnących się aż do teraz. Kto raz trafił do zarządu za czasów CDP, ten już w&nbsp;nim został (za wyjątkiem jednej osoby).

Cały ten przykład pokazuje nam kilka rzeczy:

* nazwy firm widoczne na zewnątrz są czymś ulotnym; zawsze mogą nastąpić przejęcia, wydzielenie mniejszych firm itp.
* pokazanie zmian na wykresach pozwala dostrzec, na ile stabilna jest. sytuacja w&nbsp;firmie
* ...ale wykres nie mówi wszystkiego.  

  CD Projekt ma od początku (przejęcia Optimusa) bardzo stabilny skład zarządu. A&nbsp;jednak, w&nbsp;świetle niedawnych zdarzeń związanych z&nbsp;premierą „Cyberpunka”, wiemy że za kulisami mieli całkiem niezły bajzel. 

# Donald.pl

Portal z&nbsp;informacjami. Ich logo to gumowa kaczuszka. Na Facebooku na tę chwilę mają ponad 270 000 obserwujących.

Jestem w&nbsp;stosunku do nich raczej neutralny.  
Z jednej strony faktycznie wspominają o&nbsp;sprawach niszowych, cytują źródła, miewają też dobre memy.  
Z drugiej -- czasem nagłówki i&nbsp;treść artykułów usilnie próbują mi sugerować, co mam myśleć. A&nbsp;ja lubię jednak własne zdanie wyrabiać :wink:  
Poza tym moją pedantyczną duszę boli notoryczny brak polskich cudzysłowów w&nbsp;ich newsach (jest \"tak\" zamiast „tak”).

W każdym razie byłem ciekaw, jak wygląda za kulisami organizacja, która od dość niszowego fanpage'a urosła do czegoś popularniejszego, mającego obecnie konto na platformie Patronite i&nbsp;różne akcje sponsorowane. Dlatego zajrzałem kaczuszce w&nbsp;bebechy.

Na ich stronie, w&nbsp;zakładce „Regulamin”, znalazłem informację, że oficjalna nazwa spółki to *Donald Media*. Numer KRS *0000698031*. Wpisałem nazwę w&nbsp;wyszukiwarkę, pobrałem dane i&nbsp;stworzyłem z&nbsp;nich wykresy:

{:.bigspace}
<img src="/assets/posts/krs-zabawy/donald-wykres.jpg" alt="Wykres pokazujący zmiany w&nbsp;spółce Donald Media."/>

W ten sposób dowiedziałem się, że Donalda można uznać za firmę rodzinną! Pomógł fakt, że **w KRS-ie numery PESEL są na widoku, a&nbsp;ich pierwsze dwie cyfry to ostatnie cyfry roku urodzenia**.

Patrząc na wykres, zobaczymy że na początku miejsce w&nbsp;zarządzie, wraz z&nbsp;udziałami, miała Maria N. Patrząc po numerze PESEL, urodzona w&nbsp;roku 1959.  
Następnie, po upływie około 2 lat, wszystko przeszło w&nbsp;ręce Jacka N., o&nbsp;identycznym nazwisku. Urodzonego w&nbsp;1983 roku.

Początkowa pani prezes przekazała stery mężczyźnie o&nbsp;tym samym nazwisku, o&nbsp;24 lata młodszemu. Matka synowi? Ciotka siostrzeńcowi/bratankowi? Głębiej się nie wkopywałem, bo poza samym faktem mnie to aż tak nie ciekawiło.

Widzimy, że w&nbsp;2020 roku do udziałowców dołączyła również spółka V27. A&nbsp;potem odeszła, a&nbsp;w jej miejsce weszła inna (również mająca V27 w&nbsp;nazwie, ale komandytowa). W&nbsp;KRS-ie widać, że ma jednak tylko 10% udziałów, czyli *de facto* nie ma możliwości sterowania firmą.

Wykresy nie nasyciły mojej ciekawości, więc wpisałem numer KRS Donalda w&nbsp;**wyszukiwarkę dokumentów finansowych** (wspomnianą na początku) i&nbsp;zajrzałem w&nbsp;załączniki do sprawozdań. 

W przypadku Donalda mieliśmy trzy zwykłe PDF-y i&nbsp;jeden zakopany w&nbsp;XML-u. Kiedy już zebrałem je wszystkie i&nbsp;do nich zajrzałem, nieco się zdziwiłem.

Spodziewałem się kwot raczej niskich, ukazujących stopniowe i&nbsp;mozolne wyrabianie zysków. W&nbsp;praktyce kwoty od początku idą w&nbsp;setki tysięcy, a&nbsp;rosną jedynie straty. Zobaczcie sami.

Plik *Protokół nr 1 2019 Donald Media Sp  z&nbsp;o o.pdf* (z 2019 r.):

{:.bigspace}
> **strata netto** (...) za okres \[do końca 2018\] roku w&nbsp;wysokości **359 601,54 PLN** zostanie pokryta z&nbsp;zysków z&nbsp;lat następnych.

Plik *Protokol1-scalone.pdf* (z 2020 r.):

{:.bigspace}
> strata netto Spółki (...) w&nbsp;wysokości **433 947,53 PLN** zostanie pokryta z&nbsp;zysków z&nbsp;lat następnych.

Plik *nr3_uchwala.pdf* (z 2021 r.):

{:.bigspace}
> strata w&nbsp;wysokości **566 300,53 zł** (...) zostanie pokryta z&nbsp;zysków z&nbsp;lat przyszłych.

W tym ostatnim, najnowszym przypadku było 12 głosów przeciw przyjęciu sprawozdania. Zapewne głosował tak drugi, mniejszy udziałowiec, V27. Ale główny właściciel ma więcej głosów (108) i&nbsp;był za, więc wszystko przeszło.

Sam nie wiem, jak to interpretować. Wiem że strata w&nbsp;świecie finansów nie oznacza, że pieniądze wyparowały. Tym niemniej była i&nbsp;rośnie.  
Poza tym kwoty startowe były wyższe niż myślałem, więc nie znalazłem odpowiedzi na to, jak wygląda rozwijanie portalu na zasadzie grosz do grosza”. No cóż, pozostaje szukać dalej.

{%include info.html
type="Ciekawostka"
text="W przypadku PDF-ów okazało się również, że nie usunięto z&nbsp;nich metadanych i&nbsp;po użyciu programiku konsolowego `pdfinfo` (część Popplera, którego i&nbsp;tak używałem w&nbsp;głównym skrypcie) jak na dłoni widać imię osoby, która je stworzyła, a&nbsp;także program, w&nbsp;którym to zrobiła."
%}

# Moliera 2

Wybitnie nie przepadam za branżą modową i&nbsp;wolałbym, żeby ludzie stroili się w&nbsp;rozum *i godność człowieka*{:.corr-del} zamiast w&nbsp;coś, co im dyktują inni. Ewentualnie narzucali na ten rozum jakieś całkiem dowolne, praktyczne szmateksy, żeby zimno nie było :wink:.

Ale na chwilę obecną branża istnieje, więc mogę co najwyżej przeanalizować jakąś spółkę, która jest z&nbsp;nią powiązana.

Nazwa *Moliera 2* pokazywała mi się czasem na wielkich billboardach, mówiących rzeczy w&nbsp;stylu „Kup nasze szpilki”. Szpilek nie kupiłem, ale wpisałem nazwę w&nbsp;DuckDuckGo i&nbsp;znalazłem ich stronę główną.

W [zakładce „Kontakt”](https://www.moliera2.com/kontakt) na ich oficjalnej stronie znalazłem dane spółki.  
I ciekawostka! Oficjalna nazwa nie ma nic wspólnego z&nbsp;żadną Molierą i&nbsp;brzmi *IT FASHION POLSKA GROUP & PARTNERS Spółka z&nbsp;o.o.*.

{:.bigspace}
<img src="/assets/posts/krs-zabawy/moliera2-wykres.jpg" alt="Wykresy pokazujące zmiany w&nbsp;spółce IT Fashion Group."/>

Patrząc na adres, widzimy skąd nazwa *Moliera 2*. Od założenia spółki aż do teraz mieszczą się w&nbsp;lokalu numer 2 na ulicy Moliera w&nbsp;Warszawie. Zewnętrzne źródła uzupełniają, że był to, oprócz siedziby, również ich pierwszy salon.

Po zrobieniu wykresów widzimy też całkiem świeżą zmianę, z&nbsp;października 2021! Główna IT Fashion Group straciła wtedy udziały, a&nbsp;wzięły je dwie inne firmy: *IT Fashion Polska Properties Sp. z&nbsp;o.o.* (czyli zapewne jakaś przybudówka głównych właścicieli Moliery), a&nbsp;także nieznana wcześniej *Modern Commerce Spółka Akcyjna*.

Ci pierwsi mają 20 udziałów, ci drudzy 80.  
Co więcej, dokładnie takie plany możemy znaleźć **w artykułach sprzed kilku miesięcy**, z&nbsp;maja tego roku:

> Modern Commerce w&nbsp;pierwszym etapie transakcji przejmie 80 proc. udziałów w&nbsp;IT Fashion Polska Group & Partners

{:.figcaption}
Źródło: [artykuł o&nbsp;przejęciu](https://biznes.interia.pl/gospodarka/news-modern-commerce-przejmie-wlasciciela-moliera2-com-za-100-mln,nId,5244147) na *biznes.interia.pl*.

Przykład Moliery potwierdza to, co widzieliśmy przy CD Projekcie: za znajomą, niezmienną nazwą mogą się kryć przeróżne przejęcia, przekształcenia i&nbsp;tym podobne.

Widzimy też jedną ważną rzecz. Oficjalne zmiany w&nbsp;KRS-ie mogą mieć znaczne opóźnienie w&nbsp;stosunku do oficjalnych komunikatów! Osoby czytające prasę wiedziałyby o&nbsp;całej akcji z&nbsp;*Modern Commerce* pięć miesięcy wcześniej niż osoby czytujące jedynie KRS.

Nic dziwnego, że współczesne firmy inwestycyjne coraz częściej sięgają po programy do [analizy danych tekstowych](https://algotrading101.com/learn/sentiment-analysis-python-guide/) (np. w prasie), żeby mieć dokładniejsze informacje.

# All in UJ

Stowarzyszenie zajmujące się organizowaniem wydarzeń dla studentów Uniwersytetu Jagiellońskiego. Numer KRS *0000450107*. 

Pierwotnie szukałem w&nbsp;wyszukiwarce całego Ujotu, jako najstarszej uczelni w&nbsp;Polsce. Zamiast niego znalazłem Stowarzyszenie All In UJ.

Nazwa od czasu założenia bez zmian, adres zmieniał się raz. Udziałowców w&nbsp;przypadku stowarzyszenia nie ma.  
Zostaje nam spojrzenie na zarząd. A&nbsp;tam ciekawe schodki! Popatrzmy:

{:.bigspace}
<img src="/assets/posts/krs-zabawy/all-in-uj-wykres-edit.jpg" alt="Wykresy pokazujące zmiany zarządu stowarzyszenia All In UJ."/>

Widać, że znacznie się to różni od kształtu w&nbsp;przypadku naszych poprzednich, komercyjnych spółek. Mamy tutaj jak na dłoni **sezonowość / kadencyjność** -- w&nbsp;regularnych odstępach czasu zazwyczaj następuje wymiana całego zarządu.

Patrząc po wykresie, jedna kadencja zarządu trwała plus minus jeden rok. Najdłuższa trwała od czerwca 2014 do czerwca 2016.  
Z kolei w&nbsp;roku 2019 miało miejsce dość dziwne przetasowanie. Ludzie siedzieli na stanowiskach jedynie 5 miesięcy, a&nbsp;potem większość z&nbsp;nich się wymieniła (niektórzy wrócili, ale na inne stanowiska). Cóż to się podziało?

Poza tym uważni obserwatorzy zobaczą, że czasem zmiany na wykresie są pozorne -- jakaś osoba została wykreślona, ale wróciła tego samego dnia, tylko że odpowiada jej nowy słupek. Dotyczy to chociażby Tomasza P., który jest z&nbsp;All In UJ od samego początku. W&nbsp;najnowszym zarządzie też jest, ale ma nowy słupek (jako piąta osoba od dołu).

To częściowo natura KRS-u, a&nbsp;częściowo ograniczenie mojego skryptu. Zdarza się, że ktoś zmieni stanowisko, na przykład z&nbsp;Koordynatora Filaru Nauka na Koordynatora Filaru Impreza -- to ich autentyczne nazwy stanowisk.  
W takim przypadku ta osoba zyskuje nową, osobną pozycję w&nbsp;KRS-ie, już z&nbsp;inną nazwą stanowiska. Mój skrypt jeszcze nie umie „rozpleść” takich przypadków, więc daje takiej osobie nowy słupek.

Czy dałoby się zmienić stanowisko bez pełnego wykreślenia i&nbsp;ponownego wpisania? Niestety nie wiem, to pewnie zależy od interfejsu, z&nbsp;jakiego korzystają.

{% include info.html
type="Ciekawostka"
text="W rubryce 3, „Cel działania organizacji”, wypatrzyłem u&nbsp;nich błędną numerację. Mamy tam:  
_K) PROMOWANIE I&nbsp;ORGANIZACJA WOLONTARIATU_,  
_**O)**{:.red} PROPAGOWANIE I&nbsp;OCHRONA WOLNOŚCI I&nbsp;PRAW CZŁOWIEKA_,  
_M) PRZECIWDZIAŁANIE MOWIE NIENAWIŚCI_"
%}

Porównując All In UJ z&nbsp;Optimusem widzimy, że zmiany w&nbsp;obrębie organizacji mogą mieć różne „kształty”. Schodki sezonowe, sugerujące regularne wymiany składu. Schodki chaotyczne, sugerujące dużą rotację.  
Patrząc na wykresy, widzimy te zmiany wyraźnie i&nbsp;z czasem powinniśmy coraz lepiej łapać na oko, z&nbsp;czym możemy mieć do czynienia.

To tyle z&nbsp;przykładów na dziś.  
Gdybyście sami chcieli zajrzeć w&nbsp;bebechy różnych firm, to służę swoimi skryptami i&nbsp;instrukcją ich obsługi! A&nbsp;jeśli nie, to zajrzyjcie do przyszłych wpisów z&nbsp;tej serii po gotowe analizy.

## Bonus: skrypty pomocnicze


# Skrypt do wyciągania PDF-ów

Możecie go pobrać <a href="/assets/skrypty/pdf_extractor.py" download>stąd</a>{:.internal}.

Działanie skryptu zademonstrowałem w&nbsp;przypadku Donald.pl. Po prostu umieszczamy go w&nbsp;tym samym folderze co pliki XML, pobrane wcześniej przez wyszukiwarkę Ministerstwa Finansów.  
Kiedy odpalimy skrypt, powstanie nam folder `pdfs`, a&nbsp;w nim wyciągnięte pliki PDF.

Dobrą stroną skryptu jest to, że korzysta z&nbsp;najprostszych funkcji i&nbsp;**nie potrzebuje do działania niczego poza domyślnym Pythonem**.

Gdybyśmy, zamiast przenosić skrypt między folderami, woleli raz go odłożyć w&nbsp;jakieś osobne miejsce i&nbsp;tylko go „przywoływać” w&nbsp;różnych folderach, to zapraszam do mojego [samouczka]({{site.url}}/tutorials/python-extended){:.internal} na temat uprzyjemniania sobie pracy z&nbsp;Pythonem.

# Skrypt do tworzenia wykresów

To ten ważniejszy z&nbsp;dwóch skryptów. Pobierzcie go <a href="/assets/skrypty/krs_visualizer.py" download>stąd</a>{:.internal}.

Jeszcze nieraz go użyję w&nbsp;ramach tej serii, więc wydzieliłem instrukcje korzystania z&nbsp;niego do [osobnego samouczka]({{site.url}}/tutorials/krs-wykresy){:.internal}.

## Dalsze kroki

Tworząc swoje wykresy, dostrzegłem pewną rzecz, która nie dawała mi spokoju.

Mianowicie: odpis z&nbsp;KRS-u dla firmy A&nbsp;pokazuje, jakie osoby albo inne firmy mają w&nbsp;niej swoje udziały. **Nie pokazuje natomiast, w&nbsp;czym sama firma A&nbsp;ma udziały**. Jeśli jest udziałowcem firm B&nbsp;i C&nbsp;(czyt. ma nad nimi choć częściową kontrolę), to KRS tego nie pokaże.

Ale jakimś cudem zewnętrzne strony, takie jak *rejestr.io*, potrafią pokazywać powiązania w&nbsp;obie strony! Zobaczmy na przykładzie spółki Glob 360, właściciela serwisu NaTemat  
(któremu niedawno zarzucono [kontrowersyjne przejęcie](https://www.facebook.com/natematcompl/posts/4484169778299200) cudzej domeny internetowej. Przy współpracy z&nbsp;kancelarią, która swego czasu kazała Niebezpiecznikowi [usunąć z&nbsp;komentarzy](https://niebezpiecznik.pl/post/oswiadczenie-w-sprawie-wymierzonej-w-niebezpiecznika-i-inne-redakcje-kampanii-oszczerstw/#akt) imię pewnej osoby).

{:.figure}
<img src="/assets/posts/krs-zabawy/glob360-powiazania-edit.jpg" alt="Graf powiązań ze strony Rejestr.io. W&nbsp;jego centrum widać firmę Glob 360. Prowadzi do niej pięć strzałek, łączących z&nbsp;nią miniaturki podpisane imiona i&nbsp;nazwiskami osób (nazwiska zakryłem). Na grafie widać również dwie strzałki odchodzace od Glob 360 i&nbsp;łączące firmę z&nbsp;dwiema innymi, Asz Dziennik oraz Mamadu. Te dwie firmy wraz z&nbsp;Glob 360 są otoczone czerwoną obwódką."/>

{:.figcaption}
Czerwoną obwódką otoczyłem powiązania, które nie byłyby widoczne w&nbsp;odpisie dla spółki Glob360.  
Źródło: [rejestr.io](https://rejestr.io/krs/329219/glob360).

Zastanowiłem się: jak to robią, że mają powiązania w&nbsp;obie strony, kiedy KRS-owe odpisy dla samego Globu by ich nie pokazywały?  
Do głowy przychodziło mi, że musieli pobrać całą treść KRS-u, dla wszystkich firm w&nbsp;Polsce, i&nbsp;na tej podstawie rozrysować powiązania.

Ale sytuacja w&nbsp;KRS-ie stale się zmienia. Żeby mieć pewność, że mają aktualne dane, musieliby cały czas je pobierać i&nbsp;analizować (chyba że mieliby jakiś osobny kanał dostępu, taki *KRS premium*. Ale nie kojarzę, żeby istniała taka opcja).

Szukając odpowiedzi, natknąłem się na kolejne cenne źródło. **Monitor Sądowy i&nbsp;Gospodarczy**. Pokazujący dane nie w&nbsp;ujęciu „na poziomie firmy”, lecz czasowym -- wszystkie oficjalne zmiany z&nbsp;życia polskich spółek, jakie miały miejsce w&nbsp;konkretnym czasie.

Analizując Monitory, miałbym jak na dłoni sytuację w&nbsp;całej Polsce. Mógłbym rozrysowywać takie powiązania jak wyżej, a&nbsp;poza tym odpytywać bazę o&nbsp;różne ciekawostki.  
Ile firm się otwarło, ile zamknęło w&nbsp;okresie pandemii? Jaka osoba ma „pod sobą” najwięcej firm? Czy jakieś spółki mają w&nbsp;nazwach literówki?

Ta ciekawość stała się początkiem większej analitycznej przygody. Ale o&nbsp;tym opowiem już w&nbsp;innym wpisie :wink:

Trzymajcie się i&nbsp;miłego buszowania w&nbsp;firmach!
