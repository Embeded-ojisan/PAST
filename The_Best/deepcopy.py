import copy

def print_matrix_without_spaces(matrix):
    for row in matrix:
        print(''.join(map(str, row)))

N = int(input())

A = []

for i in range(N):
    a = input()
    A.append([int(char) for char in a])


# ここでB=AやB=A.copy()としてしまうと参照を渡してしまう
B = copy.deepcopy(A)

for i in range(0, N-1):
    B[0][i+1] = A[0][i]
    B[i+1][N-1] = A[i][N-1]
    B[N-1][N-i-2] = A[N-1][N-i-1]
    B[N-i-2][0] = A[N-i-1][0]

print_matrix_without_spaces(B)