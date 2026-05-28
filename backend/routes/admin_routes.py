from flask import Blueprint, jsonify
from models.student import Student
from models.job import JobPosition
from models.application import Application
from models.user import User
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
    
# DASHBOARD STATS
@admin_bp.route("/stats", methods=["GET"])
@jwt_required()
def dashboard_stats():

    claims = get_jwt()

    if claims["role"] != "admin":

        return jsonify({
            "message": "Access denied"
        }), 403

    total_students = Student.query.count()

    total_companies = Company.query.count()

    total_jobs = JobPosition.query.count()

    total_applications = Application.query.count()

    return jsonify({

        "students": total_students,

        "companies": total_companies,

        "jobs": total_jobs,

        "applications": total_applications

    }), 200
    
# GET ALL COMPANIES
@admin_bp.route("/companies", methods=["GET"])
@jwt_required()
def get_companies():

    claims = get_jwt()

    if claims["role"] != "admin":

        return jsonify({
            "message": "Access denied"
        }), 403

    companies = Company.query.all()

    company_list = []

    for company in companies:

        company_list.append({

            "id": company.id,

            "company_name": company.company_name,

            "approved": company.approved

        })

    return jsonify(company_list), 200


# DELETE COMPANY
@admin_bp.route("/delete-company/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_company(id):

    claims = get_jwt()

    if claims["role"] != "admin":

        return jsonify({
            "message": "Access denied"
        }), 403

    company = Company.query.get(id)

    if not company:

        return jsonify({
            "message": "Company not found"
        }), 404

    db.session.delete(company)

    db.session.commit()

    return jsonify({
        "message": "Company deleted"
    }), 200
    
# GET ALL STUDENTS
@admin_bp.route("/students", methods=["GET"])
@jwt_required()
def get_students():

    claims = get_jwt()

    if claims["role"] != "admin":

        return jsonify({
            "message": "Access denied"
        }), 403

    students = Student.query.all()

    student_list = []

    for student in students:

        student_list.append({

            "id": student.id,

            "full_name": student.full_name

        })

    return jsonify(student_list), 200



