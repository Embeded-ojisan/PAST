N = int(input())

s = 0
check = 1

while check < N:
    if check & N:
        break
    else:
        s += 1
        check = check << 1

print(str(s))