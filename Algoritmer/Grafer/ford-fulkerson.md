# Ford-Fulkerson
<!-- [L8] Forstå Ford-Fulkerson-Method og Ford-Fulkerson -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->
Baserer seg på restkapasiteten og finner forøkende stier, så lenge det er mulig.
Når det ikke lenger er mulig er flyten maksimal. Dette er det algoritmen kommer frem til.

Ford Fulkerson er en generell metode som kan implementere forskjellige subrutiner:

F.eks om vi bruker BFS får vi algoritmen som heter Edmonds-Karp.

Normal implementasjon:

- Finn forøkende sti først
- Finn så flaskehalsen i stien(lavest restkapasitet)
- Oppdaterer flyt langs stien med denne verdien.

Alternativ implementasjon, fletter inn BFS: (denne versjonen står ikke i læreboka)

- Finn flaskehalser underveis
- Hold styr på hvor mye flyt vi får frem til hver node
- Traverser bare noder vi ikke har nådd frem til ennå(BFS egenskap)

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

Maksimal flyt

Input: Et flytnett $G$  
Output: En flyt $f$ for $G$ med maks $|f|$

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

![](/Figurer/ford-fulkerson.png)

Operasjon | Antall | Kjøretid | Totalt
---------|----------|---------| ---------
Finn forøkende sti | $O(V*E)$ | $O(E)$ | $O(E*f*)$

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Algoritme | Info | Best case | Worst case
---------|----------|---------|---------
Ford-Fulkerson | TODO | $O(V\cdot E^2)$ | $O(E_f)$
Edmonds-Karp | Ford-Fulkerson med BFS | $O(V\cdot E^2)$ | $O(V\cdot E^2)$

## Python kodeeksempel
