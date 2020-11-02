# Insertion sort
<!-- [A8] Forstå Insertion-Sort -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

En effektiv algoritme for å sortere et lavt antall elementer.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->
Input: En sekvens med $n$ nummer $(a_1,a_2,...\space a_n)$  
Output: En permutasjon (omorganisering) av input sekvensen slik at $(a'_1 \leq a'_2 \leq ... a'_n)$

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

- In-place: Insertion sort lager aldri en kopi av sekvensen under kjøringen, så den er lite plasskrevende.
- Stabil: den relative rekkefølgen til elementene i listen opprettholdes under sorteringen

## Kjøretid og utregning

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
| $\Theta(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$

## Python kodeeksempel

```python
def insertion_sort(A):
    for x in range(1,len(A)):
        key = A[x]
        # Plasserer A[x] inn i den sorterte sublisten [0..x-1]
        i = x-1
        while i>=0 and A[i] > key:
            # Flytter hvert element en til høyre, så lenge key < A[i]
            A[i+1] = A[i]
            i -= 1
        # Plasserer key på riktig plass
        A[i+1] = key
    return A;
```
