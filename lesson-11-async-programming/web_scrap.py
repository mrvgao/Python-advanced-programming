import random

import requests
import aiohttp
import asyncio
import time

url = lambda base: f"https://aqicn.org/city/{base}/"

BASES = ("beijing", "wuhan", "nanjing", "shanghai", "chengdu")


async def get_pages_mock(index):
    await asyncio.sleep(random.uniform(0.01, 0.1))
    print(f'get {index} success!')


def get_pages():
    for base in BASES:
        r = requests.get(url(base))
        # rate = r.json()['rates']
        rate = r.text
        print(base, rate)


async def get_page_async(session: aiohttp.ClientSession, base: str):
    # async with session.get(
    #     url(base)
    # ) as r:
    #     rate = r.text
    #     print('get page func')
    #     return base, rate
    async with session.get(url(base)) as r:
        print(r.text)


async def main():
    async with aiohttp.ClientSession() as session:
        # await get_page_async(session, BASES[0])
        # print('hello test')
        for result in await asyncio.gather(*[get_pages_mock(i) for i in range(10)]):
            pass
        # for result in await asyncio.gather(*[get_page_async(session, base) for base in BASES]):
        #     print(result)


if __name__ == '__main__':
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # get_pages()
    elapsed = time.time() - started

    print(f'time consumed: {elapsed}')
