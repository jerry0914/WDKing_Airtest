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
    
def _check_app_start(retry:int =0):
    result = None
    if retry<60:
        result = exists(Template(r"tpl1751624985466.png"))
        if result:
            return "download"
        result = exists(Template(r"tpl1751954040752.png", record_pos=(0.002, 1.013), resolution=(1080, 2400)))
        if result:
            return "ad"
        else:
            _check_app_start(retry+1)
    return None
    
def _click_data_download():
    result = _waitForExists(Template(r"tpl1751624985466.png"),retry=60)
    if result:
        touch(result)
        return;

def _enter_password():
    result = _waitForExists(Template(r"tpl1751959430709.png", record_pos=(-0.004, -0.001), resolution=(1080, 2400)),retry=30)
    if result:
        touch(result)
        sleep(2)
        text("1299")
        touch(Template(r"tpl1751625381773.png", record_pos=(-0.002, 0.154), resolution=(1080, 2400)))
        
def _trial_player_login()->bool:
    result = _waitForExists(Template(r"tpl1751627315854.png",record_pos=(-0.006, 0.68), resolution=(1080, 2400)),retry=30)
    if result:
        touch(result)
    if result:
        result = _waitForExists(Template(r"tpl1751959709375.png", record_pos=(0.258, 0.688), resolution=(1080, 2400)),retry=30)
        if result:
              touch(result)
    return result is not False

def _close_ad(lastResult:bool = False)->bool:
    target = _waitForExists(Template(r"tpl1751954040752.png", record_pos=(0.002, 1.013), resolution=(1080, 2400)),retry=2)
    result = lastResult | (target is not False)
    if target:
        touch(target)
        sleep(1)
        _close_ad(True)
    return result
       
def _close_navi(lastResult:bool = False)->bool:
    target = _waitForExists(Template(r"tpl1751954806599.png", record_pos=(0.005, 1.049), resolution=(1080, 2400)),retry=2)
    result = lastResult | (target is not False)
    if target:
        touch(target)
        sleep(1)
        _close_navi(True)
    return result

def _waitForExists(v,retry:int):
    result=False
    for i in range(0, retry):
        result = exists(v)
        if result is not False:
            break
    return result

def _waitAndTouchTarget(v,retry:int=3):
    target = _waitForExists(v,retry)
    if target:
        touch(target)
    return target

def close_ad_and_nave():
    result  = _close_ad()
    result |= _close_navi()
    if result:
        close_ad_and_nave()
              
def Ready_To_Play():
    launch_app()
    sleep(50)
    is_app_start = _check_app_start()
    if is_app_start is "download": 
        _click_data_download()
        sleep(100)
        _enter_password()
        _trial_player_login()
        close_ad_and_nave()
    elif is_app_start == "ad":
        close_ad_and_nave()
    _waitAndTouchTarget(Template(r"tpl1751973367903.png", record_pos=(-0.275, 0.007), resolution=(1080, 2400)),retry=10)
    sleep(1)
    assert check_lobby_ready()
    
def check_lobby_ready():
    return _waitForExists(Template(r"tpl1752222802882.png", record_pos=(-0.354, 0.869), resolution=(1080, 2400)),retry=3)

def Click_SG_Tab():
    return _waitAndTouchTarget(Template(r"tpl1752226110055.png", record_pos=(-0.002, 0.87), resolution=(1080, 2400)))

def Click_BG_Tab():
    return _waitAndTouchTarget(Template(r"tpl1752225832370.png", record_pos=(0.352, 0.87), resolution=(1080, 2400)))

def Click_SP_Tab():
    return _waitAndTouchTarget(Template(r"tpl1752225913580.png", record_pos=(0.174, 0.869), resolution=(1080, 2400)))

def Click_Home_Tab():
    return _waitAndTouchTarget(Template(r"tpl1752222802882.png", record_pos=(-0.354, 0.869), resolution=(1080, 2400)))

def Close_MsgBox():
    _waitAndTouchTarget(Template(r"tpl1752221679199.png", record_pos=(-0.006, 0.083), resolution=(1080, 2400)),retry=2)
        
def BackToLobbyInGame():
    _waitAndTouchTarget(Template(r"tpl1752221821048.png", record_pos=(-0.253, -0.996), resolution=(1080, 2400)),retry=2)

Ready_To_Play()
