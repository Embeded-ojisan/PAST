A = list(map(int,input().split()))
B = list(map(int,input().split()))

atotal = sum(A)
btotal = sum(B)

diff = atotal-btotal+1

print(diff)