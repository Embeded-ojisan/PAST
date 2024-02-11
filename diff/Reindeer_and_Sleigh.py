import bisect

n, q = list(map(int, input().split()))

r = list(map(int, input().split()))

r.sort()

sum = [0]*n
sum[0] = r[0]

for i in range(n-1):
    sum[i+1] = sum[i] + r[i+1]

def bsearch(query):
    left = 0
    right = len(r)-1

    while left <= right:
        mid = (left+right)//2
        if sum[mid] == query:
            return mid
        elif sum[mid] < query:
            left = mid+1
        else:
            right = mid-1
    return right

moji = []

for i in range(q):
    query = int(input())
    ans = bisect.bisect_right(sum, query)
    moji.append(ans)

print(r)
print(sum)

for i in moji:
    print(str(i))

