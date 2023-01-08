import asyncio

import aiohttp


async def test_visitor():
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "http://localhost:8000/get_form?visitor_phone_number=+7 915 115 95 18&visitor_email=alex@me.com&visitor_name=alex&date=2020-12-12"
        ) as resp:
            print(await resp.text())


async def test_visitor_2():
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "http://localhost:8000/get_form?visitor_phone_number=8 915 115 95 18&visitor_email=alex@me.com&visitor_name=alex&date=2020-12-12"
        ) as resp:
            print(await resp.text())


async def test_restaurant():
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "http://localhost:8000/get_form?restaurant_phone_number=+7 915 115 95 18&restaurant_email=alex@me.com&restaurant_name=Zvezda&date=2020-12-12&restaurant_address=Krasnaya plochad"
        ) as resp:
            print(await resp.text())


async def test_dish():
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "http://localhost:8000/get_form?dish_name=sushi&date=2020-12-12"
        ) as resp:
            print(await resp.text())


async def main():
    await test_visitor()
    await test_visitor_2()
    await test_restaurant()
    await test_dish()


if __name__ == "__main__":
    asyncio.run(main())
