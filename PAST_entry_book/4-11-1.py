

S = input()

na = 0
nb = 0
nc = 0

na = S.count("a")
nb = S.count("b")
nc = S.count("c")

mx = max(na, nb, nc)

if na == mx:
    print("a")
elif nb == mx:
    print("b")
elif nc == mx:
    print("c")