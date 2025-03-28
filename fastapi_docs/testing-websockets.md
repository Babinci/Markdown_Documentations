[Skip to content](https://fastapi.tiangolo.com/advanced/testing-websockets/#testing-websockets)

# Testing WebSockets [¶](https://fastapi.tiangolo.com/advanced/testing-websockets/\#testing-websockets "Permanent link")

You can use the same `TestClient` to test WebSockets.

For this, you use the `TestClient` in a `with` statement, connecting to the WebSocket:

[Python 3.8+](https://fastapi.tiangolo.com/advanced/testing-websockets/#__tabbed_1_1)

```md-code__content
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()

def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}

```

Note

For more details, check Starlette's documentation for [testing WebSockets](https://www.starlette.io/testclient/#testing-websocket-sessions).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top