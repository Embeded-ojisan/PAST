import sys

B = int(input())

ans = 1

while ans**ans <= B:
    if ans**ans == B:
        print(ans)
        sys.exit()
    ans += 1

print("-1")