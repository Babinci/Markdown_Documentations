[Skip to content](https://fastapi.tiangolo.com/advanced/templates/#templates)

# Templates [¶](https://fastapi.tiangolo.com/advanced/templates/\#templates "Permanent link")

You can use any template engine you want with **FastAPI**.

A common choice is Jinja2, the same one used by Flask and other tools.

There are utilities to configure it easily that you can use directly in your **FastAPI** application (provided by Starlette).

## Install dependencies [¶](https://fastapi.tiangolo.com/advanced/templates/\#install-dependencies "Permanent link")

Make sure you create a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/), activate it, and install `jinja2`:

```

fast →pip install jinja2
```

## Using `Jinja2Templates` [¶](https://fastapi.tiangolo.com/advanced/templates/\#using-jinja2templates "Permanent link")

- Import `Jinja2Templates`.
- Create a `templates` object that you can reuse later.
- Declare a `Request` parameter in the _path operation_ that will return a template.
- Use the `templates` you created to render and return a `TemplateResponse`, pass the name of the template, the request object, and a "context" dictionary with key-value pairs to be used inside of the Jinja2 template.

[Python 3.8+](https://fastapi.tiangolo.com/advanced/templates/#__tabbed_1_1)

```md-code__content
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

```

Note

Before FastAPI 0.108.0, Starlette 0.29.0, the `name` was the first parameter.

Also, before that, in previous versions, the `request` object was passed as part of the key-value pairs in the context for Jinja2.

Tip

By declaring `response_class=HTMLResponse` the docs UI will be able to know that the response will be HTML.

Technical Details

You could also use `from starlette.templating import Jinja2Templates`.

**FastAPI** provides the same `starlette.templating` as `fastapi.templating` just as a convenience for you, the developer. But most of the available responses come directly from Starlette. The same with `Request` and `StaticFiles`.

## Writing templates [¶](https://fastapi.tiangolo.com/advanced/templates/\#writing-templates "Permanent link")

Then you can write a template at `templates/item.html` with, for example:

```md-code__content
<html>
<head>
    <title>Item Details</title>
    <link href="{{ url_for('static', path='/styles.css') }}" rel="stylesheet">
</head>
<body>
    <h1><a href="{{ url_for('read_item', id=id) }}">Item ID: {{ id }}</a></h1>
</body>
</html>

```

### Template Context Values [¶](https://fastapi.tiangolo.com/advanced/templates/\#template-context-values "Permanent link")

In the HTML that contains:

```md-code__content
Item ID: {{ id }}

```

...it will show the `id` taken from the "context" `dict` you passed:

```md-code__content
{"id": id}

```

For example, with an ID of `42`, this would render:

```md-code__content
Item ID: 42

```

### Template `url_for` Arguments [¶](https://fastapi.tiangolo.com/advanced/templates/\#template-url_for-arguments "Permanent link")

You can also use `url_for()` inside of the template, it takes as arguments the same arguments that would be used by your _path operation function_.

So, the section with:

```md-code__content
<a href="{{ url_for('read_item', id=id) }}">

```

...will generate a link to the same URL that would be handled by the _path operation function_ `read_item(id=id)`.

For example, with an ID of `42`, this would render:

```md-code__content
<a href="/items/42">

```

## Templates and static files [¶](https://fastapi.tiangolo.com/advanced/templates/\#templates-and-static-files "Permanent link")

You can also use `url_for()` inside of the template, and use it, for example, with the `StaticFiles` you mounted with the `name="static"`.

```md-code__content
<html>
<head>
    <title>Item Details</title>
    <link href="{{ url_for('static', path='/styles.css') }}" rel="stylesheet">
</head>
<body>
    <h1><a href="{{ url_for('read_item', id=id) }}">Item ID: {{ id }}</a></h1>
</body>
</html>

```

In this example, it would link to a CSS file at `static/styles.css` with:

```md-code__content
h1 {
    color: green;
}

```

And because you are using `StaticFiles`, that CSS file would be served automatically by your **FastAPI** application at the URL `/static/styles.css`.

## More details [¶](https://fastapi.tiangolo.com/advanced/templates/\#more-details "Permanent link")

For more details, including how to test templates, check [Starlette's docs on templates](https://www.starlette.io/templates/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top