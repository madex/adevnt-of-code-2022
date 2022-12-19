import re
f = open('test.txt')
m = {}
for line in f.read().strip().split('\n'):
    match = re.search(r'Valve (..).*=(-?\d+).*valve.? (.*)', line)
    if match:
        m[match.group(1)] = [int(match.group(2)), 
                     [x for x in match.group(3).split(', ')]]
f.close()
openValve = []
import functools

@functools.cache
def go(to, min_left, pressureSum, ele):
    global way, openValve
    v = m[to]
    #print(to, min_left, pressureSum, openValve)
    if min_left == 0:
        return pressureSum
    else:
        ret = 0
        if v[0] > 0 and v[0] not in openValve:
            openValve.append(v[0])
            pSum = pressureSum + v[0] * (min_left-1)
            ret = go(to, min_left-1, pSum, ele)
            openValve.pop()
        return max(ret, max(go(x, min_left-1, pressureSum, ele) for x in v[1]))

print("Part 1: ", go('AA', 30, 0, False))
#print("Part 2: ", go('AA', 26, 0, True))
