---
layout: post
title:  "Intel Management Engine"
subtitle: "Potencjalny szpieg w twoim procesorze."
description: "Potencjalny szpieg w twoim procesorze"
date:   2021-07-26 17:10:37 +0100
tags: [Hardware, Centralizacja, DRM]
firmy: [Intel]
category: cyfrowy_feudalizm
category_readable: "Cyfrowy&nbsp;feudalizm"
image: 
   path: /assets/posts/intel-management-engine/intel-management-engine-hellsing.jpg
   width: 1200
   height: 700

image-width: 1200
image-height: 670
---

Od razu przejdźmy do rzeczy.

We wszystkich procesorach Intela stworzonych po 2008 roku znajduje się moduł Intel Management Engine.  
**Minimalistyczny „system ponad systemem” będący poza naszą kontrolą. I&nbsp;mający pełną władzę nad komputerem**.

{:.post-meta .bigspace}
Druga firma od procesorów, AMD, też ma zresztą swój odpowiednik. *PSP*. Ale jest o&nbsp;nim mniej informacji, więc tutaj go pominę.

Co to znaczy „pełną władzę”? Przede wszystkim ma wgląd do pamięci komputera. A&nbsp;zatem obrazu na ekranie, wpisywanych haseł, przesyłanych informacji...

Po drugie, oprócz oglądania może te informacje swobodnie zmieniać. Szyfrując część danych i&nbsp;trzymając je poza naszym zasięgiem. A&nbsp;nawet kontrolując wyświetlany obraz bez wiedzy naszego systemu.

<img src="/assets/posts/intel-management-engine/intel-management-engine-hellsing.jpg" alt="Przerobiony kadr z&nbsp;anime Hellsing. Pokazuje mężczyznę w&nbsp;białym stroju stojącego w&nbsp;ciemnościach tyłem do widza. Jego postawa wyraża strach. Wokół znajduje się wiele czerwonych oczu patrzących na niego. Zamiast jednego z&nbsp;nich wklejono opakowanie procesora Intela w&nbsp;kształcie bryły o&nbsp;wielu ścianach, otoczone czerwoną aurą."/>

{:.figcaption}
Źródło: anime *Hellsing* (z moimi przeróbkami).

Brzmi spiskowo, ale ma to całkiem realne, komercyjne uzasadnienie. **To nie zwykli Kowalscy są głównymi klientami Intela, tylko duże firmy**. Składające komputery albo używające całych ich flot. Dla nich możliwość większej kontroli nad systemem jest atrakcyjna, więc ją dostają.

Inną przyczyną dodania IME były zapewne interesy gigantów branży filmowej. Chcących gwarancji, że ich zaszyfrowane filmy dotrą aż do monitora bez możliwości ich zapisania.

Tym niemniej, skoro IME już tam siedzi i&nbsp;ma takie możliwości, jego przejęcie dałoby wirusa ostatecznego -- niewykrywalnego przez żaden program i&nbsp;pozbawionego barier.  
Co więcej, **prototypy takich superwirusów już powstały**. 

Temat dość niszowy, ale niesłychanie ciekawy. Zapraszam do lektury!

{% include info.html
type="Więcej informacji"
text="Mój wpis przycina stronę techniczną i&nbsp;akronimy do minimum. Jeśli chcecie zagłębić się w temat, to polecam:  
Bardzo fajny, przekrojowy artykuł od Zaufanej Trzeciej Strony, nazywający IME [jedynym legalnym trojanem](https://zaufanatrzeciastrona.pl/post/intel-management-engine-jedyny-legalny-trojan-sprzetowy/) (rodzaj wirusa).  
[Przystępne objaśnienie IME](https://www.howtogeek.com/334013/intel-management-engine-explained-the-tiny-computer-inside-your-cpu/) ze strony HowToGeek.  
Są również całkiem konkretne [informacje z&nbsp;Wikipedii](https://en.wikipedia.org/wiki/Intel_Management_Engine)."
 %}

## Natura i&nbsp;możliwości IME

Najlepiej posłuchać chyba samego oskarżonego. Intel w&nbsp;żadnym razie nie wypiera się istnienia IME, a&nbsp;nawet opisuje go [w oficjalnej broszurze](https://www.intel.com/content/dam/www/public/us/en/security-advisory/documents/intel-csme-security-white-paper.pdf) (nazywa go tu CSME, ale to jeden pies; nazwa i&nbsp;położenie kilka razy się zmieniały).

IME siedzi sobie w&nbsp;elemencie zwanym *PCH* (*Platform Controller Hub*) -- to taki kluczowy węzeł między różnymi elementami, w&nbsp;tym procesorem (*CPU*), podłączonymi urządzeniami (*I/O*), pamięcią (*flash*) a&nbsp;siecią (*LAN*).

{:.figure}
<img src="/assets/posts/intel-management-engine/intel-csme-schemat.webp" alt="Schemat pokazujący położenie Intel Management Engine pośrodku kilku innych elementów komputera."/>

{:.figcaption}
Położenie IME wśród innych części komputera.  
Źródło: broszura Intela.

Jest również praktycznie samowystarczalnym komputerem -- ma własny mały procesorek, system plików, pamięć, zegar...

Takie położenie i&nbsp;budowa dają mu szereg niezwykłych możliwości:

* nie da się go całkiem usunąć, bo jest potrzebny do uruchomienia systemu,
* potrafi działać na resztkach energii, **nawet po odłączeniu komputera od zasilania**,
* pozwala zdalnie włączyć komputer przez przesłanie energii kablem sieciowym (*Wake on LAN*),
* umożliwia sterowanie wieloma komputerami naraz,
* pozwala wyświetlać na ekranie konsolę i&nbsp;przesyłać różne komendy. Bez udziału systemu operacyjnego. Również zdalnie.

Nie wszystkie możliwości są dostępne na naszych komputerach, część jest dodatkowo płatna i&nbsp;wymaga osobnych umów. Ale wszystko mieści się w możliwościach IME. 

Broszura Intela zawiera fragmenty brzmiące jak reklama. Czytając między wierszami, można zobaczyć, czym próbują skusić klientów korporacyjnych.

{:.bigspace}
> Intel CSME supports HW DRM that helps users enjoy premium services from third-party providers, with control access to copyright material

Przetłumaczmy z&nbsp;korporacyjnego na ludzki. *HW DRM* to skrót od *hardware DRM*, czyli zabezpieczeń antypirackich na poziomie sprzętu (czyt. silniejszych niż programy).

W tym akapicie sugerują, że mogą zablokować użytkownikom dostęp do wybranych treści. I&nbsp;zapewnić, że nie będą mogli skopiować ich w&nbsp;formie cyfrowej (czasem to blokuje nawet robienie screenów). Zatem pozostanie im bierna konsumpcja i&nbsp;*enjoyowanie*.

{:.bigspace}
> Intel® Boot Guard is a&nbsp;feature that aids boot-execution integrity (...) so that the user can be more confident that the system is running an authentic, OEM BIOS

*Boot* i&nbsp;powiązane słowa odnoszą się po prostu do włączania komputera. *Authentic, OEM BIOS* oznacza mini-programy, uruchamiane od razu po włączeniu, dodane tam przez producenta sprzętu.

Niektórzy użytkownicy lubili majsterkować i&nbsp;wgrywać zamiast oficjalnego BIOS-a własne, takie jak *[coreboot](https://www.coreboot.org/)*.  
Dzięki temu mieli więcej kontroli nad sprzętem, ich komputery włączały się szybciej i&nbsp;byli wolni od ograniczeń dyktowanych przez producenta.

Intel w&nbsp;tym fragmencie się chwali, że może odebrać im swobodę wyboru -- komputer się nie włączy, jeśli sprzęt nie będzie się zgadzał z&nbsp;tym co ustawił producent. [Skończy się majsterkowanie](https://www.pcworld.com/article/2883903/how-intel-and-pc-makers-prevent-you-from-modifying-your-pcs-firmware.html).

{:.bigspace}
> Since CSME plays a&nbsp;critical, security role in Intel platform, Intel is committed to harden Intel CSME and implement various defense-in-depth mechanisms to help prevent abuse and attacks.

W tym miejscu obiecują, że będą dalej rozwijać i&nbsp;uszczelniać swojego *bożka w&nbsp;maszynie*, na wypadek gdyby jego kontrola przestała być absolutna.

Intel zrobił tu coś sprytnego. Odbiera użytkownikom możliwości i&nbsp;reklamuje to jako atut dużym partnerom biznesowym. A&nbsp;jednocześnie **jest chroniony od strony PR-owej, mówiąc że chodzi o&nbsp;bezpieczeństwo** (które IME gdzieś-jakoś-niby nieco poprawia).

Tylko można zadać sobie pytanie, co bardziej ugodzi w&nbsp;przeciętnego człowieka:

1. Ataki hakerskie, z&nbsp;gatunku naprawdę rzadkich i&nbsp;zaawansowanych? Kiedy są dużo łatwiejsze sposoby na oszustwo?
2. ...Czy wstawianie do komputera różnych szyfrowanych ścieżek dla wielkich korpo, poza zasięgiem użytkowników?

Nie ma sensu odpowiadać. Intel zdecydował za nas.

# Czym nie jest IME -- studzenie zapału

Przy tylu niepokojących faktach łatwo dać się ponieść i&nbsp;uznać, że IME już tu i&nbsp;teraz szpieguje i&nbsp;wysyła gdzieś wszystkie nasze dane. Wolę zachować umiar:

> Gdyby Intel Management Engine kontaktował się z&nbsp;siecią w&nbsp;innych sytuacjach, zapewne usłyszelibyśmy o&nbsp;tym dzięki programom takim jak Wireshark, które pozwalają każdemu monitorować ruch sieciowy.

{:.figcaption}
Źródło: [HowToGeek](https://www.howtogeek.com/334013/intel-management-engine-explained-the-tiny-computer-inside-your-cpu/).

Dlatego nazwałem go jedynie **potencjalnym** szpiegiem. IME ma wielkie możliwości i&nbsp;gdzieś zapewne są warianty szpiegowskie. Ale raczej nie na wielką skalę.

Dlaczego? Królestwo IME kończy się na naszym komputerze. Wysyłając dane w&nbsp;świat, traci nad nimi kontrolę. A&nbsp;po drodze można mu podstawić własne routery, czujniki, urządzenia starszej daty -- analizujące wszystko, co wysyła.

Poza tym temat fascynuje badaczy od cyberbezpieczeństwa. Możecie być pewni, że naświetlają go na wszelkie sposoby. **Gdyby IME słał dane w&nbsp;świat, to ktoś by to nagłośnił**.

Zatem aktywne szpiegowanie świata bym na razie wykluczył. Słabość IME, ta pierwsza i&nbsp;zamierzona, to prędzej odbieranie wolności pod płaszczykiem ochrony. Żeby przyjrzeć się kolejnym, najlepiej popatrzeć chronologicznie.

## Trochę historii

Historia ME to saga o&nbsp;korporacyjnym betonie, tańcu na ostrzu noża i&nbsp;nadużyciu pewnego dzieła.

# 1981 -- powstanie Minixa

Choć Intel Management Engine, „system w&nbsp;systemie”, ma nieco ponad 10 lat, historia sięga dużo dalej. [40&nbsp;lat wstecz](https://www.zdnet.com/article/minixs-creator-would-have-liked-knowing-intel-was-using-it/).

To dlatego, że Intel nie stworzył go od zera, lecz użył gotowego rozwiązania -- systemu operacyjnego **Minix** autorstwa prof. Andrew Tanenbauma. Takiego giganta informatyki, którego podręczniki przerabiało wielu studentów.

<img src="/assets/posts/intel-management-engine/tanenbaum-minix.webp" alt="Dwa obrazki umieszczone obok siebie. Pierwszy pokazuje profesora Tanenbauma, a&nbsp;drugi to rysunek uśmiechniętej głowy szopa pracza."/>

{:.figcaption}
Profesor Tanenbaum i&nbsp;Rocky Raccoon, maskotka systemu Minix 3.

Jak sama nazwa wskazuje, Minix jest mały. *System operacyjny* może nam się kojarzyć z&nbsp;czymś wielkim. Z&nbsp;przyjaznym interfejsem, mnóstwem możliwości i&nbsp;opcji.  
Ale większość taka nie jest. Wielu urządzeniom możliwość wyświetlania grafiki jest niepotrzebna, a&nbsp;do szczęścia wystarczy przesuwanie bitów.

O mały włos, a&nbsp;Minix nigdy by nie powstał. Tanenbaum testował go na płytce od Intela (tego samego; istnieją od 1977 r.). Napotkał poważny problem -- system co pewien czas się samoistnie wyłączał.

Pomogła dopiero uwaga pewnego studenta, który gdzieś wyczytał, że chip Intela pod wpływem wyższej temperatury wysyła sygnał przerywający.

W tamtym momencie prof. Tanenbaum podobno wyraził się dość niecenzuralnie o&nbsp;Intelu. Za to, że ukrywają takie rzeczy i&nbsp;nie mówią o&nbsp;nich w&nbsp;dokumentacji:

> Tak więc powiedziałem o&nbsp;Intelu te wszystkie niemiłe rzeczy, których nie powtórzę w&nbsp;Internecie. Jeśli chcą dodać czujnik temperatury, to proszę bardzo. Ale proszę: opisujcie to w&nbsp;instrukcji, wspomnijcie gdzieś o&nbsp;tym.

{:.figcaption}
Źródło: transkrypcja [wywiadu](https://www.coursera.org/lecture/python-databases/bonus-interview-andrew-Tanenbaum-minix-OiNHy) (tłumaczenie moje).

Jak później zobaczycie, podejście Intela niewiele się zmieniło od tamtego czasu.

# Minix trafia do procesorów Intela

W 2000 roku Tanenbaum udostępnił Minixa na darmowej licencji BSD -- absolutnie każdy mógł zajrzeć do jego kodu źródłowego i&nbsp;użyć go we własnym produkcie.

Jednocześnie liczył na skomercjalizowanie systemu. Wbrew pozorom otwarty kod nie jest sprzeczny z&nbsp;tym celem. Widzieć i&nbsp;ocenić może go każdy, ale mało kto umie go wdrożyć tak skutecznie jak twórca.

Z profesorem kontaktowali się pracownicy Intela. Raz zadając techniczne pytania związane z&nbsp;systemem, innym razem prosząc o&nbsp;wprowadzenie pewnych zmian (ograniczenie zużycia pamięci itp.).

Jak napisał [w liście otwartym](https://www.cs.vu.nl/~ast/intel/), nie wiedział do czego użyją tej wiedzy. Efekt końcowy go rozczarował.

> W&nbsp;swojej korespondencji ludzie z&nbsp;Intela nie mówili, nad czym pracują. Firmy rzadko opowiadają o&nbsp;przyszłych produktach bez zawarcia umów o&nbsp;poufności. Myślałem że to układ ethernetowy, chip graficzny albo coś podobnego. Gdybym podejrzewał, że budują urządzenie szpiegowskie, to z&nbsp;pewnością bym z&nbsp;nimi nie współpracował.

{:.figcaption}
Źródło: list otwarty prof. Tanenbauma. Wszystkie tłumaczenia moje.

List kończy się słowami:

{:.bigspace}
> Umieszczenie potencjalnego szpiega w&nbsp;każdym komputerze to okropny finał dla tej historii.

Na tym kończy się część z&nbsp;nadużyciem cudzego dzieła. W&nbsp;późniejszych latach historia IME i&nbsp;zawartego w&nbsp;nim Minixa to głównie odkrywanie luk i&nbsp;niebezpieczne zbliżanie się do przejęcia nad nim kontroli.

# Okres analiz i&nbsp;znajdowania błędów

Możliwości IME od początku były intrygujące. Różni badacze, w&nbsp;szczególności rosyjscy (mają tam mocnych speców od cyberbezpieczeństwa), wzięli go sobie na warsztat.

Wyspecjalizowała się w&nbsp;tym firma Positive Technologies. Na ich blogu można znaleźć cały szereg artykułów [o dziurawych zabezpieczeniach IME](http://blog.ptsecurity.com/search?q=management+engine).

Powstały liczne omówienia i&nbsp;prezentacje, takie jak ta [na konferencji RECON 2014](https://www.youtube.com/watch?v=4kCICUPc9_8), w&nbsp;której autor rozpoznaje różne programy zewnętrzne, zapewne kupione od innych firm i&nbsp;wepchnięte przez Intela do IME.

Z czasem zaczęto znajdować również tzw. *podatności*, czyli luki w&nbsp;zabezpieczeniach, pozwalające w&nbsp;sprytny sposób włamać się do tego systemu.

Te najwredniejsze dotyczyły wprawdzie tylko wersji IME z&nbsp;aktywowaną funkcją administracyjną (*AMT*), dodatkowo płatną... ale przez to były groźniejsze dla dużych firm.

{:.figure}
<img src="/assets/posts/intel-management-engine/podatnosci-amt.webp" alt="Slajd z&nbsp;prezentacji, ozdobiony w&nbsp;górnej części motywem konferencji BlackHat. Utrzymany w&nbsp;kolorystyce ciemnej z&nbsp;elementami zielonymi, neonowymi. Pokazuje oś czasu dla trzech podatności związanych z&nbsp;AMT, a&nbsp;także datę wprowadzania aktualizacji."/>

{:.figcaption}
Źródło: Slajd z&nbsp;konferencji *BlackHat Europe 2017*.


Jedna szczególnie wredna otrzymała numer CVE-2017-5689, kryptonim *Silent Bob is silent* i&nbsp;ocenę 9,8 / 10 pod względem ryzyka.

{:.bigspace}
> Ta podatność jest banalnie łatwa do wykorzystania. Maksymalnie pięć linijek kodu w&nbsp;Pythonie, można to zrobić jednolinijkową komendą. Daje pełną kontrolę nad dotkniętymi maszynami, w&nbsp;tym możliwość odczytywania i&nbsp;modyfikowania wszystkiego. Można jej użyć do trwałego instalowania złośliwych programów (być może na poziomie *firmware'u*)

Auć.

Jak napisał kolejny rosyjski badacz w&nbsp;jednej z&nbsp;[analiz po fakcie](https://www.blackhat.com/docs/us-17/thursday/us-17-Evdokimov-Intel-AMT-Stealth-Breakthrough-wp.pdf):

{:.bigspace}
> Nasuwa się logiczne pytanie: „Jaki wpływ może mieć \[ta podatność\]?”. Wyszukiwarka Shodan wskazywała na dzień 2 maja 6378 adresów IP połączonych z&nbsp;usługą Intel AMT. Jednak należy wziąć pod uwagę, że jej dane dotyczą jedynie \[publicznego\] Internetu, a&nbsp;sporą część urządzeń połączonych z&nbsp;AMT wykorzystuje się w&nbsp;sieciach firmowych.

Później Intel wypuścił łatkę naprawiającą [8 innych podatności](https://www.intel.com/content/www/us/en/support/articles/000025619/software.html). Z&nbsp;tego siedem wymagało fizycznego dostępu do komputera, na przykład wpięcia pendrive'a.  
Oprócz nich była jedna groźniejsza, oznaczona numerem CVE-2017-5712 (ocena zagrożenia 7,2 / 10), która **pozwalała przejąć komputer zdalnie, przez sieć**.

Mogło być tego więcej, ale *mea culpa*, nie jestem jeszcze na tyle obeznany z&nbsp;tematem, żeby wyłowić te dla ME.

Możliwe że to właśnie tego potrzebowały większe firmy, żeby się przestraszyć. W&nbsp;końcu sterują zdalnie całymi flotami urządzeń. Skutki ataku przez *AMT* byłyby dla nich opłakane.

# Maj 2017 - odkrycie furtki dla NSA

Równolegle z&nbsp;lukami bezpieczeństwa znaleziono sposób na uśpienie IME.

Wcześniej [wydawało się nie do ruszenia](https://hardenedlinux.github.io/firmware/2016/11/17/neutralize_ME_firmware_on_sandybridge_and_ivybridge.html) -- wszelkie próby grzebania kończyły się na tym, że komputer przez chwilę działał, ale po 30 minutach się wyłączał. Do tego sieć powiązań, zależność od fizycznych elementów, szyfrowanie... Programista płakał, jak majstrował.

Pomoc w&nbsp;usunięciu szpiega, paradoksalnie, przyszła za strony szpiegów. A&nbsp;raczej zostawionej dla nich furtki.

Okazało się, że IME posiada pewien specjalny tryb *HAP* (*High Assurance Platform*; w&nbsp;wolnym tłumaczeniu *Platforma Wysokiego Zaufania*). Jego działanie polega po prostu na tym, że IME przestaje działać.

Jak sugerują fragmenty kodu, **ten specjalny tryb dodano na żądanie amerykańskiego NSA** (agencji zajmującej się szpiegostwem; taki odpowiednik CIA w&nbsp;cyberprzestrzeni).  
Możliwe że tajniacy uznali IME za miecz obosieczny i&nbsp;zbyt duże zagrożenie dla swoich komputerów.

Mądrzy agenci. Dzięki odkryciom badaczy każdy może być jak oni i&nbsp;wyłączyć u&nbsp;siebie IME.

> Z&nbsp;ustaleń badaczy wynika, że aby na dobre zneutralizować Management Engine, należy kolejno ustawić bit HAP, następnie \[zmienić kilka innych rzeczy\].  
W efekcie uzyskujemy całkowicie zneutralizowane Management Engine (...), które się nie zawiesza: HAP wyłącza ME na wystarczająco wczesnym etapie.

{:.figcaption}
Źródło: [artykuł z&nbsp;dobreprogramy.pl](https://www.dobreprogramy.pl/Rosjanie-zneutralizowali-Intel-Management-Engine-pomogl-sekretny-bit-NSA,News,82851.html) (skróty moje).

...Wróć. Może jednak nie każdy?

> Dla przeciętnego użytkownika wyłączenie Intel ME jest praktycznie niemożliwe -- zgodnie z&nbsp;zamysłem.

{:.figcaption}
Źródło: [HowToGeek](https://www.howtogeek.com/334013/intel-management-engine-explained-the-tiny-computer-inside-your-cpu/) (tłumaczenie moje).

W każdym razie, jeśli jesteście nieprzeciętni i&nbsp;nie boicie się ryzyka, możecie skorzystać ze [skryptu do wyłączenia ME](https://github.com/corna/me_cleaner/wiki/How-does-it-work%3F) stworzonego przez badaczy.

Ale nie zapominajmy: **nawet jeśli uda się wyłączyć ME, to usunięcie nie wchodzi w&nbsp;grę**. Jest tak sklejony z&nbsp;innymi rzeczami, że bez niego komputer się nie włączy.

IME można co najwyżej uśpić. Zaśnie snem wiecznym, w&nbsp;komnacie w&nbsp;centrum naszego komputera. Być może czekając na *pocałunek prawdziwej miłości*{:.corr-del}pakiet aktualizacji, który go obudzi.

# Późniejszy 2017 -- bunt firm

Po fali skandali i&nbsp;odkryciu sposobu -- nawet tymczasowego -- na wyłączenie IME, niektóre firmy się zbuntowały. Nastąpił swoisty *exodus*:

* Purism, firma od początku reklamująca się chronieniem prywatności, zapowiedziała blokowanie ME na swoich laptopach.
* To samo zrobił inny producent laptopów, System76.
* Pod koniec 2017 roku również Dell dodał do oferty biznesowe [laptopy z&nbsp;wyłączonym ME](https://liliputing.com/2017/12/dell-also-sells-laptops-intel-management-engine-disabled.html). Za dodatkową opłatą.

Również pracownik Google, Ronald Minnich, ogłosił na pewnej konferencji, że **Google pracuje nad usunięciem ME ze swoich urządzeń**.

Jego prezentacja ma wdzięczny tytuł, w&nbsp;wolnym tłumaczeniu „Zastąp Linuxem swój *firmware* pełen luk” (gdzie Linux to alternatywny system, *firmware* to te mini-programy, a&nbsp;luki odnoszą się do błędów w&nbsp;zabezpieczeniach).

{:.figure}
<img src="/assets/posts/intel-management-engine/minnich-ime-prezentacja.webp" alt="Zdjęcie pokazujące prelegenta i&nbsp;slajd z&nbsp;jego prezentacji. Czerwona ramka dodana przeze mnie otacza informacje o&nbsp;tym, że Management Engine ma własny mały serwer, przez który da się włamać."/>

{:.figcaption}
Źródło: slajd z [prezentacji](https://youtu.be/iffTJ1vPCSo?t=380) Minnicha.

W prezentacji nawiązywał do głośnych historii z&nbsp;dziurami w&nbsp;zabezpieczeniach ME. Argumentował, że ten moduł jest jak niezbadana czarna skrzynka.  
Usunięcie go oznaczałoby odzyskanie większej kontroli nad swoim sprzętem.

Google jak Google, ale czasem trudno się nie zgodzić.

# 2018 -- luka w&nbsp;urządzeniach Apple

Pewien artykuł w&nbsp;*The Register* opisuje [kolejną wpadkę z&nbsp;IME](https://www.theregister.com/2018/10/03/intel_management_engine_hole/), tym razem u&nbsp;Apple.

Rosyjscy badacze odkryli, że IME posiada Tryb Fabryczny (*Manufacturing Mode*) dla producentów, który pozwala zmieniać pewne ustawienia IME. Jak mówią w&nbsp;wywiadzie:

{:.bigspace}
> Tryb Fabryczny jest przeznaczony do konfigurowania i&nbsp;testowania na etapie produkcji. Należy go zatem wyłączyć przed przejściem do sprzedaży komercyjnej.

Apple zapomniało ten tryb wyłączyć, przez co ich komputery były podatne na atak. Badacze im to zgłosili i&nbsp;w czerwcu Jabłkowi załatali lukę. Ale niesmak pewnie pozostał.

{% include info.html type="Ciekawostka" text="Jeśli umiecie korzystać z&nbsp;Pythona (tylko że wersji 2.7, nie powyżej 3), to możecie skorzystać ze [skryptu od rosyjskich badaczy](https://github.com/ptresearch/mmdetect) wykrywającego, czy wasz IME ma wyłączony Tryb Fabryczny." %}

Niedopatrzenie z&nbsp;winy Apple? Trochę pewnie tak, nie mam interesu w&nbsp;tym żeby ich bronić. Ale badacze dodają również:

{:.bigspace}
> Jednak ten tryb i&nbsp;potencjalne ryzyko **nie zostały opisane nigdzie w&nbsp;publicznej dokumentacji Intela**.

Czy to trochę nie przypomina problemów z&nbsp;Minixem i&nbsp;płytką Intela w&nbsp;1981 roku? :wink: Pewne rzeczy się nie zmieniają.

Redaktorzy z&nbsp;*The Register* zwrócili się do Intela z&nbsp;prośbą o&nbsp;komentarz. Rzecznik odpisał im:

{:.bigspace}
> Manufacturing Mode is an essential CSME design feature  
(...)  
End users who are concerned about the status of their systems can check with their system manufacturer.

Czyli tłumacząc na ludzki: „Smuteczek, ale nic nie zmienimy. Z&nbsp;pretensjami idźcie do Apple i&nbsp;innych składaczy komputerków”.

{:.bigspace}
> As always, Intel encourages end users to follow good security practices and keep their system software and firmware up to date.

„...I pamiętajcie, żeby myć ząbki po każdym posiłku”.

# 2020 -- wyciek danych Intela

Intel mimo wszystkich skandali, podatności i&nbsp;odchodzących firm pozostał niewzruszony. Ani myślał usuwać IME ani wydawać procesory w&nbsp;wersji pozbawionej tego modułu.

Kolejny cios przyszedł w&nbsp;2020 roku, kiedy z&nbsp;firmy wyciekł pokaźny pakiet 20 GB kodu źródłowego i&nbsp;dokumentów. Związanych między innymi z&nbsp;IME.

> Intel ME Bringup guides + (flash) tooling + samples for various platforms  
Intel Trace Hub + decoder files for various Intel ME versions

{:.figcaption}
Źródło: [Bleeping Computer](https://www.bleepingcomputer.com/news/security/intel-leak-20gb-of-source-code-internal-docs-from-alleged-breach/)

{% include info.html type="Ciekawostka" text="Wisienką na torcie jest notka od jednej z&nbsp;osób, które udostępniały pliki. Jak widać, w&nbsp;Intelu nie lubią silnych haseł."
trailer="<blockquote>
If you find password protected zips in the release <strong>the password is probably either \"Intel123\" or \"intel123\"</strong>. This was not set by me or my source, this is how it was aquired from Intel.
</blockquote>"
%}

Sam ani myślę zbliżać się do tak ciemnych spraw. Być może mój bliżej nieznany kolega, który jest większym ryzykantem, spróbuje znaleźć informacje z&nbsp;wycieku i&nbsp;się wczytać. Ale póki co jeszcze szuka :wink:

W każdym razie widać, że opieranie swojego bezpieczeństwa na zatajaniu informacji może co najwyżej opóźnić ich wypłynięcie.  
Gdyby w&nbsp;tych dokumentach były kluczowe informacje pozwalające „rozgryźć” IME, to hakerzy mieliby uciechę większą niż anioły bieszczadzkie.

# 2021 -- Intel i&nbsp;Windows 11

Niedawno Intel ogłosił współpracę z&nbsp;Microsoftem w&nbsp;zakresie wprowadzania nowego Windowsa.  
System dopiero zapowiedziano, więc możemy tylko spekulować. Z&nbsp;naszego punktu widzenia pewien niepokój może budzić jedna wiadomość:

**Windows 11 ma wymagać IME do działania** (źródło np. [tutaj](https://www.bleepingcomputer.com/news/microsoft/how-to-bypass-the-windows-11-tpm-20-requirement/)).

{:.post-meta .bigspace}
(ściśle rzecz biorąc, wymaga *zaufanego modułu (TPM)*, czyli elementu szyfrującego na poziomie sprzętowym; ale dla procesorów Intela to właśnie IME, a&nbsp;dla procesorów AMD -- PSP)

Co więcej, wymaga dość nowej jego wersji. W&nbsp;praktyce oznacza to, że wiele komputerów o&nbsp;wystarczającej mocy do uciągnięcia Windowsa 11, ale pozbawionych szyfrujących bajerów, nie będzie mogło ulec aktualizacji i&nbsp;zostanie ze starym systemem (albo pójdzie na śmietnik).

Pomijając ten fakt, ścisła współpraca tych dwóch firm mogłaby pozwolić jeszcze silniej odbierać kontrolę użytkownikom.

* Wzajemne chronienie sobie tyłków.

  Intel mógłby uniemożliwiać poprzez IME instalowanie alternatywnych systemów operacyjnych (takich jak Linux). A&nbsp;Windows mógłby blokować próby usuwania IME.

* Jeszcze mocniejszy DRM.

  Firmy mogłyby dogadać się z&nbsp;duetem Intel & Microsoft, żeby te blokowały możliwość kopiowania i&nbsp;przesyłania pewnych rzeczy na każdym możliwym poziomie.

* Brak możliwości wyłączenia wkurzających funkcji Windowsa (telemetria, przymusowe aktualizacje). Próby usunięcia przechwytywałoby IME.

Czy taka czarna wizja przyszłości może się ziścić? Dużo zależy tu od Microsoftu.  
Z jednej strony ma teraz duży wkład w&nbsp;*open source* i&nbsp;pracował m.in. nad integrowaniem Linuksa z&nbsp;Windowsem.  
Z drugiej -- niechlubną przeszłość, która doprowadziła do kar za monopolistyczne zachowania.

W kwestii Intela możemy natomiast zgadywać, znając poprzednie fakty, że raczej nie miałby oporów przed odbieraniem pewnych rzeczy szarym obywatelom.

## Podsumowanie

Wychodzi na to, że nieprędko pozbędziemy się małego, lecz wszechmocnego chochlika ME z&nbsp;naszych procesorów.

Intelowi za bardzo zależy na jego obecności. Do tego stopnia, że nawet opór ze strony innych wielkich korpo go nie przekonał do poluzowania kontroli nad tym, co w&nbsp;procesorze siedzi. Poświęcając jedną relację, nawiązuje inną.

Cała ta historia jest dla mnie świetną opowieścią ku przestrodze. Mamy tu:

* wielką firmę, której klientami są inne wielkie firmy, o&nbsp;interesach niekoniecznie zgodnych z&nbsp;naszymi;
* próbę odebrania nam kontroli nad własnymi urządzeniami;
* próbę utrzymania konkurencyjności przez trzymanie różnych rzeczy w&nbsp;tajemnicy;
* wykorzystanie cudzego dzieła, udostępnionego na otwartej licencji, do własnych celów;
* współpracę ze służbami i&nbsp;dodawanie dla nich specjalnych opcji;
* drętwe PR-owe slogany o&nbsp;bezpieczeńśtwie, kiedy pozostałe działania zbierają krytykę.

Czy cokolwiek możemy zrobić? Niestety, poza bojkotem takich praktyk, niewiele. W&nbsp;przeciwieństwie do mojej serii „Internetowa inwigilacja”, gdzie kontrolujemy przeglądarkę, tutaj mamy ograniczone pole manewru.

Jest niby AMD, ale oni również mają swój odpowiednik IME. Mniej opisany i&nbsp;mniej skandaliczny, ale może również go kiedyś opiszę. Jest Arm (obecnie święcący triumfy w&nbsp;nowych komputerach Apple), ale on też ma elementy zamknięte i&nbsp;„czarnoskrzynkowe”.

Możemy śledzić losy firm wprost sprzeciwiających się IME -- takich jak Purism, System76... A&nbsp;także różnych rzeczy związanych z&nbsp;**ruchem *open hardware***, który próbuje stworzyć od podstaw nowe podzespoły, udostępniając publicznie wszystkie plany.

Poza tym jest jedna uniwersalna prawda, jaką możemy wynieść z&nbsp;historii wyłączania IME -- **nie ma czegoś takiego jak furtka, która przepuszcza tylko bohaterów i&nbsp;blokuje złoczyńców**.  
Specjalny wyłącznik był przeznaczony dla służb, ale zdołali go użyć badacze. Innym razem mogą to być hakerzy.

Pamiętajmy: gdy ktoś mówi, żeby zabezpieczenia zawierały lukę specjalnie dla władz (i&nbsp;obowiązkowo powołuje się przy tym na bezpieczeństwo, dobro dzieci itp.)... to proszę, olewajmy cwaniaka. Historia ma aż nadto przykładów na to, jak takie rzeczy się kończą.

Jeśli dotrwaliście do końca, to chylę czoła :smile: Do zobaczenia w&nbsp;najbliższych, raczej lżejszych wpisach.
