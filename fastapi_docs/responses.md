[Skip to content](https://fastapi.tiangolo.com/reference/responses/#custom-response-classes-file-html-redirect-streaming-etc)

# Custom Response Classes - File, HTML, Redirect, Streaming, etc. [¶](https://fastapi.tiangolo.com/reference/responses/\#custom-response-classes-file-html-redirect-streaming-etc "Permanent link")

There are several custom response classes you can use to create an instance and return them directly from your _path operations_.

Read more about it in the [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/).

You can import them directly from `fastapi.responses`:

```md-code__content
from fastapi.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    ORJSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
    StreamingResponse,
    UJSONResponse,
)

```

## FastAPI Responses [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi-responses "Permanent link")

There are a couple of custom FastAPI response classes, you can use them to optimize JSON performance.

## `` fastapi.responses.UJSONResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse "Permanent link")

```md-code__content
UJSONResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `JSONResponse`

JSON response using the high-performance ujson library to serialize data to JSON.

Read more about it in the
[FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `200` |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |
| `media_type` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `background` | **TYPE:** `BackgroundTask | None`**DEFAULT:** `None` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    content: typing.Any,<br>    status_code: int = 200,<br>    headers: typing.Mapping[str, str] | None = None,<br>    media_type: str | None = None,<br>    background: BackgroundTask | None = None,<br>) -> None:<br>    super().__init__(content, status_code, headers, media_type, background)<br>``` |

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.media_type "Permanent link")

```md-code__content
media_type = 'application/json'

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.render "Permanent link")

```md-code__content
render(content)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any` |

Source code in `fastapi/responses.py`

|     |     |
| --- | --- |
| ```<br>31<br>32<br>33<br>``` | ```md-code__content<br>def render(self, content: Any) -> bytes:<br>    assert ujson is not None, "ujson must be installed to use UJSONResponse"<br>    return ujson.dumps(content, ensure_ascii=False).encode("utf-8")<br>``` |

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.UJSONResponse.delete_cookie "Permanent link")

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

## `` fastapi.responses.ORJSONResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse "Permanent link")

```md-code__content
ORJSONResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `JSONResponse`

JSON response using the high-performance orjson library to serialize data to JSON.

Read more about it in the
[FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `200` |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |
| `media_type` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `background` | **TYPE:** `BackgroundTask | None`**DEFAULT:** `None` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    content: typing.Any,<br>    status_code: int = 200,<br>    headers: typing.Mapping[str, str] | None = None,<br>    media_type: str | None = None,<br>    background: BackgroundTask | None = None,<br>) -> None:<br>    super().__init__(content, status_code, headers, media_type, background)<br>``` |

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.media_type "Permanent link")

```md-code__content
media_type = 'application/json'

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.render "Permanent link")

```md-code__content
render(content)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any` |

Source code in `fastapi/responses.py`

|     |     |
| --- | --- |
| ```<br>44<br>45<br>46<br>47<br>48<br>``` | ```md-code__content<br>def render(self, content: Any) -> bytes:<br>    assert orjson is not None, "orjson must be installed to use ORJSONResponse"<br>    return orjson.dumps(<br>        content, option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SERIALIZE_NUMPY<br>    )<br>``` |

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.ORJSONResponse.delete_cookie "Permanent link")

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

## Starlette Responses [¶](https://fastapi.tiangolo.com/reference/responses/\#starlette-responses "Permanent link")

## `` fastapi.responses.FileResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse "Permanent link")

```md-code__content
FileResponse(
    path,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
    filename=None,
    stat_result=None,
    method=None,
    content_disposition_type="attachment",
)

```

Bases: `Response`

| PARAMETER | DESCRIPTION |
| --- | --- |
| `path` | **TYPE:** `str | PathLike[str]` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `200` |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |
| `media_type` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `background` | **TYPE:** `BackgroundTask | None`**DEFAULT:** `None` |
| `filename` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `stat_result` | **TYPE:** `stat_result | None`**DEFAULT:** `None` |
| `method` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `content_disposition_type` | **TYPE:** `str`**DEFAULT:** `'attachment'` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>292<br>293<br>294<br>295<br>296<br>297<br>298<br>299<br>300<br>301<br>302<br>303<br>304<br>305<br>306<br>307<br>308<br>309<br>310<br>311<br>312<br>313<br>314<br>315<br>316<br>317<br>318<br>319<br>320<br>321<br>322<br>323<br>324<br>325<br>326<br>327<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    path: str | os.PathLike[str],<br>    status_code: int = 200,<br>    headers: typing.Mapping[str, str] | None = None,<br>    media_type: str | None = None,<br>    background: BackgroundTask | None = None,<br>    filename: str | None = None,<br>    stat_result: os.stat_result | None = None,<br>    method: str | None = None,<br>    content_disposition_type: str = "attachment",<br>) -> None:<br>    self.path = path<br>    self.status_code = status_code<br>    self.filename = filename<br>    if method is not None:<br>        warnings.warn(<br>            "The 'method' parameter is not used, and it will be removed.",<br>            DeprecationWarning,<br>        )<br>    if media_type is None:<br>        media_type = guess_type(filename or path)[0] or "text/plain"<br>    self.media_type = media_type<br>    self.background = background<br>    self.init_headers(headers)<br>    self.headers.setdefault("accept-ranges", "bytes")<br>    if self.filename is not None:<br>        content_disposition_filename = quote(self.filename)<br>        if content_disposition_filename != self.filename:<br>            content_disposition = f"{content_disposition_type}; filename*=utf-8''{content_disposition_filename}"<br>        else:<br>            content_disposition = f'{content_disposition_type}; filename="{self.filename}"'<br>        self.headers.setdefault("content-disposition", content_disposition)<br>    self.stat_result = stat_result<br>    if stat_result is not None:<br>        self.set_stat_headers(stat_result)<br>``` |

### `` chunk\_size`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.chunk_size "Permanent link")

```md-code__content
chunk_size = 64 * 1024

```

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.media_type "Permanent link")

```md-code__content
media_type = media_type

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.render "Permanent link")

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

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.FileResponse.delete_cookie "Permanent link")

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

## `` fastapi.responses.HTMLResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse "Permanent link")

```md-code__content
HTMLResponse(
    content=None,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `Response`

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

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.media_type "Permanent link")

```md-code__content
media_type = 'text/html'

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.render "Permanent link")

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

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.HTMLResponse.delete_cookie "Permanent link")

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

## `` fastapi.responses.JSONResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse "Permanent link")

```md-code__content
JSONResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `Response`

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `200` |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |
| `media_type` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `background` | **TYPE:** `BackgroundTask | None`**DEFAULT:** `None` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    content: typing.Any,<br>    status_code: int = 200,<br>    headers: typing.Mapping[str, str] | None = None,<br>    media_type: str | None = None,<br>    background: BackgroundTask | None = None,<br>) -> None:<br>    super().__init__(content, status_code, headers, media_type, background)<br>``` |

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.media_type "Permanent link")

```md-code__content
media_type = 'application/json'

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.render "Permanent link")

```md-code__content
render(content)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `Any` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>``` | ```md-code__content<br>def render(self, content: typing.Any) -> bytes:<br>    return json.dumps(<br>        content,<br>        ensure_ascii=False,<br>        allow_nan=False,<br>        indent=None,<br>        separators=(",", ":"),<br>    ).encode("utf-8")<br>``` |

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.JSONResponse.delete_cookie "Permanent link")

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

## `` fastapi.responses.PlainTextResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse "Permanent link")

```md-code__content
PlainTextResponse(
    content=None,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `Response`

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

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.media_type "Permanent link")

```md-code__content
media_type = 'text/plain'

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.render "Permanent link")

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

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.PlainTextResponse.delete_cookie "Permanent link")

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

## `` fastapi.responses.RedirectResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse "Permanent link")

```md-code__content
RedirectResponse(
    url, status_code=307, headers=None, background=None
)

```

Bases: `Response`

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `str | URL` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `307` |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |
| `background` | **TYPE:** `BackgroundTask | None`**DEFAULT:** `None` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    url: str | URL,<br>    status_code: int = 307,<br>    headers: typing.Mapping[str, str] | None = None,<br>    background: BackgroundTask | None = None,<br>) -> None:<br>    super().__init__(content=b"", status_code=status_code, headers=headers, background=background)<br>    self.headers["location"] = quote(str(url), safe=":/%#?=@[]!$&'()*+,;")<br>``` |

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.media_type "Permanent link")

```md-code__content
media_type = None

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.render "Permanent link")

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

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.RedirectResponse.delete_cookie "Permanent link")

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

## `` fastapi.responses.Response [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response "Permanent link")

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

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.media_type "Permanent link")

```md-code__content
media_type = None

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.render "Permanent link")

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

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.Response.delete_cookie "Permanent link")

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

## `` fastapi.responses.StreamingResponse [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse "Permanent link")

```md-code__content
StreamingResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `Response`

| PARAMETER | DESCRIPTION |
| --- | --- |
| `content` | **TYPE:** `ContentStream` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `200` |
| `headers` | **TYPE:** `Mapping[str, str] | None`**DEFAULT:** `None` |
| `media_type` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `background` | **TYPE:** `BackgroundTask | None`**DEFAULT:** `None` |

Source code in `starlette/responses.py`

|     |     |
| --- | --- |
| ```<br>215<br>216<br>217<br>218<br>219<br>220<br>221<br>222<br>223<br>224<br>225<br>226<br>227<br>228<br>229<br>230<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    content: ContentStream,<br>    status_code: int = 200,<br>    headers: typing.Mapping[str, str] | None = None,<br>    media_type: str | None = None,<br>    background: BackgroundTask | None = None,<br>) -> None:<br>    if isinstance(content, typing.AsyncIterable):<br>        self.body_iterator = content<br>    else:<br>        self.body_iterator = iterate_in_threadpool(content)<br>    self.status_code = status_code<br>    self.media_type = self.media_type if media_type is None else media_type<br>    self.background = background<br>    self.init_headers(headers)<br>``` |

### `` body\_iterator`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.body_iterator "Permanent link")

```md-code__content
body_iterator

```

### `` charset`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.charset "Permanent link")

```md-code__content
charset = 'utf-8'

```

### `` status\_code`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.status_code "Permanent link")

```md-code__content
status_code = status_code

```

### `` media\_type`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.media_type "Permanent link")

```md-code__content
media_type = (
    media_type if media_type is None else media_type
)

```

### `` body`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.body "Permanent link")

```md-code__content
body = render(content)

```

### `` background`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.background "Permanent link")

```md-code__content
background = background

```

### `` headers`property`[¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.headers "Permanent link")

```md-code__content
headers

```

### `` render [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.render "Permanent link")

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

### `` init\_headers [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.init_headers "Permanent link")

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

### `` set\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.set_cookie "Permanent link")

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

### `` delete\_cookie [¶](https://fastapi.tiangolo.com/reference/responses/\#fastapi.responses.StreamingResponse.delete_cookie "Permanent link")

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






Thanks for your feedback!






Thanks for your feedback!


Back to top