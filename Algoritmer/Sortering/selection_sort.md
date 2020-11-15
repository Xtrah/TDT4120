# Selection sort

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

En tidkrevende sorteringsalgoritme som søker gjennom en usortert liste og flytter det minste elementet hver gang.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->
1. Sett det første elementet som minimum.
2. Se etter mindre elementer i lista og sett eventuelle lavere elementer som ny minimum.
3. Når hele lista er traversert, flytt minimum til starten av lista.
4. Sett det neste usorterte elementet som minimum. Hvis det ikke finnes flere usorterte elementer, er lista sortert.
5. Hopp tilbake til steg 2.

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

- In-place: Ja, det blir ikke opprettet kopier av lista, elementer blir kun flyttet.
- Stabil: Nei, garanterer ikke at den relative rekkefølgen til like elementer er lik under sorteringen av listen.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

I utgangspunktet kan vi se at algoritmen inneholder 2 løkker, som gir $n \sdot n = n^2$.

Det å finne minimum i en liste krever at $n$ elementer sjekkes ($n-1$ sammenligninger), for så å flytte den til starten av lista. For å finne neste minste må man sjekke $n-1$ elementer, osv. Antall sammenligninger er dermed:
$$(n-1)+(n-2) \space ...+1 = \sum_{i=1}^{n-1} i = \frac{1}{2}(n^2-n)$$
Som gir kjøretiden $O(n^2)$ når vi dropper konstanter og lavere ordens ledd i svaret.

Best case | Average case | Worst case
---------|----------|---------
 $O(n^2)$ | $O(n^2)$ | $O(n^2)$

 <!--
 Best case | Average case | Worst case
---------|----------|---------
 $\Omega(n^2)$ | $\Theta(n^2)$ | $O(n^2)$
 -->

## Python kodeeksempel

Kilde: <https://www.programiz.com/dsa/selection-sort#code>

```python
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
```
