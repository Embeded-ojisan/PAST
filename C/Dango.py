N = int(input())
S = input()

cnt = 0
ans = -1

for i in range(N):
    if S[i] == 'o':
        cnt += 1
    else:
        if cnt > 0:
            ans = max(ans, cnt)
        cnt = 0

if cnt > 0:
    if N-cnt-1 >= 0 and S[N-cnt-1] == '-':
        ans = max(ans, cnt)

print(ans)