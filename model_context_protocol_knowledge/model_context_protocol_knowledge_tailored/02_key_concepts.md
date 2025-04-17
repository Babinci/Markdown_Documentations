# Model Context Protocol (MCP) - Key Concepts and Terminology

This section defines the core concepts and terminology of the Model Context Protocol standard and its Python SDK implementation.

## Core Protocol Concepts

### 1. Tool

A **Tool** in MCP represents a discrete capability that extends an LLM's functionality. Conceptually, a tool is:

- A named function with a well-defined purpose
- A capability that accepts structured inputs and returns structured outputs
- A discrete unit of functionality that can be discovered and invoked
- A blackbox from the LLM's perspective - it knows what a tool does but not how it works

In the MCP Python SDK, tools are typically implemented as:
```python
from mcp.types import Tool

# Example tool definition
weather_tool = Tool(
    name="get_weather",
    description="Get current weather for a location",
    function=get_weather_function,  # The actual implementation
    # Optional input schema definition
)
```

### 2. Tool Registry

A **Tool Registry** is the component that maintains the collection of available tools. Its responsibilities include:

- Storing tool definitions with their metadata
- Providing a lookup mechanism to find tools by name
- Supporting tool discovery operations
- Enforcing access controls on tool availability

This concept is not directly exposed in the SDK but is managed internally by the MCP server components.

### 3. Protocol Transport

The **Protocol Transport** defines how messages are exchanged between clients and servers. The MCP standard supports multiple transport mechanisms:

- **Stdio Transport**: Communication via standard input/output streams
- **HTTP Transport**: Communication via HTTP/HTTPS requests (typically using Server-Sent Events)
- **Custom Transports**: Implementation-specific channels for specialized deployments

In the Python SDK:
```python
# Stdio transport example
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client

# Define server parameters
server_params = StdioServerParameters(
    command="python",
    args=["-m", "my_server.main"],
    env={"KEY": "value"}
)

# Create transport
async with stdio_client(server_params) as transport:
    stdin, stdout = transport
    # Use the transport...
```

### 4. Protocol Operations

The **Protocol Operations** are the core methods defined by MCP:

- **list_tools**: Discover available tools and their schemas
- **call_tool**: Execute a specific tool with arguments
- **initialize**: Set up a new client-server session (optional)
- **shutdown**: Clean up an existing session (optional)

These operations form the API contract between clients and servers, regardless of how they're implemented.

### 5. Message Format

The **Message Format** defines the structure of communication between MCP clients and servers. MCP uses JSON-RPC 2.0, which includes:

- **Request Objects**: Messages sent from client to server
- **Response Objects**: Messages sent from server to client
- **Notification Objects**: One-way messages with no response
- **Error Objects**: Standardized error responses

Example JSON-RPC message for tool execution:
```json
{
  "jsonrpc": "2.0",
  "id": "request-123",
  "method": "call_tool",
  "params": {
    "tool_name": "get_weather",
    "args": {
      "location": "New York"
    }
  }
}
```

## MCP Python SDK Components

### 6. ClientSession

The **ClientSession** is the primary interface for MCP clients. It:

- Manages the connection to an MCP server
- Provides methods for tool discovery and execution
- Handles message serialization and deserialization
- Manages request and response correlation

In the Python SDK:
```python
from mcp import ClientSession

# Create a session with transport streams
session = ClientSession(stdin, stdout)

# Initialize the session
await session.initialize()

# List available tools
tools_response = await session.list_tools()

# Call a tool
result = await session.call_tool("get_weather", {"location": "New York"})
```

### 7. FastMCP

**FastMCP** is a server-side implementation in the Python SDK that:

- Registers and hosts tool definitions
- Processes incoming JSON-RPC requests
- Routes requests to appropriate tools
- Manages session lifecycle
- Handles authentication and authorization

Usage:
```python
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool

# Create server
mcp_server = FastMCP("my_tool_server")

# Register tools
mcp_server.add_tool(Tool(
    name="get_weather",
    description="Get current weather for a location",
    function=get_weather_function
))

# Run the server
mcp_server.run()
```

### 8. Tool Schema

A **Tool Schema** uses JSON Schema to define the structure of tool inputs. It:

- Documents required and optional parameters
- Defines parameter types and constraints
- Enables automated validation
- Provides runtime documentation

Example schema structure:
```json
{
  "type": "object",
  "properties": {
    "location": {
      "type": "string",
      "description": "City name or coordinates"
    },
    "units": {
      "type": "string",
      "enum": ["metric", "imperial"],
      "default": "metric"
    }
  },
  "required": ["location"]
}
```

### 9. Authentication Mechanism

The **Authentication Mechanism** in MCP provides security through:

- **Bearer Tokens**: Authentication credentials passed in headers or environment
- **Production vs. Development Modes**: Different security requirements based on deployment context
- **Selective Authentication Bypass**: Optional configuration for specific operations

In the Python SDK, authentication is typically handled via environment variables or parameters:
```python
# Client-side token passing
os.environ["DYNAMIC_API_TOKEN"] = "your_secure_token_here"

# Server-side token validation
if PRODUCTION_MODE and not DYNAMIC_API_TOKEN:
    logger.critical("Production mode requires authentication token")
    sys.exit(1)
```

### 10. Dynamic Tool Generation

**Dynamic Tool Generation** is an extended capability that:

- Creates tool definitions from OpenAPI/Swagger specifications
- Converts API endpoints to MCP tools automatically
- Generates input validation schemas from API parameters
- Maps operation IDs to tool names

This is not part of the core protocol but is a common implementation pattern, especially in systems like JobAssistant.

## Protocol Extension Concepts

### 11. LLM Integration Patterns

While not part of the core MCP specification, common LLM integration patterns include:

- **System Prompt Injection**: Adding tool descriptions to LLM system prompts
- **Structured Output Formatting**: Using XML or JSON templates for tool calls
- **Multi-turn Interaction**: Managing conversation context with tool results
- **Tool Selection Logic**: Helping LLMs decide when and how to use tools

### 12. Transport Mechanisms

MCP implementations can use various transport mechanisms:

- **Stdio**: Using standard input/output for local communication
- **HTTP/SSE**: Using HTTP requests and Server-Sent Events for remote communication
- **WebSockets**: Enabling bidirectional communication for real-time applications
- **Custom Channels**: Implementation-specific communication methods

## Relationship Between Concepts

- The **Protocol** defines the standards for communication
- **Tools** provide the actual functionality to be invoked
- **ClientSession** provides the client-side API for discovering and calling tools
- **FastMCP** implements the server-side handling of tool registration and execution
- **Tool Schema** standardizes input validation and documentation
- **Authentication** secures access to tools based on credentials and permissions

Understanding these concepts provides a foundation for working with any MCP implementation, regardless of the specific application domain or extension mechanisms used.
