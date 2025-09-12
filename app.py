from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Home Page!"


if __name__ == "__main__":
    app.run(debug=True)


