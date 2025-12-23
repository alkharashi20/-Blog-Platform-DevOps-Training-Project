import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/blog")
def blog():
    auth = requests.post("http://auth:3000/login").json()
    posts = requests.get("http://post:5001/posts").json()

    return jsonify({
        "token": auth["token"],
        "posts": posts
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
