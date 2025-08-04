import time
from autoclicker import start

if __name__ == "__main__":
    start()
    print("✅ Autoclicker ready. It's activate when you stop moving th mouse for the time you have programmed in config.py .")
    print("❌ press Ctrl+C or esc to stop the program.")
    while True:
        time.sleep(1)
