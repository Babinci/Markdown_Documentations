# Model Context Protocol (MCP) - Protocol Operations and Methods

This section describes the core operations defined by the Model Context Protocol standard and how they're implemented in the Python SDK.

## Core Protocol Operations

The MCP defines a small set of fundamental operations that form the basis of communication between clients and servers:

### 1. `list_tools` Operation

**Purpose**: Discover available tools and their input schemas  
**Method**: `list_tools`  
**Request Parameters**: None  
**Response**: List of available tools with metadata

**Protocol Format**:

Request:
```json
{
  "jsonrpc": "2.0",
  "id": "discovery-request-1",
  "method": "list_tools",
  "params": {}
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": "discovery-request-1",
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {"type": "string"},
            "units": {"type": "string", "enum": ["metric", "imperial"]}
          },
          "required": ["location"]
        }
      }
    ]
  }
}
```

**SDK Implementation**:

Client-side:
```python
from mcp import ClientSession

async def discover_tools(session: ClientSession):
    response = await session.list_tools()
    for tool in response.tools:
        print(f"Tool: {tool.name}")
        print(f"Description: {tool.description}")
        print(f"Input Schema: {tool.inputSchema}")
```

Server-side:
```python
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool

# Create server
server = FastMCP("my_tools_server")

# Register tools
server.add_tool(Tool(
    name="get_weather",
    description="Get current weather for a location",
    function=get_weather_function
))

# Run server (handles list_tools automatically)
server.run()
```

**Key Characteristics**:
- Usually the first operation called after establishing a connection
- Returns complete metadata for all available tools
- Can be used for tool discovery or documentation generation
- May be secured with authentication in production environments
- May have custom access control for different tools based on permissions

### 2. `call_tool` Operation

**Purpose**: Execute a specific tool with provided arguments  
**Method**: `call_tool`  
**Request Parameters**:
  - `tool_name`: Name of the tool to call (string)
  - `args`: Arguments to pass to the tool (object)
**Response**: Result of tool execution

**Protocol Format**:

Request:
```json
{
  "jsonrpc": "2.0",
  "id": "tool-call-123",
  "method": "call_tool",
  "params": {
    "tool_name": "get_weather",
    "args": {
      "location": "San Francisco",
      "units": "metric"
    }
  }
}
```

Success Response:
```json
{
  "jsonrpc": "2.0",
  "id": "tool-call-123",
  "result": {
    "temperature": 18.5,
    "conditions": "foggy",
    "humidity": 85
  }
}
```

Error Response:
```json
{
  "jsonrpc": "2.0",
  "id": "tool-call-123",
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": {
      "details": "Missing required parameter: location"
    }
  }
}
```

**SDK Implementation**:

Client-side:
```python
async def call_weather_tool(session: ClientSession, location: str, units: str = "metric"):
    try:
        result = await session.call_tool(
            "get_weather",
            {"location": location, "units": units}
        )
        print(f"Temperature: {result['temperature']}°{units == 'metric' ? 'C' : 'F'}")
        print(f"Conditions: {result['conditions']}")
    except Exception as e:
        print(f"Error calling tool: {str(e)}")
```

Server-side:
```python
# Tool implementation
async def get_weather(location: str, units: str = "metric"):
    # Implementation details...
    return {
        "temperature": 22.5,
        "conditions": "partly cloudy",
        "humidity": 65
    }

# Register with server
server.add_tool(Tool(
    name="get_weather",
    description="Get current weather for a location",
    function=get_weather
))
```

**Key Characteristics**:
- Primary operation for tool execution
- Arguments validated against tool's input schema
- Supports both synchronous and asynchronous tool implementations
- Returns structured result data or error details
- Usually requires authentication in production environments

### 3. `initialize` Operation (Optional)

**Purpose**: Initialize a session between client and server  
**Method**: `initialize`  
**Request Parameters**:
  - `client_info`: Information about the client (optional)
  - `authentication`: Authentication credentials (optional)
**Response**: Session information and capabilities

**Protocol Format**:

Request:
```json
{
  "jsonrpc": "2.0",
  "id": "init-1",
  "method": "initialize",
  "params": {
    "client_info": {
      "name": "my_client",
      "version": "1.0.0"
    }
  }
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": "init-1",
  "result": {
    "server_info": {
      "name": "my_server",
      "version": "2.1.0"
    },
    "capabilities": {
      "supports_streaming": true,
      "max_request_size": 1048576
    }
  }
}
```

**SDK Implementation**:

Client-side:
```python
async def initialize_session(session: ClientSession):
    init_result = await session.initialize()
    print(f"Connected to server: {init_result.server_info.name} {init_result.server_info.version}")
    print(f"Server capabilities: {init_result.capabilities}")
```

**Key Characteristics**:
- Optional operation for session initialization
- Can be used to exchange capability information
- May include authentication steps
- Typically called once at the beginning of a session

### 4. `shutdown` Operation (Optional)

**Purpose**: Gracefully terminate a session  
**Method**: `shutdown`  
**Request Parameters**: None  
**Response**: Acknowledgment of shutdown

**Protocol Format**:

Request:
```json
{
  "jsonrpc": "2.0",
  "id": "shutdown-1",
  "method": "shutdown",
  "params": {}
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "id": "shutdown-1",
  "result": {
    "status": "success",
    "message": "Session terminated successfully"
  }
}
```

**SDK Implementation**:

In the SDK, this is typically handled by the connection cleanup:
```python
async def close_session(session: ClientSession):
    await session.shutdown()  # Explicit shutdown
    # Or implicitly via context manager:
    # async with ClientSession(stdin, stdout) as session:
    #     # Use session...
    # # Shutdown happens automatically when exiting context
```

**Key Characteristics**:
- Optional operation for graceful termination
- Allows server to clean up resources
- May be omitted in some implementations
- Typically called once at the end of a session

## Error Handling in MCP

The MCP defines a standard approach to error handling using JSON-RPC error objects:

### Standard Error Format

```json
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": {
      "details": "Parameter 'location' is required",
      "parameter": "location",
      "type": "missing_required"
    }
  }
}
```

### Error Categories

1. **Protocol Errors** (JSON-RPC standard errors):
   - Parse Error (-32700): Invalid JSON
   - Invalid Request (-32600): Not a valid JSON-RPC request
   - Method Not Found (-32601): Method doesn't exist
   - Invalid Params (-32602): Invalid method parameters
   - Internal Error (-32603): Internal JSON-RPC error
   - Server Error (-32000 to -32099): Implementation-defined server errors

2. **Tool Execution Errors** (MCP-specific):
   - Tool Not Found (40400): Requested tool doesn't exist
   - Tool Execution Failed (40000): Error during tool execution
   - Tool Input Validation Failed (40001): Input doesn't match schema
   - Tool Output Validation Failed (40002): Output doesn't match schema

3. **Authentication Errors**:
   - Authentication Required (40100): Missing authentication
   - Invalid Token (40101): Invalid or expired token
   - Insufficient Permissions (40300): Token lacks required permissions

### Error Handling in the SDK

Client-side:
```python
try:
    result = await session.call_tool("get_weather", {"loc": "London"})  # Wrong parameter name
    process_result(result)
except ValueError as e:
    # Handle validation errors
    print(f"Validation error: {str(e)}")
except RPCError as e:
    # Handle RPC errors with code and message
    print(f"RPC error {e.code}: {e.message}")
    if e.data:
        print(f"Details: {e.data}")
except Exception as e:
    # Handle other errors
    print(f"Unexpected error: {str(e)}")
```

Server-side:
```python
# Error handling in tool implementation
async def get_weather(location: str):
    try:
        # Implementation...
        if not location:
            raise ValueError("Location cannot be empty")
            
        # API call or other logic...
        
        return {
            "temperature": 22.5,
            "conditions": "partly cloudy"
        }
    except ValueError as e:
        # Client errors (invalid input)
        raise RPCError(
            code=40001,
            message="Invalid input",
            data={"details": str(e)}
        )
    except ExternalAPIError as e:
        # External service errors
        raise RPCError(
            code=40000,
            message="External API error",
            data={"details": str(e), "service": "weather_api"}
        )
```

## MCP Client SDK Methods

The MCP Python SDK Client provides these primary methods that map to the protocol operations:

### 1. `list_tools()`

**Purpose**: Discover available tools on the server  
**Returns**: `ListToolsResponse` with tools array

```python
async def discover_available_tools(session):
    response = await session.list_tools()
    return response.tools
```

### 2. `call_tool(tool_name, args)`

**Purpose**: Execute a tool with arguments  
**Parameters**:
  - `tool_name`: String name of the tool
  - `args`: Dictionary of tool arguments
**Returns**: Tool-specific result object

```python
async def execute_tool(session, tool_name, args):
    try:
        result = await session.call_tool(tool_name, args)
        return result
    except RPCError as e:
        handle_error(e)
```

### 3. `initialize()`

**Purpose**: Initialize the session  
**Returns**: `InitializeResponse` with server info and capabilities

```python
async def setup_session(session):
    init_result = await session.initialize()
    print(f"Connected to: {init_result.server_info.name}")
```

### 4. `shutdown()`

**Purpose**: End the session gracefully  
**Returns**: `ShutdownResponse` with status

```python
async def end_session(session):
    await session.shutdown()
```

## MCP Server SDK Methods

The MCP Python SDK Server provides these primary methods:

### 1. `add_tool(tool)`

**Purpose**: Register a tool with the server  
**Parameters**:
  - `tool`: Tool instance to register
**Returns**: None

```python
def register_tools(server):
    server.add_tool(Tool(
        name="get_weather",
        description="Get weather information",
        function=get_weather_function
    ))
```

### 2. `run()`

**Purpose**: Start the server and handle client requests  
**Parameters**: None  
**Returns**: Does not return until stopped

```python
def start_server():
    server = FastMCP("my_tool_server")
    register_tools(server)
    server.run()  # Blocks until terminated
```

These operations and methods form the core of the Model Context Protocol, providing a consistent interface for tool discovery and execution across different implementations.
