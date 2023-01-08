import asyncio

import aiohttp


async def test_request():
    req = input(
        "Введите ваш запрос ('http://localhost:8000/get_form?' уже применено):\n"
    )
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://localhost:8000/get_form?{req}") as resp:
            print(await resp.text())


async def main():
    await test_request()


if __name__ == "__main__":
    asyncio.run(main())
