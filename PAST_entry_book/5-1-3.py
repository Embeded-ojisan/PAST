N = int(input())

S = [list(input()) for _ in range(N)]

for I in range(N-2, -1, -1):
    for J in range(1, 2*N-3):
        if S[I][J] == '#' and (S[I+1][J-1] == 'X' or S[I+1][J] == 'X' or S[I+1][J+1] == 'X'):
            S[I][J] = 'X'
        
for i in range(0, N):
    print(''.join(S[i]))