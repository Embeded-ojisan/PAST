S = input()
T = input()

def count(s, res):
    res = [0]*27
    for c in s:
        if c == '@':
            res[26] += 1
        else:
            res[ord(c)-ord('a')] += 1
    return res

def solve():
    cs = [0]*27
    ct = [0]*27
    cs = count(S, cs)
    ct = count(T, ct)

    A = "atcoder"
    inA = [False]*26

    for c in A:
        inA[ord(c)-ord('a')] = True

    for i in range(26):
        if inA[i] == False:
            if cs[i] != ct[i]:
                return False
    
    for i in range(26):
        if inA[i] == True:
            if cs[i] < ct[i]:
                cs[26] -= ct[i] - cs[i]
            else:
                cs[26] -= cs[i] - ct[i]

    if cs[26] < 0 or ct[26] < 0:
        return False
    return True

if solve():
    print("Yes")
else:
    print("No")