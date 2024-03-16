# 配列の中身のprintの仕方

N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (N+1)
ans = []

for i in range(3*N):
    cnt[A[i]] += 1
    if cnt[A[i]] == 2:
        ans.append(A[i])

moji = ""

# 配列の中身のprintの仕方
print(*ans)