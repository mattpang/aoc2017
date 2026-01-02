#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \
# hexgrid can be (q,r,s) coords: https://www.redblobgames.com/grids/hexagons/#distances

s = open('inputs/11.txt').read().strip()

hex_dir = {'n':(0,1,-1),'s':(0,-1,1),'ne':(1,0,-1),'se':(1,-1,0),'sw':(-1,0,1),'nw':(-1,1,0)}

def dist(xin):
    x,y,z = 0,0,0
    biggest = 0 
    for d in xin.split(','):
        x+=hex_dir[d][0]
        y+=hex_dir[d][1]
        z+=hex_dir[d][2]
        
        d= (abs(x)+abs(y)+abs(z))//2
        biggest = max(biggest,d)
    print(d)
    print(biggest)
    return d


# ne,ne,ne is 3 steps away.
# ne,ne,sw,sw is 0 steps away (back where you started).
# ne,ne,s,s is 2 steps away (se,se).
# se,sw,se,sw,sw is 3 steps away (s,s,sw).

# assert dist('ne,ne,ne') == 3
# assert dist('ne,ne,sw,sw') == 0
# assert dist('ne,ne,s,s') == 2
# assert dist('se,sw,se,sw,sw') == 3

dist(s)