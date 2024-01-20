N = int(input())

Power10 = [None]*17
for i in range(17):
    Power10[i] = 10 ** i

R = [ [None] * 10 for i in range(17)]

for i in range(16):
    Digit = (N//Power10[i]) % 10

    for j in range(10):
        if j < Digit:
            R[i][j] = (N//Power10[i+1]+1)*Power10[i]
        if j == Digit:
            R[i][j] = (N//Power10[i+1])*Power10[i] + (N % Power10[i]) + 1
        if j > Digit:
            R[i][j] = (N//Power10[i+1])*Power10[i]

Answer = 0
for i in range(16):
    for j in range(10):
        Answer += j*R[i][j]

print(Answer)