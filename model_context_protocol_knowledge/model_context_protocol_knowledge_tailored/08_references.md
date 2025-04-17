# Model Context Protocol (MCP) - References

This section provides references to key files in the codebase with brief descriptions of their purpose. These references serve as pointers for developers seeking more detailed implementation information.

## MCP Client References

### Core Client Implementation

| File | Description |
|------|-------------|
| `mcp_client/jobassistant_mcp_client/core/mcp.py` | Main MCP client implementation containing the `MCPClient` class that handles connection management, tool discovery, and execution |
| `mcp_client/jobassistant_mcp_client/config/mcp_settings.json` | Configuration file containing server connection parameters including command, arguments, and environment settings |
| `mcp_client/jobassistant_mcp_client/core/orchestrator.py` | LLM orchestration layer that integrates with various providers (Google, OpenRouter, LMStudio) and manages rate limits |

### API and Router Implementation

| File | Description |
|------|-------------|
| `mcp_client/jobassistant_mcp_client/routers/api_mcp.py` | FastAPI router that exposes MCP functionality through HTTP endpoints for status, connection, tool listing, and execution |
| `mcp_client/jobassistant_mcp_client/routers/api_conversation_tools.py` | FastAPI router for conversation management with integrated tool execution, parsing, and result handling |

### System Prompt Generation

| File | Description |
|------|-------------|
| `mcp_client/jobassistant_mcp_client/system_prompt_generator.py` | Dynamically generates system prompts that include MCP tool information, with caching and multiple fallback strategies |
| `mcp_client/jobassistant_mcp_client/system_prompts/system_prompt_template.md` | Template for system prompts with placeholders for dynamic tool information and detailed XML formatting instructions |

### Client Schema Files

| File | Description |
|------|-------------|
| `mcp_client/jobassistant_mcp_client/schemas/tool.py` | Defines `ToolRequest` and `ToolResponse` models for tool execution |
| `mcp_client/jobassistant_mcp_client/schemas/conversation.py` | Defines conversation and message models with specialized fields for tool calls and results |

## MCP Server References

### Main Server Implementation

| File | Description |
|------|-------------|
| `mcp_server/my_openapi_mcp/main.py` | Entry point for the MCP server with authentication flow, configuration loading, and server lifecycle management |
| `mcp_server/my_openapi_mcp/tools.py` | Dynamic tool generation from OpenAPI specifications |
| `mcp_server/my_openapi_mcp/schemas.py` | Pydantic model generation for request validation |
| `mcp_server/my_openapi_mcp/utils.py` | Utility functions for OpenAPI parsing, logging setup, and schema resolution |

### Server Configuration and Analysis

| File | Description |
|------|-------------|
| `mcp_server/my_openapi_mcp/auth_flow_analysis.md` | Detailed analysis of the authentication flow in the MCP server |
| `mcp_server/my_openapi_mcp/load_config.py` | Configuration loading from environment variables and config files |

## Key Code Snippets

### MCP Client Connection

```python
# From mcp_client/jobassistant_mcp_client/core/mcp.py
async def connect_to_server(self, bearer_token=None):
    """
    Connect to the JobAssistant MCP server using the configuration from mcp_settings.json
    
    Args:
        bearer_token (str, optional): Authorization bearer token to pass to the server in production mode
            
    Returns:
        bool: True if connected successfully, False otherwise
    """
    # Log the token status (only first few characters for security)
    if bearer_token:
        logger.info(f"Connect request with bearer token: {bearer_token[:8]}...")
    else:
        logger.info("Connect request without bearer token")
    # Prevent multiple connection attempts
    async with self._connect_lock:
        if self._connecting:
            logger.info("Connection attempt already in progress")
            return False
                
        if self.session is not None:
            # If token changed, we need to reconnect
            if bearer_token is not None and self.token != bearer_token:
                logger.info("Bearer token changed, reconnecting to MCP server")
                await self.cleanup()
            else:
                logger.info("Already connected to MCP server")
                return True
                
        self._connecting = True
        # Store the token
        self.token = bearer_token
```

### MCP Server Tool Generation

```python
# From mcp_server/my_openapi_mcp/tools.py
def create_dynamic_tools(mcp, API_BASE_URL, API_HEADERS, API_WHITE_LIST, API_BLACK_LIST, 
                         openapi_spec_json, version, logs_dir=None, requests_log_file=None):
    """
    Create dynamic tools for the FastMCP server
    
    Args:
        mcp: FastMCP instance
        API_BASE_URL: Base URL for API requests
        API_HEADERS: Headers to include in API requests
        API_WHITE_LIST: White list of operationIds
        API_BLACK_LIST: Black list of operationIds
        openapi_spec_json: OpenAPI specification as JSON
        version: OpenAPI version
        logs_dir: Logs directory
        requests_log_file: Requests log file path
    
    Returns:
        None
    """
    from utils import extract_api_metadata
    from schemas import create_pydantic_model_from_json, get_param_type, model_cache, model_mapping
    
    # Make these variables available to dynamically generated functions
    globals()['API_BASE_URL'] = API_BASE_URL
    globals()['API_HEADERS'] = API_HEADERS
    globals()['API_WHITE_LIST'] = API_WHITE_LIST
    globals()['API_BLACK_LIST'] = API_BLACK_LIST
    
    logger.info("Loading Tools From Swagger Spec")
    
    # ... rest of the implementation
```

### Authentication Flow Validation

```python
# From mcp_server/my_openapi_mcp/main.py
def _validate_authentication():
    """Validate authentication settings for production mode"""
    global PRODUCTION_MODE, DYNAMIC_API_TOKEN, ALLOW_TOOL_DISCOVERY_WITHOUT_TOKEN
    
    # Ensure a dynamic token is provided in production mode before proceeding
    # Only enforce this if tool discovery without token is not allowed
    if PRODUCTION_MODE and not DYNAMIC_API_TOKEN and not ALLOW_TOOL_DISCOVERY_WITHOUT_TOKEN:
        # Use logger here now that it's initialized
        logger.critical("PRODUCTION MODE is enabled, but no DYNAMIC_API_TOKEN was provided by the client. Exiting.")
        sys.exit(1)
    
    # Special case for tool discovery without token
    if PRODUCTION_MODE and not DYNAMIC_API_TOKEN and ALLOW_TOOL_DISCOVERY_WITHOUT_TOKEN:
        logger.warning("SECURITY: Running in production mode without token, but tool discovery is allowed")
        logger.warning("SECURITY: Only the list_tools operation will work, all other operations will require a token")
```

## MCP Protocol References

### FastMCP Base Implementation

The FastMCP class that the custom implementation extends is part of the imported MCP library. It provides:

- Server initialization
- Tool registration
- JSON-RPC message handling
- Session management

### MCP Protocol Format

The MCP protocol is based on JSON-RPC 2.0 with standard message formats:

```json
// Request format
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "method": "operation-name",
  "params": { ... }
}

// Response format
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "result": { ... }
}

// Error format
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "error": {
    "code": error-code,
    "message": "error-message",
    "data": { ... }
  }
}
```

## External References

While no external documentation is provided in the current code base, developers may want to refer to:

1. **MCP Library Documentation**: The base MCP library used (imported as `from mcp.server.fastmcp import FastMCP`) should have its own documentation that explains the underlying protocol in more detail.

2. **OpenAPI/Swagger Documentation**: Since the MCP server generates tools from OpenAPI specifications, the [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) is a useful reference.

3. **JSON-RPC 2.0 Specification**: The [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification) provides details on the underlying protocol format.

4. **Pydantic Documentation**: The MCP server uses Pydantic for model validation, so the [Pydantic documentation](https://docs.pydantic.dev/) is useful for understanding schema validation.

## File Structure Overview

```
mcp_client/
└── jobassistant_mcp_client/
    ├── config/
    │   └── mcp_settings.json  # Server configuration
    ├── core/
    │   ├── mcp.py             # Main MCP client implementation
    │   └── orchestrator.py    # LLM orchestration
    ├── routers/
    │   ├── api_conversation_tools.py  # Conversation API with tool integration
    │   └── api_mcp.py         # REST API for MCP functionality
    ├── schemas/
    │   ├── conversation.py    # Conversation models
    │   └── tool.py            # Tool request/response models
    ├── system_prompts/
    │   └── system_prompt_template.md # Template for LLM system prompts
    └── system_prompt_generator.py # Dynamic prompt generation

mcp_server/
└── my_openapi_mcp/
    ├── auth_flow_analysis.md  # Authentication flow documentation
    ├── load_config.py         # Configuration loading
    ├── main.py                # Server entry point with CustomFastMCP
    ├── schemas.py             # Dynamic model generation
    ├── tools.py               # Dynamic tool generation from OpenAPI
    └── utils.py               # Utility functions for logging, API processing
```

This reference section provides pointers to the most important parts of the codebase for developers seeking to understand, modify, or extend the Model Context Protocol implementation in the JobAssistant AI Agent project.
