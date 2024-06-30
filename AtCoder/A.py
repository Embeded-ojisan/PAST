S = input()

ansM = 0
ansR = 0

for i in range(len(S)):
    if S[i] == 'R':
        ansR = i
    elif S[i] == 'M':
        ansM = i

if ansR < ansM:
    print("Yes")
else:
    print("No")