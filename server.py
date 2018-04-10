import json
from flask import abort, Flask, request
# from flask_debugtoolbar import DebugToolbarExtension
import data

app = Flask(__name__)
# toolbar = DebugToolbarExtension(app)

@app.route("/")
def main():
    """Return greeting."""
    return "Hi, friend!"

@app.route("/users", methods=["GET"])
@app.route("/users/<int:user_id>")
def get_user(user_id=None):
    """Return list of users, or specific user."""
    if not user_id:
        user_id = request.args.get("user_id")
    
    if not user_id:
        return json.dumps(data.users)

    user_id = int(user_id)
    user = data.users.get(user_id)

    if not user:
        abort(404)

    return json.dumps(data.users[user_id])

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404</h1>\nI'm sorry, I couldn't find that for you.", 404

if __name__ == "__main__":
    # Refresh when files change.
    app.debug = True

    app.run()
