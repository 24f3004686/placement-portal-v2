from flask import Flask

from config import Config
from extensions import db, bcrypt, jwt
from flask_cors import CORS
# Import models
import models

# Import route blueprints
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.company_routes import company_bp
from routes.student_routes import student_bp
from routes.job_routes import job_bp


app = Flask(__name__)
CORS(app)
# Load config
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(company_bp)
app.register_blueprint(student_bp)
app.register_blueprint(job_bp)


@app.route("/")
def home():
    return "Placement Portal Backend Running"


if __name__ == "__main__":
    app.run(debug=True)
