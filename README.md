# TDT4120 Algoritmer og datastrukturer

<!-- TODO: Innholdsfortegnelse -->

- [Hva er algoritmer?](#hva-er-algoritmer)
- [Datastrukturer](#datastrukturer)
- [Algoritmer](Algoritmer/)

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

## Hva er algoritmer?

- Bruke force er ofte helt ubrukelig
- Dekomponer til mindre instanser og bruk de til å finne en løsning

En **algoritme** er en tydelig definert fremgangsmåte som kan ta en verdi eller en mengde verdier som **input** og produserer en verdi eller en mengde verdier som **output**. Algoritmen er ofte en sekvens av beregninger, presist beskrevet. Input verdiene kan deles opp flere **instanser**.

### Kjøretid

Et mål på hvor effektiv algoritmen er det viktigste når man skal analysere alle algoritmer. Vi trenger å beregne kjøretider fordi vi har en begrensning på hvor raske og hvor mye lagringsplass en datamaskin har tilgjengelig. Kjøretiden er det *asymptotiske forholdet mellom størrelsen på problemet og hvor lang tid det vil ta å løse det*.

- Problem: Relasjon mellom input og output
- Instans: En bestemt input
- Problemstørrelse, $n$: Lagringsplass som trengs for en instans
- Kjøretid: En funksjon av problemstørrelsen; større problemer krever mer tid (men hvor mye?)
- Eksempel: Hvis vi teller operasjoner, og hver operasjon tar ett mikrosekund, hvor mye rekker vi på ett år?

Vi er interessert i hvor fort kjøretiden **vokser**. Vi er interessert i en **grov størrelsesorden**.

#### Asymptotisk notasjon

- Dropp konstanter og lavere ordens ledd
- $\omega$ $\leftrightarrow$ $>$ (lille omega)
- $\Omega$  $\leftrightarrow$ $\ge$ (store omega, nedre grense)
- $\Theta$  $\leftrightarrow$ $=$ (store theta, øvre og nedre grense)
- $O$  $\leftrightarrow$ $\le$ (store o, øvre grense)
- $o$  $\leftrightarrow$ $>$ (lille o)

##### Forenkling av asymptotisk notasjon

Generelt er ideen at et uttrykk $B$ er en forenkling av uttrykk $A$ dersom $A=B$ og $B$ er enklere enn $A$. Forenkling bør medføre minst mulig tap av presisjon. Med _enklere_ menes kortere/færre tegn eller lignende. I asymptotisk notasjon er sum det samme som maksimum, og man må velge uttrykk til høyre som ikke har strengere øvre og/eller nedre grenser enn venstresiden. Summer som inneholder et ledd med kun en nedre grense kan ikke ha noen øvre grense totalt sett. Ledd som blir beskrevet kun med nedre grense f.eks  $\Omega(n)$ kan ha en ukjent øvre grense. Denne ukjente øvre grensen kan være uendelig stor. Vi må derfor ha dette i bakhodet når vi skal forenkle sammensatte uttrykk slik vi gjør i eksempel 1 og 2.

###### Eksempel 1

$$O(n)+\Omega(n)=\Omega(n)$$

Uansett hvilken funksjon vi har fra $O(n)$ og $\Omega(n)$, om vi legger dem sammen vil den resulterende funksjonen tilhøre klassen $\Omega(n)$. Det vil ikke påvirke resultatet å legge til flere øvre grenser $O(anything)$.

Uformelt kan man si "Funksjonen er minst $n$". Da kan man like gjerne si "Funksjonen er minst $n$ pluss maks $n^2$". Det endrer ingenting. Det blir som om vi sier «Emnet har minst 1000 studenter og så maks 200 studenter til». Det eneste vi vet da er at det er minst 1000 studenter. Og vi kan like gjerne uttrykke det som «Emnet har minst 1000 studenter og så maks 2.000.000 studenter til». Det er fortsatt korrekt. Vi vet fortsatt bare at emnet har minst 1000 studenter. _[(Piazza H20)](https://piazza.com/class/kdptcutti24r?cid=21_f1)_

###### Eksempel 2

$$\Theta(n^2)+O(n^4)+\Omega(\log n)$$

Vi kan forenkle eksempel 2 ved å skrive $\Omega(n^2)+O(n^4)$ som vil være en mer generell notasjon og derfor ok. Samtidig vil $\omega(n^2)+o(n^4)$ være feil fordi lille omega er en strengere notasjon, og utelukker leddet som inneholder $\Theta (n^2)$.

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
    - `if n > 1`: If-statements med en sjekk ansees som 1 steg.
    - `FUNCTION-A(n/3)`: For rekursive kall, i dette tilfellet der funksjon A kaller seg selv, vil vi sette inn $T_a(n/3)$.
    - `FUNCTION-B(n-2)`: Hva med parameteren $n-2$? Dette er en konstant endring og trenger dermed ikke å vurderes her. Sett inn funksjon C og A for B.

    Dette gir oss: $$T_A(n) = T_C(n)+1+T_A(n/3)+T_C(n)+1+T_A(n/3)$$

    Bytt så ut $T_C(n) = \Theta(\sqrt(n))$

    $$T_A(n) = \sqrt(n)+1+T_A(n/3)+\sqrt(n)+1+T_A(n/3)$$

    $$T_A(n) = 2\cdot T_A(n/3)+2\cdot \sqrt(n)+2$$

2. Bruk deretter masterteoremet:
    - $a = 2$, $b=3$, $f(n)=2\cdot sqrt(n)+2$
    - $\log_3(2) \approx 0.95 = d$
    - Finn graden av $f(n)$ som her er $1/2=c$. *Merk:* $\sqrt(n) = n^{1/2}$.
    - Vurder forholdet mellom $c$ og $d$. I vårt tilfelle er $d>c$ og dermed er det tilfelle 1 med $\Omega$.
    - Hvordan vi da finner løsningen baserer seg på tilfellet. Formatet på kjøretiden vår kommer dermed til å være på formatet til løsningen på tilfelle 2.

Dette gir oss følgende

$$T(n) \in \Theta(n^{\log_b a})$$
$$T(n) \in \Theta(n^{\log_3 2})$$

### Klasser av input

- Best, verst og forventet_
- Kjøretid: Funksjon av problemstørrelse
- Best-case: Beste mulige kjøretid for en gitt størrelse
- Average-case: Forventet, gitt en sannsynlighetsfordeling
- **Worst-case: Verste mulige (brukes mest)**

### Dekomponering/rekursiv dekomponering

- Eks: summere elementene i en tabell
- Rekursjon: summer alle unntatt siste
- Grunntilfelle: tom sum er null
- Induktivt premiss: summen er rett
- Induksjonstrinn: legg til siste element

#### Induksjon

- Del opp i mindre problemer (trinn for trinn)
- Induktivt premiss: anta at du kan løse de mindre problemene
- Induksjonstrinn: konstruer fullstendig løsning ut fra del-løsningene

1. Velge vilkårlig heltall å vise for det, da kan det vises for alle (eksempel)
2. Midlertidig anta P og vis deretter Q - da kan P implisere Q

Tolkning: Hva er relasjonen mellom input og output?  
Analyse: Del en vilkårlig instans i delinstanser  
Syntese: Bygg løsning av hypotetiske delløsninger  

#### Induksjon: iterativ utgave

- Invariant: egenskap som ikke endres
- Initialisering: inv. er sann ved start
- Vedlikehold i hver iterasjon

### In-place begrepet

En in-place algoritme vil ikke allokere mer minne under kjøring for å manipulere input. Det gjelder derimot ikke for det ekstra minnet som blir allokert for variabler.

### Stabile sorteringsalgoritmer

En sorteringsalgoritme kan sies å være stabil om rekkefølgen av like elementer i listen blir bevart etter sortering. For eksempel om vi har lista  
$$[B1, C1, C2, A1]$$
og sorterer den, får vi  
$$[A1, B1, C1, C2]$$.

## Datastrukturer

For å unngå grunnleggende kjøretidsfeller er det viktig å kunne organisere og strukturere data fornuftig. En **datastruktur** er en måte å organisere og organisere data for å muliggjøre tilgang og modifikasjon. Det er ingen universal datastruktur som fungerer godt for alle formål.

### Stakker og køer (stacks and queues)

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

En **kø** har en "First In First Out" (FIFO) struktur. `POP` returnerer elementet som **først** ble satt inn med $O(1)$.

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

### Lenkede lister

En lenket liste er en lineær datastruktur som representerer elementer i sekvens. Hvert element i lista er en node med en verdi og en peker som peker videre på det neste elementet. I en dobbel-lenket liste peker hver node/element også på det forrige elementet.

Handling | Kjøretid enkel liste
---------|--------
Innsetting på starten | $O(1)$
Innsetting på slutten | $O(n)$
Oppslag | $O(n)$
Slette element | oppslagstid $+\ O(1) = O(n)$

I en dobbel lenket liste gjøres innsetting på $O(1)$ da man kun trenger å endre `.prev` og `.next` til de nye naboene.

### Hashtabeller

I stedet for å lete gjennom en liste, som kan ta $O(n)$ i verste fall, eller en sortert liste på $O(\log n)$, vil letetiden i en hashtabell være konstant, $O(1)$, fordi lagerstedet til en hashtabell er vanligvis i maskinens hurtigminne hvor man har $O(1)$ tilgang til alle plassene.

Hvis flere nøkler kobles til samme plass i minnet oppstår **kollisjon**. Da vil flere ulike faktiske nøkler gi samme hashverdi.

### Dynamiske tabeller

### Grafer og trær

En graf er en matematisk modell over parvise relasjoner mellom objekter, altså flere små relasjoner.

Et tre er en begrenset form av en graf. Trær har en retning (forelder-/barn-forhold) og inneholder ikke kretser.

#### Indeksering

Indekseringen av elementer går fra topp-til-bunn, fra venstre til høyre. Det betyr at topp-elementet alltid har indeks 0, mens det mest høyrestående elementet på det laveste nivået har høyest indeks.

Det øverste elementet (med index 0) er rot-noden.

De midterste elementene (som har både foreldere og barn) regnes som **interne noder**.

De mest dyptstående elementene er **løv-noder**. De har ingen barn.

#### Dybde og høyde

Når man snakker om trær er det vanlig å bruke terminologi som beskriver avstanden fra roten:

- Avstanden mellom roten og et vilkårlig element kalles **dybde**.
- Avstanden mellom roten og det dypeste elementet kalles **høyden** til treet.

#### Hauger (heaps)

![Illustrasjon heaps](https://i.imgur.com/0yYXmiC.png)

En haug (heap) er en sortert tre-struktur. Elementer som legges til en heap blir først sammenlignet med sin forelder-node (parent). Avhengig av om haugen sorterer etter min eller max, blir verdiene byttet om i stien opp til roten helt til rekken er sortert. Bildet under illustrerer sorteringsprosessen etter at et element blir lagt til i haugen.

![Illustrasjon av sortering](https://i.imgur.com/zhgXzNZ.jpg)

1. Den originale haugen
2. Element legges til
3. Elementet bytter plass med forelder-noden

#### Binære trær og søketrær

Et tre er binærtre dersom hver node har 0-2 barn. I et binært søketre har hvert element en spesifikk orden. Barnet til venstre vil alltid være mindre enn rotelementet, og barnet til høyre vil være større.

Denne ordenen gjør traversering/søking svært effektivt.

##### Søking i et binært søketre i forhold til i en array

![Illustrasjon søking](https://i.imgur.com/PnplIZP.gif)  
_Det binære søketreet finner elementet fortere ved at algoritmen kan eliminere elementer som ligger langt unna mål-elementet. Man kan sammenligne denne strategien med binærsøk hvor man halverer antall elementer man vurderer for hver iterasjon._

##### Hvordan en sortert array kan bli omgjort til et søketre

![Illustrajon liste til binært søketre](https://i.imgur.com/bDAYNEz.gif)

#### Binære hauger (binary heaps)

_En binær haug kan aldri være et binært søketre._ Dette er fordi en binær haug sorterer alle elementene sine slik at forelderen alltid er større/mindre enn barne-noden. I et binært søketre er alltid venstre barne-node mindre, mens høyre barne-node alltid er større. Dermed, siden sorteringsstrukturen er så vidt forskjellig, vil det aldri være mulig at du får et tre som kan være begge samtidig.
