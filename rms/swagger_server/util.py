import base64
import datetime
import json
import logging
import sys
import typing
import connexion
import six

from rms.AESEncrypt import AESEncrypt

USER = "Eap-User"


def create_logger(name):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
    )
    logger_instance = logging.getLogger(name)
    logger_instance.setLevel(logging.INFO)
    logger_instance.addHandler(handler)
    return logger_instance


logger = create_logger(__name__)


def get_user(request):
    user = request.headers[USER]
    encrypt = AESEncrypt()
    user_decode = encrypt.decrypt(user)
    user_json = json.loads(user_decode)
    user_name = user_json['username']
    return user_name


def get_ou_id(request):
    user = request.headers[USER]
    encrypt = AESEncrypt()
    user_decode = encrypt.decrypt(user)
    user_json = json.loads(user_decode)
    ou_id = user_json['organization']['id']
    return ou_id


def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        if isinstance(data, datetime.date):
            return data
        else:
            return deserialize_date(data)
    elif klass == datetime.datetime:
        if isinstance(data, datetime.datetime):
            return data
        else:
            return deserialize_datetime(data)
    elif type(klass) == typing.GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        if isinstance(data, (list, dict)):
            return deserialize_model(data, klass)
        else:
            return copy_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def copy_model(data, klass):
    """Deserializes list or dict to entity.

        :param data: dict, list.
        :type data: dict | list
        :param klass: class literal.
        :return: entity object.
        """
    instance = klass()

    if not instance.swagger_types:
        return data
    for attr, attr_type in six.iteritems(instance.swagger_types):

        if data is not None \
                and instance.attribute_map[attr] in data.attribute_map:
            value = data.__getattribute__(attr)
            setattr(instance, attr, _deserialize(value, attr_type))
    return instance


def deserialize_model(data, klass):
    """Deserializes list or dict to entity.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: entity object.
    """
    instance = klass()

    if not instance.swagger_types:
        return data

    for attr, attr_type in six.iteritems(instance.swagger_types):
        if data is not None \
                and instance.attribute_map[attr] in data \
                and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}


def get_attr_value(data, attr):
    if isinstance(data, dict):
        return data[attr]
    elif isinstance(data, object) and hasattr(data, attr):
        return getattr(data, attr)
    else:
        NotImplementedError
