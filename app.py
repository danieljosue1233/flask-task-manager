from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    role = "user"
    notes = ["Nota 1", "Nota 2", "Nota 3"]
    return render_template("home.html", role=role, notes=notes)


@app.route("/about")
def about():
    return "This is a simple Flask application."


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Thank you for contacting us!", 201
    return "Contact us at example@email.com"


@app.route("/api/info")
def api_info():
    data = {
        "name": "Flask App",
        "version": "1.0",
    }
    return jsonify(data), 200
