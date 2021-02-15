#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
#refactored answer with new approach (eval)
if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        if cmd != "print":
            args = s[1:]
            cmd +=  '(' + ','.join(args) + ')'
            eval('l.'+cmd)
        
        else:
            print (l)