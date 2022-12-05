# 0 Rock  1 Paper  2 Scissors
# 0 wins 2   1 wins 0   2 wins 1
win = [2, 0, 1]
def round(a, b):
    if a == b:
        return 3
    elif win[a] == b:
        return 6
    return 0

def opponentResult(o, r):
    score = 0
    if r == 1: # draw
        score = 3 + o + 1
    elif r == 0: # loose
        score = win[o] + 1
    else: # win
        for i in range(3):
            if win[i] == o:
                score += 6 + i + 1
                break
    return score

score1 = 0
score2 = 0
with open("input.txt") as fp:
    for line in fp:
        if len(line) > 0:
            o, y = ord(line[0]) - ord('A'), ord(line[2]) - ord('X')
            score1 += round(y, o) + y + 1
            score2 += opponentResult(o, y)
print(score1)
print(score2)
