from typing import List
from fastapi import WebSocket

active_connections: List[WebSocket] = []

async def broadcast(message: str):
    for ws in active_connections:
        try:
            await ws.send_text(message)
        except:
            pass
