from flask import Blueprint, jsonify
from models.student import Student
from models.company import Company
from models.job import JobPosition
from models.application import Application

public_bp = Blueprint("public", __name__)

@public_bp.route("/dashboard", methods=["GET"])
def public_dashboard():

    return jsonify({

        "students": Student.query.count(),

        "companies": Company.query.count(),

        "jobs": JobPosition.query.count(),

        "applications": Application.query.count(),

        "placed": Application.query.filter_by(status="Placed").count(),

        "selected": Application.query.filter_by(status="Selected").count(),

        "rejected": Application.query.filter_by(status="Rejected").count(),

        "pending": Application.query.filter(
            Application.status.in_([
                "Pending",
                "Applied",
                "Shortlisted"
            ])
        ).count()

    })
