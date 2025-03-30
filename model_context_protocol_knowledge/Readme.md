# Model Context Protocol (MCP)

<div align="center">

<strong>A standardized protocol for LLM applications to connect with external data sources and tools</strong>

[![Protocol Revision](https://img.shields.io/badge/Protocol%20Revision-2024--11--05-blue)](https://spec.modelcontextprotocol.io)
[![Documentation](https://img.shields.io/badge/docs-modelcontextprotocol.io-blue.svg)](https://modelcontextprotocol.io)
[![GitHub Discussions](https://img.shields.io/github/discussions/modelcontextprotocol/python-sdk)](https://github.com/modelcontextprotocol/python-sdk/discussions)

</div>

## Table of Contents

- [Model Context Protocol (MCP)](#model-context-protocol-mcp)
  - [Overview](#overview)
  - [Protocol Specification](#protocol-specification)
    - [Messages](#messages)
    - [Transports](#transports)
    - [Connection Lifecycle](#connection-lifecycle)
    - [Protocol Layers](#protocol-layers)
    - [Architecture](#architecture)
    - [Core Components](#core-components)
    - [Server Features](#server-features)
      - [Prompts](#prompts)
      - [Resources](#resources)
      - [Tools](#tools)
    - [Client Features](#client-features)
      - [Sampling](#sampling)
      - [Roots](#roots)
    - [Design Principles](#design-principles)
    - [Security and Trust & Safety](#security-and-trust--safety)
  - [MCP Python SDK](#mcp-python-sdk)
    - [Installation](#installation)
    - [Quickstart](#quickstart)
    - [Core Concepts](#core-concepts)
      - [Server](#server)
      - [Resources](#resources-1)
      - [Tools](#tools-1)
      - [Prompts](#prompts-1)
      - [Images](#images)
      - [Context](#context)
    - [Running Your Server](#running-your-server)
    - [Examples](#examples)
    - [Advanced Usage](#advanced-usage)
  - [Documentation](#documentation)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

[Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.

MCP provides a standardized way for applications to:

- Share contextual information with language models
- Expose tools and capabilities to AI systems
- Build composable integrations and workflows

The protocol uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 messages to establish communication between:

- **Hosts**: LLM applications that initiate connections
- **Clients**: Connectors within the host application
- **Servers**: Services that provide context and capabilities

MCP takes inspiration from the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which standardizes how to add support for programming languages across a whole ecosystem of development tools. Similarly, MCP standardizes how to integrate additional context and tools into the ecosystem of AI applications.

## Protocol Specification

The Model Context Protocol specification defines the authoritative protocol requirements, based on the TypeScript schema in [schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.ts).

### Messages

All messages between MCP clients and servers **MUST** follow the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines three fundamental types of messages:

| Type            | Description                            | Requirements                           |
| --------------- | -------------------------------------- | -------------------------------------- |
| `Requests`      | Messages sent to initiate an operation | Must include unique ID and method name |
| `Responses`     | Messages sent in reply to requests     | Must include same ID as request        |
| `Notifications` | One-way messages with no reply         | Must not include an ID                 |

**Responses** are further sub-categorized as either **successful results** or **errors**. Results can follow any JSON object structure, while errors must include an error code and message at minimum.

#### Request Format

```json
{
  "jsonrpc": "2.0",
  "id": "request-id-1",
  "method": "method-name",
  "params": {
    "parameterName": "value"
  }
}
```

#### Response Format

```json
{
  "jsonrpc": "2.0",
  "id": "request-id-1",
  "result": {
    "propertyName": "value"
  }
}
```

#### Error Response Format

```json
{
  "jsonrpc": "2.0",
  "id": "request-id-1",
  "error": {
    "code": -32602,
    "message": "Error description",
    "data": {
      "additionalDetails": "value"
    }
  }
}
```

#### Notification Format

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/event-name",
  "params": {
    "parameterName": "value"
  }
}
```

### Transports

MCP defines two standard transport mechanisms for client-server communication:

1. **stdio**: Communication over standard input/output
   - The client launches the server as a subprocess
   - Messages are sent via stdin and stdout
   - Messages are delimited by newlines
   - Server may use stderr for logging

2. **HTTP with Server-Sent Events (SSE)**:
   - Server operates as an independent process
   - Provides an SSE endpoint for client connections
   - Provides an HTTP POST endpoint for receiving messages
   - Server sends an `endpoint` event with the URI for client messages
   - All messages use the same JSON-RPC format

Custom transports may be implemented as long as they preserve the JSON-RPC message format and lifecycle requirements.

### Connection Lifecycle

The MCP connection lifecycle consists of three phases:

1. **Initialization**: 
   - Client sends `initialize` request with capabilities
   - Server responds with supported capabilities
   - Client sends `initialized` notification

2. **Operation**:
   - Normal protocol operations based on negotiated capabilities
   - Both parties respect negotiated protocol version and capabilities

3. **Shutdown**:
   - Connection termination using transport-specific mechanisms
   - No specific shutdown messages are defined

#### Version Negotiation

During initialization, clients and servers negotiate protocol versions:
- Client sends the latest version it supports
- Server responds with same version if supported, or another supported version
- Client should disconnect if it doesn't support server's version

#### Capability Negotiation

During initialization, clients and servers exchange capabilities to determine available features:

| Category | Capability     | Description                         |
| -------- | -------------- | ----------------------------------- |
| Client   | `roots`        | Filesystem root directories         |
| Client   | `sampling`     | LLM sampling support                |
| Server   | `prompts`      | Prompt templates                    |
| Server   | `resources`    | Readable resources                  |
| Server   | `tools`        | Callable tools                      |
| Server   | `logging`      | Structured logging                  |

Each capability may include sub-capabilities like `listChanged` (support for list change notifications) or `subscribe` (support for individual item change subscription).

### Protocol Layers

The Model Context Protocol consists of several key components that work together:

- **Base Protocol**: Core JSON-RPC message types
- **Lifecycle Management**: Connection initialization, capability negotiation, and session control
- **Server Features**: Resources, prompts, and tools exposed by servers
- **Client Features**: Sampling and root directory lists provided by clients
- **Utilities**: Cross-cutting concerns like logging and argument completion

All implementations **MUST** support the base protocol and lifecycle management components. Other components **MAY** be implemented based on the specific needs of the application.

### Architecture

The Model Context Protocol (MCP) follows a client-host-server architecture where each host can run multiple client instances. This architecture enables users to integrate AI capabilities across applications while maintaining clear security boundaries and isolating concerns. Built on JSON-RPC, MCP provides a stateful session protocol focused on context exchange and sampling coordination between clients and servers.

### Core Components

The architecture consists of three main components:

1. **Host**
   - The host process acts as the container and coordinator:
   - Creates and manages multiple client instances
   - Controls client connection permissions and lifecycle
   - Enforces security policies and consent requirements
   - Handles user authorization decisions
   - Coordinates AI/LLM integration and sampling
   - Manages context aggregation across clients

2. **Clients**
   - Each client is created by the host and maintains an isolated server connection:
   - Establishes one stateful session per server
   - Handles protocol negotiation and capability exchange
   - Routes protocol messages bidirectionally
   - Manages subscriptions and notifications
   - Maintains security boundaries between servers

3. **Servers**
   - Servers provide specialized context and capabilities:
   - Expose resources, tools and prompts via MCP primitives
   - Operate independently with focused responsibilities
   - Request sampling through client interfaces
   - Must respect security constraints
   - Can be local processes or remote services

### Server Features

Servers provide the fundamental building blocks for adding context to language models via MCP. These primitives enable rich interactions between clients, servers, and language models:

| Primitive | Control                | Description                                        | Example                         |
| --------- | ---------------------- | -------------------------------------------------- | ------------------------------- |
| Prompts   | User-controlled        | Interactive templates invoked by user choice       | Slash commands, menu options    |
| Resources | Application-controlled | Contextual data attached and managed by the client | File contents, git history      |
| Tools     | Model-controlled       | Functions exposed to the LLM to take actions       | API POST requests, file writing |

#### Prompts

Prompts are user-controlled templates that define structured interactions with language models. They help users perform common tasks and provide consistent instructions to AI models.

Key characteristics:
- **User-controlled**: Typically triggered by explicit user actions (slash commands, menu options)
- **Parameterized**: Can accept arguments to customize behavior
- **Structured**: May include multiple messages with different roles (user/assistant)
- **Multi-modal**: Can contain text, images, or embedded resources

Prompt capabilities must be declared during server initialization:
```json
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

Core operations:
- `prompts/list`: Discover available prompts
- `prompts/get`: Retrieve specific prompt with arguments
- `notifications/prompts/list_changed`: Notify when available prompts change

#### Resources

Resources provide contextual data to language models, such as files, database schemas, or application-specific information. Each resource is uniquely identified by a URI.

Key characteristics:
- **Application-controlled**: Host applications determine how to incorporate context
- **URI-based**: Each resource has a unique URI identifier
- **Content-typed**: Resources include MIME type information
- **Subscribable**: Optional notifications for resource changes
- **Templated**: Parameterized templates allow dynamic resource access

Resource capabilities must be declared during server initialization:
```json
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}
```

Core operations:
- `resources/list`: Discover available resources
- `resources/read`: Retrieve resource contents
- `resources/templates/list`: List parameterized resource templates
- `resources/subscribe`: Subscribe to resource change notifications
- `notifications/resources/updated`: Notify when a resource changes
- `notifications/resources/list_changed`: Notify when available resources change

Standard URI schemes include:
- `https://`: Web resources
- `file://`: Filesystem-like resources
- `git://`: Git version control integration

#### Tools

Tools enable language models to take actions by invoking functions exposed by the server. They allow models to interact with external systems like databases or APIs.

Key characteristics:
- **Model-controlled**: Language models can discover and invoke tools
- **Schema-defined**: Each tool declares its input schema with JSON Schema
- **Interactive**: Results can feed back into the conversation
- **Error-aware**: Distinct handling for protocol vs. execution errors
- **Security-focused**: Design emphasizes human oversight

Tool capabilities must be declared during server initialization:
```json
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}
```

Core operations:
- `tools/list`: Discover available tools
- `tools/call`: Invoke a specific tool with arguments
- `notifications/tools/list_changed`: Notify when available tools change

For security, implementations should:
- Validate all tool inputs
- Implement proper access controls
- Rate limit tool invocations
- Sanitize tool outputs
- Include human oversight through confirmation prompts

### Client Features

Clients can implement additional features to enrich the capabilities of connected MCP servers.

#### Sampling

Sampling allows servers to request language model generations ("completions") via clients. This enables servers to implement agentic behaviors by leveraging AI capabilities through a standardized interface, without requiring direct API access or keys.

Key characteristics:
- **Server-initiated**: Servers request generations that clients fulfill
- **Human-in-the-loop**: Clients typically show prompts to users for review
- **Model-abstracted**: Uses preference system rather than direct model selection
- **Multi-modal**: Supports text and image content in both prompts and responses

Sampling capabilities must be declared during client initialization:
```json
{
  "capabilities": {
    "sampling": {}
  }
}
```

Core operations:
- `sampling/createMessage`: Request language model generation

When requesting sampling, servers can specify model preferences through:
1. **Capability priorities**: Normalized values (0-1) for cost, speed, and intelligence
2. **Model hints**: Optional suggestions for specific models or families

```json
{
  "hints": [
    { "name": "claude-3-sonnet" },
    { "name": "claude" }
  ],
  "costPriority": 0.3,
  "speedPriority": 0.8,
  "intelligencePriority": 0.5
}
```

For security, implementations should:
- Implement user approval controls
- Validate message content
- Implement rate limiting
- Handle sensitive data appropriately

#### Roots

Roots allow clients to expose filesystem boundaries to servers. They define the directories and files that servers can access within the filesystem.

Key characteristics:
- **Client-controlled**: Clients define accessible filesystem areas
- **URI-based**: Each root has a unique file:// URI
- **Boundary-setting**: Establishes clear security perimeters
- **Dynamically updated**: Can change during a session

Root capabilities must be declared during client initialization:
```json
{
  "capabilities": {
    "roots": {
      "listChanged": true
    }
  }
}
```

Core operations:
- `roots/list`: Retrieve accessible filesystem roots
- `notifications/roots/list_changed`: Notify when available roots change

For security, implementations should:
- Only expose roots with appropriate permissions
- Validate all root URIs to prevent path traversal
- Implement proper access controls
- Monitor root accessibility
- Prompt users for consent before exposing roots

### Design Principles

MCP is built on several key design principles:

1. **Servers should be extremely easy to build**
   - Host applications handle complex orchestration responsibilities
   - Servers focus on specific, well-defined capabilities
   - Simple interfaces minimize implementation overhead
   - Clear separation enables maintainable code

2. **Servers should be highly composable**
   - Each server provides focused functionality in isolation
   - Multiple servers can be combined seamlessly
   - Shared protocol enables interoperability
   - Modular design supports extensibility

3. **Servers should not be able to read the whole conversation, nor "see into" other servers**
   - Servers receive only necessary contextual information
   - Full conversation history stays with the host
   - Each server connection maintains isolation
   - Cross-server interactions are controlled by the host
   - Host process enforces security boundaries

4. **Features can be added to servers and clients progressively**
   - Core protocol provides minimal required functionality
   - Additional capabilities can be negotiated as needed
   - Servers and clients evolve independently
   - Protocol designed for future extensibility
   - Backwards compatibility is maintained

### Security and Trust & Safety

The Model Context Protocol enables powerful capabilities through arbitrary data access and code execution paths. With this power comes important security and trust considerations that all implementors must carefully address.

#### Key Principles

1. **User Consent and Control**
   - Users must explicitly consent to and understand all data access and operations
   - Users must retain control over what data is shared and what actions are taken
   - Implementors should provide clear UIs for reviewing and authorizing activities

2. **Data Privacy**
   - Hosts must obtain explicit user consent before exposing user data to servers
   - Hosts must not transmit resource data elsewhere without user consent
   - User data should be protected with appropriate access controls

3. **Tool Safety**
   - Tools represent arbitrary code execution and must be treated with appropriate caution
   - Hosts must obtain explicit user consent before invoking any tool
   - Users should understand what each tool does before authorizing its use

4. **LLM Sampling Controls**
   - Users must explicitly approve any LLM sampling requests
   - Users should control:
     - Whether sampling occurs at all
     - The actual prompt that will be sent
     - What results the server can see
   - The protocol intentionally limits server visibility into prompts

## MCP Python SDK

The Python SDK implements the full MCP specification, making it easy to:

- Build MCP clients that can connect to any MCP server
- Create MCP servers that expose resources, prompts and tools
- Use standard transports like stdio and SSE
- Handle all MCP protocol messages and lifecycle events

### Installation

#### Adding MCP to your python project

We recommend using [uv](https://docs.astral.sh/uv/) to manage your Python projects. In a uv managed python project, add mcp to dependencies by:

```bash
uv add "mcp[cli]"
```

Alternatively, for projects using pip for dependencies:
```bash
pip install mcp
```

#### Running the standalone MCP development tools

To run the mcp command with uv:

```bash
uv run mcp
```

### Quickstart

Let's create a simple MCP server that exposes a calculator tool and some data:

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

You can install this server in [Claude Desktop](https://claude.ai/download) and interact with it right away by running:
```bash
mcp install server.py
```

Alternatively, you can test it with the MCP Inspector:
```bash
mcp dev server.py
```

### Core Concepts

#### Server

The FastMCP server is your core interface to the MCP protocol. It handles connection management, protocol compliance, and message routing:

```python
# Add lifespan support for startup/shutdown with strong typing
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass

from fake_database import Database  # Replace with your actual DB type

from mcp.server.fastmcp import Context, FastMCP

# Create a named server
mcp = FastMCP("My App")

# Specify dependencies for deployment and development
mcp = FastMCP("My App", dependencies=["pandas", "numpy"])


@dataclass
class AppContext:
    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context"""
    # Initialize on startup
    db = await Database.connect()
    try:
        yield AppContext(db=db)
    finally:
        # Cleanup on shutdown
        await db.disconnect()


# Pass lifespan to server
mcp = FastMCP("My App", lifespan=app_lifespan)


# Access type-safe lifespan context in tools
@mcp.tool()
def query_db(ctx: Context) -> str:
    """Tool that uses initialized resources"""
    db = ctx.request_context.lifespan_context["db"]
    return db.query()
```

#### Resources

Resources are how you expose data to LLMs. They're similar to GET endpoints in a REST API - they provide data but shouldn't perform significant computation or have side effects:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"
```

#### Tools

Tools let LLMs take actions through your server. Unlike resources, tools are expected to perform computation and have side effects:

```python
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")


@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m**2)


@mcp.tool()
async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.weather.com/{city}")
        return response.text
```

#### Prompts

Prompts are reusable templates that help LLMs interact with your server effectively:

```python
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("My App")


@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]
```

#### Images

FastMCP provides an `Image` class that automatically handles image data:

```python
from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage

mcp = FastMCP("My App")


@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")
```

#### Context

The Context object gives your tools and resources access to MCP capabilities:

```python
from mcp.server.fastmcp import FastMCP, Context

mcp = FastMCP("My App")


@mcp.tool()
async def long_task(files: list[str], ctx: Context) -> str:
    """Process multiple files with progress tracking"""
    for i, file in enumerate(files):
        ctx.info(f"Processing {file}")
        await ctx.report_progress(i, len(files))
        data, mime_type = await ctx.read_resource(f"file://{file}")
    return "Processing complete"
```

### Running Your Server

#### Development Mode

The fastest way to test and debug your server is with the MCP Inspector:

```bash
mcp dev server.py

# Add dependencies
mcp dev server.py --with pandas --with numpy

# Mount local code
mcp dev server.py --with-editable .
```

#### Claude Desktop Integration

Once your server is ready, install it in Claude Desktop:

```bash
mcp install server.py

# Custom name
mcp install server.py --name "My Analytics Server"

# Environment variables
mcp install server.py -v API_KEY=abc123 -v DB_URL=postgres://...
mcp install server.py -f .env
```

#### Direct Execution

For advanced scenarios like custom deployments:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

if __name__ == "__main__":
    mcp.run()
```

Run it with:
```bash
python server.py
# or
mcp run server.py
```

#### Mounting to an Existing ASGI Server

You can mount the SSE server to an existing ASGI server using the `sse_app` method:

```python
from starlette.applications import Starlette
from starlette.routes import Mount, Host
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("My App")

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

# or dynamically mount as host
app.router.routes.append(Host('mcp.acme.corp', app=mcp.sse_app()))
```

### Examples

#### Echo Server

A simple server demonstrating resources, tools, and prompts:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Echo")


@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"


@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"


@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"
```

#### SQLite Explorer

A more complex example showing database integration:

```python
import sqlite3

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SQLite Explorer")


@mcp.resource("schema://main")
def get_schema() -> str:
    """Provide the database schema as a resource"""
    conn = sqlite3.connect("database.db")
    schema = conn.execute("SELECT sql FROM sqlite_master WHERE type='table'").fetchall()
    return "\n".join(sql[0] for sql in schema if sql[0])


@mcp.tool()
def query_data(sql: str) -> str:
    """Execute SQL queries safely"""
    conn = sqlite3.connect("database.db")
    try:
        result = conn.execute(sql).fetchall()
        return "\n".join(str(row) for row in result)
    except Exception as e:
        return f"Error: {str(e)}"
```

### Advanced Usage

#### Low-Level Server

For more control, you can use the low-level server implementation directly:

```python
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fake_database import Database  # Replace with your actual DB type

from mcp.server import Server


@asynccontextmanager
async def server_lifespan(server: Server) -> AsyncIterator[dict]:
    """Manage server startup and shutdown lifecycle."""
    # Initialize resources on startup
    db = await Database.connect()
    try:
        yield {"db": db}
    finally:
        # Clean up on shutdown
        await db.disconnect()


# Pass lifespan to server
server = Server("example-server", lifespan=server_lifespan)


# Access lifespan context in handlers
@server.call_tool()
async def query_db(name: str, arguments: dict) -> list:
    ctx = server.request_context
    db = ctx.lifespan_context["db"]
    return await db.query(arguments["query"])
```

#### Writing MCP Clients

The SDK provides a high-level client interface for connecting to MCP servers:

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=["example_server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)


# Optional: create a sampling callback
async def handle_sampling_message(
    message: types.CreateMessageRequestParams,
) -> types.CreateMessageResult:
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="Hello, world! from model",
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write, sampling_callback=handle_sampling_message
        ) as session:
            # Initialize the connection
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()

            # Get a prompt
            prompt = await session.get_prompt(
                "example-prompt", arguments={"arg1": "value"}
            )

            # List available resources
            resources = await session.list_resources()

            # List available tools
            tools = await session.list_tools()

            # Read a resource
            content, mime_type = await session.read_resource("file://some/path")

            # Call a tool
            result = await session.call_tool("tool-name", arguments={"arg1": "value"})
```

## Documentation

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [Model Context Protocol specification](https://spec.modelcontextprotocol.io)
- [Officially supported servers](https://github.com/modelcontextprotocol/servers)

## Contributing

We are passionate about supporting contributors of all levels of experience and would love to see you get involved in the project. See the [contributing guide](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
