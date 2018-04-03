from flask import Flask
import data

app = Flask(__name__)

@app.route("/")
def main():
    """Return greeting."""
    return "Hi, friend!"

@app.route("/users"):
def get_users():
    """Return list of users."""
    return data.users

if __name__ == "__main__":
    app.run()
