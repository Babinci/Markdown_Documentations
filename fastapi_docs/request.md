[Skip to content](https://fastapi.tiangolo.com/reference/request/#request-class)

# `Request` class [¶](https://fastapi.tiangolo.com/reference/request/\#request-class "Permanent link")

You can declare a parameter in a _path operation function_ or dependency to be of type `Request` and then you can access the raw request object directly, without any validation, etc.

You can import it directly from `fastapi`:

```md-code__content
from fastapi import Request

```

Tip

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.

## `` fastapi.Request [¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request "Permanent link")

```md-code__content
Request(scope, receive=empty_receive, send=empty_send)

```

Bases: `HTTPConnection`

| PARAMETER | DESCRIPTION |
| --- | --- |
| `scope` | **TYPE:** `Scope` |
| `receive` | **TYPE:** `Receive`**DEFAULT:** `empty_receive` |
| `send` | **TYPE:** `Send`**DEFAULT:** `empty_send` |

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>``` | ```md-code__content<br>def __init__(self, scope: Scope, receive: Receive = empty_receive, send: Send = empty_send):<br>    super().__init__(scope)<br>    assert scope["type"] == "http"<br>    self._receive = receive<br>    self._send = send<br>    self._stream_consumed = False<br>    self._is_disconnected = False<br>    self._form = None<br>``` |

### `` scope`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.scope "Permanent link")

```md-code__content
scope = scope

```

### `` app`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.app "Permanent link")

```md-code__content
app

```

### `` url`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.url "Permanent link")

```md-code__content
url

```

### `` base\_url`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.base_url "Permanent link")

```md-code__content
base_url

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.headers "Permanent link")

```md-code__content
headers

```

### `` query\_params`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.query_params "Permanent link")

```md-code__content
query_params

```

### `` path\_params`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.path_params "Permanent link")

```md-code__content
path_params

```

### `` cookies`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.cookies "Permanent link")

```md-code__content
cookies

```

### `` client`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.client "Permanent link")

```md-code__content
client

```

### `` session`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.session "Permanent link")

```md-code__content
session

```

### `` auth`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.auth "Permanent link")

```md-code__content
auth

```

### `` user`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.user "Permanent link")

```md-code__content
user

```

### `` state`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.state "Permanent link")

```md-code__content
state

```

### `` method`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.method "Permanent link")

```md-code__content
method

```

### `` receive`property`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.receive "Permanent link")

```md-code__content
receive

```

### `` url\_for [¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.url_for "Permanent link")

```md-code__content
url_for(name, /, **path_params)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `name` | **TYPE:** `str` |
| `**path_params` | **TYPE:** `Any`**DEFAULT:** `{}` |

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>182<br>183<br>184<br>185<br>186<br>187<br>``` | ```md-code__content<br>def url_for(self, name: str, /, **path_params: typing.Any) -> URL:<br>    url_path_provider: Router | Starlette | None = self.scope.get("router") or self.scope.get("app")<br>    if url_path_provider is None:<br>        raise RuntimeError("The `url_for` method can only be used inside a Starlette application or with a router.")<br>    url_path = url_path_provider.url_path_for(name, **path_params)<br>    return url_path.make_absolute_url(base_url=self.base_url)<br>``` |

### `` stream`async`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.stream "Permanent link")

```md-code__content
stream()

```

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>218<br>219<br>220<br>221<br>222<br>223<br>224<br>225<br>226<br>227<br>228<br>229<br>230<br>231<br>232<br>233<br>234<br>235<br>236<br>``` | ```md-code__content<br>async def stream(self) -> typing.AsyncGenerator[bytes, None]:<br>    if hasattr(self, "_body"):<br>        yield self._body<br>        yield b""<br>        return<br>    if self._stream_consumed:<br>        raise RuntimeError("Stream consumed")<br>    while not self._stream_consumed:<br>        message = await self._receive()<br>        if message["type"] == "http.request":<br>            body = message.get("body", b"")<br>            if not message.get("more_body", False):<br>                self._stream_consumed = True<br>            if body:<br>                yield body<br>        elif message["type"] == "http.disconnect":  # pragma: no branch<br>            self._is_disconnected = True<br>            raise ClientDisconnect()<br>    yield b""<br>``` |

### `` body`async`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.body "Permanent link")

```md-code__content
body()

```

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>238<br>239<br>240<br>241<br>242<br>243<br>244<br>``` | ```md-code__content<br>async def body(self) -> bytes:<br>    if not hasattr(self, "_body"):<br>        chunks: list[bytes] = []<br>        async for chunk in self.stream():<br>            chunks.append(chunk)<br>        self._body = b"".join(chunks)<br>    return self._body<br>``` |

### `` json`async`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.json "Permanent link")

```md-code__content
json()

```

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>246<br>247<br>248<br>249<br>250<br>``` | ```md-code__content<br>async def json(self) -> typing.Any:<br>    if not hasattr(self, "_json"):  # pragma: no branch<br>        body = await self.body()<br>        self._json = json.loads(body)<br>    return self._json<br>``` |

### `` form [¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.form "Permanent link")

```md-code__content
form(
    *,
    max_files=1000,
    max_fields=1000,
    max_part_size=1024 * 1024
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `max_files` | **TYPE:** `int | float`**DEFAULT:** `1000` |
| `max_fields` | **TYPE:** `int | float`**DEFAULT:** `1000` |
| `max_part_size` | **TYPE:** `int`**DEFAULT:** `1024 * 1024` |

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>287<br>288<br>289<br>290<br>291<br>292<br>293<br>294<br>295<br>296<br>``` | ```md-code__content<br>def form(<br>    self,<br>    *,<br>    max_files: int | float = 1000,<br>    max_fields: int | float = 1000,<br>    max_part_size: int = 1024 * 1024,<br>) -> AwaitableOrContextManager[FormData]:<br>    return AwaitableOrContextManagerWrapper(<br>        self._get_form(max_files=max_files, max_fields=max_fields, max_part_size=max_part_size)<br>    )<br>``` |

### `` close`async`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.close "Permanent link")

```md-code__content
close()

```

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>298<br>299<br>300<br>``` | ```md-code__content<br>async def close(self) -> None:<br>    if self._form is not None:  # pragma: no branch<br>        await self._form.close()<br>``` |

### `` is\_disconnected`async`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.is_disconnected "Permanent link")

```md-code__content
is_disconnected()

```

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>302<br>303<br>304<br>305<br>306<br>307<br>308<br>309<br>310<br>311<br>312<br>313<br>314<br>``` | ```md-code__content<br>async def is_disconnected(self) -> bool:<br>    if not self._is_disconnected:<br>        message: Message = {}<br>        # If message isn't immediately available, move on<br>        with anyio.CancelScope() as cs:<br>            cs.cancel()<br>            message = await self._receive()<br>        if message.get("type") == "http.disconnect":<br>            self._is_disconnected = True<br>    return self._is_disconnected<br>``` |

### `` send\_push\_promise`async`[¶](https://fastapi.tiangolo.com/reference/request/\#fastapi.Request.send_push_promise "Permanent link")

```md-code__content
send_push_promise(path)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `path` | **TYPE:** `str` |

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>316<br>317<br>318<br>319<br>320<br>321<br>322<br>``` | ```md-code__content<br>async def send_push_promise(self, path: str) -> None:<br>    if "http.response.push" in self.scope.get("extensions", {}):<br>        raw_headers: list[tuple[bytes, bytes]] = []<br>        for name in SERVER_PUSH_HEADERS_TO_COPY:<br>            for value in self.headers.getlist(name):<br>                raw_headers.append((name.encode("latin-1"), value.encode("latin-1")))<br>        await self._send({"type": "http.response.push", "path": path, "headers": raw_headers})<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top