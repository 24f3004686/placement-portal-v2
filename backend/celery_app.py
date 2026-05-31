from celery import Celery

celery = Celery(

    "placement_portal",

    broker="redis://localhost:6379/0",

    backend="redis://localhost:6379/0"

)

celery.conf.beat_schedule = {

    "interview-reminder": {

        "task": "tasks.interview_reminder",

        "schedule": 60.0

    }

}

celery.conf.timezone = "Asia/Kolkata"