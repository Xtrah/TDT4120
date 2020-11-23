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
1 Initialize-Single-Source(G,s)
2 for i=1 to |G.V| - 1
3   for each edge (u.v) ∈ G.E
4     Relax(u,v,w)
5 for each edge (u.v) ∈ G.Ez
6   if v.d > u.d + w (u,v)
7     return False
8 return True
```

1: Avstand = uendelig, forgjengernoder = NIL, startnode avstand = 0

2: Tell opp til V-1 ganger

3-4: For hver kant, slakk kanten

5-6: Er første del av relax!

7: Dersom kanten ikke ble slakket helt etter 4, returner false. Det betyr at det er en negativ sykel i grafen!

8: Hvis alle var korrekt slakket, returner true. Algoritmen fungerte!

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

\+ Kan oppdage negative sykler

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->
Operasjon | Antall | Kjøretid
----------|----------|---------
Initialisering | 1 | $\Theta(V)$
RELAX | V-1 | $\Theta(E)$
RELAX | 1 | $O(E)$

$\Theta(V*E)$

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | TODO | TODO

## Python kodeeksempel
