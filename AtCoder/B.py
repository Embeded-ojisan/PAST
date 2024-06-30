def split_string_into_chunks(S, i):
    X = []
    # 文字列をi文字ずつに分割し、配列Xに追加
    for start in range(0, len(S), i):
        X.append(S[start:start + i])
    return X

def collect_ith_characters(X, i):
    result = ''
    for substring in X:
        if len(substring) >= i:
            result += substring[i-1]  # i-1は0インデックスのため
    return result

S, T = list(map(str, input().split()))

if len(T) == 1:
   print("No")
   exit()

for j in range(1, len(S)//len(T)+1):
    # 文字列Sをlen(S)//len(T)文字分ずつ区切る
    X = split_string_into_chunks(S, j)

    # 区切った各要素の先頭から順番にi文字目を連結する
    for i in range(len(S)//len(T)+1):
        result = collect_ith_characters(X, i)
        if result == T:
            print("Yes")
            exit()

print("No")