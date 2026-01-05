d = '''     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
'''

d = open('inputs/19.txt').read()

grid = dict()
# scan first line for the start of the track. 
for y,line in enumerate(d.splitlines()):
    for x,c in enumerate(line):
        if y==0 and c=='|':
            pos = (x,y)
        if c!=' ':
            grid[x,y] = c


# at a turn, you will match your current direction and the new direction
current_dir = 'd'
moves = {'d':(0,1),'u':(0,-1),'l':(-1,0),'r':(1,0)}
turns = {(0,1,'|'):'d', (1,0,'-'):'r', (-1,0,'-'):'l',(0,-1,'|'):'u'}
flip = {'d':'u','l':'r','r':'l','u':'d'}
letters = []
i=1
while True:
    next_move = moves[current_dir]
    # print(f'{next_move=}')
    npos = (pos[0]+next_move[0] , pos[1]+next_move[1])

    if grid.get(npos) == '+':
        detected_dirs = [] 
        for k,v in turns.items():
            # print('next dir:',grid.get(npos),grid.get((npos[0]+k[0],npos[1]+k[1])))
            if grid.get((npos[0]+k[0],npos[1]+k[1])):
                detected_dirs.append(v)

        # print(f'{detected_dirs=}')
        current_dir = list(set(detected_dirs) - set([flip[current_dir]]))[0]
        # print(f'new direction {current_dir} at {npos}')
    elif grid.get(npos) not in ['-','|',None]:
        letters.append(grid.get(npos))
    elif grid.get(npos) is None:
        print(grid.get(npos),npos)
        print('maybe end of maze')
        break
    
    pos = npos
    i+=1

# print(f'{letters=}')
print(''.join(letters))
print(i)