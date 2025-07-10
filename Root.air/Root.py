# -*- encoding=utf8 -*-
__author__ = "werewolf.k."

from airtest.core.api import *
import time

#引進LoginAir
using("common.air")
using("sp6023.air")
using("sp1027.air")
import common,sp6023,sp1027

auto_setup(__file__)

common.start_app_()

# 登入到電子館
common.login_to_ele_lobby()

sp1027.spin_test()    

common.game_back_to_ele_lobby()

sp6023.spin_test()    

common.game_back_to_ele_lobby()
    
