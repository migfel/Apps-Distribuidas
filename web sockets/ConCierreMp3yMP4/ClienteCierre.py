import asyncio
import websockets

async def send_file(file_path):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                await websocket.send(chunk)
        await websocket.send(b"")  # Send an empty message to signal the end

async def main():
    await send_file("your_audio.mp3")
    await send_file("your_video.mp4")

asyncio.get_event_loop().run_until_complete(main())
