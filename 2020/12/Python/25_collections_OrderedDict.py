#exploring OrderedDict
from collections import OrderedDict

#unlike dict, OrderedDict keeps a track of order in which the enters are being entered
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
d['h'] = 8
d['i'] = 9
d['j'] = 10

#OrderedDict will retain it's order of inserting elements
for k,v in d.items():
    print (k,v)