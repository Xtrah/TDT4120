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

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

Bra for sparse graphs (altså få kanter i forhold til antall noder?)

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Med Fibonacci-haug: $O(V^3)$

Med binære min-heap: $O(V*E*lgV)$

$O(V^2 \log V + VE)$

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | TODO | TODO

## Python kodeeksempel
