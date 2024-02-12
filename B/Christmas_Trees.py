A, M, L, R = list(map(int, input().split()))

l = L-A
r = R-A

if l < 0:
    x = -1*l//m+1
    l += x*M
    r += x*M

ans = r//M - (l-1)//M

print(ans)