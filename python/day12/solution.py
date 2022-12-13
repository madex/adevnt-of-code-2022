ways = []

f = open('input.txt')
m = [[c for c in x] for x in f.read().strip().split('\n')]
f.close()
print(m)

def get(p):
    global m
    return m[p[0]][p[1]] if 0 <= p[0] < len(m) and 0 <= p[1] < len(m[0]) else '_'

def add(p, v):
    return [p[0]+v[0], p[1]+v[1]]


def find_way(positions):
    global ways
    last = positions[-1]
    ch = get(last)
    if ch == 'S':
        ch = 'a'
    for v in [[1,0], [-1,0], [0,1], [0,-1]]:
        cur = add(last, v)
        cur_ch = get(cur)
        if cur in positions:
            continue
        elif ord(ch) <= ord(cur_ch) <= ord(ch) + 1:
            positions.append(cur)
            find_way(positions)
            positions.pop()
        elif ch == 'z' and cur_ch == 'E':
            ways.append(len(positions))
            print(len(positions))
            #print(len(positions), [(x, get(x)) for x in positions])
            return

S = []
for x in range(len(m)):
    for y in range(len(m[0])):
        if m[x][y] == 'S':
            S = [x, y]
            break
find_way([S])
print(min(ways))

