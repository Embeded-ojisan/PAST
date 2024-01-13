R, B = list(map(int, input().split()))
x, y = list(map(int, input().split()))

def check(x):
    r = R-x
    b = B-x

    if r < 0 or b > 0:
        return False
    
    num = r//(X-1)+b//(y-1)
    return (num>=x)

ok = 0
ng = 10**18 + 1

while abs(ok-ng)>1:
    mid = (ok+ng)//2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)