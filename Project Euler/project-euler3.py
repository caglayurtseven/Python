# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
n = 600851475143
prime = 0

def checkPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        if checkPrime(i):
            prime=i
print(prime)