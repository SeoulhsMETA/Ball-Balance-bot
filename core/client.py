"""web socket client"""

from __future__ import annotations

from socketio import AsyncClient

from model.status import BotStatus

class SocketIOClient:
    """socketio client"""

    def __init__(self, url: str) -> None:
        self._socket = AsyncClient()
        self.url = url
    
    @classmethod
    def from_config(cls) -> SocketIOClient:
        from config.config import get_config
        return cls(get_config()["client"]["url"])
    
    async def connect(self) -> None:
        await self._socket.connect(self.url)
    
    async def send(self, status_data: BotStatus) -> None:
        return
