# Johnsons algoritme
<!-- [K4] Forstå Johnson -->

<!--
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Johnsons algoritme kjører en kombinasjon av Bellman-Ford og Dijkstra. Det som er spesielt med denne algoritmen er hvordan den justerer kantvekter, selv når de er negative.

Algoritmen returnerer enten en matrise for alle korteste vei vektene for alle nodeparene eller rapporterer at det finnes negative sykler i grafen.

Hvis vi har få kanter og kun positive kanter lønner det seg å bruke Dijkstras algoritme fra alle nodene.
Har vi derimot negative kanter og relativt få kanter er Johnsons algoritme løsningen.

Johnsons øker kantvektene, men vi kan ikke øke alle kantvektene med det største negative kantens vekt, da blir de nodene med mange kanter urettmessige "dyre". Vi er ikke garantert å bevare rangeringen av stiene om vi øker kantvektene med en konstant.

Johnsons implementerer løser dette ved å implementere en "teleskopsum". En sum som kollapser som et teleskop. Annenhvert ledd er minus det forrige. Vi ønsker at langs en hver sti skal ha en teleskopsum.
Algoritmen tilordner hver node verdi og så endrer vi kantvekten med differansen av de to verdiene. Kanten frra $u$ til $v$ oppdateres med differansen $h(u) - h(v)$. Slik vil positive og negative ledd oppheve hverandre:

![Johnson sum](/Figurer/johnsons-sum.png)

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->
- Trinn 5-6 er der teleskopsummen implementeres
- Trinn 7-11 er der matrisen med korteste vei fra alle til alle genereres.
![Johnson algorithm](/Figurer/johnsons.png)

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

Relativt få kanter med negative kanter så er johnsons et godt valg.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Med Fibonacci-haug: $O(V^3)$

Med binære min-heap: $O(V*E*lgV)$

$O(V^2 \log V + VE)$

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | $O(V^2 \log V + VE)$ | TODO

## Python kodeeksempel
