key = int(input())
data = [57, 49, 28, 546, 44, 29, 98, 75, 38, 3, 2, 57]
n = len(data)
flg = False
i = 0
while i < n:
    if data[i] == key:
        print("data[{}]が{}です".format(i, key))
        flg = True
        break
    else:
        i += 1
if flg is False:
    print(f"{key}は存在しません")
