from extensions import db


class Application(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    status = db.Column(
        db.String(30),
        default="Applied"
    )

    feedback = db.Column(
        db.String(200)
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id")
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("job_position.id")
    )