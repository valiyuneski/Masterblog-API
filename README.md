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
GET /api/posts/search?title=flask → returns posts where title contains “flask”.
	•	GET /api/posts/search?content=api → returns posts where content contains “api”.
	•	GET /api/posts/search?title=flask&content=tips → returns posts matching both conditions.
	•	If no matches → returns [] (empty list).

Postman Tests
	1.	GET http://localhost:5002/api/posts/search?title=flask
→ should return post(s) with “flask” in title.
	2.	GET http://localhost:5002/api/posts/search?content=api
→ should return post(s) with “api” in content.
	3.	GET http://localhost:5002/api/posts/search?title=hello
→ should return [].

GET list with sorting:
How it works:
	•	GET /api/posts → returns posts in original order.
	•	GET /api/posts?sort=title&direction=asc → sorts by title alphabetically.
	•	GET /api/posts?sort=content&direction=desc → sorts by content, descending.
	•	If sort is invalid → 400 Bad Request.
	•	If direction is invalid → 400 Bad Request.

 Postman Testing
	1.	GET http://localhost:5002/api/posts
→ returns posts in insertion order.
	2.	GET http://localhost:5002/api/posts?sort=title&direction=asc
→ posts sorted alphabetically by title.
	3.	GET http://localhost:5002/api/posts?sort=content&direction=desc
→ posts sorted by content, reverse order.
	4.	GET http://localhost:5002/api/posts?sort=author
→ 400 Bad Request with error message.
	5.	GET http://localhost:5002/api/posts?sort=title&direction=wrong
→ 400 Bad Request with error message.