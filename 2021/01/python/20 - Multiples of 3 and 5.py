'''
https://projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

num = int(input("Enter a number less than 1000: "))
sum = 0
multiples = []
if num <= 1000:
	for i in range(num+1):
		if i%3 == 0 or i%5 == 0:
			sum += i
			multiples.append(i)
	print("The multiples are: ")
	for i in multiples:
		print(i, end = ' ')
	print(f"The sum of these multiples are: {sum}")
else:
	print("Range out of bounds! ")