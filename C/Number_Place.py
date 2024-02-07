import sys

def FirstCheck():
    for i in range(9):
        C = [False]*10
        for j in range(9):
            if C[A[i][j]] == True:
                return False
            else:
                C[A[i][j]] = True
    return True

def SecondCheck():
    for i in range(9):
        C = [False]*10
        for j in range(9):
            if C[A[j][i]] == True:
                return False
            else:
                C[A[j][i]] = True
    return True

def ThirdCheck():
    for i in range(3):

        for j in range(3):
            
            C = [False]*10

            for k in range(3):

                for l in range(3):
                    if C[A[k+3*i][l+3*j]] == True:
                        return False
                    else:
                        C[A[k+3*i][l+3*j]] = True
    return True

A = []

for i in range(9):
    A.append(list(map(int, input().split())))

CheckResult = False

# 1つ目の条件のチェック
CheckResult = FirstCheck()
if CheckResult == False:
    print("No")
    sys.exit()

# 2つめの条件のチェック
CheckResult = SecondCheck()
if CheckResult == False:
    print("No")
    sys.exit()

# 3つめの条件チェック
CheckResult = ThirdCheck()
if CheckResult == False:
    print("No")
    sys.exit()

print("Yes")