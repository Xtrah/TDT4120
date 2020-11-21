import sys

def cut_rod(prices,length): # Running time O(2^n), super inefficient
    if length <= 0:
        return 0
    q = -sys.maxsize
    for i in range(1, length+1):
        q = max(q, prices[i] + cut_rod(prices, length-i))
    return q


def cut_rod_improved_aux(prices, length, memory):
    if memory[length] >= 0: # If it has been memorized before
        return memory[length] # Return the optimal solution for this subproblem
    maximum = -1
    if length == 0:
        maximum = 0 # There is nothing to cut
    for i in range(1, length+1):
        maximum = max(maximum, prices[i] + cut_rod_improved_aux(prices, length-i, memory))
    memory[length] = maximum

    return maximum



def cut_rod_improved(prices, length):
    r = [-1]*(length+1)
    result = cut_rod_improved_aux(prices, length, r)
    print(r)
    return result


def bottom_up_cut_rod(prices, length):
    memory = [-1]*(length+1)
    memory[0] = 0
    for i in range(length+1):
        maximum = -1
        for j in range(i+1):
            maximum = max(maximum, prices[j] + memory[i-j])
        memory[i] = maximum
    print(memory)
    return memory[length]

prices = [1,5,8,9,10,17,17,20,24,30]
length = len(prices)

print(bottom_up_cut_rod([0] + prices,length)) # Remember to add a [0] to the list before passing it in