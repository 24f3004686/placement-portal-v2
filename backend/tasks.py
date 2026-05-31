from celery_app import celery
from models.student import Student
from models.company import Company
from models.application import Application
from models.job import JobPosition
from models.notification import Notification
from extensions import db
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


@celery.task
def test_task():
    print("Celery is working!")
    return "Success"


@celery.task
def export_history_csv(student_id):

    print(
        f"Exporting CSV for student {student_id}"
    )

    return "CSV Exported"


@celery.task
def export_company_csv(company_id):

    print(
        f"Exporting applications for company {company_id}"
    )

    return "Company CSV Exported"


@celery.task
def interview_reminder():

    from app import app

    with app.app_context():

        applications = Application.query.filter(
            Application.interview_date != None
        ).all()

        for app_obj in applications:

            job = JobPosition.query.get(
                app_obj.job_id
            )

            student = Student.query.get(
                app_obj.student_id
            )

            message = f"""
Reminder:

Your interview for {job.title}
is scheduled on {app_obj.interview_date}
"""

            notification = Notification(
                student_id=student.id,
                message=message
            )

            db.session.add(notification)

            print(message)

        db.session.commit()

        print(
            "Interview reminders created"
        )

@celery.task
def generate_placement_report():

    from app import app

    with app.app_context():

        total_students = Student.query.count()

        total_companies = Company.query.count()

        total_jobs = JobPosition.query.count()

        total_applications = Application.query.count()

        placed_students = (
            Application.query
            .filter_by(status="Placed")
            .count()
        )

        placement_rate = 0

        if total_students > 0:

            placement_rate = round(

                (placed_students / total_students) * 100,

                2

            )

        os.makedirs(
            "reports",
            exist_ok=True
        )

        pdf_file = (
            "reports/placement_report.pdf"
        )

        html_file = (
            "reports/placement_report.html"
        )

        # ---------- PDF ----------

        doc = SimpleDocTemplate(
            pdf_file
        )

        styles = getSampleStyleSheet()

        content = [

            Paragraph(
                "Placement Report",
                styles["Title"]
            ),

            Spacer(1, 20),

            Paragraph(
                f"Total Students: {total_students}",
                styles["Normal"]
            ),

            Paragraph(
                f"Total Companies: {total_companies}",
                styles["Normal"]
            ),

            Paragraph(
                f"Total Jobs: {total_jobs}",
                styles["Normal"]
            ),

            Paragraph(
                f"Applications: {total_applications}",
                styles["Normal"]
            ),

            Paragraph(
                f"Placed Students: {placed_students}",
                styles["Normal"]
            ),

            Paragraph(
                f"Placement Rate: {placement_rate}%",
                styles["Normal"]
            )

        ]

        doc.build(content)

        # ---------- HTML ----------

        html_content = f"""
        <html>
        <head>
            <title>Placement Report</title>
        </head>

        <body>

            <h1>Placement Report</h1>

            <hr>

            <h3>Total Students: {total_students}</h3>

            <h3>Total Companies: {total_companies}</h3>

            <h3>Total Jobs: {total_jobs}</h3>

            <h3>Total Applications: {total_applications}</h3>

            <h3>Placed Students: {placed_students}</h3>

            <h3>Placement Rate: {placement_rate}%</h3>

        </body>
        </html>
        """

        with open(

            html_file,

            "w",

            encoding="utf-8"

        ) as f:

            f.write(
                html_content
            )

        print(
            f"PDF Generated: {pdf_file}"
        )

        print(
            f"HTML Generated: {html_file}"
        )

        return {

            "pdf": pdf_file,

            "html": html_file

        }