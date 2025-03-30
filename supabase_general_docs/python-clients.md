# Choosing a Python Client for AI & Vectors

As described in [Structured & Unstructured Embeddings](https://supabase.com/docs/guides/ai/structured-unstructured), AI workloads come in many forms.

## Supabase Vecs for Data Science

For data science or ephemeral workloads, the [Supabase Vecs](https://supabase.github.io/vecs/) client gets you started quickly. All you need is a connection string and vecs handles setting up your database to store and query vectors with associated metadata.

You can get your connection string from the [**Database Settings**](https://supabase.com/dashboard/project/_/settings/database) page in your dashboard:

1. Make sure to check **Use connection pooling**
2. Copy the URI
3. Change the URI scheme from `postgres` to `postgresql`. `vecs` uses SQLAlchemy under the hood, which only supports `postgresql` as a dialect.

Example usage:

```python
import vecs

# create vector store client
vx = vecs.create_client("postgresql://postgres:[YOUR-PASSWORD]@[HOST]:6543/postgres")

# create a collection with a cosine distance metric
docs = vx.create_collection(name="docs", dimension=3)

# upsert vectors and their metadata into a collection
docs.upsert(
    vectors=[
        (
            "vec1",           # the vector's identifier
            [0.1, 0.2, 0.3],  # the vector. list or numpy.ndarray
            {"year": 1973}    # associated metadata
        ),
        (
            "vec2",
            [0.7, 0.8, 0.9],
            {"year": 2012}
        )
    ]
)

# query for vectors
docs.query(
    query_vector=[0.1, 0.2, 0.3],  # required
    limit=5,                        # number of results to return
    filters={"year": 2012},         # metadata filters
    include_metadata=True,          # return vector metadata?
    include_value=True              # return vector values?
)
```

## ORMs for Production Applications

For production Python applications with version-controlled migrations, we recommend adding first-class vector support to your toolchain by [registering the vector type with your ORM](https://github.com/pgvector/pgvector-python). 

pgvector provides bindings for the most commonly used SQL drivers/libraries including:
- Django
- SQLAlchemy
- SQLModel
- psycopg
- asyncpg
- Peewee

Example with SQLAlchemy:

```python
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    embedding = Column(Vector(384))  # dimensions match your model output
    
engine = create_engine("postgresql://postgres:password@localhost:5432/postgres")
Base.metadata.create_all(engine)

# Insert document with embedding
with Session(engine) as session:
    document = Document(
        content="Sample text document",
        embedding=[0.1, 0.2, 0.3, ...]  # 384-dimensional vector
    )
    session.add(document)
    session.commit()
    
# Query by vector similarity
with Session(engine) as session:
    query_embedding = [0.1, 0.2, 0.3, ...]  # 384-dimensional vector
    results = session.query(Document).order_by(
        Document.embedding.cosine_distance(query_embedding)
    ).limit(5).all()
```

## Resources

- [Supabase Vecs Documentation](https://supabase.github.io/vecs/)
- [pgvector Python](https://github.com/pgvector/pgvector-python)
- [Structured & Unstructured Embeddings Guide](https://supabase.com/docs/guides/ai/structured-unstructured)
- [Vector Columns Documentation](https://supabase.com/docs/guides/database/extensions/pgvector)
