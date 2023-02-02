import json
from programs import basic
from utils.validator import json_validator
from config import strip

async def handler(ws, path):
    print('client connected')
    try:
        async for message in ws:
            try:
                message_json = json.loads(message)
                # TODO: fix validator
                # json_validator(message_json)
                res = init_program(message_json)
                await ws.send(res)
            except Exception as e:
                print(e)
                await ws.send('ERROR: invalid json')   
    except ws.exceptions.ConnectionClosed as e:
        print('client disconnected')
        

def init_program(message):
    led_strip = strip.init()
    
    program = message['program']
    if program == 'static': 
        basic.static(led_strip, message['r'], message['g'], message['b'])
        return f'initalizing program: {program}'
    
    else:
        return f'program: {program} is unknown'