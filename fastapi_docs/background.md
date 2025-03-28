[Skip to content](https://fastapi.tiangolo.com/reference/background/#background-tasks-backgroundtasks)

# Background Tasks - `BackgroundTasks` [¶](https://fastapi.tiangolo.com/reference/background/\#background-tasks-backgroundtasks "Permanent link")

You can declare a parameter in a _path operation function_ or dependency function with the type `BackgroundTasks`, and then you can use it to schedule the execution of background tasks after the response is sent.

You can import it directly from `fastapi`:

```md-code__content
from fastapi import BackgroundTasks

```

## `` fastapi.BackgroundTasks [¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks "Permanent link")

```md-code__content
BackgroundTasks(tasks=None)

```

Bases: `BackgroundTasks`

A collection of background tasks that will be called after a response has been
sent to the client.

Read more about it in the
[FastAPI docs for Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).

#### Example [¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks--example "Permanent link")

```md-code__content
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `tasks` | **TYPE:** `Sequence[BackgroundTask] | None`**DEFAULT:** `None` |

Source code in `starlette/background.py`

|     |     |
| --- | --- |
| ```<br>32<br>33<br>``` | ```md-code__content<br>def __init__(self, tasks: typing.Sequence[BackgroundTask] | None = None):<br>    self.tasks = list(tasks) if tasks else []<br>``` |

### `` func`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks.func "Permanent link")

```md-code__content
func = func

```

### `` args`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks.args "Permanent link")

```md-code__content
args = args

```

### `` kwargs`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks.kwargs "Permanent link")

```md-code__content
kwargs = kwargs

```

### `` is\_async`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks.is_async "Permanent link")

```md-code__content
is_async = is_async_callable(func)

```

### `` tasks`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks.tasks "Permanent link")

```md-code__content
tasks = list(tasks) if tasks else []

```

### `` add\_task [¶](https://fastapi.tiangolo.com/reference/background/\#fastapi.BackgroundTasks.add_task "Permanent link")

```md-code__content
add_task(func, *args, **kwargs)

```

Add a function to be called in the background after the response is sent.

Read more about it in the
[FastAPI docs for Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).

| PARAMETER | DESCRIPTION |
| --- | --- |
| `func` | The function to call after the response is sent.<br>It can be a regular `def` function or an `async def` function.<br>**TYPE:** `Callable[P, Any]` |
| `*args` | **TYPE:** `args`**DEFAULT:** `()` |
| `**kwargs` | **TYPE:** `kwargs`**DEFAULT:** `{}` |

Source code in `fastapi/background.py`

|     |     |
| --- | --- |
| ```<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>``` | ```md-code__content<br>def add_task(<br>    self,<br>    func: Annotated[<br>        Callable[P, Any],<br>        Doc(<br>            """<br>            The function to call after the response is sent.<br>            It can be a regular `def` function or an `async def` function.<br>            """<br>        ),<br>    ],<br>    *args: P.args,<br>    **kwargs: P.kwargs,<br>) -> None:<br>    """<br>    Add a function to be called in the background after the response is sent.<br>    Read more about it in the<br>    [FastAPI docs for Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).<br>    """<br>    return super().add_task(func, *args, **kwargs)<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback!


Back to top