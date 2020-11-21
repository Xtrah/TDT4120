# Breadth first search (BFS)
<!-- [H2] Forstå BFS, også for å finne korteste vei uten vekter -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

```pseudo
BFS(G,s):
1  for hver node element in G.V:
2    u.color = white
3    u.d = ∞
4    u.𝜋 = NIL
5  s.color = gray
6  s.d = 0
7  s.𝜋 = NIL
8  Q = tom graf
9  ENQUEUE(Q,s)
10  while Q != tom graf:
11    u = DEQUEUE(Q)
12    for hver v in G.Adj[u]:
13      if v.color == white:
14        v.color = gray
15        v.d = u.d + 1
16        v.𝜋 = u
17        ENQUEUE(Q,v)
18  u.color = black
```

1-9: Setup:

- Sett alle hvite = ubesøkt
- Avstand = $\infty$, forgjenger = NIL
- Startnode grå = Vi sier ifra at vi besøker snart
- Avstand til startnode = 0
- Lag besøkskø, legg til startnode

11: Pop av den første som skal bli besøkt.

12: Gå gjennom hver av dens naboer

13-17:

- Finner man noder som er hvite (ikke blitt sett) -> Planlegg besøk. 
- Gjør dem grå (sett)
- Noter avstand som er det den forgjengeren var + 1
- Sett forgjengeren = u
- Legg til i planlagt besøkskøen

18: Etter alle naboene til u er planlagt besøkt kan vi si hade og gjøre den svart.

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

\+ Svært effektiv når man har en graf med kanter som er like lange.

\+ God når dybden på treet varierer eller om kun **et** svar trengs, f.eks. den korteste stien i et tre.

\- Mindre minneeffektiv pga prioritetskøen som holder på **alle** nodene.

\- Skal hele treet traverseres så er DFS bedre.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Worst case
---------|----------
$\Theta(V)$ | $\Theta(V+E)$

## Python kodeeksempel
