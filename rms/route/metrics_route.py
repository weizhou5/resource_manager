from flask import Blueprint
from prometheus_client import generate_latest
from prometheus_client import REGISTRY

metrics_blueprint = Blueprint('metrics', __name__)


@metrics_blueprint.route('/metrics', methods=['GET'])
def show_metrics():
    # registry = REGISTRY
    metrics = generate_latest(REGISTRY)
    return metrics, 200
