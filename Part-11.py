def add(*arg):
    sum = 0
    print(arg[1])
    stuff = list(arg)
    stuff[1] = 5
    for i in stuff:
        sum += i
    return sum



def Hello(**kwargs):
    for key, value in kwargs.items():
        return value



print(Hello(first = "Apex", last = "Code"))