# Binary search (bisect)
<!-- [C3] Forstå Bisect og Bisect' (se appendiks C i pensumhefte) -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Binary search er en av de mest effektive metodene å søke igjennom en sortert liste. Den halverer en sortert liste gang på gang helt til den har en liste med kun ett element.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

**Input:** En sortert liste `array`, antall elementer `n`, det vi søker etter `target`.  
**Output:** Indeks for `target` i `array`

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
Binary search krever en sortert input liste.

## Trinn for trinn
<!-- Pseudokode med forklaring -->

1. La `min = 0` og `max = n-1`
2. Om `max < min`, stopp. `target` er ikke i `array`, så vi returnerer `-1`.
3. Compute `guess` som gjennomsnittet av `max` og `min`, rundet ned til et heltall.
4. Om `array[guess]` er lik `target`, returner `guess`.
5. Om `guess` er for lav, altså `array[guess] < target`, sett `min = guess + 1`.
6. Hvis ikke var `guess` for høyt. Sett `max = guess - 1`.
7. Gå tilbake til steg 2.

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

Binary search er en utrolig god algoritme for store, sorterte lister, i forhold til lineært søk (brute force).

Hvis `array` har 10 elementer, trenger vi kun å sjekke 3 elementer for å finne `target` eller konkludere med at `target` ikke eksisterer (33%).

Enda bedre, hvis `array` har 10 000 000 elementer, trenger vi kun å sjekke 24 elementer (0.0002%).

## Kjøretid og utregning

Best case er `target` på midten av lista og algoritmen returnerer umiddelbart. Average case og worst case er mer sannsynlig, hvor algoritmen vil søke igjennom $n$ elementer hvor den eliminerer halvparten av elementene ved hver iterasjon.

Best case | Average case | Worst case
---------|----------|---------
$O(1)$ | $O(\log n)$ | $O(\log n)$

## Python kodeeksempel

```python
def binary_search(array, target, start=0):
    # Dersom lista er tom, kan vi ikke finne elementet
    if not array:
        return -1
    guess = len(array) // 2
    guess_value = array[guess]
    if target == guess_value:
        return start + guess
    elif target < guess_value:
        # Første halvdel
        return binary_search(array[:guess], target, start)
    elif target > guess_value:
        # Siste halvdel
        return binary_search(array[guess + 1:], target, start + guess + 1)
```
