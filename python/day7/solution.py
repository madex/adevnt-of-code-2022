class Dir:
    def __init__(self, name="", dir=True, size=None):
        self.name   = name
        self.dir    = dir
        self.size   = size
        self.sub    = []
        self.parent = None

    def insert(self, node):
        self.sub.append(node)
        node.parent = self

root = Dir("/", True)
cur = root
sumSmall = 0
dirSizes = []

def searchSize(dir, limit):
    global sumSmall, dirSizes
    size = 0
    for f in dir.sub:
        if f.dir:
            size += searchSize(f, limit)
        else:
            size += f.size
    if size <= limit:
        sumSmall += size
    dirSizes.append(size)
    return size

with open("input.txt") as fp:
    for line in fp:
        l = [x for x in line.strip().split(' ')]
        if l[0] == '$':
            if l[1] == "cd":
                if l[2] == "/":
                    cur = root
                elif l[2] == "..":
                    cur = cur.parent
                else:
                    newSub = None
                    for x in cur.sub:
                        if x.name == l[2]:
                            newSub = x
                            break
                    if newSub != None:
                        cur = newSub
        else:
            if l[0] == "dir":
                cur.insert(Dir(l[1], True))
            else:
                cur.insert(Dir(l[1], False, int(l[0])))
total = searchSize(root, 100_000)
print("Part 1 :", sumSmall) # 95437
dirSizes.sort()
for d in dirSizes:
    if 70_000_000 - total + d >= 30_000_000:
        print("Part 2 :", d) # 24933642
        break
