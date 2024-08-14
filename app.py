from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return "<h1>Hello from Flask & Dockerfile</h1><h2>Built and tested in Konflux</h2>"

if __name__ == "__main__":
    app.run(debug=True)
