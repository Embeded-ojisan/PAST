i = 0
while i < N:
    j = i
    while j < N and S[j] == S[i]:
        j += 1

    print(S[i], j-1)

    i = j