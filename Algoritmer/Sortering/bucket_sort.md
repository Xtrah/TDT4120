# Bucket sort
<!-- [D5] Forstå Bucket-Sort -->

<!--
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Bucket sort antar at input-listen er generert tilfeldig og er uniformt fordelt over et intervall. Bucket sort deler elementene inn i $k$ like store intervaller/bøtter, og så fordeles de $n$ input-tallene i bøttene. Deretter sorteres elementene i bøttene med en annen algoritme, som f.eks. insertion sort.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->
Krever uniform sannsynlighetsfordeling: For at bucket sort skal fungere må vi unngå at alle tallene havner i samme bøtte.

## Trinn for trinn
<!-- Pseudokode med forklaring -->
1. Lag en array med initielt tomme "bøtter"
2. Gå over input-listen, fordel/flytt hvert element til sin bøtte
3. Sorter hver ikke-tomme bøtte med en sorteringsalgoritme, vanligvis insertion sort
4. I rekkefølge besøk hver bøtte, flytt alle elementene tilbake til den originale listen slik at den til slutt er ferdig sortert

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre
<!-- TODO <https://en.wikipedia.org/wiki/Bucket_sort#Comparison_with_other_sorting_algorithms> -->

- In-place: Nei, bucket sort oppretter mange underlister
- Stabil: Ja dersom den underliggende algoritmen er det.
- Bucket sort med hver bøtte med størrelse 1 er en generell counting sort.
- Bucket sort med 2 bøtter er en generell quick sort som velger `mid` som pivot.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Kjøretid baserer seg i stor grad på subrutinen som blir brukt i algoritmen. Om man bruker insertion sort for å sortere hver bøtte som har gjennomsnittlig kjøretid på $\Theta(n^2)$, vil den totale gjennomsnittlige kjøretiden til bucket sort være i samme størrelsesorden.

Om man velger et konstant antall bøtter vil ikke dette påvirke den asymptotiske kjøretiden, da denne konstanten ikke vil ha noe å si når $n$ blir stor nok.

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
$\Theta(n)$ | $\Theta(n)$ | $\Theta(n^2)$ | $O(n)$

## Python kodeeksempel
