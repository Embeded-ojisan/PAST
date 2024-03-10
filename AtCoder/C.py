N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

L = int(input())
C = list(map(int, input().split()))

Q = int(input())
X = list(map(int, input().split()))

def checker(x):
    for a in A:
        for b in B:
            for c in C:
                if a+b+c == x:
                    return "Yes"
    return "No"

for x in X:
    ans = checker(x)
    print(ans)