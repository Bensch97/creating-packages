def primes(n):
    prime_nums = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, num)):
            prime_nums.append(num)
    return prime_nums

def is_prime(l):
    for num in range(2, l + 1):
        if all(num % i != 0 for i in range(2, l)):
            return True
        else:
            return False