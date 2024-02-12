S = input()

t = ""

for c in S:
    t += c
    if len(t) >= 3 and t[len(t)-3:len(t)] == "ABC":
        t = t.removesuffix("ABC")

print(t)