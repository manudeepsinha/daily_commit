'''
With the yield keyword, we can know it's a generator. It is much 
efficient as it does not store all the values but the current one
and formula to yield next one.
'''

#Below is a simple generator which generates random integers
def rand_num(low,high,n):
    import random
    for x in range(n):
        yield random.randint(low,high)

#driver_code
for num in rand_num(1,10,12):
    print(num)

'''
Or we can do num = rand_num(1,10,12) then print(next(num)) to yield 
the next value. For the last value, if we use next() then it generates
StopIteration error.
''' 