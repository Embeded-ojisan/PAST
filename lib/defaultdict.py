from collections import defaultdict

# 例：存在しないキーにアクセスすると、自動で int() の初期値 0 が作られる
count_dict = defaultdict(int)

print(count_dict['apple'])  # キー 'apple' は未登録だが、int() → 0 を生成
count_dict['apple'] += 1
print(count_dict['apple'])  # 1

#以下はdefaultdictの配列のパターン

import sys
input = sys.stdin.readline

from collections import defaultdict

N, Q = list(map(int, input().split()))
dict = [defaultdict(int) for _ in range(N)] 

A = list(map(int, input().split()))

dict[0][A[0]] += 1

for i in range(1, N):
    dict[i].update(dict[i-1])
    dict[i][A[i]] += 1

def is_feasible(x, val, cnt):
    return cnt == dict[x][val]

def bsearch(low, high, val, cnt):
    ans = None

    while low <= high:
        mid = (low + high) // 2
        
        ans = is_feasible(mid, val, cnt)
        if ans:
            low = mid + 1
        else:
            high = mid - 1
    
    return (ans, low)

for _ in range(Q):
    x, k = list(map(int, input().split()))

    flags, ind = bsearch(0, len(A), x, k)
    if flags == True:
        print(ind)
    else:
        print("-1")
