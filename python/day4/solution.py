import re
count1 = 0
count2 = 0
with open("input.txt") as fp:
    for line in fp:
        r = [int(x) for x in re.split(',|-', line.strip())]
        if (r[0] <= r[2] and r[1] >= r[3]) or (r[2] <= r[0] and r[3] >= r[1]):
            count1 += 1
        if ((r[0] >= r[2] and r[0] <= r[3]) or (r[1] >= r[2] and r[1] <= r[3]) or 
            (r[2] >= r[0] and r[2] <= r[1]) or (r[3] >= r[0] and r[3] <= r[1])):
            count2 += 1
print(count1)
print(count2)