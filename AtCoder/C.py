import sys

def swap_characters(s, i, j):
    # 文字列をリストに変換
    s_list = list(s)
    # 要素を交換
    s_list[i], s_list[j] = s_list[j], s_list[i]
    # リストを文字列に戻す
    return ''.join(s_list)

S = input()

l = len(S)

dict = {}

flag = False

for i in range(l):
    for j in range(i+1, l):
        if S[i] != S[j]:
            index = swap_characters(S, i, j)
            getv = dict.get(index, 0)
            dict[index] = getv + 1
        else:
            flag = True

if flag == True:
    print(str(len(dict)+1))
else:
    print(len(dict))
