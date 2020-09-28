# Binary search (bisect)

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Binary search er en av de mest effektive metodene å søke igjennom en sortert liste.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
Binary search krever en sortert liste.

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning

Best case | Average case | Worst case
---------|----------|---------
 $O(1)$ | $O(\log n)$ | $O(\log n)$

## Python kodeeksempel

```python
def binary_search(li, value, start=0):
    # Dersom lista er tom, kan vi ikke finne elementet
    if not li:
        return -1
    middle = len(li) // 2
    middle_value = li[middle]
    if value == middle_value:
        return start + middle
    elif value < middle_value:
        # Første halvdel
        return binary_search(li[:middle], value, start)
    elif value > middle_value:
        # Siste halvdel
        return binary_search(li[middle + 1:], value, start + middle + 1)
```
