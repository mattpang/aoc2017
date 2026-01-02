from collections import deque

p = [3,4,1,5]
loop = [0,1,2,3,4]
limit = 5

limit = 256
p = [189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62]
loop = [x for x in range(256)]

skip = 0
pos = 0 
for l in p:
    to_reverse = []
    for x in range(l):
        n = (pos + x) % limit
        to_reverse.append(loop[n])
    to_reverse.reverse()
    for x in range(l):
        n = (pos + x) % limit
        loop[n] = to_reverse[x]
    pos += l + skip
    pos = pos % limit
    skip += 1


print(loop[0]*loop[1])
from functools import reduce

limit = 256
p = [ord(x) for x in "189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"]
# p = [ord(x) for x in "AoC 2017"]
p.extend([17,31,73,47,23])
loop = [x for x in range(256)]

skip = 0
pos = 0 
for _ in range(64):
    for l in p:
        to_reverse = []
        for x in range(l):
            n = (pos + x) % limit
            to_reverse.append(loop[n])
        to_reverse.reverse()
        for x in range(l):
            n = (pos + x) % limit
            loop[n] = to_reverse[x]
        pos += l + skip
        pos = pos % limit
        skip += 1


dense = []
for x in range(0,16):
	slice = loop[16*x:16*x+16]
	dense.append('%02x'%reduce((lambda x,y: x ^ y),slice))
print(''.join(dense))
