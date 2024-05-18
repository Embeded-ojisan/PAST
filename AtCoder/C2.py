N = int(input())

t = []

for i in range(N):
    a, c = list(map(int, input().split()))
    t.append((a, c, i+1))

i = 0
while i < len(t):
    j = 0
    while j < len(t) and i < len(t):
        if t[i][1] < t[j][1] and t[i][0] > t[j][0]:
            del t[j]
        j += 1
    i += 1


print(len(t))
moji = ""
for i in range(len(t)):
    moji += str(t[i][2]) + " "

print(moji)
