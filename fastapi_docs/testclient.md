[Skip to content](https://fastapi.tiangolo.com/reference/testclient/#test-client-testclient)

# Test Client - `TestClient` [¶](https://fastapi.tiangolo.com/reference/testclient/\#test-client-testclient "Permanent link")

You can use the `TestClient` class to test FastAPI applications without creating an actual HTTP and socket connection, just communicating directly with the FastAPI code.

Read more about it in the [FastAPI docs for Testing](https://fastapi.tiangolo.com/tutorial/testing/).

You can import it directly from `fastapi.testclient`:

```md-code__content
from fastapi.testclient import TestClient

```

## `` fastapi.testclient.TestClient [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient "Permanent link")

```md-code__content
TestClient(
    app,
    base_url="http://testserver",
    raise_server_exceptions=True,
    root_path="",
    backend="asyncio",
    backend_options=None,
    cookies=None,
    headers=None,
    follow_redirects=True,
    client=("testclient", 50000),
)

```

Bases: `Client`

| PARAMETER | DESCRIPTION |
| --- | --- |
| `app` | **TYPE:** `ASGIApp` |
| `base_url` | **TYPE:** `str`**DEFAULT:** `'http://testserver'` |
| `raise_server_exceptions` | **TYPE:** `bool`**DEFAULT:** `True` |
| `root_path` | **TYPE:** `str`**DEFAULT:** `''` |
| `backend` | **TYPE:** `Literal['asyncio', 'trio']`**DEFAULT:** `'asyncio'` |
| `backend_options` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `dict[str, str] | None`**DEFAULT:** `None` |
| `follow_redirects` | **TYPE:** `bool`**DEFAULT:** `True` |
| `client` | **TYPE:** `tuple[str, int]`**DEFAULT:** `('testclient', 50000)` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>365<br>366<br>367<br>368<br>369<br>370<br>371<br>372<br>373<br>374<br>375<br>376<br>377<br>378<br>379<br>380<br>381<br>382<br>383<br>384<br>385<br>386<br>387<br>388<br>389<br>390<br>391<br>392<br>393<br>394<br>395<br>396<br>397<br>398<br>399<br>400<br>401<br>402<br>403<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    app: ASGIApp,<br>    base_url: str = "http://testserver",<br>    raise_server_exceptions: bool = True,<br>    root_path: str = "",<br>    backend: typing.Literal["asyncio", "trio"] = "asyncio",<br>    backend_options: dict[str, typing.Any] | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    headers: dict[str, str] | None = None,<br>    follow_redirects: bool = True,<br>    client: tuple[str, int] = ("testclient", 50000),<br>) -> None:<br>    self.async_backend = _AsyncBackend(backend=backend, backend_options=backend_options or {})<br>    if _is_asgi3(app):<br>        asgi_app = app<br>    else:<br>        app = typing.cast(ASGI2App, app)  # type: ignore[assignment]<br>        asgi_app = _WrapASGI2(app)  # type: ignore[arg-type]<br>    self.app = asgi_app<br>    self.app_state: dict[str, typing.Any] = {}<br>    transport = _TestClientTransport(<br>        self.app,<br>        portal_factory=self._portal_factory,<br>        raise_server_exceptions=raise_server_exceptions,<br>        root_path=root_path,<br>        app_state=self.app_state,<br>        client=client,<br>    )<br>    if headers is None:<br>        headers = {}<br>    headers.setdefault("user-agent", "testclient")<br>    super().__init__(<br>        base_url=base_url,<br>        headers=headers,<br>        transport=transport,<br>        follow_redirects=follow_redirects,<br>        cookies=cookies,<br>    )<br>``` |

### `` headers`property``writable`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.headers "Permanent link")

```md-code__content
headers

```

HTTP headers to include when sending requests.

### `` follow\_redirects`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.follow_redirects "Permanent link")

```md-code__content
follow_redirects = follow_redirects

```

### `` max\_redirects`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.max_redirects "Permanent link")

```md-code__content
max_redirects = max_redirects

```

### `` is\_closed`property`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.is_closed "Permanent link")

```md-code__content
is_closed

```

Check if the client being closed

### `` trust\_env`property`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.trust_env "Permanent link")

```md-code__content
trust_env

```

### `` timeout`property``writable`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.timeout "Permanent link")

```md-code__content
timeout

```

### `` event\_hooks`property``writable`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.event_hooks "Permanent link")

```md-code__content
event_hooks

```

### `` auth`property``writable`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.auth "Permanent link")

```md-code__content
auth

```

Authentication class used when none is passed at the request-level.

See also [Authentication](https://fastapi.tiangolo.com/quickstart/#authentication).

### `` base\_url`property``writable`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.base_url "Permanent link")

```md-code__content
base_url

```

Base URL to use when sending requests with relative URLs.

### `` cookies`property``writable`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.cookies "Permanent link")

```md-code__content
cookies

```

Cookie values to include when sending requests.

### `` params`property``writable`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.params "Permanent link")

```md-code__content
params

```

Query parameters to include in the URL when sending requests.

### `` task`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.task "Permanent link")

```md-code__content
task

```

### `` portal`class-attribute``instance-attribute`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.portal "Permanent link")

```md-code__content
portal = None

```

### `` async\_backend`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.async_backend "Permanent link")

```md-code__content
async_backend = _AsyncBackend(
    backend=backend, backend_options=backend_options or {}
)

```

### `` app`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.app "Permanent link")

```md-code__content
app = asgi_app

```

### `` app\_state`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.app_state "Permanent link")

```md-code__content
app_state = {}

```

### `` build\_request [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.build_request "Permanent link")

```md-code__content
build_request(
    method,
    url,
    *,
    content=None,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

Build and return a request instance.

- The `params`, `headers` and `cookies` arguments
are merged with any values set on the client.
- The `url` argument is merged with any `base_url` set on the client.

See also: [Request instances](https://fastapi.tiangolo.com/advanced/clients/#request-instances)

| PARAMETER | DESCRIPTION |
| --- | --- |
| `method` | **TYPE:** `str` |
| `url` | **TYPE:** `URL | str` |
| `content` | **TYPE:** `RequestContent | None`**DEFAULT:** `None` |
| `data` | **TYPE:** `RequestData | None`**DEFAULT:** `None` |
| `files` | **TYPE:** `RequestFiles | None`**DEFAULT:** `None` |
| `json` | **TYPE:** `Any | None`**DEFAULT:** `None` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `RequestExtensions | None`**DEFAULT:** `None` |

Source code in `httpx/_client.py`

|     |     |
| --- | --- |
| ```<br>320<br>321<br>322<br>323<br>324<br>325<br>326<br>327<br>328<br>329<br>330<br>331<br>332<br>333<br>334<br>335<br>336<br>337<br>338<br>339<br>340<br>341<br>342<br>343<br>344<br>345<br>346<br>347<br>348<br>349<br>350<br>351<br>352<br>353<br>354<br>355<br>356<br>357<br>358<br>359<br>360<br>361<br>362<br>363<br>364<br>365<br>366<br>367<br>368<br>369<br>``` | ```md-code__content<br>def build_request(<br>    self,<br>    method: str,<br>    url: URL | str,<br>    *,<br>    content: RequestContent | None = None,<br>    data: RequestData | None = None,<br>    files: RequestFiles | None = None,<br>    json: typing.Any | None = None,<br>    params: QueryParamTypes | None = None,<br>    headers: HeaderTypes | None = None,<br>    cookies: CookieTypes | None = None,<br>    timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,<br>    extensions: RequestExtensions | None = None,<br>) -> Request:<br>    """<br>    Build and return a request instance.<br>    * The `params`, `headers` and `cookies` arguments<br>    are merged with any values set on the client.<br>    * The `url` argument is merged with any `base_url` set on the client.<br>    See also: [Request instances][0]<br>    [0]: /advanced/clients/#request-instances<br>    """<br>    url = self._merge_url(url)<br>    headers = self._merge_headers(headers)<br>    cookies = self._merge_cookies(cookies)<br>    params = self._merge_queryparams(params)<br>    extensions = {} if extensions is None else extensions<br>    if "timeout" not in extensions:<br>        timeout = (<br>            self.timeout<br>            if isinstance(timeout, UseClientDefault)<br>            else Timeout(timeout)<br>        )<br>        extensions = dict(**extensions, timeout=timeout.as_dict())<br>    return Request(<br>        method,<br>        url,<br>        content=content,<br>        data=data,<br>        files=files,<br>        json=json,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        extensions=extensions,<br>    )<br>``` |

### `` stream [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.stream "Permanent link")

```md-code__content
stream(
    method,
    url,
    *,
    content=None,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

Alternative to `httpx.request()` that streams the response body
instead of loading it into memory at once.

**Parameters**: See `httpx.request`.

See also: [Streaming Responses](https://fastapi.tiangolo.com/quickstart#streaming-responses)

| PARAMETER | DESCRIPTION |
| --- | --- |
| `method` | **TYPE:** `str` |
| `url` | **TYPE:** `URL | str` |
| `content` | **TYPE:** `RequestContent | None`**DEFAULT:** `None` |
| `data` | **TYPE:** `RequestData | None`**DEFAULT:** `None` |
| `files` | **TYPE:** `RequestFiles | None`**DEFAULT:** `None` |
| `json` | **TYPE:** `Any | None`**DEFAULT:** `None` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault | None`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `RequestExtensions | None`**DEFAULT:** `None` |

| YIELDS | DESCRIPTION |
| --- | --- |
| `Response` |  |

Source code in `httpx/_client.py`

|     |     |
| --- | --- |
| ```<br>839<br>840<br>841<br>842<br>843<br>844<br>845<br>846<br>847<br>848<br>849<br>850<br>851<br>852<br>853<br>854<br>855<br>856<br>857<br>858<br>859<br>860<br>861<br>862<br>863<br>864<br>865<br>866<br>867<br>868<br>869<br>870<br>871<br>872<br>873<br>874<br>875<br>876<br>877<br>878<br>879<br>880<br>881<br>882<br>883<br>884<br>885<br>886<br>887<br>888<br>889<br>``` | ```md-code__content<br>@contextmanager<br>def stream(<br>    self,<br>    method: str,<br>    url: URL | str,<br>    *,<br>    content: RequestContent | None = None,<br>    data: RequestData | None = None,<br>    files: RequestFiles | None = None,<br>    json: typing.Any | None = None,<br>    params: QueryParamTypes | None = None,<br>    headers: HeaderTypes | None = None,<br>    cookies: CookieTypes | None = None,<br>    auth: AuthTypes | UseClientDefault | None = USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,<br>    timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,<br>    extensions: RequestExtensions | None = None,<br>) -> typing.Iterator[Response]:<br>    """<br>    Alternative to `httpx.request()` that streams the response body<br>    instead of loading it into memory at once.<br>    **Parameters**: See `httpx.request`.<br>    See also: [Streaming Responses][0]<br>    [0]: /quickstart#streaming-responses<br>    """<br>    request = self.build_request(<br>        method=method,<br>        url=url,<br>        content=content,<br>        data=data,<br>        files=files,<br>        json=json,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>    response = self.send(<br>        request=request,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        stream=True,<br>    )<br>    try:<br>        yield response<br>    finally:<br>        response.close()<br>``` |

### `` send [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.send "Permanent link")

```md-code__content
send(
    request,
    *,
    stream=False,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT
)

```

Send a request.

The request is sent as-is, unmodified.

Typically you'll want to build one with `Client.build_request()`
so that any client-level configuration is merged into the request,
but passing an explicit `httpx.Request()` is supported as well.

See also: [Request instances](https://fastapi.tiangolo.com/advanced/clients/#request-instances)

| PARAMETER | DESCRIPTION |
| --- | --- |
| `request` | **TYPE:** `Request` |
| `stream` | **TYPE:** `bool`**DEFAULT:** `False` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault | None`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |

Source code in `httpx/_client.py`

|     |     |
| --- | --- |
| ```<br>891<br>892<br>893<br>894<br>895<br>896<br>897<br>898<br>899<br>900<br>901<br>902<br>903<br>904<br>905<br>906<br>907<br>908<br>909<br>910<br>911<br>912<br>913<br>914<br>915<br>916<br>917<br>918<br>919<br>920<br>921<br>922<br>923<br>924<br>925<br>926<br>927<br>928<br>929<br>930<br>931<br>932<br>933<br>934<br>935<br>936<br>937<br>938<br>939<br>940<br>``` | ```md-code__content<br>def send(<br>    self,<br>    request: Request,<br>    *,<br>    stream: bool = False,<br>    auth: AuthTypes | UseClientDefault | None = USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,<br>) -> Response:<br>    """<br>    Send a request.<br>    The request is sent as-is, unmodified.<br>    Typically you'll want to build one with `Client.build_request()`<br>    so that any client-level configuration is merged into the request,<br>    but passing an explicit `httpx.Request()` is supported as well.<br>    See also: [Request instances][0]<br>    [0]: /advanced/clients/#request-instances<br>    """<br>    if self._state == ClientState.CLOSED:<br>        raise RuntimeError("Cannot send a request, as the client has been closed.")<br>    self._state = ClientState.OPENED<br>    follow_redirects = (<br>        self.follow_redirects<br>        if isinstance(follow_redirects, UseClientDefault)<br>        else follow_redirects<br>    )<br>    self._set_timeout(request)<br>    auth = self._build_request_auth(request, auth)<br>    response = self._send_handling_auth(<br>        request,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        history=[],<br>    )<br>    try:<br>        if not stream:<br>            response.read()<br>        return response<br>    except BaseException as exc:<br>        response.close()<br>        raise exc<br>``` |

### `` close [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.close "Permanent link")

```md-code__content
close()

```

Close transport and proxies.

Source code in `httpx/_client.py`

|     |     |
| --- | --- |
| ```<br>1276<br>1277<br>1278<br>1279<br>1280<br>1281<br>1282<br>1283<br>1284<br>1285<br>1286<br>``` | ```md-code__content<br>def close(self) -> None:<br>    """<br>    Close transport and proxies.<br>    """<br>    if self._state != ClientState.CLOSED:<br>        self._state = ClientState.CLOSED<br>        self._transport.close()<br>        for transport in self._mounts.values():<br>            if transport is not None:<br>                transport.close()<br>``` |

### `` request [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.request "Permanent link")

```md-code__content
request(
    method,
    url,
    *,
    content=None,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `method` | **TYPE:** `str` |
| `url` | **TYPE:** `URLTypes` |
| `content` | **TYPE:** `RequestContent | None`**DEFAULT:** `None` |
| `data` | **TYPE:** `_RequestData | None`**DEFAULT:** `None` |
| `files` | **TYPE:** `RequestFiles | None`**DEFAULT:** `None` |
| `json` | **TYPE:** `Any`**DEFAULT:** `None` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>413<br>414<br>415<br>416<br>417<br>418<br>419<br>420<br>421<br>422<br>423<br>424<br>425<br>426<br>427<br>428<br>429<br>430<br>431<br>432<br>433<br>434<br>435<br>436<br>437<br>438<br>439<br>440<br>441<br>442<br>443<br>444<br>445<br>446<br>447<br>448<br>449<br>450<br>451<br>``` | ```md-code__content<br>def request(  # type: ignore[override]<br>    self,<br>    method: str,<br>    url: httpx._types.URLTypes,<br>    *,<br>    content: httpx._types.RequestContent | None = None,<br>    data: _RequestData | None = None,<br>    files: httpx._types.RequestFiles | None = None,<br>    json: typing.Any = None,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    if timeout is not httpx.USE_CLIENT_DEFAULT:<br>        warnings.warn(<br>            "You should not use the 'timeout' argument with the TestClient. "<br>            "See https://github.com/encode/starlette/issues/1108 for more information.",<br>            DeprecationWarning,<br>        )<br>    url = self._merge_url(url)<br>    return super().request(<br>        method,<br>        url,<br>        content=content,<br>        data=data,<br>        files=files,<br>        json=json,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` get [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.get "Permanent link")

```md-code__content
get(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `URLTypes` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>453<br>454<br>455<br>456<br>457<br>458<br>459<br>460<br>461<br>462<br>463<br>464<br>465<br>466<br>467<br>468<br>469<br>470<br>471<br>472<br>473<br>474<br>``` | ```md-code__content<br>def get(  # type: ignore[override]<br>    self,<br>    url: httpx._types.URLTypes,<br>    *,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    return super().get(<br>        url,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` options [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.options "Permanent link")

```md-code__content
options(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `URLTypes` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>476<br>477<br>478<br>479<br>480<br>481<br>482<br>483<br>484<br>485<br>486<br>487<br>488<br>489<br>490<br>491<br>492<br>493<br>494<br>495<br>496<br>497<br>``` | ```md-code__content<br>def options(  # type: ignore[override]<br>    self,<br>    url: httpx._types.URLTypes,<br>    *,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    return super().options(<br>        url,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` head [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.head "Permanent link")

```md-code__content
head(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `URLTypes` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>499<br>500<br>501<br>502<br>503<br>504<br>505<br>506<br>507<br>508<br>509<br>510<br>511<br>512<br>513<br>514<br>515<br>516<br>517<br>518<br>519<br>520<br>``` | ```md-code__content<br>def head(  # type: ignore[override]<br>    self,<br>    url: httpx._types.URLTypes,<br>    *,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    return super().head(<br>        url,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` post [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.post "Permanent link")

```md-code__content
post(
    url,
    *,
    content=None,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `URLTypes` |
| `content` | **TYPE:** `RequestContent | None`**DEFAULT:** `None` |
| `data` | **TYPE:** `_RequestData | None`**DEFAULT:** `None` |
| `files` | **TYPE:** `RequestFiles | None`**DEFAULT:** `None` |
| `json` | **TYPE:** `Any`**DEFAULT:** `None` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>522<br>523<br>524<br>525<br>526<br>527<br>528<br>529<br>530<br>531<br>532<br>533<br>534<br>535<br>536<br>537<br>538<br>539<br>540<br>541<br>542<br>543<br>544<br>545<br>546<br>547<br>548<br>549<br>550<br>551<br>``` | ```md-code__content<br>def post(  # type: ignore[override]<br>    self,<br>    url: httpx._types.URLTypes,<br>    *,<br>    content: httpx._types.RequestContent | None = None,<br>    data: _RequestData | None = None,<br>    files: httpx._types.RequestFiles | None = None,<br>    json: typing.Any = None,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    return super().post(<br>        url,<br>        content=content,<br>        data=data,<br>        files=files,<br>        json=json,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` put [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.put "Permanent link")

```md-code__content
put(
    url,
    *,
    content=None,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `URLTypes` |
| `content` | **TYPE:** `RequestContent | None`**DEFAULT:** `None` |
| `data` | **TYPE:** `_RequestData | None`**DEFAULT:** `None` |
| `files` | **TYPE:** `RequestFiles | None`**DEFAULT:** `None` |
| `json` | **TYPE:** `Any`**DEFAULT:** `None` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>553<br>554<br>555<br>556<br>557<br>558<br>559<br>560<br>561<br>562<br>563<br>564<br>565<br>566<br>567<br>568<br>569<br>570<br>571<br>572<br>573<br>574<br>575<br>576<br>577<br>578<br>579<br>580<br>581<br>582<br>``` | ```md-code__content<br>def put(  # type: ignore[override]<br>    self,<br>    url: httpx._types.URLTypes,<br>    *,<br>    content: httpx._types.RequestContent | None = None,<br>    data: _RequestData | None = None,<br>    files: httpx._types.RequestFiles | None = None,<br>    json: typing.Any = None,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    return super().put(<br>        url,<br>        content=content,<br>        data=data,<br>        files=files,<br>        json=json,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` patch [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.patch "Permanent link")

```md-code__content
patch(
    url,
    *,
    content=None,
    data=None,
    files=None,
    json=None,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `URLTypes` |
| `content` | **TYPE:** `RequestContent | None`**DEFAULT:** `None` |
| `data` | **TYPE:** `_RequestData | None`**DEFAULT:** `None` |
| `files` | **TYPE:** `RequestFiles | None`**DEFAULT:** `None` |
| `json` | **TYPE:** `Any`**DEFAULT:** `None` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>584<br>585<br>586<br>587<br>588<br>589<br>590<br>591<br>592<br>593<br>594<br>595<br>596<br>597<br>598<br>599<br>600<br>601<br>602<br>603<br>604<br>605<br>606<br>607<br>608<br>609<br>610<br>611<br>612<br>613<br>``` | ```md-code__content<br>def patch(  # type: ignore[override]<br>    self,<br>    url: httpx._types.URLTypes,<br>    *,<br>    content: httpx._types.RequestContent | None = None,<br>    data: _RequestData | None = None,<br>    files: httpx._types.RequestFiles | None = None,<br>    json: typing.Any = None,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    return super().patch(<br>        url,<br>        content=content,<br>        data=data,<br>        files=files,<br>        json=json,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` delete [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.delete "Permanent link")

```md-code__content
delete(
    url,
    *,
    params=None,
    headers=None,
    cookies=None,
    auth=USE_CLIENT_DEFAULT,
    follow_redirects=USE_CLIENT_DEFAULT,
    timeout=USE_CLIENT_DEFAULT,
    extensions=None
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `URLTypes` |
| `params` | **TYPE:** `QueryParamTypes | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `HeaderTypes | None`**DEFAULT:** `None` |
| `cookies` | **TYPE:** `CookieTypes | None`**DEFAULT:** `None` |
| `auth` | **TYPE:** `AuthTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `follow_redirects` | **TYPE:** `bool | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `timeout` | **TYPE:** `TimeoutTypes | UseClientDefault`**DEFAULT:** `USE_CLIENT_DEFAULT` |
| `extensions` | **TYPE:** `dict[str, Any] | None`**DEFAULT:** `None` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>615<br>616<br>617<br>618<br>619<br>620<br>621<br>622<br>623<br>624<br>625<br>626<br>627<br>628<br>629<br>630<br>631<br>632<br>633<br>634<br>635<br>636<br>``` | ```md-code__content<br>def delete(  # type: ignore[override]<br>    self,<br>    url: httpx._types.URLTypes,<br>    *,<br>    params: httpx._types.QueryParamTypes | None = None,<br>    headers: httpx._types.HeaderTypes | None = None,<br>    cookies: httpx._types.CookieTypes | None = None,<br>    auth: httpx._types.AuthTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    follow_redirects: bool | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    timeout: httpx._types.TimeoutTypes | httpx._client.UseClientDefault = httpx._client.USE_CLIENT_DEFAULT,<br>    extensions: dict[str, typing.Any] | None = None,<br>) -> httpx.Response:<br>    return super().delete(<br>        url,<br>        params=params,<br>        headers=headers,<br>        cookies=cookies,<br>        auth=auth,<br>        follow_redirects=follow_redirects,<br>        timeout=timeout,<br>        extensions=extensions,<br>    )<br>``` |

### `` websocket\_connect [¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.websocket_connect "Permanent link")

```md-code__content
websocket_connect(url, subprotocols=None, **kwargs)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `url` | **TYPE:** `str` |
| `subprotocols` | **TYPE:** `Sequence[str] | None`**DEFAULT:** `None` |
| `**kwargs` | **TYPE:** `Any`**DEFAULT:** `{}` |

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>638<br>639<br>640<br>641<br>642<br>643<br>644<br>645<br>646<br>647<br>648<br>649<br>650<br>651<br>652<br>653<br>654<br>655<br>656<br>657<br>658<br>659<br>``` | ```md-code__content<br>def websocket_connect(<br>    self,<br>    url: str,<br>    subprotocols: typing.Sequence[str] | None = None,<br>    **kwargs: typing.Any,<br>) -> WebSocketTestSession:<br>    url = urljoin("ws://testserver", url)<br>    headers = kwargs.get("headers", {})<br>    headers.setdefault("connection", "upgrade")<br>    headers.setdefault("sec-websocket-key", "testserver==")<br>    headers.setdefault("sec-websocket-version", "13")<br>    if subprotocols is not None:<br>        headers.setdefault("sec-websocket-protocol", ", ".join(subprotocols))<br>    kwargs["headers"] = headers<br>    try:<br>        super().request("GET", url, **kwargs)<br>    except _Upgrade as exc:<br>        session = exc.session<br>    else:<br>        raise RuntimeError("Expected WebSocket upgrade")  # pragma: no cover<br>    return session<br>``` |

### `` lifespan`async`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.lifespan "Permanent link")

```md-code__content
lifespan()

```

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>693<br>694<br>695<br>696<br>697<br>698<br>``` | ```md-code__content<br>async def lifespan(self) -> None:<br>    scope = {"type": "lifespan", "state": self.app_state}<br>    try:<br>        await self.app(scope, self.stream_receive.receive, self.stream_send.send)<br>    finally:<br>        await self.stream_send.send(None)<br>``` |

### `` wait\_startup`async`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.wait_startup "Permanent link")

```md-code__content
wait_startup()

```

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>700<br>701<br>702<br>703<br>704<br>705<br>706<br>707<br>708<br>709<br>710<br>711<br>712<br>713<br>714<br>715<br>``` | ```md-code__content<br>async def wait_startup(self) -> None:<br>    await self.stream_receive.send({"type": "lifespan.startup"})<br>    async def receive() -> typing.Any:<br>        message = await self.stream_send.receive()<br>        if message is None:<br>            self.task.result()<br>        return message<br>    message = await receive()<br>    assert message["type"] in (<br>        "lifespan.startup.complete",<br>        "lifespan.startup.failed",<br>    )<br>    if message["type"] == "lifespan.startup.failed":<br>        await receive()<br>``` |

### `` wait\_shutdown`async`[¶](https://fastapi.tiangolo.com/reference/testclient/\#fastapi.testclient.TestClient.wait_shutdown "Permanent link")

```md-code__content
wait_shutdown()

```

Source code in `starlette/testclient.py`

|     |     |
| --- | --- |
| ```<br>717<br>718<br>719<br>720<br>721<br>722<br>723<br>724<br>725<br>726<br>727<br>728<br>729<br>730<br>731<br>``` | ```md-code__content<br>async def wait_shutdown(self) -> None:<br>    async def receive() -> typing.Any:<br>        message = await self.stream_send.receive()<br>        if message is None:<br>            self.task.result()<br>        return message<br>    await self.stream_receive.send({"type": "lifespan.shutdown"})<br>    message = await receive()<br>    assert message["type"] in (<br>        "lifespan.shutdown.complete",<br>        "lifespan.shutdown.failed",<br>    )<br>    if message["type"] == "lifespan.shutdown.failed":<br>        await receive()<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top