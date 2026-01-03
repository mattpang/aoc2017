from collections import Counter

d = '''0: 3
1: 2
4: 4
6: 4'''

d = open('inputs/13.txt').read()

wall = dict()
for line in d.splitlines():
    b,depth = line.split(': ')
    wall[int(b)] = int(depth)


def run(delay:int):
    tally = 0 
    wall_pos = Counter()

    for tick in range(1,delay+max(wall.keys())+1):
        # it doesn't cycle, but moves up and down the depth.
        #  for 4:, a cycle should be every 6.
        # 0,1,2,3,2,1,0,2,3 etc

        for k,v in wall.items():
            wall_pos[k] += int(((tick-1)//(v-1)%2-0.5)*-2)
            
            if wall_pos[k]==0 and (tick-delay)==k:
                tally+=tick*v

    return tally

print(run(delay=0))
# print(run(delay=10))
# method is too slow to loop

import itertools
def scanner(height, delay):
    offset = delay % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

part2 = next(wait for wait in itertools.count() if not any(scanner(wall[pos], wait + pos) == 0 for pos in wall))
print(part2)
