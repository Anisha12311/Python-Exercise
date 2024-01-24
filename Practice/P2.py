from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    
color = Color(input("Enter the color name: "))

match color:
    case Color.RED:
        print("This is red color")
    case Color.GREEN:
        print("This is green")
    case Color.BLUE:
        print("This is blue")
        


class Point:
    __match_args__ = ('x','y')
    def __init__(self, x,y):
        self.x = x
        self.y = y

points = []
points = [Point(2,3)]
match points:
    case []:
        print("No points")
    case [Point(0,0)]:
        print("the origin")
    case [Point(x,y)]:
        print(f"Singe point {x} {y}")
    case _:
        print("Something else")

# Fibonacci Series     
def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end= " ")
        a,b = b, a+b
    print()
    
fib(2000)        

# Default Paramater

def ask_ok(prompt, retries = 4, reminder = 'Please try again'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        elif reply in {'n','no', 'nop', 'nope'}:
            return False
        retries = retries-1
        if retries<0:
            raise ValueError('Invaild use response ')
        print(reminder)

        
ask_ok('Do you really want to quit? : ') 


def arr(a,L = []):
    L.append(a)
    return L

print(arr(1))

#  Arbitrary Argument Lists

def concat(*arg, sep = "/"):
    return sep.join(arg)

print(concat("earth", "moon"))

# lambda

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key = lambda pair : pair[1])
print(pairs)