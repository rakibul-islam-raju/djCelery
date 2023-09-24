import os
from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djCelery.settings")
app = Celery("djCelery")
app.config_from_object("django.conf:settings", namespace="CELERY")


# routing
# app.conf.task_routes = {
#     "newapp.tasks.task1": {"queue": "queue1"},
# }

# Task Prioritize
# app.conf.broker_transport_options = {
#     "priority_steps": list(range(10)),
#     "sep": ":",
#     "queue_order_strategy": "priority",
# }

app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    )
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

app.autodiscover_tasks()
