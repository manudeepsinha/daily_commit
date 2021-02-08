#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_marks = student_marks[query_name]
    print('{0.2f}'.format(sum(query_marks)/len(query_marks)))
    #My attempt (that was long indeed covering the constraints) for reference
    # if n >= 2 and n <= 10 and cond for marks and len of marks array = 3
    '''if query_name in student_marks.keys():
        avg = 0
        for marks in student_marks[query_name]:
            avg += marks
        avg /= 3
        if len(str(avg).split('.')[1]):
            pass
        break
    '''
    