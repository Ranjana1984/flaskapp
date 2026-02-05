from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps with Flask! welcome to webapp
    This is very diffcult task and easy also"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
