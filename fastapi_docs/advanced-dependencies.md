[Skip to content](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#advanced-dependencies)

# Advanced Dependencies [¶](https://fastapi.tiangolo.com/advanced/advanced-dependencies/\#advanced-dependencies "Permanent link")

## Parameterized dependencies [¶](https://fastapi.tiangolo.com/advanced/advanced-dependencies/\#parameterized-dependencies "Permanent link")

All the dependencies we have seen are a fixed function or class.

But there could be cases where you want to be able to set parameters on the dependency, without having to declare many different functions or classes.

Let's imagine that we want to have a dependency that checks if the query parameter `q` contains some fixed content.

But we want to be able to parameterize that fixed content.

## A "callable" instance [¶](https://fastapi.tiangolo.com/advanced/advanced-dependencies/\#a-callable-instance "Permanent link")

In Python there's a way to make an instance of a class a "callable".

Not the class itself (which is already a callable), but an instance of that class.

To do that, we declare a method `__call__`:

[Python 3.9+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_1_1)

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

🤓 Other versions and variants

[Python 3.8+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_2_1)[Python 3.8+ - non-Annotated](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_2_2)

```md-code__content
from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

Tip

Prefer to use the `Annotated` version if possible.

```md-code__content
from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}

```

In this case, this `__call__` is what **FastAPI** will use to check for additional parameters and sub-dependencies, and this is what will be called to pass a value to the parameter in your _path operation function_ later.

## Parameterize the instance [¶](https://fastapi.tiangolo.com/advanced/advanced-dependencies/\#parameterize-the-instance "Permanent link")

And now, we can use `__init__` to declare the parameters of the instance that we can use to "parameterize" the dependency:

[Python 3.9+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_3_1)

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

🤓 Other versions and variants

[Python 3.8+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_4_1)[Python 3.8+ - non-Annotated](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_4_2)

```md-code__content
from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

Tip

Prefer to use the `Annotated` version if possible.

```md-code__content
from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}

```

In this case, **FastAPI** won't ever touch or care about `__init__`, we will use it directly in our code.

## Create an instance [¶](https://fastapi.tiangolo.com/advanced/advanced-dependencies/\#create-an-instance "Permanent link")

We could create an instance of this class with:

[Python 3.9+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_5_1)

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

🤓 Other versions and variants

[Python 3.8+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_6_1)[Python 3.8+ - non-Annotated](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_6_2)

```md-code__content
from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

Tip

Prefer to use the `Annotated` version if possible.

```md-code__content
from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}

```

And that way we are able to "parameterize" our dependency, that now has `"bar"` inside of it, as the attribute `checker.fixed_content`.

## Use the instance as a dependency [¶](https://fastapi.tiangolo.com/advanced/advanced-dependencies/\#use-the-instance-as-a-dependency "Permanent link")

Then, we could use this `checker` in a `Depends(checker)`, instead of `Depends(FixedContentQueryChecker)`, because the dependency is the instance, `checker`, not the class itself.

And when solving the dependency, **FastAPI** will call this `checker` like:

```md-code__content
checker(q="somequery")

```

...and pass whatever that returns as the value of the dependency in our _path operation function_ as the parameter `fixed_content_included`:

[Python 3.9+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_7_1)

```md-code__content
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

🤓 Other versions and variants

[Python 3.8+](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_8_1)[Python 3.8+ - non-Annotated](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#__tabbed_8_2)

```md-code__content
from fastapi import Depends, FastAPI
from typing_extensions import Annotated

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: Annotated[bool, Depends(checker)]):
    return {"fixed_content_in_query": fixed_content_included}

```

Tip

Prefer to use the `Annotated` version if possible.

```md-code__content
from fastapi import Depends, FastAPI

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False

checker = FixedContentQueryChecker("bar")

@app.get("/query-checker/")
async def read_query_check(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}

```

Tip

All this might seem contrived. And it might not be very clear how is it useful yet.

These examples are intentionally simple, but show how it all works.

In the chapters about security, there are utility functions that are implemented in this same way.

If you understood all this, you already know how those utility tools for security work underneath.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top