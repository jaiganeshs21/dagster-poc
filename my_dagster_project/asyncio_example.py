from dagster import op, graph
import asyncio
import os

@op
async def task_1():
    print(f"Inside task 1. PID: {os.getpid()}")
    await asyncio.sleep(10)
    return "done"

@op
async def task_2(task1):
    print(f"Inside task 2. PID: {os.getpid()}")
    await asyncio.sleep(10)
    return "done"

@op
async def task_3(task2):
    print(f"Inside task 3. PID: {os.getpid()}")
    await asyncio.sleep(10)
    return "done"

@op
async def task_4(task3):
    print(f"Inside task 4. PID: {os.getpid()}")
    await asyncio.sleep(10)
    return "done"

@op
async def task_5(task4):
    print(f"Inside task 5. PID: {os.getpid()}")
    await asyncio.sleep(10)
    return "done"

@graph
def daily_etl_async():
    task1 = task_1()
    task2 = task_2(task1)
    task3 = task_3(task2)
    task4 = task_4(task3)
    task5 = task_5(task4)