"""LangChain Practice"""
import asyncio
import os
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from typing import Iterator



sequence = RunnableLambda(lambda x: x + 1) | RunnableLambda(lambda x: x * 2)
print(sequence.invoke(1))  # 4
print(sequence.batch([1, 2, 3]))  # [4, 6, 8]


sequence = RunnableLambda(lambda x: x + 1) | {
    "mul_2": RunnableLambda(lambda x: x * 2),
    "mul_5": RunnableLambda(lambda x: x * 5),
}
print(sequence.invoke(1))  # {'mul_2': 4, 'mul_5': 10}

def add_one(x: int) -> int:
    return x + 1


runnable = RunnableLambda(add_one)

print(runnable.get_input_jsonschema())


def add_one1(x: int) -> int:
    """Function"""
    return x + 1

def add_one2(x: int) -> Iterator[int]:
    """Function"""
    yield x + 1

def mul_two(x: int) -> int:
    """Function"""
    return x * 2


runnable_1 = RunnableLambda(add_one2 )
runnable_2 = RunnableLambda(mul_two)
sequence = runnable_1.pipe(runnable_2)

print(sequence.invoke(1))

async def main():
    result = await sequence.ainvoke(1)
    print(result)

asyncio.run(main())


print(sequence.batch([1, 2, 3]))

async def main2():
    result1=await sequence.abatch([1, 2, 3])

asyncio.run(main2())

print("\n"+"*"*50+"\n")
def count_up_to(n: int) -> Iterator[int]:
    for i in range(1, n + 1):
        yield i

runnable5 = RunnableLambda(count_up_to)

for value in runnable5.stream(5):
    print(value)