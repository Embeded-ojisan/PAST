N, Q = map(int, input().split())

S = input()

result = [0]*Q

for q in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    for i in range(l,r):
        if S[i] == "A" and S[i+1] == "C":
            result[q] +=1

for i in range(Q):
    print(result[i])