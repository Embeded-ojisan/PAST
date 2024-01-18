Aorg, Borg = map(int, input().split())
A = Aorg
B = Borg

while A >= 1 and B >= 1:
    if A > B:
        A = A%B
    else:
        B = B%A

if A == 0:
    print(Aorg*Borg//B)
else:
    print(Aorg*Borg//A)