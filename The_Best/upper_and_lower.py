S = input()

# 入力として受け取った文字の大文字/小文字の数を数える
upper = sum(1 for c in S if c.isupper())
lower = sum(1 for c in S if c.islower())

if upper > lower:
    ans = S.upper()
else:
    ans = S.lower()

print(ans)