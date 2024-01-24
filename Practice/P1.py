a,b = 0,1
n=10
while a < 10:
    print(a, end = " ")
    a,b = b,a+b


for i in range(10):
    print(i)
    
print(list(range(5,10)))
print(list(range(-10,-100,-30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
    
for num in range(2,10):
    if num%2 ==0:
        print("Even number : " + str(num))
    else:
        print("Odd number : " + str(num))

def prime(number):
    if number <=1 :
        return False
    
    for num in range(2, int(number ** 0.5) + 1):
        if number % num  == 0: 
            return False
        
    return True

for i in range(0,10):
    if prime(i):
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
        
    