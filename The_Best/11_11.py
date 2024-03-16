# ゾロ目の解法

def check(a, b):
    s = str(a) + str(b)
    s = sorted(s)
    return s[0] == s[len(s)-1]

N = int(input())

D = [0] + list(map(int, input().split()))

ans = 0

for i in range(1, N+1):
    for j in range(D[i]):
        day = str(j)
        month = str(i)
        if check(i, j) == True:
            ans += 1

print(ans)