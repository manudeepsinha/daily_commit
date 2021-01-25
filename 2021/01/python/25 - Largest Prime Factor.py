'''
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def maxPrimeFactors(n):
    
    #setting max prime variable as lowest
    maxPrime = -1
    
    #print the number of 2s that divide n
    while n%2 == 0:
        maxPrime = 2
        n >>= 1		#same as n/= 2
    
    #now checking the possibilities of n as odd
    for i in range(3, int(math.sqrt(n)), 2):
        while n%i == 0:
            maxPrime = i
            n /= i
    #checking the possibility that the number itself being prime and greater than 2
    if n > 2:
        maxPrime = n
        
    return int(maxPrime)

#driver code
num = input("Enter the number: ")
print(maxPrimeFactors(int(num)))