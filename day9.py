import re 
from collections import Counter
brackets = Counter()


def clean_garbage(a):
    # negate any chars following a !
    a = re.sub('!.','',a)
    # remove anything inside garbage tags. 
    a= re.sub('<.*?>', "",a)
    return a


def score(s):
    x = clean_garbage(s)
    tally=0

    # nested groups are worth +1 each level. 
    for c in x:
        if c =='{':
            brackets['{'] +=1
        elif c=='}':
            tally+= brackets['{']
            brackets['{'] -= 1
    
    return tally

def count_garbage(s):
    a = re.sub('!.','',s)
    g = re.finditer('<.*?>', a)
    t = 0 
    for match in g:
        m = match.span()
        t += m[1]-m[0] - 2
    print(t)
    return t

assert score('{}') == 1
assert score('{{{}}}') == 6
assert score('{{},{}}') == 5
assert score('{{{},{},{{}}}}') == 16
assert score('{<a>,<a>,<a>,<a>}') == 1
assert score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
assert score('{{<!!>},{<!!>},{<!!>},{<!!>}}')==9
assert score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

d = open('inputs/9.txt').read().strip()

print(score(d))
count_garbage(d)