# Quick sort

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

- Splitt og hersk: Quick sort deler listen inn i mindre lister til den ender opp med en liste med 0-1 elementer, før den rekursivt sorterer de større listene.
- In-place: Quick sort lager ingen kopier av listen eller sublistene, men krever litt minne for lagring av listene i de rekursive kallene.
- Ustabil: Quick sort garanterer ikke at den relative rekkefølgen til like elementer er lik under sorteringen av listen.

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

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

## Python kodeeksempel

```python
def quicksort(li):
    if len(li) < 2:
        return li
    pivot = li[0]
    lo = [x for x in li if x < pivot]
    hi = [x for x in li if x > pivot]
    return quicksort(lo) + pivot + quicksort(hi)
```
