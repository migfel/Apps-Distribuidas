import asyncio
import websockets

async def receive_file(websocket, path):
    try:
        filename = f"received_file{path[-4:]}"  # Extract file extension
        with open(filename, "wb") as file:
            while True:
                data = await websocket.recv()
                if not data:
                    break
                file.write(data)
        print(f"File {filename} received successfully.")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed.")

start_server = websockets.serve(receive_file, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
