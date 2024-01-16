N = int(input())
A = [0] + list(map(int, input().split()))

result = True
# print(str(A[3]))

if N % 2 > 0:
    while True:
        k = N//2 +1
        check = 0
        for i in range(1, N+1):
            check += 1
            if i <= k:
                if A[i] >= i:
                    continue
                else:
                    result = False
            if k < i:
                if A[i] >= k - i:
                    continue
                else:
                    result = False
        if check == N and result == True:
            break
        else:
            del A[1]
            del A[N]
            N -= 2
else:
    while True:
        k = N//2 +1
        del A[1]

        check = 0
        for i in range(1, N+1):
            check += 1
            if i <= k:
                if A[i] >= i:
                    continue
                else:
                    result = False
            if k < i:
                if A[i] >= k - i:
                    continue
                else:
                    result = False
        if check == N and result == True:
            break
        else:
            del A[1]
            del A[N]
            N -= 2

print(str(k))
