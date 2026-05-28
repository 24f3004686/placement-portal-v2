from flask import Blueprint, request, jsonify

from extensions import db, bcrypt

from flask_jwt_extended import create_access_token

from models.user import User
from models.student import Student
from models.company import Company
from models.job import JobPosition


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


# STUDENT REGISTER
@auth_bp.route("/student/register", methods=["POST"])
def student_register():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    full_name = data.get("full_name")

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return jsonify({
            "message": "User already exists"
        }), 400

    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    user = User(
        email=email,
        password=hashed_password,
        role="student"
    )

    db.session.add(user)
    db.session.commit()

    student = Student(
        user_id=user.id,
        full_name=full_name
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        "message": "Student registered successfully"
    }), 201


# COMPANY REGISTER
@auth_bp.route("/company/register", methods=["POST"])
def company_register():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    company_name = data.get("company_name")

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return jsonify({
            "message": "User already exists"
        }), 400

    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    user = User(
        email=email,
        password=hashed_password,
        role="company"
    )

    db.session.add(user)
    db.session.commit()

    company = Company(
        user_id=user.id,
        company_name=company_name,
        approved=False
    )

    db.session.add(company)
    db.session.commit()

    return jsonify({
        "message": "Company registered. Waiting for admin approval."
    }), 201


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return jsonify({
            "message": "Invalid email"
        }), 401

    valid_password = bcrypt.check_password_hash(
        user.password,
        password
    )

    if not valid_password:
        return jsonify({
            "message": "Invalid password"
        }), 401

    if user.role == "company":

        company = Company.query.filter_by(
            user_id=user.id
        ).first()

        if not company.approved:
            return jsonify({
                "message": "Company not approved by admin"
            }), 403

    access_token = create_access_token(
    identity=str(user.id),
    additional_claims={
        "role": user.role
    }
    )

    return jsonify({
        "message": "Login successful",
        "token": access_token,
        "role": user.role
    }), 200


# DASHBOARD STATS
