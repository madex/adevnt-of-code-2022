import math
class Monkey:
    def __init__(self, str):
        _, items, op, test, true, false = str.strip().split('\n')
        self.item  = [int(i) for i in items.split(':')[1].split(',')]
        words      = op.split()
        op         = ''.join(words[-3:])
        self.op    = lambda old,op=op:eval(op)
        self.test  = int(test.split()[-1])
        self.true  = int(true.split()[-1])
        self.false = int(false.split()[-1])
        self.insp  = 0

f = open('input.txt')
inp = f.read()
monkey = [Monkey(x) for x in inp.split('\n\n')]
f.close()
for r in range(20):
    for m in monkey:
        while len(m.item) > 0:
            m.insp += 1
            i = m.item.pop(0)
            i = m.op(i)
            to = m.true if (i % m.test) == 0 else m.false
            monkey[to].item.append(i // 3)
            
part1 = [m.insp for m in monkey]
part1.sort(reverse=True)
print("Part 1:", part1[0] * part1[1]) # 10605
monkey = [Monkey(x) for x in inp.split('\n\n')]
common_divisor = math.prod([m.test for m in monkey])
for r in range(10_000):
    for m in monkey:
        while len(m.item) > 0:
            m.insp += 1
            i = m.item.pop(0)
            i = m.op(i)
            to = m.true if (i % m.test) == 0 else m.false
            monkey[to].item.append(i % common_divisor)

part2 = [m.insp for m in monkey]
part2.sort(reverse=True)
print("Part 2:", part2[0] * part2[1]) # 2713310158
