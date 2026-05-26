---
layout: page
title: "Walka z Usługami Google na Androidzie (krótka wersja)"
description: "Obrazki wyrażają więcej niż tysiąc słów. A słowa też tu są."
---

W tym pomocniczym miniwpisie zebrałem kilka schematów pokazujących różne etapy **walki z&nbsp;aplikacją Usługi Google o&nbsp;kontrolę nad swoim smartfonem**. Pod każdym schematem znajdziecie rozwijane streszczenie całej sytuacji.

{:.post-meta .bigspace-after}
Z założenia nie ma to być wpis samowystarczalny, tylko uzupełnienie innych. Będę do niego linkował.

### Tryb domyślny

<img src="/assets/posts/google/uslugi-google-play/1-android-warstwy-google-play-dziala.png" alt="Trzy warstwy systemu Android w&nbsp;trybie domyślnym, przy włączonych Usługach Google Play. Najniższa warstwa, zawierająca Usługi, oznaczona jako niedostępna."/>

{% include details.html summary="Opis schematu" %}

{:.bigspace-before}
System Android został podzielony na tym schemacie na kilka poziomów, podpisanych po prawej stronie.  
Obszar środkowy (zielony) to strefa, w&nbsp;której użytkownicy mają najwięcej swobody. Mają m.in. możliwość odinstalowania lub przynajmniej dezaktywacji wielu aplikacji (obrazują to ikonki małych dźwigni).

Nie mają jednak wglądu w&nbsp;dwa miejsca:

* do warstwy nad sobą (plików wewnętrznych różnych aplikacji),
* do głębszych warstw systemu (nazwanych tu *jądrem* -- dość luźno, bez związku z&nbsp;oficjalną definicją).

W tym drugim miejscu znajdują się **Usługi Google**, mocno zżyte z&nbsp;różnymi funkcjami systemu. Zapewniają udogodnienia, ale za cenę komunikowania się z&nbsp;korporacją Google i&nbsp;ujawniania jej różnych, potencjalnie wrażliwych informacji. Na schemacie ich interakcje symbolizują strzałki między ikoną Google'a a&nbsp;ikoną Usług.

Od Usług Google zależy działanie niektórych aplikacji. Tutaj przykładem apki zależnej jest Sklep Google Play, zaś zależność symbolizuje linia przerywana.

{:.post-meta .bigspace-after}
Druga z&nbsp;przykładowych aplikacji, mobilny Firefox, może sprawnie działać bez Usług, ale nadal jest niedostępna dla użytkowników (ze względu na mechanizmy Androida). Stąd jej żółte tło.

{% include details-end.html %}

### Wyłączenie Usług Google przez opcje

<img src="/assets/posts/google/uslugi-google-play/2-android-warstwy-google-play-wylaczone.png" alt="Trzy warstwy systemu Android przy wyłączonych Usługach Google Play. Ikona Google i&nbsp;ich aplikacje są wyszarzone, nie działają."/>

{% include details.html summary="Opis schematu" %}

{:.bigspace-before}
Jak widać na pierwszym schemacie, przy Usługach Google'a widnieje ikonka dźwigni. A&nbsp;to oznacza, że chętni użytkownicy mogą je [wyłączyć przez oficjalne menu systemowe](https://www.ciemnastrona.com.pl/2024/02/03/smartfon-degoogle#fina%C5%82owy-boss--us%C5%82ugi-google-play){:.internal}.

Wyłączenie Usług w&nbsp;żadnym stopniu nie wpływa na układ warstw czy ich dostępność, więc większość schematu pozostaje bez zmian. W&nbsp;tym trybie przestają oczywiście działać same Usługi (dlatego ikona jest zaciemniona), a&nbsp;także ich komunikacja z&nbsp;Google'em. Co ma sporo zalet z&nbsp;punktu widzenia prywatności.

Efektem ubocznym jest natomiast brak możliwości korzystania z&nbsp;aplikacji, które były od Usług zależne. To dlatego cała ikona aplikacji Sklep Google Play stała się szara i&nbsp;widać na niej ikonkę błędu.

{:.post-meta .bigspace-after}
Choć sam zatrzymałem się na tym etapie, uprzedzam lojalnie, że nie jest to rozwiązanie dla każdego i&nbsp;wymaga znalezienia zamienników dla wielu aplikacji. Zachęcam natomiast do wyłączenia Usług na próbę, w&nbsp;ramach eksperymentu -- świetny sposób na ujrzenie patologicznego zrośnięcia Google'a z&nbsp;Androidem.

{% include details-end.html %}

### Rootowanie lub alternatywny system kontra Play Integrity

<img src="/assets/posts/google/uslugi-google-play/3-android-warstwy-root-albo-custom-rom.png" alt="Trzy warstwy systemu alternatywnego wobec Androida. Najniższa warstwa jest teraz oznaczona jako dostępna, ale ikona Google i&nbsp;ich aplikacje są wyszarzone, nie działają."/>

{% include details.html summary="Opis schematu" %}

{:.bigspace-before}
Zrootowanie telefonu i&nbsp;wgranie alternatywnego systemu to dwa różne zabiegi, prowadzące do niemal tego samego efektu -- **zyskania kontroli nad wcześniej niedostępnym, „głębszym” obszarem telefonu**.

{:.post-meta .bigspace-after}
W praktyce obszar dotąd czerwony staje się zielony jedynie po [*zrootowaniu* telefonu](https://wolnoscwkieszeni.pl/uwolnic-smartfona-2/), czyli zyskaniu uprawnień admina (językiem linuksowym: *roota*).  
Wbrew pozorom takie uprawnienia nie są normą nawet na otwartych systemach alternatywnych, bo ich brak ma zalety pod kątem cyberbezpieczeństwa. Warstwa dolna miałaby na nich kolor żółty. Ale zdecydowałem się na zielony, bo jeśli ktoś chce, to zwykle łatwo na nich uzyska *roota*.

Jeśli ktoś uzna, że chce skorzystać na tak zmienionym systemie z&nbsp;Usług Google albo apek od nich zależnych, to bardzo możliwe, że zderzy się z komunikatem o&nbsp;błędzie.

A to dlatego, że Usługi zawierają funkcję o&nbsp;nazwie **_Play Integrity_**. Polega ona na tym, że skanują na życzenie niektórych aplikacji swoje otoczenie. Wypatrują oznak tego, że otaczający je system został zmieniony i&nbsp;nie jest już typowym Androidem jak z&nbsp;pierwszego schematu.  
O swoich wątpliwościach mogą powiadomić zainteresowane aplikacje. Te zaś mogą świadomie odmówić działania i&nbsp;szantażować: „jeśli nie zresetujesz telefonu do postaci grzecznego Androida, to się nie włączę”.

Właśnie taki stan pokazuje schemat. Dolna warstwa już zielona, czyli dostępna. Usługi włączone. Ale zarówno one, jak i&nbsp;aplikacja zależna są oznaczone na szaro, niefunkcjonalne.

{:.post-meta .bigspace-after}
Zakładam tu niższy poziom weryfikacji. W&nbsp;takich warunkach istnieje parę sposobów, żeby oszukać Usługi -- choćby przez użycie aplikacji pokroju Magiska... Jednak zgodnie z&nbsp;[prawem Murphy'ego](https://pl.wikipedia.org/wiki/Prawa_Murphy%E2%80%99ego) zakładam, że jeśli obejścia mogą nie zadziałać, to nie zadziałają.

{% include details-end.html %}

### Instalacja systemu GrapheneOS

<img src="/assets/posts/google/uslugi-google-play/4-android-warstwy-graphene-os.png" alt="Trzy warstwy systemu GrapheneOS. Usługi Google są odgrodzone od reszty systemu i&nbsp;widać po kolorach, że działają prawidłowo"/>

{% include details.html summary="Opis schematu" %}

{:.bigspace-before}
Wśród otwartych, alternatywnych systemów jest jeden, który wyróżnia się pod kątem doszlifowania i&nbsp;może przełamać barierę z poprzedniego schematu. To **GrapheneOS**, który stosuje wobec Usług Google *sandboxing* (dosłownie „zamknięcie w&nbsp;piaskownicy”, w&nbsp;praktyce „odizolowanie”).

Intuicyjnie: Usługi Google zostają niejako umieszczone w&nbsp;makiecie systemu, stworzonej specjalnie dla nich. [Nie ma tam wrażliwych danych użytkowników](https://grapheneos.org/usage#sandboxed-google-play), więc ich nie dosięgną. Są tam za to imitacje rzeczy znanych Usługom z&nbsp;czystego Androida, z&nbsp;którego wyciągnęłyby co chcą. Mając do nich dostęp, powinny uznać system za niezmieniony i&nbsp;nie alarmować aplikacji zależnych po odpaleniu Play Integrity.

Odgrodzenie Usług obrazuje na schemacie pogrubiony kwadrat wypełniony czerwonym tłem, otaczający ich ikonę. Widać również, że cała komunikacja z&nbsp;Google'em i&nbsp;aplikacjami zależnymi działa jak na domyślnym systemie.

Bardzo chciałbym powiedzieć, że to niezawodny sposób na wygranie wojny o&nbsp;smartfona (zwłaszcza że Graphene nawiązał niedawno współpracę z&nbsp;Motorolą, co mogłoby go przybliżyć codziennym użytkownikom).  
Niestety niżej czeka jeszcze jeden schemat.

{% include details-end.html %}

### Weryfikacja Play Integrity na poziomie sprzętowym

<img src="/assets/posts/google/uslugi-google-play/5-android-warstwy-graphene-os-pokonany-trusted-computing.png" alt="Cztery warstwy systemu Graphene OS i&nbsp;przepływ informacji między Usługami Google a&nbsp;kryptograficznym chipem. Ikona Google i&nbsp;ich aplikacje są wyszarzone, nie działają"/>

{% include details.html summary="Opis schematu" %}

{:.bigspace-before}
Zainstalowanym systemem nadal jest tutaj Graphene OS, więc prawie wszystko jest jak na poprzednim schemacie. Tylko że tym razem, niestety, nawet on został pokonany.

Wewnątrz smartfonów tkwi bowiem niezależny chip kryptograficzny. Bywa nazywany różnie: w&nbsp;przypadku ogólnym to *TEE* (*Trusted Execution Environment*), ale czasem producenci chipów albo telefonów wypuszczają coś pod własną marką.  
Osobiście preferuję nazwę **enklawa**, podpatrzoną od ajfonów i&nbsp;podkreślającą izolację oraz niedostępność, czyli kluczowe cechy takich elementów.

Chip bierze udział w&nbsp;procesie uruchamiania systemu i&nbsp;zapisuje sobie informację o tym, czy to czysty, niezmieniany Android, czy też coś nietypowego. Okazuje swoje zapiski na życzenie Usługom Google Play -- w&nbsp;sposób oznaczony cyfrowo i&nbsp;niemożliwy do podrobienia -- jeśli apka zależna od Usług zechce poświadczenia na poziomie [`MEETS_DEVICE_INTEGRITY`](https://developer.android.com/google/play/integrity/overview#have-tiered) lub wyższym.

Po poznaniu prawdy o&nbsp;zmienionym systemie aplikacje mogą złośliwie odmówić działania. Tak robią: liczne aplikacje bankowe, Revolut, apki od gier online, a&nbsp;nawet... apka McDonalda.

Przeciw takiej barierze nawet GrapheneOS jest bezsilny i&nbsp;musi ulec. A&nbsp;wielu użytkowników nie interesuje przyczyna -- przyjmują, że skoro nie działa, to jest to wina niedopracowanych alternatyw i&nbsp;lepiej trzymać się Google'a. W&nbsp;ten sposób monopol Wielkiego G&nbsp;się cementuje.

{:.post-meta .bigspace-after}
A jeśli tego poziomu weryfikacji zaczną wymagać apki rządowe albo unijne, narzucone odgórnie jako obowiązkowe dla obywateli -- to czeka nas rządowo-googlowa dystopia i&nbsp;pogrom alternatyw. I&nbsp;niestety nie jest to przyszłość tylko teoretyczna.

{% include details-end.html %}
