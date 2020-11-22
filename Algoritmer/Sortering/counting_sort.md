# Counting sort
<!-- [D3] Forstå Counting-Sort, og hvorfor den er stabil -->

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
- **Counting sort** slår **radix sort** hvis antallet elementer $n \gg k$ forskjellige elementer.
  - Dette er også det tilfellet hvor algoritmen er mest effektiv.
- Sorterer basert på at alle input-elementene $n$ er heltall med en range mellom $0$ og $k$.
- In-place: Nei, da den lager en ny liste midlertidig for å telle antall forekomster av hvert element
- Stabil: Ja, den relative rekkefølgen til elementene i listen opprettholdes under sorteringen. Dette skjer fordi den teller forekomster av hvert element, og for å sørge for at rett forekomst er relativt rett i output lista.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
$\Omega(n+k)$ | $\Theta(n+k)$ | $O(n+k)$ | $O(n+k)$

Dersom $k \gg n$, domineres $n$ av $k$ og derfor er $\Theta(k)$ også gyldig. I den sammenhengen vil det også være mer nøyaktig enn kjøretiden over, da vi fjerner unødvendige ledd.

Det samme gjelder motsatt vei dersom $n \gg k$, da vil kjøretiden bli $\Theta(n)$.

## Python kodeeksempel

Ved universitetet på Pluto har hvert emne sin egen karakterskala. For et gitt emne består karakterskalaen av alle heltall i, slik at $0 \leq i \leq k$. Administrasjonen ved universitetet ønsker å sortere karakterene i emnene, slik at de lettere kan utføre statistiske utregninger. Dessverre kjenner ikke administrasjonen til verdien for $k$ for hvert enkelt emne, de vet kun at denne verdien alltid er slik at $k<2048$.

Implementer en variant av COUNTING-SORT&trade; som ikke tar inn $k$, men som alltid vil kunne sortere en liste av karakterer i et emne ved universitetet på Pluto. Metoden skal skrive resultatet til B, som har lik lengde som A.

```python
def counting_sort(A, B):
  AmountCount = []
  k = 2048
  AmountCount = [0]*k # Genererer array på lengde k
  for grade in A:
    AmountCount[grade] += 1 # Teller instanser av hvert tall
  for i in range(1,k):
    AmountCount[i] += AmountCount[i-1]
  for n in range(len(A),0,-1): # Går baklengs for å gjøre algoritmen stabil
    num = A[n-1]
    B[AmountCount[num]-1] = num
    AmountCount[num] -= 1
  return B
```
