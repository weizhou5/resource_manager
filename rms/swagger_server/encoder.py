import six
from connexion.apps.flask_app import FlaskJSONEncoder

from rms.common.JsonSerializable import JsonSerializable
from rms.swagger_server.models.base_model_ import Model


class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr, _ in six.iteritems(o.swagger_types):
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        if isinstance(o, JsonSerializable):
            return o.to_json()
        return FlaskJSONEncoder.default(self, o)
