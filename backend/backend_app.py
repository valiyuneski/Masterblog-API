from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post about Flask."},
    {"id": 2, "title": "Second post", "content": "This is the second post about APIs."},
    {"id": 3, "title": "Flask Tips", "content": "Some useful tips for working with Flask."}
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """ GET all posts with optional sorting """
    sort_field = request.args.get("sort")
    direction = request.args.get("direction", "asc").lower()

    # Validate sort field if provided
    if sort_field and sort_field not in ["title", "content"]:
        return jsonify({"error": f"Invalid sort field '{sort_field}'. Must be 'title' or 'content'."}), 400

    # Validate direction if provided
    if direction not in ["asc", "desc"]:
        return jsonify({"error": f"Invalid direction '{direction}'. Must be 'asc' or 'desc'."}), 400

    # Apply sorting if sort_field is provided
    if sort_field:
        reverse = direction == "desc"
        sorted_posts = sorted(POSTS, key=lambda p: p[sort_field].lower(), reverse=reverse)
        return jsonify(sorted_posts), 200

    # Default: return original order
    return jsonify(POSTS), 200



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


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """DELETE a post by ID"""
    global POSTS
    post_to_delete = next((post for post in POSTS if post["id"] == post_id), None)

    if not post_to_delete:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    POSTS = [post for post in POSTS if post["id"] != post_id]

    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """ PUT (update) a post by ID """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    post_to_update = next((post for post in POSTS if post["id"] == post_id), None)

    if not post_to_update:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    # Update only provided fields, keep old values if missing
    if "title" in data and data["title"]:
        post_to_update["title"] = data["title"]
    if "content" in data and data["content"]:
        post_to_update["content"] = data["content"]

    return jsonify(post_to_update), 200


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    """ SEARCH posts by title or content """
    title_query = request.args.get("title", "").lower()
    content_query = request.args.get("content", "").lower()

    results = [
        post for post in POSTS
        if (title_query in post["title"].lower() if title_query else True)
        and (content_query in post["content"].lower() if content_query else True)
    ]

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
