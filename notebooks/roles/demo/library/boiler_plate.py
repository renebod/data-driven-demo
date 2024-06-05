#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():

    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            name      = dict(required=True),
            enabled   = dict(required=True, type='bool'),
            something = dict(aliases=['whatever'])
        )
    )
    module.exit_json(changed=True, something_else=12345)

if __name__ == '__main__':
    main()
