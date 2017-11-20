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
