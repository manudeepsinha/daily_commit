#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
''' 1/2 test cases fail.
    Failed test case:
                        29
                        append 1
                        append 6
                        append 10
                        append 8
                        append 9
                        append 2
                        append 12
                        append 7
                        append 3
                        append 5
                        insert 8 66
                        insert 1 30
                        insert 6 75
                        insert 4 44
                        insert 9 67
                        insert 2 44
                        insert 9 21
                        insert 8 87
                        insert 1 75
                        insert 1 48
                        print
                        reverse
                        print
                        sort
                        print
                        append 2
                        append 5
                        remove 2
                        print

    Expected o/p        [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
                        [5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
                        [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
                        [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]

    My o/p              Wrong ans
'''
if __name__ == '__main__':
    N = int(input())
    lst = []
    while N != 0:
        action = input().split()
        if not in 'insertprintremoveappendsortpopreverse':
            break
        else:
            if action [0] == 'insert':
                lst.insert(int(action[1]),int(action[2]))
            
            elif action [0] == 'print':
                print(lst)
            
            elif action [0] == 'remove':
                lst.remove(int(action[1]))
            
            elif action [0] == 'append':
                lst.append(int(action[1]))
            
            elif action [0] == 'sort':
                lst.sort()
            
            elif action [0] == 'pop':
                lst.pop()
            
            else:
                lst = sorted(lst,reverse = True)
            N -= 1