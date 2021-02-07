#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
#solution in python 2 to practice syntax for TCS

if __name__ == '__main__':
    n = int(raw_input())
    arr = list(map(int, raw_input().strip.split()))
    #applying all the constraints in the if condition
    if n >= 2 and n <= 10 and len(arr) == n and all(x >= -100 and x <= 100 for x in arr):
        arr = sorted(arr,reverse=True)
        num = arr[0]
        for x in arr:
            if x < num:
                break
        print x