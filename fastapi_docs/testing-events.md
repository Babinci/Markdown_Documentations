[Skip to content](https://fastapi.tiangolo.com/advanced/testing-events/#testing-events-startup-shutdown)

# Testing Events: startup - shutdown [¶](https://fastapi.tiangolo.com/advanced/testing-events/\#testing-events-startup-shutdown "Permanent link")

When you need your event handlers ( `startup` and `shutdown`) to run in your tests, you can use the `TestClient` with a `with` statement:

[Python 3.8+](https://fastapi.tiangolo.com/advanced/testing-events/#__tabbed_1_1)

```md-code__content
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

items = {}

@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}

@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]

def test_read_items():
    with TestClient(app) as client:
        response = client.get("/items/foo")
        assert response.status_code == 200
        assert response.json() == {"name": "Fighters"}

```

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top