from typing import List
from fastapi import WebSocket
from app.ws.SessionManager import SessionManager
from app.ws.schemas import Connection


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[Connection] = []
        self.__sessions_manager = SessionManager()

    async def connect(self, websocket: WebSocket, session_id: str, user_id: str):
        await websocket.accept()
        self.active_connections.append(
            Connection(
                id=user_id,
                websocket=websocket
            )
        )
        self.__sessions_manager.connect_user(session_id, user_id)

    def disconnect(self, session_id: str, user_id: str):
        for connection in self.active_connections:
            if connection.id == user_id:
                self.active_connections.remove(connection)
                self.__sessions_manager.remove_user(session_id, user_id)

    async def personal_message(self, message: str, user_id: str):
        for connection in self.active_connections:
            if connection.id == user_id:
                await connection.websocket.send_json(message)

    async def broadcast(self, message: str, session_id: str, user_id: str):
        users = self.__sessions_manager.get_session_users(session_id)

        for connection in self.active_connections:
            if connection.id != user_id and connection.id in users:
                await connection.websocket.send_json(message)
