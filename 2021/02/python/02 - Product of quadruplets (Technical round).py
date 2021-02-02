'''
    The following is a question on mock technical test. The question (paraphrased) goes like this:
    A non-empty array A consisting of N numeric values is given.
    The product of quadruplet (P,Q,R,S) equates to A[P]*A[Q]*A[R]*A[S]  (0<=P<Q<R<S<N).
    For example, array A such that:
    A[0] = -3   A[1] = 1    A[2] = 2    A[3] = -2   A[4] = 5    A[5] = 6    A[6] = 1
    (0,1,2,3), product is -3*1*2*-2 = 12
    (1,2,4,5), product is  1*2*5* 6 = 30
    (2,4,5,6), product is  2*5*6* 1 = 60
    60 is the product of quadruplets (2,4,5,6), which is maximal.

    Your goal is to find the maximal product of any quadruplet for input array A[].
    Write an efficient algorithm for the following assumptions:
    N is an int/float within the range[4..100,000]
'''
num = input("Enter count of values you are going to insert:")
print(f"Enter {num} numbers:")
A = []
for i in range(int(num)):
    temp = float(input())
    if temp < int(num):
        A.append(temp)
while True:
    if int(num) < 4:
        print("Invalid input")
        break
    maxProd = 1
    A.sort()
    for i in range(4):
        maxProd *= A[::-1][i]
    print(maxProd)
    break