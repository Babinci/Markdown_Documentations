[Skip to content](https://fastapi.tiangolo.com/reference/response/#response-class)

# `Response` class [¶](https://fastapi.tiangolo.com/reference/response/\#response-class "Permanent link")

You can declare a parameter in a _path operation function_ or dependency to be of type `Response` and then you can set data for the response like headers or cookies.

You can also use it directly to create an instance of it and return it from your _path operations_.

You can import it directly from `fastapi`:

```md-code__content
from fastapi import Response

```

## `` fastapi.Response [¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response "Permanent link")

```md-code__content
Response(
    content=None,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any`**DEFAULT:** `None` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `200` |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |
| `media_type` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `background` | **TYPE:** `BackgroundTask | None`**DEFAULT:** `None` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    content: typing.Any = None,<br>    status_code: int = 200,<br>    headers: typing.Mapping[str, str] | None = None,<br>    media_type: str | None = None,<br>    background: BackgroundTask | None = None,<br>) -> None:<br>    self.status_code = status_code<br>    if media_type is not None:<br>        self.media_type = media_type<br>    self.background = background<br>    self.body = self.render(content)<br>    self.init_headers(headers)<br>``` |

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.media_type "Permanent link")

```md-code__content
media_type = None

```

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.background "Permanent link")

```md-code__content
background = background

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.body "Permanent link")

```md-code__content
body = render(content)

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.render "Permanent link")

```md-code__content
render(content)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>48<br>49<br>50<br>51<br>52<br>53<br>``` | ```md-code__content<br>def render(self, content: typing.Any) -> bytes | memoryview:<br>    if content is None:<br>        return b""<br>    if isinstance(content, (bytes, memoryview)):<br>        return content<br>    return content.encode(self.charset)  # type: ignore<br>``` |

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.init_headers "Permanent link")

```md-code__content
init_headers(headers=None)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>``` | ```md-code__content<br>def init_headers(self, headers: typing.Mapping[str, str] | None = None) -> None:<br>    if headers is None:<br>        raw_headers: list[tuple[bytes, bytes]] = []<br>        populate_content_length = True<br>        populate_content_type = True<br>    else:<br>        raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]<br>        keys = [h[0] for h in raw_headers]<br>        populate_content_length = b"content-length" not in keys<br>        populate_content_type = b"content-type" not in keys<br>    body = getattr(self, "body", None)<br>    if (<br>        body is not None<br>        and populate_content_length<br>        and not (self.status_code < 200 or self.status_code in (204, 304))<br>    ):<br>        content_length = str(len(body))<br>        raw_headers.append((b"content-length", content_length.encode("latin-1")))<br>    content_type = self.media_type<br>    if content_type is not None and populate_content_type:<br>        if content_type.startswith("text/") and "charset=" not in content_type.lower():<br>            content_type += "; charset=" + self.charset<br>        raw_headers.append((b"content-type", content_type.encode("latin-1")))<br>    self.raw_headers = raw_headers<br>``` |

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.set_cookie "Permanent link")

```md-code__content
set_cookie(
    key,
    value="",
    max_age=None,
    expires=None,
    path="/",
    domain=None,
    secure=False,
    httponly=False,
    samesite="lax",
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `key` | **TYPE:** `str` |
| `value` | **TYPE:** `str`**DEFAULT:** `''` |
| `max_age` | **TYPE:** `int | None`**DEFAULT:** `None` |
| `expires` | **TYPE:** `datetime | str | int | None`**DEFAULT:** `None` |
| `path` | **TYPE:** `str | None`**DEFAULT:** `'/'` |
| `domain` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `secure` | **TYPE:** `bool`**DEFAULT:** `False` |
| `httponly` | **TYPE:** `bool`**DEFAULT:** `False` |
| `samesite` | **TYPE:** `Literal['lax', 'strict', 'none'] | None`**DEFAULT:** `'lax'` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>``` | ```md-code__content<br>def set_cookie(<br>    self,<br>    key: str,<br>    value: str = "",<br>    max_age: int | None = None,<br>    expires: datetime | str | int | None = None,<br>    path: str | None = "/",<br>    domain: str | None = None,<br>    secure: bool = False,<br>    httponly: bool = False,<br>    samesite: typing.Literal["lax", "strict", "none"] | None = "lax",<br>) -> None:<br>    cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()<br>    cookie[key] = value<br>    if max_age is not None:<br>        cookie[key]["max-age"] = max_age<br>    if expires is not None:<br>        if isinstance(expires, datetime):<br>            cookie[key]["expires"] = format_datetime(expires, usegmt=True)<br>        else:<br>            cookie[key]["expires"] = expires<br>    if path is not None:<br>        cookie[key]["path"] = path<br>    if domain is not None:<br>        cookie[key]["domain"] = domain<br>    if secure:<br>        cookie[key]["secure"] = True<br>    if httponly:<br>        cookie[key]["httponly"] = True<br>    if samesite is not None:<br>        assert samesite.lower() in [<br>            "strict",<br>            "lax",<br>            "none",<br>        ], "samesite must be either 'strict', 'lax' or 'none'"<br>        cookie[key]["samesite"] = samesite<br>    cookie_val = cookie.output(header="").strip()<br>    self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))<br>``` |

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/response/\#fastapi.Response.delete_cookie "Permanent link")

```md-code__content
delete_cookie(
    key,
    path="/",
    domain=None,
    secure=False,
    httponly=False,
    samesite="lax",
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `key` | **TYPE:** `str` |
| `path` | **TYPE:** `str`**DEFAULT:** `'/'` |
| `domain` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `secure` | **TYPE:** `bool`**DEFAULT:** `False` |
| `httponly` | **TYPE:** `bool`**DEFAULT:** `False` |
| `samesite` | **TYPE:** `Literal['lax', 'strict', 'none'] | None`**DEFAULT:** `'lax'` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>``` | ```md-code__content<br>def delete_cookie(<br>    self,<br>    key: str,<br>    path: str = "/",<br>    domain: str | None = None,<br>    secure: bool = False,<br>    httponly: bool = False,<br>    samesite: typing.Literal["lax", "strict", "none"] | None = "lax",<br>) -> None:<br>    self.set_cookie(<br>        key,<br>        max_age=0,<br>        expires=0,<br>        path=path,<br>        domain=domain,<br>        secure=secure,<br>        httponly=httponly,<br>        samesite=samesite,<br>    )<br>``` |

Was this page helpful?