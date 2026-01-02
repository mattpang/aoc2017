# find the root of the tree
from dataclasses import dataclass

d = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''

d = open('inputs/7.txt').read()

@dataclass
class leaf():
    parent_name:str
    children:list[str]
    weight:int

from collections import defaultdict
store = defaultdict(leaf)
children = set()
all_nodes = set()
for line in d.splitlines():
    parts = line.split()
    weight = int(parts[1][1:-1])
    node = parts[0]
    if len(parts)>3:
        _, branches = line.split('->')
        
        all_nodes.add(node)
        
        children_nodes = branches.strip().split(', ')
        store[node] = leaf(node,children_nodes,weight=weight)
        for branch in children_nodes:
            children.add(branch)
            all_nodes.add(branch)
    else:
        store[node] = leaf(parent_name=node,children=[],weight=weight)

root = list(all_nodes - children)[0]
print(root)

print(store[root])

def get_branch_weight(x): 
    branch_weights = []
    nw = 0 
    if len(store[x].children)>0:
        print(store[x].children)

        for child in store[x].children:
            w = (store[x].weight + get_branch_weight(child))
            # if the branch weights aren't equal, need to fix the base weight.
            branch_weights.append((w,child))
            nw+=w
        if len(set([x[0] for x in branch_weights])) != 1:
            print(x,branch_weights,store[x].children)
        return nw
    else:
        print(store[x].parent_name,store[x].weight)
        return store[x].weight

print(get_branch_weight(root))