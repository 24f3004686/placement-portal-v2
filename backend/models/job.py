from extensions import db


class JobPosition(db.Model):

    __tablename__ = "job_positions"

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(db.Text)

    salary = db.Column(db.Float)

    skills_required = db.Column(db.Text)

    deadline = db.Column(db.Date)

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    company = db.relationship(
        "Company",
        backref="jobs",
        lazy=True
    )

    def __repr__(self):
        return f"<Job {self.title}>"