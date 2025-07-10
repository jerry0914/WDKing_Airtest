# -*- encoding=utf8 -*-
__author__ = "Jerry_Huang"

from airtest.core.api import *
using("common.air")
import common

auto_setup(__file__)
def spin_test():
    if exists(Template(r"tpl1727860219029.png", threshold=0.95, rgb=True, record_pos=(0.311, -0.189), resolution=(1080, 1920))):
        touch(Template(r"tpl1727860219029.png", record_pos=(0.305, -0.19), resolution=(1080, 1920)))
    wait (Template(r"tpl1727860295719.png", threshold=0.9, rgb=True, record_pos=(0.313, -0.19), resolution=(1080, 1920)),timeout=120, interval=3)
    touch(Template(r"tpl1727860295719.png", record_pos=(0.305, -0.19), resolution=(1080, 1920)))    
    common.wait_game_info_button()
    if exists(Template(r"tpl1727860432224.png", record_pos=(-0.001, 0.047), resolution=(1080, 1920))):
        touch(Template(r"tpl1727860432224.png", record_pos=(-0.001, 0.057), resolution=(1080, 1920)))
    common.wait_enter_into_game()
    common.check_close_dialog()
    for i in range(0,10):
        wait(Template(r"tpl1727860576436.png", threshold=0.95, rgb=True, record_pos=(-0.001, 0.715), resolution=(1080, 1920)),timeout=120,interval=3)
        print("第{}次Spin".format(i+1))
        touch(Template(r"tpl1727860576436.png", record_pos=(-0.003, 0.705), resolution=(1080, 1920)))
        common.in_game_wait_go_back(timeout=300)





    

    

