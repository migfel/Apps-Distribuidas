import asyncio
import websockets

async def enviar_archivo(ruta_archivo):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        with open(ruta_archivo, "rb") as archivo:
            while True:
                fragmento = archivo.read(1024)
                if not fragmento:
                    break
                await websocket.send(fragmento)
        await websocket.send(b"")  # Enviar un mensaje vacío para señalizar el final

async def main():
    await enviar_archivo("tu_audio.mp3")
    await enviar_archivo("tu_video.mp4")

asyncio.get_event_loop().run_until_complete(main())

