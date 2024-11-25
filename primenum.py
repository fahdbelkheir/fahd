import math


def is_prime(N):
    if N <= 1:
        return False  
    if N <= 3:
        return True   
    if N % 2 == 0 or N % 3 == 0:
        return False  

    
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    
    number = int(input("Enter an integer: "))

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__== "__main__":
    main()