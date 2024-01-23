age = int(input("How old are you ? : "))

if age == 100:
    print("You are old man")
elif age>18:
    print("You are adult ")

elif age < 0:
    print("You are not born yet")
else:
    print("You are a child")
    
    
temp= int(input("What's the temperature  outside?: "))

if temp > 0 and temp<=30:
    print("The temp is good")
elif temp < 0 or temp >=40:
    print("The temp is bad")
else:
    print("The temp is moderate")


name = ""
while len(name) == 0:
    name = input("Enter the name : ")
print(name)
