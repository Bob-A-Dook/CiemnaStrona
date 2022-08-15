---
layout: post
title:  "Internetowa inwigilacja plus 3 – DNS"
subtitle: "Książka telefoniczna internetów."
description: "Książka telefoniczna internetów"
date:   2022-08-14 00:10:00 +0100
tags: [DNS, Internet, Inwigilacja, Podstawy]
firmy: [Cloudflare, Google]
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
image: "dns/dns-baner.jpg"
image-width: 1200
image-height: 700
---

Witam w&nbsp;trzecim wpisie rozszerzającym serię „Internetowa inwigilacja”! Nadal walczymy z&nbsp;podglądaczami usadowionymi na drodze naszej korespondencji, takimi jak firmy telekomunikacyjne.

Gorąco zachęcam, żeby przed tym wpisem zapoznać się z&nbsp;dwoma poprzednimi.  
W pierwszym przedstawiam szyfrowaną [komunikację przez HTTPS]({% post_url 2022-08-13-https %}){:.internal} oraz nietypową analogię z kłódkami i&nbsp;skrzynkami.  
W drugim -- [szyfrowanie metadanych]({% post_url 2022-08-13-metadane-esni-ech %}){:.internal}, czyli m.in. informacji o&nbsp;odwiedzanych stronach, wcześniej publicznie widocznych.

Ten wpis przedstawi sposoby na **szyfrowanie komunikacji z&nbsp;DNS-em -- swoistą książką telefoniczną internetu**.  
Razem z&nbsp;poprzednim wpisem tworzą całość. Samo chowanie metadanych raczej nic by nam nie dało bez uszczelnienia DNS-a. I&nbsp;*vice versa*.

Zapraszam do lektury!

{:.post-meta .bigspace-before}
Wpis skupia się na roli DNS-a w&nbsp;większej prywatnościowej układance i&nbsp;omawia go pobieżnie. Parę ciekawych technikaliów przesunę do osobnego wpisu, o&nbsp;zastosowaniach cenzorskich.  
Poza tym nie zajmuję się zawodowo cyberbezpieczeństwem, nie wierzcie mi na ślepo.

# Spis treści

* [Czym jest DNS](#czym-jest-dns)
* [Po pierwsze: zaufany DNS](#po-pierwsze-zaufany-dns)
* [DoH i&nbsp;DoT, czyli szyfrowanie na ratunek](#doh-idot-czyli-szyfrowanie-na-ratunek)
  * [Jasne i&nbsp;ciemne strony](#jasne-iciemne-strony)
* [Ostatni element układanki](#ostatni-element-układanki)
* [Podsumowanie i&nbsp;przestroga](#podsumowanie-iprzestroga)
* [Bonus: porady prywatnościowe](#bonus-porady-prywatnościowe)
  * [Włączanie DoH i&nbsp;DoT](#włączanie-doh-idot)
  * [Włączanie ECH i&nbsp;kontrola prywatności](#włączanie-ech-ikontrola-prywatności)
  * [Dla właścicieli stron](#dla-właścicieli-stron)

## Czym jest DNS

Wszystkie interakcje przez internet (nawet te najbardziej podstawowe, jak „odwiedzenie stronki”) porównywałem dotąd do wysyłania i&nbsp;odbierania przesyłek przez pocztę -- naszą przeglądarkę.

W naszej pocztowej analogii pomijaliśmy dotąd pewną rzecz.  
Mianowicie: w&nbsp;przypadku korespondencji pocztowej sami musimy zapisać dokładny adres na kopercie. Zaś w&nbsp;przeglądarce wystarczy że klikniemy link albo wpiszemy w&nbsp;pasek nazwę strony.

To tak, jakbyśmy na kopercie listu napisali jedynie „Jan Kowalski”, nie podając adresu. No, może coś bardziej go identyfikującego, jak PESEL. A&nbsp;jednak jakimś cudem to działa. Nasza „poczta” doręcza prośbę o&nbsp;stronkę, a&nbsp;my ją otrzymujemy.  
Jak? Logika dyktuje, że mają gdzieś jakieś źródło, w&nbsp;którym są w&nbsp;stanie znaleźć aktualny adres (*IP*) wskazanej im z&nbsp;nazwy osoby (*stronki*).

Hipoteza: może na naszym komputerze jest wielka baza z&nbsp;informacjami? Łącząca wszystkie możliwe nazwy stron z&nbsp;ich adresami?  
Pudło -- choć faktycznie niektóre pary nazwa-adres są zapisywane na naszym dysku, dla szybszego dostępu w&nbsp;przyszłości.  
Ale nie dla całego światowego internetu. Takie coś zajmowałoby bardzo dużo miejsca; do tego musiałoby być ciągle aktualizowane. W&nbsp;końcu adresy IP stronek mogą się czasem zmieniać.

Zatem nie na naszym urządzeniu. To gdzie?  
Odpowiedź: w&nbsp;pewnym wybranym miejscu w&nbsp;internecie, na tak zwanych **serwerach DNS** (skrót od *Domain Name System*). To tam znajdują się **informacje o&nbsp;tym, jaki adres IP odpowiada danej nazwie strony**.

Trzymając się analogii pocztowej: DNS jest trochę jak podwykonawca dogadany z&nbsp;pocztą. Trzyma u&nbsp;siebie aktualne książki telefoniczne, w&nbsp;których sprawdza na życzenie adresy użytkowników. A&nbsp;także, opcjonalnie, przechowuje niektóre ich rzeczy.

Kiedy w&nbsp;okienku naszej „poczty” prosimy o&nbsp;wysłanie komuś listu (podając tylko jego nazwę), to pracownicy piszą za kulisami do tego człowieka od adresów:  
„Hej, klient chce wysłać prośbę o&nbsp;stronę do *ciemnastrona.com.pl*. Pod jakim to adresem?”.  
Taki list do DNS-a zawiera sam adres domeny -- najogólniejszy możliwy. DNS nie dowiedziałby się zatem, jaki konkretnie wpis chcemy odwiedzić.

{:.bigspace-before}
<div class="black-bg mono">
https://www.ciemnastrona.com.pl<span class="red">/internetowa_inwigilacja/2021/01/11/internetowa-inwigilacja-1-podstawy</span>
</div>

{:.figcaption}
Pełen adres strony, którą chcemy odwiedzić; DNS jest pytany jedynie o&nbsp;nazwę domeny, czyli część nie na czerwono. To wystarczy, bo podstrony i&nbsp;tak będą pod tym samym adresem.

Ale problemem jest to, że ten list domyślnie nie jest w&nbsp;żaden sposób szyfrowany. **Korespondencja z&nbsp;DNS-em jest widoczna dla postronnych**.

{:.bigspace-before}
<img src="/assets/posts/dns/dns-brak-szyfrowania.jpg" alt="Schemat pokazujący komunikację z&nbsp;DNS-em złożony z&nbsp;dwóch linijek, z&nbsp;których każda odpowiada jednemu etapowi komunikacji. Po lewej stronie w&nbsp;obu przypadkach widać ikonę laptopa, po prawej serwera podpisanego DNS, między nimi strzałkę wskazującą kierunek komunikacji."/>

{:.figcaption}
Źródło ikon: Flaticon ([laptop](https://www.flaticon.com/free-icons/computer), [serwer](https://www.flaticon.com/free-icons/server), [strzałka](https://www.flaticon.com/free-icons/down-arrow)), ikony Linuksa, Wikimedia Commons. Aranżacja moja.

Jeśli czytaliście poprzedni wpis, to być może wiecie, ile trzeba było zachodu, żeby ukryć adres domeny widoczny na przesyłkach wysyłanych bezpośrednio do adresata.  
A teraz widzimy, że wszystkie te działania byłyby na nic, gdybyśmy nic nie zrobili z&nbsp;DNS-em -- ujawnialibyśmy dokładnie to samo, tyle że na wcześniejszym etapie. Trzeba załatać tę lukę.

## Po pierwsze: zaufany DNS

DNS bywa stosowany jako narzędzie cenzury. Ale *nie omówię tego w&nbsp;tym wpisie*. Tutaj skupiam się na ochronie prywatności przed zewnętrznymi podglądaczami, stojącymi na drodze korespondencji.

Pod tym względem środki zaradcze są proste. Przede wszystkim **pilnujmy, żeby nasz DNS nie należał do tego samego operatora telekomunikacyjnego, przed którym chcemy się ukryć**. Inaczej wszystko na nic. Sposoby na sprawdzenie i&nbsp;zmianę DNS-a wskazuję pod koniec wpisu.

A jeśli należy do kogoś innego, ale też niezaufanego?  
DNS widzi jedynie odwiedzaną domenę. Zatem gdyby okazał się wścibski i&nbsp;kompletował naszą „teczkę”, to zgromadzi wyłącznie skrócone nazwy. Jak *ciemnastrona.com.pl* (bez linków do konkretnych wpisów), *youtube.com* (bez konkretnych filmów) i&nbsp;tak dalej.

Problemem dla prywatności jest bardziej sytuacja, kiedy przez dłuższy czas mamy jednego i&nbsp;tego samego DNS-a. Na dłuższą metę nazbiera sporo informacji o&nbsp;nas, jak ogólne zainteresowania, godziny aktywności w&nbsp;sieci i&nbsp;tym podobne.

To szczególnie bolesne, jeśli i&nbsp;tak zbiera o&nbsp;nas informacje osobnymi kanałami. Z&nbsp;tego względu proponuję w&nbsp;miarę możliwości **nie korzystać z&nbsp;DNS-a spod adresu *8.8.8.8*, od Google**. Ta firma już i&nbsp;tak za dużo nas wie.

A co z&nbsp;różnymi pośrednikami, wspominanymi w&nbsp;moich wpisach?  
Zarówno sensowne VPN-y, jak i&nbsp;przeglądarka [Tor Browser](https://www.reddit.com/r/TOR/comments/90ohrr/which_dns_server_does_tor_use/) korzystają z&nbsp;własnych serwerów DNS. Więc jeśli ich używamy, to doborem DNS-a nie musimy się aż tak przejmować. Ale nowinki z&nbsp;tego wpisu są skierowane bardziej dla użytkowników bez takiego sprzętu.

## DoH i&nbsp;DoT, czyli szyfrowanie na ratunek

OK, wybraliśmy zaufanego DNS-a. Ale nie chcemy się z&nbsp;nim komunikować na widoku publicznym. Pogłówkujmy.

* Większość zwykłej „korespondencji” między nami a&nbsp;innymi stronami jest szyfrowana; przesyłana w&nbsp;zamkniętych na kłódki, pancernych skrzynkach. Daje nam to prywatność względem podsłuchiwaczy.
* Ta między nami a&nbsp;DNS-em nie jest. Może zostać podsłuchana.

No to może... korespondencję z&nbsp;DNS-em również spróbujmy zaszyfrować?  
Bingo! W&nbsp;tym właśnie celu powstały metody szyfrowania komunikacji z&nbsp;DNS-em: *DNS-over-TLS* oraz *DNS-over-HTTPS*. W&nbsp;skrócie DoT i&nbsp;DoH.

Zaraz przejdziemy do różnic między nimi. Ale wierzcie mi, są bardzo podobne. Zresztą *TLS* to taki fundament *HTTPS*. Polegają dokładnie na tym, na czym polegała opisana dwa wpisy temu szyfrowana komunikacja ze stronkami.

Najpierw wysyłamy DNS-owi prośbę o&nbsp;szyfrowany kontakt. Jeśli ten wspiera taką opcję, to odsyła nam otwartą kłódkę (*klucz publiczny*) z&nbsp;niepodrabialnym hologramem (*certyfikatem*). Odsyłamy mu swoją i&nbsp;od tej pory przesyłamy wiadomości w&nbsp;zamkniętych skrzynkach (*zaszyfrowane*).

Przedstawiam mocną zachętę do korzystania z&nbsp;tych metod :wink:

> Kiedy Google i&nbsp;Mozilla ogłosiły plany wspierania DoH jako rozwiązania przeciw cenzurze, wszyscy spodziewali się głośnego sprzeciwu ze strony reżimów takich jak Chiny, Iran czy Rosja; tymczasem nadszedł on z&nbsp;najmniej spodziewanych miejsc \[Wielka Brytania, USA\].

{:.figcaption}
Źródło: [artykuł](https://www.zdnet.com/article/dns-over-https-causes-more-problems-than-it-solves-experts-say/) ze strony zdnet.com. Tłumaczenie moje.

A wracając do samych metod. Obie za kulisami korzystają z&nbsp;tego samego bajeru, protokołu `TLS`. Dlaczego zatem mają różne nazwy?

Wyobraźmy sobie, że przesyłki mogą opuszczać naszą pocztę różnymi drzwiami, tak zwanymi *portami*. Podobnie jak na prawdziwej poczcie, gdzie możemy mieć osobne drogi wyjścia dla listów i&nbsp;paczek.

Od rzeczy wysyłanych do DNS-a mamy drzwi numer 53&nbsp;(*port 53*). Zaś szyfrowana komunikacja z&nbsp;DNS-em metodą DoT ma osobny *port 853*.  
Najzwyklejsza szyfrowana korespondencja z&nbsp;innymi stronami, poprzez HTTPS, wychodzi z&nbsp;kolei przez drzwi numer 443&nbsp;(*port 443*). Tamtędy wychodzą również „przesyłki” nadawane metodą DoH.

{:.post-meta}
[Rożnice między DoH a&nbsp;DoT](https://www.cloudflare.com/learning/dns/dns-over-tls/) są przystępnie opisane na stronie Cloudflare. Pozwoliłem sobie zaczerpnąć informacji od nich i&nbsp;z paru innych źródeł.

{% include info.html
type="Ciekawostka"
text="Na korzyść mojego porównania portów do drzwi -- *porta* to [po łacińsku](https://en.wiktionary.org/wiki/Port) właśnie *brama* albo *wejście*. Już Rzymianie, przestraszeni podbojami Hannibala, używali zwrotu *Hannibal ante portas*, czyli „Hannibal u&nbsp;bram”.  
Z kolei przodkiem współczesnego portu (morskiego, lotniczego...) jest według tego samego źródła łaciński *portus*.  
A czy słowa *portus* i&nbsp;*porta* są jakoś powiązane? Według losowego tweeta tak -- [mają wspólne źródło](https://nitter.net/Walkyrjenny/status/1480901226296483842#m) od słowa oznaczającego z&nbsp;grubsza *przekraczać*.  
Etymologia to fajna sprawa :smile:"
%}

# Jasne i&nbsp;ciemne strony

Wiemy już, czym DoH i&nbsp;DoT się różnią -- „wychodzą różnymi drzwiami”. Co to oznacza w&nbsp;praktyce?

DoT ma osobny port, więc się wyróżnia; gdyby ktoś chciał nam zablokować tę formę komunikacji, mógłby po prostu zapieczętować drzwi numer 853. Byłoby to łatwe i&nbsp;raczej pozbawione efektów ubocznych.

W przypadku DoH-a jest inaczej; szyfrowane listy do DNS-a wychodzą tymi samymi „drzwiami” co nasza najbardziej typowa korespondencja.  
Nie ma zatem łatwej opcji ich zablokowania albo przechwytywania przez czyhanie przy konkretnych drzwiach.

Z tego względu DoH nie jest lubiany przez administratorów sieci, którzy chcieliby mieć oko na to, na jakie witryny zaglądamy.

1. Zwykłą komunikację z&nbsp;DNS-em by odczytali.
2. DoT-a by nam po prostu zablokowali, żebyśmy musieli wrócić do punktu&nbsp;1.
3. A&nbsp;w obliczu DoH-a musieliby się namęczyć.

Różne stronki, zwykle piszące z&nbsp;punktu widzenia firmowych działów bezpieczeństwa, przedstawiają właściwości DoH-a jako wadę. Mnie tam los adminów ani ziębi, ani grzeje, więc nie podzielam obaw. Im mniej ktoś ma nade mną kontroli, tym lepiej :wink:

Jako użytkownik bardziej obawiam się wykorzystania tej właściwości do obejścia blokad antyreklamowych.  
Bo widzicie... istnieją skuteczne, choć nieco bardziej wymagające, metody blokowania reklam przez DNS. Takie jak [PiHole](https://www.reddit.com/r/pihole/comments/7qbg57/what_are_the_benefits_of_using_pihole_instead_of/).  
Ich działanie opiera się właśnie na przechwytywaniu i&nbsp;olewaniu próśb wysyłanych pod adresy z&nbsp;czarnej listy. Mogą działać na poziomie całej domowej sieci, chroniąc nas np. przed reklamami pobieranymi przez *Smart TV*.

Jeśli aplikacje mają możliwość komunikacji przez DoH i&nbsp;DoT, to mogą to wykorzystać, żeby ukryć przed naszym PiHole'em, że właśnie proszą nielubianą przez nas stronkę o&nbsp;zaserwowanie nam reklam.

DoT-a byśmy im jeszcze mogli zablokować; DoH-a nie za bardzo albo z&nbsp;trudem. Możemy wypić smutne piwko pojednania z&nbsp;administratorami sieci, których wcześniej przechytrzyliśmy.

Mój przykład nie jest zresztą teorią i&nbsp;już znaleziono w&nbsp;naturalnym środowisku [apki przemycające reklamy przez DoH](https://www.reddit.com/r/pihole/comments/l69exz/ios_14_apps_bypassing_pihole_using_encrypted_dns/). No ale cóż, mamy ciekawe czasy.

## Ostatni element układanki

To dla tych, którzy czytali dwa poprzednie wpisy. DNS jest bowiem nie tylko luką do załatania, miejscem ujawnienia informacji. Jest również niezbędnym krokiem do zaszyfrowania metadanych (przez ESNI/ECH).

To z&nbsp;niego możemy odebrać „kłódkę” potrzebną do zamknięcia skrzynki z&nbsp;metadanymi. W&nbsp;końcu, poza samymi informacjami o adresach, może zawierać dowolne inne rzeczy. No i&nbsp;tak czy siak się z&nbsp;nim kontaktujemy, nim odwiedzimy nową stronkę.

Połączymy teraz DoT/DoH ze wspomnianymi wcześniej ESNI/ECH oraz HTTPS-em. I&nbsp;otrzymamy prywatność.

Działa tu zasada „wszystko albo nic”. Nasza interakcja musi spełniać szereg warunków, żebyśmy byli skutecznie chronieni przed wzrokiem telekomów.

1. Mamy zaufanego DNS-a poza kontrolą firmy telekomunikacyjnej.
2. Łączymy się z&nbsp;nim w&nbsp;sposób szyfrowany (DoH/DoT).
3. Pozyskujemy z&nbsp;niego kłódkę do zamknięcia metadanych metodą ESNI/ECH.
4. Piszemy na adres IP, pod którym znajduje się wiele różnych stronek.  
   Dane wskazujące konkretną spośród&nbsp;nich zamykamy na wspomnianą kłódkę.
5. Serwer, z&nbsp;którym piszemy, musi wspierać ESNI/ECH. Odczytuje zaszyfrowany adres i&nbsp;przekazuje adresatowi naszą przesyłkę.
6. Nasz adresat musi wspierać HTTPS, żeby komunikacja z&nbsp;nim była szyfrowana (ale w&nbsp;obecnych czasach to norma).
   

Kiedy już sobie wyjaśniliśmy brakujący element układanki i&nbsp;wiemy, jaka jest rola DNS-a w&nbsp;całym procesie, możemy rozbudować schemat z&nbsp;poprzedniego wpisu.  
Kolorowe linie odgradzają „terytoria” różnych podmiotów, a&nbsp;każda strzałka to jedna interakcja. Czytamy je od góry do dołu:

<img src="/assets/posts/dns/doh-esni-ech-schemat.jpg" alt="Duży schemat pokazujący interakcje podczas szyfrowanej komunikacji. Po lewej stronie widać ikonę laptopa, po prawej stronie ikony serwerów. Część środkowa, w&nbsp;której znajdują się strzałki symbolizujące interakcje, jest otoczona niebieską obwódką. Widać nad nią ikonę wszystkowidzącego oka z&nbsp;dorysowaną łzą, podpisaną 'ISP'." />

{:.figcaption}
Z tego co rozumiem, DNS nie musi należeć to tej samej firmy, która zapewnia hosting naszemu adresatowi. Ale rozwiązanie promuje głównie Cloudflare, więc odniosłem to do ich sytuacji.

Wścibskie firmy telekomunikacyjne widzą od teraz tylko dwie rzeczy:

* Adres IP serwera DNS. Ale to żadna tajemnica.
* Adres IP odwiedzanej strony. Który nie jest problemem, jeśli pod tym samym adresem „mieszka” wiele różnych stron.

Cała reszta komunikacji -- nawet najogólniejsze metadane -- jest zaszyfrowana. Jesteśmy chronieni przed niepożądanymi oczami.

...Oczywiście nikt nie wyklucza, że po tych wszystkich przeprawach nawiążemy bezpieczną komunikację z&nbsp;jakąś stronką, a&nbsp;ona sama zacznie zbierać o&nbsp;nas dane.  
Wszystkie rzeczy z&nbsp;pierwszych dwunastu wpisów „Internetowej inwigilacji” cały czas mogą się wydarzyć. Życie :wink:

Jeśli kogoś interesuje ten temat, to polecam bardziej obszerne [omówienie spraw wokół DNS-a](https://www.privacyguides.org/basics/dns/) ze stronki Privacy Guides. A&nbsp;także wpisy na blogu Cloudflare.

## Podsumowanie i&nbsp;przestroga

Tym wpisem domykam mini-trylogię o&nbsp;ukrywaniu się przed podglądaczami, takimi jak dostawcy internetu. Podczas tej podróży poznaliśmy kilka groźnie brzmiących akronimów (HTTPS + DoT/DoH + TLS 1.3 + ESNI/ECH), które, mam nadzieję, objaśniłem w&nbsp;przystępny sposób.

Kiedy wszystkie naraz są aktywne -- zarówno u&nbsp;nas, jak też u&nbsp;odwiedzanej stronki -- zyskujemy prywatność. Domyślnie, w&nbsp;tle, bez korzystania z&nbsp;VPN-ów i&nbsp;pośredników. A&nbsp;jest szansa, że te rozwiązania się upowszechnią, jak kiedyś HTTPS.

Ale oprócz blasków są też cienie.  
Powtórzę jeszcze raz, że to dość nowe wynalazki. **Wiele serwerów DNS nie wspiera jeszcze DoH i&nbsp;DoT**. Nie mówiąc o&nbsp;takich nowinkach jak ESNI/ECH.  
Po drugie: pionierami w&nbsp;kwestii wdrożeń jest na razie kilka organizacji, którym się chciało to ustawić. To na przykład Cloudflare czy Google.

Google ze śledzenia jest znany i&nbsp;już nieraz o&nbsp;nim pisałem. Jego DNS mógłby odczytywać, jakie strony odwiedzamy -- nawet jeśli nie korzystamy z&nbsp;ich przeglądarki ani usług. A&nbsp;fakt, że komunikujemy się przez DoH/DoT, mógłby wręcz uczynić nas priorytetowym celem obserwacji.
 
Cloudflare jest nieco bardziej wiarygodny (zarabiają na infrastrukturze, a&nbsp;nie reklamach), ale to wciąż amerykański gigant, od którego i&nbsp;tak światowy internet jest niepokojąco zależny. Oddawanie wrażliwych kwestii garstce wielkich graczy może budzić niepokój.

Ale, jeśli mamy obawy, możemy się pocieszyć tym, że same protokoły są otwarte i&nbsp;inni również mogą je wdrożyć.  
Przykładem mniejszego gracza [wspierającego DoT/DoH](https://nitter.net/njal_la/status/1521462683387764736#m) jest Njalla, dość charakterna szwedzka firma oferująca hosting (i mająca bardzo... wolnościowe podejście do kwestii cyfrowych).

W każdym razie, nawet gdybyśmy włączyli wszystkie zabezpieczenia, nie spoczywajmy na laurach. Szczególnie zdeterminowanym podglądaczom pozostaje jeszcze analiza naszego ruchu sieciowego (*traffic analysis*). Jeszcze o&nbsp;niej wspomnę.  
A teraz część dla chętnych, którzy chcą wypróbować opisane bajery.

## Bonus: porady prywatnościowe

# O&nbsp;hierarchii słów parę

DNS, z&nbsp;jakiego korzysta nasze urządzenie, może być ustawiany na kilku poziomach.

* Proponowany przez hotspota.

  Domyślny. Kiedy się łączymy z&nbsp;jakimś hotspotem, to zwykle proponuje nam ustawionego u&nbsp;siebie DNS-a. Na przykład jeden hotspot na dworcu potrafi domyślnie używać DNS-a od Google, inny od Cloudflare'a itp.  
Zarówno na Windowsie, jak i&nbsp;na Linuksie możemy go sprawdzić, klikając ikonę połączenia internetowego na dolnym pasku i&nbsp;wybierając opcję w stylu `Informacje o połączeniu`.

* Na poziomie systemu.

  Jeśli takie coś ustawimy, *to ma wyższy priorytet niż DNS proponowany przez hotspota*.

* Na poziomie konkretnego programu/aplikacji.

  Ma najwyższy priorytet, ale obowiązuje tylko dla konkretnego programu.

Poza tym być może da się wymusić, żeby wszystkie programy korzystały z&nbsp;konkretnego DNS-a. Ale to już poza zakresem tego wpisu.

Na razie zapamiętajmy tyle, że **kiedy ręcznie ustawimy DNS-a w&nbsp;naszej przeglądarce, to zapewne zawsze będzie z&nbsp;niego korzystała**. Ale inne aplikacje nie będą. Przykładowe włączenie DoH w&nbsp;Firefoksie, zgodnie z&nbsp;poniższymi poradami, nie da nam szyfrowanego DNS-a w&nbsp;pozostałych programach.

# Włączanie DoH i&nbsp;DoT

Pokażę tylko na przykładzie Firefoksa i&nbsp;Brave'a, do tego tylko ten pierwszy będzie z&nbsp;obrazkiem. To dlatego, że na tę chwilę jest jedyną znaną mi przeglądarką, która wspiera zarówno DoH, jak i&nbsp;ECH.

Kliknijcie w&nbsp;interesujące Was szczegóły, żeby je rozwinąć.

<details class="bigspace-before">
<summary><strong>Firefox na komputerze</strong></summary>
<p>Żeby oszczędzić sobie klikania, wklejamy w&nbsp;pasek następujący tekst:</p>
<div class="black-bg mono">
about:preferences
</div>
<p>A jeśli wolimy klikać, to ikona trzech kresek w&nbsp;górnym prawym rogu i&nbsp;<code class="language-plaintext highlighter-rouge">Ustawienia</code>.</p>
<p>Kiedy już otworzymy opcje, zjeżdżamy na dół, znajdując tam zakładkę <em>Sieć</em>. Klikamy przycisk <code class="language-plaintext highlighter-rouge">Ustawienia...</code> obok niej.</p>
<p>Na dole możemy zaznaczyć opcję <em>DNS poprzez HTTPS</em> i&nbsp;wybrać dostawcę. Domyślnie jest Cloudflare, ale możemy tam również wkleić znany adres IP własnego DNS-a.</p>
<p><img src="/assets/posts/dns/firefox-doh.jpg" alt="Zrzuty ekranu pokazujące włączanie krok po kroku DNS-over-HTTPS na Firefoksie"></p>
</details>

<details class="bigspace-after">
<summary><strong>Brave na komputerze</strong></summary>
<p>Żeby oszczędzić sobie klikania przez opcje, możemy wkleić do paska:</p>
<div class="black-bg mono">
brave://settings/security
</div>
<p>A jeśli wolicie klikać, to najpierw ikona trzech kresek w&nbsp;górnym prawym rogu, potem <code class="language-plaintext highlighter-rouge">Ustawienia</code>, <code class="language-plaintext highlighter-rouge">Prywatność i&nbsp;bezpieczeństwo</code>, <code class="language-plaintext highlighter-rouge">Bezpieczeństwo</code>.</p>
<p>Można tam włączyć opcję <em>Użyj bezpiecznego serwera DNS</em> i&nbsp;wybrać jednego z&nbsp;dostępnych dostawców (Cloudflare, OpenDNS, Quad9…). Od razu po włączeniu proponuję przejść się po paru stronach i&nbsp;upewnić, czy wszystko działa.</p>
</details>

Ogólna uwaga: jeśli chodzi o&nbsp;grzebanie w&nbsp;ustawieniach, jestem fanem podejścia lekarskiego. „Po pierwsze -- nie szkodzić”. Dlatego zapamiętajmy sobie, co zmieniamy, żeby w&nbsp;razie potrzeby móc to potem odkręcić :wink:

# Włączanie ECH i&nbsp;kontrola prywatności

Kiedy mamy już DNS-a przez DoH lub DoT, do pełnego zaszyfrowania pozostaje jeden krok. **Pokażę go to tylko dla Firefoksa**, inne chyba jeszcze nie wspierają ECH. Być może zadziała też na opartych na nim przeglądarkach.

<details class="bigspace">
<summary><strong>Firefox na komputerze</strong></summary>
<p>Wpisujemy w&nbsp;pasku górnym <code class="language-plaintext highlighter-rouge">about:config</code>, potwierdzamy że akceptujemy ryzyko. W&nbsp;pasku wyszukiwania zaczynamy wpisywać <em>echc</em>, a&nbsp;powinna wyskoczyć nam opcja <code class="language-plaintext highlighter-rouge">network.dns.echconfig.enabled</code>. Klikamy po prawej stronie, żeby zmieniła wartość na <em>true</em>.</p>
<p>Opcja pod nią jest bardzo praktyczna, bowiem sprawia, że w&nbsp;razie niepowodzenia komunikacji przez ECH Firefox wróci do metody klasycznej. W&nbsp;obecnych czasach, gdy ECH raczkuje, takie zdarzenie może być częste.</p>
<p>Jest tam również opcja dotycząca HTTP3. Póki co jej nie ruszałem.</p>
<p><img src="/assets/posts/dns/firefox-ech-config.jpg" alt="Zrzuty ekranu pokazujące krok po kroku, jakie opcje pozwalają włączyć Encrypted Client Hello na Firefoksie."></p>
</details>

Kiedy już wszystko powłączamy, możemy sprawdzić czy nam działa [przez stronę Cloudflare](https://www.cloudflare.com/ssl/encrypted-sni/). Klikamy przycisk `Check My Browser`.

Natomiast uprzedzę -- stronka dotyczy sprawdzania ESNI. A&nbsp;ten, jak pisałem w&nbsp;poprzednim wpisie, jest zastępowany przez ECH i&nbsp;nie da się go włączyć w&nbsp;nowych wersjach Firefoksa.  
[Porady](https://blog.cloudflare.com/encrypt-that-sni-firefox-edition/) dotyczące jego włączania są nieaktualne.

Patrząc po [wątku na forum](https://community.cloudflare.com/t/ech-replacing-esni-fails-the-browsing-experience-security-check/240056), to zamierzone. Nastawmy się po prostu na to, że zdobędziemy w&nbsp;tym teście maksymalnie 3&nbsp;na 4&nbsp;punkty. Jeśli kiedyś pojawi się wersja dla ECH, to uaktualnię wpis.

{:.bigspace-before .figure}
<img src="/assets/posts/dns/cloudflare-esni-check.jpg" alt="Wyniki testu Cloudflare, widać wypełnione trzy z&nbsp;czterech rzeczy. Bezpieczny DNS, DNSSEC, TLS wersja 1.3. Jedyna niespełniona rzecz to Bezpieczny adres SNI."/>

{:.figcaption}
Pierwsza pozycja to DoT/DoH, DNSSEC jest poza tematem tego wpisu, potem prywatniejsza wersja TLS, na końcu ESNI.

Po włączeniu zestawu DoH + ECH powinniśmy spełniać wszystkie warunki wypisane wcześniej w&nbsp;tym wpisie. Na wybranych stronach (głównie od Cloudflare; ale hostują ich sporo) zyskujemy ochronę przed wzrokiem podglądaczy, bez konieczności używania VPN-a.

Tym niemniej, jeśli nas to nie przekonuje i&nbsp;sami nie wiemy komu ufać... zawsze możemy dmuchać na zimne i&nbsp;szukać wrażliwych (ale legalnych!) rzeczy anonimowo, przez publiczny komputer, bez logowania na żadne konto. W&nbsp;bibliotece albo podobnym miejscu.

# Dla właścicieli stron

{:.post-meta .bigspace-after}
Oczywiście tylko do tych, którzy próbują prowadzić legalne/etyczne stronki w&nbsp;odległych i&nbsp;niesprecyzowanych krajach autorytarnych :wink:

Jeśli macie smykałkę techniczną, możecie wczytać się w&nbsp;temat i&nbsp;sprawdzić, czy platforma zapewniająca hosting Waszej stronce wspiera ESNI/ECH. Albo, jeśli hostujecie stronę całkiem sami i&nbsp;jesteście hardkorami, skonfigurować to samodzielnie. Bylibyście pionierami.

Natomiast jeśli nie macie takiej możliwości -- albo uważacie, że ESNI i&nbsp;inne bajery nie pomogą Waszym gościom, bo na przykład i&nbsp;tak wpadną przez domyślnego DNS-a -- możecie nieco ich ochronić w&nbsp;inny sposób. Zapewniając im wiarygodną wymówkę na wypadek, gdyby ich telekom sobie zapisywał, jakie domeny odwiedzili.

Skoro firma telekomunikacyjna widzi tylko sam *trzon*, nazwę domeny... to może by tak sprawić, żeby nazwa nie przyciągała uwagi? Nie dawać czegoś takiego:

{:.bigspace}
<div class="black-bg mono">https://zla-strona.pl</div>

...tylko korzystać z&nbsp;nazwy niewinnej, a&nbsp;prawdziwy cel strony spychać do jej podstronek:

{:.bigspace-before}
<div class="black-bg mono">https://dobra-strona.pl<span class="red">/niedobra-podstrona</span></div>

{:.figcaption}
Pamiętajmy, że podglądacze nie zobaczą tego, co na czerwono.

Do tego można wrzucić trochę całkowicie niewinnych podstronek (dbając o&nbsp;to, żeby rozmiar tych podstron oraz liczba osadzonych w&nbsp;nich elementów pokrywały się z&nbsp;grzecznymi; to przez aspekt analizy ruchu).

W ten sposób nawet gdyby jakiś dyktator zanotował, że użytkownicy odwiedzili Waszą legalną/etyczną domenę, to nie będzie miał dowodów, że było przeglądane coś, co by mu się nie spodobało.

A jeśli Wasza strona już ma kontrowersyjną reputację i&nbsp;taki dupochron to za mało?
W takim wypadku możecie skopiować swoje treści i&nbsp;wrzucić je na jakąś wielką platformę spoza czarnej listy autokratów.  
Wścibski telekom widziałby jedynie, że ktoś wszedł na przykład na *reddit.com*, ale nie widziałby, że spośród milionów wątków poczytał ten Wasz.

