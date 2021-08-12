# Transitive-Closure
<!-- [K3] Forstå Transitive-Closure -->

<!--
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Transitive-Closure er lik som Floyd-Warshall, men sjekker kun om det finnes en sti eller ikke, og ignorerer kantvekter.

Vi kjører en kunstig konstruering av delinstanser: Vi begrenser hvilke noder vi har lov til å gå igjennom.

Vi kan først forsøke å gå gjennom $k-1$ noder og deretter først kun gå fra $i$ til $k-1$ noder og $k$ til $j$.

Notasjon: $t^{(k)}_{ij}$

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

Input: En rettet graf $G=(V,E)$.  
Output: En rettet graf $G*=(V,E*)$ der $(i,j)\in E*$ hvis og bare hvis det finnes en sti fra $i$ til $j$ i $G$.

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | TODO | TODO

## Python kodeeksempel
