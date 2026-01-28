---
layout: page
title: "Linux – jak ustalić, jakie polecenia konsolowe odpowiadają programom z menu?"
description: "Tłumaczenie przyjaznego świata ludzkiego na szybszy konsolowy."
---

Zacznę od małej opowiastki motywacyjnej.

Oto siedzę sobie przed laptopem. Na ekranie mam system na bazie Linuksa. Tym razem to PorteuX, nie mój codzienny Mint.  
Ale wersja nie ma aż takiego znaczenia. Próbowałem różnych Linuksów i&nbsp;wszystkie służyły mi dzielnie, nie pokazując ani jednej reklamy. Praca na nich to spokój i&nbsp;*zen*.

Na głównym pasku (który u&nbsp;mnie jest paskiem dolnym) znajduje się ikona systemu. Kiedy ją kliknę, to rozwinie się menu.  
Lista dostępnych programów. Pogrupowanych logicznie, w&nbsp;tematyczne zakładki. *Biuro*, *Akcesoria* i&nbsp;tak dalej.

Jednym z&nbsp;dostępnych programów jest często przeglądarka. Firefox. Względnie prywatny, choć od pewnego czasu, niestety, [idący ku gorszemu](/2024/08/27/make-firefox-private){:.internal}.

Wśród programów jest również osławiony **Terminal**, zwany konsolą. Czarne pole, w&nbsp;które wpisuje się tekst, żeby poczuć się panem swojego komputera.

Osobiście nie mam nic przeciwko klikaniu, ale czasem lubię „przykonsolić”. Mógłbym na przykład wpisać takie hakierskie polecenie:

```
firefox
```

Gdy to wpiszę i&nbsp;nacisnę *Enter*, to osiągnę ten sam efekt, co w&nbsp;przypadku kliknięcia Firefoksa przez menu. Program się uruchomi.

{:.post-meta .bigspace-after}
Z tym małym bonusem, że w&nbsp;konsoli będą się wyświetlały różne informacje, zwykle ukryte przed moimi oczami. A&nbsp;jeśli zamknę okno konsoli, to z&nbsp;automatu zamknie się również Firefox.

Pod każdym programem z&nbsp;menu kryje się zazwyczaj coś konsolowego.

W tym przypadku komenda to po prostu nazwa programu, tyle że zapisana małymi literami. Ale warto wiedzieć, że **nie jest to zasada uniwersalna; nazwy konsolowe nie muszą odpowiadać tym z&nbsp;menu**.

W tym miejscu budzi się moja ciekawość. „A jak ustalić, *jaka* komenda odpowiada czemuś, co widzę w&nbsp;menu?”. Na przykład programowi od robienia zrzutów (zdjęć) ekranu?  
Na to pytanie odpowiem w&nbsp;tym wpisie. Zapraszam!

## Rozwiązanie

Należy kliknąć interesujący nas program z&nbsp;menu prawym przyciskiem myszy. Wyświetli się wtedy małe menu kontekstowe z&nbsp;opcjami.

Czasem w&nbsp;tym menu będzie opcja `Właściwości`. Jeśli tak, to należy ją kliknąć.

{% include details.html summary="A jeśli nie widać takiej opcji?" %}

{:.bigspace-before}
Brak opcji to nic niepokojącego, po prostu jest tylko na niektórych Linuksach.  
Jeśli jej nie ma, to należy wybrać ze wspomnianego wyżej menu opcję `Dodaj do pulpitu`.

{:.bigspace-before}
<img src="/assets/tutorials/linux/komendy-odpowiadajace-programom/mate-screenshot-dodawanie-skrotu-do-pulpitu.png" alt="Zrzut ekranu pokazujący menu kontekstowe nad jedną z pozycji z&nbsp;menu głównego. Wyróżnioną opcją jest umieszczenie skrótu na pulpicie."/>

{:.figcaption}
Tu akurat widok z&nbsp;Porteuksa po angielsku. Jeśli kogoś odstrasza szata graficzna, to uspokoję, że Mint jest ładniejszy.

Następnie należy najechać kursorem na świeżo dodaną ikonkę z&nbsp;pulpitu i&nbsp;nacisnąć prawy przycisk myszy.  
Pojawi się menu, w&nbsp;którym już prawie na pewno będzie coś związanego z&nbsp;właściwościami. Można to kliknąć.

<img src="/assets/tutorials/linux/komendy-odpowiadajace-programom/mate-screenshot-wlasciwosci.png" alt="Zrzut ekranu pokazujący okno z&nbsp;informacjami na temat programu, takimi jak nazwa i&nbsp;opis. Jedno z&nbsp;pól, podpisane jako 'command', zawiera polecenie konsolowe."/>

{% include info.html
type="Ciekawostka"
text="Utworzony na pulpicie skrót prowadzi tak naprawdę do pliku z&nbsp;rozszerzeniem `.desktop`, tak zwanego „uruchamiacza” (ang. *launcher*).  
Dałoby się go otworzyć w&nbsp;Notatniku i&nbsp;znaleźć tam szereg ciekawych informacji. Ale to temat na osobną opowieść."
%}

{% include details-end.html %}

W ten czy inny sposób wyświetlą się właściwości wybranego programu. Wśród nich szczególnie ciekawa jest ta dotycząca polecenia (ang. *command*), wyróżniona na obrazku:

{:.figure .bigspace}
<img src="/assets/tutorials/linux/komendy-odpowiadajace-programom/mate-screenshot-ustalanie-komendy.png" alt="Zrzut ekranu pokazujące menu kontekstowe nad ikoną z pulpitu oraz wyróżnioną opcję 'Właściwości'."/>

Widać tu, że program z&nbsp;mojego przykładu (obecny w&nbsp;menu pod nazwą *Take Screenshot*) nosi w&nbsp;konsoli nazwę `mate-screenshot` i&nbsp;jest uruchamiany z&nbsp;parametrem <code>&#8209;&#8209;interactive</code>.

{:.post-meta .bigspace-after}
MATE to nazwa środowiska graficznego, z&nbsp;którego korzystam. Domyślnie zawiera kilka przydatnych programów. Jak ten od screenów albo inny, od wyszukiwania plików (polecam!).

Całą widoczną tu komendę mógłbym sobie zaznaczyć, skopiować i&nbsp;wkleić do konsoli (domyślnie przez <code>Ctrl+<span class="red">Shift</span>+V</code>!), po czym wykonać, naciskając *Enter*.  
Efekt byłby dokładnie taki sam jak przy kliknięciu ikony w&nbsp;menu.

{% include info.html
type="Uwaga"
text="Czasem komenda zawiera jakąś **zmienną**. Literę z&nbsp;procentem, na przykład `%U`.  
To ogólne oznaczenie, dzięki któremu program może otwierać pliki (choćby przez menu kontekstowe i&nbsp;opcję `Otwórz za pomocą`).  
Taka komenda nie zadziała w&nbsp;konsoli -- przed użyciem należy z&nbsp;niej usunąć zmienną. Albo wpisać zamiast niej ścieżkę i nazwę jakiegoś konkretnego pliku."
%}

## Świat możliwości

Znając nazwę konsolową programu, można czasem odkryć możliwości, o&nbsp;jakie go nie podejrzewaliśmy podczas codziennego korzystania.

Pierwszym krokiem po poznaniu nazwy konsolowej może być próba wyświetlenia mikroinstrukcji, jaką posiada każdy szanujący się program konsolowy. Dla programu z&nbsp;przykładu wyżej:

<div class="black-bg mono">
mate-screenshot -h
</div>

{:.post-meta .bigspace-after}
Czasem zamiast `-h` za pomoc odpowiada `--help`. W&nbsp;przypadku tego od *screenów* działają oba warianty, ale ogólnie nie ma reguły, każdy program ustawia własne skróty.

Wyświetli się omówienie różnych dostępnych opcji. Po lewej stronie *argumenty* (opcje wpływające na działanie programu). Po prawej opis ich działania.

Widać na przykład, że w&nbsp;przypadku mojego programu argument `-c` pozwala wysłać zrobionego screena prosto do systemowego schowka, z&nbsp;pominięciem jakiegokolwiek menu graficznego:

```
mate-screenshot -c
```

A to już przydatna właściwość, do której bym nie dotarł, korzystając z&nbsp;programu w&nbsp;sposób domyślny! Wciśnięcie klawisza *PrintScreen* zawsze prowadzi bowiem do pojawienia się graficznego okienka.

Co dalej? Jeśli często przenoszę w&nbsp;schowku screeny, to mógłbym zaoszczędzić sobie czasu, podpinając komendę wyżej pod nowy skrót klawiszowy.

Albo może... dodać jeszcze parę linijek, żeby otrzymać pełnoprawny **skrypt konsolowy**?

```
mate-screenshot -c
xclip -selection clipboard -target image/png -out > /tmp/img.png
gimp /tmp/img.png
```

W tym wypadku program numer jeden wykonuje *screena* i&nbsp;wrzuca go do schowka. Kolejny program (`xclip`) go z&nbsp;tego schowka wyciąga i&nbsp;zapisuje do tymczasowego pliku. Program numer trzy -- GIMP od grafiki -- otwiera ten plik w&nbsp;celu dalszej obróbki.

{:.post-meta .bigspace-after}
Nieco mnie razi to tworzenie pliku tymczasowego, ale nie znalazłem informacji o&nbsp;tym, żeby GIMP wspierał bezpośrednie wrzucanie obrazków przez konsolę.

Stworzony skrypt można [lekko dopracować](/2024/12/09/rury-wprowadzenie#problem-pierwszy-niewykonywalność){:.internal} (włączyć jedną opcję i&nbsp;umieścić go w&nbsp;odpowiednim folderze), zyskując przydatne narzędzie, które można wezwać z&nbsp;dowolnej części systemu. Albo nawet podpiąć pod skrót klawiszowy.

A to tylko jedna z&nbsp;wielu możliwości. Ogranicza nas jedynie nasza wyobraźnia... No i&nbsp;znajomość komend kryjących się pod czytelnymi nazwami.  
Ale to drugie, mam nadzieję, umiesz już sprawdzić po lekturze wpisu :wink:

## Słowo na koniec

To mit, że na Linuksie *trzeba* używać konsoli. Na wielu popularniejszych swobodnie można jej uniknąć.

Ale kiedy raz się pozna jej możliwości, to trudno wrócić do klikania menu. Stąd się biorą ci różni ludzie na forach, zawsze podsuwający konsolkę jako rozwiązanie. Oni po prostu wsiąkli. Trochę ich rozumiem, choć ciągłe konsolowe rady powielają stereotyp.

Ja z&nbsp;kolei stoję w rozkroku między światami i&nbsp;lubię tłumaczyć z&nbsp;konsolowego na ludzki.

{% include info.html
type="Podobne wpisy"
text="Jeśli chcesz poznać więcej podstaw Linuksa, zaserwowanych w&nbsp;podobny sposób jak tutaj, to zapraszam na przykład do wpisu o&nbsp;[włączaniu języka polskiego na Mincie](/tutorials/linux-mint-jezyk-polski-system){:.internal}.  
Albo do wpisu na temat [zdobywania czcionek z&nbsp;Windowsa](/tutorials/libre-office-czcionki-worda){:.internal}. Zawarte tam rady pozwolą na przykład używać *Comic Sansa* w&nbsp;programie Libre Office."
%}
