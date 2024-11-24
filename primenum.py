import math

# Function to check if a number is prime
def is_prime(N):
    if N <= 1:
        return False  # 0 and 1 are not prime numbers
    if N <= 3:
        return True   # 2 and 3 are prime numbers
    if N % 2 == 0 or N % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    # Check divisors from 5 to √N
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

# Main function
def main():
    # Prompt the user to enter an integer
    number = int(input("Enter an integer: "))

    # Check if the number is prime and display the result
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Call the main function to execute the program
if __name__== "__main__":
    main()