# str.format()
# random

import random
name = "Apexcode"
lastname = "Hub"
number = 1000
print("Hello, my name is {1} {0}".format(name, lastname))
print("Hello, my name is {:^10} {}".format(name, lastname))

print("The number is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:e}".format(number))

list = ["King", "Queen", "Servent"]

randomlist = random.choice(list)

list2 = [1,2,3,4,5,6,7,8,9,"K", "Q", "A"]
random.shuffle(list2)

print(randomlist)
print(list2)




