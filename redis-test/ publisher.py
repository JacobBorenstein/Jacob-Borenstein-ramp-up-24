from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()

r = redis.Redis(host='localhost', port=6379)

class Message(BaseModel):
    text: str

@app.post("/publish")
async def publish_message(message: Message):
    r.publish('channel', message.text)
    return {"status": "Message published"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)