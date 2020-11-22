# Floyd-Warshall
<!-- [K2] Forstå Floyd-Warshall -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Floyd-Warshall brukes til å finne den korteste veien mellom alle noder i en vektet rettet graf ved bruk av dynamisk programmering og vektmatriser.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

Input: En vektet, rettet graf $G=(V,E)$ uten negative sykler, der $V=[1,...,n]$, og vektene er gitt av matrisen $W=(w_{ij})$  
Output: En $n*n$ matrise $D=(d_{ij})$ med avstander, dvs. $d_{ij}=s(i,j)$

Returnerer en forgjengermatrise $\Pi=(\pi_{ij})$

$\pi^{(k)}_{ij}$ er forelderen til noden $j$ på den korteste veien (stien) fra noden $i$.

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

1. Takes in matrix $W$ ($n \times n$)
2. For each row $k$ in matrix $W$: Get the matrix $D^{k}$
3. For each vertex $i$: for each vertex $j$: find shortest path from $i$ to $j$
4. Set point in matrix equal to that path
5. Return altered matrix

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

In-place: Ja, alt skjer inne i matrisen.

|                                   | Floyd Warshall |
|-----------------------------------|----------------|
| Complexity                        | $O(v^3)$       |
| Recommended graph size            | Small          |
| Good for APSP*                    | Yes            |
| Can detect negative cycles        | Yes            |
| SP on graph with weighted edges   | Bad in general |
| SP on graph with unweighted edges | Bad in general |

*APSP = All Pairs Shortest Path

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

$\Theta(V^3)$ da det er tre nøstede løkker i algoritmen.

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 $\Theta(V^3)$ | $\Theta(V^3)$ | $\Theta(V^3)$ | $\Theta(V^2)$

## Python kodeeksempel
