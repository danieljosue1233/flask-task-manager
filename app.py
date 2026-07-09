from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
)

from models import Note, db

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)


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


@app.route("/create_note", methods=["POST", "GET"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        note = Note(title=title, content=content)
        db.session.add(note)
        db.session.commit()

        return redirect(
            url_for(
                "home",
            )
        )
    return render_template("note_form.html")


@app.route("/edit_note/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.title = request.form.get("title", note.title)
        note.content = request.form.get("content", note.content)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_note.html", note=note)


# añade una alerta que confirme que si quiero eliminar la nota


@app.route("/delete_note/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("home"))
