from flask import Blueprint, flash, redirect, render_template, session, url_for

from app.forms import NoteForm
from app.models import Note, db

notes_bp = Blueprint("notes", __name__)


@notes_bp.route("/create_note", methods=["POST", "GET"])
def create_note():
    if "user_id" not in session:
        return redirect(url_for("users.login"))

    form = NoteForm()
    if form.validate_on_submit():
        note = Note(
            title=form.title.data, content=form.content.data, user_id=session["user_id"]
        )
        db.session.add(note)
        db.session.commit()
        flash("Note created successfully!", "success")
        return redirect(url_for("home"))

    return render_template("note_form.html", form=form)


@notes_bp.route("/edit_note/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    if "user_id" not in session:
        return redirect(url_for("users.login"))

    note = Note.query.get_or_404(note_id)
    form = NoteForm(obj=note)

    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        db.session.commit()
        flash("Note updated successfully!", "success")
        return redirect(url_for("home"))

    return render_template("edit_note.html", form=form, note=note)


@notes_bp.route("/delete_note/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    if "user_id" not in session:
        return redirect(url_for("users.login"))
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash("Note deleted successfully!", "success")
    return redirect(url_for("home"))
