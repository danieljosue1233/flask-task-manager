from dotenv import load_dotenv
from flask import Flask, render_template, request, session
from flask_migrate import Migrate

from app.models import Note, User, db
from app.notes.routes import notes_bp
from app.users.routes import users_bp

from .config import Config

load_dotenv()

migrate = Migrate()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(notes_bp)
    app.register_blueprint(users_bp)

    with app.app_context():
        db.create_all()

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

    return app
