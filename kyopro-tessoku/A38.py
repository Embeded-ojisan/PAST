D, N = map(int, input().split())

L = [None]*N
R = [None]*N
H = [None]*N

LIM = [24] * (D+1)

for i in range(N):
    for j in range(L[i], R[i]+1):
        LIM[j] = min(LIM[j], H[j])

Answer = 0
for i in range(1, D+1):
    Answer += LIM[i]

print(Answer)