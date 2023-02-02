#!/usr/bin/env python

import websockets
import asyncio
import os
from dotenv import load_dotenv
from server.handler import handler

load_dotenv()

try:
    port = os.getenv('WS_PORT')
except:
    print('Unable to load port from .env')
    exit()

ws = websockets.serve(handler, 'localhost', )
print(f'Starting WebSocket Server on port {port}')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(ws)
    asyncio.get_event_loop().run_forever()