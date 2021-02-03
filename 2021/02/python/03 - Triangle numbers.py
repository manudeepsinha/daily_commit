#triangle numbers WIP question
num = int(input("Enter the number of triangle numbers to print: ")) + 1
i = 0
number = 0
for i in range(1,num):
    number += i
    print(number, end=' ')
