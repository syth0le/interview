import asyncio
import types
import requests
from aiostream import stream
from bs4 import BeautifulSoup
import time

STAT = dict()
STAT_CAMO = dict()
STAT_RES = dict()


class Config:
    URL = 'https://spoty-readme.herokuapp.com/'
    CAMO = 'https://camo.githubusercontent.com/c9f6ddb9215657cc194a5813204a726cf1654b65ebea7d177987004167d2042c/68747470733a2f2f73706f74792d726561646d652e6865726f6b756170702e636f6d2f'


async def request_url(url):
    return requests.request(method='get', url=url)


def decorator_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()

        print(type(res))
        # return f'{res} - {round(finish-start, 5)}'
        print(round(finish-start, 5))
        return res
    return wrapper


def say_hello(function):
    def decorated(*args, **kwargs):
        function_instance = function(*args, **kwargs)
        if isinstance(function_instance, types.AsyncGeneratorType):
            async def inner():
                print("Hello async generator!")
                async for v in function_instance:
                    yield v
        else:
            async def inner():
                print("Hello coroutine!")
                return await function_instance
        return inner()
    return decorated


async def statistics(url):
    for _ in range(20):
        start = time.time()
        req = await request_url(url=url)
        _1 = time.time()
        print(_1 - start, end='->')
        soup = BeautifulSoup(req.text, features="html.parser")
        _2 = time.time()
        print(_2 - _1, end='->')
        temp = soup.find('div', {'class': 'song'}).text
        _3 = time.time()
        print(_3 - _2, end='->')
        if temp not in STAT:
            STAT[temp] = 1
        else:
            STAT[temp] += 1
        _4 = time.time()
        print(_4 - _3, end='::RES::')
        print(_4 - start)
        yield f"URL: {temp}"
        await asyncio.sleep(0.1)


async def camo_stat(url):
    for _ in range(20):
        start = time.time()
        req_camo = await request_url(url=url)
        _1 = time.time()
        print(_1 - start, end='->')
        soup_camo = BeautifulSoup(req_camo.text, features="html.parser")
        _2 = time.time()
        print(_2 - _1, end='->')
        temp_camo = soup_camo.find('div', {'class': 'song'}).text
        _3 = time.time()
        print(_3 - _2, end='->')
        if temp_camo not in STAT_CAMO:
            STAT_CAMO[temp_camo] = 1
        else:
            STAT_CAMO[temp_camo] += 1
        _4 = time.time()
        print(_4 - _3, end='::RES::')
        print(_4 - start)
        yield f"CAMO: {temp_camo}"
        await asyncio.sleep(0.2)


async def main():
    combine = stream.merge(statistics(Config.URL), camo_stat(Config.CAMO))
    async with combine.stream() as streamer:
        async for item in streamer:
            print(item)


def new_dict(SU,SC,FS):
    for elem in SU:
        if elem not in FS:
            FS[elem] = SU[elem]
        else:
            FS[elem] += SU[elem]
    for elem in SC:
        if elem not in FS:
            FS[elem] = SC[elem]
        else:
            FS[elem] += SC[elem]
    return FS


start = time.time()
asyncio.run(main())
print(STAT)
print(STAT_CAMO)
print(new_dict(STAT_CAMO, STAT, STAT_RES))
finish = time.time()
print(round(finish-start, 5))
