# Masterblog-API

Prerequisites:
python3 -m venv .venv
pip install flask
pip install flask_cors
pip install --upgrade pip

Run backend:
python3 backend/backend_app.py

POST: "http://localhost:5002/api/posts"
{
    "content": "This is the third post.",
    "id": 3,
    "title": "Third post"
}

DELETE: "http://localhost:5002/api/posts/3"

UPDATE PUT: "http://localhost:5002/api/posts/3"
{
    "title": "<new title>",
    "content": "<new content>"
}

SEARCH GET request to http://localhost:5002/api/posts/search
How it works
•	GET /api/posts/search?title=flask → returns posts where title contains “flask”.
•	GET /api/posts/search?content=api → returns posts where content contains “api”.
•	GET /api/posts/search?title=flask&content=tips → returns posts matching both conditions.
•	If no matches → returns [] (empty list).