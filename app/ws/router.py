from fastapi import APIRouter
from fastapi import WebSocket, WebSocketDisconnect
from app.ws.ConnectionManager import ConnectionManager

manager = ConnectionManager()

router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"]
)


@router.websocket("/{session_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str, user_id: str):
    await manager.connect(websocket, session_id, user_id)
    try:
        await manager.personal_message(f"Connected successfully.", user_id)

        while True:
            data = await websocket.receive_json()
            await manager.broadcast(f"User {user_id}: {data}", session_id, user_id)
    except WebSocketDisconnect:
        manager.disconnect(session_id, user_id)
