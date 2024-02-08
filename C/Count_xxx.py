def rle(s):
    tmp, count, ans = s[0], 1, ""
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans += tmp+str(count)
            tmp = s[i]
            count = 1
    ans += tmp+str(count)
    return ans

N = int(input())
S = input()

s = rle(S)

mx = [0]*26

for len in range(len(s)//2):
    mx[ord(s[2*len]) - ord('a')] = max(mx[ord(s[2*len]) - ord('a')], int(s[2*len+1]))

ans = 0
for len in mx:
    ans += len

print(str(ans))