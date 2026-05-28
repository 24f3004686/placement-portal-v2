from flask import Blueprint

student_bp = Blueprint(
    "student",
    __name__,
    url_prefix="/student"
)

@student_bp.route("/")
def student_home():
    return "Student Routes Working"
