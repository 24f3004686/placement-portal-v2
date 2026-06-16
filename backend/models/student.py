from extensions import db


class Student(db.Model):

    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    full_name = db.Column(
        db.String(100),
        nullable=False
    )
    
    approved = db.Column(
        db.Boolean,
        default=False
    )
    
    branch = db.Column(db.String(100))

    cgpa = db.Column(db.Float)

    graduation_year = db.Column(db.Integer)

    skills = db.Column(db.Text)

    resume = db.Column(db.String(255))

    user = db.relationship(
        "User",
        backref="student",
        lazy=True
    )

    def __repr__(self):
        return f"<Student {self.full_name}>"