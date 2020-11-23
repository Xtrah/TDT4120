# Depth first search (DFS)
<!-- [H3] Forstå DFS og parentesteoremet -->

<!-- 
1. Kjenne den formelle definisjonen av det generelle problemet den løser
2. Kjenne til eventuelle tilleggskrav den stiller for å være korrekt
3. Vite hvordan den oppfører seg; kunne utføre algoritmen, trinn for trinn!
4. Forstå korrekthetsbeviset; hvordan og hvorfor virker algoritmen egentlig?
5. Kjenne til eventuelle styrker eller svakheter, sammenlignet med andre
6. Kjenne kjøretidene under ulike omstendigheter, og forstå utregningen
-->

DFS er en algoritme som er nyttig for å traversere grafer.

Klassifisering av kanter:

1. Trekanter: Er kanter i dybde først skogen G. Kanten (u,v) er en tre kant hvis den først var oppdaget ved å utforske (u,v).
2. Back edges are those edges (u,v) connecting a vertex u to an ancestor  in a
depth-first tree. We consider self-loops, which may occur in directed graphs, to
be back edges.
3. Forward edges are those nontree edges (u,v) connecting a vertex u to a descendant in a depth-first tree.
4. Cross edges are all other edges. They can go between vertices in the same
depth-first tree, as long as one vertex is not an ancestor of the other, or they can
go between vertices in different depth-first trees.

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->

Fargeforklaringer:

- Hvit: Sett, men ikke besøkt
- Grå: Besøkt, men ikke ferdig
- Svart: Ferdig

Bokstav- og forkortelsesforklaringer:

- G: Graf
- d: Starttid
- f: Sluttid
- 𝜋: forgjenger

```pseudo
DFS(G):
1  for hver node u element i G.V
2    u.color = hvit
3    u.𝜋 = NIL
4  time = 0
5  for hver node u element i G.V
6    if u.color == hvit
7      DFS-VISIT(G,u)


DFS-VISIT(G,u)
1  time = time + 1
2  u.d = time
3  u.color = grå
4  for hver v element G.adj[u]
5    if v.color == hvit
6      v.𝜋 = u
7      DFS-VISIT(G,v)
8  u.color = svart
9  time = time + 1
10  u.f = time

```

**DFS(G) forklaring:**

1-4: Setup

- Gjør hver node hvit, ikke besøkt
- Hver forgjenger = NIL
- Tiden starter på 0

5-7: Sjekk hver node. Om vi ikke har besøkt den (hvit farge), besøk den.

**DFS-VISIT(G,u)** Der $d$ er en ubesøkt node i DFS-treet.

1-3: Setup

- Tiden den ble besøkt er tiden + 1
- Starttiden (d) = den tiden
- Gjør noden grå, den er blitt besøkt

4: Se på hver nabonode til denne noden

6: Om naboen ikke er blitt besøkt (hvit), besøk den (rekursivt kall med DFS-VISIT).

8-10: Avskjed

- Når du har besøkt alle nabonodene til u:
  - Gjør den svart (ferdig)
  - Noter nåværende tid ved å legge til 1
  - Gi den sluttid (u.f) = nåværende tid

## Korrekthetsbevis

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

Best case | Worst case
---------|----------
$\Theta(V+E)$ | $\Theta(V+E)$

## Python kodeeksempel
