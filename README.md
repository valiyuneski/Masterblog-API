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