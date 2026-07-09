import os

from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy

DB_FILE = os.path.join(os.path.dirname(__file__), "database.db")
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Note {self.id}: {self.content}>"


@app.route("/")
def home():
    role = "user"
    notes = Note.query.all()
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
        note = Note(content=note_content)
        db.session.add(note)
        db.session.commit()

        return redirect(url_for("confirmation", note=note_content))
    return render_template("note_form.html")
