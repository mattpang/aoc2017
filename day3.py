# implment the spiral instead of doing the equation for it. 
# when you hit the new biggest of that direct, you turn.

def calc(x:int):

    biggest_up = 0 
    biggest_down =0
    biggest_left = 0
    biggest_right = 0 

    n_dir = complex(1,0)
    pos = complex(0,0)
    grid = dict() 

    grid[1] = pos

    n_pos = pos

    for i in range(2,x+1):
        
        n_pos += n_dir
        if n_pos.real > biggest_right:
            biggest_right = n_pos.real
            n_dir *= complex(0,1)
        elif n_pos.real < biggest_left:
            biggest_left = n_pos.real
            n_dir *= complex(0,1)
        elif n_pos.imag > biggest_down:
            biggest_down = n_pos.imag
            n_dir *= complex(0,1)
        elif n_pos.imag < biggest_up:
            biggest_up = n_pos.imag
            n_dir *= complex(0,1)
        
        grid[i] = n_pos

    return int(abs(grid[x].real) + abs(grid[x].imag))



def p2(x:int):

    biggest_up = 0 
    biggest_down =0
    biggest_left = 0
    biggest_right = 0 

    n_dir = complex(1,0)
    pos = complex(0,0)
    grid = dict() 

    grid[pos] = 1

    n_pos = pos

    for i in range(2,x+1):
        
        n_pos += n_dir
        if n_pos.real > biggest_right:
            biggest_right = n_pos.real
            n_dir *= complex(0,1)
        elif n_pos.real < biggest_left:
            biggest_left = n_pos.real
            n_dir *= complex(0,1)
        elif n_pos.imag > biggest_down:
            biggest_down = n_pos.imag
            n_dir *= complex(0,1)
        elif n_pos.imag < biggest_up:
            biggest_up = n_pos.imag
            n_dir *= complex(0,1)
        
        # get all the neighbours.
        value = 0 
        for i in range(-1,2):
            for j in range(-1,2):
                if i!=0 or j!=0:
                    # print(complex(i,j))
                    value += grid.get(n_pos+complex(i,j),0)
        grid[n_pos] = value

        if value>x:
            print(value)
            break

assert calc(12) == 3
assert calc(23) == 2
assert calc(1024) == 31
print(calc(361527)) 

p2(361527)