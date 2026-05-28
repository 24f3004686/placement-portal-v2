from flask import Blueprint

company_bp = Blueprint(
    "company",
    __name__,
    url_prefix="/company"
)

@company_bp.route("/")
def company_home():
    return "Company Routes Working"
