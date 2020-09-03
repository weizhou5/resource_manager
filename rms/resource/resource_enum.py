from enum import Enum

from rms.resource.k8s import K8s
from rms.resource.rms import Rms


class ResourceEnum(Enum):
    RMS = Rms()
    K8S = K8s()
