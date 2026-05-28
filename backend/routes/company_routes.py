from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt,
    get_jwt_identity
)

from extensions import db

from models.job import JobPosition


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
