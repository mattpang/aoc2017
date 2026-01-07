d = '''..#
#..
...'''

d = open('inputs/22.txt').read()

# print(pos,grid)  
def run(n):
    grid = dict()
    
    for y,line in enumerate(d.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                grid[complex(x,y)] = c
                
    c =  len(d.splitlines()) // 2
    pos = complex(c,c)
    facing = complex(0,-1)
    
    infected = 0 
    for i in range(n):
        if grid.get(pos) is None:
            # turn left
            grid[pos] = '#'
            facing *= complex(0,-1)
            pos += facing
            infected +=1
        elif grid.get(pos) == '#':
            # turn right
            del grid[pos]
            facing *= complex(0,1)
            pos += facing
            
        
        # xs = [int(x.real) for x in grid.keys()]
        # ys = [int(x.imag) for x in grid.keys()]
    
        # for y in range(min(ys)-1,max(ys)+2):
        #     line = ''
        #     for x in range(min(xs)-1,max(xs)+2):
        #         c = grid.get(complex(x,y),'.')
        #         if pos == complex(x,y):
        #             c = 'X'
        #         line+=c
        #     print(line)
        # print('---')    
        
    print(infected)
    
    return infected
    

def run_pt2(n,debug=False):
    grid = dict()
    
    for y,line in enumerate(d.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                grid[complex(x,y)] = c
                
    c =  len(d.splitlines()) // 2
    pos = complex(c,c)
    facing = complex(0,-1)
    
    infected = 0 
    for i in range(n):
        if grid.get(pos) is None:
            # turn left
            grid[pos] = 'W'
            facing *= complex(0,-1)
            pos += facing
        elif grid.get(pos) == '#':
            # turn right
            grid[pos] = 'F'
            facing *= complex(0,1)
            pos += facing
        elif grid.get(pos) == 'W':
            grid[pos] = '#'
            infected +=1
            pos += facing
        elif grid.get(pos) == 'F':
            # reflects if flagged
            del grid[pos]
            facing *= complex(0,1)
            facing *= complex(0,1)
            pos += facing

        if debug:
            xs = [int(x.real) for x in grid.keys()]
            ys = [int(x.imag) for x in grid.keys()]
        
            for y in range(min(ys)-1,max(ys)+2):
                line = ''
                for x in range(min(xs)-1,max(xs)+2):
                    c = grid.get(complex(x,y),'.')
                    if pos == complex(x,y):
                        c = 'X'
                    line+=c
                print(line)
            print('---')    
        

    return infected

# assert run(70) == 41
# assert run(10000) == 5587
# assert run_pt2(7,True)== 26
# assert run_pt2(10000000) == 2511944
print(run(10000))
print(run_pt2(10000000))