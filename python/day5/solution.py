f = open('input.txt')
stackStr, moves = f.read().split('\n\n', 1)
stackStr = stackStr.split('\n')
stackStr.reverse()
stackStr.pop(0) # remove stack numbers
moves = moves.split('\n')
stack = []
# build stack
for x in stackStr:
    stacks = len(x)//4 + 1
    if len(stack) < stacks:
        stack = [[] for _ in range(stacks)]
    for i in range(0, stacks):
        c = x[1 + 4*i]
        if c != ' ':
            stack[i].insert(0, c)
stackP2 = [x[:] for x in stack] # deep copy
for m in moves:
    m = [int(m.split(' ')[x]) for x in range(1, 6, 2)]
    # do moves part1
    for i in range(m[0]):
        stack[m[2]-1].insert(0, stack[m[1]-1].pop(0))
    # do moves part2
    h = []
    for i in range(m[0]):
        h.insert(0, stackP2[m[1]-1].pop(0))
    for i in range(m[0]):
        stackP2[m[2]-1].insert(0, h.pop(0))
# build result string1
result, result2 = "", ""
for x in stack:
    result += x[0]
# build result string1
for x in stackP2:
    result2 += x[0]
print(result) # test CMX
print(result2) # test MCD
f.close()
