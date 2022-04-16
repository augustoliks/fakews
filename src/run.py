from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketDisconnect
)
from typing import List
import uvicorn
import asyncio
from pathlib import Path
import logging
import json


mocks = [
    json.dumps(json.loads(path.read_text())) 
    for path in Path('.').glob('mock-*.json')
]


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        logging.info('client ws conectado')
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        logging.info('client ws desconectado')
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket, time_wait=1):
        logging.info('mesagem enviada')
        await asyncio.sleep(time_wait)
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


def configure_app(app: FastAPI):
    connection_manager = ConnectionManager()

    @app.websocket("/ws")
    async def ws(websocket: WebSocket):
        await connection_manager.connect(websocket)
        try:
            while True:
                for mock in mocks:
                    await connection_manager.send_personal_message(
                        message=mock,
                        websocket=websocket,
                        time_wait=1
                    )
        except WebSocketDisconnect:
            connection_manager.disconnect(websocket)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('websockets')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    app = FastAPI()
    configure_app(app)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8090
    )
