# walrus operator

# foods = list()

# while food := input('What food do you like? : ') != "quit":
#     foods.append(food)


# Higer order function

def Upper(text):
    return text.upper()
def Lower(text):
    return text.lower()

def Hello(fun):
    text = fun("Hello")
    print(text)

Hello(Upper)

# lambda function

double = lambda x:x*2
age = lambda age : True if age>=18 else False
print(double(3))
print(age(19))

# sort method

students = ['Ani','tsms', 'son']
students_1 = ('Ani','tsms', 'son')
sortS = sorted(students_1,reverse=True)


allstudent = [('Ani',21,'A'),('tsms',22,'D'),('Son',24,'B')]

# students.sort()

grades = lambda grade : grade[2]
allstudent.sort(key=grades)

for i in allstudent:
    print(i)