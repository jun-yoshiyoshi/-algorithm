MAX = 6
que = [0] * MAX
head, tail = 0, 0


def enqueue(d):
    global tail
    nt = (tail + 1) % MAX

    if nt == head:
        print("これ以上データをいれられません")
    else:
        que[tail] = d
        tail = nt
        print("データ", d, "を追加しました")


def dequeue():
    global head
    if head == tail:
        print("取り出すデータが存在しません")
        return None
    else:
        d = que[head]
        head = (head + 1) % MAX
        return d


for i in range(6):
    enqueue(i)

for i in range(6):
    d = dequeue()
    print("取り出したデータ", d)
