N, M = list(map(int, input().split()))

H = list(map(int, input().split()))

ans = 0
rest = M

for h in H:
    if M >= h:
        M -= h
        ans += 1
    else:
        break

print(ans)