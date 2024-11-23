def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime_pairs(number):
    """Find all pairs of primes that sum up to the given number."""
    prime_pairs = []
    for i in range(2, number // 2 + 1):
        if is_prime(i):
            complement = number - i
            if is_prime(complement):
                prime_pairs.append((i, complement))
    return prime_pairs


def can_be_sum_of_two_primes(number):
    """Check if a number can be expressed as the sum of two primes.
    
    Returns all possible pairs of primes.
    """
    return find_prime_pairs(number)


def get_input():
    """Handle user input with validation."""
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 4:
                print("Number must be greater or equal to 4.")
            else:
                return number
        except ValueError:
            print("Invalid input, please enter a valid integer.")


def print_result(number, results):
    """Print the result based on whether the number can be expressed 
    as the sum of two primes."""
    if results:
        print(f"{number} can be expressed as the sum of:")
        for prime1, prime2 in results:
            print(f" - {prime1} and {prime2}")
    else:
        print(f"{number} cannot be expressed as the sum of two primes.")


def main():
    """Main function to run the program."""
    number = get_input()
    results = can_be_sum_of_two_primes(number)
    print_result(number, results)


if __name__ == "__main__":
    main()
