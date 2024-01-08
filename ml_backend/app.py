from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<p>Welcome to EZ AI!</p>"