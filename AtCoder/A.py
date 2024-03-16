import sys

S = input()

ans = 0

if S[0] != '<' or S[len(S)-1] != '>':
    print("No")
    sys.exit()
else:
    for i in range(1, len(S)-1):
        if S[i] != '=':
            print("No")
            sys.exit()

print("Yes")
