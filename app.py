from flask import (
    Flask,
    render_template,
    request,
)

from models import Note, db
from notes.routes import notes_bp

app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)
app.register_blueprint(notes_bp)


@app.route("/about")
def about():
    return "This is a simple Flask application."


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Thank you for contacting us!", 201
    return "Contact us at example@email.com"


@app.route("/")
def home():
    notes = Note.query.all()
    return render_template("home.html", notes=notes)
