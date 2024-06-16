N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 配列AとBを合体して配列Cとする
C = A + B

C.sort()


for i in range(N + M - 1):
    # C[i]が配列Aの中に存在するか否かを見たい場合はin Aを用いる
    if C[i] in A and C[i + 1] in A:
        print("Yes")
        exit()
print("No")