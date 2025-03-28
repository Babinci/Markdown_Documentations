# AI & Vectors

## The best vector database is the database you already have

Supabase provides an open source toolkit for developing AI applications using Postgres and pgvector. Use the Supabase client libraries to store, index, and query your vector embeddings at scale.

The toolkit includes:

- A [vector store](https://supabase.com/docs/guides/ai/vector-columns) and embeddings support using Postgres and pgvector.
- A [Python client](https://supabase.com/docs/guides/ai/vecs-python-client) for managing unstructured embeddings.
- An [embedding generation](https://supabase.com/docs/guides/ai/quickstarts/generate-text-embeddings) process using open source models directly in Edge Functions.
- [Database migrations](https://supabase.com/docs/guides/ai/examples/headless-vector-search#prepare-your-database) for managing structured embeddings.
- Integrations with all popular AI providers, such as [OpenAI](https://supabase.com/docs/guides/ai/examples/openai), [Hugging Face](https://supabase.com/docs/guides/ai/hugging-face), [LangChain](https://supabase.com/docs/guides/ai/langchain), and more.

## Search

You can use Supabase to build different types of search features for your app, including:

- [Semantic search](https://supabase.com/docs/guides/ai/semantic-search): search by meaning rather than exact keywords
- [Keyword search](https://supabase.com/docs/guides/ai/keyword-search): search by words or phrases
- [Hybrid search](https://supabase.com/docs/guides/ai/hybrid-search): combine semantic search with keyword search

## Examples

Check out all of the AI [templates and examples](https://github.com/supabase/supabase/tree/master/examples/ai) in our GitHub repository.

- [Headless Vector Search](https://supabase.com/docs/guides/ai/examples/headless-vector-search) - A toolkit to perform vector similarity search on your knowledge base embeddings.
- [Image Search with OpenAI CLIP](https://supabase.com/docs/guides/ai/examples/image-search-openai-clip) - Implement image search with the OpenAI CLIP Model and Supabase Vector.
- [Hugging Face inference](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning) - Generate image captions using Hugging Face.
- [OpenAI completions](https://supabase.com/docs/guides/ai/examples/openai) - Generate GPT text completions using OpenAI in Edge Functions.
- [Building ChatGPT Plugins](https://supabase.com/docs/guides/ai/examples/building-chatgpt-plugins) - Use Supabase as a Retrieval Store for your ChatGPT plugin.
- [Vector search with Next.js and OpenAI](https://supabase.com/docs/guides/ai/examples/nextjs-vector-search) - Learn how to build a ChatGPT-style doc search powered by Next.js, OpenAI, and Supabase.

## Integrations

- [OpenAI](https://supabase.com/docs/guides/ai/examples/building-chatgpt-plugins) - OpenAI is an AI research and deployment company. Supabase provides a simple way to use OpenAI in your applications.
- [Amazon Bedrock](https://supabase.com/docs/guides/ai/integrations/amazon-bedrock) - A fully managed service that offers a choice of high-performing foundation models from leading AI companies.
- [Hugging Face](https://supabase.com/docs/guides/ai/hugging-face) - Hugging Face is an open-source provider of NLP technologies. Supabase provides a simple way to use Hugging Face's models in your applications.
- [LangChain](https://supabase.com/docs/guides/ai/langchain) - LangChain is a language-agnostic, open-source, and self-hosted API for text translation, summarization, and sentiment analysis.
- [LlamaIndex](https://supabase.com/docs/guides/ai/integrations/llamaindex) - LlamaIndex is a data framework for your LLM applications.

## Case studies

- [Berri AI Boosts Productivity by Migrating from AWS RDS to Supabase with pgvector](https://supabase.com/customers/berriai) - Learn how Berri AI overcame challenges with self-hosting their vector database on AWS RDS and successfully migrated to Supabase.
- [Mendable switches from Pinecone to Supabase for PostgreSQL vector embeddings](https://supabase.com/customers/mendableai) - How Mendable boosts efficiency and accuracy of chat powered search for documentation using Supabase with pgvector.
- [Markprompt: GDPR-Compliant AI Chatbots for Docs and Websites](https://supabase.com/customers/markprompt) - AI-powered chatbot platform, Markprompt, empowers developers to deliver efficient and GDPR-compliant prompt experiences on top of their content, by leveraging Supabase's secure and privacy-focused database and authentication solutions.
