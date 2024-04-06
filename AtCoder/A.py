N = int(input())

moji = ""
for i in range(1, N+1):
    if i%3 == 0:
        moji += "x"
    else:
        moji += "o"

print(moji)