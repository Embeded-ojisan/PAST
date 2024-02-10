def checker(num, min_num, max_ac, nokori_ac, max_normal, nokori_normal, n):
    for j in range(n):
        if nokori_ac < 0 or nokori_normal < 0:
            return (False, min_num)

        if S[j] == "1":
            if nokori_normal > 0:
                nokori_normal -= 1
            elif nokori_ac > 0:
                nokori_ac -= 1
            else:
                return (False, min_num)
        elif S[j] == "2":
            if nokori_ac > 0:
                nokori_ac -= 1
            else:
                return (False, min_num)
        elif S[j] == "0":
            nokori_ac = max_ac
            nokori_normal = max_normal
    min_num = min(min_num, num)
    return (True, min_num)

N, M = list(map(int, input().split()))

S = input()

min_num = N
CheckResult = False

for i in range(N, -1, -1):
    max_ac = i
    nokori_ac = i

    max_normal = M
    nokori_normal = M

    temp = min_num
    
    (CheckResult, temp) = checker(i, temp, max_ac, nokori_ac, max_normal, nokori_normal, N)
    if CheckResult == False:
        break
    else:
        min_num = temp

print(min_num)