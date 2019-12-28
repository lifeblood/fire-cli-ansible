from bootstrap import app


class Ansible(object):
    def __init__(self):
        pass

    def get_hosts(self):
        pass

    def bootstrap(self, role, json_parameter):
        cmd = ['ansible-playbook playbooks/' + role + '.yml -e ' + json_parameter]
        app.utils().subprocess_check_call(*cmd)
        pass


