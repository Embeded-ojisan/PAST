A, B, C = list(map(int, input().split()))

WARI = 998244353

D = A*(A+1)//2
E = B*(B+1)//2
F = C*(C+1)//2

ans = (D*E*F)&WARI

print(ans)