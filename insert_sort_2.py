import random
n = int(input())
data = [random.randint(1, 99) for _ in range(n)]

for i in range(1, n):
    tmp = data[i]
    j = i
    while j > 0 and data[j - 1] > tmp:
        data[j] = data[j - 1]
        j = j - 1
    data[j] = tmp

print(data, "ソート後のデータ")
