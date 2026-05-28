from extensions import db


class JobPosition(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    skills_required = db.Column(
        db.String(200)
    )

    salary = db.Column(
        db.String(50)
    )

    benefits = db.Column(
        db.String(200)
    )

    status = db.Column(
        db.String(20),
        default="Active"
    )

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("company.id")
    )