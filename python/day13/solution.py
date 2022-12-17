def compare(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]
    if isinstance(a, int)  and isinstance(b, list):
        a = [a]
    if isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if i == len(b):
                return -1
            res = compare(a[i], b[i])
            if res != 0:
                return res
        if len(b) > len(a):
            return 1   
    else:
        if a < b:
            return 1
        elif b < a:
            return -1
    return 0

f = open('input.txt')
m = [[eval(c) for c in x.split('\n')] for x in f.read().strip().split('\n\n')]
f.close()
right_order = []
for i, pair in enumerate(m, start=1):
    if compare(pair[0], pair[1]) == 1:
        right_order.append(i)

print("Part 1:", sum(right_order))

packets = [p[i] for p in m for i in range(2)]
packets.append([[2]])
packets.append([[6]])
from functools import cmp_to_key
packets = sorted(packets, key=cmp_to_key(lambda p1, p2: compare(p2, p1)))
part2 = 1
for i,p in enumerate(packets, start=1):
    if p==[[2]] or p==[[6]]:
        part2 *= i
print("Part 2:", part2)
