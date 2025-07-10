# -*- encoding=utf8 -*-
__author__ = "jerry_huang"

from airtest.core.api import *
import time
import subprocess
import urllib.request

auto_setup(__file__)

def start_app_():

    package_name = "com.wudiking.wd_dev"
    activity_name = "com.unity3d.player.UnityPlayerActivity"
    stop_app(package_name)
    start_app(package_name)

def is_app_started()->bool:
    is_ready=False
    for i in range(0,100):
        if exists(Template(r"tpl1726122408230.png")):
            is_ready=True
            break
        if exists(Template(r"tpl1724405137858.png")):
            is_ready=True
            break
        sleep(1.0)
    return is_ready

def login_to_ele_lobby():
    is_ready = is_app_started()
    assert_equal(is_ready,True,"is_app_started")

    if exists(Template(r"tpl1726122408230.png")):   
        touch(Template(r"tpl1726122426318.png"))


    #使用試玩帳號進入
    for i in range(1, 30):
        if exists(Template(r"tpl1724405137858.png")):
            touch(Template(r"tpl1724405137858.png"))
            wait(Template(r"tpl1724409014499.png"),timeout=120, interval=3)
            break;
        time.sleep(1)
            


    #進到電子館
    #=============================================================

    touch(Template(r"tpl1724409014499.png", record_pos=(-0.244, 0.275), resolution=(1080, 2400)))


    wait (Template(r"tpl1724384775404.png", record_pos=(-0.196, -0.719), resolution=(1080, 2400)),timeout=120, interval=3)

    touch(Template(r"tpl1724384775404.png", record_pos=(-0.196, -0.719), resolution=(1080, 2400)))
    
    is_in_eglobby=wait_to_ele_lobby()
    assert_equal(is_in_eglobby,True, "login_to_ele_lobby")

    #=============================================================

def in_game_wait_go_back(timeout=120)->bool:
    wait(Template(r"tpl1727918781875.png", threshold=0.95, rgb=True, record_pos=(0.423, -0.615), resolution=(1080, 1920)),timeout=timeout,interval=3)
    is_exists = exists(Template(r"tpl1727918781875.png", threshold=0.95, rgb=True, record_pos=(0.052, -0.792), resolution=(1080, 1920))) is not None
    return is_exists 
    
def game_back_to_ele_lobby():
    
    is_ok = in_game_wait_go_back()
    assert_equal(is_ok,True, "game_back_to_ele_lobby1")
    touch(Template(r"tpl1727918781875.png", record_pos=(-0.196, -0.719), resolution=(1080, 2400)))
    is_in_eglobby=wait_to_ele_lobby()
    assert_equal(is_in_eglobby,True, "game_back_to_ele_lobby2")

def wait_to_ele_lobby(timeout=120)->bool:
    
    wait(Template(r"tpl1727919671082.png", threshold=0.7, rgb=False, record_pos=(0.423, -0.615), resolution=(1080, 1920)),timeout=timeout,interval=3)
    is_exists = exists(Template(r"tpl1727919671082.png", threshold=0.7, rgb=False, record_pos=(0.052, -0.792), resolution=(1080, 1920))) is not None
    return is_exists

def wait_game_info_button(timeout=120) -> bool:
    
    wait(Template(r"tpl1727920561150.png", threshold=0.7, rgb=False, record_pos=(0.423, -0.615), resolution=(1080, 1920)),timeout=timeout,interval=3)
    is_exists = exists(Template(r"tpl1727920561150.png", threshold=0.7, rgb=False, record_pos=(0.052, -0.792), resolution=(1080, 1920))) is not None
    return is_exists

def wait_enter_into_game(timeout=120) -> bool:
    wait(Template(r"tpl1727918781875.png", threshold=0.7, rgb=False, record_pos=(0.423, -0.615), resolution=(1080, 1920)),timeout=timeout,interval=3)
    is_exists = exists(Template(r"tpl1727918781875.png", threshold=0.7, rgb=False, record_pos=(0.052, -0.792), resolution=(1080, 1920))) is not None
    return is_exists



def check_close_dialog():
    if exists(Template(r"tpl1727861835380.png", record_pos=(0.004, 0.083), resolution=(1080, 1920))):
        touch(Template(r"tpl1727861835380.png", record_pos=(-0.008, 0.089), resolution=(1080, 1920)))


        
            