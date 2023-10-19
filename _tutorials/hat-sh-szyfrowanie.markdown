---
layout: page
title: Szyfrowanie na własną rękę z użyciem Hat.sh
description: "Kapelusz zakryje nasze tajemnice."
---

Hat.sh to darmowe narzędzie o&nbsp;otwartym kodzie źródłowym.  
Ma postać [prostej stronki internetowej](https://hat.sh/). Może działać (oczywiście po pierwszym pobraniu) bez żadnego dostępu do sieci. Pozwala nam szybko i&nbsp;łatwo zabezpieczać pliki hasłem.

{:.figure .bigspace-before}
<img src="/assets/tutorials/hatsh/hatsh-logo.jpg" alt="Logo programu hat.sh, pokazujące czarny piracki kapelusz z&nbsp;literką X&nbsp;pośrodku."/>

{:.figcaption}
Źródło: [stronka projektu *hat.sh*](https://github.com/sh-dv/hat.sh).

Po raz pierwszy użyłem go podczas tworzenia wpisu na temat kontroli czatów. Chciałem pokazać, że wścibskie apki służące do komunikacji dałoby się przechytrzyć, wrzucając do nich wyłącznie zaszyfrowane rzeczy.

## Wstępna weryfikacja 

Ale nie wierzcie na słowo jakiejś Ciemnej Stronie. Nim powierzymy Hatowi swoje tajemnice, trzeba go zweryfikować!

Na Githubie, [stronie z&nbsp;kodem źródłowym](https://github.com/sh-dv/hat.sh), nasz Kapelusz ma ponad 1900&nbsp;gwiazdek (pozytywnych ocen).

Dobry wynik! Ale zdarzało się już, że ktoś podkupił popularną rzecz, żeby ją zmienić w złodzieja danych. Dlatego dla pewności wyszukałem nazwę stronki również w&nbsp;social mediach:

* na [forum HackerNews](https://hn.algolia.com/?dateRange=all&page=0&prefix=false&query=%22hat.sh%22&sort=byDate&type=story);
* na [Reddicie](https://duckduckgo.com/?q=%22hat.sh%22+site%3Areddit.com&t=lm&ia=web).

Żadnych aferek nie znalazłem. Na Reddicie parę [sceptycznych głosów](https://www.reddit.com/r/crypto/comments/pghvas/comment/hbbese8/), ale dotyczących bardziej samego faktu, że ktoś używa nowinek zamiast sprawdzonego GPG. Zastrzeżeń do szyfrowania nie widziałem.

Dla pewności, gdyby Hat jednak stał się złośliwy od czasu publikacji tego wpisu, można sięgnąć do [dawnych, pewnych wersji zarchiwizowanych na *Archive.org*](https://web.archive.org/web/20221019042028/https://hat.sh/) (podlinkowałem do października 2022, ale migawek jest dużo więcej).

Kolejna sprawa to fakt, że Hat ma postać pojedynczej strony internetowej. I&nbsp;ta „internetowość” może niektórych zaniepokoić.  
Zwłaszcza jeśli ktoś czytał [„Internetową inwigilację”](/serie/internetowa_inwigilacja){:.internal}. W&nbsp;końcu przy każdej prośbie o&nbsp;dowolną stronę internetową wysyłamy trochę swoich informacji :wink:

Ale serwer Hata kontaktuje się z&nbsp;nami tylko raz, dając nam stronkę. A&nbsp;cały kod oraz interfejs już są w&nbsp;niej osadzone. **Przetwarzanie plików zachodzi wewnątrz naszej przeglądarki. Nikt tych danych nie otrzymuje**.

...Według zapewnień. Ale dla pewności zrobiłem jeszcze parę rzeczy:

* Uruchomiłem stronkę w&nbsp;trybie prywatnym.

  W&nbsp;ten sposób nie byłaby w&nbsp;stanie zapisać sobie jakichś informacji na później, w&nbsp;*plikach cookies*, żeby je gdzieś wysłać następnym razem, kiedy ją odwiedzimy.

  W&nbsp;tym trybie nie jest jednak w&nbsp;stanie korzystać z&nbsp;niektórych funkcji, więc rozmiar przyjmowanych plików jest ograniczony do 1&nbsp;GB.

* Po tym, jak stronka się załadowała, wyłączyłem na laptopie łączność z&nbsp;internetem (przez dolny pasek menu).  
  Wszystko mimo to działało.

Wniosek: zapewnienia twórców wydają są prawdziwe, Kapelusz (na tę chwilę) nie wysyła obcym danych. No to go użyjmy.

## Instrukcja korzystania

Nim zaczniemy -- sprawa hasła. Jeśli chcemy wysyłać pliki innej osobie, a&nbsp;nie szyfrować wyłącznie na własne potrzeby, to **warto dogadać się co do hasła jakimś zaufanym kanałem**.  
Po ludzku -- możemy choćby spotkać się w&nbsp;świecie fizycznym i&nbsp;ustalić hasło przy piwie :smile:


{% include info.html
type="Porada"
text="Gdybyśmy koniecznie musieli wysłać nasze hasło taką samą drogą co szyfrowany plik, to Hat.sh daje możliwość skorzystania z&nbsp;kryptografii asymetrycznej.  
Otrzymujemy wtedy *klucz publiczny* (który możemy normalnie, na widoku komuś wysłać), zaś po swojej stronie zachowujemy *klucz prywatny*.  
Ale w&nbsp;tym samouczku zakładam, że nie mamy takiej sytuacji i&nbsp;że możemy ustalić hasło w&nbsp;bezpiecznym miejscu. Albo szyfrujemy tylko na swoje osobiste potrzeby."
%}

Na początek mamy jakiś plik, który chcemy zaszyfrować, żeby go żadni złoczyńcy i&nbsp;stalkerzy nie podejrzeli. Format dowolny -- obrazek, nagranie...

Do naszego przykładu wezmę najprostszy plik tekstowy z&nbsp;krótką wiadomością:

{:.bigspace}
<img src="/assets/tutorials/hatsh/oryginalna-wiadomosc.jpg" alt="Zrzut ekranu pokazujący pojedynczy plik tekstowy nazwany wiadomosc.txt. Poniżej widać jego zawartość, tekst 'Niedługo zaczną czytać nasze rozmowy' oraz emotkę przerażonej twarzy."/>

Ładujemy w&nbsp;przeglądarce stronkę Hata (pamiętając, że po załadowaniu możemy wyłączyć internet). Zaznaczamy, że chcemy coś *zaszyfrować*. Potem wybieramy opcję załadowania pliku z&nbsp;dysku.

{:.bigspace}
<img src="/assets/tutorials/hatsh/hatsh-szyfrowanie-poczatek.jpg" alt="Zrzut ekranu pokazujący interfejs stronki hat.sh"/>

Po wybraniu trybu Hat zapyta nas o&nbsp;hasło. Wpisujemy coś długiego, złożonego z&nbsp;wielkich i&nbsp;małych liter. Komputer zawsze będzie miał więcej „losowości” niż człowiek, więc najlepiej sobie wygenerować.

Ale w&nbsp;tym przykładzie użyję czegoś z&nbsp;ludzkich słów. Optymalizując pod łatwość zapamiętania, a&nbsp;nie bezpieczeństwo. `NawetNieCzujęJakSzyfruję`.  
Hasło oczywiście zapamiętujemy lub zapisujemy. Nikt tego za nas nie zrobi :wink:

{:.bigspace}
<img src="/assets/tutorials/hatsh/hatsh-szyfrowanie-haslo.jpg" alt="Fragment interfejsu Hata, w&nbsp;którym wpisuje się hasło. Widać tu podkreślony na czerwono tekst 'nawet nie czuję jak szyfruję', bez spacji w&nbsp;środku. Poniżej znajduje się informacja, że Hat będzie przetwarzał wszystko offline, w&nbsp;naszej przeglądarce."/>

Strona poinformuje nas, że zaszyfrowany plik jest gotów do pobrania. Klikamy dalej i&nbsp;zapisujemy na dysk nasz zaszyfrowany plik, z&nbsp;rozszerzeniem `.enc`.

{:.bigspace}
<img src="/assets/tutorials/hatsh/hatsh-szyfrowanie-pobieranie.jpg" alt="Zrzut ekranu pokazujący informację o&nbsp;skutecznym zaszyfrowaniu pliku. A&nbsp;pod spodem jego miniaturka, o&nbsp;nazwie 'wiadomosc.txt.enc'."/>

### Odszyfrowywanie

Po zapisaniu zaszyfrowanego pliku możemy go wysłać znajomej osobie. Albo sami do niego wrócić, jeśli szyfrowaliśmy tylko na własne potrzeby (np. na czas trzymania na dysku zewnętrznym).

W każdym razie -- osoba mająca szyfrowany plik również otwiera Hata, wybiera tryb deszyfracji, ładuje plik, wpisuje hasło. Po czym pobiera pierwotną, odszyfrowaną treść.

{:.bigspace}
<img src="/assets/tutorials/hatsh/hatsh-deszyfrowanie.jpg" alt="Seria zrzutów ekranu pokazujących różne elementy interfesu hat.sh, wybierane w&nbsp;trybie odszyfrowywania plików"/>

I to tyle! Miłego testowania życzę :smile:

{% include info.html
type="Ciekawostka"
text="Kto chce, ten może również użyć dodatku do przeglądarki [SingleFile](https://github.com/gildas-lormeau/SingleFile/wiki), żeby zapisać sobie stronkę w postaci pojedynczego pliku HTML (koniecznie trzeba zaznaczyć w&nbsp;opcjach, żeby nie usuwało JavaScriptu).  
Sprawdziłem i&nbsp;wszystko działa. Jedynie interfejs ma parę wad (czerwone tło w&nbsp;jednym miejscu; nie widziałem tekstu wpisywanego w&nbsp;pole od deszyfracji, choć tam był).  
Mając Hata w&nbsp;formie pliku, możemy z&nbsp;niego korzystać do woli, bez użycia internetu. A&nbsp;nawet rozsyłać go *innym rebeliantom*{:.corr-del} znajomym przez Bluetooth, żeby potem używali w&nbsp;swoich przeglądarkach. Bez żadnego internetu."
%}

