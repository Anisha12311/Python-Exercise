# Duck typing 

class Duck:
    def talk(self):
        print("The duck is talking ")
    def walk(self):
        print("The duck is walking")
class Chicken:
    def talk(self):
        print("The chicken is talking")
    def walk(self):
        print("The chicken is walking")
        
class Person:
    def catch(self,duck):
        duck.talk()
        duck.walk()
        print("The duck is caught")
        
duck = Duck()
chicken = Chicken()

person = Person()
person.catch(chicken)
  