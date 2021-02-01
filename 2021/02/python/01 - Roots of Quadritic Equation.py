'''
    A similar type of question encountered in HackerEarth's Codearena where have to find whether given equation has real roots.
    This function takes three coeff as arguments and the prints root of the equation.
'''
import math

def findRoots (a,b,c):

    #calculation discriminent using the formula
    dis = (b * b) - (4 * a * c)

    sqrt_val = math.sqrt(abs(dis))

    #checking the conditions of disciminent
    if dis > 0:
        print('Real and different roots.')
        print((-b + sqrt_val)/(2*a))
        print((-b - sqrt_val)/(2*a))

    elif dis == 0:
        print('Real and same roots.')
        print(-b / (2*a))

    else:
        print('Complex roots.')
        print(-b / (2*a) , " + i", sqrt_val)
        print(-b / (2*a) , " - i", sqrt_val)

#driver code
coef = int(input().split())
if len(coef) == 3:
    if coef[0] == 0:
        print('Incorrect input for quadritic equation.')
    else:
        findRoots(int(coef[0]), int(coef[1]), int(coef[2]))
else:
    print('Enter correct number of coefficients.') 