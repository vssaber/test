import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time, datetime
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', INDEX)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

print("its not right")
print("its lala")
