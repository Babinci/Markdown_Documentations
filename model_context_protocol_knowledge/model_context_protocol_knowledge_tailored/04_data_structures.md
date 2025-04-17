# Model Context Protocol (MCP) - Core Data Structures and Types

This section describes the primary data structures and types defined by the Model Context Protocol standard and how they're implemented in the Python SDK.

## Protocol Message Structures

### JSON-RPC 2.0 Format

The MCP standard uses JSON-RPC 2.0 as its underlying message format. All communication between clients and servers follows this specification:

#### 1. Request Message

```json
{
  "jsonrpc": "2.0",
  "id": "unique-request-id",
  "method": "method-name",
  "params": {
    "param1": "value1",
    "param2": "value2"
  }
}
```

Key components:
- `jsonrpc`: Always "2.0" to indicate protocol version
- `id`: Unique identifier to correlate requests and responses
- `method`: The operation to perform (e.g., "list_tools", "call_tool")
- `params`: Object containing method-specific parameters

#### 2. Success Response

```json
{
  "jsonrpc": "2.0",
  "id": "unique-request-id",
  "result": {
    "field1": "value1",
    "field2": "value2"
  }
}
```

Key components:
- `jsonrpc`: Always "2.0"
- `id`: Matches the id from the corresponding request
- `result`: Object containing the operation result

#### 3. Error Response

```json
{
  "jsonrpc": "2.0",
  "id": "unique-request-id",
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": {
      "details": "Parameter 'location' is required"
    }
  }
}
```

Key components:
- `jsonrpc`: Always "2.0"
- `id`: Matches the id from the corresponding request
- `error`: Object containing error details
  - `code`: Numeric error code (standard or custom)
  - `message`: Human-readable error message
  - `data`: Optional object with additional error details

### JSON-RPC Error Codes

The MCP standard uses these error codes:

| Code | Message | Meaning |
|------|---------|---------|
| -32700 | Parse error | Invalid JSON was received |
| -32600 | Invalid Request | The JSON sent is not a valid Request object |
| -32601 | Method not found | The method does not exist / is not available |
| -32602 | Invalid params | Invalid method parameter(s) |
| -32603 | Internal error | Internal JSON-RPC error |
| -32000 to -32099 | Server error | Implementation-defined server errors |
| 40000 | Tool execution error | Error occurred during tool execution |
| 40100 | Authentication error | Authentication failed |
| 40300 | Permission denied | Authorization failed |

## Core Protocol Data Structures

### 1. Tool Definition

The `Tool` structure represents a capability available through the MCP:

```json
{
  "name": "get_weather",
  "description": "Get current weather for a location",
  "inputSchema": {
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
}
```

Key components:
- `name`: Unique identifier for the tool
- `description`: Human-readable description of the tool's purpose
- `inputSchema`: JSON Schema defining the tool's input parameters

In the Python SDK, tools are defined using the `Tool` class:

```python
from mcp.types import Tool

weather_tool = Tool(
    name="get_weather",
    description="Get current weather for a location",
    function=get_weather_function,
    # Optional input schema - can be auto-generated
)
```

### 2. List Tools Request

Request to discover available tools:

```json
{
  "jsonrpc": "2.0",
  "id": "discovery-1",
  "method": "list_tools",
  "params": {}
}
```

In the Python SDK:
```python
response = await session.list_tools()
```

### 3. List Tools Response

Response containing available tools:

```json
{
  "jsonrpc": "2.0",
  "id": "discovery-1",
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "inputSchema": {
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
      },
      {
        "name": "search_web",
        "description": "Search the web for information",
        "inputSchema": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "Search query"
            },
            "num_results": {
              "type": "integer",
              "description": "Number of results to return",
              "default": 5
            }
          },
          "required": ["query"]
        }
      }
    ]
  }
}
```

### 4. Call Tool Request

Request to execute a specific tool:

```json
{
  "jsonrpc": "2.0",
  "id": "execution-1",
  "method": "call_tool",
  "params": {
    "tool_name": "get_weather",
    "args": {
      "location": "New York",
      "units": "metric"
    }
  }
}
```

In the Python SDK:
```python
result = await session.call_tool(
    "get_weather", 
    {"location": "New York", "units": "metric"}
)
```

### 5. Call Tool Response

Response containing tool execution result:

```json
{
  "jsonrpc": "2.0",
  "id": "execution-1",
  "result": {
    "temperature": 22.5,
    "conditions": "partly cloudy",
    "humidity": 65,
    "wind_speed": 10
  }
}
```

## JSON Schema Usage

The MCP relies heavily on JSON Schema for defining tool inputs:

### Basic Schema Example

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

### Complex Schema Example

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search query"
    },
    "filters": {
      "type": "object",
      "properties": {
        "date_range": {
          "type": "object",
          "properties": {
            "start": {
              "type": "string",
              "format": "date"
            },
            "end": {
              "type": "string",
              "format": "date"
            }
          }
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "sort": {
      "type": "string",
      "enum": ["relevance", "date", "popularity"],
      "default": "relevance"
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 100,
      "default": 10
    }
  },
  "required": ["query"]
}
```

## Python SDK Implementation

### ClientSession Response Types

The Python SDK provides structured response types:

```python
# Response from list_tools
class ListToolsResponse:
    tools: List[Tool]  # List of available tools

# Response from call_tool
# This is typically the direct result returned by the tool function
```

### Tool Implementation in Python

Tools in the Python SDK are defined with:

```python
from mcp.types import Tool

# Simplest form - function signature used for schema
weather_tool = Tool(
    name="get_weather",
    description="Get current weather for a location",
    function=get_weather_function
)

# With explicit schema
weather_tool_with_schema = Tool(
    name="get_weather",
    description="Get current weather for a location",
    function=get_weather_function,
    inputSchema={
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "units": {"type": "string", "enum": ["metric", "imperial"]}
        },
        "required": ["location"]
    }
)
```

### Server Configuration Types

The SDK provides types for server configuration:

```python
# Server parameters for stdio transport
class StdioServerParameters:
    command: str
    args: List[str]
    env: Dict[str, str]

# Server settings
class Settings:
    name: str
    timeout: int = 60
    # Additional settings...
```

## Transport-Specific Data Structures

### Stdio Transport

For stdio transport, data is exchanged as newline-delimited JSON:

```
{"jsonrpc":"2.0","id":"req1","method":"list_tools","params":{}}\n
{"jsonrpc":"2.0","id":"req1","result":{"tools":[...]}}\n
```

### HTTP/SSE Transport

For HTTP transport:
- Requests use standard HTTP POST with JSON body
- Responses use Server-Sent Events format:

```
event: result
data: {"jsonrpc":"2.0","id":"req1","result":{"tools":[...]}}

event: error
data: {"jsonrpc":"2.0","id":"req2","error":{"code":-32602,"message":"Invalid params"}}
```

These data structures form the foundation of the Model Context Protocol, enabling standardized communication between clients and servers regardless of the specific implementation details. By adhering to these structures, different MCP implementations can interoperate seamlessly.
