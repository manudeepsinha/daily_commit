'''
    The following is a question on mock technical test. The question goes like this:
    A marathod is a long-distance rance with an official distance of 42.195 kilometers (26 miles 385 yards), usually
    run as a road race or footrace.
    A local marathon was organized at Bavdhan, Pune. The distance actually covered by the participants has been recorded
    in an array R[] which is an integer array holding the values in kilometers. If there are N number of participants who
    started running at a particular time, then the size of R is N. The participants should cover a distance more than 
    0.0 km to get recorded in array R[].
    Find the max distances covered by 3 highest racers excluding finishers. If there are only 1 or 2 racers excluding
    finishers, give their distances covered. R[] will be input float array. Write the code to take input array R[], 
    and return 3 maximum distances excluding finishing distances d, d=42.195km
'''
R = []
highest = []
d = 42.195
off = False
print("Enter the distances covered by racers in Marathon (Kilometers) please\n(press q to terminate):")
while (True):
    i = input()
    if i == 'q':
        break
    else:
        flt_i = float(i)
        if (flt_i =< 0.0 or flt_i > d):
            print("Invalid input")
            off = True
            break
        R.append(flt_i)
if not off:
    for i in range(len(R)):
        if R[i] != d:
            highest.append(R[i])
    highest.sort()
    print("Highest Distance excluding finishers:")
    if len(highest) >= 3:
        print(highest[::-1][:3])
    else:
        print(highest)