def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

cells = [None]*9

for i in range(3):
    cells[3*i], cells[3*i+1], cells[3*i+2] = list(map(int, input().split()))

rows = [[0, 1, 2],[3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

order = [0]*9

for i in range(9):
    order[i] = i

not_disappoint = 0
all = 0

while True:
    all += 1
    disappoint_flag = False
    for a, b, c in rows:
        if cells[a] == cells[b] and order[a] < order[c] and order[b] < order[c]:
            disappoint_flag = True
        elif cells[a] == cells[c] and order[a] < order[b] and order[c] < order[b]:
            disappoint_flag = True
        elif cells[b] == cells[c] and order[b] < order[a] and order[c] < order[a]:
            disappoint_flag = True

    if disappoint_flag == False:
        not_disappoint += 1

    if not next_permutation(order, 0, 9):
        break

print(not_disappoint)
print(all)
print(not_disappoint/all)