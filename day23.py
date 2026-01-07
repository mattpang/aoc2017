# The code it's running seems to be a variant of the kind you saw recently on that tablet. The general functionality seems very similar, but some of the instructions are different:

# set X Y sets register X to the value of Y.
# sub X Y decreases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
# Only the instructions listed above are used. The eight registers here, named a through h, all start at 0.

# The coprocessor is currently set to some kind of debug mode, which allows for testing, but prevents it from doing any meaningful work.

# If you run the program (your puzzle input), how many times is the mul instruction invoked?

from collections import Counter

d = open('inputs/23.txt').read()
ops = set()
reg = Counter()

def val(s:str):
    try:
        v = int(s)
    except ValueError:
        v = reg[s]
    return v    

pos = 0 
lines = d.splitlines()[:-1]
tally = 0 
while pos>=0 and pos<=len(lines):

    parts = lines[pos].split()
    print(parts)

    A = parts[1]
    B = val(parts[2])
    
    match parts[0]:
        case 'mul':
            reg[A] *= B
            tally+=1
        case 'sub':
            reg[A] -= B
        case 'set':
            reg[A] = B
        case 'jnz':
            a_val = val(A)
            if a_val != 0:
                pos += B 
                continue
    print(reg)
    pos+=1       

print(tally)