N, K = map(int, input().split())

k = K - 2*(N-1)

if k%2 == 0:
    print("Yes")
else:
    print("No")