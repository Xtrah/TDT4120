# MST-Kruskal
<!-- [I5] Forstå MST-Kruskal -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Kruskals algoritme legger til alle kanter i en graf i en sortert liste basert på kantvekt. Deretter legger den til kantene i lista til en MST så lenge de ikke skaper sykler.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->
1. Legg til alle kanter i en liste basert på kantvekt
2. Start med invarianten, $T$ er et tomt MST
3. Legg til den billigste kanten i treet til $T$, som opprettholder invarianten (ikke skaper sykler)
4. Gjenta 3 til alle noder er dekket

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Kjøretiden til Kruskal er avhengig av hvilken underliggende datastruktur vi velger. Pensum bruker disjoint-set skog da den er asymptotisk den raskeste kjent.

Utdypende kjøretidsanalyse er ganske omfattende og finnes på s. 633 i boka.

Datastruktur | Tidskompleksitet
---------|----------
Disjoint-set skog | $O(E\lg V)$

## Python kodeeksempel
