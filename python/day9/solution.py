D = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
h = [0, 0]
t = [0, 0]
visit = set()
s = [[0, 0] for _ in range(10)]
visit2 = set()

def move_head(d, c):
    global h, t, visit, D
    vec = D[d]
    for i in range(int(c)):
        h[0] += vec[0] 
        h[1] += vec[1]
        if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1 :
            t = [h[0] - vec[0], h[1] - vec[1]]
        visit.add(str(t))

def move_long_head(d, c):
    global s, visit, D
    vec = D[d]
    for i in range(int(c)):
        s[0][0] += vec[0] 
        s[0][1] += vec[1]
        for i in range(len(s) - 1):
            d = [s[i][0] - s[i+1][0], s[i][1] - s[i+1][1]]
            if abs(d[0]) > 1 or abs(d[1]) > 1:
                s[i+1] = [s[i][0] - (d[0]//2 if abs(d[0]) > 1 else 0), 
                          s[i][1] - (d[1]//2 if abs(d[1]) > 1 else 0)]
        visit2.add(str(s[9]))

with open("input.txt") as fp:
    for line in fp:
        l = [x for x in line.strip().split(' ')]
        move_head(l[0], l[1])
        move_long_head(l[0], l[1])

print("Part 1:", len(visit))
print("Part 2:", len(visit2))
