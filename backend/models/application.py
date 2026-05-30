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

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id")
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("job_position.id")
    )
    interview_date = db.Column(
        db.String(100)
    )

    feedback = db.Column(
        db.Text
    )
    
    offer_letter = db.Column(
    db.String(255)
    )