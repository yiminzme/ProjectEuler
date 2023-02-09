# please give me a python solution for the following question:

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_twice_square(n):
    return (n % 8 == 7) and (int((n/2)**0.5))**2 == n/2

def odd_composite_sum_of_prime_and_twice_square(n):
    while n < 10000:
        if not is_prime(n) and n % 2 == 1:
            i = 0
            while i < n:
                if is_prime(i) and is_twice_square(n - i):
                    return False
                i += 1
        n += 2
    return True

n = 9
while not odd_composite_sum_of_prime_and_twice_square(n):
    n += 2
print(n)