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
<!-- TODO: Gjøre pi om til tegnet pi og element i tegn istedet for "elem" + tom graf tegn for tom graf.-->
```pseudo
BFS(G,s):
  for hver node element i G.V:
    u.color = white
    u.d = uendelig
    u.pi = NIL
  s.color = gray
  s.d = 0
  s.pi = NIL
  Q = tom graf
  ENQUEUE(Q,s)
  while Q != tom graf:
    u = DEQUEUE(Q)
    for hver v elem G.Adj[u]:
      if v.color == white:
        v.color = gray
        v.d = u.d + 1
        v.pi = u
        ENQUEUE(Q,v)
  u.color = black
```

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

Svært effektiv når man har en graf med kanter som er like lange.

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Worst case
---------|----------
$\Theta(V)$ | $\Theta(V+E)$

## Python kodeeksempel
