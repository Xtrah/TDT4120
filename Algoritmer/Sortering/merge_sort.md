# Merge sort
<!-- [C4] Forstå Merge-Sort -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Merge sort er en effektiv splitt og hersk algoritme som rekursivt deler listen i to flere ganger, før den sorterer de tilbake parvis.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->
Input: En sekvens med $n$ nummer $(a_1,a_2,...\space a_n)$  
Output: En permutasjon (omorganisering) av input sekvensen slik at $(a'_1 \leq a'_2 \leq ... a'_n)$

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn

1. Splitt den $n$ lange sekvensen til to subsekvenser med $n/2$ elementer hver.
2. Sorter subsekvensene rekursivt ved bruk av merge sort.
3. Kombiner (merge) de to sorterte subsekvensene parvis sammen for å produsere en sortert output.

## Korrekthetsbevis
<!-- TBA -->
Hvis du slår sammen to sorterte lister med merge metoden, vil du til slutt få en sortert liste.

## Styrker og svakheter sammenlignet med andre

- Ikke in-place: Merge sort lager en kopi av hele sekvensen som skal sorteres, med en øvre og en nedre halvdel. Da den kopierer mer enn et konstant nummer av elementer på en gang, merge sort er **ikke in-place**
- Stabil: Ja, den relative rekkefølgen til elementene i listen opprettholdes under sorteringen

## Kjøretid og utregning

Kilde: side 36, Introduction to Algorithms

<!-- Utregning for Merge? -->
Det er gitt at `Merge` bruker $\Theta(n)$ for å slå sammen $n$ elementer.

I utgangspunktet vil merge sort fungere for både partalls- og oddetallslister, men for enkelhets skyld tar kun utregningen hvor vi antar listen kan deles på 2, slik at hver påfølgende liste er $n/2$ stor. Rekurrensen $T(n)$, worst-case for merge sort hvor $n > 1$, blir da:

1. Splitt: Finn midten av av inneværende liste tar konstant tid uansett størrelse, $O(1)$  
2. Hersk: Rekursivt løs 2 underproblemer, hver av størrelse $n/2$, som legger på $2T(n/2)$.
3. Kombiner: `Merge` prosedyren slår sammen $n$ elementer, og bruker $\Theta(n)$.
4. Dermed har vi rekurrensen $T(n)=2T(n/2)+n$
5. Ved å bruke masterteoremet finner vi kjøretiden $O(n \log n)$

Best case | Average case | Worst case | Minne
---------|----------|---------|--------
 $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$

## Python kodeeksempel

![GIF LOL](https://i.imgur.com/R0JN21t.gif)

```python
def merge_sort(li):
    if len(li) < 2: # Dersom vi har en liste med ett element, returner listen, da den er sortert
        return li
    sorted_l = merge_sort(li[:len(li)//2])
    sorted_r = merge_sort(li[len(li)//2:])
    return merge(sorted_l, sorted_r)

def merge(left, right):
    res = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        elif len(left) > 0:
            res.append(left.pop(0))
        elif len(right) > 0:
            res.append(right.pop(0))
    return res
```
