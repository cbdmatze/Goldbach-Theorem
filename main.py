from input_output import get_input, print_result
from sum_primes import can_be_sum_of_two_primes

def main():
    """Main function to run the program"""
    number = get_input()
    result = can_be_sum_of_two_primes(number)
    print_result(number, result)


if __name__ == "__main__":
    main()
