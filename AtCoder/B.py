A = []

a = input()
n = 0

while a != '0':
    A.append(a)
    n += 1
    a = input()

moji = ""

print('0')

for i in range(n-1, -1, -1):
    print(A[i])