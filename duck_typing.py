#duck typing - concept where the class of an object is less important than the methods /attributes
#the class type is not checked if minimum methods/attributes are present
# "if it walks like a duck, quacks like a duk, then it must be a duck."

class Duck:

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class Chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the meat")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)   #notice that this does not bring an error because duck and chicken\
                        #have the same attributes
print()
person.catch(duck)