# Ciemna Strona

Blog o ochronie prywatności i przekrętach korporacji. Bez teorii spiskowych.

Jeśli chcecie po prostu poczytać bloga, to znajdziecie go pod adresem *[ciemnastrona.com.pl](https://www.ciemnastrona.com.pl)*, natomiast ta strona zawiera jego kod źródłowy.

Kod może się przydać, gdybyście byli ciekawi jak to działa. Albo chcieli umieścić treść bloga na własnym serwerze (w razie gdyby we mnie jakiś piorun siarczysty-łognisty strzelił albo krew nagła zalała).

## Pobieranie kodu

Kod bloga możecie pobrać w formie pliku ZIP, klikając zielony przycisk `Code` zaraz nad listą plików i wybierając opcję `Download ZIP`. Potem go rozpakowujecie.

...Możecie to również zrobić w bardziej „hakierski” sposób. Najpierw [instalujecie](https://www.atlassian.com/git/tutorials/install-git#linux) program *git*. Potem otwieracie konsolę (taką jak PowerShell) w folderze, do którego chcecie skopiować pliki. Wklejacie w nią adres aktualnej strony:

```
git clone https://github.com/Bob-A-Dook/CiemnaStrona
```

Po chwili wszystkie pliki pobiorą się do folderu, w którym odpaliliście komendę.

## Korzystanie z kodu

Mając kod u siebie na dysku, możecie go edytować.

Przede wszystkim możecie usunąć ze swojej kopii kodu plik *CNAME*, bo wskazuje na moją domenę.

Blog jest hostowany na Github Pages i wykorzystuje silnik Jekyll.

Żeby zainstalować Jekylla, postępujcie zgodnie z [instrukcjami z oficjalnej strony](https://jekyllrb.com/docs/installation/).  
Oprócz niego wykorzystuję motyw `Minima`, dodatek `jemoji` (od wyświetlania emoji w stylu Githuba) i program `bundle` (do testowania bloga). Je również trzeba zainstalować.

Proces twórczy wygląda u mnie tak:

W swoim folderze z kodem trzymam foldery *_ideas* i *_drafts*.

Do *_ideas* dodaję różne pliki, luźne przemyślenia, tworzę szkielety wpisów itp.  
Kiedy wpisy nabierają kształtu, zapisuję je do plików z rozszerzeniem *.markdown* i przenoszę je do folderu *_drafts*.  Odpowiadające im obrazki umieszczam w folderze *assets/draft_imgs*.  
(Wszystkie te foldery są wymienione w pliku *.gitignore*, więc nie załadują się na Githuba, kiedy będę aktualizował kod).

Testuję wygląd strony, wpisując w konsolę:

```
bundle exec jekyll serve --drafts
```

W ten sposób włączam lokalne testowanie. Od teraz mogę wejść w link widoczny w konsoli (albo wpisać w pasek przeglądarki `http://127.0.0.1:4000/`), żeby zobaczyć jak będzie wyglądała moja strona.  
Po każdej zmianie w plikach wystarczy ją odświeżyć (`F5`), żeby zobaczyć co się zmieniło. Nie muszę wpisywać tekstu w konsolę od nowa.

Kiedy uznam że wpis jest gotowy, przenoszę plik z nim z folderu *_drafts* do *_posts*, a obrazki i inne pliki pomocnicze z *assets/draft_imgs* do *assets/posts*.  
Oczywiście w samym wpisie też zamieniam *draft_imgs* na *posts*, żeby odnośniki prowadziły do odpowiednich plików.

Kiedy chcę załadować wszystkie wprowadzone zmiany na Githuba (i tym samym na publiczną stronę), to wpisuję w konsolę:

```
git add .
git commit -m "Informacja o tym, co się zmieniło"
git push ciemnastrona master
```

Po krótkim czasie strona się zaktualizuje i zmiany będą widoczne dla wszystkich pod adresem *ciemnastrona.com.pl*.

Oprócz tego do tworzenia bloga używam skryptów pomocniczych w Pythonie (do konwersji obrazków na format *webp*, wstawiania spacji nierozdzielających itp.). Kiedyś może je dorzucę, ale nie są niezbędne.
