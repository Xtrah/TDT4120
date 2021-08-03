# Ford-Fulkerson
<!-- [L8] Forstå Ford-Fulkerson-Method og Ford-Fulkerson -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Generell metode, ikke egentlig noen bestemt algoritme. Ford-Faulkerson med BFS er Edmonds-Karp algoritmen.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

Input: Et flytnett $G$  
Output: En flyt $f$ for $G$ med maks $|f|$

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Algoritme | Info | Best case | Worst case
---------|----------|---------|---------
Ford-Fulkerson | TODO | $O(V\cdot E^2)$ | $O(E_f)$
Edmonds-Karp | Ford-Fulkerson med BFS | $O(V\cdot E^2)$ | $O(V\cdot E^2)$

## Python kodeeksempel
