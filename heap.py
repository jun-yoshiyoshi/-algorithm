data = [1, 2, 4, 5, 3, 6, 8]
n = len(data)
print(data, "元のデータ")

for i in range((n - 1) // 2, -1, -1):
    p = i
    c = p * 2 + 1
    while c < n:
        if c < n - 1 and data[c] < data[c + 1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[p], data[c] = data[c], data[p]

    p = c
    c = p * 2 + 1

print(data, "初期ヒープ")
