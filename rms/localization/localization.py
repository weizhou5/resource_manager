# TODO localization improvement
# TODO naive implementation
import json
from enum import Enum
from pathlib import Path


class Locale(Enum):
    ZH = 'zh'
    EN = 'en'


def localize(text, locale: Locale):
    # TODO only supports zh for now
    json_file = str(Path(__file__).parent / '{}.json'.format(locale.value))
    with open(json_file, 'r', encoding='utf-8') as f:
        locale_json = json.load(f)
        return locale_json.check_pvc(text, text)

