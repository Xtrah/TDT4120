# Heap sort
<!-- [E2] Forstå Heapsort -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

En max-heap er sortert slik at rot-noden er den største noden av alle nodene i heapen. Alle forelder-noder i heapen er større en barne-nodene sine. For Min-heap er det motsatt.

Heapsort begynner med å bygge en max-heap (Build-max-heap) av en liste med tall. Man sikrer dermed en gyldig Max-heap hvor rot-noden er den største noden i heapen.

Heapsort henter derette ut roten (det største tallet) og trekker opp en av nodene fra bunnen og setter den som ny rot. Nå er alle sub-grafene til roten en max-heap, men roten i seg selv gjør at hele treet er feil (ettersom den er av lav verdi).

Ved å kjøre max-heapify vil man nok en gang kunne hente opp det største tallet i heapen. Dette tallet kan igjen hentes ut og erstattes med et lavt tall fra bunnen av heapen.

ALgoritmen utnytter altså at max-heapify alltid finner maximum i heapen og bruker dette til å sortere den originale listen.

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

- In-place: Ja
- Stabil: Nei, Heap sort er typisk ustabil, men kan bli implementert som stabil. Den vil vanligvis endre den relative rekkefølgen ved duplikat-verdier.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->
Best case | Average case | Worst case | Minne
---------|----------|---------|--------
 $O(n \log n)$ | ??? | $O(n \log n)$ | $O(1)$
<!-- En heap bruker logaritmisk tid for å ta ut det største eller minste elementet i heapen (?) -->

Heapsort bygger først en max-heap ved hjelp av Build-max-heap. Nå er det største elementet på toppen. Dette elementet hentes ut fra heapen. Den flytter så en av de minste elementene helt til toppen før den kjører Max-heapify igjen.

Max-heapify garanterer at det største elementet i heapen nok en gang kommer til toppen. Denne prosessen gjør det mulig å hente ut det største elementet i heapen hver gang.

$O(n \log (n))$ kommer av at det kjøres Max-heapify for hvert element.

## Python kodeeksempel
