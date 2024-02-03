N, D, P = list(map(int, input().split()))
F = [0] + list(map(int, input().split()))

F.sort()

p = P//D
count = 0
Flag = False

for i in range(1, N+1):
    if F[i] >= p:
        count += 1

total = 0
totalplus = 0

pathnum = count//D

if count >= D:
    total = P*(count//D)
    totalplus = total+P

    for i in range(1, N+1-pathnum*D):
        total += F[i]

    for i in range(1, N+1-pathnum*(D+1)):
        totalplus += F[i]

    total = min(total, totalplus)
else:
    total = sum(F)
    totalplus = P

    for i in range(1, N+1-pathnum):
        totalplus += F[i]
    total = min(total, totalplus)

print(str(total))