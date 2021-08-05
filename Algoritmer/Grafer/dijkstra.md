# Dijkstras algoritme
<!-- [J11] Forstå Dijkstra -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

Dijkstras er en grådig korteste vei algoritme som finner distanser til alle noder fra startnoden (single source shortest path). Man holder orden på hvilken node som har det laveste estimatet underveis.

Den eneste forskjellen på DAG-shortest-path og Dijkstra er hvordan vi velger den neste noden.

I DAG-shortest-path kan vi finne rekkefølgen på nodene som skal slakkes i lineær tid $\Theta(V)$ som følge av den topologiske sorteringen mens i Dijkstra må vi finne denne rekkefølgen underveis med f.eks en binær haug som tar logaritmisk tid $\Theta(lgV)$.



## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

Dijkstra krever at alle kanter er ikke-negative. Hvis det finnes negative sykler vil den ikke terminere som normalt.

Dijkstra er mest effektiv når brukt i en heap. Andre datastrukturer kan gi høyere kjøretid og er ikke dekket i pensum.

## Trinn for trinn
<!-- Pseudokode med forklaring -->
1. La $Q$ være en min-prioritetskø
2. Legg alle noder i $Q$
3. Så lenge $Q$ ikke er tom:
    - $u = Q$.pop()
    - for hver nabo $v$ av $u$:  
    `Relax(u,v)`

Alternativt

```pseudo

Dijkstra(G,q,s):
1 INITIALIZE-SINGLE-SOURCE(G,s)
2 S = ∅
3 Q = G.V
4 while Q != ∅
5   u = EXTRACT-MIN(Q)
6   S = S U {u}
7   for hver node v i G.Adj[u]
8       RELAX(u,v,w)

```

1. Setup: Alle avstander = uendelig, alle innkanter = NIL og avstanden til startnoden = 0
2. S: ettet med ferdige noder = tomt
3. Q: Pri-kø er satt til alle noder (tenk på det som en traverseringskø, bare setter det inn med en gang som i Prim)
4. Så lenge det er igjen noder i pri-kø
5. Hent ut det minste elemenentet fra køen. Den minste utnoden. Priorteten er avstandsestimatet, ikke den korteste kanten inn til traverseringstreet.
6. S brukes bare for forklaring her. Trengs ikke, men kan brukes fint i bevis.
7. For hver nabonode, kjør Relax. Vi finner en ny lengde til $u$, "reklamer" dette til alle naboer.

## Korrekthetsbevis

Når vi kjører `pop` på $u$ vil $u.d$ være korteste vei.

Altså: Når vi velger å besøke node $u$ har vi allerede funnet korteste vei til $u$.

Optimal substruktur. Gitt ingen negative kanter vil det umulig kunne være noen kortere vei, da du alltid henter den veien det er kortest til nå.

## Styrker og svakheter sammenlignet med andre

- Dijkstra bruker ideer tilsvarende breadth-first search og MST-Prim.
- Bruker avstandsestimat istedenfor kantlengde
- Lavere kjøretid enn Bellman-Ford algoritmen
- Takler **ikke** negative kantvekter

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

$\space$ | Innsetting | Pop | Oppdater
 -|----------|----------|---------
 Array | 1 | V | 1
 Binary Heap | $log(V)$ | $log(V)$ | log(V)

$|V|$: Innsettinger og pop'inger  
$|E|$: Relax

Dijkstra kjøretid basert på tabellen over:

Array: $O(V^2)$  
Binary heap: $O((V+E)\log V)$

------

Operasjon | Antall | Kjøretid
----------|----------|---------
Initialisering | 1 | $\Theta(V)$
BUILD-HEAP | 1 | $\Theta(V)$
EXTRACT-MIN | V | $O(lg(V))$
DECREASE-KEY* | E | $O(lg(V))$

*Nødvendig i RELAX

Dette gir total kjøretid $O(V\space lg(V) + E\space lg (V)$)

------

Kjøretiden avhenger av hvordan min-prioritetskøen er implementert.

Datastruktur | Tidskompleksitet
---------|----------
Fibonacci heap | $O(V\lg V + E)$
Binary min-heap | $O(E\lg V + V\lg V)$
Array | $O(V^2)$

## Python kodeeksempel
