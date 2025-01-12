#!/usr/bin/env python3
'''
alias commands
'''

from MAVProxy.modules.lib import mp_module

class AliasModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(AliasModule, self).__init__(mpstate, "alias", "custom command aliases")
        self.add_command('ps', self.cmd_ps, "alias for 'param set'")

    def cmd_set_param_chksm(self, args):
        param_name = "REC_PARAM_HSH"
        value = 1
        self.master.param_set_send(param_name, value)
        #print(f"Set parameter {param_name} to {value}")

    def cmd_set_fw_chksm(self, args):
        param_name = "REC_FW_HSH"
        value = 1
        self.master.param_set_send(param_name, value)
        #print(f"Set parameter {param_name} to {value}")

    def cmd_pair_gps(self, args):
        param_name = "GPS_CACHE_UID"
        value = 1
        self.master.param_set_send(param_name, value)
        #print(f"Set parameter {param_name} to {value}")

def init(mpstate):
    return AliasModule(mpstate)

