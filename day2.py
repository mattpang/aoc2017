d = open('inputs/2.txt').read().splitlines()

tally= 0
p2_total = 0 
for line in d:
    t = list(map(int,line.split()))
    tally+=max(t) - min(t)

    for y in t:
        for x in t:
            if x!=y:
                if x%y==0:
                    p2_total+= (max(x,y) // min(x,y))

print(tally)
print(p2_total)