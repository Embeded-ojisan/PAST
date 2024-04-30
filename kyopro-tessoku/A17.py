N = int(input())
A = [0] + [0] + list(map(int, input().split()))
B = [0] + [0] + [0] + list(map(int, input().split()))

dp = [0] * 100009
dp[1] = 0
dp[2] = A[2]

for i in range(3, N+1):
    dp[i] = min(dp[i-1] + A[i], dp[i-2] + B[i])

Answer = []

Place = N
while True:
    Answer.append(Place)
    if Place == 1:
        break
    if dp[Place-1]+A[Place] == dp[Place]:
        Place = Place - 1
    else:
        Place = Place - 2

Answer.reverse()

moji = ""

print(len(Answer))

for i in Answer:
    moji += str(i) + " "

print(moji)