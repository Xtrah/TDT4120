# TDT4120 Algoritmer og datastrukturer

## Overordnede læringsmål i faget

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

<!--
Markdown symboler: 
<https://gist.github.com/LKS90/252ac41bd4a173be35b0> 
-->

- Dropp konstanter og lavere ordens ledd
- $\omega$ $\leftrightarrow$ $>$ (lille omega)
- $\Omega$  $\leftrightarrow$ $\ge$ (store omega, nedre grense)
- $\Theta$  $\leftrightarrow$ $=$ (store theta, øvre og nedre grense)
- $O$  $\leftrightarrow$ $\le$ (store o, øvre grense)
- $o$  $\leftrightarrow$ $>$ (lille o)

##### Forenkling av asymptotisk notasjon

Generelt er ideen at et uttrykk $B$ er en forenkling av uttrykk $A$ dersom $A=B$ og $B$ er enklere enn $A$. Forenkling bør medføre minst mulig tap av presisjon. Med _enklere_ menes kortere/færre tegn e.l. I asymptotisk notasjon er sum det samme som maksimum, og man må velge uttrykk til høyre som ikke har strengere øvre og/eller nedre grenser enn venstresiden. Og summer som inneholder et ledd med kun en nedre grense kan ikke ha noen øvre grense totalt sett.

###### Eksempel 1

$$O(n)+\Omega(n)=\Omega(n)$$

Uansett hvilken funksjon vi har fra $O(n)$ og $\Omega(n)$, om vi legger dem sammen vil den resulterende funksjonen tilhøre klassen $\Omega(n)$. Det vil ikke påvirke resultatet å legge til flere øvre grenser $O(anything)$.

Uformelt kan man si "Funksjonen er minst $n$". Da kan man like gjerne si "Funksjonen er minst $n$ pluss maks $n^2$". Det endrer ingenting.

Det blir som om jeg sier «Emnet har minst 1000 studenter og så maks 200 studenter til». Det eneste jeg vet da er at det er minst 1000 studenter. Og jeg kan like gjerne uttrykke det som «Emnet har minst 1000 studenter og så maks 2.000.000 studenter til». Det er fortsatt korrekt, og jeg vet fortsatt egentlig bare at emnet har minst 1000 studenter. _[(Piazza H20)](https://piazza.com/class/kdptcutti24r?cid=21_f1)_

###### Eksempel 2

$$\Theta(n^2)+O(n^4)+\Omega(\log n)$$

*TBA*! <!-- Sjekk øving 1 oppgave 9. Hvorfor er ikke lille omega rett? -->
ω(n2)+o(n4)ω(n2)+o(n4)

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
2. Regn ut $\log_b(a)$
3. Konsulter tabellen under for å finne ut hvilket tilfelle som gjelder

Tilfelle | Krav | Løsning
:----:|:----:|:----:
1 | $f(n)\in O(n^{\log_b a-\epsilon})$ | $T(n) \in \Theta(n^{\log_b a})$
2 | $f(n)\in \Theta(n^{\log_b a} \log^k n)$ | $T(n) \in \Theta(n^{\log_b a}\log^{k+1} n)$
3 | $f(n)\in \Omega(n^{\log_b a+\epsilon})$ | $T(n) \in \Theta(f(n))$

##### Eksempel

$$T(n)=64\cdot T(n/4)+3n^3+7n$$

1. $a = 64$, $b=4$, $f(n)=3n^3+7n$
2. $\log_4(64) = 3 = d$
3. Finn graden av $f(n)$ som her er $3=c$.
4. Vurder forholdet mellom $c$ og $d$. I vårt tilfelle er $d=c$ og dermed er det tilfelle 2 med $\Theta$. Hvis $d>c$, hadde det vært tilfelle 1 med $O$. Hvis $d<c$ hadde det vært tilfelle 3 med $\Omega$.
5. Hvordan vi da finner løsningen baserer seg på tilfellet. Formatet på kjøretiden vår kommer dermed til å være på formatet til løsningen på tilfelle 2.

$$T(n) \in \Theta(n^{\log_b a}\log^{k+1}(n))$$
$$T(n) \in \Theta(n^{\log_4 64}\log^{0+1}(n))$$
$$T(n) \in \Theta(n^{3}\log^{}(n))$$

### Klasser av input

- **Best, verst og forventet**
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

## Datastrukturer

For å unngå grunnleggende kjøretidsfeller er det viktig å kunne organisere og strukturere data fornuftig. En **datastruktur** er en måte å organisere og organisere data for å muliggjøre tilgang og modifikasjon. Det er ingen universal datastruktur som fungerer godt for alle formål.

### Stakker og køer (stacks and queues)

Stakker og køer er dynamiske sett med 2 viktige metoder, `PUSH` og `POP`, som hvv. legger til og fjerner elementer.

- En **stack** har en "Last In First Out" (LIFO) struktur. `POP` returnerer elementet som **sist** ble satt inn.
- En **kø** har en "First In First Out" (FIFO) struktur. `POP` returnerer elementet som **først** ble satt inn.

![Illustrasjon stakker og køer](https://i.imgur.com/phsBXVL.png)

### Lenkede lister

En lenket liste er en lineær datastruktur som representerer elementer i sekvens. Hvert element peker videre på det neste elementet. I en dobbel-lenket liste peker hvert element også på det forrige elementet.

Handling | Kjøretid
---------|--------
Innsetting på starten | $O(1)$
Innsetting på slutten | $O(n)$
Oppslag | $O(n)$
Slette element | oppslagstid $+\ O(1)$

### Hashtabeller

I stedet for å lete gjennom en liste, som kan ta $O(n)$ i verste fall, eller en sortert liste på $O(\log n)$, vil letetiden i en hashtabell være konstant, $O(1)$, fordi lagerstedet til en hashtabell er vanligvis i maskinens hurtigminne hvor man har $O(1)$ tilgang til alle plassene.

Hvis flere nøkler kobles til samme plass i minnet oppstår **kollisjon**. Da vil flere ulike faktiske nøkler gi samme hashverdi.

### Dynamiske tabeller
