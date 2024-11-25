import asyncio
from time import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    start_time = time()
    for i in range(5):
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {i + 1} шар.')
    time_ = round(time() - start_time, 2)
    print(f'Силач {name} закончил соревнование со временем выполнения {time_} секунд.')


async def start_tournament():
    await asyncio.gather(
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5),
    )


asyncio.run(start_tournament())
