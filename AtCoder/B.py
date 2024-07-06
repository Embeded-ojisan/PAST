a, b, c, d, e, f = list(map(int, input().split()))
g, h, i, j, k, l = list(map(int, input().split()))

ans = "No"

# x軸とy軸
if d < g and e < h:
    ans = "Yes"

if d > g and e > h:
    ans = "Yes"

# y軸とz軸
if e < h and f < i:
    ans = "Yes"

if e > h and f > i:
    ans = "Yes"

# z軸とx軸
if f < i and d < g:
    ans = "Yes"

if f > i and d > g:
    ans = "Yes"

print(ans)