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

