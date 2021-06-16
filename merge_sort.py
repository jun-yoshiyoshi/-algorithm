import random

n = int(input())
data = [random.randint(1, 99) for _ in range(n)]
print(data, "元のデータ")


def merge(le, mi, ri):
    buff = [0] * (ri - le)
    i, j, p = le, mi, 0
    while i < mi and j < ri:
        if data[i] <= data[j]:
            buff[p] = data[i]
            i += 1
            p += 1
        else:
            buff[p] = data[j]
            j += 1
            p += 1
    while i < mi:
        buff[p] = data[i]
        i += 1
        p += 1
    while j < ri:
        buff[p] = data[j]
        j += 1
        p += 1
    for _ in range(le, ri):
        data[_] = buff[_ - le]


s = 2
while s < n:
    loop = n // s
    fragment = n % s
    for i in range(loop):
        merge(i * s, i * s + (s // 2), i * s + s)
    if fragment > 0:
        merge((loop - 1) * s, loop * s, n)
    s = s * 2
print(data, "ソート後のデータ")
