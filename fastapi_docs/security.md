[Skip to content](https://fastapi.tiangolo.com/reference/security/#security-tools)

# Security Tools [¶](https://fastapi.tiangolo.com/reference/security/\#security-tools "Permanent link")

When you need to declare dependencies with OAuth2 scopes you use `Security()`.

But you still need to define what is the dependable, the callable that you pass as a parameter to `Depends()` or `Security()`.

There are multiple tools that you can use to create those dependables, and they get integrated into OpenAPI so they are shown in the automatic docs UI, they can be used by automatically generated clients and SDKs, etc.

You can import them from `fastapi.security`:

```md-code__content
from fastapi.security import (
    APIKeyCookie,
    APIKeyHeader,
    APIKeyQuery,
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    HTTPDigest,
    OAuth2,
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    OAuth2PasswordRequestFormStrict,
    OpenIdConnect,
    SecurityScopes,
)

```

## API Key Security Schemes [¶](https://fastapi.tiangolo.com/reference/security/\#api-key-security-schemes "Permanent link")

## `` fastapi.security.APIKeyCookie [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyCookie "Permanent link")

```md-code__content
APIKeyCookie(
    *,
    name,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `APIKeyBase`

API key authentication using a cookie.

This defines the name of the cookie that should be provided in the request with
the API key and integrates that into the OpenAPI documentation. It extracts
the key value sent in the cookie automatically and provides it as the dependency
result. But it doesn't define how to set that cookie.

#### Usage [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyCookie--usage "Permanent link")

Create an instance object and use that object as the dependency in `Depends()`.

The dependency result will be a string containing the key value.

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyCookie--example "Permanent link")

```md-code__content
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyCookie

app = FastAPI()

cookie_scheme = APIKeyCookie(name="session")

@app.get("/items/")
async def read_items(session: str = Depends(cookie_scheme)):
    return {"session": session}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `name` | Cookie name.<br>**TYPE:** `str` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if the cookie is not provided, `APIKeyCookie` will<br>automatically cancel the request and send the client an error.<br>If `auto_error` is set to `False`, when the cookie is not available,<br>instead of erroring out, the dependency result will be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, in a cookie or<br>in an HTTP Bearer token).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/api_key.py`

|     |     |
| --- | --- |
| ```<br>235<br>236<br>237<br>238<br>239<br>240<br>241<br>242<br>243<br>244<br>245<br>246<br>247<br>248<br>249<br>250<br>251<br>252<br>253<br>254<br>255<br>256<br>257<br>258<br>259<br>260<br>261<br>262<br>263<br>264<br>265<br>266<br>267<br>268<br>269<br>270<br>271<br>272<br>273<br>274<br>275<br>276<br>277<br>278<br>279<br>280<br>281<br>282<br>283<br>284<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    name: Annotated[str, Doc("Cookie name.")],<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if the cookie is not provided, `APIKeyCookie` will<br>            automatically cancel the request and send the client an error.<br>            If `auto_error` is set to `False`, when the cookie is not available,<br>            instead of erroring out, the dependency result will be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, in a cookie or<br>            in an HTTP Bearer token).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model: APIKey = APIKey(<br>        **{"in": APIKeyIn.cookie},  # type: ignore[arg-type]<br>        name=name,<br>        description=description,<br>    )<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyCookie.model "Permanent link")

```md-code__content
model = APIKey(
    **{"in": cookie}, name=name, description=description
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyCookie.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyCookie.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

### `` check\_api\_key`staticmethod`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyCookie.check_api_key "Permanent link")

```md-code__content
check_api_key(api_key, auto_error)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `api_key` | **TYPE:** `Optional[str]` |
| `auto_error` | **TYPE:** `bool` |

Source code in `fastapi/security/api_key.py`

|     |     |
| --- | --- |
| ```<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>``` | ```md-code__content<br>@staticmethod<br>def check_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]:<br>    if not api_key:<br>        if auto_error:<br>            raise HTTPException(<br>                status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"<br>            )<br>        return None<br>    return api_key<br>``` |

## `` fastapi.security.APIKeyHeader [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyHeader "Permanent link")

```md-code__content
APIKeyHeader(
    *,
    name,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `APIKeyBase`

API key authentication using a header.

This defines the name of the header that should be provided in the request with
the API key and integrates that into the OpenAPI documentation. It extracts
the key value sent in the header automatically and provides it as the dependency
result. But it doesn't define how to send that key to the client.

#### Usage [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyHeader--usage "Permanent link")

Create an instance object and use that object as the dependency in `Depends()`.

The dependency result will be a string containing the key value.

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyHeader--example "Permanent link")

```md-code__content
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader

app = FastAPI()

header_scheme = APIKeyHeader(name="x-key")

@app.get("/items/")
async def read_items(key: str = Depends(header_scheme)):
    return {"key": key}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `name` | Header name.<br>**TYPE:** `str` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if the header is not provided, `APIKeyHeader` will<br>automatically cancel the request and send the client an error.<br>If `auto_error` is set to `False`, when the header is not available,<br>instead of erroring out, the dependency result will be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, in a header or<br>in an HTTP Bearer token).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/api_key.py`

|     |     |
| --- | --- |
| ```<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    name: Annotated[str, Doc("Header name.")],<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if the header is not provided, `APIKeyHeader` will<br>            automatically cancel the request and send the client an error.<br>            If `auto_error` is set to `False`, when the header is not available,<br>            instead of erroring out, the dependency result will be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, in a header or<br>            in an HTTP Bearer token).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model: APIKey = APIKey(<br>        **{"in": APIKeyIn.header},  # type: ignore[arg-type]<br>        name=name,<br>        description=description,<br>    )<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyHeader.model "Permanent link")

```md-code__content
model = APIKey(
    **{"in": header}, name=name, description=description
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyHeader.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyHeader.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

### `` check\_api\_key`staticmethod`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyHeader.check_api_key "Permanent link")

```md-code__content
check_api_key(api_key, auto_error)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `api_key` | **TYPE:** `Optional[str]` |
| `auto_error` | **TYPE:** `bool` |

Source code in `fastapi/security/api_key.py`

|     |     |
| --- | --- |
| ```<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>``` | ```md-code__content<br>@staticmethod<br>def check_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]:<br>    if not api_key:<br>        if auto_error:<br>            raise HTTPException(<br>                status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"<br>            )<br>        return None<br>    return api_key<br>``` |

## `` fastapi.security.APIKeyQuery [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyQuery "Permanent link")

```md-code__content
APIKeyQuery(
    *,
    name,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `APIKeyBase`

API key authentication using a query parameter.

This defines the name of the query parameter that should be provided in the request
with the API key and integrates that into the OpenAPI documentation. It extracts
the key value sent in the query parameter automatically and provides it as the
dependency result. But it doesn't define how to send that API key to the client.

#### Usage [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyQuery--usage "Permanent link")

Create an instance object and use that object as the dependency in `Depends()`.

The dependency result will be a string containing the key value.

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyQuery--example "Permanent link")

```md-code__content
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyQuery

app = FastAPI()

query_scheme = APIKeyQuery(name="api_key")

@app.get("/items/")
async def read_items(api_key: str = Depends(query_scheme)):
    return {"api_key": api_key}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `name` | Query parameter name.<br>**TYPE:** `str` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if the query parameter is not provided, `APIKeyQuery` will<br>automatically cancel the request and send the client an error.<br>If `auto_error` is set to `False`, when the query parameter is not<br>available, instead of erroring out, the dependency result will be<br>`None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, in a query<br>parameter or in an HTTP Bearer token).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/api_key.py`

|     |     |
| --- | --- |
| ```<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    name: Annotated[<br>        str,<br>        Doc("Query parameter name."),<br>    ],<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if the query parameter is not provided, `APIKeyQuery` will<br>            automatically cancel the request and send the client an error.<br>            If `auto_error` is set to `False`, when the query parameter is not<br>            available, instead of erroring out, the dependency result will be<br>            `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, in a query<br>            parameter or in an HTTP Bearer token).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model: APIKey = APIKey(<br>        **{"in": APIKeyIn.query},  # type: ignore[arg-type]<br>        name=name,<br>        description=description,<br>    )<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyQuery.model "Permanent link")

```md-code__content
model = APIKey(
    **{"in": query}, name=name, description=description
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyQuery.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyQuery.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

### `` check\_api\_key`staticmethod`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.APIKeyQuery.check_api_key "Permanent link")

```md-code__content
check_api_key(api_key, auto_error)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `api_key` | **TYPE:** `Optional[str]` |
| `auto_error` | **TYPE:** `bool` |

Source code in `fastapi/security/api_key.py`

|     |     |
| --- | --- |
| ```<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>``` | ```md-code__content<br>@staticmethod<br>def check_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]:<br>    if not api_key:<br>        if auto_error:<br>            raise HTTPException(<br>                status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"<br>            )<br>        return None<br>    return api_key<br>``` |

## HTTP Authentication Schemes [¶](https://fastapi.tiangolo.com/reference/security/\#http-authentication-schemes "Permanent link")

## `` fastapi.security.HTTPBasic [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasic "Permanent link")

```md-code__content
HTTPBasic(
    *,
    scheme_name=None,
    realm=None,
    description=None,
    auto_error=True
)

```

Bases: `HTTPBase`

HTTP Basic authentication.

#### Usage [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasic--usage "Permanent link")

Create an instance object and use that object as the dependency in `Depends()`.

The dependency result will be an `HTTPBasicCredentials` object containing the
`username` and the `password`.

Read more about it in the
[FastAPI docs for HTTP Basic Auth](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/).

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasic--example "Permanent link")

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `realm` | HTTP Basic authentication realm.<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if the HTTP Basic authentication is not provided (a<br>header), `HTTPBasic` will automatically cancel the request and send the<br>client an error.<br>If `auto_error` is set to `False`, when the HTTP Basic authentication<br>is not available, instead of erroring out, the dependency result will<br>be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, in HTTP Basic<br>authentication or in an HTTP Bearer token).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/http.py`

|     |     |
| --- | --- |
| ```<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    realm: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            HTTP Basic authentication realm.<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if the HTTP Basic authentication is not provided (a<br>            header), `HTTPBasic` will automatically cancel the request and send the<br>            client an error.<br>            If `auto_error` is set to `False`, when the HTTP Basic authentication<br>            is not available, instead of erroring out, the dependency result will<br>            be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, in HTTP Basic<br>            authentication or in an HTTP Bearer token).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model = HTTPBaseModel(scheme="basic", description=description)<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.realm = realm<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasic.model "Permanent link")

```md-code__content
model = HTTPBase(scheme='basic', description=description)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasic.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` realm`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasic.realm "Permanent link")

```md-code__content
realm = realm

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasic.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

## `` fastapi.security.HTTPBearer [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBearer "Permanent link")

```md-code__content
HTTPBearer(
    *,
    bearerFormat=None,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `HTTPBase`

HTTP Bearer token authentication.

#### Usage [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBearer--usage "Permanent link")

Create an instance object and use that object as the dependency in `Depends()`.

The dependency result will be an `HTTPAuthorizationCredentials` object containing
the `scheme` and the `credentials`.

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBearer--example "Permanent link")

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()

security = HTTPBearer()

@app.get("/users/me")
def read_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
    return {"scheme": credentials.scheme, "credentials": credentials.credentials}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `bearerFormat` | Bearer token format.<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if the HTTP Bearer token is not provided (in an<br>`Authorization` header), `HTTPBearer` will automatically cancel the<br>request and send the client an error.<br>If `auto_error` is set to `False`, when the HTTP Bearer token<br>is not available, instead of erroring out, the dependency result will<br>be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, in an HTTP<br>Bearer token or in a cookie).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/http.py`

|     |     |
| --- | --- |
| ```<br>252<br>253<br>254<br>255<br>256<br>257<br>258<br>259<br>260<br>261<br>262<br>263<br>264<br>265<br>266<br>267<br>268<br>269<br>270<br>271<br>272<br>273<br>274<br>275<br>276<br>277<br>278<br>279<br>280<br>281<br>282<br>283<br>284<br>285<br>286<br>287<br>288<br>289<br>290<br>291<br>292<br>293<br>294<br>295<br>296<br>297<br>298<br>299<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    bearerFormat: Annotated[Optional[str], Doc("Bearer token format.")] = None,<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if the HTTP Bearer token is not provided (in an<br>            `Authorization` header), `HTTPBearer` will automatically cancel the<br>            request and send the client an error.<br>            If `auto_error` is set to `False`, when the HTTP Bearer token<br>            is not available, instead of erroring out, the dependency result will<br>            be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, in an HTTP<br>            Bearer token or in a cookie).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model = HTTPBearerModel(bearerFormat=bearerFormat, description=description)<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBearer.model "Permanent link")

```md-code__content
model = HTTPBearer(
    bearerFormat=bearerFormat, description=description
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBearer.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBearer.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

## `` fastapi.security.HTTPDigest [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPDigest "Permanent link")

```md-code__content
HTTPDigest(
    *, scheme_name=None, description=None, auto_error=True
)

```

Bases: `HTTPBase`

HTTP Digest authentication.

#### Usage [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPDigest--usage "Permanent link")

Create an instance object and use that object as the dependency in `Depends()`.

The dependency result will be an `HTTPAuthorizationCredentials` object containing
the `scheme` and the `credentials`.

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPDigest--example "Permanent link")

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPAuthorizationCredentials, HTTPDigest

app = FastAPI()

security = HTTPDigest()

@app.get("/users/me")
def read_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
    return {"scheme": credentials.scheme, "credentials": credentials.credentials}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if the HTTP Digest is not provided, `HTTPDigest` will<br>automatically cancel the request and send the client an error.<br>If `auto_error` is set to `False`, when the HTTP Digest is not<br>available, instead of erroring out, the dependency result will<br>be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, in HTTP<br>Digest or in a cookie).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/http.py`

|     |     |
| --- | --- |
| ```<br>356<br>357<br>358<br>359<br>360<br>361<br>362<br>363<br>364<br>365<br>366<br>367<br>368<br>369<br>370<br>371<br>372<br>373<br>374<br>375<br>376<br>377<br>378<br>379<br>380<br>381<br>382<br>383<br>384<br>385<br>386<br>387<br>388<br>389<br>390<br>391<br>392<br>393<br>394<br>395<br>396<br>397<br>398<br>399<br>400<br>401<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if the HTTP Digest is not provided, `HTTPDigest` will<br>            automatically cancel the request and send the client an error.<br>            If `auto_error` is set to `False`, when the HTTP Digest is not<br>            available, instead of erroring out, the dependency result will<br>            be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, in HTTP<br>            Digest or in a cookie).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model = HTTPBaseModel(scheme="digest", description=description)<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPDigest.model "Permanent link")

```md-code__content
model = HTTPBase(scheme='digest', description=description)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPDigest.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPDigest.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

## HTTP Credentials [¶](https://fastapi.tiangolo.com/reference/security/\#http-credentials "Permanent link")

## `` fastapi.security.HTTPAuthorizationCredentials [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPAuthorizationCredentials "Permanent link")

Bases: `BaseModel`

The HTTP authorization credentials in the result of using `HTTPBearer` or
`HTTPDigest` in a dependency.

The HTTP authorization header value is split by the first space.

The first part is the `scheme`, the second part is the `credentials`.

For example, in an HTTP Bearer token scheme, the client will send a header
like:

```md-code__content
Authorization: Bearer deadbeef12346

```

In this case:

- `scheme` will have the value `"Bearer"`
- `credentials` will have the value `"deadbeef12346"`

### `` scheme`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPAuthorizationCredentials.scheme "Permanent link")

```md-code__content
scheme

```

The HTTP authorization scheme extracted from the header value.

### `` credentials`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPAuthorizationCredentials.credentials "Permanent link")

```md-code__content
credentials

```

The HTTP authorization credentials extracted from the header value.

## `` fastapi.security.HTTPBasicCredentials [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasicCredentials "Permanent link")

Bases: `BaseModel`

The HTTP Basic credentials given as the result of using `HTTPBasic` in a
dependency.

Read more about it in the
[FastAPI docs for HTTP Basic Auth](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/).

### `` username`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasicCredentials.username "Permanent link")

```md-code__content
username

```

The HTTP Basic username.

### `` password`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.HTTPBasicCredentials.password "Permanent link")

```md-code__content
password

```

The HTTP Basic password.

## OAuth2 Authentication [¶](https://fastapi.tiangolo.com/reference/security/\#oauth2-authentication "Permanent link")

## `` fastapi.security.OAuth2 [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2 "Permanent link")

```md-code__content
OAuth2(
    *,
    flows=OAuthFlows(),
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `SecurityBase`

This is the base class for OAuth2 authentication, an instance of it would be used
as a dependency. All other OAuth2 classes inherit from it and customize it for
each OAuth2 flow.

You normally would not create a new class inheriting from it but use one of the
existing subclasses, and maybe compose them if you want to support multiple flows.

Read more about it in the
[FastAPI docs for Security](https://fastapi.tiangolo.com/tutorial/security/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `flows` | The dictionary of OAuth2 flows.<br>**TYPE:** `Union[OAuthFlows, Dict[str, Dict[str, Any]]]`**DEFAULT:** `OAuthFlows()` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if no HTTP Authorization header is provided, required for<br>OAuth2 authentication, it will automatically cancel the request and<br>send the client an error.<br>If `auto_error` is set to `False`, when the HTTP Authorization header<br>is not available, instead of erroring out, the dependency result will<br>be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, with OAuth2<br>or in a cookie).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/oauth2.py`

|     |     |
| --- | --- |
| ```<br>321<br>322<br>323<br>324<br>325<br>326<br>327<br>328<br>329<br>330<br>331<br>332<br>333<br>334<br>335<br>336<br>337<br>338<br>339<br>340<br>341<br>342<br>343<br>344<br>345<br>346<br>347<br>348<br>349<br>350<br>351<br>352<br>353<br>354<br>355<br>356<br>357<br>358<br>359<br>360<br>361<br>362<br>363<br>364<br>365<br>366<br>367<br>368<br>369<br>370<br>371<br>372<br>373<br>374<br>375<br>376<br>377<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    flows: Annotated[<br>        Union[OAuthFlowsModel, Dict[str, Dict[str, Any]]],<br>        Doc(<br>            """<br>            The dictionary of OAuth2 flows.<br>            """<br>        ),<br>    ] = OAuthFlowsModel(),<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if no HTTP Authorization header is provided, required for<br>            OAuth2 authentication, it will automatically cancel the request and<br>            send the client an error.<br>            If `auto_error` is set to `False`, when the HTTP Authorization header<br>            is not available, instead of erroring out, the dependency result will<br>            be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, with OAuth2<br>            or in a cookie).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model = OAuth2Model(<br>        flows=cast(OAuthFlowsModel, flows), description=description<br>    )<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2.model "Permanent link")

```md-code__content
model = OAuth2(
    flows=cast(OAuthFlows, flows), description=description
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

## `` fastapi.security.OAuth2AuthorizationCodeBearer [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2AuthorizationCodeBearer "Permanent link")

```md-code__content
OAuth2AuthorizationCodeBearer(
    authorizationUrl,
    tokenUrl,
    refreshUrl=None,
    scheme_name=None,
    scopes=None,
    description=None,
    auto_error=True,
)

```

Bases: `OAuth2`

OAuth2 flow for authentication using a bearer token obtained with an OAuth2 code
flow. An instance of it would be used as a dependency.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `authorizationUrl` | **TYPE:** `str` |
| `tokenUrl` | The URL to obtain the OAuth2 token.<br>**TYPE:** `str` |
| `refreshUrl` | The URL to refresh the token and obtain a new one.<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `scopes` | The OAuth2 scopes that would be required by the _path operations_ that<br>use this dependency.<br>**TYPE:** `Optional[Dict[str, str]]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if no HTTP Authorization header is provided, required for<br>OAuth2 authentication, it will automatically cancel the request and<br>send the client an error.<br>If `auto_error` is set to `False`, when the HTTP Authorization header<br>is not available, instead of erroring out, the dependency result will<br>be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, with OAuth2<br>or in a cookie).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/oauth2.py`

|     |     |
| --- | --- |
| ```<br>494<br>495<br>496<br>497<br>498<br>499<br>500<br>501<br>502<br>503<br>504<br>505<br>506<br>507<br>508<br>509<br>510<br>511<br>512<br>513<br>514<br>515<br>516<br>517<br>518<br>519<br>520<br>521<br>522<br>523<br>524<br>525<br>526<br>527<br>528<br>529<br>530<br>531<br>532<br>533<br>534<br>535<br>536<br>537<br>538<br>539<br>540<br>541<br>542<br>543<br>544<br>545<br>546<br>547<br>548<br>549<br>550<br>551<br>552<br>553<br>554<br>555<br>556<br>557<br>558<br>559<br>560<br>561<br>562<br>563<br>564<br>565<br>566<br>567<br>568<br>569<br>570<br>571<br>572<br>573<br>574<br>575<br>576<br>577<br>578<br>579<br>580<br>581<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    authorizationUrl: str,<br>    tokenUrl: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The URL to obtain the OAuth2 token.<br>            """<br>        ),<br>    ],<br>    refreshUrl: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            The URL to refresh the token and obtain a new one.<br>            """<br>        ),<br>    ] = None,<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    scopes: Annotated[<br>        Optional[Dict[str, str]],<br>        Doc(<br>            """<br>            The OAuth2 scopes that would be required by the *path operations* that<br>            use this dependency.<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if no HTTP Authorization header is provided, required for<br>            OAuth2 authentication, it will automatically cancel the request and<br>            send the client an error.<br>            If `auto_error` is set to `False`, when the HTTP Authorization header<br>            is not available, instead of erroring out, the dependency result will<br>            be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, with OAuth2<br>            or in a cookie).<br>            """<br>        ),<br>    ] = True,<br>):<br>    if not scopes:<br>        scopes = {}<br>    flows = OAuthFlowsModel(<br>        authorizationCode=cast(<br>            Any,<br>            {<br>                "authorizationUrl": authorizationUrl,<br>                "tokenUrl": tokenUrl,<br>                "refreshUrl": refreshUrl,<br>                "scopes": scopes,<br>            },<br>        )<br>    )<br>    super().__init__(<br>        flows=flows,<br>        scheme_name=scheme_name,<br>        description=description,<br>        auto_error=auto_error,<br>    )<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2AuthorizationCodeBearer.model "Permanent link")

```md-code__content
model = OAuth2(
    flows=cast(OAuthFlows, flows), description=description
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2AuthorizationCodeBearer.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2AuthorizationCodeBearer.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

## `` fastapi.security.OAuth2PasswordBearer [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordBearer "Permanent link")

```md-code__content
OAuth2PasswordBearer(
    tokenUrl,
    scheme_name=None,
    scopes=None,
    description=None,
    auto_error=True,
)

```

Bases: `OAuth2`

OAuth2 flow for authentication using a bearer token obtained with a password.
An instance of it would be used as a dependency.

Read more about it in the
[FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `tokenUrl` | The URL to obtain the OAuth2 token. This would be the _path operation_<br>that has `OAuth2PasswordRequestForm` as a dependency.<br>**TYPE:** `str` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `scopes` | The OAuth2 scopes that would be required by the _path operations_ that<br>use this dependency.<br>**TYPE:** `Optional[Dict[str, str]]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if no HTTP Authorization header is provided, required for<br>OAuth2 authentication, it will automatically cancel the request and<br>send the client an error.<br>If `auto_error` is set to `False`, when the HTTP Authorization header<br>is not available, instead of erroring out, the dependency result will<br>be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, with OAuth2<br>or in a cookie).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/oauth2.py`

|     |     |
| --- | --- |
| ```<br>400<br>401<br>402<br>403<br>404<br>405<br>406<br>407<br>408<br>409<br>410<br>411<br>412<br>413<br>414<br>415<br>416<br>417<br>418<br>419<br>420<br>421<br>422<br>423<br>424<br>425<br>426<br>427<br>428<br>429<br>430<br>431<br>432<br>433<br>434<br>435<br>436<br>437<br>438<br>439<br>440<br>441<br>442<br>443<br>444<br>445<br>446<br>447<br>448<br>449<br>450<br>451<br>452<br>453<br>454<br>455<br>456<br>457<br>458<br>459<br>460<br>461<br>462<br>463<br>464<br>465<br>466<br>467<br>468<br>469<br>470<br>471<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    tokenUrl: Annotated[<br>        str,<br>        Doc(<br>            """<br>            The URL to obtain the OAuth2 token. This would be the *path operation*<br>            that has `OAuth2PasswordRequestForm` as a dependency.<br>            """<br>        ),<br>    ],<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    scopes: Annotated[<br>        Optional[Dict[str, str]],<br>        Doc(<br>            """<br>            The OAuth2 scopes that would be required by the *path operations* that<br>            use this dependency.<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if no HTTP Authorization header is provided, required for<br>            OAuth2 authentication, it will automatically cancel the request and<br>            send the client an error.<br>            If `auto_error` is set to `False`, when the HTTP Authorization header<br>            is not available, instead of erroring out, the dependency result will<br>            be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, with OAuth2<br>            or in a cookie).<br>            """<br>        ),<br>    ] = True,<br>):<br>    if not scopes:<br>        scopes = {}<br>    flows = OAuthFlowsModel(<br>        password=cast(Any, {"tokenUrl": tokenUrl, "scopes": scopes})<br>    )<br>    super().__init__(<br>        flows=flows,<br>        scheme_name=scheme_name,<br>        description=description,<br>        auto_error=auto_error,<br>    )<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordBearer.model "Permanent link")

```md-code__content
model = OAuth2(
    flows=cast(OAuthFlows, flows), description=description
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordBearer.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordBearer.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

## OAuth2 Password Form [¶](https://fastapi.tiangolo.com/reference/security/\#oauth2-password-form "Permanent link")

## `` fastapi.security.OAuth2PasswordRequestForm [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm "Permanent link")

```md-code__content
OAuth2PasswordRequestForm(
    *,
    grant_type=None,
    username,
    password,
    scope="",
    client_id=None,
    client_secret=None
)

```

This is a dependency class to collect the `username` and `password` as form data
for an OAuth2 password flow.

The OAuth2 specification dictates that for a password flow the data should be
collected using form data (instead of JSON) and that it should have the specific
fields `username` and `password`.

All the initialization parameters are extracted from the request.

Read more about it in the
[FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm--example "Permanent link")

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    data = {}
    data["scopes"] = []
    for scope in form_data.scopes:
        data["scopes"].append(scope)
    if form_data.client_id:
        data["client_id"] = form_data.client_id
    if form_data.client_secret:
        data["client_secret"] = form_data.client_secret
    return data

```

Note that for OAuth2 the scope `items:read` is a single scope in an opaque string.
You could have custom internal logic to separate it by colon characters ( `:`) or
similar, and get the two parts `items` and `read`. Many applications do that to
group and organize permissions, you could do it as well in your application, just
know that that it is application specific, it's not part of the specification.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `grant_type` | The OAuth2 spec says it is required and MUST be the fixed string<br>"password". Nevertheless, this dependency class is permissive and<br>allows not passing it. If you want to enforce it, use instead the<br>`OAuth2PasswordRequestFormStrict` dependency.<br>**TYPE:** `Union[str, None]`**DEFAULT:** `None` |
| `username` | `username` string. The OAuth2 spec requires the exact field name<br>`username`.<br>**TYPE:** `str` |
| `password` | `password` string. The OAuth2 spec requires the exact field name<br>\`password".<br>**TYPE:** `str` |
| `scope` | A single string with actually several scopes separated by spaces. Each<br>scope is also a string.<br>For example, a single string with:<br>\`\`\`python<br>"items:read items:write users:read profile openid"<br>\`\`\`\`<br>would represent the scopes:<br>- `items:read`<br>- `items:write`<br>- `users:read`<br>- `profile`<br>- `openid`<br>**TYPE:** `str`**DEFAULT:** `''` |
| `client_id` | If there's a `client_id`, it can be sent as part of the form fields.<br>But the OAuth2 specification recommends sending the `client_id` and<br>`client_secret` (if any) using HTTP Basic auth.<br>**TYPE:** `Union[str, None]`**DEFAULT:** `None` |
| `client_secret` | If there's a `client_password` (and a `client_id`), they can be sent<br>as part of the form fields. But the OAuth2 specification recommends<br>sending the `client_id` and `client_secret` (if any) using HTTP Basic<br>auth.<br>**TYPE:** `Union[str, None]`**DEFAULT:** `None` |

Source code in `fastapi/security/oauth2.py`

|     |     |
| --- | --- |
| ```<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>``` | `````md-code__content<br>def __init__(<br>    self,<br>    *,<br>    grant_type: Annotated[<br>        Union[str, None],<br>        Form(pattern="^password$"),<br>        Doc(<br>            """<br>            The OAuth2 spec says it is required and MUST be the fixed string<br>            "password". Nevertheless, this dependency class is permissive and<br>            allows not passing it. If you want to enforce it, use instead the<br>            `OAuth2PasswordRequestFormStrict` dependency.<br>            """<br>        ),<br>    ] = None,<br>    username: Annotated[<br>        str,<br>        Form(),<br>        Doc(<br>            """<br>            `username` string. The OAuth2 spec requires the exact field name<br>            `username`.<br>            """<br>        ),<br>    ],<br>    password: Annotated[<br>        str,<br>        Form(),<br>        Doc(<br>            """<br>            `password` string. The OAuth2 spec requires the exact field name<br>            `password".<br>            """<br>        ),<br>    ],<br>    scope: Annotated[<br>        str,<br>        Form(),<br>        Doc(<br>            """<br>            A single string with actually several scopes separated by spaces. Each<br>            scope is also a string.<br>            For example, a single string with:<br>            ```python<br>            "items:read items:write users:read profile openid"<br>            ````<br>            would represent the scopes:<br>            * `items:read`<br>            * `items:write`<br>            * `users:read`<br>            * `profile`<br>            * `openid`<br>            """<br>        ),<br>    ] = "",<br>    client_id: Annotated[<br>        Union[str, None],<br>        Form(),<br>        Doc(<br>            """<br>            If there's a `client_id`, it can be sent as part of the form fields.<br>            But the OAuth2 specification recommends sending the `client_id` and<br>            `client_secret` (if any) using HTTP Basic auth.<br>            """<br>        ),<br>    ] = None,<br>    client_secret: Annotated[<br>        Union[str, None],<br>        Form(),<br>        Doc(<br>            """<br>            If there's a `client_password` (and a `client_id`), they can be sent<br>            as part of the form fields. But the OAuth2 specification recommends<br>            sending the `client_id` and `client_secret` (if any) using HTTP Basic<br>            auth.<br>            """<br>        ),<br>    ] = None,<br>):<br>    self.grant_type = grant_type<br>    self.username = username<br>    self.password = password<br>    self.scopes = scope.split()<br>    self.client_id = client_id<br>    self.client_secret = client_secret<br>````` |

### `` grant\_type`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm.grant_type "Permanent link")

```md-code__content
grant_type = grant_type

```

### `` username`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm.username "Permanent link")

```md-code__content
username = username

```

### `` password`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm.password "Permanent link")

```md-code__content
password = password

```

### `` scopes`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm.scopes "Permanent link")

```md-code__content
scopes = split()

```

### `` client\_id`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm.client_id "Permanent link")

```md-code__content
client_id = client_id

```

### `` client\_secret`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestForm.client_secret "Permanent link")

```md-code__content
client_secret = client_secret

```

## `` fastapi.security.OAuth2PasswordRequestFormStrict [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict "Permanent link")

```md-code__content
OAuth2PasswordRequestFormStrict(
    grant_type,
    username,
    password,
    scope="",
    client_id=None,
    client_secret=None,
)

```

Bases: `OAuth2PasswordRequestForm`

This is a dependency class to collect the `username` and `password` as form data
for an OAuth2 password flow.

The OAuth2 specification dictates that for a password flow the data should be
collected using form data (instead of JSON) and that it should have the specific
fields `username` and `password`.

All the initialization parameters are extracted from the request.

The only difference between `OAuth2PasswordRequestFormStrict` and
`OAuth2PasswordRequestForm` is that `OAuth2PasswordRequestFormStrict` requires the
client to send the form field `grant_type` with the value `"password"`, which
is required in the OAuth2 specification (it seems that for no particular reason),
while for `OAuth2PasswordRequestForm` `grant_type` is optional.

Read more about it in the
[FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).

#### Example [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict--example "Permanent link")

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestFormStrict, Depends()]):
    data = {}
    data["scopes"] = []
    for scope in form_data.scopes:
        data["scopes"].append(scope)
    if form_data.client_id:
        data["client_id"] = form_data.client_id
    if form_data.client_secret:
        data["client_secret"] = form_data.client_secret
    return data

```

Note that for OAuth2 the scope `items:read` is a single scope in an opaque string.
You could have custom internal logic to separate it by colon characters ( `:`) or
similar, and get the two parts `items` and `read`. Many applications do that to
group and organize permissions, you could do it as well in your application, just
know that that it is application specific, it's not part of the specification.

the OAuth2 spec says it is required and MUST be the fixed string "password".

This dependency is strict about it. If you want to be permissive, use instead the
OAuth2PasswordRequestForm dependency class.

username: username string. The OAuth2 spec requires the exact field name "username".
password: password string. The OAuth2 spec requires the exact field name "password".
scope: Optional string. Several scopes (each one a string) separated by spaces. E.g.
"items:read items:write users:read profile openid"
client\_id: optional string. OAuth2 recommends sending the client\_id and client\_secret (if any)
using HTTP Basic auth, as: client\_id:client\_secret
client\_secret: optional string. OAuth2 recommends sending the client\_id and client\_secret (if any)
using HTTP Basic auth, as: client\_id:client\_secret

| PARAMETER | DESCRIPTION |
| --- | --- |
| `grant_type` | The OAuth2 spec says it is required and MUST be the fixed string<br>"password". This dependency is strict about it. If you want to be<br>permissive, use instead the `OAuth2PasswordRequestForm` dependency<br>class.<br>**TYPE:** `str` |
| `username` | `username` string. The OAuth2 spec requires the exact field name<br>`username`.<br>**TYPE:** `str` |
| `password` | `password` string. The OAuth2 spec requires the exact field name<br>\`password".<br>**TYPE:** `str` |
| `scope` | A single string with actually several scopes separated by spaces. Each<br>scope is also a string.<br>For example, a single string with:<br>\`\`\`python<br>"items:read items:write users:read profile openid"<br>\`\`\`\`<br>would represent the scopes:<br>- `items:read`<br>- `items:write`<br>- `users:read`<br>- `profile`<br>- `openid`<br>**TYPE:** `str`**DEFAULT:** `''` |
| `client_id` | If there's a `client_id`, it can be sent as part of the form fields.<br>But the OAuth2 specification recommends sending the `client_id` and<br>`client_secret` (if any) using HTTP Basic auth.<br>**TYPE:** `Union[str, None]`**DEFAULT:** `None` |
| `client_secret` | If there's a `client_password` (and a `client_id`), they can be sent<br>as part of the form fields. But the OAuth2 specification recommends<br>sending the `client_id` and `client_secret` (if any) using HTTP Basic<br>auth.<br>**TYPE:** `Union[str, None]`**DEFAULT:** `None` |

Source code in `fastapi/security/oauth2.py`

|     |     |
| --- | --- |
| ```<br>216<br>217<br>218<br>219<br>220<br>221<br>222<br>223<br>224<br>225<br>226<br>227<br>228<br>229<br>230<br>231<br>232<br>233<br>234<br>235<br>236<br>237<br>238<br>239<br>240<br>241<br>242<br>243<br>244<br>245<br>246<br>247<br>248<br>249<br>250<br>251<br>252<br>253<br>254<br>255<br>256<br>257<br>258<br>259<br>260<br>261<br>262<br>263<br>264<br>265<br>266<br>267<br>268<br>269<br>270<br>271<br>272<br>273<br>274<br>275<br>276<br>277<br>278<br>279<br>280<br>281<br>282<br>283<br>284<br>285<br>286<br>287<br>288<br>289<br>290<br>291<br>292<br>293<br>294<br>295<br>296<br>297<br>298<br>299<br>300<br>301<br>302<br>303<br>304<br>305<br>``` | `````md-code__content<br>def __init__(<br>    self,<br>    grant_type: Annotated[<br>        str,<br>        Form(pattern="^password$"),<br>        Doc(<br>            """<br>            The OAuth2 spec says it is required and MUST be the fixed string<br>            "password". This dependency is strict about it. If you want to be<br>            permissive, use instead the `OAuth2PasswordRequestForm` dependency<br>            class.<br>            """<br>        ),<br>    ],<br>    username: Annotated[<br>        str,<br>        Form(),<br>        Doc(<br>            """<br>            `username` string. The OAuth2 spec requires the exact field name<br>            `username`.<br>            """<br>        ),<br>    ],<br>    password: Annotated[<br>        str,<br>        Form(),<br>        Doc(<br>            """<br>            `password` string. The OAuth2 spec requires the exact field name<br>            `password".<br>            """<br>        ),<br>    ],<br>    scope: Annotated[<br>        str,<br>        Form(),<br>        Doc(<br>            """<br>            A single string with actually several scopes separated by spaces. Each<br>            scope is also a string.<br>            For example, a single string with:<br>            ```python<br>            "items:read items:write users:read profile openid"<br>            ````<br>            would represent the scopes:<br>            * `items:read`<br>            * `items:write`<br>            * `users:read`<br>            * `profile`<br>            * `openid`<br>            """<br>        ),<br>    ] = "",<br>    client_id: Annotated[<br>        Union[str, None],<br>        Form(),<br>        Doc(<br>            """<br>            If there's a `client_id`, it can be sent as part of the form fields.<br>            But the OAuth2 specification recommends sending the `client_id` and<br>            `client_secret` (if any) using HTTP Basic auth.<br>            """<br>        ),<br>    ] = None,<br>    client_secret: Annotated[<br>        Union[str, None],<br>        Form(),<br>        Doc(<br>            """<br>            If there's a `client_password` (and a `client_id`), they can be sent<br>            as part of the form fields. But the OAuth2 specification recommends<br>            sending the `client_id` and `client_secret` (if any) using HTTP Basic<br>            auth.<br>            """<br>        ),<br>    ] = None,<br>):<br>    super().__init__(<br>        grant_type=grant_type,<br>        username=username,<br>        password=password,<br>        scope=scope,<br>        client_id=client_id,<br>        client_secret=client_secret,<br>    )<br>````` |

### `` grant\_type`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict.grant_type "Permanent link")

```md-code__content
grant_type = grant_type

```

### `` username`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict.username "Permanent link")

```md-code__content
username = username

```

### `` password`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict.password "Permanent link")

```md-code__content
password = password

```

### `` scopes`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict.scopes "Permanent link")

```md-code__content
scopes = split()

```

### `` client\_id`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict.client_id "Permanent link")

```md-code__content
client_id = client_id

```

### `` client\_secret`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OAuth2PasswordRequestFormStrict.client_secret "Permanent link")

```md-code__content
client_secret = client_secret

```

## OAuth2 Security Scopes in Dependencies [¶](https://fastapi.tiangolo.com/reference/security/\#oauth2-security-scopes-in-dependencies "Permanent link")

## `` fastapi.security.SecurityScopes [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.SecurityScopes "Permanent link")

```md-code__content
SecurityScopes(scopes=None)

```

This is a special class that you can define in a parameter in a dependency to
obtain the OAuth2 scopes required by all the dependencies in the same chain.

This way, multiple dependencies can have different scopes, even when used in the
same _path operation_. And with this, you can access all the scopes required in
all those dependencies in a single place.

Read more about it in the
[FastAPI docs for OAuth2 scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `scopes` | This will be filled by FastAPI.<br>**TYPE:** `Optional[List[str]]`**DEFAULT:** `None` |

Source code in `fastapi/security/oauth2.py`

|     |     |
| --- | --- |
| ```<br>611<br>612<br>613<br>614<br>615<br>616<br>617<br>618<br>619<br>620<br>621<br>622<br>623<br>624<br>625<br>626<br>627<br>628<br>629<br>630<br>631<br>632<br>633<br>634<br>635<br>636<br>637<br>638<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    scopes: Annotated[<br>        Optional[List[str]],<br>        Doc(<br>            """<br>            This will be filled by FastAPI.<br>            """<br>        ),<br>    ] = None,<br>):<br>    self.scopes: Annotated[<br>        List[str],<br>        Doc(<br>            """<br>            The list of all the scopes required by dependencies.<br>            """<br>        ),<br>    ] = scopes or []<br>    self.scope_str: Annotated[<br>        str,<br>        Doc(<br>            """<br>            All the scopes required by all the dependencies in a single string<br>            separated by spaces, as defined in the OAuth2 specification.<br>            """<br>        ),<br>    ] = " ".join(self.scopes)<br>``` |

### `` scopes`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.SecurityScopes.scopes "Permanent link")

```md-code__content
scopes = scopes or []

```

The list of all the scopes required by dependencies.

### `` scope\_str`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.SecurityScopes.scope_str "Permanent link")

```md-code__content
scope_str = join(scopes)

```

All the scopes required by all the dependencies in a single string
separated by spaces, as defined in the OAuth2 specification.

## OpenID Connect [¶](https://fastapi.tiangolo.com/reference/security/\#openid-connect "Permanent link")

## `` fastapi.security.OpenIdConnect [¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OpenIdConnect "Permanent link")

```md-code__content
OpenIdConnect(
    *,
    openIdConnectUrl,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `SecurityBase`

OpenID Connect authentication class. An instance of it would be used as a
dependency.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `openIdConnectUrl` | The OpenID Connect URL.<br>**TYPE:** `str` |
| `scheme_name` | Security scheme name.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `description` | Security scheme description.<br>It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>**TYPE:** `Optional[str]`**DEFAULT:** `None` |
| `auto_error` | By default, if no HTTP Authorization header is provided, required for<br>OpenID Connect authentication, it will automatically cancel the request<br>and send the client an error.<br>If `auto_error` is set to `False`, when the HTTP Authorization header<br>is not available, instead of erroring out, the dependency result will<br>be `None`.<br>This is useful when you want to have optional authentication.<br>It is also useful when you want to have authentication that can be<br>provided in one of multiple optional ways (for example, with OpenID<br>Connect or in a cookie).<br>**TYPE:** `bool`**DEFAULT:** `True` |

Source code in `fastapi/security/open_id_connect_url.py`

|     |     |
| --- | --- |
| ```<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    openIdConnectUrl: Annotated[<br>        str,<br>        Doc(<br>            """<br>        The OpenID Connect URL.<br>        """<br>        ),<br>    ],<br>    scheme_name: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme name.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    description: Annotated[<br>        Optional[str],<br>        Doc(<br>            """<br>            Security scheme description.<br>            It will be included in the generated OpenAPI (e.g. visible at `/docs`).<br>            """<br>        ),<br>    ] = None,<br>    auto_error: Annotated[<br>        bool,<br>        Doc(<br>            """<br>            By default, if no HTTP Authorization header is provided, required for<br>            OpenID Connect authentication, it will automatically cancel the request<br>            and send the client an error.<br>            If `auto_error` is set to `False`, when the HTTP Authorization header<br>            is not available, instead of erroring out, the dependency result will<br>            be `None`.<br>            This is useful when you want to have optional authentication.<br>            It is also useful when you want to have authentication that can be<br>            provided in one of multiple optional ways (for example, with OpenID<br>            Connect or in a cookie).<br>            """<br>        ),<br>    ] = True,<br>):<br>    self.model = OpenIdConnectModel(<br>        openIdConnectUrl=openIdConnectUrl, description=description<br>    )<br>    self.scheme_name = scheme_name or self.__class__.__name__<br>    self.auto_error = auto_error<br>``` |

### `` model`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OpenIdConnect.model "Permanent link")

```md-code__content
model = OpenIdConnect(
    openIdConnectUrl=openIdConnectUrl,
    description=description,
)

```

### `` scheme\_name`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OpenIdConnect.scheme_name "Permanent link")

```md-code__content
scheme_name = scheme_name or __name__

```

### `` auto\_error`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/security/\#fastapi.security.OpenIdConnect.auto_error "Permanent link")

```md-code__content
auto_error = auto_error

```

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top