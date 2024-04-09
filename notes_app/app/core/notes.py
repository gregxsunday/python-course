from flask import Blueprint, request, render_template, flash
from app.database.models import Note
from flask_login import login_required, current_user
from app.extensions import db

mod = Blueprint('notes', __name__)


@mod.route('/notes/<note_id>', methods=['GET'])
@login_required
def get_note(note_id):
    note = Note.query.filter_by(id=note_id).first_or_404()
    # FIX: if note.user == current_user
    return (render_template('notes/get_note.html', nav='notes', note=note))


@mod.route('/notes/<note_id>', methods=['POST'])
@login_required
def modify_note(note_id):
    content = request.form.get('content')
    note = Note.query.filter_by(id=note_id).first_or_404()

    if not content:
        flash('Niewłaściwe żądanie')
        notes = Note.query.filter_by(user=current_user)
        return render_template('notes/list_notes.html', nav='notes', notes=notes), 403

    if note.user != current_user:
        flash('Brak dostępu do notatki')
        notes = Note.query.filter_by(user=current_user)
        return render_template('notes/list_notes.html', nav='notes', notes=notes), 403

    note.content = content
    db.session.commit()

    notes = Note.query.filter_by(user=current_user)
    return (render_template('notes/list_notes.html', nav='notes', notes=notes))


@mod.route('/notes/', methods=['GET'])
@login_required
def list_notes():
    notes = Note.query.filter_by(user=current_user)
    return (render_template('notes/list_notes.html', nav='notes', notes=notes))


@mod.route('/notes/', methods=['POST'])
@login_required
def create_note():
    name = request.form.get('name')
    content = request.form.get('content')

    if not name or not content:
        flash('Niewłaściwe żądanie')
        notes = Note.query.filter_by(user=current_user)
        return render_template('notes/list_notes.html', nav='notes', notes=notes), 404

    note = Note(name=name, content=content, user=current_user)

    db.session.add(note)
    db.session.commit()

    notes = Note.query.filter_by(user=current_user)
    return (render_template('notes/list_notes.html', nav='notes', notes=notes))
