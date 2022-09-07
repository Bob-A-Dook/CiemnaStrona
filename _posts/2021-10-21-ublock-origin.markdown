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

image-width: 900
image-height: 669
---

## Na szybko

Zwykle tworzę dłuższe teksty do spokojnego czytania. Ten będzie wyjątkiem.

Masz mało czasu. Nie chcesz czytać o&nbsp;prywatności w&nbsp;sieci. Ani grzebać w&nbsp;ustawieniach.  
Za 5 minut skończy Ci się cierpliwość i&nbsp;wrócisz do Fejsa, Tik-Toka albo innych rozrywek.

Te 5 minut nam wystarczy. W&nbsp;parę kliknięć poprawisz swoją prywatność w&nbsp;sieci.  
Jak? Dodając do swojej przeglądarki **uBlock Origin -- darmowy dodatek blokujący elementy śledzące** (tzw. *trackery*).

Będzie działał w&nbsp;tle i&nbsp;nawet go nie zauważysz. Za to Google, Facebook i&nbsp;inne wścibskie korpo przestaną widzieć, co robisz po opuszczeniu ich głównych stron.

{% include info.html type="Uwaga" text="Użytkownicy Apple mogą być rozczarowani. Ten dodatek podobno nie działa na żadnej przeglądarce na iPhone'ach ani na nowszych (13+) wersjach Safari na Maca." %}

{:.post-meta .bigspace}
Jeśli odstrasza Cię pośpiech i&nbsp;jednak wolisz poczytać na spokojnie, możesz przejść [do dłuższej wersji wpisu]({% post_url 2021-10-21-ublock-origin-wiecej %}){:.internal}.

# Czy to bezpieczne?

Słuszne wątpliwości :+1:. Każdy dodatek do przeglądarki to mały programik, który może robić za kulisami coś podejrzanego.  
Na korzyść uBO przemawiają solidne fakty:

* Jego [kod źródłowy](https://github.com/gorhill/uBlock) jest publicznie dostępny i&nbsp;często wykorzystywany przez programistów.
  
  Oficjalną metodą „sklonowało” go ponad 2100 osób. Wystawili mu ponad 26&nbsp;000 gwiazdek uznania.  
  Gdyby coś było nie tak, ktoś szybko wszcząłby alarm.

* uBO jest w&nbsp;wąskim gronie [16 dodatków](https://addons.mozilla.org/en-US/android/search/?promoted=recommended&sort=users&type=extension) akceptowanych w&nbsp;mobilnej wersji Firefoksa.

  Mozilla -- firma reklamująca się dbaniem o&nbsp;prywatność -- za niego ręczy. Mają interes w&nbsp;tym, żeby porządnie go sprawdzać, bo inaczej ryzykowaliby własną reputacją.

* Oceny mówią same za siebie:

  <img width="500px" src="/assets/posts/ublock-origin/ubo-oceny.jpg" alt="Cztery małe zrzuty ekranu pokazujące oceny, jakie zebrał uBlock Origin w&nbsp;bazach dodatków Chrome'a, Firefoksa, Opery i&nbsp;Edge'a. We wszystkich ma w&nbsp;zaokrągleniu 5 gwiazdek wystawionych przez tysiące osób."/>

  {:.figcaption}
  Źródło: Oceny z&nbsp;archiwów [Chrome'a](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm), [Opery](https://addons.opera.com/en/extensions/details/ublock/), [Firefoksa](https://addons.mozilla.org/pl/firefox/addon/ublock-origin/) i&nbsp;Edge'a.

* Wszystkie pozwolenia, o&nbsp;jakie prosi ten dodatek podczas instalacji, są obszernie omówione [na jego stronie](https://github.com/gorhill/uBlock/wiki/Permissions).

# „Ale ja już mam *ad blockera*”

Parę popularnych blokerów (jak AdBlock) to wydmuszki, które za pieniądze przepuszczają reklamy sponsorów.  
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

Przełamałem wątpliwości? To przejdźmy do instalacji.

## Instalacja

Poniżej zebrałem instrukcje instalacji dla różnych urządzeń. Kliknij je, żeby je rozwinąć.

<details>
<summary class="bigspace"><strong>Na komputerze</strong></summary>

<p>Tak jak pisałem, uBlock Origin nie działa na nowej wersji Safari.<br/>Dla innych popularnych przeglądarek sprawa jest łatwa.</p>
<ol>
<li>Wejdź na <a href="https://ublockorigin.com/">stronę główną dodatku</a> i&nbsp;tam kliknij w&nbsp;link do instalacji<br/> (powinien automatycznie dopasować się do Twojej przeglądarki).</li>
<li>Przejdziesz na stronę oficjalnego archiwum dodatków. Kliknij tam przycisk „Instaluj” lub podobnie brzmiący;</li>
<li>Przeklikaj się przez okienka.<br/>Jeśli odstraszają cię nazwy niektórych pozwoleń, o&nbsp;które prosi dodatek, możesz poczytać <a href="https://github.com/gorhill/uBlock/wiki/Permissions">ich uzasadnienie</a>. To nic groźnego!</li>
</ol>

{% include info.html type="Porada" trailer="
<p>uBO ma wprawdzie wersję na Chrome'a i&nbsp;nawet działa, ale <strong>wtedy sam Chrome jest naszą największą słabością</strong>. Jest ściśle związany z&nbsp;Google i&nbsp;przesyła mu różne informacje (o ile nie pogrzebiemy w&nbsp;ustawieniach).<br/>
Jeśli jesteśmy uparci i&nbsp;nie chcemy zmienić go na coś bardziej prywatnościowego (Firefox albo Brave), warto przynajmniej pomyśleć o&nbsp;przejściu na Chromium.<br/>To goły silnik Chrome'a. Ma prawie identyczny wygląd i&nbsp;działanie, ale nie jest tak mocno zintegrowany ze śledzącym gigantem.</p>" %}
</details>

<details>
<summary class="bigspace"><strong>Na telefonach z&nbsp;Androidem</strong></summary>
<p>W przypadku Androida nie każda przeglądarka wspiera dodatki. <strong>Musisz mieć mobilnego Firefoksa albo Kiwi Browser</strong> (albo jakąś inną, o&nbsp;jakiej nie słyszałem. Ale na pewno nie żadne Chrome'y).</p>
<p>Kiwi Browser jeszcze nie testowałem, więc nie będę o&nbsp;niej mówił. Pokażę instalację na przykładzie mobilnego Firefoksa (którego zresztą polecam! Waży 70 MB, instalacja nie potrwa długo, a&nbsp;jest jedną z&nbsp;niewielu nie-wścibskich przeglądarek na telefony).</p>
<ol>
<li>Najpierw, jeśli jeszcze nie mamy mobilnego Firefoksa, pobieramy go i&nbsp;instalujemy;</li>
<li>Włączamy Firefoksa i&nbsp;przesuwamy palcem po ekranie, żeby z&nbsp;dołu wysunął się pasek z&nbsp;opcjami;</li>
<li>Wciskamy na nim ikonę trzech kropek po prawej;</li>
<li>Wybieramy z&nbsp;menu <code>Dodatki</code>, a&nbsp;potem <code>Zarządzaj dodatkami</code>;</li>
<li>Wyszukujemy na liście <i>uBlock Origin</i> i&nbsp;klikamy plusa przy jego nazwie, żeby go zainstalować. Gotowe!</li>
</ol>
</details>

<details>
<summary class="bigspace"><strong>Na telefonach „prywatnościowych” (Pinephone, Librem...)</strong></summary>

<p>Mowa tu o&nbsp;telefonach, które nie korzystają one z&nbsp;popularnego Androida czy iOS, tylko z&nbsp;Linuxa dopasowanego do urządzeń mobilnych.</p>
<p>Jeśli wierzyć <a href="https://www.kirsle.net/status-of-mobile-linux-apps-on-pinephone-screenshots">temu wpisowi na temat Pinephone'a</a>, w&nbsp;ich przypadku najpierw pobieramy przeglądarkę (<strong>wersję komputerową, a&nbsp;nie mobilną</strong>), a&nbsp;następnie instalujemy na niej uBO.<br/>
Czyli dokładnie jak w&nbsp;przypadku komputerów (patrz wyżej).</p>
</details>

## Co dalej?

Jeśli tu jesteś, to jest szansa, że udało Ci się wytrzymać te kilka minut i&nbsp;zainstalować uBO. Gratulacje! :metal:

Na pozór nic się nie zmieniło. Cytując „Narrenturm” Sapkowskiego:

{:.bigspace}
> Koniec świata (...) nie nastąpił. Nie nastały Dni Kary i&nbsp;Pomsty. (...) Świat nie zginął i&nbsp;nie spłonął. Przynajmniej nie cały.  
Ale i&nbsp;tak było wesoło.

Ale wierz mi, że od teraz uBO cały czas Cię chroni w&nbsp;tle.

Od teraz wiele firm śledzących nasze kroki w&nbsp;sieci może się wypchać sianem.  
A stronki też jakieś takie lżejsze i&nbsp;szybsze bez reklamowego chłamu.

Jeśli masz jeszcze chwilę czasu, to zachęcam do przeczytania [rozszerzonej wersji wpisu]({% post_url 2021-10-21-ublock-origin-wiecej %}){:.internal}.

Piszę w&nbsp;nim więcej o&nbsp;uBO, jego funkcjach i&nbsp;paru rzeczach, jakie można zrobić, żeby jeszcze lepiej nas chronił.
