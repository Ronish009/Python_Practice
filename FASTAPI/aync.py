import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("Hi")

asyncio.run(main())


async def fun():
    print("Hello Ronish")
    await asyncio.sleep(2)
    print("Task1 is completed")


def greet(name):
    return "Hello " + name.lower()


print(greet("Alice"))
print(1+3)

dic={}
dic['Alice']=[]
dic['Alice'].append(1)
dic['Alice'].append(2)
print(dic)