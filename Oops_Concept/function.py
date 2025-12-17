"""Mutiple Argument and Multipe Key Argument"""
def test(*arg,**karg):
    """Function for arg and karg"""
    for i in arg:
        print(i)
    for k,v in karg.items():
        print(f"{k} : {v}")

test(1,2,3,4,"ronish","arghyadip",a1="Ronish",a2="Arghyadip")


def f1():
    """Function for inner Function"""
    print("Before f1")
    def inner_f2():
        s = "Ronish"
        print(s)
    inner_f2()
    print("before f3")
    def f3():
        name = "Arghyadip"
        print(name)

    f3()

f1()


# Anonymous Function

l =lambda x:x*x
print(l(2))

a=12
print(a)
a=13
print(a)

#Fabonni Series Sum Using Lambda
f = lambda x: 1 if x==1 else 0 if x==0  else f(x-1)+f(x-2)
print(f(10))

#Fibonni series Sum
def f10(n):
    """Fibonni series Sum"""
    if n==1:
        return 1
    if n==0:
        return 0
    return f10(n-1)+f10(n-2)

#Fabonni Series Print
def f2(n):
    """Fabonni Series Print"""
    print(0, " ", end="")
    print(1, " ", end="")

    def f11(n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        return f11(n - 1) + f11(n - 2)
    for i in range(2,n):
        print(f11(i)," ",end='')

f2(10)
