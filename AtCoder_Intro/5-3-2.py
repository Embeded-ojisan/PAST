N = int(input())
M = 101

D = [False]*M

for _ in range(N):
    temp = int(input())
    D[temp] = True

num = 0

for d in D:
    if d == True:
        num += 1

print(num)