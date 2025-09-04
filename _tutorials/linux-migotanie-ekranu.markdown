---
layout: page
title: Jak naprawić błąd z migotaniem ekranu na Linuksie
description: "Intel nabroił, a darmowy system dostaje za to bęcki."
---

Systemy operacyjne oparte na Linuksie mogą być wybawieniem w&nbsp;czasach, kiedy [Microsoft mocno przegina](/2025/04/22/koniec-windows-10-rok-linuksa){:.internal}, kończąc wsparcie dla Windowsa 10&nbsp;i proponując w&nbsp;zamian Windowsa 11. Pełnego niedoróbek i&nbsp;niedziałającego na wielu urządzeniach przez sztucznie stawiane wymogi.

Jeśli ludzie mają przechodzić na nowy system, ważne jest jednak dobre pierwsze wrażenie. Każdy możliwy błąd – nawet jeśli nie wynika z&nbsp;winy Linuksa – może zostać uznany za dowód dziadostwa i&nbsp;zniechęcić do systemu.

Idealnym przykładem jest błąd, z&nbsp;którym sam się zetknąłem, polegający na nagłym migotaniu ekranu w&nbsp;losowych momentach.  
Występuje na względnie nowych Linuksach i&nbsp;wynika z&nbsp;działań firmy Intel. Można go łatwo naprawić przez aktualizację jądra systemu albo wpisanie krótkiego fragmentu tekstu w&nbsp;odpowiednie miejsce.

O co chodzi? Już piszę.

## Spis treści

* [Opis błędu](#opis-błędu)
* [Diagnoza](#diagnoza)
* [Rozwiązania](#rozwiązania)
  * [Sposób 1&nbsp;– aktualizacja jądra systemu](#sposób-1-aktualizacja-jądra-systemu)
  * [Sposób 2&nbsp;– zmiana parametru programu GRUB](#sposób-2-zmiana-parametru-programu-grub)
  * [Sposób 3&nbsp;(dla trybu live USB)](#sposób-3dla-trybu-live-usb)
  * [Jak sprawdzić, czy zadziałało](#jak-sprawdzić-czy-zadziałało)
* [Słowo na koniec](#słowo-na-koniec)

## Opis błędu

Korzystam sobie beztrosko z&nbsp;Linuksa na komputerze, jeżdżę kursorem po oknach, klikam w&nbsp;różne rzeczy. Nagle, na ułamek sekundy, ekran błyska bielą albo czernią. Potem obraz wraca.

Albo może chcę połączyć się z&nbsp;jakimś hotspotem? Zjeżdżam kursorem w&nbsp;stronę ikonki Wi-Fi w&nbsp;dolnym prawym rogu i&nbsp;rozwijam listę wykrytych punktów.

{:.figure .bigspace}
<img src="/assets/tutorials/linux-migotanie-ekranu/linux-mint-sieci-wifi.jpg" alt="Zrzut ekranu pokazujący dolny róg ekranu na Linuksie. Widać tam długą listę hotspotów o&nbsp;zakrytych nazwach"/>

Jeśli mam pecha, to w&nbsp;tym momencie ekran zaczyna migać z&nbsp;dużo większą intensywnością, jak stroboskop. Odruchowo uciekam kursorem, migotanie w&nbsp;momencie ustaje.

{:.post-meta .bigspace-after}
Nieprzypadkowo przywołuję tu listę hotspotów. Zauważyłem, że tam szczególnie lubi aktywować się błąd, zwłaszcza jeśli lista wykrytych hotspotów jest długa, jak na screenie. Przynajmniej w&nbsp;przypadku Minta w&nbsp;wariancie Mate, z&nbsp;którego najczęściej korzystam. 

Opisane dwa oblicza błędu -- pojedyncze błyski albo ich gwałtowna seria -- wydają się pojawiać w&nbsp;całkiem losowych momentach. Dekoncentrują i&nbsp;irytują, zaburzając spokojne sesje przy komputerze.

Problem pojawia się na paru nowych, polecanych i&nbsp;popularnych Linuksach, jak wspomniany już Mint (sprawdzałem warianty Mate i&nbsp;Cinnamon) czy Fedora w&nbsp;wariancie KDE Plasma. To niedobrze, bo **jest spora szansa, że z&nbsp;błędem zderzy się niejedna osoba właśnie migrująca z&nbsp;Windowsa**.

## Diagnoza

Na początku nie miałem żadnych informacji poza tym, że coś mi migocze. Przeszukałem zatem anglojęzyczny internet pod kątem hasła `linux screen flickering` (albo `screen glitching`). W&nbsp;ten sposób trafiłem na różne dyskusje na forach.

Polecam spośród nich dwie: [jedną z&nbsp;oficjalnego forum Minta](https://forums.linuxmint.com/viewtopic.php?t=427916) i&nbsp;drugą [z Launchpada](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2062951). Poza rozwiązaniem problemu można tam znaleźć również genezę błędu:

* problem dotyczy komputerów z&nbsp;procesorami Intela;
* dokładniej rzecz biorąc, dotyczy zintegrowanej, wbudowanej w&nbsp;procesor karty graficznej;
* **winny jest błąd w&nbsp;sterowniku od firmy Intel**, *i915*, dodanym przez pracowników firmy do jądra Linuksa.

Jeśli mamy procesor Intela i&nbsp;zintegrowaną z&nbsp;nim kartę graficzną, to jest spora szansa, że to właśnie ona jest przyczyną błędu. Jeśli nie, zaś w&nbsp;komputerze tkwią np. tylko podzespoły od AMD czy nVidii -- to obawiam się, że problem tkwi w&nbsp;czymś innym i&nbsp;nie będę w&nbsp;stanie pomóc. Reszta poradnika skupia się na tym intelowym błędzie.

{% include details.html summary="Dodatkowy (konsolowy) sposób na zdiagnozowanie problemu" %}

Błyskom, o&nbsp;których tu piszę, towarzyszy bardzo konkretny, zakulisowy błąd. Można sprawdzić, czy występuje w&nbsp;naszym przypadku. W&nbsp;tym celu trzeba uruchomić terminal/konsolę (np. klikając ikonkę z&nbsp;dolnego paska) i&nbsp;użyć następującego polecenia:

<div class="black-bg mono">
dmesg -T
</div>

{:.figcaption}
Dla osób całkiem niekonsolowych: trzeba to wkleić w&nbsp;konsolę, po czym nacisnąć *Enter*.

W konsoli wyświetli się dziennik błędów. Można go sobie przewijać myszą/touchpadem, wypatrując takiego komunikatu (wyróżniającego się czerwonym kolorem):

<pre class="black-bg mono nospace">
i915 0000:00:02.0: [drm] *ERROR* CPU pipe A FIFO underrun
</pre>

{:.figcaption}
Mikrociekawostka: w&nbsp;tym kontekście DRM to nie zabezpieczenia antypirackie, lecz *Direct Rendering Manager*, moduł od grafiki.

Czas wystąpienia błędu, widoczny na początku linijki, powinien się pokrywać z&nbsp;momentem wystąpienia błysków. Jeśli tak -- to super, prawie na pewno mamy ten konkretny problem, o&nbsp;którym tu piszę. Stąd już tylko krok do rozwiązania :smile:

{% include details-end.html %}

Intel nie przyniósł wprawdzie obiecanych miejsc pracy w&nbsp;hucznie zapowiadanej, wielkiej polskiej fabryce, bo niedawno [wycofał się z&nbsp;projektu](https://polskieradio24.pl/artykul/3556235,inwestycja-intela-odwolana-miala-zmienic-nasze-miejsce-na-swiatowej-mapie)... Ale przynajmniej dał mi trochę (niepłatnej) roboty przy tym wpisie. Dzięki, Intelu, dobre i&nbsp;to :wink:

{:.post-meta .bigspace-after}
Gdyby ktoś chciał więcej prztyczków wymierzonych Intelowi, to zachęcam do wpisu o&nbsp;module [Intel Management Engine](/cyfrowy_feudalizm/2021/07/26/intel-management-engine){:.internal}. Taki mało znany dynks upychany w&nbsp;procesorach, który może działać wbrew interesom użytkowników.

## Rozwiązania

Zacznę od czegoś doraźnego. Jeśli zaczyna się dłuższa seria błysków, to powinno ją szybko zakończyć **przesunięcie kursora w&nbsp;górę**. Z&nbsp;jakiegoś subtelnego powodu błąd „trzyma się dołu ekranu”.

Oczywiście rozwiązaniem bym tego nie nazwał, bo choć jest to sposób na zredukowanie liczby błysków, to już pierwszy z&nbsp;nich wystarczy, żeby zirytować i&nbsp;wybić z&nbsp;rytmu. Istnieje natomiast parę sposobów na to, żeby wyłączyć je raz a&nbsp;dobrze.

{% include info.html
type="Uwaga"
text="Opis rozwiązań dostosowałem do systemu Linux Mint. Na innych rozwiązanie może być podobne (jeśli chodzi o&nbsp;konkretne rzeczy wklejane do konkretnych plików), ale nie mogę tego zagwarantować."
%}

### Sposób 1&nbsp;– aktualizacja jądra systemu

Jeśli Linux jest już u&nbsp;nas zainstalowany na dysku, to najprostszym sposobem na naprawę błędu będzie **aktualizacja jądra systemu**, czyli jego centralnej części, odpowiedzialnej m.in. za sterowniki. W&nbsp;jego nowszych wersjach usterka jest już załatana.

To sposób łatwy i przyjemny, wymagający jedynie klikania myszą.  
Poniżej dokładniej opisałem kroki dla systemu Linux Mint. W&nbsp;przypadku innych wariantów Linuksa można sobie poszukać w&nbsp;internecie pod hasłem `<nazwa_linuksa> aktualizacja jądra`, też powinny wyskoczyć przystępne rozwiązania.

{% include details.html summary="Jak zaktualizować jądro Minta" %}

W przypadku Minta należy kliknąć w&nbsp;ikonkę systemu w&nbsp;dolnym lewym rogu, żeby wyświetlić listę wszystkich zainstalowanych programów, podzielonych na kategorie (jeśli zamiast nich pokaże się zakładka `Ulubione`, to należy kliknąć `Wszystkie programy` w&nbsp;górnym prawym rogu, żeby przełączyć tryb).

Następnie trzeba kliknąć kafelek `Administracja` i&nbsp;wybrać program `Menedżer aktualizacji` z&nbsp;rozwijanej listy. Tam pokaże się lista rzeczy, jakie można zaktualizować. Należy z&nbsp;niej wybrać jądro systemu, inne rzeczy można póki co odhaczyć.

Gdy aktualizacja zacznie się pobierać, to można sobie zrobić kawę, bo może chwilę potrwać. Po jej zakończeniu należy uruchomić ponownie komputer.

{% include details-end.html %}

### Sposób 2&nbsp;– zmiana parametru programu GRUB

Jeśli mamy zainstalowanego Linuksa, ale z&nbsp;jakiegoś powodu nie możemy albo nie chcemy aktualizować jądra, to można ręcznie dodać jedną konkretną opcję w&nbsp;ustawieniach programu GRUB (*Great Unified Bootloader*, gdzie *bootloader* można rozumieć jako *uruchamiacza*; to on ładuje system podczas uruchamiania).

I tutaj robi się ciekawie. O&nbsp;ile znalezione przeze mnie rozwiązania opierają się ogólnie na tym samym -- wklejeniu tekstu w&nbsp;odpowiednie miejsce -- o&nbsp;tyle są różne propozycje [co do samego tekstu](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2062951).  
Najpewniejsze i&nbsp;najmniej problematyczne wydaje mi się użycie takiego. Można je sobie skopiować:

```
intel_iommu=igfx_off
```

Miałem okazję osobiście przetestować to ustawienie, działało sprawnie i&nbsp;bez efektów ubocznych. Niektórzy piszą, że po jego włączeniu nieco gorzej działają maszyny wirtualne, takie jak VirtualBox... Ale większość osób i&nbsp;tak z&nbsp;nich nie korzysta i&nbsp;nie powinny odczuć negatywów.

{% include details.html summary="Alternatywna opcja" %}

W tym miejscu podam też inne opcje, które zadziałały u&nbsp;komentujących. Gdyby ktoś się na nie zdecydował, to we wszystkich miejscach, gdzie wklejam `intel_iommu=igfx_off`, należy zamiast tego wkleić poniższy tekst:

```
i915.enable_dc=0 intel_idle.max_cstate=2
```

Jeśli zdecydujesz się użyć tego zestawu parametrów, to zachęcam do skopiowania ich stąd, a&nbsp;nie ręcznego przepisywania -- jest tu trochę niuansów ze spacjami, kropkami i&nbsp;podkreślnikami, które łatwo przegapić na oko.

{:.post-meta .bigspace-after}
[Na forum](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1958191) ktoś napisał, że przy wartości `2` jeszcze czasem migotało, przy `4` przestało zupełnie.

{% include details-end.html %}

Skopiowany tekst należy teraz wkleić do *pliku konfiguracyjnego* GRUB-a. **To plik systemowy, więc zmiana jego treści wymaga uprawnień administratora**. Poniżej dwa sposoby na otwarcie go w&nbsp;trybie uprzywilejowanym:

* Zwykła klikanina

  Można otworzyć „Eksploratora” (przeglądarkę plików) i&nbsp;kliknąć w&nbsp;kolumnie po lewej stronie `System plików`, żeby wejść do głównego folderu systemowego. W nim należy kliknąć folder `etc`.  
  Wewnątrz niego należy kliknąć folder `default` prawym przyciskiem myszy (ważne!), wybrać opcję `Otwórz jako administrator` i&nbsp;zaakceptować ostrzeżenie.  
  Na koniec należy kliknąć zawarty w&nbsp;tym folderze plik tekstowy `grub` (*nie* folder *grub.d*).

* Sposób konsolowy
  
  Można też uruchomić konsolę i&nbsp;wpisać w&nbsp;nią:

  <pre class="black-bg mono nospace">
  sudo xdg-open /etc/default/grub 
  </pre>

  {:.figcaption}
  Polecenie `xdg-open` powinno otworzyć plik w&nbsp;domyślnym programie do edycji tekstu; może jednak nie działać na niektórych Linuksach. Po wykoniu komendy system poprosi o&nbsp;podanie hasła.

Niezależnie od wybranego sposobu, skończy się otwarciem pliku GRUB-a w&nbsp;edytorze tekstu. Na Mincie u&nbsp;góry będzie groźna poprzeczka z&nbsp;napisem `Elevated Privileges` na czerwonym tle. Znak, że mamy uprawnienia admina. I&nbsp;zachęta, żeby zachować czujność i&nbsp;nie zmieniać byle czego.

W pliku należy wypatrzyć wzrokiem linijkę zaczynającą się od `GRUB_CMDLINE_LINUX_DEFAULT` i&nbsp;dokleić do niej skopiowane wcześniej ustawienie (pamiętając, żeby było oddzielone spacjami od treści innych ustawień; nie należy też ruszać cudzysłowów podwójnych!).

Tak wyglądała u&nbsp;mnie zmieniona linijka po wklejeniu tekstu:

<pre class="black-bg mono nospace">
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash <span class='corr-ins'>intel_iommu=igfx_off</span>"
</pre>

{:.figcaption}
Uwaga dla urządzeń mobilnych: tekst wyżej może nie mieścić się w&nbsp;polu na szerokość. W&nbsp;razie czego można przewijać je w&nbsp;poziomie.

Po zmianie tekstu należy zapisać plik (`Ctrl+S`). Następnie trzeba otworzyć konsolę (można ikoną z&nbsp;dolnego paska, nie trzeba w&nbsp;konkretnym folderze) i&nbsp;użyć w&nbsp;niej komendy:

<div class="black-bg mono nospace">
sudo update-grub
</div>

{:.figcaption}
Jak to przy *sudo* -- zapewne poprosi o&nbsp;podanie hasła.

Ustawienie zostanie zapamiętane i&nbsp;powinno być od teraz ładowane przy każdym uruchomieniu komputera. Należy go teraz wyłączyć i&nbsp;włączyć ponownie i&nbsp;zobaczyć, czy migotanie ustało.

### Sposób 3&nbsp;(dla trybu live USB)

A co, jeśli ktoś nie ma Linuksa zainstalowanego na dysku, tylko uruchamia go z&nbsp;pendrive'a, w&nbsp;tzw. *trybie live*? Być może w&nbsp;celu przetestowania go przed instalacją? Fajnie by było się jak najszybciej upewnić, że nie będzie się skazanym na migotanie.

W tym wypadku edycja plików GRUB-a z&nbsp;poprzedniego punktu nic by nie dała, *nie dałaby nic*{:.corr-del}. Sesja *live* jest ulotna, a&nbsp;po wyłączeniu komputera ustawienia z&nbsp;plików zostaną wyczyszczone.

Ale nie wszystko stracone. Te same wartości można ustawiać również *przed* załadowaniem systemu. Kiedy podczas jego uruchamiania wyświetli się czarno-białe [okno GRUB-a](https://linuxmint-user-guide.readthedocs.io/en/latest/grub.html), trzeba:

* nacisnąć klawisz `E`,
* po pojawieniu się menu z&nbsp;opcjami uruchamiania poszukać wzrokiem tekstu `quiet splash` i&nbsp;dopisać w&nbsp;tej linijce nasze ustawienie ratujące sytuację.

  <div class="black-bg mono nospace">
  quiet splash <span class="corr-ins">intel_iommu=igfx_off</span> --
  </div>

  {:.figcaption}
  Tym razem trzeba wpisać to ręcznie, więc warto zwracać szczególną uwagę na literówki oraz na to, czy ustawienie jest oddzielone spacjami od tych po bokach.

* nacisnąć `F10`, żeby kontynuować uruchamianie z&nbsp;nowymi opcjami.

### Jak sprawdzić, czy zadziałało

Najprostszym, intuicyjnym sposobem wydaje mi się celowe i&nbsp;wielokrotne zajrzenie w&nbsp;miejsce, gdzie błąd lubi się pojawiać.

W przypadku Minta jest to wspomniana lista hotspotów, o&nbsp;ile wokół nas jest ich wiele.

Klikamy ikonę połączenia w&nbsp;dolnym rogu i&nbsp;najeżdżamy kursorem na opcję `Dostępne sieci`, żeby lista się rozwinęła. Odsuwamy kursor, żeby się schowała. I&nbsp;tak kilkanaście razy (im więcej, tym większa pewność). Jeśli nic nie mignie, to jest spora szansa, że błąd został zażegnany.

## Słowo na koniec

Opisany tutaj błąd jest niestety z&nbsp;gatunku tych najgorszych -- jest *regresją*, czyli zmianą na gorsze pojawiającą się po aktualizacji do nowej (teoretycznie lepszej) wersji.

Poza tym jest wyjątkowo widoczny i&nbsp;irytujący. Sprawia, że Linux wypada niekorzystnie. A&nbsp;że to ludzie z&nbsp;Intela odpowiadali za zmiany? Raczej mało kto się o&nbsp;tym dowie.

W podobny sposób Linuksowi (i&nbsp;szerszemu ruchowi otwartego oprogramowania) już nieraz niesłusznie się dostawało za cudze przewinienia. Bo niektórzy intuicyjnie wypatrują winnych tam, gdzie coś jest darmowe.

Nie będę udawał, że Linux to system, który każdemu podpasuje. Nie mam też zamiaru ukrywać, że występują w&nbsp;nim czasem błędy. Chętnie wychodzę im naprzeciw, tak jak w&nbsp;tym poradniku.  
Ale jeśli miałbym poprosić o&nbsp;coś w&nbsp;zamian, to byłoby to porzucenie u&nbsp;siebie (albo zwalczanie u&nbsp;innych) mentalności „darmowe = złe”. Dojrzenie niuansów. Tylko w&nbsp;ten sposób alternatywy mogą się przebić i&nbsp;podkopać pozycję monopolistów :smile:

