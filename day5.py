d = '''0
3
0
1
-3'''

d = open('inputs/5.txt').read()

reg = list(map(int,d.splitlines()))

pos = 0 
jumps = 0


while pos >= 0 and pos < len(reg):
    if reg[pos] >= 3:
        reg[pos] -= 1
        pos = pos + reg[pos] + 1
    else:
        reg[pos] += 1
        pos = pos + reg[pos] - 1
    
    # print(pos,reg)
    jumps +=1

print(jumps)