from flask import request, jsonify
from api import app

import api.models.note
import api.views.note
import api.models.user
import api.views.user






@app.route("/alive", methods=["GET", ])
def alive():
    if request.method == "GET":
        return jsonify({"status": "OK"})


if __name__ == '__main__':
    app.run(debug=True)
