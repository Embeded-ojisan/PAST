def sieve(n):
    """
    エラトステネスの篩で 2 から n までの素数を列挙してリストで返す。
    """
    if n < 2:
        return []

    # 0..n の各数が素数かどうかを管理する配列
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # 2 から √n まで調べる
    import math
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if is_prime[i]:
            # i が素数なら、その倍数をすべて合成数にマーク
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # True になっているインデックスが素数
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# 使い方の例
if __name__ == "__main__":
    上限 = 50
    primes_up_to_50 = sieve(上限)
    print(f"{上限} 以下の素数: {primes_up_to_50}")
