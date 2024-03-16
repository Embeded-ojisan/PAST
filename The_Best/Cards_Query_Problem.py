# 空の配列の定義方法 & set型の使い方

N = int(input())
Q = int(input())

q = []

# []*Nだとダメ
cards = [[] for _ in range(N)]

# ただの{}だとdict型だと処理される
boxes = [set() for _ in range(200001)]

for qi in range(Q):
    qtemp = list(map(int, input().split()))
    
    if qtemp[0] == 1:
        cards[qtemp[2]].append(qtemp[1])
        boxes[qtemp[1]].add(qtemp[2])

    if qtemp[0] == 2:
        cards[qtemp[1]].sort()
        print(*cards[qtemp[1]])

    if qtemp[0] == 3:
        print(*boxes[qtemp[1]])