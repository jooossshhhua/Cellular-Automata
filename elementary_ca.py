import time
# A minimal 1D elementary CA (e.g. Rule 30)
def evolve(rule, cells):
    n = len(cells)
    new = [0]*n
    for i in range(n):
        neighborhood = (cells[(i-1)%n]<<2) | (cells[i]<<1) | cells[(i+1)%n] #get neighborhood value 0-7
        new[i] = (rule >> neighborhood) & 1 #shift rule # by value of neighbors then extract LSB
    return new

# Example usage
rule = int(input("Enter an integer rule number (0-255): "))
state = [0]*20 + [1] + [0]*20 #start state
delay = 1
iter = int(input("Enter number of iterations:(1-20) "))
for _ in range(iter):
    print(''.join('█' if c else ' ' for c in state))  #if cell is 1, print block, else print space
    state = evolve(rule, state)
    time.sleep(delay)
