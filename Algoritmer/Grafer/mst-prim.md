# MST-Prim
<!-- [I6] Forstå MST-Prim -->

<!--
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Prims algoritme vedlikeholder en løsningsmengde med noder, og legger til en node som deler kant med løsningsmengden ved hver iterasjon. Så lenge kanten som blir lagt til ikke skaper en sykel, og er den billigst mulige, så er den trygg.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

1. Start et tre med en enkel node, valgt tilfeldig
2. Legg alle mulige valg å vokse til i en prioritetskø basert på kantvekt
3. Voks treet via billigste kant som ikke skaper en sykel
4. Gjenta til prioritetskøen er tom

```pytho
MST-PRIM(G,w,r)
1   for each u in G.V                 # FOR hver node i grafen
2     u.key = ∞                           # u sin billigste kant settes lik ∞
3     u.𝜋 = NIL                           # Forelder-noden settes til NIL
4   r.key = 0                         # Roten sin billigste kant settes til 0 (for å vise at det er roten)
5   Q = G.V                           # Lager en prioritetskø som lagrer kanter fra billigst til dyrest
6   while Q = Ø                       # WHILE prioritetskøen ikke er tom:
7     u = EXTRACT-MIN(Q)                  # Finn billigste kant og gå til noden som ligger i andre enden av den
8     for each v in G.Adj[u]              # FOR hver hostliggende node til u:
9       if v in Q and w(u,v) < v.key          # IF v er i pri-kø & w(u,v) < v sin billigste kant
10          v.𝜋 = u                                 # Setter foreldernode til u
11          v.key = w(u,v)                          # Setter billigste kant til denne kanten
```

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

Prim bruker ideer tilsvarende breadth-first search.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Kjøretiden avhenger av hvordan prioritetskøen er implementert i steg 2.

Med Binary Min-Heaps:

- `BUILD-MIN-HEAP` utfører linje 1-5 i $O(V)$ tid
- Hele `while` loopen går igjennom alle noder, altså $|V|$ ganger, og `EXTRACT-MIN` bruker $O(\lg V)$ tid, totalt $O(V\lg V)$
- `for` loopen utføres på $O(E)$ tid

Datastruktur | Tidskompleksitet
---------|----------
Binary Min-Heap | $O(E\lg V$)
Fibbonaci Heaps | $O(E+V\lg V)$ (bedre)

## Python kodeeksempel
