from collections import defaultdict

d = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''

d = open('inputs/12.txt').read()

tree = defaultdict(set)

for line in d.splitlines():
    s,t = line.split('<->')
    for e in t.split(', '):
        tree[s.strip()].add(e.strip())

                

def walk(x):
    group = {x}
    new = {x}
    while new:
        next = set() 
        for item in new:
            next.update(tree[item])
        new = next - group
        group.update(next)
    return group

print(len(walk('0')))

seen = set()
for k in tree.keys():
    # count number of unique sets
    g = walk(k)
    seen.add(str(sorted(g)))
print(len(seen))