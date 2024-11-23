def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


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


def print_result(number, result):
    """Print the result based on weather the number
    can be expressed as the sum of two primes."""
    if result:
        prime1, prime2 = result
        print(f"{number} can be espressed as the sum of {prime1} and {prime2}.")
    else:
        print(f"{number} cannot be expressed as the sum of two pries.")

def main():
    """Main function to run the program"""
    number = get_input()
    result = can_be_sum_of_two_primes(number)
    print_result(number, result)


if __name__ == "__main__":
    main()
