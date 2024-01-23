class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
    def drive(self) : 
        print("I am driving the car")
    def stop(self):
        print("I stopped the car")
    
car_1 = Car("Corvette", "Pink", "2022")

print(car_1.model)

car_1.drive()