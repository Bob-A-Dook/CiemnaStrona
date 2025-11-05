---
layout: page
title: Python – pobieranie dodatkowych modułów
description: "Samouczek o tym, jak używać modułu pip do pobierania dodatkowych modułów Pythona"
---

{:.figcaption}
Ten wpis to rozwinięcie [podstawowego samouczka]({{site.url}}/tutorials/using-python) o&nbsp;używaniu skryptów w&nbsp;języku Python.

Staram się, żeby moje skrypty były niezależne i&nbsp;mieściły się w&nbsp;jednym pliku. Ale czasami to niemożliwe. Niektóre zadania wymagają pomocy modułów zewnętrznych.

Tak jest w&nbsp;przypadku skryptów, które dołączyłem np. do [wpisu o&nbsp;metadanych w&nbsp;obrazkach]({% post_url 2021-02-10-gdzie-jestem-zapytaj-moich-zdjec %}){:.internal}.

Do otwierania obrazków potrzeba modułu zewnętrznego PIL (*Python Imaging Library*). Jeśli otworzycie mój skrypt w&nbsp;IDLE i&nbsp;naciśniecie `F5`, żeby go odpalić -- a&nbsp;nie macie PIL-a -- to wyświetli się komunikat:

{:.figure .bigspace}
<img src="/assets/tutorials/using-pip/1.webp" alt="Zrzut ekranu z&nbsp;IDLE w&nbsp;trybie interaktywnym. Widać, napisany czerwonymi literami, komunikat 'Brak modułu PIL. Żeby skrypt działał, zainstaluj go, wpisując w&nbsp;PowerShell pip install pillow'."/>

Na szczęście można bardzo szybko i&nbsp;łatwo instalować moduły zewnętrzne. Python ma od tego programik **_PIP_**.

{% include info.html type="Ciekawostka" text="Rozwinięcie akronimu PIP to... _**P**IP **I**nstalls **P**ackages_. To tak zwany *akronim rekurencyjny*, lubiany [w kręgach programistów](https://pl.wikipedia.org/wiki/Akronim_rekurencyjny). Można by go rozwijać w&nbsp;nieskończoność, bo rozwinięcie znów zawiera pełen akronim." %}

Dzięki PIP-owi uniwersum Pythona stoi otworem. Możemy ściągać z&nbsp;internetu wszelkie dodatkowe narzędzia, jakich tylko potrzebujemy.

<img src="/assets/tutorials/using-pip/pip-boy.webp" alt="Metalowa tabliczka z&nbsp;gry Fallout, stylizowana na dawne amerykańskie plakaty reklamowe. Widać na niej napis Pip-Boy 2000 i&nbsp;uśmiechniętego, rysunkowego mężczyznę unoszącego kciuk do góry."/>

{:.figcaption}
Źródło: [nexusmods.com](https://staticdelivery.nexusmods.com/images/1151/341894-1515547342.jpg).

## Spis treści

* [PIP na Windowsie](#pip-na-windowsie)
* [Instalacja na Linuksie](#instalacja-na-linuksie)
* [Znaj swój moduł](#znaj-swój-moduł)

## PIP na Windowsie

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

# Instalacja na Linuksie

Przede wszystkim piąteczka!

Linux to ciekawa sprawa. Z&nbsp;jednej strony pozwala oszczędzić sobie roboty, bo Python jest na nim domyślnie zainstalowany.

Ale, żeby nie było zbyt fajnie -- to Python systemowy, który od pewnego czasu **ma ograniczone możliwości instalowania zewnętrznych modułów**. To zmiana na gorsze w&nbsp;porównaniu z&nbsp;tym, co było wcześniej. Dlatego ta część samouczka nieco się zdezaktualizowała i&nbsp;wymagała przepisania :disappointed:

Kwestia instalowania zewnętrznych modułów na Linuksie (przez PIP-a i&nbsp;nie tylko) jest teraz opisana [w&nbsp;innym samouczku](/tutorials/python-blad-externally-managed-environment){:.internal}, zapraszam tam serdecznie!

Tutaj zostawię tylko parę uwag uzupełniających, pokazujących różnice między Linuksem a&nbsp;Windowsem pod względem korzystania z&nbsp;PIP-a.

{% include details.html summary="Informacje uzupełniające na temat PIP-a" %}

{:.bigspace-before}
Zakładam, że odwiedziliście link znad tej zakładki i macie teraz którąś z następujących rzeczy:

* PIP-a w aktywnym środowisku wirtualnym,
* PIP-a zainstalowanego jako moduł systemowego Pythona (plus gotowość do użycia opcji `--break-system-packages`).

Jeśli tak, to służę paroma informacjami uzupełniającymi.

{:.post-meta .bigspace-before}
Niektóre z poniższych informacji są już nieaktualne, przynajmniej na Mincie i&nbsp;paru innych popularnych Linuksach. Ale zostawiam, bo może pomogą przy innych systemach.

Przede wszystkim warto wiedzieć, że czasem macie zainstalowane dwie wersje Pythona -- starą wersję `2.7` oraz nowszą `3.coś`. To tej drugiej chcecie używać.  
Upewnijcie się, jak jest. Wpiszcie w konsoli `pip --version` i&nbsp;spójrzcie, jaką wersję Pythona wyświetla pod koniec.  
Jeśli pod samym *pip* macie wersję drugą, to&nbsp;w celu użycia trzeciej **musicie, tam gdzie inni wpisują samo `pip`, wpisywać `pip3`**.

{:.post-meta .bigspace-after}
Koniec części (raczej) nieaktualnej.

Druga sprawa: zapewne przy próbie instalacji będzie Wam wyskakiwał błąd *Permission Denied*. [To normalne](https://stackoverflow.com/questions/33922240/why-i-cant-do-some-things-without-sudo-using-python-and-pip), Linux chroni część systemu przed zmianami. W&nbsp;razie błędu należy dopisać też opcję `--user`, żeby instalować dla konkretnego użytkownika.

Podsumowując: tam, gdzie na Windowsie byście po prostu wpisali:

```
pip install jakiś_pakiet
```

Na Linuksie **zapewne musicie wpisać**:

```
pip3 install --user jakiś_pakiet
```

Warto o tym pamiętać, czytając instrukcje z&nbsp;internetu.

{% include details-end.html %}

# Znaj swój moduł

Jak sami widzicie, pobieranie modułów zewnętrznych Pythona jest całkiem bezbolesne.

Natomiast nie byłbym sobą, gdybym nie wspomniał o&nbsp;ich ciemnej stronie. Moduły zewnętrzne **nie podlegają żadnym rygorystycznym weryfikacjom**, dlatego warto czasem osobiście je sprawdzić. Zwłaszcza jeśli poleca je Wam jakaś nieznana strona.

Zawsze kiedy polecam jakiś moduł zewnętrzny, dorzucam też linki do jego źródła. Dzięki temu można osobiście sprawdzić, na ile dany moduł jest popularny i&nbsp;kto za nim stoi.

Nie daje to oczywiście 100% gwarancji bezpieczeństwa (nawet do najbardziej zaufanego modułu ktoś mógł „dorzucić” szemrany kod -- przykładem [afera XZ](/cyfrowy_feudalizm/2024/03/31/xz-backdoor){:.internal}). Ale nawet taka lekka kontrola jest lepsza niż ślepe zgadzanie się na wszystko -- co przecież często robimy, instalując różne *byznesowe* programy od korpo.
