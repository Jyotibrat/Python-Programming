# Program to print first n prime numbers

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to print the first n prime numbers
def print_first_n_primes(n):
    count = 0  # Counter for prime numbers
    num = 2  # Starting number to check for primes
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

# Input: Number of primes to print
n = int(input("Enter the number of prime numbers to print: "))
print_first_n_primes(n)