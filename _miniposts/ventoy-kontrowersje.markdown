---
layout: page
title: Kontrowersje wokół programu Ventoy
description: "Magicznie rozwiązuje problemy. Ale co, jeśli to czarna magia?"
---

Program o nazwie Ventoy wprowadził małą rewolucję w świecie instalowania systemów (głównie tych opartych na Linuksie, ale nie tylko).  
Tam, gdzie kiedyś był podzielony ekosystem, a sposobów instalacji było multum, zagościł teraz jeden intuicyjny program. Pozwala stworzyć jednego pendrive'a instalacyjnego, na którym może gościć wiele instalatorów. A potem, po wpięciu pendrive'a, można łatwo uruchomić dowolny z nich. Magia!

Ta magia znalazła się jednak pod lupą krytyków. Wskazują, że Ventoy ma swoje nieudokumentowane obszary, igra sobie z zabezpieczeniami systemu, a do tego byłby wymarzonym celem dla hakerów.  
W tym krótkim wpisie odniosę się do zarzutów i powiem, dlaczego osobiście mimo wszystko dałem Ventoyowi szansę, a nawet stworzyłem [mały przewodnik](/tutorials/ventoy){:.internal} po jego obsłudze.

## Lista wątpliwości

A zatem do dzieła! Lista kontrowersji wraz z moimi subiektywnymi komentarzami.

### Kraj pochodzenia autora

Autor Ventoya pochodzi z Chin.

Z pozoru czepianie się tego brzmi jak toporne uprzedzenia na tle narodowościowym, ale to niekoniecznie atak na człowieka.  
Komentujący mogą się obawiać, że państwo chińskie, widząc projekt popularny w cyberprzestrzeni, położy na nim ręce i dorzuci jakąś niespodziankę od siebie. Może wbrew autorowi, powołując się na interes kraju.

...Tylko że takie samo zagrożenie może wystąpić w przypadku innych, popularnych, całkiem zachodnich projektów, przejętych w sposób polubowny lub wrogi. Autor Ventoya nigdy nie ukrywał pochodzenia, do tego zwrócił na siebie uwagę. Jego projekt nie wydaje mi się przez to dobrym kandydatem na przykrywkę tajnej operacji.

### Brak przejrzystości

Choć kod źródłowy Ventoya jest publicznie dostępny, między czytelnymi fragmentami trafiają się nieprzejrzyste bloki zer i jedynek.

Sprawę [nagłośniono](https://github.com/ventoy/Ventoy/issues/2795) półtora roku temu. Wzbudziła uzasadnione obawy, bo w niejawnych i niezrozumiałych rzeczach mogą kryć się pułapki. Tak było w przypadku chociażby [przejęcia projektu XZ](/cyfrowy_feudalizm/2024/03/31/xz-backdoor){:.internal}; sprawy cytowanej zresztą w podlinkowanym wątku.

Ale autor [wyszedł tym zarzutom naprzeciw](https://github.com/ventoy/Ventoy/issues/3224), dokumentując pochodzenie niektórych modułów i wyjaśniając, że w pewnych przypadkach trudno było dorwać kod źródłowy, dlatego wybrał szybszą ścieżkę brania gotowców.  
Jego argumenty brzmią rozsądnie. Czasem szybciej i prościej jest wziąć gotowy, stworzony przez kogoś program (blok zer i jedynek) niż dobierać ustawienia i zależności, żeby stworzyć ten sam program od podstaw, na własnym komputerze. Zwłaszcza gdyby konfiguracja dla programu A była sprzeczną z tą dla programu B -- pojęcie „piekła zależności” jest znane i rozumiane w światku programistycznym.

Być może autor Ventoya woli dodawać nowe funkcje niż usprawniać fundamenty. Co jest pewną oznaką ludzkiej słabości (dość powszechnej). Ale niekoniecznie świadczy o złośliwości.

### Naciski na popularyzację programu

Pod filmikiem youtuberki o nicku *Veronica Explains* [pojawiały się komentarze](https://linuxmom.net/@vkc/112906968594601449) dość nachalnie zachęcające autorkę do zrobienia materiału u Ventoyu.

To również wzbudziło skojarzenia z aferą XZ, bo w jej kulminacyjnej fazie użyto trollkont do zwiększenia zasięgu rażenia. Trolle naciskały na osoby ze świata Linuksa, zachęcając do wprowadzenia najnowszej (i zainfekowanej, o czym nie mówiły) wersji programu do jak największej liczby systemów.

...Ale w społecznościach internetowych nie brakuje też całkiem realnych fanatyków, promujących ulubione rzeczy tam, gdzie tylko się da. Przydałaby się analiza komentarzy pod różnymi filmami, żeby wyłapać, czy narracja i zajadłość powtarzają się częściej (jak w przypadku [trolli od Monsanto](/2022/12/24/biotechnologia-trolle-youtube){:.internal}). Gdyby przypadki były jednostkowe, ograniczone do paru twórców -- to nie wierzyłbym w teorię o zorganizowanych naciskach.

### Oznaczenie przez antywirusy

Program iVentoy (tego samego autora, ale **nie ten Ventoy, o którym zrobiłem samouczek**) został [oznaczony przez program antywirusowy](https://github.com/ventoy/PXE/issues/106) jako złośliwy.

...Tyle że został oznaczony, bo dodaje własny certyfikat do listy zaufanych. A to działanie z gatunku szarej strefy, które nie musi być cyberatakiem. Autor [wyjaśnia](https://github.com/ventoy/PXE/issues/106#issuecomment-2857344318): iVentoy służy do załadowania systemu przez sieć, więc musi się z nią połączyć. Na bardzo wczesnym etapie uruchamiania. Do tego potrzeba sterownika.

No to autor znalazł jakiś otwarty (weryfikowalny, bezpieczny) sterownik sieciowy. Windows go odrzucał, bo jest rygorystyczny. Zatem autor „siłowo” oznaczył sterownik jako godny zaufania. To takie powiedzenie Windowsowi-pedantowi: „masz, daj mi spokój i uruchom się wreszcie”.

Obchodzenie ograniczeń systemu -- czasem sensownych, czasem upierdliwych -- nie jest w tych kręgach czymś dziwnym. Autorowi dostało się bardziej za to, że wyraźnie nie opisał użytego obejścia.

## Ufać czy nie ufać?

Podsumowując: wątpliwości jest na tyle, że można poczuć niepokój. Ale wiele rzeczy dałoby się też uzasadnić niefortunną kombinacją programistycznych sztuczek (żeby Ventoy działał tak płynnie jak działa) i odrobiną lenistwa w dokumentowaniu tychże sztuczek.

Dla mnie to wszystko to poziom magii, więc nie zweryfikuję nic od strony technicznej. Mogę tylko czytać i zestawiać w głowie różne opinie.

Osobiście **ufam nie tyle Ventoyowi, co branży cyberbezpieczeństwa**.

Obawy wobec projektu rozbrzmiały dość głośno (sam [wątek](https://github.com/ventoy/Ventoy/issues/2795) z kwietnia 2024 roku zebrał koło 700 reakcji na platformie Github). Sporo osób usłyszało o możliwym ryzyku ze strony Ventoya, zawołano „bezpieczników”.

Tacy ludzie mieliby wszelki interes w tym, żeby wyłapać ewentualne zagrożenia. W tym świecie reputacja jest wszystkim, a zapobiegnięcie cyberatakowi dałoby spory jej zastrzyk.  
Zakładam, że przez te półtora roku od czasu nagłośnienia obaw wzięli kod Ventoya pod lupę. Poskanowali, poanalizowali, również części nieprzejrzyste (mają ku temu narzędzia) -- ale nikt nie ogłosił jednoznacznie, że to zagrożenie.

A jeśli Ventoy teraz jest dobry, ale stanie się zły?

Może. Ale obstawiam, że od czasu nagłośnienia sprawy jego kod jest regularnie analizowany przez programy skanujące i przez to nieatrakcyjny dla hakerów. A gdyby mimo to go uzłośliwili -- to powinien rozbrzmieć alarm.

{:.post-meta .bigspace-after}
To właśnie firmy od automatycznych skanerów opublikowały w pierwszej kolejności [opis niedawnego cyberataku](https://news.ycombinator.com/item?id=45260741) (niezwiązanego z Ventoyem), wykorzystując okazję do zareklamowania swoich usług.  
Pokazuje to, że mają narzędzia i motywację. A mówimy tu o przypadku, gdy tylko asekuracyjnie monitorowały pewien ekosystem. Przy Ventoyu byłby to monitoring celowy i skupiony.

Jeśli przekonały cię moje argumenty i dopuszczasz teraz myśl o poznaniu Ventoya, to zapraszam do [samouczka](/tutorials/ventoy){:.internal}.
