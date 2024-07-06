a, b, c, d, e, f = list(map(int, input().split()))
g, h, i, j, k, l = list(map(int, input().split()))

ans = "Yes"

if d <= g or e <= h or f <= i:
    ans = "No"
elif j <= a or k <= b or l <= c:
    ans = "No"

print(ans)