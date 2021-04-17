---
layout: page
title: Python – pobieranie dodatkowych modułów
description: "Samouczek o tym, jak używać modułu pip do pobierania dodatkowych modułów Pythona"
---

{:.figcaption}
Ten wpis to rozwinięcie [podstawowego samouczka]({{site.url}}/tutorials/using-python) o&nbsp;używaniu skryptów w&nbsp;języku Python.

Staram się, żeby moje skrypty były niezależne i&nbsp;mieściły się w&nbsp;jednym pliku. Ale czasami to niemożliwe. Niektóre zadania wymagają pomocy modułów zewnętrznych.

Tak jest w&nbsp;przypadku skryptów, które dołączyłem np. do [wpisu o&nbsp;metadanych w&nbsp;obrazkach]({% post_url 2021-02-10-gdzie-jestem-zapytaj-moich-zdjec %}).

Do otwierania obrazków potrzeba modułu zewnętrznego PIL (*Python Imaging Library*). Jeśli otworzycie mój skrypt w&nbsp;IDLE i&nbsp;naciśniecie `F5`, żeby go odpalić -- a&nbsp;nie macie PIL-a -- to wyświetli się komunikat:

{:.figure .bigspace}
<img src="/assets/tutorials/using-pip/1.webp" alt="Zrzut ekranu z&nbsp;IDLE w&nbsp;trybie interaktywnym. Widać, napisany czerwonymi literami, komunikat 'Brak modułu PIL. Żeby skrypt działał, zainstaluj go, wpisując w&nbsp;PowerShell pip install pillow'."/>

Na szczęście można bardzo szybko i&nbsp;łatwo instalować moduły zewnętrzne. Python ma od tego programik **_PIP_**.

{% include info.html type="Ciekawostka" text="Rozwinięcie akronimu PIP to... _**P**IP **I**nstalls **P**ackages_. To tak zwany *akronim rekurencyjny*, lubiany [w kręgach programistów](https://pl.wikipedia.org/wiki/Akronim_rekurencyjny). Można by go rozwijać w&nbsp;nieskończoność, bo rozwinięcie znów zawiera pełen akronim." %}

Dzięki PIP-owi uniwersum Pythona stoi otworem. Możemy ściągać z&nbsp;internetu wszelkie dodatkowe narzędzia, jakich tylko potrzebujemy.

<img src="/assets/tutorials/using-pip/pip-boy.webp" alt="Metalowa tabliczka z&nbsp;gry Fallout, stylizowana na dawne amerykańskie plakaty reklamowe. Widać na niej napis Pip-Boy 2000 i&nbsp;uśmiechniętego, rysunkowego mężczyznę unoszącego kciuk do góry."/>

{:.figcaption}
Źródło: [nexusmods.com](https://staticdelivery.nexusmods.com/images/1151/341894-1515547342.jpg).

Żeby użyć PIP-a, trzeba skorzystać z&nbsp;PowerShella, domyślnej konsoli Windowsa  
(konsola to takie okienko, w&nbsp;którym wpisujemy różne polecenia, a&nbsp;komputer je od razu wykonuje).

Otwieramy Eksplorator Windows. W&nbsp;lewym górnym rogu klikamy opcję `Plik`. Wybieramy `Otwórz program Windows PowerShell`.

{:.figure}
<img src="/assets/tutorials/using-pip/2.webp" alt="Zrzut ekranu pokazujący lewy górny róg programu Eksplorator Windows, z&nbsp;klikniętą zakładką 'Plik'. Czerwoną obwódką otoczono drugą z&nbsp;wymienionych opcji, 'Otwórz program Windows PowerShell'."/>

{:.figcaption}
Jeden z&nbsp;wielu sposobów na włączenie PowerShella.

Super, mamy okno konsoli! Teraz możemy w&nbsp;nie wpisywać dowolne rzeczy.  
Chcemy pobrać `pillow`, więc w&nbsp;tym wypadku wpisujemy:

<div class="black-bg mono">pip install pillow</div>

{:.figcaption}
Możecie po prostu skopiować tę linijkę i&nbsp;wkleić do PowerShella, wciskając `Ctrl+V`.

Naciskamy `Enter`, żeby potwierdzić. Powinno nam pobrać i&nbsp;zainstalować moduł:

{:.figure .bigspace}
<img src="/assets/tutorials/using-pip/3.webp" alt="Zrzut ekranu z&nbsp;Powershella. U&nbsp;góry widać wpisaną komendę 'pip install pillow', poniżej biały pasek postępu wypełniony w&nbsp;całości, a&nbsp;na samym dole linijkę tekstu 'Successfully installed pillow'."/>

Gdybyśmy teraz odpalili przez IDLE skrypt wspomniany na początku:

{:.figure .bigspace}
<img src="/assets/tutorials/using-pip/4.webp" alt="Zrzut ekranu z&nbsp;IDLE. Widać komunikaty, napisane niebieskimi literami i&nbsp;mówiące 'Sprawdzam obrazki' oraz że obrazek nie zawiera metadanych."/>

I zrobione! Może i&nbsp;metadanych tu nie ma, ale skrypt działa jak powinien.

{% include info.html type="Porada" text="Instalowanie modułów Pythona wymaga łączności z&nbsp;internetem. Jeśli jej nie ma albo coś przerywa, to może wyskoczyć kilka ostrzeżeń i&nbsp;błąd jak z&nbsp;obrazka poniżej.  
Wtedy sprawdzamy jakość swojego połączenia na innej dowolnej stronce i&nbsp;próbujemy znowu.  
Jeśli to nie pomaga, to znaczy że coś się popsuło po stronie PyPI (stronki z&nbsp;modułami Pythona). Najlepiej się nie zrażać i&nbsp;po jakimś czasie spróbować ponownie." trailer="<p class='figure'><img src='/assets/tutorials/using-pip/pip-error.webp' alt='Zrzut ekranu z&nbsp;PowerShella, pokazujący długi komunikat o&nbsp;błędzie w&nbsp;połączeniu i&nbsp;mówiący, że nie znaleziono odpowiedniej wersji modułu pillow'/></p>" %}

# Znaj swój moduł

Jak sami widzicie, pobieranie modułów zewnętrznych Pythona jest całkiem bezbolesne.

Natomiast nie byłbym sobą, gdybym nie wspomniał o&nbsp;ich ciemnej stronie. Moduły zewnętrzne **nie podlegają żadnym rygorystycznym weryfikacjom**, dlatego warto czasem osobiście je sprawdzić. Zwłaszcza jeśli poleca je Wam jakaś nieznana strona.

Zawsze kiedy polecam jakiś moduł zewnętrzny, dorzucam też linki do jego źródła. Dzięki temu można osobiście sprawdzić, na ile dany moduł jest popularny i&nbsp;kto za nim stoi.

Nie daje to oczywiście 100% gwarancji bezpieczeństwa (nawet do najbardziej zaufanego modułu ktoś mógł „dorzucić” szemrany kod). Ale nawet taka lekka kontrola jest lepsza niż ślepe zgadzanie się na wszystko -- co przecież często robimy, instalując różne *byznesowe* programy od korpo.
