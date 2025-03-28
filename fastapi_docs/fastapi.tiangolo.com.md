[Skip to content](https://fastapi.tiangolo.com/#fastapi)

# FastAPI [¶](https://fastapi.tiangolo.com/\#fastapi "Permanent link")

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/)

_FastAPI framework, high performance, easy to learn, fast to code, ready for production_

[![Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**Documentation**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

**Source Code**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:

- **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).
- **Fast to code**: Increase the speed to develop features by about 200% to 300%. \*
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors. \*
- **Intuitive**: Great editor support. Completion everywhere. Less time debugging.
- **Easy**: Designed to be easy to use and learn. Less time reading docs.
- **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- **Robust**: Get production-ready code. With automatic interactive documentation.
- **Standards-based**: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).

\\* estimation based on tests on an internal development team, building production applications.

## Sponsors [¶](https://fastapi.tiangolo.com/\#sponsors "Permanent link")

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![](https://fastapi.tiangolo.com/img/sponsors/platform-sh.png)](https://platform.sh/try-it-now/?utm_source=fastapi-signup&utm_medium=banner&utm_campaign=FastAPI-signup-June-2023 "Build, run and scale your apps on a modern, reliable, and secure PaaS.")[![](https://fastapi.tiangolo.com/img/sponsors/porter.png)](https://www.porter.run/ "Deploy FastAPI on AWS with a few clicks")[![](https://fastapi.tiangolo.com/img/sponsors/bump-sh.svg)](https://bump.sh/fastapi?utm_source=fastapi&utm_medium=referral&utm_campaign=sponsor "Automate FastAPI documentation generation with Bump.sh")[![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![](https://fastapi.tiangolo.com/img/sponsors/coherence.png)](https://www.withcoherence.com/?utm_medium=advertising&utm_source=fastapi&utm_campaign=website "Coherence")[![](https://fastapi.tiangolo.com/img/sponsors/mongodb.png)](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/?utm_campaign=fastapi_framework&utm_source=fastapi_sponsorship&utm_medium=web_referral "Simplify Full Stack Development with FastAPI & MongoDB")[![](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")[![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![](https://fastapi.tiangolo.com/img/sponsors/haystack-fastapi.svg)](https://github.com/deepset-ai/haystack/ "Build powerful search from composable, open source building blocks")[![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/ "Pay as you go for market data")[![](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")

[Other sponsors](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## Opinions [¶](https://fastapi.tiangolo.com/\#opinions "Permanent link")

" _\[...\] I'm using **FastAPI** a ton these days. \[...\] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

" _We adopted the **FastAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. \[for Ludwig\]_"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber** [(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

" _**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! \[built with **FastAPI**\]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** [(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

" _I’m over the moon excited about **FastAPI**. It’s so fun!_"

Brian Okken - **[Python Bytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855) podcast host** [(ref)](https://twitter.com/brianokken/status/1112220079972728832)

* * *

" _Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted **Hug** to be - it's really inspiring to see someone build that._"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator** [(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

" _If you're looking to learn one **modern framework** for building REST APIs, check out **FastAPI** \[...\] It's fast, easy to use and easy to learn \[...\]_"

" _We've switched over to **FastAPI** for our **APIs** \[...\] I think you'll like it \[...\]_"

Ines Montani - Matthew Honnibal - **[Explosion AI](https://explosion.ai/) founders - [spaCy](https://spacy.io/) creators** [(ref)](https://twitter.com/_inesmontani/status/1144173225322143744) \- [(ref)](https://twitter.com/honnibal/status/1144031421859655680)

* * *

" _If anyone is looking to build a production Python API, I would highly recommend **FastAPI**. It is **beautifully designed**, **simple to use** and **highly scalable**, it has become a **key component** in our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer._"

Deon Pillsbury - **Cisco** [(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

## **Typer**, the FastAPI of CLIs [¶](https://fastapi.tiangolo.com/\#typer-the-fastapi-of-clis "Permanent link")

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

If you are building a CLI app to be used in the terminal instead of a web API, check out [**Typer**](https://typer.tiangolo.com/).

**Typer** is FastAPI's little sibling. And it's intended to be the **FastAPI of CLIs**. ⌨️ 🚀

## Requirements [¶](https://fastapi.tiangolo.com/\#requirements "Permanent link")

FastAPI stands on the shoulders of giants:

- [Starlette](https://www.starlette.io/) for the web parts.
- [Pydantic](https://docs.pydantic.dev/) for the data parts.

## Installation [¶](https://fastapi.tiangolo.com/\#installation "Permanent link")

Create and activate a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/) and then install FastAPI:

```

fast →pip install "fas
```

**Note**: Make sure you put `"fastapi[standard]"` in quotes to ensure it works in all terminals.

## Example [¶](https://fastapi.tiangolo.com/\#example "Permanent link")

### Create it [¶](https://fastapi.tiangolo.com/\#create-it "Permanent link")

- Create a file `main.py` with:

```md-code__content
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

Or use `async def`...

If your code uses `async` / `await`, use `async def`:

```md-code__content
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

**Note**:

If you don't know, check the _"In a hurry?"_ section about [`async` and `await` in the docs](https://fastapi.tiangolo.com/async/#in-a-hurry).

### Run it [¶](https://fastapi.tiangolo.com/\#run-it "Permanent link")

Run the server with:

```

fast →fastapi dev main
```

About the command `fastapi dev main.py`...

The command `fastapi dev` reads your `main.py` file, detects the **FastAPI** app in it, and starts a server using [Uvicorn](https://www.uvicorn.org/).

By default, `fastapi dev` will start with auto-reload enabled for local development.

You can read more about it in the [FastAPI CLI docs](https://fastapi.tiangolo.com/fastapi-cli/).

### Check it [¶](https://fastapi.tiangolo.com/\#check-it "Permanent link")

Open your browser at [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery).

You will see the JSON response as:

```md-code__content
{"item_id": 5, "q": "somequery"}

```

You already created an API that:

- Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
- Both _paths_ take `GET` _operations_ (also known as HTTP _methods_).
- The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
- The _path_ `/items/{item_id}` has an optional `str` _query parameter_ `q`.

### Interactive API docs [¶](https://fastapi.tiangolo.com/\#interactive-api-docs "Permanent link")

Now go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API docs [¶](https://fastapi.tiangolo.com/\#alternative-api-docs "Permanent link")

And now, go to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

You will see the alternative automatic documentation (provided by [ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Example upgrade [¶](https://fastapi.tiangolo.com/\#example-upgrade "Permanent link")

Now modify the file `main.py` to receive a body from a `PUT` request.

Declare the body using standard Python types, thanks to Pydantic.

```md-code__content
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

```

The `fastapi dev` server should reload automatically.

### Interactive API docs upgrade [¶](https://fastapi.tiangolo.com/\#interactive-api-docs-upgrade "Permanent link")

Now go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

- The interactive API documentation will be automatically updated, including the new body:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

- Click on the button "Try it out", it allows you to fill the parameters and directly interact with the API:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

- Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Alternative API docs upgrade [¶](https://fastapi.tiangolo.com/\#alternative-api-docs-upgrade "Permanent link")

And now, go to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

- The alternative documentation will also reflect the new query parameter and body:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Recap [¶](https://fastapi.tiangolo.com/\#recap "Permanent link")

In summary, you declare **once** the types of parameters, body, etc. as function parameters.

You do that with standard modern Python types.

You don't have to learn a new syntax, the methods or classes of a specific library, etc.

Just standard **Python**.

For example, for an `int`:

```md-code__content
item_id: int

```

or for a more complex `Item` model:

```md-code__content
item: Item

```

...and with that single declaration you get:

- Editor support, including:
  - Completion.
  - Type checks.
- Validation of data:
  - Automatic and clear errors when the data is invalid.
  - Validation even for deeply nested JSON objects.
- Conversion of input data: coming from the network to Python data and types. Reading from:
  - JSON.
  - Path parameters.
  - Query parameters.
  - Cookies.
  - Headers.
  - Forms.
  - Files.
- Conversion of output data: converting from Python data and types to network data (as JSON):
  - Convert Python types ( `str`, `int`, `float`, `bool`, `list`, etc).
  - `datetime` objects.
  - `UUID` objects.
  - Database models.
  - ...and many more.
- Automatic interactive API documentation, including 2 alternative user interfaces:
  - Swagger UI.
  - ReDoc.

* * *

Coming back to the previous code example, **FastAPI** will:

- Validate that there is an `item_id` in the path for `GET` and `PUT` requests.
- Validate that the `item_id` is of type `int` for `GET` and `PUT` requests.
  - If it is not, the client will see a useful, clear error.
- Check if there is an optional query parameter named `q` (as in `http://127.0.0.1:8000/items/foo?q=somequery`) for `GET` requests.
  - As the `q` parameter is declared with `= None`, it is optional.
  - Without the `None` it would be required (as is the body in the case with `PUT`).
- For `PUT` requests to `/items/{item_id}`, read the body as JSON:
  - Check that it has a required attribute `name` that should be a `str`.
  - Check that it has a required attribute `price` that has to be a `float`.
  - Check that it has an optional attribute `is_offer`, that should be a `bool`, if present.
  - All this would also work for deeply nested JSON objects.
- Convert from and to JSON automatically.
- Document everything with OpenAPI, that can be used by:
  - Interactive documentation systems.
  - Automatic client code generation systems, for many languages.
- Provide 2 interactive documentation web interfaces directly.

* * *

We just scratched the surface, but you already get the idea of how it all works.

Try changing the line with:

```md-code__content
    return {"item_name": item.name, "item_id": item_id}

```

...from:

```md-code__content
        ... "item_name": item.name ...

```

...to:

```md-code__content
        ... "item_price": item.price ...

```

...and see how your editor will auto-complete the attributes and know their types:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

For a more complete example including more features, see the [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/).

**Spoiler alert**: the tutorial - user guide includes:

- Declaration of **parameters** from other different places as: **headers**, **cookies**, **form fields** and **files**.
- How to set **validation constraints** as `maximum_length` or `regex`.
- A very powerful and easy to use **Dependency Injection** system.
- Security and authentication, including support for **OAuth2** with **JWT tokens** and **HTTP Basic** auth.
- More advanced (but equally easy) techniques for declaring **deeply nested JSON models** (thanks to Pydantic).
- **GraphQL** integration with [Strawberry](https://strawberry.rocks/) and other libraries.
- Many extra features (thanks to Starlette) as:
  - **WebSockets**
  - extremely easy tests based on HTTPX and `pytest`
  - **CORS**
  - **Cookie Sessions**
  - ...and more.

## Performance [¶](https://fastapi.tiangolo.com/\#performance "Permanent link")

Independent TechEmpower benchmarks show **FastAPI** applications running under Uvicorn as [one of the fastest Python frameworks available](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7), only below Starlette and Uvicorn themselves (used internally by FastAPI). (\*)

To understand more about it, see the section [Benchmarks](https://fastapi.tiangolo.com/benchmarks/).

## Dependencies [¶](https://fastapi.tiangolo.com/\#dependencies "Permanent link")

FastAPI depends on Pydantic and Starlette.

### `standard` Dependencies [¶](https://fastapi.tiangolo.com/\#standard-dependencies "Permanent link")

When you install FastAPI with `pip install "fastapi[standard]"` it comes with the `standard` group of optional dependencies:

Used by Pydantic:

- [`email-validator`](https://github.com/JoshData/python-email-validator) \- for email validation.

Used by Starlette:

- [`httpx`](https://www.python-httpx.org/) \- Required if you want to use the `TestClient`.
- [`jinja2`](https://jinja.palletsprojects.com/) \- Required if you want to use the default template configuration.
- [`python-multipart`](https://github.com/Kludex/python-multipart) \- Required if you want to support form "parsing", with `request.form()`.

Used by FastAPI / Starlette:

- [`uvicorn`](https://www.uvicorn.org/) \- for the server that loads and serves your application. This includes `uvicorn[standard]`, which includes some dependencies (e.g. `uvloop`) needed for high performance serving.
- `fastapi-cli` \- to provide the `fastapi` command.

### Without `standard` Dependencies [¶](https://fastapi.tiangolo.com/\#without-standard-dependencies "Permanent link")

If you don't want to include the `standard` optional dependencies, you can install with `pip install fastapi` instead of `pip install "fastapi[standard]"`.

### Additional Optional Dependencies [¶](https://fastapi.tiangolo.com/\#additional-optional-dependencies "Permanent link")

There are some additional dependencies you might want to install.

Additional optional Pydantic dependencies:

- [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) \- for settings management.
- [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) \- for extra types to be used with Pydantic.

Additional optional FastAPI dependencies:

- [`orjson`](https://github.com/ijl/orjson) \- Required if you want to use `ORJSONResponse`.
- [`ujson`](https://github.com/esnme/ultrajson) \- Required if you want to use `UJSONResponse`.

## License [¶](https://fastapi.tiangolo.com/\#license "Permanent link")

This project is licensed under the terms of the MIT license.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top