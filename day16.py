from collections import deque

reg='abcde'
d='s1,x3/4,pe/b'

d = open('inputs/16.txt').read().strip()
reg = 'abcdefghijklmnop'

def dance(reg:str):
    r = deque(reg)

    for step in d.split(','):
        if step.startswith('s'):
            s = int(step[1:])
            r.rotate(s)
        elif step.startswith('x'):
            a,b = map(int,step[1:].split('/'))

            A = r[a]
            B = r[b]
            r[b] = A 
            r[a] = B

        elif step.startswith('p'):
            a,b = step[1:].split('/')
            # swap a and b's positions around.
            a_pos = r.index(a)
            b_pos = r.index(b)
            r[a_pos] = b
            r[b_pos] = a

    return ''.join(r)

# assert dance() == 'baedc'
print(dance(reg))

reg = 'abcdefghijklmnop'
seen = set()
counter = 0 
while True:
    reg = dance(reg)
    counter+=1
    if reg in seen:
        if counter%100==0:
            print(counter,reg)
    else:
        seen.add(reg)
