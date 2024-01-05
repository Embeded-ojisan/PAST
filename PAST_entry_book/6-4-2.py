

N, L = list(map(int, input().split()))

# Xはハードルのある座標xの配列
X = list(map(int, input().split()))


T1, T2, T3 = list(map(int, input().split()))

# Hはハードルがある座標xにおいてTrueとなる配列
H = [False]*(L+1)

for x in X:
    H[X] = True

# costは座標iで行動を終了し、もしハードルがあれば処理し終わった時の、それまでの所要時間の最小値
cost = [10*100]*(L+1)

cost[0] = 0

for i in range(1, L+1):

    # ここで場合分けしたうえでiにおいて値の一番小さい値をcostに代入しようとしている
    ## 素朴に書くと場合分けしてコードを書くと行数が長くなるため以下のように順繰りにminする実装としている
    
    ### 行動1
    cost[i] = min(cost[i], cost[i-1]+T1)

    ### 行動2
    if i >= 2:
        cost[i] = min(cost[i], cost[i-2] + T1 + T2)

    ### 行動3
    if i >= 4:
        cost[i] = min(cost[i], cost[i-4]+T1+3*T2)

    ### もしハードルがあれば加算
    if H[i]:
        cost[i] += T3

# 初期値をセット
ans = cost[L]

for i in [L-3, L-2, L-1]:
    if i >= 0:
        ans = min(ans, cost[i]+T1/2+T2*(2*(L-i)-1)//2)

print(ans)