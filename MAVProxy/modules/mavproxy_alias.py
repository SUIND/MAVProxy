#!/usr/bin/env python3
'''
alias commands
'''

from MAVProxy.modules.lib import mp_module

class AliasModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(AliasModule, self).__init__(mpstate, "alias", "custom command aliases")
        self.add_command('ps', self.cmd_ps, "alias for 'param set'")

    def cmd_ps(self, args):
    if len(args) < 2:
        print("Usage: ps PARAM_NAME VALUE")
        return
    param_name = args[0]
    try:
        value = float(args[1])  # Ensure the value is converted to a float
    except ValueError:
        print(f"Invalid value: {args[1]} is not a float")
        return
    self.master.param_set_send(param_name, value)
    print(f"Set parameter {param_name} to {value}")

def init(mpstate):
    return AliasModule(mpstate)

