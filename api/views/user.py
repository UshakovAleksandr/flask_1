from flask import request, jsonify
from api import app
from flask.views import MethodView
from api.models.user import User
from validation.validator import validate
from validation.schemas.user_schema import USER_CREATE


class UserView(MethodView):

    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {f"error": f"User with id {user_id} not found"}, 404
        return jsonify(user.to_dict())

    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {f"error": f"Note with id {user_id} not found"}, 404
        for key in request.json:
            setattr(user, key, request.json[key])
        try:
            user.save()
            return jsonify(user.to_dict()), 200
        except:
            return jsonify({"error": "All user params must be unique"}), 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {f"error": f"Note with id {user_id} not found"}, 404
        user.delete()
        return jsonify({f"Note with id {user_id}": "deleted"}), 200


class UserAllView(MethodView):

    def get(self):
        users = User.query.all()
        if not users:
            return {f"error": "Users not found"}, 404
        return jsonify([user.to_dict() for user in users])

    @validate("json", USER_CREATE)
    def post(self):
        user = User(**request.json)
        user.set_password(request.json["password"])
        try:
            user.save()
            return jsonify(user.to_dict()), 201
        except:
            return jsonify({"error": "User params must be unique"})


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('user_operation'), methods=["GET", "PUT", "DELETE"])
app.add_url_rule('/users', view_func=UserAllView.as_view('user_create'), methods=['GET', "POST"])
