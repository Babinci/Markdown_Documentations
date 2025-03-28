[Skip to content](https://fastapi.tiangolo.com/reference/httpconnection/#httpconnection-class)

# `HTTPConnection` class [¶](https://fastapi.tiangolo.com/reference/httpconnection/\#httpconnection-class "Permanent link")

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.

You can import it from `fastapi.requests`:

```md-code__content
from fastapi.requests import HTTPConnection

```

## `` fastapi.requests.HTTPConnection [¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection "Permanent link")

```md-code__content
HTTPConnection(scope, receive=None)

```

Bases: `Mapping[str, Any]`

A base class for incoming HTTP connections, that is used to provide
any functionality that is common to both `Request` and `WebSocket`.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `scope` | **TYPE:** `Scope` |
| `receive` | **TYPE:** `Receive | None`**DEFAULT:** `None` |

Source code in `starlette/requests.py`

|     |     |
| --- | --- |
| ```<br>76<br>77<br>78<br>``` | ```md-code__content<br>def __init__(self, scope: Scope, receive: Receive | None = None) -> None:<br>    assert scope["type"] in ("http", "websocket")<br>    self.scope = scope<br>``` |

### `` scope`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.scope "Permanent link")

```md-code__content
scope = scope

```

### `` app`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.app "Permanent link")

```md-code__content
app

```

### `` url`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.url "Permanent link")

```md-code__content
url

```

### `` base\_url`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.base_url "Permanent link")

```md-code__content
base_url

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.headers "Permanent link")

```md-code__content
headers

```

### `` query\_params`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.query_params "Permanent link")

```md-code__content
query_params

```

### `` path\_params`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.path_params "Permanent link")

```md-code__content
path_params

```

### `` cookies`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.cookies "Permanent link")

```md-code__content
cookies

```

### `` client`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.client "Permanent link")

```md-code__content
client

```

### `` session`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.session "Permanent link")

```md-code__content
session

```

### `` auth`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.auth "Permanent link")

```md-code__content
auth

```

### `` user`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.user "Permanent link")

```md-code__content
user

```

### `` state`property`[¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.state "Permanent link")

```md-code__content
state

```

### `` url\_for [¶](https://fastapi.tiangolo.com/reference/httpconnection/\#fastapi.requests.HTTPConnection.url_for "Permanent link")

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

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top