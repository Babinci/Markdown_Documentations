# Face Similarity Search with Supabase Vecs

This guide demonstrates how to build a face similarity search system that can identify celebrities who look most similar to any given face using Supabase Vecs and the pgvector extension.

## Overview

You'll learn how to:
1. Set up a Postgres database with pgvector for storing face embeddings
2. Run a Jupyter notebook that connects to your database
3. Load the "ashraq/tmdb-people-image" celebrity dataset
4. Generate face embeddings using the `face_recognition` model
5. Perform similarity searches to find matching faces

## Project Setup

First, create a Supabase database to store your face embeddings:

1. [Create a new project](https://database.new/) in the Supabase dashboard
2. Enter your project details and save your password securely
3. Wait for your database to be provisioned (usually takes less than a minute)

### Finding Your Credentials

You'll need these details to connect to your database:
- **Database credentials**: Find connection strings in [Database Settings](https://supabase.com/dashboard/project/_/settings/database)
- **API credentials**: Your API URL and keys in [API Settings](https://supabase.com/dashboard/project/_/settings/api)

## Launching the Notebook

The face similarity example is available as a Jupyter notebook:

[![Open In Colab](https://supabase.com/docs/img/ai/colab-badge.svg)](https://colab.research.google.com/github/supabase/supabase/blob/master/examples/ai/face_similarity.ipynb)

1. Click the "Open in Colab" button above
2. Click "Copy to Drive" at the top of the notebook to save it to your Google Drive
3. Run the notebook in Google Colab

## Connecting to Your Database

In the notebook, locate the cell that defines the database connection:

```python
import vecs
DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"
# create vector store client
vx = vecs.create_client(DB_CONNECTION)
```

Replace the `DB_CONNECTION` string with your Supabase database connection string with these modifications:

1. Use the **connection pooling** string (ending with `*.pooler.supabase.com`) since Colab doesn't support IPv6
2. Change the protocol from `postgres://` to `postgresql://` as required by SQLAlchemy

You can find your connection string in the [Database Settings](https://supabase.com/dashboard/project/_/settings/database) page of your Supabase project.

## Notebook Walkthrough

Follow these steps in the notebook:

1. **Install Dependencies**: The notebook installs necessary packages like `face_recognition`, `vecs`, and `Pillow`

2. **Load Celebrity Dataset**: The notebook loads a dataset of celebrity face images

3. **Generate Face Embeddings**: For each image:
   - Detect faces using the `face_recognition` library
   - Generate an embedding (feature vector) for each detected face
   - Store the embedding in your Supabase vector database

4. **Create a Search Collection**: The notebook creates a named collection in your database to store and query the face embeddings

5. **Perform Similarity Searches**: Upload your own image or use a test image to:
   - Generate an embedding for the query face
   - Find the most similar celebrity faces in the database
   - Display the matching faces with similarity scores

## Viewing Results in Supabase

You can view the stored embeddings in the Supabase dashboard:

1. Go to the [Table Editor](https://supabase.com/dashboard/project/_/editor/)
2. Select the `vecs` schema from the schema dropdown
3. Explore the collections and vectors tables

![Supabase Table Editor](https://supabase.com/docs/img/ai/google-colab/colab-documents.png)

## Next Steps

Now that you understand how to implement face similarity search with Supabase Vecs, you can:

1. **Build a web application**: Create a user interface for face matching
2. **Enhance the model**: Add more features like age detection or emotion recognition
3. **Scale your database**: Optimize for larger datasets with indexing strategies
4. **Implement privacy features**: Add consent mechanisms and data protection measures

For more AI application examples using Supabase, check out the [examples section](https://supabase.com/docs/guides/ai#examples) in the documentation.
