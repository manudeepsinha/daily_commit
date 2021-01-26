'''
	https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def isPrime(num):
	if num < 2: return "Neither Prime nor Composite"

	for i in range(2, int(num*0.5)+1):		#this is the logic that reduces the time excessively
		if n % i == 0:
			return False
		return True

sum = 0
for i in range(2,2000000):
	if isPrime(i):
		sum += 1

print(sum)	#142913828922