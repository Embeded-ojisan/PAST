N = int(input())

t = []

for i in range(N):
    a, c = list(map(int, input().split()))
    t.append((a, c, i+1))

t.sort(reverse=True, key=lambda x: x[0])


i = 0
while i < len(t):
    j = i+1
    while j < len(t):
        if t[i][1] < t[j][1]:
            del t[j]
        j += 1
    i += 1

a = []

for i in range(len(t)):
    a.append(t[i][2])

a.sort()

print(len(a))
moji = ""
for i in range(len(a)):
    moji += str(a[i]) + " "

print(moji)
