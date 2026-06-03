def is_prime(n):
    if n < 2:          # 0 and 1 are not prime numbers, so return False
        return False
    for i in range(2, n):    # check every number from 2 to n-1
        if n % i == 0:       # if n is divisible by i (no remainder), it's not prime
            return False     # found a factor, so return False immediately
    return True              # no factors found, so n is prime

print(is_prime(73))  # True
print(is_prime(75))  # False