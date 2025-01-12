#!/usr/bin/env python3
'''
alias commands
'''

from MAVProxy.modules.lib import mp_module

class AliasModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(AliasModule, self).__init__(mpstate, "alias", "custom command aliases")
        self.add_command('set_param_chksm', self.cmd_set_param_chksm, "update param checksum")
        self.add_command('set_fw_chksm', self.cmd_set_fw_chksm, "update fw checksum")
        self.add_command('pair_gps', self.cmd_pair_gps, "bind GPS to AP")

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

