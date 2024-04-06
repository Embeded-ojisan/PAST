N = int(input())

a = []
c = []

d = {}

for i in range(N):
    atemp, ctemp = list(map(int, input().split()))

    if ctemp in d:
        dtemp = d[ctemp]
        if dtemp > atemp:
            d[ctemp] = atemp
    else:
        d[ctemp] = atemp

min_iter = 10**9 + 1
min_value = 0
for key, value in d.items():
    if min_value < value:
        min_value = value
        min_iter = key

print(min_value)