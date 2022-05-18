import time
import asyncpg
import asyncio
import scrapper

async def update():
    todo=[]
    DSN = 'postgres://postgres:admin@pgdb:5432/fortstats'
    conn = await asyncpg.connect(DSN)
    rows = await conn.fetch('SELECT FortID FROM fortistats')
    for x in rows:
        todo.append("https://fortnitetracker.com/profile/all/"+x['fortid'])

    scrape = await scrapper.scrape(todo)

    for y in scrape:

        await conn.fetch("UPDATE public.fortistats SET wins={1}, winper={2}, kills={3}, kd={4} where fortid = \'{0}\'".format(*y))  

async def updater():
    while True:
        time.sleep(300)
        await update()

if __name__ == '__main__':
    asyncio.run(updater())