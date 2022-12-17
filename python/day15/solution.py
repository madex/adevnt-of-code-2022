import re
f = open('input.txt')
m = []
for line in f.read().strip().split('\n'):
    match = re.search(r'=(-?\d+).*=(-?\d+).*=(-?\d+).*=(-?\d+)', line)
    if match:
        m.append([int(match.group(i)) for i in range(1, 5)])
f.close()
y =  2000000
blocked = set()
for e in m:
    d = abs(e[0] - e[2]) + abs(e[1] - e[3])
    e.append(d)
    a = abs(e[1] - y)
    for x in range(e[0] - d + a , e[0] + d - a + 1):
        if x not in blocked and abs(e[0] - x) + a <= d:
            blocked.add(x)
# remove x from beacons
for e in m:
    if e[3] == y:
        blocked.discard(e[2])

print("Part 1:", len(blocked))
cMax = 400000

def check(x, y):
    for e in m:
        if abs(e[0] - x) + abs(e[1] - y) <= e[4]:
            return True
    return False

for x in range(cMax + 1):
    for y in range(cMax + 1):
        if not check(x, y):
            print("Part 2:", 4000000*x + y)
            break