from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    """Returns a "welcome" message."""
    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    """returns a "welcome home" message."""
    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    """returns a "welcome back" message."""
    return "welcome back"

if __name__ == "__main__":
    app.run(debug=True)