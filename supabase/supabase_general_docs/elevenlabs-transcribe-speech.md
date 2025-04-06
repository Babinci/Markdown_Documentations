# Building a Speech Transcription Telegram Bot

This tutorial explains how to build a Telegram bot that transcribes audio and video messages in 99 languages using TypeScript with Deno in Supabase Edge Functions and the ElevenLabs Scribe model.

## Introduction

The bot you'll build can:
- Receive voice messages, audio, and video files from Telegram users
- Transcribe the speech content using ElevenLabs' speech-to-text API
- Reply with accurate transcriptions in the original language
- Log all transcription activities in a Supabase database

You can test the finished product at [t.me/ElevenLabsScribeBot](https://t.me/ElevenLabsScribeBot) or find the [example project on GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/speech-to-text/telegram-transcription-bot).

## Requirements

Before getting started, you'll need:
- An [ElevenLabs](https://elevenlabs.io/) account with an API key
- A [Supabase](https://supabase.com/) account (sign up via [database.new](https://database.new/))
- The [Supabase CLI](https://supabase.com/docs/guides/local-development) installed
- The [Deno runtime](https://docs.deno.com/runtime/getting_started/installation/) installed
- A [Telegram](https://telegram.org/) account

## Setup Process

### 1. Register a Telegram Bot

Use the [BotFather](https://t.me/BotFather) to create a new Telegram bot:
1. Start a chat with BotFather
2. Send the `/newbot` command
3. Follow the instructions to set a name and username
4. Receive your secret bot token (keep this secure)

### 2. Create a Supabase Project

After installing the Supabase CLI, initialize a local project:

```bash
supabase init
```

### 3. Create a Database Table for Logs

Create a new migration:

```bash
supabase migrations new init
```

Add the following SQL to the migration file:

```sql
CREATE TABLE IF NOT EXISTS transcription_logs (
  id BIGSERIAL PRIMARY KEY,
  file_type VARCHAR NOT NULL,
  duration INTEGER NOT NULL,
  chat_id BIGINT NOT NULL,
  message_id BIGINT NOT NULL,
  username VARCHAR,
  transcript TEXT,
  language_code VARCHAR,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  error TEXT
);

ALTER TABLE transcription_logs ENABLE ROW LEVEL SECURITY;
```

### 4. Create a Supabase Edge Function

Create a new Edge Function to handle Telegram webhook requests:

```bash
supabase functions new scribe-bot
```

### 5. Set Up Environment Variables

Create a `.env` file in the `supabase/functions` directory:

```
# ElevenLabs API key
ELEVENLABS_API_KEY=your_api_key

# Telegram bot token from BotFather
TELEGRAM_BOT_TOKEN=your_bot_token

# A random secret to secure the function
FUNCTION_SECRET=random_secret
```

## Implementation

Add the following code to your `scribe-bot/index.ts` file:

```typescript
import { Bot, webhookCallback } from 'https://deno.land/x/grammy@v1.34.0/mod.ts'
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { createClient } from 'jsr:@supabase/supabase-js@2'
import { ElevenLabsClient } from 'npm:elevenlabs@1.50.5'

console.log(`Function "elevenlabs-scribe-bot" up and running!`)

const elevenLabsClient = new ElevenLabsClient({
  apiKey: Deno.env.get('ELEVENLABS_API_KEY') || '',
})

const supabase = createClient(
  Deno.env.get('SUPABASE_URL') || '',
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') || ''
)

async function scribe({
  fileURL,
  fileType,
  duration,
  chatId,
  messageId,
  username,
}: {
  fileURL: string
  fileType: string
  duration: number
  chatId: number
  messageId: number
  username: string
}) {
  let transcript: string | null = null
  let languageCode: string | null = null
  let errorMsg: string | null = null

  try {
    const sourceFileArrayBuffer = await fetch(fileURL).then((res) => res.arrayBuffer())
    const sourceBlob = new Blob([sourceFileArrayBuffer], {
      type: fileType,
    })

    const scribeResult = await elevenLabsClient.speechToText.convert({
      file: sourceBlob,
      model_id: 'scribe_v1',
      tag_audio_events: false,
    })

    transcript = scribeResult.text
    languageCode = scribeResult.language_code

    // Reply to the user with the transcript
    await bot.api.sendMessage(chatId, transcript, {
      reply_parameters: { message_id: messageId },
    })
  } catch (error) {
    errorMsg = error.message
    console.log(errorMsg)
    await bot.api.sendMessage(chatId, 'Sorry, there was an error. Please try again.', {
      reply_parameters: { message_id: messageId },
    })
  }

  // Write log to Supabase.
  const logLine = {
    file_type: fileType,
    duration,
    chat_id: chatId,
    message_id: messageId,
    username,
    language_code: languageCode,
    error: errorMsg,
  }

  console.log({ logLine })
  await supabase.from('transcription_logs').insert({ ...logLine, transcript })
}

const telegramBotToken = Deno.env.get('TELEGRAM_BOT_TOKEN')
const bot = new Bot(telegramBotToken || '')

const startMessage = `Welcome to the ElevenLabs Scribe Bot\\! I can transcribe speech in 99 languages with super high accuracy\\!    
\nTry it out by sending or forwarding me a voice message, video, or audio file\\!    
\n[Learn more about Scribe](https://elevenlabs.io/speech-to-text) or [build your own bot](https://elevenlabs.io/docs/cookbooks/speech-to-text/telegram-bot)\\!  `

bot.command('start', (ctx) => ctx.reply(startMessage.trim(), { parse_mode: 'MarkdownV2' }))

bot.on([':voice', ':audio', ':video'], async (ctx) => {
  try {
    const file = await ctx.getFile()
    const fileURL = `https://api.telegram.org/file/bot${telegramBotToken}/${file.file_path}`
    const fileMeta = ctx.message?.video ?? ctx.message?.voice ?? ctx.message?.audio

    if (!fileMeta) {
      return ctx.reply('No video|audio|voice metadata found. Please try again.')
    }

    // Run the transcription in the background.
    EdgeRuntime.waitUntil(
      scribe({
        fileURL,
        fileType: fileMeta.mime_type!,
        duration: fileMeta.duration,
        chatId: ctx.chat.id,
        messageId: ctx.message?.message_id!,
        username: ctx.from?.username || '',
      })
    )

    // Reply to the user immediately to let them know we received their file.
    return ctx.reply('Received. Scribing...')
  } catch (error) {
    console.error(error)
    return ctx.reply(
      'Sorry, there was an error getting the file. Please try again with a smaller file!'
    )
  }
})

const handleUpdate = webhookCallback(bot, 'std/http')

Deno.serve(async (req) => {
  try {
    const url = new URL(req.url)
    if (url.searchParams.get('secret') !== Deno.env.get('FUNCTION_SECRET')) {
      return new Response('not allowed', { status: 405 })
    }
    return await handleUpdate(req)
  } catch (err) {
    console.error(err)
  }
})
```

## Deployment

### 1. Link Your Project

Link your local project to your Supabase account:

```bash
supabase link
```

### 2. Apply Database Migrations

Apply the database migrations to create the required table:

```bash
supabase db push
```

Check your Supabase dashboard to verify that the `transcription_logs` table was created.

### 3. Deploy the Edge Function

Deploy the function with:

```bash
supabase functions deploy --no-verify-jwt scribe-bot
```

Note the function URL from your Supabase dashboard (it should look like `https://<project-ref>.functions.supabase.co/scribe-bot`).

### 4. Set Up the Webhook

Configure your Telegram bot to use your Edge Function as a webhook by visiting:

```
https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook?url=https://<PROJECT_REFERENCE>.supabase.co/functions/v1/scribe-bot?secret=<FUNCTION_SECRET>
```

Replace the placeholders with your actual values.

### 5. Set Function Secrets

Set your environment variables in your Supabase project:

```bash
supabase secrets set --env-file supabase/functions/.env
```

## Testing the Bot

1. Open Telegram and search for your bot by username
2. Start a conversation with your bot
3. Send a voice message, audio file, or video with speech
4. The bot should respond with a transcription of the speech
5. Check your Supabase database to verify that a new log entry was created

## How It Works

1. User sends an audio/video message to the bot on Telegram
2. Telegram forwards the message to your webhook URL (Edge Function)
3. Edge Function validates the request and extracts the file URL
4. The file is downloaded and sent to ElevenLabs Scribe API for transcription
5. The transcription is sent back to the user as a reply
6. All activity is logged in the Supabase database
7. Background tasks are used to ensure fast response times

The bot automatically detects the language being spoken and provides transcriptions in 99 languages, making it a powerful multilingual speech-to-text tool.