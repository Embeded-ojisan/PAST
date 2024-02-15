S = input()
T = input()

s1 = ord(S[0])
s2 = ord(S[1])

t1 = ord(T[0])
t2 = ord(T[1])

def func(a, b):
    d = abs(a-b)
    return d==2 or d==3

s = func(s1, s2)
t = func(t1, t2)

if s==t:
    print("Yes")
else:
    print("No")