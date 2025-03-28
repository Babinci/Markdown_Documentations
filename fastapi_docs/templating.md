[Skip to content](https://fastapi.tiangolo.com/reference/templating/#templating-jinja2templates)

# Templating - `Jinja2Templates` [¶](https://fastapi.tiangolo.com/reference/templating/\#templating-jinja2templates "Permanent link")

You can use the `Jinja2Templates` class to render Jinja templates.

Read more about it in the [FastAPI docs for Templates](https://fastapi.tiangolo.com/advanced/templates/).

You can import it directly from `fastapi.templating`:

```md-code__content
from fastapi.templating import Jinja2Templates

```

## `` fastapi.templating.Jinja2Templates [¶](https://fastapi.tiangolo.com/reference/templating/\#fastapi.templating.Jinja2Templates "Permanent link")

```md-code__content
Jinja2Templates(
    directory: (
        str | PathLike[str] | Sequence[str | PathLike[str]]
    ),
    *,
    context_processors: (
        list[Callable[[Request], dict[str, Any]]] | None
    ) = None,
    **env_options: Any
)

```

```md-code__content
Jinja2Templates(
    *,
    env: Environment,
    context_processors: (
        list[Callable[[Request], dict[str, Any]]] | None
    ) = None
)

```

```md-code__content
Jinja2Templates(
    directory=None,
    *,
    context_processors=None,
    env=None,
    **env_options
)

```

templates = Jinja2Templates("templates")

return templates.TemplateResponse("index.html", {"request": request})

| PARAMETER | DESCRIPTION |
| --- | --- |
| `directory` | **TYPE:** `str | PathLike[str] | Sequence[str | PathLike[str]] | None`**DEFAULT:** `None` |
| `context_processors` | **TYPE:** `list[Callable[[Request], dict[str, Any]]] | None`**DEFAULT:** `None` |
| `env` | **TYPE:** `Environment | None`**DEFAULT:** `None` |
| `**env_options` | **TYPE:** `Any`**DEFAULT:** `{}` |

Source code in `starlette/templating.py`

|     |     |
| --- | --- |
| ```<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    directory: str | PathLike[str] | typing.Sequence[str | PathLike[str]] | None = None,<br>    *,<br>    context_processors: list[typing.Callable[[Request], dict[str, typing.Any]]] | None = None,<br>    env: jinja2.Environment | None = None,<br>    **env_options: typing.Any,<br>) -> None:<br>    if env_options:<br>        warnings.warn(<br>            "Extra environment options are deprecated. Use a preconfigured jinja2.Environment instead.",<br>            DeprecationWarning,<br>        )<br>    assert jinja2 is not None, "jinja2 must be installed to use Jinja2Templates"<br>    assert bool(directory) ^ bool(env), "either 'directory' or 'env' arguments must be passed"<br>    self.context_processors = context_processors or []<br>    if directory is not None:<br>        self.env = self._create_env(directory, **env_options)<br>    elif env is not None:  # pragma: no branch<br>        self.env = env<br>    self._setup_env_defaults(self.env)<br>``` |

### `` context\_processors`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/templating/\#fastapi.templating.Jinja2Templates.context_processors "Permanent link")

```md-code__content
context_processors = context_processors or []

```

### `` env`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/templating/\#fastapi.templating.Jinja2Templates.env "Permanent link")

```md-code__content
env = _create_env(directory, **env_options)

```

### `` get\_template [¶](https://fastapi.tiangolo.com/reference/templating/\#fastapi.templating.Jinja2Templates.get_template "Permanent link")

```md-code__content
get_template(name)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `name` | **TYPE:** `str` |

Source code in `starlette/templating.py`

|     |     |
| --- | --- |
| ```<br>130<br>131<br>``` | ```md-code__content<br>def get_template(self, name: str) -> jinja2.Template:<br>    return self.env.get_template(name)<br>``` |

### `` TemplateResponse [¶](https://fastapi.tiangolo.com/reference/templating/\#fastapi.templating.Jinja2Templates.TemplateResponse "Permanent link")

```md-code__content
TemplateResponse(
    request: Request,
    name: str,
    context: dict[str, Any] | None = None,
    status_code: int = 200,
    headers: Mapping[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> _TemplateResponse

```

```md-code__content
TemplateResponse(
    name: str,
    context: dict[str, Any] | None = None,
    status_code: int = 200,
    headers: Mapping[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> _TemplateResponse

```

```md-code__content
TemplateResponse(*args, **kwargs)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `*args` | **TYPE:** `Any`**DEFAULT:** `()` |
| `**kwargs` | **TYPE:** `Any`**DEFAULT:** `{}` |

Source code in `starlette/templating.py`

|     |     |
| --- | --- |
| ```<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>210<br>211<br>212<br>213<br>214<br>215<br>216<br>``` | ```md-code__content<br>def TemplateResponse(self, *args: typing.Any, **kwargs: typing.Any) -> _TemplateResponse:<br>    if args:<br>        if isinstance(args[0], str):  # the first argument is template name (old style)<br>            warnings.warn(<br>                "The `name` is not the first parameter anymore. "<br>                "The first parameter should be the `Request` instance.\n"<br>                'Replace `TemplateResponse(name, {"request": request})` by `TemplateResponse(request, name)`.',<br>                DeprecationWarning,<br>            )<br>            name = args[0]<br>            context = args[1] if len(args) > 1 else kwargs.get("context", {})<br>            status_code = args[2] if len(args) > 2 else kwargs.get("status_code", 200)<br>            headers = args[2] if len(args) > 2 else kwargs.get("headers")<br>            media_type = args[3] if len(args) > 3 else kwargs.get("media_type")<br>            background = args[4] if len(args) > 4 else kwargs.get("background")<br>            if "request" not in context:<br>                raise ValueError('context must include a "request" key')<br>            request = context["request"]<br>        else:  # the first argument is a request instance (new style)<br>            request = args[0]<br>            name = args[1] if len(args) > 1 else kwargs["name"]<br>            context = args[2] if len(args) > 2 else kwargs.get("context", {})<br>            status_code = args[3] if len(args) > 3 else kwargs.get("status_code", 200)<br>            headers = args[4] if len(args) > 4 else kwargs.get("headers")<br>            media_type = args[5] if len(args) > 5 else kwargs.get("media_type")<br>            background = args[6] if len(args) > 6 else kwargs.get("background")<br>    else:  # all arguments are kwargs<br>        if "request" not in kwargs:<br>            warnings.warn(<br>                "The `TemplateResponse` now requires the `request` argument.\n"<br>                'Replace `TemplateResponse(name, {"context": context})` by `TemplateResponse(request, name)`.',<br>                DeprecationWarning,<br>            )<br>            if "request" not in kwargs.get("context", {}):<br>                raise ValueError('context must include a "request" key')<br>        context = kwargs.get("context", {})<br>        request = kwargs.get("request", context.get("request"))<br>        name = typing.cast(str, kwargs["name"])<br>        status_code = kwargs.get("status_code", 200)<br>        headers = kwargs.get("headers")<br>        media_type = kwargs.get("media_type")<br>        background = kwargs.get("background")<br>    context.setdefault("request", request)<br>    for context_processor in self.context_processors:<br>        context.update(context_processor(request))<br>    template = self.get_template(name)<br>    return _TemplateResponse(<br>        template,<br>        context,<br>        status_code=status_code,<br>        headers=headers,<br>        media_type=media_type,<br>        background=background,<br>    )<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top