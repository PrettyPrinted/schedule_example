from celery import shared_task, current_app as celery_app
from redbeat import RedBeatSchedulerEntry

@shared_task(bind=True)
def withdrawal(self, payrolltransactnumber, red_beat_name):

    print("WITHDRAWING: ", payrolltransactnumber)

    # the follow is to remove the scheduled task from the redbeat scheduler
    # otherwise it will eventually run again
    try:
        entry = RedBeatSchedulerEntry.from_key("redbeat:" + red_beat_name, app=celery_app)
    except KeyError:
        entry = None

    if entry:
        entry.delete()

    return "DONE"