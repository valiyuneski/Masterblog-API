from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Get all POSTS jsonified"""
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    """Add POST, expects JSON with title and content"""
    data = request.get_json()

    # Validate input
    if not data:
        return jsonify({"error": "Request must be JSON"}), 400
    
    missing_fields = []
    if "title" not in data or not data["title"]:
        missing_fields.append("title")
    if "content" not in data or not data["content"]:
        missing_fields.append("content")
    
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Generate new ID
    new_id = max([post["id"] for post in POSTS], default=0) + 1

    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"]
    }

    POSTS.append(new_post)

    return jsonify(new_post), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
