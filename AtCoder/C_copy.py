N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

L = int(input())
C = list(map(int, input().split()))

Q = int(input())
X = list(map(int, input().split()))

ans = []

for i in range(N):
    for j in range(M):
        for k in range(L):
            aaa = A[i]+B[j]+C[k]
            ans.append(aaa)

ans.sort()

def checker(x):
    left = 0
    right = len(ans)-1
    while left <= right:
        mid = (left + right)//2
        if ans[mid] == x:
            print("Yes")
            return
        elif ans[mid] < x:
            left = mid + 1
        else:
            right = mid -1
    print("No")
    return

for x in X:
    checker(x)
