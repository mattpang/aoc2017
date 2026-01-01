from collections import deque
d = '91212129'
# d = '12131415'
d = open('inputs/1.txt').read()

def solve(x,pt=True):
    y = deque(x)
    if pt:
        y.rotate(len(x)//2)
    else:
        y.rotate(1)
    t=0
    for a,b in zip(x,y):
        if a==b:
            t+=int(a)
    return t

print(solve(d,False))
print(solve(d))