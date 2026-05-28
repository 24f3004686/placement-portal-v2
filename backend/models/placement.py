from extensions import db


class Placement(db.Model):

    __tablename__ = "placement"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id"),
        nullable=False
    )

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("company.id"),
        nullable=False
    )

    position = db.Column(db.String(100))

    salary = db.Column(db.Float)

    joining_date = db.Column(db.Date)

    student = db.relationship(
        "Student",
        backref="placements",
        lazy=True
    )

    company = db.relationship(
        "Company",
        backref="placements",
        lazy=True
    )

    def __repr__(self):
        return f"<Placement {self.id}>"