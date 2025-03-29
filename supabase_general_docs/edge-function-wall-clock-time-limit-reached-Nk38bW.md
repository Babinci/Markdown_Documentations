# Resolving "Wall Clock Time Limit Reached" in Edge Functions

## What Does This Error Mean?

The message "wall clock time limit reached" indicates that your Edge Function has reached the maximum allowed execution time. This time is measured like a real clock on the wall - it includes the entire duration a process takes to complete, including any waiting time or periods of inactivity.

When this message appears in your Edge Function logs, it means that the function has been terminated after either:
- Reaching the specified wall clock duration limit
- Hitting a resource limit such as CPU time used or memory utilized

## Current Limits

Edge Functions on Supabase have the following execution limits:

- **Wall Clock Time Limit**: 400 seconds for the total duration your Edge Function can run
- **CPU Execution Time**: 200 milliseconds of active computing time

## Understanding the Warning Message

Important: The "wall clock time limit reached" message is sometimes expected and not always an error. This message is automatically printed when a worker has been terminated, even if it hasn't actually reached the time limit.

However, if your function terminates with this warning **and returns a 546 error response**, this indicates that your function is genuinely exceeding the allowed execution time.

## Troubleshooting Steps

If you're facing the "wall clock time limit reached" error with a 546 error code, follow these steps:

1. **Review Your Function's Logic**
   - Look for inefficient operations or prolonged processes
   - Optimize code and minimize unnecessary calculations
   - Implement asynchronous operations where possible

2. **Divide Complex Tasks**
   - Break down complex functions into smaller, more focused functions
   - This approach helps manage workloads more effectively
   - Consider using background tasks for longer operations

3. **Monitor Execution Time**
   - Use Supabase's logging tools to track your function's performance
   - Access logs at: [Supabase Project Functions](https://app.supabase.com/project/_/functions)
   - Select your function and click on "Logs"

4. **Check Documentation**
   - For more debugging tips, refer to: [Debugging Edge Functions](https://supabase.com/docs/guides/functions/debugging#logs--debugging)

## Future Considerations

There are plans to make the wall clock time limit configurable per project in the future. Currently, the only way to adjust this limit is by self-hosting [Edge Functions](https://github.com/supabase/edge-runtime/).

Stay updated on changes by regularly checking the [Supabase Changelog](https://github.com/orgs/supabase/discussions/categories/changelog).