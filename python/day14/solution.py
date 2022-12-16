f = open('input.txt')
m = [[[int(t) for t in c.split(',')] for c in x.split(' -> ')] for x in f.read().strip().split('\n')]
f.close()
#print(m)
x_coord = [i[0] for t in m for i in t]
y_coord = [i[1] for t in m for i in t]
x_min, x_max = min(x_coord) - 1, max(x_coord) + 1
y_min, y_max = 0,                max(y_coord) + 1

grid = [['.' for _ in range(x_max)] for _ in range(y_max)]
grid[0][500] = '+'

def draw_line(p1, p2):
    if p1[0] == p2[0]:
        if p1[1] < p2[1]:
            for y in range(p1[1], p2[1]+1):
                grid[y][p1[0]] = '#'
        else:
            for y in range(p2[1], p1[1]+1):
                grid[y][p1[0]] = '#'
    elif p1[1] == p2[1]:
        if p1[0] < p2[0]:
            for x in range(p1[0], p2[0]+1):
                grid[p1[1]][x] = '#'
        else:
            for x in range(p2[0], p1[0]+1):
                grid[p1[1]][x] = '#'

for l in m:
    for i in range(len(l) - 1):
        draw_line(l[i], l[i+1])

sand = 0

def print_grid():
    global grid
    for l in grid:
        print("".join(l[x_min:x_max]))
    print()

def drop_sand():
    global sand, grid
    x, y = 500, 0
    while True:
        if y+1 >= y_max:
            return False
        elif grid[y+1][x] == '.':
            y += 1
        elif grid[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif grid[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            sand += 1
            grid[y][x] = 'o'
            return y != 0            

while drop_sand():
    a = 1

print("Part 1: ", sand)
y_max += 2
x_max *= 2
x_min -= 50
grid = [['.' for _ in range(x_max)] for _ in range(y_max)]
grid[0][500] = '+'
sand = 0
for l in m:
    for i in range(len(l) - 1):
        draw_line(l[i], l[i+1])
draw_line([0, y_max-1], [x_max-1, y_max-1])
while drop_sand():
    a = 1

print("Part 2: ", sand)