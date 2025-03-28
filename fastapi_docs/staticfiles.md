[Skip to content](https://fastapi.tiangolo.com/reference/staticfiles/#static-files-staticfiles)

# Static Files - `StaticFiles` [¶](https://fastapi.tiangolo.com/reference/staticfiles/\#static-files-staticfiles "Permanent link")

You can use the `StaticFiles` class to serve static files, like JavaScript, CSS, images, etc.

Read more about it in the [FastAPI docs for Static Files](https://fastapi.tiangolo.com/tutorial/static-files/).

You can import it directly from `fastapi.staticfiles`:

```md-code__content
from fastapi.staticfiles import StaticFiles

```

## `` fastapi.staticfiles.StaticFiles [¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles "Permanent link")

```md-code__content
StaticFiles(
    *,
    directory=None,
    packages=None,
    html=False,
    check_dir=True,
    follow_symlink=False
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `directory` | **TYPE:** `PathLike | None`**DEFAULT:** `None` |
| `packages` | **TYPE:** `list[str | tuple[str, str]] | None`**DEFAULT:** `None` |
| `html` | **TYPE:** `bool`**DEFAULT:** `False` |
| `check_dir` | **TYPE:** `bool`**DEFAULT:** `True` |
| `follow_symlink` | **TYPE:** `bool`**DEFAULT:** `False` |

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    directory: PathLike | None = None,<br>    packages: list[str | tuple[str, str]] | None = None,<br>    html: bool = False,<br>    check_dir: bool = True,<br>    follow_symlink: bool = False,<br>) -> None:<br>    self.directory = directory<br>    self.packages = packages<br>    self.all_directories = self.get_directories(directory, packages)<br>    self.html = html<br>    self.config_checked = False<br>    self.follow_symlink = follow_symlink<br>    if check_dir and directory is not None and not os.path.isdir(directory):<br>        raise RuntimeError(f"Directory '{directory}' does not exist")<br>``` |

### `` directory`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.directory "Permanent link")

```md-code__content
directory = directory

```

### `` packages`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.packages "Permanent link")

```md-code__content
packages = packages

```

### `` all\_directories`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.all_directories "Permanent link")

```md-code__content
all_directories = get_directories(directory, packages)

```

### `` html`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.html "Permanent link")

```md-code__content
html = html

```

### `` config\_checked`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.config_checked "Permanent link")

```md-code__content
config_checked = False

```

### `` follow\_symlink`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.follow_symlink "Permanent link")

```md-code__content
follow_symlink = follow_symlink

```

### `` get\_directories [¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.get_directories "Permanent link")

```md-code__content
get_directories(directory=None, packages=None)

```

Given `directory` and `packages` arguments, return a list of all the
directories that should be used for serving static files from.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `directory` | **TYPE:** `PathLike | None`**DEFAULT:** `None` |
| `packages` | **TYPE:** `list[str | tuple[str, str]] | None`**DEFAULT:** `None` |

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>``` | ```md-code__content<br>def get_directories(<br>    self,<br>    directory: PathLike | None = None,<br>    packages: list[str | tuple[str, str]] | None = None,<br>) -> list[PathLike]:<br>    """<br>    Given `directory` and `packages` arguments, return a list of all the<br>    directories that should be used for serving static files from.<br>    """<br>    directories = []<br>    if directory is not None:<br>        directories.append(directory)<br>    for package in packages or []:<br>        if isinstance(package, tuple):<br>            package, statics_dir = package<br>        else:<br>            statics_dir = "statics"<br>        spec = importlib.util.find_spec(package)<br>        assert spec is not None, f"Package {package!r} could not be found."<br>        assert spec.origin is not None, f"Package {package!r} could not be found."<br>        package_directory = os.path.normpath(os.path.join(spec.origin, "..", statics_dir))<br>        assert os.path.isdir(package_directory), (<br>            f"Directory '{statics_dir!r}' in package {package!r} could not be found."<br>        )<br>        directories.append(package_directory)<br>    return directories<br>``` |

### `` get\_path [¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.get_path "Permanent link")

```md-code__content
get_path(scope)

```

Given the ASGI scope, return the `path` string to serve up,
with OS specific path separators, and any '..', '.' components removed.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `scope` | **TYPE:** `Scope` |

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>``` | ```md-code__content<br>def get_path(self, scope: Scope) -> str:<br>    """<br>    Given the ASGI scope, return the `path` string to serve up,<br>    with OS specific path separators, and any '..', '.' components removed.<br>    """<br>    route_path = get_route_path(scope)<br>    return os.path.normpath(os.path.join(*route_path.split("/")))<br>``` |

### `` get\_response`async`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.get_response "Permanent link")

```md-code__content
get_response(path, scope)

```

Returns an HTTP response, given the incoming path, method and request headers.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `path` | **TYPE:** `str` |
| `scope` | **TYPE:** `Scope` |

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>``` | ```md-code__content<br>async def get_response(self, path: str, scope: Scope) -> Response:<br>    """<br>    Returns an HTTP response, given the incoming path, method and request headers.<br>    """<br>    if scope["method"] not in ("GET", "HEAD"):<br>        raise HTTPException(status_code=405)<br>    try:<br>        full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, path)<br>    except PermissionError:<br>        raise HTTPException(status_code=401)<br>    except OSError as exc:<br>        # Filename is too long, so it can't be a valid static file.<br>        if exc.errno == errno.ENAMETOOLONG:<br>            raise HTTPException(status_code=404)<br>        raise exc<br>    if stat_result and stat.S_ISREG(stat_result.st_mode):<br>        # We have a static file to serve.<br>        return self.file_response(full_path, stat_result, scope)<br>    elif stat_result and stat.S_ISDIR(stat_result.st_mode) and self.html:<br>        # We're in HTML mode, and have got a directory URL.<br>        # Check if we have 'index.html' file to serve.<br>        index_path = os.path.join(path, "index.html")<br>        full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, index_path)<br>        if stat_result is not None and stat.S_ISREG(stat_result.st_mode):<br>            if not scope["path"].endswith("/"):<br>                # Directory URLs should redirect to always end in "/".<br>                url = URL(scope=scope)<br>                url = url.replace(path=url.path + "/")<br>                return RedirectResponse(url=url)<br>            return self.file_response(full_path, stat_result, scope)<br>    if self.html:<br>        # Check for '404.html' if we're in HTML mode.<br>        full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, "404.html")<br>        if stat_result and stat.S_ISREG(stat_result.st_mode):<br>            return FileResponse(full_path, stat_result=stat_result, status_code=404)<br>    raise HTTPException(status_code=404)<br>``` |

### `` lookup\_path [¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.lookup_path "Permanent link")

```md-code__content
lookup_path(path)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `path` | **TYPE:** `str` |

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>``` | ```md-code__content<br>def lookup_path(self, path: str) -> tuple[str, os.stat_result | None]:<br>    for directory in self.all_directories:<br>        joined_path = os.path.join(directory, path)<br>        if self.follow_symlink:<br>            full_path = os.path.abspath(joined_path)<br>            directory = os.path.abspath(directory)<br>        else:<br>            full_path = os.path.realpath(joined_path)<br>            directory = os.path.realpath(directory)<br>        if os.path.commonpath([full_path, directory]) != str(directory):<br>            # Don't allow misbehaving clients to break out of the static files directory.<br>            continue<br>        try:<br>            return full_path, os.stat(full_path)<br>        except (FileNotFoundError, NotADirectoryError):<br>            continue<br>    return "", None<br>``` |

### `` file\_response [¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.file_response "Permanent link")

```md-code__content
file_response(
    full_path, stat_result, scope, status_code=200
)

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `full_path` | **TYPE:** `PathLike` |
| `stat_result` | **TYPE:** `stat_result` |
| `scope` | **TYPE:** `Scope` |
| `status_code` | **TYPE:** `int`**DEFAULT:** `200` |

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>``` | ```md-code__content<br>def file_response(<br>    self,<br>    full_path: PathLike,<br>    stat_result: os.stat_result,<br>    scope: Scope,<br>    status_code: int = 200,<br>) -> Response:<br>    request_headers = Headers(scope=scope)<br>    response = FileResponse(full_path, status_code=status_code, stat_result=stat_result)<br>    if self.is_not_modified(response.headers, request_headers):<br>        return NotModifiedResponse(response.headers)<br>    return response<br>``` |

### `` check\_config`async`[¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.check_config "Permanent link")

```md-code__content
check_config()

```

Perform a one-off configuration check that StaticFiles is actually
pointed at a directory, so that we can raise loud errors rather than
just returning 404 responses.

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>``` | ```md-code__content<br>async def check_config(self) -> None:<br>    """<br>    Perform a one-off configuration check that StaticFiles is actually<br>    pointed at a directory, so that we can raise loud errors rather than<br>    just returning 404 responses.<br>    """<br>    if self.directory is None:<br>        return<br>    try:<br>        stat_result = await anyio.to_thread.run_sync(os.stat, self.directory)<br>    except FileNotFoundError:<br>        raise RuntimeError(f"StaticFiles directory '{self.directory}' does not exist.")<br>    if not (stat.S_ISDIR(stat_result.st_mode) or stat.S_ISLNK(stat_result.st_mode)):<br>        raise RuntimeError(f"StaticFiles path '{self.directory}' is not a directory.")<br>``` |

### `` is\_not\_modified [¶](https://fastapi.tiangolo.com/reference/staticfiles/\#fastapi.staticfiles.StaticFiles.is_not_modified "Permanent link")

```md-code__content
is_not_modified(response_headers, request_headers)

```

Given the request and response headers, return `True` if an HTTP
"Not Modified" response could be returned instead.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `response_headers` | **TYPE:** `Headers` |
| `request_headers` | **TYPE:** `Headers` |

Source code in `starlette/staticfiles.py`

|     |     |
| --- | --- |
| ```<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>210<br>211<br>212<br>213<br>214<br>215<br>216<br>217<br>218<br>219<br>220<br>``` | ```md-code__content<br>def is_not_modified(self, response_headers: Headers, request_headers: Headers) -> bool:<br>    """<br>    Given the request and response headers, return `True` if an HTTP<br>    "Not Modified" response could be returned instead.<br>    """<br>    try:<br>        if_none_match = request_headers["if-none-match"]<br>        etag = response_headers["etag"]<br>        if etag in [tag.strip(" W/") for tag in if_none_match.split(",")]:<br>            return True<br>    except KeyError:<br>        pass<br>    try:<br>        if_modified_since = parsedate(request_headers["if-modified-since"])<br>        last_modified = parsedate(response_headers["last-modified"])<br>        if if_modified_since is not None and last_modified is not None and if_modified_since >= last_modified:<br>            return True<br>    except KeyError:<br>        pass<br>    return False<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top