from aiohttp import web
import asyncpg
import scrapper
import marshmallow
import subprocess
import sys

class UserData(marshmallow.Schema):
    class Meta:
        ordered = True  
    fortid = marshmallow.fields.Str()
    wins = marshmallow.fields.Int()
    winper = marshmallow.fields.Float()
    kills = marshmallow.fields.Int()
    kd = marshmallow.fields.Float()


async def push(request):
    DSN = 'postgres://postgres:admin@pgdb:5432/fortstats'
    conn = await asyncpg.connect(DSN)
    url = ["https://fortnitetracker.com/profile/all/"+request.match_info['id']]
    data = (await scrapper.scrape(url))[0]
    if data == False: #handler for if data does not exist
        return web.Response(text="Push Failed")
    else:
        await conn.fetch("INSERT INTO public.fortistats(fortid, wins, winper, kills, kd) VALUES ('{0}', {1}, {2}, {3}, {4})".format(*data))
        return web.Response(text="Push Success")

async def pull(request):
    schema = UserData()

    DSN = 'postgres://postgres:admin@pgdb:5432/fortstats'
    conn = await asyncpg.connect(DSN)

    row = await conn.fetch('SELECT * FROM public.fortistats where fortid = \''+request.match_info['id'] + "\'")
    result = schema.dump(row[0])
    return web.json_response(result)

async def pullall(request):
    outlist=[]
    DSN = 'postgres://postgres:admin@pgdb:5432/fortstats'
    conn = await asyncpg.connect(DSN)
    rows = await conn.fetch('SELECT FortID FROM fortistats')
    for x in rows:
        outlist.append(x['fortid'])
    return web.json_response(outlist)

async def update(request):
    todo=[]
    DSN = 'postgres://postgres:admin@pgdb:5432/fortstats'
    conn = await asyncpg.connect(DSN)
    rows = await conn.fetch('SELECT FortID FROM fortistats')
    for x in rows:
        todo.append("https://fortnitetracker.com/profile/all/"+x['fortid'])

    scrape = await scrapper.scrape(todo)

    for y in scrape:

        await conn.fetch("UPDATE public.fortistats SET wins={1}, winper={2}, kills={3}, kd={4} where fortid = \'{0}\'".format(*y))  
    return web.Response(text="Success")

app = web.Application()
app.add_routes([web.get('/push/{id}', push)])
app.add_routes([web.get('/pull/{id}', pull)])
app.add_routes([web.get('/pullall', pullall)])
app.add_routes([web.get('/update', update)])
p = subprocess.Popen([sys.executable, 'updater.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

web.run_app(app)
