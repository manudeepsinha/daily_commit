#exploring defaultdict
from collections import defaultdict

#making d as defaultdict and passing object that will assign default value (here 0) to unknown key instead
#of throwing KeyError
d = defaultdict(lambda:0)

#now assigning some values in the defaultdict
d['one'] = 1
d['two'] = 2

#now printing keys and values present in d
print('Printing keys currently present in the defaultdict.')
for key in d:
    print(key)
print('\n\nPrinting values currently present in the defaultdict.')
for values in d.values():
    print(values)

#now calling unknown key and it'll assign the default to that key
print('\n\nNow calling an unknown keys zero and three')
print(d['zero'])
print(d['three'])

#now printing keys and values present in d
print('\n\nPrinting keys now present in the defaultdict.')
for key in d:
    print(key)
print('\n\nPrinting values currently present in the defaultdict.')
for values in d.values():
    print(values)