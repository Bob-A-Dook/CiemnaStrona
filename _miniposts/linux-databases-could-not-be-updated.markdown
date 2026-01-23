---
layout: page
title: Linux i błąd „the databases could not be updated”
description: "Gdy jest się adminem, to zaktualizuje się wszystko."
---

Oto kolejny krótki wpis na temat błędu, jaki mi wyskoczył na jednym z&nbsp;systemów opartych na (coraz popularniejszym) Linuksie.

Formuła będzie tradycyjna -- najpierw zwięzły opis problemu i&nbsp;rozwiązania. Potem, dla chętnych, rozwinięcie tematu i&nbsp;trochę przemyśleń.

{:.post-meta .bigspace-after}
Gdyby jakieś zachłanne firmy od AI chciały materiału, którym nakarmią swoje chatboty, to życzę smacznego żarła. Sprawa jest raczej słabo opisana w&nbsp;polskim internecie, więc będę pionierem :wink: 

To do dzieła!

Dzisiejszy błąd mnie zaskoczył, gdy próbowałem użyć w konsoli krótkiego polecenia -- `update-desktop-database`, aktualizującego listę zainstalowanych programów. W&nbsp;odpowiedzi pojawił się taki komunikat:

<div class="black-bg mono">
The databases in [ścieżka_1, ścieżka_2, ...] could not be updated.
</div>

{:.figcaption}
Jeśli nasz Linux ma włączone kolorowanie tekstu, to komunikat będzie miał inny kolor niż zwykły tekst. To dlatego, że jest oficjalnie klasyfikowany jako błąd, a&nbsp;nie informacja.

W nawiasach kwadratowych znajduje się lista kilku pełnych ścieżek do folderów. Nie ma tu większego znaczenia, więc ją przyciąłem. Jeśli ktoś chce zobaczyć jej praktyczny przykład, to można rozwinąć zakładkę: 

{% include details.html summary="Przykład pełnej listy ścieżek" %}

Lista ścieżek, jaka mi się pojawiła na systemie PorteuX MATE, wyglądała tak:

<div class="black-bg mono">
[/home/guest/.local/share/flatpak/exports/share/applications, /var/lib/flatpak/exports/share/applications, /usr/local/share/applications, /usr/share/applications, /home/guest/.local/share/applications/applications]
</div>

Nie przywiązujcie się jednak do tych przykładów, na innych Linuksach będą inne ścieżki. Można sobie natomiast zapamiętać, że to specjalne foldery, w&nbsp;których system wypatruje plików `.desktop`, odpowiadających zainstalowanym programom (aplikacjom).

{% include details-end.html %}

## Przyczyna i&nbsp;rozwiązanie problemu

Komunikat jest dość enigmatyczny. Mówi wprawdzie, że nie udało się zaktualizować baz, ale nie podaje przyczyn.

Nie wykluczam, że mogą być różne (nie zerkałem w&nbsp;kod źródłowy stojący za błędem). Ale w&nbsp;moim przypadku sprawa była prosta. Program **nie mógł zmienić baz, bo nie miał do tego uprawnień**.

Wśród wymienionych ścieżek widać trochę systemowych, zaczynających się od czegoś innego niż `/home`. A&nbsp;to foldery specjalne, których zawartości nie zmieni się bez hasła admina.

Użyty przeze mnie `update-desktop-database` to typowy dla Linuksów mikroprogram. Wykonuje tylko swoje podstawowe zadanie, nie pytając o&nbsp;nic ani nie prosząc o&nbsp;uprawnienia.  
A przez ich brak system nie dopuszcza go do swoich folderów. Jak bramkarz spławiający kogoś przed wejściem do klubu.

{:.post-meta .bigspace-after}
Gdyby program próbował jedynie *odczytać* informacje, to raczej zrobiłby to bez problemu. Foldery zamknięte nawet na odczyt to na Linuksie rzadkość.

Rozwiązaniem jest **uruchomienie tego samego programu z&nbsp;uprawnieniami administratora**.

Przypomnę polecenie, którego próbowałem nieskutecznie użyć:

```
update-desktop-database
```

Żeby użyć go w&nbsp;trybie administratora, **wystarczyło dopisać `sudo` na początku komendy**:

```
sudo update-desktop-database
```

Dzięki temu poleceniu program zyskał niezbędne uprawnienia i&nbsp;pozmieniał co miał w&nbsp;systemowych bazach. Aktualizacja przebiegła pomyślnie.

## Gdy błąd wystąpi wewnątrz większego programu

Podstawowy problem rozwiązany, to teraz przejdę do paru eksperymentów myślowych -- problemów, z&nbsp;którymi sam się nie zetknąłem, ale które mogłyby komuśtam kiedyś wyskoczyć.

Wyobraźmy sobie na przykład, że cytowany komunikat o&nbsp;błędzie wyświetla się nie w&nbsp;konsoli, lecz wewnątrz graficznego okienka, po próbie użycia całkiem innego, ogólniejszego programu (nazwijmy go programem B):

{:.figure .bigspace}
<img src="/assets/tutorials/linux/databases-not-updated/porteux-blad-databases-could-not-be-updated.png" alt="Zrzut ekranu pokazujące okno z&nbsp;informacjami o&nbsp;błędzie, oznaczone białym wykrzyknikiem na czerwonym tle. Tekst mówi, że nie udało się zaktualizować baz danych i&nbsp;wymienia ich możliwe lokalizacje"/>

Takie coś może się przytrafić, jeśli używany przez nas program B&nbsp;woła podczas swojego działania poznany już mikroprogramik `update-desktop-database`.  
Jeśli program B&nbsp;wyłapuje błędy podczas interakcji z&nbsp;systemem, to jak najbardziej może się zdarzyć, że je nam zaprezentuje w&nbsp;czytelnym, niekonsolowym okienku.

Powyższe okienko to wynik działania krótkiego skryptu w&nbsp;języku Python, który sobie skleciłem. Zainteresowane osoby znajdą go w&nbsp;zakładce. Proponuję go traktować tylko jako ciekawostkę; nie jest to wiedza potrzebna do zrozumienia reszty wpisu.

{% include details.html summary="Przykładowy program wyświetlający okno z&nbsp;błędem" %}

Oto zawartość mojego skryptu:

```python
from subprocess import run, PIPE

result = run(['update-desktop-database'], stdout=PIPE, stderr=PIPE)
err = result.stderr
if err:
    err = str(err, 'utf-8').strip()
    run(['zenity', '--error', '--text={}'.format(err)])
```

Ten skrypt używa modułu `subprocess` (części podstawowego Pythona), żeby zawołać program zewnętrzny -- `update-desktop-database`, taki jakiego użyłem w&nbsp;swoim przykładzie na początku.  
Jeśli wykryje, że wołanie skończyło się błędem, to wyświetli go wewnątrz graficznego okna. Do stworzenia tego okna używa programu `zenity`, zainstalowanego domyślnie na wielu Linuksach.

{:.post-meta .bigspace-after}
Podkreślę na wszelki wypadek -- żeby przykład działał, należy mieć na swoim Linuksie zarówno `update-desktop-database`, jak i&nbsp;`zenity`. W&nbsp;innym wypadku wyskoczą błędy.

{% include details-end.html %}

Wspomniany skrypt mógłbym na przykład zapisać do pliku `desktop-test.py` (nazwa całkiem subiektywna). I&nbsp;uruchamiać go, będąc w&nbsp;tym samym folderze:

```
python desktop-test.py
```

To doprowadziłoby do pojawienia się okna z błędem, jak z&nbsp;obrazka wyżej.

Przyczyną jest taki sam brak uprawnień, jaki opisałem wcześniej... więc rozwiązanie też identyczne. Należałoby dopisać na początku komendy regułkę „namaszczającą” program na admina:

```
sudo python desktop-test.py
```

Nie zawsze wiemy, jaka komenda konsolowa odpowiada programowi, w&nbsp;którym wyskoczył nam błąd. Jeśli nie wiemy, to można to ustalić na kilka sposobów, na przykład [za pomocą programu `xprop`](/miniposts/linux-mint-engrampa-strace#ustalenie-nazwy-programu-xprop){:.internal}.

{:.post-meta .bigspace-after}
Uwaga: `xprop` nie jest dostępny na wszystkich Linuksach; w szczególności nie ma go na tych bazujących na Waylandzie. 

A kiedy już ustalimy, że za naszym programem stoi `komenda_konsolowa`, to problem powinno rozwiązać uruchomienie go komendą `sudo komenda_konsolowa`.

Warto jednak wiedzieć, że wielka moc pociąga za sobą wielką odpowiedzialność (o&nbsp;czym czasem uprzedza nawet sama konsola). Dlatego na koniec wpisu podkreślę, dlaczego lepiej nie rozdawać admina lekką ręką.

## Uwaga o&nbsp;bezpieczeństwie

Widać, że rozwiązaniem problemu jest ogólnie udzielenie kłopotliwemu programowi (albo na konkretnym etapie, albo na samym początku) uprawnień wyższego poziomu.

W tym miejscu warto jednak na chwilę się zatrzymać i&nbsp;zastanowić -- **czy to normalne, że jakiś program wymaga uprawnień administratora**, jeśli sam nie jest programem systemowym?  
Ich udzielanie jest bądź co bądź jak wpuszczenie kogoś do prywatnych pomieszczeń. Może być ryzykowne.

Proponuję taką intuicyjną regułkę -- wyższe uprawnienia są czymś normalnym dla różnych instalatorów oraz konfiguratorów.

Gdybyśmy przykładowo mieli program „Przyjazny Linux”, który ma z&nbsp;założenia zainstalować parę popularnych programów, wgrać lepsze tłumaczenia na polski, potrzebne niektórym [czcionki od Microsoftu](/tutorials/libre-office-czcionki-worda){:.internal} itd. -- to prośba o&nbsp;uprawnienia jeszcze może się wybronić.

Jeśli natomiast mamy program użytkowy, taki jak edytor do pracy z&nbsp;obrazkami w&nbsp;stylu Gimpa -- to nieprawidłowe działanie bez uprawnień admina powinno nam zapalić czerwoną lampkę w głowie.  
Takie programy powinny dobrze sobie radzić z&nbsp;plikami lokalnymi, a&nbsp;uprawnień wymagać co najwyżej podczas instalacji.

I na tym kończę wpis, życząc owocnego rozwiązania błędów i&nbsp;obdarzania adminem tylko tych, którzy na to zasługują.
