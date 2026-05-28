from flask import Blueprint, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt
)

student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/student"
)


@student_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def student_dashboard():

    claims = get_jwt()

    if claims["role"] != "student":
        return jsonify({
            "message": "Access denied"
        }), 403

    return jsonify({
        "message": "Welcome Student",
        "role": claims["role"]
    }), 200