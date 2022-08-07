import json
import time
from typing import Any, Dict, List
from fastapi import WebSocket


class DownloadsHandler:
    """ Handles anime downloads """

    downloads: Dict[str, Any]
    """
        Example
            downloads[anime]
    """

    active_connections: List[WebSocket]

    def __init__(self) -> None:
        self.downloads = {}
        self.active_connections = []

    def listen(self):
        while True:
            time.sleep(5)
            self.broadcast()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self):
        data = json.dumps(self.downloads)
        for conn in self.active_connections:
            await conn.send_json(data)
