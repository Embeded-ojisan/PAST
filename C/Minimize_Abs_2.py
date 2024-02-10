d = int(input())

ans = d
y = 2*10**6

for x in range(2*10**6):
    while y > 0 and x*x+y*y > d:
        y -= 1
    ans = min(ans, abs(x*x+y*y-d))
    ans = min(ans, abs(x*x+(y+1)*(y+1)-d))

print(ans)