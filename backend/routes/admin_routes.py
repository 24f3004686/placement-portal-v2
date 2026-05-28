from flask import Blueprint, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from extensions import db

from models.company import Company


admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


# ADMIN DASHBOARD
@admin_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():

    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({
            "message": "Access denied"
        }), 403

    return jsonify({
        "message": "Welcome Admin",
        "role": claims["role"]
    }), 200


# APPROVE COMPANY
@admin_bp.route("/approve-company/<int:company_id>", methods=["PUT"])
@jwt_required()
def approve_company(company_id):

    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({
            "message": "Access denied"
        }), 403

    company = Company.query.get(company_id)

    if not company:
        return jsonify({
            "message": "Company not found"
        }), 404

    company.approved = True

    db.session.commit()

    return jsonify({
        "message": "Company approved successfully"
    }), 200