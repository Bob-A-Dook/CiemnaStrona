---
layout: post
title: "Zamknij wroga w symulacji. Prywatność maszyn wirtualnych"
subtitle: "Jeden system zdradza zbyt wiele? To dorzućmy drugi."
description: "Jeden system zdradza zbyt wiele? To dorzućmy drugi."
date:   2025-02-10 21:00:00 +0100
tags: [Inwigilacja, Podstawy, Porady]
firmy: [Proctorio]
image:
  path: /assets/posts/inwigilacja/maszyny-wirtualne/maszyny-wirtualne-baner.jpg
  width: 1200
  height: 700
  alt: "Kadr przedzielony murem, pod którym widnieje logo VirtualBoxa. Po jednej stronie siedzą ludzie patrzący na cienie na ścianie, po przeciwnej animatorzy z sylwetkami na patykach"
---

W internecie coraz częściej można znaleźć na różnorodnych forach i&nbsp;grupkach pytania o&nbsp;to, jak chronić swoją cyfrową prywatność. Wśród odpowiedzi czasem przewija się krótkie: [„używaj maszyny wirtualnej”](https://www.reddit.com/r/privacy/search/?q=%22use+a+virtual+machine%22&type=comments&sort=new).

Rada jak najbardziej ma sens. Problem w&nbsp;tym, że jest ciut enigmatyczna, a&nbsp;dla ludzi spoza świata komputerowego -- może nawet kompletnie niezrozumiała.  
Dlatego trochę ją odczaruję i&nbsp;pokażę krótko, o&nbsp;co z&nbsp;tymi maszynami chodzi. Opiszę ogólniki, kładąc fundament pod ewentualne przyszłe wpisy na temat VirtualBoxa, systemu Qubes itd.

Zobaczymy, że czasem od celowego ukrywania skuteczniejsze jest odsłonięcie przed podglądaczami swojej rzeczywistości. Wiarygodnej, zaspokajającej ich ciekawość. Tyle że nieprawdziwej.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/maszyny-wirtualne/maszyny-wirtualne-baner.jpg" alt="Kadr przedzielony murem, pod którym widnieje logo VirtualBoxa. Po jednej stronie siedzą ludzie patrzący na cienie na ścianie, po przeciwnej animatorzy z&nbsp;sylwetkami na patykach"/>

{:.figcaption}
Źródło: [ilustracja jaskini Platona](https://commons.wikimedia.org/wiki/File:An_Illustration_of_The_Allegory_of_the_Cave,_from_Plato%E2%80%99s_Republic.jpg) z&nbsp;Wikimedia Commons, ikona programu VirtualBox. Przeróbki moje.

## Spis treści

* [Czym są maszyny wirtualne](#czym-są maszyny-wirtualne)
* [Wycinek szerokiego świata](#wycinek-szerokiego-świata)
* [Prywatność dzięki izolacji](#prywatność-dzięki-izolacji)
  * [Ochrona przed czytaniem naszych plików](#ochrona-przed-czytaniem-naszych-plików)
  * [Ochrona przed czytaniem plików systemowych](#ochrona-przed-czytaniem-plików-systemowych)
  * [Ochrona przed profilowaniem przez czcionki](#ochrona-przed-profilowaniem-przez-czcionki)
* [Przechytrzenie głęboko zagnieżdżonych programów](#przechytrzenie-głęboko-zagnieżdżonych-programów)
* [Ograniczenia maszyn wirtualnych](#ograniczenia-maszyn-wirtualnych)
  * [Możliwość wykrycia](#możliwość-wykrycia)
  * [Łączenie informacji z&nbsp;różnych programów](#łączenie-informacji-zróżnych-programów)
  * [Złośliwy hardware](#złośliwy-hardware)
* [Przykład z&nbsp;życia: Proctorio](#przykład-zżycia-proctorio)
* [Podsumowanie](#podsumowanie)

<details class="framed">
<summary><strong>Jeśli komuś nie chce się czytać całości</strong></summary>
{% include info.html
type="Streszczenie"
text="Maszyny wirtualne w&nbsp;kontekście prywatności są jak **pokazanie podglądaczom wiarygodnej fasady, która nijak nie odpowiada naszemu prawdziwego życiu**.  
W najczęstszym przypadku są trochę jak [tryb prywatny](/2024/09/09/tryb-prywatny-incognito){:.internal} w&nbsp;przeglądarce. Chowają przed uruchomionymi w&nbsp;sobie programami pliki z&nbsp;głównego systemu oraz informacje o&nbsp;nim. Zamiast tego pokazują czysty system jak po instalacji."
trailer="<p class='bigspace-before'>
Drugą supermocą maszyn wirtualnych jest oszukiwanie inwazyjnych programów wymagających dostępu do głębszej warstwy systemu. Owszem, dają im dostęp do fundamentów... Ale nie <i>tych prawdziwych</i>, gdzie tkwią nasze wrażliwe informacje.<br/>
Programy trzymające się litery prawa nie wyrwą się z&nbsp;maszyn wirtualnych. Mogą natomiast rozpoznać, że w&nbsp;nich są, i&nbsp;odmówić działania. Poza tym maszyny wirtualne nie chronią przed profilowaniem czy weryfikacją na poziomie fizycznego sprzętu.</p>"
%}
</details>

## Czym są maszyny wirtualne

Maszyna wirtualna to po angielsku *virtual machine*, w&nbsp;skrócie VM. Dla wygody będę czasem skracał do „VM&#8209;ka”.

Skąd nazwa? W&nbsp;informatyce „maszyna” oznacza ogólnie coś, co przyjmuje i&nbsp;wykonuje instrukcje w&nbsp;określonym formacie. „Wirtualna” -- czyli jak taka nakładka na coś realnego. Nadbudówka.

Opis brzmi mgliście i&nbsp;ogólnikowo? Trochę tak. Ale ogólność jest uzasadniona, bo samo pojęcie maszyn wirtualnych może obejmować bardzo wiele rzeczy (niektóre krótko omawiam niżej, w&nbsp;rozwijanych ciekawostkach).  
W tym wpisie będzie o&nbsp;tyle łatwo, że odnoszę się tylko do jednej ich postaci -- **systemu operacyjnego uruchomionego wewnątrz innego systemu**.

Jak wygląda takie coś w&nbsp;praktyce, z&nbsp;punktu widzenia użytkowników?  
Wyobraźmy sobie, że mamy zwykłe otwarte okna z&nbsp;różnymi programami. Jak Firefox, Notatnik czy LibreOffice. Można je przesuwać po ekranie, minimalizować itd. Jedno z&nbsp;tych okien odpowiada programowi od wirtualizacji, nazywanemu po angielsku *hypervisor*.

Przykładem takiego programu jest VirtualBox. Gdy jest uruchomiony, to w&nbsp;jego oknie widzimy -- jak na monitorze -- wnętrze załadowanego, pełnoprawnego systemu operacyjnego: pulpit, ustawienia, okna itd.

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/maszyny-wirtualne/ubuntu-na-windowsie.jpg" alt="Okno systemu Ubuntu uruchomione wewnątrz systemu Windows"/>

{:.figcaption}
Jeden z&nbsp;wielu wariantów systemu Linux w&nbsp;programie VirtualBox na Windowsie. Źródło: [ten film](https://www.youtube.com/watch?v=x5MhydijWmc).  
Gdyby ktoś chciał spróbować wirtualki z&nbsp;przyjaznym systemem Linux Mint, to przystępny wideoporadnik po polsku można znaleźć [choćby tutaj](https://www.youtube.com/watch?v=XO7bs1BBbjA) (oba linki: YouTube). 

Napisałem wyżej o&nbsp;systemie otwartym _wewnątrz_ systemu, bo to intuicyjnie pasuje do zagnieżdżonych w&nbsp;sobie okienek. Ale żeby łatwiej wyobrazić sobie zalety i&nbsp;ograniczenia dowolnej VM&#8209;ki, zachęcam do myślenia o&nbsp;niej również jak o&nbsp;systemie opartym **_na_** innym systemie.

Przedstawiam przeróbkę typowej [piramidki](/assets/posts/apki/apki-piramida.jpg){:.internal}, której często używam w&nbsp;różnych wpisach. W&nbsp;przypadku VM-ek jedyna różnica polega na tym, że na warstwie programów stawiamy kolejny system oraz jego własne rzeczy. Piramida rośnie w&nbsp;górę.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/maszyny-wirtualne/maszyna_wirtualna_piramida.jpg" alt="Schemat pokazujący warstwy systemu. Widać, że na fizycznym sprzęcie stoi system operacyjny Windows, na nim program Virtualbox, na nim system Linux, a&nbsp;na nim program Firefox."/>

{:.figcaption}
Źródła: procesor z&nbsp;serwisu Flaticon, ikony systemów Windows i&nbsp;Linux Mint oraz programów Firefox i&nbsp;VirtualBox. Przeróbki moje.


Na samym dole mamy fizyczny sprzęt (*hardware*) oraz sterujące nim programy (*firmware*). Wyżej główny system (ang. *host system*; dosłownie system-gospodarz). Na tym systemie otwarte programy, z&nbsp;których jeden to VirtualBox. Na nim oparty inny system (ang. *guest system*, czyli system-gość). A&nbsp;na tym systemie -- jego własne programy.

{% include info.html
type="Ciekawostka"
text="Gdyby ktoś chciał, dałoby się zrobić „VM&#8209;cepcję” i&nbsp;uruchamiać maszyny wirtualne wewnątrz maszyn wirtualnych. Wieża rosłaby w&nbsp;górę, ale -- tak jak w&nbsp;prawdziwej „Incepcji” -- czas ulegałby rozciąganiu. Im dalej od fizycznego sprzętu znajduje się warstwa, tym wolniej wszystko w&nbsp;niej działa."
%}

## Wycinek szerokiego świata

Wyżej wspomniałem, że maszyny wirtualne to rozległy temat. Na potrzeby tego wpisu dość mocno przytnę zakres tematyczny i&nbsp;napiszę jedynie o:

* maszynach rozumianych jako system w&nbsp;systemie;
* działających na komputerze osobistym, a&nbsp;nie smartfonie;
* uruchamianych przez program taki jak VirtualBox;
* prywatnościowych zastosowaniach (z&nbsp;lekkim zahaczeniem o&nbsp;ogólniejszy wątek *izolacji*);
* przeciwnikach działających legalnie (nie uwzględniam hakerstwa).

Nawiązania do innych możliwości dodam jedynie w&nbsp;formie rozwijanych streszczeń. Chętne osoby mogą sobie zerknąć i przekonać się, że omawiane w&nbsp;tym wpisie sprawy to zaledwie kawałek sporego tortu.

<details class="framed bigspace-before">
<summary><strong>Maszyny wirtualne na smartfonach?</strong></summary>

<p>Smartfonowy system Android ma u&nbsp;swoich podstaw Linuksa. Coraz śmielej sięga po jego moce, również te związane z&nbsp;wirtualizacją. W&nbsp;nadchodzącej <a href="https://techweez.com/2024/10/15/android-16-will-include-a-terminal-and-full-linux-vm-support/">wersji numer 16</a> ma już być wbudowana możliwość uruchamiania Linuksa w&nbsp;VM&#8209;ce na Androidzie.<br />
Niezależnie od tego powstają projekty eksperymentalne, obchodzące ograniczenia. Już parę lat temu ktoś uruchomił <a href="https://www.xda-developers.com/android-13-dp1-google-pixel-6-kvm-virtual-machine/">Windowsa na Androidzie</a>, a&nbsp;na Windowsie grę.</p>

<p>…Tylko że, choć te nowinki budzą ciekawość i&nbsp;mają pewien sens z&nbsp;punktu widzenia <em>kompatybilności</em> (uruchamiania czegoś, co na Androidzie by nie ruszyło), nie dają rewolucji w&nbsp;sferze <em>prywatności</em>.</p>

<p>To dlatego, że prywatnościową cechę maszyn wirtualnych, czyli <em>izolację</em>, mamy na smartfonach niejako w&nbsp;pakiecie. W&nbsp;przeciwieństwie do komputerów osobistych, <strong>apki smartfonowe mają względną odrębność</strong>. Każda jest jak osobna całość, z&nbsp;własnymi plikami. Apki bez szczególnych uprawnień nie mogą zaglądać do nieswoich przestrzeni.</p>

<p>W tej izolacji istnieją pewne luki – <a href="/apki/2022/11/16/apki-pliki" class="internal">wspólne pliki i&nbsp;foldery</a>, identyfikator reklamowy czy ogólne ustawienia systemowe. Nie zmienia to jednak faktu, że domyślnie smartfony dają lepszą izolację niż komputery osobiste.</p>

<p>A jeśli ktoś chce przenieść ją na jeszcze wyższy poziom, to może rozważyć założenie na Androidzie osobnego <a href="https://digitalprivacy.shop/blog/android-multiple-user-profiles">profilu użytkownika</a>. Pod względem prywatności byłby on smartfonowym odpowiednikiem VM&#8209;ki, z&nbsp;innymi aplikacjami i&nbsp;plikami niż nasz główny profil.</p>

<p class="post-meta bigspace-after">Zachęcam jednak, żeby poczytać o&nbsp;metodach profilowania z&nbsp;dalszej części tego wpisu. Smartfony, dając szeroki dostęp do czujników, mogą być szczególnie narażone na opisane tam metody.</p>
</details>

<details class="framed bigspace-before">
<summary><strong>„Programistyczne” maszyny wirtualne</strong></summary>

<p>Jeśli ktoś pamięta młodość z&nbsp;komputerami osobistymi, to być może gdzieś w&nbsp;głowie kołacze się nazwa <em>Java Virtual Machine</em>. Takie coś, co trzeba było zainstalować, żeby działały niektóre programy. Nazwa pochodzi od języka programowania Java.</p>

<p class="post-meta bigspace-after">Oprócz Javy z&nbsp;maszyny wirtualnej korzysta parę innych języków, jak Python. Żeby jeszcze bardziej namotać, ten drugi ma w&nbsp;pakiecie rozwiązanie zwane <em>środowiskami wirtualnymi</em>. To jeszcze inna rzecz, dotycząca z&nbsp;kolei instalowania plików.</p>

<p>Tego rodzaju „VM&#8209;ki” są czymś całkiem innym od tych, na których skupia się wpis. Z&nbsp;systemami w&nbsp;systemach czy z&nbsp;izolacją mają niewiele wspólnego. A&nbsp;z prywatnością już zupełnie nic.</p>

<p>Skąd zbieżność nazw? Intuicyjnie można sobie wyobrazić, że wspomniane języki nie rozmawiają bezpośrednio z&nbsp;(realnym) procesorem. Nim się do niego zwrócą, wykonują własne, wewnętrzne instrukcje. Wykonawca instrukcji to w&nbsp;żargonie komputerowym maszyna, a&nbsp;nakładka na coś realnego to coś wirtualnego. Stąd „programistyczne VM&#8209;ki”.</p>

<div style="margin-top:3em">
  <div class="subcontent-heading">
<span style="padding-left: 10px; padding-right: 15px">
Ciekawostka
</span>
  </div>
  <div class="bold-border" style="padding:10px;border-radius:0px 10px 10px 0px">
    <p style="margin-bottom:0px">Z takimi maszynami wirtualnymi mamy ogólnie do czynienia, kiedy ktoś na istniejącym, znanym języku programowania dostawi własną warstwę. Patrząc w&nbsp;ten sposób, maszyny mogłyby znajdować się nawet wewnątrz stron internetowych, tworząc na bazie powszechnego kodu JavaScript własne instrukcje.<br />
Z takiego czegoś korzysta TikTok, maskując w&nbsp;ten sposób prawdziwą naturę swojej strony internetowej. Niektórzy podjęli się <a href="https://news.ycombinator.com/item?id=34306963">analizy ich VM&#8209;ki</a>.</p>
    
  </div>
</div>
</details>

## Prywatność dzięki izolacji

Wyobraźmy sobie, że musimy zainstalować jakiś program, któremu nie do końca ufamy. Nie na zasadzie „jest wirusem”, lecz na zasadzie „zbiera moje dane”. Potrzebujemy jego możliwości, ale nie chcemy go stawiać nigdzie obok wrażliwych informacji. A&nbsp;komputer mamy jeden.

W takim przypadku zyskuje na atrakcyjności kluczowa cecha maszyn wirtualnych -- **izolacja**. Odrębność, odgrodzenie od głównego systemu.  
Można sobie wyobrazić, że w&nbsp;każdej VM&#8209;ce siedzi całkiem osobny system. Ma własne pliki, własne ustawienia, własne programy... A&nbsp;to daje ogromne możliwości.

### Ochrona przed czytaniem naszych plików

W przypadku systemów na komputerach osobistych (Windows, MacOS, popularniejsze Linuksy) granice między programami są zwykle umowne i&nbsp;nieszczelne.

Po pierwsze: często zapisujemy pliki do publicznie dostępnych miejsc (jak folder `Dokumenty`). Z&nbsp;założenia chcemy je tam trzymać i&nbsp;co najwyżej wyświetlić czasem w&nbsp;domyślnym podglądzie.  
Ale, niezależnie od naszych intencji, mogą tam sięgnąć również inne programy. W&nbsp;przypadku zdjęć mogą na przykład odczytywać [współrzędne geograficzne z&nbsp;metadanych]({% post_url 2021-02-10-gdzie-jestem-zapytaj-moich-zdjec %}){:.internal}.

Po drugie: czasem programy zapisują różne rzeczy do własnych folderów, o&nbsp;nazwach wyraźnie sugerujących, że to ich foldery wewnętrzne. Przykład: `.mozilla/firefox`. Ale cóż po nazwie, gdy nie ma żadnych barier osłaniających te miejsca przed innymi rzeczami zainstalowanymi na komputerze?

Pokazałem to już kiedyś na przykładzie [pamięci podręcznej przeglądarek]({% post_url 2021-12-24-caching %}){:.internal}. Wystarczył względnie prosty skrypt, żeby sięgać do plików Opery, Chrome'a czy Firefoksa (zapisywanych na dysku, żeby uniknąć wielokrotnego pobierania różnych elementów).

Były tam wszelkiej maści awatary z&nbsp;social mediów czy wyświetlone obrazki, wraz z&nbsp;linkami. Rzeczy, które pozwoliłyby postronnym ustalić, jakie *dokładnie* treści oglądaliśmy. Nawet jeśli w&nbsp;historii przeglądania była tylko najogólniejsza możliwa nazwa, jak `facebook.com`.

Inny przykład? Poniżej fragment pliku z&nbsp;historią otwieranych dokumentów, jaki tworzy sobie pakiet OnlyOffice (skądinąd fajny zamiennik Microsoft Office'a). Pełna ścieżka do pliku na moim Linuksie: `~/.local/share/onlyoffice/desktopeditors/recents.xml`. Już początek nazwy sugeruje, że folder jest ogólnodostępny.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/maszyny-wirtualne/onlyoffice-podpowiedz.jpg" alt="Zrzut ekranu pokazujący fragment pliku z&nbsp;historią dokumentów otwartych w&nbsp;OnlyOffice. Widać tu datę i&nbsp;nazwę pliku."/>

Po datach można poznać czyjś rytm dnia. Liczba pozycji na liście ukazuje stopień obłożenia pracą. Nazwy plików -- branżę i&nbsp;charakter tejże pracy. I&nbsp;wszystko to odczytane z&nbsp;samych metadanych, nawet bez zaglądania do dokumentu.

To tylko wycinek niezliczonych możliwości, jakie mają aplikacje zaglądające do plików. Na szczęście **maszyna wirtualna przed tym chroni -- zwyczajnie nie ma w&nbsp;niej naszych plików i&nbsp;folderów**. System uruchomiony w&nbsp;VM&#8209;ce wygląda dla wścibskiego programu jak taki po świeżej instalacji.

{% include info.html
type="Uwaga"
text="Oczywiście z&nbsp;czasem może się to zmieniać, a&nbsp;plików w&nbsp;VM&#8209;kach może przybywać -- można do nich wracać, wczytując i&nbsp;zapisując ich stan jak w&nbsp;grach komputerowych; nie muszą być jednorazowe.  
Jeśli zachowamy ostrożność i&nbsp;unikniemy przerzucania do maszynki rzeczy z&nbsp;naszego głównego systemu, to nie powinny się w niej znaleźć wrażliwe informacje. Tym niemniej warto raz na jakiś czas usuwać VM&#8209;kę i&nbsp;wgrywać nową, żeby metadane nagromadzonych w&nbsp;niej plików zdradzały jak najmniej."
%}

### Ochrona przed czytaniem plików systemowych

Nie tylko pliki od pomniejszych, zainstalowanych programów mogą zawierać wrażliwe informacje. Czasem również ustawienia samego systemu są żywą opowieścią.

Komputer zapisuje na przykład historię hotspotów, z&nbsp;jakich korzystaliśmy, żeby potem automatycznie łapać z&nbsp;nimi łączność. W&nbsp;tej historii są ich czytelne, publiczne nazwy.

Potencjalne programy stalkujące mogą odczytać z&nbsp;takiej historii nasze zamiłowania (`Klub_Fitness_Guest`, `NeuroKonferencja Free`) i&nbsp;historię wędrówek (`ChataMagory` -- z&nbsp;życia). A&nbsp;na dłuższą metę również lokalizację (punkty, które najczęściej lądują na liście najnowszych. Nawet jeśli nazwa mało mówi, to da się czasem [wyszukać ją w&nbsp;bazie]({% post_url 2023-07-15-sledzenie-lokalizacji %}#wi-fi){:.internal} przypisującej hotspoty do współrzędnych geograficznych).

To tylko jeden przykład; oprócz tego są też logi systemowe, [systemowa historia wyszukań](https://support.microsoft.com/en-us/windows/windows-search-and-privacy-99fb8251-7260-1cd6-1bbb-15c2370eb168), z&nbsp;nieco nowszych rzeczy Recall... I&nbsp;mnóstwo innych możliwości, z&nbsp;których wielu dotąd nie poznałem. Pozostawiam wyobraźni.

Ale, niezależnie od natury informacji ukrytych w&nbsp;ustawieniach, **czysta VM&#8209;ka przed tym ochroni**. Będzie jak nowy komputer z&nbsp;nowymi ustawieniami. Oczywiście warto pamiętać, żeby nie importować swoich ustawień z&nbsp;głównego komputera, zwłaszcza jeśli są mocno spersonalizowane. Nowa wirtualka, nowi my.

### Ochrona przed profilowaniem przez czcionki

Profilowanie przez czcionki jest o&nbsp;tyle ciekawe, że może je wykonywać nawet (mocno ograniczany przez przeglądarkę) [kod ze stron internetowych]({% post_url 2022-06-10-fingerprinting %}#czcionki){:.internal}, które odwiedzamy.

Działa to tak, że kod na stronach prosi przeglądarkę o&nbsp;uformowanie tekstu z&nbsp;użyciem konkretnej czcionki. Przeglądarka, reagując na prośbę, sięga do wspólnego systemowego folderu. Jeśli nie znajdzie tam szukanej czcionki, to używa zastępczej.

Prosząc o&nbsp;wiele różnych czcionek i&nbsp;analizując efekty końcowe (użyto żądanej czy zastępczej), strony internetowe mogą [ustalać](https://browserleaks.com/fonts), jaki zestaw czcionek u&nbsp;siebie mamy. I&nbsp;odróżniać nas na tej podstawie od innych osób.

{% include info.html
type="Ciekawostka"
text="Zdarza się również, że jakaś unikalna czcionka zostaje celowo wrzucona przez jakiś program A&nbsp;do folderu na czcionki. Gdy później inny program B&nbsp;zapyta system, czy jest dostępna, to dostanie odpowiedź twierdzącą. I&nbsp;na tej podstawie ustali, że mamy u&nbsp;siebie program A.  
W praktyce [wykorzystywał to](https://www.ctrl.blog/entry/teamviewer-font-privacy.html) program do zdalnego sterowania komputerem, TeamViewer, wyświetlając inną stronę niektórym użytkownikom."
%}

Świeża VM&#8209;ka ochroni przed wieloma formami profilowania przez czcionki. Z&nbsp;tego prostego względu, że zawiera tylko czcionki domyślne systemu-gościa, który w&nbsp;niej zainstalowaliśmy.

{:.post-meta .bigspace-after}
Oczywiście na dłuższą metę, w&nbsp;miarę instalowania przez system z&nbsp;wirtualki różnych czcionek znalezionych w&nbsp;sieci, również zacznie się on wyróżniać.

## Przechytrzenie głęboko zagnieżdżonych programów

Teraz coś związanego pośrednio ze śledzeniem, bezpośrednio -- z&nbsp;*kontrolą*.

Zazwyczaj instalacja programu polega na tym, że grzecznie umieszcza on swoje pliki w&nbsp;określonych folderach. Czasem ustawia wartości jakichś zmiennych systemowych. Potem już podporządkowuje się systemowi pod sobą (przypomnę: hierarchia z&nbsp;piramidy).

Istnieją jednak programy, które domagają się umieszczenia przynajmniej jakiejś swojej cząstki w&nbsp;warstwie głębszej -- prosto w&nbsp;**jądrze systemu**. Dzięki temu pod pewnym względem **to one stają się nadrzędne wobec użytkownika**.

Przykładem takiego programu był Falcon Sensor, którego błąd doprowadził w&nbsp;zeszłym roku do [masowego zawieszenia się komputerów z&nbsp;Windowsem]({% post_url 2024-07-24-crowdstrike %}){:.internal}.

Innym przykładem są *anti-cheaty*, czyli zabezpieczenia przed oszukiwaniem w&nbsp;grach komputerowych. Mając oko na wszystkie procesy działające na komputerze, mogą wyłapać, czy ktoś stosuje na przykład automatyczne celowanie lub wbudowane skrypty. 

Mając wielkie przywileje, takie programy zyskują duże możliwości gromadzenia danych. I, co gorsza, trudno im odmówić. Jeśli mniejszy, inwazyjny moduł nie zasygnalizuje głównemu programowi „OK, siedzę w&nbsp;jądrze”, to całość po prostu nie zadziała.

...Ale co, jeśli damy mu taki uprzywilejowany dostęp, ale **tylko do jądra systemu w&nbsp;VM&#8209;ce**?  
Wilk syty i&nbsp;owca cała. Program sądzi, że tkwi tam, gdzie powinien. Ale wciąż to my jesteśmy bliżej fundamentu piramidy, bardziej uprzywilejowani.  
Nawet jeśli uznamy VM&#8209;kę za kompletnie przejętą przez zbira, to wciąż pozostaje zaledwie pojedynczym, małym oknem na naszym pulpicie. Oddalonym od tajemnic.

## Ograniczenia maszyn wirtualnych

Istnieją rzeczy, przed którymi nawet najszczelniejsza VM&#8209;ka nas nie uchroni.

Po pierwsze: przed błędami ludzkimi. Gdybyśmy na przykład skopiowali na pendrive'a wrażliwe pliki, a&nbsp;potem udostępnili go VM&#8209;ce, to każdy tkwiący w&nbsp;niej cyfrowy gremlin może się dorwać do sekretów.

Ale załóżmy nawet, że jesteśmy ostrożni. Nigdy nie naruszamy bariery między systemem a&nbsp;wirtualką, do tego co jakiś czas tworzymy nową. Nadal pozostaje parę ograniczeń.

### Możliwość wykrycia

Podglądacze, skutecznie blokowani przez VM&#8209;kę, mają interes w&nbsp;tym, żeby rozpoznawać takie więzienia wokół siebie. Widząc je, mogą po prostu odmówić działania lub udawać niewinne programy.

A rozpoznanie „życia w&nbsp;symulacji” wbrew pozorom może być całkiem łatwe. **Niektóre programy od wirtualizacji bywają gadatliwe**. Przykład? Program VMWare umieszczał w&nbsp;plikach konfiguracyjnych, które każdy program może sobie podejrzeć (dokładniej: w&nbsp;polu `CPUID`) informację o wirtualności systemu.

Takie zachowanie może dziwić, patrząc na opisane wcześniej korzyści prywatnościowe. Ale można uznać, że są one niejako niezamierzone i&nbsp;wynikają z&nbsp;izolacji typowej dla VM-ek. Ich twórcy niekoniecznie mają prywatność na uwadze. 

Gdyby nawet program wprost nie ujawniał podstawowych informacji, pewne rzeczy wciąż pozostaną nie do uniknięcia:

* maszyna wirtualna dodaje kolejny poziom do wszystkich obliczeń, przez co jest wolniejsza niż system pierwotny,
* dostaje jedynie część zasobów (pamięci, miejsca na dysku) od głównego komputera.

Wścibskie programy mogą przeprowadzić serię testów. Trochę w&nbsp;stylu *benchmarków* do testowania wydajności w&nbsp;grach komputerowych, tyle że wykonanych w&nbsp;złej wierze. Wyniki testów mogą porównywać ze znanymi wzorcami.

Jeśli ujawnią, że dany procesor zachowuje się nietypowo jak na swój model (inne wzorce przy stopniowym zwiększaniu obciążenia), to program domyśli się, że ktoś właśnie go zamknął w&nbsp;VM&#8209;ce. I&nbsp;odmówi działania.

Takich luk jest sporo i&nbsp;mogą być bardzo trudne do załatania. Pomóc może natomiast fakt, że dyskretniejsze wirtualki rozwijają też badacze cyberbezpieczeństwa, żeby analizować w&nbsp;nich wirusy. Zwykli prywatnościowcy mogą skorzystać z&nbsp;ich dorobku :sunglasses: Przykład? [Projekt Pafish](https://github.com/a0rtega/pafish), zbierający metody wykrywania VM-ek.

W odpowiedzi na rozwój technik wykrywania powstały lepsze metody maskujące. Jak [CloakBox](https://github.com/Batlez/CloakBox), ukrywający fakt, że korzystamy z&nbsp;VirtualBoxa.

{:.post-meta}
Uwaga: nie korzystałem z&nbsp;CloakBoxa, więc nie ręczę za niego i&nbsp;przywołuję go wyłącznie jako studium przypadku. Osoby chętne mogą zajrzeć mu w&nbsp;kod źródłowy i&nbsp;spojrzeć na użyte techniki. 

### Łączenie informacji z&nbsp;różnych programów

VM&#8209;ki bardzo pomagają, gdy mamy prostą sytuację: wszystko co złe w&nbsp;VM&#8209;ce, rzeczy dobre na głównym systemie, i&nbsp;tak do końca życia (naszego urządzenia).

Jeśli jednak:

1. mamy więcej niż jedną kopię złego programu;

   {:.post-meta .bigspace-after}
   Czy to w&nbsp;różnych VM&#8209;kach, czy nawet jakąś na prawdziwym systemie. Można dołożyć nawet przypadek, gdy programy są różne, ale zawierają elementy gościnne (SDK) od tej samej firmy od reklam śledzących.

2. każda z&nbsp;kopii programu łączy się przez internet ze swoimi twórcami...

...to zachodzi ryzyko, że **programy zastosują profilowanie (ang. _fingerprinting_) i&nbsp;zorientują się, że są w&nbsp;rękach tej samej osoby**. Co może być szczególnie groźne, gdyby choć jeden z&nbsp;nich ustalił ponadto dane osobowe.

Takie profilowanie jest możliwe dzięki temu, że dwie niezależne „nogi”, trzymane w&nbsp;rozkroku dzięki VM&#8209;kowej izolacji, stykają się w&nbsp;fizycznej warstwie systemu.

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/maszyny-wirtualne/maszyna_wirtualna_deanonimizacja.jpg" alt="Ponownie schemat pokazujący system Linux stojący na systemie Windows. Wszystko poza dwoma Firefoksami i&nbsp;warstwą dolną (fizycznym sprzętem) jest przyciemnione. Od obu programów do sprzętu prowadzą kolorowe linie, idąc następnie u&nbsp;ikonie internetu, a&nbsp;na koniec ku ikonie wszystkowidzącego oka."/>

{:.figcaption}
Źródła: jak wcześniej, plus ikony z&nbsp;serwisu Flaticon.

Niżej niepełna lista informacji, z&nbsp;których programy zamknięte w&nbsp;wirtualnych klatkach mogą zbudować nasz profil.

{% include info.html
type="Uwaga"
text="Opisuję tu parę naprawdę wrednych metod, z&nbsp;którymi pewnie mało kto zetknie się w&nbsp;życiu. Bardzo proszę się nie zniechęcać i nie myśleć, że dbanie o&nbsp;prywatność jest trudne i&nbsp;bezcelowe. Analogia *erpegowa*: my tu expimy na smokach, żeby bezproblemowo kosić codzienne gobliny :wink:"
%}

* **Język i&nbsp;strefa czasowa**

  Wiele osób, mimo że oddziela od siebie system realny i&nbsp;wirtualny, może dla wygody ustawić w&nbsp;nich prawdziwy język i&nbsp;strefę czasową. Dla szpicli to dobry sygnał uzupełniający, choć raczej nie główna metoda demaskowania -- chyba że jesteśmy jedynym polskojęzycznym użytkownikiem z&nbsp;[najmniej zaludnionej strefy czasowej](https://earthscience.stackexchange.com/questions/12504/least-populated-time-zones).

* **Kamerka i&nbsp;mikrofon**

  W&nbsp;skrajnym przypadku każdy z&nbsp;programów mógłby uruchomić kamerkę, zrobić zdjęcie naszej gęby i&nbsp;wysłać je do swoich twórców. Algorytmy łatwo rozpoznają, że zarówno program A, jak i&nbsp;B (z&nbsp;VM&#8209;ki) widziały tę samą osobę. I&nbsp;tożsamości powiązane, dzień popsuty.

  Ale to skrajność. W&nbsp;praktyce programy z&nbsp;VM&#8209;ki, mając dostęp do kamerki, mogłyby zamiast tego sięgnąć do informacji o&nbsp;jej technicznych parametrach (stabilizacji, balansie bieli itd.). Analogicznie z&nbsp;mikrofonem.  
  Ponownie: sygnał raczej niegroźny solo, groźny po połączeniu z&nbsp;innymi.

* **Hotspoty i&nbsp;internet**

  Różne tożsamości w&nbsp;różnych VM&#8209;kach... Ale co z&nbsp;tego, jeśli łączą się z&nbsp;tym samym internetem?

  Najprostszą cechą łączącą tożsamości może być [adres IP]({% post_url 2021-06-12-adres-ip %}){:.internal}. Internetowy odpowiednik adresu pocztowego, nadawany w&nbsp;uproszczeniu przez hotspota, z&nbsp;którym się łączymy.  
Choć jest nieco bardziej zmienny niż adres nieruchomości, wciąż pozwala dojrzeć powiązanie: „różne programy, A&nbsp;i B, uruchamiane krótko po sobie, piszą do nas z&nbsp;tego samego IP! Być może mają tego samego użytkownika”.

  To może spróbujemy ukryć adres z&nbsp;VM&#8209;ki za jakimś pośrednikiem (np. VPN-em), którego nie używamy poza nią? Istotnie, wtedy adresy byłyby inne. Ale ku przestrodze: nawet w&nbsp;skądinąd szczelnych przeglądarkach, jeśli nie zadbamy w&nbsp;ustawieniach o&nbsp;parę szczegółów, wścibscy podglądacze mogą czasem [wymusić tryb wideokonferencji]({% post_url 2023-11-05-webrtc %}){:.internal}, żeby dorwać prawdziwy adres IP zza pośrednika.

  Załóżmy, że to naprawiliśmy. Ale jeśli program w&nbsp;VM&#8209;ce i&nbsp;program spoza niej mają możliwość sprawdzania aktualnych [hotspotów wokół nas]({% post_url 2023-07-15-sledzenie-lokalizacji %}#wi-fi){:.internal} -- czyli zarówno czytelnych nazw, jak `McD Hotspot`, jak i&nbsp;identyfikatorów BSSID -- to łatwo powiążą tożsamości.

  {:.post-meta .bigspace-after}
  Wyżej pisałem, że VM&#8209;ka pomaga przy ukrywaniu systemowej *historii* połączeń z&nbsp;hotspotami. Tutaj mówię o&nbsp;czymś innym: danych napływających na bieżąco, gdy mamy łączność z&nbsp;siecią.

* **Procesor, karta graficzna, karta dźwiękowa...**

  Po pierwsze -- programy mogą po prostu [zapytać](https://www.whonix.org/wiki/VM_Fingerprinting). Pewne ogólne informacje, jak te o&nbsp;procesorze (na Linuksie z&nbsp;pliku `/proc/cpuinfo`), są ujawniane na życzenie.

  Wspomniałem wcześniej, że programy mogą zmuszać komputer do wykonywania *benchmarków*, żeby ustalić, że zostały zamknięte w&nbsp;VM&#8209;ce. Podobnymi testami mogą ustalić **charakterystyczne cechy wyróżniające nasz sprzęt**.

  Można powiedzieć, że elementy fizyczne mają swoje tiki. Jeden procesor szybciej rysuje kształty niż inny, a&nbsp;po osiągnięciu liczby X&nbsp;trójkątów następuje w&nbsp;nim skokowe spowolnienie. Karta dźwiękowa trochę „ścina na brzegach” i&nbsp;„spłyca scenę przy mocnych basach” (pozdrawiam twórczość audiofilską :wink: ).

  Do takich informacji [sięgają nawet strony internetowe]({% post_url 2022-06-10-fingerprinting %}){:.internal}, poprzez kod JavaScript. Mimo że przeglądarki narzucają na nie restrykcje i&nbsp;nie ujawniają zbyt wiele. Zainstalowane programy widzą jeszcze więcej, będąc bliżej systemu i&nbsp;sprzętu.

  {:.post-meta .bigspace-after}
  Osoby zainteresowane tematem mogą znaleźć różne przykłady pod hasłem `hardware fingerprinting`.

### Złośliwy hardware

Pokazałem wcześniej, że można „przelicytować” złośliwe programy chcące wniknąć do dolnej warstwy. Dać im miejsce w&nbsp;jądrze systemu, ale jedynie w&nbsp;tym wirtualnym, trzymając realne z&nbsp;dala od nich.

Ale w&nbsp;podobny sposób inni mogą przelicytować nas. **Jeśli mają swojego „agenta” w&nbsp;warstwie fizycznej, to koniec gry, będzie on poza naszym zasięgiem**. I&nbsp;może na przykład meldować złemu programowi, że chcemy go oszukać przez wirtualizację.

Tacy fizyczni agenci nie są niestety moim wymysłem ani straszeniem. We współczesnych urządzeniach układy z&nbsp;założenia odizolowane od użytkowników są na porządku dziennym.

Jednym z&nbsp;tego rodzaju układów jest [Intel Management Engine]({% post_url 2021-07-27-intel-management-engine %}){:.internal}, czyli swego rodzaju „system u&nbsp;podstawy systemu”. Procesory Intela nie zadziałają, jeśli się nie uruchomi. A&nbsp;gdy już się uruchomi, to ma pełną władzę nad głównym systemem, dostęp do jego pamięci i&nbsp;każdej wykonywanej instrukcji.  
Na procesorach AMD jego odpowiednikiem jest Platform Security Processor. 

Innym rodzajem tych elementów są mniejsze układy kryptograficzne, takie jak Trusted Platform Module. Wymagany przez nowego Windowsa.

Układy mogą dawać osobom z&nbsp;zewnątrz, jak twórcy wścibskich programów, bardzo silne gwarancje. Szczególnie wredna jest **zdalna atestacja** (omówiona krok po kroku [w tym wpisie]({% post_url 2024-10-22-trusted-computing-kajdany %}){:.internal}; próba jej praktycznego użycia przez Google'a jest z&nbsp;kolei [tutaj]({% post_url 2023-07-29-web-environment-integrity %}){:.internal}).

Atestacja polega na tym, że ktoś może wysłać do fizycznego chipa pytanie o&nbsp;to, czy jest obecnie na realnym, niemodyfikowanym systemie. Odpowiedź z&nbsp;założenia zawsze będzie prawdziwa i&nbsp;niemożliwa do podrobienia -- jest oznaczona cyfrowym podpisem, który może stworzyć wyłącznie element zamknięty w&nbsp;mikroukładzie.

Ogólnie można przyjąć taką regułkę: jeśli coś jest związane z&nbsp;fizycznym sprzętem, to żadne VM&#8209;ki nas nie ocalą. Dokładanie górnych warstw nie pomoże przeciw wrogom siedzącym w&nbsp;fundamencie. Nawet gdyby sami nie zbierali danych, mogą przynajmniej donosić zbieraczom, że jest frajer do golenia.

## Przykład z&nbsp;życia: Proctorio

Na koniec, po tych wszystkich rozważaniach, coś życiowego.

Kilka lat temu, za czasów pandemii, chwilowy *boom* przeżyły wszelkie formy pracy i&nbsp;nauki zdalnej. Jak nauka, to egzaminy. A&nbsp;na nich zdarza się ściąganie. Uczelniom nie było w&nbsp;smak, że nie mają jak mu zaradzić.   
Wówczas, wśród innych podobnych produktów, na scenę *całe na biało*{:.corr-del} weszło **Proctorio**. Dość inwazyjny program komputerowy analizujący, czy ktoś nie ściąga podczas egzaminu. Oceniali to m.in. na podstawie obrazu z&nbsp;kamerki internetowej i&nbsp;metod uczenia maszynowego (potocznie: AI).

{:.post-meta .bigspace-after}
Choć nazwa kojarzy się z&nbsp;[jelitami](https://pl.wikipedia.org/wiki/Proktologia), jej trzonem jest w&nbsp;istocie [*proctor*](https://www.etymonline.com/word/proctor). W&nbsp;anglosferze nadzorowanie ludzi podczas egzaminów dotąd nazywa się *proctoringiem*.

Twórcy programu oczywiście przedstawiali swoje algorytmy jako niezawodne. Coś, w&nbsp;co każda szanująca się uczelnia powinna zainwestować. W&nbsp;praktyce dość szybko [odkryto](https://www.theverge.com/2021/4/8/22374386/proctorio-racial-bias-issues-opencv-facial-detection-schools-tests-remote-learning), że prawdopodobnie korzystali z&nbsp;darmowego pakietu OpenCV, nie wnosząc zbyt wiele innowacji.

Co gorsza, algorytmy potrafiły nękać negatywnymi opiniami osoby w&nbsp;jakikolwiek sposób nietypowe. Wyróżniające się [kolorem skóry](https://www.theverge.com/2021/4/8/22374386/proctorio-racial-bias-issues-opencv-facial-detection-schools-tests-remote-learning), zezem, rozbieganym wzrokiem, zwykłymi tikami polegającymi na błądzeniu wzrokiem... Proctorio potrafi(-ło) [przerwać ich egzamin](https://xcancel.com/Linkletter/status/1864165609824559139#m) i&nbsp;oflagować ich zachowanie jako podejrzane, do oceny przez egzaminatorów.

Jeden z&nbsp;głośnych krytyków działań firmy, Ian Linkletter z&nbsp;kanadyjskiej uczelni, został przez nich pozwany po tym, jak udostępnił parę linków do ich filmików. Były rzekomo niejawne, więc firma oskarżyła go o&nbsp;naruszenie praw autorskich.

{% include info.html
type="Ciekawostka"
text="Podobny zarzut wysunęła firma Newag wobec polskiej ekipy, która wykryła sztuczne, antykonkurencyjne blokady cyfrowe w&nbsp;ich pociągach. Stwierdziła, że przez pokazywanie screenów z&nbsp;krótkimi fragmentami kodu naruszają ich prawa autorskie."
%}

Walka Linklettera z&nbsp;Proctorio toczy się już kilka lat. Sąd w&nbsp;Kanadzie, wbrew rozumowi i&nbsp;godności człowieka, nie uznał pozwu Proctorio za SLAPP, czyli zastraszanie drogą prawną. Rozprawa będzie zatem musiała się odbyć, [walka trwa](https://linkletter.opened.ca/). Oburzeni mogą wesprzeć pana Linklettera.

Ogólnie: Proctorio i&nbsp;automaty oceniające nie budzą sympatii i&nbsp;wiele osób chętnie by im zagrało na nosie. Jednym ze sposobów byłoby właśnie uruchomienie programu pilnującego w&nbsp;VM&#8209;ce. Żeby nasycić jego chęć dostępu do głębszych warstw systemu.

Tenże (wirtualny) system można otworzyć w&nbsp;oknie na jednej połowie ekranu. A&nbsp;na drugiej połowie, w&nbsp;oknie należącym już do pierwotnego systemu -- notatki, z&nbsp;których coś można sobie czytać. Żadna aplikacja nie powinna być w stanie wychylić się z&nbsp;VM&#8209;ki i&nbsp;dojrzeć, co ktoś porabia na prawdziwym systemie.

Nie pójdzie to raczej jak po maśle, bo Proctorio dobrze zna taką metodę obejścia. Na swojej stronie piszą, że ich program nie będzie działał w&nbsp;maszynach wirtualnych. Do tego aktywnie wykrywają ich istnienie i&nbsp;[odmawiają działania](https://shkspr.mobi/blog/2021/11/proctoru-is-dystopian-spyware/).

{:.bigspace-before}
> Maszyny wirtualne: jeśli w&nbsp;chwili łączenia się z&nbsp;nami twój program działa w&nbsp;maszynie wirtualnej, poprosimy cię o wyjście z&nbsp;niej i&nbsp;uruchomienie programu na twoim głównym systemie w&nbsp;celu podejścia do testu. 

{:.figcaption}
Tłumaczenie moje.

Bardziej zmotywowane osoby mogłyby przeanalizować, na jakiej podstawie Proctorio wykrywa VM&#8209;kę wokół siebie, i&nbsp;jakoś ją zamaskować. Swoją działającą konfiguracją mogą się potem dzielić z&nbsp;innymi. Taki wesoły, buntowniczy wyścig zbrojeń.

{:.figure .bigspace-before}
<img src="/assets/posts/inwigilacja/maszyny-wirtualne/proctorio.jpg" alt="Zrzut ekranu z&nbsp;Nittera pokazujący, jak jedna osoba pisze, że kiedyś omijali Proctorio z&nbsp;użyciem maszyny wirtualnej, a&nbsp;druga nieco w&nbsp;nią wątpi."/>

{:.figcaption}
Część Twitterka (tu wyświetlona przez *xcancel.com*) nie wierzy w&nbsp;studencki potencjał. Ja wierzę :smile:

## Podsumowanie

Maszyna wirtualna jest przydatnym narzędziem w&nbsp;prywatnościowym arsenale. Czymś w&nbsp;rodzaju drugiej tożsamości lub maski, którą na pewien czas zakładamy.

Ukrywa to, co nagromadziliśmy na głównym dysku, zapisane opcje i&nbsp;preferencje. Zamiast nich pokazuje proste, świeże, dość bezpłciowe oblicze. Jest idealna w&nbsp;przypadku, gdy chcemy u&nbsp;siebie zainstalować jakiś program, któremu nie do końca ufamy.

Zaczyna jednak nieco zawodzić w&nbsp;przypadku, gdy chcemy trzymać dwie tożsamości na jednym urządzeniu, a&nbsp;każda z&nbsp;nich wchodzi w&nbsp;interakcje z&nbsp;potencjalnym programem-podglądaczem.  
Istnieją metody pozwalające ustalić, że osoba A&nbsp;to tak naprawdę osoba B, kiedy obie VM&#8209;ki są na tym samym kompie/laptopie. Jeśli bardzo nam zależy na rozdzieleniu tożsamości, to silniejsze gwarancje daje korzystanie z&nbsp;całkiem osobnego urządzenia i&nbsp;sieci.

Jeśli przeciwnik aktywnie próbuje wykryć VM&#8209;kę -- nawet przez proste testowanie wydajności -- to rozpoczyna się wyścig zbrojeń. Być może jakoś przechytrzymy podglądacza, być może on nas. Ale na tym etapie VM&#8209;ka przestaje być komfortowym rozwiązaniem dla codziennego użytkownika.

Życzę, żebyśmy jednak nie nadziali się na tak zdeterminowanych dziadów, a&nbsp;wirtualna maska skutecznie zasłaniała nasze prawdziwe oblicza. Pozwalając je zostawić dla tych osób, które na nie zasługują :smile: 

