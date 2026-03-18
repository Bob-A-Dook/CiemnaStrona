---
layout: post
title: "Firefox ujawnia miniaturki filmów? Prywatnościowa ciekawostka"
subtitle: "Okruchy dla podglądaczy mogą leżeć w najmniej oczekiwanych miejscach."
description: "Okruchy dla podglądaczy mogą leżeć w najmniej oczekiwanych miejscach."
date:   2026-03-13 17:00:00 +0100
tags: [Inwigilacja, Podstawy]
image:
  path: /assets/posts/inwigilacja/firefox-mpris/firefox-mpris-baner.jpg
  width: 1200
  height: 700
  alt: "Zdjęcie cytryny odbijającej się w lustrze. Jej oryginał to czarny kontur ze znakiem zapytania, stojący obok loga Firefoksa. W lustrze podpisanym firefox-mpris odbija się jej prawdziwa postać, na którą nałożono miniaturkę filmu."
---

Wiosna za rogiem, czas się budzić ze snu zimowego i&nbsp;dodać jakieś wpisy na stronie głównej :smile:

Systemy operacyjne i&nbsp;przeglądarki internetowe można uznać, z&nbsp;perspektywy użytkowników, za fundamenty współczesnego cyfrowego świata.  
Te pierwsze umożliwiają podporządkowanie sobie urządzeń elektronicznych, jak laptopy czy smartfony. Te drugie pozwalają nawigować po oceanie internetu.

W każdej z&nbsp;tych dwóch kategorii istnieje co najmniej kilka znaczących opcji, różniących się pod względem stopnia „korporatyzacji”, a&nbsp;także szanowania prywatności swoich użytkowników.

Zestawiając ze sobą skrajności: systemy na bazie otwartego, darmowego [Linuksa](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal} bardziej szanują użytkowników niż Windows od Microsoftu. Zaś przeglądarka Firefox chroni prywatność o&nbsp;niebo lepiej niż Chrome.

{:.post-meta .bigspace-after}
Choć czasem niestety też się [mizia ze światem reklam](/2024/08/27/make-firefox-private){:.internal}.

Tym ciekawsza jest w&nbsp;tych realiach sytuacja, kiedy jedynie po połączeniu dwóch prywatniejszych rzeczy, Linuksa i&nbsp;Firefoksa, ujawnia się jakąś informację na swój temat.  
Może niezbyt groźną, niemal nieistotną na tle innych danych... ale bez wątpienia istniejącą i&nbsp;możliwą do wykorzystania.

Takie coś odkryłem na swoim komputerze. **Podczas odtwarzania niektórych filmów Firefox tworzy ich tymczasowe miniaturki** w&nbsp;folderze ukrytym, ale domyślnie ogólnodostępnym.  
Gdyby ktoś miał u&nbsp;siebie zainstalowany jakiś wścibski program, to mógłby on co pewien czas, bez łamania żadnych zabezpieczeń, zerkać tam i&nbsp;odgadywać po miniaturach, co akurat oglądamy.

Nie uważam tego za powód do alarmu, stąd „ciekawostka” w&nbsp;tytule. Tym niemniej warto ją poznać.  
Zapraszam!

{:.bigspace-before}
<img src="/assets/posts/inwigilacja/firefox-mpris/firefox-mpris-baner.jpg" alt="Zdjęcie cytryny odbijającej się w&nbsp;lustrze. Jej oryginał to czarny kontur ze znakiem zapytania, stojący obok loga Firefoksa. W&nbsp;lustrze podpisanym firefox-mpris odbija się jej prawdziwa postać, na którą nałożono miniaturkę filmu."/>

{:.figcaption}
Źródło: [zdjęcie cytryny](https://www.freepik.com/free-photo/lime-blue-table-isolated-orange_7727489.htm) ze strony Freepik (autor: *drobotdean*). Przeróbki moje.

## Odkrycie

Wierzcie lub nie, ale odkrycia dokonałem zupełnym przypadkiem, szukając sposobu na instalowanie dodatku [uBlock Origin](/2021/10/21/ublock-origin){:.internal} automatycznie, bez uruchamiania przeglądarki. W&nbsp;tym celu zajrzałem do jej plików wewnętrznych, słuchając sobie filmu z&nbsp;YouTube'a w&nbsp;tle (ważne!).

{:.post-meta .bigspace-after}
Gwoli ścisłości: korzystałem z&nbsp;Librewolfa, czyli przeglądarki opartej na Firefoksie i&nbsp;jeszcze bardziej uszczelnionej pod kątem prywatności. Ale ma to minimalne znaczenie, dlatego przez większość wpisu będzie o&nbsp;Firefoksie.

{% include info.html
type="Więcej o&nbsp;tych plikach"
text="W przypadku Linuksa po pierwszym uruchomieniu przeglądarki Firefox powstaje, w&nbsp;folderze domowym (tym domyślnym, gdzie są podfoldery *Muzyka*, *Dokumenty* itd.), ukryty folder na różne rzeczy.  
Jeśli przeglądarka to zwykły Firefox, to folder nosi nazwę `.mozilla` (od firmy). W&nbsp;przypadku opartego na nim Librewolfa nazywa się `.librewolf`."
%}

Moim oczom ukazał się folder o&nbsp;nazwie `firefox-mpris`. Kolejny szczęśliwy traf, bo nazwa podstawowego Firefoksa rzucała się w&nbsp;oczy w&nbsp;folderach Librewolfa, z&nbsp;którego akurat korzystałem. W&nbsp;innym wypadku mógłbym ją pominąć, a&nbsp;tak przyciągnęła wzrok. Zajrzałem do środka.

A tam ujrzałem pojedynczy plik. Format PNG, czyli obrazek. **Przedstawiał miniaturkę filmu, który akurat oglądałem**.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/firefox-mpris/firefox-mpris-miniaturka.png" alt="Zrzut ekranu pokazujący miniaturkę filmu, z&nbsp;tekstem 'Kurzgesagt Propaganda'" />

## Obserwacje

Nazwa pliku to ciąg kilku cyfr, po których pojawia się podkreślnik. A&nbsp;po nim kolejna liczba.

Ta pierwsza liczba wbrew pozorom nie jest losowa; to **numer procesu** odpowiadającego uruchomionemu Firefoksowi. Coś, co jest przydzielane przez system każdemu działającemu programowi, ale rzadko widoczne dla użytkowników.

{:.post-meta .bigspace-after}
To dokładnie ta sama liczba, którą wyświetliłby program `xprop` po kliknięciu okna Firefoksa.  
Swoją drogą: przydatna właściwość, gdyby ktoś chciał ustalić numer procesu najprostszymi narzędziami, bez konsoli czy włączania Monitora Systemu.

Druga liczba z&nbsp;kolei zaczyna się od zera i&nbsp;rośnie o&nbsp;1 z każdym kolejnym załadowanym filmem. Do jakiej wartości? Na pewno osiąga dwucyfrową, tyle sprawdziłem. Nie testowałem limitów, a&nbsp;w kodzie źródłowym Lisa/Wilka nie planuję póki co szperać.

Z ciekawości zacząłem sobie eksperymentować i&nbsp;sprawdzać, w&nbsp;jakich sytuacjach pojawia się miniaturka.

Jak się okazuje -- pokazywała się za każdym razem, kiedy odtwarzałem w&nbsp;przeglądarce jakiś film ze strony **_youtube.com_**. I&nbsp;znikała wraz z&nbsp;całym folderem `firefox-mpris`, kiedy zamknąłem kartę, w&nbsp;której ten film się znajdował (samo wciśnięcie pauzy nic nie zmieniało).

{% include details.html summary="Inne obserwacje" %}

{:.bigspace-before}
Parę innych, mniej znaczących ciekawostek dotyczących działania miniaturki:

* zawsze widoczna była u&nbsp;mnie tylko jedna miniaturka naraz;
* gdybym w&nbsp;trakcie odtwarzania pierwszego filmu zaczął odtwarzać też inny, w&nbsp;osobnej karcie, to miniaturka by się zmieniła i&nbsp;pokazywała ten później włączony;
* czasem jednak nie była na bieżąco z&nbsp;odtwarzanym filmem, zwłaszcza jeśli przełączałem się między filmami przez pauzowanie jednego i&nbsp;odtwarzanie drugiego;
* gdybym akurat miał w&nbsp;przeglądarce plików wyświetloną zawartość folderu z&nbsp;miniaturą, to po przełączeniu na nowy film (np. wskutek autoodtwarzania) by mnie z&nbsp;tego folderu wyrzuciło do nadrzędnego.

  Przyczyna? Według moich obserwacji Firefox nie ogranicza się do zmiany samej miniatury, tylko usuwa i&nbsp;dodaje od nowa cały folder.

{% include details-end.html %}

Sprawdziłem, czy miniaturka pojawia się również w&nbsp;przypadku PeerTube'a, a&nbsp;nawet znanej stronki z&nbsp;filmami mniej familijnymi -- czego się nie robi dla nauki!  
Nie pojawiała się. Ulga, zwłaszcza w&nbsp;tym drugim przypadku :smile:

Kiedy już się znudziłem eksperymentowaniem, to wyszukałem w&nbsp;DuckDuckGo tekstu `firefox-mpris`, żeby znaleźć jakieś pewniejsze źródło wyjaśniające całą sprawę.

## Wyjaśnienie

Kluczem jest tutaj słowo `mpris` w&nbsp;nazwie folderu. To akronim oznaczający [*Media Player Remote Interfacing Specification*](https://wiki.archlinux.org/title/MPRIS). Standard pozwalający dzielić się z&nbsp;systemem informacjami o&nbsp;multimediach.

Na Linuksach istnieje coś takiego jak **_D-Bus_**. To, mówiąc ogólnie, sposób na przekazywanie systemowi informacji przez różne programy, w&nbsp;sposób ustandaryzowany, żeby ten mógł lepiej wszystko ze sobą integrować. MPRIS to jego część.

Linux, na którym wszystko sprawdzałem, był oparty na względnie minimalistycznym środowisku (MATE) i&nbsp;nie wykorzystywał możliwości MPRIS. Nic mi się nie pokazywało poza miniaturą w&nbsp;folderze.

Inne środowiska, jak Cinnamon, potrafią lepiej wykorzystywać to udogodnienie.

Jeśli podczas odtwarzania filmu kliknie się kontrolkę odpowiedzialną za dźwięk na systemowym pasku, to pojawia się miniatura oraz trochę informacji na temat odtwarzanego klipu.

{:.figure .bigspace}
<img src="/assets/posts/inwigilacja/firefox-mpris/linux-miniatura-ogladanego-filmu.jpg" alt="Zrzut ekranu pokazujący kontrolkę odpowiedzialną za głośność. Nad nią wyświetla się tytuł filmu 'Czy Kurzgesagt tworzy propagandę dla miliarderów?', a&nbsp;także miniaturka przedstawiająca mężczyzn w&nbsp;garniturach"/>

{:.post-meta .bigspace-after}
Miniaturka byłaby widoczna również na ekranie logowania. Czy to dobrze, czy źle -- zależy od człowieka (i&nbsp;pewnie od filmiku).

Jak widać, to całkiem przydatna opcja. A&nbsp;nawet doceniana w&nbsp;komputerowym światku. [Na forum HN](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=%22mpris%22&sort=byDate&type=story) ludzie polecają różne swoje odtwarzacze multimediów, wskazując integrację z&nbsp;MPRIS jako zaletę.

Te bajery mają jednak swoją cenę, którą jest powstawanie miniaturek w&nbsp;folderze.

## Ocena ryzyka

Z punktu widzenia prywatności **powstała miniaturka jest ogólnodostępna**. Gdyby na naszym systemie oprócz przeglądarki działał jakiś program, to mógłby co pewien czas wypatrywać folderu `.mozilla/firefox-mpris` i&nbsp;zapisywać sobie zauważone tam obrazki, wraz z&nbsp;godziną utworzenia miniaturki. Miałby małą kronikę naszej historii oglądanych filmów.

...Tylko że to zagrożenie raczej niewielkie na tle tego, co program mógłby wyciągnąć z&nbsp;innego folderu ogólnodostępnego, `.cache/mozilla`, gdzie znajduje się [pamięć podręczna](/2021/12/24/caching){:.internal} Firefoksa. A&nbsp;tam skarby, takie jak miniaturki *wszystkich* obrazków, jakie załadowała przeglądarka.

Teoretycznie może zajść sytuacja, gdy jakiś administrator systemu ustawia taką politykę bezpieczeństwa, żeby żaden program nie miał dostępu do folderu `.cache` (bo wrażliwe rzeczy). Równocześnie mógłby zostawić dostęp do folderu `.mozilla`, żeby ludzie mieli np. możliwość integrowania innych programów z&nbsp;przeglądarką.

W takim wypadku miniatura byłaby faktycznym wyciekiem informacji. Ale to raczej naciągany scenariusz.

A w&nbsp;przypadku typowym? Nieznaczące zagrożenie na tle pamięci podręcznej. 

## Wyłączanie opcji

Niezależnie od skali zagrożenia, ktoś mógłby zechcieć nie tworzyć miniaturek. Jak je wyłączyć?  
Ktoś już o to [zapytał na Reddicie](https://www.reddit.com/r/firefox/comments/q1vnns/what_is_firefoxmpris/) i&nbsp;dostał bardzo konkretną odpowiedź.

Po pierwsze: według komentarza **miniaturka nie pojawia się, jeśli ogląda się film w&nbsp;zakładce prywatnej/_incognito_**. Kolejny dowód na to, że w&nbsp;tryb prywatny jednak włożoną jakąśtam pracę i&nbsp;[nie jest tylko zabawką do ukrywania historii](/2024/09/09/tryb-prywatny-incognito){:.internal}.

A co, jeśli nie chcemy każdorazowo używać tego trybu? W&nbsp;takim wypadku można wyłączyć tworzenie miniaturek w&nbsp;ustawieniach, żeby uczynić ich brak stanem domyślnym całego Firefoksa.

{% include details.html summary="Więcej o&nbsp;wyłączaniu przez opcje" %}

{:.bigspace-before}
Należy uruchomić przeglądarkę i wpisać w&nbsp;pasek u&nbsp;góry (ten sam, w&nbsp;którym wyświetlają się adresy stron) tekst `about:config`. Gdyby pojawiło się ostrzeżenie, to można je przeklikać.

Pojawi się lista dostępnych opcji. W&nbsp;pasek wyszukiwania po lewej stronie można zacząć wpisywać tekst `media.hard`...

Powinno wyświetlć się kilka opcji, w&nbsp;tym tę, która nas interesuje -- **`media.hardwaremediakeys.enabled`**. Należy kliknąć ikonkę dwóch strzałek po jej prawej stronie, żeby wartość obok niej zmieniła się na `false`. Zrobione.

{% include details-end.html %}

## Słowo na koniec

W tym wpisie pokazałem ciekawostkę -- ujawnienie pewnych informacji przez teoretycznie najbezpieczniejszą kombinację systemu i&nbsp;przeglądarki.

Piszę „ciekawostkę”, bo nie uważam tego za realne zagrożenie, zwłaszcza na tle łatwo dostępnej pamięci podręcznej przeglądarki.

{:.post-meta .bigspace-after}
Patrzę na to trochę jak na okrężne metody [odczytywania historii przeglądania](/internetowa_inwigilacja/2023/08/19/historia-przegladania){:.internal} (które polegają *de facto* na zamaskowaniu formularza, w&nbsp;którym użytkownicy sami klikają strony, które ostatnio widzieli).

Ta sprawa wyraźnie pokazuje natomiast pewną uniwersalną rzecz w&nbsp;realiach cyfrowej prywatności -- **informacje mogą wyciekać z&nbsp;najmniej spodziewanych miejsc, a&nbsp;próba ich przewidzenia to walka z&nbsp;wiatrakami**.

W tym wypadku musiało wystąpić kilka czynników naraz: przeglądarka Firefox, system na bazie Linuksa (wspierający *D-Busa*), do tego film odtwarzany z&nbsp;YouTube'a.

Odkryłem to zupełnym przypadkiem, uszczelniłem. Ale ilu innych rzeczy, pojawiających się w jeszcze bardziej nietypowych warunkach, nie odkryłem i&nbsp;nie uszczelnię?

W takich realiach najpewniejsze wydają się sposoby ogólne, oparte na redukcji *wszystkich* informacji, a&nbsp;nie ściganiu konkretnych luk.

1. Instalować na swoim systemie jak najmniej programów.
2. Izolować od siebie uruchamiane programy.
   
   {:.post-meta .bigspace-after}
   Zaawansowani użytkownicy mogą użyć czegoś w&nbsp;rodzaju Firejaila; inni mogą uruchomić cały system w&nbsp;jakiejś przyjaznej w&nbsp;obsłudze maszynie wirtualnej, takiej jak VirtualBox.

Istnieje też sposób trzeci -- **jak najczęściej ładować świeży system**. Żeby potencjalny wścibski program, nawet jeśli się nawinie, miał dość ubogą ucztę, pozbawioną naszych danych.

Stałe zaczynanie od zera może brzmieć absurdalnie, zwłaszcza jeśli ktoś przywykł do typowych, ciężkich, ładujących się dość długo systemów.  
Ale przy lżejszych Linuksach, ładowanych z&nbsp;pendrive'a? Możliwe i&nbsp;skuteczne. Co jeszcze pokażę w&nbsp;przyszłych wpisach.

I na tej zajawce zakończę. Do zobaczenia! :smile:
