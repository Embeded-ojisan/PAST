T = input()
N = int(input())

A = []
S = []

for i in range(N):
    S.append(list(map(str, input().split())))
    A.append(int(S[i][0]))
    del S[i][0]

ans = 0
t = ""

for i in range(N):
    flag = False
    templen = 0
    tempt = ""
    for a in S[i]:
        if t + a == T[0:(len(t)+len(a))] and templen < len(t)+len(a):
            flag = True
            tempt = t+a
            templen = len(t)+len(a)
    if flag == True:
        ans += 1
        t = tempt
        print(t)

if ans != 0 and t == T:
    print(ans)
else:
    print("-1")