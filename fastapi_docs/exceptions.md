[Skip to content](https://fastapi.tiangolo.com/reference/exceptions/#exceptions-httpexception-and-websocketexception)

# Exceptions - `HTTPException` and `WebSocketException` [¶](https://fastapi.tiangolo.com/reference/exceptions/\#exceptions-httpexception-and-websocketexception "Permanent link")

These are the exceptions that you can raise to show errors to the client.

When you raise an exception, as would happen with normal Python, the rest of the execution is aborted. This way you can raise these exceptions from anywhere in the code to abort a request and show the error to the client.

You can use:

- `HTTPException`
- `WebSocketException`

These exceptions can be imported directly from `fastapi`:

```md-code__content
from fastapi import HTTPException, WebSocketException

```

## `` fastapi.HTTPException [¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.HTTPException "Permanent link")

```md-code__content
HTTPException(status_code, detail=None, headers=None)

```

Bases: `HTTPException`

An HTTP exception you can raise in your own code to show errors to the client.

This is for client errors, invalid authentication, invalid data, etc. Not for server
errors in your code.

Read more about it in the
[FastAPI docs for Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/).

#### Example [¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.HTTPException--example "Permanent link")

```md-code__content
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `status_code` | HTTP status code to send to the client.<br>**TYPE:** `int` |
| `detail` | Any data to be sent to the client in the `detail` key of the JSON<br>response.<br>**TYPE:** `Any`**DEFAULT:** `None` |
| `headers` | Any headers to send to the client in the response.<br>**TYPE:** `Optional[Dict[str, str]]`**DEFAULT:** `None` |

Source code in `fastapi/exceptions.py`

|     |     |
| --- | --- |
| ```<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    status_code: Annotated[<br>        int,<br>        Doc(<br>            """<br>            HTTP status code to send to the client.<br>            """<br>        ),<br>    ],<br>    detail: Annotated[<br>        Any,<br>        Doc(<br>            """<br>            Any data to be sent to the client in the `detail` key of the JSON<br>            response.<br>            """<br>        ),<br>    ] = None,<br>    headers: Annotated[<br>        Optional[Dict[str, str]],<br>        Doc(<br>            """<br>            Any headers to send to the client in the response.<br>            """<br>        ),<br>    ] = None,<br>) -> None:<br>    super().__init__(status_code=status_code, detail=detail, headers=headers)<br>``` |

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.HTTPException.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` detail`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.HTTPException.detail "Permanent link")

```md-code__content
detail = detail

```

### `` headers`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.HTTPException.headers "Permanent link")

```md-code__content
headers = headers

```

## `` fastapi.WebSocketException [¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.WebSocketException "Permanent link")

```md-code__content
WebSocketException(code, reason=None)

```

Bases: `WebSocketException`

A WebSocket exception you can raise in your own code to show errors to the client.

This is for client errors, invalid authentication, invalid data, etc. Not for server
errors in your code.

Read more about it in the
[FastAPI docs for WebSockets](https://fastapi.tiangolo.com/advanced/websockets/).

#### Example [¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.WebSocketException--example "Permanent link")

```md-code__content
from typing import Annotated

from fastapi import (
    Cookie,
    FastAPI,
    WebSocket,
    WebSocketException,
    status,
)

app = FastAPI()

@app.websocket("/items/{item_id}/ws")
async def websocket_endpoint(
    *,
    websocket: WebSocket,
    session: Annotated[str | None, Cookie()] = None,
    item_id: str,
):
    if session is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Session cookie is: {session}")
        await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `code` | A closing code from the<br>[valid codes defined in the specification](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1).<br>**TYPE:** `int` |
| `reason` | The reason to close the WebSocket connection.<br>It is UTF-8-encoded data. The interpretation of the reason is up to the<br>application, it is not specified by the WebSocket specification.<br>It could contain text that could be human-readable or interpretable<br>by the client code, etc.<br>**TYPE:** `Union[str, None]`**DEFAULT:** `None` |

Source code in `fastapi/exceptions.py`

|     |     |
| --- | --- |
| ```<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    code: Annotated[<br>        int,<br>        Doc(<br>            """<br>            A closing code from the<br>            [valid codes defined in the specification](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1).<br>            """<br>        ),<br>    ],<br>    reason: Annotated[<br>        Union[str, None],<br>        Doc(<br>            """<br>            The reason to close the WebSocket connection.<br>            It is UTF-8-encoded data. The interpretation of the reason is up to the<br>            application, it is not specified by the WebSocket specification.<br>            It could contain text that could be human-readable or interpretable<br>            by the client code, etc.<br>            """<br>        ),<br>    ] = None,<br>) -> None:<br>    super().__init__(code=code, reason=reason)<br>``` |

### `` code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.WebSocketException.code "Permanent link")

```md-code__content
code = code

```

### `` reason`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/exceptions/\#fastapi.WebSocketException.reason "Permanent link")

```md-code__content
reason = reason or ''

```

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top