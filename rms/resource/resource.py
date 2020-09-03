class Resource(object):

    def create_pvc(self, body):
        raise NotImplementedError()

    def delete_pvc(self, namespace, name):
        raise NotImplementedError()

    def check_pvc(self, namespace, name):
        raise NotImplementedError()

    def get_mount(self, namespace, name):
        raise NotImplementedError()

    def namespace_list(self, ou_id):
        raise NotImplementedError()

    def check_key_tab(self, namespace, ou_id):
        raise NotImplementedError()
