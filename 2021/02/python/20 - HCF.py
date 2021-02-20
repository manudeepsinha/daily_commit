#HCF code
#pending: error and exception handling
def hcf(small,big):
    ans = []
    for i in range (1, small + 1):
        if (small % i == 0) and (big % i == 0):
            ans.append(i)
    return max(ans)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 < num2:
    print(f'HCF of numbers {num1} and {num2} is: {hcf(num1,num2)}')
else:
    print(f'HCF of numbers {num1} and {num2} is: {hcf(num2,num1)}')