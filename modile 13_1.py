import asyncio

async def start_strongman(name, power):
    print(f'f Силач {name} начал соревнования.')
    t = 1/power
    for i in range(5):
        await asyncio.sleep(t)
        print(f'f Силач {name} поднял {i+1}')
    print(f'fСилач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apolon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

