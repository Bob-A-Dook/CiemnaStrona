---
layout: post
title:  "Internetowa inwigilacja 1 – podstawy"
subtitle: "Nasze wizytówki, czyli nagłówki (HTTP)"
date:   2021-01-11 16:28:41 +0100
tags: [Internet, Inwigilacja, Porady]
category: internetowa_inwigilacja
category_readable: "Internetowa&nbsp;inwigilacja"
---

Zdarzyło Wam się podczas przeglądania internetu zderzyć się z&nbsp;blokadą? Albo odnieść wrażenie, że jakaś strona wie o&nbsp;Was więcej, niż byście chcieli?

{:.bigspace}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/wstep_kolaz.webp" alt="Różne komunikaty świadczące o tym, że strona rozpoznaje urządzenie albo lokalizację użytkownika. Między innymi 'Logowanie na nowym urządzeniu' i 'Ta treść nie jest dostępna w twoim regionie'."/>

Czasem stronki nie chcą nam czegoś pokazać. Albo jedna i&nbsp;ta sama reklama chodzi za nami po różnych, niezwią&shy;zanych ze sobą stronach. Albo wyświetla się (ale tylko na telefonie!) ponaglenie, żebyśmy zamiast stronki użyli aplikacji mobilnej.

Skąd oni to wszystko wiedzą?

Tej kwestii poświęcę serię wpisów *Internetowa inwigilacja*. Pokażę w&nbsp;nich różne metody, dzięki którym właściciele odwiedzanych stron mogą nas rozpoz&shy;nawać i&nbsp;zbierać o&nbsp;nas informacje.

To pierwszy z&nbsp;tych wpisów. Wprowadzę tutaj analogię ułatwiającą zrozumienie komunikacji przez internet. I&nbsp;pokażę, ile informacji wysyłamy właścicielom stron przy pierwszym kontakcie -- kiedy dopiero się „przedstawiamy” innemu komputerowi i&nbsp;jeszcze nawet nic nam nie odesłał.

## Internet jako poczta

Zacznę od odrobiny słowotwórstwa. *Inter* oznacza *między*, a&nbsp;*net* oznacza *sieć*. Czyli: *sieć* komputerów komunikujących się *między* sobą.

Jaki jest inny, bardziej swojski przykład sieci komunikacyjnej? Poczta!

* Zarówno szarzy obywatele (**klienci**), jak i&nbsp;większe organizacje (**serwery**) mogą sobie wysyłać listy i&nbsp;paczki.
* ...Przy czym zwykli ludzie częściej wysyłają lekkie listy z&nbsp;prośbami. A&nbsp;więksi gracze odpowiadają na ich prośby, odsyłając różne rzeczy w&nbsp;paczkach.
* Wszystko trzeba przesyłać przez placówki pocztowe. Zakładamy, że nie można tak po prostu podejść i&nbsp;przekazać bezpośrednio.
* Na kopertach/opakowaniach można umieszczać różnorodne informacje. Ale, żeby była możliwa dwustronna komunikacja, wśród tych informacji muszą być adresy odbiorcy i&nbsp;nadawcy (**adresy IP**).
* W&nbsp;odróżnieniu od prawdziwej poczty, biurokracja jest minimalna. Wszystko załatwiamy przez zaufaną panią z&nbsp;okienka (**przeglądarkę**), która już zna potrzebne informacje, sprawdzi adresy w&nbsp;katalogach itp. Wystarczy że powiemy, kogo i&nbsp;o co chcemy prosić.

Analogia nie jest w&nbsp;100% moja, podpatrzyłem różne jej części w&nbsp;internecie. Na przykład motyw wysyłanych kopert pojawia się m.in. [w&nbsp;tym filmiku](https://www.youtube.com/watch?v=ewrBalT_eBM).

{% include info.html type="Uwaga" text="Pomijam w&nbsp;tej analogii sporo rzeczy, jak na przykład to że dane są wysyłane w&nbsp;częściach, czasem następuje ponowne wysłanie, adres IP ma inne miejsce w&nbsp;hierarchii niż reszta informacji itp.  
Przyjmiemy dla uproszczenia, że **jeden list/paczka = wszystkie rzeczy wysłane podczas jednej interakcji**." %}

## Informacje w&nbsp;nagłówkach

Załóżmy, że chcemy zrobić najprostszą rzecz jaką się da. „Wejść” na dowolną stronkę internetową. Na przykład na listę wpisów z&nbsp;*ciemnastrona.com.pl*. To tylko trzy proste kroki:

1. Prosimy panią w&nbsp;okienku o&nbsp;stronę (*wpisujemy jej adres w&nbsp;pasku przeglądarki*);
2. Nasza prośba zostaje wysłana, ktoś (*serwer*) ją odbiera;
3. Odsyłają nam to, o&nbsp;co prosiliśmy (albo i&nbsp;nie)

Trzymając się analogii pocztowej: już nas znają na poczcie i&nbsp;wiedzą, że chcemy format taki a&nbsp;taki, mówimy po polsku itp. Więc kiedy mówimy w&nbsp;okienku, do kogo chcemy wysłać prośbę, po prostu biorą odpowiednią etykietę z&nbsp;tymi informacjami i&nbsp;naklejają ją na nasz list/paczkę. W&nbsp;świecie rzeczywistym taką etykietą z&nbsp;informacjami są **nagłówki HTTP**.

Przykładowy zestaw nagłówków w&nbsp;formie etykiety na paczce:

{:.bigspace}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/http_header_example.webp" alt="Lista nagłówków HTTP stylizowana na etykietę na paczce. Między innymi: User Agent, referer, pliki cookies, język."/>

Oprócz nich na opakowaniu -- ale w&nbsp;innym miejscu -- znajduje się również nasz adres IP.

Po wysłaniu naszej przesyłki tracimy nad nią kontrolę. Nie wiemy, co się z&nbsp;nią dalej dzieje. Odbiera ją adresat albo jakiś jego pełnomocnik -- w&nbsp;przypadku Ciemnej Strony serwer należący do amerykańskiej firmy, Githuba.

Nie wiemy, na które informacje z&nbsp;„etykiety” zwróci uwagę ani co z&nbsp;nimi zrobi. Może na ich podstawie na przykład:

* Uszanować prośbę.

  Czyli odesłać nam stronkę, o&nbsp;którą prosimy, uwzględniając informacje z&nbsp;etykiety; jeśli np. informacje mu wskażą, że korzystamy z&nbsp;urządzenia mobilnego, może nam od razu przesłać mniejszą wersję.

* Zignorować prośbę.

  Niektóre informacje z&nbsp;etykiety nie mają większego znaczenia albo trudno się do nich odnieść. Jeśli na etykiecie np. jest wskazane, że używamy języka polskiego, ale strona nie ma polskiej wersji, to tak czy siak dostaniemy wersję angielską.

* Dyskryminować nas.

  Co, jeśli na podstawie informacji serwer wywnioskuje że piszemy z&nbsp;Polski, a&nbsp;nie lubi Polaków? Może nam wtedy odesłać notkę „Nie mamy twojej strony, i&nbsp;co nam zrobisz?”. Albo inny, bardziej dyplomatyczny wariant tych słów. Najbardziej wkurzające w&nbsp;informacjach z&nbsp;nagłówków może być właśnie to, że często na ich podstawie blokuje się nam treść.

Jest jednak jeszcze jedna, może nawet gorsza możliwość. Niezależnie od działań widocznych na zewnątrz, serwer może:

* Gromadzić i&nbsp;analizować informacje

  Serwer zawsze może sobie zapisać komplet informacji o&nbsp;całej naszej interakcji: dokładny czas, nasz adres IP oraz wszystkie informacje z&nbsp;„etykiety”. Często je przechowuje w&nbsp;formie plików tekstowych, tak zwanych **logów**.

Do zapisanych informacji serwer może wrócić po dowolnym czasie, o&nbsp;ile nie zostaną do tego momentu usunięte. Co może z&nbsp;nimi zrobić?

Jeśli **będzie je tylko liczył**, to zakładam ostrożnie, że wiele nie zrobi. Zwłaszcza że informacje z&nbsp;nagłówków mogą się zmieniać albo nie być prawdziwe (sam Wam pokażę, jak je zmieniać :smiling_imp:).

Poza tym takie informacje często się powtarzają. Prawie każdy smartfoniarz zostanie odnotowany jako Android + Chrome + popularny język, ewentualnie jako iOS + Safari.

Ale co, jeśli odwiedzamy jedną stronę przez dłuższy czas i&nbsp;ciągle używamy dość unikalnej kombinacji (np. ustawiony język suahili + system operacyjny Linux + jakaś niszowa przeglądarka)?

Wtedy ktoś analizujący logi może słusznie założyć, że jesteśmy jedną i&nbsp;tą samą osobą.  
Potem, nawet jeśli nie znają naszej tożsamości, mogą ująć nas w&nbsp;statystykach jako pojedynczego bywalca. Trochę w&nbsp;stylu Spotify'a:

{:.figure}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/spotify_reklama.webp" alt="Billboard z napisem 'Dear Person in TriBeCa who listened to Cheap Thrills 955 times this year. Were all the expensive thrills taken?'"/>

{:.figcaption}
Źródło: [Tribeca Citizen](https://tribecacitizen.com/2017/01/02/seen-heard-did-disney-bail-on-the-world-trade-center-mall/)

A szczególnie sadystyczny administrator może zostawić serwerowi instrukcję w&nbsp;stylu „Jeśli fotkę tego kota po raz setny wyświetli ten świr z&nbsp;Linuxem + dziwną przeglądarką + ustawionym językiem suahili, to zacznij wyświetlać że kitka nie ma, bo zaoglądany na śmierć”.

Poza tymi wydumanymi przykładami zwykłe liczenie informacji z nagłówków nie jest dla nas groźne.

Jeśli natomiast serwer **zacznie analizować zebrane informacje i&nbsp;łączyć je z&nbsp;innymi**, to może zdziałać zadziwiająco wiele, w&nbsp;tym również rozpoznawać nas jako konkretną jednostkę i&nbsp;śledzić nasze działania.

Kolejne wpisy będą poświęcone tym możliwościom. Jest spora szansa, że będziecie równie zaskoczeni jak ja, kiedy po raz pierwszy się o&nbsp;tym dowiedziałem.

A tymczasem możemy się tutaj zatrzymać, jeśli chodzi o&nbsp;dawkę informacji. Więcej w&nbsp;kolejnych wpisach! :wink:

Jeśli natomiast chcecie zobaczyć, jak osobiście sprawdzać nagłówki, to zapraszam do krótkiego samouczka. Osoby na każdym poziomie dadzą radę -- są tu dwa skróty klawiszowe, kilka kliknięć i&nbsp;brak ryzyka, że coś się popsuje.

## Bonus: Jak sprawdzać nagłówki HTTP

Chcesz sprawdzić, co jest naklejone na Twoją przesyłkę?

Najprostsze rozwiązanie -- możesz to zrobić na przykład przez stronkę [Web Sniffer](https://websniffer.cc/my). Pod linijką *Request Header* zobaczysz, co wysłało Twoje urządzenie na jej serwer. To dobra opcja, jeśli korzystasz z&nbsp;urządzenia mobilnego.

{% include info.html type="Ciekawostka" text="Tę stronkę już podawałem jako przykład w&nbsp;pierwszym wpisie. Jest na niej jedna reklama Google'a, bo nie znalazłem niczego, co by pokazywało informacje z&nbsp;nagłówków HTTP i&nbsp;było wolne od reklam/analityki. Waga strony bez reklamy to ok. 4 kB. Waga strony po załadowaniu całej reklamy, to ok. 1,5 MB (ponad 375 razy więcej; głównie elementy śledzące) :roll_eyes:" %}

Jeśli natomiast masz dostęp do komputera, to nie trzeba odwiedzać żadnej strony, wszystkie informacje masz na miejscu.

Pokażę to na przykładzie Firefoksa, ale narzędzia Chrome'a są bliźniaczo podobne.

Najpierw naciskamy `Ctrl+Shift+I` (jak „Irena”). Pojawi się okno ze szczegółowymi informacjami -- w&nbsp;Firefoksie na dole, w&nbsp;Chrome'ie po prawej stronie ekranu.

Okno na dole jest moim zdaniem mało wygodne. W&nbsp;obu przeglądarkach możemy zmienić układ, klikając w&nbsp;opcje w&nbsp;prawym górnym rogu i&nbsp;wybierając np. `Wyświetlaj z prawej`:

{:.figure .bigspace}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/devtools_layout.webp" alt=""/>

Klikamy zakładkę `Sieć` w&nbsp;górnym pasku:

{:.figure .bigspace}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/devtools_network.webp" alt="Górny pasek narzędzi przeglądarki Firefoksa z zaznaczoną opcją 'Sieć'"/>

Naciskamy `F5`, żeby odświeżyć stronę. Okno zapełni się listą rzeczy, o&nbsp;które poprosiła nasza przeglądarka. Klikamy dowolną z nich, na przykład pierwszą od góry:

{:.figure .bigspace}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/devtools_first_file.webp" alt="Lista stron, do których przeglądarka wysłała żądanie. Zaznaczony główny plik html."/>

Pojawi się okno ze szczegółowymi informacjami. Klikamy w nim zakładkę `Nagłówki`:

{:.figure .bigspace}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/devtools_headers.webp" alt="Dolny pasek narzędzi przeglądarki Firefoksa z zaznaczoną opcją 'Nagłówki'"/>

Pod spodem wyświetlą się dwie listy -- najpierw lista nagłówków, jakie dostaliśmy od serwera (*Nagłówki odpowiedzi*), a&nbsp;pod spodem nagłówki wysłane przez nas, nasza „etykieta” (*Nagłówki żądania*). To o&nbsp;tym mówiłem przez cały wpis.

{:.figure .bigspace}
<img src="/assets/posts/internetowa-inwigilacja-1-podstawy/naglowki_odpowiedzi.webp" alt="Lista nagłówków żądania"/>

{% include info.html type="Ciekawostka" text="Jeśli spojrzysz na kolumnę 2 głównej listy (*Domena*), to zobaczysz że większość rzeczy pochodzi z&nbsp;*ciemnastrona.com.pl*. Część jednak przybyła z&nbsp;domeny *github.githubassets.com*.  
To strona zewnętrzna i&nbsp;to nie ją odwiedzasz. Mimo to, jeśli spojrzysz na nagłówki, zobaczysz że dostała prawie wszystko to, co nasza Ciemna Strona.  
Tak niestety jest -- odwiedzane przez nas strony to często straszni plotkarze i&nbsp;**od razu przekazują innym informacje o&nbsp;odwiedzających**. Nigdy nie zakładajmy, że wysłanie czegoś pozostanie prywatną sprawą między nami a&nbsp;stroną.  
W tym przypadku odnośniki na szczęście nie zdradzają tajemnic. To taka wygodna opcja korzystania z&nbsp;ikonek emoji od Githuba. Który zapewnia hosting Ciemnej Stronie, więc tak czy siak widziałby wszystkie etykiety.  
A do plotkarskich stron jeszcze wrócimy. Trzymajcie się i&nbsp;do zobaczenia! :metal:" %}


