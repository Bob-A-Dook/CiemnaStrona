---
layout: post
title: "Instalujemy uBlock Origin"
subtitle: "Tarcza, która cię osłoni (przed śledzeniem)."
description: "Tarcza, która cię osłoni (przed śledzeniem)."
date:   2021-10-21 10:00:00 +0100
tags: [Internet, Inwigilacja, Porady]
image: 
   path: /assets/posts/ublock-origin/google-vs-ublock-origin.jpg
   width: 1200
   height: 700
   alt: "Postać stoi naprzeciw smoka z logiem Google na głowie, trzymając ikonę uBlock Origin jak tarczę"
---

## Na szybko

Zwykle tworzę dłuższe teksty do spokojnego czytania. Ten będzie wyjątkiem.

Masz mało czasu. Nie chcesz czytać o&nbsp;prywatności w&nbsp;sieci. Ani grzebać w&nbsp;ustawieniach.  
Za 5-10 minut skończy Ci się cierpliwość i&nbsp;wrócisz do Fejsa, TikToka albo innych rozrywek.

Tyle nam wystarczy. W&nbsp;parę kliknięć poprawisz swoją prywatność w&nbsp;sieci.  
Jak? Dodając do swojej przeglądarki **uBlock Origin -- darmowy dodatek blokujący elementy śledzące** (tzw. *trackery*).

Będzie działał w&nbsp;tle i&nbsp;nawet go nie zauważysz. Za to Google, Facebook i&nbsp;inne wścibskie korpo przestaną widzieć, co robisz po opuszczeniu ich głównych stron.

{% include info.html type="Uwaga"
text="Użytkownicy Apple mogą być rozczarowani. Ten dodatek podobno nie działa na żadnej przeglądarce na iPhone'ach ani na nowszych (13+) wersjach Safari na Maca.  
Poza tym jeśli tylko masz możliwość użycia innych przeglądarek niż Chrome czy Edge, to gorąco zachęcam. Te dwie [mocno osłabiły uBO](/google/2022/05/11/google-manifest-v3){:.internal}. Zadziała na nich, ale nie rozwinie skrzydeł." %}

{:.post-meta .bigspace}
Jeśli odstrasza Cię pośpiech i&nbsp;jednak wolisz poczytać na spokojnie, możesz przejść [do dłuższej wersji wpisu]({% post_url 2021-10-21-ublock-origin-wiecej %}){:.internal}.

W rozwijanych zakładkach poniżej -- szybkie rozwianie częstych wątpliwości.

{% include details.html summary="Czy to bezpieczne?" %}
<a id="#czy-to-bezpieczne"/>

{:.bigspace-before}
Słuszne wątpliwości :+1:. Każdy dodatek do przeglądarki to mały programik, który może robić za kulisami coś podejrzanego.  
Na korzyść uBO i jego bezpieczeństwa przemawiają jednak solidne fakty.

{:.post-meta .bigspace-after}
Liczby ostatnio sprawdzane 30.05.2026 r., od tego czasu mogły się jeszcze poprawić :wink:

* Jego [kod źródłowy](https://github.com/gorhill/uBlock) jest publicznie dostępny i&nbsp;często wykorzystywany przez programistów.
  
  Oficjalną metodą „sklonowało” go ponad 4100&nbsp;osób. Wystawili mu ponad 65&nbsp;000 gwiazdek uznania.  
  Gdyby coś było nie tak, ktoś szybko wszcząłby alarm.

* uBO jest w&nbsp;wąskim gronie [27&nbsp;dodatków](https://addons.mozilla.org/en-US/android/search/?promoted=recommended&sort=users&type=extension) akceptowanych w&nbsp;mobilnej wersji Firefoksa.

  Mozilla -- firma reklamująca się dbaniem o&nbsp;prywatność -- za niego ręczy. Mają interes w&nbsp;tym, żeby porządnie go sprawdzać, bo inaczej ryzykowaliby własną reputacją.

* Oceny mówią same za siebie:

  <img width="500px" src="/assets/posts/ublock-origin/ubo-oceny.jpg" alt="Cztery małe zrzuty ekranu pokazujące oceny, jakie zebrał uBlock Origin w&nbsp;bazach dodatków Chrome'a, Firefoksa, Opery i&nbsp;Edge'a. We wszystkich ma w&nbsp;zaokrągleniu 5 gwiazdek wystawionych przez tysiące osób."/>

  {:.figcaption}
  Tu jeszcze stan z 2021 roku, nie aktualizowałem.  
  Źródło: oceny z&nbsp;archiwów [Chrome'a](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm), [Opery](https://addons.opera.com/en/extensions/details/ublock/), [Firefoksa](https://addons.mozilla.org/pl/firefox/addon/ublock-origin/) i&nbsp;Edge'a.

* Wszystkie pozwolenia, o&nbsp;jakie prosi ten dodatek podczas instalacji, są obszernie omówione [na jego stronie](https://github.com/gorhill/uBlock/wiki/Permissions).

{% include details-end.html %}

{% include details.html summary="„Ale ja już mam ad blockera”" %}
<a id="#ale-ja-już-mam-ad-blockera"/>

{:.bigspace-before}
Parę popularnych blokerów (jak AdBlock) to wydmuszki, które [za pieniądze przepuszczają reklamy sponsorów](/2023/10/26/adblock-nazwa){:.internal}.  
A nawet te z&nbsp;nich, które są fair, często są mniej skuteczne niż uBO.

Spójrzmy szybko na wykres skuteczności (procent blokowanych *trackerów* z&nbsp;gatunku tych sprytniejszych):

{:.figure}
<img width="600px" src="/assets/posts/ublock-origin/adblock-skutecznosc.jpg" alt="Pięć wykresów słupkowych dla różnych przeglądarek i&nbsp;dodatków, pokazujących procent blokowanych trackerów. Najwyższe słupki odpowiadają w&nbsp;każdym przypadku uBlock Origin, a&nbsp;najwyższy ze wszystkich jest ten dla nowej wersji uBlock Origin na Firefoksie"/>

{:.figcaption}
Źródło: [wpis na blogu](https://blog.apnic.net/2020/08/04/characterizing-cname-cloaking-based-tracking/) towarzyszący artykułowi naukowemu o&nbsp;*trackerach*.  
Edytowany przeze mnie.

Mamy 5 przeglądarek (nazwy pod wykresem).  
Dla każdej z&nbsp;nich pierwszy (niebieski) słupek to tryb normalny, bez dodatków. Widać że takie Adblock i&nbsp;Adblock Plus są od niego niewiele lepsze, czasem nawet gorsze (!).

Zaś ostatnie dwa słupki, ciemnozielony i&nbsp;czerwony, to uBlock Origin. Wersja nowa i&nbsp;nieco starsza. Są wyższe niż reszta, czyli więcej blokują.  
Wniosek: **uBO jest najskuteczniejszy, niezależnie od przeglądarki**.

{:.post-meta .bigspace-after}
Choć najlepszy na Firefoksie; warto spróbować tej kombinacji, jeśli tylko mamy możliwość.

{% include details-end.html %}

Przełamałem wątpliwości? To przejdźmy do instalacji.

## Instalacja

Poniżej zebrałem instrukcje instalacji dla różnych urządzeń. Kliknij je, żeby je rozwinąć.

{% include details.html summary="Na komputerze" %}

{:.bigspace-before}
Tak jak pisałem, uBlock Origin nie działa na nowej wersji Safari. Instalacja na innych przeglądarkach jest za to banalnie łatwa.

1. Wejdź na [stronę projektu uBlock Origin](https://github.com/gorhill/uBlock) i&nbsp;kliknij w&nbsp;link obok ikony twojej przeglądarki.
  
   {:.post-meta}
   Jeśli jej tam nie ma, to jest szansa, że zadziała wersja zainstalowana ręcznie, z&nbsp;pliku (ostatnia pozycja na liście, podpisana *Github -- Releases*. Jeśli ją wybierzesz, to zignoruj pozostałe punkty.

2. Przejdziesz na stronę oficjalnego archiwum dodatków. Kliknij tam przycisk „Instaluj” lub podobnie brzmiący.
3. Przeklikaj się przez okienka.  
   Jeśli odstraszają cię nazwy niektórych pozwoleń, o&nbsp;które prosi dodatek, możesz poczytać [ich uzasadnienie](https://github.com/gorhill/uBlock/wiki/Permissions). To nic groźnego!

{:.nospace}
{% include info.html
type="Porada"
text="uBO ma wprawdzie wersję na Chrome'a, która nawet działa, ale [wtedy sam Chrome działa przeciw nam](/google/2022/05/11/google-manifest-v3){:.internal}. Jest ściśle związany z&nbsp;Google i&nbsp;przesyła mu różne informacje (o ile nie pogrzebiemy w&nbsp;ustawieniach).  
Jeśli jesteśmy uparci i&nbsp;nie chcemy zmienić go na coś bardziej prywatnościowego (Firefox albo Brave), warto przynajmniej pomyśleć o&nbsp;przejściu na **Chromium**. To goła podstawa Chrome'a. Ma prawie identyczny wygląd i&nbsp;działanie, ale nie jest tak zrośnięty ze śledzącym gigantem."
%}
{% include details-end.html %}

{% include details.html summary="Na telefonach z&nbsp;Androidem" %}

{:.bigspace-before}
W przypadku Androida niestety niewiele przeglądarek wspiera dodatki. **Musisz mieć mobilnego Firefoksa** *albo Kiwi Browser*{:.corr-del} (niestety nie jest już rozwijana). Albo jakąś inną, o&nbsp;jakiej nie słyszałem. Ale na pewno nie żadne Chrome'y.  
Instalację pokażę tu na przykładzie mobilnego Firefoksa.

{:.post-meta .bigspace-after}
Którego zresztą polecam! Instalacja nie potrwa długo, a&nbsp;zyskamy jedną z&nbsp;niewielu nie-wścibskich przeglądarek na telefony.

Robimy tak:

1. Najpierw, jeśli jeszcze nie mamy mobilnego Firefoksa, pobieramy go i&nbsp;instalujemy;
2. Włączamy Firefoksa i&nbsp;przesuwamy palcem po ekranie, żeby z&nbsp;dołu wysunął się pasek z&nbsp;opcjami;
3. Wciskamy na nim ikonę trzech kropek po prawej;
4. Wybieramy z&nbsp;menu `Dodatki`, a&nbsp;potem `Zarządzaj dodatkami`;
5. Wyszukujemy na liście *uBlock Origin* i&nbsp;klikamy plusa przy jego nazwie, żeby go zainstalować. Gotowe!

{% include details-end.html %}

{% include details.html summary="Na telefonach „prywatnościowych” (Pinephone, Librem...)" %}

{:.bigspace-before}
Mowa tu o&nbsp;telefonach, które nie korzystają z&nbsp;popularnego Androida czy iOS, tylko z&nbsp;wersji systemu Linux dopasowanej do urządzeń mobilnych.  
Osobiście z nich nie korzystałem, ale myślę że warto szerzyć świadomość. Stąd ta krótka notka.

Jeśli wierzyć [temu wpisowi na temat Pinephone'a](https://www.kirsle.net/status-of-mobile-linux-apps-on-pinephone-screenshots), w&nbsp;ich przypadku najpierw pobieramy przeglądarkę (**wersję komputerową, a&nbsp;nie mobilną**), a&nbsp;następnie instalujemy na niej uBO. Jak na zwykłym komputerze (zob. wcześniejszą instrukcję).
{% include details-end.html %}

## Co dalej?

Jeśli tu jesteś, to jest szansa, że udało Ci się wytrzymać te kilka minut i&nbsp;zainstalować uBO. Gratulacje! :metal:

Na pozór nic się nie zmieniło. Cytując „Narrenturm” Sapkowskiego:

{:.bigspace}
> Koniec świata (...) nie nastąpił. Nie nastały Dni Kary i&nbsp;Pomsty. (...) Świat nie zginął i&nbsp;nie spłonął. Przynajmniej nie cały.  
Ale i&nbsp;tak było wesoło.

Ale wierz mi, że **od teraz uBO cały czas Cię chroni w&nbsp;tle**.  
Od teraz wiele firm śledzących Twoje kroki w&nbsp;sieci może się wypchać sianem.  
A stronki też jakieś takie lżejsze i&nbsp;szybsze bez reklamowego chłamu.

Jeśli masz jeszcze chwilę czasu, to zachęcam do przeczytania [rozszerzonej wersji wpisu]({% post_url 2021-10-21-ublock-origin-wiecej %}){:.internal}.  
Piszę w&nbsp;nim więcej o&nbsp;uBO, jego funkcjach i&nbsp;paru rzeczach, jakie można zrobić, żeby jeszcze lepiej Cię chronił.
