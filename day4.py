d = open('inputs/4.txt').read().splitlines()

t = 0 
for line in d:
    if len(set(line.split())) == len(line.split()):
        t+=1

print(t)
# part2 no anagrams

t = 0 
for line in d:
    if len(set(map(str,map(sorted,line.split())))) == len(line.split()):
        t+=1

print(t)

