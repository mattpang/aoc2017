steps = 12523873
left, right = 0, 1
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5

instructions = {
    (a, 0): (1, right, b),
    (a, 1): (1, left, e),
    (b, 0): (1, right, c),
    (b, 1): (1, right, f),
    (c, 0): (1, left, d),
    (c, 1): (0, right, b),
    (d, 0): (1, right, e),
    (d, 1): (0, left, c),
    (e, 0): (1, left, a),
    (e, 1): (0, right, d),
    (f, 0): (1, right, a),
    (f, 1): (1, right, c),
}

t = dict()
head = 0
state = 0

for i in range(steps):
    value, direction, n_letter = instructions[(state, t.get(head, 0))]
    t[head] = value

    if direction == right:
        head += 1
    else:
        head -= 1
    state = n_letter

print(sum(t.values()))
