ways = []

f = open('input.txt')
m = [[c for c in x] for x in f.read().strip().split('\n')]
f.close()
#print(m)

def get(p):
    global m
    return m[p[0]][p[1]] if 0 <= p[0] < len(m) and 0 <= p[1] < len(m[0]) else '_'

def add(p, v):
    return [p[0]+v[0], p[1]+v[1]]
S = []
E = []
for x in range(len(m)):
    for y in range(len(m[0])):
        c = [x, y]
        if get(c) == 'E':
            E = c
        elif get(c) == 'S':
            S = c

dist = { str(E): 0 }

def can_go(fr, to):
    fr_s, to_s = get(fr), get(to)
    return to_s != '_' and str(to) not in dist and \
           (ord(fr_s) - ord(to_s) <= 1 or 
            (fr_s == 'a' and to_s == 'S') or 
             fr_s == 'E' and to_s == 'z') 

last = 'E'
queue = [ E ]
while queue:
    cur = queue.pop(0)
    d = dist[str(cur)]
    for v in [[1,0], [-1,0], [0,1], [0,-1]]:
        n = add(cur, v)
        if can_go(cur, n):
            queue.append(n)
            dist[str(n)] = d + 1
p1 = dist[str(S)]
print("Part 1: ", p1)
for x in range(len(m)):
    for y in range(len(m[0])):
        c = [x, y]
        if get(c) == 'a' and str(c) in dist and dist[str(c)] < p1:
            p1 = dist[str(c)]
print("Part 2: ", p1)
