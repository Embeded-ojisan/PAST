S = input()

upper = sum(1 for c in S if c.isupper())
lower = sum(1 for c in S if c.islower())

if upper > lower:
    ans = S.upper()
else:
    ans = S.lower()

print(ans)