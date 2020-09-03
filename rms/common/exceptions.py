import json


class ServiceException(Exception):
    def __init__(self, msg):
        # TODO inner 5 digit error code for inner use
        self.error_code = msg.value['code']
        self.error_title = msg.value['msg']
        self.error_msg = msg.value['msg']

    def __init__(self, code, title, msg):
        # TODO inner 5 digit error code for inner use
        self.error_code = code
        self.error_title = title
        self.error_msg = msg


class ServiceCompilerException(ServiceException):
    def __init__(self, error_code, error_msg):
        super(ServiceCompilerException, self).__init__(error_code, error_msg, 'Compiler Exception')
