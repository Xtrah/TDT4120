import random

# Når k=O(n), er kjøretiden θ(n). Slår den nedre grensen til sammenligningsbaserte sorteringsalgoritmer, fordi
# det ikke er en sammenligningsbasert sorteringsalgoritme. Baserer seg heller på verdiene til tallene den sammenligner.
# Er en stabil sorteringsalgoritme. TODO: Forklar hvorfor
# Listen kan ikke inneholde negative tall eller desimaltall
def counting_sort(A, B, k): # A = Usortert liste. B = Liste hvor resultatet skal puttes. k = Det største tallet i listen
    # Eksempel input A=[3,2,1]
    C = [0]*(k+1)
    for i in range(len(A)):
        C[A[i]] += 1 # C sier nå hvor mange ganger hvert tall opptrer i listen, C=[1,1,1]
    for i in range(1, k+1):
        C[i] += C[i-1] # C sier nå hvilken indeks hvert tall skal plasseres på i resultatlisten, C=[1,2,3] (merk at vi må ta -1 ved innsetting senere)
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i] # B[1-1] = 1, B[2-1] = 2, B[3-1] = 3
        C[A[i]] -= 1 # Neste gang dette tallet dukker opp, må det plasseres 1 plass lenger til venstre
    return B



for i in range(1000):
    testList = []
    for j in range(20):
        testList.append(random.randint(0,10))
    B = [0] * len(testList)
    k = 10
    counting_sort(testList, B, k)
    print(B)
