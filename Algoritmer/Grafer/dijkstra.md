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

## Den formelle definisjonen av det generelle problemet
<!-- Et problem er relasjonen mellom input og output -->

## Tilleggskrav for korrekthet
<!-- Korrekhet: algoritmer virker, gir det svaret den skal -->
<!-- Eks: Binary search må ha en sortert liste -->

## Trinn for trinn
<!-- Pseudokode med forklaring -->
1. La $Q$ være en min-prioritetskø
2. Legg alle noder i $Q$
3. Så lenge $Q$ ikke er tom:
    - $u = Q$.pop()
    - for hver nabo $v$ av $u$:  
    `Relax(u,v)`

## Korrekthetsbevis

Når vi kjører `pop` på $u$ vil $u.d$ være korteste vei.

Altså: Når vi velger å besøke node $u$ har vi allerede funnet korteste vei til $u$.

Optimal substruktur. Gitt ingen negative kanter vil det umulig kunne være noen kortere vei, da du alltid henter den veien det er kortest til nå.

## Styrker og svakheter sammenlignet med andre

## Kjøretid og utregning
<!-- Under ulike omstendigheter -->

|V| Innsettinger og pop'inger  
|E| Relax

Array: $O(V^2)$  
Binary heap: $O((V+E)\log V)$
<!-- TODO: Sjekk opp. Fra eksamensforelesning 2020 -->

Best case | Average case | Worst case | Minne
---------|----------|---------|---------
 TODO | TODO | TODO | TODO

## Python kodeeksempel
