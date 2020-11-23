# Topological sort
<!-- [H5] Forstå Topological-Sort -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->
Dersom man har behov for rekkefølge på nodene så gir topologisk sortering en lineær sortering av noder i en DAG slik at for hver kant $u,v$ så kommer $u$ før $v$. Det kan finnes flere topologiske sorteringer for en graf.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->
```pseudo

Topological-Sort(G):
1   kall DFS for å beregne slutt-tid for hver node
2   for hver node som blir ferdig
3   insert den foran i en lenket liste
4 returner den lenkede listen

```

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

DFS: $\Theta(V+E)$

Insert i listen: $O(1)$

Kjøretid: $\Theta(V+E)$

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | TODO | TODO

## Python kodeeksempel
