N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

temp = A[0]
ans = A[0]

for i in range(N):
    if A[i] != temp:
        ans = A[i]
        break

print(ans)