import time

for i  in range(10):
    print(i+1, "Good morning")
    
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)

print("Good morning")

# nested loop

rows = int(input("How many rows ? : "))
columns = int(input("How many columns ? : "))
symbol = input("What was the symbol? : ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()