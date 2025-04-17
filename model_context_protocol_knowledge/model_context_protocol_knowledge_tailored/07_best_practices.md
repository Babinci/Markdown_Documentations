# Model Context Protocol (MCP) - Best Practices and Gotchas

This section outlines best practices for using the Model Context Protocol and highlights common pitfalls to avoid.

## Security Best Practices

### Authentication and Authorization

1. **Never hardcode bearer tokens in source code**
   - ✅ Use environment variables, secure vaults, or runtime parameters
   - ❌ Don't include tokens in code, config files in version control, or logs

2. **Use dynamic tokens in production**
   - ✅ Generate short-lived tokens with appropriate scopes
   - ❌ Don't use static tokens that never expire in production

3. **Be cautious with tool discovery permissions**
   - ✅ Only enable `ALLOW_TOOL_DISCOVERY_WITHOUT_TOKEN` in controlled environments
   - ❌ Don't enable this setting if tool list contains sensitive information

4. **Log authentication events appropriately**
   - ✅ Log authentication failures and bypass events
   - ❌ Don't log full tokens, even in debug mode (log prefixes only)

5. **Apply the principle of least privilege**
   - ✅ Use token scopes or API whitelist/blacklist to restrict access
   - ❌ Don't grant more access than needed for the specific use case

### API Security

1. **Validate all external API inputs**
   - ✅ Use generated Pydantic models to validate inputs before passing to APIs
   - ❌ Don't blindly pass user inputs to external systems

2. **Apply proper request sanitization**
   - ✅ Validate and sanitize path parameters, query parameters, and headers
   - ❌ Don't trust that LLMs will always format inputs correctly

3. **Use HTTPS for all API connections**
   - ✅ Ensure API_BASE_URL uses HTTPS protocol
   - ❌ Don't use unencrypted HTTP in production

## Performance Best Practices

### Efficient Tool Execution

1. **Cache tool information**
   - ✅ Cache tool descriptions and schemas after initial discovery
   - ❌ Don't call `list_tools` unnecessarily for each interaction

2. **Consider batch operations**
   - ✅ Use batch APIs where available instead of multiple individual calls
   - ❌ Don't make sequential API calls when a single batch operation would work

3. **Implement appropriate timeouts**
   - ✅ Set reasonable timeouts based on expected tool execution time
   - ❌ Don't use very long or indefinite timeouts that could block the system

4. **Monitor tool execution times**
   - ✅ Log execution duration for performance analysis
   - ❌ Don't ignore consistently slow tools that may need optimization

### Resource Management

1. **Clean up resources properly**
   - ✅ Always call `cleanup()` when done with the MCP client
   - ❌ Don't leave connections open indefinitely

2. **Reuse client connections**
   - ✅ Create a single client instance and reuse it for multiple operations
   - ❌ Don't create new connections for every tool call

3. **Implement appropriate error handling**
   - ✅ Add retry logic with backoff for transient errors
   - ❌ Don't retry indefinitely without limits

## Integration with LLMs

### Prompt Engineering

1. **Use dynamic system prompt generation**
   - ✅ Use `get_system_prompt()` to generate prompts with current tool information
   - ✅ Pass the bearer token to ensure authenticated tool discovery
   - ❌ Don't hardcode tool descriptions that might become outdated

2. **Structure tool usage with XML format**
   - ✅ Follow the established XML format for tool requests:
     ```xml
     <use_mcp_tool>
     <server_name>jobassistant</server_name>
     <tool_name>get_weather</tool_name>
     <arguments>
     {
       "location": "New York"
     }
     </arguments>
     </use_mcp_tool>
     ```
   - ❌ Don't use inconsistent formats that the parser might not recognize

3. **Implement robust parsing logic**
   - ✅ Use regex patterns that account for whitespace and formatting variations
   - ✅ Handle JSON parsing errors gracefully
   - ✅ Extract all required components (server_name, tool_name, arguments)
   - ❌ Don't rely on simple string splitting that might fail with complex outputs

4. **Structure conversation flow with tool results**
   - ✅ Include tool results in conversation history for context
   - ✅ Use structured message types with tool flags
   - ✅ Track which messages contain tool calls and results
   - ❌ Don't lose track of the conversation state when tools are used

### Error Handling

1. **Provide helpful error messages**
   - ✅ Return descriptive error messages that guide the LLM to correct usage
   - ❌ Don't return technical errors without explanation

2. **Implement graceful fallbacks**
   - ✅ Have strategies for when tools are unavailable or fail
   - ❌ Don't leave the LLM unable to respond when tools fail

## Common Gotchas and Pitfalls

### 1. Bearer Token Issues

**Problem**: Authentication fails despite providing a token
```
Error: Failed to connect to MCP server: Authentication failed
```

**Common Causes**:
- Token has incorrect format
- Token is expired
- Token lacks required permissions
- Production mode is enabled but no dynamic token provided

**Solution**:
```python
# Verify token format and validity
# Check PRODUCTION_MODE setting
# Ensure token has appropriate permissions
# Use proper environment variable settings:

# For development:
os.environ["PRODUCTION_MODE"] = "FALSE"

# For production:
os.environ["PRODUCTION_MODE"] = "TRUE"
os.environ["DYNAMIC_API_TOKEN"] = "valid_token_here"
```

### 2. Tool Discovery Failures

**Problem**: No tools are returned despite successful connection
```
Found 0 available tools
```

**Common Causes**:
- API whitelist/blacklist configuration is incorrect
- OpenAPI specification couldn't be loaded
- Path to OpenAPI spec is incorrect
- Permission issues with OpenAPI spec access

**Solution**:
```python
# Check whitelist/blacklist configuration
os.environ["API_WHITE_LIST"] = "[]"  # Empty list to allow all
os.environ["API_BLACK_LIST"] = "[]"  # Empty list to block none

# Verify OpenAPI spec path
os.environ["OPENAPI_SPEC_PATH"] = "/correct/path/to/openapi.json"

# Check logs for more detailed error messages
```

### 3. Tool Execution Validation Errors

**Problem**: Tool calls fail with validation errors
```
Error: Invalid parameter: 'locaton' is not a valid parameter (did you mean 'location'?)
```

**Common Causes**:
- Typos in parameter names
- Incorrect parameter types
- Missing required parameters
- Incorrectly formatted parameter values

**Solution**:
```python
# Always check the tool's input schema before calling
tools = await client.get_available_tools()
schema = next(t["input_schema"] for t in tools if t["name"] == "get_weather")
print(f"Required parameters: {schema.get('required', [])}")
print(f"Properties: {schema.get('properties', {})}")

# Validate arguments match schema before calling
args = {
    "location": "New York",  # Correct spelling
    "units": "metric"        # Match expected values
}
```

### 4. OpenAPI Spec Loading Issues

**Problem**: Server fails to start due to OpenAPI spec issues
```
Error: Failed to load OpenAPI spec: No content retrieved
```

**Common Causes**:
- Invalid URL or file path
- Network connectivity issues
- Authentication required for spec access
- Malformed OpenAPI specification

**Solution**:
```python
# For local files, verify path
os.environ["OPENAPI_SPEC_PATH"] = os.path.abspath("./openapi.json")

# For URLs, include necessary headers
os.environ["API_HEADERS"] = "Authorization:Bearer token,Accept:application/json"

# Verify spec is valid JSON and follows OpenAPI standard
# Use a tool like Swagger Editor to validate the spec
```

### 5. Data Type Conversion Issues

**Problem**: Parameters are passed but API calls fail with type errors
```
Error: Expected integer for 'limit', got string '10'
```

**Common Causes**:
- JSON serialization converting numbers to strings
- Boolean values converted to strings
- Date/time format mismatches
- Nested object formatting issues

**Solution**:
```python
# Explicitly convert types before passing to tool
args = {
    "keywords": "python developer",
    "limit": int(10),  # Explicitly convert to int
    "remote_only": bool(True)  # Explicitly convert to boolean
}

# For dates, use ISO format
from datetime import datetime
args["start_date"] = datetime.now().isoformat()
```

### 6. Concurrency and Connection Issues

**Problem**: Connections fail or hang in multi-threaded environments
```
Error: Connection timeout or Event loop is closed
```

**Common Causes**:
- Using synchronous code with async functions
- Running in wrong event loop
- Not properly awaiting async operations
- Connection cleanup issues

**Solution**:
```python
# Ensure proper async/await usage
async def main():
    client = MCPClient()
    try:
        await client.connect_to_server()
        result = await client.call_tool("get_weather", {"location": "London"})
        print(result)
    finally:
        # Always cleanup
        await client.cleanup()

# Run in proper event loop
import asyncio
asyncio.run(main())
```

### 7. Environment Configuration Confusion

**Problem**: Server starts but with unexpected configuration
```
WARNING: PRODUCTION_MODE enabled but no dynamic token provided. Using static token from .env
```

**Common Causes**:
- Conflicting environment variables
- Command line arguments overriding environment variables
- Config file settings not being applied
- Environment variables not properly exported

**Solution**:
```python
# Be explicit about all configuration
os.environ.clear()  # Clear existing to avoid conflicts
os.environ.update({
    "PRODUCTION_MODE": "TRUE",
    "DYNAMIC_API_TOKEN": "your_token",
    "OPENAPI_SPEC_PATH": "https://example.com/openapi.json",
    "API_BASE_URL": "https://example.com/api",
    "LOG_LEVEL": "INFO"
})

# Or use a clean environment for subprocess
import subprocess
subprocess.run(
    ["python", "-m", "mcp_server.my_openapi_mcp.main"],
    env={"PRODUCTION_MODE": "TRUE", "DYNAMIC_API_TOKEN": "your_token"}
)
```

### 8. XML Tool Request Parsing Issues

**Problem**: LLM response contains a tool call but extraction fails
```
None returned from extract_tool_command, despite <use_mcp_tool> in response
```

**Common Causes**:
- Malformed XML in LLM response
- Missing required elements (server_name, tool_name, arguments)
- Invalid JSON in arguments section
- Nested or overlapping XML tags
- Whitespace or formatting issues affecting regex matching

**Solution**:
```python
# More robust extraction with flexible regex
async def extract_tool_command(llm_response: str) -> Optional[Dict[str, Any]]:
    """Extract tool command with more robust regex patterns"""
    # Look for the tool pattern with flexible whitespace
    tool_pattern = r'<use_mcp_tool>\s*(.*?)\s*</use_mcp_tool>'
    match = re.search(tool_pattern, llm_response, re.DOTALL)
    
    if not match:
        return None
    
    tool_content = match.group(1)
    
    # Extract required components with flexible whitespace
    patterns = {
        "server_name": r'<server_name>\s*(.*?)\s*</server_name>',
        "tool_name": r'<tool_name>\s*(.*?)\s*</tool_name>',
        "arguments": r'<arguments>\s*(.*?)\s*</arguments>'
    }
    
    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, tool_content, re.DOTALL)
        if not match:
            logger.warning(f"Failed to extract {key} from tool request")
            return None
        extracted[key] = match.group(1).strip()
    
    # Parse JSON with error handling
    try:
        arguments = json.loads(extracted["arguments"])
    except json.JSONDecodeError as e:
        logger.warning(f"Failed to parse arguments JSON: {e}")
        logger.debug(f"Arguments string: {extracted['arguments']}")
        return None
    
    return {
        "server_name": extracted["server_name"],
        "tool_name": extracted["tool_name"],
        "arguments": arguments
    }
```

### 9. Tool Response Parsing Issues

**Problem**: Tool executes but response handling fails
```
Error: 'content' field not found in response
```

**Common Causes**:
- Response format changed in API
- Error response not properly handled
- JSON parsing errors
- Missing or renamed fields
- Tool execution failed but error not properly captured

**Solution**:
```python
# Always check status before accessing content
result = await client.call_tool("get_weather", {"location": "London"})
if result["status"] == "success":
    # Use defensive access with .get() to avoid KeyError
    temp = result.get("content", {}).get("temperature", "N/A")
    print(f"Temperature: {temp}")
else:
    print(f"Error: {result.get('content', 'Unknown error')}")

# For more complex responses, add validation
import jsonschema
expected_schema = {
    "type": "object",
    "required": ["temperature", "conditions"],
    "properties": {
        "temperature": {"type": "number"},
        "conditions": {"type": "string"}
    }
}
try:
    jsonschema.validate(result["content"], expected_schema)
    # Process content
except jsonschema.exceptions.ValidationError:
    print("Response format not as expected")
```

## Debugging Strategies

### 1. Enable Debug Logging

```python
# In client code
import logging
logging.getLogger("mcp").setLevel(logging.DEBUG)

# For server
os.environ["DEBUG"] = "TRUE"
```

### 2. Inspect Request and Response Logs

```bash
# Check server logs
cat ./logs/logs_server.log

# Check request logs
cat ./logs/logs_requests.log
```

### 3. Use Tool Introspection

```python
# Get detailed tool information
tools = await client.get_available_tools()
for tool in tools:
    print(f"\nTool: {tool['name']}")
    print(f"Description: {tool['description']}")
    print("Input Schema:")
    import json
    print(json.dumps(tool['input_schema'], indent=2))
```

### 4. Test Tools in Isolation

```python
# Test a specific tool directly
async def test_tool(tool_name, args):
    client = MCPClient()
    try:
        await client.connect_to_server()
        print(f"Testing {tool_name} with args: {args}")
        result = await client.call_tool(tool_name, args)
        print(f"Status: {result['status']}")
        print(f"Content: {result['content']}")
    finally:
        await client.cleanup()

# Run tests
asyncio.run(test_tool("get_weather", {"location": "London"}))
```

By following these best practices and being aware of common pitfalls, you'll be able to effectively use the Model Context Protocol in your applications while avoiding major issues.
