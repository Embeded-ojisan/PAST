def ham(s, t):
    if len(s) != len(t):
        return 999
    res = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            res += 1
    return res

def f(s, t):
    if len(s) != len(t)+1:
        return False
    si = 0
    for ti in range(len(t)):
        while si < len(s) and s[si] != t[ti]:
            si += 1
        if si == len(s):
            return False
        si += 1
    return True

N, T = list(map(str, input().split()))

N = int(N)

S = []
ans = []

for i in range(N):
    S=input()
    ok = False
    if len(S)+1>=len(T):
        if f(S, T)==True:
            ok = True
        if f(T, S)==True:
            ok = True
        if ham(S, T) <= 1:
            ok = True
    if ok==True:
        ans.append(i+1)

moji = ""

print(str(len(ans)))
for i in ans:
    moji += str(i) + " "

print(moji)
