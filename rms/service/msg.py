from enum import Enum


class Msg(Enum):
    AMOUNT_ERROR = {'code': 1001, 'msg': 'amount invalid'}
    INSERT_ERROR = {'code': 1002, 'msg': 'Failed to mysql insert'}
    DELETE_ERROR = {'code': 1003, 'msg': 'Failed to mysql delete'}
    QUERY_ERROR = {'code': 1004, 'msg': 'Failed to mysql query'}
    CREATE_PVC_ERROR = {'code': 1005, 'msg': 'Failed to pvc create'}
