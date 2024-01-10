N, K = list(map(int, input().split()))

num = 0

for x in range(1, N+1):
    for y in range(1, N+1):
        z = K-(x+y)
        if 0 < z and z < N+1:
            num += 1

print(str(num))