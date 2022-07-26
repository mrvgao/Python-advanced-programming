import time
import asyncio


async def f1():
    print('step into f1')
    await asyncio.sleep(0.1)
    # time.sleep(0.1)
    print('execute f1')


async def f2():
    # time.sleep(0.5)
    print('step into f2')
    await asyncio.sleep(0.05)
    print('execute f2')


async def f3():
    # time.sleep(0.001)
    print('step into f3')
    await asyncio.sleep(0.001)
    print('execute f3')


def main():
    f1()
    f2()
    f3()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[
        f1(),
        f2(),
        f3(),
    ]))
    loop.close()
