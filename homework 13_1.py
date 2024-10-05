import asyncio


def get_delay(power):
    return 1 / power


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        delay = get_delay(power)
        print(f'Силач {name} поднял {i} шар.')
        await asyncio.sleep(delay)

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    names = ['Pasha', 'Denis', 'Apollon']
    powers = [3, 4, 5]

    tasks = []
    for name, power in zip(names, powers):
        task = asyncio.create_task(start_strongman(name, power))
        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(start_tournament())
















