# Using Realtime with Next.js

In this guide, we explore the best ways to receive real-time Postgres changes with your Next.js application. We'll show both client and server side updates, and explore which option is best for different scenarios.

## Overview

Supabase Realtime enables you to:

- Listen to database changes in real-time
- Update your UI automatically when data changes
- Implement collaborative features
- Build interactive applications

## Client vs. Server Components

Next.js App Router introduces two component types:

1. **Server Components** - Render on the server, but don't update in real-time
2. **Client Components** - Render on the client and can update dynamically

This guide explores both approaches for integrating Supabase Realtime.

## Video Tutorial

For a comprehensive walkthrough that covers both client and server approaches:

<iframe width="560" height="315" src="https://www.youtube.com/embed/YR-xP6PPXXA" title="Client vs Server Components in Next.js app directory // Merging server state with realtime updates" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Watch on YouTube](https://www.youtube.com/watch?v=YR-xP6PPXXA)

## Client-Side Implementation

Client components can establish websocket connections and update in real-time. Here's how to implement Realtime in a client component:

```tsx
'use client'

import { useEffect, useState } from 'react'
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs'
import type { Database } from '@/lib/database.types'

export default function RealtimeMessages() {
  const [messages, setMessages] = useState<any[]>([])
  const supabase = createClientComponentClient<Database>()

  useEffect(() => {
    // Initial data fetch
    const fetchMessages = async () => {
      const { data, error } = await supabase
        .from('messages')
        .select('*')
        .order('created_at', { ascending: false })
      
      if (data) setMessages(data)
    }
    
    fetchMessages()
    
    // Set up realtime subscription
    const channel = supabase.channel('realtime-messages')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'messages',
        },
        (payload) => {
          // Handle different events
          if (payload.eventType === 'INSERT') {
            setMessages(prevMessages => [payload.new, ...prevMessages])
          } else if (payload.eventType === 'UPDATE') {
            setMessages(prevMessages => 
              prevMessages.map(message => 
                message.id === payload.new.id ? payload.new : message
              )
            )
          } else if (payload.eventType === 'DELETE') {
            setMessages(prevMessages => 
              prevMessages.filter(message => message.id !== payload.old.id)
            )
          }
        }
      )
      .subscribe()
    
    // Cleanup function
    return () => {
      supabase.removeChannel(channel)
    }
  }, [supabase])
  
  return (
    <div>
      <h1>Messages</h1>
      <ul>
        {messages.map((message) => (
          <li key={message.id}>{message.content}</li>
        ))}
      </ul>
    </div>
  )
}
```

## Server-Side Implementation with Client Updates

You can combine server-side rendering with client-side updates for the best of both worlds:

```tsx
// page.tsx (Server Component)
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs'
import { cookies } from 'next/headers'
import type { Database } from '@/lib/database.types'
import RealtimeMessages from './realtime-messages'

export default async function Home() {
  const supabase = createServerComponentClient<Database>({ cookies })
  
  // Server-side data fetching
  const { data: initialMessages } = await supabase
    .from('messages')
    .select('*')
    .order('created_at', { ascending: false })
  
  return (
    <main>
      <h1>Supabase Realtime Demo</h1>
      {/* Pass initial data to client component */}
      <RealtimeMessages initialMessages={initialMessages || []} />
    </main>
  )
}

// realtime-messages.tsx (Client Component)
'use client'

import { useEffect, useState } from 'react'
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs'
import type { Database } from '@/lib/database.types'

export default function RealtimeMessages({ 
  initialMessages 
}: { 
  initialMessages: any[] 
}) {
  const [messages, setMessages] = useState(initialMessages)
  const supabase = createClientComponentClient<Database>()

  useEffect(() => {
    const channel = supabase.channel('realtime-messages')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'messages',
        },
        (payload) => {
          // Handle the realtime updates
          // (same handling logic as in the client-side example)
        }
      )
      .subscribe()
    
    return () => {
      supabase.removeChannel(channel)
    }
  }, [supabase])
  
  return (
    <div>
      <ul>
        {messages.map((message) => (
          <li key={message.id}>{message.content}</li>
        ))}
      </ul>
    </div>
  )
}
```

## Best Practices

1. **Optimize Initial Load**:
   - Use server components for the initial data fetch to improve SEO and loading performance
   - Pass the initial data to client components

2. **Minimize Client-Side Code**:
   - Keep realtime-specific code in client components
   - Use server components for everything else

3. **Efficient Subscription Management**:
   - Subscribe only to the specific tables and columns you need
   - Properly clean up subscriptions when components unmount

4. **State Management**:
   - Consider using a state management solution like Zustand, Jotai, or React Context for more complex applications
   - Keep realtime state consistent with server state

5. **Error Handling**:
   - Implement reconnection logic for dropped connections
   - Provide meaningful feedback to users when realtime updates fail

## Advanced Patterns

### Optimistic Updates

Update the UI immediately when a user takes an action, then confirm with the real-time response:

```tsx
function MessageList() {
  const [messages, setMessages] = useState([])
  const [optimisticMessages, setOptimisticMessages] = useState([])
  
  async function addMessage(content) {
    // Generate a temporary ID
    const tempId = `temp-${Date.now()}`
    
    // Add optimistic message
    setOptimisticMessages([...optimisticMessages, { id: tempId, content }])
    
    // Send to server
    const { data, error } = await supabase
      .from('messages')
      .insert({ content })
      .select()
    
    // Remove optimistic message when real message is received via subscription
  }
}
```

### Custom Hooks

Create reusable hooks for common realtime patterns:

```tsx
// useRealtimeTable.ts
export function useRealtimeTable(table, queryOptions = {}) {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const supabase = createClientComponentClient()
  
  useEffect(() => {
    // Initial fetch
    const fetchData = async () => {
      setLoading(true)
      try {
        const { data: result, error: queryError } = await supabase
          .from(table)
          .select('*')
          .order('created_at', { ascending: false })
          
        if (queryError) throw queryError
        setData(result)
      } catch (err) {
        setError(err)
      } finally {
        setLoading(false)
      }
    }
    
    fetchData()
    
    // Realtime subscription
    const channel = supabase.channel(`realtime-${table}`)
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table,
        },
        (payload) => {
          if (payload.eventType === 'INSERT') {
            setData(prev => [payload.new, ...prev])
          } else if (payload.eventType === 'UPDATE') {
            setData(prev => 
              prev.map(item => item.id === payload.new.id ? payload.new : item)
            )
          } else if (payload.eventType === 'DELETE') {
            setData(prev => 
              prev.filter(item => item.id !== payload.old.id)
            )
          }
        }
      )
      .subscribe()
      
    return () => {
      supabase.removeChannel(channel)
    }
  }, [table, JSON.stringify(queryOptions)])
  
  return { data, loading, error }
}

// Usage
function MessagesComponent() {
  const { data: messages, loading } = useRealtimeTable('messages', {
    order: { column: 'created_at', ascending: false },
    limit: 50
  })
  
  if (loading) return <div>Loading...</div>
  
  return (
    <ul>
      {messages.map(message => (
        <li key={message.id}>{message.content}</li>
      ))}
    </ul>
  )
}
```

## Performance Considerations

When using Realtime with Next.js, consider these performance tips:

1. **Selective Subscriptions**: Subscribe only to necessary tables and columns
   ```tsx
   .on('postgres_changes', {
     event: 'INSERT',
     schema: 'public',
     table: 'messages',
     filter: 'room_id=eq.123'
   })
   ```

2. **Debounce Frequent Updates**: For high-frequency updates, debounce state updates
   ```tsx
   import { debounce } from 'lodash'
   
   // Debounced state update for cursor positions
   const debouncedUpdateCursor = debounce((position) => {
     setCursorPosition(position)
   }, 50)
   ```

3. **Virtualization for Long Lists**: Use a virtualization library for long lists that update in real-time
   ```tsx
   import { FixedSizeList } from 'react-window'
   
   // In your component
   return (
     <FixedSizeList
       height={500}
       width="100%"
       itemCount={messages.length}
       itemSize={50}
     >
       {({ index, style }) => (
         <div style={style}>
           {messages[index].content}
         </div>
       )}
     </FixedSizeList>
   )
   ```

4. **Selective Re-rendering**: Use React.memo and careful state management to prevent unnecessary re-renders

## Conclusion

Using Supabase Realtime with Next.js provides a powerful combination for building responsive, real-time applications. By leveraging server components for the initial load and client components for real-time updates, you can create applications that are both performant and reactive to data changes.
