from flask import (  # type: ignore[import]
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

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


@app.route("/confirmation")
def confirmation():
    return "Your action has been confirmed."


@app.route("/create_note", methods=["POST", "GET"])
def create_note():
    if request.method == "POST":
        note_content = request.form.get("note", "No encontrada")

        return redirect(url_for("confirmation", note=note_content))
    return render_template("note_form.html")
