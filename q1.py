def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    """Return a list of prime numbers between 2 and n."""
    return [x for x in range(2, n+1) if is_prime(x)]

