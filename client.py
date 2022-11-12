from dbm import dumb
import websocket
import asyncio
import json
async def main():
    id = None
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:25505")
    while True:
        recive = ws.recv()
        message = json.loads(recive)
        if(message["type"]=="setup"):
            load = message["info"]
            id = load["id"]
            print('Enter your name:')
            name = input()
            load = {
                "id":id,
                "type":"info",
                "info":{
                    "name":name
                }
            }
            payload = json.dumps(load)
            ws.send(payload)
            print("Welcome "+name)

asyncio.get_event_loop().run_until_complete(main())