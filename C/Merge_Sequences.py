N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []

for i in range(N):
    C.append((A[i], i))

for i in range(M):
    C.append((B[i], N+i))

C.sort()

ai = [0]*N
bi = [0]*M

for i in range(N+M):
    j = C[i][1]
    if j < N:
        ai[j] = i+1
    else:
        bi[j-N] = i+1

mojiA = ""
for i in range(N):
    mojiA += str(ai[i]) + " "

mojiB = ""
for i in range(M):
    mojiB += str(bi[i]) + " "

print(mojiA)
print(mojiB)