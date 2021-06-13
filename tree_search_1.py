le = 0
ri = 1
data = 2
node = [
    [1, 2, 10],
    [3, 4, 5],
    [5, None, 12],
    [None, None, 2],
    [6, 7, 8],
    [None, None, 11],
    [None, None, 6],
    [None, None, 9],
]


def traverse(p):
    if p != None:
        traverse(node[p][le])
        print(node[p][data])
        traverse(node[p][ri])


print("二分探索木を通り掛け順に巡回")
traverse(0)
