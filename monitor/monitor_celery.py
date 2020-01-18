import sys
import os
from datetime import timedelta

from celery import Celery
from celery.task import periodic_task

from monitor import Monitor
# Para poder usar la función que envía los correos
sys.path.append('notifier')
from notifier import Notifier
from notifier import NotificationList

# Indicamos el broker que vamos a usar para Celery
broker = os.environ['CELERY_BROKER_URL']
monitor = Monitor.Monitor()
n = NotificationList.NotificationList()
notifier = Notifier.Notifier(n)

# Estado del servicio que no es downtime
OK = 'operational'

# Creamos la aplicación
app = Celery('monitor_celery', broker=broker)

# Tarea periódica que Celery
@periodic_task(run_every=timedelta(seconds=10))
def check_services():
    """Revisa el estado de de los servicios y notifica si alguno se encuentra en downtime"""
    data = monitor.get_services_status()
    #data = {'Git Operations': 'operational', 'API Requests': 'operational', 'Webhooks': 'operational', 'Visit www.githubstatus.com for more information': 'operational', 'Issues, PRs, Projects': 'operational', 'GitHub Actions': 'degraded_performance', 'GitHub Packages': 'operational', 'GitHub Pages': 'operational', 'Other': 'operational'}

    for name, status in data.items():
        if status != OK:
            notifier.notification(name)
