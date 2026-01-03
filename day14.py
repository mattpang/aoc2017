from scipy import ndimage
import numpy as np 
from functools import reduce

def knothash(s:str):
    limit = 256
    p = [ord(x) for x in s]
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
    return ''.join(dense)


used = 0 
phrase = 'flqrgnkx'
phrase = 'oundnydw'
grid = [] 
for row in range(128):
    out = knothash(f'{phrase}-{row}')
    row_bits = ''
    for c in out:
        row_bits+=str(bin(int(c,base=16)))[2:].zfill(4)

    used += sum([i=='1' for i in row_bits])
    row = [i=='1' for i in row_bits]
    grid.append(row)
print(used)

# part 2 is easy with ndimage's ndimage.label functions. 
g = np.asarray(grid)
labels, num_features = ndimage.label(g,structure=[[0,1,0],
 [1,1,1],
 [0,1,0]])
print(num_features)