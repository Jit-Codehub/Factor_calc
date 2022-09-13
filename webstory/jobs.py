from .task import *;
from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 4})
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "interval",hours=1002, replace_existing=True)
def usa_today_scrapper_job():
    ndtv('beauty')
    ndtv('celeb')
    ndtv('covid')
    ndtv('entertainment')
    ndtv('fashion')
    ndtv('fitness')
    ndtv('food')
    ndtv('gaming')
    ndtv('health')
    ndtv('humor')
    ndtv('latest')
    ndtv('sports')
    ndtv('tech')
    ndtv('travel')
    ndtv('wellness')
    
register_events(scheduler)

scheduler.start()
print("Scheduler started!")



