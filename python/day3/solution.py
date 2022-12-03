prior1 = 0
prior2 = 0
c = []

def get_prior(ch):
    if ord(x) >= ord('a'):
        return ord(x) - ord('a') + 1
    else:
        return ord(x) - ord('A') + 27

with open("input.txt") as fp:
    for line in fp:
        l2 = len(line)//2
        a, b = line[:l2], line[l2:]
        for x in a:
            if b.find(x) != -1:
                prior1 += get_prior(x)
                break
        c.append(line)
        if len(c) == 3:
            for x in c[0]:
                if c[1].find(x) != -1 and c[2].find(x) != -1:
                    prior2 += get_prior(x)
                    break
            c = []    

print(prior1) # test 157
print(prior2) # test 70
