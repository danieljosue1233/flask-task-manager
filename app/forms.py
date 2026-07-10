from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    email = EmailField(
        "Correo",
        validators=[
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingresa un correo valido"),
        ],
    )
    password = PasswordField(
        "Contrasena",
        validators=[DataRequired(message="La contrasena es obligatoria")],
    )
    submit = SubmitField("Iniciar Sesion")


class RegisterForm(FlaskForm):
    name = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(
                min=2, max=100, message="El nombre debe tener entre 2 y 100 caracteres"
            ),
        ],
    )
    email = EmailField(
        "Correo",
        validators=[
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingresa un correo valido"),
        ],
    )
    password = PasswordField(
        "Contrasena",
        validators=[
            DataRequired(message="La contrasena es obligatoria"),
            Length(min=6, message="La contrasena debe tener al menos 6 caracteres"),
        ],
    )
    submit = SubmitField("Registrarse")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("El correo ya esta registrado")


class NoteForm(FlaskForm):
    title = StringField(
        "Titulo",
        validators=[
            DataRequired(message="El titulo es obligatorio"),
            Length(
                min=1, max=100, message="El titulo debe tener entre 1 y 100 caracteres"
            ),
        ],
    )
    content = TextAreaField(
        "Contenido",
        validators=[
            DataRequired(message="El contenido es obligatorio"),
            Length(
                min=1,
                max=200,
                message="El contenido debe tener entre 1 y 200 caracteres",
            ),
        ],
    )
    submit = SubmitField("Guardar")
