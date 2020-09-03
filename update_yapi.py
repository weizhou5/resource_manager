import json
import requests

with open('rms/swagger/swagger.json') as swagger:
    data = json.load(swagger)
    request_body = {
        "type": "swagger",
        "json": json.dumps(data),
        "merge": "merge",
        "token": "a0beeff7f2ed0892ca5e452783b423266c1bc432d4ec76197814ade8b387f91b"
    }
    url = "http://beta-yapi-cn2.eniot.io/api/open/import_data"
    try:
        response = requests.post(url, data=request_body)
        response.raise_for_status()
        print("yapi updated")
    except requests.exceptions.HTTPError as e:
        print(e.response.text)
