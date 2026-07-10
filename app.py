from flask import (
    Flask,
    render_template,
    request,
    session,
)

from models import Note, User, db
from notes.routes import notes_bp
from users.routes import users_bp

app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)
app.register_blueprint(notes_bp)
app.register_blueprint(users_bp)


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
    user = None
    notes = []
    if "user_id" in session:
        user = User.query.get(session["user_id"])
        notes = Note.query.filter_by(user_id=session["user_id"]).all()
    return render_template("home.html", notes=notes, user=user)
