[Skip to content](https://fastapi.tiangolo.com/reference/uploadfile/#uploadfile-class)

# `UploadFile` class [¶](https://fastapi.tiangolo.com/reference/uploadfile/\#uploadfile-class "Permanent link")

You can define _path operation function_ parameters to be of the type `UploadFile` to receive files from the request.

You can import it directly from `fastapi`:

```md-code__content
from fastapi import UploadFile

```

## `` fastapi.UploadFile [¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile "Permanent link")

```md-code__content
UploadFile(file, *, size=None, filename=None, headers=None)

```

Bases: `UploadFile`

A file uploaded in a request.

Define it as a _path operation function_ (or dependency) parameter.

If you are using a regular `def` function, you can use the `upload_file.file`
attribute to access the raw standard Python file (blocking, not async), useful and
needed for non-async code.

Read more about it in the
[FastAPI docs for Request Files](https://fastapi.tiangolo.com/tutorial/request-files/).

#### Example [¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile--example "Permanent link")

```md-code__content
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

```

| PARAMETER | DESCRIPTION |
| --- | --- |
| `file` | **TYPE:** `BinaryIO` |
| `size` | **TYPE:** `int | None`**DEFAULT:** `None` |
| `filename` | **TYPE:** `str | None`**DEFAULT:** `None` |
| `headers` | **TYPE:** `Headers | None`**DEFAULT:** `None` |

Source code in `starlette/datastructures.py`

|     |     |
| --- | --- |
| ```<br>414<br>415<br>416<br>417<br>418<br>419<br>420<br>421<br>422<br>423<br>424<br>425<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    file: typing.BinaryIO,<br>    *,<br>    size: int | None = None,<br>    filename: str | None = None,<br>    headers: Headers | None = None,<br>) -> None:<br>    self.filename = filename<br>    self.file = file<br>    self.size = size<br>    self.headers = headers or Headers()<br>``` |

### `` file`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.file "Permanent link")

```md-code__content
file

```

The standard Python file object (non-async).

### `` filename`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.filename "Permanent link")

```md-code__content
filename

```

The original file name.

### `` size`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.size "Permanent link")

```md-code__content
size

```

The size of the file in bytes.

### `` headers`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.headers "Permanent link")

```md-code__content
headers

```

The headers of the request.

### `` content\_type`instance-attribute`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.content_type "Permanent link")

```md-code__content
content_type

```

The content type of the request, from the headers.

### `` read`async`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.read "Permanent link")

```md-code__content
read(size=-1)

```

Read some bytes from the file.

To be awaitable, compatible with async, this is run in threadpool.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `size` | The number of bytes to read from the file.<br>**TYPE:** `int`**DEFAULT:** `-1` |

Source code in `fastapi/datastructures.py`

|     |     |
| --- | --- |
| ```<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>``` | ```md-code__content<br>async def read(<br>    self,<br>    size: Annotated[<br>        int,<br>        Doc(<br>            """<br>            The number of bytes to read from the file.<br>            """<br>        ),<br>    ] = -1,<br>) -> bytes:<br>    """<br>    Read some bytes from the file.<br>    To be awaitable, compatible with async, this is run in threadpool.<br>    """<br>    return await super().read(size)<br>``` |

### `` write`async`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.write "Permanent link")

```md-code__content
write(data)

```

Write some bytes to the file.

You normally wouldn't use this from a file you read in a request.

To be awaitable, compatible with async, this is run in threadpool.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `data` | The bytes to write to the file.<br>**TYPE:** `bytes` |

Source code in `fastapi/datastructures.py`

|     |     |
| --- | --- |
| ```<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>``` | ```md-code__content<br>async def write(<br>    self,<br>    data: Annotated[<br>        bytes,<br>        Doc(<br>            """<br>            The bytes to write to the file.<br>            """<br>        ),<br>    ],<br>) -> None:<br>    """<br>    Write some bytes to the file.<br>    You normally wouldn't use this from a file you read in a request.<br>    To be awaitable, compatible with async, this is run in threadpool.<br>    """<br>    return await super().write(data)<br>``` |

### `` seek`async`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.seek "Permanent link")

```md-code__content
seek(offset)

```

Move to a position in the file.

Any next read or write will be done from that position.

To be awaitable, compatible with async, this is run in threadpool.

| PARAMETER | DESCRIPTION |
| --- | --- |
| `offset` | The position in bytes to seek to in the file.<br>**TYPE:** `int` |

Source code in `fastapi/datastructures.py`

|     |     |
| --- | --- |
| ```<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>``` | ```md-code__content<br>async def seek(<br>    self,<br>    offset: Annotated[<br>        int,<br>        Doc(<br>            """<br>            The position in bytes to seek to in the file.<br>            """<br>        ),<br>    ],<br>) -> None:<br>    """<br>    Move to a position in the file.<br>    Any next read or write will be done from that position.<br>    To be awaitable, compatible with async, this is run in threadpool.<br>    """<br>    return await super().seek(offset)<br>``` |

### `` close`async`[¶](https://fastapi.tiangolo.com/reference/uploadfile/\#fastapi.UploadFile.close "Permanent link")

```md-code__content
close()

```

Close the file.

To be awaitable, compatible with async, this is run in threadpool.

Source code in `fastapi/datastructures.py`

|     |     |
| --- | --- |
| ```<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>``` | ```md-code__content<br>async def close(self) -> None:<br>    """<br>    Close the file.<br>    To be awaitable, compatible with async, this is run in threadpool.<br>    """<br>    return await super().close()<br>``` |

Was this page helpful?