from devialet import devialet_api
import aiohttp
import asyncio

async def test():
    session = aiohttp.ClientSession(raise_for_status=True)
    api = devialet_api.DevialetApi('192.168.1.17', session)
    await api.async_update()
    print(api.source_list)
    # print(await api.async_select_source("Optical jack (1)"))
    await session.close()


asyncio.run(test())
