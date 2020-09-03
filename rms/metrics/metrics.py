import os
import threading

from flask import Flask
from prometheus_client import Summary, Counter

from rms.utils import flask_app_config, rms_config

ouId = os.getenv("OU_ID", "ouId")
app = Flask(os.getenv('FLASK_CONFIG', 'development'))
s = Summary(name='eap_storage_resource_manager_summary', documentation='summary', labelnames=['ouId', "label"])
c = Counter(name='eap_storage_resource_manager_counter', documentation='counter', labelnames=['ouId', "label"])
second = rms_config()["frequency_second"]


def health():
    try:
        s.labels(ouId, 'health').observe(1)
    except Exception as e:
        s.labels(ouId, 'health').observe(0)
    finally:
        c.labels(ouId, 'health').inc(1)
    timer = threading.Timer(second, health)
    timer.start()


def metrics_summary(label, count):
    s.labels(ouId, label).observe(count)
    c.labels(ouId, label).inc(1)
