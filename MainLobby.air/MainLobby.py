# -*- encoding=utf8 -*-
__author__ = "Jerry_Huang"

from airtest.core.api import *
from airtest.core.api import *
import time
import subprocess
import urllib.request

auto_setup(__file__)

def launch_app():
    package_name = "com.wudiking.wd_dev"
    activity_name = "com.unity3d.player.UnityPlayerActivity"
    stop_app(package_name)
    start_app(package_name)
    
def is_app_started()->bool:
    result=False

def _click_data_download():
    result = waitForExists(Template(r"tpl1751624985466.png"),retry=60)
    if result:
        touch(result)
        return;

def _enter_password():
    result = waitForExists(Template(r"tpl1751959430709.png", record_pos=(-0.004, -0.001), resolution=(1080, 2400)),retry=30)
    if result:
        touch(result)
        sleep(2)
        text("1299")
        touch(Template(r"tpl1751625381773.png", record_pos=(-0.002, 0.154), resolution=(1080, 2400)))
        
def is_first_time_enter_main_lobby()->bool:
    result = waitForExists(Template(r"tpl1751627315854.png",record_pos=(-0.006, 0.68), resolution=(1080, 2400)),retry=30)
    if result:
        touch(result)
    if result:
        result = waitForExists(Template(r"tpl1751959709375.png", record_pos=(0.258, 0.688), resolution=(1080, 2400)),retry=30)
        if result:
              touch(result)
    return result is not False


def _close_ad(lastResult:bool = False)->bool:
    target = waitForExists(Template(r"tpl1751954040752.png", record_pos=(0.002, 1.013), resolution=(1080, 2400)),retry=3)
    result = lastResult | (target is not False)
    if target:
        touch(target)
        sleep(1)
        _close_ad(True)
    return result
       
def _close_navi(lastResult:bool = False)->bool:
    target = waitForExists(Template(r"tpl1751954806599.png", record_pos=(0.005, 1.049), resolution=(1080, 2400)),retry=3)
    result = lastResult | (target is not False)
    if target:
        touch(target)
        sleep(1)
        _close_navi(True)
    return result


def waitForExists(v,retry:int):
    result=False
    for i in range(0, retry):
        result = exists(v)
        if result is not False:
            break
    return result

def close_ad_and_nave():
    result  = _close_ad()
    result |= _close_navi()
    if result:
        close_ad_and_nave()

# launch_app()
# sleep(30)
# _click_data_download()
# sleep(100)
# _enter_password()
# is_first_time_enter_main_lobby()
close_ad_and_nave()
assert exists(Template(r"tpl1751973367903.png", record_pos=(-0.275, 0.007), resolution=(1080, 2400)))


