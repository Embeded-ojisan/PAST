n, m = list(map(int, input().split()))

l = list(map(int, input().split()))

wa = 0
ac = 10**15

def f(arg_w):
    line = 0
    rem = 0
    for i in range(n):
        if rem >= l[i]+1:
            rem -= l[i]+1
        else:
            line += 1
            rem = arg_w - l[i]
            if rem < 0:
                return False
    return line <= m

while abs(wa-ac) > 1:
    wj = (wa+ac)//2
    if f(wj)==True:
        ac = wj
    else:
        wa = wj

print(ac)

