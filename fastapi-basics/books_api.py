from fastapi import FastAPI

books = [
    {"title": "Python Basics", "author": "John Doe", "publisher": "TechPress"},
    {"title": "FastAPI Guide", "author": "Jane Smith", "publisher": "WebPub"},
    {"title": "AI Future", "author": "Alan Turing", "publisher": "SciencePub"},
    {"title": "Deep Learning", "author": "Ian Goodfellow", "publisher": "MIT Press"},
]

app = FastAPI()

@app.get("/search")
def search_books(q: str = ""):
    if not q:
        return books

    return [
        book for book in books
        if q.lower() in book["title"].lower()
        or q.lower() in book["author"].lower()
        or q.lower() in book["publisher"].lower()
    ]