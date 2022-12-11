class Monkey:
    def __init__(self, str):
        for l in str.split('\n'):
            li = l.split(':')
            if li[0] == '  Starting items':
                self.item = [int(x.strip()) for x in li[1].split(',')]
            elif li[0] == '  Operation':
                self.op = li[1][len(" new = old "):].split(' ')
            elif li[0] == '  Test':
                self.test = int(li[1][len(" divisible by "):])
            elif li[0] == '    If true':
                self.true = int(li[1][len(" throw to monkey "):])
            elif li[0] == '    If false':
                self.false = int(li[1][len(" throw to monkey "):])
        self.insp = 0

f = open('input.txt')
inp = f.read()
monkey = [Monkey(x) for x in inp.split('\n\n')]
f.close()
for r in range(20):
    for m in monkey:
        while len(m.item) > 0:
            m.insp += 1
            i = m.item.pop(0)
            v = i if m.op[1] == 'old' else int(m.op[1])
            if m.op[0] == '+':
                i = i + v
            elif m.op[0] == '*':
                i = i * v
            to = m.true if (i % m.test) == 0 else m.false
            monkey[to].item.append(i // 3)
            
part1 = [m.insp for m in monkey]
part1.sort(reverse=True)
print("Part 1:", part1[0] * part1[1]) # 10605
monkey2 = [Monkey(x) for x in inp.split('\n\n')]
common_divisor = 1
for m in monkey2:
    common_divisor *= m.test 
for r in range(10000):
    for m in monkey2:
        while len(m.item) > 0:
            m.insp += 1
            i = m.item.pop(0)
            v = i if m.op[1] == 'old' else int(m.op[1])
            if m.op[0] == '+':
                i = i + v
            elif m.op[0] == '*':
                i = i * v
            to = m.true if (i % m.test) == 0 else m.false
            monkey2[to].item.append(i % common_divisor)

part2 = [m.insp for m in monkey2]
part2.sort(reverse=True)
print("Part 2:", part2[0] * part2[1]) # 2713310158
