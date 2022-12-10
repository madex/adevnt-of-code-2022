x = 1
cycle = 0
signal = 0
rows = ""

def update_inc():
    global x, cycle, signal, rows
    cycle += 1
    if (cycle - 20) % 40 == 0:
        signal += cycle * x  
    pos = (cycle - 1) % 40
    rows += '#' if pos >= x - 1 and pos <= x + 1 else '.'
    if pos == 39:
        rows += "\n"
          
with open("input.txt") as fp:
    for line in fp:
        l = [x for x in line.strip().split(' ')]
        if l[0] == "noop":
            update_inc()
        elif l[0] == "addx":
            update_inc()
            update_inc()
            x += int(l[1])

print("Part 1: ", signal)
print("Part 2: ")
print(rows)