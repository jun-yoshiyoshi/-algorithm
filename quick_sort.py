import random
n = int(input())
data = [random.randint(1, 99) for _ in range(n)]
print(data, "元のデータ")


def quick_sort(le, ri):
    i, j = le, ri
    p = data[(le+ri)//2]
    while True:
        while data[i] < p:
            i += 1
        while data[j] > p:
            j -= 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1
    if le < i - 1:
        quick_sort(le, i - 1)
    if ri > j + 1:
        quick_sort(j + 1, ri)


quick_sort(0, n - 1)
print(data, "ソート後のデータ")
