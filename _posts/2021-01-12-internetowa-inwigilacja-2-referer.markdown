---
layout: post
title:  "Internetowa inwigilacja 2 – referer"
subtitle: "„Skąd przybywasz?”"
date:   2021-01-12 19:39:35 +0100
tags: [Internet, Inwigilacja, Porady]
firmy: [Google]
keep_referers: true
category: internetowa_inwigilacja
category_readable: "Internetowa inwigilacja"
---

W poprzednim wpisie pokazałem krótko nagłówki HTTP -- rodzaj naszej wizytówki przesyłanej za każdym razem, kiedy odwiedzamy jakąś stronę. 
 
Teraz skupię się na jednym z&nbsp;tych nagłówków, *refererze* (po polsku *strona odsyłająca*). Jego działanie było dla mnie kompletną niespo&shy;dzianką. Mimo że jest czymś absolutnie powszechnym.

Krótko: **kiedy przechodzimy między stronami internetowymi, właściciele drugiej strony często się dowiadują, jaka była ta pierwsza. I&nbsp;przekazują to innym**.

Zaskoczeni?

Zamiast opisywać suche fakty, pokażę Wam referera w&nbsp;akcji.

{% include info.html type="Ciekawostka" text="Angielska nazwa, *referer*, zawiera błąd ortograficzny. W&nbsp;środku powinny być dwa *r*. Jednak błąd wślizgnął się do oficjalnej specyfikacji, zanim ktoś zdążył go poprawić :roll_eyes:" %}

<a id="experiment"/>
## Referer w&nbsp;praktyce

Poniżej mamy dwa linki. Oba prowadzą do tej samej strony, na której się teraz znajdujemy. Kliknij i&nbsp;zobacz, jaki referer wyświetli się w&nbsp;czarnym polu pod nimi:

1. <a href="">Pierwszy link (z refererem)</a>.  
2. <a href="" rel="noreferrer">Drugi link (bez referera)</a>.  

Przychodzisz ze strony:
<div class="black-bg"><strong id="reff">Masz wyłączony JavaScript!</strong></div>

{% include info.html type="Uwaga" text="Gdybyś, zamiast klikać w&nbsp;linki, po prostu odświeżył(-a) stronę, przez menu albo naciskając `F5`, to nic by się nie pojawiło. Referery wiążą się ściśle z&nbsp;klikaniem w&nbsp;linki." %}

Oba linki prowadzą do tej samej strony. Jednak w&nbsp;drugim przypadku wprost dodałem do linku zakaz przesłania referera. **Te informacje są ujawniane domyślnie, o&nbsp;ile strona ich nie wyłączy**.

No ale dobra, możesz powiedzieć. Co z&nbsp;tego? Ciemna Strona dowiaduje się, że przychodzę z&nbsp;Ciemnej Strony. Nic specjalnego.

Póki poruszamy się po jednej stronie i&nbsp;nie pobieramy nic z&nbsp;zewnątrz, referer to faktycznie bzdet. Możesz jednak spróbować wejść na inną stronkę zewnętrzną, taką jak *What is my Referer*:

<a href="https://www.whatismyreferer.com">*whatismyreferer.com* z&nbsp;refererem z&nbsp;Ciemnej Strony</a>

Robiąc to, „poniesiesz” ze sobą na stronę B&nbsp;informację o&nbsp;tym, że przybywasz z&nbsp;Ciemnej Strony (strona A).  
Co więcej, strona B&nbsp;sama może pobierać część rzeczy ze stron C, D&nbsp;i kolejnych  
(często np. strony nie trzymają własnych czcionek, tylko proszą o&nbsp;nie Google Fonts; nie analizują ruchu samodzielnie, tylko odsyłają go do Google Analytics itp.).

Chcieliśmy tylko odwiedzić jedną stronę przez link. A&nbsp;ta papla **przesłała obcym stronom nasz nagłówek, razem z&nbsp;refererem**. Więc, tak jak w&nbsp;przypadku plotkar i&nbsp;plotkarzy z&nbsp;prawdziwego życia, teraz wiedzą już wszyscy.

Co więcej, tak się dzieje nawet wtedy, kiedy zależy nam na prywatności. **Przeglądanie w&nbsp;trybie prywatnym/incognito nie wyłącza przekazywania refererów**.

Zdziwieni?

Na pocieszenie powiem, że na niektórych stronach przekazywanie refererów jest wyłączone. Poza tym są one przesyłane **tylko wtedy, kiedy klikamy w&nbsp;linki**. Chodzenie między stronami przez „Wstecz” i&nbsp;„Dalej”, odświeżanie strony, wklejanie adresu w&nbsp;pasek przeglądarki -- żadna z&nbsp;tych rzeczy nie wyśle informacji o&nbsp;tym, gdzie byliśmy poprzednio.

## Ciemne strony referera

Referer podobno nie powstał w&nbsp;złych celach, tylko jest takim trochę reliktem dawnej sieci, który ułatwiał stronom tworzenie powiązań.

Mimo to jest kilka sposobów, w&nbsp;jakie może zostać użyty przeciwko nam:

* **Sam link do strony może sugerować coś wstydliwego**

  Przykład: [9 na 10 stron poświęconych problemom zdrowotnym łączyło się z innymi stronkami, przekazując przy tym nagłówki użytkowników](https://nakedsecurity.sophos.com/2015/02/26/how-nine-out-of-ten-healthcare-pages-leak-private-data/).  
  Dzięki temu firmy analityczne i&nbsp;reklamowe dostawały paczkę informacji. Na podstawie niektórych, na przykład plików *cookies*, mogły zapewne rozpoznać konkretnych użytkowników. A&nbsp;do tego w&nbsp;pakiecie dostawały referera pokazującego, że ta osoba oglądała właśnie podstrony o&nbsp;chorobach wenerycznych.

* **Referer może być częścią naszej „teczki”**

  Nawet jeśli nie wstydzimy się poszczególnych stron, strony potrafiące nas zidentyfikować mogą je połączyć z&nbsp;innymi informacjami, jakie o&nbsp;nas zbiorą i&nbsp;stworzyć na tej podstawie profil naszej osoby. Później mogą go również ujawnić firmom marketingowym (albo szerszej publice, jeśli ich dane wyciekną).

* **Zdradza popularność stron**.

  Odpowiednik takiego „kto przeglądał twój profil” na LinkedInie.  
  Czasami popularność nie jest fajną rzeczą. Jeśli administrator jakiejś strony A analizuje referery, to może zobaczyć, że trafia na nią coraz więcej użytkowników ze stronki B. Zaciekawiony może ją sprawdzić. A co, jeśli strona B to na przykład forum, na którym często beszta się stronę A? Albo konkurencja? W ten sposób strona A może podjąć działania przeciw B. O&nbsp;której by się nie dowiedziała, gdyby nie referery.

* **Umacnia kontrolę internetowych gigantów**.

  Trochę jak poprzedni punkt, ale w&nbsp;wersji na dużą skalę. Referery to cenne informacje o&nbsp;dynamice powiązań w&nbsp;internecie. Firmy takie jak Google mogą dawać innym [możliwość analizowania ruchu](https://support.google.com/google-ads/answer/2382957?hl=pl-PL) na stronie. Ale kto im zabroni liczyć przy tym referery i&nbsp;mieć wgląd w&nbsp;kawał internetu?  
Dzięki temu widzą jako jedni z&nbsp;pierwszych, jakie strony (a zatem również poglądy, organizacje itp.) rosną w&nbsp;siłę, a&nbsp;jakie słabną. I&nbsp;w jakie dziedziny warto włożyć ręce, żeby jeszcze bardziej umocnić swoją pozycję.  
Czy tak robią? Na chwilę obecną chcę bardziej wczytać się w&nbsp;temat, więc nie powiem. Ale sama możliwość nie napawa optymizmem.

To tyle tytułem wiedzy. Mam nadzieję że trochę Cię zaskoczyłem.

Jeśli chcesz coś z&nbsp;tym zrobić (jako użytkownik lub właściciel strony), to czytaj dalej! 

## Jak ukrywać referery

Można to zrobić bardzo łatwo. Zależy od tego, do której grupy należysz:

# Wolisz nic nie zmieniać ani nie instalować.

...W sumie niezbyt Cię obchodzą te całe referery. Albo może nie używasz swojego komputera i&nbsp;nie chcesz tak po prostu czegoś na nim zmieniać.

Ale załóżmy, że chcesz jednorazowo ukryć referera. Na przykład jesteś na jakiejś dość „osobistej” stronce A. Jest na niej link do strony B. I&nbsp;trochę jednak nie chcesz, żeby ktoś ze strony B&nbsp;zobaczył, skąd przychodzisz.

Rozwiązanie: **zamiast klikać w&nbsp;link, skopiuj go do głównego paska przeglądarki**.  
Znane mi przeglądarki (Firefox, mobilny Firefox Focus i&nbsp;Chrome, a&nbsp;pewnie wiele innych) nie wysyłają wtedy referera. A&nbsp;na stronkę wejdziesz.

Możesz to przetestować, kopiując do paska <a href="https://www.whatismyreferer.com">ten link, który normalnie przesłałby referera</a> (do *whatismyreferer.com*).

{% include info.html type="Porada" text="Na komputerze klikasz link prawym przyciskiem myszy i&nbsp;wybierasz `Kopiuj adres odnośnika`. Potem klikasz górny pasek adresu i&nbsp;tam wklejasz adres.  
Jeśli używasz komórki, przytrzymaj palec na linku i&nbsp;pasku, żeby wyświetliły się opcje kopiowania i&nbsp;wklejania." %}

# Możesz użyć dodatku do przeglądarki

Zachęcam! To minuta klikania, a&nbsp;uwolni Cię od refererów na dobre.

**W przypadku Chrome'a**:

1. Instalujemy [dodatek *Referer Control*](https://chrome.google.com/webstore/detail/referer-control/hnkcfpcejkafcihlgbojoidoihckciin) z&nbsp;oficjalnej stronki Google'a.

   Pójdzie szybko i&nbsp;bezboleśnie, do tego na początku nic Ci się nie zmieni.

2. Wchodzimy w&nbsp;menu tego dodatku, na przykład klikając ikonę po prawej stronie od górnego paska z&nbsp;adresem:

   {:.figure .bigspace}
   <img src="/assets/posts/internetowa-inwigilacja-2-referer/chrome_extensions.webp" alt="Ikona dodatku Referer Control na górnym pasku."/>

3. Otworzy się strona z&nbsp;opcjami dodatku. Klikamy opcję `Block` w&nbsp;dolnej części menu. Nie zmieniamy niczego innego.

   {:.figure .bigspace}
   <img src="/assets/posts/internetowa-inwigilacja-2-referer/referer_control_block.webp" alt="Zaznaczona opcja 'Block' w opcjach Referer Controla."/>

4. Klikamy w&nbsp;linki na tej stronie, żeby sprawdzić czy działa jak powinno.

   Włączone ustawienie nie usuwa refererów w&nbsp;obrębie tej samej strony, więc wszystkie moje linki odświeżające stronę powinny pokazywać to co poprzednio.  
Natomiast po kliknięciu w&nbsp;link do zewnętrznej stronki (*whatismyreferer*) powinno pokazywać brak referera.

{% include info.html type="Heheszki" text="Jeśli masz nastrój na śmieszkowanie, możesz ustawić jako referer dowolny tekst, jaki tylko się Ci podoba -- wystarczy kliknąć zakładkę `Custom` i&nbsp;wpisać go w&nbsp;polu.  
Według [tego źródła](https://stackoverflow.com/questions/11798451/what-is-the-maximum-length-of-referer) referer może liczyć do 2000 znaków, więc całkiem długa rozprawka by się zmieściła.  
Sam natomiast zachęcam do trollowania podglądaczy czymś krótkim, treściwym i&nbsp;wyglądającym jak prawdziwy adres strony:" trailer="<p class='figure'><img src='/assets/posts/internetowa-inwigilacja-2-referer/referer-control-custom.webp' alt='Menu Referer Controla z ustawioną opcją Custom i wpisanym tekstem google-is-evil.com.'/></p>" %}

**W przypadku Firefoksa**:

1. Instalujemy [dodatek *Referer Modifier*](https://addons.mozilla.org/en-US/firefox/addon/referer-modifier/) z&nbsp;oficjalnej stronki.
   
   (Na Firefoksie tez można użyć *Referer Controla*, ale według opinii użytkowników coś w&nbsp;nim nie działa. Dlatego osobiście korzystam z&nbsp;zamiennika).

2. Dodatek będzie niewidoczny na pasku, więc musimy wejść do menu dodatków (np. przez menu główne albo naciskając `Ctrl+Shift+A`).
3. Wybieramy go z&nbsp;listy i&nbsp;klikamy w&nbsp;zakładkę `Preferencje`:

   {:.figure .bigspace}
   <img src="/assets/posts/internetowa-inwigilacja-2-referer/referer_modifier_preferencje.webp" alt="Środkowa zakładka 'preferencje' w opcjach dodatku."/>

4. Patrzymy na opcje, naciskamy guzik na prawo od napisu *ANY* i&nbsp;wybieramy opcję `Remove`. Przy *SAME* najbezpieczniejsza jest z&nbsp;kolei opcja `Keep`:

   {:.figure .bigspace}
   <img src="/assets/posts/internetowa-inwigilacja-2-referer/referer_modifier_remove.webp" alt="Opcje zaznaczone w ustawieniach Referer Modifiera"/>

5. **Ważne!** Klikamy przycisk `Save configuration`. Nic się nie wyświetli, ale nasze ustawienia zostaną zapisane.

   Referer nie będzie wysyłany, jeśli klikniemy na stronie A link do strony B. Ale będzie działał w&nbsp;obrębie jednej strony (czyli np. Ciemna Strona → Ciemna Strona).

6. Testujemy na linkach z&nbsp;tej strony, czy wszystkie referery usunięte.

**W przypadku innych przeglądarek**:

Wiele innych przeglądarek na komputery (Edge, Brave, Opera, Vivaldi...) opiera się na tym samym silniku co Chrome, więc *Referer Control* powinien w&nbsp;nich działać tak samo.  
O Safari od Apple trudno mi się wypowiadać, bo nie korzystałem.

Na telefonie jest trudniej, ponieważ większość przeglądarek nie daje Wam możliwości instalowania dodatków.

Chwalebnym wyjątkiem na Androidzie jest Firefox (nie *Focus/Klar* ani inne wyspecjalizowane wersje, tylko ta główna). Nie sprawdzałem, ale powinno dać się na nim zainstalować *Referer Modifiera*, o&nbsp;którym wcześniej wspominałem.

Nie wiem, jak jest na iOS (iPhone'ach). Wiem jedynie, że wszystkie przeglądarki na tym systemie muszą korzystać z&nbsp;silnika Safari (również Chrome i&nbsp;Firefox!). Więc jeśli Safari nie daje możliwości usuwania refererów, to niestety mamy pecha.

# Masz swoją stronkę i&nbsp;nie chcesz zdradzać refererów użytkowników.

To się ceni! :+1:

Jeśli używasz do tworzenia swojej strony popularnego Wordpressa, to możliwe że nie musisz nic robić. Według [tego artykułu](https://www.reliablesoft.net/noreferrer-noopener/) **Wordpress automatycznie wyłącza przekazywanie refererów**.

Natomiast jeśli musisz samodzielnie usunąć referery, jednym ze sposobów jest dodanie atrybutu `rel="noreferrer"` do tych linków, które nie powinny ich przekazywać. Czyli zamiast `<a href="TWÓJ_LINK">` dajesz `<a href="TWÓJ_LINK" rel="noreferrer">`.

Możesz też wyłączyć wszystkie referery za jednym zamachem. Wystarczy że **dodasz jedną linijkę do głównego szablonu swojej strony**, w&nbsp;jej elemencie `head`. Ta linijka to `<meta name="referrer" content="same-origin"/>`.

Jeśli ją dodasz -- i&nbsp;nie wyłączysz żadną inną regułką -- referery będą działały tylko w&nbsp;obrębie Twojej stronki, a&nbsp;w przypadku linków do stron zewnętrznych będą usuwane. Obce strony nie zobaczą, że ktoś przyszedł od Ciebie.

Taką właśnie metodę wybrałem dla Ciemnej Strony. Do szablonu dodałem regułkę wskazującą, żeby usunąć referery. W&nbsp;tym poście wyjątkowo jej nie dodałem, żeby dało się pokazać działanie refererów.

Możesz natomiast wejść na dowolną inną podstronkę -- na przykład stronę główną -- i&nbsp;spojrzeć w&nbsp;źródło strony (`prawy przycisk myszy → Pokaż źródło`).  
O ile nic nie zmieniałem, element wyłączający referery będzie w&nbsp;linijce 7 od góry.

<script>
var referrer = document.referrer;
if (referrer == "") {referrer = "(referer nieznany)"};
document.getElementById("reff").innerHTML = referrer;
</script>
