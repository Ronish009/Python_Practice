from Oops_Concept.Class import Student,Aclass,Bclass,Cclass,Dclass,Calculator,Animal,Cat,Dog,Ronish,Abstraction,Welcome

if __name__ == "__main__":
    s=Student("Ronish",35)
    s.print()

    d=Aclass("Ronish")
    d.print()

    d=Bclass("Ronish1")
    d.sound()

    c=Cclass("Ronish")
    c.sound()
    c.sound1()

    d=Dclass("Ronish")
    d.sound2()

    calc = Calculator()
    print(calc.add(5, 10))
    print(calc.add(5, 10, 15))
    print(calc.add(1, 2, 3, 4))

    a=Animal()
    d=Dog()
    c=Cat()
    # c.make_animal_speak(a)
    # c.make_animal_speak(c)
    print(c.make_animal_speak(a))
    print(c.make_animal_speak(d))


    # 3 Operator Overloading
    # We create a simple class that customizes the '+' operator.
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            # This special method defines the behavior of the '+' operator.
            return Vector(self.x + other.x, self.y + other.y)

        def __repr__(self):
            return f"Vector({self.x}, {self.y})"


    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v3 = v1 + v2
    print(v3)
    r1=Ronish("Ron")
    print(r1)
    s=Welcome("Raj")
    s.key()
    s.test()
