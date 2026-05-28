from app import app
from extensions import db, bcrypt
from models.user import User


with app.app_context():

    # Check if admin already exists
    existing_admin = User.query.filter_by(
        role="admin"
    ).first()

    if not existing_admin:

        # Hash password
        hashed_password = bcrypt.generate_password_hash(
            "admin123"
        ).decode("utf-8")

        # Create admin user
        admin = User(
            email="admin@ppa.com",
            password=hashed_password,
            role="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully!")

    else:
        print("Admin already exists!")
