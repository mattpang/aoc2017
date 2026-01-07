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

reg['a'] = 1

while pos>=0 and pos<=len(lines):

    parts = lines[pos].split()

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
    
    # print(reg['a'],reg['b'],reg['c'],reg['d'],reg['e'],reg['f'])
    pos+=1       

print(tally)

h = 0
for x in range(106700,123700 + 1,17):
	for i in range(2,x):
		if x % i == 0:
			h += 1
			break
print(h)