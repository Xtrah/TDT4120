# Radix sort
<!-- ![D4] Forstå Radix-Sort, og hvorfor den trenger en stabil subrutine -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Radix sort antar at input er $n$ elementer med $d$ siffer, der hvert siffer kan ha opp til $k$ forskjellige verdier. Algoritmen ser som regel på det minst signifikante sifferet, sorterer med hensyn på dette sifferet, og gjentar så med det nest minst signifikante sifferet, osv. Sorterer stabilt på hvert siffer. Kan bruke bl.a. counting sort eller insertion sort som underalgoritme. Utnytter at det er et begrenset antall siffer.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

- Må ha en stabil sub-algoritme for å fungere. Dvs at den underliggende algoritmen som sorterer underlistene må være stabil.

## Trinn for trinn
<!-- Pseudokode med forklaring -->

## Korrekthetsbevis
<!-- TBA -->

## Styrker og svakheter sammenlignet med andre

- **Radix sort** slår **counting sort** hvis antallet elementer $n \ll k$ forskjellige elementer.
- In-place: Nei
- Stabil: Ja

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
$\Theta(d(n+k))$ | $\Theta(d(n+k))$ | $\Theta(d(n+k))$ | $O(n+k)$

der $d$ er antallet siffer i maksimum, $n$ er antall elementer og $k$ er antallet unike elementer.

## Python kodeeksempel

```python
def modified_counting_sort(A, B, idx): # A = Usortert liste. B = Liste hvor resultatet skal puttes. idx = indeksen som sorteringen skal basere seg på
    k = 10
    C = [0]*(k+1)
    for i in range(len(A)):
        index = int(str(A[i])[idx])
        C[index] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        index = int(str(A[i])[idx])
        B[C[index]-1] = A[i]
        C[index] -= 1
    return B


def radix_sort(A, d):
    for i in range(d-1, -1, -1):
        B = [0]*len(A)
        A = modified_counting_sort(A,B,i)
    return A
```
