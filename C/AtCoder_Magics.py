from functools import cmp_to_key

def compare(i, j):
    if a[i] > a[j]:
        return -1
    elif a[i] < a[j]:
        return 1
    else:
        return 0

N = int(input())

a = []
c = []
iss = []

for i in range(N):
    atemp, ctemp = list(map(int, input().split()))
    a.append(atemp)
    c.append(ctemp)
    iss.append(i)

iss.sort(key=cmp_to_key(compare))

ans = []

for i in iss:
    if len(ans) == 0 or c[ans[-1]] > c[i]:
        ans.append(i)

ans.sort()

for i in range(len(ans)):
    ans[i] += 1

output = " ".join(map(str, ans))

print(len(ans))
print(output)

