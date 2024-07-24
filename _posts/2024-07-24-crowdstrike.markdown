---
layout: post
title: "CrowdStrike 2024. Pogrom korporacyjnych Windowsów"
subtitle: "Antywirus miał chronić przed wszystkim. Nie ochronił przed sobą."
description: "Antywirus miał chronić przed wszystkim. Nie ochronił przed sobą."
date:   2024-07-24 12:00:00 +0100
tags: [Afera, Centralizacja, Internet]
firmy: [CrowdStrike, Microsoft]
category: cyfrowy_feudalizm
category_readable: "Cyfrowy&nbsp;feudalizm"
image:
  path: /assets/posts/centralizacja/crowdstrike/crowdstrike-blue-screen-baner.jpg
  width: 1200
  height: 700
  alt: "Przerobiony kadr z anime, na którym rozzłoszczony mężczyzna pokazuje na ścianę telewizorów z niebieskimi ekranami"
---

W zeszły piątek, 19&nbsp;lipca 2024&nbsp;roku, wielu Polaków odliczało ostatnie godziny przed weekendem. W&nbsp;tym samym czasie w&nbsp;USA dzień się dopiero zaczynał.

Miliony firmowych komputerów z&nbsp;systemem Windows -- niczym człowiek otwierający poranną gazetę, żeby zaktualizować swoją wiedzę o&nbsp;świecie -- załadowały nowe aktualizacje. W&nbsp;tym jedną rutynową, od programu antywirusowego firmy CrowdStrike.

Bum.

Miliony ekranów zaświeciły się na niebiesko. W&nbsp;tym błękicie pływały komunikaty o&nbsp;błędach, a&nbsp;czasem pojedyncze smutne buźki. `:(`.  
Słynny **„niebieski ekran śmierci”**. Informacja, że pokazujący go Windows już ma dość, chrzani to wszystko i&nbsp;idzie spać.

{:.figure .bigspace-before}
<img src="/assets/posts/centralizacja/crowdstrike/crowdstrike-blue-screen-baner.jpg" alt="Kadr z&nbsp;anime pokazujący starszego mężczyznę w&nbsp;sklepie, który zwraca się do sprzedawcy, pokazując dłonią ścianę telewizorów. Wyświetla się na nich niebieski ekran śmierci."/>

{:.figcaption}
Źródło: anime *Inuyashiki*. Przeróbki moje.

To przełożyło się zapewne na mniej weekendowego snu u&nbsp;wielu osób. Zwłaszcza tych od spraw technicznych. Trzeba było przywrócić do działania całe legiony wykopyrtniętych urządzeń.  
Ale ostatecznie się udało i, poza bardziej pechowymi przypadkami, problem został rozwiązany. Trwa teraz ocenianie strat i&nbsp;zadawanie pytań.

Dlaczego, choć dotknęło to Windowsów, nie do końca jest wpadką Microsoftu? Dlaczego uderzyło tak nagle i&nbsp;gwałtownie? Dlaczego, mimo wielkiego obszaru rażenia, trafiło głównie w&nbsp;wielkie organizacje, oszczędzając komputery osobiste?

I przede wszystkim -- dlaczego centralizacja i&nbsp;stawianie świata na jednym kruchym filarze nie jest dobrym pomysłem? 

Zapraszam na omówienie sprawy!

{% include info.html
type="Szczera uwaga"
text="Jak zawsze, gdy tykam tematów cyberbezpieczeństwa -- przypominam, że jestem hobbystą, a&nbsp;to luźny wpis popularyzatorski."
%}

## Spis treści

* [Obszar rażenia](#obszar-rażenia)
* [Niebieski ekran śmierci](#niebieski-ekran-śmierci)
* [CrowdStrike](#crowdstrike)
* [Techniczna strona awarii](#techniczna-strona-awarii)
  * [Bomba numer 291](#bomba-numer-291)
  * [Prosta naprawa](#prosta-naprawa)
  * [„Czy próbowałeś wyłączyć i&nbsp;włączyć ponownie?”](#czy-próbowałeś-wyłączyć-iwłączyć-ponownie)
  * [Samozaszyfrowanie](#samozaszyfrowanie)
* [Rola Microsoftu](#rola-microsoftu)
  * [Nieszczelność systemu](#nieszczelność-systemu)
  * [Dążenia do monopolizacji](#dążenia-do-monopolizacji)
* [Konsekwencje](#konsekwencje)

## Obszar rażenia

Awaria dotknęła wszelkich możliwych branż -- w&nbsp;znacznej mierze korporacji międzynarodowych, mających silną obecność w&nbsp;Stanach Zjednoczonych (za moment rozwinę ten wątek). Mocno dostała w&nbsp;kość również Holandia.

Parę migawek z&nbsp;tego całego chaosu:

* Na całym świecie padły systemy lotnisk, masowo odwoływano loty.

  Chaos dodatkowo potęgował fakt, że klienci, którzy zostali na lodzie, udali się do hoteli blisko lotnisk, często sieciówek... Również dotkniętych awarią.

* Oberwały też same linie lotnicze. Z&nbsp;tych znanych w&nbsp;Polsce: [WizzAir i&nbsp;RyanAir](https://warszawa.wyborcza.pl/warszawa/7,54420,31156201,globalna-awaria-systemu-windows-spradzamy-sytuacje-na-warszawskich.html).
* W&nbsp;niektórych motelach [nie działały zamki elektroniczne](https://mastodon.radio/@wa7iut/112813617928668882); radzono ludziom, żeby nie zamykali drzwi. 
* Jeśli wierzyć Wikipedii, błąd wyświetlały popularne, kojarzące mi się z Wielkim Bratem teleekrany reklamowe od Clear Channel.
* Awaria uderzyła też [w drużynę Mercedesa](https://www.racefans.net/2024/07/19/global-crowdstrike-outage-leaves-mercedes-fixing-computers-before-practice/), prowadzącą ćwiczenia przed wyścigami Formuły 1. Którą to zresztą drużynę sponsoruje firma winna awarii.
* Dostało się nawet niektórym [szpitalom i&nbsp;aptekom](https://news.ycombinator.com/item?id=41016987), choć chyba głównie w&nbsp;USA. Ludzie musieli przekładać operacje.
* W&nbsp;Polsce, z&nbsp;innych firm obsługujących ludność cywilną, oberwały m.in.: Lotnisko Chopina, Santander Bank, Carrefour.

{:.bigspace-before}
<img src="/assets/posts/centralizacja/crowdstrike/crowdstrike-bsod-kolaz.jpg" alt="Kolaż złożony z&nbsp;trzech zdjęć niebieskich ekranów w&nbsp;różnych miejscach: za wózkami sklepowymi, na terminalu lotniska i&nbsp;na zapleczu zespołu wyścigowego Mercedesa."/>

{:.figcaption}
Źródła: zdjęcia i&nbsp;komentarze spod postów na Facebooku ([tego](https://www.facebook.com/wtf1official/posts/pfbid0jNQRNKJifzoxxGeJyebXCSuj8MryQoomNLGounB62FXfw7BGH7qPpfgZJYE43TKMl) oraz [tego](https://www.facebook.com/sekurak/posts/pfbid0gtaJDQKY1NkbeWsiCsGq3QJ2VTWguWwDYL4kCPq9ZXLwsCk8tM5teJ6QhYgKZQLMl)). Wikipedia, [zdjęcie](https://commons.wikimedia.org/wiki/File:CrowdStrike_BSOD_at_LGA.jpg) autorstwa *Smishra1*. Aranżacja moja.

I tak dalej, było tego dużo więcej.

Jeśli ktoś chce poznać więcej przykładów, to proponuję [megawątek](https://news.ycombinator.com/item?id=41002195) na forum HN (ponad 3800&nbsp;komentarzy, absolutny rekord), [dyskusję](https://www.reddit.com/r/sysadmin/comments/1e6vq04/many_windows_10_machines_blue_screening_stuck_at/) na Reddicie albo przeszukanie innych portali pod hasłami `crowdstrike`, `"blue screen"`, `bsod` i&nbsp;tak dalej.

Wedle analizy Microsoftu wadliwa aktualizacja uderzyła w&nbsp;kilkadziesiąt milionów komputerów. Możliwe, że to największa taka awaria w historii. Pod względem samego zasięgu, nie mówiąc już o&nbsp;konsekwencjach.

To tyle z&nbsp;podsumowania suchych faktów. A&nbsp;na czym cała awaria polegała i&nbsp;skąd się wzięła?

## Niebieski ekran śmierci

Aby lepiej zrozumieć całą sytuację, musimy (po-)znać pewną cechę wielu współczesnych systemów, w&nbsp;tym również Windowsa.

Bo widzicie -- zazwyczaj **systemy operacyjne mają warstwy** Jak cebula. Lub ogry.

System ma swoją część powierzchowną, widoczną, przeznaczoną dla użytkowników. To różne graficzne interfejsy i&nbsp;kontrolki. Ustawienia, które można łatwo zmieniać. Głośność, język, te sprawy.

Programy, jak popularny Word czy Firefox, sa warstwę wyżej. System jest ich fundamentem i&nbsp;są zwykle zależne od niego oraz ustawień, jakie wprowadzimy.  
Jeśli któryś z&nbsp;nich przestanie działać wskutek błędu, to wyłączy się zapewne tylko on. Bo system pod spodem pozostaje nienaruszony.

Pod powierzchnią systemu znajduje się natomiast głębsza warstwa, do której użytkownicy zwykle nie zaglądają. A&nbsp;nawet nie mogą w&nbsp;niej grzebać bez uprawnień administratora. To **jądro systemu** (ang. *kernel*).

{:.bigspace}
<img src="/assets/posts/centralizacja/crowdstrike/crowdstrike-piramida.jpg" alt="Piramida pokazująca trzy warstwy systemu: programy, przestrzeń użytkownika oraz jądro systemu. Logo Windowsa nachodzi na obie dolne warstwy. W&nbsp;najniższej, jądrze systemu, widać oprócz tego ikonę rysunkowego ptaka."/>

Niebieski ekran, czyli słynny *BSOD* (*Blue Screen of Death*, niebieski ekran śmierci) to po prostu błąd na poziomie jądra. A&nbsp;że warstwy wyższe są zależne od niższych, to wpadka na takim poziomie prowadzi do wyłączenia całego komputera.

{% include info.html
type="Heheszki"
text="Niebieski ekran śmierci towarzyszy Windowsom niemal od zarania dziejów. Jedynie nieznacznie zmienił wygląd, zyskując kod QR i&nbsp;smutną buźkę.  
Kiedyś przydarzył się na żywo na oczach samego szefa Microsoftu, Billa G., podczas [oficjalnej prezentacji Windowsa 98](https://www.youtube.com/watch?v=IW7Rqwwth84) (uwaga: YouTube)."
%}

A czym jest ta ikona wewnątrz jądra? To Falcon Sensor (dosł. „Sokoli Czujnik”) -- antywirus od **niezależnej firmy CrowdStrike**. Część ogólniejszego pakietu usług nazwanych [Falcon](https://www.crowdstrike.com/products/faq/). Dobrowolnie zainstalowany przez użytkowników.

To dlatego słowa „awaria z&nbsp;winy Microsoftu” są nieco naciągane. Microsoft był tu jak deweloper, który pobudował domy. Duże firmy były jak nabywcy tych domów. Zaś Falcon to gość, którego zaprosili i&nbsp;który narozrabiał, grzebiąc przy instalacji [jak Randy z&nbsp;„Chłopaków z&nbsp;baraków”](https://www.youtube.com/watch?v=HNrYJUxdW6M) (YT). 

Można oczywiście mieć zastrzeżenia do tego, że deweloper bardziej wszystkiego nie zabezpieczył (jeszcze do tego wrócę). Albo że ogólnie jest zachłanny. Ale sama destrukcja wynikała z&nbsp;działań gościa.

A dlaczego Falcon gnieździ się w&nbsp;jądrze? Bo obecność w dolnej warstwie daje mu przywileje względem tego co wyżej. Może sprawniej dostrzegać wirusy, a&nbsp;one nie mają jak mu zaszkodzić.

Warto też wiedzieć, że piramidka systemowa buduje się od dołu, przy każdym włączeniu urządzenia.  
**Falcon Sensor uruchamia się na początku**. Więc jeśli przy każdym uruchamianiu będzie się psuł, to system nawet się nie włączy i&nbsp;może wpaść w&nbsp;pętlę śmierci. Reset → niebieski ekran → reset...

Kolejna sprawa do wyjaśnienia -- dlaczego Falcon uderzył w&nbsp;tak wiele firm? Żeby odpowiedzieć na to pytanie, przedstawię jego autorów.

## CrowdStrike

W świecie cyberbezpieczeństwa jest wiele mniejszych, niszowych, mocno wyspecjalizowanych firm. Ale CrowdStrike (będę czasem pisał CS) to coś innego.

Można powiedzieć, że to **megakorpo od cyberbezpieczeństwa**. Trochę jak Microsoft w&nbsp;branży systemów operacyjnych albo Adobe w&nbsp;świecie tworzenia cyfrowych treści.

Ich kolory to czerwień, logo to pikujący sokół.



Są notowani na amerykańskiej giełdzie -- jako [`CRWD`](https://finance.yahoo.com/quote/CRWD/), gdyby ktoś uznał ich za przyszłościową inwestycję :wink:

Na własnej stronie chwalą się tym, że są numerem jeden według [rankingu Gartnera](https://www.crowdstrike.com/wp-content/uploads/2024/03/platform-report-gartner.png) (firmy konsultingowej zajmującej się bardziej technicznymi korpo).

{:.figure .bigspace-before}
<img src="/assets/posts/centralizacja/crowdstrike/crowdstrike-gartner.jpg" alt="Wykres firmy Gartner, pokazujący różne. Najwyższą pozycję zajmuje CrowdStrike" width="600px"/>

{:.figcaption}
Źródło: raport Gartnera z&nbsp;2023 roku.  
Warto zwrócić uwagę, że Microsoft jest tu na drugim miejscu, jako konkurencja CS-a w&nbsp;tym segmencie.

Duże giełdowe korpo w&nbsp;USA? Zatem oczywiście ogłaszają z pompą [inicjatywy „dobroobywatelskie”](https://www.crowdstrike.com/about/environmental-social-governance/), społeczne, ekologiczne itd.  
Czyli zapewne płacą innym wielkim podmiotom, żeby zrobiły wszystko za nich i&nbsp;wydały im zaświadczenia. Przykład z&nbsp;ich własnej strony: ClimeCo od kompensowania emisji.  
Podwykonawca robi swoje. A&nbsp;CS zyskuje podziw mniej sceptycznych obywateli. Oraz punkciki ESG, którymi może skusić więcej funduszy inwestycyjnych.

Choć to wielki gracz, przed tym piątkiem raczej mało było o&nbsp;nich słychać w&nbsp;codziennym życiu. Nie kojarzę na przykład, żeby ktokolwiek robił [memy](https://i1.memy.pl/obrazki/6e141030657_z_radiowezla_leciala_audycja_gdy_nagle_rozleglo_sie_bdziag.jpg) z&nbsp;tekstem „baza wirusów programu CrowdStrike została zaktualizowana”.

{:.post-meta .bigspace-after}
Na wypadek, gdyby kogoś dopadła nostalgia do programu z&nbsp;mema -- warto wiedzieć, że był zamieszany w&nbsp;parę niefajnych [skandali](https://www.safetydetectives.com/blog/avast-scandal-why-we-stopped-recommending-avast-avg/) związanych z&nbsp;gromadzeniem danych użytkowników.

CrowdStrike nie potrzebuje popularności w&nbsp;świecie cywilnym, bo **ich klientami są inne wielkie korpo, chcące odhaczyć wymóg dbania o&nbsp;bezpieczeństwo**. Analogicznie jak sam CS przy odpowiedzialności społecznej.

A zatem: korporacje płacą CrowdStrike'owi, instalują u&nbsp;siebie ich antywirusa. Mają zaliczony audyt. Nie muszą wprowadzać u&nbsp;siebie głębszych zmian, „podwykonawca wszystko ogarnie”.

Jako dodatkową zachętę CrowdStrike oferuje całą kolekcję modnych słów na czasie, w&nbsp;formie wyliczanki:

{:.figure .bigspace-before}
<img src="/assets/posts/centralizacja/crowdstrike/crowdstrike-buzzwords.jpg" alt="Różne słowa, mówiące między innymi o&nbsp;AI i&nbsp;oparciu na danych, jakimi CrowdStrike zachwala swoje rozwiązania."/>

{:.figcaption}
Źródło tej i kolejnej grafiki: [oficjalna strona Falcona](https://www.crowdstrike.com/platform/).

Kadry menedżerskie innych korpo, zbałamucone tymi słówkami i&nbsp;widzące, że ich znajomi z&nbsp;pól golfowych podpinają swoje korposy pod CrowdStrike'a, idą za tłumem. Ptaszysko zdobywa Amerykę, budując gniazda w&nbsp;coraz to nowych wielkich organizacjach:

{:.figure .bigspace}
<img src="/assets/posts/centralizacja/crowdstrike/crowdstrike-klienci.jpg" alt="Garść danych pokazujących, że z&nbsp;usług CrowdStrike korzysta większość dużych firm w&nbsp;różnych sektorach, w&nbsp;tym większość z&nbsp;rankingów Fortune 500&nbsp;oraz Fortune 1000." width="600px"/>

To wyjaśnienie jednej z&nbsp;zagadek. „Dlaczego awaria nie dotknęła zwykłych ludzi?”. Bo raczej nie mają u&nbsp;siebie tego antywirusa. To rzecz z&nbsp;korpoświatka.

## Techniczna strona awarii

Wiele firm miało Sokoła w&nbsp;trzewiach swoich Windowsów, a&nbsp;trzewia te były wrażliwe na wszelkie błędy... Ale jakoś przez lata wszystko się toczyło bez większych skandali. Co sprawiło, że rypło akurat kilka dni temu?

{% include info.html
type="Źródła"
text="Sprawę opisał sam CrowdStrike [na oficjalnej stronie](https://www.crowdstrike.com/blog/falcon-update-for-windows-hosts-technical-details/). Z&nbsp;polskich stron analizę sytuacji przedstawił [Niebezpiecznik](https://niebezpiecznik.pl/post/niebieskie-ekrany-smierci-na-milionach-komputerow-padly-banki-linie-lotnicze-media-i-wiele-innych/). Trochę [rozważań](https://threadreaderapp.com/thread/1814343502886477857.html) przedstawił na Twitterze Patrick Wardle."
%}

### Bomba numer 291

Przyczyną błędu były zmiany w&nbsp;jednym z&nbsp;plików, jakie CrowdStrike określa mianem *channel files*. Z&nbsp;tego co widziałem, to taka ich wewnętrzna nazwa na pliki konfiguracyjne, czyli zawierające ogólne instrukcje wpływające na zachowanie programu.

Widziałem pogłoski, że CrowdStrike mniej rygorystycznie podchodził do takich plików, traktując zmiany w&nbsp;nich jako lżejszy rodzaj aktualizacji; może dlatego błąd się przemknął.

W tym wypadku przyczyną błędu był plik numer 291, mówiący Sokołowi, w&nbsp;jaki sposób powinien monitorować zagrożenia związane z&nbsp;przepływem danych „rurami” (strukturami typu *named pipes*) między różnymi częściami systemu.

W tym pliku, z&nbsp;tego czy innego powodu, znalazły się jakieś dane „niestrawne” dla Falcona, niepasujące do schematów, jakie spodziewał się odczytać. Następował niespodziewany błąd programu.

{% include info.html
type="Ciekawostka"
text="Na Twitterze ktoś zwrócił uwagę na to, że wadliwy plik [był pełen zer](https://x.com/jeremyphoward/status/1814364640127922499). Mocny sygnał, że coś może z&nbsp;nim być nie tak.  
Jak na ironię -- produkt CrowdStrike'a jest wyspecjalizowany w&nbsp;tym, żeby dostrzegać podejrzane wzorce w&nbsp;cudzych danych i&nbsp;programach. Ale nie stosował tej czujności wobec plików związanych ze sobą."
%}

Tu nasuwa się logiczny wniosek -- jeśli to konkretne pliki odpowiadają za zniszczenia, to może da się je jakoś zmienić albo usunąć? Bingo!

### Prosta naprawa

W korporacyjnych realiach szeregowi pracownicy raczej niewiele mogą, gdy ich ekrany pokryją się błękitem. Są na swoich komputerach tylko gośćmi, a&nbsp;dostęp do bebechów ma jedynie administracja.

Ale kiedy grzecznie oddadzą swoje urządzenia, to osoby od spraw technicznych zapewne zabiorą je do swojej okablowanej groty w&nbsp;piwnicy. I&nbsp;zrobią następujące rzeczy, zgodnie z&nbsp;zaleceniami:

1. uruchomią Windowsa [w trybie awaryjnym](https://support.microsoft.com/en-us/topic/kb5042421-crowdstrike-issue-impacting-windows-endpoints-causing-an-0x50-or-0x7e-error-message-on-a-blue-screen-b1c700e0-7317-4e95-aeee-5d67dd35b92f);
2. przejdą do folderu `C:\Windows\System32\drivers\CrowdStrike`;
3. usuną pliki pasujące do wzorca `C-00000291*.sys`.

   Jak rozumiem, gwiazdka oznacza tu jakiś dalszy ciąg cyfr/znaków, który nie ma większego znaczenia.

W ten sposób Falcon nie znajdzie pliku-bomby, a&nbsp;w międzyczasie dostanie aktualizację, która już podsunie mu bezpieczne, niewybuchowe rzeczy.

Niektórzy wspominali również o&nbsp;usunięciu całego folderu `CrowdStrike` albo przynajmniej zmianie jego nazwy. Gdyby usunięcie pliku nie wystarczyło, to zawsze jest to jakaś opcja.

### „Czy próbowałeś wyłączyć i&nbsp;włączyć ponownie?”

Istnieje również sposób partyzancki. Jak radzi sam Microsoft, [może pomóc wytrwałe resetowanie systemu](https://www.msn.com/en-us/money/other/microsofts-outage-tip-for-customers-try-rebooting-your-system-15-times/ar-BB1qhBLN). W&nbsp;połączeniu z&nbsp;odrobiną szczęścia, bo czasem potrzeba nawet kilkunastu prób.

{:.post-meta .bigspace-after}
Zakładam, że nie działałoby to przy zaszyfrowanym dysku, opisanym poniżej.

Jakim cudem to działa? Zapewne, budząc się do życia po włączeniu systemu, ptaszysko CrowdStrike'a zaczyna robić kilka rzeczy naraz. Wysyła do serwerów firmy pytanie o&nbsp;aktualizacje, a&nbsp;jednocześnie zaczyna szperać w&nbsp;plikach.

Zazwyczaj szperanie kończy się pierwsze. Sokół trafia na bombę ukrytą w&nbsp;pliku 291&nbsp;i wybucha razem z&nbsp;całym systemem, nim doleci aktualizacja.  
...Ale może się też zdarzyć, że aktualizacja dotrze pierwsza i&nbsp;podmieni bombę na coś bezpiecznego (albo powie Sokołowi, żeby nie otwierał pliku -- nie zagłębiałem się w&nbsp;dokładne działanie). 

<h3 id='samozaszyfrowanie'>Samoza<span class='corr-del'>oranie</span>szyfrowanie</h3>

Najgorzej mają, paradoksalnie, ludzie bardziej dbający o&nbsp;bezpieczeństwo, jeśli szyfrowali dyski programem BitLocker.

To zabezpieczenie przed sytuacją, gdy ktoś wykrada dysk twardy z&nbsp;firmowego komputera i&nbsp;bez problemów odczytuje go na innym urządzeniu. BitLocker, stanowiący część Windowsa, pozwala zaszyfrować dysk. Nie można go odczytać bez podania hasła podczas uruchamiania kompa.

Zwykle takie bezpieczeństwo to zaleta. Ale tym razem jest utrudnieniem, bo nie ma jak się dostać do folderów i&nbsp;usunąć plików od CS-a. Ptaszysko się włącza, nim dysk zostanie odszyfrowany, i&nbsp;konsekwentnie ubija system.

Na szczęście nie wszystko stracone! Przy ustawianiu szyfrowania BitLocker generuje awaryjny klucz odzyskiwania dostępu (*recovery key*), który należy [gdzieś sobie zapisać](https://support.microsoft.com/en-us/windows/back-up-your-bitlocker-recovery-key-e63607b4-77fb-4ad3-8022-d6dc428fbd0d) na czarną godzinę. Wybawienie w&nbsp;sytuacji takiej jak ta. Chyba że:

* klucz gdzieś zaginął przez te wszystkie lata, gdy nikt z&nbsp;niego nie korzystał,
* albo nikt nie pamięta, gdzie został odłożony, a&nbsp;[jedyna dokumentacja jest na zablokowanym kompie](https://news.ycombinator.com/item?id=41003710),
* albo wszystkie zapasowe klucze są trzymane na osobnym komputerze, który również padł przez CrowdStrike'a,
* albo cały dział informatyczny został [przeniesiony do Indii](https://news.ycombinator.com/item?id=41006884).

Jak widać, awaria niektórym dokopała bardziej niż innym :wink: 

## Rola Microsoftu

Microsoftowi dość mocno się dostało za to, że to jego systemy tak nagle padły.  
Pojawiły się głosy, że to idealny moment, żeby zakończyć dominację Windowsa i&nbsp;zwrócić się ku alternatywie -- **systemowi Linux**.

Jego kod źródłowy jest otwarty, rozwijany publicznie przez tysiące osób, również z&nbsp;dużych firm informatycznych. Istnieje wiele jego wariantów, nie ma skupienia władzy w&nbsp;rękach jednego dyktatora. Niektóre wersje mają interfejsy bardzo podobne do Windowsa.

Czy niechęć do Windowsa i&nbsp;chęć zmiany są uzasadnione?

Wcześniej wspomniałem, że Microsoft jest trochę jak deweloper, który sprzedał dom klientowi, a&nbsp;klient zaprosił kłopotliwego gościa. Na pewno nie zawiesili komputerów z&nbsp;własnej inicjatywy. Ale parę rzeczy jednak bym im zarzucił.

### Nieszczelność systemu 

Po pierwsze: mogli bardziej dopracować i&nbsp;uszczelnić możliwości kontaktu między jądrem a&nbsp;modułami gościnnymi.

Ciągnąc analogię deweloperską -- teraz jest tak, jakby we wszystkich mieszkaniach oddawanych do użytku zostawiali w&nbsp;jakimś miejscu odkrytą instalację elektryczną. A&nbsp;mogli przecież nieco ją zabezpieczyć, dołożyć izolacji. Ograniczyć gościom możliwość niszczycielskich działań.

Jak wskazuje programista Brendan Gregg we wpisie [*No more blue fridays*](https://www.brendangregg.com/blog/2024-07-22/no-more-blue-fridays.html), z&nbsp;pomocą może przyjść nowinka zwana eBPF -- narzędzia przeznaczone do monitorowania tego, co się dzieje wewnątrz jądra. Na systemie Linux już działają, na Windowsach trwają próby wdrożenia.

Analogia: to tak, jakby zamykać Sokoła i&nbsp;podobne mu moduły gościnne w&nbsp;szczelnym laboratorium. Mają do dyspozycji wszelkie mikroskopy, jakie tylko chcą. Ale nie mogą wyjść i&nbsp;wnieść żadnej bomby z&nbsp;zewnątrz.

Niektórzy zwracają też uwagę na to, że już w&nbsp;zamierzchłych czasach dało się przywrócić system do stanu [z czasu ostatniego udanego uruchomienia](https://news.ycombinator.com/item?id=41010044). Microsoft nie musiałby wynajdować niczego od nowa, wystarczyłoby odkurzyć to przydatne rozwiązanie. Byłoby wybawieniem w&nbsp;sytuacjach kryzysowych.

Ale rozumiem też, że sprawa nie jest zero-jedynkowa. Że Falcon, jako antywirus, jednak potrzebuje pewnych przywilejów, których nie potrzebują inni. Żeby potencjalne wirusy nie mogły go wyprzedzić, wyłączyć, usunąć. Okej, niech będzie.

### Dążenia do monopolizacji

Mój drugi, silniejszy zarzut: **Microsoft aktywnie spychał organizacje ku monokulturze Windowsa**.

Oferowali usługi w&nbsp;pakietach -- w&nbsp;taki sposób, że organizacjom wygodniej było brać ekosystem w&nbsp;100% oparty na Windowsie niż różnicować. Do większych podmiotów potrafili wysyłać całe armie sprzedawców i&nbsp;akwizytorów.

Jaskrawym przykładem jest [sprawa Monachium](https://itsfoss.com/munich-linux-failure/). Jego samorząd zwrócił się ku Linuksowi i&nbsp;rozwiązaniom o&nbsp;otwartym kodzie źródłowym, żeby się uniezależnić.

Microsoft potraktował to osobiście. Zaczął oferować niemalże dumpingowe zniżki, publikować analizy pokazujące Windowsa jako oszczędniejszego, lobbować na poziomie politycznym. Ostatecznie do urzędów wrócił Windows.

W piątkowym przypadku błąd wymagał jednoczesnej obecności Windowsa i&nbsp;CrowdStrike'a. To nieco zawęziło obszar rażenia. Ale co by było, gdyby dotknął aktualizacji *samego Windowsa*?  
Skala strat byłaby niewyobrażalna. I&nbsp;sam Microsoft się do tego ryzyka przyczynił, nie znając umiaru w&nbsp;windowsowaniu świata.

Podsumowując: choć MS nie zawinił wprost, moim zdaniem stworzył klimat dla takich sytuacji jak ta. Więc nie jest mi ich żal i&nbsp;popieram naciski na otwarte alternatywy. Zwłaszcza we wszelkich wrażliwszych sektorach.

{% include info.html
type="Ciekawostka"
text="Choć jestem za Linuksem, z&nbsp;kronikarskiego obowiązku muszę przyznać, że *też kiedyś oberwali przez aktualizację CrowdStrike'a*. Miało to miejsce parę miesięcy temu i&nbsp;jakoś nie przebiło się do mediów.  
Zasada była bardzo podobna -- system ma swoje jądro, dostępne dla uprzywilejowanych programów. W&nbsp;to miejsce trafia Falcon. Jego błąd ubija całe jądro, a&nbsp;zatem cały system. Różnica polega na tym, że na Linuksie nie ma niebieskich ekranów śmierci, a&nbsp;błąd na poziomie fundamentów nazywa się **_kernel panic_** („popłoch jądra”).  
Linux ma wiele wariantów (dystrybucji). W&nbsp;tym wypadku pierwszy oberwał [Debian](https://access.redhat.com/solutions/7068083). Potem awaria dotknęła również [systemu Rocky Linux](https://forums.rockylinux.org/t/crowdstrike-freezing-rockylinux-after-9-4-upgrade/14041)."
%}

## Konsekwencje

Afera w&nbsp;większości ma się ku końcowi. Są zapewne firmy, które bardziej oberwały, pogubiły klucze zapasowe itd. Nie zazdroszczę ich pracownikom i&nbsp;ślę wirtualne kondolencje.

Nie zazdroszczę też CrowdStrike'owi. Niebawem pewnie zwrócą się do niego te setki klientów z&nbsp;rankingu Fortune, którymi tak się chwalił. Będą chcieli odzyskać choć część kwot, które stracili w&nbsp;piątek.

Afera pozwoli również dokładniej **poznać infrastrukturę firm**.

Analogia: wiosną można się przejść i&nbsp;zapamiętać sobie, gdzie kwitną drzewa i&nbsp;krzewy. Takie rośliny zwykle mają owoce, zaś o&nbsp;tej porze roku szczególnie się wyróżniają. Po zapamiętaniu miejsca można tam wrócić po kilku miesiącach w&nbsp;nadziei na zbiory.

W podobny sposób wszyscy zainteresowani (w&nbsp;tym hakerzy) mogą sobie teraz zbierać informacje wymieniane na forach i&nbsp;zdjęciach. Tam, gdzie w&nbsp;piątek było niebiesko, tam jest CrowdStrike. Z&nbsp;taką informacją można zrobić różne rzeczy. Choć niełatwo by było zaplanować atak, który wyrządzi większe szkody niż nasz antywirus :wink:

W&nbsp;całej tej sytuacji dostrzegam też bardzo pozytywny aspekt. Oto prosta, zrozumiała dla ludzi katastrofa. **Jasne pokazanie zagrożeń związanych z&nbsp;centralizacją**.

Nie są nowe. Kiedyś sam je [pobieżnie opisałem]({% post_url 2021-04-07-cyfrowy-feudalizm-fakty %}){:.internal}, niemal na początku istnienia bloga, opierając się na jeszcze starszych źródłach. Nowe jest natomiast nastawienie społeczeństwa.

Podczas większych dyskusji na temat centralizacji i&nbsp;cyfrowego uzależnienia prawie zawsze w&nbsp;komentarzach pojawiały się jakieś cwaniaki. Szydzące z&nbsp;realistów i&nbsp;pesymistów: „Ludzkość się rozwija! Chcesz wrócić do jaskiń, luddysto?”.

I czasem wygrywali dyskusję, bo sceptykom brakowało argumentów bliskich ludziom. Wychodzili na panikarzy snujących katastroficzne wizje.

Ta dyskusja się zmienia. Dzięki aferom takim jak ta z&nbsp;Newagiem, bliskich i&nbsp;zrozumiałych, spopularyzowała się świadomość zagrożenia. Mogę bezproblemowo rozmawiać o&nbsp;tych sprawach z&nbsp;większością znajomych.

Teraz powinno być jeszcze lepiej. Po obecnej aferze można usłyszeć słowa przestrogi w&nbsp;popularnych mediach:

> To jest bardzo cenna lekcja dla użytkowników tego oprogramowania, którzy powinni się zastanowić nad pewną heterogenicznością środowisk, bo być może nie zawsze warto polegać na jednym rozwiązaniu

{:.figcaption}
Źródło: [Wywiad](https://tvn24.pl/biznes/tech/globalna-awaria-crowdstrike-to-cenna-lekcja-problemu-nie-dalo-sie-usunac-zdalnie-st8011587) z&nbsp;Michałem Majem z&nbsp;Niebezpiecznika, opublikowany na stronie TVN24.

W sprawie wypowiedział się nawet minister cyfryzacji, tonem niepochlebnym wobec cyfrowej zależności, a&nbsp;swoje zdanie potwierdził w&nbsp;kolejnych wywiadach.

{% include comment.html
author="Ministerstwo Cyfryzacji"
source="twitter"
text="\[sytuacja pokazuje\] również, jak ważna jest różnorodność oprogramowania, z&nbsp;którego korzystamy oraz bycie przygotowanym na różne sytuacje. To także znak, że jeśli cały świat będzie korzystać z&nbsp;usług jednej firmy, każda awaria unieruchomi cały świat"
%}

{:.figcaption}
Źródło: [tweet](https://x.com/CYFRA_GOV_PL/status/1815270166130721136) cytujący wywiad ministra w&nbsp;radiu TOK FM. Skróty moje.

Jak widać, wiatr wieje w&nbsp;dobrą stronę. Przeciwnikom centralizacji pozostaje kuć żelazo, póki gorące. Czytać o&nbsp;niej, rozmawiać ze znajomymi, chwalić otwarte rozwiązania. W&nbsp;razie czego mój blog służy przykładami :wink:

Oddolne działania i&nbsp;budowanie oporu społecznego potrafią wiele zdziałać -- swego czasu rząd Boliwii [walczył z&nbsp;własnymi obywatelami]({% post_url 2023-09-23-bechtel-boliwia-woda %}){:.internal}, broniąc swojego układziku z&nbsp;korporacją Bechtel; ale gdy ludzie byli nieugięci, politycy ustąpili.

Pozostaje mieć nadzieję, że zmiany będą zachodziły nadal, a&nbsp;ludzie decyzyjni zejdą ze stromej, niebezpiecznej ścieżki uzależnienia, do którego prowadzi obecny „rozwój”.

{:.bigspace-before .no-right-border}
> We are the blue screen planet  
And we are numb  
You built this wall  
For years to come  
This sickening mindset  
You must overcome  
Now!

{:.figcaption}
Źródło: Neurotech, [*Blue Screen Planet 1&nbsp;-- Axiom*](https://www.youtube.com/watch?v=yz8LghvHzYw) (YT).

