def swap_characters(s, i, j):
    # 文字列をリストに変換
    s_list = list(s)
    # 要素を交換
    s_list[i], s_list[j] = s_list[j], s_list[i]
    # リストを文字列に戻す
    return ''.join(s_list)

N = int(input())
S = input()

W = [False]*N
now = False

for i in range(N):
    if S[i] == '"':
        if now != True:
            now = True
        else:
            now = False
        W[i] = True
    else:
        W[i] = now

for i in range(N):
    if W[i] == False and S[i] == ',':
        S = S[0:i] + '.' + S[i+1:len(S)]

print(S)
