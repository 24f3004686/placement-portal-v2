from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt,
    get_jwt_identity
)

from extensions import db

from models.job import JobPosition
from models.application import Application
from models.student import Student
from tasks import export_company_csv
from flask import send_file


company_bp = Blueprint(
    "company",
    __name__,
    url_prefix="/company"
)


# COMPANY DASHBOARD
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


# CREATE JOB
@company_bp.route("/create-job", methods=["POST"])
@jwt_required()
def create_job():

    claims = get_jwt()

    if claims["role"] != "company":

        return jsonify({
            "message": "Access denied"
        }), 403

    data = request.get_json()

    company_id = int(get_jwt_identity())

    new_job = JobPosition(

        title=data["title"],

        skills_required=data["skills_required"],

        salary=data["salary"],

        benefits=data["benefits"],

        company_id=company_id

    )

    db.session.add(new_job)

    db.session.commit()

    return jsonify({
        "message": "Job created successfully"
    }), 201


# GET COMPANY JOBS
@company_bp.route("/jobs", methods=["GET"])
@jwt_required()
def get_company_jobs():

    claims = get_jwt()

    if claims["role"] != "company":

        return jsonify({
            "message": "Access denied"
        }), 403

    company_id = int(get_jwt_identity())

    jobs = JobPosition.query.filter_by(
        company_id=company_id
    ).all()

    job_list = []

    for job in jobs:

        job_list.append({

            "id": job.id,

            "title": job.title,

            "skills_required": job.skills_required,

            "salary": job.salary,

            "status": job.status

        })

    return jsonify(job_list), 200

# CLOSE JOB
@company_bp.route("/close-job/<int:job_id>", methods=["PUT"])
@jwt_required()
def close_job(job_id):

    claims = get_jwt()

    if claims["role"] != "company":

        return jsonify({
            "message": "Access denied"
        }), 403

    job = JobPosition.query.get(job_id)

    if not job:

        return jsonify({
            "message": "Job not found"
        }), 404

    job.status = "Closed"

    db.session.commit()

    return jsonify({
        "message": "Job closed"
    }), 200
    
    
# REOPEN JOB
@company_bp.route("/reopen-job/<int:job_id>", methods=["PUT"])
@jwt_required()
def reopen_job(job_id):

    claims = get_jwt()

    if claims["role"] != "company":

        return jsonify({
            "message": "Access denied"
        }), 403

    job = JobPosition.query.get(job_id)

    if not job:

        return jsonify({
            "message": "Job not found"
        }), 404

    job.status = "Active"

    db.session.commit()

    return jsonify({
        "message": "Job reopened"
    }), 200
    
# DELETE JOB
@company_bp.route("/delete-job/<int:job_id>", methods=["DELETE"])
@jwt_required()
def delete_job(job_id):

    claims = get_jwt()

    if claims["role"] != "company":

        return jsonify({
            "message": "Access denied"
        }), 403

    job = JobPosition.query.get(job_id)

    if not job:

        return jsonify({
            "message": "Job not found"
        }), 404

    db.session.delete(job)

    db.session.commit()

    return jsonify({
        "message": "Job deleted"
    }), 200


@company_bp.route("/schedule-interview/<int:application_id>", methods=["PUT"])
@jwt_required()
def schedule_interview(application_id):

    application = Application.query.get(application_id)

    if not application:
        return jsonify({"message": "Application not found"}), 404

    data = request.get_json()

    application.status = "Interview Scheduled"

    application.interview_date = data.get("interview_date")

    db.session.commit()

    return jsonify({
        "message": "Interview Scheduled"
    }), 200
    
    
@company_bp.route("/feedback/<int:application_id>", methods=["PUT"])
@jwt_required()
def add_feedback(application_id):

    application = Application.query.get(application_id)

    if not application:
        return jsonify({"message": "Application not found"}), 404

    data = request.get_json()

    application.feedback = data.get("feedback")

    db.session.commit()

    return jsonify({
        "message": "Feedback Added"
    }), 200
    
    
    
@company_bp.route("/select/<int:application_id>", methods=["PUT"])
@jwt_required()
def select_candidate(application_id):

    application = Application.query.get(application_id)

    if not application:
        return jsonify({
            "message": "Application not found"
        }), 404

    application.status = "Selected"

    db.session.commit()

    return jsonify({
        "message": "Candidate Selected"
    }), 200
    
    
@company_bp.route("/applications", methods=["GET"])
@jwt_required()
def company_applications():

    claims = get_jwt()

    if claims["role"] != "company":

        return jsonify({
            "message": "Access denied"
        }), 403

    company_id = int(get_jwt_identity())

    jobs = JobPosition.query.filter_by(
        company_id=company_id
    ).all()

    result = []

    for job in jobs:

        applications = Application.query.filter_by(
            job_id=job.id
        ).all()

        for app in applications:

            student = Student.query.get(
                app.student_id
            )

            result.append({
                
                   "application_id": app.id,
                   "student_id": student.id,
                   "student_name": student.full_name,
                   "full_name": student.full_name,
                   "branch": student.branch,
                   "cgpa": student.cgpa,
                   "graduation_year": student.graduation_year,
                   "skills": student.skills,
                   "resume": student.resume,
                   "job_title": job.title,
                   "status": app.status,
                   "interview_date": app.interview_date,
                   "feedback": app.feedback

            })

    return jsonify(result), 200


@company_bp.route("/update-status/<int:application_id>", methods=["PUT"])
@jwt_required()
def update_status(application_id):

    data = request.get_json()

    application = Application.query.get(application_id)

    if not application:

        return jsonify({
            "message": "Application not found"
        }), 404

    application.status = data.get("status")

    db.session.commit()

    return jsonify({
        "message": "Status updated"
    }), 200
    
@company_bp.route("/offer/<int:application_id>", methods=["PUT"])
@jwt_required()
def offer_candidate(application_id):

    application = Application.query.get(application_id)

    if not application:

        return jsonify({
            "message": "Application not found"
        }), 404

    application.status = "Offer"

    application.offer_letter = (
        f"Offer Letter - {application.id}"
    )

    db.session.commit()

    return jsonify({
        "message": "Offer Released"
    }), 200
    
    
@company_bp.route("/placed/<int:application_id>", methods=["PUT"])
@jwt_required()
def placed_candidate(application_id):

    application = Application.query.get(application_id)

    if not application:

        return jsonify({
            "message": "Application not found"
        }), 404

    application.status = "Placed"

    db.session.commit()

    return jsonify({
        "message": "Student Placed"
    }), 200
    
    
@company_bp.route("/student/<int:student_id>")
@jwt_required()
def view_student(student_id):

    student = Student.query.get(student_id)

    return jsonify({

        "name": student.full_name,
        "branch": student.branch,
        "cgpa": student.cgpa,
        "graduation_year": student.graduation_year,
        "skills": student.skills,
        "resume": student.resume,
        

    }), 200
    
    
@company_bp.route(
    "/export-csv",
    methods=["POST"]
)
@jwt_required()
def export_csv():

    company_id = int(
        get_jwt_identity()
    )

    task = export_company_csv.delay(
        company_id
    )

    return jsonify({

        "message": "Export started",
        "task_id": task.id

    }), 202
    
@company_bp.route(
    "/download-report/pdf",
    methods=["GET"]
)
@jwt_required()
def download_pdf():

    return send_file(

        "reports/placement_report.pdf",

        as_attachment=True

    )
    
    
@company_bp.route(
    "/download-report/html",
    methods=["GET"]
)
@jwt_required()
def download_html():

    return send_file(

        "reports/placement_report.html",

        as_attachment=True

    )