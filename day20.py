from collections import defaultdict

d='''p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<9,0,0>
'''
d = open("inputs/20.txt").read()

class dot():
  
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def step(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]
    
    def man_dist(self):
        return sum([abs(i) for i in self.p])


def run(part2:bool):

    for z in range(1000):
        min_d = None
        min_part = None
        for i, part in num.items():
            part.step()
            if min_d is None or part.man_dist() < min_d:
                min_part = i
                min_d = part.man_dist()

        if part2:
            pos_dict = defaultdict(list)
            for i, part in num.items():
                k = tuple(part.p)
                pos_dict[k].append(i)

            for k, v in pos_dict.items():
                if len(v) > 1:
                    for i in v:
                        del num[i]

    if part2:
        print(len(num))
    else:
        print(min_part)

num = dict()

for i, line in enumerate(d.splitlines()):
    p, v, a = line.split(", ")
    
    aa = list(map(int, a[3:-1].split(",")))
    vv = list(map(int, v[3:-1].split(",")))
    pp = list(map(int, p[3:-1].split(",")))
    
    num[i] = dot(pp,vv,aa)
    

run(False)

num = dict()
for i, line in enumerate(d.splitlines()):
    p, v, a = line.split(", ")
    
    aa = list(map(int, a[3:-1].split(",")))
    vv = list(map(int, v[3:-1].split(",")))
    pp = list(map(int, p[3:-1].split(",")))
    
    num[i] = dot(pp,vv,aa)
    

run(True)