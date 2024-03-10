S = input()

flag = False
A = []

for i in range(len(S)):
    if S[i] == '|':
        A.append(i)

moji = S[0:A[0]] + S[A[1]+1:len(S)]

print(moji)