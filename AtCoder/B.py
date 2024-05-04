S = input()
T = input()

num = len(S)
numT = len(T)

moji = ""
temp = 0

i = 0

while i < num:
#    idx = T.find(S[i], temp, numT)
    for j in range(temp, numT):
        if S[i] == T[j]:
            idx = j
            break
    temp = idx + 1
    i += 1
    moji += str(idx+1) + " "

print(moji)