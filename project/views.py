from flask import Blueprint
from celery import current_app as celery_app
from redbeat import RedBeatSchedulerEntry
from celery.schedules import crontab

main = Blueprint("main", __name__)

@main.route("/webhook")
def webhook():
    schedule_name = "test_schedule" # can be whatever you want but should be unique for each scheduled task
    interval = crontab(month_of_year=8, day_of_month=22, hour=4, minute=30)
    entry = RedBeatSchedulerEntry(schedule_name, 'project.tasks.withdrawal', interval, args=[12345, schedule_name], app=celery_app)
    entry.save()

    return "Withdrawal scheduled"