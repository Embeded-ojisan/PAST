N = int(input())

d = []

total = 0

for i in range(N):
    s, c = list(input().split())

    c = int(c)

    total += c

    # 配列の末尾にタプルを追加
    d.append((s, c))

# タプルの配列のソート方法(index 0でソート)
d.sort(key=lambda x: x[0])

ans = total % N

# タプルの配列の特定の要素へのアクセス方法
print(d[ans][0])

