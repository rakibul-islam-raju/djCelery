import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djCelery.settings")
app = Celery("djCelery")
app.config_from_object("django.conf:settings", namespace="CELERY")


# routing
# app.conf.task_routes = {
#     "newapp.tasks.task1": {"queue": "queue1"},
# }

# Task Prioritize
app.conf.broker_transport_options = {
    "priority_steps": list(range(10)),
    "sep": ":",
    "queue_order_strategy": "priority",
}

app.autodiscover_tasks()
