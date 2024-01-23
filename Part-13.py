try:
    numerator = int(input("Enter the value to divide : "))
    denominator = int(input("Enter the value by divide : "))
    result = numerator/denominator
except ZeroDivisionError:
    print("You can not divide by 0! Try another number")
except ValueError : 
    print("Enter only number value")
except Exception:
    print("Something went wrong ! ")
    
else: 
    print(result)
    
finally : 
    print("Always run! ")