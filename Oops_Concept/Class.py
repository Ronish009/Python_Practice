from html.entities import name2codepoint


class Student:
    city="ronish"
    def __init__(self,name="Unknown",age=0):
        self.name=name
        self.age=age
    def print(self):
        print("Name:, Age:, City: ",self.name, self.age, self.city)
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city} " )


class Aclass:
    # def __init__(self,name="Unknown"):
    #     self.name=name

    def __init__(self,name):
        self.name=name
        print("A Constructer")

    def print(self):
        print(f"Welcome {self.name}")

class Bclass(Aclass):
    def __init__(self,name):
        super().__init__(name)
        print("B Constructer")

    def sound(self):
        print("Single Inheritance")

    def sound1(self):
        print("Testing")

class Cclass(Bclass):
    def __init__(self,name):
        super().__init__(name)
        print("C Constructer")
    def sound(self):
        super().sound()
        print("Muti Level Inheritance")

class Dclass(Cclass,Bclass):
    def __init__(self,name):
        super().__init__(name)

    def sound2(self):
        print("Multiple Inheritance")


class Calculator:
    def add(self, *args):
        return sum(args)


class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

    # def make_animal_speak(self,ron):
    #     print(ron.speak())
    def make_animal_speak(self,ron):
        return ron.speak()


class Ronish:
    def __init__(self,name):
        print(f"name : {name}")

    def __repr__(self):
        return "This is Ronish Class"



class Abstraction:
    def __init__(self,name):
        self.name=name
    def key(self):
         pass
    def test(self):
         print(f"Welcome to India !!! {self.name}")


class Welcome(Abstraction):
    def key(self):
        print("Hiiiii")