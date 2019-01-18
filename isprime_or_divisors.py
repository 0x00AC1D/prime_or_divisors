from itertools import combinations
from functools import reduce
import operator

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not num % 2:
        return False

    for i in range(3, round(num**0.5)+1, 2):
        if not num % i:
            return False
    return True

def prime_factors_readable(num):
    divisors = []
    prime = 2
    while num > 1:
        while not num % prime:
            divisors.append(prime)
            num = num / prime
        prime += 1
    return divisors

def prime_factors_efective(num):
    """2 instructions per iteration faster than above"""
    divisors = []
    while not num % 2:
        divisors.append(2)
        num = num / 2
    prime = 3
    while num > 1:
        while not num % prime:
            divisors.append(prime)
            num = num / prime
        prime += 2
    return divisors

def divisors(prime_factors):
    divisors = list(set(prime_factors))
    for i in range(2, len(prime_factors)):
        divisors.extend([reduce(operator.mul, comb) for comb in set(combinations(prime_factors, i))])
    return sorted(divisors)

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"Besides one and itself, {num} is divisible by {', '.join(map(str, divisors(prime_factors_efective(num))))}.")