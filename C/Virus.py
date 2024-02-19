N, D = list(map(int, input().split()))

X = []
Y = []

for i in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

def near(a, b):
    dx = X[a] - X[b]
    dy = X[a] - X[b]
    return dx*dx+dy*dy <= D*D

ans = [False]*N
q = []

ans[0] = True
q.append(0)

while len(q) != 0:
    v = q.pop(0)
    for u in range(N):
        if near(v, u)==True:
            if ans[u]:
                continue
            ans[u] = True
            q.append(u)

for i in range(N):
    if ans[i] == True:
        print("Yes")
    else:
        print("No")
