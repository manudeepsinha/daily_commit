#LCM code
#pending: error and exception handling
def lcm(small,big):
    ans = big
    while True:
        if (ans % small == 0) and (ans % big == 0):
            return ans
        ans += 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 < num2:
    print(f'LCM of numbers {num1} and {num2} is: {lcm(num1,num2)}')
else:
    print(f'LCM of numbers {num1} and {num2} is: {lcm(num2,num1)}')