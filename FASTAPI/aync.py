import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(10)
    print("Hi")

asyncio.run(main())


async def fun():
    print("Hello Ronish")
    await asyncio.sleep(10)
    print("Task1 is completed")
