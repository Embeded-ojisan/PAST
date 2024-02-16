import sys
import copy

class Sheet:
    def __init__(self):
        self.h = 0
        self.w = 0
        self.s = ""

    def input(self):
        h, w = list(map(int, input().split()))
        self.h = h
        self.w = w
        self.s = [[] for _ in range(h)]
        for i in range(self.h):
            self.s[i]=input()

    def clear(self):
        for i in range(self.h):
            moji = ''
            for j in range(self.w):
                moji += '.'
            self.s[i] = moji

    def copy(self, a, di, dj):
        for i in range(a.h):
            for j in range(a.w):
                if a.s[i][j] == '.':
                    continue
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= self.h or nj < 0 or nj >= self.w:
                    return False
                self.s[ni] = self.s[ni][0:nj-1] + a.s[i][j] + self.s[ni][nj+1:self.h]
        return True

a = Sheet()
b = Sheet()
x = Sheet()

a.input()
b.input()
x.input()

for ai in range(-1*a.h, x.h):
    for aj in range(-1*a.w, x.w):
        for bi in range(-1*b.h, x.h):
            for bj in range(-1*b.w, x.w):
                y = copy.deepcopy(x)
                y.clear()
                if y.copy(a, ai, aj) == False:
                    continue
                if y.copy(b, bi, bj) == False:
                    continue
                if x.s == y.s:
                    print("Yes")
                    sys.exit()

print(y.s)
print("No")