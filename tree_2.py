#left = 0
#right = 1
data = 2
node = [[1, 2, 10], [3, 4, 20], [5, None, 30], [None, None, 40], [
    6, 7, 50], [None, None, 60], [None, None, 70], [None, None, 80]]
MAX = len(node)

print("指定の番号のノードを調べます")
print("入力せずにEnterを押すと終了")

while True:
    s = input("number=")
    if s == "":
        break
    try:
        n = int(s)
    except:
        print("数値を入力してください")
        continue
    if 0 <= n and n < MAX:
        print("node{}の値は{}".format(n, node[n][data]))
