# inheritance   
class Animal: 
    Alive = True
    
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping  ")
        
class Rabbit(Animal):
    def run(self):
        print("Rabbit is very small")
class Mouse(Animal):
    pass
class Camel(Animal) :
    pass


rabbit = Rabbit()
mouse = Mouse()
camel = Camel()
rabbit.eat()
rabbit.run()
print(camel.Alive)


class Dog(Animal) :
    def bark(self):
        print("Dog is barking")

class Goat(Dog):
    def grass(self):
        print("The goat is eating grass")
        
        
goat = Goat()
