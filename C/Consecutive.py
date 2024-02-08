n, q = list(map(int, input().split()))

s = input()

l = [0]*q
r = [0]*q

for i in range(q):
    l[i], r[i] = list(map(int, input().split()))

for i in range(n-1):
    if s[i]==s[i+1]:
        a[i] = 1

sum = []*n

for i in range(n):
    sum[i+1] = sum[i] + a[i]

for qi in range(q):
    ans = sum[r[i]-1]-sum[l[i]-1]
    print(str(ans))
