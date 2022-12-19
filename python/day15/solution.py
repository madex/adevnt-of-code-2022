def check(y, part1):
    blocked = []
    for e in m:
        d = abs(e[0] - e[2]) + abs(e[1] - e[3])
        a = abs(e[1] - y)
        if a <= d:
            blocked.append([e[0] - d + a, e[0] + d - a]) 
    blocked.sort()
    b = blocked.pop(0)
    for x in blocked:
        if b[0] <= x[0] <= b[1]:
            if x[1] > b[1]:
                b[1] = x[1]
        else:
            return x[0] - 1
    if part1:
        return b[1] - b[0] + 1 
    return -1

import re
f = open('input.txt')
m = []
for line in f.read().strip().split('\n'):
    match = re.search(r'=(-?\d+).*=(-?\d+).*=(-?\d+).*=(-?\d+)', line)
    if match:
        m.append([int(match.group(i)) for i in range(1, 5)])
f.close()
y = 2000000 # 10
blocked = check(y, True)
# remove x from beacons
rem = set()
for e in m:
    if e[3] == y:
        rem.add(e[2])
print("Part 1:", blocked - len(rem))
cMax = 4000000 # 20

for y in range(cMax + 1):
    x = check(y, False)
    if x != -1:
        print("Part 2:", 4000000*x + y)
        break
