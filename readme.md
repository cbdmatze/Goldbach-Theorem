
Goldbach's conjecture is an unproven hypothesis in number theory, first proposed by German mathematician Christian Goldbach in 1742. 

It posits that every even integer greater than 2 can be expressed as the sum of two prime numbers.

For example, 8 = 3 + 5, and 28 = 11 + 7. 

Despite extensive computional verification for large numbers, no formal proof has been found to either confirm or refute the conjecture. 

It remains one of the most famous unsolved problems in mathematics.



_markdown_

Goldbach's theorem

This python program checks if a given number can be expressed as the sum of two prime numbers.

It handles input validation, checks for prime numbers, and finds the appropriate prime pairs if they exist.

The program is structured in a modular and scalable way, breaking tasks into small, dedicated functions across multiple files. 



_installation_
...python3.x



_steps_
1. clone the repository:
'''bash
>>> git clone https://github.com/MatthiasBuettner/Goldbachtheorem.git

2. navigate to the project directory:
>>> cd Goldbach theorem

3. Run the program:
>>> python main.py



_usage_

1.  When prompted, enter a number (> = 4) to check if it can be expressed as     the sum of two primes.

2. The program will either display the prime pair or inform you that the number cannot be expressed as the sum of two primes.



_example_

Enter a number: 10
10 can be expressed as the sum of 3 and 7.


_file_structure_

Goldbachtheorem/

-main.py                # The main script that orchestrates the flow.
-primes.py              # Contains the 'is_prime()' function.
-input_output.py        # Handles user input and output.
-sum_primes.py          # Contains logic for checking if a number is the sum of 
                          two primes.




_license_

This project is licensed under the MIT License. See the LICENSE file for details. 



_contributing_

Feel free to fork this repository, open issues, and submit pull requests. All contributions are welcome!

