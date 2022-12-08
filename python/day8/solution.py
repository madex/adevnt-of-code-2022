def mark_visible(m, v, pos, vec):
    max_hight = -1
    for _ in range(len(m)):
        h = m[pos[0]][pos[1]]
        if h > max_hight:
            max_hight = h
            v[pos[0]][pos[1]] = 1
        pos[0] += vec[0]
        pos[1] += vec[1]

def scenic_score(m, pos, vec):
    height = m[pos[0]][pos[1]]
    score  = 0
    pos[0] += vec[0]
    pos[1] += vec[1]
    while pos[0] >= 0 and pos[0] < len(m) and pos[1] >= 0 and pos[1] < len(m):
        cur = m[pos[0]][pos[1]] 
        score += 1
        if cur >= height:
            break
        pos[0] += vec[0]
        pos[1] += vec[1]
    return score

f = open('input.txt')
m = [[int(x) for x in i] for i in f.read().strip().split('\n')]
f.close()
v = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
for x in range(len(m)):
    for y in range(len(m)):
        if x == 0:
            mark_visible(m, v, [x, y], [1, 0])
        elif x == len(m) - 1:
            mark_visible(m, v, [x, y], [-1, 0])
        elif y == 0:
            mark_visible(m, v, [x, y], [0, 1])
        elif y == len(m) - 1:
            mark_visible(m, v, [x, y], [0, -1])
print("Part 1:", sum(sum(x) for x in v))
max_tss = 0
for x in range(1,len(m)-1):
    for y in range(1,len(m)-1):
        tss = 1
        for v in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            tss *= scenic_score(m, [x, y], v)
        if tss > max_tss:
            max_tss = tss
print("Part 2:", max_tss)
