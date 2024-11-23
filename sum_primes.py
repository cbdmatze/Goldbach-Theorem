from primes import is_prime

def find_prime_pairs(number):
    """Find two primes that sum up to the number."""
    for i in range(2, number // 2 + 1):
        if is_prime(i):
            complement = number - i
            if is_prime(complement):
                return i, complement
    return None, None


def can_be_sum_of_two_primes(number):
    """Check if a number can be expressed as the sum of two primes."""
    prime1, prime2 = find_prime_pairs(number)
    if prime1 and prime2:
        return prime1, prime2
    return None
