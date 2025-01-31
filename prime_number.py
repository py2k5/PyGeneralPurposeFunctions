##print all the prime numbers till a given number

n = int(input("Enter a number:"))

def prime_num(num):
    for n in range(2, num):
        for x in range(2, n):
            print("current n is {} and x is {}".format(n,x))
            if n % x == 0:
                print( n, 'equals', x, '*', n/x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

prime_num(n)


##optimal version

import math

def prime_num(num):
    if num < 2:
        return  # No prime numbers less than 2

    print(2, "is a prime number")  # 2 is the only even prime number

    for n in range(3, num + 1, 2):  # Check only odd numbers
        is_prime = True
        #If n is not divisible by any number up to its square root, it is prime. This reduces the number of iterations significantly.
        for x in range(3, int(math.sqrt(n)) + 1, 2):  # Check divisibility up to sqrt(n)
            if n % x == 0:
                is_prime = False
                break
        if is_prime:
            print(n, "is a prime number")

# Example usage
prime_num(20)
