#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():

    module = AnsibleModule(
        argument_spec = dict(
            name        = dict(required=True),
            telephone   = dict(required=True),
            state       = dict(default='present', choices=['present', 'absent'])
        )
    )
    msg = "If you need to call " + module.params["name"] + ", please dial: " + module.params["telephone"]
    module.exit_json(changed=False, msg=msg)

if __name__ == '__main__':
    main()