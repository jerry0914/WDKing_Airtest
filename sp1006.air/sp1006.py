# -*- encoding=utf8 -*-
__author__ = "Jerry_Huang"

from airtest.core.api import *
using("MainLobby.air")
import MainLobby

auto_setup(__file__)

large_icon_base=Template(r"tpl1752228461658.png")
large_icon_ready=Template(r"tpl1752228461658.png")
small_icon_base=Template(r"tpl1752228461658.png")
small_icon_ready=Template(r"tpl1752231412310.png")


def _check_large_icon():
    return MainLobby._waitForExists(large_icon_base,retry=1)

def _check_small_icon():
    return MainLobby._waitForExists(small_icon_base,retry=1)

def _swipe_to_top():
    for i in range(0,10):
        swipe((500,1500),vector=[0.01, 0.3])
        sleep(1)

def search_game_icon():
    _swipe_to_top()
    target = _check_large_icon()
    if target is False:
        for i in range(0,10):
            target = _check_small_icon()
            if target:
                break
            else:
                swipe((500,1500),vector=[0.01, -0.3])
    return target

def wait_download_and_click_small():
    target = MainLobby._waitForExists(small_icon_ready,retry=1)
    touch(small_icon_base)
    if target is False:
        # waiting for download...
        target = MainLobby._waitForExists(small_icon_base,retry=180)
    if target:
        touch(small_icon_base)
    return target

def Spin_Test():
    assert search_game_icon()
    assert wait_download_and_click_small()
    _run_spin_test_base()
    assert MainLobby.GoBackHallInGame();

    

    
def _run_spin_test_base():
    MainLobby.Close_FirstSpinMsgBox();
    assert MainLobby._waitAndTouchTarget(Template(r"tpl1752232270905.png", record_pos=(0.003, 0.933), resolution=(1080, 2400)),retry=2)
    sleep(3)
    assert MainLobby._waitAndTouchTarget(Template(r"tpl1752232270905.png", record_pos=(0.003, 0.933), resolution=(1080, 2400)),retry=15)
    
    
Spin_Test()
    
