# Python projekts

Šis projekts ir rakstīts python valodā. Projekta kods no lietotāja saņem pilsētas nosaukumu, un pēc tam lietotājs saņem laika prognozi nākamajām 7 dienām, kas ietver daudzus laikapstāļu aspektus.

## Uzdevums

Ir jāatrast laika prognozi ievadītajai pilsētai nākamajām 7 dienām ar detalizētu informāciju.

Izmantojot Selenium bibliotēku, var viegli piekļūt brauzerim, izmantojot kodu.

Galvenie punkti:

1. Lietotāja ievade (input):

Lietotājam ir jāievada izvēlētu pilsētu, lai no turienes saņemtu laiks prognozi.

2. Automātiska datu iegūšana:

Ir izstrādāta programma pilnīgi automātiskai informācijas nolasīšanai no vietnes.

3. Datu attēlošana(output):

Iegūtie dati ir skaist sakārtoti, lai informāciju būtu viegli lasīt. Pateicoties tabulate bibliotēkai, iegūtie dati ir sakārtoti skaistā tabulā.

4. GitHub:

Projekts, tā kods un teorētiskā daļa ir augšupielādēti vitnē GitHub, lai varētu pilnībā piekļūt jebkurai informācijai par projektu, kā arī tā izmantošanu.

## Python bibliotēkas

1. Selenium - instrumentu kopums atuomatizētiem tīmekļa pārlūkprogrammas testiem un darbībām. Tas ļauj ar kodu automatizēt tīmekļa darbību.

        from selenium import webdriver

        from selenium.webdriver.chrome.service  import Service

        from selenium.webdriver.common.by  import By

2. Time - bibliotēka nodrošina funkcijas laika aizkavēšanai programmā, piemēram, gaidīšanai pirms koda fragmenta izpildes.

        import time

3. Tabulate - bibliotēka skaistai informācijas formatēšanai izvadei. Izveido pilnvērtīgus skaistus tabulus un veic daudzas citas funkcijas. Piemēram, informācijas izvadīšana html formātā.

        from tabulate import tabulate


## Programmatūras izmantošanas metodes

1. Projekta kodu var izmantot tīmekļa vietnei. Piemēram, lapā tiks parādīta laika prognoze visai nedēļai.

2. Šo kodu var mēģināt izmantot lietojumprogrammās, kuru mērķis ir tieši tāds pats - prognozes attēlošana.

3. To arī var izmantot, lai izveidotu spēli. Piemēram, pamatojoties uz kodu, spēlē tiks parādīti atbilstoši laikapstākļi.



### Artūras Cekanavičius, 231RDB171#   p r o j e k t s 
