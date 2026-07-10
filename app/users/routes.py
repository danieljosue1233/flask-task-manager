from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User, db

users_bp = Blueprint("users", __name__)


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template(
                "register.html", error="El correo ya esta registrado"
            )

        hashed_password = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        return redirect(url_for("home"))

    return render_template("register.html")


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("home"))

        return render_template("login.html", error="Correo o contrasena incorrectos")

    return render_template("login.html")


@users_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))
