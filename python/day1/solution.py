#f = open('test.txt') # = 24000 / 45000
f = open('input.txt')
inp = [sum(list(map(int, x.split('\n')))) for x in f.read().split('\n\n')]
print(max(inp))
print(sum(sorted(inp, reverse=True)[0:3]))
f.close()
