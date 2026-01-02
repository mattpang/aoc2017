
d = open('inputs/6.txt').read()
r = list(map(int,d.split()))
# r = [0,2,7,0]
seen = set()
count=0
twice = False
first_seen = None

while True:

    b = r.index(max(r))
    amt = r[b]
    r[b] = 0
    c=1
    while amt>0: 
        r[(b+c) %len(r)] +=1
        amt-=1
        c+=1
    
    combo = ''.join([str(x) for x in r])
    count+=1
    if combo in seen:
        if first_seen is None:
            first_seen = combo
            first_idx = count
            continue

        if combo == first_seen and first_seen is not None:
            break
        twice = True
        
    seen.add(combo)
    
print(first_idx)
print(count-first_idx)