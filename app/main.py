from fastapi import FastAPI
from app.ws.router import router as router_websocket


app = FastAPI(
    title="Real-Time Chat"
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(router_websocket)

