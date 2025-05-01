from app import create_app
from flask import render_template, jsonify, request
from flask_cors import CORS

app = create_app()
CORS(app)

# In-memory storage for posts
posts = [
    {"title": "First Post", "content": "This is my first blog post!"},
    {"title": "Second Post", "content": "Learning Flask is fun!"},
]

@app.route('/')
def home():
    return "Welcome to the Blog API!"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# GET API Route - to get all posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# POST API Route - to add a new post
@app.route('/api/add_post', methods=['POST'])
def add_post():
    data = request.get_json()

    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"error": "Title and Content are required."}), 400

    # Add the new post to the posts list
    new_post = {
        "title": title,
        "content": content
    }
    posts.append(new_post)

    return jsonify({"message": "Post added successfully", "post": new_post}), 201

# PATCH API Route - to update an existing post
@app.route('/api/update_post/<int:post_index>', methods=['PATCH'])
def update_post(post_index):
    if post_index < 0 or post_index >= len(posts):
        return jsonify({"error": "Post not found."}), 404

    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if title:
        posts[post_index]['title'] = title
    if content:
        posts[post_index]['content'] = content

    return jsonify({"message": "Post updated successfully", "post": posts[post_index]})

# DELETE API Route - to delete a post
@app.route('/api/delete_post/<int:post_index>', methods=['DELETE'])
def delete_post(post_index):
    if post_index < 0 or post_index >= len(posts):
        return jsonify({"error": "Post not found."}), 404

    deleted_post = posts.pop(post_index)
    return jsonify({"message": "Post deleted successfully", "deleted": deleted_post})

if __name__ == "__main__":
    app.run(debug=True)
