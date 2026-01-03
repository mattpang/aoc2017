# Generator A starts with 289
# Generator B starts with 629

def gen(x,factor):
    
    return (x*factor) %2147483647

a= 65
b= 8921

a=289
b=629

def part1():
    tally = 0 
    for i in range(40_000_000):
        a = gen(x=a,factor=16807)
        b = gen(x=b,factor=48271)
        if a & 0xffff == b & 0xffff:
            tally+=1
        # print(a,b,a & 0xffff,b & 0xffff)
    print(tally)

def gen2(x,factor,mod):
    while True:
        x = (x*factor) % 2147483647
        if x%mod==0:
            yield x

def part2():
    tally = 0
    A = gen2(x=a,factor=16807,mod=4)
    B = gen2(x=b,factor=48271,mod=8)
    for i in range(5_000_000):
        if next(A) & 0xffff == next(B) & 0xffff:
            tally+=1
    return tally

print(part1())
print(part2())