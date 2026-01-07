from collections import Counter
from enum import CONTINUOUS
from itertools import permutations
import heapq

d = '''0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10'''

d = open('inputs/24.txt').read()

parts = d.splitlines()

valid = Counter()
valid_str = []

stack = []

starters = []
for i in parts:
    if i[0]=='0':
        starters.append(i)
print(starters)

for starter in starters:
    used = []
    used.append(starter)
    pstr = 0
    a1,last = list(map(int,starter.split('/')))
    pstr -= a1
    pstr -= last
    
    heapq.heappush(stack,(pstr,used,last))

biggest = 0
strongest = None
while len(stack)>0:
    pstr,consumed,last = heapq.heappop(stack)

    # add for each one that is valid, not just the first one.
    for i in set(parts).difference(set(consumed)):
        b1,b2 = list(map(int,i.split('/')))
        if b1==last or b2==last:
            if b1==last:
                nlast = b2
            else:
                nlast = b1
                            
            heapq.heappush(stack,(pstr-b1-b2,consumed+[i],nlast))
            if biggest< abs(pstr):
                biggest = abs(pstr)
                strongest = consumed
            
            

print(biggest, strongest)
# 1360