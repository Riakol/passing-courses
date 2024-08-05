def checker(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def primes(left, right):
    all_primes = checker(right)
    output = [i for i in all_primes if left <= i <= right]
    for x in output:
        yield x

