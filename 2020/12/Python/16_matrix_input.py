x = input('Enter the numbers of the matrix: ')
c = int(input('Enter the number of columns: '))
x = x.split()
matrix = []
r = []
i = 0
#converting user input data in integer to do operations later on
for i in x:
    r.append(int(i))

length = int(len(r)/c)

#loop condition c-1 as last element may end up with more entries (whatever is left after evenly distributing)
while i != c-1:
    
    matrix.append(r[:length])
    del r[:length]
    i += 1

#appending whatever is left in the list r in matrix
matrix.append(r[:])    
print(matrix)