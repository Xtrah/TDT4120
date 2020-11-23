# DAG-Shortest-Path
<!-- [J9] Forstå DAG-Shortest-Path -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

DAG står for Directed Acyclic Graph (rettet asyklisk graf). Som navnet antyder har grafen rettede kanter og ingen sykler.

Alle trær er DAGer fordi de er rettede og har ingen sykler.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->
- Kan **IKKE** ha sykler i input.
- Må ha topologisk sortering.

Men:

- Kan ha negative kanter i input.
- Kan ha negative kanter i output.

## Trinn for trinn
<!-- Pseudokode med forklaring -->
**Parametere:**  
G: Graf  
w: Vekting  
s: Startnode

```pseudo
DAG-SHORTEST-PATH(G,w,s)
1 Topologisk sortering av nodene i G
2   INITIALIZE-SINGLE-SOURCE(G,s)
3   for hver node u i G.V
4     for hver kant (u, v) i G.E
5       RELAX(u,v,w)
```

```pseudo
RELAX(u,v,w):
1   if v.d > u.d + w(u,v):
2     v.d = u.d + w(u,v)
3     v.𝜋 = u
```

1: Topologisk sortering: Gir en lineær sortering av nodene i en DAG slik at for hver kant u,v kommer u før v.

2: Alle avstander = uendelig, alle innkanter = NIL og avstanden til startnoden = 0

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Operasjon | Antall | Kjøretid
----------|----------|---------
Topologisk sortering | 1 | $\Theta(V+E)$
Initialisering | 1 | $\Theta(V)$
RELAX | E | $\Theta(1)$

Med bakgrunn i tabellen over gir dette oss: $\Theta(V+E)$

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | TODO | TODO

## Python kodeeksempel
