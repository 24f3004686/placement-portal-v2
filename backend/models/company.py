from extensions import db


class Company(db.Model):

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    company_name = db.Column(
        db.String(100),
        nullable=False
    )

    industry = db.Column(db.String(100))

    location = db.Column(db.String(100))

    website = db.Column(db.String(255))

    hr_contact = db.Column(db.String(100))

    approved = db.Column(
        db.Boolean,
        default=False
    )

    user = db.relationship(
        "User",
        backref="company",
        lazy=True
    )

    def __repr__(self):
        return f"<Company {self.company_name}>"