[Skip to content](https://fastapi.tiangolo.com/deployment/manually/#run-a-server-manually)

# Run a Server Manually [¶](https://fastapi.tiangolo.com/deployment/manually/\#run-a-server-manually "Permanent link")

## Use the `fastapi run` Command [¶](https://fastapi.tiangolo.com/deployment/manually/\#use-the-fastapi-run-command "Permanent link")

In short, use `fastapi run` to serve your FastAPI application:

```

fast →fastapi run main.p
```

That would work for most of the cases. 😎

You could use that command for example to start your **FastAPI** app in a container, in a server, etc.

## ASGI Servers [¶](https://fastapi.tiangolo.com/deployment/manually/\#asgi-servers "Permanent link")

Let's go a little deeper into the details.

FastAPI uses a standard for building Python web frameworks and servers called ASGI. FastAPI is an ASGI web framework.

The main thing you need to run a **FastAPI** application (or any other ASGI application) in a remote server machine is an ASGI server program like **Uvicorn**, this is the one that comes by default in the `fastapi` command.

There are several alternatives, including:

- [Uvicorn](https://www.uvicorn.org/): a high performance ASGI server.
- [Hypercorn](https://hypercorn.readthedocs.io/): an ASGI server compatible with HTTP/2 and Trio among other features.
- [Daphne](https://github.com/django/daphne): the ASGI server built for Django Channels.
- [Granian](https://github.com/emmett-framework/granian): A Rust HTTP server for Python applications.
- [NGINX Unit](https://unit.nginx.org/howto/fastapi/): NGINX Unit is a lightweight and versatile web application runtime.

## Server Machine and Server Program [¶](https://fastapi.tiangolo.com/deployment/manually/\#server-machine-and-server-program "Permanent link")

There's a small detail about names to keep in mind. 💡

The word " **server**" is commonly used to refer to both the remote/cloud computer (the physical or virtual machine) and also the program that is running on that machine (e.g. Uvicorn).

Just keep in mind that when you read "server" in general, it could refer to one of those two things.

When referring to the remote machine, it's common to call it **server**, but also **machine**, **VM** (virtual machine), **node**. Those all refer to some type of remote machine, normally running Linux, where you run programs.

## Install the Server Program [¶](https://fastapi.tiangolo.com/deployment/manually/\#install-the-server-program "Permanent link")

When you install FastAPI, it comes with a production server, Uvicorn, and you can start it with the `fastapi run` command.

But you can also install an ASGI server manually.

Make sure you create a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/), activate it, and then you can install the server application.

For example, to install Uvicorn:

```

fast →pip install "uvico
```

A similar process would apply to any other ASGI server program.

Tip

By adding the `standard`, Uvicorn will install and use some recommended extra dependencies.

That including `uvloop`, the high-performance drop-in replacement for `asyncio`, that provides the big concurrency performance boost.

When you install FastAPI with something like `pip install "fastapi[standard]"` you already get `uvicorn[standard]` as well.

## Run the Server Program [¶](https://fastapi.tiangolo.com/deployment/manually/\#run-the-server-program "Permanent link")

If you installed an ASGI server manually, you would normally need to pass an import string in a special format for it to import your FastAPI application:

```

fast →uvicorn main:app -
```

Note

The command `uvicorn main:app` refers to:

- `main`: the file `main.py` (the Python "module").
- `app`: the object created inside of `main.py` with the line `app = FastAPI()`.

It is equivalent to:

```md-code__content
from main import app

```

Each alternative ASGI server program would have a similar command, you can read more in their respective documentation.

Warning

Uvicorn and other servers support a `--reload` option that is useful during development.

The `--reload` option consumes much more resources, is more unstable, etc.

It helps a lot during **development**, but you **shouldn't** use it in **production**.

## Deployment Concepts [¶](https://fastapi.tiangolo.com/deployment/manually/\#deployment-concepts "Permanent link")

These examples run the server program (e.g Uvicorn), starting **a single process**, listening on all the IPs ( `0.0.0.0`) on a predefined port (e.g. `80`).

This is the basic idea. But you will probably want to take care of some additional things, like:

- Security - HTTPS
- Running on startup
- Restarts
- Replication (the number of processes running)
- Memory
- Previous steps before starting

I'll tell you more about each of these concepts, how to think about them, and some concrete examples with strategies to handle them in the next chapters. 🚀

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top