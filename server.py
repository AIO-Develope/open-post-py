# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)
posts = []

@app.route('/post', methods=['POST'])
def create_post():
    data = request.get_json()
    username = data.get('username')
    text = data.get('text')
    
    post = {'username': username, 'text': text}
    posts.append(post)
    
    return jsonify({'message': 'Post created successfully'})

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
