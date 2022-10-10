---
layout: post
title:  "Apki to pułapki 1 – podstawy"
subtitle: "Gdy wpuścimy szpiega do siebie."
description: "Gdy wpuścimy szpiega do siebie"
date:   2022-10-09 22:37:00 +0100
tags: [Android, Programy, Inwigilacja, Podstawy]
category: apki
category_readable: "Apki to pułapki"
image:
  path: /assets/posts/apki/apki-piramida-baner.jpg
  width: 1200
  height: 700

---

Zdarzało Wam się, że odwiedzacie jakąś stronę przez urządzenie mobilne, a&nbsp;ta próbuje Was przegonić do aplikacji?

<img src="/assets/posts/apki/apki-zacheta-do-instalacji.jpg" alt="Kolaż pokazujący cztery różne okna zachęcające do zainstalowania aplikacji zamiast korzystania ze strony internetowej."/>

{:.figcaption}
Strony: *messenger.com*, *gmail.com*, *amazon.com*, *reddit.com*.  
Gdybyśmy je odwiedzali przez komputer, to po prostu by nam się wyświetliła strona.

Dlaczego właścicielom stron tak zależy na tym, żebyśmy zainstalowali ich aplikację? Skoro strona i&nbsp;tak działa?  
Czasem mają jakiś sensowny powód, dla którego to robią. Na przykład potrzebują (coraz rzadszych) funkcji, których nie daje im nasza przeglądarka. **Ale często motywuje ich chęć zbierania danych**.

W innej mojej serii, [„Internetowej inwigilacji”](/serie/internetowa_inwigilacja/){:.internal}, omawiałem nieco węższy przypadek. Sytuację, kiedy surfujemy po internecie, korzystając z&nbsp;*przeglądarki*.  
To konkretny, dość specyficzny rodzaj programu. Ujawnia obcym (najczęściej dużym firmom z&nbsp;branży reklam śledzących) tylko wybrane rzeczy.

Analizowanie nas na podstawie tego, co nasz komputer wyśle w&nbsp;internet, jest trochę jak rozmowa z&nbsp;nami przez zamknięte drzwi mieszkania.

Jasne, ktoś może poznać ton naszego głosu. Odczytać tabliczkę z&nbsp;nazwiskiem na drzwiach. Zadać wścibskie pytania o&nbsp;to, co mamy w&nbsp;domu. Ale nie ma pewności, że mówimy prawdę.  
**Zainstalowanie wścibskiej aplikacji jest jak wpuszczenie takiego szpiega do swojego domu**. Jego możliwości śledzenia drastycznie rosną.

To tym zagrożeniom będzie poświęcona moja nowa seria, „Apki to pułapki”. W&nbsp;tym wprowadzającym wpisie przedstawię ogólny model działania współczesnych urządzeń i&nbsp;parę przemyśleń na temat zagrożeń. Później będę się do tego odnosił.  
Zapraszam, świat śledzenia czeka!

## Warstwy smartfona

> Cebula ma warstwy, *ogry*{:.corr-del} smartfony mają warstwy.

{:.figcaption}
Źródło: pierwsza część „Shreka”.

W poprzedniej serii, „Internetowej inwigilacji”, przyjąłem model *pocztowy* (przeglądarka jako poczta, wysyłane dane jako paczki, zamiast adresów domów adresy IP).

Tym razem potrzebowałem modelu pokazującego, do czego mają dostęp aplikacje i&nbsp;dokąd sięgają możliwości użytkowników. Chciałem też, żeby objął w&nbsp;przyszłości przypadek wrogich producentów (DRM, SafetyNet...). 

Chwilę pogłówkowałem. Ostatecznie mój wymysł przyjął kształt piramidki z&nbsp;paroma niuansami:

{:.bigspace-before}
<img src="/assets/posts/apki/apki-piramida.jpg" alt="Schemat pokazujący hierarchię we współczesnym urządzeniu. Ma kształt odwróconej piramidy. Na samym dole mamy ikonę procesora podpisaną CPU. Odchodzą od niej strzałki do ikonek symbolizujących aparat, mikrofon i&nbsp;sieć wi-fi. Cała warstwa jest podpisana 'hardware'. Nad nią w&nbsp;piramidzie mamy kolejno: 'firmware', 'jądro systemu' oraz 'system operacyjny'. Na tej warstwie stoją kolejne piramidy, już nie odwrócone. Jedna z&nbsp;nich jest podpisana 'programy', a&nbsp;na niej stoi warstwa podpisana 'dodatki do programów'."/>

{:.figcaption}
Źródło: Flaticon, Emojipedia, Wikimedia Commons (szczegóły [pod koniec wpisu](#źródła)).  
Aranżacja i przeróbki moje.

Zaraz omówię z&nbsp;osobna warstwy tego prowizorycznego modelu. Ale najpierw kilka założeń, jakie chciałem na nim pokazać:

1. **Wszystko na tym schemacie (oprócz fizycznego sprzętu) to programy**.

   Np. firmware to programy sterujące fizycznym sprzętem. System operacyjny to program uruchamiający inne programy. 

2. Między warstwami cały czas są przesyłane dane i&nbsp;pliki. Same w&nbsp;sobie nieaktywne, „martwe”. To programy mogą coś z&nbsp;nimi zrobić. 

3. Im niżej znajduje się jakaś warstwa głównej piramidy, tym jest istotniejsza dla całości.

   Jej „awaria” psuje wszystko, co na niej stoi. A&nbsp;jej „przejęcie” jest równoznaczne z&nbsp;przejęciem tego co wyżej.

4. Warstwy niżej położone narzucają wyższym sposób komunikacji.

   Zwykle ich twórcy określają to w&nbsp;jakiejś specyfikacji. Jeśli twórcy wyższych warstw się do tego nie dopasują, to coś nie zadziała.

5. Warstwę najniższą (*hardware*, czyli fizyczny sprzęt) dzielę na dwie kategorie -- podstawową i&nbsp;poboczną.

   Podstawowa to sprzęt niezbędny do działania, jak procesor albo pamięć. Oprócz tego mamy różnego rodzaju urządzenia poboczne (będące częścią urządzenia albo do niego podłączane), które porozumiewają się z&nbsp;tymi kluczowymi.

## Omówienie poszczególnych warstw

Serię opracowałem z&nbsp;myślą o smartfonach, ale powyższy model jak najbardziej pasuje również do komputerów osobistych. Spójrzmy teraz na typowe cechy poszczególnych warstw oraz przykłady ich ciemnych stron. I&nbsp;ze świata smartfonów, i&nbsp;komputerów.  
Zacznijmy od góry.

{% include info.html
type="Uwaga"
text="Nie będę tutaj mówił o&nbsp;kwestiach cyberbezpieczeństwa i&nbsp;wirusach. Korporacje, choć wścibskie, zwykle jednak trzymają się ram prawnych i&nbsp;nas nie hakują.  
Natomiast miejmy na uwadze, że jak najbardziej mogą istnieć programy -- z&nbsp;dowolnej warstwy naszej piramidki -- zdolne uderzyć w&nbsp;słabe punkty systemu i&nbsp;przejąć warstwy pod sobą."
%}

### Dodatki do programów

Wiele programów, zwłaszcza mniejszych, stanowi zamkniętą całość. Jasne, możemy podrzucać im różnorodne pliki. Ale ramy działania narzucają twórcy.

Czasem jednak ludzie chcą elastyczności. Możliwości dopasowania programów do własnych potrzeb. Z&nbsp;tego względu ich twórcy dają możliwość tworzenia niezależnych dodatków.

Dodatki same są mini-programami, napisanymi w&nbsp;języku programowania „zrozumiałym” dla programu macierzystego.  
Jednocześnie są od tego programu całkiem zależne i&nbsp;**nie są w&nbsp;stanie zyskać większych możliwości niż on** -- jeśli na przykład wyłączymy Firefoksowi dostęp do internetu, to zainstalowane na nim dodatki również nie będą w&nbsp;stanie się połączyć.

Do tej pory siłą rzeczy omawiałem tylko dodatki przeglądarkowe, w&nbsp;szczególności uBlock Origin (blokujący reklamy śledzące na odwiedzanych stronach).

Natomiast kategoria jest znacznie szersza, a&nbsp;jakieś swoje dodatki wspiera prawie każdy większy program.  
Za pewien rodzaj dodatków możemy uznać skrypty VBA pakietu Office. A&nbsp;nawet skrypty udostępniane przeze mnie na Ciemnej Stronie (programem-uruchamiaczem jest wtedy tak zwany *interpreter Pythona*, taki jak IDLE).

Potencjalne zagrożenia związane z&nbsp;dodatkami? Jeśli jakiś program, skądinąd bezpieczny, daje im wiele możliwości, to mogą zmienić go w&nbsp;program szpiegowski.  
Przykładem jest kontrowersyjny [dodatek do przeglądarki firmy Proctorio](https://threadreaderapp.com/thread/1301360994044850182.html) odpowiadający za monitorowanie studentów podczas egzaminów.

### Programy

Bodajże najszersza kategoria. Na każdym systemie możemy ich zwykle mieć tyle, ile tylko chcemy. Ale są spore różnice w&nbsp;sposobie korzystania z&nbsp;nich.

W przypadku pecetów (a przynajmniej Linuksa i&nbsp;Windowsa, które sprawdzałem) da się po prostu wziąć plik w&nbsp;odpowiednim formacie, jak EXE, i&nbsp;go kliknąć. Uruchomimy program bez żadnej instalacji.

W przypadku Androida można wprawdzie pobrać plik z&nbsp;apką w&nbsp;formacie APK... Ale, z&nbsp;tego co wiem, po kliknięciu musimy go zainstalować, a&nbsp;na ekranie głównym pojawi nam się jego ikona. Nie unikniemy tego.

Z kolei iOS od Apple jest systemem zamkniętym. Aplikacje musimy instalować przez ich centralną bazę, AppStore. Rzekomo dla naszego bezpieczeństwa.

W warstwie programów znajdziemy pełno wrednych rzeczy. Na ich omawianie mam całą serię, więc tutaj tylko drobny spoiler odnośnie tego, co nas czeka:

* Onavo -- apka od Facebooka. Zbierała dane o&nbsp;innych zainstalowanych aplikacjach. W&nbsp;ten sposób [szybko wykryli, że WhatsApp zyskuje na popularności](https://www.theverge.com/2019/2/22/18235908/facebook-onavo-vpn-privacy-service-data-collection) i&nbsp;go odkupili.
* Różne aplikacje do monitorowania cyklu miesiączkowego.

  Zbierały dane na potęgę. Użytkowniczkom to raczej nie przeszkadzało. Aż tu nagle w&nbsp;USA zmieniło się prawo. Od teraz dane z&nbsp;apek mogą zostać użyte jako [dowód (karalnego) przerwania ciąży](https://truthout.org/articles/privacy-experts-warn-data-from-period-tracking-apps-may-soon-be-used-against-you/).

* Banalne aplikacje w&nbsp;stylu latarek. Które jednak proszą o&nbsp;[dostęp do wszelkich możliwych pozwoleń](https://www.zdnet.com/article/most-android-flashlight-apps-request-an-absurd-number-of-permissions/).

### System operacyjny

Dokładniej rzecz biorąc, mam tutaj na myśli tę „publiczną” część systemu.  
My, użytkownicy, możemy się po niej poruszać i&nbsp;korzystać z&nbsp;różnych systemowych apek (kalkulatora, programu do zrzutów ekranu), a&nbsp;także zmieniać wiele ustawień.  
Z kolei aplikacje mogą korzystać z&nbsp;pewnych wspólnych części, takich jak systemowy schowek.

Pod wieloma względami ta warstwa nas chroni, ponieważ pozwala dodawać niektóre aplikacje do czarnej listy albo w&nbsp;inny sposób je kontrolować.  
Ale co, jeśli sam system działa przeciwko nam?

Można tu wspomnieć chociażby o&nbsp;niesławnych aktualizacjach Windowsa, włączających się w&nbsp;najmniej odpowiednich momentach. Albo ekranach [nachalnie namawiających](https://www.techradar.com/news/microsofts-windows-10-nag-screens-are-back-with-a-vengeance) do instalacji dodatkowych usług od Microsoftu. 

Również Apple zaliczyło wtopę, kiedy wyszło na jaw, jak wiele informacji ich system MacOS [wysyłał do ich centrali](https://www.howtogeek.com/701176/does-apple-track-every-mac-app-you-run-ocsp-explained/). Za każdym razem, kiedy uruchomiliśmy jakiś program.

Czasem istnieje opcja wyłączenia takich rzeczy. Może nawet dostępna dla użytkowników bez dłubania w&nbsp;trzewiach systemu. Ale, póki nie leży w&nbsp;interesie producenta, raczej nie znajdziemy jej na wierzchu.

### Jądro systemu

To ta głębiej położona, niejawna część systemu.  
Na komputerach osobistych zwykle mamy do niej dostęp, ale dopiero jeśli mamy uprawnienia administratora (w przypadku Linuksa zwanego *superużytkownikiem*). Często wymaga to wpisania osobnego hasła.

W przypadku systemów mobilnych **Google i&nbsp;Apple ograniczają nam dostęp**. Domyślnie możemy poruszać się co najwyżej na poziomie systemu operacyjnego, nie niżej. Jądro rezerwują dla siebie.

Niepokorni mogą jednak „złamać” swój telefon i&nbsp;zyskać nad nim pełnię władzy. W&nbsp;przypadku Androida taki proces nazywa się *rooting*, a&nbsp;w przypadku iOS -- *jailbreaking*.

Rzadko bo rzadko, ale warstwa „jądrowa” potrafi być wobec nas również szpiegiem.  
Twórcy gier z&nbsp;serii *Call of Duty* wymagali zainstalowania oprócz nich tak zwanego rozszerzenia jądra (*kernel extension*). To coś jak dodatek do programu, tylko że instalowany głębiej w&nbsp;bebechach systemu.

W ten sposób gracze (poziom warstwy systemu) mieli kontrolę nad grą (warstwa programów), ale rozszerzenie umieszczone poza ich zasięgiem (warstwa jądra) miało kontrolę nad tym, co z&nbsp;nią robią.  
Wszystko to [oficjalnie dla walki z&nbsp;oszustami](https://www.howtogeek.com/761510/pc-games-are-installing-low-level-drivers-in-windows/). Co nie zmienia faktu, że wymagało wpuszczenia obcej firmy głęboko w&nbsp;swój system.

### Firmware i&nbsp;hardware

Hardware to fizyczny sprzęt, zaś firmware to po prostu programy sterujące tym sprzętem.  
Spróbujcie sobie wpisać dowolną nazwę elementu i&nbsp;słowo *firmware*, a&nbsp;macie sporą szansę, że coś wyskoczy. `SSD firmware`. `Camera firmware`. `GPS firmware`.

Jak pisałem wyżej, proponuję rozdzielić to na dwie kategorie -- rzeczy kluczowe i&nbsp;poboczne.

Rzeczy poboczne oczywiście potrafią być wredne, ale ich możliwości są ograniczone.  
Mikrofon nie zaszkodzi nam sam z&nbsp;siebie. Jakiś wredny program musi najpierw kazać mu nas nagrać -- co się nie uda, jeśli jest fizycznie wyłączony -- a&nbsp;potem uzyskać dostęp do internetu, żeby wysłać to nagranie w&nbsp;świat.

Rzeczy kluczowe, jak procesor, są dużo ważniejsze. To sam dół naszej piramidy, więc wszystko od tego zależy. Do tego praktycznie wszystkie interakcje z&nbsp;innymi sprzętami muszą tędy przechodzić. To taki komputerowy węzeł komunikacyjny.

**Firmy mogą w&nbsp;tym miejscu dodawać rzeczy wrogie użytkownikom, a&nbsp;my mamy prawie zerowe możliwości walki**. Kto tu umie przestrajać układy scalone i&nbsp;łamać szyfry?

Stworzyłem kiedyś wpis na temat [Intel Management Engine]({% post_url 2021-07-27-intel-management-engine %}){:.internal} -- swoistego minikomputera od Intela. Zagnieżdżonego w&nbsp;tym kluczowym punkcie zapewne na życzenie ludków z&nbsp;Hollywood, pragnących zabezpieczeń antypirackich. Nieprzeniknionego, stanowiącego wymarzony cel dla hakerów.

A takich elementów tylko przybywa. Apple jakiś czas temu planowało wprowadzenie systemu [wykrywania i&nbsp;zgłaszania nielegalnych obrazków](https://cyberdefence24.pl/bezpieczenstwo-informacyjne/tlumaczymy-jak-bedzie-dzialal-system-apple-wykrywajacy-pornografie-dziecieca). Odpowiadałby za to specjalny chip od analizy obrazu, również zagnieżdżony na tym najgłębszym poziomie. Tam, gdzie użytkownik nie sięgnie.  

## Nasze możliwości

Choć każda warstwa może działać przeciwko nam, nie jesteśmy bezbronni.

W przypadku komputerów osobistych zwykle zachowujemy jakąś kontrolę nad swoim systemem. Poza tym nie jesteśmy naganiani na aplikacje.  
Nie oznacza to, że nikt nie będzie próbował nas śledzić. Ale łatwiej nam ograniczyć liczbę programów do minimum, a&nbsp;internetu używać głównie przez przeglądarkę.

W przypadku urządzeń mobilnych sytuacja jest moim zdaniem znacznie cięższa. Presję na dzielenie się danymi mamy zarówno ze strony zewnętrznych firm, jak i&nbsp;samych producentów.  
Tym niemniej wciąż jest parę rzeczy, które warto zrobić dla poprawienia prywatności.

### Unikanie aplikacji

Czasem, kiedy podczas przeglądania internetu wyświetla nam się nachalny baner naganiający dla aplikacji, możemy go obejść -- **udając że nie jesteśmy urządzeniem mobilnym**.

W tym celu wchodzimy w&nbsp;ustawienia przeglądarki. Zwykle znajdziemy tam opcję `Wersja na komputery`.  
Po jej kliknięciu strona powinna nam się załadować ponownie -- większa, cięższa i&nbsp;nieprzystosowana do urządzenia mobilnego... Ale działająca.

Jeśli kogoś interesuje, jak to działa za kulisami, to polecam mój wpis na temat *[user agenta]({% post_url 2021-06-11-user-agent %})*{:.internal}.

### Pozwolenia na smartfonach

W przypadku systemów mobilnych (zarówno Androida, jak i&nbsp;iOS) pewną kontrolę nad dzikimi apkami daje nam **system pozwoleń**. Sami możemy ustawiać, na co chcemy zezwolić poszczególnym aplikacjom.

Jak by to wyglądało na naszej piramidce? Ano tak, że wchodząc w&nbsp;ustawienia telefonu, poruszamy się po warstwie *systemu operacyjnego*. Możemy jednym pstryczkiem zablokować wybranej apce dostęp do mikrofonu.

Same aplikacje są warstwę wyżej, więc muszą porozumiewać się z systemem na jego zasadach. Chcąc coś nagrać, muszą grzecznie poprosić system. „Użyczysz mi mikrofonu?”. A&nbsp;jeśli nie daliśmy pozwolenia, to ten odmówi.  
W takiej sytuacji apka może co najwyżej wyświetlić nam komunikat o&nbsp;błędzie, ale nie jest w&nbsp;stanie zawetować naszej decyzji.

Ciemna strona pozwoleń? Niektóre rzeczy uznano na smartfonach za tak powszechne, że **nie wymagają pozwolenia. Taki przywilej ma na przykład łączność z&nbsp;internetem**. Dzięki temu każda apka może wysłać zebrane o&nbsp;nas informacje swoim twórcom.

Moja rada na teraz: wyłączmy aplikacjom jak najwięcej pozwoleń. Pozwolenie na mikrofon powinny mieć tylko te, których używamy do rozmów i&nbsp;nagrywania. Czyli najlepiej tylko systemowa apka *Aparat*. Możemy nim nagrywać, a&nbsp;potem przesyłać filmiki, wybierając je z&nbsp;apki *Galeria*.  
Z kolei dostęp do GPS-a powinna mieć tylko jedna wybrana apka, której używamy do nawigacji. Polecam *Mapy.cz*.

### Monitorowanie ruchu internetowego

Możliwość raczej nie dla każdego użytkownika, ale jak najbardziej realna.

Dane i&nbsp;pliki przesyłane między różnymi warstwami systemu są „martwe”. Nie oznacza to, że są niegroźne -- czasem czytanie danych wywołuje efekty uboczne. Swego czasu istniał chociażby „znaczek śmierci”, [zawieszający smartfony od Apple](https://serhack.me/articles/crash-iphone-telugu-character-en/).

Ale **dane nigdy nie zadziałają same z&nbsp;siebie. Zawsze musi je zacząć przetwarzać jakiś program**.

Co to nam daje? Załóżmy, że na naszym komputerze jest program szpiegowski. Zbiera o&nbsp;nas trochę informacji i&nbsp;wysyła je w&nbsp;świat przez internet.

Tylko że „wysłanie w&nbsp;świat” oznacza, że traci je z&nbsp;oczu. Użycie internetu oznacza, że zapewne muszą przejść przez nasz router. A&nbsp;„martwość” danych oznacza, że nie będą w&nbsp;stanie w&nbsp;żaden sposób się bronić przed przechwyceniem i&nbsp;skopiowaniem przez nas. Potem możemy je analizować.

W ten sposób każda osoba znająca się na rzeczy może regularnie monitorować ruch i&nbsp;patrzeć, czy aplikacja próbuje wysłać coś podejrzanego.  
Można podejść do sprawy śledzenia badawczo, zamiast tylko machać ręką i&nbsp;jojczeć „panie, te wszystkie apki śledzo”.

### Wybieranie otwartych rozwiązań

Nie jestem radykałem w&nbsp;kwestii wolnego oprogramowania. Cieszy mnie każda zmiana na plus, nawet drobna. Dopasowana do naszych chęci i&nbsp;możliwości.

Każdy, absolutnie każdy może na przykład zmieniać aplikacje na mniej wścibskie. Przeglądarkę Chrome zastąpić czymś otwartym poza kontrolą Wujka Google. Jak Brave albo Firefox.

Ale warstwę niżej nadal mamy potencjalnie wścibski system.  
Jeśli to Windows, a&nbsp;my nie potrzebujemy programów działających tylko na nim, to możemy spróbować go zmienić na system Linux. Polecam [Minta](https://linuxmint.com/).  
Jeśli Android, to można użyć systemu alternatywnego, takiego jak [LineageOS](https://lineageos.org/) albo [GrapheneOS](https://grapheneos.org/). Nie testowałem, ale często słyszę pochlebne opinie.

Ale pod systemem nadal mamy zamknięty, nieprzenikniony firmware. Zatem fani prywatności mogą spróbować przejść na eksperymentalne, alternatywne smartfony, jak Pinephone albo Librem. 

Ale nawet urządzenia najbardziej zorientowane na prywatność muszą polegać na paru zamkniętych modułach kupionych od innych firm, jak choćby modemy.  
W takim wypadku prawdziwi prywatnościowi puryści mogą mieć oko na ruch *[open hardware](https://en.wikipedia.org/wiki/List_of_open-source_hardware_projects)*, dążący do zbudowania wszystkiego na otwartych podstawach.

Każdy może znaleźć rozwiązanie dla siebie!  
Ale ogólnie warto rozglądać się za otwartymi, szanującymi prywatność alternatywami, żeby nie czuć się w&nbsp;tym świecie jak cielak do monetyzowania. Od razu przyjemniej się żyje.

Tym akcentem zakończę. W&nbsp;kolejnych wpisach dowiemy się więcej -- i&nbsp;na temat uprawnień, i&nbsp;metod śledzenia, i&nbsp;bezpieczniejszych alternatyw. Do zobaczenia! :smile:

## Źródła

* Piramida Maslowa autorstwa *Androidmarsexpress* (ze zbiorów Wikimedia Commons, licencja [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0));
* ikona [procesora](https://www.flaticon.com/free-icon/cpu_984391) -- Flaticon, autorstwa Freepik.
* ikona [strzałek](https://www.flaticon.com/free-icon/transaction_7789028) -- Flaticon, autorstwa NextGen;
* ikona [mikrofonu](https://emojipedia.org/microphone/) -- emoji od JoyPixels;
* ikona [sygnału wi-fi](https://www.flaticon.com/free-icon/wifi_2099193) -- Flaticon, autorstwa Freepik;
* ikona [aparatu fotograficznego]() -- emoji od Microsoftu;
* ikony programów Signal, Firefox, uBlock Origin, SingleFile.

