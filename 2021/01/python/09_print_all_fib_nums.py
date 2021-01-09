#printing fibonacii sequence using dynamic paradigm
#some refactoring is pending for the outlier cases (reduce if-else cond)
def fib(n):
    f = [0,1]
    
    if n == 0:
        return -1
    
    elif n <= 2:
        if n == 1:
            return f[0]
        else:
            return f
    else:
        for i in range(2,n):
            f.append(f[i-1] + f[i-2])
        return f


num = int(input('How many numbers of Fibonacii sequence you want to print?'))
op = fib(num)
if op == list:
    for i in op:
        print(i, end=' ')
else:
    if op == -1:
        pass
    else:
        print(op)