N, L, R = list(map(int, input().split()))

A = []

for i in range(1, N+1):
    A.append(i)

# 配列の要素L-1から要素Rを逆順に変更
A[L-1:R] = A[L-1:R][::-1]

output = ' '.join(map(str, A))

print(output)