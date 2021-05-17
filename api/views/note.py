from flask import request, jsonify
from api import app, auth, g
from api.models.note import Note
from api.models.user import User
from flask.views import MethodView


class NotesAllView(MethodView):

    def get(self):
        notes = Note.query.all()
        if not notes:
            return {f"Notes": "not found"}, 404
        return jsonify([note.to_dict() for note in notes]), 200


class NoteView(MethodView):

    def get(self, user_id):
        notes = Note.query.filter(Note.user_id == user_id).all()
        if not notes:
            return {f"error": f"Notes by user {user_id} not found"}, 404
        return jsonify([note.to_dict() for note in notes])

    @auth.login_required()
    def post(self, user_id):
        user = User.query.get(user_id)
        note = Note(user_id=user.id, **request.json)
        try:
            note.save()
            return jsonify(note.to_dict()), 201
        except:
            return jsonify({"error": "Param 'header' must be unique"}), 404


class NoteUserView(MethodView):

    def get(self, user_id, note_id):
        note = Note.query.filter(Note.user_id == user_id, Note.id == note_id).first()
        if not note:
            return {f"error": f"Notes with id {note_id} by user {user_id} not found"}, 404
        return jsonify(note.to_dict())

    @auth.login_required()
    def put(self, user_id, note_id):
        user = g.user
        note = Note.query.filter(Note.user_id == user_id, Note.id == note_id).first()
        if not note:
            return {f"error": f"Notes with id {note_id} by user {user_id} not found"}, 404
        if note.user != user:
            return {f"error": f"Access denied to note with id={note_id}"}, 403
        for key in request.json:
            setattr(note, key, request.json[key])
        try:
            note.save()
            return jsonify(note.to_dict()), 200
        except:
            return jsonify({"error": f"All note params must be unique"}), 404

    @auth.login_required()
    def delete(self, user_id, note_id):
        user = g.user
        note = Note.query.filter(Note.user_id == user_id, Note.id == note_id).first()
        if not note:
            return {f"error": f"Notes with id {note_id} by user {user_id} not found"}, 404
        if note.user != user:
            return {f"error": f"Access denied to note with id={note_id}"}, 403
        note.delete()
        return jsonify({f"Note with id {note_id}": "deleted"}), 200


app.add_url_rule('/notes', view_func=NotesAllView.as_view('notes_create'), methods=['GET', ])
app.add_url_rule('/users/<int:user_id>/notes', view_func=NoteView.as_view('note_operation'),
                 methods=["GET", "POST"])
app.add_url_rule('/users/<int:user_id>/notes/<int:note_id>', view_func=NoteUserView.as_view('note_operation1'),
                 methods=["GET", "PUT", "DELETE"])
