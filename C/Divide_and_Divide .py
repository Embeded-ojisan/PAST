N = int(input())

memo = [10**17]*N

def f(x):
    if x == 1:
        return 0
    
    if memo[x] != 10**17:
        return memo[x]
    
    res  f(x/2)+f(x-x/2)+x

    memo[x] = res
    return res

print(str(f(N)))