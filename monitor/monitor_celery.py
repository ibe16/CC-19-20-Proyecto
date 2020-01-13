import sys
import os
from datetime import timedelta

from celery import Celery
from celery.task import periodic_task

from monitor import Monitor
sys.path.append('notifier')
from notifier import Notifier

broker = os.environ['CELERY_BROKER_URL']
monitor = Monitor.Monitor()
notifier = Notifier.Notifier()

OK = 'operational'

app = Celery('monitor_celery', broker=broker)

@periodic_task(run_every=timedelta(seconds=10))
def check_services():
    data = monitor.get_services_status()
    #data = {'Git Operations': 'operational', 'API Requests': 'operational', 'Webhooks': 'operational', 'Visit www.githubstatus.com for more information': 'operational', 'Issues, PRs, Projects': 'operational', 'GitHub Actions': 'degraded_performance', 'GitHub Packages': 'operational', 'GitHub Pages': 'operational', 'Other': 'operational'}

    for name, status in data.items():
        if status != OK:
            notifier.notification(name)
