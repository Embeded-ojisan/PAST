# 文字列の削除(削除した後、文字列を戻り値として返すので注意)

S = input()

t = ""

for c in S:
    t += c
    if len(t) >= 3 and t[len(t)-3:len(t)] == "ABC":
        # 削除した文字列を戻り値として返すので注意
        t = t.removesuffix("ABC")

print(t)