from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/posts")
def posts():
    return jsonify([
        {"id": 1, "title": "First Post"},
        {"id": 2, "title": "Second Post"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
