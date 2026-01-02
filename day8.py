from collections import Counter

d = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

d = open('inputs/8.txt').read() 

reg = Counter()
# so there's always something in reg.values()
reg['a']=0

biggest = -1
for line in d.splitlines():
    p = line.split()
    
    if eval(f'{reg[p[4]]} {p[5]} {p[6]}'):
        match p[1]:
            case 'inc':
                reg[p[0]] += int(p[2])
            case 'dec':
                reg[p[0]] -= int(p[2])
    biggest = max(biggest,max(reg.values()))

print(max(reg.values()))      
print(biggest)  
