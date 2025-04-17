# Model Context Protocol (MCP) - Usage Patterns and Workflows

This section describes common usage patterns and workflows for implementing and using the Model Context Protocol, with examples from the Python SDK.

## Basic Usage Patterns

### 1. Client Session Lifecycle

The fundamental pattern for client interaction with MCP:

```python
import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def basic_mcp_workflow():
    # 1. Set up server parameters
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_server.main"],
        env={"API_TOKEN": "your_token_here"}
    )
    
    # 2. Create transport and session
    async with stdio_client(server_params) as transport:
        stdin, stdout = transport
        
        # 3. Create session
        session = ClientSession(stdin, stdout)
        
        # 4. Initialize (optional)
        await session.initialize()
        
        # 5. Discover tools
        tools_response = await session.list_tools()
        print(f"Available tools: {[tool.name for tool in tools_response.tools]}")
        
        # 6. Call tools
        result = await session.call_tool("sample_tool", {"param1": "value1"})
        print(f"Result: {result}")
        
        # 7. Session cleanup happens automatically via context manager

# Run the async function
asyncio.run(basic_mcp_workflow())
```

Key aspects:
- Transport setup with server parameters
- Session creation with transport streams
- Tool discovery before usage
- Tool execution with structured arguments
- Proper resource cleanup via context manager

### 2. Server Implementation Pattern

The standard pattern for creating an MCP server:

```python
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool

# 1. Define tool functions
async def sample_tool(param1: str, param2: int = 0) -> dict:
    """Tool that demonstrates basic functionality"""
    return {
        "message": f"Processed {param1} with value {param2}",
        "status": "success"
    }

async def advanced_tool(query: str, options: dict = None) -> dict:
    """More complex tool with nested parameters"""
    options = options or {}
    
    # Implementation...
    
    return {
        "results": [
            {"id": 1, "name": "Result 1"},
            {"id": 2, "name": "Result 2"}
        ],
        "count": 2,
        "query": query
    }

# 2. Create server
server = FastMCP("sample_server")

# 3. Register tools
server.add_tool(Tool(
    name="sample_tool",
    description="A simple example tool",
    function=sample_tool
))

server.add_tool(Tool(
    name="advanced_tool",
    description="A more complex tool with nested parameters",
    function=advanced_tool
))

# 4. Run server (blocks until terminated)
if __name__ == "__main__":
    server.run()
```

Key aspects:
- Clear tool function definitions with type hints
- Docstrings for tool descriptions
- Tool registration with server
- Server initialization and execution

## Advanced Usage Patterns

### 1. Custom Client Wrapper

For applications that need a higher-level interface to MCP:

```python
import os
import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

class MCPClient:
    """A higher-level wrapper for MCP client functionality"""
    
    def __init__(self):
        self.session = None
        self.transport = None
        self.tools = []
        self.connected = False
        
    async def connect(self, server_command="python -m mcp_server.main", token=None):
        """Connect to MCP server"""
        # Set environment with token if provided
        env = os.environ.copy()
        if token:
            env["API_TOKEN"] = token
            
        # Parse command and args
        parts = server_command.split()
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        
        # Setup transport
        self.transport = await stdio_client(
            StdioServerParameters(command=command, args=args, env=env)
        )
        stdin, stdout = self.transport
        
        # Create and initialize session
        self.session = ClientSession(stdin, stdout)
        await self.session.initialize()
        
        # Discover tools
        response = await self.session.list_tools()
        self.tools = response.tools
        self.connected = True
        
        return self.tools
        
    async def call_tool(self, tool_name, args):
        """Call a tool with arguments"""
        if not self.connected:
            raise RuntimeError("Not connected to MCP server")
            
        return await self.session.call_tool(tool_name, args)
        
    def get_tool_descriptions(self):
        """Get formatted descriptions of available tools"""
        if not self.connected:
            return "Not connected to MCP server"
            
        descriptions = []
        for tool in self.tools:
            desc = f"Tool: {tool.name}\n"
            desc += f"Description: {tool.description}\n"
            
            if tool.inputSchema:
                desc += "Parameters:\n"
                for param, details in tool.inputSchema.get("properties", {}).items():
                    required = "required" if param in tool.inputSchema.get("required", []) else "optional"
                    desc += f"  - {param}: {details.get('description', 'No description')} ({required})\n"
            
            descriptions.append(desc)
            
        return "\n".join(descriptions)
        
    async def cleanup(self):
        """Clean up resources"""
        if self.transport:
            await self.transport.aclose()
            self.transport = None
            self.session = None
            self.connected = False

# Example usage
async def use_custom_client():
    client = MCPClient()
    try:
        await client.connect(token="your_token_here")
        print(client.get_tool_descriptions())
        
        result = await client.call_tool("sample_tool", {"param1": "test"})
        print(f"Result: {result}")
    finally:
        await client.cleanup()

asyncio.run(use_custom_client())
```

Key benefits:
- Simplified API for common operations
- Built-in connection management
- Tool description formatting
- Automatic cleanup
- Token passing

### 2. Dynamic Tool Generation from API Specs

A common pattern is generating MCP tools from OpenAPI specifications:

```python
import json
import requests
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool

def create_dynamic_tools(server, openapi_spec_path):
    """Create MCP tools dynamically from an OpenAPI specification"""
    # Load OpenAPI spec (from file or URL)
    if openapi_spec_path.startswith(('http://', 'https://')):
        response = requests.get(openapi_spec_path)
        spec = response.json()
    else:
        with open(openapi_spec_path, "r") as f:
            spec = json.load(f)
    
    # Extract paths and operations
    paths = spec.get("paths", {})
    
    for path, methods in paths.items():
        for method, details in methods.items():
            # Skip if no operationId
            if "operationId" not in details:
                continue
                
            operation_id = details["operationId"]
            summary = details.get("summary", "")
            description = details.get("description", summary)
            
            # Create dynamic function
            async def dynamic_tool_function(**kwargs):
                """Dynamically created tool function"""
                # Implementation would make API call to the endpoint
                # For this example, we just return the arguments
                return {
                    "path": path,
                    "method": method,
                    "arguments": kwargs,
                    "status": "would make API call in real implementation"
                }
            
            # Set function metadata
            dynamic_tool_function.__name__ = operation_id
            dynamic_tool_function.__doc__ = description
            
            # Extract parameters for schema
            parameters = []
            for param in details.get("parameters", []):
                parameters.append(param)
            
            # Create input schema
            input_schema = {
                "type": "object",
                "properties": {},
                "required": []
            }
            
            for param in parameters:
                name = param["name"]
                schema = param.get("schema", {})
                required = param.get("required", False)
                
                input_schema["properties"][name] = schema
                if required:
                    input_schema["required"].append(name)
            
            # Register tool
            server.add_tool(Tool(
                name=operation_id,
                description=description,
                function=dynamic_tool_function,
                inputSchema=input_schema
            ))
            
            print(f"Registered dynamic tool: {operation_id}")

# Example usage
server = FastMCP("api_server")
create_dynamic_tools(server, "openapi.json")
server.run()
```

Key aspects:
- Loads and parses OpenAPI specification
- Creates dynamic functions for each operation
- Generates input schemas from parameter definitions
- Registers tools with the server

### 3. LLM Integration Pattern

A common pattern for integrating MCP with LLMs:

```python
import asyncio
import json
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

# Example LLM response processing function
def extract_tool_call(llm_response):
    """Extract tool call from LLM response"""
    # Look for a tool call pattern in the response
    # This example uses a simple JSON format, but could be XML or other format
    if "TOOL_CALL:" not in llm_response:
        return None
    
    try:
        # Extract the JSON between markers
        start = llm_response.find("TOOL_CALL:") + len("TOOL_CALL:")
        end = llm_response.find("END_TOOL_CALL")
        if end == -1:
            end = None
            
        tool_json = llm_response[start:end].strip()
        tool_data = json.loads(tool_json)
        
        return {
            "tool_name": tool_data.get("tool_name"),
            "args": tool_data.get("args", {})
        }
    except json.JSONDecodeError:
        return None

# Simulate LLM response (would be replaced with actual LLM API call)
def simulate_llm_response(prompt):
    """Simulate an LLM response for the example"""
    # In a real implementation, this would call an LLM API
    if "get_weather" in prompt and "location" in prompt:
        return """I'll check the weather for you.

TOOL_CALL:
{
  "tool_name": "get_weather",
  "args": {
    "location": "New York",
    "units": "metric"
  }
}
END_TOOL_CALL"""
    else:
        return "I don't have a specific tool for that query. How else can I help you?"

async def llm_with_tools_workflow(user_input, system_prompt=None):
    """Example workflow with LLM using MCP tools"""
    # 1. Connect to MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_server.main"]
    )
    
    async with stdio_client(server_params) as transport:
        stdin, stdout = transport
        session = ClientSession(stdin, stdout)
        
        # 2. Get available tools
        tools_response = await session.list_tools()
        tools = tools_response.tools
        
        # 3. Format tool descriptions for LLM prompt
        tool_descriptions = []
        for tool in tools:
            desc = f"Tool: {tool.name}\nDescription: {tool.description}\n"
            
            if tool.inputSchema:
                desc += "Parameters:\n"
                for param, details in tool.inputSchema.get("properties", {}).items():
                    required = "required" if param in tool.inputSchema.get("required", []) else "optional"
                    desc += f"  - {param}: {details.get('description', '')} ({required})\n"
            
            tool_descriptions.append(desc)
        
        # 4. Create LLM prompt with tools
        prompt = f"""
System: {system_prompt or 'You are a helpful assistant with access to tools.'}

Available Tools:
{'\n'.join(tool_descriptions)}

To use a tool, respond with:
TOOL_CALL:
{{
  "tool_name": "name_of_tool",
  "args": {{
    "param1": "value1",
    "param2": "value2"
  }}
}}
END_TOOL_CALL

User: {user_input}
"""
        
        # 5. Generate LLM response (simulated)
        llm_response = simulate_llm_response(prompt)
        
        # 6. Extract tool call from response
        tool_call = extract_tool_call(llm_response)
        if not tool_call:
            return llm_response
        
        # 7. Execute tool
        try:
            tool_result = await session.call_tool(
                tool_call["tool_name"],
                tool_call["args"]
            )
            
            # 8. Generate final response with tool result
            final_prompt = f"""
{prompt}

I executed the tool {tool_call['tool_name']} with the arguments:
{json.dumps(tool_call['args'], indent=2)}

The result was:
{json.dumps(tool_result, indent=2)}

Please provide a final response based on this information.
"""
            
            # 9. Generate final LLM response
            final_response = simulate_llm_response(final_prompt)
            
            # Return either the final response or original with tool result
            return final_response
        except Exception as e:
            # Return error information
            return f"Error executing tool: {str(e)}"

# Example usage
async def main():
    result = await llm_with_tools_workflow("What's the weather like in New York?")
    print(result)

asyncio.run(main())
```

Key aspects:
- Dynamic tool discovery for up-to-date capabilities
- Structured prompt engineering with tool descriptions
- Pattern-based extraction of tool calls from LLM responses
- Multi-step conversation flow with tool execution
- Error handling for failed tool calls

### 4. Authentication Patterns

The MCP system supports several authentication patterns:

```python
# 1. Environment Variable Authentication
import os

os.environ["API_TOKEN"] = "your_secure_token"
server_params = StdioServerParameters(
    command="python",
    args=["-m", "mcp_server.main"],
    env={"DYNAMIC_API_TOKEN": os.environ["API_TOKEN"]}
)

# 2. Token Refresh Pattern
async def get_token_and_connect(client):
    """Example of token refresh pattern"""
    # This function would get a fresh token from an auth service
    token = await fetch_new_token_from_auth_service()
    
    # Connect with the fresh token
    await client.connect(token=token)
    
    # Schedule token refresh before expiration
    token_lifetime = 3600  # seconds
    refresh_margin = 300   # refresh 5 minutes before expiry
    
    async def refresh_token():
        await asyncio.sleep(token_lifetime - refresh_margin)
        await get_token_and_connect(client)
    
    # Start refresh task in background
    asyncio.create_task(refresh_token())

# 3. Production vs Development Pattern
def start_server(production_mode=False):
    """Example of production vs development mode pattern"""
    env = {}
    
    if production_mode:
        # In production, require dynamic token from client
        env["PRODUCTION_MODE"] = "TRUE"
    else:
        # In development, use static token from .env file
        env["PRODUCTION_MODE"] = "FALSE"
        
    return StdioServerParameters(
        command="python",
        args=["-m", "mcp_server.main"],
        env=env
    )

# 4. Tool Discovery Bypass Pattern
def start_server_with_discovery_bypass():
    """Example of allowing tool discovery without authentication"""
    env = {
        "PRODUCTION_MODE": "TRUE",
        "ALLOW_TOOL_DISCOVERY_WITHOUT_TOKEN": "TRUE"
    }
    
    return StdioServerParameters(
        command="python",
        args=["-m", "mcp_server.main"],
        env=env
    )
```

Key aspects:
- Environment-based token passing
- Token refresh mechanisms for long-running sessions
- Production vs development authentication modes
- Selective authentication bypass for tool discovery

These patterns and workflows demonstrate the flexibility of the Model Context Protocol and its Python SDK, enabling a wide range of implementation approaches for various use cases.
