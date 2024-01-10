D = int(input())

N = int(input())

Total = [0] * D

for i in range(N):
    L, R = list(map(int, input().split()))
    for j in range(L, R+1):
        Total[j-1] += 1

for t in Total:
    print(str(t))