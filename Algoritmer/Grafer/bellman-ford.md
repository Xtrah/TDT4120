# Bellman-Ford
<!-- [J8] Forstå Bellman-Ford -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Bellman-Ford algoritmen løser single-source shortest-path (SSSP) problemet i det generelle tilfellet hvor kanter kan ha negativ vekt.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

Gitt en vektet rettet graf $G=(V,E)$ med kilde $s$ og en vektfunksjon $w : E -> \mathbb{R}$, vil Bellman-Ford returnere `True` hvis og bare hvis grafens startnode ikke finner noen ingen negativ-vekt sykler.

G = graf | w = vekting | i = teller | u = fra-node | v = til-node

```pseudo
Bellman-Ford(G,w,s)
  Initialize-Single-Source(G,s)
for i=1 to |G.V| - 1
    for each edge (u.v) ∈ G.E
      Relax(u,v,w)
for each edge (u.v) ∈ G.Ez
  if v.d > u.d + w (u,v)
    return False
return True
```

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | TODO | TODO

## Python kodeeksempel
