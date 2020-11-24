# Quick sort
<!-- [C5] Forstå Quicksort og Randomized-Quicksort -->
<!-- TODO: Randomized-Quicksort -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Quick sort er en sammenligningsbasert splitt og hersk algoritme som velger et pivot-element, og sorterer resten av elementene basert på om de er høyere eller lavere enn pivot-elementet.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->
1. Velg et pivot-element.
2. Sorter resten av elementene i 2 del-lister utifra om de er større eller mindre enn pivot-elementet.
3. Sorter de 2 del-listene rekursivt til de bare inneholder 1 element.
4. Sett sammen elementene til du har en hel sortert liste.

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

- Splitt og hersk: Quick sort deler listen inn i mindre lister til den ender opp med en liste med 0-1 elementer, før den rekursivt sorterer de større listene.
- In-place: Ja, quick sort lager ingen kopier av listen eller sublistene, men krever litt minne for lagring av listene i de rekursive kallene.
- Ustabil: Quick sort garanterer ikke at den relative rekkefølgen til like elementer er lik under sorteringen av listen.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Kjøretiden avhenger i stor grad av hvilket element som blir valgt som pivot. Den absolutt verste kjøretiden $O(n^2)$ vil være en sortert liste i  stigende eller synkende rekkefølge hvor det første (høyeste eller minste) elementet blir valgt som pivot. Løsningen her er å velge tilfeldig pivot-element hver gang.

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 $O(n\log n)$ | $O(n\log n)$ | $O(n^2)$ | $O(\lg n)$

Grunnen til at worst-case er at første eller siste element i en sortert liste blir valgt er at man da må sjekke alle elementene.

Velger man det midterste elementet i den sorterte listen, må man sjekke logaritmisk færre elementer for hver følgende pivot.

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

## Python kodeeksempel fra boka

```python
def exchange(A, idx_A, idx_B):
    temp = A[idx_A]
    A[idx_A] = A[idx_B]
    A[idx_B] = temp


def partition(A, start, end):
    pivot = A[end]
    i = start - 1 # Index of smaller elements
    for j in range(start, end):
        if A[j] < pivot: # If the element is smaller than the pivot
            i += 1  # Increment index of smaller elements
            exchange(A, i, j) # Exchange the element at i with the element that is smaller than the pivot
    exchange(A, i + 1, end) # The pivot is placed after all the elements that are smaller than itself
    return i + 1 # Return the index of the pivot


# Partition will still use the last index as pivot, so exchange it with a random element
def randomized_partition(A, start, end):
    i = random.randint(start, end)
    exchange(A, end, i)
    return partition(A, start, end)


def quicksort(A, start, end):
    if start < end:
        mid = randomized_partition(A, start, end)  # Put the pivot in the right place
        quicksort(A, start, mid - 1)
        quicksort(A, mid + 1, end)
```
