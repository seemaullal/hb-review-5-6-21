from flask import Flask, render_template, redirect, flash, session, request, jsonify
import jinja2
import requests
import json

app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = "this-should-be-something-unguessable"

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = True


@app.route("/")
def index():
    """Return homepage."""
    return render_template("homepage.html")

@app.route("/api/todos")
def todos():
    """Return homepage."""
    file_json = open("todos.json").read()
    return jsonify(json.loads(file_json))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
