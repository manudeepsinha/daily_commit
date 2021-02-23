#prints the armstrong numbers for a given range
def isArmstrong(num):
    length = len(str(num))
    temp = num
    numSum = 0
    while temp:
        digit = temp%10
        numSum += digit**length
        temp = temp//10
    if num == numSum:
        return True
    else:
        return False

#driver code:
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
if lower >= 0 and upper > 0 and upper > lower:
    for num in range(lower, upper+1):   #inclusive of upper bound
        if isArmstrong(num):
            print(num, end=' ')
else:
    print("Invalid range.")