from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return "<h1>Happy holidays from Flask & Konflux!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
