from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import uvicorn

app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    context = {
        'data': f"{limit} blog posts",
    }
    if published:
        return context
    else:
        return "No published posts."


@app.get('/blog/unpublished')
def unpublished():
    context = {
        "data": "All unpublished blogs."
    }

    return context


@app.get('/blog/{id}')
def show(id: int):
    context = {
        'id': id
    }
    return context


@app.get('/blog/{id}/comments')
def comments(id: int, limit=100):
    context = {
        "comments": {
            "Lorem ipsum dolor.",
            "Sit amet proin gravida.",
        }
    }

    return context


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    context = {
        "title": request.title,
        "body": request.body,
        "published": True
    }

    return context


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)