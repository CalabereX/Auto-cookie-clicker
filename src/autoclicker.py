import time
import pyautogui
import mouse
import keyboard
import threading
import sys
from config import AUTOCLICK_INTERVAL, IDLE_TIME
from utils import is_cookie_clicker_open

last_mouse_move_time = time.time()
clicking = False
ignore_mouse = False

def track_mouse_activity():
    global last_mouse_move_time, ignore_mouse
    def on_move(event):
        global last_mouse_move_time, ignore_mouse
        if not ignore_mouse:
            last_mouse_move_time = time.time()
    mouse.hook(on_move)

def autoclick():
    global last_mouse_move_time, clicking, ignore_mouse
    while True:
        if is_cookie_clicker_open():
            if time.time() - last_mouse_move_time > IDLE_TIME:
                if not clicking:
                    print("Autoclicker restarted.", flush=True)
                    clicking = True
                ignore_mouse = True
                pyautogui.click()
                ignore_mouse = False
            else:
                if clicking:
                    print("Autoclicker paused.", flush=True)
                    clicking = False
        else:
            if clicking:
                print("Cookie Clicker closed, autoclicker stoped.", flush=True)
                clicking = False
        time.sleep(AUTOCLICK_INTERVAL)

def monitor_exit_key():
    global running
    keyboard.wait("esc")
    print("ESC pressed. exit autoclicker...", flush=True)
    running = False
    sys.exit()

def start():
    print("waiting that you open the cookie clicker on steam ...", flush=True)
    threading.Thread(target=autoclick, daemon=True).start()
    threading.Thread(target=track_mouse_activity, daemon=True).start()
    monitor_exit_key()  
