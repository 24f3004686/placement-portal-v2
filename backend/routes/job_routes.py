from flask import Blueprint

job_bp = Blueprint(
    "job",
    __name__,
    url_prefix="/job"
)

@job_bp.route("/")
def job_home():
    return "Job Routes Working"
