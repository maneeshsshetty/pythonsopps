import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
even_numbers = [x for x in range(1, 101) if x % 2 == 0]
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
prime_numbers = [x for x in range(1, 101) if is_prime(x)]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Prime numbers:", prime_numbers)
