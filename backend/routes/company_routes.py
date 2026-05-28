from flask import Blueprint, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt
)

company_bp = Blueprint(
    "company",
    __name__,
    url_prefix="/company"
)


@company_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def company_dashboard():

    claims = get_jwt()

    if claims["role"] != "company":
        return jsonify({
            "message": "Access denied"
        }), 403

    return jsonify({
        "message": "Welcome Company",
        "role": claims["role"]
    }), 200