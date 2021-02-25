#prints strong numbers for a given range
factorialList = []

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)

for i in range(10):
    factorialList.append(factorial(i))

def isStrong(num):
    numSum = 0
    temp = num
    while temp:
        digit = temp % 10
        numSum += factorialList[digit]
        temp = temp // 10
    
    if numSum == num:
        return True
    else:
        return False

#driver code:
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
if lower >= 0 and upper > 0 and upper > lower:
    for num in range(lower, upper+1):   #inclusive of upper bound
        if isStrong(num):
            print(num, end=' ')
else:
    print("Invalid range.")