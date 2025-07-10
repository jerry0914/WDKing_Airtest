# -*- encoding=utf8 -*-
__author__ = "Jerry_Huang"

from airtest.core.api import *
#引進LoginAir
using("common.air")
import common
auto_setup(__file__)
def spin_test():
    
    if exists(Template(r"tpl1726123845888.png", threshold=0.95, rgb=True, record_pos=(-0.328, -0.422), resolution=(1080, 1920))):
        touch(Template(r"tpl1726123845888.png", record_pos=(-0.317, -0.414), resolution=(1080, 1920)))

    wait (Template(r"tpl1724409890448.png", record_pos=(-0.317, -0.516), resolution=(1080, 2400)),timeout=180, interval=3)
    touch(Template(r"tpl1724409890448.png"))

    common.wait_game_info_button()
    if exists(Template(r"tpl1724385189071.png", record_pos=(-0.004, 0.057), resolution=(1080, 2400))):
        touch(Template(r"tpl1724385189071.png", record_pos=(-0.004, 0.057), resolution=(1080, 2400)))
    common.wait_enter_into_game()
    common.check_close_dialog()
    for i in range(0, 10):
        wait(Template(r"tpl1724384851689.png", record_pos=(-0.006, 0.932), resolution=(1080, 2400)),timeout=120, interval=3)
        print("第{}次Spin".format(i+1))
        touch(Template(r"tpl1724384851689.png", record_pos=(-0.006, 0.932), resolution=(1080, 2400)))
        common.in_game_wait_go_back(timeout=300)