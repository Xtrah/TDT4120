# Heap sort

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Det er flere metoder å sortere en heap. En max-heap er et binærtre hvor hver nodes verdi aldri er høyere enn sin forelder, og en min-heap det motsatte, hver verdi kan aldri ha en lavere verdi enn sin forelder.

Heap sort er en sammenligningsbasert algoritme, lik selection sort, hvor vi først finner maksimum og flytter den til enden, og gjentar.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

- Heap sort er in-place.
- Heap sort er typisk ustabil, men kan bli implementert som stabil. Den vil vanligvis endre den relative rekkefølgen ved duplikat-verdier.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

## Python kodeeksempel
