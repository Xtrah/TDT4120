# Counting sort

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Counting sort er en effektiv sorteringsalgoritme om det er mange elementer, men få forskjellige elementer.

Anta at du kan kun ha $k$ distinkte elementer. Tell hvor mange instanser det er av hvert element, og gjør tellingen om til indekser. Flytt elementer til en ny liste basert på indeksen du fant.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

- Listen må bestå av heltall-verdier

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

- Ikke sammenligningsbasert
- **Counting sort** slår **radix sort** hvis antallet elementer $n \gg k$ forskjellige elementer. (_Dette er også det tilfellet hvor algoritmen er mest effektiv._)
- Sorterer basert på at alle input-elementene $n$ er heltall med en range mellom $0$ og $k$.
- Ikke in-place da den lager en ny liste midlertidig for å telle antall forekomster av hvert element
- Stabil: den relative rekkefølgen til elementene i listen opprettholdes under sorteringen

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
TODO | TODO | TODO | TODO

## Python kodeeksempel
