import random
n = int(input())
data = [random.randint(1, 99) for _ in range(n)]
print(data, "元のデータ")

for i in range(n - 1):
    for j in range(n - 1, i, -1):
        if data[j - 1] > data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]

print(data)
