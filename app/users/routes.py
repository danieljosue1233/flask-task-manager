from flask import Blueprint, redirect, render_template, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from app.forms import LoginForm, RegisterForm
from app.models import User, db

users_bp = Blueprint("users", __name__)


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            name=form.name.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        return redirect(url_for("home"))

    return render_template("register.html", form=form)


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session["user_id"] = user.id
            return redirect(url_for("home"))

        return render_template(
            "login.html", form=form, error="Correo o contrasena incorrectos"
        )

    return render_template("login.html", form=form)


@users_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))
