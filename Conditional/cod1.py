"""Check eligibility based on age."""
import keyword
AGE=16
if AGE>12:
    print("Eligible")
else:
    print("Not eligible")
print()
mark=float(input("Enter your percentage :  "))
if mark<30:
    print("You are failed")
elif 30<mark<60:
    print("You got second division")
elif 60>mark<75:
    print("You got first division")
else:
    print("Yo got first division with extension")


print("Keyword of Python : ",keyword.kwlist)
print("Total Keyword of Python : ",len(keyword.kwlist))

num=int(input("Enter any number : "))
while num>0:
    print(num)
    num-=1

