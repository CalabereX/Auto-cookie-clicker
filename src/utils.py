import psutil
from config import COOKIE_CLICKER_PROCESS

def is_cookie_clicker_open():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == COOKIE_CLICKER_PROCESS:
            return True
    return False