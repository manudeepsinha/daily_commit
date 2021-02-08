#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
from operator import itemgetter
records = []
n = int(raw_input())
if n >= 2 or n <= 5:
    for _ in range(n):
        rec = []
        name = raw_input()
        score = float(raw_input())
        rec.append(name)
        rec.append(score)
        records.append(rec)
    records = sorted(records, key = itemgetter(1,0))
	maxNum = records[0][1]
	while records[0][1] == maxNum:
	    records.pop(0)
	maxNum = records[0][1]
	i = 0
	for i in range(len(records)):
	    if maxNum == records[i][1]:
	        print records[i][0]