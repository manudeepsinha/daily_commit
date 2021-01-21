'''The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Note: this code is not tried. 
'''

sum_of_sq = 0
i = 0
sq_of_sum = ((100*(100+1))/2)**2

for i in range(100+1):
	sum_of_sq += i**2
print(sq_of_sum - sum_of_sq)