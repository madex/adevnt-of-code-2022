f = open('input.txt')
s = f.read().strip()
f.close()
#s = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # 11
for i in range(len(s) - 3):
    if len(set(s[i:i + 4])) == 4:
        print("Part 1:", i + 4)
        break
#s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 19
for i in range(len(s) - 13):
    if len(set(s[i:i + 14])) == 14:
        print("Part 2:", i + 14)
        break