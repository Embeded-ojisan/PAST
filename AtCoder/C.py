from itertools import product

def count_valid_combinations(N, M, K, tests):
    count = 0
    
    for combination in product(['o', 'x'], repeat=N):
        valid = True
        for test in tests:
            correct_keys = sum(1 for key in test[1] if combination[key - 1] == 'o')
            if (test[0] == 'o' and correct_keys < K) or (test[0] == 'x' and correct_keys >= K):
                valid = False
                break
        if valid:
            count += 1
    
    return count

N, M, K = map(int, input().split())
tests = []
for _ in range(M):
    C, *keys, result = input().split()
    C = int(C)
    keys = list(map(int, keys))
    tests.append((result, keys))


result = count_valid_combinations(N, M, K, tests)
print(result)
