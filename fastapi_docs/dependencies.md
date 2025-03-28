[Skip to content](https://fastapi.tiangolo.com/reference/dependencies/#dependencies-depends-and-security)

# Dependencies - `Depends()` and `Security()` [¶](https://fastapi.tiangolo.com/reference/dependencies/\#dependencies-depends-and-security "Permanent link")

## `Depends()` [¶](https://fastapi.tiangolo.com/reference/dependencies/\#depends "Permanent link")

Dependencies are handled mainly with the special function `Depends()` that takes a callable.

Here is the reference for it and its parameters.

You can import it directly from `fastapi`:

```md-code__content
from fastapi import Depends

```

## `` fastapi.Depends [¶](https://fastapi.tiangolo.com/reference/dependencies/\#fastapi.Depends "Permanent link")

```md-code__content
Depends(dependency=None, *, use_cache=True)

```

Declare a FastAPI dependency.

It takes a single "dependable" callable (like a function).

Don't call it directly, FastAPI will call it for you.

Read more about it in the
[FastAPI docs for Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/).

**Example**

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `dependency` | A "dependable" callable (like a function).<br>Don't call it directly, FastAPI will call it for you, just pass the object<br>directly.<br>**TYPE:** `Optional[Callable[..., Any]]`**DEFAULT:** `None` |
| `use_cache` | By default, after a dependency is called the first time in a request, if<br>the dependency is declared again for the rest of the request (for example<br>if the dependency is needed by several dependencies), the value will be<br>re-used for the rest of the request.<br>Set `use_cache` to `False` to disable this behavior and ensure the<br>dependency is called again (if declared more than once) in the same request.<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/param_functions.py`

|     |     |
| --- | --- |
| ```<br>2220<br>2221<br>2222<br>2223<br>2224<br>2225<br>2226<br>2227<br>2228<br>2229<br>2230<br>2231<br>2232<br>2233<br>2234<br>2235<br>2236<br>2237<br>2238<br>2239<br>2240<br>2241<br>2242<br>2243<br>2244<br>2245<br>2246<br>2247<br>2248<br>2249<br>2250<br>2251<br>2252<br>2253<br>2254<br>2255<br>2256<br>2257<br>2258<br>2259<br>2260<br>2261<br>2262<br>2263<br>2264<br>2265<br>2266<br>2267<br>2268<br>2269<br>2270<br>2271<br>2272<br>2273<br>2274<br>2275<br>2276<br>2277<br>``` | ````md-code__content<br>def Depends(  # noqa: N802<br>    dependency: Annotated[<br>        Optional[Callable[..., Any]],<br>        Doc(<br>            """<br>            A "dependable" callable (like a function).<br>            Don't call it directly, FastAPI will call it for you, just pass the object<br>            directly.<br>            """<br>        ),<br>    ] = None,<br>    *,<br>    use_cache: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, after a dependency is called the first time in a request, if<br>            the dependency is declared again for the rest of the request (for example<br>            if the dependency is needed by several dependencies), the value will be<br>            re-used for the rest of the request.<br>            Set `use_cache` to `False` to disable this behavior and ensure the<br>            dependency is called again (if declared more than once) in the same request.<br>            """<br>        ),<br>    ] = True,<br>) -> Any:<br>    """<br>    Declare a FastAPI dependency.<br>    It takes a single "dependable" callable (like a function).<br>    Don't call it directly, FastAPI will call it for you.<br>    Read more about it in the<br>    [FastAPI docs for Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/).<br>    **Example**<br>    ```python<br>    from typing import Annotated<br>    from fastapi import Depends, FastAPI<br>    app = FastAPI()<br>    async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):<br>        return {"q": q, "skip": skip, "limit": limit}<br>    @app.get("/items/")<br>    async def read_items(commons: Annotated[dict, Depends(common_parameters)]):<br>        return commons<br>    ```<br>    """<br>    return params.Depends(dependency=dependency, use_cache=use_cache)<br>```` |

## `Security()` [¶](https://fastapi.tiangolo.com/reference/dependencies/\#security "Permanent link")

For many scenarios, you can handle security (authorization, authentication, etc.) with dependencies, using `Depends()`.

But when you want to also declare OAuth2 scopes, you can use `Security()` instead of `Depends()`.

You can import `Security()` directly from `fastapi`:

```md-code__content
from fastapi import Security

```

## `` fastapi.Security [¶](https://fastapi.tiangolo.com/reference/dependencies/\#fastapi.Security "Permanent link")

```md-code__content
Security(dependency=None, *, scopes=None, use_cache=True)

```

Declare a FastAPI Security dependency.

The only difference with a regular dependency is that it can declare OAuth2
scopes that will be integrated with OpenAPI and the automatic UI docs (by default
at `/docs`).

It takes a single "dependable" callable (like a function).

Don't call it directly, FastAPI will call it for you.

Read more about it in the
[FastAPI docs for Security](https://fastapi.tiangolo.com/tutorial/security/) and
in the
[FastAPI docs for OAuth2 scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).

**Example**

```md-code__content
from typing import Annotated

from fastapi import Security, FastAPI

from .db import User
from .security import get_current_active_user

app = FastAPI()

@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])]
):
    return [{"item_id": "Foo", "owner": current_user.username}]

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `dependency` | A "dependable" callable (like a function).<br>Don't call it directly, FastAPI will call it for you, just pass the object<br>directly.<br>**TYPE:** `Optional[Callable[..., Any]]`**DEFAULT:** `None` |
| `scopes` | OAuth2 scopes required for the _path operation_ that uses this Security<br>dependency.<br>The term "scope" comes from the OAuth2 specification, it seems to be<br>intentionally vague and interpretable. It normally refers to permissions,<br>in cases to roles.<br>These scopes are integrated with OpenAPI (and the API docs at `/docs`).<br>So they are visible in the OpenAPI specification.<br>)<br>**TYPE:** `Optional[Sequence[str]]`**DEFAULT:** `None` |
| `use_cache` | By default, after a dependency is called the first time in a request, if<br>the dependency is declared again for the rest of the request (for example<br>if the dependency is needed by several dependencies), the value will be<br>re-used for the rest of the request.<br>Set `use_cache` to `False` to disable this behavior and ensure the<br>dependency is called again (if declared more than once) in the same request.<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/param_functions.py`

|     |     |
| --- | --- |
| ```<br>2280<br>2281<br>2282<br>2283<br>2284<br>2285<br>2286<br>2287<br>2288<br>2289<br>2290<br>2291<br>2292<br>2293<br>2294<br>2295<br>2296<br>2297<br>2298<br>2299<br>2300<br>2301<br>2302<br>2303<br>2304<br>2305<br>2306<br>2307<br>2308<br>2309<br>2310<br>2311<br>2312<br>2313<br>2314<br>2315<br>2316<br>2317<br>2318<br>2319<br>2320<br>2321<br>2322<br>2323<br>2324<br>2325<br>2326<br>2327<br>2328<br>2329<br>2330<br>2331<br>2332<br>2333<br>2334<br>2335<br>2336<br>2337<br>2338<br>2339<br>2340<br>2341<br>2342<br>2343<br>2344<br>2345<br>2346<br>2347<br>2348<br>2349<br>2350<br>2351<br>2352<br>2353<br>2354<br>2355<br>2356<br>2357<br>2358<br>2359<br>2360<br>``` | ````md-code__content<br>def Security(  # noqa: N802<br>    dependency: Annotated[<br>        Optional[Callable[..., Any]],<br>        Doc(<br>            """<br>            A "dependable" callable (like a function).<br>            Don't call it directly, FastAPI will call it for you, just pass the object<br>            directly.<br>            """<br>        ),<br>    ] = None,<br>    *,<br>    scopes: Annotated[<br>        Optional[Sequence[str]],<br>        Doc(<br>            """<br>            OAuth2 scopes required for the *path operation* that uses this Security<br>            dependency.<br>            The term "scope" comes from the OAuth2 specification, it seems to be<br>            intentionally vague and interpretable. It normally refers to permissions,<br>            in cases to roles.<br>            These scopes are integrated with OpenAPI (and the API docs at `/docs`).<br>            So they are visible in the OpenAPI specification.<br>            )<br>            """<br>        ),<br>    ] = None,<br>    use_cache: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, after a dependency is called the first time in a request, if<br>            the dependency is declared again for the rest of the request (for example<br>            if the dependency is needed by several dependencies), the value will be<br>            re-used for the rest of the request.<br>            Set `use_cache` to `False` to disable this behavior and ensure the<br>            dependency is called again (if declared more than once) in the same request.<br>            """<br>        ),<br>    ] = True,<br>) -> Any:<br>    """<br>    Declare a FastAPI Security dependency.<br>    The only difference with a regular dependency is that it can declare OAuth2<br>    scopes that will be integrated with OpenAPI and the automatic UI docs (by default<br>    at `/docs`).<br>    It takes a single "dependable" callable (like a function).<br>    Don't call it directly, FastAPI will call it for you.<br>    Read more about it in the<br>    [FastAPI docs for Security](https://fastapi.tiangolo.com/tutorial/security/) and<br>    in the<br>    [FastAPI docs for OAuth2 scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).<br>    **Example**<br>    ```python<br>    from typing import Annotated<br>    from fastapi import Security, FastAPI<br>    from .db import User<br>    from .security import get_current_active_user<br>    app = FastAPI()<br>    @app.get("/users/me/items/")<br>    async def read_own_items(<br>        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])]<br>    ):<br>        return [{"item_id": "Foo", "owner": current_user.username}]<br>    ```<br>    """<br>    return params.Security(dependency=dependency, scopes=scopes, use_cache=use_cache)<br>```` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top