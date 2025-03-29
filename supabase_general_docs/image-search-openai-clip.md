# Image Search with OpenAI CLIP and Supabase Vector

This guide demonstrates how to implement powerful image search capabilities using the OpenAI CLIP (Contrastive Language-Image Pre-Training) model and Supabase Vector.

## What is CLIP?

The [OpenAI CLIP Model](https://github.com/openai/CLIP) was trained on a diverse dataset of (image, text) pairs. This versatile model can be used for multiple types of cross-modal search operations:

- Text-to-Image search
- Image-to-Text search
- Image-to-Image search
- Text-to-Text search

The model can also be fine-tuned on your own image and text data using the standard `SentenceTransformers` training code.

## Project Setup

This tutorial walks through creating a Python application that enables semantic image search using text queries. The complete application code is available on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/image_search#image-search-with-supabase-vector).

### Prerequisites

- Python 3.7 or newer
- [Poetry](https://python-poetry.org/) for dependency management
- [Supabase CLI](https://supabase.com/docs/guides/cli) for local development
- Some images to index and search

### Step 1: Create a New Python Project

Install Poetry if you haven't already:

```bash
pip install poetry
```

Initialize a new project:

```bash
poetry new image-search
```

### Step 2: Set Up a Local Supabase Instance

Initialize Supabase in your project:

```bash
supabase init
```

Start your local Supabase stack:

```bash
supabase start
```

Make note of the DB URL that is displayed after the stack starts. You'll need this for connecting to your database.

### Step 3: Install Dependencies

Add the necessary libraries to your project:

```bash
poetry add vecs sentence-transformers matplotlib
```

These packages provide:
- `vecs`: Supabase Vector Python client for vector storage and retrieval
- `sentence-transformers`: Framework for generating text and image embeddings
- `matplotlib`: Library for displaying image results

### Step 4: Create the Application

Create a Python file called `main.py` in your project directory with the following imports:

```python
from PIL import Image
from sentence_transformers import SentenceTransformer
import vecs
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

DB_CONNECTION = "postgresql://postgres:postgres@localhost:54322/postgres"
```

### Step 5: Create Image Embeddings

Create a `seed` function to generate embeddings for your images and store them in Supabase Vector:

```python
def seed():
    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)
    
    # create a collection of vectors with 512 dimensions
    images = vx.get_or_create_collection(name="image_vectors", dimension=512)
    
    # Load CLIP model
    model = SentenceTransformer('clip-ViT-B-32')
    
    # Encode images:
    img_emb1 = model.encode(Image.open('./images/one.jpg'))
    img_emb2 = model.encode(Image.open('./images/two.jpg'))
    img_emb3 = model.encode(Image.open('./images/three.jpg'))
    img_emb4 = model.encode(Image.open('./images/four.jpg'))
    
    # add records to the *images* collection
    images.upsert(
        records=[
            (
                "one.jpg",        # the vector's identifier
                img_emb1,         # the vector (list or np.array)
                {"type": "jpg"}   # associated metadata
            ), (
                "two.jpg",
                img_emb2,
                {"type": "jpg"}
            ), (
                "three.jpg",
                img_emb3,
                {"type": "jpg"}
            ), (
                "four.jpg",
                img_emb4,
                {"type": "jpg"}
            )
        ]
    )
    
    print("Inserted images")
    
    # index the collection for fast search performance
    images.create_index()
    print("Created index")
```

### Step 6: Implement Text-to-Image Search

Create a `search` function that finds the most relevant image for a text query:

```python
def search():
    # create vector store client
    vx = vecs.create_client(DB_CONNECTION)
    images = vx.get_or_create_collection(name="image_vectors", dimension=512)
    
    # Load CLIP model
    model = SentenceTransformer('clip-ViT-B-32')
    
    # Encode text query
    query_string = "a bike in front of a red brick wall"
    text_emb = model.encode(query_string)
    
    # query the collection filtering metadata for "type" = "jpg"
    results = images.query(
        data=text_emb,                      # required
        limit=1,                            # number of records to return
        filters={"type": {"$eq": "jpg"}},   # metadata filters
    )
    
    result = results[0]
    print(result)
    
    plt.title(result)
    image = mpimg.imread('./images/' + result)
    plt.imshow(image)
    plt.show()
```

### Step 7: Configure Poetry Scripts

Add these functions as scripts in your `pyproject.toml` file:

```toml
[tool.poetry.scripts]
seed = "image_search.main:seed"
search = "image_search.main:search"
```

### Step 8: Run the Application

1. Create an `images` directory in your project and add some JPG images
2. Run the seeding script to create embeddings:
   ```bash
   poetry run seed
   ```
3. Execute a text-to-image search:
   ```bash
   poetry run search
   ```

The application will display the image that best matches your text query.

## Advanced Usage

### Customizing the Search

- Modify the `query_string` variable to search for different concepts
- Increase the `limit` parameter in the query to return more matching images
- Create a more interactive application with user input for the query string

### Implementing Image-to-Image Search

You can also use CLIP for reverse image search by encoding an image as the query:

```python
# Replace text_emb with an image embedding
query_image = Image.open('./images/query.jpg')
query_emb = model.encode(query_image)

# The rest of the query remains the same
results = images.query(
    data=query_emb,
    limit=5,
    filters={"type": {"$eq": "jpg"}},
)
```

## Conclusion

This implementation demonstrates how to combine OpenAI's CLIP model with Supabase Vector to create a powerful semantic image search system. With this foundation, you can expand to larger image collections and more sophisticated search interfaces.

The same approach can be adapted for other multi-modal applications like product search, content recommendation, or visual question answering.
