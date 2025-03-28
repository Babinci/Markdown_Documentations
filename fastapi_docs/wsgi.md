[Skip to content](https://fastapi.tiangolo.com/advanced/wsgi/#including-wsgi-flask-django-others)

# Including WSGI - Flask, Django, others [¶](https://fastapi.tiangolo.com/advanced/wsgi/\#including-wsgi-flask-django-others "Permanent link")

You can mount WSGI applications as you saw with [Sub Applications - Mounts](https://fastapi.tiangolo.com/advanced/sub-applications/), [Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/).

For that, you can use the `WSGIMiddleware` and use it to wrap your WSGI application, for example, Flask, Django, etc.

## Using `WSGIMiddleware` [¶](https://fastapi.tiangolo.com/advanced/wsgi/\#using-wsgimiddleware "Permanent link")

You need to import `WSGIMiddleware`.

Then wrap the WSGI (e.g. Flask) app with the middleware.

And then mount that under a path.

[Python 3.8+](https://fastapi.tiangolo.com/advanced/wsgi/#__tabbed_1_1)

```md-code__content
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, request
from markupsafe import escape

flask_app = Flask(__name__)

@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"

app = FastAPI()

@app.get("/v2")
def read_main():
    return {"message": "Hello World"}

app.mount("/v1", WSGIMiddleware(flask_app))

```

## Check it [¶](https://fastapi.tiangolo.com/advanced/wsgi/\#check-it "Permanent link")

Now, every request under the path `/v1/` will be handled by the Flask application.

And the rest will be handled by **FastAPI**.

If you run it and go to [http://localhost:8000/v1/](http://localhost:8000/v1/) you will see the response from Flask:

```md-code__content
Hello, World from Flask!

```

And if you go to [http://localhost:8000/v2](http://localhost:8000/v2) you will see the response from FastAPI:

```md-code__content
{
    "message": "Hello World"
}

```

Was this page helpful?