from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt,
    get_jwt_identity
)

from extensions import db

from models.student import Student
from models.job import JobPosition
from models.application import Application
from models.user import User
from tasks import export_history_csv
from models.notification import Notification



student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/student"
)


# STUDENT DASHBOARD

# GET PROFILE

@student_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():

    user_id = int(get_jwt_identity())

    student = Student.query.filter_by(
        user_id=user_id
    ).first()

    if not student:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify({
        "full_name": student.full_name,
        "branch": student.branch,
        "cgpa": student.cgpa,
        "graduation_year": student.graduation_year,
        "skills": student.skills,
        "resume": student.resume
    }), 200


# UPDATE PROFILE

@student_bp.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():

    user_id = int(get_jwt_identity())

    student = Student.query.filter_by(
        user_id=user_id
    ).first()

    if not student:
        return jsonify({
            "message": "Student not found"
        }), 404

    data = request.get_json()

    student.branch = data.get("branch")
    student.cgpa = data.get("cgpa")
    student.graduation_year = data.get("graduation_year")
    student.skills = data.get("skills")
    student.resume = data.get("resume")

    db.session.commit()

    return jsonify({
        "message": "Profile updated"
    }), 200


# APPLY JOB

@student_bp.route("/apply/<int:job_id>", methods=["POST"])
@jwt_required()
def apply_job(job_id):

    user_id = int(get_jwt_identity())

    student = Student.query.filter_by(
        user_id=user_id
    ).first()

    if not student:
        return jsonify({
            "message": "Student not found"
        }), 404

    existing = Application.query.filter_by(
        student_id=student.id,
        job_id=job_id
    ).first()

    if existing:
        return jsonify({
            "message": "Already applied"
        }), 400

    application = Application(
        student_id=student.id,
        job_id=job_id
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "message": "Application submitted"
    }), 201

# MY APPLICATIONS

@student_bp.route("/applications", methods=["GET"])
@jwt_required()
def my_applications():

    user_id = int(get_jwt_identity())

    student = Student.query.filter_by(
        user_id=user_id
    ).first()

    if not student:
        return jsonify({
            "message": "Student not found"
        }), 404

    applications = Application.query.filter_by(
        student_id=student.id
    ).all()

    result = []

    for app in applications:

        job = JobPosition.query.get(app.job_id)

        result.append({
            "id": app.id,
            "job_title": job.title,
            "status": app.status,
            "interview_date": app.interview_date,
            "feedback": app.feedback
            
        })

    return jsonify(result), 200






@student_bp.route("/jobs", methods=["GET"])
@jwt_required()
def get_jobs():

    jobs = JobPosition.query.filter_by(
        status="Active"
    ).all()

    result = []

    for job in jobs:

        result.append({
            "id": job.id,
            "title": job.title,
            "skills_required": job.skills_required,
            "salary": job.salary,
            "status": job.status
        })

    return jsonify(result), 200


@student_bp.route("/offer-letter/<int:application_id>")
@jwt_required()
def get_offer_letter(application_id):

    application = Application.query.get(application_id)

    if application.status != "Selected":

        return jsonify({
            "message": "No offer letter available"
        }), 400

    return jsonify({

        "company": application.job.company.company_name,

        "job": application.job.title,

        "salary": application.job.salary,

        "status": "Selected"

    }), 200
    
    
@student_bp.route(
    "/export-csv",
    methods=["POST"]
)
@jwt_required()
def export_csv():

    student_id = int(
        get_jwt_identity()
    )

    task = export_history_csv.delay(
        student_id
    )

    return jsonify({

        "message": "Export started",
        "task_id": task.id

    }), 202
    
    
@student_bp.route(
    "/notifications",
    methods=["GET"]
)
@jwt_required()
def get_notifications():

    student_id = int(
        get_jwt_identity()
    )

    notifications = (
        Notification.query
        .filter_by(
            student_id=student_id
        )
        .order_by(
            Notification.created_at.desc()
        )
        .all()
    )

    return jsonify([

        {
            "id": n.id,
            "message": n.message,
            "created_at":
            str(n.created_at)
        }

        for n in notifications

    ])
    
    
@student_bp.route(
    "/notifications-test",
    methods=["GET"]
)
def notifications_test():

    notifications = Notification.query.all()

    return jsonify([

        {
            "id": n.id,
            "message": n.message
        }

        for n in notifications

    ])