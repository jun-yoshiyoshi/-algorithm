key = int(input())

data = [57, 49, 28, 546, 44, 29, 98, 75, 38, 3, 2, 57]
n = len(data)

flg = False

for i in range(n):
    if data[i] == key:
        print("data[{}]が{}です。".format(i, key))
        flg = True
        break

if flg == False:
    print(str(key)+"は存在しません")
