from extensions import db


class Application(db.Model):

    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("job_positions.id"),
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="Applied"
    )

    applied_date = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    student = db.relationship(
        "Student",
        backref="applications",
        lazy=True
    )

    job = db.relationship(
        "JobPosition",
        backref="applications",
        lazy=True
    )

    def __repr__(self):
        return f"<Application {self.id}>"