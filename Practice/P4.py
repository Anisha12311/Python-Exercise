import math

q = 'Ani'
l = 'sha'
print(f'this is the pi value {math.pi:.3f}')

print('this is the first value {0}{1}'.format(q,l))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, age in table.items():
    print(f'{name:10}===>{age:10d}')
    
    
bugs = 'roaches'
value = 3443
area = 'living room'

print(f'Debugging {bugs=} {value=} {area=}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}'.format(table))
print('Dcab: {0[Dcab]:d}'.format(table))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    
    
import json

x = [1,'simple']
print(json.dumps(x))


try:
    raise Exception('spam', 'egg')
except Exception as inst:
    print("Start")
    print(type(inst))
    print(inst.args)
    print("heelooo")
    x,y = inst.args
    print("X", x)
    print("Y", y)
    
    