---
layout: post
title:  "O cenzurze stron internetowych"
subtitle: "Wilk przeskoczy, wąż się prześlizgnie. My też."
description: "Wilk przeskoczy, wąż się prześlizgnie. My też."
date:   2022-09-12 07:10:00 +0100
tags: [Cenzura, DNS, Internet, Podstawy]
image:
   path: "/assets/posts/dns/dns-cenzura-baner.jpg"
   width: 1200
   height: 700
   alt: Przejście z barierkami symbolizujące blokadę stron internetowych. Obok niego w trawie wydeptano ścieżkę zakrytą napisem „Zmiana DNS-a”. Źródłem oryginalnego obrazka jest strona r4bb1t.
---

Gdzieś w&nbsp;odległych zakątkach tego świata mieszkają ludzie, którzy mieli pecha. Urodzili się w&nbsp;krajach mniej lub bardziej autorytarnych, próbujących ściśle kontrolować ich dostęp do informacji.

Często ta kontrola jest dziurawa i&nbsp;wystarczy parę prostych sposobów, żeby ją ominąć. Nie są one żadną wiedzą tajemną i&nbsp;można je znaleźć w&nbsp;zwykłych komentarzach internautów.

Jednak komentarze bywają odpowiednikiem ryby dla głodnego. Spełniają doraźną potrzebę, mówiąc trafnie *co zrobić*; ale nie mówią przy tym, *dlaczego* to robimy.

„Użyj Tora albo VPN-a”. „Zmień DNS-a”. Większości osób mało mówią takie inkantacje. A&nbsp;jeśli nawet ktoś znajdzie konkretne porady i&nbsp;raz obejdzie cenzurę, to kolejna aktualizacja urządzenia albo przeglądarki może go cofnąć do punktu wyjścia.

Stworzyłem ten wpis, żeby nieco wypełnić tę lukę informacyjną, dać wędkę zamiast ryby. Pokazać w&nbsp;przystępny sposób, dlaczego pewne metody -- zarówno cenzury, jak i&nbsp;obejścia -- działają.

{:.figure .bigspace-before}
<img src="/assets/posts/dns/dns-cenzura-baner.jpg" alt="Przejście z&nbsp;barierkami, obok którego w&nbsp;trawie wydeptano ścieżkę. Przejście jest zakryte banerem ostrzegającym, że wchodzimy na nielegalną stronę. Na ścieżkę nałożono napis „Zmiana DNS-a”."/>

{:.figcaption}
Źródło obrazka: [r4bb1t.com](http://www.r4bb1t.com/2015/01/ux-design-theory-vs-reality-summed-up.html). Przeróbki moje.

{:.post-meta}
A jeśli nie interesuje Cię „dlaczego” i&nbsp;jesteś tu po same rozwiązania, to możesz przeskoczyć do [odpowiedniej części wpisu](#omijamy-blokady).

# Spis treści

* [Wprowadzenie i&nbsp;motywacja](#wprowadzenie-imotywacja)
* [Anatomia klikania w&nbsp;link](#anatomia-klikania-wlink)
* [Metody internetowej cenzury](#metody-internetowej-cenzury)
  * [Cenzura przez DNS](#cenzura-przez-dns)
  * [Cenzura przez adresy IP](#cenzura-przez-adresy-ip)
  * [Strącenie niewygodnej stronki](#strącenie-niewygodnej-stronki)
* [Omijamy blokady](#omijamy-blokady)
  * [Użycie innego hotspota](#użycie-innego-hotspota)
  * [Archiwa internetowe](#archiwa-internetowe)
  * [Stronki pośredniczące](#stronki-pośredniczące)
  * [Google Translate i&nbsp;podobne serwisy](#google-translate-ipodobne-serwisy)
  * [VPN / Tor](#vpn--tor)
  * [Zmiana DNS-a](#zmiana-dns-a)
* [Podsumowanie](#podsumowanie)

## Wprowadzenie i&nbsp;motywacja

To co, dupochronik na początek? :wink:  
Mój wpis jest neutralnym omówieniem narzędzi pozwalających omijać cenzurę **w krajach całkiem obcych, nie utrzymujących z&nbsp;Polską stosunków dyplomatycznych**. Wszelkie podobieństwo do metod omijania polskich blokad jest niezamierzone i&nbsp;przypadkowe.

Skoro ta sprawa z&nbsp;głowy, to odpowiem jeszcze na hipotetyczny zarzut:  
„Jeśli to blokują, to widocznie mają ważny powód! Po co tam wchodzisz?”.

Po pierwsze: niekoniecznie muszą mieć ważny powód. Czasem to po prostu kaprys prywatnego operatora telekomunikacyjnego (to oni wprowadzają cenzurę od strony technicznej).

Pewien taki hiszpański operator, Masmovil, [blokował stronę Projektu Tor](https://nitter.net/njal_la/status/1467838745575665673#m), zapewniającego darmowe narzędzia do zachowania anonimowości w&nbsp;sieci. Nie mieli żadnego nakazu sądowego, żeby taką blokadę wprowadzić, zrobili to na własną rękę i&nbsp;wbrew niektórym swoim klientom.

Po drugie: może nie jestem przeciwny blokadzie, ale mam powód, żeby zajrzeć na drugą stronę. Na przykład chcę zobaczyć, jakie kwestie „trendują” na cenzurowanych stronach propagandowych, żeby użyć tej wiedzy [do wyłapywania trolli]({% post_url 2022-04-15-trolle-rosja-ukraina %}){:.internal}.

Po trzecie: może po prostu tak mi każe buntownicza natura.

Są dziesiątki powodów i&nbsp;nie będę w&nbsp;nie wnikał. Chcę tu tylko dzielić się (amatorską) wiedzą i&nbsp;przydatnymi metodami, a&nbsp;nie bawić się w&nbsp;moralizowanie. A&nbsp;zatem -- przejdźmy do wiedzy.

## Anatomia klikania w&nbsp;link

Z punktu widzenia internautów życie jest proste -- przewijamy sobie stronę w&nbsp;naszej przeglądarce, aż nasz wzrok przykuje jakiś link. Klikamy w&nbsp;niego. Chwilę później na naszym ekranie wyświetla się kolejna strona. Przewijamy...

Za kulisami dzieje się jednak kilka ciekawych rzeczy. Warto je pobieżnie poznać, żeby wiedzieć, jak działa cenzura.

Załóżmy, że klikamy w&nbsp;zwykły link -- [taki jak ten]({% post_url 2021-01-11-internetowa-inwigilacja-1-podstawy %}){:.internal}, prowadzący do mojego pierwszego wpisu z&nbsp;serii „Internetowa inwigilacja”.  
Jego pełen adres jest taki:

<div class="black-bg mono bigspace">
https://www.ciemnastrona.com.pl<span class="red">/internetowa_inwigilacja/2021/01/11/internetowa-inwigilacja-1-podstawy</span>
</div>

Fragment na biało to **_domena_ -- taki trzon nazwy strony**. Jest jak parasol, pod którym zebrane są wszystkie podstrony. Czyli na przykład różne wpisy na moim blogu.

Tylko że domena to odpowiednik czytelnej nazwy adresata. Taki „Jan Nowak” na wysyłanej pocztówce z&nbsp;wakacji.  
Jeśli chcemy coś wysłać temu Nowakowi, to musimy na kopercie zapisać również jego adres. Inaczej nasza przesyłka nie dotrze na miejsce. W&nbsp;internecie takimi adresami są *adresy IP*.

Problem: w&nbsp;momencie klikania w&nbsp;link do nieznanej wcześniej strony przeglądarka nie zna jej adresu IP. Ma tylko czytelną nazwę domeny, *ciemnastrona.com.pl*. W&nbsp;jakiś sposób musi przejść od tej czytelnej nazwy do właściwego adresu.

W tym celu wysyła pytanie do **DNS-a -- swoistej książki adresowej internetu**. Ten odpisuje, podając liczbowy adres. Jak na przykład:

<div class="black-bg mono bigspace">
213.186.33.5
</div>

Mając ten ogólny adres, przeglądarka wysyła pod niego prośbę o&nbsp;konkretną rzecz. Czyli w&nbsp;naszym przypadku -- o&nbsp;pierwszy wpis z&nbsp;„Internetowej Inwigilacji”.

Otrzymuje go, a&nbsp;strona wyświetla się na naszym ekranie. Dla wzrokowców schemat całej interakcji, czytamy od góry do dołu:

{:.bigspace-before}
<img src="/assets/posts/dns/internet-plus-dns-schemat.jpg" alt="Schemat pokazujący w&nbsp;dwóch linijkach interakcje podczas przeglądania internetu. W&nbsp;pierwszej linijce widać dwie strzałki między ikonami laptopa a&nbsp;serwera z&nbsp;napisem DNS. Nad górną strzałką widać kartkę z&nbsp;napisem 'ciemnastrona.com.pl' i&nbsp;znakiem zapytania. Zaraz pod nią widać strzałkę idącą od DNS-a do laptopa, z&nbsp;kartką, na której napisany jest adres. Druga linijka też zawiera dwie strzałki. Od laptopa do innego serwera wysyłana jest kartka z&nbsp;pytaniem o&nbsp;konkretny wpis. Zaraz pod nią jest ostatnia strzałka, od serwera do laptopa. Widać nad nią ikonę z&nbsp;logiem Ciemnej Strony." loading="lazy" width="800" height="600"/>

{:.figcaption}
Źródło tych i&nbsp;kolejnych ikon: Flaticon, ikony systemu Linux.  
Dokładna lista [pod koniec wpisu](#źródła-obrazków).

...Ale co, jeśli coś pójdzie nie tak?  
Być może Ciemna Strona jest w&nbsp;jakimś obcym, odległym od Polski kraju cenzurowana. W&nbsp;takim wypadku zamiast upragnionej strony moglibyśmy zobaczyć jedynie pustkę. Albo stronę z&nbsp;ostrzeżeniem.

## Metody internetowej cenzury

Cenzura nastąpiła zapewne na którymś z dwóch etapów:

* Na etapie kontaktu z&nbsp;DNS-em (cenzura przez DNS, najczęstszy rodzaj);
* Na etapie kontaktu z&nbsp;właściwym adresatem (cenzura przez IP).

Oczywiście możliwe też, że cenzor uderzył bezpośrednio w&nbsp;stronkę, którą chcieliśmy odwiedzić.

Przybliżmy teraz różne metody cenzurowania treści w&nbsp;internecie.

### Cenzura przez DNS

Wspomniałem wyżej, że DNS jest jak *książka adresowa internetu* i&nbsp;że to do niego zwraca się nasza przeglądarka. Ale to dość szczątkowe informacje. Czym on jest, do kogo należy?

Odpowiedź: DNS (*Domain Name System*) to całe skupisko serwerów -- mocnych komputerów odpowiadających na zapytania internautów.

Pojedynczy serwer nie pomieściłby wszystkich adresów stron. Dlatego DNS ma ścisłą hierarchię. Jeśli nie zna jakiegoś adresu, o&nbsp;który go pytamy, to „przekazuje pytanie wyżej”. W&nbsp;korpojęzyku: *eskaluje*.  
Któryś z&nbsp;serwerów powinien wiedzieć, jaki jest adres szukanej przez nas strony.

Zresztą *System* w&nbsp;liczbie pojedynczej może trochę przekłamywać, bo *nie ma czegoś takiego jak pojedynczy, ogólnoświatowy DNS*.

Często każda firma telekomunikacyjna daje nam własny. Zapewne wpięty w&nbsp;coś globalniejszego, ale poza tym kontrolowany przez nią. W&nbsp;Polsce takimi telekomami są na przykład Play i&nbsp;Orange.

A w&nbsp;jaki sposób go „daje”? Ano w&nbsp;taki, że w&nbsp;momencie łączenia się z&nbsp;internetem nasz punkt dostępu -- czyli na przykład router albo telefon, jeśli korzystamy z&nbsp;sieci mobilnej -- proponuje nam adres DNS-a ustawiony przez producenta.

Zatem **najczęściej korzystamy z&nbsp;tego, co nam ustawiła firma telekomunikacyjna. Zapewne ich własnego DNS-a, nad którym mają kontrolę**.  
Zaś dzięki tej kontroli może na przykład ustawić na prośbę rządu, żeby DNS wysyłał nieprawdziwą informację, gdy tylko zostanie zapytany o&nbsp;adres cenzurowanej strony.

{:.bigspace}
<img src="/assets/posts/dns/evil-dns.jpg" alt="Schemat podobny do poprzedniego. Pokazuje strzałkę z&nbsp;pytaniem o&nbsp;domenę ciemnastrona.com.pl. Wychodzi ona od laptopa do serwera z&nbsp;napisem DNS, na który tym razem nałożonę emotkę uśmiechniętego diabełka. Poniżej widać strzałkę idącą od złego serwera do laptopa, a&nbsp;na niej napis 'Nie wiem'." loading="lazy" width="800" height="321"/>

**To najczęściej stosowana metoda cenzury. Jest dla rządów prosta, bo wystarczy wysłać oficjalne żądanie do firmy telekomunikacyjnej**. Jest też dość skuteczna, bo wielu użytkowników korzysta z&nbsp;domyślnych DNS-ów i&nbsp;nie ma pojęcia, jak je zmienić.

#### Cenzura tak, oszustwo nie

Fałszywe informacje? Możemy sobie teraz wyobrazić scenariusz straszniejszy niż cenzura -- DNS całkowicie nas okłamuje. Pytamy go o&nbsp;stronę fikcyjnego banku *nasz-bank.pl*, zaś on odsyła nam adres IP odpowiadający całkiem innej stronce, *niedobrzy-ludzie.lol*.

W pasku przeglądarki widzimy domenę naszego banku, a&nbsp;strona jest wierną podróbką tej prawdziwej bankowej. Ufnie wpisujemy w&nbsp;formularze nasze dane i&nbsp;zostajemy ograbieni.  
Na szczęście **to raczej mało realny scenariusz i&nbsp;DNS nas wprost nie oszuka**.

Po pierwsze: czasem działa mechanizm obronny o&nbsp;nazwie *[DNSSEC](https://blog.cloudflare.com/dnssec-an-introduction/)* (skrót od *DNS Security Extensions*).

Tak jak wcześniej wspominałem, DNS ma swoją hierarchię. Serwery wyżej położone mogą ręczyć za te będące niżej. Zyskujemy swoisty łańcuszek zaufania; zaczynający się od jednego z&nbsp;nielicznych podmiotów zapisanych w&nbsp;naszej przeglądarce.

Ta centralizacja zaufania może budzić mieszane uczucia. Ale dzięki temu, że wychodzi od instytucji międzynarodowych, powinna być odporna na próby oszustwa na poziomie krajów.  
Kiedy *DNSSEC* działa, to mamy gwarancję, że DNS udziela nam autentycznej odpowiedzi.

Po drugie: niezależnie od tego, czy działa DNSSEC, [drugą warstwą ochronną jest HTTPS](https://security.stackexchange.com/questions/137855/does-https-protect-against-dns-rebinding).

Za każdym razem, kiedy odwiedzamy stronki zaczynającą się od `https://`, muszą one okazać naszej przeglądarce *certyfikat* -- swoisty „dowód tożsamości”, inny dla każdej strony i&nbsp;wystawiony przez jedną z akceptowanych instytucji. Praktycznie nie do podrobienia.

Wniosek: o&nbsp;ile nie zajdą jakieś szczególne okoliczności, to DNS raczej nie będzie w&nbsp;stanie całkowicie nas okłamać. Uff.

{% include info.html
type="Ciekawostka"
text="Jeśli budzi Wasz niepokój fakt, że filarami bezpieczeństwa w&nbsp;internecie jest tylko kilka organizacji, to obawy mogą być uzasadnione.  
Przypadek złej/przejętej instytucji poręczającej już miał miejsce. Była to głośna [aferka wokół DigiNotar](https://www.theregister.com/2011/09/06/diginotar_audit_damning_fail/) -- wystawili komuś całkiem obcemu certyfikaty przeznaczone dla Google, Skype'a, Microsoftu... Mogło to pozwolić hakerom zyskać wgląd do kont mailowych 300&nbsp;000 Irańczyków.  
Warto o&nbsp;tych sprawach wiedzieć, ale są nieco poza tematyką tego wpisu."
%}

Tym niemniej DNS nadal może wyrządzić nam złośliwość. Na nasze pytanie o&nbsp;adres strony może po prostu skłamać „nie wiem, nie znam”.  
Nie trafimy wtedy na żadną stronę, ale w&nbsp;naszej przeglądarce wyświetli się charakterystyczny błąd.

{:.figure .bigspace}
<img src="/assets/posts/dns/dns-nxdomain.jpg" alt="Komunikat mówiący, że nie udało się wyświetlić domeny. Jej nazwa jest zamazana, a&nbsp;pod spodem widać kod błędu DNS_PROBE_FINISHED_NXDOMAIN" loading="lazy" width="429" height="230"/>

Jeśli go zobaczymy, to warto zacząć się rozglądać za sposobem na obejście cenzury. Parę przykładowych za moment.

### Cenzura przez adresy IP

Nawet jeśli poznaliśmy adres stronki, zagrożenie cenzurą nie znika. Możliwe jest bowiem blokowanie adresów IP.

Kiedy cokolwiek wysyłamy w&nbsp;sieć -- również prośby o&nbsp;konkretne strony -- adres IP naszego adresata jest widoczny na zewnątrz. Dla każdego, komu tylko chce się patrzeć. A&nbsp;cenzorom się chce.

Nasza prośba o&nbsp;stronkę zapewne będzie przechodziła przez infrastrukturę firmy telekomunikacyjnej -- ich routery i&nbsp;inne bajery. Całkiem możliwe, że **spojrzą na adres IP, zobaczą że jest na liście stron blokowanych i&nbsp;nie prześlą naszej prośby dalej**. Nie dostaniemy upragnionej stronki.

{:.bigspace}
<img src="/assets/posts/dns/evil-router.jpg" alt="Schemat pokazujący, jak od laptopa odchodzi strzałka i&nbsp;trafia do routera ozdobionego emotką uśmiechniętego diabełka. Od routera wychodzi kolejna strzałka, skierowana do rysunkowego kosza na śmieci, a&nbsp;nad nią widać karteczkę zaadresowaną do 'abcd'. Po prawej stronie widać serwer podpisany 'abcd', do którego ostatecznie nie trafia żadna strzałka." loading="lazy" width="800" height="400"/>

Jeśli to taka skuteczna metoda, to dlaczego nie jest częściej stosowana?

A dlatego, że w&nbsp;obecnych czasach pod jednym adresem IP często znajduje się wiele różnych domen. Do tego adresy IP bywają co pewien czas zmieniane.  
Gdyby tak po prostu zablokować adres IP, to wiele całkiem przypadkowych stron przestałoby działać. Z&nbsp;punktu widzenia telekomu to niezadowoleni klienci.

Mimo to znane są przypadki, kiedy ich takie wahania nie powstrzymały.  
Raz zrobiła to nasza autokratyczna Rosja, [uderzając w&nbsp;popularne serwery od Amazona i&nbsp;Google'a](https://www.bleepingcomputer.com/news/government/russia-bans-18-million-amazon-and-google-ips-in-attempt-to-block-telegram/).

Innym przykładem są [blokady nałożone przez pewien austriacki telekom](https://news.ycombinator.com/item?id=32630757). Zapewne pod presją wydawnictwa naukowego Elsevier. Zarówno na domeny, jak też na adresy IP.

Wśród zablokowanych adresów były największe firmy oferujące infrastrukturę internetową.  
Telekomy musiały dobrze wiedzieć, że taka blokada będzie małą internetową katastrofą. A&nbsp;jednak podjęły ten krok.

### Strącenie niewygodnej stronki

Czasem ktoś bardzo nie chce, żeby ludzie poznali pewne informacje. Może wtedy uderzyć w&nbsp;samo źródło, zamiast stawiać dziurawe płotki na drodze zwykłych internautów. 

Może to zrobić, wysyłając na przykład groźne prawnicze pismo do firmy zapewniającej tej stronie hosting. Albo koordynując cyfrowy atak, polegający na przeciążeniu niewygodnej strony przez bombardowanie jej zapytaniami. 

Oczywiście w&nbsp;skali międzynarodowej możliwości tej metody są ograniczone.  
Jest mała szansa na to, że jakaś firma z&nbsp;USA tak od ręki usunie hostowaną przez siebie stronę, bo jakiś Chińczyk napisał, że jej nie lubi.

Natomiast jeśli cenzor ubije stronkę, w&nbsp;ten czy inny sposób, to żadne DNS-y czy VPN-y nie pomogą. Po prostu jej nie ma. Trzeba czekać aż się odrodzi albo ją zastąpić czymś nowym.

## Omijamy blokady

Najczęstszą blokadą jest ta na poziomie DNS-a. Zatem zmiana DNS-a wydaje się rozwiązaniem najlepiej dopasowanym do problemu i&nbsp;często jest polecana.

Problem w&nbsp;tym, że wymaga to zmiany ustawień. Tak, to dość łatwe i&nbsp;wymaga tylko paru kliknięć. Ale może odstraszać wiele osób, obawiających się że „coś popsują”.

Z tego względu postanowiłem **zacząć od metod pozbawionych efektów ubocznych**. Nie musimy niczego zmieniać po swojej stronie, żeby z&nbsp;nich skorzystać. Po prostu próbujemy. Jeśli nie zadziała, to sprawdzamy kolejną metodę.

### Użycie innego hotspota

Rozwiązanie rzadko polecane jako sposób na zmianę DNS-a, a&nbsp;jednak całkiem realne. Jest o&nbsp;tyle fajne, że nie wymaga żadnego grzebania w&nbsp;ustawieniach.

Po prostu **zabieramy laptopa na spacer do kawiarni lub galerii handlowej, tam podłączamy się do jakiegoś otwartego hotspota**.

Żeby sprawdzić na komputerze, jakiego proponują nam DNS-a, możemy po połączeniu z&nbsp;siecią kliknąć w&nbsp;ikonę siły sygnału w&nbsp;prawym dolnym rogu i&nbsp;wybrać stamtąd opcję `Informacje o połączeniu` albo coś podobnego.  
Sprawdzałem na systemach Windows i&nbsp;Linux Mint, tu przykład z&nbsp;tego drugiego:

{:.figure .bigspace-before}
<img src="/assets/posts/dns/hotspot-galeria-dns.jpg" alt="Zrzut ekranu okna z&nbsp;informacjami na temat hotspota w&nbsp;Galerii Krakowskiej. Czerwoną ramką otoczona pola zawierające liczbowe adresy DNS-ów" loading="lazy" width="437" height="419"/>

{:.figcaption}
Hotspot w&nbsp;pewnej galerii. Proponuje nam dwa adresy DNS, podstawowy i&nbsp;rezerwowy. O&nbsp;ile nie ustawiliśmy własnego, to nasz komputer skorzysta z&nbsp;któregoś z nich.

Czasami administratorzy ręcznie ustawiają w&nbsp;routerach DNS-y spod adresów *1.1.1.1* (Clouflare) albo *8.8.8.8* (Google). Które nie cenzurują krajowych stronek, a&nbsp;przy tym są na tyle powszechne, że ustawianie ich nie budzi podejrzeń.

Jeśli trafimy na takiego hotspota, to ominiemy blokadę na poziomie DNS-a. Nie musimy nic robić, po prostu przeglądamy internet jak zawsze.

Blokada na poziomie IP nadal by nas zatrzymała. Ale, jak wspominałem, takie przypadki są dużo rzadsze.

### Archiwa internetowe

To serwisy, które zapisują i&nbsp;przechowują treść stron internetowych podsyłaną im przez użytkowników.   
O ile same nie są blokowane albo nie wywarto na nie nacisków, to powinniśmy być w&nbsp;stanie łatwo je odwiedzić i&nbsp;znaleźć na nich poszukiwaną treść.

Jak z&nbsp;nich korzystać?

1. Kopiujemy link do naszej cenzurowanej strony.

   Prawy przycisk myszy i&nbsp;opcja `Kopiuj link/odnośnik`; na urządzeniu mobilnym przytrzymujemy palcem, żeby pojawiły się opcje.

2. Odwiedzamy stronę archiwum.

   Podam tu przykłady dwóch -- *[Wayback Machine](http://web.archive.org/)* oraz *[archive.ph](https://archive.ph/)*.

3. Wklejamy link w&nbsp;pole.

   Zwracamy przy tym uwagę na to, żeby wkleić we właściwe -- w&nbsp;przypadku *archive.ph* górne pole w&nbsp;czerwonej ramce to miejsce na wklejenie strony do zarchiwizowania. Wyszukiwarka stron już zapisanych jest niżej.

Jeśli ktoś wcześniej zapisał treść do archiwum, to wyświetli się kalendarz z&nbsp;datami zrzutów. Klikamy w&nbsp;którąś z&nbsp;nich, żeby wyświetlić treść strony w&nbsp;danym dniu. 

Ograniczeniem archiwów jest to, że przechowują jedynie zrzut z&nbsp;określonego momentu w&nbsp;czasie. Jeśli cenzurowana strona się często zmienia, to możliwe że w&nbsp;archiwum nie będzie jej najbardziej aktualnej wersji.

To zamrożenie w&nbsp;czasie może być również zaletą. **Archiwum to nasz jedyny ratunek, jeśli strona została ubita przez cenzora**.

{% include info.html
type="Ciekawostka"
text="Archiwa czasem same są blokowane na poziomie DNS-ów. Nie zawsze przez cenzurę krajową.  
Takie na przykład *archive.is*, czyli jedno z&nbsp;najbardziej niepokornych archiwów, nie działało, gdy próbowało się poznać jego adres przez DNS-a od Cloudflare (dziękuję za informację, M.). Według pewnego wpisu, odsyłającego do źródeł, [nie była to taka czarno-biała sprawa](https://jarv.is/notes/cloudflare-dns-archive-is-blocked/).  
W każdym razie w&nbsp;internecie nie ma co wierzyć komukolwiek na sto procent, jest pełno odcieni szarości."
%}

### Stronki pośredniczące

To strony internetowe takie jak [ProxySite](https://proxysite.page/en/) oraz zapewne sporo innych (osobiście nie testowałem żadnej).

Podajemy im link do odwiedzanej strony, a&nbsp;te odwiedzają ją swoimi skryptami, pobierają i&nbsp;nam wyświetlają. Zapewne korzystają przy tym z&nbsp;własnego DNS-a i&nbsp;raczej są niezależne od naszego telekomu. Więc cenzura ich nie powstrzyma. 

Wady tej metody?  
Domniemana: nie mamy pewności, czy takie stronki nie zbierają o&nbsp;nas ogólnych danych (jak te, które opisywałem w&nbsp;„Internetowej inwigilacji”). Fakt, że świadomie próbujemy ominąć cenzurę, może nas dodatkowo wyróżniać z&nbsp;tłumu.  
Techniczna: raczej nie pobierzemy w&nbsp;taki sposób stron dynamicznie ładowanych lub wymagających logowania.

### Google Translate i&nbsp;podobne serwisy

{:.post-meta .bigspace-after}
Metodę z&nbsp;GT znalazłem w&nbsp;jednym z&nbsp;komentarzy na Zaufanej Trzeciej Stronie.

Sposób dość nieoczekiwany, ale wbrew pozorom jak najbardziej ma sens. Możecie użyć [Google Translate w&nbsp;trybie tłumaczenia stron internetowych](https://translate.google.com/?sl=auto&tl=pl&op=websites) i&nbsp;w ten sposób poznać ich treść, omijając cenzurę.

To działa, ponieważ GT też jest *de facto* stronką-posrednikiem. Odwiedza wskazaną stronę swoimi skryptami, pobiera jej treść i&nbsp;pokazuje nam tłumaczenie.

W podobny sposób zadziałałaby jakakolwiek usługa, która pobiera strony za nas. Może oferuje coś podobnego jakiś przyszłościowy startup, który przerabia strony na wersję o&nbsp;wyższym kontraście dla osób z&nbsp;wadami wzroku? Albo zamienia czcionki na stronie na Comic Sans?

Możliwości jest wiele, a&nbsp;ich „katalog” otwarty.  
**O ile jakiś serwis sam nie jest blokowany i&nbsp;może pobrać stronkę za nas, to nada się na pośrednika**.

Wady? W&nbsp;przypadku Google fakt, że pewnie dodadzą informację o&nbsp;tym, jakie to strony u&nbsp;nich tłumaczyliśmy, do zbieranej na nas teczki. Odwiedzane serwisy też mogą cenzurować. No i&nbsp;mamy te same kwestie techniczne co przy oficjalnych stronkach-pośrednikach.

### VPN / Tor

Nazwy, które bardzo często wymieniane są razem.  
VPN-y reklamują się na tyle intensywnie -- również w&nbsp;kontekście omijania blokad na Netflixa -- że większość młodszego pokolenia pewnie coś o nich słyszała. Tor jest raczej mniej znany.

Planuję kiedyś stworzyć wpis dokładniej omawiający różnice i&nbsp;synergie między tymi dwoma wynalazkami.

Ale jeśli chodzi o&nbsp;zajrzenie na pojedynczą cenzurowaną stronkę, to szczerze powiedziawszy są niemal identyczne. **Oba są pośrednikami, które biorą od nas rzeczy przeznaczone dla innego serwera i&nbsp;wysyłają je w&nbsp;swoim imieniu**.

A nas zadowala dosłownie każdy pośrednik, który spełnia następujące warunki:

* Musi korzystać z&nbsp;własnych, niezależnych od naszego telekomu serwerów DNS.

  W&nbsp;innym wypadku nie dalibyśmy rady omijać blokad na poziomie DNS-a.  
  Na szczęście to raczej standard. Robią to zarówno Tor, jak i&nbsp;wiele VPN-ów. 

* Nie ujawnia, jaki jest adres IP serwera, z&nbsp;którym chcemy się skontaktować.
* Jego (pośrednika) adres IP nie jest blokowany.

  Dzięki tym właściwościom ominiemy również potencjalne blokady poprzez adresy IP.

Choć Tor jest potężniejszy, wydaje mi się tu prostszym rozwiązaniem -- możemy po prostu go [pobrać z&nbsp;oficjalnej strony](https://www.torproject.org/download/), zainstalować, odwiedzić cenzurowaną stronkę. A&nbsp;potem zostawić na dysku. Nie będzie nam wchodził w&nbsp;drogę, a&nbsp;czasem pomoże.  
Myślę, że można nawet szczerze go polubić. Mimo kilku niedogodności:

* Będzie blokowany przez niektóre strony; inne mogą częściej wyświetlać nam Captchę i&nbsp;podobne przeszkadzajki.
* Przeglądanie z&nbsp;nim może być dość powolne.

Dla jasności: wady nie wynikają wyłącznie z&nbsp;winy Tora. Spowolnienie jest nieuniknione, kiedy nasze dane są wysyłane przez liczne „węzły przesiadkowe”. Zaś za blokowanie odpowiadają właściciele stron, zapewne korzystający z&nbsp;gotowych list. Tym niemniej wady istnieją.

Jeśli Tor to zbyt ciężkie działo na nasze potrzeby, to można również skorzystać z&nbsp;darmowego VPN-a (z nazwy), zintegrowanego z&nbsp;przeglądarką Opera.  
VPN od Opery nie jest zbyt wysoko oceniany, ale to raczej przez porównanie z&nbsp;konkurencją. Na nasze potrzeby w&nbsp;zupełności wystarczy -- sprawdzałem na przykładowej stronie, cenzurę ominął.

Żeby nie dublować tu instrukcji, odsyłam [do tej z&nbsp;mojego dawnego wpisu]({% post_url 2021-06-12-adres-ip %}#vpn-zintegrowany-zoperą){:.internal}. Kontekst minimalnie inny, ale kroki są dokładnie takie same.

Istnieją również liczne komercyjne VPN-y, których jednak nie będę tutaj wymieniał.

### Zmiana DNS-a

{:.figure}
<img src="/assets/posts/dns/dns-graffiti.jpg" alt="Zdjęcie pokazujące napisy na fasadzie tureckiego budynku. Wskazują one dwa adresy DNS do ominięcia cenzury: jeden złożony z&nbsp;czterech ósemek, a&nbsp;drugi z&nbsp;dwóch ósemek i&nbsp;dwóch czwórek." loading="lazy" width="624" height="351">

{:.figcaption}
Kiedy rząd Turcji zablokował w&nbsp;2014 roku Twittera, ludzie wypisywali sprejem na ścianach adres DNS-a, który pozwoliłby ominąć cenzurę (tu akurat DNS od Google'a).  
Źródło: [blog Cloudflare](https://blog.cloudflare.com/dnssec-an-introduction/).

Jeśli już jesteśmy gotowi grzebać w&nbsp;ustawieniach, to można pokusić się o ustawienie jakiegoś mniej cenzorskiego DNS-a.  
Nie jest to trudne, ale na każdym systemie i&nbsp;dla każdej przeglądarki robi się to nieco inaczej.

Tutaj ograniczę się jedynie **do zmiany DNS-a w&nbsp;dwóch przeglądarkach -- Brave i&nbsp;Firefox**, w&nbsp;wersjach na komputer.  
W przeglądarkach, bo w&nbsp;razie czego łatwiej odkręcić zmiany niż te na poziomie systemu.  
W tych dwóch konkretnych, bo uważam je za bardziej szanujące prywatność użytkowników niż reszta.

Pozwoliłem sobie przekleić instrukcje z&nbsp;innego wpisu na temat DNS-a. I&nbsp;lekko edytować, żeby nie było żem leniwy:

<details class="bigspace-before">
<summary><strong>Firefox na komputerze</strong></summary>
<p>Żeby oszczędzić sobie klikania, wklejamy w&nbsp;górny pasek:</p>
<div class="black-bg mono">
about:preferences
</div>
<p>A jeśli wolimy klikać, to ikona trzech kresek w&nbsp;górnym prawym rogu i&nbsp;<code class="language-plaintext highlighter-rouge">Ustawienia</code>.</p>
<p>Kiedy już otworzymy opcje, zjeżdżamy na dół, znajdujemy zakładkę <em>Sieć</em>. Klikamy przycisk <code class="language-plaintext highlighter-rouge">Ustawienia...</code> po prawej.</p>
<p>Na dole możemy zaznaczyć opcję <em>DNS poprzez HTTPS</em> i&nbsp;wybrać dostawcę. Domyślnie jest tam Cloudflare, można też wkleić adres IP znanego sobie DNS-a.</p>
</details>

<details class="bigspace-after">
<summary><strong>Brave na komputerze</strong></summary>
<p>Aby przejść prosto do menu, możemy wkleić do paska:</p>
<div class="black-bg mono">
brave://settings/security
</div>
<p>A jeśli wolimy klikać? Najpierw ikona trzech kresek w&nbsp;górnym prawym rogu, potem <code class="language-plaintext highlighter-rouge">Ustawienia</code>, <code class="language-plaintext highlighter-rouge">Prywatność i&nbsp;bezpieczeństwo</code>, <code class="language-plaintext highlighter-rouge">Bezpieczeństwo</code>.</p>
<p>Klikamy opcję <em>Użyj bezpiecznego serwera DNS</em> i&nbsp;wybieramy któregoś z&nbsp;dostępnych dostawców (Cloudflare, OpenDNS, Quad9…).</p>
</details>

A jeśli ktoś korzysta z&nbsp;innej przeglądarki albo chce zmienić domyślny DNS dla całego swojego systemu?  
W takim wypadku polecam bardzo solidny [poradnik ze strony *kwestiabezpieczeństwa.pl*](https://kwestiabezpieczenstwa.pl/dns/).

{% include info.html
type="Heheszki"
text="Cloudflare zdobył bardzo cenny adres IP, [1.1.1.1](https://en.wikipedia.org/wiki/1.1.1.1), i&nbsp;użył go w&nbsp;roli swojego łatwego do zapamiętania adresu DNS. Wywołało to niemały, acz niezamierzony chaos.  
To dlatego, że cztery jedynki często stosowano w&nbsp;kodzie serwerów testowych. Ludzie założyli na wyrost, że nie będzie krył się pod nimi żaden realny serwer. I&nbsp;używali ich jako zapychacza -- taki trochę odpowiednik tekstu *lorem ipsum...* na niekompletnych stronach internetowych.  
Analogia: było to trochę jak rutynowe siadanie na krześle. Niby nie mamy gwarancji, że będzie stało tam gdzie zawsze. Ale przyzwyczailiśmy się, że zatrzyma nam tyłek w&nbsp;drodze ku ziemi. Siadamy, nawet się nie oglądając. A&nbsp;pewnego dnia *bam*, krzesła nie ma.  
Adres 1.1.1.1 zaczął działać, mnóstwo nieplanowanych danych poleciało w&nbsp;stronę Cloudflare'a, było zabawnie :smiling_imp:."
%}

Pamiętajmy, że każdy DNS może mieć własne sympatie i&nbsp;antypatie. Raz będzie dobry do ominięcia cenzury, ale innym razem sam będzie się bawił w&nbsp;cenzora.  
Dlatego nie nastawiajmy się na to, że symboliczne postawienie na cztery jedynki albo ósemki rozwiąże wszystkie nasze problemy.

## Podsumowanie

Internet, ku utrapieniu cenzorów, jest dość niepokorny. Możemy łatwo obejść próby blokowania stron, korzystając z&nbsp;wielu dostępnych nam opcji.

Mam nadzieję, że ten wpis dołoży pewną cegiełkę do internetowej wiedzy i&nbsp;sprawi, że niektórzy zobaczą, co kryje się za odpowiedziami „zmień DNS-a” udzielanymi przez internetowych komentatorów.

Jednocześnie warto pamiętać o&nbsp;drugiej stronie medalu.  
Odchodząc od operatorów krajowych, stajemy się odporni na *stricte* krajową cenzurę. Ale wiele osób robi to, wchodząc na terytorium Google, Cloudflare'a lub wpływowych VPN-ów. Wielkich firm, które już i&nbsp;tak mocno trzymają rękę na pulsie światowego internetu.

Nie widzę prostego rozwiązania tego dylematu. Ale na pewno nie warto żadnej organizacji ufać bezgranicznie.

Poza tym nie zapominajmy, że świat idzie do przodu. Możliwe, że również cenzura się kiedyś unowocześni.  
Modele uczenia maszynowego pozwalają szybko wyszukiwać treści (tekst i&nbsp;obrazki) podobne do już istniejących, nawet jeśli nie są ich dokładną kopią. W&nbsp;ten sposób cenzorzy mogliby sprawniej wyłapywać całe ogólne, niepożądane ruchy społeczne i&nbsp;szybciej tworzyć listy stron zakazanych.

Dlatego tym ważniejsze jest w&nbsp;krajach zagrożonych autorytaryzmem, żeby **jak najwięcej osób poznało uniwersalne sposoby na omijanie cenzury**. Jej skuteczność zależy bowiem od poziomu wiedzy technicznej u&nbsp;ogółu społeczeństwa.

Na tym koniec na dziś. Życzę, żeby żadne liche płotki (w każdym znaczeniu) nie powstrzymały Was przed odwiedzeniem upragnionych stron. Do zobaczenia! :smile:

### Źródło ikonek

* Serwer, laptop, router, strzałka -- Flaticon.

  [Laptop](https://www.flaticon.com/free-icons/computer) i&nbsp;[router](https://www.flaticon.com/free-icons/router) od *vectorsmarket15*, [serwer](https://www.flaticon.com/free-icons/server) od *Smashicons*, [strzałka](https://www.flaticon.com/free-icons/down-arrow) od *Freepik*.

* Kosz na śmieci -- [Emojipedia](https://emojipedia.org/wastebasket/), wersja *JoyPixels*.
* Emota diabełka -- ikony pakietu *jemoji*.
* Miniaturka strony internetowej i&nbsp;kartki papieru -- ikony systemu Linux Mint.

Aranżacja każdorazowo moja własna.
