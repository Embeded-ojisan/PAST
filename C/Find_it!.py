N = int(input())
A = [0] + list(map(int, input().split()))

id = [0] * (N+1)

k = 1
v = 1

while id[v] == 0:
    id[v] = k
    k += 1
    v = A[v]

ans = []

length = k-id[v]

for i in range(length):
    ans.append(v)
    v = A[v]

print(str(len(ans)))

moji = ""
for v in ans:
    moji += str(v) + ' '

print(moji)