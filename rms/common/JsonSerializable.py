import pprint


def list_class_properties(cls):
    return [k for k, v in cls.__dict__.items() if type(v) is property and not k.startswith('__')]


class JsonSerializable(object):
    def to_json(self):
        # default to_json, overwrite it if want customization
        properties = {}
        property_keys = list_class_properties(type(self))
        for key in property_keys:
            properties[key] = getattr(self, key)
        return properties

    def __repr__(self):
        return pprint.pformat(self.to_json())
