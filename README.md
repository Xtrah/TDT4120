# TDT4120 Algoritmer og datastrukturer

- [Algoritmer](Algoritmer/)
- [Eksterne ressurser](Ressurser/)

<details>
<summary>Overordnede læringsmål i faget</summary>

- Ha kunnskap om
  - et bredt spekter av etablerte algoritmer og datastruktuer
  - klassiske algoritmiske problemer med kjente effektive løsninger
  - komplekse algoritmer uten kjente effektive løsninger
- Ha ferdigheter for å
  - analysere algoritmers korrekthet og kjøretid
  - formulere problemer som kan løses av algoritmer
  - konstruere nye effektive algoritmer
- Være i stand til å
  - bruke eksisterende algoritmer og programvare på nye problemer
  - utvikle nye løsninger på praktiske algoritmiske problemstillinger
- Ved hver algoritme skal man
  - kjenne til den formelle definisjonen av det generelle problemet algoritmen løser
  - kjenne til eventuelle tilleggskrav den stiller for å være korrekt
  - vite hvordan den oppfører seg, kunne utføre den, trinn for trinn
  - forstå korrekthetsbeviset; hvordan og hvorfor virker det egentlig?
  - kjenne til eventuelle styrker og svakheter sammenlignet med andre
  - kjenne til kjøretiden under ulike omstendigheter, og forstå utregningen
- Ved hver datastruktur skal man
  - Forstå algoritmene for de ulike operasjonene på strukturen
  - Forstå hvordan strukturen representeres i minnet
- Ved hvert problem skal man kunne
  - angi presist hva input er
  - angi presist hva output er og hvilke egenskaper det må ha

</details>

## Problemer og algoritmer

- Brute force er ofte helt ubrukelig
- Dekomponer til mindre instanser og bruk de til å finne en løsning

En **algoritme** er en tydelig definert fremgangsmåte som kan ta en verdi eller en mengde verdier som **input** og produserer en verdi eller en mengde verdier som **output**. Algoritmen er ofte en sekvens av beregninger, presist beskrevet. Input verdiene kan deles opp flere **instanser**.

Å **analysere en algoritme** har fått betydningen å "forutse ressurskravene til algoritmen": minne, kommunikasjonsbåndbredde, hardware, beregningstid, og ofte totalkostnaden av disse.

<!-- [A1] Forstå bokas pseudokode-konvensjoner (den starter på index 1) -->

### Random-access machine modellen (RAM)
<!-- [A2] Kjenne egenskapene til random-access machine-modellen (RAM) -->
En abstrakt maskin som har følgende egenskaper:

- Aritmetikk: $+$ $-$ $*$ $/$ $\bmod$, $\lfloor x \rfloor$, $\lceil x \rceil$  (enkle instruksjoner)
- Flytting av data og programkontroll
- Instruksjoner kjøres sekvensielt og ikke samtidig
- Håndterer heltall og flyttall

Alle disse operasjonene tar **konstant** tid.

### Kjøretid
<!-- [A3] Kunne definere problem, instans og problemstørrelse -->
Et mål på hvor effektiv algoritmen er det viktigste når man skal analysere alle algoritmer. Vi trenger å beregne kjøretider fordi vi har en begrensning på hvor raske og hvor mye lagringsplass en datamaskin har tilgjengelig. Kjøretiden er det *asymptotiske forholdet mellom størrelsen på problemet og hvor lang tid det vil ta å løse det*.

- Problem: Relasjon mellom input og output
- Instans: En bestemt input
- Problemstørrelse, $n$: Lagringsplass som trengs for en instans
- Kjøretid: En funksjon av problemstørrelsen; større problemer krever mer tid (men hvor mye?)
- Eksempel: Hvis vi teller operasjoner, og hver operasjon tar ett mikrosekund, hvor mye rekker vi på ett år?

Vi er interessert i hvor fort kjøretiden **vokser**. Vi er interessert i en grov størrelsesorden.

#### Noen vanlige kjøretider

Kompleksitet | Navn | Type
:-----------:|:----:|:-----:
 $\Theta(n!)$ | Factorial | Generell
 $\Omega(k^n)$ | Eksponensiell | Generell
 $O(n^k)$ | Polynomisk | Generell
 $\Theta(n^3)$ | Kubisk | Tilfelle av polynomisk
 $\Theta(n^2)$ | Kvadratisk | Tilfelle av polynomisk
 $\Theta(n\lg n)$ | Loglineær | Kombinasjon av lineær og logaritmisk
 $\Theta(n)$ | Lineær | Generell
 $\Theta(\lg n)$ | Logaritmisk | Generell
 $\Theta(1)$ | Konstant | Generell

### Asymptotisk notasjon
<!-- ![A4] Kunne definere asymptotisk notasjon, O, Ω, Θ, o og ω. -->
- Dropp konstanter og lavere ordens ledd
- $\omega$ $\leftrightarrow$ $>$ (lille omega)
- $\Omega$  $\leftrightarrow$ $\ge$ (store omega, nedre grense)
- $\Theta$  $\leftrightarrow$ $=$ (store theta, øvre og nedre grense)
- $O$  $\leftrightarrow$ $\le$ (store o, øvre grense)
- $o$  $\leftrightarrow$ $<$ (lille o)

#### Asymptotisk optimal

Den asymotiske kjøretiden = den beste mulige kjøretiden for det gitte problemet.

OBS: Vanligvis verste tilfelle, men kan variere.

F.eks. sier vi at Merge sort er asymptotisk optimal, fordi den har verste kjøretid $O(n\lg n)$, og vi vet at verste kjøretid for sortering generelt er $\Omega(n\lg n)$. Dermed går det ikke an å bli bedre i verste tilfelle. Men i beste tilfelle er jo f.eks. Insertion sort bedre, så den har en asymptotisk optimal best-case (som ofte ikke er så interessant; det er jo lett å legge til en optimal best-case, f.eks ved å bare sjekke om input allerede er sortert før vi setter igang sorteringen).

«Optimal» betyr «best» (altså det du kaller «mest optimal»). Om man vil ha mange aktiviteter, så vil de optimale løsningene være de løsningene som har flest aktiviteter. Ingen andre vil være bedre, men det kan være flere optimale løsninger (som altså har nøyaktig like mange aktiviteter/som er nøyaktig like bra).

En optimal løsning er så bra som det er mulig å være – ingen løsninger kan være bedre – men det kan være flere optimale løsninger, som er nøyaktig like bra.

> _[(Piazza H20 @158)](https://piazza.com/class/kdptcutti24r?cid=158)_
> _[(Piazza H20 @240)](https://piazza.com/class/kdptcutti24r?cid=240)_

#### Forenkling av asymptotisk notasjon

Generelt er ideen at et uttrykk $B$ er en forenkling av uttrykk $A$ dersom $A=B$ og $B$ er enklere enn $A$. Forenkling bør medføre minst mulig tap av presisjon. Med _enklere_ menes kortere/færre tegn eller lignende. I asymptotisk notasjon er sum det samme som maksimum, og man må velge uttrykk til høyre som ikke har strengere øvre og/eller nedre grenser enn venstresiden. Summer som inneholder et ledd med kun en nedre grense kan ikke ha noen øvre grense totalt sett. Ledd som blir beskrevet kun med nedre grense f.eks  $\Omega(n)$ kan ha en ukjent øvre grense. Denne ukjente øvre grensen kan være uendelig stor. Vi må ha dette i bakhodet når vi skal forenkle sammensatte uttrykk slik vi gjør i eksempel 1 og 2.

##### Forenkling eksempel 1

$$O(n)+\Omega(n)=\Omega(n)$$

Uansett hvilken funksjon vi har fra $O(n)$ og $\Omega(n)$, om vi legger dem sammen vil den resulterende funksjonen tilhøre klassen $\Omega(n)$. Det vil ikke påvirke resultatet å legge til flere øvre grenser $O(anything)$.

> Uformelt kan man si "Funksjonen er minst $n$". Da kan man like gjerne si "Funksjonen er minst $n$ pluss maks $n^2$". Det endrer ingenting. Det blir som om vi sier «Emnet har minst 1000 studenter og så maks 200 studenter til». Det eneste vi vet da er at det er minst 1000 studenter. Og vi kan like gjerne uttrykke det som «Emnet har minst 1000 studenter og så maks 2.000.000 studenter til». Det er fortsatt korrekt. Vi vet fortsatt bare at emnet har minst 1000 studenter. _[(Piazza H20 @21)](https://piazza.com/class/kdptcutti24r?cid=21_f1)_

##### Forenkling eksempel 2

$$\Theta(n^2)+O(n^4)+\Omega(\log n)$$

Vi kan forenkle ved å skrive $\Omega(n^2)+O(n^4)$ som vil være en mer generell notasjon og derfor OK. $\omega(n^2)+o(n^4)$ vil være feil fordi lille omega er en strengere notasjon, og utelukker leddet som inneholder $\Theta(n^2)$.

### Klasser av input
<!-- ![A5] Kunne definere best-case, average-case og worst-case -->
- Best, verst og forventet
- Kjøretid: Funksjon av problemstørrelse
- Best-case: Beste mulige kjøretid for en gitt størrelse
- Average-case: Forventet, gitt en sannsynlighetsfordeling
  - Har vi ingen sannsynlighetsfordeling antas alle inputs like sannsynlige.
- Worst-case: Verste mulige (brukes mest)

### Dekomponering/rekursiv dekomponering
<!-- ![A6] Forstå løkkeinvarianter og induksjon -->
<!-- ![A7] Forstå rekursiv dekomponering og induksjon over delinstanser -->

- Eks: summere elementene i en tabell
- Rekursjon: summer alle unntatt siste - en funksjon kaller seg selv
- Grunntilfelle: tom sum er null
- Induktivt premiss: summen er rett
- Induksjonstrinn: legg til siste element

#### Induksjon

- Del opp i mindre problemer (trinn for trinn)
- Induktivt premiss: anta at du kan løse de mindre problemene
- Induksjonstrinn: konstruer fullstendig løsning ut fra delløsningene

Eksempel:

1. Velge vilkårlig heltall å vise for det, da kan det vises for alle
2. Midlertidig anta $P$ og vis deretter $Q$ - da kan $P$ implisere $Q$

Tolkning: Hva er relasjonen mellom input og output?  
Analyse: Del en vilkårlig instans i delinstanser  
Syntese: Bygg løsning av hypotetiske delløsninger  

##### Iterativ dekomponering: Induksjon - Iterativ utgave

- (Løkke) Invariant: egenskap som ikke endres. Sann før og etter hver iterasjon
  - Initialize: anta at invariant er sann før start
  - Vedlikehold: holder den før/etter interasjon?
  - Terminering: løkken sier noe nyttig
- Vedlikehold i hver iterasjon

### Insertion sort
<!-- [A8] Forstå Insertion-Sort -->
[Link til insertion sort](Algoritmer/Sortering/insertion_sort.md)

## Datastrukturer

For å unngå grunnleggende kjøretidsfeller er det viktig å kunne organisere og strukturere data fornuftig. En **datastruktur** er en måte å organisere og organisere data for å muliggjøre tilgang og modifikasjon. Det er ingen universal datastruktur som fungerer godt for alle formål.

### Stakker og køer (stacks and queues)
<!-- [B1] Forstå hvordan stakker og køer fungerer (Stack-Empty, Push, Pop, Enqueue, Dequeue) -->
Stakker og køer er dynamiske sett med 2 viktige metoder, `PUSH` og `POP`, som hvv. legger til og fjerner elementer.

En **stack** har en "Last In First Out" (LIFO) struktur. `POP` returnerer elementet som **sist** ble satt inn.

```python
class Stack:
     def __init__(self):
         self.l = []

     def isEmpty(self):
         return self.l == []

     def push(self, item):
         self.l.append(item)

     def pop(self):
         return self.l.pop()
```

En **kø** har en "First In First Out" (FIFO) struktur. `POP` eller `DEQUEUE` returnerer elementet som **først** ble satt inn med $O(1)$.

```python
class Queue:
    def __init__(self):
        self.l = []

    def isEmpty(self):
        return self.l == []

    def enqueue(self, item):
        self.l.insert(0,item)

    def dequeue(self):
        return self.l.pop()
```

![Illustrasjon stakker og køer](https://i.imgur.com/phsBXVL.png)

#### Prioritetskø

En prioritetskø er en type kø som _ikke_ er "First In First Out" (FIFO) strukturert. Alle elementer i køen har en verdi som angir prioritet, og det er alltid elementet med størst _eller_ minst som _først_ tas ut av køen.

- `DEQUEUE` vil ta ut elementet med størst/minst prioritet
- `ENQUEUE` vil sette inn et element med en gitt prioritet

### Lenkede lister
<!-- [B2] Forstå hvordan lenkede lister fungerer (List-Search, List-Insert, List-Delete, List-Delete', List-Search', List-Insert') -->
En lenket liste er en lineær datastruktur som representerer elementer i sekvens. Hvert element i lista er en node med en verdi og en peker som peker videre på det neste elementet. I en dobbel-lenket liste peker hver node/element også på det forrige elementet.

Handling | Kjøretid enkel liste
---------|--------
Innsetting på starten | $O(1)$
Innsetting på slutten | $O(n)$
Oppslag | $O(n)$
Slette element | oppslagstid $+\ O(1) = O(n)$

I en dobbel lenket liste gjøres innsetting på $O(1)$ da man kun trenger å endre `.prev` og `.next` til de nye naboene.

<!-- TODO: Sentinels (NIL objekter) -->
<!-- TODO: List-Search, List-Insert, List-Delete, List-Delete', List-Search', List-Insert'-->

### Pekere og objekter
<!-- [B3] Forstå hvordan pekere og objekter kan implementeres -->

### Hashtabeller
<!-- ![B4] Forstå hvordan direkte adressering og hashtabeller fungerer (Hash-Insert, Hash-Search) -->
<!-- [B5] Forstå konfliktløsing ved kjeding (chaining) (Chained-Hash-Insert, Chained-Hash-Search, Chained-Hash-Delete) -->
<!-- [B6] Kjenne til grunnleggende hashfunksjoner -->
I stedet for å lete gjennom en liste, som kan ta $O(n)$ i verste fall, eller en sortert liste på $O(\log n)$, vil letetiden i en hashtabell være konstant, $O(1)$, fordi lagerstedet til en hashtabell er vanligvis i maskinens hurtigminne hvor man har $O(1)$ tilgang til alle plassene.

Hvis flere nøkler kobles til samme plass i minnet oppstår **kollisjon**. Da vil flere ulike faktiske nøkler gi samme hashverdi.

### Statiske datasett
<!-- [B7] Vite at man for statiske datasett kan ha worst-case O(1) for søk -->

### Amortisert analyse
<!-- [B8] Kunne definere amortisert analyse -->
Amortisert analyse er en metode for å kunne analysere en gitt algoritmes kompleksitet.

- Kjøretid for en enkelt operasjon: ikke alltid informativt
- Se på gjennomsnitt per operasjon etter mange har blitt utført

Amortisert analyse ser på gjennomsnittet av av worst case tilfellene ved forskjellige inputstørrelser, som i mange tilfeller er mye bedre enn det verste tilfellet. Det er derfor worst case ofte er mer pessimistisk enn amortisert analyse.

Når du har en sekvens med en datastrukturs operasjoner, som du kjenner kjøretiden til, så kan man utføre amortisert analyse.

Husk denne:
$$\sum^{h-1}_{i=0}2^i = 2^h-1$$
<!-- TODO: Utdyp -->

### Dynamiske tabeller
<!-- [B9] Forstå hvordan dynamiske tabeller fungerer (Table-Insert) -->

## Splitt og hersk
<!-- ![C1] Forstå designmetoden divide-and-conquer (splitt og hersk) -->

### Maximum subarray problemet
<!-- [C2] Forstå maximum-subarray-problemet med løsninger -->

### Bisect og Bisect'
<!-- [C3] Forstå Bisect og Bisect' (se appendiks C i pensumhefte) -->
[Link til binary search (bisect)](Algoritmer/Sortering/binary_search_(bisect).md)

### Merge sort
<!-- [C4] Forstå Merge-Sort -->
[Link til merge sort](Algoritmer/Sortering/merge_sort.md)

### Quick sort
<!-- [C5] Forstå Quicksort og Randomized-Quicksort -->
[Link til quick sort](Algoritmer/Sortering/quick_sort.md)

Quick sort er [in-place](#In-place).

### Rekurrenser
<!-- ![C6] Kunne løse rekurrenser med substitusjon, rekursjonstrær og masterteoremet -->

En type likning - Rekursive likninger

Eksempel på en rekurrens: $T(n)=4T(^n/_2) + n^2$

De beskriver f.eks. kjøretiden til rekursive algoritmer. Man *trenger* ikke bruke rekurrenser om det ikke er rekursjon!

Metoder for å regne ut rekurrenser:

- Substitusjon:
  - Bytte ut inputargumenter til noe som gjør rekurrensen enklere å løse.
- Rekursjonstre
- [Masterteoremet](#masterteoremet):
  - Rekurrensen må være på formen $T(n)=aT(^n/_b) + f(n)$
- Iterasjonsmetoden (induksjon):
  - Gjentatt ekspandering av den rekursive forekomsten av funksjonen - det gir oss en sum som vi kan regne ut
  - Gjør at vi kan "se" et mønster
- Variabelskifte

#### Substitusjon
<!-- TODO -->

#### Rekursjonstre
<!-- TODO: Utdyp -->

Iterasjonsmetoden med flere grener. Fin måte å visualisere arbeidet, men kan være overveldende i starten.

- Vi itererer gjennom hva algoritmen koster for hvert nivå i treet, og legger det sammen. Da får vi en sum (kostnad løvnivå + $\sum_{h-1}^{i=0}$ pris for nivå $i$).
- Høyden til treet, er hvor lang tid det tar å komme seg til grunntilfellet. Kjøretiden blir kostnaden til hvert nivå.
- Kan ofte bruke masterteoremet istedet, men det bevises via rekurrenstrær.
- Eks: $T(n)=3T(n/4)+cn^2=3T(n/4)+\Theta(n^2)$. (s. 88 i boka)

#### Masterteoremet

Kontekst: Finne kjøretid, ofte for splitt og hersk algoritmer

$$T(n)=aT(^n/_b) + f(n)$$
$$a\ge1,\  b>1$$

1. Identifiser $a, b, f(n)$
2. Regn ut $\log_b(a) = d$ og finn graden av $f(n) = c$
3. Vurder forholdet mellom $c$ og $d$. Hvis $d>c$ gjelder tilfelle 1 med $O$. Hvis $c=d$ gjelder tilfelle 2 med $\Theta$. Hvis $d<c$ gjelder tilfelle 3 med $\Omega$.
4. Konsulter tabellen under med tilfeller

Tilfelle | Krav | Løsning
:----:|:----:|:----:
1 | $f(n)\in O(n^{\log_b a-\epsilon})$ | $T(n) \in \Theta(n^{\log_b a})$
2 | $f(n)\in \Theta(n^{\log_b a} \log^k n)$ | $T(n) \in \Theta(n^{\log_b a}\log n)$
3 | $f(n)\in \Omega(n^{\log_b a+\epsilon})$ | $T(n) \in \Theta(f(n))$

##### Eksempel masterteorem 1

$$T(n)=64\cdot T(n/4)+3n^3+7n$$

1. $a = 64$, $b=4$, $f(n)=3n^3+7n$
2. $\log_4(64) = 3 = d$
3. Finn graden av $f(n)$ som her er $3=c$.
4. I vårt tilfelle er $d=c$ og dermed er det tilfelle 2 med $\Theta$.
5. Hvordan vi da finner løsningen baserer seg på tilfellet. Formatet på kjøretiden vår kommer dermed til å være på formatet til løsningen på tilfelle 2.

$$T(n) \in \Theta(n^{\log_b a}\log^{k+1}(n))$$
$$T(n) \in \Theta(n^{\log_4 64}\log^{0+1}(n))$$
$$T(n) \in \Theta(n^{3}\log^{}(n))$$

##### Eksempel masterteorem 2

```python
def FUNCTION-A(n):
  FUNCTION-C(n)
  if n > 1:
    FUNCTION-A(n/3)
    FUNCTION-B(n-2)

def FUNCTION-B(n):
  FUNCTION-C(n)
  if n > 1:
    FUNCTION-A(n/3)
```

Funksjonen `FUNCTION-C` har kjøretid $\Theta(\sqrt(n))$. Hva blir kjøretiden til funksjonen `FUNCTION-A`, som funksjon av $n$?

Vi gjenkjenner rekurrensen på følgende måte:

1. Prøv å formulere funksjon A som en rekurrens ved å vurdere en operasjon av gangen:
    - `FUNCTION-C(n)`: Legg til `FUNCTION-C(n)`
    - `if n > 1`: If-statements med en sjekk anses som ett steg.
    - `FUNCTION-A(n/3)`: For rekursive kall, i dette tilfellet der funksjon A kaller seg selv, vil vi sette inn $T_a(n/3)$.
    - `FUNCTION-B(n-2)`: Hva med parameteren $n-2$? Dette er en konstant endring og trenger dermed ikke å vurderes her. Sett inn funksjon C og A for B.

    Dette gir oss: $$T_A(n) = T_C(n)+1+T_A(n/3)+T_C(n)+1+T_A(n/3)$$

    Bytt så ut $T_C(n) = \Theta(\sqrt(n))$

    $$T_A(n) = \sqrt(n)+1+T_A(n/3)+\sqrt(n)+1+T_A(n/3)$$

    $$T_A(n) = 2\cdot T_A(n/3)+2\cdot \sqrt(n)+2$$

2. Bruk deretter masterteoremet:
    - $a = 2$, $b=3$, $f(n)=2\cdot \sqrt(n)+2$
    - $\log_3(2) \approx 0.95 = d$
    - Finn graden av $f(n)$ som her er $1/2=c$. **Merk:** $\sqrt{n} = n^{1/2}$
    - Vurder forholdet mellom $c$ og $d$. Her er $d>c$ og dermed er det Masterteorem-tilfelle 1 med $\Omega$.
    - Hvordan vi da finner løsningen baserer seg på tilfellet. Formatet på kjøretiden vår kommer dermed til å være på formatet til løsningen på tilfelle 2.

Dette gir oss følgende

$$T(n) \in \Theta(n^{\log_b a})$$
$$T(n) \in \Theta(n^{\log_3 2})$$

#### Iterasjonsmetoden
<!-- ![C7] Kunne løse rekurrenser med iterasjonsmetoden (se appendiks B i pensumhefte) -->

#### Variabelskifte
<!-- [C8] Forstå hvordan variabelskifte fungerer* -->

Bytt ut vanskelige uttrykk

1. Sett opp ny rekurrens av en annen variabel, f.eks. $T(n)=T(2^k)=S(k)$
2. Løs den, f.eks. med masterteoremet
3. Bytt tilbake til $T(n)$

**Eksempel:** Løs rekurrensen $T(n) = T(\sqrt{n})+\lg n$.
<!-- TODO -->

## Rangering i lineær tid

### Worst case for sammenligningsbasert sortering (sorteringsgrensen)
<!-- ![D1] Forstå hvorfor sammenligningsbasert sortering har en worst-case på Ω(n lg n) -->

> Any comparison sort algorithm requires $\Omega(n\lg n)$ comparisons in the worst case.

Du må ha sett på hvert element for å sammenligne, derav første $n$. Videre må hvert element ... <!-- TODO -->

Det er umulig å sortere raskere uten å anta egenskaper ved problemet.

### Stabile sorteringsalgoritmer
<!-- [D2] Vite hva en stabil sorteringsalgoritme er -->
En sorteringsalgoritme kan sies å være **stabil** om rekkefølgen av like elementer i listen blir bevart etter sortering. For eksempel om vi har lista  
$$[B1, C2, C1, A1]$$
og sorterer den kun etter bokstaver, vil rekkefølgen for $C$ forbli uforandret:
$$[A1, B1, C2, C1]$$

### Counting sort
<!-- [D3] Forstå Counting-Sort, og hvorfor den er stabil -->
[Link til counting sort](Algoritmer/Sortering/counting_sort.md)

### Radix sort
<!-- ![D4] Forstå Radix-Sort, og hvorfor den trenger en stabil subrutine -->
[Link til radix sort](Algoritmer/Sortering/radix_sort.md)

### Bucket sort
<!-- [D5] Forstå Bucket-Sort -->
[Link til bucket sort](Algoritmer/Sortering/bucket_sort.md)

### Randomized-Select og Select
<!-- [D6] Forstå Randomized-Select -->
<!-- [D7] Kjenne til Select - merk: Det kreves ikke grundig forståelse av virkemåten til Select. -->
<!-- TODO -->

## Rotfaste trestrukturer

Et tre er en begrenset form av en graf. Trær har en retning (forelder-/barn-forhold) og inneholder ikke kretser/sykler.

### Terminologi

**Indekseringen** av elementer går fra topp-til-bunn, fra venstre til høyre. Det betyr at topp-elementet alltid har indeks 0, mens det mest høyrestående elementet på det laveste nivået har høyest indeks.

- Det øverste elementet (med index 0) er _rot-noden_.
- De midterste elementene (som har både foreldre og barn) regnes som _interne noder_.
- De mest dyptstående elementene er _løvnoder_ (leafs). De har ingen barn.

Når man snakker om trær er det vanlig å bruke terminologi som beskriver avstanden fra roten:

- Avstanden mellom roten og et vilkårlig element kalles **dybde**.
- Avstanden mellom roten og det dypeste elementet kalles **høyden**.

### Heaps
<!-- ! [E1] Forstå hvordan heaps fungerer, og hvordan de kan brukes som prioritetskøer (Parent, Left, Right, Max-Heapify, Build-Max-Heap, Heapsort, Max-Heap-Insert, Heap-Extract-Max, Heap-Increase-Key, Heap-Maximum. Også tilsvarende for minheaps, f.eks., Build-Min-Heap og Heap-Extract-Min.) -->

En haug (heap) er en sortert tre-struktur. Elementer som legges til en heap blir først sammenlignet med sin forelder-node (parent). Avhengig av om haugen sorterer etter min eller max, blir verdiene byttet om i stien opp til roten helt til rekken er sortert.

![Illustrasjon heaps](https://i.imgur.com/0yYXmiC.png)

En haug er **komplett** dersom alle interne noder har to barn og alle løvnoder er på samme nivå. Om antallet noder er $2^h-1$, for en eller annen høyde $h$, så er treet som haugen representerer komplett.

Bildet under illustrerer sorteringsprosessen etter at et element blir lagt til i haugen.

<img src="https://i.imgur.com/zhgXzNZ.jpg" alt="Illustrasjon av sortering" width="200" style="float:right; margin:1em"/>

1. Den originale haugen
2. Element legges til
3. Elementet bytter plass med forelder-noden

### Heap sort
<!-- [E2] Forstå Heapsort -->
[Link til heap sort](Algoritmer/Grafer/heap_sort.md)

### Implementasjon av rotfaste trær
<!-- [E3] Forstå hvordan rotfaste trær kan implementeres -->
<!-- TODO -->

### Binære trær og søketrær
<!-- ![E4] Forstå hvordan binære søketrær fungerer (Inorder-Tree-Walk, Tree-Search, Iterative-Tree-Search, Tree-Minimum, TreeMaximum, Tree-Successor, Tree-Predecessor, Tree-Insert, Transplant, Tree-Delete) - merk: det kreves ikke grundig forståelse av Transplant og Tree-Delete. -->
<!-- [E5] Vite at forventet høyde for et tilfeldig binært søketre er Θ(lg n) -->
<!-- [E6] Vite at det finnes søketrær med garantert høyde på Θ(lg n) -->
Et tre er et binærtre dersom hver node har 0-2 barn. I et binært søketre har hvert element en spesifikk orden. Barnet til venstre vil alltid være mindre enn rotelementet, og barnet til høyre vil være større.

#### Søking i et binært søketre i forhold til i en array

![Illustrasjon søking](https://i.imgur.com/PnplIZP.gif)  
_Det binære søketreet finner elementet raskere ved at algoritmen kan eliminere elementer som ligger langt unna mål-elementet. Man kan sammenligne denne strategien med binærsøk hvor man halverer antall elementer man vurderer for hver iterasjon._

Denne ordenen gjør traversering/søking svært effektivt.

##### Hvordan en sortert array kan bli omgjort til et søketre

![Illustrajon liste til binært søketre](https://i.imgur.com/bDAYNEz.gif)

##### Binære hauger (binary heaps)

En haug er et binærhaug dersom det er 0-2 barn.

_En binær haug kan aldri være et binært søketre._ Dette er fordi en binær haug sorterer alle elementene sine slik at forelderen alltid er større/mindre enn barne-noden. I et binært søketre er alltid venstre barne-node mindre, mens høyre barne-node alltid er større. Dermed, siden sorteringsstrukturen er så vidt forskjellig, vil det aldri være mulig at du får et tre som kan være begge samtidig.

## Dynamisk programmering
<!-- ![F1] Forstå ideen om en delinstansgraf -->
<!-- ![F2] Forstå designmetoden dynamisk programmering -->

Dynamisk programmering, som splitt og hersk algoritmer, løser problemer ved å kombinere løsninger på delproblemer, ofte rekursivt. Hvis delproblemene overlapper kan man lagre svaret fra et delproblem for å løse problemet i andre. Dynamisk programmering gjelder når delproblemenes delproblem er like. Det er i slike tilfeller splitt og hersk algoritmer gjør mer arbeid enn nødvendig, da de vil løse disse problemene på nytt og på nytt, imens dynamisk programmering sørger for at svar fra like del-delproblemer er lagret i en tabell.

Dynamisk programmering skjer typisk i optimaliseringsproblemer.

Krav til DP:

- Optimal substruktur (løsningen er en kombinasjon av delproblemer)
- Overlappende subproblemer

Hvordan gjøre det i praksis?

- Memoisering (top-down problemløsning)
- Iterasjon (bottom-up problemløsning)

### Memoisering (top-down)
<!-- ![F3] Forstå løsning ved memoisering (top-down) -->

### Iterasjon (bottom-up)
<!-- [F4] Forstå løsning ved iterasjon (bottom-up) -->

### Konstruere løsning fra lagrede beslutninger
<!-- [F5] Forstå hvordan man rekonstruerer en løsning fra lagrede beslutninger -->

### Optimal delstruktur
<!-- [F6] Forstå hva optimal delstruktur er -->

### Overlappende delinstanser
<!-- [F7] Forstå hva overlappende delinstanser er -->

### Stavkutting (rod cutting) og LCS
<!-- [F8] Forstå eksemplene stavkutting og LCS -->

### Ryggsekkproblemet (0-1 knapsack)
<!-- [F9] Forstå løsningen på det binære ryggsekkproblemet (se appendiks D i pensumhefte) (Knapsack, Knapsack') -->

## Grådige algoritmer
<!-- ![G1] Forstå designmetoden grådighet -->
<!-- ![G2] Forstå grådighetsegenskapen (the greedy-choice property) -->

Grådige algoritmer er motpælen til dynamisk programmering. I stedet for å velge forskjellige valg underveis, vil en grådig algoritme velge den løsningen som ser mest lovende ut der og da. For å bruke grådige algoritmer må vi ha:

- Grådighetsegenskapen: vi kan finne en global optimal løsning ved å ta lokalt optimale valg
- Optimal delstruktur: kan fortsette på samme måte. Opt. løsning bygger på opt. delløsninger. Hvis ikke må vi løse ting på en helt annen måte etter første valg.

Disse egenskapene sammen gir en optimal løsning.

### Aktivitetsutvalgproblemet
<!-- [G3] Forstå eksemplene aktivitet-utvelgelse og det kontinuerlige ryggsekkproblemet -->

#### Huffmans algoritme
<!-- [G4] Forstå Huffman og Huffman-koder -->
Huffmans algoritme er en grådig algoritme som komprimerer data veldig effektivt, vanligvis mellom 20%-90%. Algoritmen bruker en tabell som teller antall hendelser av hvert tegn i en sekvens med tegn, og bygger et binærtre basert på frekvensene.

## Traversering av grafer
<!-- [H1] Forstå hvordan grafer kan implementeres -->
<!-- [H2] Forstå BFS, også for å finne korteste vei uten vekter -->
<!-- [H3] Forstå DFS og parentesteoremet -->
<!-- [H4] Forstå hvordan DFS klassifiserer kanter -->
<!-- [H5] Forstå Topological-Sort -->
<!-- [H6] Forstå hvordan DFS kan implementeres med en stakk -->
<!-- [H7] Forstå hva traverseringstrær (som bredde-først- og dybde-først-trær) er -->
<!-- ![H8] Forstå traversering med vilkårlig prioritetskø -->

Vi traverserer en graf ved å besøke noder vi vet om. Vi vet i utgangspunktet bare om startnoden, men oppdager naboene til dem vi besøker. Traversering er viktig i seg selv, men danner også ryggraden til flere mer avanserte algoritmer.

Traversering har matching som motivasjon:

- Vi husker hvor vi kom fra.
- Vi besøker ikke samme node mer enn en gang
  - Vi lager et traverseringstre. Finner stier fra startnoeden til alle noder vi når fram til.
- Vi besøker noder, oppdager noder langst kanter og vedlikeholder en huskeliste.

### Grafrepresentasjoner:

- Nabomatriser
- Nabolister

**Nabomatriser:**

Viser forholdet mellom noder ved hjelp av en matrise og verdier for eksistens av forhold.

![Illustrasjon nabomatrise](https://i.postimg.cc/vHsGRZ33/image.png)

*Spørsmål:* Er 5 nabo med 4?

**Svar:** Sjekk rad 5 kolonne 4. Hvis det står "1", ja, da er de naboer med et forhold fra 5 til 4 $(5 \rightarrow 4)$. I figuren er det vist et symmetrisk forhold. Det innebærer at 5 er nabo med 4 og 4 er nabo med 5. Grafen er urettet.

Godt egnet til raske oppslag, ikke så mye til traversering: For oppslag trenger du kun å sjekke rad for så å sjekke respektiv kolonne for å finne ut om et forhold eksisterer. For traversering må man gå over flere ruter som ikke har noe innhold for å sjekke en hel rad. I tillegg kan nabomatriser fort ta mye plass.

De fleste algoritmer bruker $\Omega(V^{2})$ operasjoner med nabomatriser. Der $V$ er antallet noder (vertices). Det finnes unntak! (Se kjendisproblemet fra forelesning 8)

**Nabolister:**

Liste (eller tabell) med ut-naboer for hver node

![Illustrasjon nabolister](https://i.postimg.cc/XvpttRFV/image.png)

*Spørsmål:* Hvem er naboen til 5?

**Svar:** Sjekk indeks 5, se igjennom listen. Naboene til 5 er 3 og 4.

Godt egnet til traversering, men dårligere til oppslag: For traversering er nabolister en kompakt metode der vi ikke trenger å gå innom noder som ikke har noe forhold. For oppslag må vi derimot gå igjennom lenger lister dersom det er mange pekere på forskjellige noder. Dersom grafen har få kanter vil nabolister også ta mindre plass enn nabomatriser.

## Minimale spenntrær

Her har vi en graf med vekter på kantene, og ønsker å bare beholde akkurat de kantene vi må for å koble sammen alle nodene, med en så lav vektsum som mulig. Erke-eksempel på grådighet: Velg én og én kant, alltid den billigste lovlige.

### Disjunkte mengder
<!-- [I1] Forstå skog-implementasjonen av disjunkte mengder (Connected-Components, Same-Component, Make-Set, Union, Link, Find-Set) -->

### Spenntrær og minimale spenntrær
<!-- [I2] Vite hva spenntrær og minimale spenntrær er -->

### Generisk-MST (Generic-MST):
<!-- ![I3] Forstå Generic-MST -->
Vi har en graf:

![Hovedgraf](https://i.imgur.com/58kEmgN.png)

**Delgrafer**: Delmengder av nodene. Vi kan ikke ha kanter som ikke er koblet til noder.

![Delgrafer](https://i.imgur.com/bACEqyO.png)

**Spenngrafer**: Delgrafer som spenner over hele den opprinnelige grafen. Den inneholder alle de opprinnelige nodemengdene og en delmengde av den opprinnelige kantmengden.

![Spenngrafer](https://i.imgur.com/m1D6tI7.png)

**Spennskoger**: Asykliske spenngrafer.

![Spennskoger](https://i.imgur.com/qxKyJSg.png)

**Spenntrær**: Sammenhengende spennskoger.

![Spenntrær](https://i.imgur.com/hyxxFdn.png)

Vi innfører **vekter** på kantene. Disse kan tolkes som **lengder** eller **kostnader**.

- Vi vil knytte sammen nodene billigst mulig.
- Det kan være flere minimale spenntrær. F.eks. om vi har flere kanter som har samme vekt.

Problemet:

![Minimal spenntrær problem](https://i.imgur.com/2NSL4Rt.png)

Hvordan løse dette?

- Grådig: Vi utvider en asyklisk kantmengde (partiell løsning) gradvis.
- Invariant: Kantmengden utgjør en del av et minimalt spenntre.

Hvordan skal vi utvide kantmengden som er en del av et minimalt spenntre, og beholde invarianten?

- Ved å finne en såkalt "trygg kant" som er en kant som bevarer invarianten.

Algoritme for generisk-MST:

![Generisk MST](https://i.imgur.com/0PitzPz.png)

Hva er trygt å legge til? Hvilken form for grådighet?

Snitt/Cut: Et snitt over en graf. Vi klipper grafen i to. (Figuren under)

- **Det respekterer kantmengden**: Det er ikke klippet noen kanter mellom noder som er svarte og noen som er hvite. Det er ingen kanter som går mellom hvite og svarte noder.
- **Lett kant**: Kanten (4,3) er en (unik) lett kant over snittet (verdi 7): Det er den kanten med lavest vekt av de som er over snittet. (Kantene over snittet på grafen under har verdiene 8, 11, 7, 14 og 10)

![Snitt](https://i.imgur.com/siVErEc.png)

Et vekslingsargument: For å vise at det er trygt å velge en lett kant over et snitt som respekterer løsningen vår. Hvis ikke risikerer vi å få en sykel. Vi må kunne dele kantmengdene våre i to separate mengder.

Fremgangsmåte:

1. Ta en optimal (eller vilkålig) løsning som ikke har valgt grådig. (Som ikke har valgt den lette kanten over det snittet).
2. Vist at vi kan endre til det grådge valget uten å få en dårligere løsning.

### Lette kanter er trygge kanter
<!-- [I4] Forstå hvorfor lette kanter er trygge kanter -->

### MST-Kruksal
<!-- [I5] Forstå MST-Kruskal -->
[Link til MST-Kruksal](Algoritmer/Grafer/MST-Kruksal.md)

### MST-Prim
<!-- [I6] Forstå MST-Prim -->
[Link til MST-Prim](Algoritmer/Grafer/MST-Prim.md)

## Korteste vei fra én til alle

Bredde-først-søk kan finne stier med færrest mulig kanter, men hva om kantene har ulik lengde? Det generelle problemet er uløst, men vi kan løse problemet med gradvis bedre kjøretid for grafer (1) uten negative sykler; (2) uten negative kanter; og (3) uten sykler. Og vi bruker samme prinsipp for alle tre!

<!-- [J1] Forstå ulike varianter av korteste-vei- eller korteste-sti-problemet (Single-source, single-destination, single-pair, all-pairs) -->
<!-- [J2] Forstå strukturen til korteste-vei-problemet -->
<!-- [J3] Forstå at negative sykler gir mening for korteste enkle vei (simple path) -->
<!-- [J4] Forstå at korteste enkle vei kan løses vha. lengste enkle vei og omvendt -->
<!-- [J5] Forstå hvordan man kan representere et korteste-vei-tre -->
<!-- ![J6] Forstå kant-slakking (edge relaxation) og Relax -->
<!-- [J7] Forstå ulike egenskaper ved korteste veier og slakking (Triangle inequality, upper-bound property, no-path property, convergence property, pathrelaxation property, predecessor-subgraph property) -->
<!-- [J8] Forstå Bellman-Ford -->
<!-- [J9] Forstå DAG-Shortest-Path -->
<!-- ![J10] Forstå kobling mellom DAG-Shortest-Path og dynamisk programmering -->
<!-- [J11] Forstå Dijkstra -->

## Korteste vei fra alle til alle

Vi kan finne de korteste veiene fra hver node etter tur, men mange av delinstansene vil overlappe – om vi har mange nok kanter lønner det seg å bruke dynamisk programmering med dekomponeringen «Skal vi innom k eller ikke?»

<!-- [K1] Forstå forgjengerstrukturen for alle-til-alle-varianten av korteste vei-problemet (Print-All-Pairs-Shortest-Path) -->
<!-- [K2] Forstå Floyd-Warshall -->
<!-- [K3] Forstå Transitive-Closure -->
<!-- [K4] Forstå Johnson -->

## Maksimal flyt

Et stort skritt i retning av generell lineær optimering (såkalt lineær programmering). Her ser vi på to tilsynelatende forskjellige problemer, som viser seg å være duale av hverandre, noe som hjelper oss med å finne en løsning.

<!-- [L1] Kunne definere flytnett, flyt og maks-flyt-problemet -->
<!-- [L2] Kunne håndtere antiparallelle kanter og flere kilder og sluk -->
<!-- ![L3] Kunne definere restnettet til et flytnett med en gitt flyt -->
<!-- [L4] Forstå hvordan man kan oppheve (cancel) flyt -->
<!-- [L5] Forstå hva en forøkende sti (augmenting path) er -->
<!-- [L6] Forstå hva snitt, snitt-kapasitet og minimalt snitt er -->
<!-- ![L7] Forstå maks-flyt/min-snitt-teoremet -->
<!-- [L8] Forstå Ford-Fulkerson-Method og Ford-Fulkerson -->
<!-- [L9] Vite at Ford-Fulkerson med BFS kalles Edmonds-Karp-algoritmen -->
<!-- [L10] Forstå hvordan maks-flyt kan finne en maksimum bipartitt matching -->
<!-- ![L11] Forstå heltallsteoremet (integrality theorem) -->

## NP-kompletthet

NP er den enorme klassen av ja-nei-problemer der ethvert ja-svar har et bevis som kan sjekkes i polynomisk tid. Alle problemer i NP kan i polynomisk tid reduseres til de såkalt komplette problemene i NP. Dermed kan ikke disse løses i polynomisk tid, med mindre alt i NP kan det. Ingen har klart det så langt...

Merk: Det kreves ikke grundig forståelse av de ulike NP-kompletthetsbevisene

<!-- [M1] Forstå sammenhengen mellom optimerings- og beslutnings-problemer -->
<!-- [M2] Forstå koding (encoding) av en instans -->
<!-- [M3] Forstå hvorfor løsningen vår på det binære ryggsekkproblemet ikke er polynomisk -->
<!-- [M4] Forstå forskjellen på konkrete og abstrakte problemer -->
<!-- [M5] Forstå representasjonen av beslutningsproblemer som formelle språk -->
<!-- [M6] Forstå definisjonen av klassene P, NP og co-NP -->
<!-- [M7] Forstå redusibilitets-relasjonen 6P -->
<!-- ![M8] Forstå definisjonen av NP-hardhet og NP-kompletthet -->
<!-- [M9] Forstå den konvensjonelle hypotesen om forholdet mellom P, NP og NPC -->
<!-- ![M10] Forstå hvordan NP-kompletthet kan bevises ved én reduksjon -->
<!-- ![M11] Kjenne de NP-komplette problemene CIRCUIT-SAT, SAT, 3-CNF-SAT, CLIQUE, VERTEX-COVER, HAM-CYCLE, TSP og SUBSET-SUM -->
<!-- [M12] Forstå at det binære ryggsekkproblemet er NP-hardt -->
<!-- [M13] Forstå at lengste enkle-vei-problemet er NP-hardt -->
<!-- [M14] Være i stand til å konstruere enkle NP-kompletthetsbevis -->

## Definisjoner

### In-place

En **in-place algoritme** vil ikke allokere mer minne under kjøring for å manipulere input. Det gjelder derimot ikke for det ekstra minnet som blir allokert for variabler.
