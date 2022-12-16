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

f = open('test.txt')
m = [[eval(c) for c in x.split('\n')] for x in f.read().strip().split('\n\n')]
f.close()
right_order = []
for i, pair in enumerate(m):
    if compare(pair[0], pair[1]) == 1:
        right_order.append(i + 1)

print("Part 1:", sum(right_order))

packets = [p[i] for p in m for i in range(2)]
packets.append([[2]])
packets.append([[6]])
t = [str(p).replace('[',"").replace(']',"").replace(',',"").replace(' ',"") for p in packets]
p2 = 1
for i, s in enumerate(sorted(t)):
    if s == '2' or s == '6':
        print(i+1, s)
        p2 *= i + 1
#print(sorted(t))
print("Part 2:", p2)
